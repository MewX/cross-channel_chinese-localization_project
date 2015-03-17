// dllmain.cpp : 定义 DLL 应用程序的入口点。
#include "stdafx.h"

// Redirectors
#pragma comment(linker, "/EXPORT:RegCloseKey=_HegCloseKey@4")
#pragma comment(linker, "/EXPORT:RegCreateKeyExA=_HegCreateKeyExA@36")
#pragma comment(linker, "/EXPORT:RegOpenKeyExA=_HegOpenKeyExA@20")
#pragma comment(linker, "/EXPORT:RegQueryValueExA=_HegQueryValueExA@24")
#pragma comment(linker, "/EXPORT:RegSetValueExA=_HegSetValueExA@24")

static HWND LoadWnd;
static HANDLE hThreadAnime, hThreadPatch, hThreadMonitor;
static int nTime;
static HINSTANCE hInst_bak;
static LONG nOldStyle;

STARTUPINFOA si_monitor;
PROCESS_INFORMATION pi_monitor;

// consts
const wchar_t *COMMON_DLG_TITLE = L"汉化补丁提示";

BOOL CALLBACK DlgProc( HWND hDlg, UINT message, WPARAM wParam, LPARAM lParam );
DWORD WINAPI ProcessThreadProc( PVOID pvParam );
DWORD WINAPI AnimeThreadProc( PVOID pvParam );
DWORD WINAPI MonitorThreadProc( PVOID pvParam );

#ifdef DEBUG
void HelloWorld( char* str )
{
    MessageBoxA(0, str, "Hijacked Successfully!\n", MB_ICONINFORMATION);
}
#endif


/********************
 * Main 
 ********************/
BOOL APIENTRY DllMain ( HINSTANCE hInst     /* Library instance handle. */ ,
                        DWORD reason        /* Reason this function is being called. */ ,
                        LPVOID reserved     /* Not used. */ )
{
    switch (reason)
    {
		static int nRet;
		static LPDWORD lpThreadID;

	case DLL_PROCESS_ATTACH:

		///* Show a process bar window */
		//LoadWnd = CreateDialogA( hInst, MAKEINTRESOURCE( IDD_FORMVIEW ), NULL,(DLGPROC)DlgProc );
		//nOldStyle = GetWindowLongA( LoadWnd, GWL_STYLE );
		//SetWindowLongA( LoadWnd, GWL_STYLE, nOldStyle & ~WS_CAPTION );
		//ShowWindow( LoadWnd, SW_SHOW );
		///nRet = DialogBoxParamA( hInst, MAKEINTRESOURCE( IDD_FORMVIEW ), NULL, DlgProc, 0 );
		////DialogBoxParamA( hInst, MAKEINTRESOURCE( IDD_FORMVIEW ), NULL, DlgProc, 0 );
		//MessageBoxA(0, "请等待初始化完成！\n", "MewCatcher", MB_ICONINFORMATION);

		//system( "pause" );

#ifdef DEBUG
		LoopCount = 0;
#endif
		// Initialize var
		nTime = 0;
		hInst_bak = hInst;
		
		// create save directory
		WinExec( "cmd /c mkdir saves_chs", SW_HIDE ); // 1st
		CreateDirectoryW( L"saves_chs", NULL );       // 2nd
		_wmkdir( L"saves_chs" );                      // 3rd

		// 要考虑到文件不存在的处理方法
		fopen_s( &FakeReg, "RegFile.chs", "rb+" );
		if( FakeReg == NULL ) {
			fopen_s( &FakeReg, "RegFile.chs", "wb+" );

		INITIALIZEREG:
			// Init structure vars
			Reg.Adapter = 0x00000000;
			Reg.DisplayMode_Window = 0x00000000;
			Reg.Size_Full_Width = 0x00000500;
			Reg.Size_Full_Height = 0x00000320;
			Reg.Size_Window_Width = 0x00000320;
			Reg.Size_Window_Height = 0x00000258;
			Reg.FullScreen = 0x00000000;
			Reg.BackBuffer_Width = 0x00000400;
			Reg.BackBuffer_Height = 0x00000400;
			Reg.KeepAspectRatio = 0x00000000;
			Reg.VSync = 0x00000001;
			Reg.UnDivideTexture = 0x00000000;
			Reg.DisableDialog = 0x00000000;
			Reg.UseCV = 0x00000000;
			Reg.JoyPad = 0x00000000;

			memcpy_s( Reg.InstallType, 4, "\x02\x00\x00\x00", 4 );
			//Reg.InstallDir[ 260 ],
			memcpy_s( Reg.InstallSrc, 260, "A:\\", 4 );
			memcpy_s( Reg.FontName, 1024, "黑体", 5 );
			memcpy_s( Reg.SpecialFontName, 1024, "黑体", 5 );
			memcpy_s( Reg.AutoMsg, 4, "\x07\x00\x00\x00", 4 );
			memcpy_s( Reg.AutoSkip, 4, "\x00\x00\x00\x00", 4 );
			memcpy_s( Reg.CursorHide, 4, "\x00\x00\x00\x00", 4 );
			memcpy_s( Reg.CursorTime, 4, "\x00\x00\x00\x00", 4 ); // OTOMEGA
			memcpy_s( Reg.D3D_DisableTnL, 4, "\x00\x00\x00\x00", 4 );
			memcpy_s( Reg.D3D_Tex16, 4, "\x00\x00\x00\x00", 4 );
			memcpy_s( Reg.DeactivePlay, 4, "\x01\x00\x00\x00", 4 );
			memcpy_s( Reg.Dialog, 4, "\x01\x00\x00\x00", 4 );
			memcpy_s( Reg.DisableCursor, 4, "\x00\x00\x00\x00", 4 );
			memcpy_s( Reg.DisablePan, 4, "\x00\x00\x00\x00", 4 );
			memcpy_s( Reg.DisableQuick, 4, "\x00\x00\x00\x00", 4 );
			memcpy_s( Reg.DisplayMode, 4, "\x00\x00\x00\x00", 4 );
			memcpy_s( Reg.EffectSkip, 4, "\x00\x00\x00\x00", 4 );
			memcpy_s( Reg.FontEdge, 4, "\x00\x00\x00\x00", 4 );
			memcpy_s( Reg.LogAlpha, 4, "\x09\x00\x00\x00", 4 ); // OTOMEGA
			memcpy_s( Reg.MsgAlpha, 4, "\x07\x00\x00\x00", 4 );
			memcpy_s( Reg.MsgPos, 8, "\x01\x00\x00\x00\xa0\x01\x00\x00", 8 );
			memcpy_s( Reg.MsgSpeed, 4, "\x02\x00\x00\x00", 4 );
			//memcpy_s( Reg.Mute, 96, "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00", 96 );
			memcpy_s( Reg.Mute, 84, "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00", 84 );
			memcpy_s( Reg.RButtonMode, 4, "\x00\x00\x00\x00", 4 );
			memcpy_s( Reg.SelAuto, 4, "\x00\x00\x00\x00", 4 );
			memcpy_s( Reg.SelSkip, 4, "\x00\x00\x00\x00", 4 );
			memcpy_s( Reg.SimpleWindow, 4, "\x00\x00\x00\x00", 4 );
			memcpy_s( Reg.SkipIcon, 4, "\x01\x00\x00\x00", 4 );
			memcpy_s( Reg.SkipType, 4, "\x01\x00\x00\x00", 4 );
			memcpy_s( Reg.SysVoice, 4, "\x00\x00\x00\x00", 4 );
			memcpy_s( Reg.TextColor, 4, "\x01\x00\x00\x00", 4 ); // OTOMEGA
			memcpy_s( Reg.UseDefaultFont, 4, "\x00\x00\x00\x00", 4 );
			memcpy_s( Reg.UseFilt, 4, "\x00\x00\x00\x00", 4 );
			memcpy_s( Reg.VoiceSkip, 4, "\x00\x00\x00\x00", 4 );
			//memcpy_s( Reg.Volume, 96, "\x58\x02\x00\x00\xe8\x03\x00\x00\xf4\x01\x00\x00\xe8\x03\x00\x00\xe8\x03\x00\x00\x20\x03\x00\x00\x20\x03\x00\x00\x20\x03\x00\x00\x20\x03\x00\x00\x20\x03\x00\x00\x20\x03\x00\x00\x20\x03\x00\x00\x20\x03\x00\x00\x20\x03\x00\x00\x20\x03\x00\x00\x20\x03\x00\x00\x20\x03\x00\x00\x20\x03\x00\x00\x20\x03\x00\x00\x20\x03\x00\x00\x20\x03\x00\x00\x20\x03\x00\x00\x20\x03\x00\x00\x20\x03\x00\x00", 96 );
			memcpy_s( Reg.Volume, 84, "\xe8\x03\x00\x00\xe8\x03\x00\x00\xe8\x03\x00\x00\xe8\x03\x00\x00\xe8\x03\x00\x00\xe8\x03\x00\x00\xe8\x03\x00\x00\xe8\x03\x00\x00\xe8\x03\x00\x00\xe8\x03\x00\x00\xe8\x03\x00\x00\xe8\x03\x00\x00\xe8\x03\x00\x00\xe8\x03\x00\x00\xe8\x03\x00\x00\xe8\x03\x00\x00\xe8\x03\x00\x00\xe8\x03\x00\x00\x58\x02\x00\x00\xe8\x03\x00\x00\xe8\x03\x00\x00", 84 );
			memcpy_s( Reg.WndPos, 8, "\x91\x00\x00\x00\x39\x00\x00\x00", 8 );


			if( FakeReg == NULL ) {
				MessageBoxW(0, L"RegFile.chs文件被占用！\r\n请关闭相关软件哦~", COMMON_DLG_TITLE, MB_ICONINFORMATION);
				ExitProcess( 0x02 );
			}
			fwrite( &Reg, sizeof( RegCC ), 1, FakeReg );
		}
		else { // 读文件初始化
			fseek( FakeReg, 0, SEEK_SET );
			fseek( FakeReg, 0, SEEK_END );
			if( ftell( FakeReg ) != sizeof( RegCC ) ) goto INITIALIZEREG;
			fseek( FakeReg, 0, SEEK_SET );
			fread( &Reg, sizeof( RegCC ), 1, FakeReg );
		}
		fclose( FakeReg );

		// 修改当前目录地址
		GetCurrentDirectoryA( 260, Reg.InstallDir );
		for( i = 0; ; i ++ ) {
			if( !Reg.InstallDir[ i ] ) break;
			if( Reg.InstallDir[ i ] == '?' ) {
				MessageBoxW(0, L"WillPlus的本引擎不支持文件目录中含有非当前系统语言字符哦亲！~"
					L"请自己把文件目录改一下呗！~\n", COMMON_DLG_TITLE, MB_ICONINFORMATION);
				ExitProcess( 0x03 );
			}
		}

#ifdef DEBUG
		fopen_s( &LogFile, "Reg.log", "w+" );
#endif
        break;

    case DLL_PROCESS_DETACH:
	RETRY_SAVE_SETTINGS:
		fopen_s( &FakeReg, "RegFile.chs", "wb+" );
		if( FakeReg == NULL ) {
			MessageBoxW(0, L"RegFile.chs文件被占用，无法保存设置，点击OK重试！", COMMON_DLG_TITLE, MB_ICONINFORMATION);
			clearerr( FakeReg );
			goto RETRY_SAVE_SETTINGS;
		}
		fseek( FakeReg, 0, SEEK_SET );
		fwrite( &Reg, sizeof( RegCC ), 1, FakeReg );
		fclose( FakeReg );
#ifdef DEBUG
		fclose( LogFile );
#endif
		// End process
		TerminateProcess( pi_monitor.hProcess, 0 );
        break;

    case DLL_THREAD_ATTACH:
        break;

	case DLL_THREAD_DETACH:
        break;
    }

    /* Returns TRUE on success, FALSE on failure */
    return TRUE;
}


/********************
 * Procs 
 ********************/
typedef struct {
	bool isLocked;
	IplImage *src;
	CvvImage cimg;
	RECT r;
	HWND h;

	char text[ 1024 ];
	int progress;
} ImgInfo;

/* Dialog Thread */
BOOL CALLBACK DlgProc( HWND hDlg, UINT message, WPARAM wParam, LPARAM lParam )
{
	static LPDWORD lpThreadID;
	const static RECT AnimeRect = { 0, 0, 400, 250 }; // 264, 150 ?
	static ImgInfo II;

	switch(message) {
    case WM_INITDIALOG:
		II.isLocked = false;
		II.src = cvLoadImage( "imgs\\white.jpg" );
		(II.cimg).CopyOf( II.src ); // copy img
		II.r = AnimeRect;
		II.h = hDlg;
		sprintf_s( II.text, 1024, "Preparing game..." );
		
		//MessageBoxA(0, "WM_INITDIALOG!\n", "MewCatcher", MB_ICONINFORMATION);
		int ScreenWidth, ScreenHeight;
		ScreenWidth = GetSystemMetrics( SM_CXSCREEN );
		ScreenHeight = GetSystemMetrics( SM_CYSCREEN );
		SetWindowPos( hDlg, HWND_TOPMOST, ( ScreenWidth - WINDOW_WIDTH ) / 2, ( ScreenHeight - WINDOW_HEIGHT ) / 2,
			WINDOW_WIDTH, WINDOW_HEIGHT, SWP_SHOWWINDOW); // Set to centre screen
		
		/* 创建一个线程来处理初始化工作 */
		hThreadAnime = CreateThread( NULL, 100, AnimeThreadProc, /*参数&rc*/ &II, 0, lpThreadID );
		hThreadPatch = CreateThread( NULL, 100, ProcessThreadProc, /*参数&rc*/ &II, 0, lpThreadID );
		hThreadMonitor = CreateThread( NULL, 100, MonitorThreadProc, /*参数&rc*/ &II, 0, lpThreadID );
		break;

	case WM_CTLCOLORSTATIC: /* 改变StaticText的背景颜色 */
		SetTextColor( (HDC)wParam, RGB( 21, 125, 240 ) ); //RGB( 0, 0, 0 ) );
		SetBkMode( (HDC)wParam, TRANSPARENT );
		return (LRESULT)GetStockObject(NULL_BRUSH);

	case WM_LBUTTONDOWN:
		SendMessage( hDlg, WM_NCLBUTTONDOWN, HTCAPTION, 0 );
		break;

	case WM_SYSCOMMAND:
		if( wParam == SC_CLOSE ) return TRUE;
		break;

	case WM_PAINT:{
		if( II.isLocked == false ) II.isLocked = true;
		else break;
		HDC hdc = GetDC( GetDlgItem( hDlg, IDC_ANIME ) );
		II.cimg.DrawToHDC( hdc, &(II.r) );
		ReleaseDC( GetDlgItem( hDlg, IDC_ANIME ), hdc );
		II.isLocked = false;}
		break;

    case WM_CLOSE:
		DestroyWindow( hDlg );
		cvReleaseImage( &(II.src) );
		LoadWnd = NULL;
		return TRUE;

    }

    return FALSE;
}

/* Background Process Thread */
DWORD WINAPI ProcessThreadProc( PVOID pvParam )
{
	// Wait op anime
	Sleep( 20 * 30 );

	////////////////////////////////////////////////////////////////////////////////
	// Here get the file size to judge whether reinit
	////////////////////////////////////////////////////////////////////////////////
PATCH_TEST:
#ifdef CHECKARC
	FILE *f_test;
	int size;

	int size_E, size_S, size_T;
	
	// patch
	f_test = fopen( "UninstallChs.exe", "rb" );
	if( f_test == NULL ) {
		if( MessageBoxW( ((ImgInfo *)pvParam)->h, L"玩家的错误: 我找不到UninstallChs.exe了。\r\n是否转到我们汉化版的官方网站重新下载？\r\n(http://www.crosschannel.cn)",
			COMMON_DLG_TITLE, MB_OKCANCEL) == IDOK) ShellExecuteA(NULL, "open", "http://www.crosschannel.cn", NULL, NULL, SW_SHOWNORMAL);
		ExitProcess( 0 );
	}
	fclose( f_test );

	// list file
	f_test = fopen( "size_list.lst", "r" );
	if( f_test == NULL ) {
		MessageBoxW(((ImgInfo *)pvParam)->h, L"内部错误: 找不到size_list.lst文件", COMMON_DLG_TITLE, MB_OK);
		ExitProcess( 0 );
	}
	fscanf( f_test, "%d%d%d", &size_E, &size_S, &size_T ); // read file size
	fclose( f_test );

	// chs
	f_test = fopen( "Chip_E.chs", "rb" );
	if( f_test == NULL ) goto CHECK_ARC;
	fseek( f_test, 0, SEEK_END );
	size = ftell( f_test );
	fclose( f_test );
	if( size != size_E ) goto CHECK_ARC;
	
	f_test = fopen( "Chip_S.chs", "rb" );
	if( f_test == NULL ) goto CHECK_ARC;
	fseek( f_test, 0, SEEK_END );
	size = ftell( f_test );
	fclose( f_test );
	if( size != size_S ) goto CHECK_ARC;
	
	f_test = fopen( "Chip_T.chs", "rb" );
	if( f_test == NULL ) goto CHECK_ARC;
	fseek( f_test, 0, SEEK_END );
	size = ftell( f_test );
	fclose( f_test );
	if( size != size_T ) goto CHECK_ARC;

	goto DONT_NEED_PATCH;

CHECK_ARC:
	// arc
	f_test = fopen( "Chip_E.arc", "rb" );
	if( f_test == NULL ) goto CHIP_E_FAIL;
	fseek( f_test, 0, SEEK_END );
	size = ftell( f_test );
	fclose( f_test );
	if( size != 4308759 ) {
	CHIP_E_FAIL:
		MessageBoxW(((ImgInfo *)pvParam)->h, L"Chip_E.arc校验失败，请重新尝试！", COMMON_DLG_TITLE, MB_OK);
		ExitProcess( 0 );
	}
	
	f_test = fopen( "Chip_S.arc", "rb" );
	if( f_test == NULL ) goto CHIP_S_FAIL;
	fseek( f_test, 0, SEEK_END );
	size = ftell( f_test );
	fclose( f_test );
	if( size != 9527598 ) {
	CHIP_S_FAIL:
		MessageBoxW(((ImgInfo *)pvParam)->h, L"Chip_S.arc校验失败，请重新尝试！", COMMON_DLG_TITLE, MB_OK);
		ExitProcess( 0 );
	}
	
	f_test = fopen( "Chip_T.arc", "rb" );
	if( f_test == NULL ) goto CHIP_T_FAIL;
	fseek( f_test, 0, SEEK_END );
	size = ftell( f_test );
	fclose( f_test );
	if( size != 85043007 ) {
	CHIP_T_FAIL:
		MessageBoxW(((ImgInfo *)pvParam)->h, L"Chip_T.arc校验失败，请重新尝试！", COMMON_DLG_TITLE, MB_OK);
		ExitProcess( 0 );
	}

	goto NEED_PATCH;

#endif

	////////////////////////////////////////////////////////////////////////////////
	// Patch
	////////////////////////////////////////////////////////////////////////////////
NEED_PATCH:
	if( MessageBoxW( ((ImgInfo *)pvParam)->h, L"咱检测到您的汉化补丁未初始化或进行不完整，\r\n即将进行自动初始化，是否开始？\r\n"
		L"（注：本补丁绿色无污染，且完美免注册表）\r\n（请预留100M以上硬盘空间哦，亲~）", COMMON_DLG_TITLE, MB_OKCANCEL) == IDCANCEL) ExitProcess(0);


	// Chip_E.arc (0%-10%)
	{
		int FileCount = 0, i, SectId, EntryId;
		char *FileDetail;
		FILE *f_arc, *f_chs, *f_in;
		ARCHDR ArcHdr;
		ARCSECTHDR *ArcSectHdr;
		ARCENTRY *ArcEntry;
		//fprintf( stderr, "\n>> Chip_E.arc\n" );
		
		f_arc = fopen( "Chip_E.arc", "rb" );
		f_chs = fopen( "Chip_E.chs", "wb" );
		if( f_arc == NULL || f_chs == NULL ) {
			MessageBoxW(((ImgInfo *)pvParam)->h, L"初始化失败！无法写入[Chip_E.*]！", COMMON_DLG_TITLE, MB_OK);
			ExitProcess( 0 );
		} // ERROR01: fail to open
		//fprintf( stderr, "1" );

		// Read all info
		fread( &ArcHdr, sizeof( ARCHDR ), 1, f_arc ); // 1
		//fprintf( stderr, "[%d]", ArcHdr.section_count );
		ArcSectHdr = (ARCSECTHDR *)malloc( ArcHdr.section_count * sizeof( ARCSECTHDR ) );
		fread( ArcSectHdr, sizeof( ARCSECTHDR ), ArcHdr.section_count, f_arc ); // 2
		for( i = 0; i < (int)ArcHdr.section_count; i ++ ) FileCount += ArcSectHdr[ i ].entry_count;
		ArcEntry = (ARCENTRY *)malloc( FileCount * sizeof( ARCENTRY ) );
		fread( ArcEntry, sizeof( ARCENTRY ), FileCount, f_arc ); // 3
		//fprintf( stderr, "2" );

		// Write all info
		fwrite( &ArcHdr, sizeof( ARCHDR ), 1, f_chs ); // 1
		fwrite( ArcSectHdr, sizeof( ARCSECTHDR ), ArcHdr.section_count, f_chs ); // 2
		fwrite( ArcEntry, sizeof( ARCENTRY ), FileCount, f_chs ); // 3, need to change then
		//fprintf( stderr, "3" );

		// Calc replacement position
		// EFCCA0030.PNG
		for( SectId = 0; SectId < (int)ArcHdr.section_count; SectId ++ ) if( !strcmp( ArcSectHdr[ SectId ].type, "PNG" ) ) break;
		//fprintf( stderr, ".(SectId=%d)", SectId );
		if( SectId == ArcHdr.section_count ) goto INNER_ERROR01; // ERROR02
		for( i = EntryId = 0; i < SectId; i ++ ) EntryId += ArcSectHdr[ i ].entry_count;
		//fprintf( stderr, "(~%d/%d)", EntryId, FileCount );
		for( ; EntryId < FileCount; EntryId ++ ) {
			//fprintf( stderr, "\n%d:%s", EntryId, ArcEntry[ EntryId ].filename );
			if( !strcmp( ArcEntry[ EntryId ].filename, "EFCCA0030" ) ) break;
		}
		//fprintf( stderr, "(=%d/%d)", EntryId, FileCount );
		if( EntryId == FileCount ) goto INNER_ERROR01; // ERROR03
		//fprintf( stderr, "4" );

		// Write files
		for( i = 0; i < FileCount; i ++ ) {
			((ImgInfo *)pvParam)->progress = 0 + (int)(10.0*i/FileCount);
			sprintf_s( ((ImgInfo *)pvParam)->text, 1024, "Patching %s.", ArcEntry[ i ].filename );

			int FileSize;
			if( i == EntryId ) { // Need to replace
				f_in = fopen( "patch_files\\Chip_E_arc\\EFCCA0030.PNG", "rb" );
				fseek( f_in, 0, SEEK_END );
				FileSize = ftell( f_in );
				
				FileDetail = (char *)malloc( FileSize );
				ArcEntry[ i ].length = FileSize;
				
				clearerr( f_in ); // reset end info
				fseek( f_in, 0, SEEK_SET );
				fread( FileDetail, 1, FileSize, f_in );
				fclose( f_in );
			}
			else {
				FileSize = ArcEntry[ i ].length;
				FileDetail = (char *)malloc( FileSize );
				fseek( f_arc, ArcEntry[ i ].offset, SEEK_SET );
				fread( FileDetail, 1, FileSize, f_arc );
			}
			
			fwrite( FileDetail, 1, FileSize, f_chs );
			free( FileDetail );
		}
		//fprintf( stderr, "5" );

		// ReCalc header info
		for( i = 1; i < FileCount; i ++ )
			ArcEntry[ i ].offset = ArcEntry[ i - 1 ].offset + ArcEntry[ i - 1 ].length;
		fseek( f_chs, sizeof( ARCHDR ) + ArcHdr.section_count * sizeof( ARCSECTHDR ), SEEK_SET );
		fwrite( ArcEntry, sizeof( ARCENTRY ), FileCount, f_chs );
		
		free( ArcSectHdr );
		free( ArcEntry );
		fclose( f_arc );
		fclose( f_chs );
	}


	// Chip_S.arc (10%-20%)
	{
		int FileCount = 0, i, SectId1, EntryId1, SectId2, EntryId2;
		char *FileDetail;
		FILE *f_arc, *f_chs, *f_in;
		ARCHDR ArcHdr;
		ARCSECTHDR *ArcSectHdr;
		ARCENTRY *ArcEntry;
		//fprintf( stderr, "\n>> Chip_S.arc\n" );
		
		f_arc = fopen( "Chip_S.arc", "rb" );
		f_chs = fopen( "Chip_S.chs", "wb" );
		if( f_arc == NULL || f_chs == NULL ) {
			MessageBoxW(((ImgInfo *)pvParam)->h, L"[初始化失败！无法写入Chip_S.*]！", COMMON_DLG_TITLE, MB_OK);
			ExitProcess( 0 );
		} // ERROR01: fail to open
		//fprintf( stderr, "1" );

		// Read all info
		fread( &ArcHdr, sizeof( ARCHDR ), 1, f_arc ); // 1
		//fprintf( stderr, "[%d]", ArcHdr.section_count );
		ArcSectHdr = (ARCSECTHDR *)malloc( ArcHdr.section_count * sizeof( ARCSECTHDR ) );
		fread( ArcSectHdr, sizeof( ARCSECTHDR ), ArcHdr.section_count, f_arc ); // 2
		for( i = 0; i < (int)ArcHdr.section_count; i ++ ) FileCount += ArcSectHdr[ i ].entry_count;
		ArcEntry = (ARCENTRY *)malloc( FileCount * sizeof( ARCENTRY ) );
		fread( ArcEntry, sizeof( ARCENTRY ), FileCount, f_arc ); // 3
		//fprintf( stderr, "2" );

		// Write all info
		fwrite( &ArcHdr, sizeof( ARCHDR ), 1, f_chs ); // 1
		fwrite( ArcSectHdr, sizeof( ARCSECTHDR ), ArcHdr.section_count, f_chs ); // 2
		fwrite( ArcEntry, sizeof( ARCENTRY ), FileCount, f_chs ); // 3, need to change then
		//fprintf( stderr, "3" );

		// Calc replacement position
		// SGCC0003_PNG.png
		for( SectId1 = 0; SectId1 < (int)ArcHdr.section_count; SectId1 ++ ) if( !strcmp( ArcSectHdr[ SectId1 ].type, "PNG" ) ) break;
		//fprintf( stderr, ".(SectId1=%d)", SectId1 );
		if( SectId1 == ArcHdr.section_count ) goto INNER_ERROR01; // ERROR02
		for( i = EntryId1 = 0; i < SectId1; i ++ ) EntryId1 += ArcSectHdr[ i ].entry_count;
		//fprintf( stderr, "(~%d/%d)", EntryId1, FileCount );
		for( ; EntryId1 < FileCount; EntryId1 ++ ) {
			//fprintf( stderr, "\n%d:%s", EntryId1, ArcEntry[ EntryId1 ].filename );
			if( !strcmp( ArcEntry[ EntryId1 ].filename, "SGCC0003" ) ) break;
		}
		//fprintf( stderr, "(=%d/%d)", EntryId1, FileCount );
		if( EntryId1 == FileCount ) goto INNER_ERROR01; // ERROR03
		//fprintf( stderr, "4" );

		// SGCC0011_PNG.png
		for( SectId2 = 0; SectId2 < (int)ArcHdr.section_count; SectId2 ++ ) if( !strcmp( ArcSectHdr[ SectId2 ].type, "PNG" ) ) break;
		//fprintf( stderr, ".(SectId2=%d)", SectId2 );
		if( SectId2 == ArcHdr.section_count ) goto INNER_ERROR01; // ERROR02
		for( i = EntryId2 = 0; i < SectId2; i ++ ) EntryId2 += ArcSectHdr[ i ].entry_count;
		//fprintf( stderr, "(~%d/%d)", EntryId2, FileCount );
		for( ; EntryId2 < FileCount; EntryId2 ++ ) {
			//fprintf( stderr, "\n%d:%s", EntryId2, ArcEntry[ EntryId2 ].filename );
			if( !strcmp( ArcEntry[ EntryId2 ].filename, "SGCC0011" ) ) break;
		}
		//fprintf( stderr, "(=%d/%d)", EntryId2, FileCount );
		if( EntryId2 == FileCount ) goto INNER_ERROR01; // ERROR03
		//fprintf( stderr, "4" );

		// Write files
		for( i = 0; i < FileCount; i ++ ) {
			((ImgInfo *)pvParam)->progress = 10 + (int)(10.0*i/FileCount);
			sprintf_s( ((ImgInfo *)pvParam)->text, 1024, "Patching %s.", ArcEntry[ i ].filename );

			int FileSize;
			if( i == EntryId1 ) { // Need to replace
				f_in = fopen( "patch_files\\Chip_S_arc\\SGCC0003_PNG.png", "rb" );
				fseek( f_in, 0, SEEK_END );
				FileSize = ftell( f_in );
				
				FileDetail = (char *)malloc( FileSize );
				ArcEntry[ i ].length = FileSize;
				
				clearerr( f_in ); // reset end info
				fseek( f_in, 0, SEEK_SET );
				fread( FileDetail, 1, FileSize, f_in );
				fclose( f_in );
			}
			else if( i == EntryId2 ) { // Need to replace
				f_in = fopen( "patch_files\\Chip_S_arc\\SGCC0011_PNG.png", "rb" );
				fseek( f_in, 0, SEEK_END );
				FileSize = ftell( f_in );
				
				FileDetail = (char *)malloc( FileSize );
				ArcEntry[ i ].length = FileSize;
				
				clearerr( f_in ); // reset end info
				fseek( f_in, 0, SEEK_SET );
				fread( FileDetail, 1, FileSize, f_in );
				fclose( f_in );
			}
			else {
				FileSize = ArcEntry[ i ].length;
				FileDetail = (char *)malloc( FileSize );
				fseek( f_arc, ArcEntry[ i ].offset, SEEK_SET );
				fread( FileDetail, 1, FileSize, f_arc );
			}
			
			fwrite( FileDetail, 1, FileSize, f_chs );
			free( FileDetail );
		}
		//fprintf( stderr, "5" );

		// ReCalc header info
		for( i = 1; i < FileCount; i ++ )
			ArcEntry[ i ].offset = ArcEntry[ i - 1 ].offset + ArcEntry[ i - 1 ].length;
		fseek( f_chs, sizeof( ARCHDR ) + ArcHdr.section_count * sizeof( ARCSECTHDR ), SEEK_SET );
		fwrite( ArcEntry, sizeof( ARCENTRY ), FileCount, f_chs );
		
		free( ArcSectHdr );
		free( ArcEntry );
		fclose( f_arc );
		fclose( f_chs );
	}
	
	
	// Chip_T.arc (20%-100%)
	{
		int FileCount = 0, i, SectId1, EntryId1, SectId2, EntryId2;
		char *FileDetail;
		FILE *f_arc, *f_chs, *f_in;
		ARCHDR ArcHdr;
		ARCSECTHDR *ArcSectHdr;
		ARCENTRY *ArcEntry;
		//fprintf( stderr, "\n>> Chip_T.arc\n" );
		
		f_arc = fopen( "Chip_T.arc", "rb" );
		f_chs = fopen( "Chip_T.chs", "wb" );
		if( f_arc == NULL || f_chs == NULL ) {
			MessageBoxW(((ImgInfo *)pvParam)->h, L"初始化失败！无法写入[Chip_T.*]！", COMMON_DLG_TITLE, MB_OK);
			ExitProcess( 0 );
		} // ERROR01: fail to open
		//fprintf( stderr, "1" );

		// Read all info
		fread( &ArcHdr, sizeof( ARCHDR ), 1, f_arc ); // 1
		//fprintf( stderr, "[%d]", ArcHdr.section_count );
		ArcSectHdr = (ARCSECTHDR *)malloc( ArcHdr.section_count * sizeof( ARCSECTHDR ) );
		fread( ArcSectHdr, sizeof( ARCSECTHDR ), ArcHdr.section_count, f_arc ); // 2
		for( i = 0; i < (int)ArcHdr.section_count; i ++ ) FileCount += ArcSectHdr[ i ].entry_count;
		ArcEntry = (ARCENTRY *)malloc( FileCount * sizeof( ARCENTRY ) );
		fread( ArcEntry, sizeof( ARCENTRY ), FileCount, f_arc ); // 3
		//fprintf( stderr, "2" );

		// Write all info
		fwrite( &ArcHdr, sizeof( ARCHDR ), 1, f_chs ); // 1
		fwrite( ArcSectHdr, sizeof( ARCSECTHDR ), ArcHdr.section_count, f_chs ); // 2
		fwrite( ArcEntry, sizeof( ARCENTRY ), FileCount, f_chs ); // 3, need to change then
		//fprintf( stderr, "3" );

		// Calc replacement position
		// SGCC0003_PNG.png
		for( SectId1 = 0; SectId1 < (int)ArcHdr.section_count; SectId1 ++ ) if( !strcmp( ArcSectHdr[ SectId1 ].type, "MSK" ) ) break;
		//fprintf( stderr, ".(SectId1=%d)", SectId1 );
		if( SectId1 == ArcHdr.section_count ) goto INNER_ERROR01; // ERROR02
		for( i = EntryId1 = 0; i < SectId1; i ++ ) EntryId1 += ArcSectHdr[ i ].entry_count;
		//fprintf( stderr, "(~%d/%d)", EntryId1, FileCount );
		for( ; EntryId1 < FileCount; EntryId1 ++ ) {
			//fprintf( stderr, "\n%d:%s", EntryId1, ArcEntry[ EntryId1 ].filename );
			if( !strcmp( ArcEntry[ EntryId1 ].filename, "T1" ) ) break;
		}
		//fprintf( stderr, "(=%d/%d)", EntryId1, FileCount );
		if( EntryId1 == FileCount ) goto INNER_ERROR01; // ERROR03
		//fprintf( stderr, "4" );

		// SGCC0011_PNG.png
		for( SectId2 = 0; SectId2 < (int)ArcHdr.section_count; SectId2 ++ ) if( !strcmp( ArcSectHdr[ SectId2 ].type, "PNG" ) ) break;
		//fprintf( stderr, ".(SectId2=%d)", SectId2 );
		if( SectId2 == ArcHdr.section_count ) goto INNER_ERROR01; // ERROR02
		for( i = EntryId2 = 0; i < SectId2; i ++ ) EntryId2 += ArcSectHdr[ i ].entry_count;
		//fprintf( stderr, "(~%d/%d)", EntryId2, FileCount );
		for( ; EntryId2 < FileCount; EntryId2 ++ ) {
			//fprintf( stderr, "\n%d:%s", EntryId2, ArcEntry[ EntryId2 ].filename );
			if( !strcmp( ArcEntry[ EntryId2 ].filename, "T1" ) ) break;
		}
		//fprintf( stderr, "(=%d/%d)", EntryId2, FileCount );
		if( EntryId2 == FileCount ) goto INNER_ERROR01; // ERROR03
		//fprintf( stderr, "4" );

		// Write files
		for( i = 0; i < FileCount; i ++ ) {
			((ImgInfo *)pvParam)->progress = 20 + (int)(80.0*i/FileCount);
			sprintf_s( ((ImgInfo *)pvParam)->text, 1024, "Patching %s.", ArcEntry[ i ].filename );

			int FileSize;
			if( i == EntryId1 ) { // Need to replace
				f_in = fopen( "patch_files\\Chip_T_arc\\T1.MSK", "rb" );
				fseek( f_in, 0, SEEK_END );
				FileSize = ftell( f_in );
				
				FileDetail = (char *)malloc( FileSize );
				ArcEntry[ i ].length = FileSize;
				
				clearerr( f_in ); // reset end info
				fseek( f_in, 0, SEEK_SET );
				fread( FileDetail, 1, FileSize, f_in );
				fclose( f_in );
			}
			else if( i == EntryId2 ) { // Need to replace
				f_in = fopen( "patch_files\\Chip_T_arc\\T1_PNG.png", "rb" );
				fseek( f_in, 0, SEEK_END );
				FileSize = ftell( f_in );
				
				FileDetail = (char *)malloc( FileSize );
				ArcEntry[ i ].length = FileSize;
				
				clearerr( f_in ); // reset end info
				fseek( f_in, 0, SEEK_SET );
				fread( FileDetail, 1, FileSize, f_in );
				fclose( f_in );
			}
			else {
				FileSize = ArcEntry[ i ].length;
				FileDetail = (char *)malloc( FileSize );
				fseek( f_arc, ArcEntry[ i ].offset, SEEK_SET );
				fread( FileDetail, 1, FileSize, f_arc );
			}
			
			fwrite( FileDetail, 1, FileSize, f_chs );
			free( FileDetail );
		}
		//fprintf( stderr, "5" );

		// ReCalc header info
		for( i = 1; i < FileCount; i ++ )
			ArcEntry[ i ].offset = ArcEntry[ i - 1 ].offset + ArcEntry[ i - 1 ].length;
		fseek( f_chs, sizeof( ARCHDR ) + ArcHdr.section_count * sizeof( ARCSECTHDR ), SEEK_SET );
		fwrite( ArcEntry, sizeof( ARCENTRY ), FileCount, f_chs );
		
		free( ArcSectHdr );
		free( ArcEntry );
		fclose( f_arc );
		fclose( f_chs );
	}

	goto PATCH_TEST; // test again


DONT_NEED_PATCH:
	((ImgInfo *)pvParam)->progress = 100;
	sprintf_s( ((ImgInfo *)pvParam)->text, 1024, "Initialization finished!~" );
	return 0;

INNER_ERROR01:
	MessageBoxW(((ImgInfo *)pvParam)->h, L"内部错误：文件写入错误，请反馈给汉化组！~", COMMON_DLG_TITLE, MB_OK);
	ExitProcess( 0 );
	return 0;
}

DWORD WINAPI AnimeThreadProc( PVOID pvParam )
{
	// Init
	IplImage *RealBG = cvLoadImage( "imgs\\CROSS+CHANNEL.jpg" ), *bak = ((ImgInfo *)pvParam)->src;
	((ImgInfo *)pvParam)->src = RealBG;
	cvReleaseImage( &bak );

	// Play BG Sound
	PlaySoundA( (LPCSTR)IDR_WAVE_BG, hInst_bak, SND_RESOURCE | SND_ASYNC );

	// Load progress imgs
	IplImage *ProgressImgs, *ProgressMasks[ 8 ];
	ProgressImgs = cvLoadImage( "imgs\\pb_basic.png", CV_LOAD_IMAGE_COLOR );
	ProgressMasks[ 0 ] = cvLoadImage( "imgs\\pb01_m.png", CV_LOAD_IMAGE_GRAYSCALE );
	ProgressMasks[ 1 ] = cvLoadImage( "imgs\\pb02_m.png", CV_LOAD_IMAGE_GRAYSCALE );
	ProgressMasks[ 2 ] = cvLoadImage( "imgs\\pb03_m.png", CV_LOAD_IMAGE_GRAYSCALE );
	ProgressMasks[ 3 ] = cvLoadImage( "imgs\\pb04_m.png", CV_LOAD_IMAGE_GRAYSCALE );
	ProgressMasks[ 4 ] = cvLoadImage( "imgs\\pb05_m.png", CV_LOAD_IMAGE_GRAYSCALE );
	ProgressMasks[ 5 ] = cvLoadImage( "imgs\\pb06_m.png", CV_LOAD_IMAGE_GRAYSCALE );
	ProgressMasks[ 6 ] = cvLoadImage( "imgs\\pb07_m.png", CV_LOAD_IMAGE_GRAYSCALE );
	ProgressMasks[ 7 ] = cvLoadImage( "imgs\\pb08_m.png", CV_LOAD_IMAGE_GRAYSCALE );

	int TimeCount = 0; // 0 - 5 [ 0 ], 6 - 10 [ 1 ] ......

	// Rectangle rises up
	for( int y = 250; y > 220; y -- ) {
		cvSetImageROI( ((ImgInfo *)pvParam)->src, cvRect(305, 192 + ( 250 - y ) / 2, 400, 250));

		IplImage *tmp = cvCreateImage(cvGetSize(((ImgInfo *)pvParam)->src),
									   ((ImgInfo *)pvParam)->src->depth,
									   ((ImgInfo *)pvParam)->src->nChannels);

		cvCopy(((ImgInfo *)pvParam)->src, tmp, NULL);
		cvResetImageROI(((ImgInfo *)pvParam)->src);

		RETRY_LOCK_IN_THREAD0:
		if( ((ImgInfo *)pvParam)->isLocked == false ) ((ImgInfo *)pvParam)->isLocked = true; // Lock
		else {
			Sleep( 20 );
			goto RETRY_LOCK_IN_THREAD0;
		}

		// Put alpha rectangle
		IplImage * pTemp=(IplImage*)cvClone( tmp ); // White part
		cvRectangle(pTemp,cvPoint(0,0),cvPoint( WINDOW_WIDTH, WINDOW_HEIGHT), CV_RGB(255,255,255),-1);
		cvAddWeighted(tmp,1.0 - 1.0*( y - 220 ) / 30,pTemp,1.0*( y - 220 ) / 30,0.0,tmp);
		cvReleaseImage( &pTemp );

		pTemp=(IplImage*)cvClone( tmp ); // Black part
		cvRectangle(pTemp,cvPoint( 0,y),cvPoint( WINDOW_WIDTH, WINDOW_HEIGHT),CV_RGB(0,0,0),-1);
		cvAddWeighted(tmp,0.8,pTemp,0.2,0.0,tmp);
		cvReleaseImage( &pTemp );

		((ImgInfo *)pvParam)->cimg.CopyOf( tmp );
		((ImgInfo *)pvParam)->isLocked = false; // Unlock
		SendMessageA( ((ImgInfo *)pvParam)->h, WM_PAINT, NULL, NULL );
		//cvWaitKey( 1000 / 30 );
		
		cvReleaseImage( &tmp );
		Sleep( 20 );
	}

	// Size from 400x250 -> 900x563
	bool ready_to_break = false;
	int progress_save = 0;
	for( int x = 400; ; ) {
		// Judge break time
		if( progress_save >= 100 ) ready_to_break = true;

		int height = x * 250 / 400;
		cvSetImageROI( ((ImgInfo *)pvParam)->src, cvRect(305-(x-400)/2, 192 + 15-(height-250)/2, x, height));

		IplImage *rsDst = cvCreateImage(cvSize( x, height ),
									   ((ImgInfo *)pvParam)->src->depth,
									   ((ImgInfo *)pvParam)->src->nChannels),
				 *tmp = cvCreateImage(cvSize( 400, 250 ),
									   ((ImgInfo *)pvParam)->src->depth,
									   ((ImgInfo *)pvParam)->src->nChannels);

		cvCopy( ((ImgInfo *)pvParam)->src, rsDst, NULL );
		cvResize( rsDst, tmp, CV_INTER_LINEAR );

		//cvResize( ((ImgInfo *)pvParam)->src, tmp );
		//cvCopy(((ImgInfo *)pvParam)->src, tmp, NULL);
		cvResetImageROI(((ImgInfo *)pvParam)->src);

		// Prepare font
		CvFont font;
		double hscale =  1.0, vscale = 1.0;
		cvInitFont( &font, CV_FONT_HERSHEY_COMPLEX_SMALL | CV_FONT_ITALIC, hscale, vscale, 0, 1, CV_AA );
		CvScalar textColor = cvScalar( 240, 125, 21 );
		CvPoint textPos = cvPoint( 40, 240 ); // x, y

	RETRY_LOCK_IN_THREAD1:
		if( ((ImgInfo *)pvParam)->isLocked == false ) ((ImgInfo *)pvParam)->isLocked = true; // Lock
		else {
			Sleep( 20 );
			goto RETRY_LOCK_IN_THREAD1;
		}

		// Put alpha rectangle
		IplImage * pTemp=(IplImage*)cvClone( tmp ); // White part
		cvRectangle(pTemp,cvPoint(0,220),cvPoint( (int)(WINDOW_WIDTH*(progress_save/100.0)), WINDOW_HEIGHT), CV_RGB(255,255,255),-1);
		cvAddWeighted(tmp,0.4,pTemp,0.6,0.0,tmp);
		cvReleaseImage( &pTemp );

		pTemp=(IplImage*)cvClone( tmp ); // Black part
		cvRectangle(pTemp,cvPoint((int)(WINDOW_WIDTH*(progress_save/100.0)),220),cvPoint( WINDOW_WIDTH, WINDOW_HEIGHT),CV_RGB(0,0,0),-1);
		cvAddWeighted(tmp,0.8,pTemp,0.2,0.0,tmp);
		cvReleaseImage( &pTemp );

		cvPutText( tmp, ((ImgInfo *)pvParam)->text, textPos, &font, textColor ); // Put text from preparing

		const int PB_StartX = 8, PB_StartY = 220;
		int AlphaSelected = TimeCount / 5 % 8; // 0 ~ 7
		for( int n = PB_StartX; n < PB_StartX + 28; n ++ ) {
			for( int m = PB_StartY; m < PB_StartY + 28; m ++ ) {
				CV_IMAGE_ELEM( tmp, uchar, m, 3*n ) = CV_IMAGE_ELEM( ProgressImgs, uchar, m - PB_StartY, 3*(n - PB_StartX) ) * CV_IMAGE_ELEM( ProgressMasks[ AlphaSelected ], uchar, m - PB_StartY, n - PB_StartX ) / 255
					+ CV_IMAGE_ELEM( tmp, uchar, m, 3*n ) * ( 255 - CV_IMAGE_ELEM( ProgressMasks[ AlphaSelected ], uchar, m - PB_StartY, n - PB_StartX ) ) / 255;
				CV_IMAGE_ELEM( tmp, uchar, m, 3*n + 1 ) = CV_IMAGE_ELEM( ProgressImgs, uchar, m - PB_StartY, 3*(n - PB_StartX) + 1 ) * CV_IMAGE_ELEM( ProgressMasks[ AlphaSelected ], uchar, m - PB_StartY, n - PB_StartX ) / 255
					+ CV_IMAGE_ELEM( tmp, uchar, m, 3*n + 1 ) * ( 255 - CV_IMAGE_ELEM( ProgressMasks[ AlphaSelected ], uchar, m - PB_StartY, n - PB_StartX ) ) / 255;
				CV_IMAGE_ELEM( tmp, uchar, m, 3*n + 2 ) = CV_IMAGE_ELEM( ProgressImgs, uchar, m - PB_StartY, 3*(n - PB_StartX) + 2 ) * CV_IMAGE_ELEM( ProgressMasks[ AlphaSelected ], uchar, m - PB_StartY, n - PB_StartX ) / 255
					+ CV_IMAGE_ELEM( tmp, uchar, m, 3*n + 2 ) * ( 255 - CV_IMAGE_ELEM( ProgressMasks[ AlphaSelected ], uchar, m - PB_StartY, n - PB_StartX ) ) / 255;
			}
		}

		((ImgInfo *)pvParam)->cimg.CopyOf( tmp );
		((ImgInfo *)pvParam)->isLocked = false; // Unlock
		SendMessageA( ((ImgInfo *)pvParam)->h, WM_PAINT, NULL, NULL );
		//cvWaitKey( 1000 / 30 );
		
		cvReleaseImage( &tmp );
		cvReleaseImage( &rsDst );
		Sleep( 15 );
		
		TimeCount ++;
		if( TimeCount > 40 ) TimeCount -= 40;

		if( ((ImgInfo *)pvParam)->progress > progress_save ) {
			progress_save ++;
			x = 400 + (int)( progress_save * ( 900 - 400 ) / 100.0 );
		}
		if( ready_to_break ) {
			Sleep( 500 );
			break;
		}
	}

	// Ending Anime, Rectangle goes down
	for( int y = 220; y < 250; y ++ ) {
		int height = 900 * 250 / 400;
		//cvSetImageROI( ((ImgInfo *)pvParam)->src, cvRect(248-(x-400)/2, 156 + 15-(height-250)/2, x, height));
		cvSetImageROI( ((ImgInfo *)pvParam)->src, cvRect(305-(900-400)/2, 192+(250-y)/2-(height-250)/2, 900, height));

		IplImage *rsDst = cvCreateImage(cvSize( 900, height ),
									   ((ImgInfo *)pvParam)->src->depth,
									   ((ImgInfo *)pvParam)->src->nChannels),
				 *tmp = cvCreateImage(cvSize( 400, 250 ),
									   ((ImgInfo *)pvParam)->src->depth,
									   ((ImgInfo *)pvParam)->src->nChannels);

		cvCopy( ((ImgInfo *)pvParam)->src, rsDst, NULL );
		cvResize( rsDst, tmp, CV_INTER_LINEAR );
		cvResetImageROI(((ImgInfo *)pvParam)->src);

		RETRY_LOCK_IN_THREAD10:
		if( ((ImgInfo *)pvParam)->isLocked == false ) ((ImgInfo *)pvParam)->isLocked = true; // Lock
		else {
			Sleep( 20 );
			goto RETRY_LOCK_IN_THREAD10;
		}

		// Put alpha rectangle
		IplImage * pTemp=(IplImage*)cvClone( tmp ); // white part
		cvRectangle(pTemp,cvPoint(0,0),cvPoint( WINDOW_WIDTH, WINDOW_HEIGHT), CV_RGB(255,255,255),-1);
		cvAddWeighted(tmp,1.0 - 1.0*( y - 220 ) / 30,pTemp,1.0*( y - 220 ) / 30,0.0,tmp);
		cvReleaseImage( &pTemp );

		pTemp=(IplImage*)cvClone( tmp ); // white part
		cvRectangle(pTemp,cvPoint( 0,y),cvPoint( WINDOW_WIDTH, WINDOW_HEIGHT),CV_RGB(255,255,255),-1);
		cvAddWeighted(tmp,0.8,pTemp,0.2,0.0,tmp);
		cvReleaseImage( &pTemp );

		((ImgInfo *)pvParam)->cimg.CopyOf( tmp );
		((ImgInfo *)pvParam)->isLocked = false; // Unlock
		SendMessageA( ((ImgInfo *)pvParam)->h, WM_PAINT, NULL, NULL );
		//cvWaitKey( 1000 / 30 );
		
		cvReleaseImage( &tmp );
		cvReleaseImage( &rsDst );
		Sleep( 20 );
	}

	cvReleaseImage( &ProgressImgs );
	cvReleaseImage( &ProgressMasks[ 0 ] );
	cvReleaseImage( &ProgressMasks[ 1 ] );
	cvReleaseImage( &ProgressMasks[ 2 ] );
	cvReleaseImage( &ProgressMasks[ 3 ] );
	cvReleaseImage( &ProgressMasks[ 4 ] );
	cvReleaseImage( &ProgressMasks[ 5 ] );
	cvReleaseImage( &ProgressMasks[ 6 ] );
	cvReleaseImage( &ProgressMasks[ 7 ] );
	
	TerminateThread( hThreadPatch, 0 );
	EndDialog( ((ImgInfo *)pvParam)->h, 0 );

	return 0;
}

DWORD WINAPI MonitorThreadProc( PVOID pvParam )
{
	//WinExec( "UninstallChs.exe m", SW_SHOW );
	
RETRY_CREATEPROC:
	ZeroMemory( &si_monitor, sizeof(si_monitor) );  
    si_monitor.cb = sizeof(si_monitor);  
    ZeroMemory( &pi_monitor, sizeof(pi_monitor) );
    if( !CreateProcessA("UninstallChs.exe", " m",NULL,NULL,FALSE,NORMAL_PRIORITY_CLASS|CREATE_SHARED_WOW_VDM |CREATE_NEW_CONSOLE | CREATE_UNICODE_ENVIRONMENT,NULL,NULL, &si_monitor, &pi_monitor)) {
        CloseHandle(pi_monitor.hThread);
        CloseHandle(pi_monitor.hProcess);
		Sleep( 500 );
		goto RETRY_CREATEPROC;
    }

	return 0;
}

/********************
 * Helpful Funcs 
 ********************/
//


/********************
 * Hijacked Funcs 
 ********************/
LONG HegCloseKey(
    HKEY hKey // handle of key to close
    )
{
#ifdef SETALLLOG
    return RegCloseKey( hKey );
#endif

#ifdef DEBUG
	LoopCount --;
	fprintf( LogFile, "< HegCloseKey( %ld );\n", hKey );
	if( !LoopCount ) fprintf( LogFile, "\n" ); // 补个换行使层次分明
	//MessageBoxA( NULL, "< HegCloseKey( %ld );", NULL, NULL );
#endif

	hKey = NULL;
	return ERROR_SUCCESS;
}

LONG HegCreateKeyExA(
    HKEY hKey,                                  // handle of an open key
    LPCSTR lpSubKey,                            // address of subkey name
    DWORD Reserved,                             // reserved
    LPSTR lpClass,                              // address of class string
    DWORD dwOptions,                            // special options test flag
    REGSAM samDesired,                          // desired security access
    LPSECURITY_ATTRIBUTES lpSecurityAttributes, // address of key security structure
    PHKEY phkResult,                            // address of buffer for opened handle
    LPDWORD lpdwDisposition                     // address of disposition value buffer
   )
{
#ifdef SETALLLOG
	return RegCreateKeyExA( hKey, lpSubKey, Reserved, lpClass, dwOptions, samDesired, lpSecurityAttributes, phkResult, lpdwDisposition );
#endif

#ifdef DEBUG
	fprintf( LogFile, "  HegCreateKeyExA( %ld, %s, %ld, %s, %ld ... );\n", hKey, lpSubKey, Reserved, lpClass, dwOptions );
	//MessageBoxA( NULL, "  HegCreateKeyExA( %ld, %s, %ld, %s, %ld ... );", NULL, NULL );
#endif
	
	//hKey = FakeHKEY;
	hKey = (HKEY)12345;
	*phkResult = (HKEY)12345;
	return ERROR_SUCCESS;
}

LONG HegOpenKeyExA(
    HKEY hKey,         // handle of open key
    LPCSTR lpSubKey,   // address of name of subkey to open
    DWORD ulOptions,   // reserved
    REGSAM samDesired, // security access mask
    PHKEY phkResult    // address of handle of open key
    )
{
#ifdef SETALLLOG
    return RegOpenKeyExA( hKey, lpSubKey, ulOptions, samDesired, phkResult );
#endif

#ifdef DEBUG
	char security[ 100 ] = { 0 };
	int Count = 0;
	LoopCount ++;
	if( samDesired == KEY_ALL_ACCESS ) strcat( security, "KEY_ALL_ACCESS" );
	else if( samDesired == KEY_WRITE ) strcat( security, "KEY_WRITE" );
	else if( samDesired == KEY_READ ) strcat( security, "KEY_READ" );
	else {
		if( samDesired == KEY_CREATE_LINK ) {
			if( Count ++ != 0 ) strcat( security, " | " ); strcat( security, "KEY_CREATE_LINK" ); }
		if( samDesired == KEY_CREATE_SUB_KEY ) {
			if( Count ++ != 0 ) strcat( security, " | " ); strcat( security, "KEY_CREATE_SUB_KEY" ); }
		if( samDesired == KEY_ENUMERATE_SUB_KEYS ) {
			if( Count ++ != 0 ) strcat( security, " | " ); strcat( security, "KEY_ENUMERATE_SUB_KEYS" ); }
		if( samDesired == KEY_EXECUTE ) {
			if( Count ++ != 0 ) strcat( security, " | " ); strcat( security, "KEY_EXECUTE" ); }
		if( samDesired == KEY_NOTIFY ) {
			if( Count ++ != 0 ) strcat( security, " | " ); strcat( security, "KEY_NOTIFY" ); }
		if( samDesired == KEY_QUERY_VALUE ) {
			if( Count ++ != 0 ) strcat( security, " | " ); strcat( security, "KEY_QUERY_VALUE" ); }
		if( samDesired == KEY_SET_VALUE ) {
			if( Count ++ != 0 ) strcat( security, " | " ); strcat( security, "KEY_SET_VALUE" ); }
	}

	fprintf( LogFile, "> HegOpenKeyExA( hKey, %s, %ld, %s, %ld );\n", lpSubKey, ulOptions, security, *phkResult );
	//MessageBoxA( NULL, "> HegOpenKeyExA( hKey, %s, %ld, %s, %ld );", NULL, NULL );
#endif

	if( !nTime ) {
		nTime |= 1;
		DllErrorStatus = 0;
		/*LoadWnd = CreateDialogA( hInst_bak, MAKEINTRESOURCE( IDD_FORMVIEW ), NULL,(DLGPROC)DlgProc );
		nOldStyle = GetWindowLongA( LoadWnd, GWL_STYLE );
		SetWindowLongA( LoadWnd, GWL_STYLE, nOldStyle & ~WS_CAPTION );
		ShowWindow( LoadWnd, SW_SHOW );
		system("pause");*/
		DialogBoxParamA( hInst_bak, MAKEINTRESOURCEA( IDD_MAIN ), NULL, DlgProc, 0 ); // need a new thread ?
		if( DllErrorStatus != 0 ) ExitProcess( 0x04 ); // Error - need to exit
	}
	
	hKey = (HKEY)12345;
	*phkResult = (HKEY)12345;
	return ERROR_SUCCESS;
}

LONG HegQueryValueExA(
    HKEY hKey,          // handle of key to query
    LPCSTR lpValueName, // address of name of value to query
    LPDWORD lpReserved, // reserved
    LPDWORD lpType,     // address of buffer for value type
    LPBYTE lpData,      // address of data buffer
    LPDWORD lpcbData    // address of data buffer size
    )
{
#ifdef SETALLLOG
    return RegQueryValueExA( hKey, lpValueName, lpReserved, lpType, lpData, lpcbData );
#endif

#ifdef DEBUG
	fprintf( LogFile, "- HegQueryValueExA( %ld, %s, %ld, %ld, lpData, %ld );\n", hKey, lpValueName, lpReserved, *lpType, *lpcbData );
	//MessageBoxA( NULL, "- HegQueryValueExA( %ld, %s, %ld, %ld, lpData, %ld );", NULL, NULL );
#endif
	
	for( i = 0; i < TableSize; i ++ ) if( !strcmp( lpValueName, KeyTable[ i ] ) ) break; // Find match
	switch( i ) {
	case 0: //"Adapter",
		*lpType = REG_DWORD;  memcpy_s( lpData, 4, &Reg.Adapter, 4 );  *lpcbData = 4;  break;
	case 1: //"DisplayMode_Window",
		*lpType = REG_DWORD;  memcpy_s( lpData, 4, &Reg.DisplayMode_Window, 4 );  *lpcbData = 4;  break;
	case 2: //"Size_Full.Width",
		*lpType = REG_DWORD;  memcpy_s( lpData, 4, &Reg.Size_Full_Width, 4 );  *lpcbData = 4;  break;
	case 3: //"Size_Full.Height",
		*lpType = REG_DWORD;  memcpy_s( lpData, 4, &Reg.Size_Full_Height, 4 );  *lpcbData = 4;  break;
	case 4: //"Size_Window.Width",
		*lpType = REG_DWORD;  memcpy_s( lpData, 4, &Reg.Size_Window_Width, 4 );  *lpcbData = 4;  break;
	case 5: //"Size_Window.Height",
		*lpType = REG_DWORD;  memcpy_s( lpData, 4, &Reg.Size_Window_Height, 4 );  *lpcbData = 4;  break;
	case 6: //"FullScreen",
		*lpType = REG_DWORD;  memcpy_s( lpData, 4, &Reg.FullScreen, 4 );  *lpcbData = 4;  break;
	case 7: //"BackBuffer.Width",
		*lpType = REG_DWORD;  memcpy_s( lpData, 4, &Reg.BackBuffer_Width, 4 );  *lpcbData = 4;  break;
	case 8: //"BackBuffer.Height",
		*lpType = REG_DWORD;  memcpy_s( lpData, 4, &Reg.BackBuffer_Height, 4 );  *lpcbData = 4;  break;
	case 9: //"KeepAspectRatio",
		*lpType = REG_DWORD;  memcpy_s( lpData, 4, &Reg.KeepAspectRatio, 4 );  *lpcbData = 4;  break;
	case 10: //"VSync",
		*lpType = REG_DWORD;  memcpy_s( lpData, 4, &Reg.VSync, 4 );  *lpcbData = 4;  break;
	case 11: //"UnDivideTexture",
		*lpType = REG_DWORD;  memcpy_s( lpData, 4, &Reg.UnDivideTexture, 4 ); *lpcbData = 4;  break;
	case 12: //"DisableDialog",
		*lpType = REG_DWORD;  memcpy_s( lpData, 4, &Reg.DisableDialog, 4 );  *lpcbData = 4;  break;
	case 13: //"UseCV",
		*lpType = REG_DWORD;  memcpy_s( lpData, 4, &Reg.UseCV, 4 );  *lpcbData = 4;  break;
	case 14: //"JoyPad",
		*lpType = REG_DWORD;  memcpy_s( lpData, 4, &Reg.JoyPad, 4 );  *lpcbData = 4;  break;

	case 15: //"InstallType",
		*lpType = REG_BINARY;  memcpy_s( lpData, 4, Reg.InstallType, 4 );  *lpcbData = 4;  break;
	case 16: //"InstallDir",
		*lpType = REG_SZ;  memcpy_s( lpData, 260, Reg.InstallDir, 260 );  *lpcbData = 260;  break;
	case 17: //"InstallSrc",
		*lpType = REG_SZ;  memcpy_s( lpData, 260, Reg.InstallSrc, 260 );  *lpcbData = 260;  break;
	case 18: //"FontName",
		*lpType = REG_SZ;  memcpy_s( lpData, 1024, Reg.FontName, 1024 );  *lpcbData = 1024;  break;
	case 19: //"SpecialFontName",
		*lpType = REG_SZ;  memcpy_s( lpData, 1024, Reg.SpecialFontName, 1024 );  *lpcbData = 1024;  break;
	case 20: //"AutoMsg",
		*lpType = REG_BINARY;  memcpy_s( lpData, 4, Reg.AutoMsg, 4 );  *lpcbData = 4;  break;
	case 21: //"AutoSkip",
		*lpType = REG_BINARY;  memcpy_s( lpData, 4, Reg.AutoSkip, 4 );  *lpcbData = 4;  break;
	case 22: //"CursorHide",
		*lpType = REG_BINARY;  memcpy_s( lpData, 4, Reg.CursorHide, 4 );  *lpcbData = 4;  break;
	case 23: //"CursorTime",
		*lpType = REG_BINARY;  memcpy_s( lpData, 4, Reg.CursorTime, 4 );  *lpcbData = 4;  break;
	case 24: //"D3D.DisableTnL",
		*lpType = REG_BINARY;  memcpy_s( lpData, 4, Reg.D3D_DisableTnL, 4 );  *lpcbData = 4;  break;
	case 25: //"D3D.Tex16",
		*lpType = REG_BINARY;  memcpy_s( lpData, 4, Reg.D3D_Tex16, 4 );  *lpcbData = 4;  break;
	case 26: //"DeactivePlay",
		*lpType = REG_BINARY;  memcpy_s( lpData, 4, Reg.DeactivePlay, 4 );  *lpcbData = 4;  break;
	case 27: //"Dialog",
		*lpType = REG_BINARY;  memcpy_s( lpData, 4, Reg.Dialog, 4 );  *lpcbData = 4;  break;
	case 28: //"DisableCursor",
		*lpType = REG_BINARY;  memcpy_s( lpData, 4, Reg.DisableCursor, 4 );  *lpcbData = 4;  break;
	case 29: //"DisablePan",
		*lpType = REG_BINARY;  memcpy_s( lpData, 4, Reg.DisablePan, 4 );  *lpcbData = 4;  break;
	case 30: //"DisableQuick",
		*lpType = REG_BINARY;  memcpy_s( lpData, 4, Reg.DisableQuick, 4 );  *lpcbData = 4;  break;
	case 31: //"DisplayMode",
		*lpType = REG_BINARY;  memcpy_s( lpData, 4, Reg.DisplayMode, 4 );  *lpcbData = 4;  break;
	case 32: //"EffectSkip",
		*lpType = REG_BINARY;  memcpy_s( lpData, 4, Reg.EffectSkip, 4 );  *lpcbData = 4;  break;
	case 33: //"FontEdge",
		*lpType = REG_BINARY;  memcpy_s( lpData, 4, Reg.FontEdge, 4 );  *lpcbData = 4;  break;
	case 34: //"LogAlpha",
		*lpType = REG_BINARY;  memcpy_s( lpData, 4, Reg.LogAlpha, 4 );  *lpcbData = 4;  break;
	case 35: //"MsgAlpha",
		*lpType = REG_BINARY;  memcpy_s( lpData, 4, Reg.MsgAlpha, 4 );  *lpcbData = 4;  break;
	case 36: //"MsgPos",
		*lpType = REG_BINARY;  memcpy_s( lpData, 8, Reg.MsgPos, 8 );  *lpcbData = 8;  break;
	case 37: //"MsgSpeed",
		*lpType = REG_BINARY;  memcpy_s( lpData, 4, Reg.MsgSpeed, 4 );  *lpcbData = 4;  break;
	case 38: //"Mute",
		*lpType = REG_BINARY;  memcpy_s( lpData, 84, Reg.Mute, 84 );  *lpcbData = 84;  break;
	case 39: //"RButtonMode",
		*lpType = REG_BINARY;  memcpy_s( lpData, 4, Reg.RButtonMode, 4 );  *lpcbData = 4;  break;
	case 40: //"SelAuto",
		*lpType = REG_BINARY;  memcpy_s( lpData, 4, Reg.SelAuto, 4 );  *lpcbData = 4;  break;
	case 41: //"SelSkip",
		*lpType = REG_BINARY;  memcpy_s( lpData, 4, Reg.SelSkip, 4 );  *lpcbData = 4;  break;
	case 42: //"SimpleWindow",
		*lpType = REG_BINARY;  memcpy_s( lpData, 4, Reg.SimpleWindow, 4 );  *lpcbData = 4;  break;
	case 43: //"SkipIcon",
		*lpType = REG_BINARY;  memcpy_s( lpData, 4, Reg.SkipIcon, 4 );  *lpcbData = 4;  break;
	case 44: //"SkipType",
		*lpType = REG_BINARY;  memcpy_s( lpData, 4, Reg.SkipType, 4 );  *lpcbData = 4;  break;
	case 45: //"SysVoice",
		*lpType = REG_BINARY;  memcpy_s( lpData, 4, Reg.SysVoice, 4 );  *lpcbData = 4;  break;
	case 46: //"TextColor",
		*lpType = REG_BINARY;  memcpy_s( lpData, 4, Reg.TextColor, 4 );  *lpcbData = 4;  break;
	case 47: //"UseDefaultFont",
		*lpType = REG_BINARY;  memcpy_s( lpData, 4, Reg.UseDefaultFont, 4 );  *lpcbData = 4;  break;
	case 48: //"UseFilt",
		*lpType = REG_BINARY;  memcpy_s( lpData, 4, Reg.UseFilt, 4 );  *lpcbData = 4;  break;
	case 49: //"VoiceSkip",
		*lpType = REG_BINARY;  memcpy_s( lpData, 4, Reg.VoiceSkip, 4 );  *lpcbData = 4;  break;
	case 50: //"Volume",
		*lpType = REG_BINARY;  memcpy_s( lpData, 84, Reg.Volume, 84 );  *lpcbData = 84;  break;
	case 51: //"WndPos"
		*lpType = REG_BINARY;  memcpy_s( lpData, 8, Reg.WndPos, 8 );  *lpcbData = 8;  break;
	default:
		*lpType = REG_BINARY;  memcpy_s( lpData, 4, ForSafe, 4 );  *lpcbData = 4;  break;
	}

	return ERROR_SUCCESS;
}

LONG HegSetValueExA(
    HKEY hKey,           // handle of key to set value for
    LPCSTR lpValueName, // address of value to set
    DWORD Reserved,      // reserved
    DWORD dwType,        // flag for value type
    CONST BYTE *lpData,  // address of value data
    DWORD cbData         // size of value data
    )
{
#ifdef SETALLLOG
    return RegSetValueExA( hKey, lpValueName, Reserved, dwType, lpData, cbData );
#endif

#ifdef DEBUG
	fprintf( LogFile, "+ HegSetValueExA( %ld, %s, %ld, %ld, lpData, %ld );\n", hKey, lpValueName, Reserved, dwType, cbData );
	//MessageBoxA( NULL, "+ HegSetValueExA( %ld, %s, %ld, %ld, lpData, %ld );", NULL, NULL );
#endif
	
	for( i = 0; i < TableSize; i ++ ) if( !strcmp( lpValueName, KeyTable[ i ] ) ) break; // Find match
	switch( i ) {
	case 0: //"Adapter",
		memcpy_s( &Reg.Adapter, 4, lpData, cbData );  break;
	case 1: //"DisplayMode_Window",
		memcpy_s( &Reg.DisplayMode_Window, 4, lpData, cbData );  break;
	case 2: //"Size_Full.Width",
		memcpy_s( &Reg.Size_Full_Width, 4, lpData, cbData );  break;
	case 3: //"Size_Full.Height",
		memcpy_s( &Reg.Size_Full_Height, 4, lpData, cbData );  break;
	case 4: //"Size_Window.Width",
		memcpy_s( &Reg.Size_Window_Width, 4, lpData, cbData );  break;
	case 5: //"Size_Window.Height",
		memcpy_s( &Reg.Size_Window_Height, 4, lpData, cbData );  break;
	case 6: //"FullScreen",
		memcpy_s( &Reg.FullScreen, 4, lpData, cbData );  break;
	case 7: //"BackBuffer.Width",
		memcpy_s( &Reg.BackBuffer_Width, 4, lpData, cbData );  break;
	case 8: //"BackBuffer.Height",
		memcpy_s( &Reg.BackBuffer_Height, 4, lpData, cbData );  break;
	case 9: //"KeepAspectRatio",
		memcpy_s( &Reg.KeepAspectRatio, 4, lpData, cbData );  break;
	case 10: //"VSync",
		memcpy_s( &Reg.VSync, 4, lpData, cbData );  break;
	case 11: //"UnDivideTexture",
		memcpy_s( &Reg.UnDivideTexture, 4, lpData, cbData );  break;
	case 12: //"DisableDialog",
		memcpy_s( &Reg.DisableDialog, 4, lpData, cbData );  break;
	case 13: //"UseCV",
		memcpy_s( &Reg.UseCV, 4, lpData, cbData );  break;
	case 14: //"JoyPad",
		memcpy_s( &Reg.JoyPad, 4, lpData, cbData );  break;

	case 15: //"InstallType",
		memcpy_s( Reg.InstallType, 4, lpData, cbData );  break;
	case 16: //"InstallDir",
		memcpy_s( Reg.InstallDir, 260, lpData, cbData );  break;
	case 17: //"InstallSrc",
		memcpy_s( Reg.InstallSrc, 260, lpData, cbData );  break;
	case 18: //"FontName",
		memcpy_s( Reg.FontName, 1024, lpData, cbData );  break;
	case 19: //"SpecialFontName",
		memcpy_s( Reg.SpecialFontName, 1024, lpData, cbData );  break;
	case 20: //"AutoMsg",
		memcpy_s( Reg.AutoMsg, 4, lpData, cbData );  break;
	case 21: //"AutoSkip",
		memcpy_s( Reg.AutoSkip, 4, lpData, cbData );  break;
	case 22: //"CursorHide",
		memcpy_s( Reg.CursorHide, 4, lpData, cbData );  break;
	case 23: //"CursorTime",
		memcpy_s( Reg.CursorTime, 4, lpData, cbData );  break;
	case 24: //"D3D.DisableTnL",
		memcpy_s( Reg.D3D_DisableTnL, 4, lpData, cbData );  break;
	case 25: //"D3D.Tex16",
		memcpy_s( Reg.D3D_Tex16, 4, lpData, cbData );  break;
	case 26: //"DeactivePlay",
		memcpy_s( Reg.DeactivePlay, 4, lpData, cbData );  break;
	case 27: //"Dialog",
		memcpy_s( Reg.Dialog, 4, lpData, cbData );  break;
	case 28: //"DisableCursor",
		memcpy_s( Reg.DisableCursor, 4, lpData, cbData );  break;
	case 29: //"DisablePan",
		memcpy_s( Reg.DisablePan, 4, lpData, cbData );  break;
	case 30: //"DisableQuick",
		memcpy_s( Reg.DisableQuick, 4, lpData, cbData );  break;
	case 31: //"DisplayMode",
		memcpy_s( Reg.DisplayMode, 4, lpData, cbData );  break;
	case 32: //"EffectSkip",
		memcpy_s( Reg.EffectSkip, 4, lpData, cbData );  break;
	case 33: //"FontEdge",
		memcpy_s( Reg.FontEdge, 4, lpData, cbData );  break;
	case 34: //"LogAlpha",
		memcpy_s( Reg.LogAlpha, 4, lpData, cbData );  break;
	case 35: //"MsgAlpha",
		memcpy_s( Reg.MsgAlpha, 4, lpData, cbData );  break;
	case 36: //"MsgPos",
		memcpy_s( Reg.MsgPos, 8, lpData, cbData );  break;
	case 37: //"MsgSpeed",
		memcpy_s( Reg.MsgSpeed, 4, lpData, cbData );  break;
	case 38: //"Mute",
		memcpy_s( Reg.Mute, 84, lpData, cbData );  break;
	case 39: //"RButtonMode",
		memcpy_s( Reg.RButtonMode, 4, lpData, cbData );  break;
	case 40: //"SelAuto",
		memcpy_s( Reg.SelAuto, 4, lpData, cbData );  break;
	case 41: //"SelSkip",
		memcpy_s( Reg.SelSkip, 4, lpData, cbData );  break;
	case 42: //"SimpleWindow",
		memcpy_s( Reg.SimpleWindow, 4, lpData, cbData );  break;
	case 43: //"SkipIcon",
		memcpy_s( Reg.SkipIcon, 4, lpData, cbData );  break;
	case 44: //"SkipType",
		memcpy_s( Reg.SkipType, 4, lpData, cbData );  break;
	case 45: //"SysVoice",
		memcpy_s( Reg.SysVoice, 4, lpData, cbData );  break;
	case 46: //"TextColor",
		memcpy_s( Reg.TextColor, 4, lpData, cbData );  break;
	case 47: //"UseDefaultFont",
		memcpy_s( Reg.UseDefaultFont, 4, lpData, cbData );  break;
	case 48: //"UseFilt",
		memcpy_s( Reg.UseFilt, 4, lpData, cbData );  break;
	case 49: //"VoiceSkip",
		memcpy_s( Reg.VoiceSkip, 4, lpData, cbData );  break;
	case 50: //"Volume",
		memcpy_s( Reg.Volume, 84, lpData, cbData );  break;
	case 51: //"WndPos"
		memcpy_s( Reg.WndPos, 8, lpData, cbData );  break;
	default:
		MessageBoxW(0, L"未知的写入指令！\r\n", COMMON_DLG_TITLE, MB_ICONINFORMATION);  break;
	}

	return ERROR_SUCCESS;
}
