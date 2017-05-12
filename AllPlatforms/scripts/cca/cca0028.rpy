label cca0028:
    stop bgm
    call gl(0,"bgcc0000b")
    call vsp(0,1)
    call vsp(1,0)
    call vsp(2,0)
    call vsp(3,0)
    call vsp(4,0)
    call vsp(5,0)
    "海水浴……か。"
    "美希には悪いけど、思い出にはなった。"
    "思い出は、心を豊かにしてくれる。"
    "だから、こんなことも言えてしまう。"
    太一 "「気にくわないこともあるだろうけど、明日から部活、来てみないか？」"
    play bgm "bgm/bgm013.ogg"
    voice "vfcca0028fyu000"
    冬子 "「……え？」"
    "困惑と戸惑いを貼りつけて、彼女は伏していた顔をあげた。"
    "憔悴したその面差しが、緋色に色づけされてどこか悲壮な印象を与えた。"
    pause (500.0/1000.0)
    call gl(0,"bgcc0000d")
    call vsp(0,1)
    stop bgm
    with Dissolve(500.0/1000.0)
    pause (1000.0/1000.0)
    play bgm "bgm/bgm003.ogg"
    call gl(0,"bgcc0003b")
    call vsp(0,1)
    with wipeleft
    太一 "「……うーむ」"
    "夜は原稿書きだ。"
    "いまいちはかどらない。"
    "ありきたりな内容。"
    "けど、とりあえずは進めておかないと。"
    太一 "「おもしろみに欠けるねぇ」"
    "そうだ。"
    "先輩に見てもらうか。"
    "思い立ったが吉日。"
    "すぐに家を出た。"
    call gl(0,"bgcc0000c")
    call vsp(0,1)
    with wipeleft
    "先輩の家だ。"
    "ノックをしてみるが、反応がない。"
    太一 "「せんぱーい！」"
    "やはりレスポンスがない。"
    太一 "「あなたの太一が来ましたよー！」"
    "シーン"
    "留守かな。"
    太一 "「……」"
    stop bgm
    "まさか、まだ学校にいる？"
    call gl(0,"bgcc0007b")
    call vsp(0,1)
    with wipeleft
    太一 "「うわー、いるし！」"
    play bgm "bgm/bgm012.ogg"
    call gl(1,"TCMM0004c|TCMM000x")
    call gp(1,t=center)
    call vsp(1,1)
    with dissolve
    voice "vfcca0028msa000"
    見里 "「わっ、ぺけくん？」"
    太一 "「無茶しすぎ！」"
    call gl(1,"TCMM0005c|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfcca0028msa001"
    見里 "「ご、ごめんなさい」"
    太一 "「はー」"
    "例によってというか、アンテナを組み立てていたようだ。"
    太一 "「こんな暗くて作業も何もないでしょーが」"
    voice "vfcca0028msa002"
    見里 "「気になっちゃって……ダメですか？」"
    太一 "「ダメ」"
    太一 "「そんなことしてる暇があったら、原稿見てくださいよ」"
    call gl(1,"TCMM0000c|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfcca0028msa003"
    見里 "「おや、もうできましたか？」"
    太一 "「途中です。でも意見聞きたくて」"
    call gl(1,"TCMM0005c|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfcca0028msa004"
    見里 "「あー、でもこう暗いと……読めないですね」"
    太一 "「そですね」"
    太一 "「もういいですから帰りましょう」"
    call gl(1,"TCMM0000c|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfcca0028msa005"
    見里 "「あ、でも……もうちょっと」"
    太一 "「みみ先輩……」"
    call gl(1,"TCMM0005c|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfcca0028msa006"
    見里 "「だってぇ～」"
    太一 "「焦って進めても、得るものはないんですよ」"
    call gl(1,"TCMM0000c|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfcca0028msa007"
    見里 "「……」"
    太一 "「ゆっくりやればいいんです。違いますか？」"
    太一 "「時間はたっぷりあるんですから」"
    太一 "「それに急げば……それだけはやく終わってしまう」"
    太一 "「先輩、それに耐えられるんですか？」"
    play bgm "bgm/bgm015.ogg"
    call gl(1,"TCMM0003c|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfcca0028msa008"
    見里 "「……っ」"
    "泣きそうな顔。"
    "背筋が痺れた。"
    "つい、自分が禁忌を口走っていたことに気づく。"
    voice "vfcca0028msa009"
    見里 "「……わたし、逃げてるんでしょうか」"
    太一 "「そですね」"
    voice "vfcca0028msa010"
    見里 "「そう、見えちゃいますか？」"
    太一 "「見えちゃいます」"
    太一 "「作業に没頭することで、逃げてる」"
    "アンテナを見あげる。"
    太一 "「無理矢理、仕事を作るようにして……わざと手間がかかるやり方で」"
    call gl(1,"TCMM0005c|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfcca0028msa011"
    見里 "「……見抜かれてましたか」"
    太一 "「それが普通だと思ったんです」"
    call gl(1,"TCMM0000c|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfcca0028msa012"
    見里 "「え？」"
    太一 "「先輩のしていることは、そうおかしなことじゃない」"
    太一 "「逃避をしたことのない人間なんていませんよ」"
    太一 "「けど先輩みたいに、必死に逃避しなければならないのは……つらいことだ」"
    太一 "「もちません、心は」"
    call gl(1,"TCMM0003c|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfcca0028msa013"
    見里 "「…………」"
    太一 "「あなたは……３０を越えているはずだ」"
    voice "vfcca0028msa014"
    見里 "「…………」"
    太一 "「強度の自傷症状」"
    voice "vfcca0028msa015"
    見里 "「…………」"
    "無言という肯定。"
    "俺はただ、言葉を重ねる。"
    太一 "「一人で作業するのはいい。けど追いつめられているなら……このまま単独で没頭するのは危険だ」"
    太一 "「……弾けたとき、ここが屋上だってことが、危険だ」"
    太一 "「わかってますか？」"
    voice "vfcca0028msa016"
    見里 "「わかって、ますよ」"
    "ぽつ、と言う。"
    太一 "「たいへん心配です」"
    "先輩は眼鏡を外した。"
    "涙ぐんだ瞳に、指の背を添える。"
    call gl(1,"TCMM0003c|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfcca0028msa017"
    見里 "「ぺけくんに、心配されるくらい……不安定だったんですね、わたし」"
    太一 "「はは……その言い方は、失礼だなあ」"
    voice "vfcca0028msa018"
    見里 "「あはは」"
    voice "vfcca0028msa019"
    見里 "「君にこんなこと言われるなんてびっくりしました」"
    "涙をぬぐう。"
    call gl(1,"TCMM0002c|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfcca0028msa020"
    見里 "「……ありがとう」"
    太一 "「いいえ」"
    voice "vfcca0028msa021"
    見里 "「だって……みんなバラバラで……このまま霧散するみたいで」"
    太一 "「俺は霧散してないですよ」"
    call gl(1,"TCMM0000c|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfcca0028msa022"
    見里 "「だって、君はなんだか……動機が不純」"
    "ばれてた。"
    太一 "「まあ」"
    call gl(1,"TCMM0031c|TCMM0031")
    call vsp(1,1)
    with dissolve
    voice "vfcca0028msa023"
    見里 "「でも確かにわたし、意固地になっていたのかも」"
    太一 "「それに厳密には一人じゃないみたいですよ？」"
    call gl(1,"TCMM0000c|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfcca0028msa024"
    見里 "「え？」"
    太一 "「これ」"
    "先ほど、給水塔の下でひろった包みを見せる。"
    call gl(1,"TCMM0021c|TCMM0021")
    call vsp(1,1)
    with dissolve
    voice "vfcca0028msa025"
    見里 "「差し入れ？」"
    太一 "「イエス」"
    太一 "「ただし中身はカレーパン」"
    call gl(1,"TCMM0000c|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfcca0028msa026"
    見里 "「…………あ」"
    "気づいて、口元を押さえる。"
    太一 "「あいつも最近、ちょっとナーバスみたいでなかなか顔見せないですけど、ね」"
    太一 "「あのバカ、自分の仲間が追い込まれるの、見てられない性格してますから」"
    太一 "「こんな傷みかけのカレーパン持ってきて」"
    call gl(1,"TCMM0002c|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfcca0028msa027"
    見里 "「でもぺけくん、嬉しそう」"
    太一 "「食べます？」"
    call gl(1,"TCMM0000c|TCMM000x")
    call vsp(1,1)
    with dissolve
    "先輩は小さくうなずいた。"
    stop bgm
    "二人で、カレーパンを食べた。"
    call gl(0,"bgcc0000d")
    call vsp(0,1)
    call vsp(1,0)
    with wipeleft
    pause (1000.0/1000.0)
    pause (1000.0/1000.0)
    return
    #