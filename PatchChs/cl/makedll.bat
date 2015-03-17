rc PatchChsRework.rc
cl /o PatchChs.dll /LD DllMain.c PatchChsRework.res /link advapi32.lib gdi32.lib user32.lib
