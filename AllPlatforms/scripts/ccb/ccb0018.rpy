label ccb0018:
    call gl(0,"bgcc0013as")
    call vsp(1,0)
    call vsp(0,1)
    with Pixellate(300.0*2/1000.0,5)
    play se "se001"
    play se "SE021"
    太一 "「はいはーい」"
    太一 "「どちら様で？」"
    voice "vfcca0020ysa000"
    遊紗 "「あ、あの、堂島です」"
    play bgm "bgm/bgm003.ogg"
    太一 "「その極道みたいな苗字とは裏腹にキュートな声は……遊紗ちゃん？　あいてるからどーぞ」"
    call gl(0,"bgcc0013azs")
    call vsp(0,1)
    call gl(1,"TCDY0000s|tcdy000x")
    call vsp(0,1)
    call vsp(1,1)
    call gp(1,t=center)#x=230
    with Dissolve(500.0/1000.0)
    "ドアがおそるおそる開き、美少女が立っていた。"
    voice "vfcca0020ysa001"
    遊紗 "「どうも、こんばん……わ」"
    call gl(0,"bgcc0004s")
    call vsp(0,1)
    call vsp(1,0)
    with wipeleft
    "座らせて、麦茶を出す。"
    "いろいろ会話をして。"
    call gl(1,"TCDY0000s|tcdy000x")
    call vsp(1,1)
    with dissolve
    voice "vfcca0020ysa019"
    遊紗 "「あの、わたし今日が誕生日なんです」"
    太一 "「へえ、そうだったのか」"
    call gl(1,"TCDY0001s|tcdy000x")
    call vsp(1,1)
    with dissolve
    voice "vfcca0020ysa020"
    遊紗 "「それでですね、これ……お誕生日プレゼントです」"
    太一 "「ええと……とりあえず、ありがとう。でも、あれ？」"
    call gl(1,"TCDY0000s|tcdy000x")
    call vsp(1,1)
    with dissolve
    voice "vfcca0020ysa022"
    遊紗 "「それと、交換日記を明日提出できたらなと思ったので……」"
    call gl(0,"bgcc0000d")
    call vsp(0,1)
    call vsp(1,0)
    with ImageDissolve("sys/EFMSK_22_MSK.bmp",time=1)
    pause (1000.0/1000.0)
    call gl(0,"bgcc0004s")
    call vsp(0,1)
    call vsp(1,0)
    with ImageDissolve("sys/EFMSK_22_MSK.bmp",time=1)
    太一 "「じゃあとりあえず交換日記と、それとこれは俺からの誕生日プレゼント」"
    call gl(1,"TCDY0004s|TCDY0004")
    call vsp(1,1)
    with dissolve
    voice "vfcca0020ysa027"
    遊紗 "「…………」"
    "この娘は驚くと絶句する癖があった。"
    太一 "「さてと、じゃ家まで送ろうか」"
    voice "vfcca0020ysa028"
    遊紗 "「……………………っっ！？」"
    "さっきの倍くらいに絶句した。"
    太一 "「もう夜だし、ちょっと危ない人もいるからね」"
    "特にこの街には。"
    太一 "「行こうか？」"
    call gl(1,"TCDY0001s|tcdy000x")
    call vsp(1,1)
    with dissolve
    voice "vfcca0020ysa029"
    遊紗 "「は、はいっ」"
    call gl(0,"bgcc0005bs")
    call vsp(0,1)
    call vsp(1,0)
    with wipeleft
    "そして、送った。"
    call gl(1,"TCDY0000s|tcdy000x")
    call vsp(1,1)
    with dissolve
    voice "vfcca0020ysa032"
    遊紗 "「その質問、毎回しますよね、太一さん？」"
    call gl(1,"TCDY0004s|TCDY0004")
    call vsp(1,1)
    with dissolve
    voice "vfcca0020ysa037"
    遊紗 "「難しくてよくわかりませんですけど……はい」"
    call gl(1,"TCDY0001s|tcdy000x")
    call vsp(1,1)
    with dissolve
    voice "vfcca0020ysa040"
    遊紗 "「きょーしゅーです」"
    call gl(0,"bgcc0000d")
    call vsp(0,1)
    call vsp(1,0)
    with Dissolve(500.0/1000.0)
    stop bgm
    "きょーしゅーです。"
    "きょーしゅー。"
    "郷愁？"
    "違う。"
    "強襲。"
    "強襲。"
    "そう、強襲。"
    "激しく、攻めること。"
    stop se
    "ああ。"
    "俺はこの言葉が、好きだな。"
    "夢の中で嗤う。"
    "とめどなく。"
    "嘲弄。"
    "沈んだ感情はすぐに深淵に呑まれる。"
    "シニシズムの虚無を思わせるメッキは溶解し、むきだしになっ……巨大な母体にまざって、戯れる。"
    "思考は一つ。"
    "敵は敵。"
    "殺さば殺す。"
    pause (1000.0/1000.0)
    pause (1000.0/1000.0)
    return
    #