label ccc4015:
    call gl(0,"bgcc0019")
    call vsp(0,1)
    call vsp(1,0)
    call vsp(2,0)
    with wipeleft
    play bgm "bgm/bgm007.ogg"
    "冬子の家。"
    "いや……屋敷。"
    call gl(0,"bgcc0000d")
    call vsp(0,1)
    with Dissolve(500.0/1000.0)
    "中に入ると、一面の闇だった。"
    "窓は締め切ってある。"
    "懐中電灯を取り出し、冬子の部屋に。"
    "昔、何度か来たことがある。"
    "父親に紹介されそうになったんだよな。"
    "……逃げたけど。"
    "二階。"
    "部屋を一つ一つ確認していく。"
    "たしかこのあたり……。"
    "無数にある扉の一つを開くと。"
    "光がさしこんだ。"
    call gl(5,"bgcc0000e")
    call gl(0,"evcc0050a")
    call vsp(5,1)
    with dissolve
    call vsp(0,1)
    call vsp(5,0)
    with Dissolve(500.0/1000.0)
    太一 "「……………………」"
    "窓は全開だった。"
    "そっと入り込んだ風が、室内を旋回してまた出ていく。"
    "だからだろうか。"
    "腐臭さえしない。"
    太一 "「……冬子」"
    "胸に、刃物がひとつき。"
    "なるほど確かに他殺体だ。"
    "刃物はこの屋敷のものだろうか。"
    "柄が華美に彫り込まれた、調度品めいた短剣である。"
    "出血はある。"
    "胸元からシーツまでを濡らして、赤黒く変色させていた。"
    "だけど。"
    "きれいな骸ではあった。"
    "冬子らしい、気高い死体だと思った。"
    太一 "「…………」"
    "俺はしばらく、佇んでいた。"
    "心臓とともに、時間まで射抜かれたのか。"
    "冬子はまるで止まっているようだった。"
    "短剣を抜いたら、すぐにでも起きて俺の非礼をののしりそうな。"
    "そんな気がした。"
    call gl(0,"bgcc0005")
    call vsp(0,1)
    with wipeleft
    "……誰が殺したのだろう。"
    "残念ながら、容疑者は数えるほどしかいない。"
    "霧。"
    "美希。"
    extend "友貴"
    "桜庭。"
    "みみ先輩。"
    "他に隠れている人間がいれば別だが、これで全員。"
    "まず霧。"
    "ないように思う。"
    "第一発見者ではあるが。"
    "考えにくい。"
    "霧の怒りは本物で、混乱もまた真実だった。"
    "美希。"
    "可能性はある。"
    "だけど動機がわからない。"
    "もはやアリバイなんて意味はないわけで、美希がどこで何をしているのか、確実に知る術はない。"
    "可哀相だが、容疑者①。"
    "友貴。"
    "容疑者②である。"
    "やはり動機は不明。"
    "桜庭。"
    "容疑者③。同上。"
    "みみ先輩。"
    "容疑者④。同上。"
    太一 "「うーん」"
    "ほとんど手がかりはない。"
    "殺しそうな人間も動機も、見えていない。"
    "また曜子ちゃんを殺した者と、冬子を殺した者が同一人物だとは限らない。"
    "……探偵って難しいな。"
    call gl(0,"bgcc0011")
    call vsp(0,1)
    with wipeleft
    "正門のあたりで、容疑者②を発見した。"
    "奇襲尋問に入る。"
    太一 "「年齢は？」"
    call gl(1,"TCST0000|TCST0000")
    call gp(1,t=center)#x=190
    call vsp(1,1)
    with dissolve
    voice "vmCCC4015yki000"
    友貴 "「……言えません」"
    "さすが友貴。"
    "俺の奇襲にも動じた様子はない。"
    太一 "「年齢を言えないだと？　理由は？」"
    call gl(1,"TCST0004|TCST0004")
    call vsp(1,1)
    with dissolve
    voice "vmCCC4015yki001"
    友貴 "「理由は言えません」"
    太一 "「理由も言えないのか？」"
    voice "vmCCC4015yki002"
    友貴 "「はい……すいません」"
    太一 "「質問を変えよう。二十歳より上かね、下かね？」"
    call gl(1,"TCST0000|TCST0000")
    call vsp(1,1)
    with dissolve
    voice "vmCCC4015yki003"
    友貴 "「下です」"
    太一 "「１８歳より下かね？」"
    call gl(1,"TCST0004|TCST0004")
    call vsp(1,1)
    with dissolve
    voice "vmCCC4015yki004"
    友貴 "「言えません」"
    太一 "「ふーむ。１７歳かね？」"
    voice "vmCCC4015yki005"
    友貴 "「絶対に言えません」"
    太一 "「君は高校生なんじゃないのか？」"
    call gl(1,"TCST0001|TCST0001")
    call vsp(1,1)
    with dissolve
    voice "vmCCC4015yki006"
    友貴 "「……そんなものはこの世に存在しません」"
    太一 "「女子高生と女子校生はどっちがダメなんだ？」"
    call gl(1,"TCST0004|TCST0004")
    call vsp(1,1)
    with dissolve
    voice "vmCCC4015yki007"
    友貴 "「どっちもダメって聞いたことがあります」"
    太一 "「生徒手帳というものを知っているかも？」"
    voice "vmCCC4015yki006"
    友貴 "「……そんなものはこの世に存在しません」"
    太一 "「年齢は？」"
    call gl(1,"TCST0000|TCST0000")
    call vsp(1,1)
    with dissolve
    voice "vmCCC4015yki008"
    友貴 "「思春期です」"
    太一 "「……年齢確かめることもできねーのかよ」"
    call gl(1,"TCST0003|TCST0000")
    call vsp(1,1)
    with dissolve
    voice "vmCCC4015yki009"
    友貴 "「しかたないだろー」"
    "尋問はダメだ。やってられん。"
    太一 "「で、どうしたんだ？」"
    call gl(1,"TCST0000|TCST0000")
    call vsp(1,1)
    with dissolve
    voice "vmCCC4015yki010"
    友貴 "「……別に。帰ろうとしてただけだよ」"
    太一 "「突っ立ってたじゃないか。なんか電波でも受信せんばかりに」"
    voice "vmCCC4015yki011"
    友貴 "「……帰るよ。帰ろうとしてたんだ」"
    hide pic1
    with dissolve
    "トロトロと友貴は去っていった。"
    太一 "「なんだあいつ？」"
    "ヤツが立っていた場所から、視線を追う。"
    "屋上。"
    "アンテナ。"
    "そして。"
    "みみ先輩―――"
    "フェンスにしがみつくようにして、街並みを眺めていた。"
    "しばらくして、身を離してアンテナ側に消えた。"
    太一 "「？」"
    "喧嘩してるんだったな、あの二人。"
    "とても人を殺す余裕があるとは思えなかった。"
    call gl(0,"bgcc0008")
    call vsp(0,1)
    with wipeleft
    "美希がトイレから出てきた。"
    call gl(1,"TCYM0000|TCYM0000")
    call gp(1,t=center)#x=180
    call vsp(1,1)
    with dissolve
    voice "vfCCC4015mki000"
    美希 "「あ、せんぱーい」"
    太一 "「よっ、容疑者②」"
    call gl(1,"TCYM0004|TCYM0002")
    call vsp(1,1)
    with dissolve
    voice "vfCCC4015mki001"
    美希 "「……え゛？」"
    太一 "「年齢は？」"
    call gl(1,"TCYM0003|TCYM0003")
    call vsp(1,1)
    with dissolve
    voice "vfCCC4015mki002"
    美希 "「言えません」"
    太一 "「年齢を言えないだと？　理由は？」"
    call gl(1,"TCYM0001|TCYM0000")
    call vsp(1,1)
    with dissolve
    voice "vfCCC4015mki003"
    美希 "「理由も言えません」"
    太一 "「ふむ。では質問を変えよう。二十歳より上かね、下かね？」"
    voice "vfCCC4015mki004"
    美希 "「下です」"
    太一 "「１８歳より下かね？」"
    call gl(1,"TCYM0003|TCYM0003")
    call vsp(1,1)
    with dissolve
    voice "vfCCC4015mki005"
    美希 "「外見は１５歳くらいに見えるとよく言われます」"
    太一 "「誰が主観の話をしろと言った」"
    call gl(1,"TCYM0000|TCYM0000")
    call vsp(1,1)
    with dissolve
    voice "vfCCC4015mki006"
    美希 "「はい、スミマセン」"
    太一 "「１８歳以下なのかね？」"
    call gl(1,"TCYM0041|TCYM0041")
    call vsp(1,1)
    with dissolve
    voice "vfCCC4015mki007"
    美希 "「仕方ありません。真実をお話します……うっ、突然お腹が痛みました」"
    太一 "「なんてタイミングだ。シット！」"
    太一 "「最後に教えてくれ。君は高校生で女子高生と女子校生で生徒手帳なのではないのかね？」"
    call gl(1,"TCYM0001|TCYM0000")
    call vsp(1,1)
    with dissolve
    voice "vfCCC4015mki008"
    美希 "「その四つの単語はこの世に存在しません」"
    太一 "「そうか……では最後に年齢は？」"
    call gl(1,"TCYM0011|TCYM0011")
    call vsp(1,1)
    with dissolve
    voice "vfCCC4015mki009"
    美希 "「十万十五歳です」"
    太一 "「木暮一族？」"
    "遅れて霧がトイレから出てきた。"
    call gl(2,"TCSK0001|TCSK000x")
    call gp(1,t=left)#x=40
    call gp(2,t=right)#x=300
    call vsp(1,1)
    call vsp(2,1)
    with Dissolve(500.0/1000.0)
    voice "vfCCC4015kri000"
    霧 "「黒須太一！」"
    "たちまち目が吊り上がる。"
    voice "vfCCC4015kri001"
    霧 "「美希、その人と話しちゃだめだよ！」"
    call gl(1,"TCYM0021|TCYM0021")
    call vsp(1,1)
    with dissolve
    voice "vfCCC4015mki010"
    美希 "「えー？　でも？」"
    call gl(2,"TCSK0002|TCSK000x")
    call vsp(2,1)
    with dissolve
    voice "vfCCC4015kri002"
    霧 "「危ないから」"
    太一 "「まだそんなことを言ってるのか」"
    太一 "「冬子、見てきたよ。確かに死んでたな」"
    call gl(2,"TCSK0001|TCSK000x")
    call vsp(2,1)
    with dissolve
    voice "vfCCC4015kri003"
    霧 "「……ぬけぬけと」"
    太一 "「仲間が死んだんだぞ。復讐より先に抱くべき感情はないのか」"
    call gl(2,"TCSK0003|TCSK0003")
    call vsp(2,1)
    with dissolve
    voice "vfCCC4015kri004"
    霧 "「そんなの……い、言われるまでもない……」"
    "……俺が言う台詞じゃないけどな。"
    call gl(1,"TCYM0001|TCYM0000")
    call vsp(1,1)
    with dissolve
    voice "vfCCC4015mki011"
    美希 "「それじゃ犯人って……」"
    太一 "「俺等全員が容疑者」"
    call gl(1,"TCYM0021|TCYM0021")
    call vsp(1,1)
    with dissolve
    voice "vfCCC4015mki012"
    美希 "「……どうしましょお？」"
    太一 "「全員が一箇所にいるのがいいんじゃないかな」"
    call gl(2,"TCSK0021|TCSK0021")
    call vsp(2,1)
    with dissolve
    voice "vfCCC4015kri005"
    霧 "「いやよ！」"
    太一 "「……だろうな」"
    voice "vfCCC4015kri006"
    霧 "「わたしは美希といます！　あなたは一人で勝手にいればいい。どうせ……あなたが犯人なんだから」"
    太一 "「……もういいよ、それで」"
    call gl(2,"TCSK0001|TCSK000x")
    call vsp(2,1)
    with dissolve
    voice "vfCCC4015kri007"
    霧 "「美希にも近づかないでください」"
    太一 "「……んー」"
    太一 "「どうしてそんなことまで、霧に約束しないといけないんだ？」"
    call gl(1,"TCYM0041|TCYM0041")
    call vsp(1,1)
    with dissolve
    voice "vfCCC4015mki013"
    美希 "「あー、またぁ……」"
    太一 "「俺は話したい相手に話しかけるよ。相手がどう反応するかは、そいつの自由」"
    call gl(2,"TCSK0002|TCSK000x")
    call vsp(2,1)
    with dissolve
    voice "vfCCC4015kri008"
    霧 "「……美希はだめです」"
    太一 "「それは霧が決めることじゃないだろ」"
    voice "vfCCC4015kri009"
    霧 "「美希は……わたしのはじめての親友ですから」"
    call gl(2,"TCSK0001|TCSK000x")
    call vsp(2,1)
    with dissolve
    voice "vfCCC4015kri010"
    霧 "「……みすみす危害を加えさせるつもりはないです」"
    太一 "「くわえないってば」"
    call gl(2,"TCSK0004|TCSK000x")
    call vsp(2,1)
    with dissolve
    voice "vfCCC4015kri011"
    霧 "「ずっと、いじめられて……あんな試験結果なんかで……」"
    "涙ぐむ。"
    "うへぇ……。"
    "げっそりした。"
    太一 "「それ俺のせいちゃうで……」"
    call gl(2,"TCSK0001|TCSK000x")
    call vsp(2,1)
    with dissolve
    voice "vfCCC4015kri012"
    霧 "「だから……わたしは……わたしの友達を、守りますから！」"
    太一 "「……あいよ」"
    "もう霧はダメだ。"
    "いろんな意味で。"
    call gl(1,"TCYM0001|TCYM0000")
    call vsp(1,1)
    with dissolve
    voice "vfCCC4015mki014"
    美希 "「霧ちん、もうよしなよ。なにもかも先輩のせいにして、もし他の人が犯人だったらどうするの？」"
    call gl(2,"TCSK0002|TCSK000x")
    call vsp(2,1)
    with dissolve
    voice "vfCCC4015kri013"
    霧 "「……そんなことない」"
    call gl(1,"TCYM0002|TCYM0002")
    call vsp(1,1)
    with dissolve
    voice "vfCCC4015mki015"
    美希 "「そうやって決めつける」"
    太一 "「ねえ？」"
    call gl(1,"TCYM0003|TCYM0003")
    call vsp(1,1)
    with dissolve
    voice "vfCCC4015mki016"
    美希 "「ねー？」"
    "美希とはウマが合うのにね。"
    太一 "「とりあえず、桜庭か友貴犯人説で動く」"
    call gl(1,"TCYM0000|TCYM0000")
    call vsp(1,1)
    with dissolve
    voice "vfCCC4015mki017"
    美希 "「男の友情っていいなぁ」"
    太一 "「誉めるない、照れるじゃねぇか」"
    太一 "「……け、けどもしみみ先輩が犯人だったら……つ、つ、つ、つみをつぐなわないといけないよね、あの罪つくりボディで」"
    call gl(1,"TCYM0003|TCYM0003")
    call vsp(1,1)
    with dissolve
    voice "vfCCC4015mki018"
    美希 "「きゃん」"
    call gl(2,"TCSK0004|TCSK000x")
    call vsp(2,1)
    with dissolve
    voice "vfCCC4015kri014"
    霧 "「……やめて……」"
    太一 "「君も気をつけたまえ。もし犯人だったら……そーとーエロいことになりますよ」"
    "架空のハマキをふかす。"
    call gl(2,"TCSK0021|TCSK0021")
    call vsp(2,1)
    with dissolve
    voice "vfCCC4015kri015"
    霧 "「やめてよっ！」"
    call gl(1,"TCYM0000|TCYM0000")
    call vsp(1,1)
    with dissolve
    太一 "「……え？」"
    voice "vfCCC4015kri016"
    霧 "「だからっ、どうして仲良くするのっっ！？」"
    "シーン……"
    voice "vfCCC4015kri017"
    霧 "「危険なのに！　危ないのに！！」"
    call gl(1,"TCYM0002|TCYM0002")
    call vsp(1,1)
    with dissolve
    voice "vfCCC4015mki019"
    美希 "「いや……霧ちん、そこまで警戒しないでも」"
    太一 "「俺も生きてちゃいけないような気がしてきた……」"
    call gl(1,"TCYM0001|TCYM0000")
    call vsp(1,1)
    with dissolve
    voice "vfCCC4015mki020"
    美希 "「霧っち言い過ぎ」"
    voice "vfCCC4015kri018"
    霧 "「美希は甘すぎるよ、この人は自分のお姉さんみたいな人、殺してるんだよ？」"
    call gl(1,"TCYM0000|TCYM0000")
    call vsp(1,1)
    with dissolve
    voice "vfCCC4015mki021"
    美希 "「あれは……どうなんですか？」"
    太一 "「俺じゃないよ。もう死んでたし」"
    太一 "「だいたいナイフの傷じゃないでしょ、あれ」"
    call gl(2,"TCSK0001|TCSK000x")
    call vsp(2,1)
    with dissolve
    voice "vfCCC4015kri019"
    霧 "「わかるもんか」"
    "俺は嘔吐するようにため息をついた。"
    太一 "「はぁ。美希、たすけて……」"
    call gl(1,"TCYM0001|TCYM0000")
    call vsp(1,1)
    with dissolve
    voice "vfCCC4015mki022"
    美希 "「霧ちんが悪い」"
    "びしっ。"
    call gl(2,"TCSK0004|TCSK000x")
    call vsp(2,1)
    with dissolve
    voice "vfCCC4015kri020"
    霧 "「どうして……わたし、美希のために……」"
    call gl(1,"TCYM0001|TCYM0000")
    call vsp(1,1)
    with dissolve
    voice "vfCCC4015mki023"
    美希 "「まだそんなこと言ってる。ゼッコーしちゃうよ」"
    voice "vfCCC4015kri021"
    霧 "「美希……」"
    太一 "「そんなゼッコーせんでも」"
    call gl(1,"TCYM0000|TCYM0000")
    call vsp(1,1)
    with dissolve
    voice "vfCCC4015mki024"
    美希 "「だって、わたし霧ちんのお人形さんじゃないです」"
    call gl(1,"TCYM0001|TCYM0000")
    call vsp(1,1)
    with dissolve
    voice "vfCCC4015mki025"
    美希 "「……まだ先輩の方が、わたしのこと尊重してくれるじゃないですか」"
    voice "vfCCC4015kri022"
    霧 "「！？」"
    "あ、今のは効いたぞ。"
    call gl(1,"TCYM0001|TCYM0000")
    call vsp(1,1)
    with dissolve
    voice "vfCCC4015mki026"
    美希 "「友達なら、尊重しようよ。こんなときに、どうして火種をまこうとするの？」"
    voice "vfCCC4015kri023"
    霧 "「だって、だってっ」"
    call gl(1,"TCYM0003|TCYM0003")
    call vsp(1,1)
    with dissolve
    voice "vfCCC4015mki027"
    美希 "「ほら、先輩にあやまろー」"
    "霧は歯を食いしばった。"
    "相当悔しい様子。"
    "キッと俺を見あげる。"
    call gl(2,"TCSK0021|TCSK0021")
    call vsp(2,1)
    with dissolve
    voice "vfCCC4015kri024"
    霧 "「……誰が、あんたなんかにっ！！」"
    voice "vfCCC4015mki028"
    美希 "「こりゃ！！」"
    hide pic2
    with dissolve
    "霧は踵を切り返し、走り去った。"
    call gl(1,"TCYM0004|TCYM0002")
    call vsp(1,1)
    with dissolve
    voice "vfCCC4015mki029"
    美希 "「うわ、逃げた……」"
    太一 "「いい逃げ足だ」"
    "二人で霧の背中が消えるのを眺めていた。"
    太一 "「……ところでさ、美希ぽん」"
    call gl(1,"TCYM0000|TCYM0000")
    call vsp(1,1)
    with dissolve
    voice "vfCCC4015mki030"
    美希 "「美希ぽんです。何でしょう？」"
    太一 "「……背、伸びた？」"
    voice "vfCCC4015mki031"
    美希 "「そうですか？　自分では見えないんですが」"
    "当然だ。"
    太一 "「あれあれ、よく見ると胸も……」"
    voice "vfCCC4015mki032"
    美希 "「だめですよぉ、踊り子さんに触っちゃ」"
    "胸を両手でガードした。"
    太一 "「ちっ」"
    "ま、いっか。"
    太一 "「とかやってるうちにもう夕方だ」"
    voice "vfCCC4015mki033"
    美希 "「……帰りますか。霧っち一人で行っちゃったし」"
    太一 "「あとでフォローしといてやってくれ。俺ではアカン……」"
    call gl(1,"TCYM0003|TCYM0003")
    call vsp(1,1)
    with dissolve
    voice "vfCCC4015mki034"
    美希 "「はーい」"
    "美希は強い。"
    "こんなときに平静でいられるタイプだとは思わなかった。"
    "人間の真価は、危機が訪れる時に発揮されるらしい。"
    stop bgm
    return
    #