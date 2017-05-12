label ccd0019:
    play bgm "bgm/bgm002.ogg"
    call gl(0,"bgcc0011")
    call vsp(0,1)
    with wipeleft
    pause (500.0/1000.0)
    call gl(0,"bgcc0006")
    call vsp(1,0)
    call vsp(0,1)
    with wipeleft
    pause (500.0/1000.0)
    call gl(0,"evcc0011a")
    call vsp(1,0)
    call vsp(0,1)
    with ImageDissolve("sys/EFMSK_22_MSK.bmp",time=1)
    "冬子がいない。"
    太一 "「……そうか」"
    "この時間帯はよく自宅で衰弱しているはずだ。"
    menu:
        "屋上":
            $B=1
        "冬子の家":
            $B=2
        "一年教室":
            $B=3
    return
    #