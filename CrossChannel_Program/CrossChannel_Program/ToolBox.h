#ifndef TOOLBOX_H
#define TOOLBOX_H

class NASCToolBox
{
public:
	NASCToolBox( void );
	~NASCToolBox( void );

	/*字符相关*/
	bool isPunctuation( wchar_t P ) const; // 判断是否为标点符号

	/*字符串相关*/
	void StringToChars( string temp, char *C ) const;
	void WstringToWchars( wstring temp, wchar_t *WC ) const;
	wstring StringToWstring( UINT LocalOption, string str ) const;
	string WstringToString( UINT LocalOption, wstring wstr ) const;
	string IntToString( long i ) const;
	int StringToInt( string str ) const;
	int StringToInt( wstring wstr ) const;
	int SubstringToInt( string str, int StartIndex, int EndIndex ) const;
	int SubstringToInt( wstring wstr, int StartIndex, int EndIndex ) const;

	/*时间计算相关*/
	int TimeToInt( string Time ) const;
	int TimeToInt( wstring Time ) const;
	string IntToTime( int Num ) const;
	wstring IntToTimeW( int Num ) const;

	/*数字相关*/
	string DecToHex( unsigned long i ) const;
	int Random( int range_min, int range_max ) const;

	/*文件相关*/
	void CreateFolder( string Name ) const;

	/*图形处理相关*/
	struct Martrix {
		int Width, Height; // 长宽
		char **Graph; // 二维动态数组
	};
	int getStringWidth( wchar_t* fontName, BYTE fontCharset, int OutLine, int fontHeight, int fontSpace, wchar_t *str );

	/*下面的是基于CairoGraphic的工具函数*/

private:

};

#endif
