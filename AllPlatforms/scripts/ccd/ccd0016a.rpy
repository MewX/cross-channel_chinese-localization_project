label ccd0016a:
    call gl(0,"bgcc0008")
    call gl(1,"TCSK0001|TCSK000x")
    call gp(1,t=center)#x=220
    call vsp(0,1)
    call vsp(1,1)
    with Dissolve(500.0/1000.0)
    voice "vfCCD0001kri028"
    霧 "「……じー」"
    "ホコリを払う俺に、霧がガンを飛ばしたりメンチを切ったりしてくる。"
    太一 "「霧……」"
    "霧から行くか。"
    voice "vfCCD0001kri029"
    霧 "「……なんですか？」"
    "冷え冷えとした反応。顔つき。"
    "目の前に立つ。"
    "頭一つ分大きな俺に、臆さず目線を向けてくる。"
    "その意気や良し。"
    太一 "「てやー」"
    call gl(5,"bgcc0000e")
    call gl(0,"evcc0028")
    play se "se100"
    call vsp(5,1)
    with dissolve
    call vsp(0,1)
    call vsp(1,0)
    call vsp(5,0)
    with Dissolve(500.0/1000.0)
    "アケスケー！"
    voice "vfCCC3002kri013"
    霧 "「っっっ？？？」"
    voice "vfCCC3002kri014"
    霧 "「あ、あれ？　あれれ？」"
    voice "vfCCC3002kri015"
    霧 "「ど、どうして戻らな……なっなっなっ？」"
    "ばたばたとスカートを押さえつける。"
    "スカートはまったく落ち着こうとはしない。"
    voice "vfCCC3002kri016"
    霧 "「す、すかぁとがっ……ふわふわ浮いてっ、ちょっと、なにコレ！？」"
    voice "vfCCD0001mki035"
    美希 "「ふしぎ発見……」"
    太一 "「手首のひねりが決め手だ」"
    voice "vfCCC3002kri017"
    霧 "「あぁあぁあぁぁぁあぁぁぁぁ……」"
    "あたふたあたふた。"
    "ばさばさふさふさ。"
    voice "vfCCD0001kri030"
    霧 "「く、空気が抜けないっ」"
    太一 "「さて」"
    call gl(0,"bgcc0008")
    call vsp(0,1)
    with ImageDissolve("sys/EFMSK_22_MSK.bmp",time=1)
    "美希を見る。"
    call gl(1,"TCYM0000|TCYM0000")
    call gp(1,t=center)#x=225
    call vsp(1,1)
    with dissolve
    voice "vfCCD0001mki036"
    美希 "「どき……」"
    太一 "「ミニスカート大好きな娘っ子への、ちょっとはやいクリスマスプレゼント」"
    call gl(1,"TCYM0002|TCYM0002")
    call vsp(1,1)
    with dissolve
    voice "vfCCD0001mki037"
    美希 "「あ……わ、わたしにもアレを……？」"
    "逃げ腰になる。"
    voice "vfCCD0001mki038"
    美希 "「あ……いや……許して下さぁい」"
    太一 "「う」"
    "く、いたいけだぜ。"
    太一 "「見逃してやりたいのは山々なのだが……許せよ」"
    voice "vfCCD0001mki039"
    美希 "「ふわぁ、せ、先輩、落ち着いて……」"
    "スカートの裾に指をかける。"
    voice "vfCCD0001mki040"
    美希 "「美希の大好きな先輩はそんなことしませんよね？」"
    "じっ、と見つめられる。"
    太一 "「……」"
    "少女の叫びに、心が動いた。"
    "その小さな腰をバックで滅茶苦茶に突き押してやりたい。"
    "愛しているから壊したい。"
    "大好きだからイジメタイ。"
    "男心は複雑なのだ。"
    voice "vfCCD0001mki041"
    美希 "「人はなぜ争わなければならないんですか！」"
    "くっ、その通りだ。"
    "まったく関係ないが正当な疑問だ。"
    "美希のピュアな言葉が俺を目覚めさせた。"
    太一 "「わかったよ、美希」"
    call gl(1,"TCYM0003|TCYM0003")
    call vsp(1,1)
    with dissolve
    voice "vfCCD0001mki042"
    美希 "「先輩、よかった」"
    "霧にも頭を下げよう。"
    hide pic1
    with dissolve
    太一 "「やーやー霧、ゴメン！」"
    call gl(4,"sgcc0013")
    play se "SE003"
    call vsp(4,1)
    with dissolve
    with vpunch
    voice "vfCCD0001kri031"
    霧 "「ゴメンじゃなーーーーーーーいっ！！」"
    stop bgm
    pause (500.0/1000.0)
    pause (1000.0/1000.0)
    call gl(0,"bgcc0000d")
    call vsp(0,1)
    call vsp(4,0)
    with Dissolve(500.0/1000.0)
    pause (500.0/1000.0)
    return
    #