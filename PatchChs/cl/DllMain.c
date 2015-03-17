#include "Common.h"

// Redirectors
#pragma comment(linker, "/EXPORT:RegCloseKey=_HegCloseKey")
#pragma comment(linker, "/EXPORT:RegCreateKeyExA=_HegCreateKeyExA")
#pragma comment(linker, "/EXPORT:RegOpenKeyExA=_HegOpenKeyExA")
#pragma comment(linker, "/EXPORT:RegQueryValueExA=_HegQueryValueExA")
#pragma comment(linker, "/EXPORT:RegSetValueExA=_HegSetValueExA")


#ifdef DEBUG
void HelloWorld( char* str )
{
    MessageBoxA( 0, str, "Hijacked Successfully!\n", MB_ICONINFORMATION );
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
		HelloWorld( "yo~" );
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
LONG __stdcall HegCloseKey(
    HKEY hKey // handle of key to close
    )
{
#ifdef SETALLLOG
    return RegCloseKey( hKey );
#endif

	return ERROR_SUCCESS;
}

LONG __stdcall HegCreateKeyExA(
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

	return ERROR_SUCCESS;
}

LONG __stdcall HegOpenKeyExA(
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

	return ERROR_SUCCESS;
}

LONG __stdcall HegQueryValueExA(
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

	return ERROR_SUCCESS;
}

LONG __stdcall HegSetValueExA(
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

	return ERROR_SUCCESS;
}
