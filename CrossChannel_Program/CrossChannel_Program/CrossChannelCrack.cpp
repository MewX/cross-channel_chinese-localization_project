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
	Test( );//������ʱ����

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
		//���
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
		//���new
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
		//����
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
		//����
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
		//���new
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
		//�����ļ��У�����Ƕ��
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
		//��ȡ�ļ��б�
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
		//��ȡ�ļ��б�
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

void CrossChannelCrack::__1_Unpack( string FileName, string OutputFolder ) //�ϰ�Ľ��
{
	_01_CreateFolder( OutputFolder );
	/*�����ļ�������char**/
	if( OutputFolder[ OutputFolder.length( ) - 1 ] != '\\' ) OutputFolder += '\\';
	char *FolderName = new char [ OutputFolder.length( ) + 1 ];
	for( UINT i = 0; i < OutputFolder.length( ); i ++ ) FolderName[ i ] = OutputFolder[ i ];
	FolderName[ OutputFolder.length( ) ] = '\0';//string --> char*

	char *TempSave;//�������붯̬�ڴ��Ÿ���һ���Զ������Ķ���

	ifstream InFile;
	ofstream OutFile;
	char FileHeader[ 9 ], tempLittleEndian[ 9 ], temp[ 2 ] = "\0";
	unsigned __int64 FileNumbers;//�ļ�����

	char *FName = new char [ FileName.length( ) + 1 ];//��'\0'�����ռ�
	for( UINT i = 0; i < FileName.length( ); i ++ ) FName[ i ] = FileName[ i ];
	FName[ FileName.length( ) ] = '\0';//string --> char*

	InFile.open( FName, ios_base::in | ios_base::binary );
	if( !InFile.is_open( ) ) {
		cout << "#### Reading-in file open failed! ####" << endl;
		return;
	}
	InFile.read( FileHeader, 8 );//��ͷ����ʶ
	FileHeader[ 8 ] = '\0';
	if( !strcmp( FileHeader, "PackOnly" ) && !strcmp( FileHeader, "PackPlus" ) ) {
		cout  << "#### Reading-in file with unexpected header! ####" << endl;
		return;
	}//�ȱ�֤Header��������������֪ͷ���е�һ�֣�֮��ͨ���ж�'O'��'P'�Ϳ���������

	TempSave = new char [ 57 ];
	InFile.read( TempSave, 56 );//����56�ֽڵĿհ�
	delete [ ] TempSave;
	InFile.read( tempLittleEndian, 8 );
	tempLittleEndian[ 8 ] = '\0';
	FileNumbers = LittleEndianCharsToValue( tempLittleEndian );//��ȡ�ļ�ѭ������

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
		File[ i ].Offset = LittleEndianCharsToValue( tempLittleEndian );//��ȡ�ļ���ʼλ�õ�ƫַ

		InFile.read( tempLittleEndian, 8 );
		tempLittleEndian[ 8 ] = '\0';
		File[ i ].Size = LittleEndianCharsToValue( tempLittleEndian );//��ȡ�ļ���С
	}//���ļ����������ݴ浽�ڴ�

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
	}//�����ļ���ע�������Ƿ�Ҫ��ת

	cout << "  >> Total: " <<FileNumbers << " file(s)." << endl;

	InFile.close( );
	delete [ ] File;
	delete [ ] FName;
	delete [ ] FolderName;
}

void CrossChannelCrack::__1_Unpack2( string FileName, string OutputFolder ) //���̰�Ľ��
{
	_01_CreateFolder( OutputFolder );
	/* �����ļ�������char* */
	if( OutputFolder[ OutputFolder.length( ) - 1 ] != '\\' ) OutputFolder += '\\';
	char *FolderName = new char [ OutputFolder.length( ) + 1 ];
	for( UINT i = 0; i < OutputFolder.length( ); i ++ ) FolderName[ i ] = OutputFolder[ i ];
	FolderName[ OutputFolder.length( ) ] = '\0';//string --> char*

	char *TempSave; // �������붯̬�ڴ��Ÿ���һ���Զ������Ķ���

	ifstream InFile;
	ofstream OutFile;
	char tempLittleEndian[ 5 ], temp[ 2 ] = "\0";
	unsigned __int64 SuffixNumbers;//��׺����
	unsigned __int64 AllFileNumbers = 0;//�ļ�����

	char *FName = new char [ FileName.length( ) + 1 ];//��'\0'�����ռ�
	for( UINT i = 0; i < FileName.length( ); i ++ ) FName[ i ] = FileName[ i ];
	FName[ FileName.length( ) ] = '\0';//string --> char*

	InFile.open( FName, ios_base::in | ios_base::binary );
	if( !InFile.is_open( ) ) {
		cout << "#### Reading-in file open failed! ####" << endl;
		return;
	}
	
	struct SuffixArchieve {
		char Name[ 5 ];
		unsigned __int64 Number;//�����ļ�������
		unsigned __int64 Offset;
	};//�����ļ���չ����ص����ݽṹ

	struct FileArchive {
		char Name[FILENAME_LENGTH + 1];
		unsigned __int64 Offset;
		unsigned __int64 Size;
	};//�����ļ������Ϣ�����ݽṹ

	InFile.read( tempLittleEndian, 4 );//LittleEndian
	tempLittleEndian[ 4 ] = '\0';//�����չ����
	SuffixNumbers = LittleEndianCharsToValue_s( 1, tempLittleEndian );//������չ������

	SuffixArchieve *SUFFIX = new SuffixArchieve [ (UINT)SuffixNumbers ];//���ɴ洢��չ����Ϣ���ݽṹ��
	for( unsigned __int64 j = 0; j < SuffixNumbers; j ++ ) {
		/*���������չ������*/
		InFile.read( SUFFIX[ j ].Name, 4 );
		SUFFIX[ j ].Name[ 4 ] = '\0';//�����ļ���չ��

		InFile.read( tempLittleEndian, 4 );//LittleEndian
		tempLittleEndian[ 4 ] = '\0';
		SUFFIX[ j ].Number = LittleEndianCharsToValue_s( 4, tempLittleEndian );//�����ļ���
		AllFileNumbers += SUFFIX[ j ].Number; // ���������ļ��ļ���
		
		InFile.read( tempLittleEndian, 4 );
		tempLittleEndian[ 4 ] = '\0';
		SUFFIX[ j ].Offset = LittleEndianCharsToValue_s( 4, tempLittleEndian );//��ȡ��չ����ʼλ�õ�ƫַ
	}

	for( unsigned __int64 j = 0; j < SuffixNumbers; j ++ ) {//��չ������ѭ��
		InFile.seekg( SUFFIX[ j ].Offset, ios_base::beg );//��λ��չ����Ӧ���ļ���������λ��

		FileArchive *File = new FileArchive [ (UINT)SUFFIX[ j ].Number ];//���ɴ洢�ļ���Ϣ���ݽṹ��
		for( unsigned __int64 i = 0; i < SUFFIX[ j ].Number; i ++ ) {
			/*���ļ����������ݴ浽�ڴ�*/
			InFile.read( File[ i ].Name, FILENAME_LENGTH);
			File[ i ].Name[FILENAME_LENGTH] = '\0';

			InFile.read( tempLittleEndian, 4 );
			tempLittleEndian[ 4 ] = '\0';
			File[ i ].Size = LittleEndianCharsToValue_s( 4, tempLittleEndian );//��ȡ�ļ���С
			InFile.read( tempLittleEndian, 4 );
			tempLittleEndian[ 4 ] = '\0';
			File[ i ].Offset = LittleEndianCharsToValue_s( 4, tempLittleEndian );//��ȡ�ļ���ʼλ�õ�ƫַ
		}

		for( unsigned __int64 i = 0; i < SUFFIX[ j ].Number; i ++ ) {
			/*���ļ������ݴ浽�ڴ�*/
			UINT a = OutputFolder.length( ) + strlen( File[ i ].Name ) + 1 + 4 + 1;//���鳤�ȣ��ļ���+�ļ���+��+��չ��+'\0'��
			char *ttt = new char [ a ];
			strcpy_s( ttt, a, FolderName );//�ȸ����ļ�����
			strcat_s( ttt, a, File[ i ].Name );//�ٸ����ļ���
			strcat_s( ttt, a, "." );//���Ÿ���'.'
			strcat_s( ttt, a, SUFFIX[ j ].Name );//�������չ��
			cout << "     -> Extracting " << ttt << " ..." << endl;
			OutFile.open( ttt, ios_base::out | ios_base::binary | ios_base::trunc );

			InFile.seekg( File[ i ].Offset, ios_base::beg );
			TempSave = new char [ (UINT)File[ i ].Size ]; // ����洢�����ļ�����
			InFile.read( TempSave, File[ i ].Size );
			OutFile.write( TempSave, File[ i ].Size );
			OutFile.close( );

			/* WIPF unpack */
			if( !memcmp( TempSave, "WIPF", 4) ) {
				WIPFHDR *wipfhdr = (WIPFHDR *)TempSave; // WIPF�ļ�ͷ��wipfhdr���ڴ��е�����λ��ֱ�ӹҹ���TempSave�ϣ�������
				WIPFENTRY *wipfentries = (WIPFENTRY *)(wipfhdr + 1);

				AllFileNumbers += wipfhdr -> entry_count;

				unsigned char *data_buff = (unsigned char *)(wipfentries + wipfhdr->entry_count); // �������ݵĹҹ�
				for( unsigned long k = 0; k < wipfhdr->entry_count; k ++ ) { // ������ǰWIPF�еĸ��ļ�
					unsigned char *pal_buff  = NULL; // ��ɫͼ����ָ��
					
					if( wipfhdr -> depth == 8 ) { // ��ɫͼ���ɰ棿
						pal_buff = data_buff;  // ��ֵ
						data_buff += 1024;       // ͼƬ�������Ų1KB �������������
					}

					unsigned long out_depth = wipfhdr -> depth / 8; // λ���
					unsigned long out_stride = ( wipfentries[ k ].width * out_depth + 3 ) & ~3; // ����
					// ע�⣬�����~3��ֵΪ11111111111111111111111111111100b
					unsigned long  out_len  = wipfentries[ k ].height * out_stride; // �������
					unsigned char *out_buff = new unsigned char[ out_len ];         // Ŀ���ļ�����
					unwipf( data_buff, wipfentries[ k ].length, out_buff, out_len );
					data_buff += wipfentries[ k ].length;

					
					ttt[ a - 1 - 4 - 1 ] = '_'; // �����»���
					string out_filename = ttt;
					if ( wipfhdr -> entry_count > 1 ) {
						char tempChars[ 255 ];
						memset( tempChars, 0, 255 );
						sprintf_s( tempChars, 255, "+%03d+%dx%dy",
								k, wipfentries[ k ].offset_x, wipfentries[ k ].offset_y );
						out_filename += tempChars;
					}
					out_filename += ".bmp";

					if( wipfhdr -> depth == 24 ) { // 24λͼ
						unsigned char *temp_buff = new unsigned char[ out_len ];
						
						unsigned long color_stride = wipfentries[ k ].width;
							// RGBɫ��� = ��
						unsigned long color_len    = wipfentries[ k ].height * color_stride;
							// �� x �� ����Ϊ��RGB��ɫ�ģ�����һ��ͼ��һɫ��

						for( unsigned long y = 0; y < wipfentries[ k ].height; y ++ ) {
							// �м�ѭ��
							struct RGB { unsigned char r, g, b; };
							RGB *rgb_line = (RGB *)( temp_buff + y * out_stride );
								// temp_buff[ y * out_stride ] �������ָ��
							unsigned char *r_line = out_buff + y * color_stride;
							unsigned char *g_line = r_line + color_len;
							unsigned char *b_line = g_line + color_len;

							for( unsigned long x = 0; x < wipfentries[ k ].width; x ++ ) {
								// ��ѭ��������ѭ����rgb_line[ ]��һ���ڵ�����
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
					
					//��Ҫ����任 24bits & 8bits
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
	// Ҫ���ı�ʱ��Ҫ��������ļ�������PureScriptFolder\WSC_ENC ������

	_01_CreateFolder( "temp" );//������ʱ�ļ���
	_03_getFileListAndSize( SourceFolder, "temp\\pack_list.txt" );
	getFolderList( SourceFolder, "temp\\pack_folder_list.txt" );
	fstream gListFile, gFile, pFile; //��ȡ�ļ�g(et)File������ļ�p(ut)File

	gListFile.open( "temp\\pack_folder_list.txt", ios::in );
	string tempName; // can save FolderName & FileName
	if( gListFile >> tempName && tempName != "WSC_Main" ) {
#ifdef OTOMEGA // �����ӵ�Chip��Ҫ���ض����ļ�ת��
		gListFile.seekg( ios::beg ); // �жϵ�ʱ���ȡ��һ��������Ҫ����
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
			

			// Ҫ�ų�Thumbs.db
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
	gListFile.close( ); // �������������ȡ�ļ��б�

	/* ���ʱ����һ�����⣬�ļ�������չ�������д */
	string RealListFileName = "temp\\pack_list.txt"; // FileName & Size

	
	/* ����CCS�ű���WSC_Main�е�WSC�ļ����Ǳ����ļ��� */
	/* ע���ַ�����ͨ���ԣ��Լ�һЩ�滻 */
	if( tempName != "WSC_Main" ) {
		;
	}

	/* ͼ��ע�����µ��ã�Ҫ����wipf���������ļ��� */
	/* ����һ���ӿڣ������ǰĿ¼�����ļ���_FixedImgs�������������е�ͬ���ļ�����Ѱ��ͼƬ */
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
				unsigned char **FileContent; // ��ά��̬����洢�ļ����ݣ����ڴ�Ҫ�ֱ����
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
					if( gFile.good( ) ) { // �����޸ĵĲ��֣���Ҫʹ�ýӿ�
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
					// SizeList[ i ] -= sizeof( bmp_header_t ) + sizeof( bmp_dib_v3_header_t ); // PS�޸ĵ��ļ��ж����ֽ�
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
					/* ���µ��ã��Լ���ɫͼ���롢��ɫͼ����ͼ */
					unsigned char *in_buff;
					int in_depth = WipfHDR.depth / 8;
					if( ColorType == 1 ) in_buff = tempFileContent;
					else in_buff = tempFileContent + 1024;
					
	//cerr << "7" << endl;
	//cerr << " height  = " << WipfEntries[ i - StartFilePos ].height << endl;
	//cerr << " width   = " << WipfEntries[ i - StartFilePos ].width << endl;
					// Step 1: ����任
					for( unsigned int rr = 0; rr < WipfEntries[ i - StartFilePos ].height / 2; rr ++ ) {
						for( unsigned int ee = 0; ee < WipfEntries[ i - StartFilePos ].width * in_depth; ee ++ ) {
							swap( in_buff[ ( WipfEntries[ i - StartFilePos ].height - rr - 1 ) * WipfEntries[ i - StartFilePos ].width * in_depth + ee ],
								  in_buff[ rr * WipfEntries[ i - StartFilePos ].width * in_depth + ee ] );
						}
					}
					
	//cerr << "8" << endl;
					// Step 2: RGB ����
					if( ColorType == 1 ) {
						unsigned long  out_stride   = ( WipfEntries[ i - StartFilePos ].width * in_depth + 3 ) & ~3;
						unsigned char *temp_buff    = new unsigned char [ SizeList[ i ] ];
						unsigned long  color_stride = WipfEntries[ i - StartFilePos ].width; // RGBɫ��� = ��
						unsigned long  color_len    = WipfEntries[ i - StartFilePos ].height * color_stride;
							// �� x �� ����Ϊ��RGB��ɫ�ģ�����һ��ͼ��һɫ��

						for( unsigned long y = 0; y < WipfEntries[ i - StartFilePos ].height; y ++ ) { // �м�ѭ��
							struct RGB { unsigned char r, g, b; };
							RGB *rgb_line = (RGB *)&tempFileContent[ y * out_stride ]; // Line Content
							unsigned char *r_line = temp_buff + y * color_stride;
							unsigned char *g_line = r_line + color_len;
							unsigned char *b_line = g_line + color_len;

							for( unsigned long x = 0; x < WipfEntries[ i - StartFilePos ].width; x ++ ) {
								// ��ѭ��������ѭ����rgb_line[ ]��һ���ڵ�����
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
	/* ���ˣ��ļ��б�RealListFileName׼����ϣ�ֱ��װ��arc��� */


	/* ��� */
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
		// ����Ҫͳһ����ƫ�Ƶ�ַ
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
		/* ����offset�洢ͬ�����ļ����ۻ����ȣ�����ͳһ����ƫ�Ƶ�ַ */
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
	tempOffset += sizeof( ARCHDR ); // ��չ������
	tempOffset += sizeof( ARCSECTHDR ) * HDR.section_count; // ��չ�����
	for( unsigned int i = 0; i < HDR.section_count; i ++ ) {
		Section[ i ].toc_offset = tempOffset;
		tempOffset += sizeof( ARCENTRY ) * Section[ i ].entry_count; // �ļ������
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

// ���ϸ���������������ж��Ƿ�ﵽ�ı���β
// �����߽�
bool checkTail(char *FileContents, int i, int Size) {

	return (

		// 5��%NΪ���ݵ�������������βΪ��  00 41 0B 
		(FileContents[i] == (char)0x00 && FileContents[i + 1] == (char)0x41 && FileContents[i + 2] == (char)0x0B)

		// %N��β 25 4E 00 �����ڶ��%N�����������ֻ��������%N��
		|| (FileContents[i] == (char)0x00 && FileContents[i - 1] == (char)0x4E && FileContents[i - 2] == (char)0x25 && FileContents[i - 5] != (char)0x4E)

		// %WE��β 25 57 45 00 (Ҫ��ȥ���滹��%�����)
		|| (FileContents[i] == (char)0x00 && FileContents[i - 1] == (char)0x45 && FileContents[i - 2] == (char)0x57 && FileContents[i - 3] == (char)0x25)

		// %FE��β 25 46 45 00
		|| (FileContents[i] == (char)0x00 && FileContents[i - 1] == (char)0x45 && FileContents[i - 2] == (char)0x46 && FileContents[i - 3] == (char)0x25)

		//%O ��β 25 4F 00
		|| (FileContents[i] == (char)0x00 && FileContents[i - 1] == (char)0x4F && FileContents[i - 2] == (char)0x25)


		// %W��β 25 57 00 B6
		|| (FileContents[i] == (char)0x00 && FileContents[i + 1] == (char)0xB6 && FileContents[i - 1] == (char)0x57 && FileContents[i - 2] == (char)0x25)

		// %AE��β 25 41 45 00
		|| (FileContents[i] == (char)0x00 && FileContents[i - 1] == (char)0x45 && FileContents[i - 2] == (char)0x41 && FileContents[i - 3] == (char)0x25)


		// %T500  25 54 35 30 30
		|| (FileContents[i - 1] == (char)0x30 && FileContents[i - 2] == (char)0x30 && FileContents[i - 3] == (char)0x35 && FileContents[i - 4] == (char)0x54 && FileContents[i - 5] == (char)0x25)

		// '  00 0F 27 00 
		|| (FileContents[i] == (char)0x00 && FileContents[i - 1] == (char)0x27 && FileContents[i - 2] == (char)0x0F && FileContents[i - 3] == (char)0x00)

		// �� 81 76 00 49
		|| (FileContents[i] == (char)0x00 && FileContents[i + 1] == (char)0x49 && FileContents[i - 1] == (char)0x76 && FileContents[i - 2] == (char)0x81)

		// ������� �� 00 41 66 00
		|| (FileContents[i] == (char)0x00 && FileContents[i + 1] == (char)0x41 && FileContents[i + 2] == (char)0x66 && FileContents[i + 3] == (char)0x00)

		// �������  8   01 38 00 00
		|| (FileContents[i - 2] == (char)0x01 && FileContents[i - 1] == (char)0x38 && FileContents[i] == (char)0x00 && FileContents[i + 1] == (char)0x00)

		// ������� <!> 00 0F 00 00
		|| (FileContents[i - 2] == (char)0x00 && FileContents[i - 1] == (char)0x0F && FileContents[i] == (char)0x00 && FileContents[i + 1] == (char)0x00)

		// ������� ) 00 0F 01 29
		|| (FileContents[i - 4] == (char)0x00 && FileContents[i - 3] == (char)0x0F && FileContents[i - 2] == (char)0x01 && FileContents[i - 1] == (char)0x29)

		// 00 41 3E 00
		|| (FileContents[i] == (char)0x00 && FileContents[i + 1] == (char)0x41 && FileContents[i + 2] == (char)0x3E && FileContents[i + 3] == (char)0x00)


		// 00 0B 09 00
		|| (FileContents[i] == (char)0x00 && FileContents[i + 1] == (char)0x0B && FileContents[i + 2] == (char)0x09 && FileContents[i + 3] == (char)0x00)

		// �������(��Ӣ�ľ���Artificial Intelligence Operating system��ֱ�ӳ��֣������ı�֮��������Artificial Intelligence Operating system) 
		// 00 0B 00 00 03
		|| (FileContents[i] == (char)0x00 && FileContents[i + 1] == (char)0x0B && FileContents[i + 2] == (char)0x00 && FileContents[i + 3] == (char)0x00 && FileContents[i + 4] == (char)0x03)


		// 00 0B 1D 00

		|| (FileContents[i] == (char)0x00 && FileContents[i + 1] == (char)0x0B && FileContents[i + 2] == (char)0x1D && FileContents[i + 3] == (char)0x00)

		// 00 41 36 00 AA28�ı���ENTER PASSWORD	

		|| (FileContents[i] == (char)0x00 && FileContents[i + 1] == (char)0x41 && FileContents[i + 2] == (char)0x36 && FileContents[i + 3] == (char)0x00)

		// 00 E5 00 41

		|| (FileContents[i] == (char)0x00 && FileContents[i + 1] == (char)0xE5 && FileContents[i + 2] == (char)0x00 && FileContents[i + 3] == (char)0x41)

		);
}
// ���ڽ�utf16������ַ���ת��Ϊwstring
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
	_01_CreateFolder( "temp" );//������ʱ�ļ���

	string FFFF;
	for( unsigned i = 0; i < InputFolder.length( ); i ++ ) {
		if( InputFolder[ i ] == '\\' ) FFFF += '_';
		else FFFF += InputFolder[ i ];
	}
	FFFF = "temp\\" + FFFF + "_FileList.txt";
	_02_getFileList( InputFolder, FFFF );//�浽temp�ļ�����

	char *TempSave;//��ʱ�洢�ַ���
	TempSave = new char [ FFFF.length( ) + 1 ];//��ʱ�洢�ļ�·��
	for( UINT i = 0; i < FFFF.length( ); i ++ ) TempSave[ i ] = FFFF[ i ];
	TempSave[ FFFF.length( ) ] = '\0';

	char *FileNameHeader = new char [ InputFolder.length( ) + 2 ];//�ļ�������+'\\'
	for( UINT i = 0; i < InputFolder.length( ); i ++ ) FileNameHeader[ i ] = InputFolder[ i ];
	FileNameHeader[ InputFolder.length( ) ] = '\0';//��������ַ����и���β
	if( InputFolder[ InputFolder.length( ) - 1 ] != '\\' ) {
		FileNameHeader[ InputFolder.length( ) ] = '\\';
		FileNameHeader[ InputFolder.length( ) + 1 ] = '\0';
	}//�Ӹ���б��

	fstream FileList, InFile/*�Ȱ�Դ�ļ��浽�ڴ棬������ڴ��е����ݽ��в�������ȡ��Ч��Ϣ���ļ�*/;
	FileList.open( TempSave, ios_base::in );//��֮��TempSave�Ϳ���ɾ����

	delete [ ] TempSave;
	TempSave = new char [ 20 ];//��ʱ�洢���������ļ���
	while( !FileList.eof( ) ) {
		FileList.getline( TempSave, 19, '\n' );//�ӡ��ļ��б��ļ����ļ��ж�ȡ�ļ���
		if( TempSave[ 0 ] == '\0' ) continue;
		char *PathTemp = new char [ 100 ];
		strcpy_s( PathTemp, strlen( FileNameHeader ) + 1, FileNameHeader );
		strcat_s( PathTemp, strlen( PathTemp ) + strlen( TempSave ) + 1, TempSave );
		cout << "PathTemp = " << PathTemp << "\t";
		InFile.open( PathTemp, ios_base::in | ios_base::binary );
		InFile.seekg( 0, ios_base::end );//ָ���Ƶ��ļ�ĩ
		UINT Size = (UINT)InFile.tellg( );
		char *FileContents = new char [ Size ];//���ɺ��ļ�һ���������
		InFile.seekg( 0, ios_base::beg );
		InFile.read( FileContents, Size );//һ���԰��ļ�����
		InFile.close( );//Դ�ļ��������ڽ���

		char *RealSaveToFolder = new char [ 255 ];//FolderName \\ SuffixName_Main & SuffixName_Junk

		/*���ļ���չ����������*/
		if( TempSave[ strlen( TempSave ) - 3 ] == 'W' && TempSave[ strlen( TempSave ) - 2 ] == 'S' && TempSave[ strlen( TempSave ) - 1 ] == 'C' ) {
			char *TempTargetFile = new char [ Size ];//���ڴ�����ʱ�洢Ҫ������ļ�����
			int TTFlength = 0;

			//����ɷ�һЩ���ü����ԭ�ı�� ror 2
			const char TextHeader    =   (char)WSC_DecryptHelper( 0x3C );                                    //�ı���ͷ
			const char TextTail[4] = { (char)WSC_DecryptHelper( 0x94 ), (char)WSC_DecryptHelper( 0x2D ),
									   (char)WSC_DecryptHelper( 0x94 ), (char)WSC_DecryptHelper( 0x41 ) }; //�ı���β
			const char TextTail2[4] = { TextTail[0], TextTail[1], TextTail[2], (char)WSC_DecryptHelper(0x3D) }; //�ı���β2 (used in I/O only)
			const char TextTail3[4] = { TextTail[0], TextTail[1], TextTail[2], (char)WSC_DecryptHelper(0xC1) }; //�ı���β3 (used in I/O only)
			const char TextTail4[4] = { TextTail[0], TextTail[1], TextTail[2], (char)WSC_DecryptHelper(0x39) }; //�ı���β4 (used in I/O only)1
			const char PinyinHeader  =   (char)WSC_DecryptHelper( 0xED );                                    //ע�Ϳ�ͷ   {
			const char PinyinMiddle  =   (char)WSC_DecryptHelper( 0xE8 );                                    //ע�ͷָ��� :
			const char PinyinTail    =   (char)WSC_DecryptHelper( 0xF5 );                                    //ע�ͽ�β   }

			for( UINT i = 0; i < Size; i ++ ) {
				FileContents[ i ] = (char)WSC_DecryptHelper( FileContents[ i ] );
			}

			char Flag = NULL;//��ǣ��ı���ȴ����ע����a��ע�����󲿷�b��ע�����Ҳ���c����������Text��d�������ı�NULL
			for( UINT i = 0; i < Size; i ++ ) {
				if( i == Size - 1 ) cout << "Flag = " << Flag << "\t";
				if( i == Size - 1 && Flag != NULL ) {
					while( TTFlength - 2 >= 0 && ( TempTargetFile[ TTFlength - 1 ] != '\x0A' || TempTargetFile[ TTFlength - 2 ] != '\x0D' ) ) {
						//����һ�����з�֮���ȫ����ɾ��
						TTFlength --;
					}
					if( TTFlength - 2 < 0 ) TTFlength = 0;
					Flag = NULL;
					cout << "in break!" << endl;
					break;
				}

				if( i < Size - 1 && FileContents[ i ] == '\0' && FileContents[ i + 1 ] == TextHeader ) {//��һ�������ı���
					if( Flag != NULL  ) {
						//������������
						while( TTFlength - 2 >= 0 && ( TempTargetFile[ TTFlength - 1 ] != '\x0A' || TempTargetFile[ TTFlength - 2 ] != '\x0D' ) ) {
							//����һ�����з�֮���ȫ����ɾ��
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
					//�ı�β����ע�Ᵽ�漰����
					Flag = NULL;
					i += 1;//��������ȥ��
					TempTargetFile[ TTFlength ] = '\x0D';
					TempTargetFile[ TTFlength + 1 ] = '\x0A';//����
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
					//ѡ���β
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
					//ѡ���β
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
					//ѡ���β
#endif

					
					while( TTFlength - 2 >= 0 && ( TempTargetFile[ TTFlength - 1 ] != '\x0A' || TempTargetFile[ TTFlength - 2 ] != '\x0D' ) ) {
						//����һ�����з�֮���ȫ����ɾ��
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
					int offset = 2; // ��ǰƫ�Ƶ�����

					//��ѡ�ͷ��Ŀ��0x0001~0x01֮����è�壬����ֱ�ӹ�����
					while((unsigned char)FileContents[ i - offset ] > (unsigned char)0x04) offset ++; // ���ص�ǰ���ҵ�����
					TempTargetFile[ TTFlength ] = '#';
					if( FileContents[ i + 1 ] == 0x52 ) TempTargetFile[ TTFlength ] = '>';
					TempTargetFile[ TTFlength + 1 ] = '#';
					TempTargetFile[ TTFlength + 2 ] = '#';
					TempTargetFile[ TTFlength + 3 ] = '#';
					TTFlength += 4; // ѡ��ı����####
					for( offset --; offset > 1; offset -- ) {
						TempTargetFile[ TTFlength ] = FileContents[ i - offset ];
						TTFlength ++;
					}
					TempTargetFile[ TTFlength ] = '\x0D';
					TempTargetFile[ TTFlength + 1 ] = '\x0A';//����
					TTFlength += 2;
					TempTargetFile[ TTFlength ] = '\0';

					i += 9; // ѭ��������+1
					continue;
				}
				/*else if( Flag == 'a' && FileContents[ i ] == PinyinHeader ) {//��һ������ƴ����
					//cout << "  Flag = b" << endl;
					Flag = 'b';
					continue;
				}
				else if( Flag == 'b' && FileContents[ i ] == PinyinMiddle ) {//��һ������ƴ���ң�ע���滻
					//cout << "  Flag = c" << endl;
					Flag = 'c';
					continue;
				}
				else if( Flag == 'c' && FileContents[ i ] == PinyinTail ) {//ƴ��β��ע��ת�����
					//cout << "  Flag = PinyinTail" << endl;
					Flag = 'a';
					continue;
				}*/
				else { 
					//cout << "  Flag = OTHERS" << endl; 
				}//������Ҫ�ı���ַ�

				bool NameFlag = false;
				if( Flag == 'a' || Flag == 'b' || Flag == 'd' ) {
					if( Flag == 'd' && FileContents[ i ] == '\x00' && !NameFlag ) {
						TempTargetFile[ TTFlength ] = ']';//Ӣ�ı�����
						NameFlag = true;
					}
					else TempTargetFile[ TTFlength ] = FileContents[ i ];
					TTFlength ++;
				}
				else if( Flag == 'c' ) {
					//����Ҫ����
				}
			}
			
			/* ����������չ��Ϊwsc�Ľ��ܺ�Ľű� */
			strcpy_s( RealSaveToFolder, strlen( FileNameHeader ) + 1, FileNameHeader );//Essential
			strcat_s( RealSaveToFolder, strlen( RealSaveToFolder ) + 9 + 1, "WSC_Main\\" );//Essential
			_01_CreateFolder( RealSaveToFolder );//Essential
			strcat_s( RealSaveToFolder, strlen( RealSaveToFolder ) + strlen( TempSave ) + 1, TempSave );//Essential
			InFile.open( RealSaveToFolder, ios_base::trunc | ios_base::out | ios_base::binary );//Essential
			InFile.write( FileContents, Size );//һ����ȫ���浽�ļ���
			InFile.close( );
				
			cout << "TTF = " << TTFlength << endl;
			if( TTFlength > 2 && Flag == NULL ) {
				/* ����������չ��Ϊtxt�Ĵ��ı� */
				RealSaveToFolder[ strlen( RealSaveToFolder ) - 1 ] = 'T';
				RealSaveToFolder[ strlen( RealSaveToFolder ) - 2 ] = 'X';
				RealSaveToFolder[ strlen( RealSaveToFolder ) - 3 ] = 'T';
				InFile.open( RealSaveToFolder, ios_base::trunc | ios_base::out | ios_base::binary );//Essential
				InFile.write( TempTargetFile, TTFlength );//һ����ȫ���浽�ļ���
				InFile.close( );
				
				EasyUnicodeFileLE ULE;
				ifstream New_Txt_Stream;//������ĵ���ʱ����
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

				
				// �����ļ�InputFolderӦ����InputFolder��
				string temp = FileNameHeader + string(TempSave);
				temp.at(temp.length() - 3) = 'T';
				temp[temp.length() - 2] = 'X';
				temp[temp.length() - 1] = 'T';
				// �������ļ�
				New_Txt_Stream.open(temp, ios::in | ios::binary);

#endif
				ULE.open( RealSaveToFolder, ios_base::trunc | ios_base::out );
				wstring TempTargetFileULE;

				TempTargetFileULE += L"//������淶����С��ʾ�������������԰�Ctrl+H�����滻��ԭ�ĵĻ���Ҳû�£�\n";
				TempTargetFileULE += L"//ԭ���� >0��9999��[Ҋ��]����������ϡ�����\n";
				TempTargetFileULE += L"//������ >1��9999��[����]�������Ǹ��ǡ�����\n";
				TempTargetFileULE += L"//ע����Ҫ�����ı�ԭ�Ķ̣���������{��:������}��ע����\\n�ǻ��з����뱣��\n";
				TempTargetFileULE += L"//�����ı������ϵ����ⶼ���Է��ʼ���imewx@qq.comѯ�ʻ�ֱ����QQ307740614\n";

				int ULEStcCount = 1;
				int ULEChoiceCount = 0;
				bool StartNewLn = true, Redo = false;
				string tmp; // ��ʱ�洢�ַ��������м���
				wstring Sign1, Sign2;
				for( int k = 0; k < TTFlength; k ++ ) {
					/* ���δ�������TempTargetFile��TempTargetFileULE���� */
					if( TempTargetFile[ k ] == '>' && TempTargetFile[ k + 1 ] == '#' && TempTargetFile[ k + 2 ] == '#' && TempTargetFile[ k + 3 ] == '#' ){
						ULEChoiceCount = 1;
						k += 4;
						if( ULEChoiceCount == 1 ) TempTargetFileULE += L"\n"; // �ಹһ������
					}
					else if( TempTargetFile[ k ] == '#' && TempTargetFile[ k + 1 ] == '#' && TempTargetFile[ k + 2 ] == '#' && TempTargetFile[ k + 3 ] == '#' ){
						ULEChoiceCount ++;
						k += 4;
						if( ULEChoiceCount == 1 ) TempTargetFileULE += L"\n"; // �ಹһ������
					}
					else {
						ULEChoiceCount = 0;
						TempTargetFileULE += L"\n"; // �ಹһ������

						Sign1 = L">0��";
						wstring num = TB.StringToWstring( 936, TB.IntToString( ULEStcCount ) );
						for( int p = 1; p + num.length( ) <= 4; p ++ ) {
							Sign1 += L"0";
						} // ����4λ����
						Sign1 += num + L"��"; // >0��9999��
						Sign2 = Sign1;
						Sign2[ 1 ] = L'1';
						Sign2[ 2 ] = L'��';
						Sign2[ 7 ] = L'��'; // >1��9999��
						ULEStcCount ++;
					}
					tmp.clear( ); // tmp���

					while( k + 1 < TTFlength && !( TempTargetFile[ k ] == 0x0D && TempTargetFile[ k + 1 ] == 0x0A ) ) {
						tmp += TempTargetFile[ k ];
						k ++;
					}
					tmp += "\n";
					k += 1; // ��������+1

					wstring res = TB.StringToWstring( 932, tmp ); // Shift-JIS
					//if (res.length() > 1) {
						//res[res.length() - 1] = L'\n';
						if (ULEChoiceCount) TempTargetFileULE += L">0��ѡ��" + TB.StringToWstring(936, TB.IntToString(ULEChoiceCount)) + L"��";
						else TempTargetFileULE += Sign1;
						TempTargetFileULE += res;
						if (ULEChoiceCount) TempTargetFileULE += L">1��ѡ��" + TB.StringToWstring(936, TB.IntToString(ULEChoiceCount)) + L"��";
						else TempTargetFileULE += Sign2;

						// ��ӵڶ���
						//Ϊ�������ԭ��
						// New_Txt_Stream.eof()||(UINT)New_Txt_Stream.tellg()==0
						if (New_Txt_Stream.eof()) {
							TempTargetFileULE += res;
						}
						else {
							//�������
							const int clength = 3;
							char cc[clength] = { '\0' };/*��ǰ������ַ�*/
							char pc[clength] = { '\0' };/*��ǰ��ǰ�����ַ�*/
							string line = "";

							while (New_Txt_Stream.read(cc, clength - 1))
							{	/*һ�ζ��������ֽ�*/
								line += cc[0];
								line += cc[1];
								if ((pc[0] == '\x0d') && (pc[1] == '\x00')
									&& (cc[0] == '\x0a') && (cc[1] == '\x00'))
								{
									/*���з���־*/
									/*Unicode�ļ����ֽ���ת��Ϊ���ַ�*/
									std::wstring wstr = UTF16StringLineToWstring(line);

									//�����ȥ\r\n�е�\r,ֻ����\n������EasyUnicodeFileLE��write�����ı���β����һ��/r
									wchar_t temp_char = wstr.at(wstr.length() - 1);
									wstr.pop_back();
									wstr.pop_back();
									wstr += temp_char;

									TempTargetFileULE += wstr;

									break;
								}
								else if (cc[0] == '\xff' && cc[1] == '\xfe') {
									// ��ȥnew_txt�ж����FF FE ħ��(���UTF16��BOM)
									line.pop_back();
									line.pop_back();
								}
								strcpy(pc, cc);/*���浱ǰ�����ַ���ǰ���ַ�*/
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
			}//û���ı���
		}//WSC�ļ�
		else { }//�жϲ�����֪�ļ���չ��
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

	// �ļ�����������'\\'
	if( OriginalUnpackFolder[ OriginalUnpackFolder.length( ) - 1 ] == '\\' ) OriginalUnpackFolder.pop_back( );
	if( PureScriptFolder[ PureScriptFolder.length( ) - 1 ] == '\\' ) PureScriptFolder.pop_back( );
	
	/** < ����˵�� >
	 *  OriginalUnpackFolder �ǽ�����ļ��У�������һ�����ļ�����WSC_Main
	 *  PureScriptFolder     ����ɵ��ı����ڵ��ļ��У���ʽ��.CCS/.OMS/...��
	 *  ������ ��PureScriptFolder������ı��ᴿ������Ϊ.TXT�ŵ�PureScriptFolder\TXT���棬��WSC_Main�����TXT�ļ���ʽһ����
	 *         Ȼ�����TXT�ļ��������ܹ���WSC�ļ�������������Ϊ.WSC�ŵ�PureScriptFolder\WSC_DEC��
	 *         ����װ�����WSC�ļ���������λ����ŵ�PureScriptFolder\WSC_ENC���档
	 *         �����������Pack��������һ��������PureScriptFolder\WSC_ENC��
	 */

	_01_CreateFolder( "temp" ); //������ʱ�ļ���
	_03_getFileListAndSize( OriginalUnpackFolder, "temp\\WSC_List.txt" ); // �������ȡWSC�ļ��б�
	_03_getFileListAndSize( PureScriptFolder, "temp\\Scripts_List.txt" ); // �������ȡCCS/OMS/...�ļ��б�
	_01_CreateFolder( PureScriptFolder + "\\WSC_DEC" ); //������ʱ�ļ���
	_01_CreateFolder( PureScriptFolder + "\\WSC_ENC" ); //������ʱ�ļ���
	_01_CreateFolder( PureScriptFolder + "\\TXT" ); //������ʱ�ļ���

	fstream gListFile, gFile, pFile;
	string tempFileName;
	unsigned int tempLen;

	/* �Ȱ�LogFile�� */
	EasyUnicodeFileLE pLogFile;
	pLogFile.open( "temp\\Rio_LogFile.txt", ios::out | ios::trunc );


	/* �������UnicodeתGB2312-TXT�Ĳ�����Ҫ����Log�ļ�����¼ת�붪ʧ���ַ� */
	cout << "  [ Unicode -> GB2312-TXT ]" << endl;
	gListFile.open( "temp\\Scripts_List.txt", ios::in );
	while( gListFile >> tempFileName >> tempLen ) {
		cout << "  TXT Process: " << tempFileName << endl;
		FILE *gUNCFile;
		if( _wfopen_s( &gUNCFile, TB.StringToWstring( 936, PureScriptFolder + "\\" + tempFileName ).c_str( ), L"rb,ccs=UNICODE" ) != 0 ) {
			cerr << "####File open ERROR! (" << tempFileName << ")\n";
			return;
		}
		fseek( gUNCFile, 2, SEEK_SET ); // �����Ŀ�ͷ

		tempLen -= 2; // ȥ����ͷ��0xFEFF
		tempLen >>= 1; // ���Զ�����һ��
		wchar_t *tempFileContent;
		tempFileContent = new wchar_t [ tempLen ];
		fread_s( tempFileContent, 2 * tempLen, 2, tempLen, gUNCFile );
		fclose( gUNCFile );

		// һ��һ�зֽ⣬һ��һ�д���
		wstring tempSaveW; // �����ʱ����ת���������ַ�������Ƿ�����
		string tempSaveFileContent = ""; // GB2312�ͱ��浽��
		unsigned int i = 0, LineCount = 0;
		wchar_t MaxSeries = 0;
		while( i < tempLen ) {
			LineCount ++; // ������һ

			/* ����һ�� */
			wstring temp = L"";
			while( i < tempLen ) {
				if( ( i <= tempLen - 2 && tempFileContent[ i ] == L'\x000D'
						&& tempFileContent[ i + 1 ] == L'\x000A' && ( i = i + 2 ) )
					|| ( ( i <= tempLen - 1 && tempFileContent[ i ] == L'\x000A' && ( i = i + 1 ) ) ) ) break;
				else temp += tempFileContent[ i ++ ];
			}
			if( temp.length( ) < 8 ) continue; // һ�������ַ���̫����
			if( temp[ 6 ] == L'>' ) MaxSeries = temp[ 7 ]; // һϵ�е������
			if( temp[ 0 ] == L'/' && temp[ 1 ] == L'/' ) continue; // ע����

			/* �����е����� */
			// >2��0001��[��ϣ]��Ϊʲô�����Ƿۺ�ɫ���ء�������
			unsigned int StartPos = 0; // �����洢���ĵ�һ���ַ��ĵ�ַ����Ϊѡ�����ͨ���ӵ�ʼ�㲻ͬ
			if( temp[ 0 ] == L'>' ) { // ��һ������
				if( temp[ 1 ] == MaxSeries ) {
					if( temp[ 3 ] == L'ѡ' ) {
						// ��һ��ѡ�ͷ�� >###���������####
						if( temp[ 5 ] == L'1' ) tempSaveFileContent += ">###";
						else tempSaveFileContent += "####";
						StartPos = 7;
					} // ѡ��
					else StartPos = 8;

					tempSaveW = TB.StringToWstring( 936, TB.WstringToString( 936, temp.substr( StartPos, temp.length( ) - StartPos ) ) );
					for( unsigned int k = StartPos; k < temp.length( ); k ++ ) {
						/* ���������һЩ�ַ��滻 */
						switch( temp[ k ] ) {
						case L'\x30FB': temp[ k ] = tempSaveW[ k - StartPos ] = L'\x00B7'; break; // ʵ�ĵ� ver1
						case L'\xFF65': temp[ k ] = tempSaveW[ k - StartPos ] = L'\x00B7'; break; // ʵ�ĵ� ver2
						case L'\x266A': temp[ k ] = tempSaveW[ k - StartPos ] = L'\x2606'; break; // ���ַ��Ż�������
						case L'\x3000': temp[ k ] = tempSaveW[ k - StartPos ] = L'\x0020'; break; // ��ո񻻳�С�ո�
						case L'\x00E4': temp[ k ] = tempSaveW[ k - StartPos ] = L'\x0061'; break; // ����a����a
						case L'\x2020': temp[ k ] = tempSaveW[ k - StartPos ] = L'\x002B'; break; // ʮ�ּܻ���+��
						default: break;
						}
					} // �ַ��滻
					if( tempSaveW != temp.substr( StartPos, temp.length( ) - StartPos ) ) {
						for( unsigned int k = StartPos; k < temp.length( ); k ++ ) {
							/* ����������������־�ĵط� */
							if( tempSaveW[ k - StartPos ] != temp[ k ] ) {
								pLogFile.writeln( L"[ " + TB.StringToWstring( 936, tempFileName ) + L" ] [ line: "
										+ TB.StringToWstring( 936, TB.IntToString( LineCount ) )
										+ L" ] ��" + temp[ k ] + L"�� in ��" + temp + L"��" );
							}
						}
					} // ˵��ת����������

					char tempContent[ 2048 ];
					string str = TB.WstringToString( 936, tempSaveW );
					memset( tempContent, '\0', sizeof( tempContent ) );
					//strcpy( tempContent, str.c_str( ) );

					// ���תȫ��
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
						// ������ת��tip��ת���ַ������������ֱ�Ų��ܱ�ת��
						else if (str[j] == '%') {
							//�������ı���ֵ
							while (str[j] < 0x80) {
								tempContent[index + j] = str[j];
								j++;
								if (j >= str.length()) {
									pLogFile.writeln(L"[ " + TB.StringToWstring(936, tempFileName) + L" ] [ line: "
										+ TB.StringToWstring(936, TB.IntToString(LineCount))
										+ L" ] endline in ��" + TB.StringToWstring(936, str) + L"��");
									break;
								}
							}
						}
						// ȫ���ַ��ĸ�λ
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
										+ L" ] endline in ��" + TB.StringToWstring( 936, str ) + L"��" );
								break;
							}
							tempContent[ index + j ] = str[ j ];
						}
						else if( str[ j ] == '{' ) {
							// problem
							// {�ʹ�:������}������:������}

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
												+ L" ] endline in ��" + TB.StringToWstring( 936, str ) + L"��" );
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
												+ L" ] endline in ��" + TB.StringToWstring( 936, str ) + L"��" );
										break;
									}
									tempContent[ index + j ] = str[ j ];
								}
								j ++;
							}
							tempContent[ index + j ] = str[ j ];
						}
						else if (str[j] == '%' && j + 2 < str.length() && '0' <= str[j + 1] && str[j + 1] <= 'z' && '0' <= str[j+2] && str[j+2] <= 'z') {
							// ��һ��ת���ַ�
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
										+ L" ] endline in ��" + TB.StringToWstring( 936, str ) + L"��" );
								break;
							}
							tempContent[ index + j ] = str[ j ];
						}
					}
						
					tempSaveFileContent += string( tempContent ) + "\n";
				} // �����������
				else continue;
			}
		}
		cout << "MaxSeries = " << (char)MaxSeries << endl;

		/* ���TXT�ļ� */
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


	/* �������GB2312-TXTǶ��GB2312-WSC_DEC&ENC�Ĳ��� */
	cout << "  [ GB2312-TXT -> GB2312-WSC_DEC&ENC ]" << endl;
	gListFile.open( "temp\\WSC_List.txt", ios::in );
	while( gListFile >> tempFileName >> tempLen ) {
		cout << "  WSC Process: " << tempFileName << endl;
		/* ��ԭ����WSC�ļ� */
		bool hasText = true;
		gFile.open( ( OriginalUnpackFolder + "\\WSC_Main\\" + tempFileName ).c_str( ), ios:: in | ios::binary );
		if( !gFile.good( ) ) { // û���ı���WSC�ļ�
			gFile.open( ( OriginalUnpackFolder + "\\" + tempFileName ).c_str( ), ios:: in | ios::binary );
			hasText = false;
		}
		char *tempWSCFileContent = new char [ tempLen ];
		gFile.read( tempWSCFileContent, tempLen );
		gFile.close( ); // ����WSC�ļ�ȫ�������ˣ�������gFile��TXT�ļ�
		cout << "01" << endl;

		/* ���ո��ᴿ��TXT�ļ� */
		tempFileName[ tempFileName.length( ) - 1 ] = 'T';
		tempFileName[ tempFileName.length( ) - 2 ] = 'X';
		tempFileName[ tempFileName.length( ) - 3 ] = 'T'; // ��ʱ��һ���ļ���
		gFile.open( ( PureScriptFolder + "\\TXT\\" + tempFileName ).c_str( ), ios::in ); // һ��һ�ж�getline
		tempFileName[ tempFileName.length( ) - 3 ] = 'W';
		tempFileName[ tempFileName.length( ) - 2 ] = 'S';
		tempFileName[ tempFileName.length( ) - 1 ] = 'C'; // ��TXT���ٸĻ�������Ϊ�����ļ���WSC
		if( !gFile.good( ) ) { // �ļ�û�򿪣�˵��û��������İ棬�Ǿ�ֱ��copy
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

		/* ����ɷ�һЩ���ü����ԭ�ı�� ( ror x, 2 ) */
		const char TextHeader    =   (char)WSC_DecryptHelper( 0x3C );                                    //�ı���ͷ

		SRCCHAR *WSCFileContent_CHS = new SRCCHAR[tempLen + 4096]; // �����4K�ֽ�
		unsigned int OutLen = 0; // ������ֽ�
		/** < ˼· >
		 *  �ж��ı�����0x00000F����һ���ǲ���0x0F��������������ֱ��0x00�������ģ�������������ֱ�����ġ����ĵ�%K%Pֹ��
		 *  �ж�ѡ���ѡ��β��Ȼ����ǰ�ҵ�0x00Ϊֹ
		 **/
		unsigned int i = 0, cLine = 0;
		char Sign = 0x00; // ��while�����н���
		while( i < tempLen ) {
			while( i < tempLen ) { // �ҿ��滻�Ĳ���
				if( i + 2 < tempLen && tempWSCFileContent[ i ] == 0x00 && tempWSCFileContent[ i + 1 ] == TextHeader) 
				{ Sign = 'a'; break; } // �����ж����ı�
#ifdef CROSSCHANNEL // Cross Channel
				else if( i > 1 && i + 10 < tempLen && tempWSCFileContent[ i ] == 0x01 && tempWSCFileContent[ i - 1 ] == 0x00
					&& (   tempWSCFileContent[ i + 1 ] == 0x52 && tempWSCFileContent[ i + 8 ] == 0x01
						|| tempWSCFileContent[ i + 1 ] == 0x53 && tempWSCFileContent[ i + 8 ] == 0x02
						|| tempWSCFileContent[ i + 1 ] == 0x54 && tempWSCFileContent[ i + 8 ] == 0x03
						|| tempWSCFileContent[ i + 1 ] == 0x55 && tempWSCFileContent[ i + 8 ] == 0x04 )
					&& tempWSCFileContent[ i + 2 ] == 0x03 && tempWSCFileContent[ i + 3 ] == 0x03 && tempWSCFileContent[ i + 4 ] == 0x01
					&& tempWSCFileContent[ i + 5 ] == 0x02 && tempWSCFileContent[ i + 6 ] == 0x00 && tempWSCFileContent[ i + 7 ] == 0x00
					&& tempWSCFileContent[ i + 9 ] == 0x00 ) { //ѡ���β
#endif
#ifdef OTOMEGA // Otomega
				else if( i > 1 && i + 10 < tempLen && tempWSCFileContent[ i ] == 0x01 && tempWSCFileContent[ i - 1 ] == 0x00
					&& (   tempWSCFileContent[ i + 1 ] == 0x52 || tempWSCFileContent[ i + 1 ] == 0x53 
						|| tempWSCFileContent[ i + 1 ] == 0x54 || tempWSCFileContent[ i + 1 ] == 0x55 )
					&& tempWSCFileContent[ i + 2 ] == 0x03 && tempWSCFileContent[ i + 3 ] == 0x07 && tempWSCFileContent[ i + 4 ] == 0x4B
					&& tempWSCFileContent[ i + 5 ] == 0x59 && tempWSCFileContent[ i + 6 ] == 0x30 && tempWSCFileContent[ i + 7 ] == 0x31
					&& tempWSCFileContent[ i + 8 ] == 0x5F && tempWSCFileContent[ i + 9 ] == 0x30 ) { //ѡ���β
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
					//ѡ���β
#endif
					Sign = 'b'; break; // �ж���ѡ��Ľ�β
				}

				WSCFileContent_CHS[OutLen++] = srcchar[i++]; // ����
			} // �жϱ�ǵ�while
			if( i >= tempLen ) { cout << "break - " << tempFileName << "; i = " << i << endl; break;} // ��������ѭ��û�����
			cout << "(" << Sign << ")";

			cLine ++;
			switch( Sign ) {
			case 'a': // �����ж����ı���ͷ
				for (int k = 0; k < 2; k++) WSCFileContent_CHS[OutLen++] = srcchar[i++]; // �����жϹ���3��2�����ֽ�

				// ����Ϊ���е�������� 16����Ϊ00 0F 00 00 
				// �Լ� '  00 0F 27 00 �����
				// ������� <!> 00 0F 00 00	
				// ������� ) 00 0F 01 29
				// ֱ��ʹ��ԭ�ļ���
				if ((tempWSCFileContent[i] == 0x00 && tempWSCFileContent[i + 1] == 0x00)
					|| (tempWSCFileContent[i] == 0x27 && tempWSCFileContent[i + 1] == 0x00)
					|| (tempWSCFileContent[i] == 0x00 && tempWSCFileContent[i + 1] == 0x00)
					|| (tempWSCFileContent[i] == 0x01 && tempWSCFileContent[i + 1] == 0x29)
					// ���%N
					|| (tempWSCFileContent[i] == 0x25 && tempWSCFileContent[i + 1] == 0x4E)
					) {
					string temp; getline(gFile, temp, '\n');
					break;
				}
				// ���ı�BA08����������ų������ﲻ��Ҫ���ӣ���Ϊû����ȡ��
				if (tempWSCFileContent[i] == 0x00) {
					break;
				}

				//������
				if (tempWSCFileContent[i] == TextHeader) { //cerr << "4<" << cLine <<"> "; // �����������������
					WSCFileContent_CHS[OutLen++] = srcchar[i++]; // ��һ��TextHeader
					unsigned int index = 0;
					string temp; getline(gFile, temp, '\n');
					cout << "[a." << temp << "]";
					//cerr << "1 ";
					//�����ޱ߽���
					//[ ��16����
					while (temp[index++] != '\x5b') {}
					// ��������ͷ��ǣ��ҵ���index���һ����
					// ]��16����
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

						//WSCFileContent_CHS[OutLen++] = temp[index++]; // �����͸��ƹ�ȥ��
					}
					index++; // ���� ]
					//cerr << "2 ";
					WSCFileContent_CHS[OutLen].srcPos = 0;
					WSCFileContent_CHS[OutLen++].srcChar = 0x00; // ��һ��0x00
					while (index < temp.length()) {
						WSCFileContent_CHS[OutLen].srcChar = temp[index++];
						WSCFileContent_CHS[OutLen++].srcPos = 0;
						//WSCFileContent_CHS[OutLen++] = temp[index++]; // ���Ӹ��ƹ�ȥ
					}
				}
				else {
					unsigned int index = 0;
					string temp; getline( gFile, temp, '\n' );
					cout << endl << "[b." << temp << "]";
					while (index < temp.length()) {
						WSCFileContent_CHS[OutLen].srcChar = temp[index++];
						WSCFileContent_CHS[OutLen++].srcPos = 0;
						//WSCFileContent_CHS[OutLen++] = temp[index++]; // ���Ӹ��ƹ�ȥ
					}
				}
				//������� ����checkTail����
				//û�����߽���
				while (
					// �����ǽ�β������
					!(tempWSCFileContent[i] == '%' && tempWSCFileContent[i + 1] == 'K')

					&& !(tempWSCFileContent[i - 2] == '%' && tempWSCFileContent[i - 1] == 'N'  && tempWSCFileContent[i] == (char)0x00)

					// %WE��β  25 57 45 00
					&& !(tempWSCFileContent[i] == (char)0x00 && tempWSCFileContent[i - 1] == (char)0x45 && tempWSCFileContent[i - 2] == (char)0x57 && tempWSCFileContent[i - 3] == (char)0x25)
					// %FE��β 25 46 45 00
					&& !(tempWSCFileContent[i] == (char)0x00 && tempWSCFileContent[i - 1] == (char)0x45 && tempWSCFileContent[i - 2] == (char)0x46 && tempWSCFileContent[i - 3] == (char)0x25)
					// %O ��β  25 4F 00	
					&& !(tempWSCFileContent[i] == (char)0x00 && tempWSCFileContent[i - 1] == (char)0x4F && tempWSCFileContent[i - 2] == (char)0x25)
					// %W��β  25 57 00 B6
					&& !(tempWSCFileContent[i] == (char)0x00 && tempWSCFileContent[i + 1] == (char)0xB6 && tempWSCFileContent[i - 1] == (char)0x57 && tempWSCFileContent[i - 2] == (char)0x25)
					// %AE��β 25 41 45 00
					&& !(tempWSCFileContent[i] == (char)0x00 && tempWSCFileContent[i - 1] == (char)0x45 && tempWSCFileContent[i - 2] == (char)0x41 && tempWSCFileContent[i - 3] == (char)0x25)
					// %T500  25 54 35 30 30
					&& !(tempWSCFileContent[i - 1] == (char)0x30 && tempWSCFileContent[i - 2] == (char)0x30 && tempWSCFileContent[i - 3] == (char)0x35 && tempWSCFileContent[i - 4] == (char)0x54 && tempWSCFileContent[i - 5] == (char)0x25)
					// �� 81 76 00 49	
					&& !(tempWSCFileContent[i] == (char)0x00 && tempWSCFileContent[i + 1] == (char)0x49 && tempWSCFileContent[i - 1] == (char)0x76 && tempWSCFileContent[i - 2] == (char)0x81)
					// ������� �� 00 41 66 00
					&& !(tempWSCFileContent[i] == (char)0x00 && tempWSCFileContent[i + 1] == (char)0x41 && tempWSCFileContent[i + 2] == (char)0x66 && tempWSCFileContent[i + 3] == (char)0x00)
					// �������  8   01 38 00 00
					&& !(tempWSCFileContent[i - 2] == (char)0x01 && tempWSCFileContent[i - 1] == (char)0x38 && tempWSCFileContent[i] == (char)0x00 && tempWSCFileContent[i + 1] == (char)0x00)



					// �����ı���β������
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

			case 'b': // �ж���ѡ��Ľ�β
				{
					OutLen --; i --; // �ж�ѡ��ʱ���õ���i-1������

					unsigned int offset = 1;
					//��ѡ�ͷ��Ŀ��0x0001~0x01֮����è�壬����ֱ�ӹ�����
					while((unsigned char)tempWSCFileContent[ i - offset ] > (unsigned char)0x04) offset ++; // ���ص�ǰ���ҵ�����
					for( offset --; offset > 0; offset -- ) OutLen --; // �жϵ�ʱ���Ѿ���ѡ�����ݸ��ƹ�ȥ�ˣ�����ҪĨ��
					unsigned int index = 4; // �� >### �� ####
					string temp; getline( gFile, temp, '\n' );
					cout << endl << "[c." << temp << "]";
					while (index < temp.length()) {
						WSCFileContent_CHS[OutLen].srcChar = temp[index++];
						WSCFileContent_CHS[OutLen++].srcPos = 0;

						//WSCFileContent_CHS[OutLen++] = temp[index++]; // ���Ӹ��ƹ�ȥ
					}
					for (int k = 0; k < 10; k++) WSCFileContent_CHS[OutLen++] = srcchar[i++]; // ����ѡ��β���
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
	_01_CreateFolder( "temp" ); //������ʱ�ļ���
	_01_CreateFolder( OutputFolder );

	string FFFF;
	for( unsigned int i = 0; i < InputFolder.length( ); i ++ ) {
		if( InputFolder[ i ] == '\\' ) FFFF += '_';
		else FFFF += InputFolder[ i ];
	}
	FFFF = "temp\\" + FFFF + "_FileList.txt";
	_02_getFileList( InputFolder, FFFF );//�浽temp�ļ�����

	char *TempSave;//��ʱ�洢�ַ���
	TempSave = new char [ FFFF.length( ) + 1 ];//��ʱ�洢�ļ�·��
	for( UINT i = 0; i < FFFF.length( ); i ++ ) TempSave[ i ] = FFFF[ i ];
	TempSave[ FFFF.length( ) ] = '\0';
	
	char *FileNameHeader1 = new char [ InputFolder.length( ) + 2 ];//�ļ�������+'\\'
	for( UINT i = 0; i < InputFolder.length( ); i ++ ) FileNameHeader1[ i ] = InputFolder[ i ];
	FileNameHeader1[ InputFolder.length( ) ] = '\0';//��������ַ����и���β
	if( InputFolder[ InputFolder.length( ) - 1 ] != '\\' ) {
		FileNameHeader1[ InputFolder.length( ) ] = '\\';
		FileNameHeader1[ InputFolder.length( ) + 1 ] = '\0';
	}//�Ӹ���б��

	char *FileNameHeader = new char [ OutputFolder.length( ) + 2 ];//�ļ�������+'\\'
	for( UINT i = 0; i < OutputFolder.length( ); i ++ ) FileNameHeader[ i ] = OutputFolder[ i ];
	FileNameHeader[ OutputFolder.length( ) ] = '\0';//��������ַ����и���β
	if( OutputFolder[ OutputFolder.length( ) - 1 ] != '\\' ) {
		FileNameHeader[ OutputFolder.length( ) ] = '\\';
		FileNameHeader[ OutputFolder.length( ) + 1 ] = '\0';
	}//�Ӹ���б��
	
	fstream FileList; // �ļ��б�
	EasyUnicodeFileLE InFile, OutFile; // �����ļ�
	FileList.open( TempSave, ios_base::in ); //��֮��TempSave�Ϳ���ɾ����
	delete [ ] TempSave;

	TempSave = new char [ 20 ];//��ʱ�洢���������ļ���
	while( !FileList.eof( ) ) {
		FileList.getline( TempSave, 19, '\n' ); //�ӡ��ļ��б��ļ����ļ��ж�ȡ�ļ���
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
		wstring WordLine, bakwstr = L""; // Ϊ�˺������ظ�����
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
						CountStep = 0; // ԭ��
						break;
					case L'1':
						CountStep = 1; // ����
						break;
					case L'2':
						CountStep = 2; // У��
						break;
					case L'3':
						CountStep = 3; // ��ɫ
						break;
					case L'4':
						CountStep = 4; // ����
						break;
					default:
						if( !AddSign && CountStep != 0 ) {
							if( CountStep == 1 ) OutFile.writeln( L"//У���� >2��9999��[����]�������Ǹ��ǡ�����" );
							else if( CountStep == 2 ) OutFile.writeln( L"//��ɫ�� >3��9999��[����]�������Ǹ��ǡ�����" );
							else if( CountStep == 3 ) OutFile.writeln( L"//������ >4��9999��[����]�������Ǹ��ǡ�����" );
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
					if( CountStep == 1 ) { //OutFile.writeln( L"//У���� >2��9999��[����]�������Ǹ��ǡ�����" );
						Wtemp[ 1 ] = L'2';
						Wtemp[ 2 ] = Wtemp[ Wtemp[ 3 ] == L'ѡ' ? 6 : 7 ] = L'��';
					}
					else if( CountStep == 2 ) { //OutFile.writeln( L"//��ɫ�� >3��9999��[����]�������Ǹ��ǡ�����" );
						Wtemp[ 1 ] = L'3';
						Wtemp[ 2 ] = Wtemp[ Wtemp[ 3 ] == L'ѡ' ? 6 : 7 ] = L'��';
					}
					else if( CountStep == 3 ) { //OutFile.writeln( L"//������ >4��9999��[����]�������Ǹ��ǡ�����" );
						Wtemp[ 1 ] = L'4';
						Wtemp[ 2 ] = Wtemp[ Wtemp[ 3 ] == L'ѡ' ? 6 : 7 ] = L'��';
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

	_01_CreateFolder( "temp" ); //������ʱ�ļ���
	_01_CreateFolder( OutputFolder );

	string FFFF;
	for( unsigned int i = 0; i < InputFolder.length( ); i ++ ) {
		if( InputFolder[ i ] == '\\' ) FFFF += '_';
		else FFFF += InputFolder[ i ];
	}
	FFFF = "temp\\" + FFFF + "_FileList.txt";
	_02_getFileList( InputFolder, FFFF );//�浽temp�ļ�����

	char *TempSave;//��ʱ�洢�ַ���
	TempSave = new char [ FFFF.length( ) + 1 ];//��ʱ�洢�ļ�·��
	for( UINT i = 0; i < FFFF.length( ); i ++ ) TempSave[ i ] = FFFF[ i ];
	TempSave[ FFFF.length( ) ] = '\0';
	
	char *FileNameHeader1 = new char [ InputFolder.length( ) + 2 ];//�ļ�������+'\\'
	for( UINT i = 0; i < InputFolder.length( ); i ++ ) FileNameHeader1[ i ] = InputFolder[ i ];
	FileNameHeader1[ InputFolder.length( ) ] = '\0';//��������ַ����и���β
	if( InputFolder[ InputFolder.length( ) - 1 ] != '\\' ) {
		FileNameHeader1[ InputFolder.length( ) ] = '\\';
		FileNameHeader1[ InputFolder.length( ) + 1 ] = '\0';
	}//�Ӹ���б��

	char *FileNameHeader = new char [ OutputFolder.length( ) + 2 ];//�ļ�������+'\\'
	for( UINT i = 0; i < OutputFolder.length( ); i ++ ) FileNameHeader[ i ] = OutputFolder[ i ];
	FileNameHeader[ OutputFolder.length( ) ] = '\0';//��������ַ����и���β
	if( OutputFolder[ OutputFolder.length( ) - 1 ] != '\\' ) {
		FileNameHeader[ OutputFolder.length( ) ] = '\\';
		FileNameHeader[ OutputFolder.length( ) + 1 ] = '\0';
	}//�Ӹ���б��
	
	fstream FileList; // �ļ��б�
	EasyUnicodeFileLE InFile, OutFile, ReferFile; // �����ļ�
	FileList.open( TempSave, ios_base::in ); //��֮��TempSave�Ϳ���ɾ����
	delete [ ] TempSave;

	
	TempSave = new char [ 20 ];//��ʱ�洢���������ļ���
	while( !FileList.eof( ) ) {
		FileList.getline( TempSave, 19, '\n' ); //�ӡ��ļ��б��ļ����ļ��ж�ȡ�ļ���
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
		wstring WordLine; // Ϊ�˺������ظ�����

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
		OutFile.writeln(L"//ԭ���� >0��0001��[̫һ]�������ա�����");
		OutFile.writeln(L"//�ᴿ�� >1��0001��[̫һ]�������ա�����");
		OutFile.writeln(L"//�����ᴿ����ı��������뷴����imewx@qq.com");
		OutFile.writeln(L"");
		for (int i = 0; i < LineCount; i++) {
			// prevent access overflow
			cerr << "CurLine: " << i << endl;
			if (array[i].length() < 8) {
				OutFile.writeln(L"");
				continue;
			}

			// 012345678 - idx
			// >0��0001��[̫һ]�������ա�����
			// >1��0001��[̫һ]�������ա�����
			cerr << "1";
			cerr << "(" << TB.WstringToString(936,array[i]) << ")";
			if (array[i][1] == L'0') {
				// This is the original script
				int beg_scr = array[i][3] == L'ѡ' ? 7 : 8;
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
					//OutFile.writeln(L">0��" + wstring(tempLineNumber) + L"��" + WordLine); // output 1
					OutFile.writeln(ReferList[ReferCount++]); // new output 1
					WordLine = array[lastOkLine].substr(beg_scr, array[lastOkLine].length() - beg_scr);
					OutFile.writeln(L">1��" + wstring(tempLineNumber) + L"��" + WordLine); // output 2
					cerr << "-";
				}
				else {
					// This is selector
					cerr << "4";
					//OutFile.writeln(array[i]);
					OutFile.writeln(ReferList[ReferCount++]);
					array[lastOkLine][1] = L'1';
					array[lastOkLine][2] = array[lastOkLine][6] = L'��';
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
			
			// ע����
			if( Wtemp.length( ) < 2 || Wtemp[ 0 ] != L'/' && Wtemp[ 1 ] != L'/' ) HeaderSign = false;

			// ������
			if( HeaderSign ) { // �ļ�ע��ͷ
				switch( Wtemp[ 7 ] ) {
					case L'0': CountStep = 0; break; // ԭ��
					case L'1': CountStep = 1; break; // ����
					case L'2': CountStep = 2; break; // У��
					case L'3': CountStep = 3; break; // ��ɫ
					case L'4': CountStep = 4; break; // ����
					default:
						if( !AddSign && CountStep != 0 ) {
							OutFile.writeln( L"//������ >2��9999��[����]�������Ǹ��ǡ�����" );
							AddSign = true;
						}
						break;
				}
				if( Wtemp[ 7 ] != L'1' && Wtemp[ 7 ] != L'2' && Wtemp[ 7 ] != L'3' && Wtemp[ 7 ] != L'4' )
					OutFile.writeln( Wtemp ); // ���ԭ��
			} else { // ���Ĳ���
				if( Wtemp.length( ) < 2 ) { // ��ֹ����Խ��
					OutFile.writeln( L"" );
					continue;
				}
				
				// ���� junk bytes
				if( Wtemp[ 3 ] == L'ѡ' && Wtemp[ 8 ] == L'\x0001' ) {
					for( int i = 9; i < Wtemp.length( ); i ++ ) Wtemp[ i - 2 ] = Wtemp[ i ];
					Wtemp.erase( Wtemp.length( ) - 2 );
				}

				if( Wtemp[ 0 ] == L'/' && Wtemp[ 1 ] == L'/' || Wtemp[ 1 ] == L'0' )
					OutFile.writeln( Wtemp );
				else if( Wtemp[ 1 ] == TB.StringToWstring( 936, TB.IntToString( CountStep ) )[ 0 ] ) {
					Wtemp[ 1 ] = L'2';
					Wtemp[ 2 ] = Wtemp[ Wtemp[ 3 ] == L'ѡ' ? 6 : 7 ] = L'��';
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
	_02_getFileList(InputFolder, "temp\\" + FFFF + "_FileList.txt");//�浽temp�ļ�����

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

	_01_CreateFolder("temp"); //������ʱ�ļ���

	string FFFF;
	for (unsigned int i = 0; i < InputFolder.length(); i++) {
		if (InputFolder[i] == '\\') FFFF += '_';
		else FFFF += InputFolder[i];
	}
	FFFF = "temp\\" + FFFF + "_FileList.txt";
	_02_getFileList(InputFolder, FFFF);//�浽temp�ļ�����

	char *TempSave;//��ʱ�洢�ַ���
	TempSave = new char[FFFF.length() + 1];//��ʱ�洢�ļ�·��
	for (UINT i = 0; i < FFFF.length(); i++) TempSave[i] = FFFF[i];
	TempSave[FFFF.length()] = '\0';

	fstream FileList; // �ļ��б�
	EasyUnicodeFileLE InFile, OutFile, ReferFile; // �����ļ�
	FileList.open(TempSave, ios_base::in); //��֮��TempSave�Ϳ���ɾ����
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

				// ��� ת ȫ�ǣ�ȥ��{:}[]��%??
				// refer proc 4

				for (unsigned int k = 0; k < Wtemp.length(); k++) {
					/* ���������һЩ�ַ��滻 */
					switch (Wtemp[k]) {
					case L'\x30FB': Wtemp[k] = L'\x00B7'; break; // ʵ�ĵ� ver1
					case L'\xFF65': Wtemp[k] = L'\x00B7'; break; // ʵ�ĵ� ver2
					case L'\x266A': Wtemp[k] = L'\x2606'; break; // ���ַ��Ż�������
					case L'\x3000': Wtemp[k] = L'\x0020'; break; // ��ո񻻳�С�ո�
					case L'\x00E4': Wtemp[k] = L'\x0061'; break; // ����a����a
					case L'\x2020': Wtemp[k] = L'\x002B'; break; // ʮ�ּܻ���+��
					default: break;
					}
				} // �ַ��滻


				char tempContent[1024] = { '\0' };
				string str = TB.WstringToString(936, Wtemp);
				memset(tempContent, '\0', sizeof(tempContent));

				// ���תȫ��
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
	//����һ���ļ��У�����Ƕ��
	if( Name.length( ) > 160 ) {
		cout << "FolderName length cannot be larger than 160!" << endl;
	}
	else {
		char tempName[ 161 ], temp[ 161 ];//temp[ ]�������δ��Ƕ���ļ���
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
				if( _access( temp, 6 ) == -1 ) _mkdir( temp );//�ж����ļ����Ƿ���ڣ���Ȼ��һ������ʡ��
			}
			temp[ i ] = tempName[ i ];
		}
		temp[ Name.length( ) ] = '\0';
		_mkdir( temp );//����tempName����Ϊ����ȫ�����磺"123\123\"
	}
	return;
}

void CrossChannelCrack::_02_getFileList( string FolderName, string SaveTo )
{
	/* ��֧�������ļ������ļ��� */
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
		tempName[ i ] = SaveTo[ i ];//tempName���SaveTo��char*���ļ���
	}
	tempName[ SaveTo.length( ) ] = '\0';

	wchar_t Dir[ 161 ];
	wstring tmp = StringToWstring( 936, FolderName );
	for( UINT i = 0; i < FolderName.length( ); i ++ ) {
		Dir[ i ] = tmp[ i ];
	}
	Dir[ FolderName.length( ) ] = L'\0';

	fstream F;
	//Unicode�汾
	//F.open( tempName, ios_base::trunc | ios_base::out | ios_base::binary );
	//ANSI�汾
	F.open( tempName, ios_base::trunc | ios_base::out );
	if( !F.is_open( ) ) {
		cout << "#### Saving-to file open failed! ####" << endl;
		return;
	}
	//F.write( "\xFF\xFE", 2 );
	
	WIN32_FIND_DATA FindFileData;
	HANDLE hFind = INVALID_HANDLE_VALUE;
	wchar_t DirSpec[ MAX_PATH ]; //����Ҫ�������ļ��е�Ŀ¼
	//DWORD dwError;
	StringCchCopy( DirSpec, MAX_PATH, Dir );
	StringCchCat( DirSpec, MAX_PATH, TEXT( "\\*" ) ); //����Ҫ�������ļ��е�����·��\*

	hFind = FindFirstFile( DirSpec, &FindFileData ); //�ҵ��ļ����еĵ�һ���ļ�

	if( hFind == INVALID_HANDLE_VALUE ) { //���hFind�������ʧ�ܣ����������Ϣ
		FindClose( hFind );
		cout << "#### Handle creating failed! ####" << endl;
		return;
	}
	else {
		while( FindNextFile( hFind, &FindFileData ) != 0) { //���ļ������ļ��д���ʱ
			if( ( FindFileData.dwFileAttributes & FILE_ATTRIBUTE_DIRECTORY ) != 0
			&& wcscmp( FindFileData.cFileName, L"." ) == 0
			|| wcscmp( FindFileData.cFileName, L".." ) == 0 ) { //�ж����ļ���&&��ʾΪ"."||��ʾΪ"."
				continue;
			}
			if( ( FindFileData.dwFileAttributes & FILE_ATTRIBUTE_DIRECTORY ) != 0 ) { //�ж�������ļ���
				// do nothing
			}
			else if( ( FindFileData.dwFileAttributes & FILE_ATTRIBUTE_DIRECTORY ) == 0) { //��������ļ���
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
	/* ��֧�������ļ������ļ��� */
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
		tempName[ i ] = SaveTo[ i ];//tempName���SaveTo��char*���ļ���
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
	wchar_t DirSpec[ MAX_PATH ]; //����Ҫ�������ļ��е�Ŀ¼
	//DWORD dwError;
	StringCchCopy( DirSpec, MAX_PATH, Dir );
	StringCchCat( DirSpec, MAX_PATH, TEXT( "\\*" ) ); //����Ҫ�������ļ��е�����·��\*

	hFind = FindFirstFile( DirSpec, &FindFileData ); //�ҵ��ļ����еĵ�һ���ļ�

	if( hFind == INVALID_HANDLE_VALUE ) { //���hFind�������ʧ�ܣ����������Ϣ
		FindClose( hFind );
		cout << "#### Handle creating failed! ####" << endl;
		return;
	}
	else {
		while( FindNextFile( hFind, &FindFileData ) != 0) { //���ļ������ļ��д���ʱ
			if( ( FindFileData.dwFileAttributes & FILE_ATTRIBUTE_DIRECTORY ) != 0
			&& wcscmp( FindFileData.cFileName, L"." ) == 0
			|| wcscmp( FindFileData.cFileName, L".." ) == 0 ) { //�ж����ļ���&&��ʾΪ"."||��ʾΪ"."
				continue;
			}
			if( ( FindFileData.dwFileAttributes & FILE_ATTRIBUTE_DIRECTORY ) != 0 ) { //�ж�������ļ���
				// do nothing
			}
			else if( ( FindFileData.dwFileAttributes & FILE_ATTRIBUTE_DIRECTORY ) == 0) { //��������ļ���
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
	/* ��֧�������ļ������ļ��� */
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
		tempName[ i ] = SaveTo[ i ];//tempName���SaveTo��char*���ļ���
	}
	tempName[ SaveTo.length( ) ] = '\0';

	wchar_t Dir[ 161 ];
	wstring tmp = StringToWstring( 936, FolderName );
	for( UINT i = 0; i < FolderName.length( ); i ++ ) {
		Dir[ i ] = tmp[ i ];
	}
	Dir[ FolderName.length( ) ] = L'\0';

	fstream F;
	//Unicode�汾
	//F.open( tempName, ios_base::trunc | ios_base::out | ios_base::binary );
	//ANSI�汾
	F.open( tempName, ios_base::trunc | ios_base::out );
	if( !F.is_open( ) ) {
		cout << "#### Saving-to file open failed! ####" << endl;
		return;
	}
	//F.write( "\xFF\xFE", 2 );
	
	WIN32_FIND_DATA FindFileData;
	HANDLE hFind = INVALID_HANDLE_VALUE;
	wchar_t DirSpec[ MAX_PATH ]; //����Ҫ�������ļ��е�Ŀ¼
	//DWORD dwError;
	StringCchCopy( DirSpec, MAX_PATH, Dir );
	StringCchCat( DirSpec, MAX_PATH, TEXT( "\\*" ) ); //����Ҫ�������ļ��е�����·��\*

	hFind = FindFirstFile( DirSpec, &FindFileData ); //�ҵ��ļ����еĵ�һ���ļ�

	if( hFind == INVALID_HANDLE_VALUE ) { //���hFind�������ʧ�ܣ����������Ϣ
		FindClose( hFind );
		cout << "#### Handle creating failed! ####" << endl;
		return;
	}
	else {
		while( FindNextFile( hFind, &FindFileData ) != 0) { //���ļ������ļ��д���ʱ
			if( ( FindFileData.dwFileAttributes & FILE_ATTRIBUTE_DIRECTORY ) != 0
			&& wcscmp( FindFileData.cFileName, L"." ) == 0
			|| wcscmp( FindFileData.cFileName, L".." ) == 0 ) { //�ж����ļ���&&��ʾΪ"."||��ʾΪ"."
				continue;
			}
			if( ( FindFileData.dwFileAttributes & FILE_ATTRIBUTE_DIRECTORY ) != 0 ) { //�ж�������ļ���
				
				wchar_t DirAdd[MAX_PATH];
				StringCchCopy(DirAdd,MAX_PATH,Dir);
				StringCchCat(DirAdd,MAX_PATH,TEXT("\\"));  
				StringCchCat(DirAdd,MAX_PATH,FindFileData.cFileName); //ƴ�ӵõ����ļ��е�����·��
				F << WstringToString( 936, DirAdd ) << endl;
			}
			else if( ( FindFileData.dwFileAttributes & FILE_ATTRIBUTE_DIRECTORY ) == 0) { //��������ļ���
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

	/*���ǿ��ַ���*/
	char *szAnsi = new char [ str.length( ) + 1 ];
	for ( UINT i = 0; i < str.length( ); i ++ ) {
		szAnsi[ i ] = str[ i ];
	}
	szAnsi[ str.length( ) ] = '\0';
			
	//setlocale( LC_ALL, "jpn" );
	//setlocale( LC_ALL, "chs" );
	//Ԥת�����õ�����ռ�Ĵ�С
	int wcsLen = ::MultiByteToWideChar( LocalOption, NULL, szAnsi, strlen(szAnsi), NULL, 0);

	//����ռ�Ҫ��'\0'�����ռ䣬MultiByteToWideChar�����'\0'�ռ�
	wchar_t *wszString = new wchar_t [ wcsLen + 1 ];
	::MultiByteToWideChar( LocalOption, NULL, szAnsi, strlen( szAnsi ), wszString, wcsLen) ; //������'\0' 
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
	//Ԥת�����õ�����ռ�Ĵ�С
	UINT strLen = ::WideCharToMultiByte( LocalOption, NULL, wszString, -1, NULL, 0, NULL, NULL );
	//����ռ䲻Ҫ��'\0'�����ռ䣬WideCharToMultiByte���'\0'�ռ�
	char *szAnsi = new char [ strLen ];
	::WideCharToMultiByte( LocalOption, NULL, wszString, -1, szAnsi, strLen, NULL, NULL );
	szAnsi[ strLen - 1 ] = '\0';

	string str = szAnsi;

	delete [ ] szAnsi;
	delete [ ] wszString;

	/*У��ת���Ƿ�����*/
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

unsigned long CrossChannelCrack::unwipf( unsigned char* buff,      // �����ļ����ĵ�array
										 unsigned long  len,       // �����ļ�����
										 unsigned char* out_buff,  // ����ļ����ĵ�array
										 unsigned long  out_len )  // ����ļ�����
{
	unsigned long  ring_len   = 4096;                        // Ѱַ��Χ����0-4095
	unsigned char* ring       = new unsigned char[ring_len]; // ������
//	unsigned long ring_index  = 0xFEE;                       // �����������
	unsigned long  ring_index = 1;                           // �����������
	unsigned char* end        = buff + len;                  // ָ������array��ĩβ
	unsigned char* out_end    = out_buff + out_len;          // ָ�����array��ĩβ

	memset(ring, 0, ring_len); // ������ ����

	while (buff < end && out_buff < out_end) { // �ж�������������array��ĩβ
		unsigned char flags = *buff++; //<1> ȡ��ǰ�ַ��浽flags����
	
		// ���ѭ�����ж�8λ��char�͵�ÿһλ�Ƿ�Ϊ1
		for (int i = 0; i < 8 && buff < end && out_buff < out_end; i++) { // �ж�������char�ͳ���8ѭ��&&������array��ĩβ
			if (flags & 0x01) { // �жϣ����λ�Ƿ�Ϊ1
			/*
			*out_buff = ring[ring_index % ring_len] = *buff++; // ��ring[ 1 ]��ʼ��ֵ��[ 0 ]����4096ѭ��
			ring_index++;
			*out_buff++;
			*/
		    *out_buff++ = ring[ring_index++ % ring_len] = *buff++; //<2>
			} else {
				if (end - buff < 2) break;
		
				unsigned long p = *buff++; //<3>
				unsigned long n = *buff++; //<4>
		
				//p = p | ( ( n >> 4 ) << 8 );
				p = (p << 4) | (n >> 4);   // ( RHL p, 4 ) OR ( RHR n, 4 ) �� p�İ�λ �� n��ǰ��λ ����
				n = (n & 0x0F) + 2;        // AND 00001111b; ADD 2 �����õ�����n�ĺ���λ
		
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

			flags >>= 1; // ����1λ��������һ���ж�
		}
	}
	
	delete [] ring;

	return out_len - (out_end - out_buff); // ���Ե����ַ�����
}

void CrossChannelCrack::wipf_fake( unsigned char  *buff,       // �����ļ����ĵ�array
								   unsigned long   len,        // ���ĵĳ���
								   unsigned char **out_buff,  // ����ļ�������array (ָ��ָ���ָ��)
								   unsigned long  *out_len )   // ����ļ�����
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
