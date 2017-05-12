label ccc4006:
    call gl(0,"bgcc0007")
    call vsp(0,1)
    with wipeleft
    "と、一人で屋上に来たのはいいが。"
    "どうしようかな。"
    "あ、先輩だ。"
    voice "vfCCC4006msa000"
    見里 "「ぱららららららっ」"
    play bgm "bgm/bgm006.ogg"
    "サバゲーの練習してる。"
    "ＳＭＧを腰だめに構えた先輩は素敵だ。"
    "ちなみにこの銃器は、毎年の合宿で使われていたものだ。"
    "無線、合宿ときたらあとはサバゲー。"
    "ちゃんとＢＢ弾タイプの電動ガンも揃っている。"
    太一 "「はろー」"
    call gl(1,"TCMM0004|TCMM000x")
    call gp(1,t=center)#x=225
    call vsp(1,1)
    with dissolve
    voice "vfCCC4006msa001"
    見里 "「えっ？」"
    "こっちを向いた。"
    "ＳＭＧが水を噴出した。"
    太一 "「わっぷ！」"
    "目と目の間を直撃。"
    "電動水鉄砲だから勢いは強い。"
    voice "vfCCC4006msa002"
    見里 "「あっ、ごめんなさい……」"
    太一 "「いえ、夏のサバゲーはウォーターガンに限りますよね」"
    call gl(1,"TCMM0000|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC4006msa003"
    見里 "「そういえば新製品が出たんですよ、滅亡前に」"
    太一 "「寒すぎる……」"
    太一 "「あのー、そういえば気になっていたんですけど」"
    call gl(1,"TCMM0002|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC4006msa004"
    見里 "「はい？」"
    太一 "「アンテナ、手つけなくていいんですか？」"
    call gl(1,"TCMM0005|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC4006msa005"
    見里 "「…………そ、そうでした」"
    太一 "「美希のペースにほだされましたね」"
    voice "vfCCC4006msa006"
    見里 "「襲ってきたからつい応戦してしまいました……」"
    "と―――"
    call gl(2,"TCYM0001|TCYM0000")
    call vsp(1,0)
    call vsp(2,1)
    call gp(2,t=center)#x=180
    with Dissolve(500.0/1000.0)
    voice "vfCCC4006mki000"
    美希 "「ＧＩダーイ！」"
    "吶喊したきた。"
    太一 "「ＧＩじゃねーっての！」"
    "応戦する俺。そして先輩。"
    extend "水鉄砲が火を噴いた。"
    "※水鉄砲が火を噴いた＝気にするな"
    太一 "「ベトナムコンプレックスどもめが！」"
    voice "vfCCC4006mki001"
    美希 "「ＧＩダーイっ！！」"
    太一 "「俺をＧＩと呼ぶなぁー！」"
    call gl(2,"TCSK0001|TCSK000x")
    call gp(1,t=left)#x=40
    call gp(2,t=right)#x=340
    call vsp(1,1)
    call vsp(2,1)
    with Dissolve(500.0/1000.0)
    voice "vfCCC4006kri000"
    霧 "「死ねー！」"
    太一 "「おわっ」"
    "くそ、なんか半分本気だな、こっちは。"
    太一 "「ベトナムコンシャスの猿め……死ぬのはおまえだ！」"
    "俺はベトコンの正しい意味を知らなかった！"
    voice "vfCCC4006kri001"
    霧 "「くっ、こしゃく……」"
    太一 "「お前がな！」"
    "水鉄砲の火線が交差する。"
    "※水鉄砲の火線が交差する＝気にするな"
    call gl(3,"TCMM0004|TCMM000x")
    call vsp(1,0)
    call vsp(2,0)
    call vsp(3,1)
    call gp(3,t=center)#x=225
    with Dissolve(500.0/1000.0)
    voice "vfCCC4006msa007"
    見里 "「停学、停学っ！」"
    call gl(1,"TCYM0003|TCYM0003")
    call gp(1,t=center)#x=180
    call vsp(3,0)
    call vsp(1,1)
    with Dissolve(500.0/1000.0)
    voice "vfCCC4006mki002"
    美希 "「うりゃー！」"
    "また部活が……。"
    "と思いつつも、目の前の敵を無視することはできない。"
    太一 "「くっ、弾（水）切れ！？」"
    "腰に装着したタンクから、弾薬をリロードする。"
    "きっちり十秒かかる。"
    call gl(2,"TCSK0001|TCSK000x")
    call gp(2,t=center)#x=220
    call vsp(2,1)
    call vsp(1,0)
    with Dissolve(500.0/1000.0)
    voice "vfCCC4006kri002"
    霧 "「……フッ」"
    "霧に邪悪に微笑む。"
    "正確な射撃を加えてきた。"
    "身を低くして走る。"
    "そう簡単には当たらない。"
    "だが十秒は長い。"
    "霧が確実に当てるため、接近してきていた。"
    "ちょうどリロード完了。"
    "撃つ。"
    hide pic2
    with dissolve
    voice "vfCCC4006kri003"
    霧 "「……あっ！？」"
    "霧が転倒した。いいぞ！"
    "もう一撃。"
    "これも外れたが、霧はさらに体勢を崩した。"
    "つんのめって、ケンケンをしながらフェンスにしがみつく。"
    "フェンスが傾いだ。"
    extend "全体重をかけていた霧は、向こう側に折れ曲がるフェンスとともに、横倒しになる。"
    stop bgm
    太一 "「霧！」"
    "駆け出す。"
    "間に合うか。"
    "無理だ、この距離では。"
    "それがわかってしまった。"
    voice "vfCCC4006kri004"
    霧 "「あ……え……？」"
    "カラカラ、と制服の金具が音を立てる。"
    "フェンスの網目と擦れて、そんな音がした。"
    "滑り落ちる最中の音。"
    "俺の目の前で、霧が、"
    "美希が、"
    太一 "「っ！？」"
    "迅速と言えた。"
    "美希は手を伸ばす。霧の手首を掴んだ。"
    "間一髪、霧は落下を免れた。"
    voice "vfCCC4006mki003"
    美希 "「……霧」"
    "フェンスを掴んだ腕は、針金で引き裂かれて出血していた。"
    "当の霧はまだぽかんとしていた。"
    "……………………。"
    "霧を引き上げる。"
    "しばらく、呆然と自失していた。"
    call gl(1,"TCYM0001|TCYM0000")
    call gp(1,t=center)#x=180
    call vsp(1,1)
    call vsp(2,0)
    with Dissolve(500.0/1000.0)
    voice "vfCCC4006mki004"
    美希 "「いったたたたぁ～」"
    "出血がひどい。"
    太一 "「これは保健室に行かないと……先輩、そっちの方、お願いします」"
    call gl(2,"TCMM0000|TCMM000x")
    call gp(2,t=center)#x=225
    call vsp(2,1)
    call vsp(1,0)
    with Dissolve(500.0/1000.0)
    voice "vfCCC4006msa008"
    見里 "「はい」"
    call gl(1,"TCYM0000|TCYM0000")
    call gp(1,t=left)#x=0
    call gp(2,t=right)#x=340
    call vsp(2,1)
    call vsp(1,1)
    with Dissolve(500.0/1000.0)
    voice "vfCCC4006mki005"
    美希 "「あ、保健室には先輩と行きますっ」"
    call gl(2,"TCMM0005|TCMM000x")
    call vsp(2,1)
    with dissolve
    voice "vfCCC4006msa009"
    見里 "「え……だめです、私そういうの……ぺけくんお願いしますっ」"
    太一 "「へーい」"
    call gl(1,"TCYM0011|TCYM0011")
    call vsp(1,1)
    with dissolve
    voice "vfCCC4006mki006"
    美希 "「あっ、わたし自分で行けるかも」"
    太一 "「手当ては無理でしょ」"
    call gl(1,"TCYM0002|TCYM0002")
    call vsp(1,1)
    with dissolve
    voice "vfCCC4006mki007"
    美希 "「あーう」"
    "俺も血は苦手だ。"
    太一 "「ま、まぁ、なんとかするって」"
    call gl(1,"TCYM0001|TCYM0000")
    call vsp(1,1)
    with dissolve
    美希 "「…………」"
    "美しい血。"
    "友達を助けた。"
    "心は疼かなかった。"
    play bgm "bgm/bgm022.ogg"
    "これなら平気かも知れない。"
    "俺たちが校舎内に入る時、霧がぺたりとへたり込むのが見えた。"
    "恐怖は遅れてやってくる。いつだって。"
    return
    #