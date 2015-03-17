# CrossChannel_Program

这是一个**不可维护的**工具包，写于2012年末。这几次出补丁也有维护，只是懒得重写罢了。

## 功能列表（大量英文错误请无视 =。=）

>**********
- Operating Choice:<br/>
    -1. Unpack a old-ver file.<br/>
    -2. Unpack a new-ver file.<br/>
    -3. Decrypt a new-ver file.<br/>
    -4. Encrypt a new-ver file.<br/>
    -5. Pack a old-ver file.<br/>
    -6. Pack a new-ver file.<br/>
    -7. Calculate the percentage of finishment.<br/>
    -8. Plus - Process Translated file to next step.<br/>
    -9. Plus - Init Translated file to double line.<br/>
    -10. Plus - Extract all chapter titles.<br/>
    -11. Plus - Put back all chapter titles.<br/>
    -12. Plus - Generate text package
**********
- Tools Choice List:
    1. Create a folder.
    2. Get file list in a folder.
    3. Get file list and its size in a folder.
    4. Convert a specific encode to Unicode.
    5. Convert Unicode to a specific encode.
    6. Convert a specific encode to Unicode-big.
    7. Convert Unicode-big to a specific encode.
    8. Convert a specific encode to UTF-8.
    9. Convert UTF-8 to a specific encode.
    10. Convert a specific encode to UTF-16.
    11. Convert UTF-16 to a specific encode.
**********

## 工具包功能介绍

双击打开这个工具会让你选择数字然后进行操作。

### -1 选项

解包2003版的C+C文件，是\*.pd文件。

### -2 选项

解包2012年复刻版的C+C文件，是\*.arc文件。

### -3 选项

解密、提纯解解出来文件，从-2选项提取出来的是二进制脚本和二级图片压缩包，所以需要进一步解密提纯。
这部分代码当时参考了Asmodean的解包工具。

### -4 选项

脚本复原，经过汉化的脚本（\*.CCS文件）通过这个选项回到二进制脚本中。
**图片的加密不在此功能中。**

### -5 选项

打包老版的封包，与-1选项是相逆的操作。（没有完成）

### -6 选项

打包新版的封包。

这个过程首先会执行加密、压缩图片的步骤，即与-3选项处理图片封包的操作相逆。
其次会执行通用的打包工序，对于加密后的脚本和压缩后的图片都通用。

### -7 选项

计算整个工程的完成度。（未完成）

当时预想的是根据我们进度表的cvs文件来统计项目完成度的，结果还是因为懒所以没有完成。

### -8 选项

给文本续行，看下面的例子：

- 初翻

>//【翻译规范】（小提示：人物姓名可以按Ctrl+H批量替换，原文的换掉也没事）<br/>
//原文例 \>0○9999○[見里]「……それは……」<br/>
//译文例 \>1●9999●[见里]「……那个是……」<br/>
//注：不要求译文比原文短；像这样的{傅:かしず}是注音；\\n是换行符，请保留<br/>
//所有文本处理上的问题都可以发邮件到crosschannel@163.com询问或直接找QQ307740614<br/><br/>
\>0○0001○最古の記憶は。<br/>
\>1●0001●最古の記憶は。<br/><br/>
\>0○0002○日付さえおぼろげな、遠い霞のなか。<br/>
\>1●0002●日付さえおぼろげな、遠い霞のなか。<br/>

- 校对

>//【翻译规范】（小提示：人物姓名可以按Ctrl+H批量替换，原文的换掉也没事）<br/>
//原文例 \>0○9999○[見里]「……それは……」<br/>
//译文例 \>1●9999●[见里]「……那个是……」<br/>
//校对例 \>2□9999□[见里]「……那个是……」<br/>
//注：不要求译文比原文短；像这样的{傅:かしず}是注音；\\n是换行符，请保留<br/>
//所有文本处理上的问题都可以发邮件到crosschannel@163.com询问或直接找QQ307740614<br/><br/>
\>0○0001○最古の記憶は。<br/>
\>1●0001●最久远的记忆。<br/>
\>2□0001□最久远的记忆。<br/><br/>
\>0○0002○日付さえおぼろげな、遠い霞のなか。<br/>
\>1●0002●在那的连日期都变得模糊的遥远阴霾中。<br/>
\>2□0002□在那的连日期都变得模糊的遥远阴霾中。

- 润色、终校以此类推……

### -9 选项

初始化收到的文本，全部统一到2行文本，即原文和译文的文本。

这一步的作用主要是校验收到的文本是否合法，因为从翻译们手上拿到的文本格式会被大改。

比如行号错乱，因为有重复的文本，我们允许从别的文本中复制过来，而不去理会行号。
这样会导致的问题不止是行号错乱，还有多复制和少复制的问题，总之都要靠这个工序来解决。

本道工序与必须与从游戏提取出来的原始文本相结合，因为原文都被翻译巨巨门改过了~

### -10 选项

提取所有的章节标题，这部分在存档界面可以看到。

### -11 选项

封回所有的章节标题。

这部分要注意的问题和-4工序一样，文本内的绝对地址跳转需要重新计算，否则游戏必然崩溃。

### -12 选项

生成文本摘要和原文，用于汉化补丁的显示原文功能。（编码部分）

这部分的解码部分是wiki908帮忙写的。见：[wiki908/getSrcLine](https://github.com/wiki908/getSrcLine)

**********

### 1 选项

创建文件夹函数。

### 2 选项

获取文件夹中的文件列表。

### 3 选项

获取文件夹中的文件列表，含文件大小。

### 4 选项

将指定编码的文件转换成Unicode-LE。（未完成）

### 5 选项

4选项的逆操作。（未完成）

### 6 选项

将指定编码的文件转换成Unicode-BE。（未完成）

### 7 选项

6选项的逆操作。（未完成）

### 8 选项

将指定编码的文件转换成UTF-8。（未完成）

### 9 选项

8选项的逆操作。（未完成）

### 10、11 选项

未完成的搞笑选项。（未完成）

## 文件简要说明

### crc32

GitHub上的开源CRC32计算库，文件中有写版权信息。

### CxImage600

一个开源的图像库，本来准备提取成png的，结果使用KAGExpress转码工具替代了。

### libbmp

开源的bmp库，文件中有写版权信息。

### EasyUnicodeFileLE

我在2010年写得Unicode读写工具，是一个调用fstream的类。（不是继承）

使用这个类可以像操作fstream一样使用基本功能，对于初学者还是很方便的。（流当时不会写）

#### 函数列表

- void open( string FileName, ios_base::open_mode OpenMode );<br/>
  打开文件，例如：f.open(string("test.txt"), ios::in);

- void close( );<br/>
  关闭文件，例如：f.close();

- wchar_t readWchar( );<br/>
  读取一个wchar_t，例如：wchar_t wc = f.readWchar();

- wstring readLine( );<br/>
  读取一行宽字符，**以\\x000D\\x000A结尾**，例如：wstring ws = f.readLine();

- void write( wstring WC );<br/>
  写入宽字符串，例如：f.write(L"test.txt");

- void write( UINT LocalOption, string S );<br/>
  写入窄字符串，例如：f.write(936, "你好，我是MewX。");

- void writeln( wstring WC );<br/>
  当时和Java以及C#学的，在write(wstring)的基础上添加了一个换行\\x000D\\x000A。

- void writeln( UINT LocalOption, string S );<br/>
  当时和Java以及C#学的，在write(UINT, string)的基础上添加了一个换行\\x000D\\x000A。

- void SetPointer( std::streamoff off, basic_istream< char, char_traits< char \> \>::pos_type PosType );<br/>
  设置文件指针，每个宽字符算一个位置。**可以自动清除EOF的标志，更方便！**<br/>
  例如定位到相对于文件开始处第10个wchar_t字符的位置：f.SetPointer(10, ios::beg);

- bool IsOpen( ) const;<br/>
  判断文件是否已经打开，打开了则为true，否则为false。

- bool IsEOF( );<br/>
  判断文件是否已经到了文件末尾。

- string testFileHeader( );<br/>
  判断已经打开的文件是Little Endian还是Big Endian。

**致命BUG：当文件中换行符为\\x000D而不是\\x000D\\x000A时，程序会崩溃。<br/>
致命缺陷：异常会直接输出，然后中断，不能继续执行了。**

### ToolBox

工具集中的小函数工具集。

这个是我以前写ASS字幕工具的时候留下的遗产 233。同样是2010年的杰作 \_(:3」∠)\_

#### 字符相关

- bool isPunctuation( wchar_t P ) const;<br/>
  判断一个字符是否为标点符号。

#### 字符串相关

功能如名字，不赘述。

- void StringToChars( string temp, char *C ) const;
- void WstringToWchars( wstring temp, wchar_t *WC ) const;
- wstring StringToWstring( UINT LocalOption, string str ) const;
- string WstringToString( UINT LocalOption, wstring wstr ) const;
- string IntToString( long i ) const;
- int StringToInt( string str ) const;
- int StringToInt( wstring wstr ) const;
- int SubstringToInt( string str, int StartIndex, int EndIndex ) const;
- int SubstringToInt( wstring wstr, int StartIndex, int EndIndex ) const;

#### 时间计算相关

- int TimeToInt( string Time ) const;<br/>
  时间参数为"h:mm:ss.mm"，和ASS字幕的时间格式一样的。

- int TimeToInt( wstring Time ) const;<br/>
  这个时间参数为L"h:mm:ss.mm"。

- string IntToTime( int Num ) const;<br/>
  TimeToInt(string)的逆过程。

- wstring IntToTimeW( int Num ) const;<br/>
  TimeToInt(wstring)的逆过程。

#### 数字相关

- string DecToHex( unsigned long i ) const;<br/>
  十进制转十六进制，我记得有BUG。

- int Random( int range_min, int range_max ) const;<br/>
  随机函数，取一个区间内的随机数。

#### 文件相关

- void CreateFolder( string Name ) const;<br/>
  创建文件夹。

#### 图形处理相关

- int getStringWidth( wchar_t* fontName, BYTE fontCharset, int OutLine, int fontHeight, int fontSpace, wchar_t *str );<br/>
  做ASS字幕时用到的，获取字符串矩阵的像素长度。从MeteroX巨巨那里抄来的。

### textFinder

这部分是wiki908帮忙写的。见：[wiki908/getSrcLine](https://github.com/wiki908/getSrcLine)

### lzss_enc

一个LZSS压缩算法函数，但是和游戏中的规则略微不同，实际上没有使用。

### CrossChannel_Program

程序主类，2012年写得，这几次出补丁有在维护，但是还是不可维护的 =。=

实现的功能和前面“功能介绍”里面写的一样。
