
rc PatchChsRework.rc
cl /LD PatchChsRework.c stdafx.c dllmain.c PatchChsRework.res /link advapi32.lib gdi32.lib user32.lib
