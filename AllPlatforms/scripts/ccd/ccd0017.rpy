label ccd0017:
    call gl(0,"bgcc0010")
    call vsp(0,1)
    with wipeleft
    "くたびれた……。"
    太一 "「なんか……全然進展しないな」"
    call gl(1,"TCHY0001|tchy000x")
    call gp(1,t=center)#x=180
    call vsp(1,1)
    with dissolve
    voice "vfCCD0001you043"
    曜子 "「でしょうね」"
    "神出鬼没。支倉曜子。"
    太一 "「……見てたの？」"
    voice "vfCCD0001you044"
    曜子 "「全部ではないけれど」"
    太一 "「悪趣味」"
    call gl(1,"TCHY0000|tchy000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCD0001you045"
    曜子 "「……汗、かいてる」"
    "ハンカチでふいてくれる。"
    太一 "「いいよ、汗なんて」"
    "のける。"
    "でもやめてはくれない。"
    "強く拒絶しなければ、駄目なのだった。"
    太一 "「ま、いいけどさ……」"
    call gl(0,"bgcc0000d")
    call vsp(0,1)
    call vsp(1,0)
    with Dissolve(500.0/1000.0)
    return
    #