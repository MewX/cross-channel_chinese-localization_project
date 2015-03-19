

// author: wiki908
// crc32 by notwa@github


#pragma once

#include <utility>
#include <list>

#define FDR_PACK_INFO     (0x00432B43)   // 定义当前坑的唯一标识
#define FDR_E_PACK_TYPE   (0x50)         // 文件是其他格式或其他坑的
#define FDR_E_ARG_TYPE    (0x51)         // 参数错误

#define FDR_W_NXF         (0x30)         // 找不到文件
#define FDR_W_NXL         (0x31)         // 找不到文本行

#define FDR_LINE_ID       (0x01)         // 每行开头的标记
#define FDR_SUCC          (0x00)         // 操作成功完成

#define FDR_CRC_STARTING   (0xFFFFFFFF)  //
#define FDR_CRC_POLYNOMIAL (0x04C11DB7)  // CRC 的默认系数

extern const char* szFDR_W_NXL;

#pragma pack(1)

// Header of package
struct FDR_HEADER
{
    unsigned long packageInfo;    // 使用 FDR_PACK_INFO 区分不同的坑
    unsigned long CRCStarting;    // FDR_CRC_STARTING
    unsigned long CRCPolynomial;  // FDR_CRC_POLYNOMIAL
    unsigned long fileCount;      // 文本文件数量
};

// Information of sub-files
struct FDR_SFINFO
{
    unsigned long nameHash;       // 文本文件名的 CRC32
    unsigned long beginOffset;    // 以 FDR_SFINFO 序列之后为起点
    unsigned long lineCount;      // 文本内行数
};

//struct TEXTPAIR                 // 每行文本的结构, 开头为 FDR_LINE_ID
//{
//    CRC32: 2EBC00DF  Text:あいうえお
//    char* singlePair = "\x01\xDF\x00\xBC\x2Eあいうえお\0";
//};

#pragma pack()

class textFinder
{
    typedef const char* rtext_t;
    typedef unsigned long ltexth_t;
    typedef unsigned long fnameh_t;
    typedef std::pair<ltexth_t, rtext_t> line_pair;
    typedef std::list<line_pair> line_list;
    typedef std::pair<fnameh_t, line_list> sub_file;
    typedef std::list<sub_file> fdr_pack;

    fdr_pack _pack;
    sub_file _curfile;
    unsigned long _curfhash;

    //line_pair _pre[2];
    //line_list::iterator _next_it;

    // CRC32 Start
    typedef unsigned long ulong;
    enum { CRC_TABLE_SIZE = 0x100 };

    ulong crc_reflect(ulong input);
    void crc_fill_table(ulong *table, ulong polynomial, long big = 0);
    void crc_le_cycle(ulong *table, ulong *remainder, char c);
public:
    ulong crc32(const char* str, const long len);
private:
    ulong crc_table[CRC_TABLE_SIZE];
    ulong crc_starting;
    ulong crc_polynomial;

    // CRC32 End


public:


    long create(const char* buff, void* flag = 0);

    long setfile(const char* fileName, void* flag = 0);
    long setfileh(const unsigned long fileNameHash, void* flag = 0);

    // rightTextOut 直接给出 buff 中的内容
    long find(const char* leftTextIn, const char** rightTextOut, void* flag = 0);
    long findh(const long leftHashIn, const char** rightTextOut, void* flag = 0);

};

template<class _T>
bool operator == (const std::pair<unsigned long, _T> &lhs, const unsigned long &rhs)
{
    return (lhs.first == rhs);
}
