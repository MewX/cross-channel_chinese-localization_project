#include "StdAfx.h"
#include "ToolBox.h"

/* * * < ERROR EXPLANATION LIST > * * */
/*
  ERROR_TB001 - Out of Array Size. ( When doing StringToChars( ) and target array's space is not enough. )
  ERROR_TB002 - Out of Array Size. ( When doing WstringToWchar( ) and target array's space is not enough. )
  ERROR_TB003 - Districted character found! ( When getting file name. )
*/

/* * * < WARNING EXPLANATION LIST > * * */
/*
  WARNING_TB001 - Converting unsafe! ( When doing StringToWstring( ) and the results is not equal to the source. )
*/


NASCToolBox::NASCToolBox( void )
{
	return;
}


NASCToolBox::~NASCToolBox( void )
{
	return;
}

bool NASCToolBox::isPunctuation( wchar_t P ) const // 计算是否为标点符号
{
	switch( P ) {
	case L'.': case L'。': case L',': case L'、': case L'！': case L'？': case L'：': case L'；':
	case L'`': case L'﹑': case L'•': case L'＂': case L'^': case L'…': case L'‘': case L'’':
	case L'“': case L'”': case L'〝': case L'〞': case L'~': case L'\\': case L'∕': case L'|':
	case L'¦': case L'‖': case L'—': case L'(': case L')': case L'﹛': case L'﹜': case L'〈':
	case L'〉': case L'﹝': case L'﹞': case L'「': case L'」': case L'‹': case L'›': case L'〖':
	case L'〗': case L'[': case L']': case L'{': case L'}': case L'《': case L'》': case L'〔':
	case L'〕': case L'『': case L'』': case L'«': case L'»': case L'【': case L'】': case L'﹐':
	case L'﹕': case L'﹔': case L'﹖': case L'＇': case L'ˊ': case L'-': case L'﹫': case L'¸':
	case L'︰': case L';': case L'¡': case L'¿': case L'´': case L'ˋ': case L'―': case L'@':
	case L'﹢': case L'+': case L'﹦': case L'=': case L'﹤': case L'<': case L'‐': case L'\'':
	case L'\"': case L'﹟': case L'#': case L'﹩': case L'$': case L'﹠': case L'&': case L'﹪':
	case L'%': case L'﹡': case L'*': case L'﹨': case L'ˆ': case L'ˇ': case L'︵': case L'︶':
	case L'︷': case L'︸': case L'︿': case L'﹀': case L'︹': case L'︺': case L'︽': case L'︾':
	case L'_': case L'﹁': case L'﹂': case L'﹃': case L'﹄': case L'︻': case L'︼': 
		return true;
	default:
		return false;
	}
}

void NASCToolBox::StringToChars( string temp, char *C ) const
{
	int L = temp.length( );
	try {
		for( int i = 0; i < L; i ++ ) C[ i ] = temp[ i ];
		C[ L ] = '\0';
	}
	catch( ... ) {
		cerr << "ERROR_TB001 - Out of Array Size." << endl;//数组越界
		system( "PAUSE" );
	}
	return;
}

void NASCToolBox::WstringToWchars( wstring temp, wchar_t *WC ) const
{
	int L = temp.length( );
	try {
		for( int i = 0; i < L; i ++ ) WC[ i ] = temp[ i ];
		WC[ L ] = L'\0';
	}
	catch( ... ) {
		cerr << "ERROR_TB002 - Out of Array Size." << endl;//数组越界
		system( "PAUSE" );
	}
	return;
}


wstring NASCToolBox::StringToWstring( UINT LocalOption, string str ) const
{
	// 932 shift_jis ANSI/OEM Japanese; Japanese (Shift-JIS)
	// 936 gb2312 ANSI/OEM Simplified Chinese (PRC, Singapore); Chinese Simplified (GB2312)
	// 949 ks_c_5601-1987 ANSI/OEM Korean (Unified Hangul Code)
	// 950 big5 ANSI/OEM Traditional Chinese (Taiwan; Hong Kong SAR, PRC); Chinese Traditional (Big5)

	/*不是空字符串*/
	char *szAnsi = new char [ str.length( ) + 1 ];
	for ( UINT i = 0; i < str.length( ); i ++ ) {
		szAnsi[ i ] = str[ i ];
	}
	szAnsi[ str.length( ) ] = '\0';
			
	//setlocale( LC_ALL, "jpn" );
	//setlocale( LC_ALL, "chs" );
	//预转换，得到所需空间的大小
	int wcsLen = ::MultiByteToWideChar( LocalOption, NULL, szAnsi, strlen(szAnsi), NULL, 0);

	//分配空间要给'\0'留个空间，MultiByteToWideChar不会给'\0'空间
	wchar_t *wszString = new wchar_t [ wcsLen + 1 ];
	::MultiByteToWideChar( LocalOption, NULL, szAnsi, strlen( szAnsi ), wszString, wcsLen) ; //最后加上'\0' 
	wszString[ wcsLen ] = '\0';
	
	wstring wstr = wszString;
	//for ( UINT i = 0; i < wcslen( wszString ); i ++ ) {
	//	wstr += wszString[ i ];
	//}

	delete [ ] szAnsi;
	delete [ ] wszString;

	return wstr;
}

string NASCToolBox::WstringToString( UINT LocalOption, wstring wstr ) const
{
	wchar_t *wszString = new wchar_t [ wstr.length( ) + 1 ];
	wcscpy_s( wszString, wstr.length( ) + 1, wstr.c_str( ) );
	wszString[ wstr.length( ) ] = '\0';
	//setlocale( LC_ALL, "jpn" );
	//setlocale( LC_ALL, "chs" );
	//预转换，得到所需空间的大小
	UINT strLen = ::WideCharToMultiByte( LocalOption, NULL, wszString, -1, NULL, 0, NULL, NULL );
	//分配空间不要给'\0'留个空间，WideCharToMultiByte会给'\0'空间
	char *szAnsi = new char [ strLen ];
	::WideCharToMultiByte( LocalOption, NULL, wszString, -1, szAnsi, strLen, NULL, NULL );
	szAnsi[ strLen - 1 ] = '\0';

	string str = szAnsi;

	delete [ ] szAnsi;
	delete [ ] wszString;

#ifdef NEEDTEST
	/*校验转码是否有损*/
	if( StringToWstring( LocalOption, str ) != wstr ) cerr << "WARNING_TB001 - Converting unsafe!" << endl;
#endif
	
	return str;
}

string NASCToolBox::IntToString( long i ) const
{
	char Str[ 11 ] = { 0 };
	sprintf_s( Str, "%ld", i );
	return Str;
}

int NASCToolBox::SubstringToInt( string str, int StartIndex, int EndIndex ) const
{
	string tmp;
	for( int i = StartIndex; i <= EndIndex; i ++ ) {
		tmp += str[ i ];
	}
	return StringToInt( tmp );
}

int NASCToolBox::SubstringToInt( wstring wstr, int StartIndex, int EndIndex ) const
{
	wstring tmp;
	for( int i = StartIndex; i <= EndIndex; i ++ ) {
		tmp += wstr[ i ];
	}
	return StringToInt( tmp );
}

string NASCToolBox::DecToHex( unsigned long i ) const
{
	const char Table[ 16 ] = { '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F' };
	if( i > 0 ) return DecToHex( i / 16 ) + Table[ i % 16];
	else return "";
}

int NASCToolBox::TimeToInt( string Time ) const
{
	// 注意，不存在负时间，所以生成的时候，有负时间的部分，都清零或者计算补间或者直接显示等替代方案
	// h : m m : s s . m m 
	// 0 1 2 3 4 5 6 7 8 9
	if( Time.length(  ) == 10 && Time[ 1 ] == ':' && Time[ 4 ] == ':' && Time[ 7 ] == '.' ) {
		return ( Time[ 0 ] - 48 ) * 360000
			+ ( ( Time[ 2 ] - 48 ) * 10 + ( Time[ 3 ] - 48 ) ) * 6000
			+ ( ( Time[ 5 ] - 48 ) * 10 + ( Time[ 6 ] - 48 ) ) * 100
			+ ( ( Time[ 8 ] - 48 ) * 10 + ( Time[ 9 ] - 48 ) );
	}
	else return 0;
}

int NASCToolBox::TimeToInt( wstring Time ) const
{
	return TimeToInt( WstringToString( 936, Time ) );
}

int NASCToolBox::StringToInt( string str ) const
{
	int L = str.length( );
	int temp = 0;
	for( int i = 0; i < L; i ++ )
	{
		temp *= 10;
		temp += str[ i ] - 48;
	}
	return temp;
}

int NASCToolBox::StringToInt( wstring wstr ) const
{
	return StringToInt( WstringToString( 936, wstr ) );
}

string NASCToolBox::IntToTime( int Num ) const
{
	// h * n : m m : s s . m m 
	// 0     1 2 3 4 5 6 7 8 9
	if( Num < 0 ) return "";
	string Time;
	Time = IntToString( Num % 100 ); Num /= 100; // get 8 & 9
	Time = ( Time.length( ) == 1 ? ".0" : "." ) + Time;
	Time = IntToString( Num % 60 ) + Time; Num /= 60; // get 5 & 6
	Time = ( Time[ 1 ] == '.' ? ":0" : ":" ) + Time;
	Time = IntToString( Num % 60 ) + Time; Num /= 60; // get 2 & 3
	Time = ( Time[ 1 ] == ':' ? ":0" : ":" ) + Time;
	Time = IntToString( Num % 60 ) + Time; // get h * n
	return Time;
}

wstring NASCToolBox::IntToTimeW( int Num ) const
{
	return StringToWstring( 936, IntToTime( Num ) );
}

int NASCToolBox::Random( int range_min, int range_max ) const
{
	/* 
		Originally, the range is [ range_min, range_max ),
		but I want to change it to [ range_min, range_max ]
		so I do "range_max ++;"
	*/
	range_max ++;
	return (int)( (double)rand( ) / ( RAND_MAX + 1 ) * ( range_max - range_min ) + range_min );
}

void NASCToolBox::CreateFolder( string Name ) const
{
	//创建一个文件夹，允许嵌套
	if( Name.length( ) > 160 ) {
		cerr << "FolderName length cannot be larger than 160!" << endl;
	}
	else {
		char tempName[ 161 ], temp[ 161 ];//temp[ ]用于依次存放嵌套文件夹
		for( UINT i = 0; i < Name.length( ); i ++ ) {
			if( Name[ 0 ] == '\\' || Name[ i ] == '/' || Name[ i ] == ':' || Name[ i ] == '?' ||
			Name[ i ] == '\"' || Name[ i ] == '<' || Name[ i ] == '?' || Name[ i ] == '|' ) {
				cerr << "#### Districted character found! ####" << endl;
				return;
			}
			tempName[ i ] = Name[ i ];
		}
		tempName[ Name.length( ) ] = '\0';
		for( UINT i = 0; i < Name.length( ); i ++ ) {
			if( tempName[ i ] == '\\' ) {
				temp[ i ] = '\0';
				if( _access( temp, 6 ) == -1 ) _mkdir( temp );//判断下文件夹是否存在，虽然这一步可以省略
			}
			temp[ i ] = tempName[ i ];
		}
		temp[ Name.length( ) ] = '\0';
		_mkdir( temp );//舍弃tempName，因为不安全，例如："123\123\"
	}
	return;
}

int NASCToolBox::getStringWidth( wchar_t* fontName, BYTE fontCharset, int OutLine, int fontHeight, int fontSpace, wchar_t *str )
//extern "C" __declspec(dllexport) bool MeasureString(int* width, int* height, WCHAR* fontName, BYTE fontCharset, int fontHeight, int fontSpace, WCHAR* str)
{
	/*
	lfCharSet:
	ANSI_CHARSET				BALTIC_CHARSET
	CHINESEBIG5_CHARSET			DEFAULT_CHARSET
	EASTEUROPE_CHARSET			GB2312_CHARSET
	GREEK_CHARSET				HANGUL_CHARSET
	MAC_CHARSET					OEM_CHARSET
	RUSSIAN_CHARSET				SHIFTJIS_CHARSET
	SYMBOL_CHARSET				TURKISH_CHARSET
	VIETNAMESE_CHARSET
	窗口的韩国语言版本：JOHAB_CHARSET
	窗口的中东语言版本：ARABIC_CHARSET	HEBREW_CHARSET
	窗口的泰国语言版本：THAI_CHARSET
	*/
	HDC dc = ::GetDC(0);
	LOGFONT logfont;
	memset(&logfont, 0, sizeof(LOGFONT));
	logfont.lfCharSet = fontCharset;
	logfont.lfHeight = fontHeight;
	logfont.lfQuality = ANTIALIASED_QUALITY;
	logfont.lfWeight = 0;
	wcscpy_s(logfont.lfFaceName, wcslen( fontName ), fontName);
	HFONT hfont = ::CreateFontIndirectW(&logfont);
	HGDIOBJ holdfont = ::SelectObject(dc, hfont);
	int width = 0;
	for (const WCHAR *p = str; *p; p++) {
		WCHAR buf[2];
		buf[0] = *p;
		buf[1] = 0;
		SIZE sz;
		GetTextExtentPoint32W(dc, buf, 1, &sz);
		width += sz.cx + fontSpace;
	}
	width -= fontSpace;
	// *height = fontHeight;
	return width;
}
