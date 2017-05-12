label ccb1008:
    call gl(0,"bgcc0008a")
    call vsp(0,1)
    call vsp(1,0)
    call vsp(2,0)
    with wipeleft
    play bgm "bgm/bgm007.ogg"
    voice "vmcca0018yki000"
    友貴 "「太一ー」"
    "廊下を歩いていると、呼び止められた。"
    太一 "「お、まだいたの？」"
    call gl(1,"TCST0000b|TCST0000")
    call gp(1,t=center)#x=190
    call vsp(1,1)
    with Dissolve(500.0/1000.0)
    voice "vmcca0018yki001"
    友貴 "「そっちこそ」"
    "友貴の顔が能面のようだった。"
    "微妙な距離を置いて、ふたり。"
    太一 "「部活だったんだよ」"
    太一 "「最近部活に出てる」"
    call gl(1,"TCST0004b|TCST0004")
    call vsp(1,1)
    with dissolve
    voice "vmcca0018yki002"
    友貴 "「……どうしてまた？」"
    太一 "「いや、目的があっていいじゃないか」"
    voice "vmcca0018yki003"
    友貴 "「部活って、例の与太話？」"
    "群青学院放送局の開局。"
    太一 "「与太じゃないよ、たぶん」"
    call gl(1,"TCST0005b|TCST0004")
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
    voice "vmcca0018yki006"
    友貴 "「……だけ？」"
    太一 "「そう」"
    call gl(1,"TCST0000b|TCST0000")
    call vsp(1,1)
    with dissolve
    voice "vmcca0018yki007"
    友貴 "「それ部活じゃない……」"
    太一 "「部活と思えば自慰だって部活だ」"
    call gl(1,"TCST0005b|TCST0004")
    call vsp(1,1)
    with dissolve
    voice "vmcca0018yki008"
    友貴 "「……最近、いろいろと動いてるのは知ってたけど、部活とはね」"
    "肩をすくめた。"
    太一 "「そっちこそ。今なにやってんだ？」"
    call gl(1,"TCST0004b|TCST0004")
    call vsp(1,1)
    with dissolve
    voice "vmcca0018yki009"
    友貴 "「部活」"
    太一 "「わはは」"
    太一 "「……え、意味わからん？」"
    call gl(1,"TCST0003b|TCST0000")
    call vsp(1,1)
    with dissolve
    voice "vmcca0018yki010"
    友貴 "「本物の部活」"
    call gl(1,"TCST0000b|TCST0000")
    call vsp(1,1)
    with dissolve
    voice "vmcca0018yki011"
    友貴 "「暇だったら参加してくれよな」"
    stop bgm
    太一 "「そりゃいいけど……」"
    call gl(1,"TCST0004b|TCST0004")
    call vsp(1,1)
    with dissolve
    voice "vmcca0018yki012"
    友貴 "「……裏切られるぞ」"
    "ぽつ、と言う。"
    太一 "「誰に？」"
    voice "vmcca0018yki013"
    友貴 "「部長に」"
    play bgm "bgm/bgm007.ogg"
    太一 "「なぜ？」"
    voice "vmcca0018yki014"
    友貴 "「だから、あまり親しくしない方がいい」"
    hide pic1
    with dissolve
    "背を向けて、友貴は立ち去る。"
    "様子が変だったな。"
    extend "どうしたんだろう？"
    stop bgm
    return
    #