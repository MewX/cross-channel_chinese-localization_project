label ccb2007:
    call gl(0,"bgcc0005a")
    call vsp(0,1)
    with wipeleft
    play bgm "bgm/bgm005.ogg"
    voice "vfccb2007fyu000"
    冬子 "「……ったら！」"
    "耳元で怒鳴られて、我に返る。"
    太一 "「は、はい？」"
    call gl(1,"TCKT0003b|TCKT000x")
    call gp(1,t=center)#x=230
    call vsp(1,1)
    with dissolve
    voice "vfccb2007fyu001"
    冬子 "「ぼーっとしてた。無視してた。傷ついた」"
    太一 "「あのなぁ」"
    太一 "「俺にはぼーっとする権利もないのですか？」"
    call gl(1,"TCKT0001b|TCKT000x")
    call vsp(1,1)
    with dissolve
    voice "vfccb2007fyu002"
    冬子 "「……宮澄先輩のこと考えてたりとかして」"
    太一 "「男のこと考えてた」"
    call gl(1,"TCKT0004b|TCKT000x")
    call vsp(1,1)
    with dissolve
    voice "vfccb2007fyu003"
    冬子 "「！！？？」"
    "冬子は衝撃に包まれた（見た感じ）。"
    call gl(1,"TCKT0006b|TCKT0006")
    call vsp(1,1)
    with dissolve
    voice "vfccb2007fyu004"
    冬子 "「おとこぉ……やだ……そんなの……（赤面）」"
    太一 "「なんてこった」"
    "最悪だった。"
    "しかもあながち外れじゃない。"
    太一 "「夢見る娘よ、あまり夢を見るなよ」"
    call gl(1,"TCKT0005b|TCKT000x")
    call vsp(1,1)
    with dissolve
    voice "vfccb2007fyu005"
    冬子 "「……３馬鹿もいつもそんな感じだったら、ちょっとは夢があるのにね」"
    太一 "「ヤメレ！」"
    "気色悪い。"
    "あの二人を相手に純愛ラブストーリーなんて。"
    stop bgm
    hide pic1
    with dissolve
    menu:
        "太一『……』"
        "桜庭を誘う":
            $B=1
        "友貴を誘う":
            $B=2
    if B == 1:
        jump LSAKU
    else:
        jump LTOMO
label LSAKU:
    call gl(1,"TCSH0001|tcsh")
    call gp(1,t=center)#x=190
    call vsp(1,1)
    with dissolve
    voice "vmccb2007sku000"
    "桜庭『太一、俺を本気にさせるなよ』"
    #goto *LBOB
label LTOMO:
    call gl(1,"TCST0000b|TCST0000")
    call gp(1,t=center)#x=200
    call vsp(1,1)
    with dissolve
    voice "vmccb2007yki000"
    "友貴『僕はおまえのそーいうトコ、嫌いじゃないよ』"
    #goto *LBOB
label LBOB:
    hide pic1
    with dissolve
    extend "ぞぞぞぞぞっ！"
    with vpunch
    play bgm "bgm/bgm005.ogg"
    太一 "「どーしてそー気色悪いこと考えるんだよ、友情だよ友情、普通の！」"
    call gl(1,"TCKT0000b|TCKT000x")
    call gp(1,t=center)#x=230
    call vsp(1,1)
    with dissolve
    voice "vfccb2007fyu006"
    冬子 "「気色悪いないでしょー。少なくとも３馬鹿って、みてくれはそれっぽく見えるもの」"
    太一 "「……俺を含めるな」"
    call gl(1,"TCKT0006b|TCKT0006")
    call vsp(1,1)
    with dissolve
    voice "vfccb2007fyu007"
    冬子 "「やだ、まだ醜いアヒルの子してるの？」"
    太一 "「うるへえ！」"
    "深刻な問題だぞ。"
    "自虐ネタにしてどうにか保ってるんだ。"
    "確かに……面貌の問題ではないのかも知れないが……。"
    "わかっていても、意識改革なんてそう簡単にはできん。"
    "だって、"
    "だってなぁ……。"
    太一 "「とにかくだ」"
    太一 "「気色悪いことを考えた罰！」"
    call gl(1,"TCKT0000b|TCKT000x")
    call vsp(1,1)
    with dissolve
    voice "vfccb2007fyu008"
    冬子 "「えっ？」"
    call gl(0,"evcc0023")
    call gl(5,"bgcc0000e")
    call vsp(1,0)
    play se "se100"
    call vsp(5,1)
    with dissolve
    hide pic1
    with dissolve
    call vsp(0,1)
    with dissolve
    hide pic5
    with dissolve
    with vpunch
    "セキララー！"
    "そんなオノマトペがどこからか聞こえた。"
    voice "vfccb2007fyu009"
    冬子 "「……ッッッ！！」"
    太一 "「どっせーい！」"
    "スカートのはしをつかんだまま、頭上に固定する。"
    "今、冬子の辱められっぷりは、並じゃない！"
    "しかも公道。"
    "さあ、どうする冬子！"
    "どうするッッッ、真剣サムライ娘ッッッ！（予告風）"
    "実のところ。"
    "殴られるのを覚悟していたし、期待してもいた。"
    "ところがである。"
    call gl(0,"evcc0023a")
    call vsp(0,1)
    with Dissolve(500.0/1000.0)
    冬子 "「……………………」"
    "ジト目で、俺を見るばかり。"
    "軽く朱色に染まったりなんかしちゃって。"
    "申し訳程度におさえた手に、本気でスキャンティをガードしようという意志はない。"
    "つうかモロ見えてるし。"
    太一 "「なん……で……怒ら……な？」"
    voice "vfccb2007fyu011"
    冬子 "「……だって、誰も見てないし……」"
    太一 "「そ！」"
    "唇が震える。"
    太一 "「そうじゃないだろう！？」"
    voice "vfccb2007fyu012"
    冬子 "「どうしてめくった方が怒るの？」"
    太一 "「そこはガーンと行くところだろう？」"
    太一 "「さあ、おまえの技を見せてくれ」"
    voice "vfccb2007fyu013"
    冬子 "「……離してよ、歩けないわ」"
    voice "vfccb2007fyu014"
    冬子 "「それに……恥ずかしい」"
    "ポッ"
    太一 "「ポッって……」"
    太一 "「それだけ？」"
    "こく、と少女はうなずく。"
    "嗚呼。"
    "ニーチェは言った。"
    "冬子は死んだ、と。"
    "否。"
    "冬子という個が死んだのではない。"
    "冬子に見立てられていた、手の早い勝ち気娘という、大いなる最大公約数的価値観が喪失せしめられたのである。"
    "冬子の個性の一部が死んだことを意味する。"
    "冬子はリアルになってしまった。また。"
    "けど俺は、いつもカリカリしている冬子が好きなんだけどなぁ。"
    "だって、それが一番安定してる。"
    "よし、こうなったら―――"
    太一 "「禁断の奥義をば」"
    voice "vfccb2007fyu015"
    冬子 "「もうはなしてよー……スースーして落ち着かないわ」"
    太一 "「もっとスースーするようにしてやる。パンツを脱いだりナプキンを押さえたりできなくしてやる」"
    voice "vfccb2007fyu016"
    冬子 "「……ちょっと、このまま引っ張るつもりじゃないでしょうね―――」"
    太一 "「てやー」"
    "そして俺は、"
    "禁じ手を解放し、"
    call gl(0,"evcc0023b")
    call vsp(0,1)
    with Dissolve(500.0/1000.0)
    "下着をおろした。"
    "足首まで。"
    "はやくモザイク！　はやくはやく！"
    "おっともうかかってたか、さすがに仕事がはやいぜ！"
    "死活問題だもんな！"
    太一 "「オゥ、トーコ！　セ　シ　ボン！（とっても素敵だ！）　セ　シ　ボン！（とっても素敵だ！）」"
    "得意のフランス語を駆使して、俺は冬子の陰部を絶賛した。"
    冬子 "「……」"
    冬子 "「……………………」"
    voice "vfccb2007fyu019"
    冬子 "「んのぉぉぉぉぉっ！！」"
    "『こんのぉ』と言っている。"
    "舌っ足らずなのだろう。"
    "キスするとよくわかる。"
    "ちょっと舌を吸うと、アップアップするから。"
    "でも反面、彼女の口腔は炉のように熱い。"
    "舌もクリームめいて柔らかく、味わうと陶然とする。"
    extend "俺は冬子とのラブラチオな日々に思いを馳せた。"
    "※ラブラチオ＝太一語。口唇愛撫全般を意味する……らしい。由来不明。ラブ＋フェラチオだと思われる。"
    "と。"
    voice "vfccb2007fyu020"
    冬子 "「スカポンターーーーーーーーーーンッッッ！！」"
    stop bgm
    call gl(4,"sgcc0012")
    call vsp(4,1)
    with dissolve
    play se "se106"
    with vpunch
    "どかーん！"
    太一 "「これこれーーーーーーっ！！」"
    "舞いながら俺は思った。"
    "もういない、新川豊という男のことを。"
    call gl(0,"bgcc0000d")
    call vsp(1,0)
    call vsp(0,1)
    call vsp(4,0)
    with Dissolve(500.0/1000.0)
    pause (500.0/1000.0)
    pause (500.0/1000.0)
    return
    #