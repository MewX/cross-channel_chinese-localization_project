# PatchChs

## cl

这个是没有使用git时的一个分支，用cl.exe命令行来编译的dll版本。

感觉这样生成的文件比VS生成的文件更小。

**用法**

- init.bat<br/>
  初始化环境变量，这个文件夹在我这里是“E:\\Program Files (x86)\\Microsoft Visual Studio 12.0\\VC\\vcvarsall.bat”。

- makedll.bat<br/>
  编译rc，然后编译dll。

## PatchChs

这个工程就是生成PatchChs.dll的工程。

作用是模拟注册表读写，以及启动汉化补丁扩展功能。

## PatchChs

没有使用git时的PatchChs的一个分支。内含cl.exe编译脚本。**（废弃）**

## PatchMonitor

外观上是卸载程序，实际上是汉化补丁辅助工具。

例如：游戏窗口标题不能显示十字架符号，必须使用外部进程才能修改，所以借用了这个卸载用的exe。

另外，显示原文的功能和复制原文译文到剪贴板的功能也是在这里实现的，监听了用户的按键操作。
