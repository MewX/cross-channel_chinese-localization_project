label ccb1014b:
    太一 "「わかりましたよ、先輩……じゃあですね、かわりに」"
    call gl(1,"TCMM0000c|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfcca0025bmsa000"
    見里 "「なぁに？」"
    太一 "「エッチなことって、したことあります？」"
    call gl(1,"TCMM0004c|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfcca0025bmsa001"
    見里 "「文脈違うじゃないですか！」"
    太一 "「先輩っていいなって思ってたんです」"
    太一 "「あの……桜舞う入学式の日、弟が死んで目的を見失った俺を救い出してくれた先輩の思い出の一言が」"
    call gl(1,"TCMM0000c|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfcca0025bmsa002"
    見里 "「だまされません、そんな最大瞬間風速的恋愛オーラにはだまされません！」"
    voice "vfcca0025bmsa003"
    見里 "「だいたい弟なんていないでしょ！」"
    太一 "「白球にかけた一夏、俺はアイツから逃げるために、野球をやめたつもりでした」"
    voice "vfcca0025bmsa004"
    見里 "「違う違う、野球は違う」"
    call gl(1,"TCMM0001c|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfcca0025bmsa005"
    見里 "「といいますか、すごくＨなこと考えてませんか？」"
    太一 "「いやー」"
    太一 "「食欲が満たされたから、あとは性欲かなって」"
    hide pic1
    with dissolve
    voice "vfcca0025bmsa006"
    見里 "「らりほー！」"
    "先輩は窓から叫んだ。"
    call gl(1,"TCMM0000c|TCMM000x")
    call gp(1,t=center)
    call vsp(1,1)
    with dissolve
    voice "vfcca0025bmsa007"
    見里 "「それ以上近寄ったら……舌を噛んで死にます」"
    太一 "「そ、そんなにイヤなのですかー！？」"
    "泣きそう。"
    "やっぱ人間容姿だ。"
    "白髪の醜悪ボーイには、人並みの恋愛など許されないのだ。"
    "でも土下座したらＨさせてくれないかな先輩。"
    stop bgm
    menu:
        "もう一押しの気がする。"
        "迫る":
            $B=1
        "ボケる":
            $B=2
    return
    #