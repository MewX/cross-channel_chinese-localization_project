========================================================================
    控制台应用程序：CrossChannel_Program 项目概述
========================================================================

应用程序向导已为您创建了此 CrossChannel_Program 应用程序。

本文件概要介绍组成 CrossChannel_Program 应用程序的每个文件的内容。


CrossChannel_Program.vcxproj
    这是使用应用程序向导生成的 VC++ 项目的主项目文件，其中包含生成该文件的 Visual C++ 的版本信息，以及有关使用应用程序向导选择的平台、配置和项目功能的信息。

CrossChannel_Program.vcxproj.filters
    这是使用“应用程序向导”生成的 VC++ 项目筛选器文件。它包含有关项目文件与筛选器之间的关联信息。在 IDE 中，通过这种关联，在特定节点下以分组形式显示具有相似扩展名的文件。例如，“.cpp”文件与“源文件”筛选器关联。

CrossChannel_Program.cpp
    这是主应用程序源文件。

/////////////////////////////////////////////////////////////////////////////
其他标准文件:

StdAfx.h, StdAfx.cpp
    这些文件用于生成名为 CrossChannel_Program.pch 的预编译头 (PCH) 文件和名为 StdAfx.obj 的预编译类型文件。

/////////////////////////////////////////////////////////////////////////////
其他注释:

应用程序向导使用“TODO:”注释来指示应添加或自定义的源代码部分。

/////////////////////////////////////////////////////////////////////////////

if( FileHeader[ 0 ] == '\x01' ) { //Header: 0x01000000 （可以直接提取的）
		/**************************/
		/*Bgm.arc; Se.arc; Rio.arc*/
		/**************************/
		InFile.read( FileSuffix, 4 );
		FileSuffix[ 4 ] = '\0';//读取文件扩展名，后面创建文件的时候要用到。

		InFile.read( tempLittleEndian, 4 );
		tempLittleEndian[ 4 ] = '\0';//存放文件数
		FileNumbers = LittleEndianCharsToValue_s( 4, tempLittleEndian );//存入文件数

		TempSave = new char [ 5 ];
		InFile.read( TempSave, 4 );
		if( TempSave[ 0 ] != '\x10' && TempSave[ 1 ] != '\x00' && TempSave[ 2 ] != '\x00' && TempSave[ 3 ] != '\x00' ) {
			cout << "#### Unexpected file header! ####" << endl;
			delete [ ] TempSave;
			return;
		}//二次校验文件头
		delete [ ] TempSave;

		FileArchive *File = new FileArchive [ (unsigned int)FileNumbers ];//生成数据结构组

		for( unsigned __int64 i = 0; i < FileNumbers; i ++ ) {
			InFile.read( File[ i ].Name, 13 );
			File[ i ].Name[ 13 ] = '\0';
			//cout << "     >> File[ " << i << " ].Name = " << File[ i ].Name << endl;

			InFile.read( tempLittleEndian, 4 );
			tempLittleEndian[ 4 ] = '\0';
			File[ i ].Size = LittleEndianCharsToValue_s( 4, tempLittleEndian );//获取文件大小
			//cout << "     >> File[ " << i << " ].Size = " << File[ i ].Size << endl;

			InFile.read( tempLittleEndian, 4 );
			tempLittleEndian[ 4 ] = '\0';
			File[ i ].Offset = LittleEndianCharsToValue_s( 4, tempLittleEndian );//获取文件开始位置的偏址
			//cout << "     >> File[ " << i << " ].Offset = " << File[ i ].Offset << endl;
			//system( "PAUSE" );
		}//把文件索引的内容存到内存

		for( unsigned __int64 i = 0; i < FileNumbers; i ++ ) {
			UINT a = OutputFolder.length( ) + strlen( File[ i ].Name ) + 1 + 4 + 1;//数组长度（文件夹+文件名+点+扩展名+'\0'）
			char *ttt = new char [ a ];
			strcpy_s( ttt, a, FolderName );//先复制文件夹名
			strcat_s( ttt, a, File[ i ].Name );//再复制文件名
			strcat_s( ttt, a, "." );//接着复制'.'
			strcat_s( ttt, a, FileSuffix );//最后复制扩展名
			cout << "     -> Extracting " << ttt << " ..." << endl;
			OutFile.open( ttt, ios_base::out | ios_base::binary | ios_base::trunc );
			delete [ ] ttt;

			InFile.seekg( File[ i ].Offset, ios_base::beg );
			TempSave = new char [ (unsigned int)File[ i ].Size + 1 ];
			InFile.read( TempSave, File[ i ].Size );
			TempSave[ File[ i ].Size ] = '\0';
			OutFile.write( TempSave, File[ i ].Size );
			delete [ ] TempSave;

			OutFile.close( );
		}//操作文件，注意区分是否要反转

		cout << "  >> Total: " <<FileNumbers << " file(s)." << endl;

		InFile.close( );
		delete [ ] File;
	}
	else if( FileHeader[ 0 ] == '\x02' ) { //Header: 0x02000000
		/************************************************************/
		/*Chip_B.arc; Chip_E.arc; Chip_I.arc; Chip_S.arc; Chip_T.arc*/
		/************************************************************/

		InFile.read( tempLittleEndian, 4 );//先过掉MSK头标记
		InFile.read( tempLittleEndian, 4 );//再过掉大的文件数标记

		TempSave = new char [ 5 ];
		InFile.read( TempSave, 4 );
		if( TempSave[ 0 ] != '\x1C' && TempSave[ 1 ] != '\x00' && TempSave[ 2 ] != '\x00' && TempSave[ 3 ] != '\x00' ) {
			cout << "#### Unexpected file header! ####" << endl;
			delete [ ] TempSave;
			return;
		}//二次校验文件头
		delete [ ] TempSave;

		InFile.read( FileSuffix, 4 );
		FileSuffix[ 4 ] = '\0';//读取文件扩展名，后面创建文件的时候要用到。

		InFile.read( tempLittleEndian, 4 );//LittleEndian
		tempLittleEndian[ 4 ] = '\0';//存放文件数
		FileNumbers = LittleEndianCharsToValue_s( 4, tempLittleEndian );//存入文件数
		
		InFile.read( tempLittleEndian, 4 );//LittleEndian
		tempLittleEndian[ 4 ] = '\0';//存放二级偏址
		InFile.seekg( LittleEndianCharsToValue_s( 4, tempLittleEndian ), ios_base::beg );//以文件头为基准，开始读取正文

		FileArchive *File = new FileArchive [ (unsigned int)FileNumbers ];//生成数据结构组

		for( unsigned __int64 i = 0; i < FileNumbers; i ++ ) {
			InFile.read( File[ i ].Name, 13 );
			File[ i ].Name[ 13 ] = '\0';
			//cout << "     >> File[ " << i << " ].Name = " << File[ i ].Name << endl;

			InFile.read( tempLittleEndian, 4 );
			tempLittleEndian[ 4 ] = '\0';
			File[ i ].Size = LittleEndianCharsToValue_s( 4, tempLittleEndian );//获取文件大小
			//cout << "     >> File[ " << i << " ].Size = " << File[ i ].Size << endl;

			InFile.read( tempLittleEndian, 4 );
			tempLittleEndian[ 4 ] = '\0';
			File[ i ].Offset = LittleEndianCharsToValue_s( 4, tempLittleEndian );//获取文件开始位置的偏址
			//cout << "     >> File[ " << i << " ].Offset = " << File[ i ].Offset << endl;
			//system( "PAUSE" );
		}//把文件索引的内容存到内存

		for( unsigned __int64 i = 0; i < FileNumbers; i ++ ) {
			UINT a = OutputFolder.length( ) + strlen( File[ i ].Name ) + 1 + 4 + 1;//数组长度（文件夹+文件名+点+扩展名+'\0'）
			char *ttt = new char [ a ];
			strcpy_s( ttt, a, FolderName );//先复制文件夹名
			strcat_s( ttt, a, File[ i ].Name );//再复制文件名
			strcat_s( ttt, a, "." );//接着复制'.'
			strcat_s( ttt, a, FileSuffix );//最后复制扩展名
			cout << "     -> Extracting " << ttt << " ..." << endl;
			OutFile.open( ttt, ios_base::out | ios_base::binary | ios_base::trunc );
			delete [ ] ttt;

			InFile.seekg( File[ i ].Offset, ios_base::beg );
			TempSave = new char [ (unsigned int)File[ i ].Size + 1 ];
			InFile.read( TempSave, File[ i ].Size );
			TempSave[ File[ i ].Size ] = '\0';
			OutFile.write( TempSave, File[ i ].Size );
			delete [ ] TempSave;

			OutFile.close( );
		}//操作文件，注意区分是否要反转

		cout << "  >> Total: " <<FileNumbers << " file(s)." << endl;

		InFile.close( );
		delete [ ] File;
	}
	else if( FileHeader[ 0 ] == '\x03' ) { //Header: 0x03000000
		/************/
		/*Effect.arc*/
		/************/
	}
	else if( FileHeader[ 0 ] == '\x07' ) { //Header: 0x07000000 
		/**********/
		/*Chip.arc*/
		/**********/
	}