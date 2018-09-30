// stdafx.h : 标准系统包含文件的包含文件，
// 或是经常使用但不常更改的
// 特定于项目的包含文件
//

#pragma once

#include "targetver.h"

#include <Windows.h>
#include <stdio.h>
#include <tchar.h>
#include <direct.h>
#include <io.h>
#include <iostream>
#include <fstream>
#include <string>
#include <Strsafe.h>

#define IOREVISION
/** < WillPlus Project List >
 *  CROSSCHANNEL
 *  OTOMEGA
 *  IO_REVISION_II
 **/

using namespace std;

#include "EasyUnicodeFileLE.h"
#include "ToolBox.h"
#include "crc32.h"
#include "textFinder.h"

// TODO: 在此处引用程序需要的其他头文件
#include "libbmp-0.1.3\bmpfile.h"
#pragma comment( lib, "..\\libs\\libbmp-0.1.3.gcc.lib" )
#include "CxImage600\xfile.h"
#include "CxImage600\ximage.h"
#include "CxImage600\ximath.h"
#pragma comment( lib, "..\\libs\\cximage600.vc6.lib" )

#include "lzss_enc.h"
#include "CrossChannelCrack.h"
