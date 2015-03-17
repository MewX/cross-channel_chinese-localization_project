# CROSS†CHANNEL 中文化（汉化）项目
这里是 CROSS†CHANNEL 中文化（汉化）项目的**[网站](http://crosschannel.cn/)和程序源代码**。

目前我们完成的是“CROSS†CHANNEL 复刻版”的汉化工作，
**2016年我们的任务是“CROSS†CHANNEL -Final Complete”**。

## 汉化人员 STAFF

参与或为这部作品汉化做出贡献的网友名单。
（排名顺序如未特殊说明均**按照拼音首字母升序排列**）

### CROSS†CHANNEL 复刻版 v0.99 汉化补丁 @2015-03

> **都督&程序：**MewX<br/>
> **最终校对：**牙刷<br/>
> **全文校对：**烬、牙刷<br/>
> **全文翻译：**白崎穣、Eruption、Haven、黑须太2、刘阿斗、荔枝蝉、旅之灵夫2、
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

## 开源内容介绍

这里是每个小项目的**简要介绍**，具体的内容见每个文件夹内的README.md介绍。

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

### Others @master

其他的一些小工具，零散的代码。

- /EngineWorkOut

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

## LICENSE

    Copyright 2013 Andreas Stuetz

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
