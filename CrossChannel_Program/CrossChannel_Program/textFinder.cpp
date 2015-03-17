

// author: wiki908
// crc32 by notwa@github

#include "stdafx.h"
#include <cstring>

#include <utility>
#include <list>

#include "textFinder.h"

inline textFinder::ulong textFinder::crc_reflect(ulong input)
{
    ulong reflected = 0;
    long i;
    for (i = 0; i < 4 * 8; i++) {
        reflected <<= 1;
        reflected |= input & 1;
        input >>= 1;
    }
    return reflected;
}

void textFinder::crc_fill_table(ulong * table, ulong polynomial, long big)
{
    ulong lsb = (big) ? 1 << 31 : 1; /* least significant bit */
    ulong poly = (big) ? polynomial : crc_reflect(polynomial);
    long c, i;

    for (c = 0; c < CRC_TABLE_SIZE; c++, table++) {
        *table = (big) ? c << 24 : c;
        for (i = 0; i < 8; i++) {
            if (*table & lsb) {
                *table = (big) ? *table << 1 : *table >> 1;
                *table ^= poly;
            }
            else {
                *table = (big) ? *table << 1 : *table >> 1;
            }
            *table &= 0xFFFFFFFF;
        }
    }
}

inline void textFinder::crc_le_cycle(ulong * table, ulong * remainder, char c)
{
    ulong byte = table[((*remainder) ^ c) & 0xFF];
    *remainder = ((*remainder) >> 8) ^ byte;
}

inline textFinder::ulong textFinder::crc32(const char * str, const long len)
{
    ulong remainder = crc_starting;
    // Table will be created in func `public:create'
    //crc_fill_table(crc_table, crc_polynomial);

    for (long i = 0; i < len; ++i)
        crc_le_cycle(crc_table, &remainder, str[i]);
    return remainder;
}

// rightTextOut == 0 时, 返回 rightOut 的长度
// rightTextOut != 0 时, 返回 0 成功, 返回负数失败
// leftTextIn 应为字符串, leftHashIn 应为文本的 CRC32
inline long textFinder::setfile(const char * fileName, void * flag)
{
    ulong fnHash = 0;
    if (fileName != 0) fnHash = crc32(fileName, strlen(fileName));
    return setfileh(fnHash, flag);
}
inline long textFinder::find(const char * leftTextIn, const char** rightTextOut, void * flag)
{
    ulong currHash = 0;
    if (leftTextIn != 0) currHash = crc32(leftTextIn, strlen(leftTextIn));
    return findh(currHash, rightTextOut, flag);
}


long textFinder::create(const char * buff, void * flag)
{
    FDR_HEADER* phdr = (FDR_HEADER*)buff;

    // check package type
    if (phdr->packageInfo != FDR_PACK_INFO) throw FDR_E_PACK_TYPE;

    // create crc32 table
    crc_starting = phdr->CRCStarting;
    crc_polynomial = phdr->CRCPolynomial;
    crc_fill_table(crc_table, crc_polynomial);

    // record text info
    FDR_SFINFO* sfinfo = (FDR_SFINFO*)(phdr + 1);
    const char* startPolong = (const char*)(sfinfo + phdr->fileCount);

    sub_file subf;
    for (ulong i = 0; i < phdr->fileCount; ++i)
    {
        line_pair pair;
        line_list list;

        const char* read = startPolong + sfinfo[i].beginOffset;
        for (ulong j = 0; j < sfinfo[i].lineCount; ++j)
        {
            if (*read != FDR_LINE_ID) throw FDR_E_PACK_TYPE;
            ltexth_t* pleft = (ltexth_t*)(read + 1);
            pair.first = *pleft;
            read += 5; // 跳过 hash 里出现的 0
            pair.second = read;
            read += strlen(read) + 1;

            list.push_back(pair);
        }

        subf.first = sfinfo[i].nameHash;
        subf.second = list;
        _pack.push_back(subf);
    }

    // _curfile = _pack.begin(); // 初始化文件检索列表
    return FDR_SUCC;
}



long textFinder::setfileh(const unsigned long fileNameHash, void * flag)
{
    if (fileNameHash == _curfhash) return FDR_SUCC;
    for (auto s : _pack)
    {
        if (s == fileNameHash)
        {
            _curfile = s;
            return FDR_SUCC;
        }
    }
    return FDR_W_NXF;
}



long textFinder::findh(const long leftHashIn, const char** rightTextOut, void * flag)
{
    if (rightTextOut == 0) throw FDR_E_ARG_TYPE;

    auto s = _curfile.second;

    if (_pre[0].first == leftHashIn)
    {
        *rightTextOut = _pre[0].second;
        return FDR_SUCC;
    }
    else if (_pre[1].first == leftHashIn)
    {
        *rightTextOut = _pre[1].second;
        _pre[0] = _pre[1];
        ++_curline_it;
        if(_curline_it != s.end())
            _pre[1] = *_curline_it;
        return FDR_SUCC;
    }
    else
    {
        for (auto t = s.begin(); t != s.end(); ++t)
        {
            if (*t == leftHashIn)
            {
                _curline_it = t;
                *rightTextOut = t->second;
                _pre[0] = *t++;
                if (t != s.end())
                    _pre[1] = *t;
                return FDR_SUCC;
            }
        }
        return FDR_W_NXL;
    }


    return FDR_W_NXL;
}

