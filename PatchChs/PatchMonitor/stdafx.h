// stdafx.h : 标准系统包含文件的包含文件，
// 或是经常使用但不常更改的
// 特定于项目的包含文件
//

#pragma once

#include "targetver.h"
#define RELEASE_DELETE
//#define LOG_ON // turn on log

#define WIN32_LEAN_AND_MEAN             //  从 Windows 头文件中排除极少使用的信息
// Windows 头文件:
#include <windows.h>
#include <shlobj.h>
#include <shellapi.h>

#define _CRT_SECURE_NO_WARNINGS

// C 运行时头文件
#include <cstdlib>
#include <algorithm>
#include <malloc.h>
#include <memory.h>
#include <tchar.h>
#include <time.h>
#include <string>
#include <sstream>
#include "textFinder.h"
#include "Resource.h"

#ifdef LOG_ON
#include <fstream>
#endif

using namespace std;


// TODO: 在此处引用程序需要的其他头文件
