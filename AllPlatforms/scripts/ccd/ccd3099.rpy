label ccd3099:
    call gl(0,"bgcc0003")
    call vsp(0,1)
    call vsp(1,0)
    call vsp(2,0)
    with wipeleft
    "そして俺は、逃げ戻った。"
    "失敗は許されない。"
    "決して。"
    "慎重に行かねばならない。"
    太一 "「はぁっ……」"
    "瞬間的にふくれあがった、悪意。"
    "思春期の性欲のようなそれを、吐き出すのは容易ではない。"
    call gl(0,"bgcc0003c")
    call vsp(0,1)
    with ImageDissolve("sys/EFMSK_22_MSK.bmp",time=1)
    "俺は残る日数を自宅で過ごした。"
    "誰とも接触しなかった。"
    "危険はおかしたくなかったからだ。"
    "そして……日曜。"
    call gl(0,"bgcc0016")
    call vsp(0,1)
    with wipeleft
    "俺は静かに時を待った。"
    "その後の皆が、どう過ごしたのかはわからない。"
    "幾度、皆の個別はかき消されたのだろう？"
    "その重い事実は、俺を眩ませた。"
    call gl(0,"bgcc0000b")
    call vsp(0,1)
    with Dissolve(500.0/1000.0)
    "そして―――"
    call gl(0,"bgcc0000d")
    call vsp(0,1)
    with Dissolve(500.0/1000.0)
    pause (1500.0/1000.0)
    $B = 1
    if SB_FALSE<151:
        jump ccd3099L_INC
    jump ccd3099L_DODGE
label ccd3099L_INC:
    $SB_FALSE += 1
label ccd3099L_DODGE:
    if SB_FALSE>149:
        $B=2
    return
    #