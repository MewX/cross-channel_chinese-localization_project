LoadPlugin("F:\Chinesization\CROSS+CHANNEL\subtitles\UnDot.dll")
#加载降噪滤镜
LoadPlugin("F:\Chinesization\CROSS+CHANNEL\subtitles\VSFilter.dll")
#加载字幕插件
LoadPlugin("F:\Chinesization\CROSS+CHANNEL\subtitles\DGDecode.dll")
#加载用于解码DVD（.d2v）的mpeg2格式的插件

DirectShowSource("F:\Chinesization\CROSS+CHANNEL\subtitles\ED.dat",convertFPS=True)
ConvertToYV12()


TextSub("F:\Chinesization\CROSS+CHANNEL\subtitles\ED_final.ass")









