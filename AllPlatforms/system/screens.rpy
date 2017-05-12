# Cross Channel on Ren'Py Ver 1.0 by fk
# All Rights Reserved 2015

screen shortcutkey:
    key "K_F1" action ShowMenu("config")
    key "K_F2" action ShowMenu("save")
    key "K_F3" action ShowMenu("load")
    key "K_F4" action HideInterface()
    key "K_F6" action Preference("auto-forward", "toggle")
    key "K_F7" action Preference("begin skipping")
    key "K_F8" action QuickSave(message='', newest=True)
    key "K_F12" action ShowMenu("shortcut")
    key "K_BACKQUOTE" action If(_preferences.language=="simplified_chinese",true = Language("japanese"),false=Language("simplified_chinese"))

##############################################################################
# Say
#
# Screen that's used to display adv-mode dialogue.
# http://www.renpy.org/doc/html/screen_special.html#say
screen say(who, what, side_image=None, two_window=False):
    # Decide if we want to use the one-window or two-window variant.
    if not two_window:

        # The one window variant.
       window:
                background None
                area (-5,600-190,796,174)
                id "window"
                fixed:
                    add "sys/"+"winbase0"+".png" alpha (persistent.windowop / 255.0) ypos -36 xpos 0
                    add  "sys/"+"winbase1"+".png"
                    text what id "what" slow_cps persistent.textspeed language "eastasian" size 23 color "fff" pos(17,19) xsize 700 kerning 1.05 line_spacing 5 font persistent.font


    else:

        # The two window variant.
        #vbox:
            #style "say_two_window_vbox"
            window:
                background None
                area (-5,600-190,796,174)
                id "window"
                fixed:
                    add "sys/"+"winbase0"+".png" alpha (persistent.windowop / 255.0) ypos -36 xpos 0
                    add  "sys/"+"winbase1"+".png"
                    text what id "what" slow_cps persistent.textspeed language "eastasian" size 23 color "fff" pos(17,19) xsize 700 kerning 1.05 line_spacing 5 font persistent.font

            if who:
                window:
                    background None
                    #style "say_who_window"
                    fixed:
                        add "sys/"+"win_nameb"+".png" alpha (persistent.windowop / 255.0) pos (-8,600-220)
                        add "sys/"+"win_namek"+".png" pos (1,600-220-5)
                        text who:
                            id "who"
                            xanchor 0.5
                            ypos 600-220+5
                            xcenter 1+268/2
                            language "eastasian"
                            size 23
                            color "fff"
                            bold False
                            kerning 1.05
                            line_spacing 5
                            font persistent.font
            
    
    imagebutton:
            area (800-42-26-20,600-113-45,80,21)
            hovered With(Dissolve(0.1))
            unhovered With(Dissolve(0.1))
            insensitive At("sys/"+"win_repeat_off"+".png",Transform(pos=(20,1)))
            idle At("sys/"+"win_repeat"+".png",Transform(pos=(20,1)))
            hover At("sys/"+"win_repeath"+".png",Transform(pos=(18,-1)))
            action VoiceReplay()
    

    imagebutton:
            area (800-42-20-20,600-113-20,80,20)
            hovered With(Dissolve(0.1))
            unhovered With(Dissolve(0.1))
            idle At("sys/"+"win_auto"+".png",Transform(pos=(20,1)))
            hover At("sys/"+"win_autoh"+".png",Transform(pos=(18,-1)))
            selected_idle At("sys/"+"win_autoh"+".png",Transform(pos=(18,-1)))
            action Preference("auto-forward", "toggle") 
    
    imagebutton:
            area (800-42-16-27,600-113+6,80,21)
            hovered With(Dissolve(0.1))
            unhovered With(Dissolve(0.1))
            idle At("sys/"+"win_skip"+".png",Transform(pos=(25,0)))
            hover At("sys/"+"win_skiph"+".png",Transform(pos=(23,-2)))
            selected_idle At("sys/"+"win_skiph"+".png",Transform(pos=(23,-2)))
            action Skip()
            
    imagebutton:
            area (800-42-26-20,600-113+30,80,21)
            hovered With(Dissolve(0.1))
            unhovered With(Dissolve(0.1))
            idle At("sys/"+"win_config"+".png",Transform(pos=(20,1)))
            hover At("sys/"+"win_configh"+".png",Transform(pos=(18,-1)))
            action ShowMenu("config",page=persistent.config)
    
    imagebutton:
            pos (2,600-34)
            hovered With(Dissolve(0.1))
            unhovered With(Dissolve(0.1))
            idle At("sys/"+"win_close"+".png",Transform())
            hover At("sys/"+"win_closeh"+".png",Transform())
            action HideInterface()
    
    imagebutton:
            area (181+110*0-20,600-24,80,21)
            hovered With(Dissolve(0.1))
            unhovered With(Dissolve(0.1))
            insensitive At("sys/"+"win_qload_off"+".png",Transform(pos=(13,0)))
            idle At("sys/"+"win_qload"+".png",Transform(pos=(13,0)))
            hover At("sys/"+"win_qloadh"+".png",Transform(pos=(11,-2)))
            action QuickLoad()
            
    imagebutton:
            area (181+110*1-20,600-24,80,21)
            hovered With(Dissolve(0.1))
            unhovered With(Dissolve(0.1))
            idle At("sys/"+"win_qsave"+".png",Transform(pos=(13,0)))
            hover At("sys/"+"win_qsaveh"+".png",Transform(pos=(11,-2)))
            action QuickSave(message='游戏进度已保存', newest=True)
            
    imagebutton:
            area (181+110*2-20,600-24,80,21)
            hovered With(Dissolve(0.1))
            unhovered With(Dissolve(0.1))
            idle At("sys/"+"win_load"+".png",Transform(pos=(18,0)))
            hover At("sys/"+"win_loadh"+".png",Transform(pos=(16,-2)))
            action ShowMenu("load")
            
    imagebutton:
            area (181+110*3-20,600-24,80,21)
            hovered With(Dissolve(0.1))
            unhovered With(Dissolve(0.1))
            idle At("sys/"+"win_save"+".png",Transform(pos=(17,0)))
            hover At("sys/"+"win_saveh"+".png",Transform(pos=(15,-2)))
            action ShowMenu("save")
    
    imagebutton:
            area (181+110*4-20,600-24,80,21)
            hovered With(Dissolve(0.1))
            unhovered With(Dissolve(0.1))
            idle At("sys/"+"win_log"+".png",Transform(pos=(21,0)))
            hover At("sys/"+"win_logh"+".png",Transform(pos=(19,-2)))
            action ShowMenu("text_history",transition=dissolve)
    key "rollback" action ShowMenu("text_history",transition=dissolve)
    if persistent.rclick == 1:
        key "game_menu" action ShowMenu("hidesay")
        
    elif persistent.rclick == 2:
        key "game_menu" action ShowMenu("text_history")
    elif persistent.rclick == 3:
        key "game_menu" action ShowMenu("save")
    use shortcutkey
screen hidesay:
    key "game_menu" action Return()
##############################################################################
# Choice
#
# Screen that's used to display in-game menus.
# http://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    use shortcutkey
    if persistent.mouse:
        on "show" action MouseMove(400,600*0.32,duration=0.6)
        on "replace" action MouseMove(400,600*0.32,duration=0.6)
    window:
        style "menu_window"
        xcenter 0.5
        
        ypos 0.29
        vbox:
            style "menu"
            spacing 12
            xcenter 0.5
            xpos 0.51

            for caption, action, chosen in items:

                if action:
                    
                    button:
                        background None
                        maximum (800,42)
                        idle_child Fixed(im.AlphaMask("sys/"+"selwin"+".png",im.MatrixColor("sys/"+"selwinm"+".png",im.matrix.invert())),At(Text(caption,style = "menu_choice",color="fff"),Transform(align=(0.5,1.0))))
                        hover_child Fixed(im.AlphaMask("sys/"+"selwinh"+".png",im.MatrixColor("sys/"+"selwinm"+".png",im.matrix.invert())),At(Text(caption,style = "menu_choice",color="fff"),Transform(align=(0.5,1.0))))
                        action action
                        #style "menu_choice_button"

                        

                else:
                    text caption style "menu_caption"

init -2:
    $ config.narrator_menu = True

    style menu_window is default

    style menu_choice is button_text:
        clear

    style menu_choice_button is button:
        xminimum int(config.screen_width * 0.75)
        xmaximum int(config.screen_width * 0.75)



##############################################################################
# Input
#
# Screen that's used to display renpy.input()
# http://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):

    window style "input_window":
        has vbox

        text prompt style "input_prompt"
        input id "input" style "input_text"

    use quick_menu

##############################################################################
# Nvl
#
# Screen used for nvl-mode dialogue and menus.
# http://www.renpy.org/doc/html/screen_special.html#nvl

screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            style "nvl_vbox"

        # Display dialogue.
        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id

                has hbox:
                    spacing 10

                if who is not None:
                    text who id who_id

                text what id what_id

        # Display a menu, if given.
        if items:

            vbox:
                id "menu"

                for caption, action, chosen in items:

                    if action:

                        button:
                            style "nvl_menu_choice_button"
                            action action

                            text caption style "nvl_menu_choice"

                    else:

                        text caption style "nvl_dialogue"

    add SideImage() xalign 0.0 yalign 1.0

    use quick_menu

##############################################################################
# Main Menu
#
# Screen that's used to display the main menu, when Ren'Py first starts
# http://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():
    use shortcutkey
    # This ensures that any other menu screen is replaced.
    tag menu
    on "show" action [Play("bgm","bgm/bgm001.ogg")]
    on "replace" action [If(renpy.music.is_playing(channel="bgm"),false = Play("bgm","bgm/bgm001.ogg"))]
    # The background of the main menu.
    window:
        style "mm_root"
        background "sys/x0000.bmp"
    imagebutton:
        idle Null(244,30)
        hover "sys/start.bmp"
        pos (279,284)
        action Start()
    imagebutton:
        pos (279,318)
        if len(renpy.list_slots(regexp='q.*')):
            idle Null(244,30)
            hover "sys/quickload.bmp"
            action QuickLoad()
        else:
            idle "sys/quickload_off.bmp"
            hover "sys/quickload_off.bmp"
            action NullAction()
    imagebutton:
        pos (279,318+34)
        if len(renpy.list_slots(regexp='[^qa_].*')):
            idle Null(244,30)
            hover "sys/load.bmp"
            action ShowMenu("load")
        else:
            idle "sys/load_off.bmp"
            hover "sys/load_off.bmp"
            action NullAction()
    imagebutton:
        pos (279,318+34*2)
        if persistent.clear:
            idle Null(244,30)
            hover "sys/omake.bmp"
            action ShowMenu("omake")
        else:
            idle "sys/omake_off.bmp"
            hover "sys/omake_off.bmp"
            action NullAction()
    imagebutton:
        idle Null(244,30)
        hover "sys/config.bmp"
        pos (279,318+34*3)
        action ShowMenu("config",page=persistent.config)
    imagebutton:
        idle Null(244,30)
        hover "sys/exit.bmp"
        pos (279,465)
        action Quit()
    # The main menu buttons.
    #frame:
    #    style_group "mm"
    #    xalign .98
    #    yalign .98

    #    has vbox

    #    textbutton _("Start Game") action Start()
    #    textbutton _("Load Game") action ShowMenu("load")
    #    textbutton _("Preferences") action ShowMenu("preferences")
    #    textbutton _("Help") action Help()
    #    textbutton _("Quit") action Quit(confirm=False)

#init -2:

    # Make all the main menu buttons be the same size.
    #style mm_button:
    #    size_group "mm"



##############################################################################
# Navigation
#
# Screen that's included in other screens to display the game menu
# navigation and background.
# http://www.renpy.org/doc/html/screen_special.html#navigation
screen navigation():

    # The background of the game menu.
    window:
        style "gm_root"

    # The various buttons.
    frame:
        style_group "gm_nav"
        xalign .98
        yalign .98

        has vbox

        textbutton _("Return") action Return()
        textbutton _("Preferences") action ShowMenu("preferences")
        textbutton _("Save Game") action ShowMenu("save")
        textbutton _("Load Game") action ShowMenu("load")
        textbutton _("Main Menu") action MainMenu()
        textbutton _("Help") action Help()
        textbutton _("Quit") action Quit()

init -2:

    # Make all game menu navigation buttons the same size.
    style gm_nav_button:
        size_group "gm_nav"


##############################################################################
# Save, Load
#
# Screens that allow the user to save and load the game.
# http://www.renpy.org/doc/html/screen_special.html#save
# http://www.renpy.org/doc/html/screen_special.html#load

# Since saving and loading are so similar, we combine them into
# a single screen, file_picker. We then use the file_picker screen
# from simple load and save screens.

screen file_picker(save=True):
    use shortcutkey
    default page = 1
    window:
        if save:
            background "sys/x0200.png"
        else:
            background "sys/x0300.png"
    imagemap:
        pos (24,145)
        ground Null()
        cache False
        idle "sys/LOAD_WIP+014+23x144y.png"
        hover "sys/LOAD_WIP+015+23x144y.png"
        selected_idle "sys/LOAD_WIP+016+23x144y.png"
        selected_hover "sys/LOAD_WIP+016+23x144y.png"
        for i in range(0,10):
            hotspot (0,38*i,81,28):
                action [FilePage(i+1),SetScreenVariable("page",i+1)]
        hotspot (0,38*10,81,28):
                action [FilePage("auto")]
    if FileCurrentPage()!="auto":
        grid 2 5:
            pos (120,101)
            transpose True
            for i in range (1,11):
                    imagebutton:
                        idle LiveComposite((335,90),(0,0),"sys/loadr1btn.png",(10,6),FileScreenshot(i))
                        hover LiveComposite((335,90),(0,0),"sys/loadr2btn.png",(10,6),FileScreenshot(i))
                        selected_idle LiveComposite((335,90),(0,0),"sys/loadr2btn.png",(10,6),FileScreenshot(i))
                        selected_hover LiveComposite((335,90),(0,0),"sys/loadr2btn.png",(10,6),FileScreenshot(i))
                        action FileAction(i)
        fixed:
            grid 2 5:
                pos (112,101)
                transpose True
                for i in range (1,11):
                    button:
                        background None
                        xysize (335,90)
                        text u"■"+("%02d"%(i+(int(FileCurrentPage())-1)*10)):
                            color "14274b"
                            pos (267-120,14)
                            size 13
        fixed:
            
            grid 2 5:
                pos (152,101)
                transpose True
                for i in range (1,11):
                    $ file_time = FileTime(i,format="%Y/%m/%d %H:%M", empty=("----/--/-- --:--"))
                    button:
                        background None
                        xysize (335,90)
                        text file_time:
                            color "14274b"
                            xalign 1.0
                            pos (387-120,14)
                            size 13
        fixed:
            grid 2 5:
                pos (152,101)
                transpose True
                for i in range (1,11):
                    $ n = FileSaveName(i)
                    button:
                        background None
                        xysize (335,90)
                        text n:
                            xysize (150,40)
                            color "14274b"
                            pos (237-120,29)
                            size 13
                            language "eastasian"
        fixed:
            grid 2 5:
                pos (152,101)
                transpose True
                for i in range (1,11):
                    button:
                        background None
                        xysize (335,90)
                        $ file_name = FileSlotName(i, 10)
                        if FileNewest(file_name):
                            add "sys/new.png" pos (221-152,135-101)
    else:
        grid 2 5:
            pos (120,101)
            transpose True
            for i in range (1,6):
                    imagebutton:
                        idle LiveComposite((335,90),(0,0),"sys/loadr1btn.png",(10,6),FileScreenshot(i,page="auto"))
                        hover LiveComposite((335,90),(0,0),"sys/loadr2btn.png",(10,6),FileScreenshot(i,page="auto"))
                        selected_idle LiveComposite((335,90),(0,0),"sys/loadr2btn.png",(10,6),FileScreenshot(i,page="auto"))
                        selected_hover LiveComposite((335,90),(0,0),"sys/loadr2btn.png",(10,6),FileScreenshot(i,page="auto"))
                        action FileAction(i,page = "auto")
            for i in range (6,11):
                    imagebutton:
                        idle LiveComposite((335,90),(0,0),"sys/loadr1btn.png",(10,6),FileScreenshot(i-5,page="quick"))
                        hover LiveComposite((335,90),(0,0),"sys/loadr2btn.png",(10,6),FileScreenshot(i-5,page="quick"))
                        selected_idle LiveComposite((335,90),(0,0),"sys/loadr2btn.png",(10,6),FileScreenshot(i-5,page="quick"))
                        selected_hover LiveComposite((335,90),(0,0),"sys/loadr2btn.png",(10,6),FileScreenshot(i-5,page="quick"))
                        action FileAction(i-5,page = "quick")
        fixed:
            grid 2 5:
                pos (112,101)
                transpose True
                for i in range (1,6):
                    button:
                        background None
                        xysize (335,90)
                        text u"■Auto"+str(i):
                            color "14274b"
                            pos (267-120,14)
                            size 13
                for i in range (6,11):
                    button:
                        background None
                        xysize (335,90)
                        text u"■Quick"+str(i-5):
                            color "14274b"
                            pos (267-120,14)
                            size 13
        fixed:
            
            grid 2 5:
                pos (152,101)
                transpose True
                for i in range (1,6):
                    $ file_time = FileTime(i,format="%Y/%m/%d %H:%M", empty=("----/--/-- --:--"),page="auto")
                    button:
                        background None
                        xysize (335,90)
                        text file_time:
                            color "14274b"
                            xalign 1.0
                            pos (387-120,14)
                            size 13
                for i in range (6,11):
                    $ file_time = FileTime(i-5,format="%Y/%m/%d %H:%M", empty=("----/--/-- --:--"),page="quick")
                    button:
                        background None
                        xysize (335,90)
                        text file_time:
                            color "14274b"
                            xalign 1.0
                            pos (387-120,14)
                            size 13
        fixed:
            
            grid 2 5:
                pos (152,101)
                transpose True
                for i in range (1,6):
                    $ n = FileSaveName(i,page="auto")
                    button:
                        background None
                        xysize (335,90)
                        text n:
                            color "14274b"
                            pos (237-120,29)
                            size 13
                for i in range (6,11):
                    $ n = FileSaveName(i-5,page="quick")
                    button:
                        background None
                        xysize (335,90)
                        text n:
                            color "14274b"
                            pos (237-120,29)
                            size 13
        fixed:
            grid 2 5:
                pos (152,101)
                transpose True
                for i in range (1,6):
                    button:
                        background None
                        xysize (335,90)
                        $ file_name = "auto-"+str(i)
                        if FileNewest(file_name):
                            add "sys/new.png" pos (221-152,135-101)
                for i in range (6,11):
                    button:
                        background None
                        xysize (335,90)
                        $ file_name = "quick-"+str(i-5)
                        if FileNewest(file_name):
                            add "sys/new.png" pos (221-152,135-101)

screen shortcut:
    tag menu
    window:
        background "sys/shortcut.bmp"
    use menu_top(page=6)
    use menu_bottom


screen save():
    if len(current_line[1].encode("utf-8"))/3 <= 10:
        timer 0.5 action SetVariable("save_name",current_line[1])
    # This ensures that any other menu screen is replaced.
    tag menu

    use file_picker
    use menu_top(page=4)
    use menu_bottom

screen load():

    # This ensures that any other menu screen is replaced.
    tag menu

    use file_picker(save=False)
    use menu_top(page=5)
    use menu_bottom

init -2:
    style file_picker_frame is menu_frame
    style file_picker_nav_button is small_button
    style file_picker_nav_button_text is small_button_text
    style file_picker_button is large_button
    style file_picker_text is large_button_text


##############################################################################
# Preferences
#
# Screen that allows the user to change the preferences.
# http://www.renpy.org/doc/html/screen_special.html#prefereces

screen menu_top(page=1):
    key "game_menu" action Return()
    if page!=1:
        imagebutton:
            pos (41,5)
            idle im.AlphaMask("sys/"+"top_config1"+".png",im.MatrixColor("sys/"+"topm"+".png",im.matrix.invert()))
            hover im.AlphaMask("sys/"+"top_config1h"+".png",im.MatrixColor("sys/"+"topm"+".png",im.matrix.invert()))
            action [ShowMenu("config",page=1),SetField(persistent,"config",1)]
    if page!=2:
        imagebutton:
            pos (41 + 121,5)
            idle im.AlphaMask("sys/"+"top_config2"+".png",im.MatrixColor("sys/"+"topm"+".png",im.matrix.invert()))
            hover im.AlphaMask("sys/"+"top_config2h"+".png",im.MatrixColor("sys/"+"topm"+".png",im.matrix.invert()))
            action [ShowMenu("config",page=2),SetField(persistent,"config",2)]
    if page!=3:
        imagebutton:
            pos (41 + 121*2,5)
            idle im.AlphaMask("sys/"+"top_config3"+".png",im.MatrixColor("sys/"+"topm"+".png",im.matrix.invert()))
            hover im.AlphaMask("sys/"+"top_config3h"+".png",im.MatrixColor("sys/"+"topm"+".png",im.matrix.invert()))
            action [ShowMenu("config",page=3),SetField(persistent,"config",3)]
    if page!=4 and in_game:
        imagebutton:
            pos (41 + 121*3,5)
            idle im.AlphaMask("sys/"+"top_save"+".png",im.MatrixColor("sys/"+"topm"+".png",im.matrix.invert()))
            hover im.AlphaMask("sys/"+"top_saveh"+".png",im.MatrixColor("sys/"+"topm"+".png",im.matrix.invert()))
            action ShowMenu("save")
    elif not in_game:
        add im.AlphaMask("sys/"+"top_save"+".png",im.MatrixColor("sys/"+"topm"+".png",im.matrix.invert())) pos (41 + 121*3,5)
    if page!=5:
        imagebutton:
            pos (41 + 121*4,5)
            idle im.AlphaMask("sys/"+"top_load"+".png",im.MatrixColor("sys/"+"topm"+".png",im.matrix.invert()))
            hover im.AlphaMask("sys/"+"top_loadh"+".png",im.MatrixColor("sys/"+"topm"+".png",im.matrix.invert()))
            action ShowMenu("load")
    if page!=6:
        imagebutton:
            pos (41 + 121*5,5)
            idle im.AlphaMask("sys/"+"top_shortcut"+".png",im.MatrixColor("sys/"+"topm"+".png",im.matrix.invert()))
            hover im.AlphaMask("sys/"+"top_shortcuth"+".png",im.MatrixColor("sys/"+"topm"+".png",im.matrix.invert()))
            action ShowMenu("shortcut")

screen menu_bottom:
    imagebutton:
        pos 800-290+73*(1-1),600-35
        idle im.AlphaMask("sys/"+"navi_back"+".png",im.MatrixColor("sys/"+"navim"+".png",im.matrix.invert()))
        hover im.AlphaMask("sys/"+"navi_backh"+".png",im.MatrixColor("sys/"+"navim"+".png",im.matrix.invert()))
        action [mr.Stop(),Return()]
    imagebutton:
        pos 800-290+73*(2-1),600-35
        idle im.AlphaMask("sys/"+"navi_title"+".png",im.MatrixColor("sys/"+"navim"+".png",im.matrix.invert()))
        hover im.AlphaMask("sys/"+"navi_titleh"+".png",im.MatrixColor("sys/"+"navim"+".png",im.matrix.invert()))
        action MainMenu()
    imagebutton:
        pos 800-290+73*(3-1),600-35
        idle im.AlphaMask("sys/"+"navi_quit"+".png",im.MatrixColor("sys/"+"navim"+".png",im.matrix.invert()))
        hover im.AlphaMask("sys/"+"navi_quith"+".png",im.MatrixColor("sys/"+"navim"+".png",im.matrix.invert()))
        action Quit()

screen config(page = 1):
    use shortcutkey
    tag menu
    default tt = Tooltip(Null())
    window:
        background "sys/cfg_bg.png"
    if page == 1:
        add im.AlphaMask("sys/"+"config1bg"+".bmp","sys/"+"config1bgm"+".bmp") pos (41,5)
        
        imagemap:
            pos (348,111)
            ground Null()
            cache False
            idle im.AlphaMask("sys/config1_button_idle.bmp","sys/config1_button_idle_mask.bmp")
            hover im.AlphaMask("sys/config1_button_hover.bmp","sys/config1_button_hover_mask.bmp")
            selected_idle im.AlphaMask("sys/config1_button_selected.bmp","sys/config1_button_selected_mask.bmp")
            selected_hover im.AlphaMask("sys/config1_button_selected.bmp","sys/config1_button_selected_mask.bmp")
            hotspot (0,0,90,28):
                action Preference("display", "window")
                hovered tt.action(im.AlphaMask("sys/CFGBG_WIP+056+47x450y.bmp","sys/CFGBG_MSK+056+47x450y.bmp"))
            hotspot (108,0,123,28):
                action Preference("display", "fullscreen")
                hovered tt.action(im.AlphaMask("sys/CFGBG_WIP+057+47x450y.bmp","sys/CFGBG_MSK+057+47x450y.bmp"))
            hotspot (0,38,80,28):
                action Preference("transitions", "all")
                hovered tt.action(im.AlphaMask("sys/CFGBG_WIP+064+47x450y.bmp","sys/CFGBG_MSK+064+47x450y.bmp"))
            hotspot (196,38,80,28):
                action Preference("transitions", "none")
                hovered tt.action(im.AlphaMask("sys/CFGBG_WIP+066+47x450y.bmp","sys/CFGBG_MSK+066+47x450y.bmp"))
            hotspot (0,76,80,28):
                action [SetField(persistent,"mouse",True),SelectedIf(persistent.mouse)]
                hovered tt.action(im.AlphaMask("sys/CFGBG_WIP+068+47x450y.bmp","sys/CFGBG_MSK+068+47x450y.bmp"))
            hotspot (98,76,80,28):
                action [SetField(persistent,"mouse",False),SelectedIf(not persistent.mouse)]
                hovered tt.action(im.AlphaMask("sys/CFGBG_WIP+068+47x450y.bmp","sys/CFGBG_MSK+068+47x450y.bmp"))
            hotspot (0,114,80,28):
                action [SetField(persistent,"mousehide",5),SelectedIf(persistent.mousehide == 5)]
                hovered tt.action(im.AlphaMask("sys/CFGBG_WIP+070+47x450y.bmp","sys/CFGBG_MSK+070+47x450y.bmp"))
            hotspot (98,114,80,28):
                action [SetField(persistent,"mousehide",30),SelectedIf(persistent.mousehide == 30)]
                hovered tt.action(im.AlphaMask("sys/CFGBG_WIP+070+47x450y.bmp","sys/CFGBG_MSK+070+47x450y.bmp"))
            hotspot (98*2,114,80,28):
                action [SetField(persistent,"mousehide",0),SelectedIf(persistent.mousehide == 0)]
                hovered tt.action(im.AlphaMask("sys/CFGBG_WIP+070+47x450y.bmp","sys/CFGBG_MSK+070+47x450y.bmp"))
            hotspot (0,152,122,28):
                action [SetField(persistent,"rclick",1),SelectedIf(persistent.rclick == 1)]
                hovered tt.action(im.AlphaMask("sys/CFGBG_WIP+073+46x450y.bmp","sys/CFGBG_MSK+073+46x450y.bmp"))
            hotspot (140,152,102,28):
                action [SetField(persistent,"rclick",2),SelectedIf(persistent.rclick == 2)]
                hovered tt.action(im.AlphaMask("sys/CFGBG_WIP+073+46x450y.bmp","sys/CFGBG_MSK+073+46x450y.bmp"))
            hotspot (260,152,80,28):
                action [SetField(persistent,"rclick",3),SelectedIf(persistent.rclick == 3)]
                hovered tt.action(im.AlphaMask("sys/CFGBG_WIP+073+46x450y.bmp","sys/CFGBG_MSK+073+46x450y.bmp"))
            hotspot (0,190,80,28):
                action [SetField(persistent,"icon",True),SelectedIf(persistent.icon)]
                hovered tt.action(im.AlphaMask("sys/CFGBG_WIP+067+47x450y.bmp","sys/CFGBG_MSK+067+47x450y.bmp"))
            hotspot (98,190,80,28):
                action [SetField(persistent,"icon",False),SelectedIf(not persistent.icon)]
                hovered tt.action(im.AlphaMask("sys/CFGBG_WIP+067+47x450y.bmp","sys/CFGBG_MSK+067+47x450y.bmp"))
            hotspot (0,228,80,28):
                action [SetField(persistent,"confirm",True),SelectedIf(persistent.confirm)]
                hovered tt.action(im.AlphaMask("sys/CFGBG_WIP+069+47x450y.bmp","sys/CFGBG_MSK+069+47x450y.bmp"))
            hotspot (98,228,80,28):
                action [SetField(persistent,"confirm",False),SelectedIf(not persistent.confirm)]
                hovered tt.action(im.AlphaMask("sys/CFGBG_WIP+069+47x450y.bmp","sys/CFGBG_MSK+069+47x450y.bmp"))
            hotspot (0,228+38,80,28):
                action [SetField(persistent,"run_in_background",True),SelectedIf(persistent.run_in_background)]
                hovered tt.action(im.AlphaMask("sys/CFGBG_WIP+071+47x450y.bmp","sys/CFGBG_MSK+071+47x450y.bmp"))
            hotspot (98,228+38,80,28):
                action [SetField(persistent,"run_in_background",False),SelectedIf(not persistent.run_in_background)]
                hovered tt.action(im.AlphaMask("sys/CFGBG_WIP+071+47x450y.bmp","sys/CFGBG_MSK+071+47x450y.bmp"))
    elif page == 2:
        default bar1 = Tooltip(LiveCrop((0,0,166,9),im.AlphaMask("sys/CFGBG_WIP+030+288x158y.bmp","sys/CFGBG_MSK+030+288x158y.bmp")))
        default bar2 = Tooltip(LiveCrop((264,165,166,9),im.AlphaMask("sys/CFGBG_WIP+030+288x158y.bmp","sys/CFGBG_MSK+030+288x158y.bmp")))
        add im.AlphaMask("sys/"+"config2bg"+".png","sys/"+"config2bgm"+".bmp") pos (41,5)
        add bar1.value pos 289,159
        add bar2.value pos 289+264,159+165
        imagemap:
            pos (154,111)
            cache False
            ground Null()
            idle im.AlphaMask("sys/config2_button_idle.bmp","sys/config2_button_idle_mask.bmp")
            hover im.AlphaMask("sys/config2_button_hover.bmp","sys/config2_button_hover_mask.bmp")
            selected_idle im.AlphaMask("sys/config2_button_selected.bmp","sys/config2_button_selected_mask.bmp")
            selected_hover im.AlphaMask("sys/config2_button_selected.bmp","sys/config2_button_selected_mask.bmp")
            hotspot (103,0,80,28):
                action [SetField(persistent,"textspeed",10),SelectedIf(persistent.textspeed == 10)]
                hovered tt.action(im.AlphaMask("sys/CFGBG_WIP+074+46x450y.bmp","sys/CFGBG_MSK+074+46x450y.bmp"))
            hotspot (194,0,80,28):
                action [SetField(persistent,"textspeed",20),SelectedIf(persistent.textspeed == 20)]
                hovered tt.action(im.AlphaMask("sys/CFGBG_WIP+074+46x450y.bmp","sys/CFGBG_MSK+074+46x450y.bmp"))
            hotspot (285,0,80,28):
                action [SetField(persistent,"textspeed",30),SelectedIf(persistent.textspeed == 30)]
                hovered tt.action(im.AlphaMask("sys/CFGBG_WIP+074+46x450y.bmp","sys/CFGBG_MSK+074+46x450y.bmp"))
            hotspot (376,0,80,28):
                action [SetField(persistent,"textspeed",50),SelectedIf(persistent.textspeed == 50)]
                hovered tt.action(im.AlphaMask("sys/CFGBG_WIP+074+46x450y.bmp","sys/CFGBG_MSK+074+46x450y.bmp"))
            hotspot (467,0,80,28):
                action [SetField(persistent,"textspeed",0),SelectedIf(persistent.textspeed == 0)]
                hovered tt.action(im.AlphaMask("sys/CFGBG_WIP+074+46x450y.bmp","sys/CFGBG_MSK+074+46x450y.bmp"))
            hotspot (0,76,91,28):
                action [SetField(persistent,"font","default.ttc"),SetField(persistent,"fontname","文泉驿微米黑"),SelectedIf(persistent.font == "default.ttc")]
                hovered tt.action(im.AlphaMask("sys/CFGBG_WIP+076+46x450y.bmp","sys/CFGBG_MSK+076+46x450y.bmp"))
            hotspot (103,76,80,28):
                action [SetField(persistent,"font","fonts/Siyuanheiti.otf"),SetField(persistent,"fontname","思源黑体"),SelectedIf(persistent.font != "default.ttc")]
                hovered tt.action(im.AlphaMask("sys/CFGBG_WIP+077+46x450y.bmp","sys/CFGBG_MSK+077+46x450y.bmp"))
            hotspot (0,203,91,28):
                action Preference("skip", "seen")
                hovered tt.action(im.AlphaMask("sys/CFGBG_WIP+078+46x450y.bmp","sys/CFGBG_MSK+078+46x450y.bmp"))
            hotspot (102,203,80,28):
                action Preference("skip", "all")
                hovered tt.action(im.AlphaMask("sys/CFGBG_WIP+079+46x450y.bmp","sys/CFGBG_MSK+079+46x450y.bmp"))
            hotspot (0,272,81,28):
                action Preference("after choices", "skip")
                hovered tt.action(im.AlphaMask("sys/CFGBG_WIP+080+46x450y.bmp","sys/CFGBG_MSK+080+46x450y.bmp"))
            hotspot (92,272,80,28):
                action Preference("after choices", "stop")
                hovered tt.action(im.AlphaMask("sys/CFGBG_WIP+080+46x450y.bmp","sys/CFGBG_MSK+080+46x450y.bmp"))
            hotspot (348,272,81,28):
                action Preference("auto-forward after click", "disable")
                hovered tt.action(im.AlphaMask("sys/CFGBG_WIP+082+46x450y.bmp","sys/CFGBG_MSK+082+46x450y.bmp"))
            hotspot (440,272,80,28):
                action Preference("auto-forward after click", "enable")
                hovered tt.action(im.AlphaMask("sys/CFGBG_WIP+082+46x450y.bmp","sys/CFGBG_MSK+082+46x450y.bmp"))
        
        
        textbutton "思源黑体" text_font "fonts/Siyuanheiti.otf" action [SetField(persistent,"font","fonts/Siyuanheiti.otf"),SetField(persistent,"fontname","思源黑体"),SensitiveIf(persistent.font != "default.ttc"),SelectedIf(persistent.font == "fonts/Siyuanheiti.otf")] pos (90,223) text_size 20 text_color "fff" text_selected_color "fff799" text_selected_outlines [(1,"2999cb",0,0)] text_insensitive_color "ddd"
        
        textbutton "方正兰亭黑" text_font "fonts/Lantinghei.ttf" action [SetField(persistent,"font","fonts/Lantinghei.ttf"),SetField(persistent,"fontname","方正兰亭黑"),SensitiveIf(persistent.font != "default.ttc"),SelectedIf(persistent.font == "fonts/Lantinghei.ttf")] pos (90,255) text_size 20 text_color "fff" text_selected_color "fff799" text_selected_outlines [(1,"2999cb",0,0)] text_insensitive_color "ddd"
        
        
        textbutton "冬青黑体" text_font "fonts/Dongqingheiti.otf" action [SetField(persistent,"font","fonts/Dongqingheiti.otf"),SetField(persistent,"fontname","冬青黑体"),SensitiveIf(persistent.font != "default.ttc"),SelectedIf(persistent.font == "fonts/Dongqingheiti.otf")] pos (210,223) text_size 20 text_color "fff" text_selected_color "fff799" text_selected_outlines [(1,"2999cb",0,0)] text_insensitive_color "ddd"
        
        textbutton "雅黑" text_font "fonts/yahei.ttf" action [SetField(persistent,"font","fonts/yahei.ttf"),SetField(persistent,"fontname","雅黑"),SensitiveIf(persistent.font != "default.ttc"),SelectedIf(persistent.font == "fonts/yahei.ttf")] pos (210,255) text_size 20 text_color "fff" text_selected_color "fff799" text_selected_outlines [(1,"2999cb",0,0)] text_insensitive_color "ddd"
        
        
        
        bar:
            pos (289,154)
            value FieldValue(persistent,"windowop",range=255)
            xsize 166
            ysize 14
            thumb At(im.AlphaMask("sys/"+"config2_barbtn"+".png",im.MatrixColor("sys/"+"config2_barbtnm"+".png",im.matrix.invert())),Transform(pos=(0,-4)))
            style None
            left_bar None
            right_bar None
            hovered [tt.action(im.AlphaMask("sys/CFGBG_WIP+075+46x450y.bmp","sys/CFGBG_MSK+075+46x450y.bmp")),bar1.action(LiveCrop((0,0,166,9),im.AlphaMask("sys/CFGBG_WIP+031+288x158y.bmp","sys/CFGBG_MSK+031+288x158y.bmp")))]
        
        bar:
            pos (289+264,154+165)
            value Preference("auto-forward time")
            xsize 166
            ysize 14
            thumb At(im.AlphaMask("sys/"+"config2_barbtn"+".png",im.MatrixColor("sys/"+"config2_barbtnm"+".png",im.matrix.invert())),Transform(pos=(0,-4)))
            style None
            left_bar None
            right_bar None
            hovered [tt.action(im.AlphaMask("sys/CFGBG_WIP+081+46x450y.bmp","sys/CFGBG_MSK+081+46x450y.bmp")),bar2.action(LiveCrop((0,0,166,9),im.AlphaMask("sys/CFGBG_WIP+031+288x158y.bmp","sys/CFGBG_MSK+031+288x158y.bmp")))]
        
        on "show" action Show("text_preview")
        on "replace" action Show("text_preview")
        on "replaced" action Hide("text_preview")
        on "hide" action Hide("text_preview")
    elif page == 3:
        default imageid = "41"
        default currentchr = "DZ"
        default bar1 = Tooltip(LiveCrop((136,0,166,9),im.AlphaMask("sys/CFGBG_WIP+038+359x119y.bmp","sys/CFGBG_MSK+038+359x119y.bmp")))
        default bar2 = Tooltip(LiveCrop((0,33,166,9),im.AlphaMask("sys/CFGBG_WIP+038+359x119y.bmp","sys/CFGBG_MSK+038+359x119y.bmp")))
        default bar3 = Tooltip(LiveCrop((0,61,166,9),im.AlphaMask("sys/CFGBG_WIP+038+359x119y.bmp","sys/CFGBG_MSK+038+359x119y.bmp")))
        default bar4 = Tooltip(LiveCrop((0,89,166,9),im.AlphaMask("sys/CFGBG_WIP+038+359x119y.bmp","sys/CFGBG_MSK+038+359x119y.bmp")))
        default bar5 = Tooltip(LiveCrop((0,117,166,9),im.AlphaMask("sys/CFGBG_WIP+038+359x119y.bmp","sys/CFGBG_MSK+038+359x119y.bmp")))
        default bar6 = Tooltip(LiveCrop((160,287,166,9),im.AlphaMask("sys/CFGBG_WIP+038+359x119y.bmp","sys/CFGBG_MSK+038+359x119y.bmp")))
        
        add im.AlphaMask("sys/CFGBG_WIP+0"+imageid+"+465x312y.bmp","sys/CFGBG_MSK+0"+imageid+"+465x312y.bmp") pos 467,314
        add im.AlphaMask("sys/"+"config3bg"+".bmp","sys/"+"config3bgm"+".bmp") pos (41,5)
        add bar1.value pos 361+136,119
        add bar2.value pos 361,119+33
        add bar3.value pos 361,119+61
        add bar4.value pos 361,119+89
        add bar5.value pos 361,119+117
        add bar6.value pos 361+160,119+287
        imagemap:
            pos 73,420-309
            cache False
            ground im.AlphaMask("sys/config3_button_idle.bmp","sys/config3_button_idle_mask.bmp")
            idle im.AlphaMask("sys/config3_button_idle.bmp","sys/config3_button_idle_mask.bmp")
            hover im.AlphaMask("sys/config3_button_hover.bmp","sys/config3_button_hover_mask.bmp")
            selected_idle im.AlphaMask("sys/config3_button_selected.bmp","sys/config3_button_selected_mask.bmp")
            selected_hover im.AlphaMask("sys/config3_button_selected.bmp","sys/config3_button_selected_mask.bmp")
            hotspot (193,0,80,28):
                action [Preference("music mute", "disable"),Preference("sound mute", "disable"),Preference("voice mute", "disable"),SetField(persistent,"music",True),SetField(persistent,"sound",True),SetField(persistent,"movievolume",True),SetField(persistent,"voice",True),SelectedIf(persistent.music or persistent.sound or persistent.voice or persistent.movievolume)]
                hovered tt.action(im.AlphaMask("sys/CFGBG_WIP+083+46x450y.bmp","sys/CFGBG_MSK+083+46x450y.bmp"))
            hotspot (284,0,80,28):
                action [Preference("music mute", "enable"),Preference("sound mute", "enable"),Preference("voice mute", "enable"),SetField(persistent,"music",False),SetField(persistent,"sound",False),SetField(persistent,"movievolume",False),SetField(persistent,"voice",False),SelectedIf(not (persistent.music or persistent.sound or persistent.voice or persistent.movievolume))]
                hovered tt.action(im.AlphaMask("sys/CFGBG_WIP+083+46x450y.bmp","sys/CFGBG_MSK+083+46x450y.bmp"))
            hotspot (148,37,49,20):
                action [Preference("music mute", "disable"),SetField(persistent,"music", True)]
                hovered tt.action(im.AlphaMask("sys/CFGBG_WIP+084+46x450y.bmp","sys/CFGBG_MSK+084+46x450y.bmp"))
            hotspot (205,37,49,20):
                action [Preference("music mute", "enable"),SetField(persistent,"music", False)]
                hovered tt.action(im.AlphaMask("sys/CFGBG_WIP+084+46x450y.bmp","sys/CFGBG_MSK+084+46x450y.bmp"))
            hotspot (148,65,49,20):
                action [Preference("sound mute", "disable"),SetField(persistent,"sound", True)]
                hovered tt.action(im.AlphaMask("sys/CFGBG_WIP+085+46x450y.bmp","sys/CFGBG_MSK+085+46x450y.bmp"))
            hotspot (205,65,49,20):
                action [Preference("sound mute", "enable"),SetField(persistent,"sound", False)]
                hovered tt.action(im.AlphaMask("sys/CFGBG_WIP+085+46x450y.bmp","sys/CFGBG_MSK+085+46x450y.bmp"))
            hotspot (148,93,49,20):
                action [SetField(persistent,"movievolume", True)]
                hovered tt.action(im.AlphaMask("sys/CFGBG_WIP+086+46x450y.bmp","sys/CFGBG_MSK+086+46x450y.bmp"))
            hotspot (205,93,49,20):
                action [SetField(persistent,"movievolume", False)]
                hovered tt.action(im.AlphaMask("sys/CFGBG_WIP+086+46x450y.bmp","sys/CFGBG_MSK+086+46x450y.bmp"))
            hotspot (148,121,49,20):
                action [Preference("voice mute", "disable"),SetField(persistent,"voice", True)]
                hovered tt.action(im.AlphaMask("sys/CFGBG_WIP+087+46x450y.bmp","sys/CFGBG_MSK+087+46x450y.bmp"))
            hotspot (205,121,49,20):
                action [Preference("voice mute", "enable"),SetField(persistent,"voice", False)]
                hovered tt.action(im.AlphaMask("sys/CFGBG_WIP+087+46x450y.bmp","sys/CFGBG_MSK+087+46x450y.bmp"))
            hotspot(233,157,80,28):
                action Preference("voice sustain", "disable")
                hovered tt.action(im.AlphaMask("sys/CFGBG_WIP+088+46x450y.bmp","sys/CFGBG_MSK+088+46x450y.bmp"))
            hotspot(324,157,80,28):
                action Preference("voice sustain", "enable")
                hovered tt.action(im.AlphaMask("sys/CFGBG_WIP+088+46x450y.bmp","sys/CFGBG_MSK+088+46x450y.bmp"))
            hotspot(1,230,12,12):
                focus_mask None
                action ToggleVoiceMute("DZ",invert=True)
                hovered tt.action(im.AlphaMask("sys/CFGBG_WIP+090+46x450y.bmp","sys/CFGBG_MSK+090+46x450y.bmp"))
            hotspot(1+72*1,230,12,12):
                focus_mask None
                action ToggleVoiceMute("W",invert=True)
                hovered tt.action(im.AlphaMask("sys/CFGBG_WIP+090+46x450y.bmp","sys/CFGBG_MSK+090+46x450y.bmp"))
            hotspot(1+72*2,230,12,12):
                focus_mask None
                action ToggleVoiceMute("MX",invert=True)
                hovered tt.action(im.AlphaMask("sys/CFGBG_WIP+090+46x450y.bmp","sys/CFGBG_MSK+090+46x450y.bmp"))
            hotspot(1+72*3,230,12,12):
                focus_mask None
                action ToggleVoiceMute("JL",invert=True)
                hovered tt.action(im.AlphaMask("sys/CFGBG_WIP+090+46x450y.bmp","sys/CFGBG_MSK+090+46x450y.bmp"))
            hotspot(1+72*4,230,12,12):
                focus_mask None
                action ToggleVoiceMute("QX",invert=True)
                hovered tt.action(im.AlphaMask("sys/CFGBG_WIP+090+46x450y.bmp","sys/CFGBG_MSK+090+46x450y.bmp"))
            hotspot(1,254,12,12):
                focus_mask None
                action ToggleVoiceMute("XC",invert=True)
                hovered tt.action(im.AlphaMask("sys/CFGBG_WIP+090+46x450y.bmp","sys/CFGBG_MSK+090+46x450y.bmp"))
            hotspot(1+72*1,254,12,12):
                focus_mask None
                action ToggleVoiceMute("YT",invert=True)
                hovered tt.action(im.AlphaMask("sys/CFGBG_WIP+090+46x450y.bmp","sys/CFGBG_MSK+090+46x450y.bmp"))
            hotspot(1+72*2,254,12,12):
                focus_mask None
                action ToggleVoiceMute("YG",invert=True)
                hovered tt.action(im.AlphaMask("sys/CFGBG_WIP+090+46x450y.bmp","sys/CFGBG_MSK+090+46x450y.bmp"))
            hotspot(1+72*3,254,12,12):
                focus_mask None
                action ToggleVoiceMute("YZ",invert=True)
                hovered tt.action(im.AlphaMask("sys/CFGBG_WIP+090+46x450y.bmp","sys/CFGBG_MSK+090+46x450y.bmp"))
            hotspot(1+72*4,254,12,12):
                focus_mask None
                action ToggleVoiceMute("YS",invert=True)
                hovered tt.action(im.AlphaMask("sys/CFGBG_WIP+090+46x450y.bmp","sys/CFGBG_MSK+090+46x450y.bmp"))
            hotspot(1,276,12,12):
                focus_mask None
                action ToggleVoiceMute("QTM",invert=True)
                hovered tt.action(im.AlphaMask("sys/CFGBG_WIP+090+46x450y.bmp","sys/CFGBG_MSK+090+46x450y.bmp"))
            hotspot(1+72*2,276,12,12):
                focus_mask None
                action ToggleVoiceMute("QTF",invert=True)
                hovered tt.action(im.AlphaMask("sys/CFGBG_WIP+090+46x450y.bmp","sys/CFGBG_MSK+090+46x450y.bmp"))
            hotspot (19,228,33,17):
                focus_mask None
                action [SetScreenVariable("imageid","41"),SetScreenVariable("currentchr","DZ"),SelectedIf(imageid=="41")]
                hovered tt.action(im.AlphaMask("sys/CFGBG_WIP+090+46x450y.bmp","sys/CFGBG_MSK+090+46x450y.bmp"))
            hotspot (19+68*1,228,20,20):
                focus_mask None
                action [SetScreenVariable("imageid","42"),SetScreenVariable("currentchr","W"),SelectedIf(imageid=="42")]
                hovered tt.action(im.AlphaMask("sys/CFGBG_WIP+090+46x450y.bmp","sys/CFGBG_MSK+090+46x450y.bmp"))
            hotspot (162,228,33,18):
                focus_mask None
                action [SetScreenVariable("imageid","43"),SetScreenVariable("currentchr","MX"),SelectedIf(imageid=="43")]
                hovered tt.action(im.AlphaMask("sys/CFGBG_WIP+090+46x450y.bmp","sys/CFGBG_MSK+090+46x450y.bmp"))
            hotspot (236,228,33,19):
                focus_mask None
                action [SetScreenVariable("imageid","44"),SetScreenVariable("currentchr","JL"),SelectedIf(imageid=="44")]
                hovered tt.action(im.AlphaMask("sys/CFGBG_WIP+090+46x450y.bmp","sys/CFGBG_MSK+090+46x450y.bmp"))
            hotspot (307,228,33,18):
                focus_mask None
                action [SetScreenVariable("imageid","45"),SetScreenVariable("currentchr","QX"),SelectedIf(imageid=="45")]
                hovered tt.action(im.AlphaMask("sys/CFGBG_WIP+090+46x450y.bmp","sys/CFGBG_MSK+090+46x450y.bmp"))
            hotspot (19,249,30,20):
                focus_mask None
                action [SetScreenVariable("imageid","46"),SetScreenVariable("currentchr","XC"),SelectedIf(imageid=="46")]
                hovered tt.action(im.AlphaMask("sys/CFGBG_WIP+090+46x450y.bmp","sys/CFGBG_MSK+090+46x450y.bmp"))
            hotspot (87,249,35,19):
                focus_mask None
                action [SetScreenVariable("imageid","47"),SetScreenVariable("currentchr","YT"),SelectedIf(imageid=="47")]
                hovered tt.action(im.AlphaMask("sys/CFGBG_WIP+090+46x450y.bmp","sys/CFGBG_MSK+090+46x450y.bmp"))
            hotspot (162,249,33,20):
                focus_mask None
                action [SetScreenVariable("imageid","48"),SetScreenVariable("currentchr","YG"),SelectedIf(imageid=="48")]
                hovered tt.action(im.AlphaMask("sys/CFGBG_WIP+090+46x450y.bmp","sys/CFGBG_MSK+090+46x450y.bmp"))
            hotspot (236,249,33,18):
                focus_mask None
                action [SetScreenVariable("imageid","49"),SetScreenVariable("currentchr","YZ"),SelectedIf(imageid=="49")]
                hovered tt.action(im.AlphaMask("sys/CFGBG_WIP+090+46x450y.bmp","sys/CFGBG_MSK+090+46x450y.bmp"))
            hotspot (307,249,33,20):
                focus_mask None
                action [SetScreenVariable("imageid","50"),SetScreenVariable("currentchr","YS"),SelectedIf(imageid=="50")]
                hovered tt.action(im.AlphaMask("sys/CFGBG_WIP+090+46x450y.bmp","sys/CFGBG_MSK+090+46x450y.bmp"))
            hotspot (18,272,65,20):
                focus_mask None
                action [SetScreenVariable("imageid","51"),SetScreenVariable("currentchr","QTM"),SelectedIf(imageid=="51")]
                hovered tt.action(im.AlphaMask("sys/CFGBG_WIP+090+46x450y.bmp","sys/CFGBG_MSK+090+46x450y.bmp"))
            hotspot (162,272,64,20):
                focus_mask None
                action [SetScreenVariable("imageid","52"),SetScreenVariable("currentchr","QTF"),SelectedIf(imageid=="52")]
                hovered tt.action(im.AlphaMask("sys/CFGBG_WIP+090+46x450y.bmp","sys/CFGBG_MSK+090+46x450y.bmp"))
        bar:
            pos (361,114+33)
            value Preference("music volume")
            xsize 166
            ysize 14
            thumb At(im.AlphaMask("sys/"+"config2_barbtn"+".png",im.MatrixColor("sys/"+"config2_barbtnm"+".png",im.matrix.invert())),Transform(pos=(0,-4)))
            style None
            left_bar None
            right_bar None
            hovered [tt.action(im.AlphaMask("sys/CFGBG_WIP+083+46x450y.bmp","sys/CFGBG_MSK+083+46x450y.bmp")),bar2.action(LiveCrop((0,0,166,9),im.AlphaMask("sys/CFGBG_WIP+031+288x158y.bmp","sys/CFGBG_MSK+031+288x158y.bmp")))]
        bar:
            pos (361,114+61)
            value Preference("sound volume")
            xsize 166
            ysize 14
            thumb At(im.AlphaMask("sys/"+"config2_barbtn"+".png",im.MatrixColor("sys/"+"config2_barbtnm"+".png",im.matrix.invert())),Transform(pos=(0,-4)))
            style None
            left_bar None
            right_bar None
            hovered [tt.action(im.AlphaMask("sys/CFGBG_WIP+083+46x450y.bmp","sys/CFGBG_MSK+083+46x450y.bmp")),bar3.action(LiveCrop((0,0,166,9),im.AlphaMask("sys/CFGBG_WIP+031+288x158y.bmp","sys/CFGBG_MSK+031+288x158y.bmp")))]
        bar:
            pos (361,114+117)
            value Preference("voice volume")
            xsize 166
            ysize 14
            thumb At(im.AlphaMask("sys/"+"config2_barbtn"+".png",im.MatrixColor("sys/"+"config2_barbtnm"+".png",im.matrix.invert())),Transform(pos=(0,-4)))
            style None
            left_bar None
            right_bar None
            hovered [tt.action(im.AlphaMask("sys/CFGBG_WIP+083+46x450y.bmp","sys/CFGBG_MSK+083+46x450y.bmp")),bar5.action(LiveCrop((0,0,166,9),im.AlphaMask("sys/CFGBG_WIP+031+288x158y.bmp","sys/CFGBG_MSK+031+288x158y.bmp")))]
        bar:
            pos (361+160,114+287)
            value SetCharacterVolume(currentchr)
            xsize 166
            ysize 14
            thumb At(im.AlphaMask("sys/"+"config2_barbtn"+".png",im.MatrixColor("sys/"+"config2_barbtnm"+".png",im.matrix.invert())),Transform(pos=(0,-4)))
            style None
            left_bar None
            right_bar None
            hovered [tt.action(im.AlphaMask("sys/CFGBG_WIP+083+46x450y.bmp","sys/CFGBG_MSK+083+46x450y.bmp")),bar6.action(LiveCrop((0,0,166,9),im.AlphaMask("sys/CFGBG_WIP+031+288x158y.bmp","sys/CFGBG_MSK+031+288x158y.bmp")))]
        
    add tt.value pos(40,450)
    use menu_top(page = page)
    use menu_bottom
    
    
screen text_preview:
    tag text
    text "现在的字体是"+persistent.fontname+"。\n文本显示速度大约是这个速度。" pos (430,223) slow_cps persistent.textspeed language "eastasian" size 23 color "fff" kerning 1.05 line_spacing 5 font persistent.font xsize 400
    if persistent.textspeed == 10:
        timer 3.0 action [Hide("text_preview"),Show("text_preview")]
    elif persistent.textspeed == 20:
        timer 1.5 action [Hide("text_preview"),Show("text_preview")]
    else:
        timer 1.0 action [Hide("text_preview"),Show("text_preview")]

init -2:
    style pref_frame:
        xfill True
        xmargin 5
        top_margin 5

    style pref_vbox:
        xfill True

    style pref_button:
        size_group "pref"
        xalign 1.0

    style pref_slider:
        xmaximum 192
        xalign 1.0

    style soundtest_button:
        xalign 1.0


##############################################################################
# Yes/No Prompt
#
# Screen that asks the user a yes or no question.
# http://www.renpy.org/doc/html/screen_special.html#yesno-prompt

screen yesno_prompt(message, yes_action, no_action):
    use shortcutkey
    if persistent.mouse:
        on "show" action MouseMove(320,370,duration=0.6)
        on "replace" action MouseMove(320,370,duration=0.6)
    modal True
    if main_menu:
        window:
            background "sys/x0000.bmp"
    window:
        background im.AlphaMask("sys/TDFILT_WIP.bmp","sys/TDFILT_MSK.bmp")
    frame:
        
        #style_group "yesno"
        
        #xfill True
        #xmargin .05
        #ypos .1
        #yanchor 0
        #ypadding .05
        align (.5,.5)
        background None
    
        maximum(720,212)
        if message == layout.LOADING:
            add im.AlphaMask("sys/loadconfirm.bmp","sys/YESNO1_MSK+000+0x0y.bmp") align (.5,.5)
        elif message == layout.OVERWRITE_SAVE:
            add im.AlphaMask("sys/overwrite.bmp","sys/YESNO1_MSK+000+0x0y.bmp") align (.5,.5)
        elif message == layout.MAIN_MENU:
            add im.AlphaMask("sys/titleconfirm.bmp","sys/YESNO1_MSK+000+0x0y.bmp") align (.5,.5)
        elif message == layout.QUIT:
            add im.AlphaMask("sys/exitconfirm.bmp","sys/YESNO1_MSK+000+0x0y.bmp") align (.5,.5)
        elif messgae == "QuickLoad":
            add im.AlphaMask("sys/quickloadconfirm.bmp","sys/YESNO1_MSK+000+0x0y.bmp") align (.5,.5)
        #else:
        #    add "img/bgMessageView@2x.png" align (.5,.5)
        #    text _(message) align (0.5,0.3) size 30 color "fff"
        
        hbox:
            align (.5,.9)
            spacing 80
            imagebutton:
                idle im.AlphaMask("sys/yes.bmp","sys/yesnom.bmp")
                hover im.AlphaMask("sys/yesh.bmp","sys/yesnom.bmp")
                action yes_action
            imagebutton:
                idle im.AlphaMask("sys/no.bmp","sys/yesnom.bmp")
                hover im.AlphaMask("sys/noh.bmp","sys/yesnom.bmp")
                action no_action


##############################################################################
# Quick Menu
#
# A screen that's included by the default say screen, and adds quick access to
# several useful functions.
screen quick_menu():

    # Add an in-game quick menu.
    hbox:
        style_group "quick"

        xalign 1.0
        yalign 1.0

        textbutton _("Back") action Rollback()
        textbutton _("Save") action ShowMenu('save')
        textbutton _("Q.Save") action QuickSave(message='', newest=True)
        textbutton _("Q.Load") action QuickLoad()
        textbutton _("Skip") action Skip()
        textbutton _("F.Skip") action Skip(fast=True, confirm=True)
        textbutton _("Auto") action Preference("auto-forward", "toggle")
        textbutton _("Prefs") action ShowMenu('preferences')

init -2:
    style quick_button:
        is default
        background None
        xpadding 5

    style quick_button_text:
        is default
        size 12
        idle_color "#8888"
        hover_color "#ccc"
        selected_idle_color "#cc08"
        selected_hover_color "#cc0"
        insensitive_color "#4448"
        
        
init python:
    
    
    button_list = []
    g = Gallery()
    g.transition = dissolve
    g.locked_button = Null()
    g.navigation = True
    g.span_buttons = False
    currentb = ""
    for name in cglist:
        if currentb!= name[0:8]:
            currentb = name[0:8]
            g.button(currentb)
            button_list.append(currentb)
            g.condition("persistent.cg['"+name+"']")
        g.image("pic/"+name+".png")
        g.condition("persistent.cg['"+name+"']")
    
    mr = MusicRoom(fadein = 1.0,fadeout = 1.0,loop=False,single_track=True)
    for i in range (1,25):
        mr.add("bgm/bgm%03d.ogg"%i)
    mr.add("bgm/bgm%03d.ogg"%25,always_unlocked=True)


screen omake_top(page=1):
    if page != 1:
        imagebutton:
            focus_mask None
            idle Null(116,22)
            hover "sys/bgm_cg.png"
            selected_idle "sys/bgm_cg.png"
            selected_hover "sys/bgm_cg.png"
            pos 222,5
            action [ShowMenu("omake",page=1),SelectedIf(page==1)]
    if page != 2:
        imagebutton:
            focus_mask None
            idle Null(116,22)
            hover "sys/cg_scene.png"
            selected_idle "sys/cg_scene.png"
            selected_hover "sys/cg_scene.png"
            pos 343,5
            action [ShowMenu("omake",page=2),SelectedIf(page==2)]
    if page != 3:
        imagebutton:
            focus_mask None
            idle Null(116,22)
            hover "sys/cg_bgm.png"
            selected_idle "sys/cg_bgm.png"
            selected_hover "sys/cg_bgm.png"
            pos 464,5
            action [ShowMenu("omake",page=3),SelectedIf(page==3)]

    

screen omake(page=1):
    tag menu
    if page == 1:
        default cgpage = 1
        window:
            background "sys/cg_p"+str(cgpage)+".png"
        for i in range(1,5):
            if cgpage != i:
                imagebutton:
                    pos 800-161,111+37*(i-1)
                    idle im.AlphaMask("sys/"+"loadpage ("+str(i)+").png",im.MatrixColor("sys/"+"loadpagem ("+str(i)+")"+".png",im.matrix.invert()))
                    hover im.AlphaMask("sys/"+"loadpageh ("+str(i)+")"+".png",im.MatrixColor("sys/"+"loadpagem ("+str(i)+")"+".png",im.matrix.invert()))
                    selected_idle im.AlphaMask("sys/"+"loadpageh ("+str(i)+")"+".png",im.MatrixColor("sys/"+"loadpagem ("+str(i)+")"+".png",im.matrix.invert()))
                    selected_hover im.AlphaMask("sys/"+"loadpageh ("+str(i)+")"+".png",im.MatrixColor("sys/"+"loadpagem ("+str(i)+")"+".png",im.matrix.invert()))
                    action [SetScreenVariable("cgpage",i),With(dissolve)]
        if cgpage!=4:
            grid 5 5:
                spacing 0
                pos 69,110
                for i in range((cgpage-1)*25,(cgpage)*25):
                    fixed:
                        xysize (105,88)
                        add g.make_button(button_list[i], "sys/CG_P"+str(cgpage)+"G_WIP+0"+"%02d"%((i-cgpage*25+25)+1)+"+"+str(82+105*((i-cgpage*25+25)%5))+"x"+str(112+88*((i-cgpage*25+25)/5))+"y.bmp",hover_border = At(Image("sys/CG_P"+str(cgpage)+"G_WIP+0"+"%02d"%((i-cgpage*25+25)+26)+"+"+str(82+105*((i-cgpage*25+25)%5))+"x"+str(112+88*((i-cgpage*25+25)/5))+"y.bmp"),Transform(pos=(12,1))),background=None)
        else:
            grid 5 2:
                spacing 0
                pos 69,110
                for i in range((cgpage-1)*25,(cgpage-1)*25+9):
                    fixed:
                        xysize (105,88)
                        add g.make_button(button_list[i], "sys/CG_P"+str(cgpage)+"G_WIP+0"+"%02d"%((i-cgpage*25+25)+1)+"+"+str(82+105*(((i-cgpage*25+25))%5))+"x"+str(112+88*(((i-cgpage*25+25))/5))+"y.bmp",hover_border = At(Image("sys/CG_P"+str(cgpage)+"G_WIP+0"+"%02d"%((i-cgpage*25+25)+26)+"+"+str(82+105*(((i-cgpage*25+25))%5))+"x"+str(112+88*(((i-cgpage*25+25))/5))+"y.bmp"),Transform(pos=(12,1))),background=None)
                add Null()
    elif page == 2:
        default scenepage = 1
        window:
            background "sys/scene_p"+str(scenepage)+".png"
        for i in range(1,4):
            if scenepage != i:
                imagebutton:
                    pos 800-161,111+37*(i-1)
                    idle im.AlphaMask("sys/"+"loadpage ("+str(i)+").png",im.MatrixColor("sys/"+"loadpagem ("+str(i)+")"+".png",im.matrix.invert()))
                    hover im.AlphaMask("sys/"+"loadpageh ("+str(i)+")"+".png",im.MatrixColor("sys/"+"loadpagem ("+str(i)+")"+".png",im.matrix.invert()))
                    selected_idle im.AlphaMask("sys/"+"loadpageh ("+str(i)+")"+".png",im.MatrixColor("sys/"+"loadpagem ("+str(i)+")"+".png",im.matrix.invert()))
                    selected_hover im.AlphaMask("sys/"+"loadpageh ("+str(i)+")"+".png",im.MatrixColor("sys/"+"loadpagem ("+str(i)+")"+".png",im.matrix.invert()))
                    action [SetScreenVariable("scenepage",i),With(dissolve)]
        if scenepage == 1:
            if renpy.seen_label("ccb2013"):
                imagebutton:
                    idle "sys/scene_b (1).bmp"
                    hover "sys/scene_bh (1).bmp"
                    selected_idle "sys/scene_bh (1).bmp"
                    selected_hover "sys/scene_bh (1).bmp"
                    action Replay("ccb2013",scope={"CIA":101,"pic":{}})
                    pos 82,113+89*0
                imagebutton:
                    idle "sys/scene_b (2).bmp"
                    hover "sys/scene_bh (2).bmp"
                    selected_idle "sys/scene_bh (2).bmp"
                    selected_hover "sys/scene_bh (2).bmp"
                    action Replay("ccb2013",scope={"CIA":102,"pic":{}})
                    pos 82,113+89*1
            if renpy.seen_label("ccb2101"):
                imagebutton:
                    idle "sys/scene_b (3).bmp"
                    hover "sys/scene_bh (3).bmp"
                    selected_idle "sys/scene_bh (3).bmp"
                    selected_hover "sys/scene_bh (3).bmp"
                    action Replay("ccb2101",scope={"pic":{}})
                    pos 82,113+89*2
            if renpy.seen_label("ccc3027"):
                imagebutton:
                    idle "sys/scene_b (4).bmp"
                    hover "sys/scene_bh (4).bmp"
                    selected_idle "sys/scene_bh (4).bmp"
                    selected_hover "sys/scene_bh (4).bmp"
                    action Replay("ccc3027",scope={"CIA":101,"pic":{}})
                    pos 82,113+89*3
                imagebutton:
                    idle "sys/scene_b (5).bmp"
                    hover "sys/scene_bh (5).bmp"
                    selected_idle "sys/scene_bh (5).bmp"
                    selected_hover "sys/scene_bh (5).bmp"
                    action Replay("ccc3027",scope={"CIA":102,"pic":{}})
                    pos 82,113+89*4
        elif scenepage == 2:
            if renpy.seen_label("ccc3027"):
                imagebutton:
                    idle "sys/scene_b (6).bmp"
                    hover "sys/scene_bh (6).bmp"
                    selected_idle "sys/scene_bh (6).bmp"
                    selected_hover "sys/scene_bh (6).bmp"
                    action Replay("ccc3027",scope={"CIA":103,"pic":{}})
                    pos 82,113+89*0
            if renpy.seen_label("ccc4022"):
                imagebutton:
                    idle "sys/scene_b (7).bmp"
                    hover "sys/scene_bh (7).bmp"
                    selected_idle "sys/scene_bh (7).bmp"
                    selected_hover "sys/scene_bh (7).bmp"
                    action Replay("ccc4022",scope={"pic":{}})
                    pos 82,113+89*1
            if renpy.seen_label("ccd4003"):
                imagebutton:
                    idle "sys/scene_b (8).bmp"
                    hover "sys/scene_bh (8).bmp"
                    selected_idle "sys/scene_bh (8).bmp"
                    selected_hover "sys/scene_bh (8).bmp"
                    action Replay("ccd4003",scope={"pic":{}})
                    pos 82,113+89*2
            if renpy.seen_label("cca0025c") or renpy.seen_label("ccb1101"):
                imagebutton:
                    idle "sys/scene_b (9).bmp"
                    hover "sys/scene_bh (9).bmp"
                    selected_idle "sys/scene_bh (9).bmp"
                    selected_hover "sys/scene_bh (9).bmp"
                    action Replay("cca0025c",scope={"pic":{}})
                    pos 82,113+89*3
            if renpy.seen_label("ccd1001"):
                imagebutton:
                    idle "sys/scene_b (10).bmp"
                    hover "sys/scene_bh (10).bmp"
                    selected_idle "sys/scene_bh (10).bmp"
                    selected_hover "sys/scene_bh (10).bmp"
                    action Replay("ccd1001",scope={"CIA":101,"pic":{}})
                    pos 82,113+89*4
        elif scenepage == 3:
            if renpy.seen_label("ccd1001"):
                imagebutton:
                    idle "sys/scene_b (11).bmp"
                    hover "sys/scene_bh (11).bmp"
                    selected_idle "sys/scene_bh (11).bmp"
                    selected_hover "sys/scene_bh (11).bmp"
                    action Replay("ccd1001",scope={"CIA":102,"pic":{}})
                    pos 82,113+89*0
            if renpy.seen_label("ccd0022a"):
                imagebutton:
                    idle "sys/scene_b (12).bmp"
                    hover "sys/scene_bh (12).bmp"
                    selected_idle "sys/scene_bh (12).bmp"
                    selected_hover "sys/scene_bh (12).bmp"
                    action Replay("ccd0022a",scope={"pic":{}})
                    pos 82,113+89*1
            if renpy.seen_label("ccd5001"):
                imagebutton:
                    idle "sys/scene_b (13).bmp"
                    hover "sys/scene_bh (13).bmp"
                    selected_idle "sys/scene_bh (13).bmp"
                    selected_hover "sys/scene_bh (13).bmp"
                    action Replay("ccd5001",scope={"CIA":101,"pic":{}})
                    pos 82,113+89*2
                imagebutton:
                    idle "sys/scene_b (14).bmp"
                    hover "sys/scene_bh (14).bmp"
                    selected_idle "sys/scene_bh (14).bmp"
                    selected_hover "sys/scene_bh (14).bmp"
                    action Replay("ccd5001",scope={"CIA":102,"pic":{}})
                    pos 82,113+89*3
    elif page == 3:
        window:
            background "sys/bgm_bg.png"
        for i in range (0,25):
            if i != 24:
                if mr.is_unlocked("bgm/bgm%03d.ogg"%(i+1)):
                    imagebutton:
                        idle "sys/bgm_buttonbg (%d).png" %(i+1)
                        hover "sys/bgm_buttonhover (%d).png" %(i+1)
                        selected_idle "sys/bgm_buttonh (%d).png" %(i+1)
                        selected_hover "sys/bgm_buttonh (%d).png" %(i+1)
                        action [Stop("bgm"),mr.Play(filename="bgm/bgm%03d.ogg"%(i+1))]
                        pos 77+227*(i/10),117+41*(i%10)
            else:
                if persistent.fullclear:
                    imagebutton:
                        idle "sys/bgm_buttonbg (%d).png" %(i+1)
                        hover "sys/bgm_buttonhover (%d).png" %(i+1)
                        selected_idle "sys/bgm_buttonh (%d).png" %(i+1)
                        selected_hover "sys/bgm_buttonh (%d).png" %(i+1)
                        action [Stop("bgm"),mr.Play(filename="bgm/bgm%03d.ogg"%(i+1))]
                        pos 77+227*(i/10),117+41*(i%10)
    use omake_top(page=page)
    use menu_bottom
    use shortcutkey
    key "game_menu" action [mr.Stop(),Return()]