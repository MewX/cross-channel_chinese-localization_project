label ccb2102:
    call gl(0,"bgcc0013c")
    call vsp(1,0)
    call vsp(0,1)
    with wipeleft
    "帰るなり。"
    play bgm "bgm/bgm013.ogg"
    call gl(1,"TCKT0006|TCKT0006")
    call gp(1,t=center)#x=230
    call vsp(1,1)
    with dissolve
    voice "vfCCB2102fyu000"
    冬子 "「太一ぃ……っ！」"
    "玄関で挑んできた。"
    太一 "「はいはい」"
    voice "vfCCB2102fyu001"
    冬子 "「……ん、はぁん」"
    "服を脱ぐのももどかしく、キスをして、繋がった。"
    call gl(0,"bgcc0000d")
    call vsp(0,1)
    call vsp(1,0)
    with Dissolve(500.0/1000.0)
    "三度交わって、冬子は気絶した。"
    stop bgm
    "夜になるまで目覚めなかった。"
    call ndemo0002
    #gosub *ndemo0002
    return
    #