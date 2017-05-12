label ccb1013:
    call gl(0,"bgcc0003b")
    call vsp(0,1)
    call vsp(1,0)
    with wipeleft
    "原稿を書いている。"
    太一 "「ひっひっひ」"
    太一 "「ひっひっひっひっひ！」"
    太一 "「ひーっひっひっひっひっひ！！（泣いている）」"
    "まとまらないよー！"
    "初日、自分の才能にうっとりしながら書いていた頃とはテンションが正反対だ。"
    voice "vfcca0024msa000"
    声 "「……けーくーんー……」"
    "誰かが呼んでる。"
    call gl(0,"bgcc0000c")
    call vsp(1,0)
    call vsp(0,1)
    with Dissolve(500.0/1000.0)
    "窓から外をのぞく。"
    太一 "「みみ先輩？」"
    play bgm "bgm/bgm012.ogg"
    voice "vfcca0024msa001"
    見里 "「こんばんはー」"
    太一 "「どうしたんですかー？」"
    voice "vfcca0024msa002"
    見里 "「どこにいるのですー？」"
    太一 "「二階の窓からそっち見てますー」"
    voice "vfcca0024msa003"
    見里 "「暗くて見えませーん」"
    太一 "「こっちはよく見えますよー」"
    voice "vfcca0024msa004"
    見里 "「どうしてなんでしょうねー」"
    太一 "「さー？」"
    voice "vfcca0024msa005"
    見里 "「ぺけくんはすごく夜目がきくんですねー」"
    太一 "「野生どーぶつなんで感覚鋭いんですよー」"
    voice "vfcca0024msa006"
    見里 "「なんかかっこいいですー」"
    "話しながらばたばたと腕を振っている。"
    "あれでけっこう幼いのだ。"
    太一 "「それより、あがってくださいー」"
    voice "vfcca0024msa007"
    見里 "「はーいー」"
    call gl(0,"bgcc0003b")
    call vsp(0,1)
    with wipeleft
    call gl(1,"TCMM0000c|TCMM000x")
    call gp(1,t=center)#x=220
    call vsp(1,1)
    with dissolve
    voice "vfcca0024msa008"
    見里 "「あ、蝋燭」"
    太一 "「執筆活動には雰囲気が大切なんですよ、おぜうさん」"
    call gl(1,"TCMM0001c|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfcca0024msa009"
    見里 "「なるほどー」"
    "ちょこんと正座。"
    call gl(1,"TCMM0000c|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfcca0024msa010"
    見里 "「お勉強でもしてたんですか？」"
    太一 "「いや、原稿です」"
    voice "vfcca0024msa011"
    見里 "「ああ」"
    太一 "「して、当家にはどのような御用向きで？」"
    call gl(1,"TCMM0002c|TCMM000x")
    voice "vfcca0024msa012"
    見里 "「あ、よく手伝ってくれてますから、ご飯をオゴろうかと思いまして」"
    "包みを掲げた。"
    call gl(1,"TCMM0000c|TCMM000x")
    voice "vfcca0024msa013"
    見里 "「お弁当です」"
    太一 "「先輩万歳」"
    voice "vfcca0024msa014"
    見里 "「二人分作ってきたんです、一緒にどうですか？」"
    太一 "「飲み物持ってきます」"
    pause (1000.0/1000.0)
    pause (1000.0/1000.0)
    call gl(0,"bgcc0003b")
    call vsp(0,1)
    with wipeleft
    太一 "「うまい」"
    太一 "「先輩は器用だなあ」"
    call gl(1,"TCMM0000c|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfcca0024msa015"
    見里 "「そうですか？　料理は最近はじめたばかりなんですけど……」"
    太一 "「まー、俺もグルメじゃないんで」"
    call gl(1,"TCMM0001c|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfcca0024msa016"
    見里 "「あ、その言い方はひどいかもです……」"
    太一 "「あー、うまいですよ。うん、うまい」"
    太一 "「火の通り方がいいですね。直火ですか？」"
    call gl(1,"TCMM0002c|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfcca0024msa017"
    見里 "「はい。もちろん」"
    太一 "「……なんか、こういう弁当食べるの、久しぶり」"
    call gl(1,"TCMM0000c|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfcca0024msa018"
    見里 "「そうなんですか？」"
    太一 "「俺……母親、いないですから」"
    call gl(1,"TCMM0004c|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfcca0024msa019"
    見里 "「まあ……」"
    太一 "「母親が恋しいのかもしれませんね、俺」"
    call gl(1,"TCMM0003c|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfcca0024msa020"
    見里 "「ぺけくん」"
    太一 "「先輩」"
    "薄闇の中、見つめ合う。"
    menu:
        "蝋燭のあえかな炎が、彼女の頬を淡い朱色に照らした。"
        "迫る":
            $B=1
        "ボケる":
            $B=2
    return
    #