label ccd3003:
    play bgm "bgm/bgm018.ogg"
    call gl(0,"bgcc0003")
    call vsp(0,1)
    call vsp(1,0)
    call vsp(2,0)
    with wipeleft
    "目を覚ます。"
    "陽光が窓を貫いていた。"
    "熟睡していたらしい。夢一つ見なかった。"
    "時間は……７時。"
    "学校に行かねば。"
    call gl(0,"bgcc0008")
    call vsp(0,1)
    with wipeleft
    "廊下に霧が立っていた。"
    太一 "「よっ」"
    call gl(1,"TCSK0001|TCSK000x")
    call gp(1,t=center)#x=220
    call vsp(1,1)
    with dissolve
    voice "vfCCC3103kri000"
    霧 "「……先輩」"
    "表情が警戒色を帯びた。"
    "火曜日では、こんなものだろう。"
    "敵意に満ちた視線。"
    "俺は目を反らす。"
    "挑発的なことも口にしない。"
    "美希が出てきた。"
    call gl(2,"TCYM0000|TCYM0000")
    call gp(2,t=left)#x=0
    call gp(1,t=right)#x=340
    call vsp(2,1)
    call vsp(1,1)
    with Dissolve(500.0/1000.0)
    voice "vfCCC3103mki000"
    美希 "「おや、先輩」"
    call gl(2,"TCYM0003|TCYM0003")
    call vsp(2,1)
    with dissolve
    voice "vfCCC3103mki001"
    美希 "「昨日はごちそうさまでした」"
    voice "vfCCC3103mki002"
    美希 "「ほら、霧も」"
    call gl(1,"TCSK0002|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3103kri001"
    霧 "「……わたしは……」"
    call gl(2,"TCYM0000|TCYM0000")
    call vsp(2,1)
    with dissolve
    voice "vfCCC3103mki003"
    美希 "「食べたじゃない」"
    call gl(1,"TCSK0000|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3103kri002"
    霧 "「そうだけど……そうだけど」"
    "葛藤。"
    "プライドに依る。"
    太一 "「いーよいーよ、俺が作ったやつじゃないし」"
    voice "vfCCC3103mki004"
    美希 "「そーなんですか？」"
    太一 "「曜子ちゃん」"
    call gl(2,"TCYM0003|TCYM0003")
    call vsp(2,1)
    with dissolve
    voice "vfCCC3103mki005"
    美希 "「あー、先輩のコレモンの人ですね」"
    "小指を立てる。"
    太一 "「コレモンというか○○モンというか。便利なモンスターではあるな」"
    "版権的にやばいのだ。"
    太一 "「そーいうわけで、はい、朝食にどうぞ」"
    call gl(2,"TCYM0004|TCYM0002")
    call vsp(2,1)
    with dissolve
    voice "vfCCC3103mki006"
    美希 "「え……よろしいんですか？」"
    太一 "「いいよ。俺、サンドイッチってあまり好きじゃないから」"
    call gl(2,"TCYM0003|TCYM0003")
    call vsp(2,1)
    with dissolve
    voice "vfCCC3103mki007"
    美希 "「悪いですねぇ」"
    太一 "「大変だろ。お菓子とかばかりじゃ」"
    call gl(2,"TCYM0001|TCYM0000")
    call vsp(2,1)
    with dissolve
    voice "vfCCC3103mki008"
    美希 "「……はい」"
    "霧が割り込んでくる。"
    "挑戦的なイントネイションで、告げる。"
    call gl(1,"TCSK0001|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3103kri003"
    霧 "「何の目的があって、こんなことをするんですか？」"
    太一 "「……目的は、ある」"
    voice "vfCCC3103kri004"
    霧 "「それは？」"
    太一 "「……霧と、話がしたい」"
    call gl(1,"TCSK0000|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3103kri005"
    霧 "「わたしと？」"
    太一 "「ただ話にはふさわしい日がある。その時まではご機嫌とりだよ」"
    call gl(2,"TCYM0021|TCYM0021")
    call vsp(2,1)
    with dissolve
    voice "vfCCC3103mki009"
    美希 "「ふさわしい日って？」"
    太一 "「うん、ちょっとね」"
    call vsp(2,0)
    call vsp(1,0)
    with Dissolve(500.0/1000.0)
    "背を向けた。"
    voice "vfCCC3103kri006"
    霧 "「あ……」"
    voice "vfCCC3103mki010"
    美希 "「い、いただきます、先輩！」"
    "後方に向けて、手だけをひらひら振った。"
    stop bgm
    call gl(0,"bgcc0003")
    call vsp(0,1)
    with wipeleft
    "昼まで時間を潰す。"
    "余計な接触をして、未知の悲劇に見舞われるわけにはいかない。"
    "今の知識と経験を有する俺、固有の俺は、死ぬわけにはいかない。"
    call gl(0,"bgcc0011")
    call vsp(0,1)
    with wipeleft
    "昼、再び学校に。"
    play bgm "bgm/bgm003.ogg"
    call gl(0,"bgcc0006")
    call vsp(0,1)
    with wipeleft
    "ここで二人は弁当を食べている……はず。"
    "食べていなかったら出直し。また来週。"
    "何度でも繰り返すさ。"
    "そして―――"
    太一 "「……食い物ありませんか？」"
    call gl(1,"TCYM0000|TCYM0000")
    call gp(1,t=center)#x=180
    call vsp(1,1)
    with dissolve
    voice "vfCCC3104mki000"
    美希 "「ありますけど……」"
    太一 "「その弁当は？」"
    call gl(1,"TCYM0003|TCYM0003")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3104mki001"
    美希 "「霧が作ったんです」"
    太一 "「うわ、いいなあ」"
    call gl(2,"TCSK0002|TCSK000x")
    call vsp(2,1)
    call gp(1,t=left)#x=40
    call gp(2,t=right)#x=345
    with Dissolve(500.0/1000.0)
    voice "vfCCC0031bkri000"
    霧 "「……先輩の分はありません」"
    "きっぱり。"
    太一 "「かなり分量があるじゃないか」"
    call gl(1,"TCYM0000|TCYM0000")
    call vsp(1,1)
    with dissolve
    voice "vfCCC0031bmki002"
    美希 "「多いですよね」"
    "明らかに三人分はありそうだ。"
    voice "vfCCC0031bkri001"
    霧 "「しかしなぜか先輩のはないんです」"
    太一 "「……むぅ」"
    太一 "「じゃー物々交換しよう」"
    call gl(1,"TCYM0003|TCYM0003")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3104mki002"
    美希 "「トレードですか」"
    太一 "「あめ玉とグミキャンディー。手作り」"
    "二人の目の色が変わった。"
    call gl(1,"TCYM0001|TCYM0000")
    call vsp(1,1)
    with dissolve
    voice "vfCCC0031bmki004"
    美希 "「てづくり？」"
    太一 "「んー。曜子ちゃんがだけど」"
    太一 "「シュガー控えめ、美容健康にいいらしい。グミはこんにゃくだね。０カロリー」"
    call gl(1,"TCYM0004|TCYM0002")
    call gl(2,"TCSK0000|TCSK000x")
    call vsp(1,1)
    with dissolve
    call vsp(2,1)
    with dissolve
    voice "vfCCC0031bgoo000"
    二人 "「０カロリー！？」"
    call vsp(1,0)
    call vsp(2,0)
    with Dissolve(500.0/1000.0)
    "……………………。"
    太一 "「わーい」"
    "交換成立。"
    call gl(1,"TCYM0003|TCYM0003")
    call vsp(1,1)
    with dissolve
    voice "vfCCC0031bmki006"
    美希 "「ママの味がする……」"
    call gl(2,"TCSK0006|TCSK000x")
    call vsp(2,1)
    with dissolve
    voice "vfCCC0031bkri003"
    霧 "「するね」"
    voice "vfCCC0031bmki007"
    美希 "「ミルクだね」"
    voice "vfCCC0031bkri004"
    霧 "「だねー」"
    太一 "「ストーカーの味だけどね」"
    voice "vfCCC3104mki003"
    美希 "「やだ、ほっぺが……落ちそう……」"
    voice "vfCCC0031bkri005"
    霧 "「ん～～～っ」"
    太一 "「うまい……霧ちんは料理の才能がある」"
    call gl(2,"TCSK0000|TCSK000x")
    call vsp(2,1)
    with dissolve
    voice "vfCCC0031bkri006"
    霧 "「……おかずはレトルトなんで」"
    太一 "「でもうまい」"
    call gl(2,"TCSK0002|TCSK000x")
    call vsp(2,1)
    with dissolve
    voice "vfCCC0031bkri007"
    霧 "「作らないと、美希がいつまでもお菓子を」"
    call gl(1,"TCYM0002|TCYM0002")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3104mki004"
    美希 "「だってぇ……」"
    太一 "「お互い食事には苦労しているようだな」"
    voice "vfCCC0031bmki010"
    美希 "「ええ……」"
    太一 "「霧ちん結婚しよう」"
    call gl(2,"TCSK0002|TCSK000x")
    call vsp(2,1)
    with dissolve
    voice "vfCCC0031bkri008"
    霧 "「不可能です」"
    call gl(1,"TCYM0021|TCYM0021")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3104mki005"
    美希 "「いやです、じゃなくて不可能なんだ……」"
    太一 "「……燃えてきた」"
    call gl(2,"TCSK0001|TCSK000x")
    call vsp(2,1)
    with dissolve
    voice "vfCCC0031bkri009"
    霧 "「水かけますよ？」"
    太一 "「そりゃ困る」"
    call gl(1,"TCYM0000|TCYM0000")
    call vsp(1,1)
    with dissolve
    voice "vfCCC0031bmki012"
    美希 "「お菓子はもっとあるのですか？」"
    太一 "「あるよ。ビスケットとか、サブレとか。曜子先生はお菓子作るの得意だから」"
    call gl(1,"TCYM0004|TCYM0002")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3104mki006"
    美希 "「……意外です」"
    太一 "「いい保存食になるらしい」"
    call gl(2,"TCSK0000|TCSK000x")
    call vsp(2,1)
    with dissolve
    voice "vfCCC0031bkri010"
    霧 "「……恋人、なんですよね？」"
    太一 "「いや、一緒に暮らしてただけだよ」"
    call gl(1,"TCYM0001|TCYM0000")
    call vsp(1,1)
    with dissolve
    voice "vfCCC0031bmki017"
    美希 "「同棲」"
    call gl(2,"TCSK0000|TCSK000x")
    call vsp(2,1)
    with dissolve
    voice "vfCCC0031bkri011"
    霧 "「同棲」"
    "二人はハモった。"
    太一 "「同棲とは違う」"
    太一 "「俺たちは親がいないから、二人ともあの家に世話になってただけだよ」"
    "効率よく説明した。"
    call gl(1,"TCYM0000|TCYM0000")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3104mki007"
    美希 "「そうでしたか」"
    call gl(2,"TCSK0002|TCSK000x")
    call vsp(2,1)
    with dissolve
    voice "vfCCC0031bkri012"
    霧 "「……あやしい関係だと思っていたのに……」"
    call gl(1,"TCYM0021|TCYM0021")
    call vsp(1,1)
    with dissolve
    voice "vfCCC0031bmki019"
    美希 "「支倉先輩も謎が多い人ですよね」"
    太一 "「まったくだ」"
    太一 "「さあ、特別に千歳あめをつけるから、みんなで七五三気分に浸ろう」"
    call gl(1,"TCYM0003|TCYM0003")
    call vsp(1,1)
    with dissolve
    voice "vfCCC0031bmki020"
    美希 "「わー、ちとせあめだ！」"
    "美希がぱっと笑顔に。"
    "すかさず霧が取り上げる。"
    call gl(1,"TCYM0004|TCYM0002")
    call vsp(1,1)
    with dissolve
    voice "vfCCC0031bmki021"
    美希 "「うおー、何するだ！」"
    call gl(2,"TCSK0002|TCSK000x")
    call vsp(2,1)
    with dissolve
    voice "vfCCC0031bkri013"
    霧 "「お菓子だけじゃダメ」"
    call gl(1,"TCYM0002|TCYM0002")
    call vsp(1,1)
    with dissolve
    voice "vfCCC0031bmki022"
    美希 "「自分だって食べてたくせにー！」"
    call gl(2,"TCSK0000|TCSK000x")
    call vsp(2,1)
    with dissolve
    voice "vfCCC0031bkri014"
    霧 "「ちゃんとごはん食べる。健康管理、これからは自分でしないといけないんだよ？」"
    call gl(1,"TCYM0000|TCYM0000")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3104mki008"
    美希 "「……はーい」"
    voice "vfCCC0031bkri015"
    霧 "「なんですか？　いやらしい目でじっと見て……」"
    太一 "「いや、いいコンビだなって思って」"
    call gl(1,"TCYM0003|TCYM0003")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3104mki009"
    美希 "「……お花ちゃんたちですから」"
    太一 "「デビューさせてやりたいくらいだ」"
    call gl(1,"TCYM0000|TCYM0000")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3104mki010"
    美希 "「……今デビューしても……」"
    "弱気な美希。"
    voice "vfCCC0031bkri016"
    霧 "「最高八枚までしか売れないね。ＣＤ」"
    call gl(1,"TCYM0001|TCYM0000")
    call vsp(1,1)
    with dissolve
    voice "vfCCC0031bmki026"
    美希 "「ミリオンは夢のまた夢」"
    call gl(2,"TCSK0006|TCSK000x")
    call vsp(2,1)
    with dissolve
    voice "vfCCC0031bkri017"
    霧 "「じゃあわたし、二枚買ってあげる」"
    call gl(1,"TCYM0003|TCYM0003")
    call vsp(1,1)
    with dissolve
    voice "vfCCC0031bmki027"
    美希 "「じゃこっちも二枚買う」"
    voice "vfCCC0031bkri018"
    霧 "「十枚だね」"
    voice "vfCCC0031bmki028"
    美希 "「うん、十枚。二桁」"
    "くすくす笑う。"
    "仲睦まじく。"
    "その様子は、俺をほんの少しばかり、潤した。"
    stop bgm
    play se "se001"
    call gl(0,"bgcc0005s")
    call vsp(0,1)
    call vsp(1,0)
    call vsp(2,0)
    with Pixellate(300.0*2/1000.0,5)
    play bgm "bgm/bgm007.ogg"
    "新川豊が雑木林を眺めていた。"
    "俺はそんな新川のもとに近寄り、声をかける。"
    太一 "「どうした？」"
    "新川は汗をかいていた。"
    "見るからに夏の汗ではない。"
    "よろと後ずさる。"
    "車が来た。"
    太一 "「新川！」"
    "とっさに押さえた。"
    "すぐ背後を、ゆっくりと軽トラが走り抜けていく。"
    "俺が話しかけても、新川はなお無反応だった。"
    "震えていた。"
    太一 "「新川？」"
    call gl(1,"TCSY0002s|tcsy")
    call gp(1,t=center)#x=180
    call vsp(1,1)
    with dissolve
    voice "vmCCC3003shi000"
    新川 "「あ……悪い」"
    "我に返る。"
    call gl(1,"TCSY0000s|tcsy")
    call vsp(1,1)
    with dissolve
    voice "vmCCC3003shi001"
    新川 "「なんか……雑木林の奥とか見てたら……すげぇ気分悪くなってきて……昔から、そうなんだけどさ……わけ、わかんねぇんだけど……」"
    "顔を手で覆って、立ちくらみに戸惑うように、しばし。"
    "青い空を見あげて、喘ぐように息を吐いた。"
    "新川が雑木林の奥に見たもの。"
    "それはきっと―――"
    stop bgm
    stop se
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
    call gl(0,"bgcc0006")
    call vsp(0,1)
    with wipeleft
    "教室に立ち寄ってみる。気まぐれだ。"
    "案の定、冬子の姿がない。"
    call gl(0,"bgcc0011a")
    call vsp(0,1)
    with wipeleft
    play bgm "bgm/bgm020.ogg"
    太一 "「ん……」"
    "心が渇く。"
    "目頭を押さえた。耳鳴りがした。"
    "来るべきではなかった。"
    "俺の心だって、いつ弾けるかわからない。"
    "今失敗すれば、また遠い確率の旅をすることになる。"
    "ここに戻ってくるのに、何百週、何千週、繰り返すことになるのか。"
    "自覚はないのだろうが……耐えられない。"
    "教室を出た。"
    "冬子のことを意識から追い出す。"
    "はじまって三日目の『いつも』。"
    stop bgm
    "だけどそれは、がらんどうで満たされていて。"
    call gl(0,"bgcc0006")
    call vsp(0,1)
    with wipeleft
    "プールだ。"
    call gl(0,"evcc0029")
    call vsp(0,1)
    with wipeleft
    太一 "「……」"
    "よし。"
    "予定通り、選択されている。"
    "霧か美希、どちらかに異常がなければ、二人の行動はある程度確定的だ。"
    "固有時間を生きた美希のような者があらわれなければ。"
    play bgm "bgm/bgm024.ogg"
    voice "vfCCC3107mki000"
    美希 "「えいっ！」"
    voice "vfCCC0039kri000"
    霧 "「あ、だめだってば、だめー！」"
    voice "vfCCC3107mki001"
    美希 "「あはははっ、霧ー、濡れちゃうよー」"
    voice "vfCCC0039kri001"
    霧 "「だって水の中じゃないっ、あっ、髪濡れる、濡れちゃうからっ」"
    voice "vfCCC3107mki002"
    美希 "「だってプールじゃなーい！」"
    voice "vfCCC3107kri000"
    霧 "「そーだけどー！」"
    voice "vfCCC3107mki003"
    美希 "「えーい」"
    voice "vfCCC0039kri003"
    霧 "「あー、髪がー」"
    voice "vfCCC0039kri004"
    霧 "「しかえしっ！」"
    voice "vfCCC0039mki004"
    美希 "「きゃー！」"
    "幸せな光景を見ていた。"
    voice "vfCCC0039kri005"
    霧 "「んのー！」"
    voice "vfCCC3107mki004"
    美希 "「わーーー！」"
    voice "vfCCC0039kri006"
    霧 "「くらえー！！」"
    voice "vfCCC3107mki005"
    美希 "「くらわないもーん」"
    voice "vfCCC0039kri007"
    霧 "「あ、ビート板使うの禁止！」"
    voice "vfCCC0039mki007"
    美希 "「楯だよー」"
    voice "vfCCC0039kri008"
    霧 "「ずるー！」"
    voice "vfCCC0039mki008"
    美希 "「髪の長さが違う分、ハンデいるもん」"
    voice "vfCCC0039kri009"
    霧 "「けど、片手になった分、攻撃力は下がってる！」"
    voice "vfCCC3107mki006"
    美希 "「わ！？」"
    voice "vfCCC0039kri010"
    霧 "「狩りの時間だー！」"
    voice "vfCCC3107mki007"
    美希 "「あー、きゃー！？」"
    "ざぶざぶと動き回りながら、水をかけあう。"
    "無邪気なもんだ。"
    "トクン"
    太一 "「……！」"
    "心臓が跳ねた。"
    "軽く胸を打たれて。"
    "無意識に心臓を押さえた。"
    "臓器に心があるわけではない。"
    "俺の感じたことが、心臓をほとんど物理的にノックした。"
    "そのことが嬉しかった。"
    "俺は『ほほえましい』と心から思ったのだ。"
    voice "vfCCC0039kri011"
    霧 "「きゃあっ！」"
    play se "SE081"
    voice "vfCCC0039mki011"
    美希 "「あははははっ、転んだー！」"
    voice "vfCCC0039kri012"
    霧 "「ずぶぬれぇ……」"
    voice "vfCCC3107mki008"
    美希 "「プールだから濡れないと」"
    voice "vfCCC0039kri013"
    霧 "「……言ったなぁ」"
    voice "vfCCC3107mki009"
    美希 "「……え、ええ？」"
    voice "vfCCC0039kri014"
    霧 "「濡れたらもう泳げるもんね」"
    voice "vfCCC0039mki014"
    美希 "「あっ、あっあっ、接近戦はだめー！」"
    voice "vfCCC0039kri015"
    霧 "「平泳ぎでクロールに勝てるもんかぁ！」"
    voice "vfCCC0039mki015"
    美希 "「あたふたあたふたっ」"
    voice "vfCCC0039kri016"
    霧 "「水浸しにしてやるっ」"
    voice "vfCCC0039mki016"
    美希 "「だめー！　濡れたら髪がワカメになるー！」"
    voice "vfCCC0039kri017"
    霧 "「ワカメちゃんにしてやるー！」"
    voice "vfCCC0039mki017"
    美希 "「わっ、わっ、まずっ」"
    voice "vfCCC0039kri018"
    霧 "「そらー！」"
    voice "vfCCC0039mki018"
    美希 "「ぎにゃーーーーーーー！！」"
    "弾ける水の音。"
    "とめどない笑声。"
    "やんわりと流れる時間を思わせて、優しい。"
    "あたたかい世界の一場面。"
    "心に刻んでいく。"
    "忘れぬよう。"
    "克明に思い出せるよう。"
    "俺はずっと、二人の少女が戯れる様子を眺めていた。"
    stop bgm
    play se "SE001"
    call gl(0,"bgcc0005s")
    call vsp(0,1)
    with Pixellate(300.0*2/1000.0,5)
    play bgm "bgm/bgm003.ogg"
    "霧とはじめて出会ったのは、新川との再会に前後する。"
    "新川に姪がいたことを俺は聞いていたけど、まさか霧のことだと思わなかった。"
    call gl(0,"bgcc0018s")
    call vsp(0,1)
    call gl(1,"TCSK0000s|TCSK000x")
    call vsp(1,1)
    with Pixellate(300.0*2/1000.0,5)
    "ぎこちない挨拶。"
    "まだ群青学院に慣れない、霧からの糾弾。"
    "きまずい空気。"
    "俺は適応できない連中のことを霧に話し、"
    "霧の言葉の矛盾に触れ、"
    "霧がその正義感ゆえに守ろうとしていた少女の、先行きを予言した。"
    "そして俺がした一つの質問。"
    太一 "「友達を作るのは大変だ。でも作らずにはいられない。どうしてかわかる？」"
    太一 "「必要だからだ。心を育てるためには」"
    "全ての者にあてはまるわけではない。"
    "ただ俺にとって、この上ない事実だった。"
    "後に美希と知り合った霧は、二人そろって放送部に入ることになった。"
    "さらに意識は飛ぶ。当時を克明に思い出す。"
    call gl(0,"bgcc0010s")
    call vsp(0,1)
    call vsp(1,0)
    with Pixellate(300.0*2/1000.0,5)
    太一 "「おー、来たなー」"
    call gl(1,"TCYM0003s|TCYM0003")
    call gl(2,"TCSK0000s|TCSK000x")
    call vsp(0,1)
    call vsp(1,1)
    call vsp(2,1)
    call gp(1,t=left)
    call gp(2,t=right)
    with Dissolve(500.0/1000.0)
    voice "vfCCC3004mki000"
    美希 "「おいっす」"
    voice "vfCCC3004kri039"
    霧 "「……ども」"
    "二人は花壇に植えられた、二輪の花のようだった。"
    太一 "「ＦＬＯＷＥＲ’Ｓ！」"
    call gl(3,"TCMM0031s|TCMM0031")
    call gp(3,t=center)#x=225
    call vsp(1,0)
    call vsp(2,0)
    call vsp(3,1)
    with Dissolve(500.0/1000.0)
    voice "vfCCC3004msa000"
    見里 "「それは？」"
    太一 "「二人の芸名ですよ。放送部では芸名が必要なんだ。みんな持ってる」"
    call gl(1,"TCYM0004s|TCYM0002")
    call gl(2,"TCSK0002s|TCSK000x")
    call vsp(0,1)
    call vsp(1,1)
    call vsp(2,1)
    call vsp(3,0)
    call gp(1,t=left)
    call gp(2,t=right)
    with Dissolve(500.0/1000.0)
    voice "vfCCC3004mki001"
    美希 "「ふぁ～」"
    call gl(4,"TCST0000s|TCST0000")
    call gp(4,t=center)#x=190
    call vsp(4,1)
    call vsp(1,0)
    call vsp(2,0)
    with Dissolve(500.0/1000.0)
    voice "vmCCC3004yki000"
    友貴 "「またそんな嘘ンガッ」"
    play se "SE003"
    with vpunch
    hide pic4
    with dissolve
    "なんとか嘘のあたりで殴り飛ばせた。"
    太一 "「友貴はインモラル、桜庭がミスター自警団、そして俺は愛貴族」"
    call gl(1,"TCYM0021s|TCYM0021")
    call gl(2,"TCSK0002s|TCSK000x")
    call vsp(0,1)
    call vsp(1,1)
    call vsp(2,1)
    call vsp(3,0)
    call gp(1,t=left)#x=0
    call gp(2,t=right)#x=320
    with Dissolve(500.0/1000.0)
    voice "vfCCC3004mki002"
    美希 "「本当ですか？」"
    太一 "「いかにも！」"
    call gl(1,"TCYM0000s|TCYM0000")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3004mki003"
    美希 "「それで会話してみてください」"
    太一 "「ヘイ、インモラル、シスコン具合はどうなってるよ？　相変わらず愛変わらずって感じなんだろ？」"
    call gl(3,"TCMM0031s|TCMM0031")
    call gp(3,t=center)#x=225
    call vsp(3,1)
    call vsp(1,0)
    call vsp(2,0)
    with Dissolve(500.0/1000.0)
    voice "vfCCC3004msa001"
    見里 "「しすこん？」"
    voice "vmCCC3004yki001"
    友貴 "「黙ってくれぇぇぇ」"
    with vpunch
    "首を締められた。"
    "本人がいるので、友貴も必死だ。"
    太一 "「……わがっだ……ごうざん……ごうざん……じぬ……」"
    call gl(5,"TCSH0000s|tcsh")
    call gp(5,t=center)#x=190
    call vsp(5,1)
    call vsp(3,0)
    with Dissolve(500.0/1000.0)
    voice "vmCCC3004sku000"
    桜庭 "「愛貴族だけに愛に死ぬのか？」"
    太一 "「天国のママンに『会い』に死ぬことになりそうだ……」"
    call gl(3,"TCMM0006s|TCMM0006")
    call vsp(3,1)
    call vsp(5,0)
    with Dissolve(500.0/1000.0)
    voice "vfCCC3004msa002"
    見里 "「こら！　ぼーりょくは停学ですよ」"
    "友貴の頭を、みみ先輩がチョップする。"
    call gl(5,"TCST0001s|TCST0001")
    call gp(3,t=left)#x=20
    call gp(5,t=right)#x=340
    call vsp(3,1)
    call vsp(5,1)
    with Dissolve(500.0/1000.0)
    voice "vmCCC3004yki002"
    友貴 "「あ、うん……」"
    太一 "「……死ぬかと思った」"
    call gl(5,"TCST0004s|TCST0004")
    call vsp(5,1)
    with dissolve
    voice "vmCCC3004yki003"
    友貴 "「自業自得なんだ」"
    call gl(2,"TCSK0002s|TCSK000x")
    call gp(2,t=center)#x=220
    call vsp(3,0)
    call vsp(5,0)
    call vsp(2,1)
    with Dissolve(500.0/1000.0)
    voice "vfCCC3004kri040"
    霧 "「……はぁ」"
    "霧はいきなり疲れていた。"
    太一 "「なんだなんだその虚弱っぷりは」"
    太一 "「放送部は名義上運動部なんだからな？」"
    call gl(3,"TCMM0005s|TCMM000x")
    call gp(3,t=center)#x=225
    call vsp(2,0)
    call vsp(3,1)
    voice "vfCCC3004msa003"
    見里 "「……またそんなことを……」"
    太一 "「三年生の方々がめでたくご卒業となり、その穴を埋めるかのように入ってきた君たち二人に、桜庭先生はたいへん期待しておられる」"
    call gl(5,"TCSH0003s|tcsh")
    call gp(5,t=center)#x=190
    call vsp(5,1)
    call vsp(3,0)
    with Dissolve(500.0/1000.0)
    voice "vmCCC3004sku001"
    桜庭 "「ああ」"
    "桜庭はクールな物事で立ち上がると、突っ込んだまま抜けなくなった指からビンをぶらさげたまま、語り出した。"
    call gl(5,"TCSH0000s|tcsh")
    call vsp(5,1)
    with dissolve
    voice "vmCCC3004sku002"
    桜庭 "「今日はみんなに、柿の種の教訓を話したいと思う」"
    太一 "「いいぞ先生！」"
    voice "vfCCC3004msa004"
    見里 "「指、鬱血しますよ」"
    call gl(5,"TCSH0003s|tcsh")
    call vsp(5,1)
    with dissolve
    voice "vmCCC3004sku003"
    桜庭 "「柿の種にピーナッツ入っているものがある。知っているな」"
    "無視して桜庭は話す。というか聞こえてない。"
    "美希はこくこくと頷く。"
    "素直だ。"
    call gl(5,"TCSH0000s|tcsh")
    call vsp(5,1)
    with dissolve
    voice "vmCCC3004sku004"
    桜庭 "「そのピーナッツが許せないという奴は、意外と多い」"
    voice "vfCCC3004mki004"
    美希 "「そうですね」"
    call gl(5,"TCSH0003s|tcsh")
    call vsp(5,1)
    with dissolve
    voice "vmCCC3004sku005"
    桜庭 "「オレはつねづね、その欺瞞が許せなかった。なぜだと思う？」"
    太一 "「は、ピーナッツが入ってこそ、ピーナッツ入り柿の種であるからですな？」"
    call gl(5,"TCSH0002s|tcsh")
    call vsp(5,1)
    with dissolve
    voice "vmCCC3004sku006"
    桜庭 "「そうだ。イヤなら純正の柿の種を食えばいい。ピーナッツ入り柿の種を手にピーナッツがイヤなどという弱音は、ピーナッツ入り柿の種の尊厳を損なうものだからだ」"
    voice "vmCCC3004sku007"
    桜庭 "「欺瞞だ」"
    太一 "「おっしゃる通り！」"
    call gl(5,"TCSH0000s|tcsh")
    call vsp(5,1)
    with dissolve
    voice "vmCCC3004sku008"
    桜庭 "「だからオレは、あえて柿の種のピーナッツだけを食っている」"
    太一 "「……馬鹿かおまえは」"
    "醒めた。"
    call gl(5,"TCSH0002s|tcsh")
    call vsp(5,1)
    with dissolve
    voice "vmCCC3004sku009"
    桜庭 "「わかってくれたか」"
    太一 "「聞けよ」"
    call gl(5,"TCSH0000s|tcsh")
    call vsp(5,1)
    with dissolve
    voice "vmCCC3004sku010"
    桜庭 "「たまに右の耳が遠い」"
    "これは本当だ。"
    "日常生活に支障はないのだが。"
    太一 "「オレを素に戻らせたおまえの引かせパワー、許し難い」"
    太一 "「おまえのサクラバという苗字から、女王陛下の名においてクの文字を剥奪する」"
    call gl(5,"TCSH0003s|tcsh")
    call vsp(5,1)
    with dissolve
    voice "vmCCC3004sku011"
    桜庭 "「なに？」"
    太一 "「おまえは今日からサラバだ。さらば桜庭。こんにちはサラバ」"
    "言葉って面白い。"
    call gl(5,"TCSH0002s|tcsh")
    call vsp(5,1)
    with dissolve
    voice "vmCCC3004sku012"
    桜庭 "「わかった」"
    call gl(4,"TCST0005s|TCST0004")
    call gp(4,t=left)#x=20
    call gp(5,t=right)#x=350
    call vsp(5,1)
    call vsp(4,1)
    with Dissolve(500.0/1000.0)
    voice "vmCCC3004yki004"
    友貴 "「いや、認めるなってば」"
    voice "vmCCC3004sku013"
    桜庭 "「オレの話はこれで終わりだ」"
    hide pic5
    with dissolve
    "再び座り込むと、ビンを抜くため指をひねりはじめた。"
    call gl(3,"TCMM0005s|TCMM000x")
    call gp(3,t=center)#x=225
    call vsp(5,0)
    call vsp(4,0)
    call vsp(3,1)
    with Dissolve(500.0/1000.0)
    voice "vfCCC3004msa005"
    見里 "「……こんな人たちです」"
    "まとめていた。"
    call gl(1,"TCYM0003s|TCYM0003")
    call gl(2,"TCSK0000s|TCSK000x")
    call vsp(1,1)
    call vsp(2,1)
    call gp(1,t=left)#x=40
    call gp(2,t=right)#x=345
    call vsp(3,0)
    with Dissolve(500.0/1000.0)
    voice "vfCCC3004mki005"
    美希 "「よくわかりました」"
    霧 "「……」"
    call gl(3,"TCMM0021s|TCMM0021")
    call vsp(1,0)
    call vsp(2,0)
    call vsp(3,1)
    with Dissolve(500.0/1000.0)
    voice "vfCCC3004msa006"
    見里 "「やっていけそうですか？」"
    call gl(1,"TCYM0003s|TCYM0003")
    call gl(2,"TCSK0000s|TCSK000x")
    call vsp(1,1)
    call vsp(2,1)
    call gp(1,t=left)#x=40
    call gp(2,t=right)#x=345
    call vsp(3,0)
    with Dissolve(500.0/1000.0)
    voice "vfCCC3004mki006"
    美希 "「なんとか、平気そうです。ね、さくちん？」"
    call gl(2,"TCSK0003s|TCSK0003")
    call vsp(2,1)
    with dissolve
    voice "vfCCC3004kri042"
    霧 "「……やっていけと先生に言われましたんで」"
    call gl(3,"TCMM0002s|TCMM000x")
    call vsp(1,0)
    call vsp(2,0)
    call vsp(3,1)
    with Dissolve(500.0/1000.0)
    voice "vfCCC3004msa007"
    見里 "「まあ、無理強いではないので……イヤだったら抜けてもいいですから」"
    太一 "「あん、だめぇ……職場には花がいるのぉ」"
    call gl(3,"TCMM0000s|TCMM000x")
    call vsp(3,1)
    with dissolve
    voice "vfCCC3004msa008"
    見里 "「……だそうです」"
    "買収するか。見ればまだガキだし、もので釣るのがいいだろ。"
    太一 "「買収するか。見ればまだガキだし、もので釣るのがいいだろ。入部祝い作戦だ」"
    call gl(4,"TCST0003s|TCST0000")
    call gp(3,t=left)#x=20
    call gp(4,t=right)#x=360
    call vsp(4,1)
    call vsp(3,1)
    with Dissolve(500.0/1000.0)
    voice "vmCCC3004yki005"
    友貴 "「また口に出してるから、太一」"
    call gl(1,"TCYM0000s|TCYM0000")
    call gl(2,"TCSK0002s|TCSK000x")
    call vsp(1,1)
    call vsp(2,1)
    call gp(1,t=left)#x=40
    call gp(2,t=right)#x=345
    call vsp(3,0)
    call vsp(4,0)
    with Dissolve(500.0/1000.0)
    美希 "「……」"
    霧 "「……」"
    太一 "「んー、よしこれだ」"
    "太一袋から二つのアイテムを取り出す。"
    太一 "「ヤマンバ美希隊員！」"
    call gl(1,"TCYM0003s|TCYM0003")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3004mki008"
    美希 "「おす、ヤマノベです。はい！」"
    "アイテムの一つは色紙。"
    太一 "「君にはあの大スターにして整形のプロ、ちょっとやんちゃんな少年だいすきマイルドロボ、マイケル·ジャクソン―――」"
    call gl(1,"TCYM0004s|TCYM0002")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3004mki009"
    美希 "「サ、サイン色紙っすか！？」"
    太一 "「を心の師と仰ぐ愛貴族·黒須太一のサインをあげよう」"
    "押しつけた。"
    voice "vfCCC3004mki010"
    美希 "「ぁゃゃ」"
    太一 "「ぉょょ」"
    太一 "「で、佐倉霧隊員！」"
    call gl(1,"TCYM0000s|TCYM0000")
    call gl(2,"TCSK0000s|TCSK000x")
    call vsp(2,1)
    with dissolve
    call vsp(1,1)
    with dissolve
    voice "vfCCC3004kri044"
    霧 "「……え？」"
    太一 "「君にはベースボールを今たらしめたビックマン、ベーブ·ルース―――」"
    call gl(2,"TCSK0002s|TCSK000x")
    call vsp(2,1)
    with dissolve
    霧 "「……」"
    太一 "「太一人形を進呈しよう」"
    call gl(3,"TCMM0005s|TCMM000x")
    call vsp(1,0)
    call vsp(2,0)
    call vsp(3,1)
    call gp(3,t=center)#x=225
    with Dissolve(500.0/1000.0)
    voice "vfCCC3004msa009"
    見里 "「繋がってないじゃないですか」"
    call gl(3,"TCMM0000s|TCMM000x")
    call vsp(3,1)
    with dissolve
    voice "vfCCC3004msa010"
    見里 "「も、ぜんぜんですよ、ぜんぜん」"
    "先輩は眼鏡をつけていることからもわかる通り（？）規則の人。"
    "無秩序なものは気になるらしい。"
    call gl(4,"TCST0000s|TCST0000")
    call gp(3,t=left)#x=20
    call gp(4,t=right)#x=360
    call vsp(4,1)
    call vsp(3,1)
    with Dissolve(500.0/1000.0)
    voice "vmCCC3004yki006"
    友貴 "「さては反応がなかったからはしょったな」"
    太一 "「……さあ、佐倉君。明けても暮れてもこの人形を肌身離さずかき抱き泣き濡れる夜の小さな友にしても良い」"
    call gl(2,"TCSK0002s|TCSK000x")
    call gp(2,t=center)#x=190
    call vsp(2,1)
    call vsp(3,0)
    call vsp(4,0)
    with Dissolve(500.0/1000.0)
    霧 "「…………」"
    "手も出さなかったので、ひもで首にかけた。"
    call gl(1,"TCYM0021s|TCYM0021")
    call gp(1,t=center)#x=180
    call vsp(2,0)
    call vsp(1,1)
    with Dissolve(500.0/1000.0)
    voice "vfCCC3004mki011"
    美希 "「ご自分で作られたので？」"
    太一 "「そうとも」"
    call gl(5,"TCSH0000s|tcsh")
    call gp(5,t=center)#x=190
    call vsp(1,0)
    call vsp(5,1)
    with Dissolve(500.0/1000.0)
    voice "vmCCC3004sku014"
    桜庭 "「まめなやつだ」"
    call gl(1,"TCYM0003s|TCYM0003")
    call vsp(5,0)
    call gp(1,t=center)#x=180
    call vsp(1,1)
    with Dissolve(500.0/1000.0)
    voice "vfCCC3004mki012"
    美希 "「ピーナッツ専門なだけに、言うことも穀物的なんですね～」"
    voice "vmCCC3004goo000"
    三人 "「！！！」"
    "俺と桜庭と友貴は、顔を見合わせた。"
    "このギャグは気に入った。"
    太一 "「合格」"
    voice "vmCCC3004yki008"
    友貴 "「うん」"
    voice "vmCCC3004sku016"
    桜庭 "「いい」"
    "美希に親指を立てた。"
    call gl(1,"TCYM0004s|TCYM0002")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3004mki013"
    美希 "「え……あれ、はい？」"
    call gl(2,"TCSK0002s|TCSK000x")
    call vsp(1,0)
    call vsp(2,1)
    call gp(2,t=center)#x=190
    with Dissolve(500.0/1000.0)
    voice "vfCCC3004kri047"
    霧 "「…………ぽいっと」"
    call gl(2,"TCSK0003s|TCSK0003")
    call vsp(2,1)
    with dissolve
    voice "vfCCC3004kri048"
    霧 "「あれ、取れない？」"
    "霧は人形を捨てようとしていた。"
    太一 "「待てーい！」"
    call gl(2,"TCSK0001s|TCSK000x")
    call vsp(2,1)
    with dissolve
    voice "vfCCC3004kri049"
    霧 "「むっ」"
    "しまったという顔。"
    太一 "「捨てようとしたのか？　捨てようとしたんだろう？」"
    "勝ち誇る。"
    太一 "「残念だったな、『たいちにんぎょうをすてるなんてとんでもない！』のだ！」"
    call gl(2,"TCSK0002s|TCSK000x")
    call vsp(2,1)
    with dissolve
    voice "vfCCC3004kri050"
    霧 "「意味がわかりません」"
    太一 "「すげー重要なアイテムなんだよ！」"
    太一 "「だから捨てようとしても無理なのだ」"
    call gl(2,"TCSK0001s|TCSK000x")
    call vsp(2,1)
    with dissolve
    voice "vfCCC3004kri051"
    霧 "「……呪いですか」"
    call gl(1,"TCYM0000s|TCYM0000")
    call gp(1,t=center)#x=180
    call vsp(1,1)
    call vsp(2,0)
    with Dissolve(500.0/1000.0)
    voice "vfCCC3004mki014"
    美希 "「わー、じゃこのサインも！」"
    "美希はサインを窓から捨てようとする。"
    "どこからともなく声が響く。"
    play se "se108"
    "『らぶきぞくのサイン』はすてられない！"
    call gl(1,"TCYM0001s|TCYM0000")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3004mki015"
    美希 "「はゃんっ！？」"
    太一 "「わはははははは！」"
    call gl(3,"TCST0003s|TCST0000")
    call gp(3,t=center)#x=190
    call vsp(3,1)
    call vsp(1,0)
    with Dissolve(500.0/1000.0)
    voice "vmCCC3004yki009"
    友貴 "「魔法使いかおまえは」"
    call gl(4,"TCMM0005s|TCMM000x")
    call gp(3,t=left)
    call gp(4,t=right)
    call vsp(4,1)
    call vsp(3,1)
    with Dissolve(500.0/1000.0)
    voice "vfCCC3004msa011"
    見里 "「入部祝いどころか……入部呪いじゃないですか」"
    "前後の扉が同時に開く。"
    call gl(1,"TCSY0000s|tcsy")
    call gl(2,"TCKT0003s|TCKT000x")
    call gp(1,t=left)
    call gp(2,t=right)
    call vsp(1,1)
    call vsp(2,1)
    call vsp(3,0)
    call vsp(4,0)
    with Dissolve(500.0/1000.0)
    voice "vmCCC3004shi008"
    新川 "「ちーす、霧って来てるかー？」"
    voice "vfCCC3004fyu000"
    冬子 "「ちょっと太一！　待っててって言ったじゃないの！　どうして一人で行っちゃうのよ！」"
    "同時の来客。"
    call gl(1,"TCMM0002s|TCMM000x")
    call gp(1,t=center)#x=225
    call vsp(1,1)
    call vsp(2,0)
    with Dissolve(500.0/1000.0)
    voice "vfCCC3004msa012"
    見里 "「まあ、いらっしゃい」"
    voice "vfCCC3004msa013"
    見里 "「二人もお客さん。冷たいお茶を出しましょう」"
    hide pic1
    with dissolve
    "あたふたと冷蔵庫に。"
    call gl(5,"TCSH0000s|tcsh")
    call gp(5,t=center)#x=190
    call vsp(5,1)
    with dissolve
    voice "vmCCC3004sku017"
    桜庭 "「今日の冷蔵庫はカラだぞ、部長先輩」"
    call gl(1,"TCMM0005s|TCMM000x")
    call gp(1,t=left)
    call gp(5,t=right)
    call vsp(1,1)
    call vsp(5,1)
    with Dissolve(500.0/1000.0)
    voice "vfCCC3004msa014"
    見里 "「はうっ」"
    call gl(1,"TCMM0002s|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3004msa015"
    見里 "「ちょっと買ってきますんで、ひきとめておいてください！」"
    太一 "「らじゃる」"
    call gl(2,"TCKT0002s|TCKT000x")
    call gp(2,t=center)#x=230
    call vsp(2,1)
    call vsp(1,0)
    call vsp(5,0)
    with Dissolve(500.0/1000.0)
    voice "vfCCC3004fyu001"
    冬子 "「あ、いいです……そんなの……」"
    call gl(1,"TCMM0002s|TCMM000x")
    call gp(1,t=center)#x=230
    call vsp(1,1)
    call vsp(2,0)
    with Dissolve(500.0/1000.0)
    voice "vfCCC3004msa016"
    見里 "「絶対ですよー！」"
    hide pic1
    with dissolve
    "ぱたぱた腕を振りながら、廊下に消えた。"
    call gl(2,"TCSK0000s|TCSK000x")
    call gp(2,t=center)#x=190
    call vsp(2,1)
    with dissolve
    voice "vfCCC3004kri052"
    霧 "「……豊、なにしにきたの？」"
    call gl(3,"TCSY0000s|tcsy")
    call gp(3,t=right)
    call gp(2,t=left)
    call vsp(3,1)
    call vsp(2,1)
    with Dissolve(500.0/1000.0)
    voice "vmCCC3004shi009"
    新川 "「いちおう挨拶に。その……身内が世話になるわけだしよ」"
    call gl(2,"TCSK0002s|TCSK000x")
    call vsp(2,1)
    with dissolve
    voice "vfCCC3004kri053"
    霧 "「いらない。帰ってよ」"
    "押し出そうとする。"
    voice "vmCCC3004yki010"
    友貴 "「新川も入部するんだ？」"
    call gl(3,"TCSY0002s|tcsy")
    call vsp(3,1)
    with dissolve
    voice "vmCCC3004shi010"
    新川 "「えっ、俺野球部だし」"
    call gl(1,"TCYM0021s|TCYM0021")
    call vsp(1,1)
    call vsp(2,0)
    call gp(1,t=left)
    with Dissolve(500.0/1000.0)
    voice "vfCCC3004mki016"
    美希 "「野球部なんてありましたっけ？」"
    voice "vmCCC3004sku018"
    桜庭 "「ひたすら野球盤を遊ぶ、部員三人だけの組織だ」"
    call gl(1,"TCYM0001s|TCYM0000")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3004mki017"
    美希 "「……はえー、ふぁにーな」"
    太一 "「この学校自体ふぁにーだからな」"
    call gl(2,"TCKT0003s|TCKT000x")
    call vsp(1,0)
    call vsp(2,1)
    call vsp(3,0)
    call gp(2,t=center)#x=230
    with Dissolve(500.0/1000.0)
    voice "vfCCC3004fyu002"
    冬子 "「あー、太一！　あんたいったいどういうつもりで約束すっぽかして……」"
    太一 "「アイテムは人に譲ることはできるぞ」"
    call gl(1,"TCYM0003s|TCYM0003")
    call vsp(1,1)
    call vsp(2,0)
    call gp(1,t=center)#x=180
    with Dissolve(500.0/1000.0)
    voice "vfCCC3004mki018"
    美希 "「あの、桐原先輩、これあげます！」"
    call gl(2,"TCKT0001s|TCKT000x")
    call gp(2,t=center)#x=230
    call vsp(1,0)
    call vsp(2,1)
    with Dissolve(500.0/1000.0)
    voice "vfCCC3004fyu003"
    冬子 "「え？」"
    "受け取る。"
    call gl(2,"TCKT0004s|TCKT000x")
    call vsp(2,1)
    with dissolve
    voice "vfCCC3004fyu004"
    冬子 "「やだコレ？　手から離れないわよ？　え、接着剤？」"
    "ぷんぷん振るが離れない。"
    voice "vfCCC3004fyu005"
    冬子 "「ちょっと、どういうことよっ！？」"
    play se "se108"
    "『らぶきぞくのサイン』はすてられない！"
    play se "se108"
    "『らぶきぞくのサイン』はすてられない！"
    play se "se108"
    "『らぶきぞくのサイン』はすてられない！"
    太一 "「無意味にすてるコマンドを繰り返すな。システムメッセージがうるさい」"
    call gl(2,"TCKT0003s|TCKT000x")
    call vsp(2,1)
    with dissolve
    voice "vfCCC3004fyu006"
    冬子 "「わけわかんないし聞こえないそんなメッセージ」"
    太一 "「人にあげるしかないな」"
    voice "vfCCC3004fyu007"
    冬子 "「じゃあアンタが責任取ってもらいなさいよ！」"
    play se "se108"
    "たいちにはあげられない！"
    voice "vfCCC3004fyu008"
    冬子 "「どうしてよ！」"
    太一 "「仲間でないと受け渡しはできないんだ」"
    太一 "「おまえと俺とは他人も同然だから、受け渡しはできない」"
    call gl(2,"TCKT0004s|TCKT000x")
    call vsp(2,1)
    with dissolve
    "冬子はぱくぱくと口を開閉させた。金魚みたい。"
    call gl(2,"TCKT0003s|TCKT000x")
    call vsp(2,1)
    with dissolve
    voice "vfCCC3004fyu009"
    冬子 "「な、な、なんですってー！！」"
    太一 "「あきらめて部員になるのだな」"
    voice "vfCCC3004fyu010"
    冬子 "「もきーーーーーーーーーーっ！！」"
    call gl(1,"TCSK0003s|TCSK0003")
    call gp(1,t=left)
    call vsp(1,1)
    call vsp(2,0)
    with Dissolve(500.0/1000.0)
    voice "vfCCC3004kri054"
    霧 "「いいからはやくかえってよー！　恥ずかしいんだから！」"
    call gl(2,"TCSY0001s|tcsy")
    call gp(2,t=right)
    call vsp(2,1)
    with dissolve
    voice "vmCCC3004shi011"
    新川 "「だってうまくやってんのかどうか心配じゃんかー……おっまえ頼りないしさ……」"
    call gl(1,"TCSK0002s|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3004kri055"
    霧 "「うまくやるから。かえって、へいきだから」"
    call gl(3,"TCSH0002s|tcsh")
    call vsp(2,0)
    call vsp(1,0)
    call gp(3,t=center)#x=190
    call vsp(3,1)
    with Dissolve(500.0/1000.0)
    voice "vmCCC3004sku019"
    桜庭 "「ふ、賑やかだな、今日は」"
    "ぽつりと、桜庭が呟く。"
    call gl(4,"TCST0000s|TCST0000")
    call gp(4,t=right)
    call gp(3,t=left)
    call vsp(4,1)
    call vsp(3,1)
    with Dissolve(500.0/1000.0)
    voice "vmCCC3004yki011"
    友貴 "「お、ビン抜けたんだ」"
    voice "vmCCC3004sku020"
    桜庭 "「石けん水の力でな」"
    "先輩がお盆にコップをのせて、よたよたと戻ってきた。"
    call gl(5,"TCMM0002s|TCMM000x")
    call vsp(5,1)
    call gp(5,t=center)#x=235
    call vsp(4,0)
    call vsp(3,0)
    with Dissolve(500.0/1000.0)
    voice "vfCCC3004msa017"
    見里 "「お茶がなくて、コップに水くんできましたー！」"
    太一 "「意味ねー！」"
    call gl(1,"TCYM0003s|TCYM0003")
    call gp(1,t=right)
    call gp(5,t=left)
    call vsp(1,1)
    call vsp(5,1)
    with Dissolve(500.0/1000.0)
    voice "vfCCC3004mki019"
    美希 "「あはははは」"
    "笑ったり怒ったり。"
    "ちょっとしたお祭り騒ぎ。"
    "こういうのがいい。"
    "思い出はこうあるべきだった。"
    太一 "「みんな見てくれ！　大変なんだ！」"
    "視線が集まる。"
    太一 "「ストリーキングが出たぞー！！」"
    "素早く服を脱いでいく。"
    call gl(2,"TCST0004s|TCST0004")
    call gp(2,t=center)#x=190
    call vsp(1,0)
    call vsp(5,0)
    call vsp(2,1)
    with Dissolve(500.0/1000.0)
    voice "vmCCC3004yki012"
    友貴 "「おまえだよ！」"
    play se "SE003"
    with Dissolve(500.0/1000.0)
    "蹴飛ばされた。"
    "冬子の尻に抱きつく。"
    call gl(1,"TCKT0004s|TCKT000x")
    call gp(1,t=center)#x=230
    call vsp(1,1)
    call vsp(2,0)
    voice "vfCCC3004fyu011"
    冬子 "「きああああああああっ！？」"
    太一 "「ちょっと薄いな。骨盤が当たる。もっと肉感的になれよ」"
    call gl(1,"TCKT0011s|TCKT0011")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3004fyu012"
    冬子 "「きええええええええっ！！」"
    "気合いだった。"
    hide pic1
    with dissolve
    call gl(4,"sgcc0012s")
    call vsp(4,1)
    with dissolve
    play se "se106"
    with vpunch
    太一 "「ぐふーっ！」"
    "霧に抱きついた。"
    call gl(4,"sgcc0013s")
    call vsp(4,1)
    with dissolve
    play se "se106"
    with vpunch
    voice "vfCCC3004kri056"
    霧 "「男に触られたーーーーーーーっ！！」"
    太一 "「ぎゃふーっ！」"
    call gl(4,"sgcc0015s")
    call vsp(4,1)
    with dissolve
    play se "se106"
    with vpunch
    voice "vfCCC3004mki020"
    美希 "「わーい！！」"
    太一 "「ぐおーっ！？」"
    voice "vfCCC3004fyu013"
    冬子 "「宮澄先輩もどうぞ」"
    voice "vfCCC3004msa018"
    見里 "「え、で、でも？」"
    voice "vfCCC3004fyu014"
    冬子 "「地面に落ちたら負けですよ」"
    "ボールか俺は。"
    voice "vfCCC3004msa019"
    見里 "「まあ大変」"
    call gl(4,"sgcc0014s")
    call vsp(4,1)
    with dissolve
    play se "se106"
    with vpunch
    voice "vfCCC3004msa020"
    見里 "「こ、こうですか？」"
    太一 "「せりゃー！！」"
    voice "vmCCC3004yki013"
    友貴 "「最後は特に気合い入ってるなー」"
    voice "vmCCC3004sku021"
    桜庭 "「あれは太一の特別サービスと見た」"
    voice "vfCCC3004mki021"
    美希 "「男っす！」"
    "楽しかった。"
    "どこまでも楽しかった。"
    "良質の思い出。"
    call gl(0,"bgcc0000d")
    call vsp(0,1)
    call vsp(1,0)
    call vsp(2,0)
    call vsp(3,0)
    call vsp(4,0)
    call vsp(5,0)
    call gp(5,t=left)
    with Dissolve(500.0/1000.0)
    stop se
    "決して忘れたくはない。"
    "そう願った。"
    stop bgm
    call gl(0,"bgcc0003b")
    call vsp(0,1)
    with wipeleft
    "その夜。"
    "外から物音がした。"
    play bgm "bgm/bgm007.ogg"
    call gl(0,"bgcc0003e")
    call vsp(0,1)
    with Dissolve(500.0/1000.0)
    "蝋燭を消す。"
    "窓際に。"
    "外を見る。"
    "家の前、道路を霧が歩いていた。"
    call gl(0,"bgcc0004c")
    call vsp(0,1)
    with wipeleft
    call gl(0,"bgcc0002c")
    call vsp(0,1)
    with wipeleft
    "追う。"
    call gl(0,"bgcc0000d")
    call vsp(0,1)
    with Dissolve(500.0/1000.0)
    "……………………。"
    call gl(0,"evcc0024b")
    call vsp(0,1)
    with Dissolve(500.0/1000.0)
    "クロスボウ―――"
    "断じて玩具ではなかった。"
    "この国で手に入る、強力無比な武器だ。"
    "連射こそできないが。"
    "静音性に優れ、破壊力に富む。"
    "霧は引き金を引いた。"
    "枯れ木に矢が刺さった。"
    "風切り音が耳に残る。"
    "霧は新しい矢をつがえる。"
    "コッキング装置で、装填を済ませた。"
    "狙いを定める。"
    霧 "「……………………」"
    "射線が傾いた。"
    "故意か、偶然か。"
    play se "SE066"
    "撃つ。"
    霧 "「…………」"
    "霧は足下に息を落とすと、頭をくしゃっとかき乱した。"
    "苛立たしげに。"
    call gl(0,"bgcc0000c")
    call vsp(0,1)
    with wipeleft
    "的にした樹に走り寄る。"
    "矢を回収。"
    "去っていった。"
    "樹のそばに行ってみる。"
    call gl(4,"sgcc0022a")
    call vsp(4,1)
    with dissolve
    太一 "「……」"
    "俺はずるいことをしているのかな？"
    "霧は俺を怪物だと思っている。"
    "人の心を食う怪物。"
    "今の俺は、まさにそうなのではないだろうか？"
    stop bgm
    call gl(0,"bgcc0000d")
    call vsp(0,1)
    call vsp(4,0)
    with Dissolve(500.0/1000.0)
    play se "se001"
    play bgm "bgm/bgm009.ogg"
    call gl(0,"bgcc0006s")
    call vsp(0,1)
    with Pixellate(300.0*2/1000.0,5)
    call gl(1,"TCSK0000s|TCSK000x")
    call gp(1,t=center)#x=220
    call vsp(1,1)
    with dissolve
    voice "vfCCC3007kri008"
    霧 "「前の学校で、友達なんていませんでしたから。兄にも私にも」"
    call gl(1,"TCSK0002s|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3007kri009"
    霧 "「友達だった人にも、裏切られて……誰も信用できなくなって……」"
    voice "vfCCC3007kri010"
    霧 "「誰も傷つけてないのに、みんなから傷つけられて」"
    太一 "「けど身を守った猛獣は、撃ち殺されるのが世の常なんだよ」"
    call gl(1,"TCSK0001s|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3007kri012"
    霧 "「……人間じゃないですか」"
    "……………………。"
    call gl(1,"TCSK0004s|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3007kri017"
    霧 "「わたしは」"
    voice "vfCCC3007kri018"
    霧 "「世界が恐くてたまらない、です」"
    太一 "「どんなところが？」"
    voice "vfCCC3007kri019"
    霧 "「……悪意が」"
    voice "vfCCC3007kri020"
    霧 "「みんなの悪意が……」"
    "……………………。"
    call gl(1,"TCSK0000s|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3007kri022"
    霧 "「……人間なんて、なくなる時にはあっさりなくなるって思ってます……だって、世界にはほとんど何もないから……」"
    voice "vfCCC3007kri023"
    霧 "「きっと『何もない』方が多いんです。『なにかある』方は、ちょっとだけなんです！」"
    voice "vfCCC3007kri024"
    霧 "「いつ押し流されてしまうかもわからないって……思って」"
    太一 "「その……ＳＦみたいな、人類滅亡とか？」"
    voice "vfCCC3007kri025"
    霧 "「そういうのとは違って……そういう理由があるのとは違って……」"
    voice "vfCCC3007kri026"
    霧 "「夢から覚めたみたいに」"
    voice "vfCCC3007kri027"
    霧 "「いがみあってばかりで、こわいだけなのに……」"
    voice "vfCCC3007kri028"
    霧 "「けどある日、突然すべてがなくなって……ちっぽけな世界で……もし自分ひとりが取り残されたらって考えると……」"
    call gl(1,"TCSK0004s|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3007kri029"
    霧 "「わたし……わたしは……」"
    "……………………。"
    太一 "「幸せの形が、人と違うだけさ」"
    call gl(1,"TCSK0003s|TCSK0003")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3007kri046"
    霧 "「……そんなのいやです」"
    voice "vfCCC3007kri047"
    霧 "「悪意はないのかもしれないけれど、わたしはそんなのはいやです」"
    voice "vfCCC3007kri048"
    霧 "「だって……人がいるのに……一人一人が絶海の孤島みたいで……閉じてて……」"
    call gl(1,"TCSK0002s|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3007kri049"
    霧 "「いやなんです……」"
    "……………………。"
    "まるで霧は、"
    "かまってください―――"
    "そう叫んでいるように見えた。"
    stop bgm
    stop se
    call gl(0,"bgcc0000d")
    call vsp(0,1)
    call vsp(1,0)
    call vsp(2,0)
    with Dissolve(500.0/1000.0)
    pause (1000.0/1000.0)
    pause (1000.0/1000.0)
    play bgm "bgm/bgm018.ogg"
    call gl(0,"bgcc0006")
    call vsp(0,1)
    with Dissolve(500.0/1000.0)
    太一 "「う……」"
    "目が覚める。"
    "夢を見ていた。"
    "懐かしい夢。"
    "霧と悪意の話。"
    "そういえば二人が、どう世界から拒絶されていたのか、俺は知らない。"
    "だいたいは想像はつくけれど。"
    "結局人は、自分のために生きている。"
    "人と触れあうことで生じる、様々な欲望の中で。"
    "皮肉である。"
    "ほどよい時間になっていた。"
    太一 "「そろそろ行くか」"
    stop bgm
    call gl(0,"bgcc0007")
    call vsp(0,1)
    with wipeleft
    "霧がいた。"
    play bgm "bgm/bgm020.ogg"
    "フェンスから外界を見渡している。"
    "既視感が、俺の意識を過去昔へと連れ去った。"
    play se "SE001"
    call gl(0,"bgcc0007s")
    call vsp(0,1)
    with Pixellate(300.0*2/1000.0,5)
    play bgm "bgm/bgm015.ogg"
    "夏も終わりかけていた。"
    "蝉たちも一際うるさい。"
    "叩きつけるような鳴き声。"
    "最後の命を振り絞っていると知れる。"
    "命の残滓に彩られる夏。"
    "霧は屋上にいた。"
    "一人だ。"
    "泣いていた。"
    "背後からでも、肩の震えを見ればわかる。"
    太一 "「霧……」"
    call gl(1,"TCSK0002s|TCSK000x")
    call gp(1,t=center)#x=220
    call vsp(1,1)
    with dissolve
    voice "vfCCC3008kri000"
    霧 "「……黒須……先輩？」"
    "涙を隠すこともなく。"
    voice "vfCCC3008kri001"
    霧 "「豊……豊が……ここから落ちて……」"
    太一 "「ああ……」"
    "知っていた。"
    "知らない者はいなかった。"
    "この街には。"
    "世間一般では、学生が一人飛び降り自殺をすれば、それなりに話題になる。"
    "保護者は学校を問いつめ、誰が悪いのか、白日のもとにさらそうとする。"
    "学校も責任を回避しようとする。"
    "群青ではそれがない。"
    "世間の誰も問いつめてはこないし、学校も逃げない。"
    "何人かの人間が責任を取った。"
    "世間は群青の危険な少年少女たちのことなど、どうでも良かった。"
    "悲しむ者は、わずか。"
    call gl(1,"TCSK0004s|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3008kri002"
    霧 "「誰も……誰も……悲しまない……わたしたちがどういう気持ちで……生きてきたのか……誰もっ」"
    "珍しく興奮していた。"
    "豊の死から、すでに一週間が経過していた。"
    "霧の悲嘆は遅れてきていた。"
    太一 "「なあ霧……豊は、幸せだったのかな」"
    霧 "「……？」"
    太一 "「あいつはあいつなりに、幸せだったのかな？」"
    "ありがちな問いかけ。"
    "けど。"
    "意味はまったく逆だった。"
    call gl(1,"TCSK0002s|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3008kri004"
    霧 "「……ずっと、つらい思いをしてきたんです」"
    太一 "「本当にずっとつらかった？」"
    太一 "「一瞬でも、幸せな時間はなかった？」"
    call gl(1,"TCSK0004s|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3008kri005"
    霧 "「それは……」"
    "あったに違いない。"
    voice "vfCCC3008kri006"
    霧 "「……先輩と友達になってからは……笑うように……」"
    voice "vfCCC3008kri007"
    霧 "「けど全然取り戻してないっ」"
    "語調が強まる。"
    call gl(1,"TCSK0021s|TCSK0021")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3008kri008"
    霧 "「受けた苦しみを、ちっとも取り戻してないっ」"
    太一 "「じゃあ霧ちんは、豊の人生が取るに足らないものだったと思ってるわけか」"
    call gl(1,"TCSK0004s|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3008kri009"
    霧 "「そうじゃ……ないですけど……」"
    太一 "「……と言ってはみたものの、悲しいのは理屈じゃないものな」"
    "俺も迷っていた。"
    "霧の処遇に。"
    太一 "「泣けばいいさ」"
    "空を見あげる。"
    "視界を埋めた純白が、巨大な入道雲と理解できるまでの刹那。"
    太一 "「せめて夏が終わる前に」"
    "蝉たちの最期とともに。"
    "万感こもごも含んだ意味に、霧には聞こえたのだろう。"
    hide pic1
    with dissolve
    voice "vfCCC3008kri010"
    霧 "「……うわぁぁぁぁぁぁぁぁぁぁぁぁぁ！」"
    "目を伏せ、俺のシャツの裾を掴んで、声を張り上げた。"
    voice "vfCCC3008kri011"
    霧 "「ゆたにぃが……死んじゃった……死んで……」"
    "嗚咽。"
    太一 "「…………」"
    "ゆたにぃ。"
    "大好きな、お兄ちゃんだったわけだ。"
    "片足でも立派に生きて。"
    "霧の両親―――"
    "豊の葬式で見た二人の顔には、軽い安堵があった。"
    "霧はそのことに気づいているのか？"
    "おそらく、悟っているに違いなかった。"
    "いろんなつらい目に遭っても、二人で支え合ってきたんだろう。"
    "いわば半身だ。"
    "霧は半分なのだ。"
    "俺と同様に……。"
    "ただ霧は、望んでそうなった。"
    "今は強い感情が気力を剥奪している。"
    "が、いずれ悲しみが薄れれば、あるべきはずのもう半分を求めるだろう。"
    "豊と霧。"
    "一心同体だった二人。"
    "霧に罪はない。"
    "けど俺は……俺の怪物は、身じろぎしてしまった。"
    太一 "「霧……」"
    "背中に手をまわす。"
    "激情が索敵を甘くして、霧は気づかない。"
    voice "vfCCC3008kri012"
    霧 "「ううう……うぁぁぁぁ……」"
    "少しずつ、情緒は沈静化していく。"
    "その頃には、俺はすっかり霧を抱きしめていた。"
    太一 "「霧……寂しい？」"
    霧 "「……？」"
    太一 "「寂しい、よな」"
    voice "vfCCC3008kri014"
    霧 "「……黒須先輩？」"
    太一 "「俺は虚しいんだ。とてもね」"
    "見下ろせば小さな面差し。"
    "深みをたたえた黒曜石がふたつ、表面を薄い塩水で濡らす。"
    太一 "「豊は幸せだったと思うよ。霧もいたし、イヤなことは忘れてたし」"
    太一 "「最期まで、幸せだったって、俺は思ってる」"
    "顔を近づける。"
    voice "vfCCC3008kri015"
    霧 "「…………ぇ」"
    "小さく狼狽を示す。"
    "顔を交差するように重ねて。"
    "唇を、盗みとる。"
    call gl(0,"evcc0049a")
    call vsp(0,1)
    call vsp(1,0)
    with Dissolve(500.0/1000.0)
    voice "vfCCC3008kri016"
    霧 "「…………っ！？」"
    "四肢が暴れかける。"
    "強く抱きしめた。"
    voice "vfCCC3008kri017"
    霧 "「……んぁ」"
    "霧の息が詰まった。"
    "フェンスに押しつけて、唇を吸い続ける。"
    voice "vfCCC3008kri018"
    霧 "「……ふぁ……ぃゃ……だめ……」"
    "驚きが、霧の思考力を奪っていた。"
    "ろくな抵抗さえない。"
    太一 "「寂しい？」"
    voice "vfCCC3008kri019"
    霧 "「……え？」"
    太一 "「寂しいんだろ？」"
    voice "vfCCC3008kri020"
    霧 "「……わか……らない……」"
    "キスする。"
    "二度目。"
    "今度は歯茎の内側に、侵略していく。"
    "同時に手を、スカートの中に。"
    voice "vfCCC3008kri021"
    霧 "「んっ……ん、んんんんっ！？」"
    stop bgm
    "突如として抵抗が強まる。"
    "霧は俺を突き放した。"
    call gl(0,"bgcc0007s")
    call gl(1,"TCSK0004s|TCSK000x")
    call gp(1,t=center)
    call vsp(0,1)
    call vsp(1,1)
    with Dissolve(500.0/1000.0)
    voice "vfCCC3008kri022"
    霧 "「や、やめてくださいっ！！」"
    太一 "「…………」"
    "俺は薄笑いを浮かべていたんだと思う。きっと。"
    play bgm "bgm/bgm014.ogg"
    voice "vfCCC3008kri023"
    霧 "「あなたは……」"
    "衝撃が、ゆっくりと嫌悪に覆われていく様を、俺は見ていた。"
    call gl(1,"TCSK0001s|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3008kri024"
    霧 "「っっ！！」"
    play se "se035"
    hide pic1
    with dissolve
    "走り去る。"
    "俺の脇を通り過ぎて。"
    play se "SE044"
    extend "軋む扉。締まる扉。"
    play se "se036"
    太一 "「……はは」"
    "顔を手で覆う。"
    "なるほど確かにこれはマズイ。"
    "口元が酷薄に吊り上がっていた。"
    call gl(0,"bgcc0000d")
    call vsp(0,1)
    call vsp(1,0)
    stop se
    with Dissolve(500.0/1000.0)
    stop bgm
    "霧とは疎遠になった。"
    "部活にもあまり顔を出さなくなった。"
    "美希が強引に連れてくることはあったが、俺のことは避けた。"
    "会話もなくなり、関係は途絶した。"
    "そんなことが、あったんだ―――"
    call gl(0,"bgcc0007")
    call vsp(0,1)
    with Dissolve(500.0/1000.0)
    太一 "「…………」"
    "はからずも霧の予言は当たることになった。"
    "人間なんて、アッサリ滅びてしまうものだ。"
    "さて。"
    太一 "「霧」"
    play bgm "bgm/bgm022.ogg"
    "そっと声をかける。"
    "霧は驚かなかった。"
    "ゆるりと振り返る。"
    call gl(0,"evcc0055")
    call vsp(0,1)
    with Dissolve(500.0/1000.0)
    voice "vfCCC3009kri000"
    霧 "「……世界がこんなことになって……人もいなくなって……」"
    voice "vfCCC3009kri001"
    霧 "「悪意はなくなったかわりに……密度もなくなって……」"
    voice "vfCCC3009kri002"
    霧 "「それでも、あなたは変わらないんですね」"
    太一 "「…………」"
    voice "vfCCC3009kri003"
    霧 "「……前から言おうと思っていました」"
    voice "vfCCC3009kri004"
    霧 "「先輩はどうして、生きてるんですか？」"
    "『なあ、ひとつ質問なんだけど……どうして今すぐにでも死なないんだ？』"
    "重なる。"
    "過去と現在。"
    "交差して。"
    "まるで、昔投げつけた刃を、今になって不意に投げ返されたような。"
    "アイロニカルな構図。"
    voice "vfCCC3009kri005"
    霧 "「自分に生きる資格があると思っているんですか？」"
    太一 "「…………」"
    voice "vfCCC3009kri006"
    霧 "「あなたは、黒い」"
    "的確な比喩だと思った。"
    voice "vfCCC3009kri007"
    霧 "「ヒトじゃない。ヒトに似たものでしかない。ヒトに擬態してる。虫みたいに」"
    voice "vfCCC3009kri008"
    霧 "「擬態して、ヒトに化けて、ヒトを襲う」"
    voice "vfCCC3009kri009"
    霧 "「あなたは人を傷つけるものです。決して相容れない」"
    voice "vfCCC3009kri010"
    霧 "「どうしてあなたの適応係数が８０を越えているのか、昔は不思議でした。けどそれはまったくおかしなことじゃない。あなたの中のヒトの部分は、文字通り二割ほどしかない」"
    "饒舌に語る。"
    "今までたくわえられた佐倉霧という様式を覆す、鮮烈なイメージを構築していく。"
    "言葉のナイフが、俺の精神を刺そうとしていた。"
    "今までは鈍い刃物しか持ち得なかった―――"
    "佐倉霧の切り札となって！"
    voice "vfCCC3009kri011"
    霧 "「怪物です」"
    voice "vfCCC3009kri012"
    霧 "「あなたの欺瞞は、怪物の分際で怪物に徹さないところです」"
    voice "vfCCC3009kri013"
    霧 "「人と怪物との間に共感が芽生えて、仲良く幸せに暮らせると思っているんですか？　あなたが人並みの幸せを手に出来ると？」"
    voice "vfCCC3009kri014"
    霧 "「ありえない」"
    voice "vfCCC3009kri015"
    霧 "「世界にわずかしかない優しさは、決してあなたのために取り分けられない。いえ、取り分けられてはならないんです」"
    voice "vfCCC3009kri016"
    霧 "「体を食い破って出てくる寄生虫に、愛を抱く人がいないのと一緒です。もしいたとしてもそれは狂人でしょう」"
    voice "vfCCC3009kri017"
    霧 "「あなたはいつも自分のために犠牲になってくれる獲物を捜してる。わたしにはわかります。今まではそれは抑えられていた。けど世界がこんなことになって、ヒトの数が少なくなって、あなたの抑えはきかなくなってきてる」"
    voice "vfCCC3009kri018"
    霧 "「擬態をする必要がなくなったからです」"
    voice "vfCCC3009kri019"
    霧 "「傷つけて楽しむため、あなたの目はいつも私たちに注がれている。それもひと思いにではなく、ゆっくりと時間をかけて嬲り尽くそうとしている」"
    voice "vfCCC3009kri020"
    霧 "「ヒトでもない、怪物でもない」"
    voice "vfCCC3009kri021"
    霧 "「では何者なんですか？　何者でもないあなたこそ、世界から消えるべきだった。わたしはそう思います」"
    voice "vfCCC3009kri022"
    霧 "「大半が悪意に満ちた人類だって、あなた一人の命よりはずっと価値があった。わたしにとってさえ、そうです」"
    voice "vfCCC3009kri023"
    霧 "「ふたつ、忠告します」"
    voice "vfCCC3009kri024"
    霧 "「まずあなたが他者との触れあいの中で本当の人間になれるのだと思っているとしたら、それは間違いです。あり得ません。人間を冒涜する考えです。先輩ほど完璧なバケモノは見たことないですから」"
    voice "vfCCC3009kri025"
    霧 "「あなたは掛け値なしの精神異常者。狂人の中の狂人」"
    voice "vfCCC3009kri026"
    霧 "「……狂える者たちの頂点です」"
    voice "vfCCC3009kri027"
    霧 "「そしてもう一つ。わたしたちに手を出そうとは思わないことです」"
    voice "vfCCC3009kri028"
    霧 "「もし先輩が生贄を求めてわたしたちに近づくことがあれば……」"
    "最後のひとつきを、霧は繰り出す。"
    voice "vfCCC3009kri029"
    霧 "「射殺します」"
    太一 "「……………………」"
    voice "vfCCC3009kri030"
    霧 "「……美希は絶対に、あなたには渡さない」"
    voice "vfCCC3009kri031"
    霧 "「壊させない！」"
    "つかつかと靴音を立てて、脇を通り過ぎる。"
    call gl(0,"bgcc0007")
    call vsp(0,1)
    with Dissolve(500.0/1000.0)
    play se "SE044"
    extend "軋む扉。締まる扉。"
    play se "se036"
    "俺は一人になった。"
    太一 "「……怪物か」"
    "言葉を反芻して、噛みしめる。"
    "知っていたとはいえ。"
    "……きつい。"
    stop bgm
    pause (500.0/1000.0)
    pause (500.0/1000.0)
    call gl(0,"bgcc0003e")
    call vsp(0,1)
    with wipeleft
    "過去の記録通り、霧がやってくる。"
    "追う。"
    call gl(0,"bgcc0002c")
    call vsp(0,1)
    with wipeleft
    "こっちだな。"
    call gl(0,"bgcc0000c")
    call vsp(0,1)
    with wipeleft
    "まっすぐ、雑木林に入る。"
    "一つ疑問なのは。"
    "曜子ちゃん。"
    "予定調和的に行動する人だろうか？"
    "もし彼女が行動しなかったら。"
    "霧と俺との溝は、埋まるのか？"
    "埋まらなかったら……。"
    "疑問を抱きつつ、目的の場所に。"
    "目を切り替えておく。"
    "夜が明るく見える。"
    voice "vfCCC3012akri000"
    霧 "「……ひゃっ」"
    play bgm "bgm/bgm019.ogg"
    "悲鳴が聞こえた。"
    call gl(0,"evcc0052")
    call vsp(0,1)
    with ImageDissolve("sys/EFMSK_22_MSK.bmp",time=1)
    太一 "「曜子ちゃん、ストップ」"
    曜子 "「……」"
    "驚く様子はなかった。"
    "たぶん、知っていたのだろう。"
    voice "vfCCC3012akri001"
    霧 "「……っ」"
    "隙と見て霧が動く。"
    "曜子ちゃん、投石。"
    voice "vfCCC3012akri002"
    霧 "「っっ！」"
    "起こりを突かれた霧には対処できない。"
    "ふくらはぎをしたたかに打つ。"
    voice "vfCCC3012akri003"
    霧 "「ぐっ！」"
    "すとんとうずくまる霧。"
    "足を抱えて、歯を食いしばる。激痛が走っているはずだ。"
    曜子 "「…………」"
    "二つ目の石を、ベルトに挟む。"
    "手首のバネをきかせて、残像の円盤を作る。瞬時。"
    voice "vfCCC3012akri004"
    霧 "「ちょ……っと……」"
    "霧の顔が青ざめる。"
    voice "vfCCC3012akri005"
    霧 "「ど、どうして……あなたが……？」"
    voice "vfCCC3012ayou002"
    曜子 "「太一を、殺そうとしたから」"
    voice "vfCCC3012akri006"
    霧 "「！？」"
    voice "vfCCC3012ayou003"
    曜子 "「太一を殺す練習をしていたから」"
    voice "vfCCC3012akri007"
    霧 "「……だ、だから……わたしを殺すんですか……？」"
    曜子 "「……」"
    "本気なのだろうか？"
    "とにかく、考える時ではない。"
    "予定通り行動するしかない。"
    voice "vfCCC3012akri008"
    霧 "「ああ……」"
    "回転数が増す。"
    "鋭い風切音。"
    "眼前で膨れあがる破壊力、霧は恐怖に射竦められる。"
    "死の確定。"
    "それが霧には信じられない。"
    "目の前で運動エネルギーがたくわえられていく。"
    voice "vfCCC3012akri009"
    霧 "「や、やめてぇ……」"
    "クロスボウを顔の前に構えて、すすり泣いた。"
    "霧の限界だ。"
    太一 "「そこまでだよ」"
    "霧の前に立つ。"
    voice "vfCCC3012akri010"
    霧 "「え……？」"
    "回転が落ちた。"
    voice "vfCCC3012ayou005"
    曜子 "「それは、生かしておくと太一に危害を加える」"
    太一 "「いいじゃないか、別に」"
    太一 "「……いいだろ？」"
    曜子 "「…………」"
    太一 "「好きにさせよう」"
    voice "vfCCC3012ayou007"
    曜子 "「……だめ」"
    太一 "「曜子ちゃん」"
    "強く名を呼ぶ。"
    "けど引き下がる様子はない。"
    "それでも霧を殺す気なのか？"
    "わからない。"
    voice "vfCCC3012ayou008"
    曜子 "「取るの」"
    太一 "「取らなくていい」"
    voice "vfCCC3012ayou009"
    曜子 "「どいて」"
    太一 "「どかない」"
    "背後で、霧が息を詰めて見守っている。"
    "命が助かった安堵と、俺に仲裁されたことへの違和。"
    voice "vfCCC3012ayou010"
    曜子 "「でも……」"
    "迷いがさす。"
    太一 "「俺を理由にして、人殺しなんてしてもらいたくないね」"
    太一 "「殺したいなら自分の理由でやってくれ」"
    "彼女は怯む。"
    "演技かも知れない。"
    voice "vfCCC3012ayou011"
    曜子 "「…………だって、太一のために……私は……」"
    "俺のため。"
    "俺の名前を出して霧を殺す。"
    "そのことが、結果として俺を傷つけるとも考えず。"
    太一 "「……いつだってそうだ。自分の気持ちだけを押しつけて」"
    太一 "「迷惑なときだって―――」"
    "曜子ちゃんが手首をひねった。"
    太一 "「……」"
    "横から首を出して会話をうかがっていた霧。"
    "その顔面の前にてのひらを置く。"
    "石が当たるかと思ったが、外れて背後の幹を叩き割った。"
    voice "vfCCC3012akri011"
    霧 "「きゃっ！？」"
    太一 "「……」"
    "……外した。"
    "やはり演技か。"
    "協力してくれている？"
    "しかしなぜ？"
    "曜子ちゃんが青ざめる。"
    voice "vfCCC3012ayou012"
    曜子 "「あ……ごめん……許して……」"
    "一瞬、混乱する。"
    "が、予定通りに進めた。"
    太一 "「裏切ったな」"
    voice "vfCCC3012ayou013"
    曜子 "「……え……あの……だから……」"
    太一 "「会話中に俺の隙を突こうとしたな」"
    太一 "「……またか」"
    "びくっと、彼女の肩が震えた。"
    太一 "「大切だと言う。愛してると言う。好意を押しつける」"
    太一 "「……なのに、ここぞという時に裏切る」"
    太一 "「またか」"
    voice "vfCCC3012ayou014"
    曜子 "「違う、それはつまり……太一の身の安全が……」"
    "しどろもどろ。"
    "さすが、演技ともなると……うまいな。"
    "二人で全部の役をやったんだもんな。"
    "さあ、うまくやってくれよ。"
    "内心、微笑む。"
    太一 "「その話はもういい！」"
    "一喝された幼女の如く、すくみあがった。"
    call gl(0,"bgcc0000d")
    call vsp(0,1)
    with Dissolve(500.0/1000.0)
    "……………………。"
    stop bgm
    "曜子ちゃんは去った。"
    "霧から武器と、抵抗する意志をごっそり奪って。"
    太一 "「……………………」"
    call gl(0,"bgcc0024")
    call vsp(0,1)
    with Dissolve(500.0/1000.0)
    "背後、緊張の発生源がまだオーラを放出し続けている。"
    play bgm "bgm/bgm020.ogg"
    "ゆっくりと怒りに転化していくそれを意識しつつ、"
    太一 "「……怪我は？」"
    call gl(1,"TCSK0002c|TCSK000x")
    call gp(1,t=center)#x=220
    call vsp(1,1)
    with dissolve
    voice "vfCCC3012akri016"
    霧 "「どうして」"
    "俺に助けられたことへの戸惑いや怒り。"
    "感情がもつれて、怒鳴りつけたいのを必死で抑えている。"
    "そんなくぐもった声だった。"
    call gl(1,"TCSK0001c|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3012akri017"
    霧 "「どうして……助けたんです……」"
    太一 "「どうしてって……言われてもなぁ」"
    太一 "「助けたかったからそうした、じゃダメかな」"
    call gl(1,"TCSK0004c|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3012akri018"
    霧 "「ふざけないでください……」"
    太一 "「……ふざけてはないけど」"
    太一 "「ま、そうだよな。納得はいかんわな」"
    太一 "「嫌っていた相手に助けられるというのは」"
    voice "vfCCC3012akri019"
    霧 "「……」"
    太一 "「本気で俺のこと、殺す気だったの？」"
    call gl(1,"TCSK0002c|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3012akri020"
    霧 "「…………」"
    太一 "「まいったな、どーも」"
    call gl(1,"TCSK0001c|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3012akri021"
    霧 "「あなたは危険すぎます」"
    太一 "「危険？」"
    voice "vfCCC3012akri022"
    霧 "「自分が楽しむために人を弄ぶあなたは」"
    call gl(1,"TCSK0021c|TCSK0021")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3012akri023"
    霧 "「こんな状況で、何も変わらないあなたはっ」"
    "突如として、声を荒げかける。"
    "すぐにトーンを落とす。"
    call gl(1,"TCSK0002c|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3012akri024"
    霧 "「……面白半分で、人を殺します」"
    "空気が澱む。"
    "憎悪が混入しているのだ。"
    "霧の吐き出す憎しみを。"
    太一 "「もう殺さない」"
    call gl(1,"TCSK0003c|TCSK0003")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3113kri000"
    霧 "「……え？」"
    太一 "「もう殺したくない」"
    call gl(1,"TCSK0000c|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3113kri001"
    霧 "「なにを……？」"
    太一 "「霧、俺だって自分が何者かくらい知ってる」"
    太一 "「もう破滅はいやだ」"
    太一 "「そんな記憶もいやだ」"
    太一 "「だから俺は闘う」"
    太一 "「自分と、闘うんだ」"
    霧 "「……………………」"
    voice "vfCCC3113kri003"
    霧 "「なぜ……」"
    voice "vfCCC3012akri030"
    霧 "「なぜわたしを助けたんです？」"
    "再度問いかけて来た。"
    call gl(1,"TCSK0003c|TCSK0003")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3012akri031"
    霧 "「見殺しにすればよかった」"
    voice "vfCCC3012akri032"
    霧 "「わたしがあなたのことを敵視していたのは……知ってるはずなのに……」"
    voice "vfCCC3012akri033"
    霧 "「わたしを助けても何の得にもならない」"
    太一 "「得さ」"
    太一 "「霧が生きて、俺の心に影響を与えてくれるなら……それは得なんだ」"
    太一 "「前に話したろう？」"
    call gl(1,"TCSK0000c|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3113kri004"
    霧 "「……あ……」"
    太一 "「それに霧が死んだら美希が悲しむ」"
    太一 "「霧の本意ではないだろう？」"
    call gl(1,"TCSK0002c|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3113kri005"
    霧 "「……はい」"
    "うん。"
    "ほんの少し、素直な霧だ。"
    "不必要にからかわなければいい。"
    太一 "「ここらへんにしておこう。霧だってそう簡単には納得できないだろうし」"
    太一 "「しっかし、すっげえ威力」"
    "投石が木に穿った穴。"
    "完全に内部にめり込んでいた。"
    call gl(1,"TCSK0004c|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3113kri006"
    霧 "「……」"
    太一 "「さ、帰ろうぜ」"
    call gl(1,"TCSK0000c|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3113kri007"
    霧 "「黒須先輩が……わからなくなりました」"
    太一 "「そうか」"
    "ただ、欺いているだけ。"
    "自分のために。"
    "霧はどこまでも、人が正しい状態でいてくれることを期待してしまうのだろう。"
    太一 "「あと曜子ちゃんの言ったこと、本気だと思う」"
    call gl(1,"TCSK0004c|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3113kri008"
    霧 "「？」"
    "口元をぬぐいながら、霧は眉をひそめた。"
    太一 "「もう武器はなしだ。持たない方がいい」"
    太一 "「破ったら、たぶん本気で襲ってくると思うよ」"
    call gl(1,"TCSK0003c|TCSK0003")
    call vsp(1,1)
    with dissolve
    霧 "「…………」"
    "肩が小さく震える。"
    "恐怖で。"
    太一 "「俺のそばにいれば、平気だと思うけど」"
    太一 "「一番いいのは、俺と敵対しないことなんだ」"
    call gl(1,"TCSK0000c|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3113kri010"
    霧 "「……敵対……しない？」"
    太一 "「一緒にいようってことだな」"
    call gl(1,"TCSK0004c|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3113kri011"
    霧 "「そんなの……」"
    太一 "「いやか？　でもこればかりはな。勝手にまとわりつかせてもらう」"
    call gl(1,"TCSK0000c|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3113kri012"
    霧 "「一つ訊いてもいいですか？」"
    太一 "「ん？」"
    voice "vfCCC3113kri013"
    霧 "「豊のこと」"
    太一 "「……ああ、その件か」"
    太一 "「今じゃなくてもいいかな？」"
    call gl(1,"TCSK0004c|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3113kri014"
    霧 "「……どうしてですか？　今だとまずいんですか？」"
    太一 "「霧の心が落ち着いてからの方がいいだろ」"
    call gl(1,"TCSK0003c|TCSK0003")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3113kri015"
    霧 "「落ち着いて……」"
    太一 "「るようには見えない」"
    "黙り込む。"
    call gl(1,"TCSK0000c|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3113kri016"
    霧 "「あの……先週のゲリラ合宿……あれは……？」"
    太一 "「あー……つまらなかったな、あれ」"
    太一 "「無理矢理セッティングして、苦労して７人集めて、なだめすかしたり嘘ついたりして……」"
    太一 "「あっという間にボロが出て」"
    "笑ってしまう。"
    "霧は異質なものでも見る目つきを、俺に投げかけている。"
    太一 "「最悪の気分で撤収したよな」"
    call gl(1,"TCSK0001c|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3113kri017"
    霧 "「……あなたが仕組んだことじゃないんですか？」"
    太一 "「そう、俺が仕組んだ」"
    voice "vfCCC3113kri018"
    霧 "「皆の傷口を広げるために？」"
    太一 "「違う」"
    太一 "「……ただ、何気ない日常を、取り戻したかった」"
    call gl(1,"TCSK0002c|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3113kri019"
    霧 "「……信じることはできません」"
    太一 "「だろうね」"
    call gl(1,"TCSK0000c|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3113kri020"
    霧 "「でも、疑うこともやめておきます」"
    太一 "「うん……さんきゅう」"
    太一 "「さて、そっちの怪我だな」"
    call gl(1,"TCSK0003c|TCSK0003")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3012akri076"
    霧 "「あ、平気です……さわらないでっ」"
    太一 "「さわらにゃわからん、と」"
    "ふくらはぎ。"
    "腫れている。"
    太一 "「……内出血だな。いい場所に当たった」"
    太一 "「歩くと痛むけど、別状はなし」"
    太一 "「他には？」"
    call gl(1,"TCSK0000c|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3012akri077"
    霧 "「肩を……」"
    太一 "「はだけて」"
    call gl(1,"TCSK0003c|TCSK0003")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3012akri078"
    霧 "「！？」"
    voice "vfCCC3012akri079"
    霧 "「や、やっぱりケダモノ……」"
    "肩を抱いて、後ずさる。"
    太一 "「おいおい、冗談だよ。本気にするな」"
    call gl(1,"TCSK0001c|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3012akri080"
    霧 "「そうやって美希や他の人にもセクハラを……してるじゃないですか」"
    太一 "「美希はなー、本気でイヤってことはちゃんと拒否するぞ？」"
    太一 "「それはだめー、なんてけたけた笑いながらぶん殴ってくるんだからな？」"
    call gl(1,"TCSK0003c|TCSK0003")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3012akri081"
    霧 "「……美希が？」"
    太一 "「そしたら俺も、無理強いはしない」"
    太一 "「いろんな接触をして境界線を調整していくのが、人付き合いってやつだろ？　違うのか？」"
    call gl(1,"TCSK0002c|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3012akri082"
    霧 "「……キレイな物言いでまとめるんですね……セクハラなのに……」"
    太一 "「霧ちんは生真面目に受け取りすぎだ」"
    太一 "「肩に触るぞ」"
    call gl(1,"TCSK0003c|TCSK0003")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3012akri083"
    霧 "「え……きゃっ」"
    "軽く揉んだら、痛がった。"
    太一 "「……こっちはまずい箇所に当たったな」"
    太一 "「どのくらい痛い？」"
    call gl(1,"TCSK0000c|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3012akri084"
    霧 "「……ほとんど……腕も動きます……」"
    太一 "「頭上に持ち上げなさい」"
    "従う。"
    太一 "「骨に異常はないな」"
    call gl(1,"TCSK0002c|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3012akri085"
    霧 "「……先輩が、力を入れすぎるんです」"
    太一 "「そんな入れてないよ」"
    call gl(1,"TCSK0000c|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3012akri086"
    霧 "「……男の人は、みんな力強いじゃないですか……島先輩とかだって、あんな細いのに一人でモニター持ち上げるし」"
    太一 "「……あいつは元バスケ部で……走れないだけで筋力はそのままだから」"
    太一 "「ま、湿布は張っておくんだぞ」"
    call gl(1,"TCSK0002c|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3113kri021"
    霧 "「……わかっています」"
    太一 "「よし、じゃ帰るか」"
    "立ち上がる。"
    太一 "「ほれ、行こう」"
    "不承不承、ついてくる。"
    call gl(1,"TCSK0002c|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3012akri088"
    霧 "「痛っ」"
    太一 "「やっぱ痛むか」"
    call gl(1,"TCSK0000c|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3113kri022"
    霧 "「……先に行ってください。一人で帰れます」"
    太一 "「ほら、乗れ」"
    "背中を。"
    call gl(1,"TCSK0003c|TCSK0003")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3113kri023"
    霧 "「……い、いいですっ」"
    太一 "「はやく」"
    call gl(1,"TCSK0021c|TCSK0021")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3113kri024"
    霧 "「いいですってば！」"
    太一 "「曜子ちゃん、いるかもよ？」"
    call gl(1,"TCSK0003c|TCSK0003")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3113kri025"
    霧 "「……だとしても……」"
    太一 "「ＯＫ。じゃ先輩命令。はやくおぶされ」"
    call gl(1,"TCSK0000c|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3113kri026"
    霧 "「……ず、ずるい、です」"
    太一 "「はーやーく」"
    "しぶしぶ。"
    hide pic1
    with dissolve
    "霧はおぶさってきた。"
    太一 "「家まで運んでやるよ」"
    voice "vfCCC3113kri027"
    霧 "「……そんなの無理だと思います……重くないんですか？」"
    太一 "「これが重い？　冗談だろ？」"
    "異様に軽い。"
    "歩き出す。"
    "踏みしめる草木の音が、さくさくと小気味よい。"
    太一 "「いい夜だ。な？」"
    voice "vfCCC3113kri028"
    霧 "「……さあ」"
    stop bgm
    call gl(0,"bgcc0000d")
    call vsp(0,1)
    with Dissolve(500.0/1000.0)
    pause (500.0/1000.0)
    pause (500.0/1000.0)
    call gl(0,"bgcc0003")
    call vsp(0,1)
    with Dissolve(500.0/1000.0)
    太一 "「金曜日、か」"
    "世界が揺り戻されるまで、あと三日。"
    "今日もなすべきことをしよう。"
    play bgm "bgm/bgm013.ogg"
    call gl(0,"bgcc0011")
    call vsp(0,1)
    with wipeleft
    "玄関先で、霧を見た。"
    "というか、下駄箱によっかかっていた。"
    "明らかに俺に見えるように。"
    "声を掛けた方がいいんだろうな。"
    太一 "「怪我の調子はどうか」"
    call gl(1,"TCSK0000|TCSK000x")
    call gp(1,t=center)#x=190
    call vsp(1,1)
    with dissolve
    voice "vfCCC3114kri000"
    霧 "「……平気です。多少、痛みますけど」"
    太一 "「家で休んでいればいいのに」"
    voice "vfCCC3114kri001"
    霧 "「いえ、そんな怪我ではありませんから」"
    太一 "「美希は？」"
    call gl(1,"TCSK0002|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3114kri002"
    霧 "「……今日は、来ないそうです」"
    voice "vfCCC3114kri003"
    霧 "「ナーバスになってるみたいで」"
    "経験値が０に戻って以来、美希は脆くなった。"
    "いや、本来の美希に戻ったのか。"
    "……人、いなくなってるんだもんなぁ。"
    太一 "「……元気ないよな、あいつ」"
    call gl(1,"TCSK0000|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3114kri004"
    霧 "「はい……無理してますから、いろいろ」"
    太一 "「暑いし」"
    "太陽を見あげた。"
    太一 "「海、行きたいな」"
    太一 "「去年は行ったよな。覚えてるか？」"
    voice "vfCCC3015kri002"
    霧 "「……はい」"
    太一 "「楽しかったな。美希には悪いけど」"
    voice "vfCCC3015kri003"
    霧 "「……はい」"
    "海か。"
    "今年は行かなかった。"
    "一人で行っても仕方ないしな。"
    "残り三日。"
    "俺は暗い衝動に支配されずに、ことをなせるのか？"
    "健全なものが欲しかった。"
    "無性に。"
    stop bgm
    太一 "「海行くか？」"
    call gl(1,"TCSK0003|TCSK0003")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3114kri005"
    霧 "「……え、海ですか？」"
    太一 "「美希も誘ってさ。三人で」"
    call gl(1,"TCSK0000|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3114kri006"
    霧 "「……美希も……」"
    太一 "「よし、行こう！」"
    voice "vfCCC3114kri007"
    霧 "「そ、そんな勝手に……」"
    "手を取る。"
    play bgm "bgm/bgm005.ogg"
    call gl(1,"TCSK0003|TCSK0003")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3114kri008"
    霧 "「きゃ？」"
    太一 "「美希を誘いに行こう」"
    voice "vfCCC3114kri009"
    霧 "「だって、水着持ってきてない」"
    太一 "「美希団地のそばにある雑貨屋に置いてあるよ」"
    voice "vfCCC3114kri010"
    霧 "「わたしの意志が」"
    太一 "「おまえね、助けてやったんだからデート一回くらいつきあえ」"
    call gl(1,"TCSK0007|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3114kri011"
    霧 "「で、でーとっ？」"
    太一 "「両手に花デート」"
    call gl(1,"TCSK0002|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3114kri012"
    霧 "「……そ、そういうのは……」"
    太一 "「いいからいいから、ＧＯ！」"
    hide pic1
    with dissolve
    voice "vfCCC3114kri013"
    霧 "「あ、ちょっと、先輩……っ」"
    "多少は強引に。"
    "そして。"
    call gl(0,"bgcc0014")
    call vsp(0,1)
    call vsp(1,0)
    with wipeleft
    "げっそりノイローゼになっていた美希を引っ張り出し、"
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
    call gp(1,t=center)#x=180
    call vsp(1,1)
    with dissolve
    voice "vfCCC3114mki000"
    美希 "「……うー」"
    call gl(2,"TCSK0002aa|TCSK000xa")
    call gp(1,t=left)
    call gp(2,t=right)
    call vsp(1,1)
    call vsp(2,1)
    with Dissolve(500.0/1000.0)
    voice "vfCCC3114kri014"
    霧 "「……むー」"
    太一 "「あー、いい、いいなあ！」"
    "清純派でも通用しそうなひかえめ思春期ボディだった。"
    call gl(1,"TCYM0001aa|TCYM000xa")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3114mki001"
    美希 "「なんか……視線を感じる」"
    call gl(2,"TCSK0002aa|TCSK000xa")
    call vsp(2,1)
    with dissolve
    voice "vfCCC3114kri015"
    霧 "「感じるね……」"
    voice "vfCCC3114mki002"
    美希 "「なんかあったら守ってね？」"
    voice "vfCCC3114kri016"
    霧 "「ごめん、無理かも」"
    "ビルダーのようにポージングを繰り返す俺は、かなり末期的に見えたらしい。"
    太一 "「じゃ遊ぼうか」"
    call gl(1,"TCYM0000aa|TCYM000xa")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3114mki003"
    美希 "「あーあーあー、霧ちんボールいったボール！」"
    call gl(2,"TCSK0000aa|TCSK000xa")
    call vsp(2,1)
    with dissolve
    voice "vfCCC3114kri017"
    霧 "「無理無理、今無理だってば！」"
    太一 "「そら、髪の毛を濡らしてやる！」"
    call gl(2,"TCSK0002aa|TCSK000xa")
    call vsp(2,1)
    with dissolve
    voice "vfCCC3114kri018"
    霧 "「やめてー！」"
    call gl(1,"TCYM0003aa|TCYM000xa")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3114mki004"
    美希 "「あー、ボールが落ちるー！」"
    call gl(2,"TCSK0002aa|TCSK000xa")
    call vsp(2,1)
    with dissolve
    voice "vfCCC3114kri019"
    霧 "「無理だってばー！」"
    太一 "「うわっ！」"
    play se "SE081"
    with vpunch
    call gl(2,"TCSK0000aa|TCSK000xa")
    call vsp(2,1)
    with dissolve
    voice "vfCCC3114kri020"
    霧 "「あ、チャンス……えい！」"
    call gl(1,"TCYM0000aa|TCYM000xa")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3114mki005"
    美希 "「おー、うまーい！」"
    太一 "「あーっとっとっとっ！」"
    太一 "「どわあっ！？」"
    play se "SE081"
    with vpunch
    voice "vfCCC3114kri021"
    霧 "「……ぷっ」"
    call gl(1,"TCYM0003aa|TCYM000xa")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3114mki006"
    美希 "「あはははは、先輩二回連続で転んでるー」"
    太一 "「あー、取られた」"
    太一 "「サーブ権はそっちだな」"
    call gl(1,"TCYM0000aa|TCYM000xa")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3114mki007"
    美希 "「よーし、いきまーす！　てあー！」"
    太一 "「撃墜！」"
    voice "vfCCC3114mki008"
    美希 "「あ、うまい」"
    call gl(2,"TCSK0000aa|TCSK000xa")
    call vsp(2,1)
    with dissolve
    voice "vfCCC3114kri022"
    霧 "「任せて……それっ」"
    太一 "「お、やるな！」"
    voice "vfCCC3114kri023"
    霧 "「二対一ですから、負けません」"
    太一 "「ここは順当にレシーブっと」"
    call gl(1,"TCYM0003aa|TCYM000xa")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3114mki009"
    美希 "「精密射撃～」"
    太一 "「わぶっ」"
    voice "vfCCC3114mki010"
    美希 "「あったりぃ！」"
    太一 "「あれ、今ので本体ダメージいくつだ？」"
    call gl(2,"TCSK0002aa|TCSK000xa")
    call vsp(2,1)
    with dissolve
    voice "vfCCC3114kri024"
    霧 "「……あと三点ですよ」"
    太一 "「やべ……」"
    call gl(2,"TCSK0000aa|TCSK000xa")
    call vsp(2,1)
    with dissolve
    voice "vfCCC3114kri025"
    霧 "「じゃ、サーブいきます」"
    太一 "「おー、本気で来い！」"
    call gl(1,"TCYM0001aa|TCYM000xa")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3114mki011"
    美希 "「ぴゅー」"
    太一 "「おいおい、最初のレシーブまでは本体攻撃なしだって！」"
    call gl(1,"TCYM0003aa|TCYM000xa")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3114mki012"
    美希 "「えー、撃ってませんよ。口で言っただけー」"
    太一 "「卑怯なことを！」"
    太一 "「そら、レシーブ！　攻撃開始！」"
    call gl(1,"TCYM0000aa|TCYM000xa")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3114mki013"
    美希 "「ひょいっと」"
    太一 "「ちっ、外したか！」"
    voice "vfCCC3114kri026"
    霧 "「そーれっ！」"
    太一 "「あ、まずいコース……」"
    call gl(1,"TCYM0003aa|TCYM000xa")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3114mki014"
    美希 "「霧ちん合体攻撃！」"
    call gl(2,"TCSK0002aa|TCSK000xa")
    call vsp(2,1)
    with dissolve
    voice "vfCCC3114kri027"
    霧 "「おーけー」"
    太一 "「わっわっわっ……そりゃ！」"
    voice "vfCCC3114mki015"
    美希 "「うあー、全部よけたー！」"
    call gl(2,"TCSK0002aa|TCSK000xa")
    call vsp(2,1)
    with dissolve
    voice "vfCCC3114kri028"
    霧 "「……サルみたい」"
    太一 "「こっちもいくぞー！　こら、こっちがレシーブしたらそっちの攻撃権はナシ」"
    call gl(1,"TCYM0000aa|TCYM000xa")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3114mki016"
    美希 "「あ、ごめんなさい」"
    太一 "「レシーブしたら、相手の捕球に対してこっちが攻撃じゃ！　せやー！　一掃～！」"
    call gl(2,"TCSK0002aa|TCSK000xa")
    call vsp(2,1)
    with dissolve
    voice "vfCCC3114kri029"
    霧 "「きゃっ、ちょっと先輩！　そういう雨っぽい水じゃ有効打として認めれないですよ」"
    太一 "「む……電池が切れてきた……かな？」"
    call gl(1,"TCYM0003aa|TCYM000xa")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3114mki017"
    美希 "「ふっふっふー、こっちは交互に撃ってたからまだまだ攻撃できますもん！」"
    太一 "「……えーい、そのくらいのハンデは納得済みだー！」"
    太一 "「攻撃できなくても、純粋にバレーだけで十分だね！」"
    call gl(1,"TCYM0000aa|TCYM000xa")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3114mki018"
    美希 "「……だって？」"
    call gl(2,"TCSK0000aa|TCSK000xa")
    call vsp(2,1)
    with dissolve
    voice "vfCCC3114kri030"
    霧 "「強気だね」"
    call gl(1,"TCYM0001aa|TCYM000xa")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3114mki019"
    美希 "「うん、すっごく強気。いっつもそう」"
    voice "vfCCC3114kri031"
    霧 "「でも空元気だね」"
    call gl(1,"TCYM0003aa|TCYM000xa")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3114mki020"
    美希 "「うん、見栄っ張りだよね」"
    太一 "「こらー、本人を前にして陰口叩くなー！」"
    voice "vfCCC3114mki021"
    美希 "「止まってると、狙撃ー！」"
    voice "vfCCC3114kri032"
    霧 "「狙撃ー！」"
    太一 "「うわあっ！」"
    play se "SE081"
    with vpunch
    voice "vfCCC3114mki022"
    美希 "「ミキリチームの勝ちー！」"
    voice "vfCCC3114kri033"
    霧 "「……ＯＫ！」"
    "ビーチバレーとサバゲーを組み合わせた高度な遊びを、俺たちは楽しんだ。"
    call gl(0,"bgcc0020")
    call vsp(0,1)
    call vsp(1,0)
    call vsp(2,0)
    with wipeleft
    "そして昼食。"
    太一 "「ふいー……フィールドが海の中だと疲れるー」"
    call gl(1,"TCYM0003aa|TCYM000xa")
    call gp(1,t=center)#x=180
    call vsp(1,1)
    with dissolve
    voice "vfCCC3114mki023"
    美希 "「美希もですー」"
    call gl(2,"TCSK0000aa|TCSK000xa")
    call gp(1,t=left)
    call gp(2,t=right)
    call vsp(1,1)
    call vsp(2,1)
    with Dissolve(500.0/1000.0)
    voice "vfCCC3114kri034"
    霧 "「お待ちどう」"
    "霧が戻ってくる。"
    voice "vfCCC3114kri035"
    霧 "「ガスが使えたから、ちょっと火使えてよかった」"
    call gl(1,"TCYM0000aa|TCYM000xa")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3114mki024"
    美希 "「いいのかなー、勝手に海の家使っちゃって」"
    太一 "「いーんだよ、こんなご時世だし」"
    call gl(1,"TCYM0001aa|TCYM000xa")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3114mki025"
    美希 "「……あー、それはあまり考えたくない～」"
    call gl(2,"TCSK0001aa|TCSK000xa")
    call vsp(2,1)
    with dissolve
    voice "vfCCC3114kri036"
    霧 "「先輩、わたしの美希をいじめないでくださいっ」"
    太一 "「……おまえのかい」"
    call gl(2,"TCSK0002aa|TCSK000xa")
    call vsp(2,1)
    with dissolve
    voice "vfCCC3114kri037"
    霧 "「そーですよ。あげません」"
    太一 "「半分は俺のだ！」"
    call gl(1,"TCYM0001aa|TCYM000xa")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3114mki026"
    美希 "「……分割統治される敗戦国みたいな身にされている……」"
    voice "vfCCC3114kri038"
    霧 "「認めません」"
    太一 "「よこせー」"
    call gl(1,"TCYM0000aa|TCYM000xa")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3114mki027"
    美希 "「わーんっ、いたいよー」"
    call gl(2,"TCSK0000aa|TCSK000xa")
    call vsp(2,1)
    with dissolve
    voice "vfCCC3114kri039"
    霧 "「……あ」"
    太一 "「わーい、俺のー」"
    call gl(1,"TCYM0001aa|TCYM000xa")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3114mki028"
    美希 "「いえ、先輩、今のは霧ちんの勝ちですよ」"
    太一 "「なぜだ！　俺が引っ張り勝ったんだぞ？」"
    call gl(1,"TCYM0001aa|TCYM000xa")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3114mki029"
    美希 "「左右に引っ張られた子供が痛がったのを見て、霧ちんは手を離した……その優しさこそ、本当の親の愛なのですよ」"
    太一 "「がーん」"
    call gl(1,"TCYM0003aa|TCYM000xa")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3114mki030"
    美希 "「というわけで霧ちんの勝ち」"
    call gl(2,"TCSK0000aa|TCSK000xa")
    call vsp(2,1)
    with dissolve
    voice "vfCCC3114kri040"
    霧 "「……はいいから、はやく食べよう？　冷めちゃう」"
    太一 "「にしても、カップラーメンと缶詰とモチってのがなぁ」"
    call gl(2,"TCSK0002aa|TCSK000xa")
    call vsp(2,1)
    with dissolve
    voice "vfCCC3114kri041"
    霧 "「贅沢言わないでください、これでもマシな方です」"
    call gl(1,"TCYM0000aa|TCYM000xa")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3114mki031"
    美希 "「海の家っぽいですよ、ラーメン」"
    太一 "「そうだね」"
    voice "vfCCC3114mki032"
    美希 "「あ、そういえば霧、あれは？」"
    call gl(2,"TCSK0000aa|TCSK000xa")
    call vsp(2,1)
    with dissolve
    voice "vfCCC3114kri042"
    霧 "「ん？」"
    voice "vfCCC3114mki033"
    美希 "「えーと、そのー」"
    "ちらっと俺を見る。"
    太一 "「聞かれたくない話？　それとも俺に告白するって話？」"
    voice "vfCCC3114goo000"
    call gl(2,"TCSK0002aa|TCSK000xa")
    call vsp(2,1)
    with dissolve
    二人 "「しません」"
    太一 "「……そのハモハモ、ムカツク」"
    太一 "「どいてようか？」"
    call gl(1,"TCYM0000aa|TCYM000xa")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3114mki035"
    美希 "「あ、いいです」"
    call gl(1,"TCYM0003aa|TCYM000xa")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3114mki036"
    美希 "「……にゃん」"
    "鳴いた。"
    call gl(2,"TCSK0002aa|TCSK000xa")
    call vsp(2,1)
    with dissolve
    voice "vfCCC3114kri044"
    霧 "「みー」"
    call gl(1,"TCYM0000aa|TCYM000xa")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3114mki037"
    美希 "「ごろにゃーごろ」"
    call gl(2,"TCSK0000aa|TCSK000xa")
    call vsp(2,1)
    with dissolve 
    voice "vfCCC3114kri045"
    霧 "「……にゃーにゃー」"
    call gl(1,"TCYM0001aa|TCYM000xa")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3114mki038"
    美希 "「にゃ！」"
    call gl(2,"TCSK0001aa|TCSK000xa")
    call vsp(2,1)
    with dissolve
    voice "vfCCC3114kri046"
    霧 "「なーご！」"
    call gl(2,"TCSK0000aa|TCSK000xa")
    call vsp(2,1)
    with dissolve
    voice "vfCCC3114kri047"
    霧 "「にゃんにゃかにゃんっ」"
    call gl(1,"TCYM0003aa|TCYM000xa")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3114mki039"
    美希 "「にゃあん……」"
    voice "vfCCC3114kri048"
    霧 "「……うにゃ？」"
    call gl(1,"TCYM0000aa|TCYM000xa")
    call vsp(1,1)
    with dissolve 
    voice "vfCCC3114mki040"
    美希 "「なーん……」"
    太一 "「ね、猫語？」"
    "美希と霧はにゃーにゃー鳴きあった。"
    太一 "「は、はわわ……コワー」"
    "ほどなくして。"
    call gl(1,"TCYM0000aa|TCYM000xa")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3114mki041"
    美希 "「そっか。一日はやく終わりましたか」"
    "腕を組んで、うんうん頷く。"
    call gl(2,"TCSK0000aa|TCSK000xa")
    call vsp(2,1)
    with dissolve
    voice "vfCCC3114kri049"
    霧 "「……こーら、言わない」"
    voice "vfCCC3114mki042"
    美希 "「あ、ゴミン」"
    太一 "「今ので通じてるのかよ」"
    "美処女ガールズは、独自の言語体系を造作りあげてしまったのかよ！"
    太一 "「お、俺にも教えてよ」"
    call gl(1,"TCYM0001aa|TCYM000xa")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3114mki043"
    美希 "「……無理っす」"
    太一 "「どうして？」"
    call gl(2,"TCSK0002aa|TCSK000xa")
    call vsp(2,1)
    with dissolve
    voice "vfCCC3114kri050"
    霧 "「……先輩は、猫っぽくないから」"
    太一 "「俺すっごい猫っぽいよ！」"
    call gl(1,"TCYM0000aa|TCYM000xa")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3114mki044"
    美希 "「えー、どこがー？」"
    太一 "「いいか、見てろよ」"
    "目を覆う。"
    "カシャ―――"
    太一 "「ほら、暗いところで目が光る！」"
    "今俺たちがいる海の家は薄暗いのだ。"
    call gl(1,"TCYM0003aa|TCYM000xa")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3114mki045"
    美希 "「わー、なつかしー！　ほらほら霧ちん、言った通りでしょ？」"
    call gl(2,"TCSK0000aa|TCSK000xa")
    call vsp(2,1)
    with dissolve
    voice "vfCCC3114kri051"
    霧 "「本当だ……光ってる」"
    太一 "「資格充分と言える」"
    call gl(1,"TCYM0000aa|TCYM000xa")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3114mki046"
    美希 "「……不思議ー」"
    voice "vfCCC3114kri052"
    霧 "「コンタクトですか？」"
    太一 "「違うよ。天然。しかも切り替え自由」"
    "目を閉じる。"
    "カシャ―――"
    太一 "「ノーマルモード」"
    call gl(1,"TCYM0003aa|TCYM000xa")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3114mki047"
    美希 "「うおー、かっくいー」"
    call gl(2,"TCSK0002aa|TCSK000xa")
    call vsp(2,1)
    with dissolve
    voice "vfCCC3114kri053"
    霧 "「かっくいい……のかな？」"
    call gl(1,"TCYM0000aa|TCYM000xa")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3114mki048"
    美希 "「それ、確か暗いところでちゃんと見えるんですよね？」"
    太一 "「うん。夜目がきくんだよ」"
    call gl(2,"TCSK0000aa|TCSK000xa")
    call vsp(2,1)
    with dissolve
    voice "vfCCC3114kri054"
    霧 "「猫みたい」"
    太一 "「なんか、たまたま猫みたいな異常になっちゃったんだって。医者が言うには」"
    太一 "「下手したら幼少時から失明してたかもしれんのだ」"
    voice "vfCCC3114kri055"
    霧 "「……そうなんですか」"
    voice "vfCCC3114mki049"
    美希 "「あ、ちょっちトイレ……」"
    hide pic1
    with dissolve
    "すててててー。"
    太一 "「……俺もトイレ」"
    "ぐいっ"
    太一 "「うおっ？」"
    call gl(2,"TCSK0002aa|TCSK000xa")
    call vsp(2,1)
    with dissolve
    voice "vfCCC3114kri056"
    霧 "「…………のぞきは駄目です」"
    太一 "「ちぇっ」"
    hide pic2
    with dissolve
    "……………………。"
    太一 "「でも美希、良さそうだね」"
    call gl(2,"TCSK0000aa|TCSK000xa")
    call gp(2,t=center)#x=220
    call vsp(2,1)
    with dissolve
    voice "vfCCC3114kri057"
    霧 "「……息抜きが必要だったんですね」"
    太一 "「美希は、別に喜怒哀楽がないわけじゃないしね」"
    太一 "「無識ってわけでもないし、健常者とほとんど一緒で」"
    太一 "「人がいないってのは、こたえると思うよ、実際」"
    call gl(2,"TCSK0000aa|TCSK000xa")
    call vsp(2,1)
    with dissolve
    voice "vfCCC3114kri058"
    霧 "「……それはどうしようもないですね」"
    太一 "「霧は寂しくない？」"
    call gl(2,"TCSK0002aa|TCSK000xa")
    call vsp(2,1)
    with dissolve
    voice "vfCCC3114kri059"
    霧 "「……わたしは……どうでしょう」"
    voice "vfCCC3114kri060"
    霧 "「悪意はなくなりましたけど……けど」"
    霧 "「……」"
    太一 "「そうだな。俺たちの心って、周囲に人間って圧力があってはじめて成立するもんな。こういうのは……やっぱまずいよなぁ」"
    太一 "「ジレンマだ」"
    太一 "「心がなかったら人は獣だよな。けど……心があればあったで、いろいろ大変で」"
    太一 "「デリケートすぎるんだよな、人間の心は」"
    call gl(2,"TCSK0000aa|TCSK000xa")
    call vsp(2,1)
    with dissolve
    voice "vfCCC3114kri062"
    霧 "「……普通に、生きていればよかったんです」"
    voice "vfCCC3114kri063"
    霧 "「けど……こんな山奥に押し込められて……わたしたちが悪いみたいに」"
    太一 "「……ま、仕方ない」"
    太一 "「人を傷つけるレベルのやつが出てきちゃったんだからさ」"
    call gl(2,"TCSK0002aa|TCSK000xa")
    call vsp(2,1)
    with dissolve
    voice "vfCCC3114kri064"
    霧 "「……そうなんですけど」"
    太一 "「でも、霧はいい子だな」"
    voice "vfCCC3114kri065"
    霧 "「……ごほっ！」"
    call gl(2,"TCSK0000aa|TCSK000xa")
    call vsp(2,1)
    with dissolve
    voice "vfCCC3114kri066"
    霧 "「と、突然変なことを……」"
    太一 "「霧の頭はポワポワしていそうだな」"
    "霧は自分の頭を押さえる。"
    voice "vfCCC3114kri067"
    霧 "「え……そおですか？」"
    太一 "「触っていい？」"
    voice "vfCCC3114kri068"
    霧 "「……えっちな気持ちでは触らないでくださいね」"
    call gl(2,"TCSK0002aa|TCSK000xa")
    call vsp(2,1)
    with dissolve
    voice "vfCCC3114kri069"
    霧 "「わかりますから」"
    "わかるんかい。"
    "頭を撫でる。"
    太一 "「……ポワポワではないな。ほわほわだな」"
    voice "vfCCC3114kri070"
    霧 "「……違いがわたしにはわからない……」"
    太一 "「ま、とにかく頑張れよ！」"
    call gl(2,"TCSK0000aa|TCSK000xa")
    call vsp(2,1)
    with dissolve
    voice "vfCCC3114kri071"
    霧 "「え……何をです？」"
    太一 "「世界は悪意で満ちているけど、そこには必ず霧の領土もあるはずだから」"
    太一 "「……武器をつきつけて、奪い取る必要もないんだ。領土は」"
    voice "vfCCC3114kri072"
    霧 "「？？？」"
    call gl(1,"TCYM0000aa|TCYM000xa")
    call gp(1,t=center)#x=180
    call vsp(1,1)
    call vsp(2,0)
    with Dissolve(500.0/1000.0)
    voice "vfCCC3114mki050"
    美希 "「あー、仲良さそうなことしてるー！」"
    太一 "「仲いいもん」"
    "抱きしめた。"
    voice "vfCCC3114kri073"
    霧 "「きょ！？」"
    "きょ？"
    call gl(1,"TCYM0001aa|TCYM000xa")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3114mki051"
    美希 "「ジェラシーッ！」"
    "じたばたした。"
    voice "vfCCC3114mki052"
    美希 "「それも、複雑なダブルジェラシーっ！」"
    "続行してじたばたした。"
    call gl(1,"TCYM0003aa|TCYM000xa")
    call vsp(1,1)
    with dissolve
    extend "そして飛び込んできた。"
    hide pic1
    with dissolve
    with vpunch
    太一 "「わっ！」"
    voice "vfCCC3114kri074"
    霧 "「わっ！」"
    voice "vfCCC3114mki053"
    美希 "「ごろにゃーご」"
    "ぐるぐる回りながら、身を寄せてくる。"
    太一 "「あんまピタピタされると興奮しちゃうからやめてー……」"
    voice "vfCCC3114mki054"
    美希 "「ぴたぴた」"
    太一 "「こらこら」"
    voice "vfCCC3114mki055"
    美希 "「ぺろぺろ」"
    太一 "「やめれー！」"
    voice "vfCCC3114kri075"
    霧 "「よしなさいっ！！」"
    太一 "「あー、遅かった……」"
    play se "se107"
    "いったー！"
    voice "vfCCC3114kri076"
    霧 "「ぎゃああ！？」"
    voice "vfCCC3114mki056"
    美希 "「へ、変形！？」"
    voice "vfCCC3114kri077"
    霧 "「いやーーーーーーっ！」"
    voice "vfCCC3114mki057"
    美希 "「みゃーーーーーーーっ！」"
    太一 "「……お、おまえらが建立した五重塔だろうがー！　責任取れー！！　クギは一本も使ってないっちゅーねんっっ！！」"
    call gl(0,"bgcc0000d")
    call vsp(0,1)
    call vsp(1,0)
    call vsp(2,0)
    with Dissolve(500.0/1000.0)
    call gl(0,"bgcc0014a")
    call vsp(0,1)
    with wipeleft
    call gl(1,"TCYM0003b|TCYM0003")
    call gp(1,t=center)#x=180
    call vsp(1,1)
    with dissolve
    voice "vfCCC3114mki058"
    美希 "「楽しかったですー！」"
    太一 "「うむ。また行こう」"
    call gl(1,"TCYM0001b|TCYM0000")
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
    voice "vfCCC3114kri078"
    霧 "「ばいばい」"
    call gl(1,"TCYM0003b|TCYM0003")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3114mki062"
    美希 "「ばいばーい！」"
    hide pic1
    with dissolve
    stop bgm
    "美希が団地方面に走り去った。"
    太一 "「霧も送ろう」"
    call gl(1,"TCSK0002b|TCSK000x")
    call gp(1,t=center)#x=220
    call vsp(1,1)
    with Dissolve(500.0/1000.0)
    voice "vfCCC3114kri079"
    霧 "「……どうも」"
    太一 "「んー、腹減ったなぁ」"
    call gl(1,"TCSK0000b|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3114kri080"
    霧 "「食べ物は、あるんですか？」"
    太一 "「あー、あるある。友貴箱丸々残ってるし」"
    call gl(1,"TCSK0002b|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3114kri081"
    霧 "「……あの……寄っていきませんか？」"
    play bgm "bgm/bgm002.ogg"
    太一 "「え？」"
    call gl(1,"TCSK0000b|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3114kri082"
    霧 "「うちに。夕食くらいは、用意します」"
    太一 "「やけにサービスいいね」"
    voice "vfCCC3114kri083"
    霧 "「……あの、お話したいことが」"
    太一 "「聞きたい話が、では？」"
    "霧は一瞬、呼吸さえ停止させる。"
    call gl(1,"TCSK0002b|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3114kri084"
    霧 "「……はい、そうです」"
    call gl(1,"TCSK0000b|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3114kri085"
    霧 "「豊のこと、うかがいたいんです」"
    voice "vfCCC3114kri086"
    霧 "「スッキリさせたい……そうでないとわたし、あなたにどういう気持ちを抱いたらいいのか……わからないんです」"
    太一 "「そっか。んー」"
    "いや、金曜日は早すぎる。"
    太一 "「じゃあ明日、では駄目かな？」"
    voice "vfCCC3114kri087"
    霧 "「明日、ですか」"
    太一 "「全部話そう。昼くらいでもいいから来てくれよ」"
    "そう、全部。"
    "正直に。"
    call gl(1,"TCSK0002b|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3114kri088"
    霧 "「わかりました」"
    太一 "「学校で」"
    call gl(1,"TCSK0000b|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3114kri089"
    霧 "「はい、黒須先輩」"
    "折り目正しく。霧らしく。"
    "背筋を伸ばして。"
    voice "vfCCC3114kri090"
    霧 "「本日は、お世話になりました。失礼します」"
    "運動部ってノリで。"
    太一 "「うん、ばいばい」"
    hide pic1
    with dissolve
    "俺たちは別れた―――"
    stop bgm
    call gl(0,"bgcc0000d")
    call vsp(0,1)
    with Dissolve(500.0/1000.0)
    call gl(0,"bgcc0003")
    call vsp(0,1)
    with Dissolve(500.0/1000.0)
    "土曜日だ。"
    "……あと一日。"
    "あと一日なんだ。"
    play bgm "bgm/bgm004.ogg"
    call gl(0,"bgcc0006")
    call vsp(0,1)
    with wipeleft
    "教室に顔を出すと、美希だけがいた。"
    太一 "「霧はー？」"
    call gl(1,"TCYM0000|TCYM0000")
    call gp(1,t=center)#x=180
    call vsp(1,1)
    with Dissolve(500.0/1000.0)
    voice "vfCCC3115mki000"
    美希 "「あ、おはようです。霧ちんはまだです」"
    太一 "「そっか」"
    太一 "「写真できた？」"
    voice "vfCCC3115mki001"
    美希 "「これから現像するんですよーう」"
    call gl(1,"TCYM0003|TCYM0003")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3115mki002"
    美希 "「焼き増し一枚五千円ですからね」"
    太一 "「たけー！」"
    call gl(1,"TCYM0000|TCYM0000")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3115mki003"
    美希 "「あ、昼ご飯みんなで食べましょうね」"
    太一 "「うむ」"
    hide pic1
    with dissolve
    "待つことにした。"
    "……………………。"
    "昼になった。"
    太一 "「……お、おそいよ二人とも！！」"
    "腹減ったなぁ。"
    "一人で食っちゃおうかな。"
    "今日は握り飯だった。"
    "ふりかけなどがまぜてあり、いかにもうまそうだ。"
    call gl(1,"TCSK0000|TCSK000x")
    call gp(1,t=center)#x=220
    call vsp(1,1)
    with dissolve
    voice "vfCCC3116kri000"
    霧 "「おはようございます、黒須先輩」"
    太一 "「……遅いよ」"
    call gl(1,"TCSK0003|TCSK0003")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3116kri001"
    霧 "「え……昼でいいと言ったのは黒須先輩ですが」"
    太一 "「そうだっけ？」"
    "言った気がする……。"
    call gl(1,"TCSK0000|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3116kri002"
    霧 "「お話、うかがいに来ました」"
    太一 "「まあ、とりあえずメシにしよう」"
    太一 "「ほら、二人分くらいはあるよ」"
    call gl(1,"TCSK0002|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3116kri003"
    霧 "「はい……じゃ、いただきます……」"
    太一 "「いただきます」"
    "もぐもぐ"
    call gl(0,"evcc0051")
    call vsp(0,1)
    call vsp(1,0)
    with ImageDissolve("sys/EFMSK_22_MSK.bmp",time=1)
    太一 "「曜子ちゃんとか平気？　いやがらせされてない？」"
    霧 "「……」"
    太一 "「されたのか？」"
    voice "vfCCC3116kri005"
    霧 "「……家を出る時、ドアのところに……」"
    太一 "「ところに？」"
    voice "vfCCC3116kri006"
    霧 "「……めすぶた、って落書きしてありました」"
    太一 "「子供か……」"
    太一 "「ソレだけ？」"
    voice "vfCCC3116kri007"
    霧 "「今のところは」"
    太一 "「ま、何もしてこないならそれに越したことはない」"
    voice "vfCCC3019akri008"
    霧 "「……あの人は、どうしてあんな石投げがうまいんですか？」"
    voice "vfCCC3019akri009"
    霧 "「おかしいですよ、ゼッタイ」"
    太一 "「たいがいのことは上手だよ」"
    太一 "「根本的なデキが違うんだろう」"
    voice "vfCCC3019akri010"
    霧 "「特殊な訓練を受けてるとか？」"
    太一 "「あー、受けてたね。なんか長期休みごとに、どっかの外国とか行って現地の軍事インストラクター雇って」"
    voice "vfCCC3019akri011"
    霧 "「軍事っ……」"
    "絶句する。"
    太一 "「投石もその時に習ったのかな。もしかしたら本物の羊飼いから習ったのかも」"
    太一 "「まだ痛む？」"
    voice "vfCCC3019akri012"
    霧 "「……どうってことは」"
    太一 "「それは重畳」"
    太一 "「他にもいろいろやってるはずだよ」"
    太一 "「人生のほとんど自己の訓練に使ってる感じ」"
    太一 "「俺もいっぱしの格闘家だけど、歯が立たないよ」"
    voice "vfCCC3019akri013"
    霧 "「格闘なんてやってたんですか？」"
    "よくぞ訊いてくれました。"
    太一 "「カラデという」"
    voice "vfCCC3019akri014"
    霧 "「……知りません」"
    太一 "「えっ？」"
    voice "vfCCC3019akri015"
    霧 "「空手のパクりですか？」"
    太一 "「……ぐぅ」"
    "怒鳴りつけたいのを必死でこらえる。"
    "空手と比較されて、黙っていたことははじめてだ。"
    太一 "「霧君……君がエイリアンに襲われたら、助けてあげられるのは俺だけなんだぞ？」"
    voice "vfCCC3116kri008"
    霧 "「エイリアンっているんですか？」"
    太一 "「それは些細な問題だ。論点のすり替えだ」"
    太一 "「あと、たぶん銃器も使える」"
    "霧は目をぱちくりとする。"
    "急に話を戻しすぎたかな？"
    太一 "「格闘というか、組み討ちになったら一瞬で殺されるんじゃないかな。いろんなワザ持ってるし、こないだすごく高価なナイフ買ってたし」"
    voice "vfCCC3019akri018"
    霧 "「……そんな……いくらなんでも殺すなんて……」"
    太一 "「自分だって俺のこと殺そうとしていたくせにー」"
    "頬をつつく。"
    voice "vfCCC3116kri009"
    霧 "「……こほっ、けほっ！！」"
    voice "vfCCC3116kri010"
    霧 "「そ、そういう明確な殺意をもっていたわけではっ！！」"
    太一 "「いーっていーって。俺寛容だから許しちゃう」"
    太一 "「君が俺を嫌うのは当然だと思うしね」"
    voice "vfCCC3116kri011"
    霧 "「……」"
    voice "vfCCC3116kri012"
    霧 "「わからなくなってます……正直」"
    voice "vfCCC3019akri022"
    霧 "「命を助けられて、何もできなくなった以上、こういう状況は仕方ありません」"
    voice "vfCCC3116kri013"
    霧 "「でも……それとは別に……今の先輩は……その……うまく言えないですが……必死に、頑張ってるような気がして……」"
    太一 "「……ほんと、君はいい目してるなぁ」"
    太一 "「人事担当になりなさい、将来は」"
    "両肩をばんばん叩いてやる。"
    voice "vfCCC3116kri014"
    霧 "「……以前は、もっと享楽的というか、あまり愉快ではない感じだったんですけど……」"
    voice "vfCCC3116kri015"
    霧 "「今の先輩はどこか違うと思うんです」"
    "やれやれ、深刻な話になっちゃったな。"
    太一 "「……いやー、失敗できないしね」"
    "頭をかく。"
    太一 "「リセットかかるんだったら、もう快楽に生きようとかいう意志もあるんだけど」"
    "リセット、という単語に霧の眉根がかすかに寄った。"
    太一 "「……うんざりするんだ、そういうの」"
    太一 "「俺の少なくて弱い心でも、そうなんだ」"
    太一 "「自分が嫌いなんだよな、俺」"
    voice "vfCCC3116kri016"
    霧 "「……自分が嫌い？」"
    太一 "「霧っちが感じてるのと似たような理由でね」"
    voice "vfCCC3116kri017"
    霧 "「それって……」"
    太一 "「でも、一つだけ解決の手段を見つけたんだ。というか苦肉の策なんだけどね」"
    太一 "「……そのために……俺は……結局みんなを……」"
    "空を見る。"
    "抜けるような青空だ。"
    voice "vfCCC3116kri018"
    霧 "「……あの、豊は―――」"
    "豊、か。"
    "答えにくいことだった。"
    太一 "「ま、そーいうわけで、今後は仲良く喧嘩しよう」"
    "さえぎって、右手をさしだす。"
    voice "vfCCC3116kri019"
    霧 "「……は、はい」"
    "慌てて、霧も右手を。"
    "握手。"
    "握手は平和の証。"
    太一 "「じゃあ休戦調停を祝ってパーティーだ」"
    voice "vfCCC3019amki000"
    美希 "「ちょーたつかんりょー！」"
    voice "vfCCC3019amki001"
    美希 "「……あれえ？」"
    太一 "「おつかれ」"
    call gl(0,"evcc0051a")
    call vsp(0,1)
    with Dissolve(500.0/1000.0)
    voice "vfCCC3116mki000"
    美希 "「もう食べてる……しかもおいしそう」"
    太一 "「俺が誘った」"
    voice "vfCCC3116mki001"
    美希 "「……うそつきー……先輩のために現像してたのにー」"
    太一 "「ご苦労！」"
    voice "vfCCC3116mki002"
    美希 "「うおー！」"
    "美希はこの痛烈な裏切りに獅子吼した。"
    voice "vfCCC3116mki003"
    美希 "「それじゃあ、この大量の食料はどうするのー？」"
    "美希はトートバックの中身を、どさどさと机に落とした。"
    call gl(0,"evcc0051b")
    call vsp(0,1)
    with Dissolve(500.0/1000.0)
    "山になって机から溢れた。"
    太一 "「食料というより、お菓子だな」"
    "まったくこの娘は。"
    voice "vfCCC3019amki005"
    美希 "「てへっ」"
    voice "vfCCC3019akri041"
    霧 "「……缶詰とかは？」"
    voice "vfCCC3019amki006"
    美希 "「なくなっちった」"
    太一 "「うーむ。お菓子を昼飯がわりにするのは……つらそうだ」"
    voice "vfCCC3019amki007"
    美希 "「そうですか？」"
    太一 "「健康にも悪い」"
    voice "vfCCC3019amki008"
    美希 "「でも美希はお菓子が大好き」"
    voice "vfCCC3019akri042"
    霧 "「わたしも、もうおなかいっぱいだから」"
    太一 "「悪い、俺も」"
    voice "vfCCC3019amki009"
    美希 "「……えー」"
    voice "vfCCC3019amki010"
    美希 "「じゃあ一人で食べますもん」"
    "むくれた。"
    voice "vfCCC3019akri043"
    霧 "「……太るよ」"
    voice "vfCCC3019amki011"
    美希 "「……」"
    voice "vfCCC3019amki012"
    美希 "「太ってもお菓子大好き」"
    "ポテトチップを食べ出す。"
    "美容面には特にやばい一品だぞ、それは。"
    太一 "「内心気にしてるんじゃないか」"
    voice "vfCCC3019amki013"
    美希 "「だってだって～っ」"
    voice "vfCCC3019akri044"
    霧 "「泣かないでよ……」"
    太一 "「ほれ、じゃあこの握り飯をやろう」"
    "成人男性サイズになっているから、美希ちんには一個でちょうどいいだろう。"
    "俺が多少物足りないが……まあいいか。"
    voice "vfCCC3019amki014"
    美希 "「あああ、手料理だぁぁぁぁ～」"
    "ひし、とおにぎりを持った手にすがりつく。"
    太一 "「欲しいかー？　んー？」"
    "高く掲げる。"
    voice "vfCCC3019amki015"
    美希 "「あっ、ほしいですー」"
    太一 "「ほれほれ」"
    "右に。"
    voice "vfCCC3019amki016"
    美希 "「ああうう～」"
    太一 "「うりうり」"
    "左に。"
    voice "vfCCC3019amki017"
    美希 "「ううああ～」"
    voice "vfCCC3019akri045"
    霧 "「……いじめだ」"
    太一 "「……ほれ」"
    voice "vfCCC3019amki018"
    美希 "「ああ、おいちいっ」"
    "はみはみと食べ始める。"
    "お菓子の山が残される。"
    太一 "「……女の子なのに不安な食生活だな。いつもこうなの？」"
    voice "vfCCC3019akri046"
    霧 "「缶詰とかパンとかです」"
    太一 "「野菜食え」"
    voice "vfCCC3019akri047"
    霧 "「ありません」"
    太一 "「ほれ、トマトだ。ちょうど二つある」"
    voice "vfCCC3019amki019"
    美希 "「ああー、トマトだぁ～」"
    太一 "「んー？　欲しいのか？」"
    voice "vfCCC3019amki020"
    美希 "「ほしいっす！」"
    太一 "「ほれほれ」"
    "右に。"
    voice "vfCCC3019amki021"
    美希 "「ああうう～」"
    太一 "「うりうり」"
    "左に。"
    voice "vfCCC3019amki022"
    美希 "「ううああ～」"
    voice "vfCCC3019akri048"
    霧 "「…………やっぱりこの人は……いじめっこだ」"
    太一 "「ふう」"
    voice "vfCCC3019akri049"
    霧 "「ん～～～」"
    voice "vfCCC3019amki023"
    美希 "「すっぱい～」"
    voice "vfCCC3019akri050"
    霧 "「でもおいしい……」"
    voice "vfCCC3019amki024"
    美希 "「涙出そう」"
    voice "vfCCC3019akri051"
    霧 "「生きてるっていいね」"
    voice "vfCCC3019amki025"
    美希 "「にゃう～」"
    "美希と霧が、口を『＊』状にしながらトマトを食べる様を横目に見ながら、俺は水筒で喉を潤した。"
    call gl(4,"sgcc0018")
    call vsp(4,1)
    with dissolve
    太一 "「…………」"
    "見てる見てる。"
    "まったくこの人……。"
    "嫉妬のかたまりだな……。"
    "俺に気取られるように姿を見せているってことは……当てつけなんだろうな。"
    hide pic4
    with dissolve
    voice "vfCCC3019amki026"
    美希 "「どうしましたっす？」"
    太一 "「いや……市原式諜報術で監視されてるだけ」"
    voice "vfCCC3019amki027"
    美希 "「市原？」"
    太一 "「Ｅ·市原を頂点とする、凄腕くのいち集団が伝えるスパイ技術……って気にしないでいいから」"
    voice "vfCCC3019amki028"
    美希 "「？」"
    voice "vfCCC3019akri052"
    霧 "「きゃああああっ！？」"
    "見ちゃったか。"
    voice "vfCCC3116kri020"
    霧 "「先輩っ、せっ、せんぱ……あ、あれあれ……」"
    太一 "「平気だ、俺のそばにいるんだ」"
    voice "vfCCC3019akri054"
    霧 "「……は、はい……」"
    voice "vfCCC3019amki029"
    美希 "「え？　え？」"
    voice "vfCCC3019akri055"
    霧 "「あ、あれ……」"
    "霧が指さす。美希が 「んに？」と見る。"
    "曜子ちゃんの姿はない。"
    voice "vfCCC3019amki030"
    美希 "「……え？　なにもないけど、どったの？」"
    voice "vfCCC3019akri056"
    霧 "「い、今確かに……先輩？」"
    太一 "「志村現象だ。美希にはもはや物理的に曜子ちゃんを観測することはできない」"
    "※志村現象＝太一物理学。安定している特定状況内で発生する観測問題の一種。見る者は見るが、見えないものは見えないまま属性が固定され、それが物理的に反映される。状況内で大きな変化があると属性は破棄されることが多い。"
    voice "vfCCC3019akri057"
    霧 "「……くっ」"
    "死ぬほど緊張していた。"
    太一 "「平気平気。ただのあてつけだから」"
    太一 "「無視しよ、無視」"
    voice "vfCCC3116kri021"
    霧 "「はい……頑張ります。無視は得意です」"
    voice "vfCCC3116mki004"
    美希 "「じゃあ食後のお菓子ー！」"
    "結局食うのか。"
    voice "vfCCC3116kri022"
    霧 "「あの……黒須先輩」"
    太一 "「なんだ」"
    voice "vfCCC3116kri023"
    霧 "「泣いてますけど……」"
    太一 "「気にしない！」"
    voice "vfCCC3116kri024"
    霧 "「気になります……」"
    太一 "「演技だ。だまされるな。ロボットに人の心がないのと一緒で、マイケルにも……じゃなくて彼女にも人の心はないのだ」"
    曜子 "「……………………」"
    "うーむ、視線が痛いぜ。"
    stop bgm
    call gl(0,"bgcc0008")
    call vsp(0,1)
    call vsp(1,0)
    call vsp(4,0)
    call vsp(2,0)
    with wipeleft
    "そして霧との対話の時間だ。"
    "美希がふらっといなくなった隙に、案の定持ちかけられた。"
    太一 "「さて、行くか」"
    call gl(1,"TCSK0000|TCSK000x")
    call gp(1,t=center)#x=220
    call vsp(1,1)
    with dissolve
    voice "vfCCC3116kri025"
    霧 "「あ、じゃあちょっとトイレ行かせてください」"
    太一 "「ん、俺もあっちのトイレ行ってくるわ」"
    call gl(0,"bgcc0000d")
    call vsp(0,1)
    call vsp(1,0)
    太一 "「……ふう」"
    "正念場だ。"
    "信頼を得ないとな。"
    call gl(0,"evcc0009")
    call vsp(0,1)
    with Dissolve(500.0/1000.0)
    voice "vfCCC3116you001"
    曜子 "「太一」"
    play bgm "bgm/bgm018.ogg"
    太一 "「……君か」"
    太一 "「協力的だよね、なんか」"
    voice "vfCCC3116you002"
    曜子 "「そう？」"
    太一 "「俺が向こうのトイレに行かないように、足止めに来てくれたの？」"
    voice "vfCCC3116you003"
    曜子 "「……ええ」"
    "正直だ。"
    太一 "「俺が霧と和解するの、いやなんじゃない？」"
    voice "vfCCC3116you004"
    曜子 "「無駄なことをしていると思う」"
    voice "vfCCC3116you005"
    曜子 "「でも、あなたの望みなら……仕方ない」"
    "そうなのか？"
    "本意なのか？"
    voice "vfCCC3116you006"
    曜子 "「手間取っているようだから、あと五分はここにいて」"
    太一 "「……行かないよ」"
    太一 "「せっかくここまで安定保ってるのに、ダイナシにしたくない」"
    太一 "「それに……手榴弾はごめんだからね」"
    voice "vfCCC3116you007"
    曜子 "「……」"
    "ニィ、と笑った。"
    "たまに見せる、本来的な支倉曜子。"
    "こうも凄絶な人間が、生まれ得るのだ。"
    太一 "「一応、こんなこと言わないと不安でしょうがないんで、悪いんだけど」"
    voice "vfCCC3116you008"
    曜子 "「……邪魔をするな、でしょう？」"
    太一 "「うん、ごめん」"
    voice "vfCCC3116you009"
    曜子 "「しない。必要な協力もしてあげる」"
    太一 "「……そう」"
    voice "vfCCC3116you010"
    曜子 "「思い出、手に入るといいね、太一」"
    "姿を消す。"
    "気配を消す。"
    "存在がかき消える。"
    "歩き方の技術一つで、神出鬼没を実現する。"
    "もう人間じゃないよ、君―――"
    stop bgm
    call gl(0,"bgcc0008")
    call vsp(0,1)
    with wipeleft
    "一年教室に。"
    "深呼吸。"
    "さあ、騙すぞ！"
    call gl(0,"bgcc0006")
    call vsp(0,1)
    with wipeleft
    "そして―――"
    play bgm "bgm/bgm020.ogg"
    call gl(0,"evcc0027a")
    call vsp(0,1)
    with wipeleft
    voice "vfCCC3117kri000"
    霧 "「……待ってました」"
    太一 "「うん」"
    "その場で立ち止まった。"
    "二人の距離。"
    "今は詰めないでおこう。"
    "霧は俺を拒絶するかも知れないのだから。"
    voice "vfCCC3117kri001"
    霧 "「まず、わたしの方から少し」"
    voice "vfCCC3117kri002"
    霧 "「わたしは、あなたを薄汚い人殺しだと思っていました」"
    太一 "「……」"
    voice "vfCCC3117kri003"
    霧 "「豊を、殺した」"
    "静かな面差し。"
    voice "vfCCC3117kri004"
    霧 "「豊が死んだ日、わたし屋上を見たんです」"
    voice "vfCCC3117kri005"
    霧 "「そして、先輩と豊が話しているのを見ました」"
    太一 "「…………」"
    "凍るな、俺の理性。"
    "……激情は、沈んでいろ。"
    voice "vfCCC3117kri006"
    霧 "「そして豊は死んだ」"
    voice "vfCCC3117kri007"
    霧 "「最初は気づかなかった。でもあとになって……屋上で、あなたが……」"
    "あの時のことか。"
    voice "vfCCC3023kri011"
    霧 "「だからあなたには関わりたくなかった」"
    voice "vfCCC3023kri012"
    霧 "「けど、あなたから関わってきた」"
    "双眼には、迷いがあった。"
    voice "vfCCC3117kri008"
    霧 "「……それでわたしは考えました。あなたが……その……人の心を食べてるんじゃないかって」"
    太一 "「ふむ」"
    太一 "「……人の心を壊して、渇望を満たす……というような意味かな？」"
    voice "vfCCC3117kri009"
    霧 "「……そうです」"
    "不安に揺れる瞳。"
    voice "vfCCC3117kri010"
    霧 "「それと……あなたがわたしを見る目」"
    voice "vfCCC3117kri011"
    霧 "「当時のそれは、わたしをぞっとさせたんです」"
    太一 "「うん……そうだろうな」"
    "鋭い子だ。"
    "故に、人の世で生きることさえつらい。"
    "たちまち心は汚染されてしまう。"
    "鋭さが、この子を群青に追いやったんだ。"
    voice "vfCCC3117kri012"
    霧 "「でも、今のあなたはわからない。正体が……いえ、今先輩がどういう状態なのか……」"
    voice "vfCCC3117kri013"
    霧 "「もしかしたら……もしかしたら今のあなたは……」"
    "窓の外に手を垂らす。"
    voice "vfCCC3117kri014"
    霧 "「……でもわたしには、こうするしかない……」"
    "引き上げる。"
    "布包み。"
    "布を取り払うと、"
    call gl(0,"evcc0024c")
    call vsp(0,1)
    with Dissolve(500.0/1000.0)
    voice "vfCCC3117kri015"
    霧 "「ごめんなさい、わたしのこと、恨んでくれていいです」"
    voice "vfCCC3117kri016"
    霧 "「だから、どうか真実を」"
    太一 "「……」"
    "曜子ちゃん、動いてくれるなよ。"
    "切に祈った。"
    太一 "「結論から言うとー、君は引き金を引いていい。その権利があるよ、霧には」"
    "受け入れよう。"
    "俺は今また、霧を食べようとしているのだから。"
    "代価を支払おう。"
    "さあ霧、俺は命を賭けたぞ。"
    "全力で来い、後輩。"
    太一 "「豊の死因は、自殺だ」"
    voice "vfCCC3117kri017"
    霧 "「…………」"
    太一 "「けど原因は俺」"
    "無限の沈黙。"
    "ほどなくして、"
    voice "vfCCC3117kri018"
    霧 "「……続けて下さい」"
    "まず一面クリア、か。"
    太一 "「長い話になるけど」"
    voice "vfCCC3117kri019"
    霧 "「話して、先輩」"
    voice "vfCCC3117kri020"
    霧 "「それで、わたしを解放してください」"
    "敵対か、容赦か。"
    "どっちかに寄ること。"
    "霧の心は、いずれかしか受けつけないのだろう。"
    "唾液で喉を潤して、俺は話しはじめた。"
    太一 "「支倉って家があったんだ、昔」"
    太一 "「大きな家でさ。洋風で。桐原の家を十倍くらい大きくしたような」"
    太一 "「大富豪ってやつだ」"
    太一 "「俺は……幼い頃に母親を亡くして、そこに引き取られた」"
    太一 "「そこに住み込みで働く、母親の遠縁にあたる管理人夫妻にね」"
    太一 "「古い風習がある家でさ」"
    太一 "「下働きの子供は、やっぱり下働きだった」"
    太一 "「俺は子供だったから、家の子供たちの遊び相手みたいな役割だった」"
    太一 "「曜子ちゃんはそこの末娘だった」"
    call gl(0,"bgcc0000d")
    call vsp(0,1)
    with Dissolve(500.0/1000.0)
    "……。"
    "…………。"
    "……………………。"
    play bgm "bgm/bgm021.ogg"
    call gl(0,"bgcc0022")
    call vsp(0,1)
    call vsp(1,0)
    with Dissolve(500.0/1000.0)
    "彼女はいつも一人だった。"
    "親族や使用人の誰とも、交わろうとはしなかった。"
    "孤高の君―――"
    "俺は、彼女を内心でそう呼んでいた。"
    "言葉をかわしたことはない。"
    "気にはなっていた。"
    "屋敷がどのような人々によって維持され、いかなる経緯をたどってこの有様になったのか、俺は知らない。"
    "ただそこは、時の流れから隔絶された楽園のごとき場所だった。"
    "住むのもまた、浮世離れした人々で。"
    "ときおり俺は彼女らに招かれ、甘い飲み物を振る舞われた。"
    "着飾り、茶を楽しみ、人を招き、散策し。"
    "毎月頭には大量の書物·衣類·嗜好品が届けられた。"
    "広い庭。"
    "庭師という人々もいた。"
    "人里離れ、地代が安いことを差し引いても、なお広漠たるものがあった。"
    "小さな俺にとって、お屋敷は広大無辺な世界そのものだったのだ。"
    "実際、屋敷時代以前の記憶はない。"
    "世界と屋敷は同じ大きさだった。"
    "ある頃からか、俺はご婦人がたに気に入られるようになった。"
    "女のような顔をしている、とのこと。"
    "また間近で見るとわかる不思議な模様を描く瞳も、彼女たちを退屈させなかった。"
    "少女の着るような（それもとりわけ華美な）ドレスを着させられた。"
    "そしてお茶の相手。"
    "子供にお茶の味などわからない。"
    "でもつきあった。"
    "砂糖菓子めいて甘やかな人々に対し、逆らうという選択肢はなかった。"
    "……少なくともイヤではなかった。"
    "退屈ではあったけど、楽だったから。"
    "こうして幼い子供らに馬乗りにされ髪引かれる玩具の身分から離れた俺は、新しい仕事として人形をすることになった。"
    "そんな俺を、彼女……孤高の君はひややかな視線で見ていた。"
    "いや、見てさえいなかった。"
    "興味がないらしく、視線はいつも俺を素通りしていった。"
    "支倉曜子。"
    "末娘。"
    "ただ家族からは、それほど可愛がられている様子はない。"
    "むしろ疎んじられていた。"
    "なるほど確かに彼女は、なかば夢幻の住人であるご婦人がたとは、違う世界に生きていた。"
    "……現実という世界に。"
    "一度、掃除の人夫として駆り出されたことがある。"
    "人形ハジメマシタ、以前のことだ。"
    "使用人さんたちにまじって参加した。"
    "通いの人間は使わない方針だったためか、人手の貸し借りは茶飯事だった。"
    "十時と三時にお茶の休憩を一時間ずつ挟みながら、順番に部屋を掃除していく。"
    "夕方には彼女の部屋に辿り着いた。"
    "はじめて彼女の声を聞いた。"
    voice "vfCCC3025you000"
    "曜子『……ここはいいわ』"
    "短くそっけない。"
    "機能的。"
    "けど、蠱惑的だった。"
    "ちらりと見た室内は、とても乙女の部屋とは思えない。"
    "数台のパソコン。"
    "四方の壁を覆い隠す本棚と、そこにおさまりきらず床に堆く積まれた書物。"
    "重々しい工作台と、真新しい工具。"
    "かなり広い私室は雑多な知識と技術で埋め尽くされていて、秘密基地を連想させた。"
    "なるほど確かに一人だけ異質な者が、異世界にはいたのだ。"
    "綺麗な衣装を着て、女の子の言葉遣いでお茶の相手をしている時、支倉曜子について問いかけたことがある。"
    "もの静かな老婦人は答えた。"
    "末の息子のそのまた娘と。"
    "若く快活な婦人は答えた。"
    "望まれて生まれた娘ではないと。"
    "姦しい三姉妹は囀った。"
    "若旦那とうら若き使用人との秘められた恋物語と、その顛末。"
    "誰にもなつかず愛を知らない娘の咎と、訪れるであろう悲劇的結末。"
    "支倉の血でありながら支倉の一員ではない、そんな汚点に対する奥ゆかしい嘆き。"
    "要するに忌み子だったのだ。"
    "誰も彼女に語りかける者はなく、彼女もまた誰にも語らなかった。"
    "腫れ物だった。"
    "彼女の実父である若旦那なる人物は、海外に留学してしまったそうだ。"
    "母親の使用人は……亡くなっていた。"
    "何者にもなれない少女。"
    "誰にも求められない少女。"
    "傷つく？"
    "否。傷つかない。"
    "支倉曜子は強かった。"
    "意に介さなかった。"
    "たぶん気づいたいたんだと思う。"
    "世界が箱庭であることを。"
    "……………………。"
    "人形生活の合間、図書室に通った。"
    "影響を受けたのかも知れない。"
    "貴婦人からは作法とお茶を学んだ。"
    "けれど知恵と技術と真実は、そこにはなかった。"
    "補うために、使う者の少ない図書室に通い詰めた。"
    "曜子ちゃんとはよく出会った。"
    "依然として会話はない。"
    "なんとなく癪だったので、俺からアプローチすることもなかった。"
    "好ましくは思っていたけど、仲良くなりたいと願いはしなかった。"
    "俺の美的傾向は、この頃から確立されたようだ。"
    "なんというか……自立しているものに惹かれた。"
    "独力で生きるものと、力に。"
    "知識にしろ技術にしろ、そういう側面がある。"
    "人は群れる。"
    "群れることを渇望する。"
    "そして同時に、聖域を持とうとする。"
    "侵害されない自分のための場所を欲する。"
    "しかし人と接すれば境界線は揺らぐ。"
    "領土は減ったり増えたりする。"
    "不快。"
    "矛盾。"
    "一般的な価値観では、千の軍隊より一人の英雄が好まれる。"
    "単一の絶対者。英雄。"
    "人の望むもの。"
    "憧れという形をとった、願望に過ぎない。"
    "一人で生きたいのか、群れて生きたいのか……人はそのどちらにもＹＥＳと答えることができる。"
    "閑話休題。"
    "図書室では、彼女の読んだ本を追って読んだ。"
    "憧れから。"
    "あるいは少女の完璧さへの嫉妬から。"
    "書物の内容は高度過ぎてほとんどわからなかった。"
    "けど読み続けた。"
    "図書室では何百回となく出会い、すれ違った。"
    "一度の会話もない空間を、俺たちは共有し続けた。"
    "そういう時代が、数年間続いた。"
    call gl(0,"bgcc0022a")
    call vsp(0,1)
    with Dissolve(500.0/1000.0)
    "で、だ。"
    "楽園には崩壊がつきもの。"
    "これは人類最初の楽園からしてそうだから、避けようのない摂理と考えられる。"
    "具体的には、屋敷のご当主である支倉氏の急激なる凋落によって。"
    "悲劇のはじまりだった。"
    "支倉のお上品な人々はいなくなった。"
    "使用人たちは残された。"
    "支倉のかわりに入ってきたのは、新興の人物とその親類縁者だった。"
    "粗暴な人々であった。"
    "老若男女、揃ってやってきた。"
    "全員が、腐肉あさりの素質を持っていた。"
    "三日経たないうちに、使用人の一人が暴行された。"
    "事件である。"
    "けれどここは箱庭だった。"
    "閉鎖された空間。"
    "独自の秩序が発生した。"
    "広大な土地に囲まれた屋敷ともなれば、治外法権に近い。"
    "日々、どんな饗宴が繰り広げられたか。"
    "屋敷の一室は、もとは夜会に用いられていたホールだった。"
    "支倉の人たちは、ちょっとしたパーティーが大好きで、よく使用されたものだ。"
    "粗暴な人々は、ここを別の夜会に用いた。"
    "上品な会話も上質の料理もなく。"
    "かわりに堕落と退廃が満たされた。"
    "……きっと、何人も犠牲になったのだと思う。"
    "たとえば、若い使用人の夫婦がいた。"
    "妻が輪姦された。"
    "いや。"
    "輪姦され続けた。"
    "ありとあらゆる方法で肉体をはけ口にされ、従属させられた。"
    "夫は抵抗した。"
    "妻を助けようと警察に連絡を取った。"
    "警察は介入してこなかった。"
    "たぶん面倒だったのだと思う。"
    "別に買収されてもいなかったんだろう。"
    "またいつでも買収できたのだろう。その気になれば。"
    "屋敷のネットで調べてみた。"
    "警察のこうした対応によって看過された犯罪は、数限りなくあった。"
    "民間の権利意識が肥大化すると、おいそれと介入できなくなるのだった。"
    "些細なミスを、親の仇のように責める人間が増えるのだ。"
    "大物相手には、動かないのが一番。"
    "怠慢ではあろうが。"
    "不完全な人間の組織としては、この程度が限度だと俺は思う。"
    "誠実さは必要だろうが。"
    "自分を助けるのは、自分の有能さだ。"
    "……と思えば腹も立たない。"
    "実害を被らない限りにおいて、他人の不手際や浅い見識に腹を立てるということは。"
    "心の一部を、他者に委託していることになる。"
    "でもそれが普通。"
    "普通であるということは。"
    "人の限界に起因する、理不尽で不完全なルールに身を置くことでもある。"
    "……優しいゆりかごであるはずがない。"
    "ことに閉鎖空間では、正常な倫理さえかすむ。"
    "粗暴なことが日常と化しやすい。"
    "たちむかうには、強固な自我。"
    "揺るぎない自己のシステムが必要だった。"
    "……彼女のような。"
    "さて。"
    "妻は慰みものにさせられ、妊娠させられたり堕胎させられたりした。"
    "男たちを悦ばせる方法を、たくさん身につけさせられた。"
    "彼女は笑わなくなった。"
    "使用人の仕事にも、参加しなくなった。"
    "衣類の着用を禁じられると、彼女は諾々と従った。"
    "彼女は刺青を彫られていた。"
    "卑猥な刺青だ。"
    "性器を指し、その所有を夫ではないと示した。"
    "粗暴な人々は、その方面において際だって有能ではあった。"
    "徐々に心も沈む。"
    "夫は最後の手段に出た。"
    "妻を連れて逃げ出したのだった。"
    "遅すぎた。"
    "三日で連れ戻された。"
    "彼らは、夫がいつキレるか賭けていたのだった。"
    "夫は殺された。"
    "妻が輪姦されている脇で。"
    "死体は庭に埋められた。"
    "男たちはゲラゲラ笑いながら、桜の木の根本に埋めたのだ。"
    "とまあ、倫理の壊れた連中だった。"
    "ある時、一人の男が家族を連れてやってきた。"
    "新キャラの登場。幼児性愛者だった。"
    "両刀とサドという二つのオプションをつけていた。"
    "サドなのでＳと呼ぶ。"
    "俺はＳに目をつけられた。"
    "再び女児の格好を強いられ、夜会に参加させられた。"
    "今度はお茶ではなく、Ｓの欲望の相手をした。"
    "Ｓは人にさせるのも好きだった。"
    "女児のような俺を、ノンケの男に相手させた。"
    "冗談半分でやる者が大半だった。"
    "たまに覚醒してしまう者もいたが（笑）"
    "夜会では、どんなえげつないことをするかが、目立つポイントだ。"
    "小学校のいじめとかでも、似たようなことは起こる。"
    "ま、集団心理というやつだ。"
    "物事にはメリットデメリットが必ずある。"
    "一義的な善し悪しを越えてだ。"
    "やがてＳのＳっぷりはエスカレート。"
    "子供を連れてきた。"
    "Ｓの息子だ。"
    "学校ではいじめっ子としてならしていた……らしい。"
    "乱交の雰囲気に圧倒されていたのも束の間、俺を見て嘲笑った。"
    "異常興奮からか。"
    "促されるまま、むしろ積極的に、そいつは参加した。"
    "血を引いているようで、すぐ才能を発揮しはじめた。"
    "早熟な精通と重なっていたせいもあるだろうか。"
    "じき夢中になった。"
    "俺は皆に笑われた。"
    "笑われながら、何週間も。"
    "攻撃を受け続けた。"
    stop bgm
    call gl(0,"bgcc0006")
    call vsp(0,1)
    with Pixellate(300.0*2/1000.0,5)
    call gl(1,"TCSK0004|TCSK000x")
    call gp(1,t=center)#x=220
    call vsp(1,1)
    with dissolve
    霧 "「…………」"
    太一 "「ここから、少しきつくなるぞ？」"
    call gl(1,"TCSK0003|TCSK0003")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3119kri001"
    霧 "「……え？」"
    "呆けた声だった。"
    voice "vfCCC3119kri002"
    霧 "「今のが、きつくないと？」"
    太一 "「そんなには」"
    call gl(1,"TCSK0002|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3119kri003"
    霧 "「先輩は……じゃあ……」"
    太一 "「それでぶっ壊れたんだよね、俺」"
    call gl(1,"TCSK0000|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3119kri004"
    霧 "「嘘……」"
    太一 "「ま、俺のことはいいや。今は豊の問題だ」"
    call gl(1,"TCSK0002|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3119kri005"
    霧 "「は、い……」"
    "涙をぬぐう。"
    太一 "「Ｓの息子というのが……その……」"
    "オブラートなんて意味はない。"
    太一 "「んー……豊、だったりするんだな」"
    call gl(1,"TCSK0000|TCSK000x")
    call vsp(1,1)
    with dissolve
    霧 "「……………………」"
    play bgm "bgm/bgm021.ogg"
    "止まった。"
    "手の震えもろともに。"
    "無論、落ち着いたわけじゃない。"
    "哀れなほど、色を失って。"
    "俺を凝視していた。"
    voice "vfCCC3119kri007"
    霧 "「……な、なにを言って……？」"
    "半笑い。"
    "感情さえコントロールできていない様子。"
    太一 "「休憩しよう」"
    "俺は椅子に座った。"
    call gl(1,"TCSK0003|TCSK0003")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3119kri008"
    霧 "「……え……なに？」"
    "霧の戸惑いを聞きながら。"
    "俺は一切喋らなかった。"
    "……………………。"
    太一 "「そろそろいい？」"
    call gl(1,"TCSK0002|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3119kri009"
    霧 "「……はい」"
    "のろのろと、霧は立ち上がる。"
    "すでに武器を構えてはいない。"
    太一 "「質問はある？」"
    call gl(1,"TCSK0000|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3119kri010"
    霧 "「……豊が……その、先輩をって……？」"
    太一 "「事実だ」"
    太一 "「まあ、雰囲気のせいもある。小さい子供、父親には逆らえないものだろう？」"
    "霧は口元を押さえる。"
    太一 "「豊の不幸は、そういう父親を持ってしまったことだったんだ」"
    call gl(1,"TCSK0003|TCSK0003")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3119kri011"
    霧 "「……聞いたこと、ある……新川の人の噂……でも……でも！」"
    太一 "「霧の言うとおり、世界には悪意が多すぎる」"
    太一 "「豊は犠牲者だよ」"
    call gl(1,"TCSK0002|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3119kri012"
    霧 "「でも……そんな話、聞いたこともないんです。ずっと暮らしてきて、そんな話があったなんて―――」"
    太一 "「記憶喪失」"
    "ぴたりと霧は口をつぐんだ。"
    "豊が記憶喪失だったことは、霧も知っているはずだ。"
    "霧の内部で、曖昧なまま放置されてきたパーツが、一気に結合される。"
    太一 "「あと、あいつの脚の怪我もな、原因を知ってる」"
    call gl(1,"TCSK0000|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3119kri013"
    霧 "「……え？」"
    call gl(5,"evcc0063")
    call vsp(5,1)
    with dissolve
    call vsp(5,0)
    with Dissolve(500.0/1000.0)
    太一 "「その場にいたからな」"
    call gl(1,"TCSK0002|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3119kri014"
    霧 "「……じゃあ……先輩は……それを知ってて？」"
    太一 "「いんにゃ？」"
    太一 "「俺は豊が生き延びたなんて思ってなかったし……名前も忘れてたよ」"
    太一 "「……あいつと出会ったのは偶然だ」"
    太一 "「当時は俺も女装させられてたし……向こうもわからなかったみたいだけど」"
    太一 "「でまあ、いろいろあって俺も解放されて……紆余曲折あってここに来たわけだけど」"
    太一 "「考えてみれば当然だよな」"
    太一 "「豊も俺も、あれで心が壊れないはずないんだ」"
    太一 "「出会うのは必然だったのかな」"
    voice "vfCCC3119kri015"
    霧 "「……信じられない」"
    太一 "「豊のことに気づいたのは、親しくなったあとだよ」"
    call gl(1,"TCSK0000|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3119kri016"
    霧 "「……だから……殺した？」"
    太一 "「すぐに殺意がわいたわけじゃない」"
    太一 "「過去のことだしな」"
    voice "vfCCC3119kri017"
    霧 "「だったら……なぜ？」"
    太一 "「苦しんでいるのなら、見逃してやろうと思った」"
    太一 "「けど俺とつるんでいる時のあいつは、幸せそうだった」"
    call gl(1,"TCSK0003|TCSK0003")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3119kri018"
    霧 "「……っ！！」"
    call gl(1,"TCSK0002|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3119kri019"
    霧 "「あの日……わたしに質問した……幸せかって……？」"
    太一 "「よく覚えてるな」"
    "笑う。"
    太一 "「そうだよ。そーいう意味だ」"
    太一 "「俺はあれで、豊が幸せだって判断したんだ」"
    太一 "「恨みにまみれていたわけじゃない」"
    太一 "「ただ……つついてみたくなった、無性に」"
    voice "vfCCC3119kri020"
    霧 "「……うう……」"
    太一 "「よく晴れた日だったよ」"
    太一 "「おまえが見たとおり、あの時の屋上ですべて話した」"
    voice "vfCCC3119kri021"
    霧 "「……う……」"
    太一 "「あいつは言った。どうすれば許してくれるって？」"
    太一 "「責める気はなかった」"
    太一 "「……ただ、一つ疑問があってさ」"
    太一 "「問いかけたんだ」"
    call gl(5,"bgcc0007s")
    call vsp(5,1)
    with Pixellate(300.0*2/1000.0,5)
    太一 "「なあ、ひとつ質問なんだけど……どうして今すぐにでも死なないんだ？」"
    hide pic5
    with dissolve
    太一 "「……ってな」"
    霧 "「…………」"
    太一 "「そしたら……あいつ本当に自殺しちゃったんだ」"
    hide pic1
    with dissolve
    "霧は崩れ落ちた。"
    "近寄って、囁きたくなる気持ち。"
    "押さえつけた―――"
    太一 "「恨みはなかった」"
    太一 "「けど……人を攻撃することで健常でいるような連中を……俺は認めるわけにはいかなかった」"
    太一 "「豊はそのどっちでもあって……俺は……本当は……」"
    太一 "「恨みがないなら……そのままで良かったんだって……今は思う」"
    太一 "「豊がいてくれたら……俺はもうちょっと、ましになれたかも知れないんだ」"
    voice "vfCCC3119kri023"
    霧 "「ああああぁぁぁぁぁぁ……っ」"
    "絞り出すような号泣。"
    太一 "「いいやつになってたんだ、あいつ……ただ、俺が壊れすぎてた」"
    太一 "「いくら表面をとりつくろっても、俺は……霧の言うとおり怪物なんだ」"
    太一 "「だから駄目なんだ」"
    太一 "「だから……俺は……」"
    "心は泣かない。"
    "涙も出ない。"
    "そんな自分が許せない。"
    "いや。"
    "許さないと決めたんだ。"
    太一 "「ごめん、霧」"
    voice "vfCCC3119kri024"
    霧 "「わあああぁぁぁぁぁぁぁ、うわ、あぁぁぁぁぁぁぁぁっ！！」"
    太一 "「当時、あの異常な空気の中、豊が自分を保つには自分より弱い俺を食うしかなかった」"
    太一 "「そして次には俺が、豊を食い物にした……」"
    太一 "「俺と豊はね、互いを食らいあったんだ、霧」"
    voice "vfCCC3119kri025"
    霧 "「……っ」"
    "霧が抱きついてきた。"
    "つい……抱きしめてしまった。"
    call gl(1,"TCSK0002|TCSK000x")
    call gp(1,t=center)
    call vsp(1,1)
    with dissolve
    voice "vfCCC3119kri026"
    霧 "「ごめんなさい……」"
    voice "vfCCC3119kri027"
    霧 "「ごめんなさい、ごめんなさい、ごめんなさいっ！」"
    voice "vfCCC3119kri028"
    霧 "「ごめんなさいぃぃ……」"
    太一 "「謝るなよ。そういう問題じゃないんだ……」"
    太一 "「泣いてくれ、俺のかわりに」"
    "いっそう声を張り上げた。"
    stop bgm
    call gl(0,"bgcc0000d")
    call vsp(0,1)
    call vsp(1,0)
    with Dissolve(500.0/1000.0)
    pause (500.0/1000.0)
    pause (1000.0/1000.0)
    call gl(0,"bgcc0003g")
    call vsp(0,1)
    with wipeleft
    play bgm "bgm/bgm003.ogg"
    "自宅。"
    "いつも寂しい空間に、今日は華がある。"
    太一 "「さ、入って」"
    call gl(1,"TCSK0000c|TCSK000x")
    call gp(1,t=center)#x=220
    call vsp(1,1)
    with dissolve
    voice "vfCCC3029kri000"
    霧 "「お、お邪魔します……」"
    "あのあと、霧は自宅に来た。"
    call gl(1,"TCSK0003c|TCSK0003")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3029kri001"
    霧 "「うわあ」"
    "混沌を愛する俺の部屋だった。"
    "客はたいてい驚く。"
    太一 "「座りたまへ」"
    call gl(1,"TCSK0002c|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3029kri002"
    霧 "「……どこに座れと」"
    太一 "「はい」"
    "トンボを渡す。"
    voice "vfCCC3029kri003"
    霧 "「……はいって」"
    太一 "「座りたい場所にスペース作ってね」"
    霧 "「……………………」"
    "自己責任。"
    "霧はトンボをかけて作った隙間に、ぎこちなく正座する。"
    voice "vfCCC3029kri005"
    霧 "「……男の人って」"
    太一 "「ちょっと待っててねー」"
    "階下に降りてトマトを持ってくる。"
    太一 "「はい、ビタミン」"
    call gl(1,"TCSK0000c|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3029kri006"
    霧 "「……どうも」"
    "おどおどと、トマトを囓る。"
    太一 "「リラックスしていいよ」"
    call gl(1,"TCSK0002c|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3120kri007"
    霧 "「……はい」"
    太一 "「で、話の続きってのは？」"
    call gl(1,"TCSK0000c|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3120kri008"
    霧 "「償いについてです」"
    太一 "「償いか」"
    "予想できたことではあるが。"
    call gl(1,"TCSK0002c|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3120kri009"
    霧 "「豊のしたこと、そしてわたしの先輩への仕打ち、今日の殺人未遂も含めて」"
    voice "vfCCC3120kri010"
    霧 "「……警察もいませんし……先輩が、決めてくれればと思います」"
    call gl(1,"TCSK0000c|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3120kri011"
    霧 "「豊とわたしの、二人分の」"
    太一 "「つまり二つ、願い事をきいてくれるわけだ」"
    voice "vfCCC3120kri012"
    霧 "「……何個だっていいです」"
    voice "vfCCC3120kri013"
    霧 "「罪がなくなることはないでしょうけど」"
    太一 "「罪のことはいいんだけどね」"
    "俺と豊のは同士討ちだし。"
    太一 "「そうだな……とりあえず一つ、お願いがある」"
    voice "vfCCC3120kri014"
    霧 "「なんでしょう？」"
    太一 "「明日、早朝……俺につきあって欲しい」"
    call gl(1,"TCSK0002c|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3120kri015"
    霧 "「……はい、わかりました」"
    太一 "「質問は？」"
    voice "vfCCC3120kri016"
    霧 "「ありません。従います」"
    太一 "「……んー」"
    太一 "「まあ、山に登るんだけどね」"
    call gl(1,"TCSK0000c|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3120kri017"
    霧 "「山ですか？」"
    太一 "「そう、合宿やったじゃん？　あそこまで行く」"
    voice "vfCCC3120kri018"
    霧 "「はい、了解です」"
    "やった。"
    voice "vfCCC3120kri019"
    霧 "「他にはありませんか？」"
    太一 "「え……他に？」"
    "考えてなかった。"
    "どうしよう？"
    call gl(1,"TCSK0002c|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3120kri020"
    霧 "「なんでも結構です」"
    太一 "「……じゃあ」"
    "唇を、寄せた。"
    call gl(1,"TCSK0000c|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3120kri021"
    霧 "「……！？」"
    "ディープ＆長時間は危険だな。水位が下がる。"
    太一 "「こんなところで、ゴチ」"
    "身を離す。"
    call gl(1,"TCSK0003c|TCSK0003")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3120kri022"
    霧 "「あっ、あのっ、あのっ？」"
    太一 "「あまり深く考えるな」"
    voice "vfCCC3120kri023"
    霧 "「でっ、でっ、でもっ」"
    太一 "「いいんだ。とにかくこれで願い事は叶った！　やったね！　美少女キラー。すげー、かっちょいー、イカス！」"
    "クールダウン。"
    太一 "「……寝る。帰れ」"
    "ベッドに入る。"
    call gl(1,"TCSK0000c|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3120kri024"
    霧 "「……先輩！」"
    "腕を取られる。"
    太一 "「明日、六時にはうちに来て俺を起こしてくれ」"
    call gl(1,"TCSK0002c|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3120kri025"
    霧 "「……だったら……ここにいます」"
    太一 "「おまいね。俺にも事情ってものが……」"
    call gl(1,"TCSK0006c|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3120kri026"
    霧 "「……ばかな人」"
    stop bgm
    太一 "「ん……んん！？」"
    "今度は霧の方から、だった。"
    call gl(0,"bgcc0000d")
    call vsp(0,1)
    call vsp(1,0)
    with Dissolve(500.0/1000.0)
    pause (500.0/1000.0)
    pause (1500.0/1000.0)
    play bgm "bgm/bgm002.ogg"
    call gl(0,"bgcc0003")
    call vsp(0,1)
    with Dissolve(500.0/1000.0)
    "そして朝―――"
    "目を覚ます。"
    太一 "「……霧？」"
    "いない。"
    "確かに昨夜は……。"
    call gl(0,"bgcc0004")
    call vsp(0,1)
    with wipeleft
    call gl(1,"TCSK0000|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3121kri000"
    霧 "「おはようございます、太一先輩」"
    太一 "「……たいちせんぱい、ね」"
    call gl(1,"TCSK0002|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3121kri001"
    霧 "「その、朝食をと思ったんですが、どうにも……」"
    太一 "「あー、なんもないからね」"
    call gl(1,"TCSK0000|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3121kri002"
    霧 "「じゃがいもがありました」"
    太一 "「なぬ、そんないいものが？」"
    "あったような気がする。"
    "……………………。"
    call gl(1,"TCSK0006|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3121kri003"
    霧 "「ふかしてみたんですけど」"
    太一 "「……ほー、ほーほー」"
    "いきなり食欲がわいた。"
    voice "vfCCC3121kri004"
    霧 "「塩でどうぞ」"
    太一 "「うん、食おう」"
    "山盛りのじゃがいも。"
    voice "vfCCC3121kri005"
    霧 "「おいしいですね」"
    太一 "「うん、うまい。火が通ってる」"
    call gl(1,"TCSK0002|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3121kri006"
    霧 "「バターあったらよかったんですけど、さすがに」"
    太一 "「なぁに、じきいくらでも食えるさ」"
    call gl(1,"TCSK0000|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3121kri007"
    霧 "「え……どうしてですか？」"
    太一 "「あ……えーと……まあ、いろいろと」"
    voice "vfCCC3121kri008"
    霧 "「？？？」"
    太一 "「うおー、食った食った」"
    call gl(1,"TCSK0002|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3121kri009"
    霧 "「お粗末様です」"
    太一 "「あ、いけね、準備しないと」"
    call gl(1,"TCSK0000|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3121kri010"
    霧 "「……あ、山に行くという」"
    voice "vfCCC3121kri011"
    霧 "「包んでいきますね、これ」"
    太一 "「あー、いっていって、着の身着のまま～」"
    voice "vfCCC3121kri012"
    霧 "「はあ……」"
    call gl(0,"bgcc0005")
    call vsp(0,1)
    call vsp(1,0)
    with wipeleft
    太一 "「ところで……疑問に思わないの？」"
    call gl(1,"TCSK0002|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3121kri013"
    霧 "「……はい、思わないです」"
    太一 "「あんま気張らないことだよ。罪なんて、ただの概念なんだから」"
    voice "vfCCC3121kri014"
    霧 "「こんなこと言ったら、怒られるかも知れませんけど」"
    call gl(1,"TCSK0006|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3121kri015"
    霧 "「……わたし、少し嬉しいんです」"
    太一 "「嬉しい？」"
    voice "vfCCC3121kri016"
    霧 "「先輩が豊のこと、友達と思ってくれてることが」"
    太一 "「……あー」"
    call gl(1,"TCSK0000|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3121kri017"
    霧 "「学校では、ずっと二人で頑張ってきたので」"
    太一 "「一心同体だったわけか」"
    voice "vfCCC3121kri018"
    霧 "「はい、そうですね」"
    太一 "「んー、豊がいなくなって……そんで美希と一心同体になったんだな」"
    voice "vfCCC3121kri019"
    霧 "「はい」"
    call gl(1,"TCSK0002|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3121kri020"
    霧 "「……卑怯でしょうか、こういうの？」"
    太一 "「いんでない。ま、俺の保証はアテにはならないけど」"
    call gl(1,"TCSK0000|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3121kri021"
    霧 "「そんなことは……」"
    太一 "「さて、登山登山。行くぞ」"
    call gl(1,"TCSK0006|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3121kri022"
    霧 "「オス」"
    call gl(0,"bgcc0015")
    call vsp(0,1)
    call vsp(1,0)
    with wipeleft
    call gl(1,"TCSK0000|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3121kri023"
    霧 "「そうそう、先輩」"
    太一 "「んー？」"
    call gl(1,"TCSK0007|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3121kri024"
    霧 "「……愛奴隷というのに、なってみようかと思うんですが」"
    太一 "「ぶっ」"
    "吹いた。"
    太一 "「血迷ったか、霧っち！」"
    call gl(1,"TCSK0002|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3121kri025"
    霧 "「ケジメは必要でしょう？」"
    call gl(1,"TCSK0000|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3121kri026"
    霧 "「それに先輩、よく愛奴隷愛奴隷言ってたじゃないですか」"
    voice "vfCCC3121kri027"
    霧 "「異論はないはずです」"
    太一 "「あるある、あれ冗談だし」"
    call gl(1,"TCSK0002|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3121kri028"
    霧 "「不慣れですけど、よろしくお願いします」"
    太一 "「お願いされない！」"
    call gl(1,"TCSK0006|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3121kri029"
    霧 "「あはっ」"
    太一 "「……おまえ俺をからかったな？」"
    call gl(1,"TCSK0002|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3121kri030"
    霧 "「いいえ、めっそうもない」"
    太一 "「ふ……一段落ついたらまたいじめてやる」"
    voice "vfCCC3121kri031"
    霧 "「どうぞ！」"
    太一 "「スカートもめくってやるぞ」"
    call gl(1,"TCSK0006|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3121kri032"
    霧 "「どうぞ！」"
    太一 "「えーと……Ｈな悪戯フルセットで」"
    voice "vfCCC3121kri033"
    霧 "「どうぞ！」"
    太一 "「……あのなあ霧！」"
    voice "vfCCC3121kri034"
    霧 "「なんでもどうぞ！」"
    call gl(1,"TCSK0007|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3121kri035"
    霧 "「……駄目ですか？」"
    太一 "「駄目ってこたないけど……それ俺が駄目になるから」"
    voice "vfCCC3121kri036"
    霧 "「え……？」"
    太一 "「それにそういうのだったら、もう一人いるしね」"
    call gl(1,"TCSK0002|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3121kri037"
    霧 "「あ……支倉先輩……」"
    call gl(1,"TCSK0000|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3121kri038"
    霧 "「あの、支倉先輩と太一先輩って……その……」"
    太一 "「ストーカーされてんのよ、俺」"
    voice "vfCCC3121kri039"
    霧 "「迷惑なんですか？」"
    太一 "「大変に迷惑だね。追っ払いたい」"
    call gl(1,"TCSK0002|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3121kri040"
    霧 "「……それ、どうです？」"
    太一 "「それ？」"
    call gl(1,"TCSK0000|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3121kri041"
    霧 "「わたしが、あの人を追い出します」"
    太一 "「……おいおい、そいつはディフィカルト教団すぎるぞ……霧ちんじゃ太刀打ちできないって」"
    call gl(1,"TCSK0002|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3121kri042"
    霧 "「特訓しますよ。いろいろ習って」"
    太一 "「無理だ……ストーカーとしての才能が違いすぎるよ」"
    call gl(1,"TCSK0006|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3121kri043"
    霧 "「愛奴隷ですから、愛で勝負します」"
    太一 "「……んー、でも霧は臆病で気弱だからなぁ……難しいと思うわ」"
    call gl(1,"TCSK0000|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3121kri044"
    霧 "「……え……そんなことは」"
    太一 "「それだって、俺に対する依存なんだぜ？」"
    霧 "「…………」"
    太一 "「いいんだけど、俺はまずいよ、霧っち」"
    call gl(1,"TCSK0003|TCSK0003")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3121kri046"
    霧 "「……じゃあ、どうしたら……わたしの居場所が……」"
    太一 "「霧っちの居場所、心当たりがある」"
    太一 "「これから向かってるとこさ」"
    voice "vfCCC3121kri047"
    霧 "「これが……？」"
    call gl(0,"bgcc0016")
    call vsp(0,1)
    call vsp(1,0)
    with wipeleft
    太一 "「そら、ついたぞ」"
    call gl(1,"TCSK0000|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3121kri048"
    霧 "「……お社、ですね？」"
    太一 "「ま、それ自体はどうでもいいんだ。こっちこっち」"
    voice "vfCCC3121kri049"
    霧 "「……何も、ないですよ？」"
    太一 "「これポケットに入れて」"
    call gl(1,"TCSK0002|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3121kri050"
    霧 "「ラジオですか？　はい……」"
    太一 "「さて、霧……俺はここで観測しているから、真っ直ぐ歩いていってくれるか？」"
    call gl(1,"TCSK0000|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3121kri051"
    霧 "「え？」"
    太一 "「ここを真っ直ぐ」"
    voice "vfCCC3121kri052"
    霧 "「いいですけど……？」"
    太一 "「ゆっくりな。俺が指示した場所で止まってくれ」"
    voice "vfCCC3121kri053"
    霧 "「……はい？」"
    call gl(1,"TCSK0002|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3121kri054"
    霧 "「そろーりそろり、と」"
    太一 "「もうちょっと先」"
    voice "vfCCC3121kri055"
    霧 "「そろそろ」"
    太一 "「少し右！」"
    call gl(1,"TCSK0000|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3121kri056"
    霧 "「こっちですか？」"
    太一 "「そーそー」"
    太一 "「そのま微速前進０．５」"
    call gl(1,"TCSK0002|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3121kri057"
    霧 "「うわ、わかんない……ゆっくり、かな？」"
    太一 "「そこでストップ」"
    call gl(1,"TCSK0006|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3121kri058"
    霧 "「はい！」"
    call gl(0,"evcc0060")
    call vsp(0,1)
    call vsp(1,0)
    with Dissolve(500.0/1000.0)
    "よし、場所はＯＫ。"
    voice "vfCCC3121kri059"
    霧 "「？」"
    stop bgm
    "これで目を切り替えれば……。"
    太一 "「なあ霧っち」"
    voice "vfCCC3121kri060"
    霧 "「はい？」"
    太一 "「居場所」"
    voice "vfCCC3121kri061"
    霧 "「え？　なんですー？」"
    太一 "「居場所だよ、霧。居場所の手に入れかた」"
    voice "vfCCC3121kri062"
    霧 "「居場所？」"
    太一 "「話したろ？　心のせめぎあいだって」"
    play bgm "bgm/bgm023.ogg"
    voice "vfCCC3121kri063"
    霧 "「はあ？」"
    太一 "「おまえは、繊細で鋭すぎるから、人よりいろんなものが見えてしまうけど」"
    太一 "「その目なら、大切な人を見つけることはできるだろ」"
    voice "vfCCC3121kri064"
    霧 "「はは……恐縮です！」"
    voice "vfCCC3121kri065"
    霧 "「でも、大切な人は、もういますから！」"
    太一 "「いいや……これから、作るんだ」"
    太一 "「それに、あとで美希も送ってやるからな」"
    voice "vfCCC3121kri066"
    霧 "「え？」"
    太一 "「つらいこととか、理不尽なこととか、悪意とか」"
    太一 "「悲喜こもごもあるけどさ」"
    太一 "「なにもないより、人の世界はマシなんだ」"
    太一 "「それはわかるよな？」"
    太一 "「だから、頑張れる」"
    voice "vfCCC3121kri067"
    霧 "「先輩？　さっきから何を？」"
    太一 "「おまえに会うのも、これで最後になるけど」"
    太一 "「もらった思い出は、ありがたく使わせてもらうさ」"
    voice "vfCCC3121kri068"
    霧 "「意味が、わからないんですけど……？」"
    太一 "「健闘を祈る！」"
    "敬礼。"
    "霧の表情が、さっと不安味を増した。"
    voice "vfCCC3121kri069"
    霧 "「なに……を……？」"
    call gl(0,"evcc0060a")
    call vsp(0,1)
    call vsp(1,0)
    with Dissolve(500.0/1000.0)
    voice "vfCCC3121kri070"
    霧 "「なにをしようとしてるんですか！？」"
    "霧がこっちに駆け戻るよりはやく。"
    "緋色が。"
    "そして。"
    stop bgm
    call gl(0,"bgcc0000d")
    call vsp(0,1)
    with Dissolve(500.0/1000.0)
    "カシャ―――"
    "俺は『観測』した。"
    "目を閉じて、開くと―――"
    pause (1500.0/1000.0)
    call gl(0,"bgcc0000b")
    call vsp(0,1)
    with Dissolve(500.0/1000.0)
    voice "vfCCC3121kri071"
    霧 "「なにをしようとしてるんですか！？」"
    voice "vfCCC3121kri072"
    霧 "「……あれ？」"
    voice "vfCCC3121kri073"
    霧 "「え……先輩？　どこ？」"
    voice "vfCCC3121kri074"
    霧 "「先輩！　先輩ってば！」"
    voice "vfCCC3121kri075"
    霧 "「あれ……いない……あれ？」"
    call gl(0,"bgcc0001b")
    call vsp(0,1)
    with wipeleft
    voice "vfCCC3121kri076"
    霧 "「……街が……え？」"
    voice "vfCCC3121kri077"
    霧 "「人が、いる？」"
    play se "SE099"
    voice "vfCCC3121kri078"
    霧 "「ラジオが……入った……」"
    voice "vfCCC3121kri079"
    霧 "「電波がっ！？」"
    voice "vfCCC3121kri080"
    霧 "「これって……？」"
    voice "vfCCC3121kri081"
    霧 "「先輩！　先輩！　先輩！　先輩先輩先輩先輩っ！」"
    voice "vfCCC3121kri082"
    霧 "「はあっ……たいち、せんぱい……？」"
    voice "vfCCC3121kri083"
    霧 "「……いないの？」"
    voice "vfCCC3121kri084"
    霧 "「うそ、どうして……」"
    voice "vfCCC3121kri085"
    霧 "「いなくなるのよ……っ」"
    voice "vfCCC3121kri086"
    霧 "「……わけ、わかんない……」"
    stop se
    play bgm "bgm/bgm001.ogg"
    voice "vfCCC3121kri087"
    霧 "「あああああーーーーーーーーっ！！」"
    voice "vfCCC3121kri088"
    霧 "「ああああああああああっ！」"
    voice "vfCCC3121kri089"
    霧 "「はぁ、はぁ……なんで……うわあああああぁぁぁぁぁぁぁぁぁぁぁぁぁぁぁっ！！」"
    call gl(0,"bgcc0000d")
    call vsp(0,1)
    with Dissolve(500.0/1000.0)
    pause (2000.0/1000.0)
    call gl(0,"bgcc0016")
    call vsp(0,1)
    with Dissolve(500.0/1000.0)
    太一 "「……」"
    太一 "「いいんだよな、これで」"
    太一 "「霧やー」"
    "一応呼んでみた。"
    "当然だけど、反応はない。"
    太一 "「うむ」"
    "ただ俺だけが観測できる。"
    "そして多世界は、限りなく同じ軸に重なっている。"
    "だから霧はすぐそばにいるんだ。"
    "互いを知覚できないだけで。"
    "同じ世界で生きている。"
    "何をもってしても繋がることはできないが。"
    "観測した瞬間、現実に固定される。"
    "いや。"
    "全ての可能性が、最初から同じ軸にある。"
    "見る者がいるか、いないか……それだけだ。"
    "さて。"
    "俺はまた、時を待とう。"
    "キャンプに戻り、テントに入る。"
    "じきだ。"
    "寝て起きたら、"
    call gl(0,"bgcc0000d")
    call vsp(0,1)
    with Dissolve(500.0/1000.0)
    "また、来週―――"
    stop bgm
    pause (1500.0/1000.0)
    return
    #