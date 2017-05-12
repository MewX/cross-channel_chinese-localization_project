label ccc0020:
    call gl(0,"bgcc0009")
    call vsp(0,1)
    call vsp(1,0)
    with wipeleft
    "昼飯はやっぱりここで食べたいところだ。"
    play bgm "bgm/bgm018.ogg"
    call gl(1,"TCSH0000|tcsh")
    call gp(1,t=center)#x=190
    call vsp(1,1)
    with dissolve
    voice "vmCCC0020sku000"
    桜庭 "「よう、太一」"
    "カレーパン桜庭だった。"
    "超辛いここのカレーパンが大好きだ。"
    太一 "「人類滅亡してもカレーパン」"
    call gl(1,"TCSH0003|tcsh")
    call vsp(1,1)
    with dissolve
    voice "vmCCC0020sku001"
    桜庭 "「……やらんぞ」"
    太一 "「いらんわい」"
    call gl(1,"TCSH0002|tcsh")
    call vsp(1,1)
    with dissolve
    voice "vmCCC0020sku002"
    桜庭 "「これを食い尽くしたら、もう食い納めだしな」"
    "表情が曇った。"
    "その背後に、パンの詰まったケースがタワー状に積んである。"
    太一 "「……これいつ搬入されたやつだ？」"
    call gl(1,"TCSH0000|tcsh")
    call vsp(1,1)
    with dissolve
    voice "vmCCC0020sku003"
    桜庭 "「昨日じゃないか？」"
    "昨日。"
    "確かに半日でもパンの販売はある。"
    "基本的に休日以外は食堂として機能しているのだ。"
    "始業式であってもパンは搬入されている。"
    "そう。"
    "つまり昨日まで、ちゃんと世界は維持されていたわけだ。"
    太一 "「にしても数が少ない」"
    "ケースの数は、いつもの十分の一もない。"
    voice "vmCCC0020sku004"
    桜庭 "「始業式で半ドンだからだろ」"
    太一 "「にしても……少ない」"
    call gl(1,"TCSH0002|tcsh")
    call vsp(1,1)
    with dissolve
    voice "vmCCC0020sku005"
    桜庭 "「それにオレは、人類が滅亡したとは思っていない」"
    太一 "「なんだって？」"
    voice "vmCCC0020sku006"
    桜庭 "「恐らく、市民全員で隠れんぼをしているんじゃないか、というのがオレの予測だ」"
    太一 "「妄想だそれは」"
    太一 "「予測なんて言葉は使うな。おまえが考えて結論を出したみたいじゃないか」"
    call gl(1,"TCSH0000|tcsh")
    call vsp(1,1)
    with dissolve
    voice "vmCCC0020sku007"
    桜庭 "「フッ……手厳しいヤツめ」"
    太一 "「満足そうに微笑むな」"
    call gl(1,"TCSH0002|tcsh")
    call vsp(1,1)
    with dissolve
    voice "vmCCC0020sku008"
    桜庭 "「だが気にすることはない」"
    voice "vmCCC0020sku009"
    桜庭 "「時間が経てば、みんな戻ってくるはずだ。オレの計算によるとな」"
    太一 "「…………オレも脳天気だが、おまえは細胞レベルで脳天気だな」"
    voice "vmCCC0020sku010"
    桜庭 "「フ」"
    "どうして傷ついた少年少女たちの中にコイツがいるんだろう。"
    "本気で悩んでしまった。"
    "桜庭がそんな俺にカレーパンを差し出す。"
    call gl(1,"TCSH0000|tcsh")
    call vsp(1,1)
    with dissolve
    voice "vmCCC0020sku011"
    桜庭 "「食え」"
    太一 "「いらん！」"
    play se "SE003"
    with vpunch
    hide pic1
    with dissolve
    play se "SE038"
    "撃墜。"
    stop bgm
    return
    #