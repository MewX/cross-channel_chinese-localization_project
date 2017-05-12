label ccb0020:
    call gl(0,"bgcc0000d")
    call vsp(0,1)
    call vsp(1,0)
    call vsp(2,0)
    with Dissolve(500.0/1000.0)
    pause (1000.0/1000.0)
    call gl(0,"bgcc0017s")
    call vsp(1,0)
    call vsp(0,1)
    with Pixellate(300.0*2/1000.0,5)
    play se "SE001"
    play bgm "bgm/bgm005.ogg"
    "楽しい海だった。"
    "今でも、皆のはしゃぎようは思い出せる。"
    call gl(4,"sgcc0009s")
    call vsp(4,1)
    with dissolve
    with vpunch
    voice "vfcca0027fyu004"
    冬子 "「きあああっ！？　どこつかんでんのよっ！？」"
    太一 "「水着のお尻のとこの布」"
    hide pic4
    with dissolve
    call gl(1,"TCMM0000as|TCMM000xad")
    call gp(1,t=center)#x=220
    call vsp(1,1)
    with dissolve
    voice "vfcca0027msa004"
    見里 "「支倉さんって……黒須君とどういうご関係なんでしょうねぇ？」"
    太一 "「ん、曜子ちゃん？」"
    call gl(1,"TCKT0004as|TCKT000xa")
    call gl(2,"TCMM0004as|TCMM000xad")
    call gl(3,"TCYM0001as|TCYM000xa")
    call gp(1,t=left)#x=-20
    call gp(2,t=center)#x=220
    call gp(3,t=right)#x=400
    call vsp(1,1)
    call vsp(2,1)
    call vsp(3,1)
    with Dissolve(500.0/1000.0)
    voice "vfcca0027doz000"
    冬子 "「曜子ちゃん！？」"
    見里 "「曜子ちゃんっ！？」"
    美希 "「曜子ちゃんっっっ？」"
    友貴 "「曜子ちゃん！！」"
    call gl(4,"TCYM0000as|TCYM000xa")
    call gp(4,t=center)#x=180
    call vsp(4,1)
    call vsp(3,0)
    call vsp(2,0)
    call vsp(1,0)
    with Dissolve(500.0/1000.0)
    voice "vfcca0027mki016"
    美希 "「ヤクザですねもう」"
    call gl(1,"TCMM0005as|TCMM000xad")
    call gp(1,t=center)#x=235
    call vsp(4,0)
    call vsp(1,1)
    with Dissolve(500.0/1000.0)
    voice "vfcca0027msa013"
    見里 "「カ、カラダはいやぁ～」"
    call gl(2,"TCDY0004as|tcdy000xa")
    call gp(2,t=center)#x=240
    call vsp(1,0)
    call vsp(2,1)
    with Dissolve(500.0/1000.0)
    voice "vfcca0027ysa001"
    遊紗 "「あのっ、失礼しますしますしますっ！！！！」"
    call gl(0,"evcc0007s")
    call vsp(0,1)
    call vsp(1,0)
    call vsp(2,0)
    with ImageDissolve("sys/EFMSK_22_MSK.bmp",time=1)
    voice "vfcca0027fyu024"
    冬子 "「ばーか」"
    voice "vfcca0027ysa015"
    遊紗 "「あっ、くるっ、くるるっ？」"
    voice "vfcca0027mki029"
    美希 "「い、いたい～、おでこいたい～」"
    voice "vfcca0027msa026"
    見里 "「……ぶつぶつぶつ」"
    太一 "「楽しかったけどな」"
    stop se
    call gl(0,"bgcc0000bs")
    call vsp(0,1)
    with Dissolve(500.0/1000.0)
    "楽しい海水浴はこれでおしまい。"
    "美希の傷は、ほんの少しだけ跡が残りそうだった。"
    "それでも帰り道、本人は晴れ晴れとした顔をしていた。"
    "傷ついたかわりに、何かを得たような。"
    "そんな顔だった。"
    "そのあと、見里先輩が放送部用のアンテナ搬入につきあうため、学校に戻って。"
    "まだ姉とは断絶していなかった友貴が、皮肉を言って。"
    "そのシスコンぶりを、当時まだ群青付属三年生だった美希にからかわれて。"
    "遊紗ちゃんが、集団というものに対してはじめて、小さく心を開いた。"
    "そんな海だったんだ。"
    call gl(0,"bgcc0000d")
    call vsp(0,1)
    with Dissolve(500.0/1000.0)
    stop bgm
    return
    #