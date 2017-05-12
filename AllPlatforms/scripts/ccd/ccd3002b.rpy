label ccd3002b:
    play bgm "bgm/bgm016.ogg"
    太一 "「霧」"
    "全身が強ばる。"
    "ゆっくりと振り向く。"
    "振り返れば、厳めしい面差し"
    call gl(0,"evcc0027a")
    call vsp(0,1)
    with ImageDissolve("sys/EFMSK_22_MSK.bmp",time=1)
    太一 "「おはよう」"
    voice "vfCCC3102bkri000"
    霧 "「……何の用です？」"
    "低い声。"
    太一 "「美希君はいないのかな？」"
    voice "vfCCC0014kri000"
    霧 "「……いません」"
    太一 "「そうか」"
    "知っている。"
    太一 "「商店街の方でうろうろしてた。情緒不安定な感じだったよ」"
    voice "vfCCC3102bkri001"
    霧 "「美希が……？」"
    太一 "「行ってあげたら？」"
    call gl(0,"bgcc0006")
    call vsp(0,1)
    with wipeleft
    "霧は応じることもなく、教室を飛び出した。"
    太一 "「おい、これ」"
    call gl(1,"TCSK0000|TCSK000x")
    call gp(1,t=center)#x=220
    call vsp(1,1)
    with dissolve
    voice "vfCCC3102bkri002"
    霧 "「……な？」"
    太一 "「昼飯。美希にあげる約束してたやつ」"
    "嘘。"
    "でもこう言わないと霧は受け取らない。"
    call gl(1,"TCSK0002|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC3102bkri003"
    霧 "「……どうして、あなたが……」"
    太一 "「ほら、急げよ。泣いてたぞ」"
    hide pic1
    with dissolve
    "訝しげに俺を一瞥し、霧は走り去った。"
    "よし、これでいい。"
    "大きく息をついた。"
    call gl(0,"bgcc0008")
    call vsp(0,1)
    with wipeleft
    "霧とのこと、一日は時間を置かねばならないだろう。"
    "日曜、世界は巻き戻される。"
    "ご破算の日。"
    "今の世界は理想郷かも知れない。"
    "致命傷が、致命とならない世界。"
    "一週間で元通り。"
    "誰を傷つけても、誰と共依存しても。"
    "リセット。"
    "冬子と仲良くしたら次はみみ先輩と。"
    "霧と。"
    "美希と。"
    "気が向いたら曜子ちゃんと。"
    "桜庭と。"
    "……それはない。"
    "だけど。"
    "可能性がそこにあり、リセットから免れている場所がある。"
    "完璧なご都合主義ではない。"
    "だから俺は―――"
    play se "se001"
    play bgm "bgm/bgm004.ogg"
    call gl(0,"bgcc0005s")
    call vsp(0,1)
    with Pixellate(300.0*2/1000.0,5)
    "去年の初夏だった。"
    "新川豊と出会ったのは。"
    "蝉のうるさい夏だった。"
    call gl(1,"TCSY0001s|tcsy")
    call vsp(1,1)
    with dissolve
    voice "vmcca0011bshi033"
    "新川『ＯＫ、なんとかやっていけそうな気がしてきた』"
    太一 "「…………」"
    "悪かったのは誰か。"
    "運命や巡り合わせのせいには、できない。"
    "誰かが悪い。あるいは、誰もが悪い。"
    "それを認められれば、結論はそう多くない。"
    stop bgm
    stop se
    return
    #