label cca0014a:
    太一 "「おい、反転属性つき勝ち気娘」"
    call gl(1,"TCKT0001|TCKT000x")
    call vsp(1,1)
    with dissolve
    voice "vfcca0014afyu000"
    冬子 "「はぁ……？」"
    太一 "「これをやる」"
    "朝のサンドイッチを差し出す。"
    call gl(1,"TCKT0000|TCKT000x")
    call vsp(1,1)
    with dissolve
    "ぽかんと、見つめる冬子。"
    voice "vfcca0014afyu001"
    冬子 "「なに、コレ」"
    太一 "「あんまん」"
    call gl(1,"TCKT0003|TCKT000x")
    call vsp(1,1)
    with dissolve
    voice "vfcca0014afyu002"
    冬子 "「んなわけないでしょ！！　サンドイッチでしょ！」"
    太一 "「知ってるじゃないか」"
    太一 "「ほれ」"
    "ずい"
    call gl(1,"TCKT0002|TCKT000x")
    call vsp(1,1)
    with dissolve
    voice "vfcca0014afyu003"
    冬子 "「……やめて」"
    play se "se048"
    "手を払われる。"
    "サンドイッチが落ちた。"
    "拾う。"
    太一 "「ちゃんと食べてるのか？」"
    call gl(1,"TCKT0002|TCKT000x")
    call vsp(1,1)
    with dissolve
    voice "vfcca0014afyu004"
    冬子 "「あんたに、関係ない」"
    "そっぽを向く。"
    太一 "「自分しか、自分の心配をしてくれる人間がいないのは、つらいだろ？」"
    voice "vfcca0014afyu005"
    冬子 "「何言ってるのかわからない」"
    太一 "「人に心配されたい」"
    太一 "「満たされたい」"
    voice "vfcca0014afyu006"
    冬子 "「……」"
    太一 "「俺、ちょっとは心配なんだけどな」"
    call gl(1,"TCKT0000|TCKT000x")
    call vsp(1,1)
    with dissolve
    "きっと俺を睨む。"
    call gl(1,"TCKT0001|TCKT000x")
    call vsp(1,1)
    with dissolve
    voice "vfcca0014afyu007"
    冬子 "「よく、言う」"
    call gl(1,"TCKT0003|TCKT000x")
    call vsp(1,1)
    with dissolve
    voice "vfcca0014afyu008"
    冬子 "「心配してるなら、どうして、どうしてっ！」"
    "いきり立つ。"
    太一 "「……桐原」"
    voice "vfcca0014afyu009"
    冬子 "「なによ！」"
    太一 "「顔色悪いな。生理か？」"
    play se "se005"
    "びたーん！"
    with vpunch
    voice "vfcca0014afyu010"
    冬子 "「馬鹿じゃないの！」"
    hide pic1
    with dissolve
    stop bgm
    "呪詛を吐いて、出て行く。"
    太一 "「あ、サンドイッチ……」"
    "ため息。"
    太一 "「……あんまいい死に方できないぞ」"
    "仕方ないので、包みをといて自分でかぶりついた。"
    return
    #