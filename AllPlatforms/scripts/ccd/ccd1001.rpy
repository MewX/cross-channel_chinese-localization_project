label ccd1001:
    if not _in_replay:
        jump N_YOUKOSTART001
    if CIA == 101:
        jump MISATOSCENE001
    if CIA == 102:
        jump MISATOSCENE002
label N_YOUKOSTART001:
    call gl(0,"bgcc0000d")
    call vsp(0,1)
    call vsp(1,0)
    with Dissolve(500.0/1000.0)
    pause (500.0/1000.0)
    "扉を押し開ける。"
    "抵抗があった。"
    "向こう側から押さえられている？"
    play se "se044"
    "強く押す。"
    "扉の向こうで、小さな乱気流が霧散した。"
    "風だったのだ。"
    call gl(1,"efcc0000")
    call gl(0,"bgcc0007")
    call gp(1,t=left)
    call vsp(1,1)
    with dissolve
    call vsp(0,1)
    with dissolve
    hide pic1
    with dissolve
    play se "se009"
    play bgm "bgm/bgm015.ogg"
    "アンテナ。"
    play se "se010"
    "それなりに形になっている。"
    "指向性や波長など、いろいろな調整が必要だ。"
    "が、そういう知識は俺にはない。"
    "先輩も詳しくはなかったが、勉強したらしい。"
    "その先輩だが……いない。"
    "工具。"
    "脚立。"
    "書物。"
    "風で飛び散った、菓子パンの空袋。"
    "作業をしていた痕跡だけが残されている。"
    "２４時間作業しているわけでもないのか。"
    "アンテナを見あげた。"
    "周囲が開けていて、背の高い建物。"
    "電波を飛ばすには、うってつけの環境らしい。"
    "コミュニティＦＭという、地域密着型のラジオ放送がある。"
    "本来、学校の部活でやるほど敷居の低いものでもない。"
    "が。"
    "立地と、群青学院のなりたちと、地元有志の善意溢れる意向。"
    "そういったものが、今回の話に結びついた。"
    "準備が進められていたが、とあるやむを得ない事件によって、うやむやになっていた。"
    "搬入されたアンテナは、一年、そのまま放置されることになった。"
    "そんな事情があるのだった。"
    "おそらくＦＭ群青に求められていたものは、健気に生きる少年少女たちの希望に満ちた愛コンテンツ、だったのだろうけど。"
    "ごめん、そんなものは群青にはありません。"
    "結果オーライだと言える。"
    "見里先輩は、ＳＯＳ計画を立てた。"
    "日曜の夜に彼女はそう言った。"
    "人類が消失してしまったことを、手分けして確認してからだ。"
    "高所にアンテナがあるのだから、完成させて発信してみようという試みは……いかにも現実味に乏しい。"
    "正直、先輩はほつれてしまった、と思った。"
    "逃避は次第に人を弱くする。"
    "そして先輩はもともと十分に弱かった。"
    voice "vfCCC0022msa000"
    見里 "「ぺけくん？」"
    "背後。"
    "向き直る。"
    太一 "「はろーです。先輩」"
    call gl(1,"TCMM0021|TCMM0021")
    call gp(1,t=center)#x=225
    call vsp(1,1)
    with dissolve
    voice "vfCCC0022msa001"
    見里 "「はろーです……えーと、どうしました？」"
    太一 "「様子を見に来ました」"
    "先輩はふんにゃりと微笑む。"
    call gl(1,"TCMM0002|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC0022msa002"
    見里 "「そうでしたか」"
    太一 "「しばらく来てなかったんですけど、だいぶできてますね」"
    call gl(1,"TCMM0000|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC0022msa003"
    見里 "「けっこう前からコツコツとやってますから」"
    "そう。"
    "放送部が自然崩壊してからこっち。"
    "先輩は一人ですべてをこなしていた。"
    "昼休みのＤＪ。"
    "各種放送。"
    "すべて。"
    "誰も手伝わなくなった。"
    "霧は俺を敵視するようになり、"
    "友貴は姉を避けるようになり、"
    "美希はおろおろと苦笑い、"
    "冬子も俺を無視しはじめ、"
    "見事、瓦解。"
    "桜庭だけがいつもと変わりなかった。"
    "変わりなく、放浪していた。"
    "俺はそれでも先輩の周囲をうろちょろしていたけど。"
    "彼女の方が、手伝いを拒んだ。"
    太一 "「……そうでしたね」"
    call gl(1,"TCMM0005|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC0022msa004"
    見里 "「びっくりしましたねぇ、それにしても」"
    太一 "「ですなー」"
    call gl(1,"TCMM0000|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC0022msa005"
    見里 "「人が一斉にいなくなるなんて」"
    太一 "「静かですよね」"
    call gl(1,"TCMM0003|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC0022msa006"
    見里 "「すごくすごく静かです」"
    太一 "「どこ行ってたんです？」"
    call gl(1,"TCMM0000|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC0022msa007"
    見里 "「ちょっと……おなかがすいたので」"
    太一 "「昼ですしね。うまく食料見つけられました？」"
    voice "vfCCC0022msa008"
    見里 "「ああ、家に戻ってました。食べ物は特に不自由してないですし」"
    太一 "「あー、さぼりだ。部長がさぼりー」"
    call gl(1,"TCMM0005|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC0022msa009"
    見里 "「ち、違いますよっ、これはさぼりではありませんっ」"
    "焦る。"
    "規則重視の人なのだ。"
    太一 "「停学、停学です」"
    voice "vfCCC0022msa010"
    見里 "「停学はいやー、履歴に傷がー」"
    太一 "「停学！　停学！」"
    voice "vfCCC0022msa011"
    見里 "「停学はだめですー」"
    "二人ではしゃいでいた。"
    call gl(0,"bgcc0000d")
    call vsp(0,1)
    call vsp(1,0)
    with Dissolve(500.0/1000.0)
    "これが今の俺たちの、最短距離だった。"
    pause (500.0/1000.0)
    pause (1000.0/1000.0)
    stop se
    stop bgm
    call gl(0,"bgcc0011")
    call vsp(0,1)
    with wipeleft
    "先輩と触れることで、どういう展開になるのか。"
    "俺は熟知している。"
    "自身の経験、そして記録。"
    "慎重に進める必要がある。"
    "先輩に近づいて。"
    "先輩に少し触れて。"
    "そして―――"
    call gl(0,"evcc0005b")
    call vsp(0,1)
    with wipeleft
    play bgm "bgm/bgm015.ogg"
    "先輩は寝ている。"
    "わかっていたことだ。"
    voice "vfcca0010msa000"
    見里 "「……」"
    "規則的な軽い寝息。"
    "しばらく見つめていた。"
    "やがて瞳が薄く開く。"
    voice "vfcca0010msa001"
    見里 "「あ……あれぁ……？」"
    太一 "「おはようございます」"
    voice "vfcca0010msa002"
    見里 "「……黒須……君？」"
    太一 "「ぺけです」"
    voice "vfcca0010msa003"
    見里 "「ぺけくん……」"
    "先輩専用のニックネームを、彼女が復唱する。"
    voice "vfCCD1001msa000"
    見里 "「いつからいたんですかぁ……恥ずかしい」"
    "顔を覆う。"
    太一 "「今来たばかりです」"
    太一 "「それより、こんなところで寝たら危ないですよ」"
    call gl(0,"evcc0005b")
    call vsp(0,1)
    with Dissolve(500.0/1000.0)
    voice "vfCCD1001msa001"
    見里 "「ああ、はい、平気です、ぐう」"
    call gl(0,"bgcc0007")
    call vsp(0,1)
    with Dissolve(500.0/1000.0)
    "引き起こす。"
    太一 "「寝たらだめです」"
    "ずれたメガネも直す。"
    call gl(1,"TCMM0000|TCMM000x")
    call gp(1,t=center)#x=225
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa002"
    見里 "「はふ」"
    太一 "「これで、いつもの先輩」"
    "外見だけは。"
    太一 "「おきましたか？」"
    call gl(1,"TCMM0011|TCMM0011")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa003"
    見里 "「うぅん……眠いぃ……」"
    太一 "「いいですけど、パンツ見えてますよ？」"
    call gl(1,"TCMM0004|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa004"
    見里 "「……っ……っ！！」"
    "目覚めた。"
    "さすが淑女。"
    太一 "「おはようございます」"
    call gl(1,"TCMM0003|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa005"
    見里 "「お、はようございます……あー、頭いたーい……」"
    太一 "「陽に当たって寝たりするからです。死にますよ」"
    call gl(1,"TCMM0000|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa006"
    見里 "「いいえ、私は生きます」"
    太一 "「決意は立派です」"
    太一 "「ただ危ないので監視させてもらいます、今後は」"
    call gl(1,"TCMM0005|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa007"
    見里 "「……へー？」"
    太一 "「つまりこの黒須太一があなたの逃避じゃなくて部活に参加するということです」"
    call gl(1,"TCMM0002|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfcca0011amsa009"
    見里 "「部活しゅーりょーっ！」"
    太一 "「部活開始ーっ！」"
    call gl(1,"TCMM0005|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa008"
    見里 "「終わったばかりなのに……」"
    太一 "「なんて、たまに遊びに来るだけですけど」"
    call gl(1,"TCMM0000|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa009"
    見里 "「なぁんだ」"
    太一 "「ではまた明日」"
    call gl(1,"TCMM0002|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa010"
    見里 "「はい、また明日」"
    call gl(0,"bgcc0011a")
    call vsp(0,1)
    call vsp(1,0)
    with wipeleft
    "校舎を出て、屋上を見上げた。"
    "アンテナが立っていた。"
    "その隣。"
    "先輩はまだ、そこにいる。"
    "作業していた。"
    "もうじき夜になるのに。"
    "一人で。"
    play se "SE001"
    call gl(0,"bgcc0011s")
    call vsp(0,1)
    with Pixellate(300.0*2/1000.0,5)
    "人と触れあわないことが、唯一の道と信じていたあの頃―――"
    "先輩と出会った。"
    call gl(1,"TCMM0002s|TCMM000x")
    call gp(1,t=center)#x=225
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa011"
    見里 "「こんにちは！」"
    太一 "「……？」"
    call gl(1,"TCMM0021s|TCMM0021")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa012"
    見里 "「いつもお一人なんですね」"
    call gl(1,"TCMM0000s|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa013"
    見里 "「わたし、宮澄見里っていいます」"
    call gl(1,"TCMM0002s|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa014"
    見里 "「一緒に、部活しませんか？」"
    "この言葉が、忘れられない。"
    "最初の他人。"
    "最初の誰か。"
    stop bgm
    call gl(0,"bgcc0000d")
    call vsp(0,1)
    call vsp(1,0)
    with Dissolve(500.0/1000.0)
    stop se
    pause (500.0/1000.0)
    pause (1000.0/1000.0)
    play bgm "bgm/bgm018.ogg"
    call gl(0,"bgcc0003")
    call vsp(0,1)
    with ImageDissolve("sys/EFMSK_22_MSK.bmp",time=1)
    "目を覚ます。"
    "陽光が窓を貫いていた。"
    "熟睡していたらしい。夢一つ見なかった。"
    "時間は……７時。"
    "学校に行かねば。"
    call gl(0,"bgcc0005")
    call vsp(0,1)
    with wipeleft
    "以前、ここをあの子と歩いた。"
    play se "se001"
    call gl(0,"bgcc0005s")
    call vsp(0,1)
    call gl(1,"TCDY0000s|tcdy000x")
    call gp(1,t=center)#x=240
    call vsp(1,1)
    with Pixellate(300.0*2/1000.0,5)
    voice "vfcca0013ysa000"
    遊紗 "「はれ？　太一さん？」"
    太一 "「おはよう」"
    call gl(1,"TCDY0001s|tcdy000x")
    call vsp(1,1)
    with dissolve
    voice "vfcca0013ysa001"
    遊紗 "「あ、おはようですっ」"
    "遊紗ちゃん―――"
    "この頃は、友達だった。"
    stop se
    call gl(0,"bgcc0007")
    call vsp(0,1)
    call vsp(1,0)
    with Pixellate(300.0*2/1000.0,5)
    pause (500.0/1000.0)
    pause (500.0/1000.0)
    call gl(0,"evcc0005b")
    call vsp(0,1)
    with wipeleft
    "寝ていた。"
    "目覚ましを取り上げる。"
    "１２時にセットされてる。"
    "夜中までやってたのかな。"
    "眠くなるまで、動いていたのかな。"
    "そんなに、つらいのかな。"
    "目覚ましの時間設定を変える。"
    play se "SE054"
    call gl(0,"bgcc0007")
    call vsp(0,1)
    with Dissolve(500.0/1000.0)
    voice "vfCCD1001msa015"
    見里 "「んあんあっ」"
    "飛び起きた。"
    太一 "「朝から寝てるったぁどういう了見っすか」"
    call gl(1,"TCMM0011|TCMM0011")
    call gp(1,t=center)#x=225
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa016"
    見里 "「寝てませんよ？」"
    太一 "「寝てます」"
    voice "vfCCD1001msa017"
    見里 "「ぐう」"
    太一 "「だから寝てますって」"
    call gl(1,"TCMM0003|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa018"
    見里 "「あぁぁ……うぅぅ」"
    "よたよたと身をもたげた。"
    call gl(1,"TCMM0011|TCMM0011")
    call vsp(1,1)
    with dissolve
    voice "vfcca0015msa002"
    見里 "「とりあえず、おはようございます」"
    太一 "「おはようございます、先輩」"
    太一 "「日中にここで寝こけると陽光で死にますよ？」"
    call gl(1,"TCMM0002|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfcca0015msa003"
    見里 "「あ、はい、そうですね、気をつけました」"
    "スカートの裾を持ち上げて眼鏡をふく先輩。"
    "目を反らす。"
    "紳士、紳士。"
    call gl(1,"TCMM0000|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfcca0015msa004"
    見里 "「にゃむっ……」"
    "眼鏡を拭きながらあくびを噛み殺す。"
    call gl(1,"TCMM0000|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa019"
    見里 "「ふー、からだがだるいです」"
    太一 "「でしょうな」"
    voice "vfCCD1001msa020"
    見里 "「何時なんですか？」"
    太一 "「八時くらいです」"
    hide pic1
    with dissolve
    "無言で横たわった。"
    "手を合わせて枕にする。"
    太一 "「死ぬというのに」"
    "転がっている荷物の中には酒瓶もある。"
    "飲んで逃げて飲んで逃げて。"
    "先輩も大変。"
    太一 "「ま、勝手にやらしてもらいますか」"
    voice "vfcca0015msa032"
    見里 "「ＺＺＺ……」"
    "先輩を背負う。"
    "まったく起きる気配はない。"
    call gl(0,"bgcc0012")
    call vsp(0,1)
    with wipeleft
    "無人の保健室。"
    "あいているベッドに先輩を寝かせる。"
    太一 "「おやすみ先輩、良い夢を」"
    stop bgm
    play bgm "bgm/bgm021.ogg"
    call gl(0,"bgcc0007")
    call vsp(0,1)
    with wipeleft
    "作業を進める。"
    "長い固有の人生を経て、技術と知識は備わっている。"
    "先輩よりも、ずっと効率的にシステムを構成していく。"
    "汗水垂らして働くのは嫌いじゃない。心地よい。"
    "肉体が自動化し、記憶の一つが浮上した。"
    "屋上を舞台に、心が過去をなぞらえて、再び衝動を再現しようとする。"
    call gl(0,"bgcc0007s")
    call vsp(0,1)
    with Pixellate(300.0*2/1000.0,5)
    "警備の目を逃れるのは、俺の日課だった。"
    "その日も、昼休みの屋上に身を置いていた。"
    "すぐに見つかるかと割り切っていたのに、存外、死角だった。"
    "昼休みの終了まで一人、ぼうと空を眺めている。"
    "誰も傷つける可能性のない安息。"
    "ひるがえって、誰とも接続できないことを意味した。"
    "構わない、と思っていた。"
    "第一目標はヒトの中で生きることで、楽しむことは考慮になかったから。"
    "爆弾を抱えていることは自覚していた。"
    "人付き合いは、俺にとって高い買い物だ。"
    "支払うべきは持続的なストレス環境。"
    "得るものは過程のみの結束。ハッピーエンド抜き。"
    "億劫になって当然だった。"
    "今度やったら、あとがないのは間違いない。"
    "孤独を日常化。"
    "自らの心を鈍感にする以外、どんな手段があったろう？"
    call gl(1,"TCMM0002s|TCMM000x")
    call gp(1,t=center)#x=225
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa021"
    見里 "「また会いましたねー、黒須君」"
    "話しかけてきたのは、向こうだった。"
    太一 "「……」"
    "戸惑い、だったと思う。"
    "そんな風に接されたこと、ついぞない。"
    "胸のでかい女だった。"
    "微量の劣情を、抱かぬでもない。"
    "俺は基本的に現実女は苦手であったわけだが、嫌悪していたわけではない。"
    "女はニコニコと、反応を待っている。"
    "立ち去るつもりはないらしい。"
    "俺は『ほっといてくれ』オーラを放った。"
    call gl(1,"TCMM0021s|TCMM0021")
    call vsp(1,1)
    with dissolve
    voice "vfcca0016msa031"
    見里 "「？」"
    "女は気づかなかった。"
    太一 "「……どうして俺の名前を？」"
    "仕方なく、応じた。敗北。"
    call gl(1,"TCMM0002s|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa022"
    見里 "「ああ、そんな声をなさってたんですね」"
    "手を叩いて、もっとニコニコした。"
    太一 "「どうして、俺の、名前を？」"
    "区切って問う。"
    call gl(1,"TCMM0000s|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa023"
    見里 "「はい。名簿で」"
    "名簿とか言う。"
    "そんな簡単に見られるものなのかよ。"
    "というか見せていいのかよ、学校。"
    "俺は皮肉を繰りだした。"
    太一 "「……探偵みたいな真似事をするんですね。犯罪者かな？」"
    太一 "「高等部では、そんなことも教えるんですか」"
    "皮肉として、かなりの自信作だった。"
    call gl(1,"TCMM0005s|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa024"
    見里 "「あう、手厳しいです」"
    call gl(1,"TCMM0002s|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa025"
    見里 "「でも確かに、ごめんなさいです」"
    "受け流される俺のアイロニー。"
    太一 "「……」"
    call gl(1,"TCMM0000s|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa026"
    見里 "「事情を説明するとですね、青田刈りです」"
    call gl(1,"TCMM0021s|TCMM0021")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa027"
    見里 "「わたし、放送部の者なんですけど……」"
    太一 "「知ってます」"
    太一 "「昼の放送で、よく聞きますから」"
    "イヤでも。"
    call gl(1,"TCMM0002s|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa028"
    見里 "「ああ、それなら話がはやいですね。ええ、あれわたしです。お昼のＤＪ」"
    太一 "「お世辞にもうまいとは思いませんけど」"
    call gl(1,"TCMM0005s|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa029"
    見里 "「……苦手なんですよ……ああいうの……」"
    "しおれる。"
    太一 "「苦手ってわかってるなら、おやめになればいい」"
    "会話慣れしていないため、変な敬語になる。"
    call gl(1,"TCMM0003s|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa030"
    見里 "「万年人手不足なんです」"
    "さっと、てのひらを上に片手を差し出して。"
    call gl(1,"TCMM0000s|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa031"
    見里 "「そこで黒須君を誘惑したいわけです」"
    太一 "「……」"
    太一 "「…………ふ」"
    "ニヒルに笑おうとしたが失敗し、顔面筋肉が電気を通されたみたいに痙攣した。"
    "……最悪だった。"
    "無表情を装備し、告げる。"
    太一 "「ごめんなさい。他、あたってください」"
    "立ち去る。"
    call gl(1,"TCMM0004s|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa032"
    見里 "「あー、ちょっとちょっと！！」"
    "……………………。"
    call gl(0,"bgcc0007")
    call vsp(0,1)
    call vsp(1,0)
    with Pixellate(300.0*2/1000.0,5)
    "彼女に誘われてはじめた部活。"
    "今は。"
    "拒絶されている。"
    stop bgm
    call gl(0,"bgcc0000d")
    call vsp(0,1)
    with Dissolve(500.0/1000.0)
    pause (500.0/1000.0)
    pause (1000.0/1000.0)
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
    play bgm "bgm/bgm010.ogg"
    call gl(0,"bgcc0007")
    call vsp(0,1)
    with wipeleft
    call gl(1,"TCMM0000|TCMM000x")
    call gp(1,t=center)#x=225
    call vsp(1,1)
    with dissolve
    voice "vfcca0016msa000"
    見里 "「ぺけくん」"
    "疑惑の視線に出迎えられた。"
    太一 "「おや、部長」"
    太一 "「二日酔いになってませんか？」"
    call gl(1,"TCMM0011|TCMM0011")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa033"
    見里 "「……なってます。あいたたた」"
    call gl(1,"TCMM0000|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa034"
    見里 "「じゃなくてですね、わたしが保健室で寝ていたりなんか作業が進められていたり……といった不思議現象が発生中です」"
    太一 "「それは俺です」"
    call gl(1,"TCMM0004|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa035"
    見里 "「あなたが？」"
    太一 "「先輩にそうしろって言われて」"
    voice "vfCCD1001msa036"
    見里 "「えっ？　そんなこと言いましたっけ？」"
    太一 "「ええ、酔ってたせいですかね。記憶にないんですか？」"
    call gl(1,"TCMM0005|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa037"
    見里 "「あああ……」"
    "悩みだす。"
    "ついでに恩も売っておく。"
    太一 "「あと先輩がいきなり裸踊りをはじめたときはどうしようかと思いました」"
    call gl(1,"TCMM0007|TCMM0007")
    call vsp(1,1)
    with dissolve
    voice "vfcca0016msa016"
    見里 "「っ！？」"
    "先輩の目が横長の『×』マークになった。"
    voice "vfcca0016msa017"
    見里 "「ああああっ！」"
    voice "vfCCD1001msa038"
    見里 "「わたしがそんなことを……信じられません！」"
    太一 "「こんな具合に……」"
    call gl(0,"bgcc0000e")
    call vsp(0,1)
    call vsp(1,0)
    with Pixellate(300.0*2/1000.0,5)
    voice "vfCCD1001msa039"
    見里 "「あつい、あついれすぅ……着てられないですぅ」"
    "先輩は左手でネクタイをほどきつつ、その三秒後に右手を斜め下４５度の角度から差し入れ、結び目に人差し指の第二関節までを０．６２秒で埋没させた。"
    "相反する両手の力がネクタイの摩擦力を上回り、長さおよそ３２センチほどの首回り部分を結び目から引き抜いた。"
    "次に右手で第一ボタンならびに第二ボタンをそれぞれ約二秒ではずし、胸元をはだけた。"
    voice "vfCCD1001msa040"
    見里 "「そーれ、ぱっぱっぱー」"
    "肩ひもを両手で落とし、右手は再びブラウスのボタン、左手はスカートのサイドホックとファスナーを外しにかかる。"
    "四秒二八時点でブラウス、七秒三四時点でスカート。"
    "下着姿になった。"
    voice "vfCCD1001msa041"
    見里 "「ぱんつもぬいじゃえですー」"
    "『も』のあたりで、足首まで落とした。"
    "足を抜いて、恥毛を風にそよがせつつ、ブラのホックを外す。"
    "張った胸がカップを押し出し、布地はふわりと宙に躍りでた。滑空するほどの浮力を得ることもできず、もんどりうって地面にとぐろを巻いた。"
    "もはや先輩の着衣は、メガネとソックス＆シューズだけ。"
    "メガネは顔の一部なので、実質全裸靴下だ。"
    voice "vfCCD1001msa042"
    見里 "「誰か見てください、わたしの一糸まとわぬ姿、誰かー」"
    "両腕を水平に伸ばし、左方向に秒速一回転でターンしながら六メートル五十三センチほど移動した。"
    voice "vfCCD1001msa043"
    見里 "「モザイクのないわたしの真実のすがたをー」"
    "残念ながらモザイクはあった。"
    voice "vfCCD1001msa044"
    見里 "「らーーらららららーーらーららー」（★★★適当に）"
    "そんな美しい先輩の姿を、俺はなすすべなく見つめていた。"
    "～ＥＮＤ～"
    call gl(0,"bgcc0007")
    call gl(1,"TCMM0003|TCMM000x")
    call vsp(0,1)
    call vsp(1,1)
    with Pixellate(300.0*2/1000.0,5)
    voice "vfCCD1001msa045"
    見里 "「……しくしくしく……見てはいけないと言ったのに、見てしまったのですね」"
    "ぺたりと斜めに座って、大和撫子泣き。"
    太一 "「それは鶴の恩返し」"
    call gl(1,"TCMM0005|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa046"
    見里 "「そんな的確に描写されているということは、事実なんですねっ！」"
    太一 "「ＹＥＳ」"
    "泣き伏す。"
    太一 "「でもご安心を。僕がうまく処理して、人目につかないよう片づけておきました」"
    call gl(1,"TCMM0000|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfcca0016msa018"
    見里 "「……ああ、そうだったの……どうも、ありがとう」"
    太一 "「いいえー」"
    太一 "「あと原稿書いてきました」"
    stop bgm
    call gl(1,"TCMM0004|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa047"
    見里 "「え？　そんなことまでお願いしてたんですか？」"
    太一 "「はい、見て下さい」"
    "文面は過去のものを転用した。"
    call gl(1,"TCMM0000|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa048"
    見里 "「ううん……これはいいですねぇ」"
    "顔をあげて、笑みを見せて。"
    call gl(1,"TCMM0002|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa049"
    見里 "「わたしたちらしいです」"
    太一 "「じゃ没はなしですね」"
    "二人で笑いさざめく。わずか。"
    "先輩の顔が、曇る。"
    play bgm "bgm/bgm013.ogg"
    call gl(1,"TCMM0003|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa050"
    見里 "「……結局、一人じゃ何もならないんですね」"
    太一 "「無理があったんでしょう」"
    太一 "「徹夜したり、日中無茶したら駄目です。禁止です」"
    voice "vfCCD1001msa051"
    見里 "「うう……後輩にお説教される部長って……」"
    "先輩が立ち上がるのと、立てかけてあった様々な資材が動き出すのが、同時だった。"
    "引き寄せる。"
    太一 "「危ない」"
    call gl(1,"TCMM0004|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfcca0016msa045"
    見里 "「え？」"
    "脚立や鉄針、工具……そんなものが。"
    play se "SE017"
    "不協和音を奏でながら、床に散らばった。"
    call gl(0,"evcc0036")
    call vsp(0,1)
    call vsp(1,0)
    with ImageDissolve("sys/EFMSK_22_MSK.bmp",time=1)
    voice "vfCCD1001msa052"
    見里 "「あ……」"
    太一 "「危ない危ない」"
    voice "vfCCD1001msa053"
    見里 "「あ……ど、どうも……」"
    太一 "「もうちょっと」"
    voice "vfCCD1001msa054"
    見里 "「あ、で、でも……」"
    太一 "「もうちょっとこうしてないと、危険ですので」"
    voice "vfCCD1001msa055"
    見里 "「……そうでしょうか……」"
    "先輩のにおい。"
    "湧きだした記憶が、リアルな初夏の空気を携えて、鼻先にけぶる。"
    play se "se001"
    call gl(0,"bgcc0007s")
    call vsp(0,1)
    with Pixellate(300.0*2/1000.0,5)
    call gl(1,"TCMM0002s|TCMM000x")
    call gp(1,t=center)#x=225
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa056"
    見里 "「こんばんわぁ」"
    "うとうとしていると、首筋に冷たい感触。"
    太一 "「……うわ、なにを？」"
    call gl(1,"TCMM0000s|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa057"
    見里 "「冷たいジュースの時間です」"
    "先輩が、二本の缶をぶらさげていた。"
    太一 "「……」"
    call gl(1,"TCMM0002s|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa058"
    見里 "「おごりですよ」"
    太一 "「…………」"
    "受け取らされた。"
    太一 "「……先輩も、しつこい人ですよね」"
    太一 "「あまり俺に関わらない方がいいと思いますよ」"
    call gl(1,"TCMM0021s|TCMM0021")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa059"
    見里 "「どうしてです？」"
    "隣に座る。"
    太一 "「ろくでもないヤツですから」"
    太一 "「気を抜くと、人を傷つけたくなる」"
    太一 "「……危険人物なんですよ」"
    call gl(1,"TCMM0000s|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa060"
    見里 "「あー……重そうです……」"
    "名簿を見たなら、察しているはずだ。"
    "赤枠で記された、俺の名を。"
    太一 "「部活だって？　俺の参加は許可されないと思いますよ」"
    太一 "「あなただってここの人間なら……わかるはずだ」"
    call gl(1,"TCMM0002s|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa061"
    見里 "「はい。だからこうしてお話してみたんですよ」"
    太一 "「……話だけじゃわからないことも多い」"
    call gl(1,"TCMM0000s|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa062"
    見里 "「一つわかったことが」"
    "指を立てる。真面目な顔。"
    太一 "「……というと？」"
    voice "vfCCD1001msa063"
    見里 "「あなたは……普通コンプレックスです」"
    太一 "「……っ」"
    "当てた。なんて人間洞察力だ。年の功か？"
    "どうやって思考を重ねたら、そんな的確な物言いができる。"
    "俺は戦慄した。"
    call gl(1,"TCMM0002s|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa064"
    見里 "「そんな顔してます」"
    "顔でかよ。"
    "俺は弛緩した。"
    call gl(1,"TCMM0000s|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa065"
    見里 "「つまり、健全さを求めているということです」"
    call gl(1,"TCMM0003s|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa066"
    見里 "「……わたしと一緒」"
    "彼女は手首の傷跡を見せた。"
    "うっすらと消えかけているそれは、だいぶ古い。"
    太一 "「……これって？」"
    call gl(1,"TCMM0000s|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa067"
    見里 "「自傷症状です」"
    voice "vfCCD1001msa068"
    見里 "「手首なんて切っても、よほど準備しない限り人は死にません」"
    voice "vfCCD1001msa069"
    見里 "「けどストレスがたまると、わたしは自分を傷つけるんですよ」"
    call gl(1,"TCMM0031s|TCMM0031")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa070"
    見里 "「わたしにとって、ストレスっていうのは……うまく説明できないですけど、きっちりしてないことなんですよ」"
    call gl(1,"TCMM0000s|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa071"
    見里 "「荒れてる部屋とか、守られてないルールとか」"
    太一 "「大変だ」"
    太一 "「世の中、ほとんどその口じゃないですか」"
    call gl(1,"TCMM0003s|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa072"
    見里 "「そーなんですよね……ストレスの元だらけです」"
    voice "vfCCD1001msa073"
    見里 "「ニッチもサッチも行かなくなって、自分を傷つけて……」"
    voice "vfCCD1001msa074"
    見里 "「時には、他人も傷つけて」"
    voice "vfCCD1001msa075"
    見里 "「そういうジレンマがあります」"
    太一 "「俺のは違います」"
    太一 "「俺のは……」"
    "ふわりと抱きしめられた。"
    太一 "「ちょ」"
    call gl(1,"TCMM0002s|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa076"
    見里 "「いいですよ、つらかったら話さなくても」"
    voice "vfCCD1001msa077"
    見里 "「……とにかく、駄目なわたしなのです」"
    voice "vfCCD1001msa078"
    見里 "「しかしながら、普通を目指して奮闘中です」"
    太一 "「先輩……は……」"
    call gl(1,"TCMM0000s|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa079"
    見里 "「飛び交う電波、燃え上がる友情、様々な事件、そして和解……あなたも凡人目指して、我々とともに頑張ってみませんか？」（*★★★演説調）"
    太一 "「…………」"
    call gl(1,"TCMM0002s|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa080"
    見里 "「群青学院放送部は、自信のない多感な少年を募集中です」"
    太一 "「……まるで宗教の勧誘だ」"
    call gl(1,"TCMM0000s|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa081"
    見里 "「いいじゃないですか、宗教」"
    太一 "「変な女」"
    call gl(1,"TCMM0006s|TCMM0006")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa082"
    見里 "「こら！」"
    太一 "「……いて」"
    "コツン"
    "頭突き。"
    voice "vfCCD1001msa083"
    見里 "「目上の人は、先輩です」"
    call gl(1,"TCMM0000s|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa084"
    見里 "「そしてあなたの飲んだジュース代は、部費から出ています」"
    太一 "「……きったな」"
    call gl(1,"TCMM0002s|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa085"
    見里 "「見学する義務がありますよ、君。うん、あります」"
    太一 "「……大人の手段だ」"
    call gl(1,"TCMM0000s|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa086"
    見里 "「部員が少なくて、一年生なのにアクセクしないといけない下っ端のお嬢ちゃんです」"
    太一 "「でかい胸、あたるんですけど。いいんですかこの体勢」"
    call gl(1,"TCMM0002s|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa087"
    見里 "「あ、君はもうそんなことに興味があるんですか？」"
    太一 "「俺、男なんですけど」"
    voice "vfCCD1001msa088"
    見里 "「うちの弟は、まだ全然子供ですよ」"
    "無防備すぎる。"
    "無防備すぎて。"
    太一 "「……はは」"
    "笑ってしまった。"
    太一 "「入部」"
    call gl(1,"TCMM0021s|TCMM0021")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa089"
    見里 "「はい？」"
    太一 "「……入部します」"
    call gl(1,"TCMM0004s|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa090"
    見里 "「え、本当の本当に？」"
    太一 "「ずっとおっぱい押しつけられて勧誘されるより、マシですから」"
    call gl(1,"TCMM0002s|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa091"
    見里 "「わあ！　やったあ！　わたし、すごい！」"
    "あんたかよ……。"
    stop se
    call gl(0,"bgcc0007")
    call vsp(0,1)
    call vsp(1,0)
    with Pixellate(300.0*2/1000.0,5)
    太一 "「逆だ」"
    太一 "「あの時と逆」"
    call gl(1,"TCMM0021|TCMM0021")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa092"
    見里 "「……あの時……？」"
    太一 "「もう忘れましたか？」"
    call gl(1,"TCMM0000|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa093"
    見里 "「ああ……あの時のことでしたか」"
    "平気で俺を胸に押し当てた先輩。"
    "当時の無邪気さは、もうない。"
    "抱きしめれば、身じろいで狼狽える。"
    "それは先輩が、俺を異性として意識してくれているということで。"
    "少し胸が弾む。"
    call gl(1,"TCMM0000|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa094"
    見里 "「……そんなことが、あったような気がします」"
    太一 "「いきなり抱きつかれて驚いたから、仕返し」"
    call gl(1,"TCMM0005|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa095"
    見里 "「あれは……だって、子供だと思っていたから」"
    太一 "「もっと警戒しないと、傷つきますよ」"
    call gl(1,"TCMM0003|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa096"
    見里 "「……自分が傷つくのは、いいのです」"
    voice "vfCCD1001msa097"
    見里 "「人を傷つけるよりは」"
    太一 "「先輩みたいな人が、どうやって人を傷つけるんだか」"
    call gl(1,"TCMM0001|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa098"
    見里 "「…………傷つけますよ……」"
    "掠れる声、額をなすりつけてきた。"
    "年上のお姉さん。"
    "今は。"
    "無垢な少女のよう。"
    stop bgm
    call gl(0,"bgcc0012a")
    call vsp(0,1)
    call vsp(1,0)
    with wipeleft
    pause (500.0/1000.0)
    call gl(0,"evcc0006a")
    call vsp(0,1)
    with wipeleft
    play bgm "bgm/bgm003.ogg"
    voice "vfCCD1001msa099"
    見里 "「あの……」"
    太一 "「ホワイ？」"
    voice "vfCCD1001msa100"
    見里 "「どうして、怪我してないのに看護されてます？」"
    太一 "「もしかして擦り傷ができてるかもしれないじゃないですか」"
    voice "vfCCD1001msa101"
    見里 "「できてましたっけ……？」"
    太一 "「まあいいんです。お疲れのようですし、少し休んだ方が」"
    voice "vfCCD1001msa102"
    見里 "「はあ……」"
    太一 "「はい、先輩の携帯」"
    voice "vfCCD1001msa103"
    見里 "「あ、どうもです」"
    太一 "「使えないのに持ってるんですね」"
    voice "vfCCD1001msa104"
    見里 "「……不安なんです。持ってないと」"
    voice "vfCCD1001msa105"
    見里 "「連絡が入ったとき、すぐに出られるように」"
    太一 "「……連絡？」"
    voice "vfCCD1001msa106"
    見里 "「家族から」"
    太一 "「先輩のご家族って……」"
    voice "vfCCD1001msa107"
    見里 "「刑務所……」"
    太一 "「え゛？」"
    voice "vfCCD1001msa108"
    見里 "「……犯罪者をなりわいとしております」"
    太一 "「は、初耳なんですけど」"
    voice "vfCCD1001msa109"
    見里 "「お金の横領が脱税でドボンなのですよ」"
    "いろいろあったらしい。"
    太一 "「俺も性犯罪者にならないよう、注意しないと」"
    voice "vfCCD1001msa110"
    見里 "「……笑えない」"
    太一 "「さて」"
    voice "vfCCD1001msa111"
    見里 "「？」"
    太一 "「そろそろ眠って下さい」"
    voice "vfCCD1001msa112"
    見里 "「えええええええっちなことされそうです～」"
    太一 "「失敬な。そんなことしやしません」"
    "今は。"
    太一 "「先輩は、安らかに生きていいんですよ」"
    call gl(0,"evcc0006")
    call vsp(0,1)
    with Dissolve(500.0/1000.0)
    "てのひらで、目を閉じさせる。"
    call gl(0,"bgcc0008a")
    call vsp(0,1)
    "廊下を出る。"
    "友貴を捜す。"
    "すぐに見つけることができた。"
    "呼びかける。"
    call gl(1,"TCST0000b|TCST0000")
    call gp(1,t=center)#x=190
    call vsp(1,1)
    with dissolve
    voice "vmCCD1001yki000"
    友貴 "「太一か……」"
    太一 "「姉さん心配か？」"
    call gl(1,"TCST0002b|TCST0001")
    call vsp(1,1)
    with dissolve
    voice "vmCCD1001yki001"
    友貴 "「……え、いやそんなんじゃないけど……事件かなって」"
    call gl(1,"TCST0004b|TCST0004")
    call vsp(1,1)
    with dissolve
    voice "vmCCD1001yki002"
    友貴 "「それに、関係ないよ。親離婚してるし」"
    call gl(1,"TCST0000b|TCST0000")
    call vsp(1,1)
    with dissolve
    voice "vmCCD1001yki003"
    友貴 "「僕らだって、別個の親と暮らしてるし」"
    "別個の親？"
    "四人家族が半々になったってことか？"
    太一 "「そうだったのか。友貴はどっちの親と？」"
    call gl(1,"TCST0004b|TCST0004")
    call vsp(1,1)
    with dissolve
    voice "vmCCD1001yki004"
    友貴 "「……母親」"
    太一 "「じゃ先輩は父親か」"
    call gl(1,"TCST0000b|TCST0000")
    call vsp(1,1)
    with dissolve
    voice "vmCCD1001yki005"
    友貴 "「まあね……」"
    voice "vmCCD1001yki006"
    友貴 "「けど、なんかやってるの？　二人で？」"
    太一 "「ああ、部活につきあってる。先輩の」"
    call gl(1,"TCST0000b|TCST0000")
    call vsp(1,1)
    with dissolve
    voice "vmcca0018yki002"
    友貴 "「……どうしてまた？」"
    太一 "「いや、目的があっていいじゃないか」"
    voice "vmcca0018yki003"
    友貴 "「部活って、例の与太話？」"
    太一 "「与太じゃないよ」"
    call gl(1,"TCST0004b|TCST0004")
    call vsp(1,1)
    with dissolve
    voice "vmcca0018yki004"
    友貴 "「太一がそういうことするのは……なんか、まあ、理由あってのことだろうけど」"
    call gl(1,"TCST0000b|TCST0000")
    call vsp(1,1)
    with dissolve
    voice "vmcca0018yki005"
    友貴 "「他に誰が参加してんの？」"
    太一 "「部長」"
    call gl(1,"TCST0001b|TCST0001")
    call vsp(1,1)
    with dissolve
    voice "vmcca0018yki006"
    友貴 "「……だけ？」"
    太一 "「そう」"
    call gl(1,"TCST0003b|TCST0000")
    call vsp(1,1)
    with dissolve
    voice "vmcca0018yki007"
    友貴 "「それ部活じゃない……」"
    太一 "「部活と思えば自慰だって部活だ」"
    call gl(1,"TCST0000b|TCST0000")
    call vsp(1,1)
    with dissolve
    voice "vmcca0018yki008"
    友貴 "「……最近、いろいろと動いてるのは知ってたけど、部活とはね」"
    "肩をすくめた。"
    太一 "「友貴もどうだ、姉弟ネコイラズで」"
    call gl(1,"TCST0004b|TCST0004")
    call vsp(1,1)
    with dissolve
    voice "vmCCD1001yki007"
    友貴 "「水入らず」"
    call gl(1,"TCST0000b|TCST0000")
    call vsp(1,1)
    with dissolve
    voice "vmCCD1001yki008"
    友貴 "「……ごめんだね」"
    太一 "「そうか」"
    call gl(1,"TCST0004b|TCST0004")
    call vsp(1,1)
    with dissolve
    voice "vmcca0018yki012"
    友貴 "「……裏切られるぞ」"
    "ぽつ、と言う。"
    太一 "「いいよ、別に」"
    call gl(1,"TCST0000b|TCST0000")
    call vsp(1,1)
    with dissolve
    voice "vmCCD1001yki009"
    友貴 "「ん……」"
    太一 "「裏切らないことが、信頼の条件か？」"
    call gl(1,"TCST0001b|TCST0001")
    call vsp(1,1)
    with dissolve
    voice "vmCCD1001yki010"
    友貴 "「そりゃ……」"
    太一 "「だったら俺も駄目じゃん」"
    call gl(1,"TCST0000b|TCST0000")
    call vsp(1,1)
    with dissolve
    voice "vmCCD1001yki011"
    友貴 "「太一は裏切ってないだろ？」"
    太一 "「いやいや、いろんなものを裏切ったしこれからも裏切るしあまつさえ横切るよ」"
    call gl(1,"TCST0003b|TCST0000")
    call vsp(1,1)
    with dissolve
    voice "vmCCD1001yki012"
    友貴 "「……それがおまえの普段言うハイレベルなギャグとはどうしても思えない」"
    "そんなこと言ってない。"
    太一 "「そんな宝物のようなギャグがそうそう出てたまるか」"
    "数撃つ派だっつうの。"
    call gl(1,"TCST0004b|TCST0004")
    call vsp(1,1)
    with dissolve
    voice "vmCCD1001yki013"
    友貴 "「とにかく、あまり親しくしない方がいいよ。太一のためだ」"
    太一 "「いーや、親しくしちゃう。もう行くとこまで行っちゃう」"
    "色を失う友貴。"
    call gl(1,"TCST0001b|TCST0001")
    call vsp(1,1)
    with dissolve
    voice "vmCCD1001yki014"
    友貴 "「な、なに……いくとこって……」"
    太一 "「ゴールさ」"
    voice "vmCCD1001yki015"
    友貴 "「ゴールって……」"
    太一 "「挿入だ」"
    voice "vmCCD1001yki016"
    友貴 "「ぐ……」"
    "ショックを受ける。"
    call gl(1,"TCST0004b|TCST0004")
    call vsp(1,1)
    with dissolve
    voice "vmCCD1001yki017"
    友貴 "「それは……けど……」"
    太一 "「インモラルは考えすぎなんだよ」"
    "肩を叩く。"
    call gl(1,"TCST0000b|TCST0000")
    call vsp(1,1)
    with dissolve
    voice "vmCCD1001yki018"
    友貴 "「友貴です！」"
    太一 "「もっとピュアにインモラっていけ。おまえのためだ」"
    call gl(1,"TCST0003b|TCST0000")
    call vsp(1,1)
    with dissolve
    voice "vmCCD1001yki019"
    友貴 "「わからない度９５％」"
    太一 "「飛び交う電波、燃え上がる友情、様々な事件、そして和解……あなたも凡人目指して、我々とともに頑張ってみませんか？」"
    友貴 "「…………」"
    太一 "「群青学院放送部は、姉に性欲をもてあます少年を募集中です」"
    "先輩から借りた言葉。"
    "友貴にも、教えてやろうと思ったんだ。"
    call gl(1,"TCST0000b|TCST0000")
    call vsp(1,1)
    with dissolve
    voice "vmCCD1001yki021"
    友貴 "「……あのなぁ」"
    stop bgm
    call gl(0,"bgcc0003e")
    call vsp(0,1)
    call vsp(1,0)
    with wipeleft
    "そろそろ友貴が来る。"
    call gl(0,"bgcc0013b")
    call vsp(0,1)
    with wipeleft
    "玄関で待機。"
    play bgm "bgm/bgm004.ogg"
    call gl(0,"bgcc0013bz")
    call gl(1,"TCST0000c|TCST0000")
    call gp(1,t=center)#x=190
    call vsp(0,1)
    call vsp(1,1)
    with Dissolve(500.0/1000.0)
    voice "vmCCD1001yki022"
    友貴 "「たい―――」"
    太一 "「よく来たな。食料サンキュー」"
    call gl(1,"TCST0001c|TCST0001")
    call vsp(1,1)
    with dissolve
    voice "vmCCD1001yki023"
    友貴 "「うわっ、びっくりしたぁ……着物着てるし」"
    太一 "「文豪っぽかろ」"
    call gl(1,"TCST0000c|TCST0000")
    call vsp(1,1)
    with dissolve
    voice "vmcca0019yki006"
    友貴 "「いつもそんな格好なの？」"
    太一 "「無論だ」"
    call gl(1,"TCST0004c|TCST0004")
    call vsp(1,1)
    with dissolve
    voice "vmcca0019yki007"
    友貴 "「すごいね」"
    "友貴はよりいっそう俺を尊敬したようだった。"
    太一 "「飛び交う電波、燃え上がる友情、様々な事件、そして和解……あなたも凡人目指して、我々とともに頑張ってみませんか？」"
    call gl(1,"TCST0003c|TCST0000")
    call vsp(1,1)
    with dissolve
    友貴 "「…………」"
    太一 "「群青学院放送部は、素直になれないシスコン症候群の少年を募集中です」"
    call gl(1,"TCST0005c|TCST0004")
    call vsp(1,1)
    with dissolve
    voice "vmCCD1001yki025"
    友貴 "「……その文句さあ……飛び交う電波って部分、なんかヤバそうなんですけど」"
    太一 "「そか？」"
    call gl(1,"TCST0003c|TCST0000")
    call vsp(1,1)
    with dissolve
    voice "vmCCD1001yki026"
    友貴 "「群青でそれは……」"
    太一 "「１クラス平均１０人くらいは電波ゆんゆんだもんな……」"
    call gl(1,"TCST0000c|TCST0000")
    call vsp(1,1)
    with dissolve
    voice "vmCCD1001yki027"
    友貴 "「ああ……」"
    太一 "「それももういないけどな……」"
    voice "vmCCD1001yki028"
    友貴 "「ああ……」"
    太一 "「ま、とにかく食い物はありがたい」"
    call gl(1,"TCST0004c|TCST0004")
    call vsp(1,1)
    with dissolve
    voice "vmCCD1001yki029"
    友貴 "「友情は見返りを―――」"
    太一 "「求めない」"
    "ぐっ"
    "不敵に笑いつつ、親指を立てあった。"
    "もはやノルマだ。"
    call gl(1,"TCST0000c|TCST0000")
    call vsp(1,1)
    with dissolve
    voice "vmCCD1001yki030"
    友貴 "「じゃあな」"
    太一 "「そっちのが一段落ついたら、部活来ないか？」"
    "とたん、表情は硬くなった。"
    call gl(1,"TCST0004c|TCST0004")
    call vsp(1,1)
    with dissolve
    stop bgm
    voice "vmCCD1001yki031"
    友貴 "「……裏切り者と、部活なんてしたくない」"
    play se "SE001"
    call gl(0,"bgcc0003s")
    call vsp(0,1)
    call vsp(1,0)
    with Pixellate(300.0*2/1000.0,5)
    play se "SE021"
    太一 "「はいはーい」"
    太一 "「どちら様で？」"
    call gl(0,"bgcc0013as")
    call vsp(0,1)
    with wipeleft
    voice "vfcca0020ysa000"
    遊紗 "「あ、あの、堂島です」"
    play bgm "bgm/bgm003.ogg"
    太一 "「その極道みたいな苗字とは裏腹にキュートな声は……遊紗ちゃん？　あいてるからどーぞ」"
    "ドアがおそるおそる開き、美少女が立っていた。"
    call gl(0,"bgcc0013azs")
    call vsp(0,1)
    call gl(1,"TCDY0004s|TCDY0004")
    call gp(1,t=center)#x=240
    with Dissolve(500.0/1000.0)
    voice "vfcca0020ysa001"
    遊紗 "「どうも、こんばん……は」"
    call gl(0,"bgcc0004s")
    call vsp(0,1)
    call vsp(1,0)
    with wipeleft
    "座らせて、麦茶を出す。"
    "いろいろ会話をして。"
    call gl(1,"TCDY0000s|tcdy000x")
    call vsp(1,1)
    with dissolve
    voice "vfcca0020ysa019"
    遊紗 "「あの、わたし今日が誕生日なんです」"
    太一 "「へえ、そうだったのか」"
    call gl(1,"TCDY0001s|tcdy000x")
    call vsp(1,1)
    with dissolve
    voice "vfcca0020ysa020"
    遊紗 "「それでですね、これ……お誕生日プレゼントです」"
    太一 "「ええと……とりあえず、ありがとう。でも、あれ？」"
    call gl(1,"TCDY0000s|tcdy000x")
    call vsp(1,1)
    with dissolve
    voice "vfcca0020ysa022"
    遊紗 "「それと、交換日記を明日提出できたらなと思ったので……」"
    call gl(0,"bgcc0004s")
    call vsp(0,1)
    call vsp(1,0)
    with ImageDissolve("sys/EFMSK_22_MSK.bmp",time=1)
    太一 "「じゃあとりあえず交換日記と、それとこれは俺からの誕生日プレゼント」"
    call gl(1,"TCDY0004s|TCDY0004")
    call vsp(1,1)
    with dissolve
    voice "vfcca0020ysa027"
    遊紗 "「…………」"
    "この娘は驚くと絶句する癖があった。"
    太一 "「さてと、じゃ家まで送ろうか」"
    voice "vfcca0020ysa028"
    遊紗 "「……………………っっ！？」"
    "さっきの倍くらいに絶句した。"
    太一 "「もう夜だし、ちょっと危ない人もいるからね」"
    "特にこの街には。"
    太一 "「行こうか？」"
    call gl(1,"TCDY0001s|tcdy000x")
    call vsp(1,1)
    with dissolve
    voice "vfcca0020ysa029"
    遊紗 "「は、はいっ」"
    call gl(0,"bgcc0005s")
    call vsp(0,1)
    with wipeleft
    "そして、送った。"
    call gl(1,"TCDY0001s|tcdy000x")
    call vsp(1,1)
    with dissolve
    voice "vfcca0020ysa032"
    遊紗 "「その質問、毎回しますよね、太一さん？」"
    call gl(1,"TCDY0003s|tcdy000x")
    call vsp(1,1)
    with dissolve
    voice "vfcca0020ysa037"
    遊紗 "「難しくてよくわかりませんですけど……はい」"
    call gl(1,"TCDY0001s|tcdy000x")
    call vsp(1,1)
    with dissolve
    voice "vfcca0020ysa040"
    遊紗 "「きょーしゅーです」"
    "きょーしゅーです。"
    "きょーしゅー。"
    "郷愁？"
    "違う。"
    "強襲。"
    stop bgm
    "強襲。"
    "そう、強襲。"
    "激しく、攻めること。"
    "ああ。"
    "俺はこの言葉が、好きだな。"
    "夢の中で笑う。"
    "とめどなく。"
    "嘲弄。"
    "沈んだ感情はすぐに深淵に呑まれる。"
    extend "シニシズムの虚無を思わせるメッキは溶解し、むきだしになっ"
    "たカケラが……巨大な母体にまざって、戯れる。"
    "思考は一つ。"
    "敵は敵。"
    "殺さば殺す。"
    stop se
    call gl(0,"bgcc0000d")
    call vsp(0,1)
    call vsp(1,0)
    with Dissolve(500.0/1000.0)
    "だけどそんな思考さえも、俺は、殺してしまいたい―――"
    call gl(0,"bgcc0007")
    call vsp(0,1)
    call vsp(1,0)
    with wipeleft
    "トンテンカンテン"
    play se "SE023"
    "トンテンカンテン"
    play bgm "bgm/bgm012.ogg"
    "今朝も屋上では、精力的な部活動が行われている。"
    play se "SE001"
    call gl(0,"bgcc0007s")
    call vsp(0,1)
    with Pixellate(300.0*2/1000.0,5)
    play bgm "bgm/bgm018.ogg"
    "入部を決意した俺だが、なかなか許可はおりなかった。"
    "先輩はいろいろと動いてくれていた。"
    "俺に気づかれないように。"
    "……速攻で気づいていたけれど、ね。"
    "部員でなくとも、部活に参加するのは平気だった。"
    "一時の気分に流されて、口走った入部宣言。"
    "すぐに後悔して、撤回しようとした。"
    "けど……甘かった。"
    "俺はずるずると、"
    call gl(0,"bgcc0006s")
    call vsp(0,1)
    with Pixellate(300.0*2/1000.0,5)
    call gl(1,"TCMM0002s|TCMM000x")
    call gp(1,t=center)#x=225
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa113"
    見里 "「黒須くーん！」"
    "ずるずると、"
    call gl(0,"bgcc0008s")
    call vsp(0,1)
    call vsp(1,0)
    with Pixellate(300.0*2/1000.0,5)
    call gl(1,"TCMM0000s|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa114"
    見里 "「こんにちはー！」"
    "引っ張られ続けた。"
    call gl(0,"bgcc0010s")
    call vsp(0,1)
    call vsp(1,0)
    with Pixellate(300.0*2/1000.0,5)
    "やがて、部室にいることの方が多くなった。"
    call gl(1,"TCMM0000s|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa115"
    見里 "「えーと」"
    voice "vfCCD1001msa116"
    見里 "「まざーぼーどの……すろっとに……けーぶるを……んしょ、と！」"
    "実質、先輩は部活動の中心だった。"
    "ちゃんと活動できる人間だったからだ。"
    "二人きり。"
    call gl(1,"TCMM0005s|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa116a"
    見里 "「べいが……べいで……はーどでぃすく……うっ、またけーぶるがささらない……」"
    太一 "「……はぁ」"
    "見ていられなかった。"
    太一 "「違う。こっち」"
    call gl(1,"TCMM0002s|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa117"
    見里 "「あ、わかりますか？」"
    太一 "「……このくらいは」"
    call gl(1,"TCMM0000s|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa118"
    見里 "「じゃ、あの、こっちは？」"
    太一 "「あのですね……どうして既製品買わないんですか？」"
    太一 "「全然知識ないんだから、できあいの買いましょうよ」"
    call gl(1,"TCMM0002s|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa119"
    見里 "「これも部活の一部になるかなって」"
    太一 "「……んー」"
    call gl(1,"TCMM0005s|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa120"
    見里 "「あ、ミシッて音が……」"
    太一 "「ちょっとちょっと！　どいてください」"
    call gl(1,"TCMM0000s|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa121"
    見里 "「え？」"
    太一 "「そんなんじゃ、せっかくの高いパーツが壊れます」"
    call gl(1,"TCMM0002s|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa122"
    見里 "「あー、助かりますー」"
    "学校も金持ちなのか、部費で購入したと思われるパーツは、高級品ばかりだった。"
    call gl(1,"TCMM0000s|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa123"
    見里 "「へー。手際いいですねー」"
    太一 "「まあ、人並みには」"
    "皮肉。"
    call gl(1,"TCMM0002s|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa124"
    見里 "「えへへー、うちの弟もパソコン得意でしたよ」"
    "通じなかった。"
    太一 "「……そーですか」"
    voice "vfCCD1001msa125"
    見里 "「男の子ですねぇ」"
    太一 "「年下好きなんですか、あなた」"
    call gl(1,"TCMM0000s|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa126"
    見里 "「はい、年下の男の子って可愛いです」"
    太一 "「……」"
    太一 "「俺もおばさんは好きですよ」"
    "皮肉②。"
    call gl(1,"TCMM0031s|TCMM0031")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa127"
    見里 "「わたしも嫌いではないですけど、おばさんは恋愛対象にはならないですねぇ」"
    太一 "「当たり前です！」"
    "つい、興奮してしまった。"
    stop se
    call gl(0,"bgcc0007")
    call vsp(0,1)
    call vsp(1,0)
    with Pixellate(300.0*2/1000.0,5)
    太一 "「おはようございます」"
    voice "vfCCD1001msa128"
    見里 "「ああ……ぺけくん……きゃあ」"
    "脚立の上から先輩が、"
    play se "se024"
    extend "ぼてり"
    with vpunch
    "と落ちた。"
    "お姫様だっこで受け止めた。"
    voice "vfCCD1001msa129"
    見里 "「うわ……わわわっ！？」"
    太一 "「人助けの役得です」"
    "すぐおろす。"
    call gl(1,"TCMM0005|TCMM000x")
    call gp(1,t=center)#x=225
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa130"
    見里 "「……ど、どぉもっ」"
    太一 "「先輩、今丸々と太った芋虫みたいな落ち方でしたよ」"
    call gl(1,"TCMM0001|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa131"
    見里 "「……想像させないでくださいな、そんなもの」"
    "渋面＋赤面。"
    太一 "「そういや、虫いないんですよね」"
    call gl(1,"TCMM0000|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa132"
    見里 "「ええ、それだけがせめてもの救い……」"
    太一 "「静かなのはいいですけどね、蝉」"
    voice "vfCCD1001msa133"
    見里 "「ええ……」"
    太一 "「そういえば―――」"
    "自然に囲まれたこの街には、毎年多くの蝉がおとなう。"
    "他にもたくさんの虫がいる。"
    "丸々と太ったカブトムシとか、たまに家の壁にへばりついて切なそうにしていたりする。"
    "市街でそんなものを見るくらいで、当然あの白いエビチリにも似た幼虫はごろごろ山に埋まって解放の瞬間を夢見ている。"
    太一 "「そういう話を学食でエビチリを食いながらしたら、先割れスプーン装備の冬子と闘うことになりました」"
    call gl(1,"TCMM0002|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa134"
    見里 "「……ぷっ」"
    voice "vfCCD1001msa135"
    見里 "「あははははははっ」"
    "たった二人でも、部活は楽しい。"
    stop bgm
    太一 "「……ん？」"
    "気配。"
    call gl(1,"TCMM0000|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa136"
    見里 "「どうしました？」"
    太一 "「いえ、ちょっとご不浄に」"
    call gl(1,"TCMM0002|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa137"
    見里 "「あら、古風」"
    call gl(0,"bgcc0000d")
    call vsp(0,1)
    call vsp(1,0)
    with wipeleft
    "校舎に続く扉。"
    "開くと、階下に向かってあわてふためく足音が。"
    太一 "「曜子ちゃんじゃなかったか……」"
    "気配の消し方が稚拙だったしな。"
    "となると。"
    太一 "「友貴……か」"
    "素直になれないシステムコンポーネント野郎め。"
    "ま、とりあえずトイレには行っておこう。"
    call gl(0,"bgcc0008")
    call vsp(0,1)
    with wipeleft
    "みょー。（最中）"
    太一 "「ふう」"
    voice "vfCCD1001you000"
    曜子 "「……見参」"
    call gl(0,"evcc0009")
    call vsp(0,1)
    with ImageDissolve("sys/EFMSK_22_MSK.bmp",time=1)
    太一 "「おわっ、出た！」"
    play bgm "bgm/bgm011.ogg"
    "本物。"
    voice "vfCCD1001you001"
    曜子 "「おんぶ」"
    太一 "「……え？」"
    voice "vfCCD1001you002"
    曜子 "「胸だっこ」"
    voice "vfCCD1001you003"
    曜子 "「お姫様だっこ」"
    太一 "「……何よ」"
    voice "vfCCD1001you004"
    曜子 "「太一があの眼鏡女を抱いた種類」"
    太一 "「眼鏡女って……」"
    voice "vfCCD1001you005"
    曜子 "「多種多様なだっこがそこにあった」"
    太一 "「……ぜんぶ見てたの？」"
    voice "vfCCD1001you006"
    曜子 "「お姫様抱っこ」"
    voice "vfCCD1001you007"
    曜子 "「お姫様抱っこ」"
    voice "vfCCD1001you008"
    曜子 "「お姫様抱っこ」"
    "見ていたようだ。"
    太一 "「何を言いたいかはよくわかった……」"
    voice "vfCCD1001you009"
    曜子 "「お姫様抱っこ」"
    太一 "「……してほしいのか……その年で」"
    voice "vfCCD1001you010"
    曜子 "「年は関係ない」"
    太一 "「……あなたは誰かにお姫様だっこされなくても生きていけます」"
    "曜子ちゃんは無表情に憮然とした。"
    太一 "「それより、ちょっと手伝って欲しいところがあるんだけど……曜子ちゃん詳しいでしょ、ああいうの？」"
    voice "vfCCD1001you011"
    曜子 "「お姫様だっこ」"
    "うーむ。"
    太一 "「……交渉ってワケ？」"
    "頷く。"
    太一 "「わかったよ、します。すればいいんでしょ」"
    voice "vfCCD1001you012"
    曜子 "「ブライダルお姫様だっこ」"
    太一 "「そんな意味のわからないアレンジはできない」"
    voice "vfCCD1001you013"
    曜子 "「普通のでいい……」"
    太一 "「じゃ、おいで」"
    曜子 "「…………」"
    "嬉しそうだな。"
    "……だまされるな。"
    call gl(0,"bgcc0008")
    call vsp(0,1)
    with ImageDissolve("sys/EFMSK_22_MSK.bmp",time=1)
    "ちんまり。"
    曜子 "「…………」"
    太一 "「……どう？」"
    voice "vfCCD1001you016"
    曜子 "「……いい」"
    太一 "「じゃ、おろすね」"
    voice "vfCCD1001you017"
    曜子 "「だめ、だめ……」"
    "慌てた。"
    太一 "「もっと？」"
    voice "vfCCD1001you018"
    曜子 "「もっと」"
    voice "vfCCD1001you019"
    曜子 "「私はまだ満ち足りてないもの……」"
    太一 "「んー」"
    "この人、結構ずっしりしてるからつらいんだけどな。"
    "筋肉は脂肪より重い。"
    "恐るべき次世代子供の標準仕様だ。"
    "……次世代って変な意味の言葉だよな。"
    voice "vfCCD1001you020"
    曜子 "「散歩」"
    太一 "「散歩か……」"
    call gl(0,"bgcc0006")
    call vsp(0,1)
    with wipeleft
    pause (500.0/1000.0)
    call gl(0,"bgcc0009")
    call vsp(0,1)
    with wipeleft
    call gl(0,"bgcc0010")
    call vsp(0,1)
    with wipeleft
    voice "vfCCD1001you021"
    曜子 "「ん……」"
    "満足げだ。"
    "元からこういう人だったなら、もうちょっと、素直に好きになれるのに。"
    voice "vfCCD1001you022"
    曜子 "「……いい」"
    太一 "「あっそう」"
    "どうしても彼女の戦略が見えてしまう。"
    voice "vfCCD1001you023"
    曜子 "「すごく、いい」"
    太一 "「さいで」"
    call gl(0,"bgcc0008")
    call vsp(0,1)
    with wipeleft
    "移動する。"
    "重くなってきた。"
    太一 "「そろそろ……いいかな」"
    voice "vfCCD1001you024"
    曜子 "「いや」"
    太一 "「……むー」"
    "それから十分近く校内を歩かされた。"
    太一 "「ま、まだ？」"
    voice "vfCCD1001you025"
    曜子 "「もうちょっと」"
    太一 "「う、ううっ」"
    "腕が。"
    call gl(0,"bgcc0006")
    call vsp(0,1)
    with wipeleft
    pause (500.0/1000.0)
    call gl(0,"bgcc0011")
    call vsp(0,1)
    with wipeleft
    call gl(0,"bgcc0012")
    call vsp(0,1)
    with wipeleft
    "さらに一巡。"
    太一 "「もうきつくなってきました」"
    voice "vfCCD1001you026"
    曜子 "「あとちょっと……」"
    太一 "「時間にして、いつなったら満ち足りるんだろう？」"
    voice "vfCCD1001you027"
    曜子 "「小一時間ばかり」"
    太一 "「俺の腕千切れる」"
    "強制退位。"
    太一 "「おしまい」"
    call gl(1,"TCHY0001|tchy000x")
    call gp(1,t=center)#x=180
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001you028"
    曜子 "「……はぁ」"
    "落胆している。"
    "仕方ない。愛のセクハラをしてやるか。"
    太一 "「じゃかわりのことをしてあげよう」"
    call gl(1,"TCHY0000|tchy000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001you029"
    曜子 "「なにを？」"
    太一 "「一度やってみたかったことがあるんだ」"
    voice "vfCCD1001you030"
    曜子 "「それは？」"
    太一 "「逆肩車」"
    call gl(1,"TCHY0001|tchy000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001you031"
    曜子 "「意味わからない」"
    太一 "「普通の肩車を連想してください」"
    voice "vfCCD1001you032"
    曜子 "「ええ」"
    太一 "「通常、上側の人の膝は下の人の顔の向きと同様、前方を向くわけですが……」"
    太一 "「これをくるっと反転させて、背後を向きます」"
    太一 "「で、下の人はそのまま動かない」"
    太一 "「逆肩車」"
    call gl(1,"TCHY0001|tchy000x")
    call vsp(1,1)
    with dissolve
    曜子 "「……………………」"
    voice "vfCCD1001you034"
    曜子 "「……太一のエロパワーには、計り知れないものが」"
    太一 "「ありがとう。さあ、やろう」"
    call gl(1,"TCHY0000|tchy000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001you035"
    曜子 "「……それは……すごく……恥ずかしいこと、だと思う」"
    "珍しくためらう。"
    太一 "「ＯＫ、じゃみみ先輩に頼むか」"
    call gl(1,"TCHY0001|tchy000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001you036"
    曜子 "「しゃがんで……」"
    "簡単。"
    "みみ先輩が了承するはずがないのに。"
    太一 "「わーい」"
    hide pic1
    with dissolve
    "曜子ちゃんが目の前に立つ。"
    voice "vfCCD1001you037"
    曜子 "「……じゃあ……」"
    "太ももが、肩に乗った。"
    "片方ずつ。"
    call gl(0,"bgcc0000d")
    call vsp(0,1)
    call vsp(1,0)
    with Dissolve(500.0/1000.0)
    "そして逆肩車、完成―――"
    太一 "「おおおおお……」"
    太一 "「おおおおおおおお……」"
    太一 "「うおおおおおおおおおおおお……」"
    "悔いなしッ！！"
    stop bgm
    play se "SE001"
    call gl(0,"bgcc1009s")
    call vsp(0,1)
    with Pixellate(300.0*2/1000.0,5)
    "去年も確か、友貴はみみ先輩とケンカをしていた。"
    voice "vmcca0022yki028"
    友貴 "「それはお姉ち……姉貴が裏切るから……」"
    voice "vmcca0022yki029"
    友貴 "「放送部に入ったのだってさ、無理矢理なんだ。帰宅部しようと思ってたのに、あなたパソコン少年でしょだったら手伝ってとか言ってさ」"
    voice "vmcca0022yki034"
    友貴 "「なんでいまさら姉貴と仲良く部活動しなきゃなんないのよ」"
    "去年と今。"
    "二度の仲違い。"
    "その質には、大きな差があった。"
    stop se
    play bgm "bgm/bgm002.ogg"
    call gl(0,"bgcc0009")
    call vsp(0,1)
    with Pixellate(300.0*2/1000.0,5)
    "そして一年経った今日。"
    "友貴は一人、パンを食べていた。"
    太一 "「……よ」"
    call gl(1,"TCST0000|TCST0000")
    call gp(1,t=center)#x=190
    call vsp(1,1)
    with dissolve
    voice "vmCCD1001yki032"
    友貴 "「ああ……パンだったらそこに残ってるよ」"
    call gl(1,"TCST0005|TCST0004")
    call vsp(1,1)
    with dissolve
    voice "vmCCD1001yki033"
    友貴 "「傷んでるかも知れないけどな」"
    太一 "「ああ」"
    "傷んではいないだろう。"
    "だがカレーパンばかりだ。"
    "確か、真ん中あたりに……。"
    "あった、コロッケパン。"
    call gl(1,"TCST0001|TCST0001")
    call vsp(1,1)
    with dissolve
    voice "vmCCD1001yki034"
    友貴 "「あれ、そんなのあったの？」"
    太一 "「調査が甘い」"
    call gl(1,"TCST0000|TCST0000")
    call vsp(1,1)
    with dissolve
    voice "vmCCD1001yki035"
    友貴 "「……交換しない？」"
    太一 "「ほら」"
    call gl(1,"TCST0005|TCST0004")
    call vsp(1,1)
    with dissolve
    voice "vmCCD1001yki036"
    友貴 "「サンキュ」"
    "友貴はコロッケパンを食べた。"
    太一 "「……それ、放送部の予算から出てるパン」"
    call gl(1,"TCST0001|TCST0001")
    call vsp(1,1)
    with dissolve
    voice "vmCCD1001yki037"
    友貴 "「ぶっ、嘘つくな！」"
    call gl(1,"TCST0000|TCST0000")
    call vsp(1,1)
    with dissolve
    voice "vmCCD1001yki038"
    友貴 "「学食のパンなんですけど」"
    太一 "「部活を手伝う義務ができたな」"
    "先輩作戦だ。"
    call gl(1,"TCST0001|TCST0001")
    call vsp(1,1)
    with dissolve
    voice "vmCCD1001yki039"
    友貴 "「ないって！」"
    太一 "「……強情なやつ」"
    call gl(1,"TCST0004|TCST0004")
    call vsp(1,1)
    with dissolve
    voice "vmCCD1001yki040"
    友貴 "「手伝う理由なんてないじゃないか」"
    太一 "「家族だろ？」"
    call gl(1,"TCST0003|TCST0000")
    call vsp(1,1)
    with dissolve
    voice "vmCCD1001yki041"
    友貴 "「……いや、だからさ……」"
    "一気に疲労が浮かぶ。"
    "俺も知ってて言ったんだけど。"
    "ありとあらやゆる人間関係において。"
    "軽度の攻撃は、快楽になる。"
    "強すぎれば損傷するが。"
    "基本的に、人が人に触れる手段は攻撃しかない。"
    "交友とは、手加減の上手さでしかないように思う。"
    太一 "「たまにはいいだろ？」"
    call gl(1,"TCST0000|TCST0000")
    call vsp(1,1)
    with dissolve
    voice "vmCCD1001yki042"
    友貴 "「……今日は、しつこいんだな。太一らしくもない」"
    "そう、俺らしくもない。"
    voice "vmCCD1001yki043"
    友貴 "「ありのままを愛するのがおまえの身上じゃないのか？」"
    太一 "「ありのままを……」"
    太一 "「お、おまえ……俺に愛されたいのか？」"
    call gl(1,"TCST0002|TCST0001")
    call vsp(1,1)
    with dissolve
    voice "vmCCD1001yki044"
    友貴 "「それは言葉のあやだって！」"
    "おどけるのも、自爆するのも、攻撃ではない。"
    "知っている。全て。"
    "俺は玄関前で騒いでる、ちんどん屋みたいなもので。"
    "踏み込むことが下手な俺は、相手のすべてを肯定するしかないのだった。"
    "それしか手はない。普段なら。"
    太一 "「まあな、そこを突かれるとつらいのだが」"
    "でも今は―――"
    call gl(1,"TCST0000|TCST0000")
    call vsp(1,1)
    with dissolve
    voice "vmCCD1001yki045"
    友貴 "「……太一も気をつけた方がいいよ、本当に」"
    太一 "「どして」"
    call gl(1,"TCST0004|TCST0004")
    call vsp(1,1)
    with dissolve
    voice "vmCCD1001yki046"
    友貴 "「裏切られるだけだ」"
    太一 "「実例を示してくれないとわかんないな」"
    voice "vmCCD1001yki047"
    友貴 "「……売られるだけだ」"
    太一 "「いくらで？」"
    call gl(1,"TCST0003|TCST0000")
    call vsp(1,1)
    with dissolve
    voice "vmCCD1001yki048"
    友貴 "「真面目に聞く気はないのか……」"
    太一 "「……すまん……シリアルな空気がこそばゆくて……」"
    call gl(1,"TCST0004|TCST0004")
    call vsp(1,1)
    with dissolve
    voice "vmCCD1001yki049"
    友貴 "「シリアス！」"
    play se "se006"
    "机を叩く。"
    太一 "「そうカッカするな。生理っぽいぞ」"
    voice "vmCCD1001yki050"
    友貴 "「男だよ！　小豆馬鹿！」"
    太一 "「あ、小豆相場のことは言うなー！！」"
    hide pic1
    with dissolve
    "永遠のトラウマ。"
    call gl(4,"sgcc0001")
    play se "SE003"
    call vsp(4,1)
    with dissolve
    with vpunch
    voice "vmCCD1001yki051"
    友貴 "「くのー！」"
    太一 "「むがー！」"
    play se "SE003"
    with vpunch
    voice "vmCCD1001yki052"
    友貴 "「いぇやー！」"
    太一 "「ちぇいさー！」"
    "合意のもと互いにつける擦過傷は、心を豊かにする。"
    "だから満たされる。"
    call gl(0,"bgcc0007")
    call vsp(0,1)
    call vsp(1,0)
    call vsp(4,0)
    with wipeleft
    "というわけで、部活中だったりする。"
    "うーん。"
    "ここか？"
    "それともここか？"
    "この穴はなんだ？　ケーブルを通すのか？"
    太一 "「……」"
    "ここにしておくか。それっぽい感じするし。"
    voice "vfcca0022msa000"
    見里 "「わかりますかー？」"
    太一 "「まー、なんとか」"
    "下では先輩が脚立を支えてくれている。"
    voice "vfcca0022msa001"
    見里 "「男の子がいると頼もしいですねー」"
    太一 "「そうでしょうとも」"
    太一 "「ご用命の際はいつでもこの私メを……」"
    "つうか。"
    "この人、弟いるじゃないか。"
    太一 "「……あの、友貴と喧嘩してますよね？」"
    "先輩の顔が、さっとかげる。"
    play bgm "bgm/bgm013.ogg"
    voice "vfcca0022msa002"
    見里 "「あー、まあ……」"
    voice "vfcca0022msa003"
    見里 "「ちょっと冷戦に」"
    太一 "「友貴もケンカなんてするんだなぁ」"
    voice "vfcca0022msa004"
    見里 "「え？」"
    太一 "「あいつ、本気で怒ることなんて滅多にないから」"
    "先輩はその言葉に、ショックを受けたようだった。"
    voice "vfcca0022msa005"
    見里 "「……当然、なのかもしれないですね」"
    太一 "「はい？」"
    voice "vfcca0022msa006"
    見里 "「人生は難しいですこんちくしょうという感じです」"
    "わけがわからない。"
    voice "vmcca0022yki037"
    "友貴『……裏切られるぞ』"
    太一 "「あの、裏切りとか、なんです？」"
    voice "vfcca0030msa011"
    見里 "「……」"
    "眉根が寄った。"
    voice "vfcca0022msa007"
    見里 "「友貴が、そう言ってたんですか？」"
    太一 "「はあ」"
    voice "vfcca0022msa008"
    見里 "「……」"
    太一 "「先輩？」"
    voice "vfcca0022msa009"
    見里 "「……うーんうーん」"
    "先輩は泣きそうな顔で、うーんうーん唸りだした。"
    太一 "「アノウ？」"
    voice "vfcca0022msa010"
    見里 "「なんといいますかーもー！」"
    call gl(0,"bgcc0000a")
    call vsp(0,1)
    with dissolve
    extend "がくがくと脚立を揺する。"
    with vpunch
    太一 "「わわわっ！？」"
    with vpunch
    voice "vfcca0022msa011"
    見里 "「ままならねーですーっ！！」"
    with vpunch
    太一 "「落ちそーですっ！！」"
    with vpunch
    "散々な部活だった。"
    stop bgm
    call gl(0,"bgcc0003b")
    call vsp(0,1)
    with wipeleft
    voice "vfcca0024msa000"
    見里 "「……けーくーんー……」"
    "先輩が来た。"
    "誤差５分ってところか。"
    "十分も遅れたら、様子を見に行こうと思っていた。"
    call gl(0,"bgcc0000c")
    call vsp(0,1)
    with wipeleft
    太一 "「はーい」"
    play bgm "bgm/bgm012.ogg"
    voice "vfcca0024msa001"
    見里 "「こんばんはー」"
    "窓の下、手提げをさげた彼女が立っていた。"
    call gl(0,"bgcc0003b")
    call vsp(0,1)
    with wipeleft
    "そして予定通り、弁当を食べる。"
    太一 "「うまい」"
    太一 "「先輩は器用だなあ」"
    call gl(1,"TCMM0000c|TCMM000x")
    call gp(1,t=center)#x=235
    call vsp(1,1)
    with dissolve
    voice "vfcca0024msa015"
    見里 "「そうですか？　料理は最近はじめたばかりなんですけど……」"
    "他愛ない会話。"
    "そして。"
    stop bgm
    call gl(0,"evcc0012")
    call vsp(0,1)
    call vsp(1,0)
    with ImageDissolve("sys/EFMSK_22_MSK.bmp",time=1)
    voice "vfCCB1101msa020"
    見里 "「ん……んん……っ……」"
    "交わる。"
    call gl(0,"evcc0013")
    call vsp(0,1)
    call vsp(1,0)
    with Dissolve(500.0/1000.0)
    "幾度か体験した行為を、忠実になぞる。"
    "手慣れた分、与えた苦痛は少なかったはずだ。"
    call gl(0,"bgcc0003e")
    太一 "「明日、海にでも行きませんか？」"
    "誘い。"
    voice "vfCCB1101msa181"
    見里 "「……そうですね」"
    "はにかみ。"
    call gl(0,"bgcc0000d")
    call vsp(0,1)
    with Dissolve(500.0/1000.0)
    "体を重ねただけでは届かない領域が、存在していた。"
    call gl(0,"bgcc0003")
    call vsp(0,1)
    with Dissolve(500.0/1000.0)
    太一 "「金曜日、か」"
    "世界が揺り戻されるまで、あと三日。"
    "今日もなすべきことをしよう。"
    play bgm "bgm/bgm005.ogg"
    call gl(0,"bgcc0007")
    call vsp(0,1)
    with wipeleft
    太一 "「先輩、待ってました」"
    call gl(1,"TCMM0000|TCMM000x")
    call gp(1,t=center)#x=235
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa138"
    見里 "「……ぺけくん」"
    太一 "「海行く約束、忘れてないでしょ？」"
    call gl(1,"TCMM0031|TCMM0031")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa139"
    見里 "「海……でも用意してないですよ」"
    太一 "「俺が用意してあるんで。ささ、参りましょう」"
    call gl(1,"TCMM0005|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa140"
    見里 "「でも……日曜日までに放送局を……」"
    太一 "「助っ人を呼んでありますので」"
    call gl(0,"bgcc0008")
    call gl(1,"TCHY0000|tchy000x")
    call vsp(0,1)
    call vsp(1,1)
    call gp(1,t=center)#x=180
    with Pixellate(300.0*2/1000.0,5)
    太一 "「というわけで、海に行ってくるんでしっかりよろしく」"
    call gl(1,"TCHY0001|tchy000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001you038"
    曜子 "「……私、太一と海に行ったことない」"
    太一 "「また今度ね」"
    太一 "「とりあえずこの暑い中、曜子ちゃんはたった一人で放送準備進めておいて。あ、こっち監視に来るのも禁止ね」"
    voice "vfCCD1001you039"
    曜子 "「……便利に使われる……」"
    call gl(0,"bgcc0000a")
    call vsp(0,1)
    call vsp(1,0)
    with Pixellate(300.0*2/1000.0,5)
    pause (500.0/1000.0)
    太一 "「似合ってますよ」"
    call gl(0,"bgcc0017")
    call vsp(0,1)
    with Dissolve(500.0/1000.0)
    "力無く先輩は首を振る。"
    voice "vfCCD1001msa141"
    見里 "「……わたしにはそうは思えません……」"
    太一 "「タオルで隠したらせっかくの魅力がダイナシです」"
    call gl(1,"TCMM0005d|TCMM000xad")
    call gp(1,t=center)#x=225
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa142"
    見里 "「痴女みたいなんですけど……」"
    太一 "「そんなことありません」"
    太一 "「先輩の貞淑な姿に、俺、すごく興奮してます」"
    call gl(1,"TCMM0004d|TCMM000xad")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa143"
    見里 "「興奮してるんじゃないですかっ」"
    太一 "「でも、似合う似合わないでいったらベストマッチですよ」"
    太一 "「エロい男百人に聞いたら、全員似合うって言うはずです」"
    call gl(1,"TCMM0001d|TCMM000xad")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa144"
    見里 "「エロくない男の人にもきいてくださいよ！」"
    太一 "「エロくない男などいない！」"
    "両腕を左右に振りきって、俺は叫んだ。"
    call gl(1,"TCMM0003d|TCMM000xad")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa145"
    見里 "「夢のない……」"
    voice "vfCCD1001msa146"
    見里 "「ああ、痴女です……恥ずかしい……」"
    "痴女です痴女ですと先輩は連呼した。"
    太一 "「恥ずかしがらないで。痴女だなんて、とんだ誤解だ」"
    太一 "「先輩は、はじめて着るエロ水着に異常興奮してしまっているだけなんです」"
    voice "vfCCD1001msa147"
    見里 "「それが痴女です、そしてあなたはアホです」"
    "ふむ。"
    太一 "「先輩が痴女、俺がアホ。似合いの二人」"
    call gl(1,"TCMM0005d|TCMM000xad")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa148"
    見里 "「だから痴女になったつもりは……」"
    太一 "「去年を思い出して、ビーチバレーといきましょう」"
    "今年は揺らしきる。"
    "胸＝ビーチバレー。"
    "この定理に、これっぽっちの間違いもない。"
    太一 "「それー」"
    call gl(1,"TCMM0005d|TCMM000xad")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa149"
    見里 "「ううう……」"
    太一 "「せやー」"
    voice "vfCCD1001msa150"
    見里 "「あっ、うあ……」"
    太一 "「先輩、どうして片手でレシーブするんですか？」"
    call gl(1,"TCMM0001d|TCMM000xad")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa151"
    見里 "「視線を感じるからです」"
    太一 "「ここには二人しかいないのに？」"
    call gl(1,"TCMM0001d|TCMM000xad")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa152"
    見里 "「残ったもう一人の視線です！」"
    "よし、両手を使わないとレシーブできない球を繰りだしてやる。"
    太一 "「えいっ、分裂魔球」"
    call gl(1,"TCMM0005d|TCMM000xad")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa153"
    見里 "「な、なんでっ！？」"
    voice "vfCCD1001msa154"
    見里 "「……あ、あ、もう！」"
    "先輩は両手を使った。"
    "たゆんっ"
    太一 "「おー」"
    "最高バランス美乳時間差上下運動。"
    call gl(1,"TCMM0001d|TCMM000xad")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa155"
    見里 "「目で犯されているような気がします……」"
    "鋭敏な人だ。"
    太一 "「ついアタックを打ちたくなる魔球」"
    call gl(1,"TCMM0004d|TCMM000xad")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa156"
    見里 "「ああっ、とてもアタックを打ちたい加減の好球！」"
    voice "vfCCD1001msa157"
    見里 "「もう、えーいっ！」"
    play se "SE031"
    with vpunch
    "ふるんっ"
    "完璧美乳マジカルローリング。"
    "今のはかなり上位ランクの思い出になった。"
    太一 "「お次は……」"
    call gl(1,"TCMM0005d|TCMM000xad")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa158"
    見里 "「もうやめてーっ！　普通のがいいんですーっ！」"
    "……このくらいにしておこう。"
    "……………………。"
    "のんびりとラリー。"
    太一 "「人となにかをするのは、楽しいですよね」"
    call gl(1,"TCMM0001d|TCMM000xad")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa159"
    見里 "「そりゃあなたは楽しいでしょうけど……」"
    太一 "「部活のことですよ」"
    call gl(1,"TCMM0000d|TCMM000xad")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa160"
    見里 "「……部活？」"
    太一 "「人がいなくなって、静かになって、もうほとんど何も残ってない」"
    太一 "「でも、楽しい」"
    太一 "「誰かと一緒になにかをするのは、楽しい」"
    太一 "「一人だったら、息が詰まるだけでしょ？」"
    voice "vfCCD1001msa161"
    見里 "「……はい」"
    太一 "「先輩は、退屈に思いませんか？」"
    call gl(1,"TCMM0003d|TCMM000xad")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa162"
    見里 "「……つまらなくはないです」"
    voice "vfCCD1001msa163"
    見里 "「けど……わたしは……」"
    太一 "「わたしは？」"
    voice "vfCCD1001msa164"
    見里 "「何も考えたくないんです」"
    "トス。"
    "ボールは高くあがり、狭い弧を描く。"
    太一 "「……なぜ」"
    "同じような球を返す。"
    voice "vfCCD1001msa165"
    見里 "「ただなにかをしているだけのものに、なれたらいいのに」"
    太一 "「ロボットみたいに？」"
    call gl(1,"TCMM0000d|TCMM000xad")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa166"
    見里 "「そうです」"
    太一 "「それは寂しいな」"
    call gl(1,"TCMM0001d|TCMM000xad")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa167"
    見里 "「……お気持ちはありがたい、ですけど」"
    太一 "「人間は、ロボットにはなれないんじゃないですか？」"
    見里 "「…………」"
    太一 "「楽しい時には、楽しむしかない、っと」"
    "ひときわ高くうちあげた。"
    call gl(1,"TCMM0003d|TCMM000xad")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa169"
    見里 "「そんな余裕、ありません……」"
    "肩が下がる。"
    "てん、とボールが落ちた。"
    stop bgm
    太一 "「先輩？」"
    "十も老けたような顔をして、"
    voice "vfCCD1001msa170"
    見里 "「これは報いなのかもしれないです」"
    voice "vfCCD1001msa171"
    見里 "「わたしの、したことに対する」"
    太一 "「……」"
    play bgm "bgm/bgm024.ogg"
    voice "vfCCD1001msa172"
    見里 "「青春したり遊んだりする資格、ないんですよね、本当は」"
    太一 "「……そんな重い罪を、先輩が？」"
    voice "vfCCD1001msa173"
    見里 "「そうですね……」"
    太一 "「そうは、思えないな」"
    call gl(1,"TCMM0000d|TCMM000xad")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa174"
    見里 "「え……？」"
    太一 "「みみ先輩程度の人に、そんな罪が犯せるなんて、思えないって言ったんです」"
    call gl(1,"TCMM0001d|TCMM000xad")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa175"
    見里 "「ぺけくん……人の事情を知らないくせに、そんなことを言うのは……よくないですよ。一度、体を許したからって……」"
    太一 "「だって先輩、逃げたがってるだけですから」"
    "歩いていって、ボールを拾う。"
    call gl(1,"TCMM0003d|TCMM000xad")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa176"
    見里 "「なにを……っ！」"
    太一 "「逃避のための部活だったんでしょ？」"
    太一 "「でもおかしいじゃないですか。世界はもう、こんな希薄になってしまってるのに」"
    太一 "「犯した罪も、後悔も、苦悩も……全部、人と一緒になくなってしまったのに」"
    太一 "「罪のなりたちも仕組みも、もうない」"
    太一 "「モラルというものは、限りなく０に近くなったんですよ？」"
    太一 "「先輩はそれを執拗に引きずってる」"
    "俺もだけど。"
    voice "vfCCD1001msa177"
    見里 "「……そういう考え方は……どうかと思います」"
    voice "vfCCD1001msa178"
    見里 "「心の傷は残るものでしょう？」"
    voice "vfCCD1001msa179"
    見里 "「……わたしは、ひどいことをしたんですから……」"
    太一 "「後悔していると？」"
    見里 "「…………」"
    太一 "「もし、その時に戻ったとして……先輩はより正しい選択ができるんですか？」"
    見里 "「…………」"
    太一 "「だったら、反省なんて意味がない」"
    太一 "「同じことが繰り返されるだけだ」"
    太一 "「であれば、先輩はそういうものなんです」"
    太一 "「……俺には、それがわかります」"
    見里 "「…………」"
    太一 "「事情は知りませんけどね」"
    太一 "「……先輩は、ただ逃避しているだけに見える」"
    太一 "「部活じゃなくてもいいんです。きっと」"
    太一 "「そこでずっと停滞してますか？」"
    太一 "「こういう言い方には抵抗があるでしょうけど、その罪深い自分を肯定してやるため、なにか手を講じないといけないんじゃないですか？」"
    call gl(1,"TCMM0001d|TCMM000xad")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa183"
    見里 "「それは……無理です」"
    call gl(1,"TCMM0003d|TCMM000xad")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa184"
    見里 "「もう絶対に、無理なんです」"
    太一 "「なぜ」"
    voice "vfCCD1001msa185"
    見里 "「人が、いないからです」"
    太一 "「じゃあどうするんです？」"
    voice "vfCCD1001msa186"
    見里 "「……そんなの……わかりません」"
    voice "vfCCD1001msa187"
    見里 "「わたしが聞きたいくらいですよ……」"
    "表情は沈潜したまま、消えている。"
    "澄んだ湖面が無表情であるように。"
    "底には煩悶が。"
    太一 "「先輩は、痛めつけて欲しいんです」"
    call gl(1,"TCMM0004d|TCMM000xad")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa188"
    見里 "「え……」"
    太一 "「罪深い自分を、罰して欲しいんじゃないですか？」"
    voice "vfCCD1001msa189"
    見里 "「そんな……ことは……」"
    "一歩距離を詰める。"
    "間近。"
    太一 "「そうしてあげましょうか？」"
    "自動化。"
    call gl(1,"TCMM0000d|TCMM000xad")
    call vsp(1,1)
    with dissolve
    見里 "「……」"
    太一 "「それで少しは楽になるかも知れないてすよ？」"
    call gl(1,"TCMM0003d|TCMM000xad")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa191"
    見里 "「そんなの……おかしいです……」"
    "先輩は戸惑う。"
    太一 "「こっちに来て下さい」"
    hide pic1
    with dissolve
    "手を取り、連れて行く。"
    "拒絶を処理するためのプロセスを挟まず。"
    "先輩も小さな悲鳴をあげたが、抵抗は見せなかった。"
    call gl(0,"bgcc0020")
    call vsp(0,1)
    with wipeleft
    "海の家の、縁側に座る。"
    call gl(1,"TCMM0001d|TCMM000xad")
    call gp(1,t=center)
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa192"
    見里 "「……なにをするんですか……？」"
    太一 "「有り体に申しましてナニをするんですよ」"
    "取り出す。"
    太一 "「舐めてください」"
    call gl(1,"TCMM0005d|TCMM000xad")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa193"
    見里 "「ひ……」"
    太一 "「日の光の下で見ると、違うでしょう？」"
    voice "vfCCD1001msa194"
    見里 "「…………舐めるって……」"
    太一 "「フェラチオですよ」"
    太一 "「さあ、はやく」"
    voice "vfCCD1001msa195"
    見里 "「男の子の……なめるなんて…………それにやり方が……よく……」"
    太一 "「アイスキャンデーをしゃぶる気持ちでやればいいんですよ」"
    太一 "「さあ、口に含んで」"
    "押しつける。"
    jump N_MISATOSCENE001
label MISATOSCENE001:
    play bgm "bgm/bgm024.ogg"
label N_MISATOSCENE001:
    call gl(0,"evcc0034")
    call vsp(0,1)
    call vsp(1,0)
    with Dissolve(500.0/1000.0)
    voice "vfCCD1001msa196"
    見里 "「……っ」"
    "咬合は弱く、守りは脆い。"
    "侵入していく。"
    voice "vfCCD1001msa197"
    見里 "「ん……んむぁ……ん……」"
    "先端だけを含ませて、ねぶらせる。"
    "奥に逃げる舌を追いかけたい衝動に駆られる。"
    "が、我慢する。"
    voice "vfCCD1001msa198"
    見里 "「んぅ、んん……んんん……しょっぱい……」"
    "先端の球体をなかば戻すように、言う。"
    太一 "「海につかったせいかな。それとも？」"
    太一 "「続けて。味がなくなるまで、よく舐めるんですよ」"
    voice "vfCCD1001msa199"
    見里 "「……んっ……んろ……れるン……ん、ん、んんん……」"
    "アイスキャンデーという単語がそうさせたのか。"
    "まだるい動きではあったが、舌の当て方は適切だ。"
    "ざらっと舐めあげられる。"
    "大きな刺激が走り、怒張する。"
    voice "vfCCD1001msa200"
    見里 "「ふぁ、そんな大きくしないでください……」"
    太一 "「無理です」"
    太一 "「さあ、続けて」"
    "腰を軽く押し込む。"
    "内部から頬を押され、まごつく先輩。"
    voice "vfCCD1001msa201"
    見里 "「ん、んんんっ、んむ……ん……」"
    太一 "「どんな感じですか？」"
    voice "vfCCD1001msa202"
    見里 "「あん……はっ……大きくて……のどに詰まって……くる、ひ……」"
    太一 "「では、舌も使ってください」"
    "接続詞の機能を無視する言い方で、さらなる奉仕を強いる。"
    voice "vfCCD1001msa203"
    見里 "「こ、こうですか？　……んっ、れるっ、れろ……」"
    太一 "「もっと情熱的にしないとだめです」"
    "具体的な方法を説明すると、先輩は耳まで赤くして、従った。"
    voice "vfCCD1001msa204"
    見里 "「んっ、んむ……んっ、れろろ……ちゅる……ねろぉ……ちゅ、んっ、んんんっ」"
    "頭を撫でる。"
    "そして残酷な問い。"
    太一 "「舐めてる気分はどうですか？」"
    voice "vfCCD1001msa205"
    見里 "「んくっ……んむっ、んっ、んっんっ……んふ、こ、これ、どんどんあつくなって……頭がぼんやりします」"
    "思考力が鈍磨しているのか、発言にためらいがない。"
    太一 "「吸引するようにもしてください」"
    voice "vfCCD1001msa206"
    見里 "「ん、んんんっ、ちゅ、ちゅる、ちゅうぅぅぅぅぅ……」"
    "頬をすぼめる。"
    "口内の粘膜が竿に張りつく。"
    "ただ吸うだけじゃ。"
    "抜ける直前まで頭部を導く。"
    "そして呑めるだけ含ませる。"
    "先輩はすぐ理解した。"
    太一 "「ん……そんな感じで」"
    voice "vfCCD1001msa207"
    見里 "「んっ、んむっ、ちゅ、れろっ……」"
    "ときたま舌も絡ませる。"
    太一 "「そう、いろいろ織り交ぜながら……うまいですよ」"
    voice "vfCCD1001msa208"
    見里 "「ふぁ、んっ、んむっ、れろろ……ちゅぅぅぅぅ―――っ、あ、また大きく……すごい、張ってる……」"
    voice "vfCCD1001msa209"
    見里 "「頬張りきれません……んむっ……ちゅる、ちゅ……はぁはぁ」"
    太一 "「じゃ、そのおっぱいを使ったらどうです？」"
    voice "vfCCD1001msa210"
    見里 "「む、胸で？」"
    "理解できない様子。"
    太一 "「挟み込んで、先端だけ舐めるんです」"
    太一 "「そのくらいサイズがあればできるでしょう？」"
    voice "vfCCD1001msa211"
    見里 "「は、恥ずかしい……」"
    太一 "「やるんですよ、みみ先輩」"
    "強めに言う。"
    太一 "「その胸は誰のものですか？」"
    voice "vfCCD1001msa212"
    見里 "「あ、ああ……ぺけくんのものです……」"
    太一 "「じゃどう使おうが俺の勝手です」"
    voice "vfCCD1001msa213"
    見里 "「使うだなんて……ん……んるっ、あはん、ン……んんんん……んんん……」"
    "余計な発言を封じるため、口に栓をする。"
    太一 "「ほら、挟んで」"
    voice "vfCCD1001msa214"
    見里 "「あ、ああ……あつっ……こ、こう？」"
    太一 "「もっと強く」"
    voice "vfCCD1001msa215"
    見里 "「はい……んっ……あ、さきっぽが……ちゅ、ちゅ……」"
    太一 "「涎、いっぱいつけるようにして、ぬるぬるにしてくださいよ」"
    voice "vfCCD1001msa216"
    見里 "「は、はい……ん、んる……れるる……ちゅ、ちゅ……んん、んっ、ふぁん……」"
    voice "vfCCD1001msa217"
    見里 "「ぬろっ、ん、んんんんっ、ん、ちゅるん……ふぁ、はぁはぁ……苦いのが……出てきてます……」"
    太一 "「気持ちいいってことです」"
    voice "vfCCD1001msa218"
    見里 "「……あぁぁ……んむ……ちゅるっ、ちゅ、ちゅ……ちゅくっ、れろれろ……ちゅうぅぅぅぅぅぅぅぅぅっ！」"
    "なんだろう、積極的だ。"
    "罰して欲しい人というのは、そういうものか？"
    "官能に焙られて沸騰した唾液。"
    "胸が潤びるほどに垂れる。"
    voice "vfCCD1001msa219"
    見里 "「や……わたしのつばで……わたしの胸……どろどろに……」"
    太一 "「先輩のおっぱいじゃないでしょ？」"
    voice "vfCCD1001msa220"
    見里 "「あ……あなたの、です……」"
    太一 "「俺のおっぱいを、もっとドロドロにしてください」"
    voice "vfCCD1001msa221"
    見里 "「あ、あぁぁ……んうぅ～、んふっ、ん……んんん～…………」"
    "いっそう情熱的に尽くす。"
    "乳房の間に、官能の熱がこもる。"
    太一 "「汗かいてきましたね。胸の合間、いい感じですよ」"
    voice "vfCCD1001msa222"
    見里 "「そんな……いい感じだなんて……恥ずかしい……」"
    太一 "「さらさらしてるようで、むにむにしてて。俺は好きです」"
    voice "vfCCD1001msa223"
    見里 "「ん、ちゅるる……ちゅうぅ、んっ、あっ、はぁはぁ、んむむ……」"
    "『好き』と言った瞬間、強くむしゃぶりついてきた。"
    "甘噛みに近い。"
    太一 "「ん……男は、さきっぽが感じるんです」"
    voice "vfCCD1001msa224"
    見里 "「……あ、じゃあ……れるっ……んんんんんん～」"
    "鈴口を、舌先がこじあけた。"
    "先端に割り入る舌。"
    voice "vfCCD1001msa225"
    見里 "「……ん、ここにも、わたしのつばを入れますね……」"
    太一 "「すぐ出てきちゃいますけどね……」"
    voice "vfCCD1001msa226"
    見里 "「ん、じゅぷ……んん……んんんんん、んっ、あんっ、ふぅん……」"
    voice "vfCCD1001msa227"
    見里 "「はぁぁ……胸、すごい……とけそうです」"
    太一 "「つばと汗でドロドロですね」"
    太一 "「まるで、性器みたい」"
    "忘れかけていた羞恥を浮き彫りにされ、先輩は声を震わせる。"
    voice "vfCCD1001msa228"
    見里 "「な……ひどい……んん、ちゅぷ……」"
    voice "vfCCD1001msa229"
    見里 "「んっんっんっ、ん～、ちゅ、あふっ……んむっ……んんん、んんんん」"
    "だがすぐに没頭。"
    太一 "「先輩の乳首、しこってますよ」"
    "それを引き戻す。"
    voice "vfCCD1001msa230"
    見里 "「は、はい……乳首、コリコリしてます……」"
    太一 "「どうしてですか？」"
    voice "vfCCD1001msa231"
    見里 "「……それは……これが……」"
    太一 "「パイズリって言うんですよ」"
    voice "vfCCD1001msa232"
    見里 "「パ、パイズリが……気持ちいいから……んちゅ、ちゅる……あん……口の中で、跳ねる……すごい……」"
    太一 "「それだけで感じちゃったんですか？」"
    voice "vfCCD1001msa233"
    見里 "「あと……ぺけくんの……おちん○ん、かたくて熱いから……んっ……」"
    太一 "「じゃ、俺のもイカせてくださいよ」"
    voice "vfCCD1001msa234"
    見里 "「……あ……胸で……？」"
    太一 "「しごきながら、強く吸って」"
    voice "vfCCD1001msa235"
    見里 "「……あ……わかりました……ん、んんん……ちゅ、ちゅ、んっんっんっ……ちゅうぅぅぅ……」"
    "素直。"
    太一 "「そう、すぐでも出ますからね、吸い続けて」"
    voice "vfCCD1001msa236"
    見里 "「あっ、んむ、んむ……あん……んっ……ん、ふぅ……んむっ」"
    voice "vfCCD1001msa237"
    見里 "「ちゅ、ちゅるっ……れろれろ……んっ、あっ……んんんんんんんんっ！」"
    voice "vfCCD1001msa238"
    見里 "「ふぁ、あん……んっんっんっんっ、んー、んんんんっ、ちゅ、ちゅうっっ……ん～～～、んんんんんん～～～～～～～～～～～っっっ！」"
    "高まった。"
    "俺は射精した。"
    call gl(0,"evcc0034a")
    call gl(5,"bgcc0000e")
    call vsp(5,1)
    with dissolve
    call vsp(0,1)
    call vsp(5,0)
    with Dissolve(500.0/1000.0)
    voice "vfCCD1001msa239"
    見里 "「んんんんんんっ！？」"
    "肉体的な快楽以上に、先輩の口内に出しているという事実に背筋が震える。"
    "尿道を通過する精液が、塊となって噴き出ていく。"
    "先輩の口に、先輩の口に。"
    "甘い声の出所。"
    "俺の精液で、汚す。"
    voice "vfCCD1001msa240"
    見里 "「……ん……あふぁ……あ……んく…………んっ……あっ？」"
    "射精途中で抜く。"
    "他の場所も汚したい。"
    "顔と乳房に、押し出されるトコロテンのような精液をかける。"
    太一 "「は……」"
    "適度に汚れて、きれいな先輩。"
    "精液臭い先輩。"
    "……いい。"
    太一 "「精液、口の中にたまってますか？」"
    voice "vfCCD1001msa241"
    見里 "「ん……んん……」"
    "頷く。"
    太一 "「舌でかきまわして、よく味わって」"
    voice "vfCCD1001msa242"
    見里 "「…………ん……ん……んんん……」"
    太一 "「飲んで」"
    voice "vfCCD1001msa243"
    見里 "「……んく……こくん……」"
    "飲み終わると、大きく吐息を落とした。"
    voice "vfCCD1001msa244"
    見里 "「あ……胸にも……すごい量……」"
    太一 "「ええ、たくさん出ましたから」"
    "乳首にまで絡む。"
    太一 "「顔に出されたご感想は？」"
    voice "vfCCD1001msa245"
    見里 "「…………す、すごい、においです……」"
    太一 "「あ、ちょっと残ってた」"
    voice "vfCCD1001msa246"
    見里 "「えっ？」"
    "括約筋を締めると、最後の一滴が飛び出た。"
    voice "vfCCD1001msa247"
    見里 "「きゃっ？」"
    "それは先輩の鼻先にへばりついた。"
    voice "vfCCD1001msa248"
    見里 "「……あん、わたしの顔……どろどろに……」"
    if not _in_replay:
        jump N_MISATOSCENE101
    return
label N_MISATOSCENE101:
    "ずっとこのままにしておきたい気持ち。"
    "撮影の用意を怠ったことが悔やまれた。"
    太一 "「……さ、顔を洗って……続き、しましょ」"
    voice "vfCCD1001msa249"
    見里 "「まだ……できるんですか……これ？」"
    voice "vfCCD1001msa250"
    見里 "「あのときは……一回だけで……」"
    太一 "「はじめてだから、優しくしたんですよ」"
    太一 "「でも、今日はもうちょっと無茶しますけど」"
    太一 "「……だって、そうして欲しいんでしょ？」"
    "耳元に囁く。"
    voice "vfCCD1001msa251"
    見里 "「あ……そんな……」"
    "水筒の水をかけて、精液を流す。"
    太一 "「立って、またがってください」"
    "先輩はのろのろと身を立てた。"
    jump N_MISATOSCENE002
label MISATOSCENE002:
    play bgm "bgm/bgm024.ogg"
label N_MISATOSCENE002:
    call gl(0,"evcc0035")
    call vsp(0,1)
    with Dissolve(500.0/1000.0)
    "抱きかかえ、挿入する瞬間、二人の呼吸が止まった。"
    "ぬるっと入る。"
    "同時に息を吐いた。"
    "繋がった一瞬、えもいわれぬ征服感に身を焙られる。"
    "知っている人とセックスをする。"
    "とりわけ親しい友人や仲間と。"
    "麻薬めいて甘美な体験。"
    "自分の周辺にいる、全ての好ましい相手と繋がることで、俺は莫大な糧を得る。"
    太一 "「入りましたね」"
    "耳を舐めながら、小声で告げる。"
    voice "vfCCD1001msa252"
    見里 "「……あ……は、はい……奥まで……すごく……」"
    太一 "「どうすごいんです？」"
    voice "vfCCD1001msa253"
    見里 "「は……おなかの中で、かたちが……わかる感じです……」"
    太一 "「へえ、立派な性感があるんだ。先輩の体、すごくエッチってことですね」"
    voice "vfCCD1001msa254"
    見里 "「な……！」"
    太一 "「そんなよく感じられるんだから、よく発達してるんですよ。セックスの能力が」"
    voice "vfCCD1001msa255"
    見里 "「……しりません……」"
    太一 "「それもすぐわかることですね」"
    voice "vfCCD1001msa256"
    見里 "「え……きゃあっ！？」"
    "突き上げる。"
    voice "vfCCD1001msa257"
    見里 "「んんんっ、んっ、あ……いきな、りぃ……」"
    "思うようには動けない。"
    "腕の力で強引に揺する。"
    voice "vfCCD1001msa258"
    見里 "「あ、あっ、あうん、はあ、あ……」"
    voice "vfCCD1001msa259"
    見里 "「こ、これ……深い……深すぎて……つらい、ですぅ……はあん、ひあっ」"
    太一 "「じゃー、今日はこれでずっとしましょ」"
    "耳に舌を入れる。"
    voice "vfCCD1001msa260"
    見里 "「はああっ……そ、そんなあ……あっ、ああ、ひあっ……あうん、ああ……」"
    太一 "「胸のクッション、気持ちいいな」"
    "小突くごとに、乳房が俺の胸板で押しつぶされた。"
    voice "vfCCD1001msa261"
    見里 "「あ……あう、おっ、んっ、あああ、んっ、あっ、ゆ、揺すらないでぇっ！」"
    太一 "「揺すらなかったら気持ちよくないですよ」"
    voice "vfCCD1001msa262"
    見里 "「はああ……は……あ……ああ、ひっ！　ひふんっ……そ、んなぁ……ずっと、こんなのされたら……きつ、いい……」"
    "ぴったりと奥まで入っているせいか、先輩はつらそうだ。"
    太一 "「ちょっと感じ変えてみたりして」"
    "先輩のお尻をよじるようにして、片方の壁をひっかいてみる。"
    voice "vfCCD1001msa263"
    見里 "「んんんんんっ！　……ひ、ひゃ、ひゃふっ……おなかの中……きついぃぃ……」"
    太一 "「はは……」"
    "気持ちいい。"
    "摩擦の感触は少なく、直接的な刺激はないが。"
    "しがみついてくる先輩の体の重み。"
    "しなって密着してくる上体。乳房。"
    "渾然となって征服感を持続させてくれる。"
    voice "vfCCD1001msa264"
    見里 "「ん、んんん、あっ、おうん、おぁぁ……ひゃあ、だめっ……我慢、できない……ん……お、お願い……ちょっと……」"
    太一 "「え？」"
    voice "vfCCD1001msa265"
    見里 "「ト、トイレに……行かせてください……」"
    太一 "「トイレ？　おしっこですか？」"
    voice "vfCCD1001msa266"
    見里 "「……は、はい……かきまわされてたら……急に」"
    "膀胱をしげきしすぎたのかな？"
    太一 "「わかりました」"
    voice "vfCCD1001msa267"
    見里 "「ご、ごめんなさい……」"
    "先輩は肩に手を置いて、身を持ち上げようとする。"
    "抜こうと。"
    "逃れようと。"
    "急に気が変わる。"
    太一 "「やっぱだめ」"
    voice "vfCCD1001msa268"
    見里 "「え……きゃあっ！」"
    "手を外されて、先輩は落ちた。"
    "派手な水音。"
    voice "vfCCD1001msa269"
    見里 "「ひぎ、ぎぃぃ……っ……あっ……んぐ……」"
    "支えを失って、自ら串刺しになった。"
    "どうして？という顔で俺を見る。"
    "今の一撃で、瞳がすっかり潤んでいた。"
    太一 "「やっぱり今やめるのいやなんで……」"
    太一 "「ここでおもらししてください」"
    "一瞬、先輩は理解しなかった。"
    "ぴたりと停止。"
    voice "vfCCD1001msa270"
    見里 "「あ、あぁぁぁぁ……だ、だめですよ……そんなの……お願いですから……行かせて……」"
    "じたばたと。"
    太一 "「どうせ海ですし、いいんじゃないですか？」"
    "抱きしめて、腕の中で暴れられる感触を楽しむ。"
    voice "vfCCD1001msa271"
    見里 "「こんなところでなんて……無理、だめっ」"
    太一 "「じゃあ、俺のこと振り払えたら行っていいですよ」"
    "ぎゅっと抱く。"
    voice "vfCCD1001msa272"
    見里 "「そんな……いじわる、です……できっこない……」"
    太一 "「じゃお、ここでもらしちゃいます？」"
    voice "vfCCD1001msa273"
    見里 "「……あ、あああ……」"
    "逡巡。"
    voice "vfCCD1001msa274"
    見里 "「んっ……んん……は、はぁ……抜いて……行かせて……」"
    "再び暴れ出す。けど力は弱い。"
    "本気で払う気はないけど、なんとか態度で説得しようという意図がほの見える。"
    "もちろん俺の気は変わらない。"
    太一 "「……じゃ五秒だけ」"
    "腕の力を抜く。"
    "先輩がおそるおそる動く。"
    "尻をつかんで腰に引き寄せる。"
    "結合が深まった。"
    voice "vfCCD1001msa275"
    見里 "「んんんんんんっ！」"
    太一 "「はい、どーぞ」"
    "また力を抜く。"
    voice "vfCCB1101msa076"
    見里 "「……」"
    "動き出すと、乳首をつまんで捻る。"
    "そんなことを何度も繰り返す。"
    "クリトリスをつねったり、アヌスをつついたり、脇腹をくすぐったり。"
    "邪魔をしまくる。"
    voice "vfCCD1001msa276"
    見里 "「……はんっ、あ、あああ……あん……ま、またぁ！　んぎっ」"
    "最後の力を振り絞って立ち上がろうとするところを、Ｗ乳首捻りで撃墜すると、先輩はもうぐったりと虚脱して動けなくなった。"
    "腰を捻って、快楽を与える。"
    voice "vfCCD1001msa277"
    見里 "「あ……あああ……だめぇ、ぐるぐるまわさないでぇ……おしっこ、すぐ出ちゃいますっ！」"
    "やめない。"
    "追い込む。"
    太一 "「こんなエッチな体をしてる人が、おもらしなんてするはずないですよ」"
    "言うと、先輩はすすり泣いた。"
    "泣きながらあごを持ち上げて、喘いだ。"
    voice "vfCCD1001msa278"
    見里 "「ふぁあああんっ、あんっ、あっん……だめっ、だ……んん……んん」"
    "身をよじって、抜こうとする。"
    "腰をつかんで引き戻す。密着。"
    voice "vfCCD1001msa279"
    見里 "「は、はあああ―――ッッッ、ん……んん……やだ……本当に……もう……」"
    "身を震わせた。"
    voice "vfCCD1001msa280"
    見里 "「……た、たすけて……行かせて……おもらしいやなの……」"
    太一 "「平気ですってば」"
    "ナニが平気なのか、俺もよくわからない。"
    "ただ夢中になって身を揺すった。"
    "先輩は木の葉になって翻弄された。"
    voice "vfCCD1001msa281"
    見里 "「そんな……だめです……いけない、です、んっ……んんんっ、あぅんっ……」"
    voice "vfCCD1001msa282"
    見里 "「ううっ、うあっ、んっく……んっ、やっ、やぁぁ……あつい……ゆるんじゃう……このままされたら……ゆるんで、もれちゃうっ！？」"
    太一 "「～」"
    voice "vfCCD1001msa283"
    見里 "「んんん……んあっ、ごめんなさい、もう許して、本当にだめなんです……やっ、あああっ！」"
    "反応が変わる。"
    "四肢がひきつれて、異様な痙攣を見せた。"
    voice "vfCCD1001msa284"
    見里 "「あ、あん、あんあんっ、んあ、くぅぅ……やぁ、細かく動かないで……痺れちゃう……おっ、おっ……おあっ、ああ……ああああああっ……」"
    "悲鳴なんだか哀訴なんだか。"
    "ひっきりなしに、嬌声が紡がれていく。"
    voice "vfCCD1001msa285"
    見里 "「き、きく……これ、きくぅ！　あ……ああっ……がっ……ひふっ！」"
    太一 "「先輩」"
    "宮澄見里という、結び目がほどける。"
    "崩壊する様が、俺を駆り立てた。"
    voice "vfCCD1001msa286"
    見里 "「ひぎっ、あう……あひ、ひゃ……ふぁ、ひいッ、あっ、ひあっ、あっ、あうっ！」"
    "小刻みな動き。"
    "そして深い打ち込み。"
    voice "vfCCD1001msa287"
    見里 "「くっ……」"
    "緩急をつければ、自由自在に声をあげさせることができる。"
    "お尻の穴に、指を入れた。"
    voice "vfCCD1001msa288"
    見里 "「んぎッ、あ……ああ……っん～～～～～～～～～～～～～ッッッ！？」"
    "斜めに絞り上げる感覚で、膣がねじれる。"
    "収縮した。"
    "同時に、"
    voice "vfCCD1001msa289"
    見里 "「は、ああああぁぁぁぁぁぁ……ああぁぁぁ……ぁぁぁぁぁぁ……いやあぁぁぁぁぁぁぁぁ……」"
    "先輩は失禁した。"
    "粗相しつつ、軽く達していた。"
    太一 "「はは、下半身熱いや。びちょびちょ」"
    voice "vfCCD1001msa290"
    見里 "「いやぁぁ……いやぁぁ……」"
    太一 "「泣かないでよ、先輩」"
    "涙を舐める。"
    "塩辛い。"
    太一 "「このまま続けてあげますから」"
    voice "vfCCD1001msa291"
    見里 "「……ふぁ……ぇあ？」"
    "放心した顔が、愛おしい。"
    "ゆっくりと、腰の律動を再開させた。"
    voice "vfCCD1001msa292"
    見里 "「あ゛っ……んぐっ……だめ、ですっ……」"
    voice "vfCCD1001msa293"
    見里 "「うああっ、はっ、はんっ……だめ、だめだめ……すぐ、だめぇぇっ！」"
    太一 "「じゃゆっくり動かしてあげます」"
    太一 "「ほら、ゆーるゆーる」"
    voice "vfCCD1001msa294"
    見里 "「ううう……おぉっ……」"
    "背中を引っかかれる。"
    "気にならない。"
    voice "vfCCD1001msa295"
    見里 "「はっ、はっ、はっ……んっ……あぁ……あんっ、ん……あぁぁぁ……」"
    "ゆっくり動き続けると、とろけるよう顔を見せた。"
    voice "vfCCD1001msa296"
    見里 "「うぅ、んっ、あん、あぁん……だめよぉ……ひうぅ……こんなっ、こんなぁ……」"
    太一 "「何されてるかわかります？」"
    voice "vfCCD1001msa297"
    見里 "「ああ、はっ……おなかの中、まんべんなくっ、擦られて、ます」"
    太一 "「そうそう」"
    太一 "「で、先輩の弱点も見つけました」"
    "発達したそこを、先端でごりごり削ってやる。"
    voice "vfCCD1001msa298"
    見里 "「……ひゃっっっ！！」"
    "呼吸が止まった。"
    "同じ箇所を削り続けた。"
    voice "vfCCD1001msa299"
    見里 "「おおっ……おふっ……きゃ、んっ、っ～～～～～～～～っっ！」"
    "先輩はあっさり達した。"
    太一 "「あはは、可愛い」"
    太一 "「続けざまに行きますよ」"
    voice "vfCCD1001msa300"
    見里 "「んぎっ……おうっ……おっ……んんん……んん……ご、ごめんなさい！」"
    "謝った。"
    "何に対しての謝罪かは謎。"
    太一 "「許しませんよ」"
    "同じ箇所を責め続けた。"
    voice "vfCCD1001msa301"
    見里 "「ごめんなさい、ごめんなさいっごめんなさいごめんなさいっ……あぐっ……ごめんなさっ……ん゛っ！！」"
    "腰に絡めた脚を、ばたばたと暴れさせる。"
    太一 "「だめですー。ほーら、大きく削りますよー。ワンツーワンツー」"
    voice "vfCCD1001msa302"
    見里 "「……んんんんんんんっ！！　だめーっ！　許し、て、えぇぇぇっ……」"
    "続けざまの絶頂。"
    "……に到達する直前で、責めをやめる。"
    "愛には焦らしも必要。"
    voice "vfCCD1001msa303"
    見里 "「あ？　……はぁ……はっ……んくっ……」"
    "しがみついたまま、荒い息。"
    "首筋や顔にキスをしても、反応がない。"
    太一 "「どうですか？」"
    voice "vfCCD1001msa304"
    見里 "「あん、ん、ん、んっ……あぁぁ……もう、なにもわかりません……」"
    太一 "「先輩……」"
    太一 "「もっと感じてもいいんですよ」"
    "また弱点を擦る。"
    voice "vfCCD1001msa305"
    見里 "「うあああ～っ、そんなっ……わたしっ……すごいこと、され、てッ……んんんんんんんんんんんっ！？」"
    "俺の方も、いよいよ終わりが近づく。"
    "腰にじんわりとした熱量が、わだかまっていた。"
    voice "vfCCD1001msa306"
    見里 "「んぎっ、あっ、ひ、ひゃあっ！　……ふぁぁぁ、あっ、あうう、あん、あんあんっ……はぁんっ！！」"
    voice "vfCCD1001msa307"
    見里 "「やぁ、これすごい、すごいっ、ひゃ、あっ、すごい……き、きくぅぅ～～～～～～っ！！」"
    voice "vfCCD1001msa308"
    見里 "「んんっ、あんっ、だめだめ、だめですっ、だめ…………」"
    "不規則な呼気。"
    "身体の反応も、四肢ごとにちぐはぐになっている。"
    voice "vfCCD1001msa309"
    見里 "「……あ…………やだ……」"
    voice "vfCCD1001msa310"
    見里 "「ん……あ……やだ、ため……なんか……来て……」"
    太一 "「イクって言うんですよ」"
    "耳に唇を寄せ、そう命じた。"
    voice "vfCCD1001msa312"
    見里 "「イ、イクっ、イキますっ、イ……イク……イ……きゃ……きゃあ！」"
    "内部を思い切り擂る。"
    "例の弱い部分だけを。"
    voice "vfCCD1001msa313"
    見里 "「いやぁ、だめぇぇ！！　あっ、イ、イクゥゥゥーーーーーーーーーーーーーーーーっ！！！！」"
    "腕の中で跳ねる肉感。"
    "抱きしめて、肌ごと味わう。"
    "少し遅れて、こちらも達した。"
    "先輩の声が掠れて消えても、精は噴出を続けていた。"
    if not _in_replay:
        jump N_MISATOSCENE102
    return
label N_MISATOSCENE102:
    stop bgm
    call gl(0,"bgcc0000d")
    call vsp(0,1)
    with Dissolve(500.0/1000.0)
    "……………………。"
    play bgm "bgm/bgm020.ogg"
    call gl(0,"bgcc0017")
    call vsp(0,1)
    with Dissolve(500.0/1000.0)
    voice "vfCCD1001msa314"
    見里 "「……これで……許されるんですか？」"
    "ブラウスのボタンをとめて、先輩は言った。"
    "ひどく沈んでいる。"
    "原因は……いじわるしたから、ではないだろう。"
    "彼女は知っているだけだ。"
    "そぐわない罰を受けても、罪は解決しないことを。"
    "いや、そもそも―――"
    voice "vfCCD1001msa315"
    見里 "「わたしは……これで……許されるんですか……？」"
    太一 "「罪は決して許されませんよ」"
    "海を眺めつつ、砂を蹴る。"
    "透き通った砂子が扇状に舞った。"
    voice "vfCCD1001msa316"
    見里 "「じゃあ……どうしようも、ないんですね……」"
    "短くない沈黙を挟んで、陰気な声。"
    太一 "「……」"
    "俺がもう少しマシな人間なら、励ますこともできた。"
    "己の思索に対し、誠実さのない論拠をうちたてて。"
    "けど俺にはできない。"
    "どうしようもない。"
    "まさにそれこそが真実だと、確信していたから。"
    "沈黙が意図を伝えた。"
    voice "vfCCD1001msa317"
    見里 "「……うう……ううううう……」"
    "慰める術はなかった。"
    "少し調子に乗りすぎた。"
    "先輩をいじめてしまった。"
    "ハッピーエンドに。"
    "美しいトラウマのカウンセリングを、するはずだったのに。"
    太一 "「……難しい」"
    call gl(0,"bgcc0000d")
    call vsp(0,1)
    with Dissolve(500.0/1000.0)
    "顔を覆う。"
    "失敗したことを、悟った。"
    stop bgm
    pause (500.0/1000.0)
    pause (500.0/1000.0)
    play se "SE001"
    play bgm "bgm/bgm018.ogg"
    call gl(0,"bgcc0007s")
    call vsp(0,1)
    with Pixellate(300.0*2/1000.0,5)
    call gl(1,"TCMM0002s|TCMM000x")
    call gp(1,t=center)#x=225
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa318"
    見里 "「親しき仲にはあだ名あり、です」"
    太一 "「はあ……」"
    call gl(1,"TCMM0000s|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa319"
    見里 "「お互いニックネームを決めましょう」"
    "ニュアンスとしてはペットネーム、という気もした。"
    "ペットみたいに気に入られているのは間違いない。"
    "どちらにしても。"
    "彼女の笑顔の下に、親愛があるかどうかはわからないのだ。"
    "俺はまだ警戒をしていた。"
    太一 "「じゃ……先輩」"
    "考えた結果、提案できたのはその呼び方だった。"
    call gl(1,"TCMM0021s|TCMM0021")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa320"
    見里 "「先輩だけじゃ区別つかないでしょう？」"
    太一 "「……合理的じゃないですね。宮澄先輩でいいじゃないですか」"
    call gl(1,"TCMM0031s|TCMM0031")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa321"
    見里 "「うーん、黒須太一……ですから」"
    "聞いてなかった。"
    voice "vfCCD1001msa322"
    見里 "「たいち君、はつまらないですよね」"
    太一 "「つまらないって、あんた……人の名前を……」"
    "何げに辛辣だな。"
    voice "vfCCD1001msa323"
    見里 "「……黒須……黒須……ばってん……ばってん！」"
    太一 "「……却下させてくださいお願いします」"
    "頭を下げた。"
    call gl(1,"TCMM0005s|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa324"
    見里 "「えー！」"
    太一 "「そんな方言みたいな呼ばれ方はゴメンです」"
    call gl(1,"TCMM0031s|TCMM0031")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa325"
    見里 "「じゃあ……ばつ……ぺけ……」"
    call gl(1,"TCMM0000s|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa326"
    見里 "「……ぺけくん？」"
    太一 "「また間抜けな響きを醸しだしてくれましたね」"
    call gl(1,"TCMM0002s|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa327"
    見里 "「あ、でもいい感じ。わたしは気に入りましたよ」"
    "ぺけだと？"
    "基本の思考に『×』があるのだった。"
    太一 "「よく考えたら……ペケってダメって意味じゃないですか」"
    call gl(1,"TCMM0000s|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa328"
    見里 "「Ｘという意味もあったりなかったり」"
    call gl(1,"TCMM0002s|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa329"
    見里 "「ぺけという記号は、交差しあってるんです」"
    太一 "「……支え合ってさえいない」"
    "寒々しかった。"
    太一 "「すれ違いって意味にしか受け取れないんですけど……」"
    call gl(1,"TCMM0000s|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa330"
    見里 "「世間から弾かれたわたしたちも、いつか誰かと交差できるといいなという願いがこめられてます」"
    太一 "「……偽善的だ」"
    "そして無理矢理だ。"
    call gl(1,"TCMM0002s|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa331"
    見里 "「さあ、こっちは決まりましたよ。そっちの番です」"
    "決まってしまった。"
    太一 "「はぁ」"
    "こうなったら、つきあうしかないのだった。"
    "彼女との短いつきあいでも、よく理解できていた。"
    太一 "「じゃ……雌奴隷」"
    call gl(1,"TCMM0031s|TCMM0031")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa332"
    見里 "「この法治国家日本で奴隷なんていませんし」"
    太一 "「愛奴隷」"
    call gl(1,"TCMM0005s|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa333"
    見里 "「どう違うんですか！」"
    太一 "「雌豚先輩？」"
    call gl(1,"TCMM0001s|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa334"
    見里 "「……そのめすぶたの後輩になるんですよ、いいんですか？」"
    太一 "「おっぱいさん」"
    call gl(1,"TCMM0005s|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa335"
    見里 "「そ、そういう目でわたしの胸を……」"
    太一 "「搾乳隷奴」"
    call gl(1,"TCMM0001s|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa336"
    見里 "「ひっくり返す意味がわかりませんです……」"
    call gl(1,"TCMM0021s|TCMM0021")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa337"
    見里 "「おっぱいから離れませんか？」"
    "注文が多い。"
    太一 "「……エロメガネさん」"
    call gl(1,"TCMM0006s|TCMM0006")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa338"
    見里 "「拒否」"
    太一 "「全部拒絶じゃないですか！」"
    "叫ぶ。"
    "クールな俺だけでは、対応できない。"
    voice "vfCCD1001msa339"
    見里 "「あなたがヘンなのばっかり提案するからです！」"
    太一 "「じゃメガネ女！」"
    call gl(1,"TCMM0031s|TCMM0031")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa340"
    見里 "「見たままですね。捻りませんか？」"
    "人をばってん呼ばわりしかけた女のセリフとしては完璧すぎた。"
    太一 "「……みみ」"
    call gl(1,"TCMM0021s|TCMM0021")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa341"
    見里 "「それは？」"
    太一 "「みやすみみさとで、みみ」"
    call gl(1,"TCMM0002s|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa342"
    見里 "「ああ、いい感じ」"
    "ふわりとほころぶ。"
    "頭悪く見えるほど、ゆるい笑い方。"
    "けど。"
    "……妙に、面映ゆい。"
    太一 "「三つあるな。みみみ、か」"
    太一 "「美々美とか書きますか？」"
    call gl(1,"TCMM0005s|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa343"
    見里 "「アホヒロインみたいな響きに……」"
    "俺みたいな危険人物に声をかけるアホな人ではあった。"
    "アホすぎて……ついつい、優しくしたくなる。"
    太一 "「……みみ先輩」"
    call gl(1,"TCMM0002s|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa344"
    見里 "「あ、それそれ、それがいいです」"
    太一 "「そうですか」"
    call gl(1,"TCMM0000s|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa345"
    見里 "「じゃこれで二人は先輩と後輩ですよ」"
    "小指を出す。"
    "違うと思ったが、応じた。指切り。"
    太一 "「どうせ、親しい名前をつけてこき使うんでしょ。奴隷制度とどう違うんだか」"
    call gl(1,"TCMM0002s|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa346"
    見里 "「愛ある強制労働ですよ」"
    call gl(1,"TCMM0000s|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa347"
    見里 "「あ、もちろん友愛の方ですよ？」"
    太一 "「どちらなりと」"
    "肩をすくめた。"
    stop se
    call gl(0,"bgcc0007a")
    call vsp(0,1)
    call vsp(1,0)
    with Pixellate(300.0*2/1000.0,5)
    "夕方。"
    "一端別れたはずの先輩が、そこにいた。"
    "曜子ちゃんはいない。"
    "みみ先輩が戻ってきて、交代する形で立ち去ったのだろう。"
    太一 "「……」"
    call gl(1,"TCMM0003b|TCMM000x")
    call gp(1,t=center)#x=225
    call vsp(1,1)
    with dissolve
    見里 "「……」"
    "目線が交錯する。"
    "それは結びつかない。"
    "ほんの一時、軸を重ねただけでしかない。"
    "俺は佇立し、先輩はのろのろと動いている。"
    "無言のまま、二人はいた。"
    "まだ、先輩をアンテナから引きはがすことはできそうにない。"
    "心に踏み込まないといけないのに。"
    "……自分からそうするのが……恐い。"
    stop bgm
    call gl(0,"bgcc0000d")
    call vsp(0,1)
    call vsp(1,0)
    with Dissolve(500.0/1000.0)
    call gl(0,"bgcc0003")
    call vsp(0,1)
    with Dissolve(500.0/1000.0)
    "土曜日だ。"
    "……あと一日。"
    "あと一日なんだ。"
    play bgm "bgm/bgm007.ogg"
    call gl(0,"bgcc0007f")
    call vsp(0,1)
    with wipeleft
    "早めに来た。"
    "見ると、作業はほとんど終わっていた。"
    "曜子ちゃんを投入したのは大きかった。"
    "あとは待つだけだ。"
    "土曜日。"
    "ヤツは高確率で、やってくる。"
    "しかし。"
    太一 "「……来ないな」"
    "いつまで待っても、扉が開く様子はない。"
    "やがて昼が過ぎ、先輩がやってきた。"
    call gl(1,"TCMM0000|TCMM000x")
    call gp(1,t=center)#x=225
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa349"
    見里 "「あ……ぺけ、くん……」"
    太一 "「みみ先輩……」"
    call gl(1,"TCMM0005|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa350"
    見里 "「……あのっ、実は……」"
    太一 "「は、はい？」"
    call gl(1,"TCMM0003|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCD1001msa351"
    見里 "「あ……いえ……なんでも、ありません」"
    hide pic1
    with dissolve
    太一 "「あ、ちょっと」"
    "伸ばした手。力無く降下させた。"
    "行っちゃった。"
    "まあ、作業はほぼ完成しているし、いいんだけど。"
    太一 "「……失敗したかな」"
    "手詰まり。"
    "いっそ、強制的に祠に連れて行って―――"
    太一 "「ダメだ」"
    "それでは、お互い得るものがない。"
    "俺が満足するだけではダメだし、先輩だけが満ち足りる展開もダメ。"
    "傲慢かも知れないが。"
    "交換しなければならない。"
    "触れあった心の感触さえ、あれば。"
    "だとしても、どうやってうまくまとめよう。"
    "わからない。"
    stop bgm
    call gl(0,"bgcc0007a")
    call vsp(0,1)
    with ImageDissolve("sys/EFMSK_22_MSK.bmp",time=1)
    "ずっと待っていた。"
    "先輩も友貴も現れない。"
    太一 "「……」"
    "無駄に時間が過ぎていく。"
    "考える。"
    "友貴があの場に来なかったということは、手伝う気がなかったということだ。"
    call gl(0,"bgcc0000d")
    call vsp(0,1)
    with Dissolve(500.0/1000.0)
    "つまり―――"
    pause (500.0/1000.0)
    pause (1000.0/1000.0)
    play se "SE098"
    "妙な物音がする。"
    play se "SE098"
    "断続的な。"
    "……不安にさせる音。"
    "破壊の音。"
    太一 "「！？」"
    "跳ね起きる。"
    play bgm "bgm/bgm019.ogg"
    call gl(0,"bgcc0007b")
    call vsp(0,1)
    with wipeleft
    "プレハブを出た。"
    "友貴がいた。"
    友貴 "「……」"
    "大きな工業用のペンチを持っている。"
    "自転車のチェーンを切断できるアレだ。"
    "アンテナが壊されていた。"
    太一 "「…………」"
    "特に配線と機器。"
    "徹底的だった。"
    "怒りに任せて叩き壊したものじゃない。"
    "合理的な思考と工具によって、的確に機能が殺された。"
    "冷静な破壊。"
    太一 "「……」"
    "俺の存在には気づいていない。"
    "模型を組み立てる熱心さが、周囲への警戒を鈍くしている。"
    "無言で近寄り、殴った。"
    call gl(1,"TCST0001c|TCST0001")
    call gp(1,t=center)#x=190
    call vsp(1,1)
    with dissolve
    voice "vmCCD1001yki054"
    友貴 "「……っ！？」"
    "瞳が俺を認めると、瞬時に驚きは消える。"
    "病的な友貴を見る。"
    太一 "「…………」"
    call gl(2,"bgcc0000c")
    call gp(2,t=left)
    play se "SE003"
    call vsp(2,1)
    with dissolve
    with vpunch
    "言葉もなく、殴り合う。"
    "冷静なケンカ……というより格闘。"
    "五分後。"
    "勝ったのは俺だった。"
    "腱に爆弾を抱えた友貴に、もともと勝ちはない。"
    voice "vmCCD1001yki055"
    友貴 "「はぁ、はぁ、はぁ……」"
    "観念したように無抵抗の友貴に馬乗りになって、話しかける。"
    太一 "「遊紗ちゃん、覚えてるか？」"
    voice "vmCCD1001yki056"
    友貴 "「……え？」"
    太一 "「近所の遊紗ちゃんだよ。俺になついてた。海にも来たろ？」"
    voice "vmCCD1001yki057"
    友貴 "「ああ……あの子か……」"
    太一 "「俺はあの子に接する時、いつも着飾ってた」"
    voice "vmCCD1001yki058"
    友貴 "「？」"
    太一 "「いい面ばかりを見せて、演技して、愛想良くしてた」"
    太一 "「結果、遊紗ちゃんは俺になついてくれたよ。俺も大好きだった」"
    voice "vmCCD1001yki059"
    友貴 "「……それが……なに」"
    太一 "「これは裏切りじゃないのか？」"
    voice "vmCCD1001yki060"
    友貴 "「……！？」"
    "本当の自分を知りながら、隠そうとする行為。"
    "騙そうとする行為。"
    "素直な自分を見せるという一般的善行と、相反する。"
    "だからイケナイこと。"
    太一 "「結局、バレてさ」"
    太一 "「俺、あの子に嫌われちゃったんだ」"
    "痛烈な断絶をもって、俺の実験は終わった。"
    太一 "「仕方ないことだけどな。だましてたんだから」"
    太一 "「……おまえも裏切りを憎んでいるものなのか？」"
    太一 "「裏切りが許せないタイプか？」"
    voice "vmCCD1001yki061"
    友貴 "「……だって、姉貴は……」"
    "喘ぐように言う。"
    "言葉は続かない。"
    "落ち着きのない様子で、俺を見返している。"
    太一 "「俺は遊紗ちゃんを裏切った。そして断絶した」"
    太一 "「けどあの子が俺を嫌った理由は、醜さを隠していたからじゃない」"
    太一 "「まさにその醜さが、彼女の生理に拒絶されたんだ」"
    太一 "「おまえが許せないのは、ほんとうに裏切りなのかな？」"
    友貴 "「……」"
    太一 "「おまえたちのやってること、二人ともそっくりに見えるよ」"
    太一 "「部活をでっちあげて、そこに没頭して」"
    太一 "「人がいなくなったんだぞ？」"
    太一 "「心の世界が、なくなったんだぞ？」"
    "希薄になった。"
    太一 "「それがどういうことなのか……友貴にはわからないか？」"
    太一 "「正しいことばかりが人間じゃない」"
    太一 "「認めるか、認めないか。それだけだ」"
    太一 "「認めるんだったら、その気持ちに理由をつけるなよ」"
    太一 "「そしたら、好きって気持ちに嘘つかなくてすむじゃん……」"
    call gl(0,"bgcc0007b")
    call gl(1,"TCST0004c|TCST0004")
    call vsp(0,1)
    call vsp(1,1)
    call vsp(2,0)
    with Dissolve(500.0/1000.0)
    voice "vmCCD1001yki063"
    友貴 "「……僕だって、そう言いたかった……」"
    太一 "「え？」"
    voice "vmCCD1001yki064"
    友貴 "「正しいことばかりが人間じゃないって、姉貴に！」"
    stop bgm
    太一 "「……何があったんだか、俺は知らないから」"
    voice "vmCCD1001yki065"
    友貴 "「姉貴は家族を売ったんだ！」"
    voice "vmCCD1001yki066"
    友貴 "「父親を、警察に！」"
    太一 "「……警察？」"
    call gl(1,"TCST0000c|TCST0000")
    call vsp(1,1)
    with dissolve
    voice "vmCCD1001yki067"
    友貴 "「姉貴は、離婚した父親の方に行ったんだ」"
    voice "vmCCD1001yki068"
    友貴 "「僕は母さんに」"
    voice "vmCCD1001yki069"
    友貴 "「そうしろって、父さんも言うから」"
    play bgm "bgm/bgm009.ogg"
    call gl(1,"TCST0004c|TCST0004")
    call vsp(1,1)
    with dissolve
    voice "vmCCD1001yki070"
    友貴 "「……父さんは、大変だったんだ！」"
    voice "vmCCD1001yki071"
    友貴 "「母さんへの慰謝料とか、学費とか……」"
    voice "vmCCD1001yki072"
    友貴 "「仕方なかったんだ！」"
    "ピンと来た。"
    太一 "「……何かの犯罪、に？　金銭目当てで？」"
    call gl(1,"TCST0000c|TCST0000")
    call vsp(1,1)
    with dissolve
    voice "vmCCD1001yki073"
    友貴 "「金銭じゃない！　ただ生きるための……必要な……」"
    call gl(1,"TCST0004c|TCST0004")
    call vsp(1,1)
    with dissolve
    voice "vmCCD1001yki074"
    友貴 "「けど、姉貴は許さなかった」"
    voice "vmCCD1001yki075"
    友貴 "「姉貴が通報したんだ！」"
    "先輩が。"
    "規律。"
    "ルール。"
    "人々が互いに取り交わした。"
    voice "vmCCD1001yki076"
    友貴 "「……家族でも、売り飛ばすんだ……姉貴は……」"
    call gl(1,"TCST0000c|TCST0000")
    call vsp(1,1)
    with dissolve 
    voice "vmCCD1001yki077"
    友貴 "「あの人はなぁ……自分の価値観を人に押しつけたがるんだよ……」"
    voice "vmCCD1001yki078"
    友貴 "「それが受け入れられなかったら、すぐおかしくなる」"
    voice "vmCCD1001yki079"
    友貴 "「わざと怪我してみたり……つきまとったり……」"
    太一 "「怪我って、自傷症状の？」"
    call gl(1,"TCST0004c|TCST0004")
    call vsp(1,1)
    with dissolve
    voice "vmCCD1001yki080"
    友貴 "「あれは、姉貴の攻撃なんだよ！」"
    voice "vmCCD1001yki081"
    友貴 "「自分を攻撃することで、人を攻撃してるんだ！」"
    voice "vmCCD1001yki082"
    友貴 "「この部活だってそうさ、ああやって一人でこもって、嫌みたらしく没頭して……あれは僕らに対する攻撃なんだよ」"
    "符合する。"
    "部活＝攻撃。"
    "ああ、そういうことか。"
    call gl(1,"TCST0006c|TCST0004")
    call vsp(1,1)
    with dissolve
    voice "vmCCD1001yki083"
    友貴 "「すぐに……おかしくなるぞ……怪我をするぞ」"
    voice "vmCCD1001yki084"
    友貴 "「わざと怪我をする」"
    "友貴の双眼に暗い炎。"
    "敵意の篝火。"
    "友貴は笑っている。"
    "人を憎むことは、心地よい。"
    voice "vmCCD1001yki085"
    友貴 "「怪我をしやすいように振る舞う」"
    call gl(1,"TCST0000c|TCST0000")
    call vsp(1,1)
    with dissolve
    voice "vmCCD1001yki086"
    友貴 "「……僕が、どうしてバスケをできなくなったと思う？」"
    太一 "「なんだって？」"
    call gl(1,"TCST0004c|TCST0004")
    call vsp(1,1)
    with dissolve
    voice "vmCCD1001yki087"
    友貴 "「姉貴をかばったんだよ。これはその後遺症なんだ」"
    "憎々しげに吐き捨てた。"
    call gl(1,"TCST0006c|TCST0004")
    call vsp(1,1)
    with dissolve
    voice "vmCCD1001yki088"
    友貴 "「……その姉貴の価値観は……規則だよ、知ってるだろ？」"
    voice "vmCCD1001yki089"
    友貴 "「あの人はなぁ……人に自分を認めさせたいだけだ……自分の居心地のいい場所にしたいだけなんだよ……」"
    太一 "「本当に嫌いなのか？」"
    voice "vmCCD1001yki090"
    友貴 "「……大嫌いだね」"
    call gl(2,"TCMM0000c|TCMM000x")
    call gp(2,t=center)#x=225
    call vsp(1,0)
    call vsp(2,1)
    with Dissolve(500.0/1000.0)
    voice "vfCCD1001msa352"
    見里 "「友貴……」"
    "俺の背後、先輩は立っていた。"
    "友貴も気づいた。"
    "言葉は止まらない。"
    "ぶちまける気なのだ。"
    call gl(1,"TCST0004c|TCST0004")
    call vsp(1,1)
    call vsp(2,0)
    with Dissolve(500.0/1000.0)
    voice "vmCCD1001yki091"
    友貴 "「……どんなに親しくしても駄目さ、太一」"
    voice "vmCCD1001yki092"
    友貴 "「何かのはずみで、姉貴のルールから外れたらおしまいだ」"
    voice "vmCCD1001yki093"
    友貴 "「……姉貴には、絆なんていらない」"
    voice "vfCCD1001msa353"
    見里 "「友貴……わたし……」"
    call gl(1,"TCST0000c|TCST0000")
    call vsp(1,1)
    with dissolve
    voice "vmCCD1001yki094"
    友貴 "「人がいなくなって、もう守るべきルールなんてどこにもないから」"
    call gl(1,"TCST0006c|TCST0004")
    call vsp(1,1)
    with dissolve
    voice "vmCCD1001yki095"
    友貴 "「だから……もう、姉貴は、このまま破滅するしかないよ」"
    "世界は心のパッチワーク。"
    "ルールはその残骸。"
    voice "vfCCD1001msa354"
    見里 "「……あのね……友貴……わたしね……」"
    "涙声が俺を透過していく。友貴に向かって。"
    voice "vmCCD1001yki096"
    友貴 "「うるさいよ！」"
    "友貴は俺に向かって叫ぶ。"
    "俺は便利な壁だった。"
    voice "vmCCD1001yki097"
    友貴 "「姉さんは、裏切り者だ！」"
    voice "vmCCD1001yki098"
    友貴 "「父さんが、あんたをかばったんだろ？」"
    voice "vmCCD1001yki099"
    友貴 "「母さんが、あんたを捨てようとしたのを、かばったんじゃないか！」"
    voice "vmCCD1001yki100"
    友貴 "「その父親を裏切るって……なに？　ぜんぜん、わからない……意味わかんない」"
    "泣いている。"
    "見ろ。"
    "おまえは、姉貴が心底好きなんじゃないか。"
    "しかし泣き顔は先輩からは見えない。"
    call gl(1,"TCST0000c|TCST0000")
    call vsp(1,1)
    with dissolve
    voice "vmCCD1001yki101"
    友貴 "「父さん、これから長い時間、償わないといけなくなる……」"
    voice "vmCCD1001yki102"
    友貴 "「そんなに……自分が大切なら……」"
    voice "vmCCD1001yki103"
    友貴 "「一人で生きていけばいいんだよぉ」"
    太一 "「……」"
    "最後の言葉には、感銘を受けた。"
    "そうだよな。"
    "心はエゴなんだよな。"
    "エゴって、心の境界線を塗りつぶす力なんだよな。"
    "世界を埋め尽くす、無数のヘックス。そのひとつひとつが、心だ。"
    "同じ大きさでなければならない。"
    "同じ形でなければならない。"
    "そうでないと……外圧を一身に受けることになる。"
    "たいていが、耐えられない。"
    "耐えられたとき。"
    "そいつはひねもす周囲を傷つけ破壊し貪り尽くす怪物となる。"
    "隣にいる誰かの面積を押し縮めながら。"
    call gl(2,"TCMM0000c|TCMM000x")
    call vsp(1,0)
    call vsp(2,1)
    call gp(2,t=center)#x=225
    with Dissolve(500.0/1000.0)
    voice "vfCCD1001msa355"
    見里 "「あ……友貴……だから……」"
    "温和に笑おうとして、半笑い。"
    voice "vfCCD1001msa356"
    見里 "「わたし……」"
    "半笑い。"
    voice "vfCCD1001msa357"
    見里 "「あ……っ」"
    hide pic2
    with dissolve
    "無理がたたって、口元がひきつれる。"
    play se "SE035"
    "俺が意識を引き戻すのと、先輩が地面を蹴る音は、同時だった。"
    "逃げた。"
    "立ち上がる。"
    "友貴に手を差し伸べた。"
    太一 "「つまり先輩はお父さんを官憲に売ったわけだな」"
    call gl(1,"TCST0000c|TCST0000")
    call vsp(1,1)
    call gp(1,t=center)#x=190
    call vsp(1,1)
    with dissolve
    voice "vmCCD1001yki104"
    友貴 "「ああ、そうだよ」"
    voice "vmCCD1001yki105"
    友貴 "「二回、崩壊させたんだ」"
    "平坦な口調。"
    "無関心な素振りをもって、糾弾する態度。"
    call gl(1,"TCST0004c|TCST0004")
    call vsp(1,1)
    with dissolve
    voice "vmCCD1001yki106"
    友貴 "「一回目は……僕の怪我だ。これで……母さんはいやになったんだ」"
    "同性からだと、自分勝手なだけの娘に見えたのか。"
    voice "vmCCD1001yki107"
    友貴 "「父さんは最後までかばってた」"
    voice "vmCCD1001yki108"
    友貴 "「それで、僕らは二組にわかれた」"
    "数秒の空白を置き。"
    call gl(1,"TCST0000c|TCST0000")
    call vsp(1,1)
    with dissolve
    voice "vmCCD1001yki109"
    友貴 "「それでもよかった。母さんはノイローゼになってたから……」"
    "離れた方が良かった。"
    call gl(1,"TCST0004c|TCST0004")
    call vsp(1,1)
    with dissolve
    voice "vmCCD1001yki110"
    友貴 "「けど……あの人は、父親にも……」"
    太一 "「ああ……そうだな」"
    call gl(1,"TCST0000c|TCST0000")
    call vsp(1,1)
    with dissolve
    voice "vmCCD1001yki111"
    友貴 "「太一？」"
    太一 "「先輩の気持ち、よくわかるよ」"
    voice "vmCCD1001yki112"
    友貴 "「……え」"
    太一 "「おまえはけっこう健全だから……わからないだろうけど」"
    太一 "「意志とは関係ないんだ」"
    太一 "「俺たちは、自動的なんだよ」"
    call gl(1,"TCST0000c|TCST0000")
    call vsp(1,1)
    with dissolve
    voice "vmCCD1001yki113"
    友貴 "「じどうてき……って……言われても……」"
    太一 "「そういう状況が来たら、こう反応するしかない」"
    太一 "「決まってるんだよ」"
    太一 "「どんな愛があっても、絆があっても、関係ない」"
    太一 "「脳の真ん中あたりがそうさせるんだ」"
    太一 "「理性じゃ制御できない」"
    太一 "「だから……大好きなのに、壊してしまうことが……あるんだ」"
    "むしろ興味が向くほどに。"
    "刃になった指先で、触れたくなる。"
    太一 "「そしてそんな自分を、俺たちは大抵憎んでいる」"
    "友貴は無言だった。一分ばかり。"
    call gl(1,"TCST0001c|TCST0001")
    call vsp(1,1)
    with dissolve
    voice "vmCCD1001yki114"
    友貴 "「…………太一……も？」"
    太一 "「おまえ、俺が何者だと思ってるんだ？」"
    太一 "「偏差値８０オーバーの男だぞ？」"
    "小さく笑う。"
    call gl(1,"TCST0005c|TCST0004")
    call vsp(1,1)
    with dissolve
    voice "vmCCD1001yki115"
    友貴 "「だって太一は平気じゃん……うまくやってるじゃん……？」"
    太一 "「演技」"
    太一 "「全部、演技」"
    太一 "「俺、遊紗ちゃんのこと大好きだった」"
    太一 "「けど……俺、そんなあの子のこと、ずっといじめられてたあの子のこと……そうと知ってて……押し倒したことがある」"
    call gl(1,"TCST0001c|TCST0001")
    call vsp(1,1)
    with dissolve
    voice "vmCCD1001yki116"
    友貴 "「！」"
    太一 "「理性ではわかってる。いけないことだって。でも、我慢できない」"
    太一 "「本当に、制御できないんだ」"
    太一 "「忘れるな、友貴」"
    太一 "「群青にいる者は誰だって、傷つきながら誰かを傷つけている」"
    call gl(1,"TCST0004c|TCST0004")
    call vsp(1,1)
    with dissolve
    友貴 "「……………………」"
    "二人の間、風が通り抜けた。"
    "荒野を駆け抜ける、乾いた空気。"
    "肌寒さを感じさせる。"
    "俺から見る友貴は、凍えているようだ。"
    太一 "「おまえが先輩のこと、ほんとに嫌いならしょうがないんだけどさ」"
    太一 "「そのお父さん、たぶんみみ先輩のこと、許してるぞ」"
    call gl(1,"TCST0000c|TCST0000")
    call vsp(1,1)
    with dissolve
    voice "vmCCD1001yki118"
    友貴 "「……！」"
    太一 "「尊重しあうのが筋だけど……できないんだからしょうがないだろ？」"
    太一 "「人間関係と、利害を一緒にするからおかしくなる」"
    太一 "「ただ好きであればいい。違うか？」"
    太一 "「……一方通行でいいんだ。お父さんがそうしたように」"
    voice "vmCCD1001yki119"
    友貴 "「僕は……」"
    太一 "「ゆっくり考えろ」"
    太一 "「答えはおまえの中にしかないんだし」"
    太一 "「答えが出たら……明日の朝、山の社まで来いよ」"
    call gl(1,"TCST0004c|TCST0004")
    call vsp(1,1)
    with dissolve
    voice "vmCCD1001yki120"
    友貴 "「社……？」"
    太一 "「昼な。俺と先輩、そこにいる予定」"
    太一 "「あと、俺先輩とＨした」"
    "友貴は唖然とした。"
    太一 "「……」"
    "そのまま一分待ったが、殴りかかってくる様子はない。"
    "震える唇で、なにかを呟く。"
    "『そうか』と読めた。"
    "ほとんど聞こえなかった。"
    太一 "「……言いたいことがあるなら、明日の昼、社に来いよ」"
    "返事はない。"
    "複雑な顔の友貴を置いて、先輩を追った。"
    stop bgm
    call gl(0,"bgcc0008b")
    call vsp(0,1)
    call vsp(1,0)
    with wipeleft
    "屋上以外、どこに行くだろう？"
    "このパターンは、はじめてだ。"
    "……説得しないと。"
    "たとえ、自分の傷を見せることになっても―――"
    call gl(0,"bgcc0011c")
    call vsp(0,1)
    with wipeleft
    pause (500.0/1000.0)
    pause (500.0/1000.0)
    call gl(0,"bgcc0000c")
    call vsp(0,1)
    with wipeleft
    "先輩の家は、閉ざされていた。"
    太一 "「……もしもーし」"
    "ドアは施錠されている。"
    "解錠はできる。けど。"
    "感覚を研ぎ澄ます。"
    "貝殻のような家の中、先輩の小さな気配が感じ取れそうだった。"
    "下腹部にわだかまった熱量を意識する。"
    "弾けると制御不能になってしまう。"
    "迷う。"
    "思う。"
    "結局、帰る。"
    "夜は塞ぎ込む時間だ。"
    "傷ついた身を、闇に沈めて癒すのだ。"
    call gl(0,"bgcc0003e")
    call vsp(0,1)
    with wipeleft
    太一 "「静かだな……」"
    "窓から外に、声をかけた。"
    "もし先輩の攻略に失敗したら。"
    "……またやり直し。"
    "触れあう機会は増える。"
    "そんな弱さを、俺は自覚していた。"
    "頬を叩く。"
    太一 "「しっかりやれ」"
    "迅速に。"
    "致命的な思い出を、作ってしまう前に。"
    call gl(0,"bgcc0000d")
    call vsp(0,1)
    with Dissolve(500.0/1000.0)
    "ベッドに入り、ゆっくりと気を落ち着かせていく。"
    "殴り合いで、たかぶった心を静めるため。"
    "キャパシティの少ない理性を、冷却するため。"
    call gl(0,"bgcc0003")
    call vsp(0,1)
    with Dissolve(500.0/1000.0)
    太一 "「よし」"
    "一晩おいて、俺は平静だった。"
    太一 "「行くか」"
    call gl(0,"bgcc0007")
    call vsp(0,1)
    with Dissolve(500.0/1000.0)
    "一応、見に来る。"
    "……来ていないようだ。"
    "自宅にこもったままか。"
    call gl(0,"bgcc0005")
    call vsp(0,1)
    with Dissolve(500.0/1000.0)
    "先輩の家の前。"
    "雑草で心なしか荒れた庭。"
    "一週間でこうはならない。"
    "父親が不在になったあと、先輩は管理していなかったんだろう。"
    "なぜか？"
    "つらかったから。"
    call gl(0,"bgcc0000a")
    call vsp(0,1)
    with Dissolve(500.0/1000.0)
    "裏口にまわる。"
    "ここも施錠されていたが、古い型のディスクシリンダーだった。"
    "鍵穴にツールをさしこみ内部のタンブラーを移動させる。"
    "ほどなくカチリと音がした。"
    太一 "「お邪魔しまーす」"
    "驚かす目的ではないので、侵入したことを声高に告げた。"
    "靴を脱いで、室内に。"
    "一階にはそれらしき部屋はない。"
    "二階。"
    "部屋は二つだけだ。"
    "片方は空室。"
    "からっぽの本棚とベッドしかない。"
    "ということは。"
    play se "se051"
    太一 "「……来ちゃいました」"
    "声をかけた。"
    "場所は変わったけど、やることは一緒だ。"
    "俺が、先輩にまとわりつく。"
    "したいのはそれだけ。"
    call gl(0,"evcc0033")
    call vsp(0,1)
    with Dissolve(500.0/1000.0)
    voice "vfCCD1001msa358"
    見里 "「……何用です」"
    "返答があった。"
    太一 "「お話、したくて」"
    voice "vfCCD1001msa359"
    見里 "「帰って欲しいです」"
    太一 "「まあまあ」"
    voice "vfCCD1001msa360"
    見里 "「……黒須君」"
    "苗字。"
    太一 "「はい？」"
    voice "vfCCD1001msa361"
    見里 "「部活はもうおしまいです」"
    voice "vfCCD1001msa362"
    見里 "「好きに生きてくださいな」"
    "淡々と言う。"
    太一 "「……俺は、好きに生きてますよ」"
    太一 "「ある程度は、ですけど」"
    太一 "「先輩と話すのが、好きなんです」"
    太一 "「だから少しくらいは、いいでしょう？」"
    見里 "「…………」"
    太一 "「先輩とお父さんのこと、聞きました」"
    太一 "「なんというか……まあ一般的には、凄絶なんだろうなって思いました」"
    太一 "「友貴もそう思ってたみたいですし」"
    太一 "「外れたらごめんなさい」"
    太一 "「……でも先輩は、お父さんのこと無茶苦茶好きなんですね？」"
    "息を詰める気配。"
    voice "vfCCD1001msa365"
    見里 "「……どうして……そう思いますか」"
    "そしてレス。"
    "対話が成立しはじめる。"
    太一 "「先輩が規則の人だから」"
    太一 "「特に身近な人間に対して、気になる相手に対して、規範を求めるって」"
    太一 "「俺に声をかけたのだって、そうだったんでしょ？」"
    見里 "「……」"
    太一 "「その相手が、ルールを逸脱したとするなら……」"
    太一 "「告発するでしょう。俺たちなら」"
    play bgm "bgm/bgm021.ogg"
    見里 "「…………」"
    太一 "「好きだからいじめたい心理と似てるのかな」"
    太一 "「人間って、本質的に気になるか気にならないかだと思ってます」"
    太一 "「あとは全部後付の理由に過ぎないって」"
    voice "vfCCD1001msa368"
    見里 "「……わかんないです」"
    太一 "「好きなのと、関与したいというのは、別個なんですよね？」"
    太一 "「興味なかったら、接触しないはずですもん」"
    太一 "「普通は、好きになったら適切な距離でつきあうものですよ」"
    太一 "「でも、俺たちはちょっぴり壊れてるから」"
    太一 "「……そうしたくないって思ってても、壊したり傷つけたりしちゃうんですよね」"
    太一 "「それは好きって気持ちを否定するものじゃなく」"
    太一 "「むしろ、好きだから……自分を見て欲しいから」"
    太一 "「先輩は傷つけて欲しいんですよね、お父さんに」"
    太一 "「だから傷つけるようなことをする」"
    太一 "「それこそが、先輩とお父さんの交信だった」"
    太一 "「どうです、この推理？」"
    voice "vfCCD1001msa369"
    見里 "「……全然、ハズレです」"
    voice "vfCCD1001msa370"
    見里 "「探偵は廃業した方がいいですよ」"
    太一 "「嘘ばっかり」"
    太一 "「どうして携帯を持ってるんです？」"
    voice "vfCCD1001msa371"
    見里 "「……癖です」"
    太一 "「連絡を待ってるんでしょ？」"
    太一 "「お父さんから」"
    voice "vfCCD1001msa372"
    見里 "「……ええ」"
    太一 "「もしかかってきたら、何を話します？」"
    太一 "「……横領はよくないとか？」"
    voice "vfCCD1001msa373"
    見里 "「違います！」"
    "知っている。"
    voice "vfCCD1001msa374"
    見里 "「わたしは……わたしはただ……！」"
    太一 "「ただ？」"
    voice "vfCCD1001msa375"
    見里 "「謝りたいんです……謝りたいだけなんです……」"
    太一 "「ごめんなさいって？」"
    voice "vfCCD1001msa376"
    見里 "「ごめんなさいって……」"
    太一 "「犯罪はいけないことですよね。先輩は正しいことをした。なのに謝りたい？」"
    voice "vfCCD1001msa377"
    見里 "「……だって……だって、だって……っ！」"
    voice "vfCCD1001msa378"
    見里 "「知らなければよかった……気づかなければ……そうしたら、ずっと幸せでいられたのに……っ！」"
    voice "vfCCD1001msa379"
    見里 "「ええ、好きでしたよ！　わたしをかばってくれたお父さんも、お母さんも、友貴も……みんな……っ！」"
    voice "vfCCD1001msa380"
    見里 "「……けど、もう謝ることもできない……」"
    voice "vfCCD1001msa381"
    見里 "「ぶちこわしにしたまま……なくなってしまって……！」"
    voice "vfCCD1001msa382"
    見里 "「なにもしたくなかった。何も考えたくなかった。どうしようもないことですから」"
    voice "vfCCD1001msa383"
    見里 "「けどもう……限界です」"
    voice "vfCCD1001msa384"
    見里 "「死にたい……今、すごく……自分を壊したいですよ……でも」"
    voice "vfCCD1001msa385"
    見里 "「死ぬの、恐い……」"
    voice "vfCCD1001msa386"
    見里 "「一人で死にたくない……」"
    voice "vfCCD1001msa387"
    見里 "「だから……なんか……」"
    voice "vfCCD1001msa388"
    見里 "「気持ち悪い……生きてるのが……気が狂いそう」"
    太一 "「……俺が、楽にしてあげましょうか？」"
    voice "vfCCD1001msa389"
    見里 "「え……？」"
    太一 "「俺が先輩を楽にしてあげます」"
    voice "vfCCD1001msa390"
    見里 "「……なに、言ってる……？」"
    太一 "「先輩にとっての規則にあたるものが、俺にもあるんですよ」"
    太一 "「なんとなく気づいてるんじゃないのかな、あなたは」"
    voice "vfCCD1001msa391"
    見里 "「……ぺけくんは……人を……」"
    太一 "「そう」"
    "ネコがじゃれるような、無邪気な衝動で。"
    voice "vfCCD1001msa392"
    見里 "「……わたしを、あなたが……？」"
    太一 "「優しくね」"
    "扉を隔てた戸惑い。"
    "体温さえ伝わらないのに、それが感じられた。"
    voice "vfCCD1001msa393"
    見里 "「……本当に？」"
    太一 "「ええ」"
    voice "vfCCD1001msa394"
    見里 "「……もしそれが本当なら……」"
    voice "vfCCD1001msa395"
    見里 "「わたし……もう……」"
    voice "vfCCD1001msa396"
    見里 "「もう、ね……」"
    play se "SE072"
    call gl(0,"bgcc0000d")
    call vsp(0,1)
    with Dissolve(500.0/1000.0)
    "静かに、扉が開く。"
    stop bgm
    pause (500.0/1000.0)
    pause (500.0/1000.0)
    call gl(0,"bgcc0015")
    call vsp(0,1)
    with wipeleft
    "道中、二人は無言だった。"
    "会話する必要がないためだ。"
    太一 "「こっちです」"
    voice "vfCCD1001msa397"
    見里 "「はい……」"
    "たまに、そう声をかけて確認する。"
    "先輩は黙ってついてきた。"
    "時計を見る。"
    "ちょうど良い時間。"
    call gl(0,"bgcc0016")
    call vsp(0,1)
    with wipeleft
    extend "到着。"
    "交差点は、変わらずそこに在り続けた。"
    "立ちこめた霧に似ている。"
    太一 "「そういえば―――」"
    "関係ないことを話す。"
    "唐突にはじまった世間話。"
    "先輩は少し目を丸くして、曖昧に相づちを打った。"
    "緋色の到来を待つばかり。"
    "あと数分といったところまで、空疎な対話に費やす。"
    太一 "「おっと……そろそろ始めましょうか」"
    太一 "「こっちですよー」"
    "柔らかい手を取って、導く。"
    "指先が冷たい。"
    "恐いのかな？"
    "適当なあたりに立たせる。"
    太一 "「ここに立ってください」"
    call gl(0,"evcc0061")
    call vsp(0,1)
    call vsp(1,0)
    with Dissolve(500.0/1000.0)
    voice "vfCCD1001msa398"
    見里 "「あの……」"
    太一 "「ん？」"
    voice "vfCCD1001msa399"
    見里 "「こんなことを言ったら……いけないのかもしれないですけど」"
    voice "vfCCD1001msa400"
    見里 "「こわいんです……」"
    太一 "「そうでしょうね」"
    "それっきり、先輩は言葉を発することができない。"
    "異常な状況に、混乱している。"
    太一 "「心を抱えて、人の世界で生きていかないといけないわけですから」"
    voice "vfCCD1001msa401"
    見里 "「……人の？」"
    voice "vfCCD1001msa402"
    見里 "「人なんて……もう……」"
    太一 "「しっ」"
    "口を押さえた。"
    "ここに誰かがやって来ている。"
    "草をかきわけ、地面に足を叩きつけ。"
    "……走って。"
    "そいつは、走ってはいけないはずなのに、走って。"
    "悠長に話している暇はないな。"
    "最後に先輩をじろじろと眺める。"
    "記憶に刷り込むために。"
    call gl(5,"bgcc0000e")
    call vsp(5,1)
    with dissolve
    hide pic5
    with dissolve
    "世界が分解されはじめた。"
    call gl(0,"evcc0061a")
    call vsp(0,1)
    call vsp(1,0)
    with Dissolve(500.0/1000.0)
    "大気の密度が変質し、空が暮れる。"
    play bgm "bgm/bgm023.ogg"
    voice "vfCCD1001msa403"
    見里 "「……夕日？」"
    "後ずさる。"
    太一 "「部活、誘ってくれてありがとう、先輩」"
    "ぴくん、と身をかたくした。"
    太一 "「あれがあなたの、価値観の押しつけだったとしても……俺は嬉しかった」"
    太一 "「俺に興味を示してくれて、ありがとう」"
    太一 "「一生、忘れません。あなたのこと、あなたの言葉、あなたの記憶」"
    voice "vfCCD1001msa404"
    見里 "「……痛く、しないでくださいね」"
    "震える肩。震える声。"
    "抱きしめたくなる。"
    "俺は踵を返し、先輩と距離をあけた。"
    voice "vfCCB1101msa001"
    見里 "「……え？」"
    太一 "「ごめん……楽にしてあげるってのは、嘘です」"
    太一 "「苦しみながら生きていくんです、先輩は」"
    太一 "「そこに俺はいないけど……」"
    "肩の前で、小さく手を振る。"
    太一 "「ばいばい先輩、楽しかった」"
    call gl(0,"bgcc0000d")
    call vsp(0,1)
    call vsp(1,0)
    with Dissolve(500.0/1000.0)
    "先輩がなにか言おうとした瞬間、俺は目を閉じた。"
    call gl(0,"bgcc0016c")
    call vsp(0,1)
    with Dissolve(500.0/1000.0)
    "そして開くと、もう彼女はいなくなっていた。"
    "ごっそりと、疲労を感じた。"
    "胸がえぐられたようだ。"
    太一 "「きつ……」"
    "しかし涙は出ない。"
    "中途半端な、この気持ち。"
    "我ながら嫌になる。"
    "そこに友貴がやってきた。"
    #\■友貴　真剣な表情
    call gl(1,"TCST0004b|TCST0004")
    call gp(1,t=center)#x=190
    call vsp(1,1)
    with dissolve
    voice "vmCCD1001yki121"
    友貴 "「姉貴は……どこ？」"
    "いきなりだった。"
    "焦っていた。"
    "走ってきて、汗だくになっている。"
    太一 "「あっちだよ、あっち」"
    #\■友貴　真剣な表情
    call gl(1,"TCST0004b|TCST0004")
    call vsp(1,1)
    with dissolve
    voice "vmCCD1001yki122"
    友貴 "「……二人で、何してたの？」"
    太一 "「山菜をな、とっていた」"
    #\■友貴　通常
    call gl(1,"TCST0000b|TCST0000")
    call vsp(1,1)
    with dissolve
    voice "vmCCD1001yki123"
    友貴 "「……太一が連れ出したんだろ」"
    太一 "「そうだよ、急げ」"
    太一 "「大変なことになってるぞ、助けてやれよ」"
    "血相を変えた。"
    #\■友貴　真剣な表情
    call gl(1,"TCST0004b|TCST0004")
    call vsp(1,1)
    with dissolve
    voice "vmCCD1001yki124"
    友貴 "「どっち？」"
    太一 "「あっちあっち！」"
    #\■友貴　驚き
    call gl(1,"TCST0001b|TCST0001")
    call vsp(1,1)
    with dissolve
    voice "vmCCD1001yki125"
    友貴 "「いないんだけど……？」"
    "座標が、重なった。"
    太一 "「遊紗ちゃんにゴメンって伝えといてくれな」"
    voice "vmCCD1001yki126"
    友貴 "「は……？」"
    太一 "「グンナイ、シスコン」"
    太一 "「……インモラルに励めよ」"
    stop bgm
    call gl(0,"bgcc0000e")
    call vsp(0,1)
    call vsp(1,0)
    call vsp(2,0)
    with Dissolve(500.0/1000.0)
    "友貴、送還。"
    pause (2000.0/1000.0)
    pause (2000.0/1000.0)
    call gl(0,"bgcc0000b")
    call vsp(0,1)
    with Dissolve(500.0/1000.0)
    voice "vfCCD1001msa405"
    見里 "「……え……ぺけくん？」"
    voice "vfcca0028msa015"
    見里 "「…………」"
    voice "vfCCD1001msa406"
    見里 "「あのぅ？」"
    voice "vmCCD1001yki127"
    友貴 "「姉さん……」"
    voice "vfCCD1001msa407"
    見里 "「友貴？　どうして、ここに……」"
    voice "vmCCD1001yki128"
    友貴 "「話を、しよう」"
    play bgm "bgm/bgm001.ogg"
    voice "vmCCD1001yki129"
    友貴 "「話したいことが、あるから……」"
    voice "vfCCD1001msa408"
    見里 "「友貴……あなた」"
    play se "SE099"
    voice "vmCCD1001yki130"
    友貴 "「あ、あれ？」"
    voice "vmCCD1001yki131"
    友貴 "「ラジオが……」"
    voice "vfCCD1001msa409"
    見里 "「電波……が……入って？」"
    play se "se200"
    voice "vfCCD1001msa410"
    見里 "「あ……」"
    voice "vmCCD1001yki132"
    友貴 "「姉さんの携帯？」"
    voice "vfCCD1001msa411"
    見里 "「……鳴ってる……かかってきてる……」"
    voice "vmCCD1001yki133"
    友貴 "「誰から？」"
    voice "vfCCD1001msa412"
    見里 "「……お父さん……の、番号……」"
    voice "vmCCD1001yki134"
    友貴 "「それって……？」"
    voice "vfCCD1001msa413"
    見里 "「わからないけど」"
    voice "vfCCD1001msa414"
    見里 "「まるで……長い夢を見ていたみたい―――」"
    stop se
    play se "se201"
    voice "vfCCD1001msa415"
    見里 "「……もしもし？」"
    stop bgm
    stop se
    with dissolve
    call gl(0,"efcc0001")
    call vsp(0,1)
    with dissolve
    call gl(0,"efcc0002")
    call vsp(0,1)
    with dissolve
    call gl(0,"efcc0001")
    call vsp(0,1)
    with dissolve
    play se "SE016"
    call gl(0,"bgcc0000d")
    call vsp(0,1)
    with dissolve
    pause (3000.0/1000.0)
    pause (2000.0/1000.0)
    call gl(0,"bgcc0016")
    call vsp(0,1)
    with Dissolve(500.0/1000.0)
    太一 "「……ははは」"
    "やり遂げた。"
    "先輩と友貴は、もういない。"
    "二度と会うこともない。"
    "きつい。"
    "思い出すだけだ。"
    "なんともはや。"
    "祠によりかかって、目を閉じた。"
    "名状しがたい、奇妙な眩暈感に包まれる。"
    "ゆらゆらと世界が揺れている気がして、三半規管が錯覚を起こした。"
    "ずっと二人のことばかり、考え続けていた。"
    "薄れゆく意識。"
    "重く機能を停止する身体。"
    "一切が分解されて構成される過程を、ヒトの知覚力は観測することができない。"
    "たやすく分解される世界。"
    "いつ終わるとも知れない。"
    "そんな場所で、俺は、生きていく。"
    "闘いは、続く。"
    call gl(0,"bgcc0000d")
    call vsp(0,1)
    with Dissolve(500.0/1000.0)
    "また、来週―――"
    pause (1500.0/1000.0)
    pause (1500.0/1000.0)
    return