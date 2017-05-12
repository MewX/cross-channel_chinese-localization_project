label ccc4002:
    call gl(0,"bgcc0000d")
    call vsp(1,0)
    call vsp(0,0)
    with Dissolve(500.0/1000.0)
    pause (500.0/1000.0)
    call gl(0,"bgcc0003")
    call vsp(0,1)
    call vsp(1,0)
    with Dissolve(500.0/1000.0)
    play bgm "bgm/bgm018.ogg"
    "目を覚ます。"
    "陽光が窓を貫いていた。"
    "熟睡していたらしい。夢一つ見なかった。"
    "時間は……７時。"
    "学校に行く必要などない。"
    "けど、体は動いた。"
    call gl(0,"bgcc0004")
    call vsp(0,1)
    with wipeleft
    "朝食の用意はされていない。"
    "当然か。"
    "美人でキャリアな睦美おばさんは料理もうまいが、もういない。"
    "引き取ってくれたこと。"
    "曜子ちゃんとのことを、穏便に取りはからってくれたこと……。"
    "感謝はいくらでもできた。"
    "孝行する前に、消失してしまった。"
    "この家にまともな食い物はない。"
    "水だけ飲んだ。"
    call gl(0,"bgcc0005")
    call vsp(0,1)
    with wipeleft
    "この道で、よく遊紗ちゃんと出会った。"
    "よくなついていた。"
    "こそばゆい、存在だった。"
    "今の俺ができるまで、俺もいろいろ苦労している。"
    "遊紗ちゃんの存在は、よく俺を癒してくれた。"
    "そんな彼女ももういない。"
    call gl(1,"TCSH0000|tcsh")
    call gp(1,t=center)#x=190
    call vsp(1,1)
    with dissolve
    voice "vmCCC0025sku000"
    桜庭 "「よう」"
    stop bgm
    "桜庭だった。"
    太一 "「よう」"
    play bgm "bgm/bgm010.ogg"
    voice "vmCCC0025sku001"
    桜庭 "「腹が減った」"
    太一 "「俺もだ」"
    call gl(1,"TCSH0003|tcsh")
    call vsp(1,1)
    with dissolve
    voice "vmCCC4002sku000"
    桜庭 "「おまえもか」"
    太一 "「そうだ」"
    call gl(1,"TCSH0002|tcsh")
    call vsp(1,1)
    with dissolve
    voice "vmCCC4002sku001"
    桜庭 "「切ないな」"
    太一 "「ああ、切ない」"
    太一 "「こんな時、俺は一般家庭に突入する」"
    "手近に民家に突っ込む。"
    "戻ってくる。"
    太一 "「大漁だったぞ」"
    "保存食がたくさんあった。"
    太一 "「見ろ、カンパンだ。しかもこんぺいとうが入ってるやつだぞ」"
    voice "vmCCC4002sku002"
    桜庭 "「……ぐす」"
    "桜庭は鼻水を垂らしていた。"
    太一 "「……避難していて正解だったようだ」"
    call gl(1,"TCSH0003|tcsh")
    call vsp(1,1)
    with dissolve
    voice "vmCCC4002sku003"
    桜庭 "「ティッシュを所望したいところだ」"
    太一 "「ない」"
    voice "vmCCC4002sku004"
    桜庭 "「……ん。なら仕方ないな」"
    "そのまま歩き出した。"
    "つらら状に垂れた鼻水が、軽妙に左右に踊る。"
    太一 "「仕方ないで済ますな！」"
    "ハンカチを出す。"
    call gl(1,"TCSH0000|tcsh")
    call vsp(1,1)
    with dissolve
    voice "vmCCC4002sku005"
    桜庭 "「……すまん」"
    太一 "「返すなよ。絶対に返すなよ？　やるんだからな」"
    voice "vmCCC4002sku006"
    桜庭 "「借りが出来た」"
    太一 "「それは返せよ」"
    call gl(1,"TCSH0002|tcsh")
    call vsp(1,1)
    with dissolve
    voice "vmCCC4002sku007"
    桜庭 "「うむ」"
    stop bgm
    return
    #