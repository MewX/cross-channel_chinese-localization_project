#ifndef CROSSCHANNELCRACK_H
#define CROSSCHANNELCRACK_H

#pragma pack( 1 )
#define ARC_VERSION 1
//#define ARC_VERSION 2
#define SECTION_SIZE 10

#if ARC_VERSION >= 2
#define FILENAME_LENGTH 13
#else
#define FILENAME_LENGTH 9
#endif

/**********************************************************************
CrossChannelCrack类的功能

必备功能：
1.UI——用户操作界面
2.提取功能（文件名，参数？）
3.封装功能（文件夹，参数？）
4.统计游戏攻略完成度（也即统计存档）

工具功能（以后独立封装成类）：
01.创建文件夹
02.获取文件夹中的文件列表
03.获取文件夹中的文件列表及各个文件的字节数
04.编码转区：从特定编码到Unicode
05.编码转区：从Unicode到特定编码，注意检查与提示字符不在字符集内。
06.编码转区：从特定编码到Unicode-bigEndian
07.编码转区：从Unicode-bigEndian到特定编码，注意检查与提示字符不在字符集内。
08.编码转区：从特定编码到UTF-8
09.编码转区：从UTF-8到特定编码，注意检查与提示字符不在字符集内。
10.编码转区：从特定编码到UTF-16
11.编码转区：从UTF-16到特定编码，注意检查与提示字符不在字符集内。
12.
**********************************************************************/

class CrossChannelCrack
{
public:
	CrossChannelCrack( string PName );
	~CrossChannelCrack( void );

	/*下面的是必备功能*/
	void RunUI( );
	void __1_Unpack( string FileName, string OutputFolder ); //老版的解包
	void __1_Unpack2( string FileName, string OutputFolder ); //复刻版的解包
	void __2_Pack( string pFileName, string SourceFolder ); //通过gFile获取封包类型，输出相应封包，源文件夹可以有注记文件
	void __3_Decrypt( string InputFolder );
	void __4_Decrypt( string OriginalUnpackFolder, string PureScriptFolder );
	void __7_CalculateSaves( string GameFolder );//计算游戏攻略完成度
	void __8_CCSProcess( string InputFolder, string OutputFolder ); // 处理CCS给下一个步骤，初翻-校对-润色-验收
	void __9_CCSInit( string InputFolder, string OutputFolder, string ReferFolder );
	void __10_GetAllChapterTitle(string InputFolder, string OutputFile);
	void __11_SetAllChapterTitle(string InputFile, string OutputFolder);
	void __12_PackText(string InputFolder, string OutputFile);

	/*下面的是工具功能*/
	void _01_CreateFolder( string Name );
	void _02_getFileList( string FolderName, string SaveTo ); /* 不支持中文文件名和文件夹 */
	void _03_getFileListAndSize( string FolderName, string SaveTo ); /* 不支持中文文件名和文件夹 */
	void _04_ConvertToUnicode( UINT LocalOption, string gFileName, string SaveTo );
	void _05_UnicodeConvertTo( UINT LocalOption, string gFileName, string SaveTo );

protected:
	wstring StringToWstring( UINT LocalOption, string str );
	string WstringToString( UINT LocalOption, wstring wstr );
	unsigned __int64 LittleEndianCharsToValue( char LEValue[ 9 ] );
	unsigned __int64 LittleEndianCharsToValue_s( UINT Length, char LEValue[ 9 ] );
	string ValueToLittleEndianChars( unsigned __int64 Value );

private:
	NASCToolBox TB;
	static const bool DebugMode = true;
	string ProjectName;

	void getFolderList( string FolderName, string SaveTo ); /* 不支持中文文件名和文件夹 */
	void Test( );

	unsigned char WSC_DecryptHelper( unsigned char s );
	unsigned char WSC_EncryptHelper( unsigned char s );

	unsigned long unwipf( unsigned char *buff,      // 输入文件正文的array
						  unsigned long  len,       // 输入文件长度
						  unsigned char *out_buff,  // 输出文件正文的array
						  unsigned long  out_len ); // 输出文件长度

	void wipf_fake( unsigned char *buff,       // 输入文件正文的array
					unsigned long  len,        // 正文的长度
					unsigned char **out_buff,  // 输出文件的正文array
					unsigned long *out_len );  // 输出文件长度

	/* Structures */
	struct ARCHDR {
		unsigned long section_count; // 区段数
	}; // 归档头部

	struct ARCSECTHDR {
		char          type[ 4 ];   // "PNG", "MOS", "OGG"
		unsigned long entry_count; // 文件数
		unsigned long toc_offset;  // 开始处的偏移地址
	}; // 归档区段细节

	struct ARCENTRY {
		char          filename[ FILENAME_LENGTH ];
		unsigned long length; // 文件长度
		unsigned long offset; // 文件开始处偏移地址
	}; // 文件细节

	struct WIPFHDR {
		unsigned char  signature[ 4 ]; // "WIPF";
		unsigned short entry_count;    // 文件数
		unsigned short depth;          // 位深度
	}; // WIPF文件头部

	struct WIPFENTRY {
		unsigned long  width;    // 宽度
		unsigned long  height;   // 高度
		unsigned long  offset_x; // x方向显示位置
		unsigned long  offset_y; // y方向显示位置
		unsigned long  unknown1; // layer?
		unsigned long  length;   // 文件长度
	}; // WIPF内含文件细节

};

#endif
