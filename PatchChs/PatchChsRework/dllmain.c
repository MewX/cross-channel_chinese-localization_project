// dllmain.cpp : 定义 DLL 应用程序的入口点。
#include "stdafx.h"

#pragma comment(linker, "/EXPORT:RegCloseKey=_HegCloseKey@4")
#pragma comment(linker, "/EXPORT:RegCreateKeyExA=_HegCreateKeyExA@36")
#pragma comment(linker, "/EXPORT:RegOpenKeyExA=_HegOpenKeyExA@20")
#pragma comment(linker, "/EXPORT:RegQueryValueExA=_HegQueryValueExA@24")
#pragma comment(linker, "/EXPORT:RegSetValueExA=_HegSetValueExA@24")

static HWND LoadWnd;
static HANDLE hThread;
static int nTime;
static HINSTANCE hInst_bak;
static LONG nOldStyle;

BOOL CALLBACK DlgProc( HWND hDlg, UINT message, WPARAM wParam, LPARAM lParam );
DWORD WINAPI ProcessThreadProc( PVOID pvParam );
DWORD WINAPI AnimeThreadProc( PVOID pvParam );


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
	case DLL_PROCESS_ATTACH:
		break;

    case DLL_THREAD_ATTACH:
        break;

	case DLL_THREAD_DETACH:
        break;

	case DLL_PROCESS_DETACH:
		break;
    }

    /* Returns TRUE on success, FALSE on failure */
    return TRUE;
}



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
#endif

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
#endif

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
#endif

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
#endif

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
#endif
	return ERROR_SUCCESS;
}

