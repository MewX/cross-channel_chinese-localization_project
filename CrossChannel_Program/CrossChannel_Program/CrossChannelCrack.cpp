#include "stdafx.h"
#include "CrossChannelCrack.h"


CrossChannelCrack::CrossChannelCrack( string PName )
{
	ProjectName = PName;
	return;
}

CrossChannelCrack::~CrossChannelCrack( void )
{
	return;
}

void CrossChannelCrack::RunUI( )
{
	Test( );//各种临时测试

	int CHOICE;
	cout << "********************************************************************************";
	cout << endl;
	UINT i = 0;
	for( ; i < ( 80 - ProjectName.length( ) ) / 2; i ++ ) cout << ' ';
	cout << ProjectName;
	i += ProjectName.length( );
	for( ; i < 80; i++ )cout << ' ';
	cout << endl;;
	cout << "********************************************************************************";
	cout << "  Operating Choice:" << endl;
	cout << "    -1. Unpack a old-ver file." << endl;
	cout << "    -2. Unpack a new-ver file." << endl;
	cout << "    -3. Decrypt a new-ver file." << endl;
	cout << "    -4. Encrypt a new-ver file." << endl;
	cout << "    -5. Pack a old-ver file." << endl;
	cout << "    -6. Pack a new-ver file." << endl;
	cout << "    -7. Calculate the percentage of finishment." << endl;
	cout << "    -8. Plus - Process Translated file to next step." << endl;
	cout << "    -9. Plus - Init Translated file to double line." << endl;
	cout << "   -10. Plus - Extract all chapter titles." << endl;
	cout << "   -11. Plus - Put back all chapter titles." << endl;
	cout << "   -12. Plus - Generate text package" << endl;
	cout << "********************************************************************************";
	cout << "  Tools Choice List:" << endl;
	cout << "     1. Create a folder." << endl;
	cout << "     2. Get file list in a folder." << endl;
	cout << "     3. Get file list and its size in a folder." << endl;
	cout << "     4. Convert a specific encode to Unicode." << endl;
	cout << "     5. Convert Unicode to a specific encode." << endl;
	cout << "     6. Convert a specific encode to Unicode-big." << endl;
	cout << "     7. Convert Unicode-big to a specific encode." << endl;
	cout << "     8. Convert a specific encode to UTF-8." << endl;
	cout << "     9. Convert UTF-8 to a specific encode." << endl;
	cout << "    10. Convert a specific encode to UTF-16." << endl;
	cout << "    11. Convert UTF-16 to a specific encode." << endl;
	cout << "********************************************************************************";
	cout << " < P.S. This program will use \"temp\" folder ! >" << endl;
	cout << " Enter your choice: ";

	try {
		cin >> CHOICE;
	}
	catch( ... ) {
		cout << "#### An error occurred! ####" << endl;
		return;
	}

	switch( CHOICE ) {
	case -1:
	{
		//解包
		string FFName, SaveTo;
		cout << "********************************************************************************";
		cout << "  Now in the old unpacking procedure..." << endl;
		cout << "  -> Enter the open file name: ";
		cin >> FFName;
		cout << "  -> Enter the target folder name: ";
		cin >> SaveTo;
		__1_Unpack( FFName, SaveTo );
		cout << "********************************************************************************";
	}
		break;
	case -2:
	{
		//解包new
		string FFName, SaveTo;
		cout << "********************************************************************************";
		cout << "  Now in the new unpacking procedure..." << endl;
		cout << "  -> Enter the open file name: ";
		cin >> FFName;
		cout << "  -> Enter the target folder name: ";
		cin >> SaveTo;
		__1_Unpack2( FFName, SaveTo );
		cout << "********************************************************************************";
	}
		break;
	case -3:
	{
		//解密
		string FFName;
		cout << "********************************************************************************";
		cout << "  Now in the decrypting procedure..." << endl;
		cout << "  -> Enter the open folder name, and all supported file will be decrypted:\n     ";
		cin >> FFName;
		__3_Decrypt( FFName );
		cout << "********************************************************************************";
	}
		break;
	case -4: 
	{
		//加密
		string Name1, Name2;
		cout << "********************************************************************************";
		cout << "  Now in the encrypting procedure..." << endl;
		cout << "  -> Enter the OriginalUnpackFolder name:\n     ";
		cin >> Name1;
		cout << "  -> Enter the PureScriptFolder name, and all supported file will be encrypted:\n     ";
		cin >> Name2;
		__4_Encrypt( Name1, Name2 );
		cout << "********************************************************************************";
	}
		break;
	case -5: goto WRONG;
	case -6:
	{
		//封包new
		string SourceFolder, FFName;
		cout << "********************************************************************************";
		cout << "  Now in the new packing procedure..." << endl;
		cout << "  -> Enter the open folder name, and all file will be packed:\n     ";
		cin >> SourceFolder;
		cout << "  -> Enter the target file name, and all file will be packed:\n     ";
		cin >> FFName;
		__2_Pack( FFName, SourceFolder );
		cout << "********************************************************************************";
	}
		break;
	case -7: goto WRONG;
	case -8:
	{
		string FFName, SaveTo;
		cout << "********************************************************************************";
		cout << "  Now in the processing procedure..." << endl;
		cout << "  -> Enter the open folder name, and all supported file will be converted:\n     ";
		cin >> FFName;
		cout << "  -> Enter the target folder name: \n     ";
		cin >> SaveTo;
		__8_CCSProcess( FFName, SaveTo );
		cout << "********************************************************************************";
	}
		break;
	case -9:
	{
		string FFName, SaveTo, PLUS;
		cout << "********************************************************************************";
		cout << "  Now in the processing procedure..." << endl;
		cout << "  -> Enter the open folder name, and all supported file will be converted:\n     ";
		cin >> FFName;
		cout << "  -> Enter the target folder name: \n     ";
		cin >> SaveTo;
		cout << "  -> Enter the target folder name: \n     ";
		cin >> PLUS;
		__9_CCSInit(FFName, SaveTo, PLUS);
		cout << "********************************************************************************";
	}
		break;
	case -10:
	{
		string FFName, SaveTo;
		cout << "********************************************************************************";
		cout << "  Now in the processing procedure..." << endl;
		cout << "  -> Enter the open folder name, containing decrypted WSC files:\n     ";
		cin >> FFName;
		cout << "  -> Enter the target file name: \n     ";
		cin >> SaveTo;
		__10_GetAllChapterTitle(FFName, SaveTo);
		cout << "********************************************************************************";
	}
		break;
	case -11:
	{
		string FFName, SaveTo;
		cout << "********************************************************************************";
		cout << "  Now in the processing procedure..." << endl;
		cout << "  -> Enter the open file name: \n     ";
		cin >> FFName;
		cout << "  -> Enter the target folder name, containing decrypted WSC files:\n     ";
		cin >> SaveTo;
		__11_SetAllChapterTitle(FFName, SaveTo);
		cout << "********************************************************************************";
	}
		break;
	case -12:
	{
		string FFName, SaveTo;
		cout << "********************************************************************************";
		cout << "  Now in the processing procedure..." << endl;
		cout << "  -> Enter the open folder name, containing 2line CCS files:\n     ";
		cin >> FFName;
		cout << "  -> Enter the target file name: \n     ";
		cin >> SaveTo;
		__12_PackText(FFName, SaveTo);
		cout << "********************************************************************************";
	}
	break;
	case  1:
	{
		//创建文件夹，可以嵌套
		string Name;
		cout << "********************************************************************************";
		cout << "  Now in the creating folder procedure..." << endl;
		cout << "  -> Enter the folder name: ";
		cin >> Name;
		_01_CreateFolder( Name );
		cout << "********************************************************************************";
	}
		break;
	case  2:
	{
		//获取文件列表
		string Name, SaveTo;
		cout << "********************************************************************************";
		cout << "  Now in the getting file list procedure..." << endl;
		cout << "  -> Enter the open folder name: ";
		cin >> Name;
		cout << "  -> Enter the saving-to file name: ";
		cin >> SaveTo;
		_02_getFileList( Name, SaveTo );
		cout << "********************************************************************************";
	}
		break;
	case  3:
	{
		//获取文件列表
		string Name, SaveTo;
		cout << "********************************************************************************";
		cout << "  Now in the getting file list & size procedure..." << endl;
		cout << "  -> Enter the open folder name: ";
		cin >> Name;
		cout << "  -> Enter the saving-to file name: ";
		cin >> SaveTo;
		_03_getFileListAndSize( Name, SaveTo );
		cout << "********************************************************************************";
	}
		break;
	case  4: goto WRONG;
	case  5: goto WRONG;
	case  6: goto WRONG;
	case  7: goto WRONG;
	case  8: goto WRONG;
	case  9: goto WRONG;
	case 10: goto WRONG;
	case 11: goto WRONG;
	default:
		WRONG:
		cout << "#### Wrong choice! ####" << endl;
		break;
	}
	return;
}

void CrossChannelCrack::__1_Unpack( string FileName, string OutputFolder ) //老版的解包
{
	_01_CreateFolder( OutputFolder );
	/*生成文件夹名称char**/
	if( OutputFolder[ OutputFolder.length( ) - 1 ] != '\\' ) OutputFolder += '\\';
	char *FolderName = new char [ OutputFolder.length( ) + 1 ];
	for( UINT i = 0; i < OutputFolder.length( ); i ++ ) FolderName[ i ] = OutputFolder[ i ];
	FolderName[ OutputFolder.length( ) ] = '\0';//string --> char*

	char *TempSave;//用于申请动态内存存放各种一次性读出来的东西

	ifstream InFile;
	ofstream OutFile;
	char FileHeader[ 9 ], tempLittleEndian[ 9 ], temp[ 2 ] = "\0";
	unsigned __int64 FileNumbers;//文件总数

	char *FName = new char [ FileName.length( ) + 1 ];//给'\0'留个空间
	for( UINT i = 0; i < FileName.length( ); i ++ ) FName[ i ] = FileName[ i ];
	FName[ FileName.length( ) ] = '\0';//string --> char*

	InFile.open( FName, ios_base::in | ios_base::binary );
	if( !InFile.is_open( ) ) {
		cout << "#### Reading-in file open failed! ####" << endl;
		return;
	}
	InFile.read( FileHeader, 8 );//读头部标识
	FileHeader[ 8 ] = '\0';
	if( !strcmp( FileHeader, "PackOnly" ) && !strcmp( FileHeader, "PackPlus" ) ) {
		cout  << "#### Reading-in file with unexpected header! ####" << endl;
		return;
	}//先保证Header里面存的是两种已知头部中的一种，之后通过判断'O'和'P'就可以区分了

	TempSave = new char [ 57 ];
	InFile.read( TempSave, 56 );//跳过56字节的空白
	delete [ ] TempSave;
	InFile.read( tempLittleEndian, 8 );
	tempLittleEndian[ 8 ] = '\0';
	FileNumbers = LittleEndianCharsToValue( tempLittleEndian );//获取文件循环变量

	struct FileArchive {
		char Name[ 129 ];
		unsigned __int64 Offset;
		unsigned __int64 Size;
	};
	FileArchive *File = new FileArchive [ (UINT)FileNumbers ];

	for( unsigned __int64 i = 0; i < FileNumbers; i ++ ) {
		InFile.read( File[ i ].Name, 128 );
		File[ i ].Name[ 128 ] = '\0';

		InFile.read( tempLittleEndian, 8 );
		tempLittleEndian[ 8 ] = '\0';
		File[ i ].Offset = LittleEndianCharsToValue( tempLittleEndian );//获取文件开始位置的偏址

		InFile.read( tempLittleEndian, 8 );
		tempLittleEndian[ 8 ] = '\0';
		File[ i ].Size = LittleEndianCharsToValue( tempLittleEndian );//获取文件大小
	}//把文件索引的内容存到内存

	for( unsigned __int64 i = 0; i < FileNumbers; i ++ ) {
		UINT a = OutputFolder.length( ) + strlen( File[ i ].Name ) + 1;
		char *ttt = new char [ a ];
		strcpy_s( ttt, a, FolderName );
		strcat_s( ttt, a, File[ i ].Name );
		cout << "     -> Extracting " << ttt << " ..." << endl;
		OutFile.open( ttt, ios_base::out | ios_base::binary | ios_base::trunc );

		InFile.seekg( File[ i ].Offset, ios_base::beg );//0x240048+
		TempSave = new char [ (UINT)File[ i ].Size + 1 ];
		InFile.read( TempSave, File[ i ].Size );
		TempSave[ File[ i ].Size ] = '\0';
		if( FileHeader[ 4 ] == 'P' ) {
			for( unsigned __int64 j = 0; j < File[ i ].Size; j ++ ) TempSave[ j ] = ~TempSave[ j ];
		}
		OutFile.write( TempSave, File[ i ].Size );
		delete [ ] TempSave;

		OutFile.close( );
		delete [ ] ttt;
	}//操作文件，注意区分是否要反转

	cout << "  >> Total: " <<FileNumbers << " file(s)." << endl;

	InFile.close( );
	delete [ ] File;
	delete [ ] FName;
	delete [ ] FolderName;
}

void CrossChannelCrack::__1_Unpack2( string FileName, string OutputFolder ) //复刻版的解包
{
	_01_CreateFolder( OutputFolder );
	/* 生成文件夹名称char* */
	if( OutputFolder[ OutputFolder.length( ) - 1 ] != '\\' ) OutputFolder += '\\';
	char *FolderName = new char [ OutputFolder.length( ) + 1 ];
	for( UINT i = 0; i < OutputFolder.length( ); i ++ ) FolderName[ i ] = OutputFolder[ i ];
	FolderName[ OutputFolder.length( ) ] = '\0';//string --> char*

	char *TempSave; // 用于申请动态内存存放各种一次性读出来的东西

	ifstream InFile;
	ofstream OutFile;
	char tempLittleEndian[ 5 ], temp[ 2 ] = "\0";
	unsigned __int64 SuffixNumbers;//后缀总数
	unsigned __int64 AllFileNumbers = 0;//文件计数

	char *FName = new char [ FileName.length( ) + 1 ];//给'\0'留个空间
	for( UINT i = 0; i < FileName.length( ); i ++ ) FName[ i ] = FileName[ i ];
	FName[ FileName.length( ) ] = '\0';//string --> char*

	InFile.open( FName, ios_base::in | ios_base::binary );
	if( !InFile.is_open( ) ) {
		cout << "#### Reading-in file open failed! ####" << endl;
		return;
	}
	
	struct SuffixArchieve {
		char Name[ 5 ];
		unsigned __int64 Number;//此种文件的数量
		unsigned __int64 Offset;
	};//定义文件扩展名相关的数据结构

	struct FileArchive {
		char Name[FILENAME_LENGTH + 1];
		unsigned __int64 Offset;
		unsigned __int64 Size;
	};//定义文件相关信息的数据结构

	InFile.read( tempLittleEndian, 4 );//LittleEndian
	tempLittleEndian[ 4 ] = '\0';//存放扩展名数
	SuffixNumbers = LittleEndianCharsToValue_s( 1, tempLittleEndian );//存入扩展名总数

	SuffixArchieve *SUFFIX = new SuffixArchieve [ (UINT)SuffixNumbers ];//生成存储扩展名信息数据结构组
	for( unsigned __int64 j = 0; j < SuffixNumbers; j ++ ) {
		/*这里存入扩展名数组*/
		InFile.read( SUFFIX[ j ].Name, 4 );
		SUFFIX[ j ].Name[ 4 ] = '\0';//存入文件扩展名

		InFile.read( tempLittleEndian, 4 );//LittleEndian
		tempLittleEndian[ 4 ] = '\0';
		SUFFIX[ j ].Number = LittleEndianCharsToValue_s( 4, tempLittleEndian );//存入文件数
		AllFileNumbers += SUFFIX[ j ].Number; // 整个包中文件的计数
		
		InFile.read( tempLittleEndian, 4 );
		tempLittleEndian[ 4 ] = '\0';
		SUFFIX[ j ].Offset = LittleEndianCharsToValue_s( 4, tempLittleEndian );//获取扩展名开始位置的偏址
	}

	for( unsigned __int64 j = 0; j < SuffixNumbers; j ++ ) {//扩展名索引循环
		InFile.seekg( SUFFIX[ j ].Offset, ios_base::beg );//定位扩展名对应的文件名的索引位置

		FileArchive *File = new FileArchive [ (UINT)SUFFIX[ j ].Number ];//生成存储文件信息数据结构组
		for( unsigned __int64 i = 0; i < SUFFIX[ j ].Number; i ++ ) {
			/*把文件索引的内容存到内存*/
			InFile.read( File[ i ].Name, FILENAME_LENGTH);
			File[ i ].Name[FILENAME_LENGTH] = '\0';

			InFile.read( tempLittleEndian, 4 );
			tempLittleEndian[ 4 ] = '\0';
			File[ i ].Size = LittleEndianCharsToValue_s( 4, tempLittleEndian );//获取文件大小
			InFile.read( tempLittleEndian, 4 );
			tempLittleEndian[ 4 ] = '\0';
			File[ i ].Offset = LittleEndianCharsToValue_s( 4, tempLittleEndian );//获取文件开始位置的偏址
		}

		for( unsigned __int64 i = 0; i < SUFFIX[ j ].Number; i ++ ) {
			/*把文件的内容存到内存*/
			UINT a = OutputFolder.length( ) + strlen( File[ i ].Name ) + 1 + 4 + 1;//数组长度（文件夹+文件名+点+扩展名+'\0'）
			char *ttt = new char [ a ];
			strcpy_s( ttt, a, FolderName );//先复制文件夹名
			strcat_s( ttt, a, File[ i ].Name );//再复制文件名
			strcat_s( ttt, a, "." );//接着复制'.'
			strcat_s( ttt, a, SUFFIX[ j ].Name );//最后复制扩展名
			cout << "     -> Extracting " << ttt << " ..." << endl;
			OutFile.open( ttt, ios_base::out | ios_base::binary | ios_base::trunc );

			InFile.seekg( File[ i ].Offset, ios_base::beg );
			TempSave = new char [ (UINT)File[ i ].Size ]; // 这个存储的是文件正文
			InFile.read( TempSave, File[ i ].Size );
			OutFile.write( TempSave, File[ i ].Size );
			OutFile.close( );

			/* WIPF unpack */
			if( !memcmp( TempSave, "WIPF", 4) ) {
				WIPFHDR *wipfhdr = (WIPFHDR *)TempSave; // WIPF文件头部wipfhdr在内存中的数据位置直接挂钩到TempSave上！！！！
				WIPFENTRY *wipfentries = (WIPFENTRY *)(wipfhdr + 1);

				AllFileNumbers += wipfhdr -> entry_count;

				unsigned char *data_buff = (unsigned char *)(wipfentries + wipfhdr->entry_count); // 正文数据的挂钩
				for( unsigned long k = 0; k < wipfhdr->entry_count; k ++ ) { // 遍历当前WIPF中的各文件
					unsigned char *pal_buff  = NULL; // 单色图数据指针
					
					if( wipfhdr -> depth == 8 ) { // 单色图，蒙版？
						pal_buff = data_buff;  // 赋值
						data_buff += 1024;       // 图片正文向后挪1KB ？？？干嘛？？？
					}

					unsigned long out_depth = wipfhdr -> depth / 8; // 位深度
					unsigned long out_stride = ( wipfentries[ k ].width * out_depth + 3 ) & ~3; // ？？
					// 注意，上面的~3的值为11111111111111111111111111111100b
					unsigned long  out_len  = wipfentries[ k ].height * out_stride; // 输出长度
					unsigned char *out_buff = new unsigned char[ out_len ];         // 目标文件内容
					unwipf( data_buff, wipfentries[ k ].length, out_buff, out_len );
					data_buff += wipfentries[ k ].length;

					
					ttt[ a - 1 - 4 - 1 ] = '_'; // 点变成下划线
					string out_filename = ttt;
					if ( wipfhdr -> entry_count > 1 ) {
						char tempChars[ 255 ];
						memset( tempChars, 0, 255 );
						sprintf_s( tempChars, 255, "+%03d+%dx%dy",
								k, wipfentries[ k ].offset_x, wipfentries[ k ].offset_y );
						out_filename += tempChars;
					}
					out_filename += ".bmp";

					if( wipfhdr -> depth == 24 ) { // 24位图
						unsigned char *temp_buff = new unsigned char[ out_len ];
						
						unsigned long color_stride = wipfentries[ k ].width;
							// RGB色间距 = 宽
						unsigned long color_len    = wipfentries[ k ].height * color_stride;
							// 高 x 宽 （因为是RGB三色的，所以一行图是一色）

						for( unsigned long y = 0; y < wipfentries[ k ].height; y ++ ) {
							// 行间循环
							struct RGB { unsigned char r, g, b; };
							RGB *rgb_line = (RGB *)( temp_buff + y * out_stride );
								// temp_buff[ y * out_stride ] 定义的是指针
							unsigned char *r_line = out_buff + y * color_stride;
							unsigned char *g_line = r_line + color_len;
							unsigned char *b_line = g_line + color_len;

							for( unsigned long x = 0; x < wipfentries[ k ].width; x ++ ) {
								// 列循环（行内循环）rgb_line[ ]是一行内的内容
								rgb_line[ x ].r = r_line[ x ];
								rgb_line[ x ].g = g_line[ x ];
								rgb_line[ x ].b = b_line[ x ];
							}
						}

						delete [ ] out_buff;
						out_buff = temp_buff;
					}

					bmp_header_t tempBMPHeader; memset( &tempBMPHeader, 0, sizeof( bmp_header_t ) );
					bmp_dib_v3_header_t tempBMPDib; memset( &tempBMPDib, 0, sizeof( bmp_dib_v3_header_t ) );
					tempBMPHeader.magic[ 0 ] = 'B'; tempBMPHeader.magic[ 1 ] = 'M';
					tempBMPDib.header_sz = 0x28;
					tempBMPDib.width = wipfentries[ k ].width;
					tempBMPDib.height = wipfentries[ k ].height;
					tempBMPDib.depth = wipfhdr -> depth;
					tempBMPDib.nplanes = 1;
					if( wipfhdr -> depth == 8 ) {
						tempBMPHeader.filesz = 0x436 + out_len;
						tempBMPHeader.offset = 0x436;
						tempBMPDib.bmp_bytesz = out_len + 0x400;
					}
					else {
						tempBMPHeader.filesz = 0x36 + out_len;
						tempBMPHeader.offset = 0x36;
						tempBMPDib.bmp_bytesz = out_len;
					}

					bmp_header_t *p_bmp_header_t = &tempBMPHeader;
					bmp_dib_v3_header_t *p_bmp_dib_v3_header_t = &tempBMPDib;
					cout << "     -> Extracting " << out_filename.c_str( ) << " ..." << endl;

					OutFile.open( out_filename.c_str( ), ios_base::out | ios_base::binary | ios_base::trunc );
					OutFile.write( (char *)p_bmp_header_t, sizeof( bmp_header_t ) );
					OutFile.write( (char *)p_bmp_dib_v3_header_t, sizeof( bmp_dib_v3_header_t ) );
					
					//需要矩阵变换 24bits & 8bits
					for( unsigned int rr = 0; rr < wipfentries[ k ].height / 2; rr ++ ) {
						for( unsigned int ee = 0; ee < wipfentries[ k ].width * out_depth; ee ++ ) {
							swap( out_buff[ ( wipfentries[ k ].height - rr - 1 ) * wipfentries[ k ].width * out_depth + ee ],
								  out_buff[ rr * wipfentries[ k ].width * out_depth + ee ] );
						}
					}

					if( wipfhdr -> depth == 24 ) {
						OutFile.write( (char *)out_buff, out_len );
					}
					else { // 8 bits
						OutFile.write( (char *)pal_buff, 1024 );
						OutFile.write( (char *)out_buff, out_len );
					}
					OutFile.close( );

					delete [ ] out_buff;
				}
			}

			delete [ ] TempSave;
			delete [ ] ttt;
		}
		delete [ ] File;
	}
	InFile.close( );

	cout << "  >> Total: " << AllFileNumbers << " file(s)." << endl;

	delete [ ] FName;
	delete [ ] FolderName;
	return;
}


void CrossChannelCrack::__2_Pack( string pFileName, string SourceFolder )
{
	// 要封文本时需要传入具体文件夹名：PureScriptFolder\WSC_ENC ！！！

	_01_CreateFolder( "temp" );//生成临时文件夹
	_03_getFileListAndSize( SourceFolder, "temp\\pack_list.txt" );
	getFolderList( SourceFolder, "temp\\pack_folder_list.txt" );
	fstream gListFile, gFile, pFile; //读取文件g(et)File与输出文件p(ut)File

	gListFile.open( "temp\\pack_folder_list.txt", ios::in );
	string tempName; // can save FolderName & FileName
	if( gListFile >> tempName && tempName != "WSC_Main" ) {
#ifdef OTOMEGA // 画布坑的Chip需要从特定的文件转码
		gListFile.seekg( ios::beg ); // 判断的时候读取了一个，现在要归零
		gListFile.clear( );
		fstream fOriListFile;
		fOriListFile.open( ( SourceFolder + "\\Chip_arc_list.txt" ).c_str( ), ios::in );
		if( !fOriListFile.good( ) ) return;
		int FileNumber; fOriListFile >> FileNumber; // Number of Fils
		string *List = new string [ FileNumber ];
		for( int i = 0; i < FileNumber; i ++ ) fOriListFile >> List[ i ]; // read all full name list
		fOriListFile.close( );

		_01_CreateFolder( ( SourceFolder + "_Fixed" ).c_str( ) );

		/* Folder Name Loop ( Read all folder names ) */
		while( gListFile >> tempName ) {
			int tempLen = tempName.length( ) - SourceFolder.length( ) - 1;
			string tempStr = tempName.substr( SourceFolder.length( ) + 1, tempLen );

			/* Calc StartPos & EndPos*/
			int i = 0, j; // i - StartPos, j - EndPos
			while( List[ i ].substr( 0, tempLen ) != tempStr ) i ++; // pass
			j = i;
			while( List[ j ].substr( 0, tempLen ) == tempStr ) j ++;
			j --;
			//cout << "i = " << i << "; j = " << j << endl;

			/* Judge MSK or MOS */
			int DefineType = 0; // MSK - 1; MOS - 2
			int SuffixStartOffset = tempLen + 1;//SourceFolder.length( )
			for( int k = i; k <= j; k ++ ) { // Full Name List Loop
				if( List[ k ].substr( SuffixStartOffset, 3 ) == "MSK" ) {
					DefineType = 1;
					break;
				}
				else if( List[ k ].substr( SuffixStartOffset, 3 ) == "MOS" ) {
					DefineType = 2;
					break;
				}
			}
			//cout << "DefineType = " << DefineType << endl;

			/* Find matched file name */
			int NumberStartOffset = SuffixStartOffset + 3 + 1; //  XXXX_MSK+001+??x??y
			_02_getFileList( tempName, "temp\\" + SourceFolder + "_" + tempStr + ".txt" );
			

			// 要排除Thumbs.db
			fstream fINListFile;
			fINListFile.open( ( tempName, "temp\\" + SourceFolder + "_" + tempStr + ".txt" ).c_str( ), ios::in );
			string tempINFileName;
			while( fINListFile >> tempINFileName ) {
				//cout << "in1" << endl;
				if( tempINFileName == "Thumbs.db" ) continue;
				fstream FIN, FOUT;
				FIN.open( ( tempName + "\\" + tempINFileName ).c_str( ), ios::in | ios::binary );
				bmp_header_t tempBMPhdr;
				bmp_dib_v3_header_t tempBMPdib;
				FIN.read( (char *)( &tempBMPhdr ), sizeof( bmp_header_t ) );
				FIN.read( (char *)( &tempBMPdib ), sizeof( bmp_dib_v3_header_t) );

				char *BMPContent;
				BMPContent = new char [ tempBMPhdr.filesz - tempBMPhdr.offset ];
				FIN.read( BMPContent, tempBMPhdr.filesz - tempBMPhdr.offset );
				FIN.close( );

				/* Find xy matched file name */
				for( int abc = i; abc < j; abc ++  ) {
					if( tempINFileName[ 1 ] == List[ abc ][ NumberStartOffset ]
					&&  tempINFileName[ 2 ] == List[ abc ][ NumberStartOffset + 1 ]
					&&  tempINFileName[ 3 ] == List[ abc ][ NumberStartOffset + 2 ] ) {
						/* write RGB and alpha file */
						int OutDepth = tempBMPdib.depth / 8;
						int AlphaSize = ( tempBMPhdr.filesz - tempBMPhdr.offset ) / OutDepth;

						/* write RGB */
						tempBMPhdr.filesz = tempBMPhdr.offset + AlphaSize * 3;
						tempBMPdib.bmp_bytesz = AlphaSize * 3;
						tempBMPdib.depth = 24;
						List[ abc ][ SuffixStartOffset ] = 'W';
						List[ abc ][ SuffixStartOffset + 1 ] = 'I';
						List[ abc ][ SuffixStartOffset + 2 ] = 'P';
						FOUT.open( ( SourceFolder + "_Fixed\\" + List[ abc ] ).c_str( ), ios::out | ios::trunc | ios::binary );
						cout << SourceFolder + "_Fixed\\" + List[ abc ] << endl;
						FOUT.write( (char *)( &tempBMPhdr ), sizeof( bmp_header_t ) );
						FOUT.write( (char *)( &tempBMPdib ), sizeof( bmp_dib_v3_header_t ) );
						for( int ccc = 0; ccc < AlphaSize * OutDepth; ) {
							FOUT.write( BMPContent + ccc, 3 );
							if( DefineType )  ccc += 4;
							else  ccc += 3;
						}
						FOUT.close( );

						/* write Alpha */
						if( DefineType == 1 ) {
							List[ abc ][ SuffixStartOffset ] = 'M';
							List[ abc ][ SuffixStartOffset + 1 ] = 'S';
							List[ abc ][ SuffixStartOffset + 2 ] = 'K';
						}
						else if( DefineType == 2 ) {
							List[ abc ][ SuffixStartOffset ] = 'M';
							List[ abc ][ SuffixStartOffset + 1 ] = 'O';
							List[ abc ][ SuffixStartOffset + 2 ] = 'S';
						}
						else break; //cerr << "???DefineType : " <<  tempName + "\\" + tempINFileName << endl;
						tempBMPhdr.offset = 0x436;
						tempBMPhdr.filesz = tempBMPhdr.offset + AlphaSize;
						tempBMPdib.bmp_bytesz = AlphaSize;
						tempBMPdib.depth = 8;
						FOUT.open( ( SourceFolder + "_Fixed\\" + List[ abc ] ).c_str( ), ios::out | ios::trunc | ios::binary );
						cout << SourceFolder + "_Fixed\\" + List[ abc ] << endl;
						FOUT.write( (char *)( &tempBMPhdr ), sizeof( bmp_header_t ) );
						FOUT.write( (char *)( &tempBMPdib ), sizeof( bmp_dib_v3_header_t ) );
						char SET[ 4 ] = { 0 };
						for( int ccc = 0; ccc <= 0xFF; ccc ++ ) {
							// Color List
							SET[ 0 ] = SET[ 1 ] = SET[ 2 ] = (char)ccc;
							FOUT.write( SET, 4 );
						}
						for( int ccc = 3; ccc < AlphaSize * OutDepth; ccc += 4 ) {
							FOUT.write( BMPContent + ccc, 1 );
						}
						FOUT.close( );

						break;
					}
				}
			}
			fINListFile.close( );
		}
		delete [ ] List;
#endif
	}
	gListFile.close( ); // 后面可以用来读取文件列表

	/* 封包时发现一个问题，文件名和扩展名必须大写 */
	string RealListFileName = "temp\\pack_list.txt"; // FileName & Size

	
	/* 处理CCS脚本，WSC_Main中的WSC文件就是备份文件了 */
	/* 注意字符集的通用性，以及一些替换 */
	if( tempName != "WSC_Main" ) {
		;
	}

	/* 图像注意上下倒置，要处理wipf，有两种文件名 */
	/* 开放一个接口，如果当前目录存在文件夹_FixedImgs，则优先在其中的同名文件夹中寻找图片 */
	int FileCount = 0;
	string *NameList; int *SizeList;
	int tempFileSize = 0;
	/* Judge to process */
	gListFile.open( "temp\\pack_list.txt", ios::in );
	while( gListFile >> tempName >> tempFileSize ) if( tempName != "Thumbs.db" ) FileCount ++;
	NameList = new string [ FileCount ];
	SizeList = new int [ FileCount ];

	//cerr << "1" << endl;
	gListFile.clear( );
	gListFile.seekg( ios::beg );
	for( int index = 0; index < FileCount; index ++ ) {
		gListFile >> NameList[ index ] >> SizeList[ index ];
		if( NameList[ index ] == "Thumbs.db" ) {
			index --;
			continue;
		}
		for( unsigned int k = 0; k < NameList[ index ].length( ); k ++ ) // Convert to CAPITAL
			if( 'a' <= NameList[ index ][ k ] && NameList[ index ][ k ] <= 'z' ) NameList[ index ][ k ] &= 0xDF;
	}
	gListFile.close( );
	
	//cerr << "2" << endl;
	int DefineType = 0; // [ 1 ]XXXX_WIP+001+123x123y.bmp; [ 2 ]XXXX_WIP.bmp; [ 0 ]XXXX.bmp
	int TypeOffset = 0;
	string MainFileNameSave;
	int StartFilePos, EndFilePos;
	for( int index = 0; index < FileCount; ) {
		DefineType = 0;
	cerr << "lst" << "(" << index << "/" << FileCount << "): "<< NameList[ index ] << endl;
		if( NameList[ index ].substr( NameList[ index ].length( ) - 3, 3 ) == "BMP" ) { // XXXX_WIP+001+123x123y.bmp
			for( unsigned int i = 0; i < NameList[ index ].length( ); i ++ ) {
				if( NameList[ index ][ i ] == '_' ) {
					while( ++ i < NameList[ index ].length( ) ) {
						if( NameList[ index ][ i ] == '+' ) {
							DefineType = 1;
							TypeOffset = i;
							break;
						}
						else if( NameList[ index ][ i ] == '.' ) {
							DefineType = 2;
							TypeOffset = i;
							break;
						}
					}
					break;
				}
				else continue;
			}
			
	//cerr << "3" << endl;
			if( DefineType ) {
	//cerr << "3.1: " << NameList[ index ] << "; TypeOffset = " << TypeOffset << ". "<< endl;
				MainFileNameSave = NameList[ index ].substr( 0, TypeOffset ); // XXXX_WIP
				StartFilePos = index;
				if( DefineType == 1 ) { // XXXX_WIP+001+123x123y.bmp
					while( ++ index < FileCount && NameList[ index ].substr( 0, TypeOffset ) == MainFileNameSave &&
						NameList[ index ].substr( NameList[ index ].length( ) - 3, 3 ) == "BMP" ) //;
					cerr << NameList[ index ] << "; " << index << endl;
					EndFilePos = index - 1;
				}
				else EndFilePos = index ++; // XXXX_WIP.bmp
	//cerr << "3.2" << endl;

				int ColorType = 0; // [ 1 ] 24bits; [ 2 ] 8bits
				if( MainFileNameSave.substr( MainFileNameSave.length( ) - 3, 3 ) == "WIP" ) ColorType = 1;
				else ColorType = 2;
				
	//cerr << "4" << endl;
				WIPFHDR WipfHDR;
				WIPFENTRY *WipfEntries = new WIPFENTRY [ EndFilePos - StartFilePos + 1 ];
				unsigned char *tempFileContent;
				unsigned char **FileContent; // 二维动态数组存储文件内容，堆内存要分别输出
				FileContent = new unsigned char * [ EndFilePos - StartFilePos + 1 ];
				WipfHDR.signature[ 0 ] = 'W'; WipfHDR.signature[ 1 ] = 'I';
				WipfHDR.signature[ 2 ] = 'P'; WipfHDR.signature[ 3 ] = 'F';
				WipfHDR.entry_count = EndFilePos - StartFilePos + 1;
				if( ColorType == 1 ) WipfHDR.depth = 24;
				else WipfHDR.depth = 8; // Judge pal bmp
				for( int i = StartFilePos; i <= EndFilePos; i ++ ) {
					cerr << "  (" << StartFilePos << "/" << i << "/" << EndFilePos << ")";
					cerr << "Loading " << NameList[ i ] << endl;
					gFile.open( ( "_FixedImgs\\" + SourceFolder + "\\" + NameList[ i ] ).c_str( ), ios::in | ios::binary );
					if( gFile.good( ) ) { // 存在修改的部分，需要使用接口
						gFile.seekg( 0, ios_base::end );
						SizeList[ i ] = (unsigned int)gFile.tellg( );
						gFile.seekg( 0, ios::beg );
					}
					else gFile.open( ( SourceFolder + "\\" + NameList[ i ] ).c_str( ), ios::in | ios::binary );

					bmp_header_t BmpHDR;
					bmp_dib_v3_header_t BmpDIB;
					gFile.read( (char *)&BmpHDR, sizeof( bmp_header_t ) );
					gFile.read( (char *)&BmpDIB, sizeof( bmp_dib_v3_header_t ) );

					SizeList[ i ] = BmpDIB.width * BmpDIB.height * WipfHDR.depth / 8;
					if( SizeList[ i ] % 4 ) SizeList[ i ] += 4 - SizeList[ i ] % 4;
					SizeList[ i ] += ( WipfHDR.depth == 8 ) ? 0x400 : 0x0;
					// SizeList[ i ] -= sizeof( bmp_header_t ) + sizeof( bmp_dib_v3_header_t ); // PS修改的文件有多余字节
					tempFileContent = new unsigned char [ SizeList[ i ] ];
					gFile.read( (char *)tempFileContent, SizeList[ i ] );
					
	//cerr << "5" << endl;
					memset( &WipfEntries[ i - StartFilePos ], 0, sizeof( WIPFENTRY ) );
					if( DefineType == 1 )
						sscanf_s( NameList[ i ].substr( TypeOffset + 5, NameList[ i ].length( ) - 4 - 5 - MainFileNameSave.length( ) ).c_str( ),
								"%dX%dY", &WipfEntries[ i - StartFilePos ].offset_x, &WipfEntries[ i - StartFilePos ].offset_y );
					WipfEntries[ i - StartFilePos ].width = BmpDIB.width;
					WipfEntries[ i - StartFilePos ].height = BmpDIB.height;
					
	//cerr << "6" << endl;
					/* 上下倒置，以及三色图分离、单色图的跳图 */
					unsigned char *in_buff;
					int in_depth = WipfHDR.depth / 8;
					if( ColorType == 1 ) in_buff = tempFileContent;
					else in_buff = tempFileContent + 1024;
					
	//cerr << "7" << endl;
	//cerr << " height  = " << WipfEntries[ i - StartFilePos ].height << endl;
	//cerr << " width   = " << WipfEntries[ i - StartFilePos ].width << endl;
					// Step 1: 矩阵变换
					for( unsigned int rr = 0; rr < WipfEntries[ i - StartFilePos ].height / 2; rr ++ ) {
						for( unsigned int ee = 0; ee < WipfEntries[ i - StartFilePos ].width * in_depth; ee ++ ) {
							swap( in_buff[ ( WipfEntries[ i - StartFilePos ].height - rr - 1 ) * WipfEntries[ i - StartFilePos ].width * in_depth + ee ],
								  in_buff[ rr * WipfEntries[ i - StartFilePos ].width * in_depth + ee ] );
						}
					}
					
	//cerr << "8" << endl;
					// Step 2: RGB 分离
					if( ColorType == 1 ) {
						unsigned long  out_stride   = ( WipfEntries[ i - StartFilePos ].width * in_depth + 3 ) & ~3;
						unsigned char *temp_buff    = new unsigned char [ SizeList[ i ] ];
						unsigned long  color_stride = WipfEntries[ i - StartFilePos ].width; // RGB色间距 = 宽
						unsigned long  color_len    = WipfEntries[ i - StartFilePos ].height * color_stride;
							// 高 x 宽 （因为是RGB三色的，所以一行图是一色）

						for( unsigned long y = 0; y < WipfEntries[ i - StartFilePos ].height; y ++ ) { // 行间循环
							struct RGB { unsigned char r, g, b; };
							RGB *rgb_line = (RGB *)&tempFileContent[ y * out_stride ]; // Line Content
							unsigned char *r_line = temp_buff + y * color_stride;
							unsigned char *g_line = r_line + color_len;
							unsigned char *b_line = g_line + color_len;

							for( unsigned long x = 0; x < WipfEntries[ i - StartFilePos ].width; x ++ ) {
								// 列循环（行内循环）rgb_line[ ]是一行内的内容
								r_line[ x ] = rgb_line[ x ].r;
								g_line[ x ] = rgb_line[ x ].g;
								b_line[ x ] = rgb_line[ x ].b;
							}
						}

						delete [ ] tempFileContent;
						tempFileContent = temp_buff;
					}
	//cerr << "9" << endl;

					if( ColorType == 1 )
						wipf_fake( tempFileContent, SizeList[ i ], &FileContent[ i - StartFilePos ], &WipfEntries[ i - StartFilePos ].length );
					else
						wipf_fake( tempFileContent + 1024, SizeList[ i ] - 1024, &FileContent[ i - StartFilePos ], &WipfEntries[ i - StartFilePos ].length );
					
					//for( int kkkk = 0; kkkk < WipfEntries[ i -StartFilePos ].length; kkkk ++ ) {
					//	if( !( kkkk % 16 ) ) fprintf_s( stderr, "\n" ); //system( "pause" ); }
					//	fprintf_s( stderr, "%2X ", (unsigned int)FileContent[ i - StartFilePos ][ kkkk ] );
					//}
					delete [ ] tempFileContent;
					gFile.close( );
				}
	//cerr << "10" << endl;
				MainFileNameSave[ MainFileNameSave.length( ) - 4 ] = '.';
				pFile.open( ( SourceFolder + "\\" + MainFileNameSave ).c_str( ), ios::out | ios::binary | ios::trunc );
				pFile.write( (char *)&WipfHDR, sizeof( WIPFHDR ) );
				pFile.write( (char *)&WipfEntries[ 0 ], sizeof( WIPFENTRY ) * WipfHDR.entry_count );
	//cerr << "11" << endl;
				for( int i = 0; i <= EndFilePos - StartFilePos; i ++ ) {
					if( ColorType == 2 ) {
						char SET[ 4 ] = { 0 };
						for( int ccc = 0; ccc <= 0xFF; ccc ++ ) {
							// Color List
							SET[ 0 ] = SET[ 1 ] = SET[ 2 ] = (char)ccc;
							pFile.write( SET, 4 );
						}
					}
					pFile.write( (char *)&FileContent[ i ][ 0 ], WipfEntries[ i ].length );
					delete [ ] FileContent[ i ];
				}
	//cerr << ".1" << endl;
				pFile.close( );
				delete [ ] FileContent;
				delete [ ] WipfEntries;
				//system( "pause" );
			}
		}
		else index ++;
	}
	delete [ ] NameList;
	delete [ ] SizeList;
	//cerr << "12" << endl;
	_03_getFileListAndSize( SourceFolder, "temp\\pack_list_old.txt" );
	gListFile.open( "temp\\pack_list_old.txt", ios::in );
	pFile.open( "temp\\pack_list.txt", ios::out | ios::trunc );
	while( gListFile >> tempName >> tempFileSize ) {
		for( unsigned int k = 0; k < tempName.length( ); k ++ ) // Convert to CAPITAL
			if( 'a' <= tempName[ k ] && tempName[ k ] <= 'z' ) tempName[ k ] = tempName[ k ] & 0xDF;
		if( tempName.substr( tempName.length( ) - 3, 3 ) == "BMP" ) continue;
		else pFile << tempName << "\t" << tempFileSize << endl;
	}
	pFile.close( );
	gListFile.close( );
	/* 至此，文件列表RealListFileName准备完毕，直接装入arc封包 */


	/* 封包 */
	//cerr << "13" << endl;
	tempFileSize = 0;
	ARCHDR HDR; HDR.section_count = 0;
	ARCSECTHDR Section[ SECTION_SIZE ]; memset( Section, 0, sizeof( ARCSECTHDR ) * SECTION_SIZE );
	ARCENTRY *Entries[ SECTION_SIZE ];
	gListFile.clear( );
	gListFile.open( RealListFileName.c_str( ), ios::in );
	while( gListFile >> tempName >> tempFileSize ) {
		for( unsigned int k = 0; k < tempName.length( ); k ++ ) // Convert to CAPITAL
			if( 'a' <= tempName[ k ] && tempName[ k ] <= 'z' ) tempName[ k ] = tempName[ k ] & 0xDF;
		unsigned int i = 0;
		for( ; i < HDR.section_count; i ++ ) {
			if( Section[ i ].type[ 0 ] == tempName[ tempName.length( ) - 3 ] &&
				Section[ i ].type[ 1 ] == tempName[ tempName.length( ) - 2 ] &&
				Section[ i ].type[ 2 ] == tempName[ tempName.length( ) - 1 ] ) break;
		}
		if( i == HDR.section_count ) { // Not Exist, Should be added
			HDR.section_count ++;
			Section[ i ].type[ 0 ] = tempName[ tempName.length( ) - 3 ];
			Section[ i ].type[ 1 ] = tempName[ tempName.length( ) - 2 ];
			Section[ i ].type[ 2 ] = tempName[ tempName.length( ) - 1 ];
		}
		Section[ i ].entry_count ++;
		// 后面要统一设置偏移地址
	}
	//cerr << "14" << endl;

	// Allocate Heap Memory
	for( unsigned int i = 0; i < HDR.section_count; i ++ ) {
		//cerr << "entry_count : " << Section[ i ].entry_count << endl;
		Entries[ i ] = new ARCENTRY [ Section[ i ].entry_count ];
		memset( Entries[ i ], 0, sizeof( ARCENTRY ) * Section[ i ].entry_count );
	}
	
	gListFile.clear( );
	gListFile.seekg( 0, ios::beg );
	int FileIndex[ SECTION_SIZE ] = { 0 };
	while( gListFile >> tempName >> tempFileSize ) {
		for( unsigned int k = 0; k < tempName.length( ); k ++ ) // Convert to CAPITAL
			if( 'a' <= tempName[ k ] && tempName[ k ] <= 'z' ) tempName[ k ] = tempName[ k ] & 0xDF;
		/* 先让offset存储同类型文件的累积长度，后面统一处理偏移地址 */
		unsigned int i = 0;
		for( ; i < HDR.section_count; i ++ ) {
			if( Section[ i ].type[ 0 ] == tempName[ tempName.length( ) - 3 ] &&
				Section[ i ].type[ 1 ] == tempName[ tempName.length( ) - 2 ] &&
				Section[ i ].type[ 2 ] == tempName[ tempName.length( ) - 1 ] ) break;
		}
	//cerr << "15" << endl;
		
		//cerr << "000:" << tempName << "; "<< tempName.length( ) << endl;
		tempName = tempName.substr( 0, tempName.length( ) - 4 );
		//cerr << "1st:" << tempName << "; "<< tempName.length( ) << endl;
		if( tempName.length( ) > 4 && tempName.substr( tempName.length( ) - 4, 4 ) == "_PNG" ) tempName = tempName.substr( 0, tempName.length( ) - 4 );
		//cerr << "2nd:" << tempName << endl;
		strcpy_s( Entries[ i ][ FileIndex[ i ] ].filename, tempName.length( ) + 1, tempName.c_str( ) );//
		Entries[ i ][ FileIndex[ i ] ].length = tempFileSize;
		//cerr << Entries[ i ][ FileIndex[ i ] ].filename << "\t" << Entries[ i ][ FileIndex[ i ] ].length << endl;
		if( FileIndex[ i ] )
			Entries[ i ][ FileIndex[ i ] ].offset
				= Entries[ i ][ FileIndex[ i ] - 1 ].offset + Entries[ i ][ FileIndex[ i ] - 1 ].length;
		//cerr << "Entried[ " << i << " ][ ? ].offset = " << Entries[ i ][ FileIndex[ i ] ].offset << endl;
		FileIndex[ i ] ++;
	}

	/* Set Offset */
	int tempOffset = 0;
	char *tempFileContent;
	tempOffset += sizeof( ARCHDR ); // 扩展名计数
	tempOffset += sizeof( ARCSECTHDR ) * HDR.section_count; // 扩展名表段
	for( unsigned int i = 0; i < HDR.section_count; i ++ ) {
		Section[ i ].toc_offset = tempOffset;
		tempOffset += sizeof( ARCENTRY ) * Section[ i ].entry_count; // 文件名表段
	}
	for( unsigned int i = 0; i < HDR.section_count; i ++ ) {
		unsigned int j = 0;
		for( ; j < Section[ i ].entry_count; j ++ ) Entries[ i ][ j ].offset += tempOffset;
		tempOffset = Entries[ i ][ j - 1 ].offset + Entries[ i ][ j - 1 ].length;
	}

	pFile.open( pFileName.c_str( ), ios::out | ios::binary | ios::trunc );
	pFile.write( (char *)( &HDR ), sizeof( ARCHDR ) );
	pFile.write( (char *)( &Section[ 0 ] ), sizeof( ARCSECTHDR ) * HDR.section_count );
	for( unsigned int i = 0; i < HDR.section_count; i ++ )
		pFile.write( (char *)( &Entries[ i ][ 0 ] ), sizeof( ARCENTRY ) * Section[ i ].entry_count );
	for( unsigned int i = 0; i < HDR.section_count; i ++ ) {
		gListFile.clear( );
		gListFile.seekg( 0, ios::beg );
		while( gListFile >> tempName >> tempFileSize ) {
			for( unsigned int k = 0; k < tempName.length( ); k ++ ) // Convert to CAPITAL
				if( 'a' <= tempName[ k ] && tempName[ k ] <= 'z' ) tempName[ k ] = tempName[ k ] & 0xDF;
			if( Section[ i ].type[ 0 ] == tempName[ tempName.length( ) - 3 ] &&
				Section[ i ].type[ 1 ] == tempName[ tempName.length( ) - 2 ] &&
				Section[ i ].type[ 2 ] == tempName[ tempName.length( ) - 1 ] ) {
					cerr << "  Packinig " << tempName << endl;
					tempFileContent = new char [ tempFileSize ];
					gFile.open( ( SourceFolder + "\\" + tempName ).c_str( ), ios::in | ios::binary );
					gFile.read( tempFileContent, tempFileSize );
					gFile.close( );
					pFile.write( tempFileContent, tempFileSize );
					delete [ ] tempFileContent;
			}
			
		}
	}
	
	pFile.close( );
	for( unsigned int i = 0; i < HDR.section_count; i ++ ) delete [ ] Entries[ i ];
	gListFile.close( );
	return;
}

// 集合各种特殊情况用于判断是否达到文本结尾
// 不检测边界
bool checkTail(char *FileContents, int i, int Size) {

	return (

		// 5个%N为内容的特殊情况，其结尾为：  00 41 0B 
		(FileContents[i] == (char)0x00 && FileContents[i + 1] == (char)0x41 && FileContents[i + 2] == (char)0x0B)

		// %N结尾 25 4E 00 （存在多个%N的情况，这里只允许两个%N）
		|| (FileContents[i] == (char)0x00 && FileContents[i - 1] == (char)0x4E && FileContents[i - 2] == (char)0x25 && FileContents[i - 5] != (char)0x4E)

		// %WE结尾 25 57 45 00 (要除去后面还有%的情况)
		|| (FileContents[i] == (char)0x00 && FileContents[i - 1] == (char)0x45 && FileContents[i - 2] == (char)0x57 && FileContents[i - 3] == (char)0x25)

		// %FE结尾 25 46 45 00
		|| (FileContents[i] == (char)0x00 && FileContents[i - 1] == (char)0x45 && FileContents[i - 2] == (char)0x46 && FileContents[i - 3] == (char)0x25)

		//%O 结尾 25 4F 00
		|| (FileContents[i] == (char)0x00 && FileContents[i - 1] == (char)0x4F && FileContents[i - 2] == (char)0x25)


		// %W结尾 25 57 00 B6
		|| (FileContents[i] == (char)0x00 && FileContents[i + 1] == (char)0xB6 && FileContents[i - 1] == (char)0x57 && FileContents[i - 2] == (char)0x25)

		// %AE结尾 25 41 45 00
		|| (FileContents[i] == (char)0x00 && FileContents[i - 1] == (char)0x45 && FileContents[i - 2] == (char)0x41 && FileContents[i - 3] == (char)0x25)


		// %T500  25 54 35 30 30
		|| (FileContents[i - 1] == (char)0x30 && FileContents[i - 2] == (char)0x30 && FileContents[i - 3] == (char)0x35 && FileContents[i - 4] == (char)0x54 && FileContents[i - 5] == (char)0x25)

		// '  00 0F 27 00 
		|| (FileContents[i] == (char)0x00 && FileContents[i - 1] == (char)0x27 && FileContents[i - 2] == (char)0x0F && FileContents[i - 3] == (char)0x00)

		// 」 81 76 00 49
		|| (FileContents[i] == (char)0x00 && FileContents[i + 1] == (char)0x49 && FileContents[i - 1] == (char)0x76 && FileContents[i - 2] == (char)0x81)

		// 特殊情况 、 00 41 66 00
		|| (FileContents[i] == (char)0x00 && FileContents[i + 1] == (char)0x41 && FileContents[i + 2] == (char)0x66 && FileContents[i + 3] == (char)0x00)

		// 特殊情况  8   01 38 00 00
		|| (FileContents[i - 2] == (char)0x01 && FileContents[i - 1] == (char)0x38 && FileContents[i] == (char)0x00 && FileContents[i + 1] == (char)0x00)

		// 特殊情况 <!> 00 0F 00 00
		|| (FileContents[i - 2] == (char)0x00 && FileContents[i - 1] == (char)0x0F && FileContents[i] == (char)0x00 && FileContents[i + 1] == (char)0x00)

		// 特殊情况 ) 00 0F 01 29
		|| (FileContents[i - 4] == (char)0x00 && FileContents[i - 3] == (char)0x0F && FileContents[i - 2] == (char)0x01 && FileContents[i - 1] == (char)0x29)

		// 00 41 3E 00
		|| (FileContents[i] == (char)0x00 && FileContents[i + 1] == (char)0x41 && FileContents[i + 2] == (char)0x3E && FileContents[i + 3] == (char)0x00)


		// 00 0B 09 00
		|| (FileContents[i] == (char)0x00 && FileContents[i + 1] == (char)0x0B && FileContents[i + 2] == (char)0x09 && FileContents[i + 3] == (char)0x00)

		// 特殊情况(在英文句子Artificial Intelligence Operating system后直接出现，并且文本之后还有两个Artificial Intelligence Operating system) 
		// 00 0B 00 00 03
		|| (FileContents[i] == (char)0x00 && FileContents[i + 1] == (char)0x0B && FileContents[i + 2] == (char)0x00 && FileContents[i + 3] == (char)0x00 && FileContents[i + 4] == (char)0x03)


		// 00 0B 1D 00

		|| (FileContents[i] == (char)0x00 && FileContents[i + 1] == (char)0x0B && FileContents[i + 2] == (char)0x1D && FileContents[i + 3] == (char)0x00)

		// 00 41 36 00 AA28文本的ENTER PASSWORD	

		|| (FileContents[i] == (char)0x00 && FileContents[i + 1] == (char)0x41 && FileContents[i + 2] == (char)0x36 && FileContents[i + 3] == (char)0x00)

		// 00 E5 00 41

		|| (FileContents[i] == (char)0x00 && FileContents[i + 1] == (char)0xE5 && FileContents[i + 2] == (char)0x00 && FileContents[i + 3] == (char)0x41)

		);
}
// 用于将utf16编码的字符串转化为wstring
std::wstring UTF16StringLineToWstring(std::string utf16line)
{
	std::wstring result = L"";
	for (int i = 0; i < utf16line.length() - 1; i += 2)
	{
		unsigned char c1 = utf16line[i];
		unsigned char c2 = utf16line[i + 1];
		unsigned short wc;
		if (c2 == 0)
		{
			wc = c1;
		}
		else
		{
			wc = c2;
			wc = wc << 8;
			wc += c1;
		}
		result += wc;
	}
	return result;
}

void CrossChannelCrack::__3_Decrypt( string InputFolder )
{
	_01_CreateFolder( "temp" );//生成临时文件夹

	string FFFF;
	for( unsigned i = 0; i < InputFolder.length( ); i ++ ) {
		if( InputFolder[ i ] == '\\' ) FFFF += '_';
		else FFFF += InputFolder[ i ];
	}
	FFFF = "temp\\" + FFFF + "_FileList.txt";
	_02_getFileList( InputFolder, FFFF );//存到temp文件夹里

	char *TempSave;//临时存储字符串
	TempSave = new char [ FFFF.length( ) + 1 ];//临时存储文件路径
	for( UINT i = 0; i < FFFF.length( ); i ++ ) TempSave[ i ] = FFFF[ i ];
	TempSave[ FFFF.length( ) ] = '\0';

	char *FileNameHeader = new char [ InputFolder.length( ) + 2 ];//文件夹名称+'\\'
	for( UINT i = 0; i < InputFolder.length( ); i ++ ) FileNameHeader[ i ] = InputFolder[ i ];
	FileNameHeader[ InputFolder.length( ) ] = '\0';//先让这个字符串有个结尾
	if( InputFolder[ InputFolder.length( ) - 1 ] != '\\' ) {
		FileNameHeader[ InputFolder.length( ) ] = '\\';
		FileNameHeader[ InputFolder.length( ) + 1 ] = '\0';
	}//加个反斜杠

	fstream FileList, InFile/*先把源文件存到内存，再针对内存中的数据进行操作，提取有效信息到文件*/;
	FileList.open( TempSave, ios_base::in );//打开之后TempSave就可以删掉了

	delete [ ] TempSave;
	TempSave = new char [ 20 ];//临时存储读出来的文件名
	while( !FileList.eof( ) ) {
		FileList.getline( TempSave, 19, '\n' );//从“文件列表文件”文件中读取文件名
		if( TempSave[ 0 ] == '\0' ) continue;
		char *PathTemp = new char [ 100 ];
		strcpy_s( PathTemp, strlen( FileNameHeader ) + 1, FileNameHeader );
		strcat_s( PathTemp, strlen( PathTemp ) + strlen( TempSave ) + 1, TempSave );
		cout << "PathTemp = " << PathTemp << "\t";
		InFile.open( PathTemp, ios_base::in | ios_base::binary );
		InFile.seekg( 0, ios_base::end );//指针移到文件末
		UINT Size = (UINT)InFile.tellg( );
		char *FileContents = new char [ Size ];//生成和文件一样大的数组
		InFile.seekg( 0, ios_base::beg );
		InFile.read( FileContents, Size );//一次性把文件读完
		InFile.close( );//源文件生命周期结束

		char *RealSaveToFolder = new char [ 255 ];//FolderName \\ SuffixName_Main & SuffixName_Junk

		/*分文件扩展名讨论问题*/
		if( TempSave[ strlen( TempSave ) - 3 ] == 'W' && TempSave[ strlen( TempSave ) - 2 ] == 'S' && TempSave[ strlen( TempSave ) - 1 ] == 'C' ) {
			char *TempTargetFile = new char [ Size ];//往内存中临时存储要输出的文件内容
			int TTFlength = 0;

			//这里可放一些懒得计算的原文标记 ror 2
			const char TextHeader    =   (char)WSC_DecryptHelper( 0x3C );                                    //文本开头
			const char TextTail[4] = { (char)WSC_DecryptHelper( 0x94 ), (char)WSC_DecryptHelper( 0x2D ),
									   (char)WSC_DecryptHelper( 0x94 ), (char)WSC_DecryptHelper( 0x41 ) }; //文本结尾
			const char TextTail2[4] = { TextTail[0], TextTail[1], TextTail[2], (char)WSC_DecryptHelper(0x3D) }; //文本结尾2 (used in I/O only)
			const char TextTail3[4] = { TextTail[0], TextTail[1], TextTail[2], (char)WSC_DecryptHelper(0xC1) }; //文本结尾3 (used in I/O only)
			const char TextTail4[4] = { TextTail[0], TextTail[1], TextTail[2], (char)WSC_DecryptHelper(0x39) }; //文本结尾4 (used in I/O only)1
			const char PinyinHeader  =   (char)WSC_DecryptHelper( 0xED );                                    //注释开头   {
			const char PinyinMiddle  =   (char)WSC_DecryptHelper( 0xE8 );                                    //注释分隔符 :
			const char PinyinTail    =   (char)WSC_DecryptHelper( 0xF5 );                                    //注释结尾   }

			for( UINT i = 0; i < Size; i ++ ) {
				FileContents[ i ] = (char)WSC_DecryptHelper( FileContents[ i ] );
			}

			char Flag = NULL;//标记，文本中却不是注释中a，注释中左部分b；注释中右部分c；有姓名的Text用d；不是文本NULL
			for( UINT i = 0; i < Size; i ++ ) {
				if( i == Size - 1 ) cout << "Flag = " << Flag << "\t";
				if( i == Size - 1 && Flag != NULL ) {
					while( TTFlength - 2 >= 0 && ( TempTargetFile[ TTFlength - 1 ] != '\x0A' || TempTargetFile[ TTFlength - 2 ] != '\x0D' ) ) {
						//到上一个换行符之间的全部都删掉
						TTFlength --;
					}
					if( TTFlength - 2 < 0 ) TTFlength = 0;
					Flag = NULL;
					cout << "in break!" << endl;
					break;
				}

				if( i < Size - 1 && FileContents[ i ] == '\0' && FileContents[ i + 1 ] == TextHeader ) {//下一个进入文本中
					if( Flag != NULL  ) {
						//这个是特殊情况
						while( TTFlength - 2 >= 0 && ( TempTargetFile[ TTFlength - 1 ] != '\x0A' || TempTargetFile[ TTFlength - 2 ] != '\x0D' ) ) {
							//到上一个换行符之间的全部都删掉
							TTFlength --;
						}
						if( TTFlength - 2 < 0 ) TTFlength = 0;
					}

					i ++;
					if( FileContents[ i + 1 ] == TextHeader ) {
						Flag = 'd';
						i ++;
						TempTargetFile[ TTFlength ] = '[';
						TTFlength ++;
					}
					else {
						Flag = 'a';
					}
					continue;
				}
				else if (
					(Flag != NULL && i + 3 < Size && FileContents[i] == TextTail[0] && FileContents[i + 1] == TextTail[1])
					|| (Flag != NULL && checkTail(FileContents, i, Size))
					) {
					//文本尾部，注意保存及换行
					Flag = NULL;
					i += 1;//可以跳过去了
					TempTargetFile[ TTFlength ] = '\x0D';
					TempTargetFile[ TTFlength + 1 ] = '\x0A';//换行
					TTFlength += 2;
					TempTargetFile[ TTFlength ] = '\0';
					continue;
				}
#ifdef CROSSCHANNEL
				// Cross Channel
				else if( i > 1 && i + 10 < Size && FileContents[ i ] == 0x01 && FileContents[ i - 1 ] == 0x00
					&& (   FileContents[ i + 1 ] == 0x52 && FileContents[ i + 8 ] == 0x01
						|| FileContents[ i + 1 ] == 0x53 && FileContents[ i + 8 ] == 0x02
						|| FileContents[ i + 1 ] == 0x54 && FileContents[ i + 8 ] == 0x03
						|| FileContents[ i + 1 ] == 0x55 && FileContents[ i + 8 ] == 0x04 )
					&& FileContents[ i + 2 ] == 0x03 && FileContents[ i + 3 ] == 0x03 && FileContents[ i + 4 ] == 0x01
					&& FileContents[ i + 5 ] == 0x02 && FileContents[ i + 6 ] == 0x00 && FileContents[ i + 7 ] == 0x00
					&& FileContents[ i + 9 ] == 0x00 ) {
					//选项结尾
#endif
#ifdef OTOMEGA
				// Otomega
				else if( i > 1 && i + 10 < Size && FileContents[ i ] == 0x01 && FileContents[ i - 1 ] == 0x00
					&& (   FileContents[ i + 1 ] == 0x52 
						|| FileContents[ i + 1 ] == 0x53 
						|| FileContents[ i + 1 ] == 0x54 
						|| FileContents[ i + 1 ] == 0x55 )
					&& FileContents[ i + 2 ] == 0x03 && FileContents[ i + 3 ] == 0x07 && FileContents[ i + 4 ] == 0x4B
					&& FileContents[ i + 5 ] == 0x59 && FileContents[ i + 6 ] == 0x30 && FileContents[ i + 7 ] == 0x31
					&& FileContents[ i + 8 ] == 0x5F && FileContents[ i + 9 ] == 0x30 ) {
					//选项结尾
#endif
#ifdef IOREVISION
				// I/O revision II
				else if (i > 2 && i + 7 < Size && FileContents[i - 1] == 0x00 && 
					
					(
						(FileContents[i] == 0x00 && FileContents[i + 1] == 0x01) ||
						(FileContents[i] == 0x01 && FileContents[i + 1] == 0x7B) ||
						(FileContents[i] == 0x01 && FileContents[i + 1] == 0x7C) ||
						(FileContents[i] == 0x01 && FileContents[i + 1] == 0x7D) ||
						(FileContents[i] == 0x01 && FileContents[i + 1] == 0x7E) 
					)

					&& FileContents[i + 2] == 0x00 && FileContents[i + 3] == 0x03
					&& FileContents[i + 4] == 0x01 && FileContents[i + 5] == 0x07 && FileContents[i + 6] == 0x00) 
				
				{
					//选项结尾
#endif

					
					while( TTFlength - 2 >= 0 && ( TempTargetFile[ TTFlength - 1 ] != '\x0A' || TempTargetFile[ TTFlength - 2 ] != '\x0D' ) ) {
						//到上一个换行符之间的全部都删掉
						TTFlength --;
					}
					if( TTFlength - 2 < 0 ) TTFlength = 0;
					Flag = NULL;

					cout << "CHOICE" << endl;
					/*
					0001 5203 0301 0200 0001 00
					0001 5303 0301 0200 0002 00
					0001 5403 0301 0200 0003 00
					0001 5503 0301 0200 0004 00
					*/
					int offset = 2; // 向前偏移到正文

					//找选项开头（目测0x0001~0x01之间有猫腻，但是直接过掉）
					while((unsigned char)FileContents[ i - offset ] > (unsigned char)0x04) offset ++; // 返回到前面找到正文
					TempTargetFile[ TTFlength ] = '#';
					if( FileContents[ i + 1 ] == 0x52 ) TempTargetFile[ TTFlength ] = '>';
					TempTargetFile[ TTFlength + 1 ] = '#';
					TempTargetFile[ TTFlength + 2 ] = '#';
					TempTargetFile[ TTFlength + 3 ] = '#';
					TTFlength += 4; // 选项的标记是####
					for( offset --; offset > 1; offset -- ) {
						TempTargetFile[ TTFlength ] = FileContents[ i - offset ];
						TTFlength ++;
					}
					TempTargetFile[ TTFlength ] = '\x0D';
					TempTargetFile[ TTFlength + 1 ] = '\x0A';//换行
					TTFlength += 2;
					TempTargetFile[ TTFlength ] = '\0';

					i += 9; // 循环变量会+1
					continue;
				}
				/*else if( Flag == 'a' && FileContents[ i ] == PinyinHeader ) {//下一个进入拼音左
					//cout << "  Flag = b" << endl;
					Flag = 'b';
					continue;
				}
				else if( Flag == 'b' && FileContents[ i ] == PinyinMiddle ) {//下一个进入拼音右，注意替换
					//cout << "  Flag = c" << endl;
					Flag = 'c';
					continue;
				}
				else if( Flag == 'c' && FileContents[ i ] == PinyinTail ) {//拼音尾部注意转换标记
					//cout << "  Flag = PinyinTail" << endl;
					Flag = 'a';
					continue;
				}*/
				else { 
					//cout << "  Flag = OTHERS" << endl; 
				}//不是需要的标记字符

				bool NameFlag = false;
				if( Flag == 'a' || Flag == 'b' || Flag == 'd' ) {
					if( Flag == 'd' && FileContents[ i ] == '\x00' && !NameFlag ) {
						TempTargetFile[ TTFlength ] = ']';//英文保留符
						NameFlag = true;
					}
					else TempTargetFile[ TTFlength ] = FileContents[ i ];
					TTFlength ++;
				}
				else if( Flag == 'c' ) {
					//不需要处理
				}
			}
			
			/* 这里生成扩展名为wsc的解密后的脚本 */
			strcpy_s( RealSaveToFolder, strlen( FileNameHeader ) + 1, FileNameHeader );//Essential
			strcat_s( RealSaveToFolder, strlen( RealSaveToFolder ) + 9 + 1, "WSC_Main\\" );//Essential
			_01_CreateFolder( RealSaveToFolder );//Essential
			strcat_s( RealSaveToFolder, strlen( RealSaveToFolder ) + strlen( TempSave ) + 1, TempSave );//Essential
			InFile.open( RealSaveToFolder, ios_base::trunc | ios_base::out | ios_base::binary );//Essential
			InFile.write( FileContents, Size );//一次性全部存到文件中
			InFile.close( );
				
			cout << "TTF = " << TTFlength << endl;
			if( TTFlength > 2 && Flag == NULL ) {
				/* 这里生成扩展名为txt的纯文本 */
				RealSaveToFolder[ strlen( RealSaveToFolder ) - 1 ] = 'T';
				RealSaveToFolder[ strlen( RealSaveToFolder ) - 2 ] = 'X';
				RealSaveToFolder[ strlen( RealSaveToFolder ) - 3 ] = 'T';
				InFile.open( RealSaveToFolder, ios_base::trunc | ios_base::out | ios_base::binary );//Essential
				InFile.write( TempTargetFile, TTFlength );//一次性全部存到文件中
				InFile.close( );
				
				EasyUnicodeFileLE ULE;
				ifstream New_Txt_Stream;//存放译文的临时变量
#ifdef CROSSCHANNEL
				RealSaveToFolder[ strlen( RealSaveToFolder ) - 3 ] = 'C';
				RealSaveToFolder[ strlen( RealSaveToFolder ) - 2 ] = 'C';
				RealSaveToFolder[ strlen( RealSaveToFolder ) - 1 ] = 'S'; // CCS
#endif
#ifdef OTOMEGA
				RealSaveToFolder[ strlen( RealSaveToFolder ) - 3 ] = 'O';
				RealSaveToFolder[ strlen( RealSaveToFolder ) - 2 ] = 'M';
				RealSaveToFolder[ strlen( RealSaveToFolder ) - 1 ] = 'S'; // OMS
#endif
#ifdef IOREVISION
				RealSaveToFolder[strlen(RealSaveToFolder) - 3] = 'I';
				RealSaveToFolder[strlen(RealSaveToFolder) - 2] = 'O';
				RealSaveToFolder[strlen(RealSaveToFolder) - 1] = 'S'; // IOS

				
				// 译文文件InputFolder应当于InputFolder下
				string temp = FileNameHeader + string(TempSave);
				temp.at(temp.length() - 3) = 'T';
				temp[temp.length() - 2] = 'X';
				temp[temp.length() - 1] = 'T';
				// 打开译文文件
				New_Txt_Stream.open(temp, ios::in | ios::binary);

#endif
				ULE.open( RealSaveToFolder, ios_base::trunc | ios_base::out );
				wstring TempTargetFileULE;

				TempTargetFileULE += L"//【翻译规范】（小提示：人物姓名可以按Ctrl+H批量替换，原文的换掉也没事）\n";
				TempTargetFileULE += L"//原文例 >0○9999○[見里]「……それは……」\n";
				TempTargetFileULE += L"//译文例 >1●9999●[见里]「……那个是……」\n";
				TempTargetFileULE += L"//注：不要求译文比原文短；像这样的{傅:かしず}是注音；\\n是换行符，请保留\n";
				TempTargetFileULE += L"//所有文本处理上的问题都可以发邮件到imewx@qq.com询问或直接找QQ307740614\n";

				int ULEStcCount = 1;
				int ULEChoiceCount = 0;
				bool StartNewLn = true, Redo = false;
				string tmp; // 临时存储字符串，按行计算
				wstring Sign1, Sign2;
				for( int k = 0; k < TTFlength; k ++ ) {
					/* 二次处理，处理TempTargetFile到TempTargetFileULE里面 */
					if( TempTargetFile[ k ] == '>' && TempTargetFile[ k + 1 ] == '#' && TempTargetFile[ k + 2 ] == '#' && TempTargetFile[ k + 3 ] == '#' ){
						ULEChoiceCount = 1;
						k += 4;
						if( ULEChoiceCount == 1 ) TempTargetFileULE += L"\n"; // 多补一个换行
					}
					else if( TempTargetFile[ k ] == '#' && TempTargetFile[ k + 1 ] == '#' && TempTargetFile[ k + 2 ] == '#' && TempTargetFile[ k + 3 ] == '#' ){
						ULEChoiceCount ++;
						k += 4;
						if( ULEChoiceCount == 1 ) TempTargetFileULE += L"\n"; // 多补一个换行
					}
					else {
						ULEChoiceCount = 0;
						TempTargetFileULE += L"\n"; // 多补一个换行

						Sign1 = L">0○";
						wstring num = TB.StringToWstring( 936, TB.IntToString( ULEStcCount ) );
						for( int p = 1; p + num.length( ) <= 4; p ++ ) {
							Sign1 += L"0";
						} // 保留4位数字
						Sign1 += num + L"○"; // >0○9999○
						Sign2 = Sign1;
						Sign2[ 1 ] = L'1';
						Sign2[ 2 ] = L'●';
						Sign2[ 7 ] = L'●'; // >1●9999●
						ULEStcCount ++;
					}
					tmp.clear( ); // tmp清空

					while( k + 1 < TTFlength && !( TempTargetFile[ k ] == 0x0D && TempTargetFile[ k + 1 ] == 0x0A ) ) {
						tmp += TempTargetFile[ k ];
						k ++;
					}
					tmp += "\n";
					k += 1; // 叠加器会+1

					wstring res = TB.StringToWstring( 932, tmp ); // Shift-JIS
					//if (res.length() > 1) {
						//res[res.length() - 1] = L'\n';
						if (ULEChoiceCount) TempTargetFileULE += L">0○选项" + TB.StringToWstring(936, TB.IntToString(ULEChoiceCount)) + L"○";
						else TempTargetFileULE += Sign1;
						TempTargetFileULE += res;
						if (ULEChoiceCount) TempTargetFileULE += L">1●选项" + TB.StringToWstring(936, TB.IntToString(ULEChoiceCount)) + L"●";
						else TempTargetFileULE += Sign2;

						// 添加第二行
						//为空则添加原文
						// New_Txt_Stream.eof()||(UINT)New_Txt_Stream.tellg()==0
						if (New_Txt_Stream.eof()) {
							TempTargetFileULE += res;
						}
						else {
							//添加译文
							const int clength = 3;
							char cc[clength] = { '\0' };/*当前读入的字符*/
							char pc[clength] = { '\0' };/*当前的前驱的字符*/
							string line = "";

							while (New_Txt_Stream.read(cc, clength - 1))
							{	/*一次读入两个字节*/
								line += cc[0];
								line += cc[1];
								if ((pc[0] == '\x0d') && (pc[1] == '\x00')
									&& (cc[0] == '\x0a') && (cc[1] == '\x00'))
								{
									/*换行符标志*/
									/*Unicode文件的字节流转换为宽字符*/
									std::wstring wstr = UTF16StringLineToWstring(line);

									//这里除去\r\n中的\r,只留下\n，否则EasyUnicodeFileLE的write会让文本结尾多了一个/r
									wchar_t temp_char = wstr.at(wstr.length() - 1);
									wstr.pop_back();
									wstr.pop_back();
									wstr += temp_char;

									TempTargetFileULE += wstr;

									break;
								}
								else if (cc[0] == '\xff' && cc[1] == '\xfe') {
									// 出去new_txt中多余的FF FE 魔数(大端UTF16的BOM)
									line.pop_back();
									line.pop_back();
								}
								strcpy(pc, cc);/*保存当前两个字符的前驱字符*/
								memset(cc, sizeof(char), clength);
							}
						}
					//}
				}
				ULE.write( TempTargetFileULE );
				ULE.close( );
				New_Txt_Stream.close();
			}
			else {
				cout << "  -> None Text." << endl;
			}//没有文本的
		}//WSC文件
		else { }//判断不是已知文件扩展名
		delete [ ] FileContents;
		delete [ ] RealSaveToFolder;
	}
	FileList.close( );
	delete [ ] TempSave;

	return;
}


struct SRCCHAR {
	unsigned char srcChar;
	unsigned int srcPos;
};

void CrossChannelCrack::__4_Encrypt( string OriginalUnpackFolder, string PureScriptFolder )
{
	// Usage:
	// -4 Rio_arc 20150305_cv

	// 文件夹名后面别加'\\'
	if( OriginalUnpackFolder[ OriginalUnpackFolder.length( ) - 1 ] == '\\' ) OriginalUnpackFolder.pop_back( );
	if( PureScriptFolder[ PureScriptFolder.length( ) - 1 ] == '\\' ) PureScriptFolder.pop_back( );
	
	/** < 函数说明 >
	 *  OriginalUnpackFolder 是解包的文件夹，里面有一个子文件夹是WSC_Main
	 *  PureScriptFolder     是完成的文本所在的文件夹（格式：.CCS/.OMS/...）
	 *  操作： 将PureScriptFolder里面的文本提纯，保存为.TXT放到PureScriptFolder\TXT里面，和WSC_Main里面的TXT文件格式一样。
	 *         然后对于TXT文件，往解密过的WSC文件里面塞，保存为.WSC放到PureScriptFolder\WSC_DEC。
	 *         对于装填过的WSC文件，进行移位运算放到PureScriptFolder\WSC_ENC里面。
	 *         封包操作交给Pack函数，第一个参数是PureScriptFolder\WSC_ENC。
	 */

	_01_CreateFolder( "temp" ); //生成临时文件夹
	_03_getFileListAndSize( OriginalUnpackFolder, "temp\\WSC_List.txt" ); // 从这里获取WSC文件列表
	_03_getFileListAndSize( PureScriptFolder, "temp\\Scripts_List.txt" ); // 从这里获取CCS/OMS/...文件列表
	_01_CreateFolder( PureScriptFolder + "\\WSC_DEC" ); //生成临时文件夹
	_01_CreateFolder( PureScriptFolder + "\\WSC_ENC" ); //生成临时文件夹
	_01_CreateFolder( PureScriptFolder + "\\TXT" ); //生成临时文件夹

	fstream gListFile, gFile, pFile;
	string tempFileName;
	unsigned int tempLen;

	/* 先把LogFile打开 */
	EasyUnicodeFileLE pLogFile;
	pLogFile.open( "temp\\Rio_LogFile.txt", ios::out | ios::trunc );


	/* 这里进行Unicode转GB2312-TXT的操作，要生成Log文件来记录转码丢失的字符 */
	cout << "  [ Unicode -> GB2312-TXT ]" << endl;
	gListFile.open( "temp\\Scripts_List.txt", ios::in );
	while( gListFile >> tempFileName >> tempLen ) {
		cout << "  TXT Process: " << tempFileName << endl;
		FILE *gUNCFile;
		if( _wfopen_s( &gUNCFile, TB.StringToWstring( 936, PureScriptFolder + "\\" + tempFileName ).c_str( ), L"rb,ccs=UNICODE" ) != 0 ) {
			cerr << "####File open ERROR! (" << tempFileName << ")\n";
			return;
		}
		fseek( gUNCFile, 2, SEEK_SET ); // 到正文开头

		tempLen -= 2; // 去掉开头的0xFEFF
		tempLen >>= 1; // 除以二方便一点
		wchar_t *tempFileContent;
		tempFileContent = new wchar_t [ tempLen ];
		fread_s( tempFileContent, 2 * tempLen, 2, tempLen, gUNCFile );
		fclose( gUNCFile );

		// 一行一行分解，一行一行处理
		wstring tempSaveW; // 这个临时储存转换出来的字符，检查是否有损
		string tempSaveFileContent = ""; // GB2312就保存到这
		unsigned int i = 0, LineCount = 0;
		wchar_t MaxSeries = 0;
		while( i < tempLen ) {
			LineCount ++; // 行数加一

			/* 分离一行 */
			wstring temp = L"";
			while( i < tempLen ) {
				if( ( i <= tempLen - 2 && tempFileContent[ i ] == L'\x000D'
						&& tempFileContent[ i + 1 ] == L'\x000A' && ( i = i + 2 ) )
					|| ( ( i <= tempLen - 1 && tempFileContent[ i ] == L'\x000A' && ( i = i + 1 ) ) ) ) break;
				else temp += tempFileContent[ i ++ ];
			}
			if( temp.length( ) < 8 ) continue; // 一行里面字符数太少了
			if( temp[ 6 ] == L'>' ) MaxSeries = temp[ 7 ]; // 一系列的最大标号
			if( temp[ 0 ] == L'/' && temp[ 1 ] == L'/' ) continue; // 注释行

			/* 分析行的内容 */
			// >2□0001□[瑞希]「为什么，会是粉红色的呢。。。」
			unsigned int StartPos = 0; // 用来存储正文第一个字符的地址，因为选项和普通句子的始点不同
			if( temp[ 0 ] == L'>' ) { // 是一个正文
				if( temp[ 1 ] == MaxSeries ) {
					if( temp[ 3 ] == L'选' ) {
						// 第一个选项开头是 >###，其余的是####
						if( temp[ 5 ] == L'1' ) tempSaveFileContent += ">###";
						else tempSaveFileContent += "####";
						StartPos = 7;
					} // 选项
					else StartPos = 8;

					tempSaveW = TB.StringToWstring( 936, TB.WstringToString( 936, temp.substr( StartPos, temp.length( ) - StartPos ) ) );
					for( unsigned int k = StartPos; k < temp.length( ); k ++ ) {
						/* 这里可以做一些字符替换 */
						switch( temp[ k ] ) {
						case L'\x30FB': temp[ k ] = tempSaveW[ k - StartPos ] = L'\x00B7'; break; // 实心点 ver1
						case L'\xFF65': temp[ k ] = tempSaveW[ k - StartPos ] = L'\x00B7'; break; // 实心点 ver2
						case L'\x266A': temp[ k ] = tempSaveW[ k - StartPos ] = L'\x2606'; break; // 音乐符号换成星星
						case L'\x3000': temp[ k ] = tempSaveW[ k - StartPos ] = L'\x0020'; break; // 大空格换成小空格
						case L'\x00E4': temp[ k ] = tempSaveW[ k - StartPos ] = L'\x0061'; break; // 重音a换成a
						case L'\x2020': temp[ k ] = tempSaveW[ k - StartPos ] = L'\x002B'; break; // 十字架换成+号
						default: break;
						}
					} // 字符替换
					if( tempSaveW != temp.substr( StartPos, temp.length( ) - StartPos ) ) {
						for( unsigned int k = StartPos; k < temp.length( ); k ++ ) {
							/* 这里就是输出错误日志的地方 */
							if( tempSaveW[ k - StartPos ] != temp[ k ] ) {
								pLogFile.writeln( L"[ " + TB.StringToWstring( 936, tempFileName ) + L" ] [ line: "
										+ TB.StringToWstring( 936, TB.IntToString( LineCount ) )
										+ L" ] “" + temp[ k ] + L"” in “" + temp + L"”" );
							}
						}
					} // 说明转换出来有损

					char tempContent[ 2048 ];
					string str = TB.WstringToString( 936, tempSaveW );
					memset( tempContent, '\0', sizeof( tempContent ) );
					//strcpy( tempContent, str.c_str( ) );

					// 半角转全角
					unsigned int j = 0, index = 0;
					for( ; j < str.length( ) && tempContent[ index + j ] == '\0' && tempContent[ index + j + 1 ] == '\0' ; j ++ ) {
						// at the begin
						pLogFile.writeln(L"[ " + TB.StringToWstring(936, tempFileName) + L" ] [ line: "
							+ TB.StringToWstring(936, TB.IntToString(LineCount))
							+ L" ] [ position: " + TB.StringToWstring(936, TB.IntToString(j)) + L" ] is the for begin pos");

						// index + j < delta - 1
						if( str[ j ] == ' ' ) { // Space is special
							tempContent[ index + j ] = 0xA1;
							tempContent[ ( ++ index ) + j ] = 0xA1;
						}
#ifdef IOREVISION 						
						// 用于跳转到tip的转义字符，其后面的数字编号不能被转码
						else if (str[j] == '%') {
							//跳过非文本的值
							while (str[j] < 0x80) {
								tempContent[index + j] = str[j];
								j++;
								if (j >= str.length()) {
									pLogFile.writeln(L"[ " + TB.StringToWstring(936, tempFileName) + L" ] [ line: "
										+ TB.StringToWstring(936, TB.IntToString(LineCount))
										+ L" ] endline in “" + TB.StringToWstring(936, str) + L"”");
									break;
								}
							}
						}
						// 全角字符的高位
						//else if(str[j] == 0)
						//{
						//	tempContent[index + j] = str[j+1]-128;
						//	j++;
						//}
#endif
						// Exceptions
						else if( j + 1 < str.length( ) && str[ j ] == '\\' && str[ j + 1 ] == 'n' ) {
							tempContent[ index + j ] = str[ j ];
							j ++;
							if( j >= str.length( ) ) {
								pLogFile.writeln( L"[ " + TB.StringToWstring( 936, tempFileName ) + L" ] [ line: "
										+ TB.StringToWstring( 936, TB.IntToString( LineCount ) )
										+ L" ] endline in “" + TB.StringToWstring( 936, str ) + L"”" );
								break;
							}
							tempContent[ index + j ] = str[ j ];
						}
						else if( str[ j ] == '{' ) {
							// problem
							// {送辞:そうじ}｛相似:そうじ}

							pLogFile.writeln(L"[ " + TB.StringToWstring(936, tempFileName) + L" ] [ line: "
								+ TB.StringToWstring(936, TB.IntToString(LineCount))
								+ L" ] [ position: " + TB.StringToWstring(936, TB.IntToString(j)) + L" ] found \'{\'");
							tempContent[ index + j ] = str[ j ];
							j ++;
							while( j < str.length( ) && str[ j ] != '}' ) {
								if( str[ j ] == ' ' ) { // Space is special
									tempContent[ index + j ] = 0xA1;
									tempContent[ ( ++ index ) + j ] = 0xA1;
								}
								else if (str[j] == ':') {
									tempContent[index + j] = str[j];
								}
								else if( str[ j ] != ':' && '!' <= str[ j ] && str[ j ] <= '~' ) {
									tempContent[ index + j ] = 0xA3;
									tempContent[ ( ++ index ) + j ] = str[ j ] + 0x80;
								}
								else {
									tempContent[ index + j ] = str[ j ];
									j ++;
									if( j >= str.length( ) ) {
										pLogFile.writeln( L"[ " + TB.StringToWstring( 936, tempFileName ) + L" ] [ line: "
												+ TB.StringToWstring( 936, TB.IntToString( LineCount ) )
												+ L" ] endline in “" + TB.StringToWstring( 936, str ) + L"”" );
										break;
									}
									tempContent[ index + j ] = str[ j ];
								}
								j ++;
							}
							pLogFile.writeln(L"[ " + TB.StringToWstring(936, tempFileName) + L" ] [ line: "
								+ TB.StringToWstring(936, TB.IntToString(LineCount))
								+ L" ] [ position: " + TB.StringToWstring(936, TB.IntToString(j)) + L" ] found \'}\'");
							tempContent[ index + j ] = str[ j ];
						}
						else if( j == 0 && str[ j ] == '[' ) {
							tempContent[ index + j ] = str[ j ];
							j ++;
							while( j < str.length( ) && str[ j ] != ']' ) {
								if( str[ j ] == ' ' ) { // Space is special
									tempContent[ index + j ] = 0xA1;
									tempContent[ ( ++ index ) + j ] = 0xA1;
								}
								else if( str[ j ] != ':' && '!' <= str[ j ] && str[ j ] <= '~' ) {
									tempContent[ index + j ] = 0xA3;
									tempContent[ ( ++ index ) + j ] = str[ j ] + 0x80;
								}
								else {
									tempContent[ index + j ] = str[ j ];
									j ++;
									if( j >= str.length( ) ) {
										pLogFile.writeln( L"[ " + TB.StringToWstring( 936, tempFileName ) + L" ] [ line: "
												+ TB.StringToWstring( 936, TB.IntToString( LineCount ) )
												+ L" ] endline in “" + TB.StringToWstring( 936, str ) + L"”" );
										break;
									}
									tempContent[ index + j ] = str[ j ];
								}
								j ++;
							}
							tempContent[ index + j ] = str[ j ];
						}
						else if (str[j] == '%' && j + 2 < str.length() && '0' <= str[j + 1] && str[j + 1] <= 'z' && '0' <= str[j+2] && str[j+2] <= 'z') {
							// 另一种转义字符
							tempContent[index + j] = str[j];
							j++;
							tempContent[index + j] = str[j];
							j++;
							tempContent[index + j] = str[j];
						}

						else if( '!' <= str[ j ] && str[ j ] <= '~' ) {
							tempContent[ index + j ] = 0xA3;
							tempContent[ ( ++ index ) + j ] = str[ j ] + 0x80;
						}
						else {
							tempContent[ index + j ] = str[ j ];
							j ++;
							if( j >= str.length( ) ) {
								pLogFile.writeln( L"[ " + TB.StringToWstring( 936, tempFileName ) + L" ] [ line: "
										+ TB.StringToWstring( 936, TB.IntToString( LineCount ) )
										+ L" ] endline in “" + TB.StringToWstring( 936, str ) + L"”" );
								break;
							}
							tempContent[ index + j ] = str[ j ];
						}
					}
						
					tempSaveFileContent += string( tempContent ) + "\n";
				} // 可以输出的行
				else continue;
			}
		}
		cout << "MaxSeries = " << (char)MaxSeries << endl;

		/* 输出TXT文件 */
		tempFileName[ tempFileName.length( ) - 1 ] = 'T';
		tempFileName[ tempFileName.length( ) - 2 ] = 'X';
		tempFileName[ tempFileName.length( ) - 3 ] = 'T';
		pFile.open( ( PureScriptFolder + "\\TXT\\" + tempFileName ).c_str( ), ios::out | ios::trunc );
		pFile.write( tempSaveFileContent.c_str( ), tempSaveFileContent.length( ) );
		pFile.close( );

		delete [ ] tempFileContent;
	}
	gListFile.close( );
	pLogFile.close( );


	/* 这里进行GB2312-TXT嵌入GB2312-WSC_DEC&ENC的操作 */
	cout << "  [ GB2312-TXT -> GB2312-WSC_DEC&ENC ]" << endl;
	gListFile.open( "temp\\WSC_List.txt", ios::in );
	while( gListFile >> tempFileName >> tempLen ) {
		cout << "  WSC Process: " << tempFileName << endl;
		/* 读原来的WSC文件 */
		bool hasText = true;
		gFile.open( ( OriginalUnpackFolder + "\\WSC_Main\\" + tempFileName ).c_str( ), ios:: in | ios::binary );
		if( !gFile.good( ) ) { // 没有文本的WSC文件
			gFile.open( ( OriginalUnpackFolder + "\\" + tempFileName ).c_str( ), ios:: in | ios::binary );
			hasText = false;
		}
		char *tempWSCFileContent = new char [ tempLen ];
		gFile.read( tempWSCFileContent, tempLen );
		gFile.close( ); // 这里WSC文件全部读完了，后面用gFile读TXT文件
		cout << "01" << endl;

		/* 读刚刚提纯的TXT文件 */
		tempFileName[ tempFileName.length( ) - 1 ] = 'T';
		tempFileName[ tempFileName.length( ) - 2 ] = 'X';
		tempFileName[ tempFileName.length( ) - 3 ] = 'T'; // 临时改一下文件名
		gFile.open( ( PureScriptFolder + "\\TXT\\" + tempFileName ).c_str( ), ios::in ); // 一行一行读getline
		tempFileName[ tempFileName.length( ) - 3 ] = 'W';
		tempFileName[ tempFileName.length( ) - 2 ] = 'S';
		tempFileName[ tempFileName.length( ) - 1 ] = 'C'; // 打开TXT后再改回来，因为保存文件是WSC
		if( !gFile.good( ) ) { // 文件没打开，说明没有这个中文版，那就直接copy
			// DEC Write
			pFile.open( ( PureScriptFolder + "\\WSC_DEC\\" + tempFileName ).c_str( ), ios::out | ios::trunc | ios::binary );
			pFile.write( tempWSCFileContent, tempLen );
			pFile.close( );

			// ENC Write
			pFile.open( ( PureScriptFolder + "\\WSC_ENC\\" + tempFileName ).c_str( ), ios::out | ios::trunc | ios::binary );
			if( hasText ) for( unsigned int j = 0; j < tempLen; j ++ ) tempWSCFileContent[ j ] = (char)WSC_EncryptHelper( tempWSCFileContent[ j ] );
			pFile.write( tempWSCFileContent, tempLen );
			pFile.close( );

			delete [ ] tempWSCFileContent;
			continue;
		}
		cout << "02";

		// add new struct to fix offset
		SRCCHAR *srcchar = new SRCCHAR[tempLen];
		for (int i = 0; i < tempLen; i++) {
			srcchar[i].srcChar = tempWSCFileContent[i];
			srcchar[i].srcPos = i;
		}

		/* 这里可放一些懒得计算的原文标记 ( ror x, 2 ) */
		const char TextHeader    =   (char)WSC_DecryptHelper( 0x3C );                                    //文本开头

		SRCCHAR *WSCFileContent_CHS = new SRCCHAR[tempLen + 4096]; // 多分配4K字节
		unsigned int OutLen = 0; // 输出的字节
		/** < 思路 >
		 *  判断文本：找0x00000F，下一个是不是0x0F：是则有人名，直到0x00才是正文；否则无人名，直接正文。正文到%K%P止。
		 *  判断选项：找选项尾，然后向前找到0x00为止
		 **/
		unsigned int i = 0, cLine = 0;
		char Sign = 0x00; // 在while里面有解释
		while( i < tempLen ) {
			while( i < tempLen ) { // 找可替换的部分
				if( i + 2 < tempLen && tempWSCFileContent[ i ] == 0x00 && tempWSCFileContent[ i + 1 ] == TextHeader) 
				{ Sign = 'a'; break; } // 初步判断是文本
#ifdef CROSSCHANNEL // Cross Channel
				else if( i > 1 && i + 10 < tempLen && tempWSCFileContent[ i ] == 0x01 && tempWSCFileContent[ i - 1 ] == 0x00
					&& (   tempWSCFileContent[ i + 1 ] == 0x52 && tempWSCFileContent[ i + 8 ] == 0x01
						|| tempWSCFileContent[ i + 1 ] == 0x53 && tempWSCFileContent[ i + 8 ] == 0x02
						|| tempWSCFileContent[ i + 1 ] == 0x54 && tempWSCFileContent[ i + 8 ] == 0x03
						|| tempWSCFileContent[ i + 1 ] == 0x55 && tempWSCFileContent[ i + 8 ] == 0x04 )
					&& tempWSCFileContent[ i + 2 ] == 0x03 && tempWSCFileContent[ i + 3 ] == 0x03 && tempWSCFileContent[ i + 4 ] == 0x01
					&& tempWSCFileContent[ i + 5 ] == 0x02 && tempWSCFileContent[ i + 6 ] == 0x00 && tempWSCFileContent[ i + 7 ] == 0x00
					&& tempWSCFileContent[ i + 9 ] == 0x00 ) { //选项结尾
#endif
#ifdef OTOMEGA // Otomega
				else if( i > 1 && i + 10 < tempLen && tempWSCFileContent[ i ] == 0x01 && tempWSCFileContent[ i - 1 ] == 0x00
					&& (   tempWSCFileContent[ i + 1 ] == 0x52 || tempWSCFileContent[ i + 1 ] == 0x53 
						|| tempWSCFileContent[ i + 1 ] == 0x54 || tempWSCFileContent[ i + 1 ] == 0x55 )
					&& tempWSCFileContent[ i + 2 ] == 0x03 && tempWSCFileContent[ i + 3 ] == 0x07 && tempWSCFileContent[ i + 4 ] == 0x4B
					&& tempWSCFileContent[ i + 5 ] == 0x59 && tempWSCFileContent[ i + 6 ] == 0x30 && tempWSCFileContent[ i + 7 ] == 0x31
					&& tempWSCFileContent[ i + 8 ] == 0x5F && tempWSCFileContent[ i + 9 ] == 0x30 ) { //选项结尾
#endif
#ifdef IOREVISION // I/O revision II
					// TODO: double check this
				//else if (i > 2 && i + 7 < tempLen && tempWSCFileContent[i] == 0x00 && tempWSCFileContent[i - 1] == 0x00
				//	&& tempWSCFileContent[i + 1] == 0x01 && tempWSCFileContent[i + 2] == 0x00 && tempWSCFileContent[i + 3] == 0x03
				//	&& tempWSCFileContent[i + 4] == 0x01 && tempWSCFileContent[i + 5] == 0x07 && tempWSCFileContent[i + 6] == 0x00) 
				else if (i > 2 && i + 7 < tempLen && tempWSCFileContent[i - 1] == 0x00 &&

					(
					(tempWSCFileContent[i] == 0x00 && tempWSCFileContent[i + 1] == 0x01) ||
						(tempWSCFileContent[i] == 0x01 && tempWSCFileContent[i + 1] == 0x7B) ||
						(tempWSCFileContent[i] == 0x01 && tempWSCFileContent[i + 1] == 0x7C) ||
						(tempWSCFileContent[i] == 0x01 && tempWSCFileContent[i + 1] == 0x7D) ||
						(tempWSCFileContent[i] == 0x01 && tempWSCFileContent[i + 1] == 0x7E)
						)

					&& tempWSCFileContent[i + 2] == 0x00 && tempWSCFileContent[i + 3] == 0x03
					&& tempWSCFileContent[i + 4] == 0x01 && tempWSCFileContent[i + 5] == 0x07 && tempWSCFileContent[i + 6] == 0x00)

				{
					//选项结尾
#endif
					Sign = 'b'; break; // 判断是选项的结尾
				}

				WSCFileContent_CHS[OutLen++] = srcchar[i++]; // 拷贝
			} // 判断标记的while
			if( i >= tempLen ) { cout << "break - " << tempFileName << "; i = " << i << endl; break;} // 这样跳出循环没有输出
			cout << "(" << Sign << ")";

			cLine ++;
			switch( Sign ) {
			case 'a': // 粗略判断是文本开头
				for (int k = 0; k < 2; k++) WSCFileContent_CHS[OutLen++] = srcchar[i++]; // 拷贝判断过的3（2）个字节

				// 这里为空行的特殊情况 16进制为00 0F 00 00 
				// 以及 '  00 0F 27 00 的情况
				// 特殊情况 <!> 00 0F 00 00	
				// 特殊情况 ) 00 0F 01 29
				// 直接使用原文即可
				if ((tempWSCFileContent[i] == 0x00 && tempWSCFileContent[i + 1] == 0x00)
					|| (tempWSCFileContent[i] == 0x27 && tempWSCFileContent[i + 1] == 0x00)
					|| (tempWSCFileContent[i] == 0x00 && tempWSCFileContent[i + 1] == 0x00)
					|| (tempWSCFileContent[i] == 0x01 && tempWSCFileContent[i + 1] == 0x29)
					// 多个%N
					|| (tempWSCFileContent[i] == 0x25 && tempWSCFileContent[i + 1] == 0x4E)
					) {
					string temp; getline(gFile, temp, '\n');
					break;
				}
				// 将文本BA08的特殊情况排除，这里不需要句子，因为没有提取到
				if (tempWSCFileContent[i] == 0x00) {
					break;
				}

				//有人名
				if (tempWSCFileContent[i] == TextHeader) { //cerr << "4<" << cLine <<"> "; // 这个是有人名的正文
					WSCFileContent_CHS[OutLen++] = srcchar[i++]; // 补一个TextHeader
					unsigned int index = 0;
					string temp; getline(gFile, temp, '\n');
					cout << "[a." << temp << "]";
					//cerr << "1 ";
					//这里无边界检测
					//[ 的16进制
					while (temp[index++] != '\x5b') {}
					// 找人名开头标记，找到后index会加一跳出
					// ]的16进制
					while (temp[index] != '\x5d') {
						//if (temp[index] == 163)
						//{
						//	temp[++index] -= 128;
						//	WSCFileContent_CHS[OutLen].srcChar = temp[index++];
						//}
						//else if (temp[index] > 163) 
						//{
						//	WSCFileContent_CHS[OutLen].srcPos = 0;
						//	WSCFileContent_CHS[OutLen++].srcChar = temp[index++];
						//	WSCFileContent_CHS[OutLen].srcChar = temp[index++];
						//}
						//else 
						//{
						//	WSCFileContent_CHS[OutLen].srcChar = temp[index++];
						//}
						WSCFileContent_CHS[OutLen].srcChar = temp[index++];
						WSCFileContent_CHS[OutLen++].srcPos = 0;

						//WSCFileContent_CHS[OutLen++] = temp[index++]; // 人名就复制过去了
					}
					index++; // 跳掉 ]
					//cerr << "2 ";
					WSCFileContent_CHS[OutLen].srcPos = 0;
					WSCFileContent_CHS[OutLen++].srcChar = 0x00; // 补一个0x00
					while (index < temp.length()) {
						WSCFileContent_CHS[OutLen].srcChar = temp[index++];
						WSCFileContent_CHS[OutLen++].srcPos = 0;
						//WSCFileContent_CHS[OutLen++] = temp[index++]; // 句子复制过去
					}
				}
				else {
					unsigned int index = 0;
					string temp; getline( gFile, temp, '\n' );
					cout << endl << "[b." << temp << "]";
					while (index < temp.length()) {
						WSCFileContent_CHS[OutLen].srcChar = temp[index++];
						WSCFileContent_CHS[OutLen++].srcPos = 0;
						//WSCFileContent_CHS[OutLen++] = temp[index++]; // 句子复制过去
					}
				}
				//特殊情况 参照checkTail函数
				//没有做边界检测
				while (
					// 特殊标记结尾的特征
					!(tempWSCFileContent[i] == '%' && tempWSCFileContent[i + 1] == 'K')

					&& !(tempWSCFileContent[i - 2] == '%' && tempWSCFileContent[i - 1] == 'N'  && tempWSCFileContent[i] == (char)0x00)

					// %WE结尾  25 57 45 00
					&& !(tempWSCFileContent[i] == (char)0x00 && tempWSCFileContent[i - 1] == (char)0x45 && tempWSCFileContent[i - 2] == (char)0x57 && tempWSCFileContent[i - 3] == (char)0x25)
					// %FE结尾 25 46 45 00
					&& !(tempWSCFileContent[i] == (char)0x00 && tempWSCFileContent[i - 1] == (char)0x45 && tempWSCFileContent[i - 2] == (char)0x46 && tempWSCFileContent[i - 3] == (char)0x25)
					// %O 结尾  25 4F 00	
					&& !(tempWSCFileContent[i] == (char)0x00 && tempWSCFileContent[i - 1] == (char)0x4F && tempWSCFileContent[i - 2] == (char)0x25)
					// %W结尾  25 57 00 B6
					&& !(tempWSCFileContent[i] == (char)0x00 && tempWSCFileContent[i + 1] == (char)0xB6 && tempWSCFileContent[i - 1] == (char)0x57 && tempWSCFileContent[i - 2] == (char)0x25)
					// %AE结尾 25 41 45 00
					&& !(tempWSCFileContent[i] == (char)0x00 && tempWSCFileContent[i - 1] == (char)0x45 && tempWSCFileContent[i - 2] == (char)0x41 && tempWSCFileContent[i - 3] == (char)0x25)
					// %T500  25 54 35 30 30
					&& !(tempWSCFileContent[i - 1] == (char)0x30 && tempWSCFileContent[i - 2] == (char)0x30 && tempWSCFileContent[i - 3] == (char)0x35 && tempWSCFileContent[i - 4] == (char)0x54 && tempWSCFileContent[i - 5] == (char)0x25)
					// 」 81 76 00 49	
					&& !(tempWSCFileContent[i] == (char)0x00 && tempWSCFileContent[i + 1] == (char)0x49 && tempWSCFileContent[i - 1] == (char)0x76 && tempWSCFileContent[i - 2] == (char)0x81)
					// 特殊情况 、 00 41 66 00
					&& !(tempWSCFileContent[i] == (char)0x00 && tempWSCFileContent[i + 1] == (char)0x41 && tempWSCFileContent[i + 2] == (char)0x66 && tempWSCFileContent[i + 3] == (char)0x00)
					// 特殊情况  8   01 38 00 00
					&& !(tempWSCFileContent[i - 2] == (char)0x01 && tempWSCFileContent[i - 1] == (char)0x38 && tempWSCFileContent[i] == (char)0x00 && tempWSCFileContent[i + 1] == (char)0x00)



					// 特殊文本结尾的特征
					// 00 41 36 00
					&& !(tempWSCFileContent[i] == 0 && tempWSCFileContent[i + 1] == 0x41 && tempWSCFileContent[i + 2] == 0x36 && tempWSCFileContent[i + 3] == 0)
					// 00 41 3E 00
					&& !(tempWSCFileContent[i] == 0 && tempWSCFileContent[i + 1] == 0x41 && tempWSCFileContent[i + 2] == 0x3E && tempWSCFileContent[i + 3] == 0)
					// 00 0B 09 00
					&& !(tempWSCFileContent[i] == 0 && tempWSCFileContent[i + 1] == 0x0B && tempWSCFileContent[i + 2] == 0x09 && tempWSCFileContent[i + 3] == 0)
					// 00 0B 1D 00
					&& !(tempWSCFileContent[i] == 0 && tempWSCFileContent[i + 1] == 0x0B && tempWSCFileContent[i + 2] == 0x1D && tempWSCFileContent[i + 3] == 0)
					// 00 E5 00 41
					&& !(tempWSCFileContent[i] == 0 && tempWSCFileContent[i + 1] == 0xE5 && tempWSCFileContent[i + 2] == 0x00 && tempWSCFileContent[i + 3] == 0x41)
					// 00 0B 00 00 03
					&& !(tempWSCFileContent[i] == 0 && tempWSCFileContent[i + 1] == 0x0B && tempWSCFileContent[i + 2] == 0x00 && tempWSCFileContent[i + 3] == 0x00 && tempWSCFileContent[i + 4] == 0x03)
					) i++;
				
				break;

			case 'b': // 判断是选项的结尾
				{
					OutLen --; i --; // 判断选项时，用到了i-1作索引

					unsigned int offset = 1;
					//找选项开头（目测0x0001~0x01之间有猫腻，但是直接过掉）
					while((unsigned char)tempWSCFileContent[ i - offset ] > (unsigned char)0x04) offset ++; // 返回到前面找到正文
					for( offset --; offset > 0; offset -- ) OutLen --; // 判断的时候已经将选项内容复制过去了，现在要抹掉
					unsigned int index = 4; // 过 >### 和 ####
					string temp; getline( gFile, temp, '\n' );
					cout << endl << "[c." << temp << "]";
					while (index < temp.length()) {
						WSCFileContent_CHS[OutLen].srcChar = temp[index++];
						WSCFileContent_CHS[OutLen++].srcPos = 0;

						//WSCFileContent_CHS[OutLen++] = temp[index++]; // 句子复制过去
					}
					for (int k = 0; k < 10; k++) WSCFileContent_CHS[OutLen++] = srcchar[i++]; // 拷贝选项尾标记
					break;
				}
			default: break;
			} // switch

		}
		gFile.close( );
		cout << "03" << endl;

		// change offsets
		for (int i = 0; i + 5 < OutLen; i++) {
			if (WSCFileContent_CHS[i].srcChar == 0x00 && WSCFileContent_CHS[i + 1].srcChar == 0x06
				&& !( WSCFileContent_CHS[i + 2].srcChar == 0x00 && WSCFileContent_CHS[i + 3].srcChar == 0x00 
					&& WSCFileContent_CHS[i + 4].srcChar == 0x00 && WSCFileContent_CHS[i + 5].srcChar == 0x00
				 ) ) {
				// 
				// i + 2 --> offset begin
				// fetch value
				unsigned int originalPos;
				((char *)&originalPos)[0] = WSCFileContent_CHS[i + 2].srcChar;
				((char *)&originalPos)[1] = WSCFileContent_CHS[i + 3].srcChar;
				((char *)&originalPos)[2] = WSCFileContent_CHS[i + 4].srcChar;
				((char *)&originalPos)[3] = WSCFileContent_CHS[i + 5].srcChar;
				cerr << tempFileName << ": originalPos=" << originalPos << ", i=" << i << endl;

				// binary search
				for (int j = 0; j < OutLen; j++) {
					// Of course, this is not.
					if (WSCFileContent_CHS[j].srcPos == originalPos) {
						unsigned int newPos = j;
						cerr << tempFileName << ": newPos=" << newPos << ", i=" << i << endl;
						
						// set value
						WSCFileContent_CHS[i + 2].srcChar = ((char *)&newPos)[0];
						WSCFileContent_CHS[i + 3].srcChar = ((char *)&newPos)[1];
						WSCFileContent_CHS[i + 4].srcChar = ((char *)&newPos)[2];
						WSCFileContent_CHS[i + 5].srcChar = ((char *)&newPos)[3];

						break;
					}
				}

				// add index
				i += 5;
			}
		}
		
		// DEC Write
		pFile.open( ( PureScriptFolder + "\\WSC_DEC\\" + tempFileName ).c_str( ), ios::out | ios::trunc | ios::binary );
		for (int i = 0; i < OutLen; i++) 
		{
			pFile.write((char *)&(WSCFileContent_CHS[i].srcChar), 1);
		}
		//pFile.write( WSCFileContent_CHS, OutLen );
		pFile.close( );

		// ENC Write
		pFile.open( ( PureScriptFolder + "\\WSC_ENC\\" + tempFileName ).c_str( ), ios::out | ios::trunc | ios::binary );
		for( unsigned int j = 0; j < OutLen; j ++ ) WSCFileContent_CHS[ j ].srcChar = (char)WSC_EncryptHelper( WSCFileContent_CHS[ j ].srcChar );
		for (int i = 0; i < OutLen; i++)
			pFile.write((char *)&(WSCFileContent_CHS[i].srcChar), 1);
		//pFile.write( WSCFileContent_CHS, OutLen );
		pFile.close( );
		cout << "04" << endl;


		delete[] WSCFileContent_CHS;
		delete[] tempWSCFileContent;
		delete[] srcchar;
	}
	gListFile.close( );

	return;
}

void CrossChannelCrack::__8_CCSProcess( string InputFolder, string OutputFolder )
{
	_01_CreateFolder( "temp" ); //生成临时文件夹
	_01_CreateFolder( OutputFolder );

	string FFFF;
	for( unsigned int i = 0; i < InputFolder.length( ); i ++ ) {
		if( InputFolder[ i ] == '\\' ) FFFF += '_';
		else FFFF += InputFolder[ i ];
	}
	FFFF = "temp\\" + FFFF + "_FileList.txt";
	_02_getFileList( InputFolder, FFFF );//存到temp文件夹里

	char *TempSave;//临时存储字符串
	TempSave = new char [ FFFF.length( ) + 1 ];//临时存储文件路径
	for( UINT i = 0; i < FFFF.length( ); i ++ ) TempSave[ i ] = FFFF[ i ];
	TempSave[ FFFF.length( ) ] = '\0';
	
	char *FileNameHeader1 = new char [ InputFolder.length( ) + 2 ];//文件夹名称+'\\'
	for( UINT i = 0; i < InputFolder.length( ); i ++ ) FileNameHeader1[ i ] = InputFolder[ i ];
	FileNameHeader1[ InputFolder.length( ) ] = '\0';//先让这个字符串有个结尾
	if( InputFolder[ InputFolder.length( ) - 1 ] != '\\' ) {
		FileNameHeader1[ InputFolder.length( ) ] = '\\';
		FileNameHeader1[ InputFolder.length( ) + 1 ] = '\0';
	}//加个反斜杠

	char *FileNameHeader = new char [ OutputFolder.length( ) + 2 ];//文件夹名称+'\\'
	for( UINT i = 0; i < OutputFolder.length( ); i ++ ) FileNameHeader[ i ] = OutputFolder[ i ];
	FileNameHeader[ OutputFolder.length( ) ] = '\0';//先让这个字符串有个结尾
	if( OutputFolder[ OutputFolder.length( ) - 1 ] != '\\' ) {
		FileNameHeader[ OutputFolder.length( ) ] = '\\';
		FileNameHeader[ OutputFolder.length( ) + 1 ] = '\0';
	}//加个反斜杠
	
	fstream FileList; // 文件列表
	EasyUnicodeFileLE InFile, OutFile; // 读入文件
	FileList.open( TempSave, ios_base::in ); //打开之后TempSave就可以删掉了
	delete [ ] TempSave;

	TempSave = new char [ 20 ];//临时存储读出来的文件名
	while( !FileList.eof( ) ) {
		FileList.getline( TempSave, 19, '\n' ); //从“文件列表文件”文件中读取文件名
		if( TempSave[ 0 ] == '\0' ) continue;

		char *PathTemp = new char [ 100 ];

		strcpy_s( PathTemp, strlen( FileNameHeader1 ) + 1, FileNameHeader1 );
		strcat_s( PathTemp, strlen( PathTemp ) + strlen( TempSave ) + 1, TempSave );
		InFile.open( PathTemp, ios_base::in );

		strcpy_s( PathTemp, strlen( FileNameHeader ) + 1, FileNameHeader );
		strcat_s( PathTemp, strlen( PathTemp ) + strlen( TempSave ) + 1, TempSave );
		OutFile.open( PathTemp, ios_base::out | ios_base::trunc );

		int CountStep = 0;
		bool HeaderSign = true, AddSign = false;
		wstring WordLine, bakwstr = L""; // 为了后面能重复调用
		while( !InFile.IsEOF( ) ) {
			wstring Wtemp;
			Wtemp = InFile.readLine( );
			

			if( ( Wtemp[ 0 ] != L'/' || Wtemp[ 1 ] != L'/' ) && HeaderSign ) {
				HeaderSign = false;
				OutFile.writeln( L"" );
			}

			if( HeaderSign ) {
				switch( Wtemp[ 7 ] ) {
					case L'0':
						CountStep = 0; // 原文
						break;
					case L'1':
						CountStep = 1; // 初翻
						break;
					case L'2':
						CountStep = 2; // 校对
						break;
					case L'3':
						CountStep = 3; // 润色
						break;
					case L'4':
						CountStep = 4; // 验收
						break;
					default:
						if( !AddSign && CountStep != 0 ) {
							if( CountStep == 1 ) OutFile.writeln( L"//校对例 >2□9999□[见里]「……那个是……」" );
							else if( CountStep == 2 ) OutFile.writeln( L"//润色例 >3■9999■[见里]「……那个是……」" );
							else if( CountStep == 3 ) OutFile.writeln( L"//验收例 >4△9999△[见里]「……那个是……」" );
							else ;
							AddSign = true;
						}
						break;
				}
				OutFile.writeln( Wtemp );
			}
			else {
				if( bakwstr != Wtemp ) OutFile.writeln( Wtemp );
				bakwstr = Wtemp; // backup

				if( Wtemp.length( ) < 2 ) continue;
				else if( Wtemp[ 1 ] == TB.StringToWstring( 936, TB.IntToString( CountStep ) )[ 0 ] ) {
					if( CountStep == 1 ) { //OutFile.writeln( L"//校对例 >2□9999□[见里]「……那个是……」" );
						Wtemp[ 1 ] = L'2';
						Wtemp[ 2 ] = Wtemp[ Wtemp[ 3 ] == L'选' ? 6 : 7 ] = L'□';
					}
					else if( CountStep == 2 ) { //OutFile.writeln( L"//润色例 >3■9999■[见里]「……那个是……」" );
						Wtemp[ 1 ] = L'3';
						Wtemp[ 2 ] = Wtemp[ Wtemp[ 3 ] == L'选' ? 6 : 7 ] = L'■';
					}
					else if( CountStep == 3 ) { //OutFile.writeln( L"//验收例 >4△9999△[见里]「……那个是……」" );
						Wtemp[ 1 ] = L'4';
						Wtemp[ 2 ] = Wtemp[ Wtemp[ 3 ] == L'选' ? 6 : 7 ] = L'△';
					}
					else ;
					OutFile.writeln( Wtemp );
				}
			}
		}
		InFile.close( );
		OutFile.close( );
		delete [ ] PathTemp;
	}
	FileList.close( );
}

void CrossChannelCrack::__9_CCSInit(string InputFolder, string OutputFolder, string ReferFolder)
{
	// Usage:
	// -9 20150305 20150305_cv Rio_arc\WSC_Main

	_01_CreateFolder( "temp" ); //生成临时文件夹
	_01_CreateFolder( OutputFolder );

	string FFFF;
	for( unsigned int i = 0; i < InputFolder.length( ); i ++ ) {
		if( InputFolder[ i ] == '\\' ) FFFF += '_';
		else FFFF += InputFolder[ i ];
	}
	FFFF = "temp\\" + FFFF + "_FileList.txt";
	_02_getFileList( InputFolder, FFFF );//存到temp文件夹里

	char *TempSave;//临时存储字符串
	TempSave = new char [ FFFF.length( ) + 1 ];//临时存储文件路径
	for( UINT i = 0; i < FFFF.length( ); i ++ ) TempSave[ i ] = FFFF[ i ];
	TempSave[ FFFF.length( ) ] = '\0';
	
	char *FileNameHeader1 = new char [ InputFolder.length( ) + 2 ];//文件夹名称+'\\'
	for( UINT i = 0; i < InputFolder.length( ); i ++ ) FileNameHeader1[ i ] = InputFolder[ i ];
	FileNameHeader1[ InputFolder.length( ) ] = '\0';//先让这个字符串有个结尾
	if( InputFolder[ InputFolder.length( ) - 1 ] != '\\' ) {
		FileNameHeader1[ InputFolder.length( ) ] = '\\';
		FileNameHeader1[ InputFolder.length( ) + 1 ] = '\0';
	}//加个反斜杠

	char *FileNameHeader = new char [ OutputFolder.length( ) + 2 ];//文件夹名称+'\\'
	for( UINT i = 0; i < OutputFolder.length( ); i ++ ) FileNameHeader[ i ] = OutputFolder[ i ];
	FileNameHeader[ OutputFolder.length( ) ] = '\0';//先让这个字符串有个结尾
	if( OutputFolder[ OutputFolder.length( ) - 1 ] != '\\' ) {
		FileNameHeader[ OutputFolder.length( ) ] = '\\';
		FileNameHeader[ OutputFolder.length( ) + 1 ] = '\0';
	}//加个反斜杠
	
	fstream FileList; // 文件列表
	EasyUnicodeFileLE InFile, OutFile, ReferFile; // 读入文件
	FileList.open( TempSave, ios_base::in ); //打开之后TempSave就可以删掉了
	delete [ ] TempSave;

	
	TempSave = new char [ 20 ];//临时存储读出来的文件名
	while( !FileList.eof( ) ) {
		FileList.getline( TempSave, 19, '\n' ); //从“文件列表文件”文件中读取文件名
		if( TempSave[ 0 ] == '\0' ) continue;

		char *PathTemp = new char [ 100 ];

		strcpy_s( PathTemp, strlen( FileNameHeader1 ) + 1, FileNameHeader1 );
		strcat_s( PathTemp, strlen( PathTemp ) + strlen( TempSave ) + 1, TempSave );
		InFile.open( PathTemp, ios_base::in );
		//cerr << "0: (" << PathTemp << ")";

		strcpy_s( PathTemp, strlen( FileNameHeader ) + 1, FileNameHeader );
		strcat_s( PathTemp, strlen( PathTemp ) + strlen( TempSave ) + 1, TempSave );
		OutFile.open( PathTemp, ios_base::out | ios_base::trunc );
		cout << "Doing " << TempSave << endl;

		int CountStep = 0, CountIdx = 1, LineCount = 0;
		bool HeaderSign = true, AddSign = false;
		wstring WordLine; // 为了后面能重复调用

		// get line number
		//cerr << "{";
		while (!InFile.IsEOF()) {
			LineCount++;
			wstring Wtemp;
			Wtemp = InFile.readLine();
			if (Wtemp.length() < 7) LineCount--;
		}
		cerr << "LineCount: " << LineCount << endl;
		
		// read all to memory
		//cerr << "}";
		InFile.SetPointer(0, ios::beg);
		wstring *array = new wstring[LineCount];
		for (int i = 0; i < LineCount; i++) {
			array[i] = InFile.readLine();
			if (array[i].length() < 7) i--; // backwards
		}

		// read all refer text in ReferFolder
		int ReferCount = 0;
		ReferFile.open(ReferFolder + "\\" + TempSave, ios::in);
		while (!ReferFile.IsEOF()) {
			wstring Wtemp = ReferFile.readLine();
			if (Wtemp.substr(0, 2) == L">0")
				ReferCount++;
		}
		wstring *ReferList = new wstring[ReferCount];
		ReferFile.SetPointer(0, ios::beg);
		for(int i = 0; i < ReferCount;) {
			wstring Wtemp = ReferFile.readLine();
			if (Wtemp.substr(0, 2) == L">0") {
				ReferList[i++] = Wtemp;
				cerr << "(" << i << ")" << TB.WstringToString(936, Wtemp) << endl;
			}
		}
		ReferFile.close();
		ReferCount = 0;
		cerr << "Loaded" << endl;
		
		// do calculating and outputing
		//cerr << ".";
		OutFile.writeln(L"//原文例 >0○0001○[太一]「金曜日、か」");
		OutFile.writeln(L"//提纯例 >1●0001●[太一]「金曜日、か」");
		OutFile.writeln(L"//这是提纯后的文本！问题请反馈至imewx@qq.com");
		OutFile.writeln(L"");
		for (int i = 0; i < LineCount; i++) {
			// prevent access overflow
			cerr << "CurLine: " << i << endl;
			if (array[i].length() < 8) {
				OutFile.writeln(L"");
				continue;
			}

			// 012345678 - idx
			// >0○0001○[太一]「金曜日、か」
			// >1●0001●[太一]「金曜日、か」
			cerr << "1";
			cerr << "(" << TB.WstringToString(936,array[i]) << ")";
			if (array[i][1] == L'0') {
				// This is the original script
				int beg_scr = array[i][3] == L'选' ? 7 : 8;
				WordLine = array[i].substr(beg_scr, array[i].length() - beg_scr);

				// get last wordLine
				int j = i + 1, lastOkLine = i + 1;
				for ( ; j < LineCount; j ++) {
					// prevent access overflow
					if (array[j].length() < 8) continue;
					
					// if is a translated line
					if (array[j][1] == L'1' || array[j][1] == L'2' || array[j][1] == L'3' || array[j][1] == L'4')
						lastOkLine = j;
					else break;
				}
				if (j == LineCount) lastOkLine = LineCount - 1;

				
				
				// get last translated line
				cerr << "2";
				if (beg_scr == 8) {
					// judge if line number match
					cerr << "3";
					if (CountIdx != TB.StringToInt(TB.WstringToString(936, array[i].substr(3, 4)))) {
						//cerr << TempSave << ": line" << CountIdx << endl;
					}

					// This is just script
					wchar_t tempLineNumber[10];
					wsprintfW(tempLineNumber, L"%04d", CountIdx);
					CountIdx++; // line number plus one
					//OutFile.writeln(L">0○" + wstring(tempLineNumber) + L"○" + WordLine); // output 1
					OutFile.writeln(ReferList[ReferCount++]); // new output 1
					WordLine = array[lastOkLine].substr(beg_scr, array[lastOkLine].length() - beg_scr);
					OutFile.writeln(L">1●" + wstring(tempLineNumber) + L"●" + WordLine); // output 2
					cerr << "-";
				}
				else {
					// This is selector
					cerr << "4";
					//OutFile.writeln(array[i]);
					OutFile.writeln(ReferList[ReferCount++]);
					array[lastOkLine][1] = L'1';
					array[lastOkLine][2] = array[lastOkLine][6] = L'●';
					OutFile.writeln(array[lastOkLine]);
					cerr << "-";
				}
				OutFile.writeln(L"");

				// set i
				i = lastOkLine;
			}
			// else continue;
		}
		 cerr << "5" << endl;

		/*while( !InFile.IsEOF( ) ) {
			wstring Wtemp;
			Wtemp = InFile.readLine( );
			
			// 注释行
			if( Wtemp.length( ) < 2 || Wtemp[ 0 ] != L'/' && Wtemp[ 1 ] != L'/' ) HeaderSign = false;

			// 正文行
			if( HeaderSign ) { // 文件注释头
				switch( Wtemp[ 7 ] ) {
					case L'0': CountStep = 0; break; // 原文
					case L'1': CountStep = 1; break; // 初翻
					case L'2': CountStep = 2; break; // 校对
					case L'3': CountStep = 3; break; // 润色
					case L'4': CountStep = 4; break; // 验收
					default:
						if( !AddSign && CountStep != 0 ) {
							OutFile.writeln( L"//复制例 >2■9999■[见里]「……那个是……」" );
							AddSign = true;
						}
						break;
				}
				if( Wtemp[ 7 ] != L'1' && Wtemp[ 7 ] != L'2' && Wtemp[ 7 ] != L'3' && Wtemp[ 7 ] != L'4' )
					OutFile.writeln( Wtemp ); // 输出原文
			} else { // 正文部分
				if( Wtemp.length( ) < 2 ) { // 防止访问越界
					OutFile.writeln( L"" );
					continue;
				}
				
				// 擦除 junk bytes
				if( Wtemp[ 3 ] == L'选' && Wtemp[ 8 ] == L'\x0001' ) {
					for( int i = 9; i < Wtemp.length( ); i ++ ) Wtemp[ i - 2 ] = Wtemp[ i ];
					Wtemp.erase( Wtemp.length( ) - 2 );
				}

				if( Wtemp[ 0 ] == L'/' && Wtemp[ 1 ] == L'/' || Wtemp[ 1 ] == L'0' )
					OutFile.writeln( Wtemp );
				else if( Wtemp[ 1 ] == TB.StringToWstring( 936, TB.IntToString( CountStep ) )[ 0 ] ) {
					Wtemp[ 1 ] = L'2';
					Wtemp[ 2 ] = Wtemp[ Wtemp[ 3 ] == L'选' ? 6 : 7 ] = L'■';
					OutFile.writeln( Wtemp );
				}
			}
		}*/

		// GC
		InFile.close( );
		OutFile.close( );
		delete[] PathTemp;
		delete[] ReferList;
	}
	FileList.close( );
}

void CrossChannelCrack::__10_GetAllChapterTitle(string InputFolder, string OutputFile)
{
	// Usage: (Note: ex from dec file)
	// -10 tempRef_cv\WSC_DEC titles.txt

	// generate temperory folder
	_01_CreateFolder("temp");

	// input file is as output file name, '\\' -> '_'
	string FFFF;
	for (unsigned int i = 0; i < InputFolder.length(); i++) {
		if (InputFolder[i] == '\\') FFFF += '_';
		else FFFF += InputFolder[i];
	}
	_02_getFileList(InputFolder, "temp\\" + FFFF + "_FileList.txt");//存到temp文件夹里

	// open list file and go through file list
	fstream FileList;
	FileList.open(("temp\\" + FFFF + "_FileList.txt").c_str(), ios::in); // use FFFF as top

	// open output file in Unicode Little Endian
	EasyUnicodeFileLE OutFile;
	OutFile.open(OutputFile, ios::out | ios::trunc);

	char *TempFileNameSave, *TempFileContentSave;
	while (!FileList.eof()) {
		// allocate memory
		TempFileNameSave = new char[20];

		// read file name
		FileList.getline(TempFileNameSave, 19, '\n');
		if (TempFileNameSave[0] == '\0') continue;

		// filter
		if (TempFileNameSave[0] != 'C' || TempFileNameSave[1] != 'C') {
			delete[] TempFileNameSave; // escape memory leak
			continue; // let it go!
		}

		// read whole file
		cout << "Doing " << InputFolder + "\\" + TempFileNameSave;
		fstream file;
		file.open((InputFolder + "\\" + TempFileNameSave).c_str(), ios::binary | ios::in);
		if (!file.good()) {
			cerr << "failed!" << endl;
			delete[] TempFileNameSave; // escape memory leak
			continue;
		}
		file.seekg(0, ios::end); // set to end
		long fileSize = file.tellg(); // get file size
		cout << "\t" << fileSize;
		TempFileContentSave = new char[fileSize]; // malloc
		file.seekg(0, ios::beg); // set to head
		file.clear(); // clear end sign
		file.read(TempFileContentSave, fileSize); // read whole file

		// find first '\xE0'
		int idx = 0;
		for (; idx < 0x44; idx++)
			if (TempFileContentSave[idx] == '\xE0' && TempFileContentSave[idx+1] != '\0')
				break;

		// go through the whole file and find 0xE3
		if (TempFileContentSave[idx] == '\xE0') {
			string t = (char *)(&TempFileContentSave[idx+1]);
			OutFile.writeln(TB.StringToWstring(932,(string)TempFileNameSave)); // output file name, shift-jis
			OutFile.writeln(TB.StringToWstring(932, t));
			OutFile.writeln(L"");
			cout << endl;
		}
		else
			cout << "\tskipped" << endl;

		// GC
		delete[] TempFileContentSave;
		delete[] TempFileNameSave;
		file.close();
	}

	OutFile.close();
	FileList.close();

	return;
}

void CrossChannelCrack::__11_SetAllChapterTitle(string InputFile, string OutputFolder)
{
	// Usage: (Note: ex from dec file)
	// -11 titles_trans.txt 20150306_cv\WSC_DEC

	// generate temperory folder
	_01_CreateFolder(OutputFolder+"\\TITLE_CHANGED_ENC");

	// open output file in Unicode Little Endian
	EasyUnicodeFileLE InFile;
	InFile.open(InputFile, ios::in);

	while (!InFile.IsEOF()){
		wstring tempLine = InFile.readLine();
		if (tempLine.length() > 4 && tempLine.substr(tempLine.length() - 4, 4) == L".WSC") {
			// find file name
			string fileName = TB.WstringToString(936, tempLine);
			cout << fileName << endl;

			// filter
			if (fileName[0] != 'C' || fileName[1] != 'C') {
				continue; // let it go!
			}
			
			// read chapter title
			tempLine = InFile.readLine();
			string titleName = TB.WstringToString(936, tempLine);

			// write title to file
			fstream srcFile;
			srcFile.open((OutputFolder + "\\" + fileName).c_str(), ios::in | ios::binary); // not judge open 'cuz lazy
			srcFile.seekg(0, ios::end);
			long fileSize = srcFile.tellg();
			char *tempFileContent = new char[fileSize];
			srcFile.seekg(0, ios::beg);
			srcFile.clear();
			srcFile.read(tempFileContent, fileSize);

			fstream destFile;
			destFile.open((OutputFolder + "\\TITLE_CHANGED_ENC\\" + fileName).c_str(), ios::out | ios::binary | ios::trunc); // not judge open 'cuz lazy

			// load file
			SRCCHAR *inbytes = new SRCCHAR[fileSize];
			for (int i = 0; i < fileSize; i++) {
				inbytes[i].srcChar = tempFileContent[i];
				inbytes[i].srcPos = i;
			}
			SRCCHAR *result = new SRCCHAR[fileSize + 2048];
			int OutLen = 0;

			// find start position
			int idx = 0;
			for (; idx < 0x44; idx++) {
				if (tempFileContent[idx] == '\xE0' && tempFileContent[idx + 1] != '\0') {
					result[OutLen++] = inbytes[idx]; // copy 0xE0
					break;
				}
				else
					result[OutLen++] = inbytes[idx];
			}

			// copy title name
			for (int i = 0; i < titleName.length() + 1; i++) { // need one more zero('\0')
				result[OutLen].srcPos = 0;
				result[OutLen++].srcChar = titleName[i];
			}

			// find zero
			int zero = idx + 1;
			for ( ; zero < fileSize; zero++)
				if (tempFileContent[zero] == '\0')
					break; // find first '\0'

			// copy the rest
			for (int i = zero + 1; i < fileSize; i++)
				result[OutLen++] = inbytes[i];

			// change offsets
			for (int i = 0; i + 5 < OutLen; i++) {
				if (result[i].srcChar == 0x00 && result[i + 1].srcChar == 0x06
					&& !(result[i + 2].srcChar == 0x00 && result[i + 3].srcChar == 0x00
					&& result[i + 4].srcChar == 0x00 && result[i + 5].srcChar == 0x00)) {
					// i + 2 --> offset begin
					// fetch value
					unsigned int originalPos;
					((char *)&originalPos)[0] = result[i + 2].srcChar;
					((char *)&originalPos)[1] = result[i + 3].srcChar;
					((char *)&originalPos)[2] = result[i + 4].srcChar;
					((char *)&originalPos)[3] = result[i + 5].srcChar;

					// binary search
					for (int j = 0; j < OutLen; j++) {
						// Of course, this is not.
						if (result[j].srcPos == originalPos) {
							unsigned int newPos = j;

							// set value
							result[i + 2].srcChar = ((char *)&newPos)[0];
							result[i + 3].srcChar = ((char *)&newPos)[1];
							result[i + 4].srcChar = ((char *)&newPos)[2];
							result[i + 5].srcChar = ((char *)&newPos)[3];

							break;
						}
					}

					// add index
					i += 5;
				}
			}

			// encrypted
			for (int i = 0; i < OutLen; i++)
				result[i].srcChar = WSC_EncryptHelper(result[i].srcChar);
			//char t[100] = { '\0' };
			//for (int i = 0; i < fileSize; i++)
			//	tempFileContent[i] = WSC_EncryptHelper(tempFileContent[i]);
			//for (int i = 0; i < titleName.length(); i++)
			//	t[i] = WSC_EncryptHelper(titleName.c_str()[i]);
			//t[titleName.length()] = '\0';

			// write file
			for (int i = 0; i < OutLen; i++)
				destFile.write((char *)&(result[i].srcChar), 1);
			//destFile.write(tempFileContent, idx+1);
			//destFile.write(t, strlen(titleName.c_str()) + 1); // add one more '\0'
			//destFile.write((char *)(&tempFileContent[zero + 1]), fileSize - zero - 1);

			// GC
			delete[] tempFileContent;
			delete[] inbytes;
			delete[] result;
			srcFile.close();
			destFile.close();
		}
	}

	// GC
	InFile.close();

	return;
}

// This CRC32 function if for No.12 function.
#define ulong unsigned long
ulong CRC32( const char *buff, int len) {
	// CRC32 init
	ulong remainder = FDR_CRC_STARTING;
	void(*cycle)(ulong*, ulong*, char) = crc_le_cycle;
	ulong table[CRC_TABLE_SIZE];

	crc_fill_table(table, 0, FDR_CRC_POLYNOMIAL);
	for (int j = 0; j < len; j++) {
		cycle(table, &remainder, buff[j]);
		//printf("i=%d, %X\n", j, remainder);
		//system("pause");
	}
	return remainder;
};

void CrossChannelCrack::__12_PackText(string InputFolder, string OutputFile)
{
	// Usage:
	// -12 20150308_cv textpack.bin

	_01_CreateFolder("temp"); //生成临时文件夹

	string FFFF;
	for (unsigned int i = 0; i < InputFolder.length(); i++) {
		if (InputFolder[i] == '\\') FFFF += '_';
		else FFFF += InputFolder[i];
	}
	FFFF = "temp\\" + FFFF + "_FileList.txt";
	_02_getFileList(InputFolder, FFFF);//存到temp文件夹里

	char *TempSave;//临时存储字符串
	TempSave = new char[FFFF.length() + 1];//临时存储文件路径
	for (UINT i = 0; i < FFFF.length(); i++) TempSave[i] = FFFF[i];
	TempSave[FFFF.length()] = '\0';

	fstream FileList; // 文件列表
	EasyUnicodeFileLE InFile, OutFile, ReferFile; // 读入文件
	FileList.open(TempSave, ios_base::in); //打开之后TempSave就可以删掉了
	delete[] TempSave;

	// pack 1
	FDR_HEADER header;
	header.packageInfo = FDR_PACK_INFO;
	header.CRCStarting = FDR_CRC_STARTING;
	header.CRCPolynomial = FDR_CRC_POLYNOMIAL;
	//header.fileCount = Fi
	list<FDR_SFINFO> info;

	// global list
	int fileCount = 0;
	list<string> lchs, ljpn;
	while (!FileList.eof()) {
		// allocate memory
		char TempFileNameSave[20] = { '\0' };

		// read file name
		FileList.getline(TempFileNameSave, 19, '\n');
		if (TempFileNameSave[0] == '\0') continue;
		cerr << "Doing " << TempFileNameSave << "\b\b\b\b: ";
		fileCount++;

		char *PathTemp = new char[100];
		strcpy_s(PathTemp, (InputFolder + "\\").length() + 1, (InputFolder + "\\").c_str());
		strcat_s(PathTemp, strlen(PathTemp) + strlen(TempFileNameSave) + 1, TempFileNameSave);
		InFile.open(PathTemp, ios_base::in);

		int lineCount = 0;
		while (!InFile.IsEOF()) {
			wstring Wtemp = InFile.readLine();
			if (Wtemp.substr(0, 2) == L">0") {
				// This is jpn text
				Wtemp = Wtemp.substr(8, Wtemp.length() - 8);
				ljpn.push_back(TB.WstringToString(932, Wtemp));
				lineCount++;
			}
			else if (Wtemp.substr(0, 2) == L">1"){
				// This is chs text
				Wtemp = Wtemp.substr(8, Wtemp.length() - 8);

				// 半角 转 全角，去除{:}[]和%??
				// refer proc 4

				for (unsigned int k = 0; k < Wtemp.length(); k++) {
					/* 这里可以做一些字符替换 */
					switch (Wtemp[k]) {
					case L'\x30FB': Wtemp[k] = L'\x00B7'; break; // 实心点 ver1
					case L'\xFF65': Wtemp[k] = L'\x00B7'; break; // 实心点 ver2
					case L'\x266A': Wtemp[k] = L'\x2606'; break; // 音乐符号换成星星
					case L'\x3000': Wtemp[k] = L'\x0020'; break; // 大空格换成小空格
					case L'\x00E4': Wtemp[k] = L'\x0061'; break; // 重音a换成a
					case L'\x2020': Wtemp[k] = L'\x002B'; break; // 十字架换成+号
					default: break;
					}
				} // 字符替换


				char tempContent[1024] = { '\0' };
				string str = TB.WstringToString(936, Wtemp);
				memset(tempContent, '\0', sizeof(tempContent));

				// 半角转全角
				unsigned int j = 0, index = 0;
				for (; j < str.length() && tempContent[index + j] == '\0' && tempContent[index + j + 1] == '\0'; j++) {
					// index + j < delta - 1
					if (str[j] == ' ') { // Space is special
						tempContent[index++] = 0xA1;
						tempContent[index++] = 0xA1;
					}

					// Exceptions
					else if (j + 1 < str.length() && str[j] == '\\' && str[j + 1] == 'n') {
						// not copy here
						j++;
					}
					else if (str[j] == '{') {
						// copy name
						j++;
						while (j < str.length() && str[j] != ':') {
							tempContent[index++] = str[j++];
						}

						// not copy here
						while (j < str.length() && str[j] != '}')
							j++;
					}
					else if (j == 0 && str[j] == '[') {
						// not copy here
						while (j < str.length() && str[j] != ']')
							j++;
					}
					else if (str[j] == '%' && j + 2 < str.length() && '0' <= str[j + 1] && str[j + 1] <= 'z' && '0' <= str[j + 2] && str[j + 2] <= 'z') {
							j += 2;
					}

					else if ('!' <= str[j] && str[j] <= '~') {
						tempContent[index++] = 0xA3;
						tempContent[index++] = str[j] + 0x80;
					}
					else {
						tempContent[index++] = str[j];
						j++;
						if (j >= str.length())
							break;

						tempContent[index++] = str[j];
					}
				}

				cerr << "[" << tempContent << "]" << endl;
				lchs.push_back(string(tempContent));
			}
		}

		// pack 2
		string t = TempFileNameSave;
		t = t.substr(0, t.length() - 4);
		cerr << "(t=" << t << ")";
		FDR_SFINFO tempInfo;
		tempInfo.nameHash = CRC32(t.c_str(), t.length()); // in caps, e.g. CCA0001
		tempInfo.lineCount = lineCount;
		//tempInfo.beginOffset
		info.push_back(tempInfo);

		cerr << "(hash:" << hex << tempInfo.nameHash << dec << "), jp(" << ljpn.size() << "), zh(" << lchs.size() << ")" << endl;

		//GC
		delete[] PathTemp;
		InFile.close();
	}

	// check
	if (ljpn.size() != lchs.size()) {
		cerr << ljpn.size() << " != " << lchs.size();
		return;
	}

	// pack 3
	header.fileCount = info.size();

	// make output file
	fstream packfile;
	packfile.open(OutputFile.c_str(), ios::trunc | ios::out | ios::binary);
	packfile.write((char *)&header, sizeof(header));
	for (int i = 0; i < info.size()*sizeof(FDR_SFINFO); i++)
		packfile.write("\0", 1);
	// then write text

	// calc CRC32
	ulong *offset = new ulong[ljpn.size()];
	offset[0] = 0; // the first value
	ulong idx = 1;
	for (list<string>::iterator i = ljpn.begin(), j = lchs.begin(); i != ljpn.end() && j != lchs.end(); i++, j++ ) {
		ulong chsCRC32 = CRC32(j->c_str(), j->length());
		packfile.write("\x01", 1);
		packfile.write((char *)&chsCRC32, 4);
		packfile.write(i->c_str(), i->length() + 1); // plus one more '\0'

		// break
		if (idx >= ljpn.size())
			break;
		ulong len = 1 + 4 + i->length() + 1;
		offset[idx] = offset[idx - 1] + len;
		idx++;
	}

	// LastPack 4
	idx = 0;
	packfile.seekp(sizeof(header), ios::beg);
	for (list<FDR_SFINFO>::iterator i = info.begin(); i != info.end(); i++) {
		i->beginOffset = offset[idx];
		idx += i->lineCount;

		packfile.write((char *)&(*i), sizeof(FDR_SFINFO));
	}

	// GC
	FileList.close();
	packfile.close();
	delete[] offset;

	return;
}
#undef ulong

void CrossChannelCrack::_01_CreateFolder( string Name )
{
	//创建一个文件夹，允许嵌套
	if( Name.length( ) > 160 ) {
		cout << "FolderName length cannot be larger than 160!" << endl;
	}
	else {
		char tempName[ 161 ], temp[ 161 ];//temp[ ]用于依次存放嵌套文件夹
		for( UINT i = 0; i < Name.length( ); i ++ ) {
			if( Name[ 0 ] == '\\' || Name[ i ] == '/' || Name[ i ] == ':' || Name[ i ] == '?' ||
			Name[ i ] == '\"' || Name[ i ] == '<' || Name[ i ] == '?' || Name[ i ] == '|' ) {
				cout << "#### Districted character found! ####" << endl;
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

void CrossChannelCrack::_02_getFileList( string FolderName, string SaveTo )
{
	/* 不支持中文文件名和文件夹 */
	if( FolderName.length( ) > 160 || SaveTo.length( ) > 160 ) {
		cout << "File of folder Name length cannot be larger than 160!" << endl;
	}
	char tempName[ 161 ];
	for( UINT i = 0; i < FolderName.length( ); i ++ ) {
		if( FolderName[ 0 ] == '\\' || FolderName[ i ] == '/' || FolderName[ i ] == ':' || FolderName[ i ] == '?' ||
		FolderName[ i ] == '\"' || FolderName[ i ] == '<' || FolderName[ i ] == '?' || FolderName[ i ] == '|' ) {
			cout << "#### Districted character found! ####" << endl;
			return;
		}
	}
	for( UINT i = 0; i < SaveTo.length( ); i ++ ) {
		if( SaveTo[ 0 ] == '\\' || SaveTo[ i ] == '/' || SaveTo[ i ] == ':' || SaveTo[ i ] == '?' ||
		SaveTo[ i ] == '\"' || SaveTo[ i ] == '<' || SaveTo[ i ] == '?' || SaveTo[ i ] == '|' ) {
			cout << "#### Districted character found! ####" << endl;
			return;
		}
		tempName[ i ] = SaveTo[ i ];//tempName存放SaveTo的char*型文件名
	}
	tempName[ SaveTo.length( ) ] = '\0';

	wchar_t Dir[ 161 ];
	wstring tmp = StringToWstring( 936, FolderName );
	for( UINT i = 0; i < FolderName.length( ); i ++ ) {
		Dir[ i ] = tmp[ i ];
	}
	Dir[ FolderName.length( ) ] = L'\0';

	fstream F;
	//Unicode版本
	//F.open( tempName, ios_base::trunc | ios_base::out | ios_base::binary );
	//ANSI版本
	F.open( tempName, ios_base::trunc | ios_base::out );
	if( !F.is_open( ) ) {
		cout << "#### Saving-to file open failed! ####" << endl;
		return;
	}
	//F.write( "\xFF\xFE", 2 );
	
	WIN32_FIND_DATA FindFileData;
	HANDLE hFind = INVALID_HANDLE_VALUE;
	wchar_t DirSpec[ MAX_PATH ]; //定义要遍历的文件夹的目录
	//DWORD dwError;
	StringCchCopy( DirSpec, MAX_PATH, Dir );
	StringCchCat( DirSpec, MAX_PATH, TEXT( "\\*" ) ); //定义要遍历的文件夹的完整路径\*

	hFind = FindFirstFile( DirSpec, &FindFileData ); //找到文件夹中的第一个文件

	if( hFind == INVALID_HANDLE_VALUE ) { //如果hFind句柄创建失败，输出错误信息
		FindClose( hFind );
		cout << "#### Handle creating failed! ####" << endl;
		return;
	}
	else {
		while( FindNextFile( hFind, &FindFileData ) != 0) { //当文件或者文件夹存在时
			if( ( FindFileData.dwFileAttributes & FILE_ATTRIBUTE_DIRECTORY ) != 0
			&& wcscmp( FindFileData.cFileName, L"." ) == 0
			|| wcscmp( FindFileData.cFileName, L".." ) == 0 ) { //判断是文件夹&&表示为"."||表示为"."
				continue;
			}
			if( ( FindFileData.dwFileAttributes & FILE_ATTRIBUTE_DIRECTORY ) != 0 ) { //判断如果是文件夹
				// do nothing
			}
			else if( ( FindFileData.dwFileAttributes & FILE_ATTRIBUTE_DIRECTORY ) == 0) { //如果不是文件夹
				F << WstringToString( 936, FindFileData.cFileName ) << endl;
			}
		}
		FindClose( hFind );
	}
	F.close( );
	return;
}

void CrossChannelCrack::_03_getFileListAndSize( string FolderName, string SaveTo )
{
	/* 不支持中文文件名和文件夹 */
	if( FolderName.length( ) > 160 || SaveTo.length( ) > 160 ) {
		cout << "File of folder Name length cannot be larger than 160!" << endl;
	}
	char tempName[ 161 ];
	for( UINT i = 0; i < FolderName.length( ); i ++ ) {
		if( FolderName[ 0 ] == '\\' || FolderName[ i ] == '/' || FolderName[ i ] == ':' || FolderName[ i ] == '?' ||
		FolderName[ i ] == '\"' || FolderName[ i ] == '<' || FolderName[ i ] == '?' || FolderName[ i ] == '|' ) {
			cout << "#### Districted character found! ####" << endl;
			return;
		}
	}
	for( UINT i = 0; i < SaveTo.length( ); i ++ ) {
		if( SaveTo[ 0 ] == '\\' || SaveTo[ i ] == '/' || SaveTo[ i ] == ':' || SaveTo[ i ] == '?' ||
		SaveTo[ i ] == '\"' || SaveTo[ i ] == '<' || SaveTo[ i ] == '?' || SaveTo[ i ] == '|' ) {
			cout << "#### Districted character found! ####" << endl;
			return;
		}
		tempName[ i ] = SaveTo[ i ];//tempName存放SaveTo的char*型文件名
	}
	tempName[ SaveTo.length( ) ] = '\0';

	wchar_t Dir[ 161 ];
	wstring tmp = StringToWstring( 936, FolderName );
	for( UINT i = 0; i < FolderName.length( ); i ++ ) {
		Dir[ i ] = tmp[ i ];
	}
	Dir[ FolderName.length( ) ] = L'\0';

	fstream F, tempFile;
	F.open( tempName, ios_base::trunc | ios_base::out );
	if( !F.is_open( ) ) {
		cout << "#### Saving-to file open failed! ####" << endl;
		return;
	}
	
	WIN32_FIND_DATA FindFileData;
	HANDLE hFind = INVALID_HANDLE_VALUE;
	wchar_t DirSpec[ MAX_PATH ]; //定义要遍历的文件夹的目录
	//DWORD dwError;
	StringCchCopy( DirSpec, MAX_PATH, Dir );
	StringCchCat( DirSpec, MAX_PATH, TEXT( "\\*" ) ); //定义要遍历的文件夹的完整路径\*

	hFind = FindFirstFile( DirSpec, &FindFileData ); //找到文件夹中的第一个文件

	if( hFind == INVALID_HANDLE_VALUE ) { //如果hFind句柄创建失败，输出错误信息
		FindClose( hFind );
		cout << "#### Handle creating failed! ####" << endl;
		return;
	}
	else {
		while( FindNextFile( hFind, &FindFileData ) != 0) { //当文件或者文件夹存在时
			if( ( FindFileData.dwFileAttributes & FILE_ATTRIBUTE_DIRECTORY ) != 0
			&& wcscmp( FindFileData.cFileName, L"." ) == 0
			|| wcscmp( FindFileData.cFileName, L".." ) == 0 ) { //判断是文件夹&&表示为"."||表示为"."
				continue;
			}
			if( ( FindFileData.dwFileAttributes & FILE_ATTRIBUTE_DIRECTORY ) != 0 ) { //判断如果是文件夹
				// do nothing
			}
			else if( ( FindFileData.dwFileAttributes & FILE_ATTRIBUTE_DIRECTORY ) == 0) { //如果不是文件夹
				string tempFName = WstringToString( 936, FindFileData.cFileName );
				F << tempFName;
				if( FolderName[ FolderName.length( ) - 1 ] != '\\' ) tempFName = "\\" + tempFName;
				tempFName = FolderName + tempFName;
				char FName[ 321 ];
				for( UINT i = 0; i < tempFName.length( ); i ++ ) {
					FName[ i ] = tempFName[ i ];
				}
				FName[ tempFName.length( ) ] = '\0';
				tempFile.open( FName, ios_base::in | ios_base::binary );
				if( !tempFile.is_open( ) ) {
					cout << "#### File didn't open! ####" << endl;
					return;
				}
				tempFile.seekg( 0, ios_base::end );     // Step 1
				F << "\t" << tempFile.tellg( ) << endl; // Step 2
				tempFile.close( );
			}
		}
		FindClose( hFind );
	}
	F.close( );
	return;
}

void CrossChannelCrack::getFolderList( string FolderName, string SaveTo )
{
	/* 不支持中文文件名和文件夹 */
	if( FolderName.length( ) > 160 || SaveTo.length( ) > 160 ) {
		cout << "File of folder Name length cannot be larger than 160!" << endl;
	}
	char tempName[ 161 ];
	for( UINT i = 0; i < FolderName.length( ); i ++ ) {
		if( FolderName[ 0 ] == '\\' || FolderName[ i ] == '/' || FolderName[ i ] == ':' || FolderName[ i ] == '?' ||
		FolderName[ i ] == '\"' || FolderName[ i ] == '<' || FolderName[ i ] == '?' || FolderName[ i ] == '|' ) {
			cout << "#### Districted character found! ####" << endl;
			return;
		}
	}
	for( UINT i = 0; i < SaveTo.length( ); i ++ ) {
		if( SaveTo[ 0 ] == '\\' || SaveTo[ i ] == '/' || SaveTo[ i ] == ':' || SaveTo[ i ] == '?' ||
		SaveTo[ i ] == '\"' || SaveTo[ i ] == '<' || SaveTo[ i ] == '?' || SaveTo[ i ] == '|' ) {
			cout << "#### Districted character found! ####" << endl;
			return;
		}
		tempName[ i ] = SaveTo[ i ];//tempName存放SaveTo的char*型文件名
	}
	tempName[ SaveTo.length( ) ] = '\0';

	wchar_t Dir[ 161 ];
	wstring tmp = StringToWstring( 936, FolderName );
	for( UINT i = 0; i < FolderName.length( ); i ++ ) {
		Dir[ i ] = tmp[ i ];
	}
	Dir[ FolderName.length( ) ] = L'\0';

	fstream F;
	//Unicode版本
	//F.open( tempName, ios_base::trunc | ios_base::out | ios_base::binary );
	//ANSI版本
	F.open( tempName, ios_base::trunc | ios_base::out );
	if( !F.is_open( ) ) {
		cout << "#### Saving-to file open failed! ####" << endl;
		return;
	}
	//F.write( "\xFF\xFE", 2 );
	
	WIN32_FIND_DATA FindFileData;
	HANDLE hFind = INVALID_HANDLE_VALUE;
	wchar_t DirSpec[ MAX_PATH ]; //定义要遍历的文件夹的目录
	//DWORD dwError;
	StringCchCopy( DirSpec, MAX_PATH, Dir );
	StringCchCat( DirSpec, MAX_PATH, TEXT( "\\*" ) ); //定义要遍历的文件夹的完整路径\*

	hFind = FindFirstFile( DirSpec, &FindFileData ); //找到文件夹中的第一个文件

	if( hFind == INVALID_HANDLE_VALUE ) { //如果hFind句柄创建失败，输出错误信息
		FindClose( hFind );
		cout << "#### Handle creating failed! ####" << endl;
		return;
	}
	else {
		while( FindNextFile( hFind, &FindFileData ) != 0) { //当文件或者文件夹存在时
			if( ( FindFileData.dwFileAttributes & FILE_ATTRIBUTE_DIRECTORY ) != 0
			&& wcscmp( FindFileData.cFileName, L"." ) == 0
			|| wcscmp( FindFileData.cFileName, L".." ) == 0 ) { //判断是文件夹&&表示为"."||表示为"."
				continue;
			}
			if( ( FindFileData.dwFileAttributes & FILE_ATTRIBUTE_DIRECTORY ) != 0 ) { //判断如果是文件夹
				
				wchar_t DirAdd[MAX_PATH];
				StringCchCopy(DirAdd,MAX_PATH,Dir);
				StringCchCat(DirAdd,MAX_PATH,TEXT("\\"));  
				StringCchCat(DirAdd,MAX_PATH,FindFileData.cFileName); //拼接得到此文件夹的完整路径
				F << WstringToString( 936, DirAdd ) << endl;
			}
			else if( ( FindFileData.dwFileAttributes & FILE_ATTRIBUTE_DIRECTORY ) == 0) { //如果不是文件夹
				// do nothing
			}
		}
		FindClose( hFind );
	}
	F.close( );
	return;
}

void CrossChannelCrack::_04_ConvertToUnicode( UINT LocalOption, string gFileName, string SaveTo )
{
	return;
}

wstring CrossChannelCrack::StringToWstring( UINT LocalOption, string str )
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
	
	wstring wstr;
	for ( UINT i = 0; i < wcslen( wszString ); i ++ ) {
		wstr += wszString[ i ];
	}

	delete [ ] szAnsi;
	delete [ ] wszString;

	return wstr;
}

string CrossChannelCrack::WstringToString( UINT LocalOption, wstring wstr )
{
	wchar_t *wszString = new wchar_t [ wstr.length( ) + 1 ];
	for ( UINT i = 0; i < wstr.length( ); i ++ ) {
		wszString[ i ] = wstr[ i ];
	}
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

	/*校验转码是否有损*/
	if( StringToWstring( LocalOption, str ) != wstr ) cout << "# Warning: Converting unsafe!" << endl;
	
	return str;
}


unsigned __int64 CrossChannelCrack::LittleEndianCharsToValue( char LEValue[ 9 ] )
{
	UINT ii = 0;
	unsigned __int64 LEresult = 0;
	while( ii < 9 ) {
		LEresult += (unsigned __int8)LEValue[ ii ] * (unsigned __int64)pow( 256, ii );
		ii ++;
	}
	return LEresult;
}
unsigned __int64 CrossChannelCrack::LittleEndianCharsToValue_s( UINT Length, char LEValue[ 9 ] )
{
	unsigned __int64 LEresult = 0;
	for( UINT i = 0; i < Length; i ++ ) {
		LEresult += (unsigned __int8)LEValue[ i ] * (unsigned __int64)pow( 256, i );
	}
	return LEresult;
}
string CrossChannelCrack::ValueToLittleEndianChars( unsigned __int64 Value )
{
	return "";
}

unsigned char CrossChannelCrack::WSC_DecryptHelper( unsigned char s )
{
    _asm{
          mov al, s;
          ror al, 2;
          mov s, al;
    }
    return s;
}
unsigned char CrossChannelCrack::WSC_EncryptHelper( unsigned char s )
{
    _asm{
          mov al, s;
          rol al, 2;
          mov s, al;
    }
    return s;
}

unsigned long CrossChannelCrack::unwipf( unsigned char* buff,      // 输入文件正文的array
										 unsigned long  len,       // 输入文件长度
										 unsigned char* out_buff,  // 输出文件正文的array
										 unsigned long  out_len )  // 输出文件长度
{
	unsigned long  ring_len   = 4096;                        // 寻址范围就是0-4095
	unsigned char* ring       = new unsigned char[ring_len]; // 剪贴板
//	unsigned long ring_index  = 0xFEE;                       // 剪贴板的索引
	unsigned long  ring_index = 1;                           // 剪贴板的索引
	unsigned char* end        = buff + len;                  // 指向输入array的末尾
	unsigned char* out_end    = out_buff + out_len;          // 指向输出array的末尾

	memset(ring, 0, ring_len); // 剪贴板 置零

	while (buff < end && out_buff < out_end) { // 判断条件：不超过array的末尾
		unsigned char flags = *buff++; //<1> 取当前字符存到flags里面
	
		// 这个循环是判断8位的char型的每一位是否为1
		for (int i = 0; i < 8 && buff < end && out_buff < out_end; i++) { // 判断条件：char型长度8循环&&不超过array的末尾
			if (flags & 0x01) { // 判断：最低位是否为1
			/*
			*out_buff = ring[ring_index % ring_len] = *buff++; // 从ring[ 1 ]开始赋值到[ 0 ]，以4096循环
			ring_index++;
			*out_buff++;
			*/
		    *out_buff++ = ring[ring_index++ % ring_len] = *buff++; //<2>
			} else {
				if (end - buff < 2) break;
		
				unsigned long p = *buff++; //<3>
				unsigned long n = *buff++; //<4>
		
				//p = p | ( ( n >> 4 ) << 8 );
				p = (p << 4) | (n >> 4);   // ( RHL p, 4 ) OR ( RHR n, 4 ) 即 p的八位 与 n的前四位 构成
				n = (n & 0x0F) + 2;        // AND 00001111b; ADD 2 这里用到的是n的后四位
		
				for (unsigned long j = 0; j < n && out_buff < out_end; j++) {
				//for (unsigned long j = 0; j <= n && out_buff < out_end; j++) {
					/*
					*out_buff = ring[ring_index % ring_len] = ring[p % ring_len];
					p++;
					ring_index++;
					*out_buff++;
					*/
					*out_buff++ = ring[ring_index++ % ring_len] = ring[p++ % ring_len];
				}
			}

			flags >>= 1; // 右移1位，进入下一轮判断
		}
	}
	
	delete [] ring;

	return out_len - (out_end - out_buff); // 忽略掉的字符数量
}

void CrossChannelCrack::wipf_fake( unsigned char  *buff,       // 输入文件正文的array
								   unsigned long   len,        // 正文的长度
								   unsigned char **out_buff,  // 输出文件的正文array (指向指针的指针)
								   unsigned long  *out_len )   // 输出文件长度
{
	//LZSS_Encode( buff, len, &(*out_buff), out_len );
					
	*out_buff = new unsigned char [ len / 8 + len + 16 ]; // 16 useless byte for safe
	*out_len = 0;
	unsigned int index = 0;
	for( ; index < len; index ++ ) {
		if( index % 8 == 0 ) (*out_buff)[ (*out_len) ++ ] = 0xFF;
		(*out_buff)[ (*out_len) ++ ] = buff[ index ];
	}
	unsigned char tempFlags = 0xFF;
	while( index % 8 ) {
		tempFlags >>= 1;
		index ++;
	}

	if( tempFlags != 0xFF ) {
		(*out_buff)[ (*out_len) - (*out_len) % 9 ] = tempFlags;
		(*out_buff)[ (*out_len) ++ ] = 0x00;
		(*out_buff)[ (*out_len) ++ ] = 0x00;
	}
	else {
		(*out_buff)[ (*out_len) ++ ] = 0x00; // tempFlags
		(*out_buff)[ (*out_len) ++ ] = 0x00;
		(*out_buff)[ (*out_len) ++ ] = 0x00;
	}

	return;
}

void CrossChannelCrack::Test( )
{
	// used for future testings
	return;
}
