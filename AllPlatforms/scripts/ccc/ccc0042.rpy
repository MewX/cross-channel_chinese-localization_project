label ccc0042:
    call gl(0,"bgcc0006")
    call vsp(0,1)
    call vsp(1,0)
    call vsp(2,0)
    with wipeleft
    pause (500.0/1000.0)
    pause (500.0/1000.0)
    call gl(0,"evcc0011a")
    call vsp(0,1)
    with Dissolve(500.0/1000.0)
    play bgm "bgm/bgm018.ogg"
    "冬子の姿はない。"
    "今日もだ。"
    "学校に来る理由もない。当然か。"
    "少しばかり物足りない。"
    "少しばかり自分の席に座ってみる。"
    "少しばかり、物思いにふけってみる。"
    stop bgm
    return
    #