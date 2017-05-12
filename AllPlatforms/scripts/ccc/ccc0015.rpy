label ccc0015:
    call gl(0,"bgcc0008")
    call vsp(0,1)
    call vsp(1,0)
    with wipeleft
    play bgm "bgm/bgm016.ogg"
    voice "vfCCC0015mki000"
    美希 "「せんぱいっ」"
    "背後から声をかけられた。"
    太一 "「よー」"
    太一 "「掃除終わった？」"
    "美希はぎょっとした。"
    call gl(1,"TCYM0004|TCYM0002")
    call gp(1,t=center)#x=180
    call vsp(1,1)
    with dissolve
    voice "vfCCC0015mki001"
    美希 "「よ、よく掃除をしていたとご存じで……」"
    call gl(1,"TCYM0021|TCYM0021")
    call vsp(1,1)
    with dissolve
    voice "vfCCC0015mki002"
    美希 "「見てました？」"
    "しまった。"
    "日記情報。極秘。"
    太一 "「……ナイショにする必要もないのかな」"
    call gl(1,"TCYM0000|TCYM0000")
    call vsp(1,1)
    with dissolve
    voice "vfCCC0015mki003"
    美希 "「ナイショとは？」"
    太一 "「あーいや、こっちのこと」"
    "いいや、しばらく伏せておこう。"
    "確かセクハラとかするんだよな。"
    "……俺もお盛んだな。"
    menu:
        "どうしたものか。"
        "セクハラ＆サイン":
            $B=1
        "デッドorアライブ":
            $B=2
    return
    #