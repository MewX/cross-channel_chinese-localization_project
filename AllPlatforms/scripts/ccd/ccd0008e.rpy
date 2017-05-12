label ccd0008e:
    call gl(0,"bgcc0000d")
    call vsp(0,1)
    call vsp(1,0)
    with Dissolve(500.0/1000.0)
    "扉が開かない。"
    "強く押し込むと、目の前に乱気流ができた。"
    play se "SE009"
    call gl(0,"bgcc0007")
    call gl(5,"bgcc0000e")
    call vsp(5,1)
    with dissolve
    call vsp(0,1)
    call vsp(5,0)
    with Dissolve(500.0/1000.0)
    "風の通り道。"
    play se "SE010"
    "耳鳴り。"
    call gl(0,"evcc0004")
    call vsp(0,1)
    with ImageDissolve("sys/EFMSK_22_MSK.bmp",time=1)
    play bgm "bgm/bgm015.ogg"
    "それと、先輩。"
    太一 "「おはようございます」"
    call gl(0,"bgcc0007")
    call gl(1,"TCMM0000|TCMM000x")
    call vsp(0,1)
    call vsp(1,1)
    call gp(1,t=center)#x=225
    with Dissolve(500.0/1000.0)
    voice "vfCCD0001msa000"
    見里 "「あら、おはようございます」"
    太一 "「どうですか、アンテナ」"
    voice "vfCCD0001msa001"
    見里 "「ぼちぼち、というところですか」"
    太一 "「これって、次の日曜日が予定日だったんですよね」"
    call gl(1,"TCMM0004|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCD0001msa002"
    見里 "「……よく記憶してますね」"
    太一 "「一応は」"
    call gl(1,"TCMM0000|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCD0001msa003"
    見里 "「そうです。何も起こらなければ、ここは……」"
    voice "vfCCD0001msa004"
    見里 "「でも、人が亡くなったんですから、仕方ありません……あ、ごめんなさい」"
    太一 "「いえー」"
    "本当に謝る必要なんてない。"
    "傷ついてさえいないのだから、俺は。"
    太一 "「まあ、そのせいで屋上に行くのが禁止になったわけですから」"
    call gl(1,"TCMM0001|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCD0001msa005"
    見里 "「……あなた方はけっこう勝手に来てたようですけどね」"
    太一 "「それを言ったら、今の先輩だって」"
    "見合わされた二人の顔。同時に頬が緩む。"
    call gl(1,"TCMM0002|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCD0001msa006"
    見里 "「じゃ、二人とも停学です。イエロー停学」"
    太一 "「そりゃ厳しいや」"
    太一 "「……これって、先輩が一人でここまで？」"
    call gl(1,"TCMM0000|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCD0001msa007"
    見里 "「図面があったので、なんとか」"
    call gl(1,"TCMM0031|TCMM0031")
    call vsp(1,1)
    with dissolve
    voice "vfCCD0001msa008"
    見里 "「でも、大変でした。いったんバラバラにされてましたから」"
    "それでも先輩は、誰にも助けを求めなかった。"
    "仮借ない陽光に身をさらして、一人で、部活を続けていた。"
    太一 "「……今さら手伝いましょうかってのも、虫の良い話なんでしょうね」"
    "先輩は相好を崩す。"
    call gl(1,"TCMM0000|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCD0001msa009"
    見里 "「ありがとうです」"
    call gl(1,"TCMM0002|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCD0001msa010"
    見里 "「お気持ちだけで十分ですよ」"
    "まあ、こんなものか。"
    太一 "「いつだって、使ってくれて良かったのに」"
    "あなたの逃避に利用してくれて。"
    call gl(1,"TCMM0000|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCD0001msa011"
    見里 "「あっ、いいんですいいんです、平気ですから」"
    call gl(1,"TCMM0002|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCD0001msa012"
    見里 "「そのかわりといってはなんですけど、今度またゆっくりお茶しましょう」"
    太一 "「はい」"
    stop se
    stop bgm
    return
    #