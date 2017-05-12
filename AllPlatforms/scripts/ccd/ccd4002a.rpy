label ccd4002a:
    太一 "「あー、俺も行くよ」"
    call gl(1,"TCYM0001|TCYM0000")
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki012"
    美希 "「……はい、どうも」"
    "一人じゃ不安なのかな。"
    "また手を繋ぐ。"
    voice "vfCCD4001mki013"
    美希 "「……なんでこんなことに……」"
    太一 "「さあねえ」"
    call gl(1,"TCYM0000|TCYM0000")
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki014"
    美希 "「死体がないってことは、消えるんですよね？」"
    太一 "「みんなでどっか行ったのかも」"
    call gl(1,"TCYM0002|TCYM0002")
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki015"
    美希 "「どっかって……」"
    太一 "「ほら、発電所あるし。避難したとか」"
    call gl(1,"TCYM0001|TCYM0000")
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki016"
    美希 "「ここ危ないってことですか？」"
    太一 "「さあ……わからない」"
    call gl(1,"TCYM0000|TCYM0000")
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki017"
    美希 "「それって……無線や電話が通じない理由にはならないと思います」"
    太一 "「ああ、そうだな」"
    call gl(0,"bgcc0000a")
    call vsp(0,1)
    call vsp(1,0)
    with wipeleft
    "で、霧の家。"
    "美希と二人で、半分ずつ家を調べた。"
    太一 "「どうだった？」"
    voice "vfCCD4001mki018"
    美希 "「いません？」"
    太一 "「こっちはいない」"
    "美希の両肩が下がる。"
    call gl(0,"bgcc0014")
    call vsp(0,1)
    with wipeleft
    太一 "「すれ違ったのかも。学校に戻ろうか？」"
    call gl(1,"TCYM0001|TCYM0000")
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki019"
    美希 "「あの道を通ってるはずなんです！」"
    call gl(1,"TCYM0002|TCYM0002")
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki020"
    美希 "「すれ違ってるわけない……」"
    太一 "「先に学校に来てたのかも？」"
    call gl(1,"TCYM0001|TCYM0000")
    call vsp(1,1)
    with dissolve
    美希 "「…………」"
    voice "vfCCD4001mki022"
    美希 "「ごめんなさい、わたし、さがしてきますっ」"
    hide pic1
    with dissolve
    "駆けていく。"
    stop bgm
    太一 "「あ、おーい！」"
    太一 "「行っちゃった……」"
    call gl(0,"bgcc0000d")
    call vsp(0,1)
    with Dissolve(500.0/1000.0)
    "それから、美希は三日ほど霧を探し続けた。"
    "一日探索するごとに、美希は外部を拒絶していった。"
    "そして三日目、完全に閉じこもった。"
    "いくら説得しても、出てくる気配はない。"
    "もうその心は、絶望に完全に包まれてしまった。"
    "……失敗。"
    return
    #