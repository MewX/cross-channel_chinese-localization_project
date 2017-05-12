# game/translations.rpy
# Simplifield Chinese translated by Magicnight (magicnight@gmail.com), lxhbs (lxhbs333@gmail.com)
# for Ren'py 6.12.0

init python:

    # Translatable strings found in common/00developer.rpy

    config.translations[u'Developer Menu'] = u'开发者菜单'
    config.translations[u'Return to the developer menu'] = u'返回开发者菜单'

    # Translatable strings found in common/00library.rpy

    config.translations[u'Skip Mode'] = u''
    config.translations[u'Fast Skip Mode'] = u'快速跳过对话模式'
    config.translations[u"While Ren'Py games may be playable without the renpy module, some features may be disabled. For more information, read the module/README.txt file or go to http://www.bishoujo.us/renpy/."] = u"尽管没有renpy组件，Ren'py游戏也能运行，但一些游戏特性可能被禁用。需要更多信息请阅读module/README.txt文件或访问http://www.bishoujo.us/renpy/。"
    config.translations[u'renpy module not found.'] = u'未找到renpy组件'
    config.translations[u'The renpy module could not be loaded on your system.'] = u'renpy组件无法在您的系统上载入'
    config.translations[u'Old renpy module found.'] = u'找到renpy组件的旧版本'
    config.translations[u"An old version (%d) of the Ren'Py module was found on your system, while this game requires version %d."] = u"在您系统中发现一个旧版(%d)的Ren'py组件，但游戏需要的版本为%d。"
    config.translations[u'Please click to continue.'] = u'点击鼠标继续'

    # Translatable strings found in common/00menus.rpy

    config.translations[u'Start Game'] = u'开始游戏'
    config.translations[u'Load Game'] = u'读取进度'
    config.translations[u'Preferences'] = u'游戏选项'
    config.translations[u'Help'] = u'帮助'
    config.translations[u'Quit'] = u'退出'
    config.translations[u'Return'] = u'返回'
    config.translations[u'Save Game'] = u'保存游戏'
    config.translations[u'Main Menu'] = u'主菜单'
    config.translations[u'Are you sure you want to quit?'] = u'您确定要退出吗？'
    config.translations[u'Are you sure you want to return to the main menu?\nThis will lose unsaved progress.'] = u'您确定要退出吗？\n未保存的游戏进程将丢失。'

    # Translatable strings found in common/_layout/one_column_preferences.rpym

    config.translations[u'Display'] = u'显示'
    config.translations[u'Transitions'] = u'过渡效果'
    config.translations[u'Skip'] = u'跳过'
    config.translations[u'Begin Skipping'] = u'开始跳过'
    config.translations[u'After Choices'] = u'选择支之后'
    config.translations[u'Text Speed'] = u'文字速度'
    config.translations[u'Auto-Forward Time'] = u'自动前进时间'
    config.translations[u'Music Volume'] = u'音乐音量'
    config.translations[u'Sound Volume'] = u'音效音量'
    config.translations[u'Voice Volume'] = u'语音音量'
    config.translations[u'Joystick...'] = u'游戏杆...'

    # Translatable strings found in common/_layout/classic_yesno_prompt.rpym

    config.translations[u'Yes'] = u'是'
    config.translations[u'No'] = u'否'

    # Translatable strings found in common/_layout/scrolling_load_save.rpym

    config.translations[u'Empty Slot.'] = u'空栏位'
    config.translations[u'Are you sure you want to overwrite your save?'] = u'您确定要覆盖存档吗？'
    config.translations[u'Loading will lose unsaved progress.\nAre you sure you want to do this?'] = u'读取进度将丢失当前的游戏进程。\n您确定要这么做吗？'
    config.translations[u'q'] = u'q'
    config.translations[u'a'] = u'a'

    # Translatable strings found in common/_layout/classic_joystick_preferences.rpym

    config.translations[u'Not Assigned'] = u'未分配'
    config.translations[u'Joystick Mapping'] = u'游戏杆映射'
    config.translations[u'Left'] = u'左'
    config.translations[u'Right'] = u'右'
    config.translations[u'Up'] = u'上'
    config.translations[u'Down'] = u'下'
    config.translations[u'Select/Dismiss'] = u'选择/解除'
    config.translations[u'Rollback'] = u'回滚'
    config.translations[u'Hold to Skip'] = u'按键跳过'
    config.translations[u'Toggle Skip'] = u'按下保持跳过'
    config.translations[u'Hide Text'] = u'隐藏文字'
    config.translations[u'Menu'] = u'菜单'
    config.translations[u'Move the joystick or press a joystick button to create the mapping. Click the mouse to remove the mapping.'] = u'移动游戏杆或按游戏杆按键建立映射。单击鼠标移除映射。'

    # Translatable strings found in common/_layout/classic_preferences_common.rpym

    config.translations[u'Test'] = u'测试'
    config.translations[u'Window'] = u'窗口'
    config.translations[u'Fullscreen'] = u'全屏'
    config.translations[u'All'] = u'全部'
    config.translations[u'Some'] = u'部分'
    config.translations[u'None'] = u'无'
    config.translations[u'Seen Messages'] = u'看过的信息'
    config.translations[u'All Messages'] = u'全部信息'
    config.translations[u'Stop Skipping'] = u'停止跳过'
    config.translations[u'Keep Skipping'] = u'继续跳过'

    # Translatable strings found in common/_layout/classic_load_save.rpym

    config.translations[u'Auto'] = u'自动'
    config.translations[u'Quick'] = u'快速'
    config.translations[u'Previous'] = u'上一页'
    config.translations[u'Next'] = u'下一页'

    # Translatable strings found in common/_compat/gamemenu.rpym

    config.translations[u'The error message was:'] = u'出错信息为：'
    config.translations[u'You may want to try saving in a different slot, or playing for a while and trying again later.'] = u'您可尝试保存到其他栏位，或者继续进行游戏稍后再尝试保存。'
    config.translations[u'Save Failed.'] = u'保存失败。'
    config.translations[u'Quick save complete.'] = u''

    # Translatable strings found in common/_compat/preferences.rpym

    config.translations[u'Joystick Configuration'] = u'游戏杆设置'

    # Translatable strings found in common/_compat/mainmenu.rpym

    config.translations[u'Continue Game'] = u'继续游戏'
    
    #QMENU翻译
    config.translations[u'Q.Load'] = u'快速读取'
    config.translations[u'Q.Save'] = u'快速保存'
    config.translations[u'Load'] = u'读取'
    config.translations[u'Save'] = u'保存'
    config.translations[u'Prefs'] = u'设置'
    
    #RPG菜单翻译
    
    config.translations[u'Cancel'] = u'取消'
    
    
