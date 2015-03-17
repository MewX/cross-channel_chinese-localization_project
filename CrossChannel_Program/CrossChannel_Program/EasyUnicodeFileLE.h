#ifndef EASYUNICODEFILELE_H
#define EASYUNICODEFILELE_H
#include "ToolBox.h"

//Little - Endian
class EasyUnicodeFileLE
{
public:
	EasyUnicodeFileLE( );
	EasyUnicodeFileLE( string FileName, ios_base::open_mode OpenMode );
	~EasyUnicodeFileLE( void );

	void open( string FileName, ios_base::open_mode OpenMode );
	void close( );

	wchar_t readWchar( ); //读取一个宽字符
	wstring readLine( ); //读取一行宽字符
	void write( wstring WC ); //写入指定宽字符串
	void write( UINT LocalOption, string S ); //写入指定窄转宽字符串
	void writeln( wstring WC ); // write line
	void writeln( UINT LocalOption, string S ); // write line
	void SetPointer( std::streamoff off, basic_istream< char, char_traits< char > >::pos_type PosType );
	bool IsOpen( ) const; // 判断是否打开，打开true，未打开false
	bool IsEOF( ); //判断是否为文件末尾
	string testFileHeader( );

private:
	static const bool DEBUG_FLAG = false;
	fstream F;
	NASCToolBox Tools;

	bool IsReadMode;
	bool Initialization( ios_base::open_mode OpenMode ) const; //初始化
	void JudgeReadOrWrite( ios_base::open_mode OpenMode );

};

#endif
