label ccd0020a:
    call gl(0,"bgcc0007")
    call vsp(0,1)
    with ImageDissolve("sys/EFMSK_12_MSK.bmp",time=1)
    play bgm "bgm/bgm011.ogg"
    太一 "「どもー」"
    call gl(1,"TCMM0000|TCMM000x")
    call gp(1,t=center)#x=225
    call vsp(1,1)
    with dissolve
    voice "vfCCD0001msa037"
    見里 "「ああ、おはようございます」"
    太一 "「どうですか？」"
    call gl(1,"TCMM0003|TCMM000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCD0001msa038"
    見里 "「全然順調じゃありません」"
    太一 "「大変ですね」"
    "アンテナを見る。"
    "根本に鉄骨やら針金やら工具やら……おいおい、工具まで高所に置きっぱなしだよ。"
    太一 "「ふーん、これが噂のアンテナかぁ」"
    "などと脚立の上の危険物を床におろす。"
    call gl(1,"TCMM0021|TCMM0021")
    call vsp(1,1)
    with dissolve
    voice "vfCCD0001msa039"
    見里 "「……あのう？」"
    太一 "「あ、こうなってるのかー」"
    "アンテナの途中にひっかけられた工具類も全部床に。"
    voice "vfCCD0001msa040"
    見里 "「寝ぼけてます？」"
    太一 "「いえ、超冷静ですー」"
    太一 "「ではでは、またまた」"
    "先輩はぽかーんと俺を見送っていた。"
    "このタイミングを外せば、怪我はない……はず。"
    call gl(0,"bgcc0008")
    call vsp(0,1)
    call vsp(1,0)
    with wipeleft
    太一 "「あ」"
    stop bgm
    "……怪我させないと進展しないんだっけか？"
    太一 "「でもなあ」"
    "だからといって、事故を見逃すってのは……。"
    太一 "「はあ」"
    "結局、攻略をはやめる効果はないんだろうな。"
    return
    #