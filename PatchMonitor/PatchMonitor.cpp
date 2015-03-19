// PatchMonitor.cpp : 定义应用程序的入口点。
//

#include "stdafx.h"
#include "PatchMonitor.h"

// func defs
wstring StringToWstring(UINT LocalOption, string str);
string WstringToString(UINT LocalOption, wstring wstr);
string int2str(long i);
LRESULT CALLBACK ChildProc(HWND hwnd, UINT message, WPARAM wParam, LPARAM lParam);
LRESULT CALLBACK HistoryProc(HWND hwnd, UINT message, WPARAM wParam, LPARAM lParam);
DWORD WINAPI ProcessThreadProc(PVOID pvParam);
DWORD WINAPI HistoryThreadProc(PVOID pvParam);

// var defs
const wchar_t *NotFound = L"（这句未找到匹配原文 _(:3」∠)_）";
HWND hParent = 0, hTextDlg = 0, hHistoryDlg = 0;
HANDLE hDlgThread, hHistoryThread;
HINSTANCE hInstGlobal;
LPDWORD lpThreadID;

// main
int APIENTRY WinMain(_In_ HINSTANCE hInstance,
                     _In_opt_ HINSTANCE hPrevInstance,
                     _In_ LPSTR    lpCmdLine,
                     _In_ int       nCmdShow)
{
	// Show CmdLine args
	//MessageBoxA( NULL, lpCmdLine, NULL, NULL );

	// Judge which
	if( !strcmp( lpCmdLine, "m" ) ) { // Work as the monitor

		/*  */
		//MessageBoxW( NULL, L"in monitoring", NULL, MB_OK );

		DWORD pid = 0;
		HWND hWnd;
		hInstGlobal = hInstance;

#ifdef LOG_ON
		// create folder
		WinExec("cmd /c mkdir logs_chs", SW_HIDE); // 1st
		CreateDirectoryW(L"logs_chs", NULL);       // 2nd
		_wmkdir(L"logs_chs");                      // 3rd

		fstream log;
		log.open((string("logs_chs") + "\\log" + int2str(time(NULL))+".txt").c_str(), ios::out | ios::trunc);

#endif

		//★All Right Reserved / 群青学园演剧部 C+C汉化委员会★
	ORI:
		// 读取启动窗口，更改标题栏
		// 这边测试过，在hijack.dll里面修改的话不能支持Unicode
		// 如果启动窗口隐藏了，要注意判断
		hWnd = FindWindowA( NULL, "启动设置" );
 		if( hWnd != NULL ) SetWindowTextW( hWnd, L"CROSS\u2020CHANNEL / 群青学院·群Ｘ会 (出品)" );
		
		// change title
		hWnd = FindWindowA( NULL, "zhCROSS+CHANNEL" );
 		if( hWnd == NULL ) { Sleep( 400 ); goto ORI; } // 找不到主窗口就一直循环，找到后继续执行
 		SetWindowTextW( hWnd, L"CROSS\u2020CHANNEL 内部测试β版 20150317" ); // CROSS\u2020CHANNEL 正式汉化版 v0.99 （附加功能挂载成功）
		hParent = hWnd;
 	
		// 侵入进程
#ifdef LOG_ON
		log << "hWnd = " << (long)hWnd << endl;
#endif

		// get pid
		int i = 0;
		while (pid == NULL) {
			if (!IsWindow(hWnd)) return 0;

#ifdef LOG_ON
			log << "trying times: " << ++ i << endl;
#endif
 			GetWindowThreadProcessId( hWnd, &pid );
			Sleep(100);
		}
#ifdef LOG_ON
		log << "pid = " << pid << endl;
#endif

		// get process handle
		i = 0;
		void *ph = 0;
		while (ph == NULL) {
			if (!IsWindow(hWnd)) return 0;

#ifdef LOG_ON
			log << "trying times: " << ++ i << endl;
#endif
			ph = OpenProcess(PROCESS_ALL_ACCESS, false, pid);
			Sleep(100);
		}
#ifdef LOG_ON
		log << "ph = " << (long)ph << endl;
#endif

		// Load "textpack.bin"
		FILE* fp = 0;
		fp = fopen("textpack.bin", "rb");
		if (!fp) {
			MessageBoxW(hWnd, L"找不到双语包！", L"无法正常启动", MB_OK);
			TerminateProcess(ph, 0);
			return 0;
		}

		fseek(fp, 0, SEEK_END);
		long fsiz = ftell(fp);
		fseek(fp, 0, SEEK_SET);

		char* buff = new char[fsiz]; // keep alive
		fread(buff, 1, fsiz, fp);
		fclose(fp);

#ifdef LOG_ON
		log << "Ready to create textpack." << endl;
#endif
		textFinder tf;
		tf.create(buff); // 导入数据

		// create window, THIS WILL CAUSE CRASH!!! I moved it into while{}
		/*static HWND hChild = CreateWindowW(L"STATIC", L"游戏原文", SWP_NOMOVE | SWP_NOSIZE | SW_HIDE, 0, 0, 400, 150, hWnd, NULL, hInstance, NULL);
		static HWND hText = CreateWindowExW(
			WS_EX_LEFT | WS_EX_LTRREADING | WS_EX_RIGHTSCROLLBAR, //dwExStyle 扩展样式
			L"Static", //lpClassName 窗口类名
			L"N/A", //lpWindowName 窗口标题
			SS_LEFT | WS_CHILD | WS_OVERLAPPED | WS_VISIBLE, //dwStyle 窗口样式
			0, //x 左边位置
			0, //y 顶边位置
			400, //nWidth 宽度
			130, //nHeight 高度
			hChild, //hWndParent 父窗口句柄
			NULL, //hMenu 菜单句柄
			NULL, //hInstance 应用程序句柄
			NULL //lpParam 附加参数
		);
		ShowWindow(hText, WS_VISIBLE);*/ 
 	
#ifdef LOG_ON
		log << "Ready to while." << endl;
#endif
		// 定义后面要用到的一些变量
		char FirstName[17] = { 0 }, SecondName[17] = { 0 }, temp[1024] = { 0 }, lpBuffer[256] = { 0 };
#ifdef LOG_ON
		bool OutputLog = false;
#endif
 		while( 1 ) {

			// Read TopTitle
			memset( temp, 0, sizeof( temp ) );
			BOOL b = ReadProcessMemory( ph, (void*)0x4FEE80, temp, 16, NULL );
			if( b && strcmp( temp, FirstName ) ) {
				strcpy( FirstName, temp );
#ifdef LOG_ON
				log << "TopName: " << FirstName << endl;
#endif
			}
		
			// Read SubTitle
			memset( temp, 0, sizeof( temp ) );
			b = ReadProcessMemory( ph, (void*)0x4F88E0, temp, 16, NULL );
			if( b && strcmp( temp, SecondName ) ) {
				strcpy( SecondName, temp );
#ifdef LOG_ON
				log << "  SubName: " << SecondName << endl;
#endif

				// convert to caps
				string temp = SecondName;
				transform(temp.begin(), temp.end(), temp.begin(), ::toupper);

#ifdef LOG_ON
				log << "tf.setfile: " << temp << endl;
#endif
				int rst = tf.setfile(temp.c_str());

				// need log
			}
			
			// read current showing text
	 		memset( temp, 0, sizeof( temp ) );
			b = ReadProcessMemory(
				ph,             
				(void*)0x4FE820,
				temp,           
				256,           
				NULL );

			if( b && strcmp( temp, lpBuffer ) ) {
				strcpy( lpBuffer, temp );
#ifdef LOG_ON
				OutputLog = false;
				log << "    " << lpBuffer << endl;
#endif
			}

			if (hTextDlg != NULL) {
				// purify
				int delta = 0, len = strlen(lpBuffer) + 1;
				for (int i = 0; i < len; i++) {
					while (lpBuffer[i] == '\\') {
						i += 2;
						delta += 2;
					}
					lpBuffer[i-delta] = lpBuffer[i];
				}

				// set text
				const char *fetchResult = 0;
				wstring realResult;
				int r = tf.find(lpBuffer, &fetchResult);
				realResult = r == FDR_W_NXL ? NotFound + StringToWstring(936, lpBuffer) : StringToWstring(932, fetchResult);

				SetWindowTextW(GetDlgItem(hTextDlg, IDC_STATICTEXT), realResult.c_str());
				//SetWindowTextA(hText, lpBuffer);
#ifdef LOG_ON
				if (!OutputLog){
					OutputLog = true;
					log << "\'`\' dlgshown: " << WstringToString(936, realResult) << " | " << lpBuffer << endl;
				}
#endif
			}

	 		// Read Content (`)VK_OEM_3
			if (GetAsyncKeyState(VK_OEM_3) < 0) {
				if (hHistoryDlg != NULL) {
					hHistoryDlg = NULL;
					TerminateThread(hHistoryThread, 0);
					hHistoryThread = 0;

					while (GetAsyncKeyState('1') < 0)
						Sleep(50);
				}

				if (hTextDlg == NULL) {
					// Abandoned codes
					/*hChild = CreateWindowW(L"STATIC", L"游戏原文", WS_CLIPCHILDREN | WS_CLIPSIBLINGS | WS_POPUP, 0, 0, 400, 200, NULL, NULL, hInstance, NULL);
					SetWindowLong(hChild, GWL_WNDPROC, (LONG)ChildProc);

					hText = CreateWindowExW(
						WS_EX_LEFT | WS_EX_LTRREADING | WS_EX_RIGHTSCROLLBAR, //dwExStyle 扩展样式
						L"Static", //lpClassName 窗口类名
						L"N/A", //lpWindowName 窗口标题
						SS_LEFT | WS_CHILD | WS_OVERLAPPED | WS_VISIBLE, //dwStyle 窗口样式
						10, //x 左边位置
						10, //y 顶边位置
						380, //nWidth 宽度
						180, //nHeight 高度
						hChild, //hWndParent 父窗口句柄
						NULL, //hMenu 菜单句柄
						NULL, //hInstance 应用程序句柄
						NULL //lpParam 附加参数
						);
					ShowWindow(hText, WS_VISIBLE);

					// set Font style
					HANDLE hFont = CreateFont(20, 0, 0, 0, FW_DONTCARE, FALSE, FALSE, FALSE, UNICODE,
						OUT_DEFAULT_PRECIS, CLIP_DEFAULT_PRECIS, DEFAULT_QUALITY, DEFAULT_PITCH | FF_SWISS, L"MS PGothic");
					SendMessageW(hText, WM_SETFONT, WPARAM(hFont), TRUE);
					ShowWindow(hChild, SW_SHOWNOACTIVATE);*/


					
					//DialogBoxW(hInstance, (LPCWSTR)IDD_DLGTEXT, NULL, (DLGPROC)ChildProc);// CreateDialogParamW(hInstance, (LPCTSTR)IDD_DLGTEXT, hWnd, (DLGPROC)ChildProc, NULL);
					
					hDlgThread = CreateThread(NULL, 100, ProcessThreadProc, NULL, 0, lpThreadID);
					while (hTextDlg == NULL)
						Sleep(50);
					SetActiveWindow(hWnd);
					// set Font style

					HANDLE hFont = CreateFontW(20, 0, 0, 0, FW_BOLD, FALSE, FALSE, FALSE, UNICODE,
						OUT_DEFAULT_PRECIS, CLIP_DEFAULT_PRECIS, DEFAULT_QUALITY, DEFAULT_PITCH | FF_SWISS, L"MS PGothic");
					SendMessageW(GetDlgItem(hTextDlg, IDC_STATICTEXT), WM_SETFONT, WPARAM(hFont), TRUE);
					// GetDlgItem( hDlg, IDC_DLG_LOGIN_EDIT_USERNAME )
					//MessageBoxA(hWnd, "test", "test", MB_OK);

					while (GetAsyncKeyState(VK_OEM_3) < 0)
						Sleep(50);
				}
				else {
					while (GetAsyncKeyState(VK_OEM_3) < 0)
						Sleep(50);

					hTextDlg = NULL;
					TerminateThread(hDlgThread, 0);
					hDlgThread = 0;
				}
				
			}

			// Show History window
			if (GetAsyncKeyState('1') < 0) {
				// close text dialog
				if (hTextDlg != NULL) {
					hTextDlg = NULL;
					TerminateThread(hDlgThread, 0);
					hDlgThread = 0;
				}

				// create history dialog
				if (hHistoryDlg == NULL) {
					hHistoryThread = CreateThread(NULL, 100, HistoryThreadProc, NULL, 0, lpThreadID);
					while (hHistoryDlg == NULL)
						Sleep(50);
					SetActiveWindow(hWnd);

					HANDLE hFont = CreateFont(20, 0, 0, 0, FW_DONTCARE, FALSE, FALSE, FALSE, UNICODE,
						OUT_DEFAULT_PRECIS, CLIP_DEFAULT_PRECIS, DEFAULT_QUALITY, DEFAULT_PITCH | FF_SWISS, L"MS PGothic");
					SendMessageW(GetDlgItem(hHistoryDlg, IDC_EDITHISTORY), WM_SETFONT, WPARAM(hFont), TRUE);

					while (GetAsyncKeyState('1') < 0)
						Sleep(50);

					// get latest index position
					unsigned long latestIndex = 0;
					memset(temp, 0, sizeof(temp));
					b = ReadProcessMemory(
						ph,
						(void*)0x6DB530, // latest index address
						temp,
						256,
						NULL);
					if (b)
						latestIndex = *(unsigned long *)temp; // get it
					else
						latestIndex = 512; // found value is 256, but it can be a little larger

					// load all history texts
					wstring result, resultBeg, resultEnd;
					const unsigned long posdelta = 0x1290;
					unsigned long pos = 0x6DC6D0;
					unsigned int index = 0;
					while (1) {
						memset(temp, 0, sizeof(temp));
						b = ReadProcessMemory(
							ph,
							(void*)pos,
							temp,
							256,
							NULL);
						pos += posdelta;

						// judge fetch succeeded
						if (b&&temp[0]!='\0') {
							// purify
							int delta = 0, len = strlen(temp) + 1;
							for (int i = 0; i < len; i++) {
								while (temp[i] == '\\') {
									i += 2;
									delta += 2;
								}
								temp[i - delta] = temp[i];
							}

							const char *fetchResult = 0;
							int r = tf.find(temp, &fetchResult);
							if (index++ < latestIndex)
								resultBeg += r == FDR_W_NXL ? NotFound + StringToWstring(936, temp) : StringToWstring(932, fetchResult) + L"\r\n\r\n";
							else
								resultEnd += r == FDR_W_NXL ? NotFound + StringToWstring(936, temp) : StringToWstring(932, fetchResult) + L"\r\n\r\n";

#ifdef LOG_ON
							log << "History Request:" << temp << endl;
#endif
						}
						else break;
					}
					result = resultEnd + resultBeg;

					// set text
					SetWindowTextW(GetDlgItem(hHistoryDlg, IDC_EDITHISTORY), result.c_str());
					PostMessage(GetDlgItem(hHistoryDlg, IDC_EDITHISTORY), WM_VSCROLL, SB_BOTTOM, 0);
				}
				else {
					while (GetAsyncKeyState('1') < 0)
						Sleep(50);

					hHistoryDlg = NULL;
					TerminateThread(hHistoryThread, 0);
					hHistoryThread = 0;
				}

			}

			// copy text
			if (GetAsyncKeyState(VK_F10) < 0) {
				//MessageBoxA(hWnd, "copy text", "get", MB_OK);

				if (OpenClipboard(hWnd))
				{
					//////////////////////////////////////////////////
					// purify
					int delta = 0, len = strlen(lpBuffer) + 1;
					for (int i = 0; i < len; i++) {
						while (lpBuffer[i] == '\\') {
							i += 2;
							delta += 2;
						}
						lpBuffer[i - delta] = lpBuffer[i];
					}

					// set text
					const char *fetchResult = 0;
					wstring realResult;
					int r = tf.find(lpBuffer, &fetchResult);
					realResult = r == FDR_W_NXL ? NotFound + StringToWstring(936, lpBuffer) : StringToWstring(932, fetchResult);

					// defs
					HGLOBAL clipBuffer;
					EmptyClipboard();
					
					// make text
					wstring result;
					result = L"原文：" + realResult // jpn
						+ L"\r\n译文：" + StringToWstring(936, lpBuffer) // chs
						+ L"\r\n纠误：\r\n";

					clipBuffer = GlobalAlloc(GMEM_DDESHARE, 2 * result.length() + sizeof(wchar_t));
					wcscpy((wchar_t*)GlobalLock(clipBuffer), result.c_str());
					GlobalUnlock(clipBuffer);
					SetClipboardData(CF_UNICODETEXT, clipBuffer);

					// clear
					CloseClipboard();
					TextOutW(GetDC(hWnd), 0, 0, L"复制成功！", wcslen(L"复制成功！"));

#ifdef LOG_ON
					//log
					log << "\'F10\' pressed: " << WstringToString(936, result) << endl;
#endif
				}
				else
					TextOutW(GetDC(hWnd), 0, 0, L"复制失败！", wcslen(L"复制失败！"));
			}

			// SLEEP
			if( !IsWindow( hWnd ) ) break;
	 		Sleep( 100 );
		}

		// GC
#ifdef LOG_ON
		log.close();
#endif
		delete[] buff;
	}
	else { // Work as uninstaller

		/* 作为卸载程序运行 */
		if( MessageBoxW( NULL, L"确定要删除CROSS\u2020CHANNEL汉化补丁吗？", L"卸载询问", MB_OKCANCEL ) == IDOK ) {
#ifdef RELEASE_DELETE
			// Delete all related files
			WinExec( "cmd /c del Chip_E.chs", SW_HIDE );
			WinExec( "cmd /c del Chip_S.chs", SW_HIDE );
			WinExec( "cmd /c del Chip_T.chs", SW_HIDE );
			WinExec( "cmd /c del RegFile.chs", SW_HIDE );
			WinExec( "cmd /c del CROSSCHANNEL_v0.99.exe", SW_HIDE );
#endif

			MessageBoxW( NULL, L"卸载完毕，很干净的哦！~ 我们会想你的~~\r\n再来光顾一下http://crosschannel.cn吧~~\r\n哦对了，如果这个卸载程序没有自删除还请手动删除一下~", L"卸载完毕", MB_OK );
			ShellExecuteA(NULL, "open", "http://www.crosschannel.cn", NULL, NULL, SW_SHOWNORMAL);

			// Delete self
			char    buf[MAX_PATH];
			HMODULE module;

			module = GetModuleHandleA(0);
			GetModuleFileNameA(module, buf, MAX_PATH);
			CloseHandle((HANDLE)4);

			__asm
			{
				lea     eax, buf
				push    0
				push    0
				push    eax
				push    ExitProcess
				push    module
				push    DeleteFileA
				push    UnmapViewOfFile
				ret
			}
		}
	}


	return 0;
}


/**
 * Functions
 **/
wstring StringToWstring(UINT LocalOption, string str)
{
	// 932 shift_jis ANSI/OEM Japanese; Japanese (Shift-JIS)
	// 936 gb2312 ANSI/OEM Simplified Chinese (PRC, Singapore); Chinese Simplified (GB2312)
	// 949 ks_c_5601-1987 ANSI/OEM Korean (Unified Hangul Code)
	// 950 big5 ANSI/OEM Traditional Chinese (Taiwan; Hong Kong SAR, PRC); Chinese Traditional (Big5)

	/*不是空字符串*/
	char *szAnsi = new char[str.length() + 1];
	for (UINT i = 0; i < str.length(); i++) {
		szAnsi[i] = str[i];
	}
	szAnsi[str.length()] = '\0';

	//setlocale( LC_ALL, "jpn" );
	//setlocale( LC_ALL, "chs" );
	//预转换，得到所需空间的大小
	int wcsLen = ::MultiByteToWideChar(LocalOption, NULL, szAnsi, strlen(szAnsi), NULL, 0);

	//分配空间要给'\0'留个空间，MultiByteToWideChar不会给'\0'空间
	wchar_t *wszString = new wchar_t[wcsLen + 1];
	::MultiByteToWideChar(LocalOption, NULL, szAnsi, strlen(szAnsi), wszString, wcsLen); //最后加上'\0' 
	wszString[wcsLen] = '\0';

	wstring wstr = wszString;
	//for ( UINT i = 0; i < wcslen( wszString ); i ++ ) {
	//	wstr += wszString[ i ];
	//}

	delete[] szAnsi;
	delete[] wszString;

	return wstr;
}

string int2str(long i) {
	string s;
	stringstream ss(s);
	ss << i;

	return ss.str();
}

string WstringToString(UINT LocalOption, wstring wstr)
{
	wchar_t *wszString = new wchar_t[wstr.length() + 1];
	wcscpy_s(wszString, wstr.length() + 1, wstr.c_str());
	wszString[wstr.length()] = '\0';
	//setlocale( LC_ALL, "jpn" );
	//setlocale( LC_ALL, "chs" );
	//预转换，得到所需空间的大小
	UINT strLen = ::WideCharToMultiByte(LocalOption, NULL, wszString, -1, NULL, 0, NULL, NULL);
	//分配空间不要给'\0'留个空间，WideCharToMultiByte会给'\0'空间
	char *szAnsi = new char[strLen];
	::WideCharToMultiByte(LocalOption, NULL, wszString, -1, szAnsi, strLen, NULL, NULL);
	szAnsi[strLen - 1] = '\0';

	string str = szAnsi;

	delete[] szAnsi;
	delete[] wszString;

	return str;
}

DWORD WINAPI ProcessThreadProc(PVOID pvParam)
{
	DialogBoxW(hInstGlobal, (LPCWSTR)IDD_DLGTEXT, NULL, (DLGPROC)ChildProc);

	return 0;
}

DWORD WINAPI HistoryThreadProc(PVOID pvParam)
{
	DialogBoxW(hInstGlobal, (LPCWSTR)IDD_DLGHISTORY, NULL, (DLGPROC)HistoryProc);

	return 0;
}

LRESULT CALLBACK ChildProc(HWND hwnd, UINT message, WPARAM wParam, LPARAM lParam)
{
	HDC hdc;
	HBRUSH hBr;

	switch (message)
	{
	case WM_INITDIALOG:
		// make a copy of hwnd
		hTextDlg = hwnd;

		// change window background
		hBr = CreateSolidBrush(RGB(77, 166, 255));
		SetClassLongPtr(hwnd, GCLP_HBRBACKGROUND, (LONG)hBr);
		break;

	case WM_LBUTTONDOWN:
		SendMessage(hwnd, WM_NCLBUTTONDOWN, HTCAPTION, 0);
		break;

	case WM_CTLCOLORSTATIC:
		// Set Text Color, and its background
		hdc = (HDC)wParam;
		if ((HWND)lParam == GetDlgItem(hwnd, IDC_STATICTEXT)) { // Set Specific Color
			SetTextColor((HDC)wParam, RGB(255, 255, 255));
		}
		SetBkMode((HDC)wParam, TRANSPARENT); // Set TRANSPARENT

		return (LRESULT)CreateSolidBrush(GetPixel(GetDC(hwnd), 1, 1));

	case WM_CLOSE:
		hTextDlg = NULL;
		DestroyWindow(hwnd);
		TerminateThread(hDlgThread, 0);
		break;
	}
	return DefWindowProc(hwnd, message, wParam, lParam);
}

LRESULT CALLBACK HistoryProc(HWND hwnd, UINT message, WPARAM wParam, LPARAM lParam)
{
	HDC hdc;
	HBRUSH hBr;

	switch (message)
	{
	case WM_INITDIALOG:
		// make a copy of hwnd
		hHistoryDlg = hwnd;

		// change window background
		hBr = CreateSolidBrush(RGB(77, 166, 255));
		SetClassLongPtr(hwnd, GCLP_HBRBACKGROUND, (LONG)hBr);
		break;

	case WM_LBUTTONDOWN:
		SendMessage(hwnd, WM_NCLBUTTONDOWN, HTCAPTION, 0);
		break;
		/*// This will cause refresh shadows, I didn't process with this problem
	case WM_CTLCOLORSTATIC:
		// Set Text Color, and its background
		hdc = (HDC)wParam;
		if ((HWND)lParam == GetDlgItem(hwnd, IDC_EDITHISTORY)) { // Set Specific Color
			SetTextColor((HDC)wParam, RGB(255, 255, 255));
		}
		SetBkMode((HDC)wParam, TRANSPARENT); // Set TRANSPARENT

		return (LRESULT)CreateSolidBrush(GetPixel(GetDC(hwnd), 1, 1));*/

	case WM_CLOSE:
		hHistoryDlg = NULL;
		DestroyWindow(hwnd);
		TerminateThread(hHistoryThread, 0);
		break;
	}
	return DefWindowProc(hwnd, message, wParam, lParam);
}
