# CROSS†CHANNEL 中文化（汉化）项目
这里是 CROSS†CHANNEL 中文化（汉化）项目的 [`网站`](http://crosschannel.cn/) 和`程序源代码`。

目前我们完成的是“CROSS†CHANNEL 复刻版”的汉化工作，
~2016年我们的任务是“CROSS†CHANNEL -Final Complete-”，“2017-2018年我们的任务是“少女们向荒野进发”。~
**然后就没了。**

## 汉化人员 STAFF

参与或为这部作品汉化做出贡献的网友名单。
（排名顺序如未特殊说明均**按照拼音首字母升序排列**）

### CROSS†CHANNEL 复刻版 v0.99 汉化补丁 @2015-03

> **都督&程序：**MewX<br/>
> **最终校对：**牙刷<br/>
> **全文校对：**烬、牙刷<br/>
> **全文翻译：**白崎穣、坂田铜时、Eruption、Haven、黑须太2、刘阿斗、荔枝蝉、旅之灵夫2、
> MarieL、姆Q的酱油瓶、秋田大学萝莉同好会会员甲、ScorpioAres、网特很多要HX、雅米多<br/>
> **图片编辑：**Revo<br/>
> **ＥＤ翻译：**kuon、牙刷、月山冥<br/>
> **ＥＤ字幕：**蝉猫<br/>
> **技术测试：**Chemstrike、Dandirion Aria、dxcayj、面皮贵、samidare、腽肭<br/>
>
> **全平台移植：**fk1995<br/>
>
> **程序协力：**夏侯飛燕<br/>
> **润色协力：**八矢夜乌、凤玄音、陌上初月、欺诈师RL、蚊子<br/>
> **翻译协力：**迟来的星、DDS、misaka10032、shamal0324、soul、童话karas、“田中ロミオ”<br/>
> **其他协力：**博士的逆袭、苍梓、了望的猪猪、妹控雪<br/>
>
> **鸣谢：（按时间顺序）**<br/>
> 希_ver、灵缡心 - 提供了在澄空发帖所需kx；<br/>
> noMeaning - 提供了2003版的特典脚本；<br/>
> OJI - 提供了迅雷会员账号供汉化组急用；<br/>
> 妹控雪 - 帮忙分流；<br/>
> Tam、三年 - 愿意帮忙繁化（组战略改变，暂不繁化）；<br/>
> 開心、帕拉丁、IO、EpicFail、dcxayj、代码菌、oathink等 - 热情关注我们汉化动态；<br/>
> 神音の森 - 无私地分享给汉化组CCFC资源；<br/>
> 镜月☆铃音汉化组 - 提供PSP版和PS3版的技术支持（组战略改变，暂不汉化）；<br/>
> **很多来应募却没有成功的，感谢你们的尝试和支持！**<br/>
> **广大吧友、坛友，感谢你们帮我们顶招募贴，帮我们宣传！**

#### 该版补丁制作流程

> 首先是文件包结构，均采用某商业单文件打包器打包。

> **CROSSCHANNEL_v0.99.exe**
- imgs/
  - CROSS+CHANNEL.jpg
  - pb_basic.png
  - pb01_m.png
  - pb02_m.png
  - pb03_m.png
  - pb04_m.png
  - pb05_m.png
  - pb06_m.png
  - pb07_m.png
  - pb08_m.png
  - white.jpg
- patch_files/
  - Chip_E_arc/
    - EFCCA0030.PNG
  - Chip_S_arc/
    - SGCC0003_PNG.png
    - SGCC0011_PNG.png
  - Chip_T_arc/
    - T1.MSK
    - T1_PNG.png
- Chip+.chs
- main.exe
- ED.dat
- highgui210.dll
- patchchs.dll
- Rio+.chs
- size_list.lst

> **UninstallChs.exe**
- textpack.bin
- main.exe

## 开源内容介绍

这里是每个小项目的**简要介绍**，具体的内容见每个文件夹内的README.md介绍。

### AllPlatforms @master

**Ren'Py的全平台移植版本，感谢@fk1995提供，据悉只能运行在特定Ren'Py版本上，所以欢迎大家贡献移植版的代码！！！**

### Scripts @master

汉化项目的全部译文，整个汉化项目的**核心成果**现已开源。

*11/19/2015* 增加了`附加剧本`和`朋友塔`的docx原始文本~

欢迎大家交流学习，可以在右边发`issue`，也可以在贴吧交流。

**禁止商用！！！禁止商用！！！禁止商用！！！遵循GPLv2-任何二次创作均需开源！！！**

### CrossChannel_Program @master

这是我用来解包封包的工具集（自己于写2012年末写的），**这套工具集是不可维护的**。
当时自己的编程水平非常渣，导致这套工具代码冗余度极高，而且也不易修改，
但是去年出序章补丁以及今年出的完整补丁还是一直在维护和使用这个工具，
**存在少量BUG和大量设计缺陷**，但并不影响正常使用。

另外，此工具在stdafx.h里面可以定义CROSSCHANNEL或者OTOMEGA的宏，
来提取“CROSS†CHANNEL”或者“乙女が紡ぐ恋のキャンバス”的封包、文本。

### PatchChs @master

这是2014年为了序章补丁写的工具，里面包含**3个工程**。
完整补丁也在使用，只是稍加维护，有不少缺陷，但是不影响用户体验。

之所以不重写维护这段重要的代码，是因为校对大哥突然开始全速校对文本了。
本来以为要明年才能汉化完的，结果今年就完成了，我各方面还没有做好准备呢~

- PatchChs

  这个工程生成PatchChs.dll的文件，游戏本身的exe导入表被我修改了，
我将advapi32.dll修改成了PatchChs.dll。
游戏原来使用的这个dll的作用是注册表的读写功能，
我们的汉化补丁为了**去除注册表依赖**，模拟了一个注册表读写功能，
即该工程PatchChs.dll，此文件会自动创建一个RegFile.chs虚拟注册表文件。

  这个dll的另一个功能是**负责补丁工作**，开启游戏的时候会检测是否已经安装补丁，
如果没有暗装，则会自动打包，动态生成汉化版需要的文件包。


- PatchChsRework

  这是以前没有使用git时创建的一个分支，这次做补丁的时候发现没有什么用了。


- PatchMonitor

  这个会以卸载程序的面目出现在补丁包中，即UninstallChs.exe。

  但同时这个工具如果传入了"-m"参数，则可以当作Monitor执行，提供按键监控功能。
在我们2015-03的汉化版本中，**添加了按下"\`/~"同步显示原文、按下"1/!"显示历史（非同步）功能**，
实际上就是通过PatchChs.dll启动的时候同时启动"UninstallChs.exe -m"来实现的。

### PatchFiles @master

部分与无关紧要的汉化补丁资源文件内容。

### Others @master

其他的一些小工具，零散的代码。

- EngineWorkOut/

  本来准备把整个引擎脚本给逆掉的，结果还是没有完成，里面是测试的一些动画效果截图。

- testpack.c

  测试局部封包的程序，最后融入PatchChs.dll中了。

- CountLine.bat

  一个统计行号的脚本。

- CalcRepeatment.cpp

  由于本游戏有很多重复的地方，于是就写了一个统计重复行的工具。
最终结果生成在“重复的文本信息.txt”文件中。

### Website @gh-pages

这个就是 http://crosschannel.cn 的网站啦，静态的没错，不过感谢GitHub提供服务器。

## Contributors

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://github.com/shuye02"><img src="https://avatars1.githubusercontent.com/u/22615765?v=4" width="100px;" alt=""/><br /><sub><b>Ye Shu</b></sub></a><br /><a href="https://github.com/MewX/cross-channel_chinese-localization_project/commits?author=shuye02" title="Documentation">📖</a></td>
    <td align="center"><a href="https://github.com/ddddyyyy"><img src="https://avatars1.githubusercontent.com/u/34983255?v=4" width="100px;" alt=""/><br /><sub><b>madyson</b></sub></a><br /><a href="#maintenance-ddddyyyy" title="Maintenance">🚧</a></td>
  </tr>
</table>

<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!
