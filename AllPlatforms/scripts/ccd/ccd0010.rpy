label ccd0010:
    call gl(0,"bgcc0000b")
    call vsp(0,1)
    with wipeleft
    pause (500.0/1000.0)
    call gl(0,"bgcc0011a")
    call vsp(0,1)
    with wipeleft
    play bgm "bgm/bgm018.ogg"
    太一 "「ほ……」"
    "いろいろ動き回ってみた。"
    "日曜日の部活。"
    "世界最後の日に、皆で大団円を迎えるため。"
    "だけど……困難さを感じた。"
    "全員を和姦……じゃなくて和解させるには、そーとーなパズルが必要だ。"
    "祠に向かう。"
    call gl(0,"bgcc0016a")
    call vsp(0,1)
    with wipeleft
    "大量のノート。"
    "読み切れないほどの分量だ。"
    "美希を手込め（表現に）にすると、霧がダメになる。"
    "情報が増えるのは良いことだ。"
    "けど増えすぎると、解析する時間がなくなる。"
    "ジレンマだ。"
    call gl(0,"bgcc0000c")
    call vsp(0,1)
    with wipeleft
    "俺は夜中まで、頭を捻り続けた。"
    voice "vfCCD0001you037"
    曜子 "「太一」"
    play se "SE019"
    "背後から、ライトがつく。"
    "懐中電灯だ。"
    call gl(0,"bgcc0016b")
    call gl(1,"TCHY0000c|tchy000x")
    call vsp(1,1)
    call vsp(0,1)
    call gp(1,t=center)#x=180
    with Dissolve(500.0/1000.0)
    "そして曜子ちゃんだ。"
    太一 "「んあ……明るい……」"
    call gl(1,"TCHY0001c|tchy000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCD0001you038"
    曜子 "「いくらその目でも、文字を読んでたら悪くするから」"
    太一 "「ん……ごめん」"
    call gl(1,"TCHY0000c|tchy000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCD0001you039"
    曜子 "「なにか発見はあった？」"
    太一 "「ない。知恵の輪に延々とハマってるみたいだ」"
    call gl(1,"TCHY0001c|tchy000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCD0001you040"
    曜子 "「そう、残念ね」"
    太一 "「曜子ちゃんはこのノートを……」"
    "問いかけて、口をつぐむ。"
    "彼女に頼ることだろうか。"
    太一 "「いいや。帰ろう」"
    "立ち上がる。"
    "ノートは一応、祠にしまう。"
    "何冊かは手にする。読める分は。"
    call gl(1,"TCHY0000c|tchy000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCD0001you041"
    曜子 "「……一緒に帰っても、いい？」"
    太一 "「いっつも監視してるくせに」"
    call gl(1,"TCHY0001c|tchy000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCD0001you042"
    曜子 "「ごめんなさい……」"
    stop bgm
    call gl(0,"bgcc0000d")
    call vsp(0,1)
    call vsp(1,0)
    with Dissolve(500.0/1000.0)
    pause (500.0/1000.0)
    return
    #