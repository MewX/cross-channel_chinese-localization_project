label ccb0007:
    call gl(0,"bgcc0008")
    call vsp(1,0)
    call vsp(0,1)
    with wipeleft
    play bgm "bgm/bgm002.ogg"
    "教室に戻る途中、処女がうずくまっていた。"
    "美希だ。"
    "山辺美希。"
    太一 "「おーす」"
    call gl(1,"TCYM0001|TCYM0000")
    call gp(1,t=center)#x=180
    call vsp(1,1)
    with dissolve
    voice "vfccb0007mki000"
    美希 "「っ！？」"
    "美希は立ち上がる。"
    "素早い挙動。"
    "ゆっくりと振り返った。"
    call gl(1,"TCYM0003|TCYM0003")
    call vsp(1,1)
    with dissolve
    voice "vfccb0007mki001"
    美希 "「あ、先輩……どぉも」"
    "顔をあげて会釈。"
    "いつもと変わる風でもない美希だ。"
    "少し違和感。"
    "美希は、こんな強かったのだろうか？"
    "もともと素質はあったようだが、一回りも二回りもたくましくなったような。"
    "そんな感じがする。"
    太一 "「なにしてんの？」"
    call gl(1,"TCYM0000|TCYM0000")
    call vsp(1,1)
    with dissolve
    voice "vfccb0007mki002"
    美希 "「そーじです」"
    太一 "「俺もやったぞ、そーじ」"
    voice "vfccb0007mki003"
    美希 "「表面的な言葉遊びで送辞と相似とか言いますか？」"
    太一 "「……言いません！」"
    call gl(1,"TCYM0021|TCYM0021")
    call vsp(1,1)
    with dissolve
    voice "vfccb0007mki004"
    美希 "「なぜ怒るです」"
    太一 "「……」"
    call gl(1,"TCYM0000|TCYM0000")
    call vsp(1,1)
    with dissolve
    voice "vfccb0007mki005"
    美希 "「なぜ黙るです」"
    太一 "「そんなオチを封じた上にせかすなようっっ」"
    call gl(1,"TCYM0003|TCYM0003")
    call vsp(1,1)
    with dissolve
    voice "vfccb0007mki006"
    美希 "「わーい、勝ったー」"
    "たくましかった。"
    太一 "「あ、思いついた」"
    "咳払い。"
    太一 "「……人類を掃除した」"
    call gl(1,"TCYM0001|TCYM0000")
    call vsp(1,1)
    with dissolve
    voice "vfccb0007mki007"
    美希 "「きさまが犯人かー！」"
    hide pic1
    with dissolve
    太一 "「はー！」"
    "たたかう二人。"
    太一 "「よっ」"
    太一 "「ほっ」"
    太一 "「……はっ？」"
    play se "se003"
    with vpunch
    太一 "「おっっ！？」"
    "胴体に一発当たってしまった。"
    "う、なんか強い？"
    "カラデをおさめたこの俺を。"
    太一 "「おのれ」"
    "ちょっぴり本気になる。"
    voice "vfccb0007mki008"
    美希 "「しゅっ」"
    "しなやかな脚が、腰より高くあがった。"
    "軸足を払ってやろうと思ったが、白パンツが垣間見えた。"
    "攻撃中止。"
    "男太一、眼前に供えられたパンツを見ないなどという惰弱な選択肢はない。"
    menu:
        "パンツ見る":
            pass
        "パンツ見る":
            pass
        "パンツ見る":
            pass
    "うむ、ない。"
    "腰を落として視線を下げた。"
    "蹴りが来る。"
    "カラデによる中段受けにて備える。"
    "腕の間を、つまさきは柔らかく貫通してきた。"
    太一 "「れ？」"
    "ありえん。"
    call gl(5,"bgcc0000d")
    call vsp(5,1)
    with dissolve
    play se "SE071"
    with vpunch
    "顎にヒット。"
    stop bgm
    太一 "「あらら？」"
    "俺は気絶した。"
    "……。"
    call vsp(5,0)
    call vsp(1,0)
    with Pixellate(300.0*2/1000.0,5)
    "…………。"
    call gl(0,"bgcc0008")
    call vsp(0,1)
    with Pixellate(300.0*2/1000.0,5)
    "……………………。"
    play bgm "bgm/bgm002.ogg"
    太一 "「はっ？」"
    call gl(1,"TCYM0000|TCYM0000")
    call gp(1,t=center)
    call vsp(1,1)
    with dissolve
    voice "vfccb0007mki009"
    美希 "「あ、よかった。気がつきましたか？」"
    太一 "「う、うー。俺ってばどれくらい気絶してた？」"
    voice "vfccb0007mki010"
    美希 "「一分たってないですよ」"
    太一 "「あー、ついに美希に負けたかー！」"
    "膝を打った。"
    call gl(1,"TCYM0003|TCYM0003")
    call vsp(1,1)
    with dissolve
    voice "vfccb0007mki011"
    美希 "「たは」"
    call gl(1,"TCYM0000|TCYM0000")
    call vsp(1,1)
    with dissolve
    voice "vfccb0007mki012"
    美希 "「でもすごく油断してらしたじゃないですか」"
    太一 "「いやー、あれは俺にとって他に選択肢がないからなー」"
    太一 "「……たぶん命がかかっていても同じだった」"
    call gl(1,"TCYM0001|TCYM0000")
    call vsp(1,1)
    with dissolve
    voice "vfccb0007mki013"
    美希 "「パンツに命を！？」"
    太一 "「チッチッチ」"
    "指を振ってみせる。"
    太一 "「ライブで見る素人娘がリアルに着用しているパンツ、だよ、君」"
    call gl(1,"TCYM0000|TCYM0000")
    call vsp(1,1)
    with dissolve
    voice "vfccb0007mki014"
    美希 "「違うんだ……」"
    太一 "「違うとも。このように―――」"
    "がっし"
    "愛弟子の短いスカートのはしをつまんだ愛指が。"
    "チョキで、しっかと挟まれているっ！"
    太一 "「はっ、防がれた！？」"
    call gl(1,"TCYM0005|TCYM0003")
    call vsp(1,1)
    with dissolve
    voice "vfccb0007mki015"
    美希 "「ふふふ」"
    "ショック。"
    太一 "「うーん、免許皆伝」"
    "横たわって膝を抱え、エビチリみたいに丸くなった。"
    太一 "「で、俺はもう引退しゆ」"
    call gl(1,"TCYM0002|TCYM0002")
    call vsp(1,1)
    with dissolve
    voice "vfccb0007mki016"
    美希 "「しゆとか言うし……」"
    "ゆさゆさと揺すられる。"
    voice "vfccb0007mki017"
    美希 "「ししょー、元気出してくださいよ」"
    太一 "「いい。引きこもる」"
    call gl(1,"TCYM0000|TCYM0000")
    call vsp(1,1)
    with dissolve
    voice "vfccb0007mki018"
    美希 "「またはじまったよこの人は」"
    voice "vfccb0007mki019"
    美希 "「……」"
    call gl(1,"TCYM0002|TCYM0002")
    call vsp(1,1)
    with dissolve
    voice "vfccb0007mki020"
    美希 "「全然……なのにな」"
    太一 "「ウイ？」"
    "フランス人のように問い返す。"
    voice "vfccb0007mki021"
    美希 "「みんなに普通なのに」"
    "声が震えた。にわかに。"
    太一 "「ミキミキ？」"
    voice "vfccb0007mki022"
    美希 "「ほら、こんなに手が震えてます」"
    "広げた両手が、汗ばんで、かじかむように。"
    "まるで怯えているかの如く。"
    太一 "「……どうして？」"
    call gl(1,"TCYM0001|TCYM0000")
    call vsp(1,1)
    with dissolve
    voice "vfccb0007mki023"
    美希 "「それはもう、せんぱいのプレッシャーみたいっぽいやつに当てられて、小心者の美希はビビリまくりなわけですよ」"
    太一 "「……」"
    call gl(1,"TCYM0000|TCYM0000")
    call vsp(1,1)
    with dissolve
    voice "vfccb0007mki024"
    美希 "「だから、元気出してください」"
    太一 "「んー」"
    "励ましてくれているだろうか。"
    "様子が変なのが気になるけど。"
    "うーむ、ポワワとしてしまうではないか。"
    太一 "「よし、免許皆伝をやろうではないか」"
    "拳を打つ。"
    voice "vfccb0007mki025"
    美希 "「え？」"
    太一 "「手帳を出しなさい」"
    call gl(1,"TCYM0001|TCYM0000")
    call vsp(1,1)
    with dissolve
    voice "vfcca0008mki012"
    美希 "「……あーあー……アレですか」"
    call gl(1,"TCYM0002|TCYM0002")
    call vsp(1,1)
    with dissolve
    voice "vfcca0008mki013"
    美希 "「なんか久々ですねえー」"
    "なんとも切なそうな顔をする。"
    "というか（というか？）泣きそう（泣きそう？）ではないか。"
    "多重に思ってしまったぞ。"
    "美希はメイトブックを取り出す。"
    "当校では身分証明書をかねるこの手帳を、『都会』の駅裏にある人気ＮＯ１高級浴場『メイトブック』にちなんでそう呼ぶ。"
    "ちなんでねぇよ、と自らに突っ込む。"
    "本当は偶然です。"
    voice "vfccb0007mki026"
    美希 "「……すんっ」"
    太一 "「どうしたん？」"
    "泣いている。"
    "というか（というか？）泣いてる（泣いてる？）。"
    "多重に思ってしまったぞ。"
    太一 "「……やっぱり、けっこうショックだったのかな？」"
    call gl(1,"TCYM0000|TCYM0000")
    call vsp(1,1)
    with dissolve
    voice "vfccb0007mki027"
    美希 "「え？」"
    太一 "「こんなことになって、世界が」"
    voice "vfccb0007mki028"
    美希 "「ああ……」"
    "微妙なためがあった。"
    call gl(1,"TCYM0001|TCYM0000")
    call vsp(1,1)
    with dissolve
    voice "vfccb0007mki029"
    美希 "「そうですね、そうかも」"
    太一 "「だろうな」"
    太一 "「俺だってびっくりだ。こんなの」"
    call gl(1,"TCYM0000|TCYM0000")
    call vsp(1,1)
    with dissolve
    voice "vfccb0007mki030"
    美希 "「せんぱいも？」"
    太一 "「ああ」"
    太一 "「もう１３歳とか１５歳の新じゃがならぬ新処女と出会う機会はなくなったわけだよなぁ」"
    call gl(1,"TCYM0001|TCYM0000")
    call vsp(1,1)
    with dissolve
    voice "vfccb0007mki031"
    美希 "「そっちかい」"
    太一 "「そら」"
    "手帳を取り上げる。"
    太一 "「美希は手帳だいぶ使いこんでるなあ。ぼろぼろだ」"
    call gl(1,"TCYM0000|TCYM0000")
    call vsp(1,1)
    with dissolve
    voice "vfcca0008mki021"
    美希 "「ぼろぼろ」"
    "無意味に繰り返すことで肯定する美希。"
    "ページを繰ると、メモ欄にはすでに俺のサインがでかでかと書かれていた。"
    "何ページにも渡っている。"
    "俺様サイン練習帳といった有様になっている。"
    "白紙を見つけ、そこに新たなサインを書き込む。"
    "いつ頃からかはじまった、俺たちのお遊びだ。"
    "他愛ないことだ。"
    "手帳を返す。"
    "受け取って、美希は胸元に抱える。"
    "ぎゅっと。"
    "失われた日常を、かき抱くように。"
    "ちょっとあふれた涙を、ぬぐってやりもする。"
    "わ、俺って紳士。"
    call gl(1,"TCYM0002|TCYM0002")
    call vsp(1,1)
    with dissolve
    voice "vfccb0007mki032"
    美希 "「ども……」"
    太一 "「なに」"
    "廊下を見渡す。"
    太一 "「しかし、掃除とはね」"
    call gl(1,"TCYM0000|TCYM0000")
    call vsp(1,1)
    with dissolve
    voice "vfccb0007mki033"
    美希 "「体動かしていた方が落ち着くかなって」"
    menu:
        太一 "「ふーん」"
        "掃除を手伝う":
            $B=1
        "スカートめくる":
            $B=2
    return
    #