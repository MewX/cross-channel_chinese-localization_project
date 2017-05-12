label ccd4003:
    #modewin
    if _in_replay:
        jump MKSCENE001
    play bgm "bgm/bgm018.ogg"
    call gl(0,"bgcc0003")
    call vsp(0,1)
    with wipeleft
    "目を覚ます。"
    "陽光が窓を貫いていた。"
    "熟睡していたらしい。夢一つ見なかった。"
    "時間は……７時。"
    "学校に行かねば。"
    call gl(0,"bgcc0011")
    call vsp(0,1)
    with wipeleft
    "美希がいた。"
    太一 "「また待ってるの？」"
    call gl(1,"TCYM0000|TCYM0000")
    call gp(1,t=center)#x=180
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki030"
    美希 "「……あ、先輩」"
    call gl(1,"TCYM0002|TCYM0002")
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki031"
    美希 "「来ないんですよ、なにかあったのかも……」"
    太一 "「霧から伝言持ってきてるよ」"
    call gl(1,"TCYM0000|TCYM0000")
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki032"
    美希 "「え？」"
    太一 "「曜子ちゃんと二人で、発電所の方を調査するらしいよ。漢だね！」"
    voice "vfCCD4001mki033"
    美希 "「支倉先輩……と？」"
    太一 "「うん。その支倉先輩に、今日はゲストで来てもらってます」"
    call gl(2,"TCHY0000|tchy000x")
    call gp(2,t=left)
    call gp(1,t=right)
    call vsp(2,1)
    call vsp(1,1)
    with Dissolve(500.0/1000.0)
    曜子 "「…………」"
    call gl(1,"TCYM0000|TCYM0000")
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki034"
    美希 "「……久しぶりにお会いします」"
    曜子 "「…………」"
    太一 "「はい、話して」"
    "背中をつつく。"
    call gl(2,"TCHY0002|tchy000x")
    call vsp(2,1)
    with dissolve
    voice "vfCCD4001you002"
    曜子 "「佐倉霧と発電所を調べる。誰にも邪魔はさせない」"
    "敵に告げるように言った。"
    call gl(1,"TCYM0004|TCYM0002")
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki035"
    美希 "「な、なるほど……」"
    "有無を言わさぬ迫力があった。"
    call gl(1,"TCYM0000|TCYM0000")
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki036"
    美希 "「霧ちんは今どこに？」"
    太一 "「すでに機上の人だ」"
    call gl(1,"TCYM0004|TCYM0002")
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki037"
    美希 "「えっ！？」"
    太一 "「そういうわけで会えない。そうだね曜子くん」"
    call gl(2,"TCHY0001|tchy000x")
    call vsp(2,1)
    with dissolve
    voice "vfCCD4001you003"
    曜子 "「……そう」"
    call gl(1,"TCYM0002|TCYM0002")
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki038"
    美希 "「そうですか……」"
    "しゅん。"
    太一 "「じゃ調査の方、よろしく」"
    voice "vfCCD4001you004"
    曜子 "「……わかった」"
    "のたくた敬礼しあう。"
    "彼女の出番はこれで終わりだ。"
    call gp(1,t=center)#x=180
    call vsp(1,1)
    call vsp(2,0)
    with Dissolve(500.0/1000.0)
    "……………………。"
    "で、曜子ちゃんを帰らせたあと。"
    stop bgm
    call gl(1,"TCYM0021|TCYM0021")
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki039"
    美希 "「支倉先輩が言うのなら、間違いはないですよね……」"
    太一 "「んだ」"
    call gl(1,"TCYM0003|TCYM0003")
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki040"
    美希 "「でも、ちゃんといるんだ、よかった」"
    "ない胸をなでおろす。"
    太一 "「なあ、どっか涼しいとこでお菓子でも食わない？」"
    play bgm "bgm/bgm002.ogg"
    call gl(1,"TCYM0001|TCYM0000")
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki041"
    美希 "「……お菓子？」"
    "目の色が変わった。"
    太一 "「あめ玉とグミキャンディー。手作り」"
    "目の色が変わった。"
    call gl(1,"TCYM0000|TCYM0000")
    call vsp(1,1)
    with dissolve
    voice "vfCCC0031bmki004"
    美希 "「てづくり？」"
    太一 "「んー。曜子ちゃんのだけど」"
    太一 "「シュガー控えめ、美容健康にいいらしい。グミはこんにゃくだね。０カロリー」"
    call gl(1,"TCYM0001|TCYM0000")
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki042"
    美希 "「０カロリー！？」"
    "決まりだった。"
    "……………………。"
    call gl(0,"bgcc0006")
    call vsp(0,1)
    call vsp(1,0)
    with wipeleft
    call gl(1,"TCYM0003|TCYM0003")
    call gp(1,t=center)#x=180
    call vsp(1,1)
    with dissolve
    voice "vfCCC0031bmki006"
    美希 "「ママの味がする……」"
    voice "vfCCC3104mki003"
    美希 "「やだ、ほっぺが……落ちそう……」"
    太一 "「うむうむ」"
    "手作りお菓子を食べて美希はご機嫌だ。"
    call gl(1,"TCYM0000|TCYM0000")
    call vsp(1,1)
    with dissolve
    voice "vfCCC0031bmki019"
    美希 "「支倉先輩も謎が多い人ですよね」"
    太一 "「んだね」"
    call gl(1,"TCYM0041|TCYM0041")
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki043"
    美希 "「恋人、なんですか？」"
    太一 "「いや、一緒に暮らしてただけだよ」"
    call gl(1,"TCYM0001|TCYM0000")
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki044"
    美希 "「同棲！」"
    太一 "「同棲とは違う」"
    太一 "「俺たちは親がいないから、二人ともあの家に世話になってただけだよ」"
    太一 "「姉弟みたいなもんだ」"
    call gl(1,"TCYM0000|TCYM0000")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3104mki007"
    美希 "「そうでしたか」"
    太一 "「さあ、千歳あめもやろう。二人でしゃぶってつららみたいにとがらせようぜ！」"
    call gl(1,"TCYM0003|TCYM0003")
    call vsp(1,1)
    with dissolve
    voice "vfCCC0031bmki020"
    美希 "「わー、ちとせあめだ！」"
    "ぱっと笑顔に。"
    call gl(0,"bgcc0003b")
    call vsp(0,1)
    call vsp(1,0)
    with wipeleft
    "美希と過ごす一日は、楽しかった。"
    "何気ないシーンの積み重ねではあったけど。"
    "印象以上に重い、その価値を俺は知っている。"
    "残された期間はわずかだ。"
    太一 "「……これも、だましてるってことになるのかな」"
    "でも向こうに帰れば、霧もいる。"
    "美希は許してくれるよな？"
    "どっちの美希も―――"
    stop bgm
    call gl(0,"bgcc0000d")
    call vsp(0,1)
    call vsp(1,0)
    with Dissolve(500.0/1000.0)
    call gl(0,"bgcc0005")
    call vsp(0,1)
    with wipeleft
    "水曜日。"
    "学校に。"
    call gl(0,"bgcc0011")
    call vsp(0,1)
    with wipeleft
    "脱走させないための門。"
    "学生を守っているというより、外の世界を、俺たちから守っているような。"
    "そんな印象を抱かせた。"
    太一 "「おはよう」"
    call gl(1,"TCYM0000|TCYM0000")
    call gp(1,t=center)#x=180
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki045"
    美希 "「よーす」"
    太一 "「霧だったら―――」"
    call gl(1,"TCYM0021|TCYM0021")
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki046"
    美希 "「ああ、いえ今日は違います」"
    play bgm "bgm/bgm004.ogg"
    call gl(1,"TCYM0000|TCYM0000")
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki047"
    美希 "「先輩待ちです」"
    太一 "「ふふふ、それって、期待しちゃってもいいってこと？」"
    call gl(1,"TCYM0003|TCYM0003")
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki048"
    美希 "「恋愛感情は０ですけど大好きです」"
    太一 "「……………………」"
    "遠い。"
    call gl(1,"TCYM0001|TCYM0000")
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki049"
    美希 "「ん……？」"
    voice "vfCCD4001mki050"
    美希 "「先輩、なんだかすえた臭いがしますね？」"
    太一 "「ああ、これ香水。汗の香り、スエット·ミント」"
    call gl(1,"TCYM0004|TCYM0002")
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki051"
    美希 "「うそだーーーーーーっ！　そんな香水あるわけねぇーーーーーーっ！」"
    call gl(1,"TCYM0001|TCYM0000")
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki052"
    美希 "「え……お風呂は？」"
    太一 "「風呂……？」"
    太一 "「俺は紳士だから風呂いらいん」"
    voice "vfCCD4001mki053"
    美希 "「……水浴びとか……」"
    太一 "「水もったいないじゃん」"
    call gl(1,"TCYM0002|TCYM0002")
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki054"
    美希 "「ぐあ……じゃあ……今日で……？」"
    太一 "「水曜日だからぁ、三日目かなぁ？」"
    "アホ口調で告げる。"
    call gl(1,"TCYM0004|TCYM0002")
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki055"
    美希 "「はっふー」"
    hide pic1
    with dissolve
    "気絶した。"
    太一 "「大丈夫か！」"
    "俺は上着を脱いで美希にのしかかった。"
    voice "vfCCD4001mki056"
    美希 "「わわわわわっ！？」"
    "本気の抵抗。"
    "……………………。"
    call gl(1,"TCYM0001|TCYM0000")
    call gp(1,t=center)
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki057"
    美希 "「……うっかり気絶もできませんね……」"
    太一 "「すまん、脊髄反射で」"
    call gl(1,"TCYM0041|TCYM0041")
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki058"
    美希 "「……なんて危険な脊髄」"
    太一 "「まあ気にするなよ。風呂に入らなくとも死ぬことはないぜ」"
    call gl(1,"TCYM0001|TCYM0000")
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki059"
    美希 "「汗くさい先輩きらいです」"
    太一 "「……そんなこと言われても」"
    voice "vfCCD4001mki060"
    美希 "「来てください」"
    "連れて行かれる。"
    call gl(0,"bgcc0007")
    call vsp(0,1)
    call vsp(1,0)
    with wipeleft
    "美希がプレハブからホースを持ってきた。"
    call gl(1,"TCYM0000|TCYM0000")
    call vsp(1,1)
    with dissolve
    voice "vfCCC4003mki017"
    美希 "「せんぱい、服脱いで」"
    call gl(1,"TCYM0001|TCYM0000")
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki061"
    美希 "「もち、下も」"
    太一 "「いいとも」"
    "脱ぐ。"
    call gl(1,"TCYM0004|TCYM0002")
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki062"
    美希 "「な、なんて下着を……」"
    "美希はまっ赤だ。"
    太一 "「この展開は読めていた！」"
    太一 "「だから原作に忠実にしてみた」"
    "屋上に佇立するのは、限りなくぞうさんパンツの俺だ。"
    "ホースに装着されたホルダーの弁が解放された。"
    call gl(1,"TCYM0001|TCYM0000")
    call vsp(1,1)
    with dissolve
    voice "vfCCC4003mki019"
    美希 "「じゃー！」"
    "強烈な水流が、俺を襲う。"
    太一 "「うぷっ」"
    call gl(1,"TCYM0003|TCYM0003")
    call vsp(1,1)
    with dissolve
    voice "vfCCC4003mki020"
    美希 "「そらそらー」"
    "むっとするシトラスミント。"
    "ボディソープをぶちまけられた。"
    "しかもボトル一本分。"
    "……俺はそんなクサイか。"
    call gl(1,"TCYM0001|TCYM0000")
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki063"
    美希 "「先輩、ごしごしこすって！」"
    太一 "「はいはい……」"
    call gl(1,"TCYM0000|TCYM0000")
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki064"
    美希 "「私が水かけますから、先輩は洗うのに専念してください」"
    太一 "「物言わぬ無洗米になりたい……」"
    call gl(1,"TCYM0003|TCYM0003")
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki065"
    美希 "「じゃがー」"
    "猫科の哺乳動物を連想させる水音の擬声語が斬新だった。"
    "やっぱり美希は俺の見込んだ有望なルーキーだ。"
    太一 "「霧とペアのときはプールでイチャイチャしてるくせに、俺のときはばっちぃ扱いか、ちぇっ」"
    voice "vfCCD4001mki066"
    美希 "「……」"
    "水流が像の鼻を叩いた。"
    "勃った。"
    call gl(1,"TCYM0002|TCYM0002")
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki067"
    美希 "「どーしてそれだけでそーなるんですかぁ！！」"
    "泣かれた。"
    太一 "「俺の敏感ボディにきいてくれ……」"
    voice "vfCCD4001mki068"
    美希 "「もうしらなーい！」"
    太一 "「だから下半身は別の生き物だというのに」"
    太一 "「ま……ついでにここもキレイにしておくか」"
    "ぞうカバーの上から竿を軽くしごきつつ、ボタンを外そうとする。"
    call gl(1,"TCYM0005|TCYM0003")
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki069"
    美希 "「やめれーっ！　処女の前ですることかっ！！」"
    太一 "「ごわっ！？」"
    "最大の水力で、顔面を叩かれた。"
    call gl(0,"bgcc0000a")
    call vsp(0,1)
    call vsp(1,0)
    with Dissolve(500.0/1000.0)
    "転倒したら、空が見えた―――"
    stop bgm
    pause (500.0/1000.0)
    pause (500.0/1000.0)
    call gl(0,"bgcc0011")
    call vsp(0,1)
    with wipeleft
    "美希は来ていない。"
    "思い出す。"
    "美希とはじめて出会った日のこと。"
    play se "SE001"
    call gl(0,"bgcc0011bs")
    call vsp(0,1)
    with Pixellate(300.0*2/1000.0,5)
    play bgm "bgm/bgm003.ogg"
    "美希に声をかけたのは、群青全体でも俺が最初だと思う。"
    "彼女は本来の学校を追い出されて、群青にやってきたラブリーな子羊ちゃんだった。"
    "初日。"
    "彼女は昼ご飯というものを持ってこなかった……らしい。"
    "その情報を、美希とクラスメイトになったみゆき経由でゲットすると、即捜しに出向いた。"
    "偶然を装って出会いイベントをセッティングするためだ。"
    "近隣に迷惑をかけないよう閉ざされた正門前。"
    "美希はそこで立ち往生していた。"
    "編入者のパターンと言える。"
    太一 "「ハーイ！」"
    call gl(1,"TCYM0004s|TCYM0002")
    call gp(1,t=center)#x=180
    call vsp(1,1)
    with dissolve
    voice "vfCCC4012mki000"
    美希 "「……え？」"
    "で、いろいろあって。"
    call gl(1,"TCYM0000s|TCYM0000")
    call vsp(1,1)
    with dissolve
    voice "vfCCC4012mki030"
    美希 "「ぷっ」"
    "小さく笑って。"
    voice "vfCCC4012mki031"
    美希 "「……変な人」"
    "ちょっとうち解けて。"
    call gl(0,"bgcc0006s")
    call vsp(0,1)
    call vsp(1,0)
    with wipeleft
    太一 "「こうなったら強引にここで食う！」"
    voice "vfCCC4012kri008"
    霧 "「な、なにしてんですか！？」"
    "同じ目的の霧と口論になって。"
    call gl(1,"TCYM0003s|TCYM0003")
    call vsp(1,1)
    with dissolve
    voice "vfCCC4012mki046"
    美希 "「あはははは……なんだかなぁ」"
    "言い争うのを、美希は複雑な表情で見ていた。"
    call gl(0,"bgcc0000d")
    call vsp(0,1)
    call vsp(1,0)
    with Dissolve(500.0/1000.0)
    pause (500.0/1000.0)
    pause (500.0/1000.0)
    stop se
    call gl(0,"bgcc0011")
    call vsp(0,1)
    with wipeleft
    "いくら待っても、美希は来なかった。"
    太一 "「……仕方ない」"
    "気が滅入る。"
    "風に当たりたい。"
    call gl(0,"bgcc0007")
    call vsp(0,1)
    with wipeleft
    "先輩のいない屋上は、どこか物静かで寂しい場所だった。"
    太一 "「はー」"
    "大の字に横たわる。"
    call gl(0,"bgcc0000a")
    call vsp(0,1)
    with wipeleft
    "風が俺の上をかすめて行く。"
    "羽のようにさらわれたいと願うが、人間の体は重く、ままならない。"
    "解放など訪れるものではない。"
    "人間は自分の重さを自覚するようにできている。"
    call gl(0,"bgcc0000d")
    call vsp(0,1)
    with Dissolve(500.0/1000.0)
    太一 "「美希、捜さないといけないんだけどな……」"
    "目を閉じると、意識がぼやけていった。"
    pause (1000.0/1000.0)
    pause (1000.0/1000.0)
    "違和感で、目を開く。"
    call gl(0,"evcc0054")
    call vsp(0,1)
    with Dissolve(500.0/1000.0)
    太一 "「…………美希？」"
    play bgm "bgm/bgm016.ogg"
    voice "vfCCC3010mki000"
    美希 "「はい」"
    "にっこりと。"
    voice "vfCCC3010mki001"
    美希 "「美希です」"
    "目尻が赤い。"
    "なにかあったのか？"
    voice "vfCCC3010mki002"
    美希 "「あ、寝ててください」"
    太一 "「……膝枕のままでいいの？」"
    voice "vfCCD4001mki070"
    美希 "「えっちなことしないでいてくれるなら」"
    太一 "「したら？」"
    voice "vfCCC3010mki004"
    美希 "「セクハラの度合いにもよりますが」"
    voice "vfCCD4001mki071"
    美希 "「……絶交」"
    太一 "「そりゃこわい。何もできない」"
    voice "vfCCD4001mki072"
    美希 "「ほんとうに？」"
    太一 "「ああ、かなりこわい、そんなことになったら１００メガショックだ」"
    voice "vfCCD4001mki073"
    美希 "「……じゃー、寝てていいです」"
    voice "vfCCD4001mki074"
    美希 "「びっくりしました、倒れてたから」"
    太一 "「寝てた」"
    voice "vfCCD4001mki075"
    美希 "「またそんなトンデモ日常を……」"
    voice "vfCCD4001mki076"
    美希 "「でも、そういう時の先輩が、一番いいですね」"
    太一 "「……そお？」"
    voice "vfCCD4001mki077"
    美希 "「面白おかしく、毎日がお祭り騒ぎみたいで」"
    call gl(0,"evcc0054a")
    call vsp(0,1)
    with Dissolve(500.0/1000.0)
    "涙。"
    "真上で泣かれると、反応のしようがない。"
    太一 "「美希……？」"
    voice "vfCCD4001mki078"
    美希 "「でも、先輩と遊べば遊ぶほど……ものたりなくて……霧ちんいないし……他のみんなも……親も、クラスメイトも……」"
    voice "vfCCD4001mki079"
    美希 "「……ぐす……日常は、なくなっちゃったんだなって……」"
    太一 "「……俺と遊んでも駄目でしたか。まぁなぁ、仕方ないんだけど……」"
    voice "vfCCD4001mki080"
    美希 "「そういう意味じゃ、ないんですけど……」"
    voice "vfCCD4001mki081"
    美希 "「わたし、自信なくて……」"
    太一 "「何の？」"
    voice "vfCCD4001mki082"
    美希 "「生きていく、自信が」"
    太一 "「馬鹿いうでない。自分を無闇に信じろ」"
    voice "vfCCD4001mki083"
    美希 "「……ぐす……無理っす……」"
    voice "vfCCD4001mki084"
    美希 "「霧ちん、いなくなったんですよね？」"
    太一 "「…………どうして？」"
    voice "vfCCD4001mki085"
    美希 "「なんとなく……」"
    voice "vfCCD4001mki086"
    美希 "「だって、人がいないんですから……そう考えるしか」"
    voice "vfCCD4001mki087"
    美希 "「みんな消えたんです」"
    voice "vfCCD4001mki088"
    美希 "「だから霧も消えた」"
    voice "vfCCD4001mki089"
    美希 "「わたしたちもいつか、消えるんですか？」"
    voice "vfCCD4001mki090"
    美希 "「消えてなくなっちゃうんですか？」"
    太一 "「……かも知れない」"
    voice "vfCCD4001mki091"
    美希 "「……ほら……あははは……先輩だって、認めた……」"
    太一 "「あのなあ美希。誰だって最後は死ぬんだ」"
    太一 "「おまえ様は、いつか終わりがあるからって、今生きてることを放棄すんのか？」"
    voice "vfCCD4001mki092"
    美希 "「……それは……」"
    太一 "「消えるんだっていーじゃん。消えるまで生きれば？」"
    太一 "「楽しいことはいくらだってあるって」"
    voice "vfCCD4001mki093"
    美希 "「……どんな？」"
    太一 "「そーだなぁ」"
    太一 "「……俺と暮らそうか？」"
    voice "vfCCD4001mki094"
    美希 "「先輩と？」"
    voice "vfCCD4001mki095"
    美希 "「告白ってやつですか？」"
    太一 "「欲しいものはなんでも買ってやろう」"
    "俺のハイエンドなギャグをスルーして、美希は目をのぞきこんでくる。"
    voice "vfCCD4001mki096"
    美希 "「えっちなこと、しようとか思ってます？」"
    太一 "「する」"
    voice "vfCCD4001mki097"
    美希 "「……う……」"
    太一 "「するね、俺は、えっちなことを。それが自分の存在意義であると信ずる者の取るべき確固たる態度でするね」"
    太一 "「俺の家の敷居をまたいだ瞬間、おまえは非処女に等しくなる」"
    voice "vfCCD4001mki098"
    美希 "「はやー……」"
    "辟易とした様子。"
    太一 "「なぜなら、おまえは箱の中に入れられた猫めいて、処女と非処女が等しいのだ」"
    "唐突に睡魔。"
    call gl(0,"bgcc0000d")
    call vsp(0,1)
    with Dissolve(500.0/1000.0)
    太一 "「ぐう……」"
    voice "vfCCD4001mki099"
    美希 "「考えておきます」"
    voice "vfCCD4001mki100"
    美希 "「って、寝てる……はや」"
    voice "vfCCD4001mki101"
    美希 "「…………まったく」"
    voice "vfCCD4001mki102"
    美希 "「ほんと、変な人」"
    voice "vfCCD4001mki103"
    美希 "「はは、あははは……」"
    voice "vfCCD4001mki104"
    美希 "「あはははは、っ、はははは……はは……」"
    "……………………。"
    pause (500.0/1000.0)
    pause (1500.0/1000.0)
    call gl(0,"evcc0054")
    call vsp(0,1)
    with Dissolve(500.0/1000.0)
    "起きると、美希が微笑んでいた。"
    太一 "「また寝ちゃった？」"
    voice "vfCCD4001mki105"
    美希 "「はい、こんこんと」"
    太一 "「ごめん、痺れたろう。起きる」"
    voice "vfCCD4001mki106"
    美希 "「その前に」"
    "押さえつけられた。"
    voice "vfCCD4001mki107"
    美希 "「お礼をしてあげます」"
    太一 "「お礼？」"
    voice "vfCCD4001mki108"
    美希 "「励ましてくれたお礼です」"
    太一 "「だったら、そのまったいらボディで……」"
    voice "vfCCD4001mki109"
    美希 "「いえ、礼は耳かきでしたいと思います」"
    太一 "「！？」"
    太一 "「起きゆ！」"
    voice "vfCCD4001mki110"
    美希 "「だめっ」"
    太一 "「それはまずい！」"
    voice "vfCCD4001mki111"
    美希 "「にゃー！」"
    "耳に棒が突っ込まれた。"
    "ざくっ"
    太一 "「！！！！」"
    with vpunch
    "あとはもう、地獄だった。"
    call gl(0,"bgcc0000a")
    call vsp(0,1)
    with wipeleft
    "結局、美希は俺の家には来なかった。"
    stop bgm
    call gl(0,"bgcc0002")
    call vsp(0,1)
    with wipeleft
    太一 "「金曜日、か」"
    "世界が揺り戻されるまで、あと三日。"
    "今日もなすべきことをしよう。"
    太一 "「……いけね、海に行かないと」"
    "昨日仕込み忘れたけど、なんとかなるかな。"
    call gl(0,"bgcc0011")
    call vsp(0,1)
    with wipeleft
    太一 "「海に行こう」"
    call gl(1,"TCYM0004|TCYM0002")
    call gp(1,t=center)#x=180
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki112"
    美希 "「……ぃえ？」"
    play bgm "bgm/bgm005.ogg"
    call gl(0,"bgcc0014")
    call vsp(0,1)
    call vsp(1,0)
    with wipeleft
    "アトミック雑貨で必要なものをかきあつめ、"
    "車を調達し、"
    "海に向かった。"
    call gl(0,"bgcc0017")
    call vsp(0,1)
    with wipeleft
    太一 "「よし、いい海っぷりだ！」"
    "ガッツポーズ。"
    太一 "「そして！」"
    call gl(1,"TCYM0000aa|TCYM000xa")
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki113"
    美希 "「はやい……展開がはやい……」"
    太一 "「さらに飛ばして行くから」"
    call gl(1,"TCYM0003aa|TCYM000xa")
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki114"
    美希 "「うーん、元気だー」"
    太一 "「さ、遊ぶぞ！」"
    call gl(0,"bgcc0000a")
    call vsp(0,1)
    call vsp(1,0)
    call vsp(2,0)
    with Dissolve(500.0/1000.0)
    太一 "「うおー！」"
    voice "vfCCD4001mki115"
    美希 "「せやー！」"
    太一 "「がー！」"
    voice "vfCCD4001mki116"
    美希 "「にぬーっ！」"
    "セパタクローと水泳を足したゲームを楽しんだ。"
    call gl(0,"bgcc0020")
    call vsp(0,1)
    with wipeleft
    "そして昼食。"
    太一 "「ふいー……フィールドが海の中だと疲れるー」"
    call gl(1,"TCYM0000aa|TCYM000xa")
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki117"
    美希 "「遊びっていうより、体力しぼりに来たって感じですね」"
    太一 "「あの遊びは失敗だな」"
    call gl(1,"TCYM0001aa|TCYM000xa")
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki118"
    美希 "「移動が水泳って……狂ってますよ。あれ人魚専用の遊びっす」"
    太一 "「正気じゃいられない十代なんだよ」"
    太一 "「さて、できたかな」"
    call gl(1,"TCYM0000aa|TCYM000xa")
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki119"
    美希 "「できますね」"
    "二人で安っぽいテーブルに顎を乗せて、二つ用意されたそれを凝視した。"
    "カップラーメン。"
    太一 "「ずるずるずる」"
    voice "vfCCD4001mki120"
    美希 "「はふはふはふ」"
    太一 "「海だからラーメンでいいんだろうけど。わびしい」"
    voice "vfCCD4001mki121"
    美希 "「……ですねぇ」"
    太一 "「そっちうまそーだな」"
    call gl(1,"TCYM0001aa|TCYM000xa")
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki122"
    美希 "「カレー味」"
    太一 "「ちょっと交換」"
    call gl(1,"TCYM0003aa|TCYM000xa")
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki123"
    美希 "「いいですよ、はい」"
    太一 "「……あ、うまい。もう一個あったっけ、それ？」"
    call gl(1,"TCYM0000aa|TCYM000xa")
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki124"
    美希 "「適当に突っ込みましたからねぇ、見て下さいよ」"
    "ただいくつかは、衝撃で器が割れてしまっている。"
    太一 "「よく考えたらカップ麺数十個もいらんよな」"
    call gl(1,"TCYM0001aa|TCYM000xa")
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki125"
    美希 "「……それ抱えてたからわたしの命があるってこと忘れるなよ」"
    "途中、事故ったのだ。"
    "すっげー怒られた。泣きながら。"
    太一 "「あ、これうまそう」"
    "一つを取り出す。"
    太一 "「ん……お湯入れる場所がないぞ？」"
    太一 "「なんだこの具。ラーメンじゃないじゃん？」"
    call gl(1,"TCYM0000aa|TCYM000xa")
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki126"
    美希 "「ほよ？」"
    太一 "「なんか高野豆腐……じゃなくてスポンジだぞ……に、ねっとりとした液体がしみこませてあって……」"
    太一 "「って、オナカップじゃねぇか！！」"
    "美希に投げつけた。"
    call gl(1,"TCYM0001aa|TCYM000xa")
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki127"
    美希 "「ぎあっ？」"
    "命中。"
    太一 "「このハレンチ処女！　おばか！」"
    call gl(1,"TCYM0000aa|TCYM000xa")
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki128"
    美希 "「なにすんですかー！」"
    太一 "「自分がラーメンと一緒に突っ込んだものをよく見てみろ！」"
    voice "vfCCD4001mki129"
    美希 "「……んー？　なんです、これ？」"
    太一 "「オナカップだ」"
    call gl(1,"TCYM0001aa|TCYM000xa")
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki130"
    美希 "「おなかっぷ？」"
    太一 "「今のエロセリフは記憶にとどめるとして、要するにＨな道具だ。俺はあまり好きじゃないが、使い捨てで、５００～９００円くらいだ！」"
    call gl(1,"TCYM0000aa|TCYM000xa")
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki131"
    美希 "「……使い方がわからぬ」"
    "眼前で使ってみせてやろうか……この小娘。"
    太一 "「もー、おまえがそんな無防備だからお兄さんは心配です」"
    voice "vfCCD4001mki132"
    美希 "「は、はあ……結構、知識ついたんですけどねぇ、誰かさんのおかげで」"
    call gl(1,"TCYM0003aa|TCYM000xa")
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki133"
    美希 "「この年でおなほーるのメンテナンス方法知ってる女の子は、そうはいませんぜ」"
    太一 "「うぇっほん。今日は暑いな」"
    "暑くないが。"
    call gl(1,"TCYM0000aa|TCYM000xa")
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki134"
    美希 "「……ねえ、それより気づきました？」"
    太一 "「うむ？」"
    voice "vfCCD4001mki135"
    美希 "「魚もクラゲも、なんもいないんですよね、海」"
    太一 "「……ああ、気づいた。貝もいない。貝殻だけだ」"
    call gl(1,"TCYM0003aa|TCYM000xa")
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki136"
    美希 "「サクラガイひろっちったです。きれー。もってかえろ」"
    太一 "「オクトパスギガンテウスもいなかった」"
    call gl(1,"TCYM0000aa|TCYM000xa")
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki137"
    美希 "「……？」"
    太一 "「まあ、そこいらあんま気にしないでおこう。科学的にボロが出る」"
    call gl(1,"TCYM0001aa|TCYM000xa")
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki138"
    美希 "「……いや、突っ込むというか、寂しい世界だなって思って」"
    voice "vfCCD4001mki139"
    美希 "「世界って寂しかったんだーと」"
    太一 "「うーむ」"
    "世界は寂しい、か。"
    "そうなんだよな。"
    call gl(1,"TCYM0003aa|TCYM000xa")
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki140"
    美希 "「さ、遊びますか！」"
    太一 "「よし、次は夜のレスリングだ」"
    call gl(1,"TCYM0000aa|TCYM000xa")
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki141"
    美希 "「……それせっくすって言いませんか……ふつー」"
    call gl(0,"bgcc0014a")
    call vsp(0,1)
    call vsp(1,0)
    with wipeleft
    call gl(1,"TCYM0003b|TCYM0003")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3114mki058"
    美希 "「楽しかったですー！」"
    太一 "「うむ。また行こう」"
    call gl(1,"TCYM0011b|TCYM0011")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3114mki059"
    美希 "「うっす！」"
    "だいぶ元気を取り戻した様子。"
    太一 "「あー、今日撮った写真、現像って時間かかるかな？」"
    call gl(1,"TCYM0021b|TCYM0021")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3114mki060"
    美希 "「はやくほしいですか？」"
    太一 "「うん。できたら明日の夜には」"
    call gl(1,"TCYM0000b|TCYM0000")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3114mki061"
    美希 "「はや……じゃあ、学校で現像しますんで、そこでお渡ししましょ」"
    太一 "「さんきゅ。じゃあね」"
    stop bgm
    call gl(1,"TCYM0002b|TCYM0002")
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki142"
    美希 "「あ……」"
    太一 "「ん？」"
    call gl(1,"TCYM0001b|TCYM0000")
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki143"
    美希 "「ええと、いえ、なんでもありません。また」"
    hide pic1
    with dissolve
    "団地方面に走り去った。"
    call gl(0,"bgcc0003")
    call vsp(0,1)
    with wipeleft
    "土曜日だ。"
    "……あと一日。"
    "あと一日なんだ。"
    play bgm "bgm/bgm024.ogg"
    call gl(0,"bgcc0006")
    call vsp(0,1)
    call vsp(1,0)
    with wipeleft
    call gl(1,"TCYM0000|TCYM0000")
    call gp(1,t=center)
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki144"
    美希 "「おはようございます、はやいですね」"
    太一 "「写真欲しいんだけど」"
    call gl(1,"TCYM0041|TCYM0041")
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki145"
    美希 "「これから現像です。時間かかりますよ」"
    太一 "「いいよ、のんびりで」"
    call gl(1,"TCYM0003|TCYM0003")
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki146"
    美希 "「つきあいません？」"
    太一 "「……あー、ここでぼんやりしてる」"
    call gl(1,"TCYM0002|TCYM0002")
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki147"
    美希 "「そですか」"
    "ちょっとしゅんとした。"
    call gl(1,"TCYM0000|TCYM0000")
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki148"
    美希 "「お昼、一緒しましょう」"
    太一 "「んー」"
    hide pic1
    with dissolve
    "美希が去る。"
    "週末について考える。"
    "否応なく。"
    "健全に、送り返すだけ。"
    "美希との何気ない会話一つ一つを、心に刻む。"
    太一 "「やっぱ、行こう」"
    "写真部の部室に向かった。"
    stop bgm
    call gl(0,"bgcc0000d")
    call vsp(0,1)
    with Dissolve(500.0/1000.0)
    pause (500.0/1000.0)
    pause (500.0/1000.0)
    play bgm "bgm/bgm002.ogg"
    call gl(0,"bgcc0013b")
    call vsp(0,1)
    with wipeleft
    太一 "「あれえ？」"
    call gl(0,"bgcc0013bz")
    call gl(1,"TCYM0000c|TCYM0000")
    call gp(1,t=center)
    call vsp(0,1)
    call vsp(1,1)
    with Dissolve(500.0/1000.0)
    voice "vfCCD4001mki149"
    美希 "「……お邪魔しまーす」"
    "来ちゃった。"
    "大きな手荷物。"
    "石けんの香り。"
    "新しい制服。"
    "これは……。"
    call gl(1,"TCYM0001c|TCYM0000")
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki150"
    美希 "「先輩から変なオーラ出てゆ」"
    太一 "「……ごほん、シッケー」"
    call gl(1,"TCYM0000c|TCYM0000")
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki151"
    美希 "「せっまいホテルですねー、支配人」"
    太一 "「は、広い場所恐怖症のお客様には好評いただいております」"
    call gl(1,"TCYM0001c|TCYM0000")
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki152"
    美希 "「……といっても、うちより広い」"
    太一 "「おいッ！」"
    call gl(0,"bgcc0004c")
    call vsp(0,1)
    with wipeleft
    call gl(1,"TCYM0004c|TCYM0002")
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki153"
    美希 "「はわはわ、すっごい、フローリング」"
    太一 "「この街なら普通だ。みんな金あまってるんだから」"
    call gl(1,"TCYM0000c|TCYM0000")
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki154"
    美希 "「うち、貧乏町時代からある激安団地なんで」"
    太一 "「ああ……あの廃墟ね」"
    call gl(1,"TCYM0003c|TCYM0003")
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki155"
    美希 "「エレベーターついてないから、電気止まってもぜーんぜん平気ー」"
    太一 "「何階なんだ？　美希んち」"
    call gl(1,"TCYM0000c|TCYM0000")
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki156"
    美希 "「……最上階」"
    太一 "「泣いていい。君は泣いていい」"
    call gl(1,"TCYM0002c|TCYM0002")
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki157"
    美希 "「うわーん！　これでもう階段昇らなくてすむですー」"
    太一 "「哀れな……」"
    call gl(1,"TCYM0003c|TCYM0003")
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki158"
    美希 "「じゃ、同情してもらったところでお部屋にご案内」"
    call gl(0,"bgcc0003e")
    call vsp(0,1)
    call vsp(1,0)
    with wipeleft
    太一 "「ここです」"
    call gl(1,"TCYM0004c|TCYM0002")
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki159"
    美希 "「あんたの部屋です！」"
    太一 "「男の家に来るということはだな……」"
    call gl(1,"TCYM0041c|TCYM0041")
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki160"
    美希 "「あー、わかりやした……」"
    太一 "「素直でよろしい」"
    call gl(1,"TCYM0021c|TCYM0021")
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki161"
    美希 "「あの先輩。でも一つ質問よろしいですか？」"
    太一 "「うん？」"
    call gl(1,"TCYM0000c|TCYM0000")
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki162"
    美希 "「隣の部屋って……？」"
    太一 "「あー、あそこは駄目だ」"
    太一 "「見てくる？」"
    voice "vfCCD4001mki163"
    美希 "「はい？」"
    hide pic1
    with dissolve
    "行かせた。"
    call gl(1,"TCYM0004c|TCYM0002")
    call gp(1,t=center)
    call vsp(1,1)
    with dissolve
    "血相変えて戻ってきた。"
    voice "vfCCD4001mki164"
    美希 "「……せせせ先輩の写真とかがバーッと一面に！！」"
    太一 "「恐いだろ？」"
    call gl(1,"TCYM0002c|TCYM0002")
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki165"
    美希 "「きついです」"
    太一 "「まあ触れずにおこう」"
    太一 "「でだ、この部屋の床、ここが君の寝床になる」"
    太一 "「はい寝袋」"
    "筒状にたたまれた寝袋を、美希はジト目で見た。"
    call gl(1,"TCYM0001c|TCYM0000")
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki166"
    美希 "「頼ってきた女の子を袋で寝かせるというのは、どういうもんでございましょうねぇ？」"
    太一 "「うちは客人は床って決まってるんだよ」"
    太一 "「布団で寝たかったらこの俺、黒須太一１００の試練を乗り越えなくてはならない」"
    "要するにセックスだ。"
    call gl(1,"TCYM0000c|TCYM0000")
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki167"
    美希 "「……」"
    "悩み出した。"
    太一 "「おいおい」"
    voice "vfCCD4001mki168"
    美希 "「……」"
    太一 "「美希ー？」"
    voice "vfCCD4001mki169"
    美希 "「……」"
    太一 "「悪戯しちゃうぞー」"
    "俺を見上げて、"
    stop bgm
    voice "vfCCD4001mki170"
    美希 "「どーぞ」"
    call gl(1,"TCYM0001c|TCYM0000")
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki171"
    美希 "「覚悟はできてます」"
    "真剣な口調だったので、面食らった。"
    太一 "「うーん……と改めて言われてもなぁ。冗談なんだし」"
    太一 "「というか、こわくないか？」"
    call gl(1,"TCYM0002c|TCYM0002")
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki172"
    美希 "「こわい、です」"
    太一 "「だろ？」"
    "左右に首を振る美希。"
    voice "vfCCD4001mki173"
    美希 "「誰もいないのが、こわい」"
    play bgm "bgm/bgm021.ogg"
    太一 "「そっちか」"
    call gl(1,"TCYM0001c|TCYM0000")
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki174"
    美希 "「霧はどうしたんです？　どうしていなくなったんです？」"
    太一 "「わからないな」"
    call gl(1,"TCYM0002c|TCYM0002")
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki175"
    美希 "「わたしも消えるんですか？　先輩も？」"
    太一 "「…………」"
    voice "vfCCD4001mki176"
    美希 "「気が、狂いそうです」"
    voice "vfCCD4001mki177"
    美希 "「……だっこして、先輩」"
    voice "vfCCD4001mki178"
    美希 "「消えちゃわないように……」"
    hide pic1
    with dissolve
    "そう言って、身を傾けてきた。"
    "受け止めるしかない。"
    "せめて夜でなければ、我慢はできたかもしれない。"
    "だけど二人を包む雰囲気は、もう拒絶できるものではなくなっていた。"
    太一 "「……だっこ、ねぇ」"
    "背中に軽く手をまわすと、美希はいっそうしがみついてくる。"
    "これもまた。"
    "思い出の一つか―――"
    "そっと美希を横たえて、"
    jump N_MKSCENE001
label MKSCENE001:
    play bgm "bgm/bgm021.ogg"
label N_MKSCENE001:
    "キスをした。"
    voice "vfCCD4001mki179"
    美希 "「ん……んは……っんっ」"
    "小さな唇に驚く。"
    "薄い、繊細な作り。"
    "しっとりと湿っていて、驚くほど柔らかい。"
    "軽くついばむ。"
    "つつくようなキス。"
    "触れては離れて、少しずつ角度を変えて。"
    voice "vfCCD4001mki180"
    美希 "「こそばゆい……ちょっと、あっ……はっ……」"
    "キスの最中にしゃべられるのは負けだ。"
    "つい、舌を入れた。"
    "美希の体が硬直する。"
    "強く抱きしめる。逃げないよう。"
    "吸って、吸って、吸って……。"
    "甘い蜜が、口内に引き込まれるように。"
    "衣服をはだけさせる。"
    "唇を離すと、美希はとまどいと苦笑を顔に同居させていた。"
    "首筋を唇でなぞる。"
    voice "vfCCD4001mki181"
    美希 "「てかげん、てかげん……う～っ」"
    "鎖骨が小さく喘いだ。"
    太一 "「すごく感じやすいんだな」"
    voice "vfCCD4001mki182"
    美希 "「う～～～～～ッッッ」"
    "手の甲で顔を覆う。"
    voice "vfCCD4001mki183"
    美希 "「……なんか……すごい……」"
    太一 "「どうすごいの？」"
    voice "vfCCD4001mki184"
    美希 "「人にさわられるって、すごい、です……きゃふっ」"
    太一 "「そう」"
    "唇が下方におりていく。"
    "往路で区切られた美希の腹筋が、小刻みにわなないた。"
    "かすかに息づく腹部が、感動するほど美しい。"
    "その理由を考えることさえ億劫になる。"
    "美希の下肢にとりついた。"
    call gl(0,"evcc0037")
    call vsp(0,1)
    with ImageDissolve("sys/EFMSK_22_MSK.bmp",time=1)
    "こちらにもキスをする。"
    voice "vfCCD4001mki185"
    美希 "「……あああぁ……ちょ、タンマ……」"
    "変な声を出す。"
    "まだ幼いつくりのそこを、丹念に濡らしていく。"
    "船型の舳先にある突起を吸う。"
    "強く。"
    voice "vfCCD4001mki186"
    美希 "「痛っ……強すぎ……ですっ」"
    "舌でねぶり、ときおり吸いあげる。"
    voice "vfCCD4001mki187"
    美希 "「あー、いたいいたいっ、なんか取れちゃう～っ」"
    太一 "「……」"
    "なんかって何だ。"
    "少し手加減する。"
    voice "vfCCD4001mki188"
    美希 "「きゃう……きゃ……ん……あわぁ……」"
    "この行為には、妙な楽しさがある。"
    "挟んだり、もてあそんだりする。"
    voice "vfCCD4001mki189"
    美希 "「あっ、はっ……はぁ……ん…………うくっ」"
    "膣を味わうと、美希はちょっとだけ息を詰まらせた。"
    太一 "「まだ痛い？」"
    voice "vfCCD4001mki190"
    美希 "「……わかんない……痺れて……ひゃあぁぁんっ」"
    "舌先でかきまわす。"
    太一 "「こういう方がいい？」"
    voice "vfCCD4001mki191"
    美希 "「優しすぎるのだめぇっ！」"
    "どっちだ……。"
    voice "vfCCD4001mki192"
    美希 "「こそばゆくて……パニクリます……」"
    太一 "「ベロ入れちゃお」"
    voice "vfCCD4001mki193"
    美希 "「あっ……入った……」"
    "無防備な声で、俺はほほえましい気分になる。"
    "たんねんに、舌を動かした。"
    voice "vfCCD4001mki194"
    美希 "「あ……あん、あっ、あんっっ……んっ……はっ」"
    voice "vfCCD4001mki195"
    美希 "「ん、んんんっ……ぅんっ、あぅっ……やぁ、なんか……のぼってきた……」"
    "指を使う。"
    "美希の宝石を、軽く押し潰す。"
    voice "vfCCD4001mki196"
    美希 "「んんっ！？　そこ、つままれたらっ……」"
    voice "vfCCD4001mki197"
    美希 "「と、取れる、取れますっ」"
    太一 "「取れません」"
    "舌を限界まで伸ばして、押し込んでみる。"
    voice "vfCCD4001mki198"
    美希 "「んんんーーーーーっ！！」"
    "背中を浮かせて、美希は弓と化した。"
    "口内に増した水気が流れ込んでくる。"
    "……………………。"
    call gl(0,"evcc0038")
    call vsp(0,1)
    with ImageDissolve("sys/EFMSK_22_MSK.bmp",time=1)
    太一 "「じゃ、正常位で入れるな？」"
    voice "vfCCD4001mki199"
    美希 "「……体位の名前とかどうでもいいですから……あんま痛くないように……できたら」"
    太一 "「正常位だから平気だ。なんせ正常だから」"
    voice "vfCCD4001mki200"
    美希 "「だから……正常位……」"
    太一 "「力抜いて」"
    voice "vfCCD4001mki201"
    美希 "「ん……こわぁ……こわー」"
    太一 "「行くぞ」"
    "腰を押し当てていく。"
    voice "vfCCD4001mki202"
    美希 "「ゆっくり、ゆっくりです！　ゆっくりプリーズ！」"
    太一 "「はいはい、ゆーっくりね」"
    voice "vfCCD4001mki203"
    美希 "「うううううう……」"
    太一 "「ゆーっくり」"
    voice "vfCCD4001mki204"
    美希 "「ううう……うわ……あうっ！」"
    "抜けた。"
    voice "vfCCD4001mki205"
    美希 "「……いったぁ……」"
    太一 "「痛いか、やっぱ」"
    voice "vfCCD4001mki206"
    美希 "「くぅ……」"
    "目尻に涙が浮いている。"
    太一 "「でもこれからだぞ、本番は」"
    "『ふえー』と美希の涙が大粒に膨らむ。"
    voice "vfCCD4001mki207"
    美希 "「も、もうイキました」"
    太一 "「嘘つくな！」"
    太一 "「でも……つらかったらやめとこうか？」"
    voice "vfCCD4001mki208"
    美希 "「あ……それも、いや……」"
    太一 "「どないやねん……」"
    voice "vfCCD4001mki209"
    美希 "「このまま、ぎゅっとしてくれるのが一番いいです」"
    太一 "「男と女のすれちがいだな」"
    "ま、いいか。"
    "抱きしめる。"
    voice "vfCCD4001mki210"
    美希 "「……っ」"
    "子供のタオルだな。俺は。"
    "しがみつくためのなにか。"
    voice "vfCCD4001mki211"
    美希 "「……また、みんな……出てこないかなぁ……」"
    太一 "「いっそ、作るか」"
    voice "vfCCD4001mki212"
    美希 "「ええ……つくるって……まさか？」"
    太一 "「動きます」"
    "スライド人生。"
    voice "vfCCD4001mki213"
    美希 "「あっ……んんんっ……うわ、ひきつれてっ……」"
    "舌では届かなかった奥まで、触れてしまう。"
    voice "vfCCD4001mki214"
    美希 "「あっ、あっ……うー、うぅぅぅ……」"
    "小さな巾着に押し込む感覚……はおそらく正しい。"
    "破れないかな？という不安がある。"
    "ゆっくりと動く。"
    "限界まで抜いてまた沈める時、美希は目をぎゅっと閉じて耐えている。"
    voice "vfCCD4001mki215"
    美希 "「んっ、あっ……んんっ……んくっ……うわー、はれつ、しそう……」"
    "俺に抱きついて、荒い息。"
    voice "vfCCD4001mki216"
    美希 "「きついっ……」"
    "きっと血も出てる。"
    "それは見たくない。"
    "振り払うよう、口づける。"
    voice "vfCCD4001mki217"
    美希 "「あ……」"
    太一 "「ごめん……俺も、破裂しそう」"
    "腰の奥に、爆弾が埋め込まれている気分だ。"
    "打ち込みたい。"
    "吐き出してしまいたい。"
    "腰をぐいと押しつけると、先端が壁を叩いた。"
    voice "vfCCD4001mki218"
    美希 "「はぁんっ……それ……そこ……」"
    "浅い。狭い。"
    "それに。"
    太一 "「……きつい」"
    "がんじがらめにされている。"
    "その中を、尽きることのない潤滑油で、往復する。"
    voice "vfCCD4001mki219"
    美希 "「うひっ、ひゃんっ、あ、あ、んっ、はぁぁぁ……」"
    "ときおりひきつるようなストロークを挟み、加速していく。"
    voice "vfCCD4001mki220"
    美希 "「先輩、も、もう……」"
    太一 "「まだまだ」"
    voice "vfCCD4001mki221"
    美希 "「そんなぁ、うう、うっ、あぉん、んっ、んっ、あんっ」"
    "ねっとりとしたぬめりが、膣道を覆っていく。"
    "突き入れるごとの水音が粘度を増していった。"
    太一 "「美希の中、よくなってきた」"
    voice "vfCCD4001mki222"
    美希 "「そんなの、わかん、ないっ……んんんっ」"
    "美希の全身から力が抜ける。"
    voice "vfCCD4001mki223"
    美希 "「はぁ、はぁ、はぁ―――あああっ、あっ……んっ、うー、も、だめぇ……」"
    太一 "「すぐくてんとなっちゃうな……」"
    voice "vfCCD4001mki224"
    美希 "「だって、こんな、激しいなんて……」"
    太一 "「こんな感じのがいいのかな？」"
    "細かく。"
    voice "vfCCD4001mki225"
    美希 "「あっあっあっあっあっあっあっ！」"
    "声が跳ねる。体も。"
    "活気を取り戻したように。"
    太一 "「ここらへんかな」"
    "膣がよれる角度で動く。"
    voice "vfCCD4001mki226"
    美希 "「うひーっ、あっ、ああっ、んっ、んっ、ん～～～～～っっ」"
    voice "vfCCD4001mki227"
    美希 "「ぬるぬる入って……きゃんっ……きてますっ」"
    太一 "「入ってるだけ？」"
    "耳を噛みながら囁く。"
    太一 "「出たり入ったりしてるでしょ？」"
    voice "vfCCD4001mki228"
    美希 "「出たり、入ったり……ううっ、んっ……はんっ……奥、奥ぅ～～～～～っ、あ～～～っ」"
    "美希の奥は驚くほど近い。"
    太一 "「こんな風にとか」"
    voice "vfCCD4001mki229"
    美希 "「きゃっ、あんっ、だめ、かべ、だめぇっ」"
    太一 "「こんな風にとか」"
    voice "vfCCD4001mki230"
    美希 "「きゃああ、あっ、壁こするの駄目っ」"
    太一 "「痛い？」"
    voice "vfCCD4001mki231"
    美希 "「痛いというか……危ない……」"
    "不思議な言い方をする。"
    太一 "「危ないことは好きだ」"
    "全身を使って美希を組み敷いていく。"
    voice "vfCCD4001mki232"
    美希 "「ふぁっ、んっ、あ、だめですっ、先輩だめ、だめだってばぁ！　……んぎっ……んんんんんんっ！！」"
    太一 "「ごめん……」"
    "行為の熱が、頭を熱くしてる。"
    "止まらない。"
    voice "vfCCD4001mki233"
    美希 "「ふぁっ、うっ……あああっ、はんっ、ん、あ、ぁくン……」"
    "腰が、淫靡に円を描く。"
    "壁が密着し吸着してくる。"
    "引き抜けばまとわって、尾てい骨から脊髄にかけて痺れが走った。"
    voice "vfCCD4001mki234"
    美希 "「うううっ、あンっ、あっ、あっ……あああっ……あうっ」"
    voice "vfCCD4001mki235"
    美希 "「あ……なんか来そう、です……」"
    太一 "「才能が、あるなっ」"
    voice "vfCCD4001mki236"
    美希 "「んんっ！　なんの……才能ですか……はんっ」"
    太一 "「気持ち、よくなる、才能」"
    voice "vfCCD4001mki237"
    美希 "「っ……もう……ばか……っ！」"
    "抱きついてきた。"
    "抱き返す。"
    "なれるだけ、一つになっておく。"
    "不意に、美希と作れる思い出もこれが最後なんだと思い出す。"
    "射精感が直前まで来ていたことにも気づく。"
    "興奮で感覚が鈍くなっていた。"
    太一 "「っ！」"
    "美希の内部を、幾度も切り刻む。"
    "そんな攻撃的な律動、リズム。"
    call gl(0,"evcc0038a")
    call vsp(0,1)
    with Dissolve(500.0/1000.0)
    voice "vfCCD4001mki238"
    美希 "「あっ……あっあっあっあっ、だめ、だめっ、危ないっ、ん、ん……んんんんんんん～～～～～っっっ！」"
    "悲鳴ともあえぎともつかない。"
    "余波だけで細かな語を刻ませる、愉悦のかたまり。"
    太一 "「ん……」"
    "それを、叩きつけた。"
    "一番奥に。"
    "抱き合ったまま、離れることもできず。"
    "互いの細胞の合一を、試みるかのごとく。"
    "吐き出し続ける。"
    "腰が抜けそうなほど。"
    "そして崩れる。"
    "二人、重なる。"
    "無造作にキスをして。"
    "小さな美希を、胸元にかき抱いた。"
    voice "vfCCD4001mki239"
    美希 "「赤ちゃん……できた……です……」"
    太一 "「……ほんとか、それ」"
    voice "vfCCD4001mki240"
    美希 "「カン……です……」"
    太一 "「はは……」"
    "冗談とも本気とも取れない。"
    "『あの』美希に近い感覚が、懐かしい。"
    太一 "「美希はかわいいな」"
    "人形みたいに、胸におさまってしまう。"
    "行為の放熱を間近で感じる。"
    "漂う、甘い体臭。"
    太一 "「……美希？」"
    美希 "「……………………」"
    "眠っていた。"
    太一 "「ははは」"
    "のんきなもんだ。"
    if not _in_replay:
        jump N_MKSCENE101
    return
label N_MKSCENE101:
    call gl(0,"bgcc0003e")
    call vsp(0,1)
    with ImageDissolve("sys/EFMSK_22_MSK.bmp",time=1)
    "美希の体を拭いて、"
    "窓を全開にして、"
    "抱いて、"
    "寝た。"
    太一 "「……はは」"
    "俺は知った。"
    "小さくてあたたかい。"
    "美希はそういうものだった。"
    stop bgm
    call gl(0,"bgcc0000d")
    call vsp(0,1)
    with Dissolve(500.0/1000.0)
    pause (1000.0/1000.0)
    pause (1000.0/1000.0)
    play bgm "bgm/bgm004.ogg"
    call gl(0,"bgcc0004")
    call vsp(0,1)
    with Dissolve(500.0/1000.0)
    call gl(1,"TCYM0021|TCYM0021")
    call gp(1,t=center)
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki241"
    美希 "「はい？　ピクニック？」"
    太一 "「そー」"
    "日曜日。"
    "朝食を食べながら、持ちかける。"
    call gl(1,"TCYM0000|TCYM0000")
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki242"
    美希 "「日曜日ですしね」"
    太一 "「用意はしてある」"
    call gl(1,"TCYM0004|TCYM0002")
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki243"
    美希 "「ほんとだ。はやぁ……」"
    "バスケットをまじまじと見つめて、"
    call gl(1,"TCYM0003|TCYM0003")
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki244"
    美希 "「んー、それって、えっちピクニックですよね？」"
    "などと笑う。"
    太一 "「ばれたか」"
    call gl(1,"TCYM0041|TCYM0041")
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki245"
    美希 "「うわ、最低だこの人」"
    太一 "「いいじゃないか。他にすることもないし」"
    call gl(1,"TCYM0021|TCYM0021")
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki246"
    美希 "「この人、ロマンスさえあったらなあとよく思います」"
    太一 "「ロマンスだけじゃ生きていけない」"
    call gl(1,"TCYM0041|TCYM0041")
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki247"
    美希 "「……露骨な」"
    太一 "「というわけで行こう。グッズとかコスチュームとかは俺が持って行くから」"
    call gl(1,"TCYM0004|TCYM0002")
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki248"
    美希 "「な、なにされるんだ、わたしは……」"
    voice "vfCCD4001mki249"
    美希 "「しかも山で」"
    太一 "「さあ」"
    call gl(1,"TCYM0041|TCYM0041")
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki250"
    美希 "「うー、まだアソコ痛いのにー……」"
    call gl(0,"bgcc0015")
    call vsp(0,1)
    call vsp(1,0)
    with wipeleft
    call gl(1,"TCYM0000|TCYM0000")
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki251"
    美希 "「で、あっしは何されるんですかー？」"
    太一 "「行けばわかるけど……未体験ゾーンと言っておこうか」"
    call gl(1,"TCYM0002|TCYM0002")
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki252"
    美希 "「はえー（涙）」"
    "サイケデリックな俺の行動に慣れているせいか、美希は不審がらずについてきてくれた。"
    太一 "「美希はご両親いるんだっけ？」"
    call gl(1,"TCYM0000|TCYM0000")
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki253"
    美希 "「いるんですよ」"
    voice "vfCCD4001mki254"
    美希 "「貧乏なご両親です」"
    voice "vfCCD4001mki255"
    美希 "「つうか、いました」"
    "過去形。"
    太一 "「あ、悪い」"
    call gl(1,"TCYM0003|TCYM0003")
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki256"
    美希 "「あは、みんないないんだから一緒です」"
    太一 "「貧乏人かぁ」"
    call gl(1,"TCYM0000|TCYM0000")
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki257"
    美希 "「おこづかいとか安いですよ」"
    太一 "「いくらよ？」"
    voice "vfCCD4001mki258"
    美希 "「３０００円」"
    "うわぁ……。"
    "格安だな。"
    太一 "「なんも買えねぇ」"
    call gl(1,"TCYM0001|TCYM0000")
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki259"
    美希 "「ためが大事です」"
    voice "vfCCD4001mki260"
    美希 "「あとお年玉」"
    call gl(1,"TCYM0021|TCYM0021")
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki261"
    美希 "「群青行くって宣告された時は、なんか金一封みたいのいっぱいもらいましたよ」"
    call gl(1,"TCYM0001|TCYM0000")
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki262"
    美希 "「あれって、どーいう意味なんでしょうねー！」"
    太一 "「……さあ」"
    "知らぬが仏。"
    太一 "「ま、どっちにしろ、またもやタメは大事になるだろうさ」"
    call gl(1,"TCYM0000|TCYM0000")
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki263"
    美希 "「……？」"
    太一 "「ついた」"
    call gl(0,"bgcc0016")
    call vsp(0,1)
    call vsp(1,0)
    with wipeleft
    call gl(1,"TCYM0000|TCYM0000")
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki264"
    美希 "「……ほこら」"
    太一 "「こっちな」"
    call gl(1,"TCYM0002|TCYM0002")
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki265"
    美希 "「こんなところでするんですかぁ……拒否権はないんでしょうかぁ？」"
    太一 "「ない」"
    voice "vfCCD4001mki266"
    美希 "「あーん」"
    太一 "「ラジオを持ちたまえ」"
    call gl(1,"TCYM0021|TCYM0021")
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki267"
    美希 "「……どういうプレイ？」"
    太一 "「なに、向こうに切り替わったら状況がすぐわかるようにな」"
    voice "vfCCD4001mki268"
    美希 "「？？？」"
    太一 "「ここを歩く、まっすぐゆっくり」"
    voice "vfCCD4001mki269"
    美希 "「？？？？？？」"
    太一 "「ほらほら」"
    call gl(1,"TCYM0000|TCYM0000")
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki270"
    美希 "「なんか、意味が……」"
    太一 "「歩く歩く」"
    voice "vfCCD4001mki271"
    美希 "「は、はぁ……」"
    "いいぞ。"
    太一 "「ストップ。動かないように」"
    太一 "「そうだな、ポーズを取りなさい」"
    voice "vfCCD4001mki272"
    美希 "「どんな」"
    太一 "「マイポーズ」"
    call gl(1,"TCYM0021|TCYM0021")
    call vsp(1,1)
    with dissolve
    voice "vfCCD4001mki273"
    美希 "「……ない、そんなものはない……どうしよう」"
    太一 "「適当でいいんだよ」"
    stop bgm
    call gl(0,"evcc0058")
    call vsp(0,1)
    call vsp(1,0)
    with Dissolve(500.0/1000.0)
    voice "vfCCD4001mki274"
    美希 "「……こんな感じで？」"
    play bgm "bgm/bgm023.ogg"
    太一 "「……………………」"
    voice "vfCCD4001mki275"
    美希 "「……あのぅ？」"
    太一 "「うむ、目に焼きつけた」"
    voice "vfCCD4001mki276"
    美希 "「何がはじまるのだ……」"
    太一 "「美希、俺は予言しよう」"
    太一 "「おまえは近い将来、タフガイになる」"
    voice "vfCCD4001mki277"
    美希 "「性転換するという意味でございますか」"
    太一 "「いい女になる」"
    voice "vfCCD4001mki278"
    美希 "「わー」"
    太一 "「経験を積めば、なかなかのものになれるおまえに、俺から言葉を贈ろう」"
    太一 "「Ｘという文字は、交差しあってできている！」"
    voice "vfCCD4001mki279"
    美希 "「……ん？」"
    太一 "「あれ、意味わかんないか？　俺はけっこう感動的なことを言ったぞ」"
    voice "vfCCD4001mki280"
    美希 "「……交差しあってるって、すれ違いってことじゃないですか」"
    太一 "「うわ、そーいうこと言うなよ！　物事はとらえかた次第だっての！」"
    voice "vfCCD4001mki281"
    美希 "「あはは」"
    voice "vfCCD4001mki282"
    美希 "「先輩はあいかわらず奥が深くて、美希にはよく理解できないです」"
    太一 "「うーむ」"
    voice "vfCCD4001mki283"
    美希 "「先輩の第一印象は変な人で、今の印象も変な人ですよ」"
    太一 "「出世してないな、俺」"
    voice "vfCCD4001mki284"
    美希 "「そんなのとつがいになった美希です、よしなに」"
    太一 "「うむ。よい子を生めよ」"
    太一 "「ああ、おまえにめくるめく性の極みを教えてやれなくて残念だ」"
    "マジで残念だ。"
    "なんつうか、ちょー残念だ。"
    "無念だ。"
    voice "vfCCD4001mki285"
    美希 "「あのう、さっきから何を？」"
    太一 "「じゃあな」"
    "手を振る。"
    voice "vfCCD4001mki286"
    美希 "「あの……」"
    太一 "「ほら、手をあげて」"
    voice "vfCCD4001mki287"
    美希 "「はい……でも」"
    太一 "「笑顔」"
    voice "vfCCD4001mki288"
    美希 "「なんか……」"
    voice "vfCCD4001mki289"
    美希 "「お別れみたいじゃないですか」"
    太一 "「そう？」"
    voice "vfCCD4001mki290"
    美希 "「おかしい、ですよ……先輩……」"
    太一 "「俺はたぶんね、美希みたいな娘か妹が欲しかったんだと思うんだ」"
    "美希の目が、開いた。"
    "その瞬間。"
    call gl(0,"evcc0058a")
    call vsp(0,1)
    with Dissolve(500.0/1000.0)
    "緋が暮れた。"
    太一 "「すげー楽しかった。じゃあな」"
    voice "vfCCD4001mki291"
    美希 "「先輩、やだ！」"
    stop bgm
    call gl(0,"bgcc0000d")
    call vsp(0,1)
    with Dissolve(500.0/1000.0)
    "カシャ―――"
    "踏み出すよりはやく。"
    "送り返した。"
    pause (2000.0/1000.0)
    pause (2000.0/1000.0)
    call gl(0,"bgcc0000b")
    call vsp(0,1)
    with Dissolve(500.0/1000.0)
    voice "vfCCD4001mki292"
    美希 "「……あ……え？」"
    voice "vfCCD4001mki293"
    美希 "「先輩ってば！」"
    voice "vfCCD4001mki294"
    美希 "「……あれ？」"
    voice "vfCCD4001mki295"
    美希 "「あれれ？」"
    voice "vfCCD4001mki296"
    美希 "「いねー！　一瞬で！」"
    voice "vfCCD4001mki297"
    美希 "「太一先輩、どちらにー！？」"
    play se "SE099"
    voice "vfCCD4001mki298"
    美希 "「あら、ラジオ鳴ってる？」"
    voice "vfCCD4001mki299"
    美希 "「…………え、どういうこと……」"
    voice "vfCCD4001mki300"
    美希 "「ラジオが鳴ってるってことは、電波が届いてるってことで……電波が出てるってことは……」"
    voice "vfCCD4001mki301"
    美希 "「あ……」"
    call gl(0,"bgcc0001b")
    call vsp(0,1)
    with wipeleft
    voice "vfCCD4001mki302"
    美希 "「街の灯」"
    stop se
    play bgm "bgm/bgm001.ogg"
    voice "vfCCD4001mki303"
    美希 "「人が、いるんだ……」"
    voice "vfCCD4001mki304"
    美希 "「うわわっ、一大事！」"
    voice "vfCCD4001mki305"
    美希 "「先輩ってば、なんか人がラジオで街なんですってば！」"
    voice "vfCCD4001mki306"
    美希 "「いない……どこに……」"
    voice "vfCCD4001mki307"
    美希 "「先に行ってますからねー！！」"
    call gl(0,"bgcc0000d")
    call vsp(0,1)
    with Dissolve(500.0/1000.0)
    pause (2000.0/1000.0)
    pause (1000.0/1000.0)
    call gl(0,"bgcc0016")
    call vsp(0,1)
    with Dissolve(500.0/1000.0)
    "一人になった。"
    "また世界から、一人分の意識が消えたわけだ。"
    "にしても。"
    太一 "「……察した、か」"
    "最後の瞬間。"
    "彼女の『やだ』という言葉は、何を意味していたのか。"
    "具体的に何が起こるかわからなかったはずなのに。"
    "伝わるものなのかな……こういうのは。"
    太一 "「本当に妊娠してないといいけど、な」"
    太一 "「いや、してた方が興奮するかな」"
    太一 "「……どっちだろう」"
    call gl(0,"bgcc0000d")
    call vsp(0,1)
    with Dissolve(500.0/1000.0)
    "そんなことを、考えていた―――"
    stop bgm
    pause (1500.0/1000.0)
    return