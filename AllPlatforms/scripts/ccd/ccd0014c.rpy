label ccd0014c:
    call gl(0,"bgcc0008")
    call gl(1,"TCSK0000|TCSK000x")
    call gp(1,t=center)#x=220
    call vsp(0,1)
    call vsp(1,1)
    with wipeleft
    "廊下に霧がいる。"
    "これもいつも通り。"
    "ただ効率よく行かないとな。"
    太一 "「霧ー」"
    call gl(1,"TCSK0001|TCSK000x")
    call vsp(1,1)
    with dissolve
    play bgm "bgm/bgm017.ogg"
    voice "vfCCD0001kri020"
    霧 "「む！」"
    "睨まれる。"
    太一 "「む！」"
    "睨む。"
    "ババババババババッ！！（心理効果）"
    "乳首が痒くなったが我慢した。"
    call gl(2,"TCYM0003|TCYM0003")
    call gp(2,t=center)#x=180
    call vsp(2,1)
    call vsp(1,0)
    with Dissolve(500.0/1000.0)
    voice "vfCCD0001mki028"
    美希 "「ふいー、スッキリしたー」"
    "やがて美希がトイレから出てくる。"
    call gl(2,"TCYM0004|TCYM0002")
    call vsp(2,1)
    with dissolve
    voice "vfCCD0001mki029"
    美希 "「にょーーーーっ！？」"
    "直前までしていた行為にふさわしい悲鳴が耳朶を打った。"
    "じり、と前に出る。"
    太一 "「俺が何の用意もなく、ここに来たとでも思ったか？」"
    "と、胸元に手を入れる。"
    "そこに必殺の武器が……あるわけではなくただのハッタリだ。"
    "かわりに乳首も掻いた。"
    "威嚇と乳首の痛痒を解消する、一石二鳥の技。"
    "霧も背中に手をまわす。"
    "クロスボウを、前方に構えた。"
    call gl(0,"evcc0024a")
    call vsp(0,1)
    call vsp(2,0)
    with ImageDissolve("sys/EFMSK_22_MSK.bmp",time=1)
    太一 "「うわああああ」"
    "適当に驚く。"
    "しかし緊張するな……。"
    "当たって死んでも問題ないとは言え。"
    "ふーむ。"
    menu:
        "そういう選択肢もあるのだろうか？"
        "ためしに攻撃":
            $B=1
        "降伏":
            $B=2
    return
    #