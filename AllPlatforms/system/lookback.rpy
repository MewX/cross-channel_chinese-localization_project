# readback.rpy
# drop in readback module for Ren'Py by delta
# this file is licensed under the terms of the WTFPL
# see http://sam.zoy.org/wtfpl/COPYING for details

# voice_replay function added by backansi from Lemma soft forum.
# required renpy 6.12 or higher.

init -3 python:
    # config.game_menu.insert(1,( "text_history", u"Text History", ui.jumps("text_history_screen"), 'not main_menu'))

    # styles
    #style.readback_window.xmaximum = 760
    #style.readback_window.ymaximum = 500
    #style.readback_window.align = (.5, .5)

    #style.readback_frame.background = None
    style.readback_frame.xpadding = 10
    style.readback_frame.xmargin = 5
    style.readback_frame.ymargin = 5
    
    style.readback_text.color = "#fff"

    style.create("readback_button", "readback_text")
    style.readback_button.background = None
    
    style.create("readback_button_text", "readback_text")
    style.readback_button_text.idle_color = "#ffffb0"
    style.readback_button_text.selected_color = "#ffffb0"
    style.readback_button_text.hover_color = "#ffffb0"
    
    style.readback_label_text.bold = True
    
    # starts adding new config variables
    config.locked = False 
    
    # Configuration Variable for Text History 
    config.readback_buffer_length = 100 # number of lines stored
    config.readback_full = True # True = completely replaces rollback, False = readback accessible from game menu only (dev mode)
    config.readback_disallowed_tags = ["size"] # a list of tags that will be removed in the text history
    config.readback_choice_prefix = ">> "   # this is prefixed to the choices the user makes in readback
    
    # ends adding new config variables
    config.locked = True
    
init -2 python:

    # Two custom characters that store what they said
    class ReadbackADVCharacter(ADVCharacter):
        def do_done(self, who, what):
            store_say(who, what)
            current_voice = ''
            return

    class ReadbackNVLCharacter(NVLCharacter):
        def do_done(self, who, what):
            store_say(who, what)
            current_voice = ''
            return
            
    # this enables us to show the current line in readback without having to bother the buffer with raw shows
    def say_wrapper(who, what, **kwargs):
        store_current_line(who, what)
        return renpy.show_display_say(who, what, **kwargs)
    
    config.nvl_show_display_say = say_wrapper
    
    adv = ReadbackADVCharacter(show_function=say_wrapper,name="")#,ctc="cursor")
    nvl = ReadbackNVLCharacter()
    NVLCharacter = ReadbackNVLCharacter
    
    # rewriting voice function to replay voice files when you clicked dialogues in text history screen
    def voice(file, **kwargs):
        global current_voice
        if not config.has_voice:
            return
        
        _voice.play = file
        
        current_voice = file

    # overwriting standard menu handler
    # Overwriting menu functions makes Text History log choice which users choose.
    def menu(items, **add_input): 
        
        newitems = []
        for label, val in items:
            if val == None:
                narrator(label, interact=False)
            else:
                newitems.append((label, val))
                
        rv = renpy.display_menu(newitems, **add_input)
        
        # logging menu choice label.
        for label, val in items:
            if rv == val:
                current_voice = ''
                store_say(None, config.readback_choice_prefix + label)
        return rv
        
    def nvl_screen_dialogue(): 
        """
         Returns widget_properties and dialogue for the current NVL
         mode screen.
         """

        widget_properties = { }
        dialogue = [ ]
        
        for i, entry in enumerate(nvl_list):
            if not entry:
                continue

            who, what, kwargs = entry

            if i == len(nvl_list) - 1:
                who_id = "who"
                what_id = "what"
                window_id = "window"

            else:
                who_id = "who%d" % i
                what_id = "what%d" % i
                window_id = "window%d" % i
                
            widget_properties[who_id] = kwargs["who_args"]
            widget_properties[what_id] = kwargs["what_args"]
            widget_properties[window_id] = kwargs["window_args"]

            dialogue.append((who, what, who_id, what_id, window_id))
        
        return widget_properties, dialogue
        
     #Overwriting nvl menu function
    def nvl_menu(items):

        renpy.mode('nvl_menu')
        
        if nvl_list is None:
            stonvl_list = [ ]

        screen = None
        
        if renpy.has_screen("nvl_choice"):
            screen = "nvl_choice"
        elif renpy.has_screen("nvl"):
            screen = "nvl"
            
        if screen is not None:

            widget_properties, dialogue = nvl_screen_dialogue()        

            rv = renpy.display_menu(
                items,
                widget_properties=widget_properties,
                screen=screen,
                scope={ "dialogue" : dialogue },
                window_style=style.nvl_menu_window,
                choice_style=style.nvl_menu_choice,
                choice_chosen_style=style.nvl_menu_choice_chosen,
                choice_button_style=style.nvl_menu_choice_button,
                choice_chosen_button_style=style.nvl_menu_choice_chosen_button,
                type="nvl",                      
                )
                
            for label, val in items:
                if rv == val:
                    current_voice = ''
                    store_say(None, config.readback_choice_prefix + label)
            return rv
            
        # Traditional version.
        ui.layer("transient")
        ui.clear()
        ui.close()

        ui.window(style=__s(style.nvl_window))
        ui.vbox(style=__s(style.nvl_vbox))

        for i in nvl_list:
            if not i:
                continue

            who, what, kw = i            
            rv = renpy.show_display_say(who, what, **kw)

        renpy.display_menu(items, interact=False,
                           window_style=__s(style.nvl_menu_window),
                           choice_style=__s(style.nvl_menu_choice),
                           choice_chosen_style=__s(style.nvl_menu_choice_chosen),
                           choice_button_style=__s(style.nvl_menu_choice_button),
                           choice_chosen_button_style=__s(style.nvl_menu_choice_chosen_button),
                           )

        ui.close()

        roll_forward = renpy.roll_forward_info()

        rv = ui.interact(roll_forward=roll_forward)
        renpy.checkpoint(rv)

        for label, val in items:
            if rv == val:
                current_voice = ''
                store_say(None, config.readback_choice_prefix + label)
        return rv
        
    ## readback
    readback_buffer = []
    current_line = None
    current_voice = None
    
    def store_say(who, what):
        global readback_buffer, current_voice
        if preparse_say_for_store(what):
            new_line = (preparse_say_for_store(who), preparse_say_for_store(what), current_voice)
            readback_buffer = readback_buffer + [new_line]
            readback_prune()
            current_voice = None

    def store_current_line(who, what):
        global current_line, current_voice
        current_line = (who, preparse_say_for_store(what), current_voice)
        

    # remove text tags from dialogue lines 
    disallowed_tags_regexp = ""
    for tag in config.readback_disallowed_tags:
        if disallowed_tags_regexp != "":
            disallowed_tags_regexp += "|"
        disallowed_tags_regexp += "{"+tag+"=.*?}|{"+tag+"}|{/"+tag+"}"
    
    from re import *
    remove_tags_expr = compile(disallowed_tags_regexp) # remove tags undesirable in readback
    def preparse_say_for_store(input):
        global remove_tags_expr
        if input:
            return sub(remove_tags_expr, "", input)

    def readback_prune():
        global readback_buffer
        while len(readback_buffer) > config.readback_buffer_length:
            del readback_buffer[0]

    # keymap overriding to show text_history.
    #def readback_catcher():
        #ui.add(renpy.Keymap(rollback=(ShowMenu("text_history"),With(easeintop))))
        #ui.add(renpy.Keymap(rollforward=NullAction()))

    if config.readback_full:
        config.rollback_enabled = False
        #config.overlay_functions.append(readback_catcher)    
    
init python:
    global yvalue
    yvalue = 0
    class NewAdj(renpy.display.behavior.Adjustment):
        def change(self,value):
            yvalue = value
            if value > self._range:
                return Return()
            else:
                return renpy.display.behavior.Adjustment.change(self, value)
                
    def store_yvalue(y):
        yvalue = int(y)

screen text_history:
    #use navigation
    tag menu
    modal True
    if not current_line and len(readback_buffer) == 0:
        $ lines_to_show = []
        
    elif current_line and len(readback_buffer) == 0:
        $ lines_to_show = [current_line]
        
    elif current_line and not ( ( len(readback_buffer) == 3 and current_line == readback_buffer[-2]) or current_line == readback_buffer[-1]):  
        $ lines_to_show = readback_buffer + [current_line]
        
    else:
        $ lines_to_show = readback_buffer
    
    
    default adj = NewAdj(changed = store_yvalue, step = 24)
    window:
        style_group "readback"
        background im.AlphaMask("sys/"+"logb"+".bmp","sys/"+"logbm"+".bmp")
        frame:
            background None
            maximum (780,600)
            align (.5,.5)
            viewport:
                $renpy.cancel_gesture()
                align (.5,.5)
                mousewheel True
                draggable True
                yadjustment adj
                yinitial 1.0
                scrollbars "vertical"
                vbox:
                    
                    
                    for line in lines_to_show:
                        
                        if line[0] and line[0] != " ":
                            text line[0] size 23 xcenter 0.15# name
                            null height 10
                        # if there's no voice just log a dialogue
                        if not line[2]:
                            $extraline = (6-len(line[1])/32)*24
                            text line[1]+"{vspace=[extraline]}" size 23
                            
                        # else, dialogue will be saved as a button of which plays voice when clicked
                        else: 
                            textbutton line[1] action Play("voice", line[2] ) text_size 23 ysize 24*6
                        
        textbutton _("Return") action [Stop("voice"),Return()] align (0.0, 1.0)
        #imagebutton idle "img/btnBack_0@2x.png" hover "img/btnBack_1@2x.png" action [Stop("voice"),Hide("text_history",transition=dissolve)] align (0.98,0.98)
        key "game_menu" action [Stop("voice"),Hide("text_history"),Return()]