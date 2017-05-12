label ccd3001:
    call gl(0,"bgcc0006")
    call vsp(0,1)
    call vsp(1,0)
    with wipeleft
    "四階。一年の教室。"
    "霧がいた。"
    call gl(0,"evcc0027")
    call vsp(0,1)
    with Dissolve(500.0/1000.0)
    "繊細な少女。"
    "壊さないよう、壊れないよう。"
    menu:
        "……せめて、思い出を。"
        "接近する":
            $B=1
        "声をかける":
            $B=2
    return
    #