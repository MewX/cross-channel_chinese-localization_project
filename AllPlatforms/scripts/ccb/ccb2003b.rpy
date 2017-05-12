label ccb2003b:
    太一 "「そ、そんなふしだらアカン！」"
    voice "vfccb2004bfyu000"
    冬子 "「……そう」"
    "食い下がらなかった。"
    太一 "「そうですよ」"
    voice "vfccb2004bfyu001"
    冬子 "「そうよね……」"
    "膝頭に。"
    "顔を埋めた。"
    太一 "「ソーリー……」"
    voice "vfccb2004bfyu002"
    冬子 "「……ぐすっ……」"
    call gl(0,"bgcc0000d")
    call vsp(1,0)
    call vsp(0,1)
    with Dissolve(500.0/1000.0)
    "……。"
    "…………。"
    "……………………。"
    call gl(0,"bgcc0002c")
    call vsp(0,1)
    with ImageDissolve("sys/EFMSK_22_MSK.bmp",time=1)
    "残ったじゃがいもをタッパーに詰めて、それを手に冬子は帰った。"
    太一 "「たくましくあれ」"
    "切に願う俺だった。"
    stop bgm
    return
    #