label ccb0006:
    play bgm "bgm/bgm004.ogg"
    call gl(0,"bgcc0008s")
    call vsp(0,1)
    call vsp(1,0)
    with Pixellate(300.0*2/1000.0,5)
    play se "se001"
    "蝉がうるさい。"
    "こんな暑いのに。"
    "奴らはいつだって本気だ。"
    太一 "「しかし」"
    "どうするかな、これから。"
    "屋上が炎天下となると、涼める場所はさほどない。"
    "手近な教室をのぞいてみると、案の定授業中だった。"
    "一年Ｅ組では、まちこ先生が授業をしていた。"
    太一 "「……」"
    "彼女とは、表層的な心の交流さえ結べなかった。"
    "あまりにも普通すぎたのだろう。"
    "今はもう他人だ。"
    "とにかく、このまま廊下をウロウロしてたら誰かに見つかる。"
    call gl(0,"bgcc0009s")
    call vsp(0,1)
    with wipeleft
    "人気のない学食で、食券を買う。"
    call gl(0,"bgcc0010s")
    call vsp(0,1)
    with wipeleft
    "部室へ。"
    "友貴が漫画雑誌を読んでいた。"
    "軽く会話をかわす。"
    "途中、マンモスが通過して大騒ぎとなった。"
    "きゃつが過ぎ去ったあと。"
    voice "vmcca0007yki028"
    友貴 "「あぶないあぶない」"
    voice "vfcca0007myk012"
    みゆき "「カーテンつけた方がいいですよねぇ、廊下側の窓」"
    voice "vmcca0007yki029"
    友貴 "「禁止されてるんだよ。学校もよくわかってるよな」"
    太一 "「いい手がある」"
    voice "vfcca0007myk013"
    みゆき "「……」"
    voice "vmcca0007yki030"
    友貴 "「……」"
    太一 "「あー、諸君らが俺をどう思っているかは知っている。だがこれはつまらないギャグではなくマジでいい手なのだ」"
    voice "vfcca0007myk014"
    みゆき "「どんなんです？」"
    太一 "「友貴、マシン使えるようにしてくれよ。あとデジカメ」"
    友貴 "「はーん？」"
    "……。"
    "…………。"
    "……………………。"
    太一 "「という感じでどうだ」"
    call gl(1,"TCST0000s|TCST0000")
    call gp(1,t=center)#x=190
    call vsp(1,1)
    with dissolve
    voice "vmccb0006yki000"
    友貴 "「カムフラージュか、へー」"
    "フルカラー印刷した『無人の室内』画像を、窓ガラスの内側に貼り付けた。"
    "視点が多少ずれてしまうが、パッと見るくらいならある程度はごまかせる。"
    call gl(1,"TCST0004s|TCST0004")
    call vsp(1,1)
    with dissolve
    voice "vmccb0006yki001"
    友貴 "「うん、これならばれないかも」"
    太一 "「わはは」"
    "誇る俺。"
    "そこにみゆきがトイレから戻ってくる。"
    太一 "「トイレどうだった？」"
    voice "vfccb0006myk000"
    みゆき "「あーんっ！」"
    "泣いた。"
    voice "vfccb0006myk001"
    みゆき "「トイレだなんて一言もいってないのにー！」"
    太一 "「ハンカチで手をふきふきしながら戻ってくれば誰だってわかるわい！」"
    call gl(1,"TCST0005s|TCST0004")
    call vsp(1,1)
    with dissolve
    voice "vmccb0006yki002"
    友貴 "「だからさ」"
    voice "vfccb0006myk002"
    みゆき "「気がついても言わないでくださいよぅ」"
    太一 "「だめだだめだ！　隙が多すぎる！」"
    太一 "「多すぎてもダメ！　少なすぎてもダメ！」"
    call gl(1,"TCST0003s|TCST0000")
    call vsp(1,1)
    with dissolve
    voice "vmccb0006yki003"
    友貴 "「なんの基準なんだ……」"
    太一 "「正しい淑女のガイドライン」"
    voice "vfccb0006myk003"
    みゆき "「なりたくないですよぅ」"
    "俺は愕然とした。"
    太一 "「な、なんてふしだらなことを」"
    太一 "「折檻だな、折檻！　折檻！　折檻！」"
    "騒ぎながらみゆきの周囲をまわる。"
    voice "vfccb0006myk004"
    みゆき "「ううう」"
    "怯えるみゆき。"
    "くそう、地味なやつめ。"
    "その地味さが俺をかき立てる。"
    太一 "「折檻！　折檻！　折檻！」"
    "とスカートをゆっくりめくっていく。"
    call gl(1,"TCST0001s|TCST0001")
    call vsp(1,1)
    with dissolve
    voice "vmccb0006yki004"
    友貴 "「お、おいおい」"
    太一 "「もし毛糸のパンツをはいていたら、汝の罪は許されるであろう」"
    太一 "「しかーし、もし薄手のショーツなどを生意気にも着用しているようであればぁ」"
    voice "vfccb0006myk005"
    みゆき "「あううぅぅぅっ」"
    stop bgm
    voice "vfccb0006kri000"
    霧 "「ちょやーッ！」"
    "この声は？"
    call gl(4,"sgcc0013s")
    hide pic1
    with dissolve
    call vsp(4,1)
    with dissolve
    play se "SE106"
    with vpunch
    太一 "「がああっ！？」"
    play bgm "bgm/bgm011.ogg"
    voice "vfccb0006kri001"
    霧 "「この女の敵っ！！」"
    "背後からの踵落としですかそうですか。"
    "ゆっくりと俺の意識は混濁して……いく直前で復帰した。"
    play se "SE038"
    extend "べち"
    with vpunch
    "気絶していれば、床に顔面を叩きつける苦痛も感じなかったものを。"
    call vsp(4,0)
    with Dissolve(500.0/1000.0)
    太一 "「……くぅ……痛いじゃないか、下級生」"
    "ギロッという感じの視線が、俺を射竦める。"
    call gl(1,"TCSK0002s|TCSK000x")
    call gp(1,t=center)#x=180
    call vsp(1,1)
    with dissolve
    voice "vfccb0006kri002"
    霧 "「どっちが悪いのか、一目瞭然ですから」"
    voice "vfccb0006myk006"
    みゆき "「あ、あの、あなたは？」"
    voice "vfccb0006kri003"
    霧 "「通りすがりの転入生」"
    太一 "「おうおう、絵になる光景だのう、友貴よ」"
    voice "vmccb0006yki005"
    友貴 "「頼むから僕が仲間であるかのように話しかけないでくれ」"
    "友貴は冷たいので我関せずの立場を取った。"
    太一 "「ちっ、偽善者め」"
    "まあいい。"
    太一 "「おい下級生、葬り去る前に名前くらいは聞いてやるぞ」"
    call gl(1,"TCSK0001s|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfccb0006kri004"
    霧 "「痴漢！」"
    太一 "「俺を置き換えるだと！？」"
    voice "vmccb0006yki006"
    友貴 "「果てしなくバカだね」"
    call gl(1,"TCSK0011s|TCSK0011")
    call vsp(1,1)
    with dissolve
    voice "vfccb0006kri005"
    霧 "「先生に報告しますから」"
    太一 "「ほ、先生とな。どの先生に泣きつくつもりかな、おぜうさん？」"
    call gl(1,"TCSK0002s|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfccb0006kri006"
    霧 "「誰にでも」"
    call gl(1,"TCSK0001s|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfccb0006kri007"
    霧 "「だってこんなの、セクハラじゃない！」"
    voice "vmccb0006yki007"
    友貴 "「……黒須と知り合ってまだ間もないけど」"
    voice "vmccb0006yki008"
    友貴 "「セクハラという単語を聞く回数が飛躍的に増えて嬉しいよ。ありがとう」"
    太一 "「気にするなマイフレン、人徳のなすわざだ」"
    call gl(1,"TCSK0011s|TCSK0011")
    call vsp(1,1)
    with dissolve
    voice "vfccb0006kri008"
    霧 "「堂々とスカートめくろうとするなんて……最低！」"
    太一 "「へえ。偉いんだ」"
    太一 "「でそれを、先生に言いつけると？」"
    call gl(1,"TCSK0021s|TCSK0021")
    call vsp(1,1)
    with dissolve
    voice "vfccb0006kri009"
    霧 "「そうよ！」"
    太一 "「なあ、正義のヒロインちゃんはこんなことは考えないのかな？」"
    太一 "「なぜ俺が白昼堂々と、しかも人前でスカートをことさらゆっくりめくろうとしていたか」"
    voice "vmccb0006yki009"
    友貴 "「……単に反応を愉しみたかったダゲァ！？」"
    play se "se003"
    with vpunch
    "正拳側中段突き。"
    太一 "「そしてなぜこの風紀委員長·島友貴がそれを止めることもできずにいたのか」"
    voice "vmccb0006yki010"
    友貴 "「はい！？」"
    call gl(1,"TCSK0003s|TCSK0003")
    call vsp(1,1)
    with dissolve
    voice "vfccb0006kri010"
    霧 "「ま、まさか……」"
    太一 "「そのまさかさ」"
    太一 "「すなわちそれは、俺がこの学院で絶大な権力を有していることを意味している！！」"
    太一 "「のう、友貴よ？」"
    voice "vmccb0006yki011"
    友貴 "「だからこっちに振るなと」"
    call gl(1,"TCSK0001s|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfccb0006kri011"
    霧 "「あんたたちっ！」"
    voice "vmccb0006yki012"
    友貴 "「おいっ！　僕は違うぞ！」"
    voice "vfccb0006kri012"
    霧 "「許さない。絶対絶対許さない！」"
    voice "vmccb0006yki013"
    友貴 "「そもそも風紀委員ってのが違うダボァ！？」"
    play se "se003"
    with vpunch
    "正拳側上段突き。"
    太一 "「ふっふっふ」"
    "ポケットに手をつっこみ、瞑想するかのように目を閉じ、名悪役の物腰で、"
    太一 "「すなわちそれは、俺がこの学院で絶大な権力を有していることを意味している！！」"
    "語尾とともにくわっと開眼した。"
    voice "vmccb0006yki014"
    友貴 "「それさっき言った」"
    太一 "「……」"
    voice "vmccb0006yki015"
    友貴 "「使いどころが少し早すぎたんじゃないかな、さっきの」"
    太一 "「…………」"
    call gl(1,"TCSK0002s|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfccb0006kri013"
    霧 "「群青学院にはいじめはないって聞いてたのに……」"
    voice "vfccb0006myk007"
    みゆき "「あの、いじめられていたわけではないので」"
    call gl(1,"TCSK0000s|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfccb0006kri014"
    霧 "「……え？」"
    voice "vfccb0006myk008"
    みゆき "「あの人たちは、いつもああなんです。悪気ないんです」"
    voice "vmccb0006yki016"
    友貴 "「たちって……」"
    "友貴はげんなりした。"
    太一 "「たちって……」"
    "俺はげんなりとした。"
    call gl(4,"sgcc0001s")
    hide pic1
    with dissolve
    play se "se003"
    call vsp(4,1)
    with dissolve
    with vpunch
    voice "vmccb0006yki017"
    友貴 "「おまえがげんなりとする理由がどこにあるんだよー！」"
    太一 "「俺は偽善者じゃない！」"
    voice "vmccb0006yki018"
    友貴 "「僕だって違う！」"
    太一 "「やるかー！」"
    "もみあいに。"
    voice "vmccb0006yki019"
    友貴 "「薄味マキャベリスト！」"
    with vpunch
    太一 "「シスコン殺人事件！」"
    with vpunch
    voice "vmccb0006yki020"
    友貴 "「低学歴低収入！」"
    with vpunch
    太一 "「アースデプリ！」"
    with vpunch
    voice "vmccb0006yki021"
    友貴 "「株の敗残者！」"
    with vpunch
    太一 "「かかか株のことは言うなー！！」"
    with vpunch
    voice "vfccb0006kri015"
    霧 "「仲間割れをっ！？」"
    voice "vfccb0006myk009"
    みゆき "「あーあ……」"
    voice "vmccb0006yki022"
    友貴 "「おまえだって人のこと、シスコンオナニーのプロとかあちこちで吹聴しただろ！」"
    太一 "「ああ言ったさ！　特に女の子に言ったさ！　皆もう大喜びさ！」"
    voice "vmccb0006yki023"
    友貴 "「あれからたまにプロとか呼ばれるようになったんだぞー！」"
    太一 "「事実だろうが！」"
    voice "vmccb0006yki024"
    友貴 "「こっちだって事実だ！」"
    太一 "「くっそー！」"
    voice "vmccb0006yki025"
    友貴 "「なにをー！」"
    play se "se039"
    extend "ポカポカポカポカッ！！"
    with vpunch
    hide pic4
    with dissolve
    "そして。"
    "俺たちは自滅した。"
    voice "vmccb0006yki026"
    友貴 "「ううう」"
    太一 "「ぐぐぐ」"
    "廊下に仰臥する二人。"
    voice "vfccb0006myk010"
    みゆき "「……保健室行きますか？」"
    太一 "「さ、さっきの正義の味方は？」"
    call gl(1,"TCSK0000s|TCSK000x")
    call gp(1,t=center)
    call vsp(1,1)
    with dissolve
    voice "vfccb0006kri016"
    霧 "「佐倉霧。正義の味方じゃない」"
    "少女は俺たちを見下しながら言った。"
    call gl(1,"TCSK0011s|TCSK0011")
    call vsp(1,1)
    with dissolve
    voice "vfccb0006kri017"
    霧 "「……そしてあなたたちも、悪なんて美意識のあるものじゃないことがわかった」"
    "ぶわっと友貴が滂沱する。"
    voice "vmccb0006yki027"
    友貴 "「ぼ、僕は関係ないのに。太一のせいで僕まで……」"
    "友貴はカブトの幼虫みたいに丸くなった。"
    voice "vmccb0006yki028"
    友貴 "「いいもう。引きこもる」"
    "しくしく泣き出す。"
    voice "vfccb0006myk011"
    みゆき "「そこまで……」"
    call gl(1,"TCSK0002s|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfccb0006kri018"
    霧 "「この子もいいって言うし、その無様さに免じて今回だけは見逃してあげます」"
    太一 "「……体が動くようになったら……おぼえてろよ……霧とやら」"
    "霧は冷笑した。"
    call gl(1,"TCSK0000s|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfccb0006kri019"
    霧 "「どうぞ、ご自由に」"
    stop se
    call gl(0,"bgcc0000d")
    call vsp(0,1)
    call vsp(1,0)
    with Dissolve(500.0/1000.0)
    "佐倉霧との出会いだった。"
    stop bgm
    pause (500.0/1000.0)
    pause (500.0/1000.0)
    return
    #