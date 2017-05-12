label ccd0101:
    call gl(0,"bgcc0016")
    call vsp(0,1)
    call vsp(1,0)
    with Dissolve(500.0/1000.0)
    #modewin
    play bgm "bgm/bgm001.ogg"
    "そして、俺は目覚めた。"
    "念のため、茂みの奥を確認する。"
    "よし。"
    "位相のずれ。とでも言うのか。"
    "俺の目だけが観測できるそれは、向こう側への帰還の道のり。"
    "観測する者だけに、真実となる。"
    "そこをくぐれば、帰れる。"
    "人の満ちた世界に。"
    "けれど。そう。"
    "俺は―――"
    stop bgm
    call gl(0,"bgcc0002")
    call vsp(0,1)
    with wipeleft
    "曜子ちゃんの姿はない。"
    "ただ弁当だけが机に置いてあった。"
    "学校に向かう。"
    play bgm "bgm/bgm016.ogg"
    call gl(0,"bgcc0005")
    call vsp(0,1)
    with wipeleft
    "無人の世界を歩く。"
    "人だけでなく、生物そのものの気配がない。"
    "満ちている感じがしない。"
    "蝉も鳴かない。"
    "不自然な、空間。"
    "交差した世界の中核で、渦巻く矛盾。"
    "わずか八人の小世界。"
    太一 "「……」"
    "七香も、出てこない。"
    七香 "「……………………」"
    stop bgm
    if SB_MKI == 1:
        jump N_CHS001
    if SB_KRI == 0:
        jump N_CHS001
    if SB_MSA != 1:
        jump Y_CHS001
    if SB_TKO != 1:
        jump Y_CHS001
    if SB_SKU != 1:
        jump Y_CHS001
    jump N_CHS002
    
label Y_CHS001:
    menu:
        "学校に行く":
            $B=1
        "田崎商店に行く":
            $B=2
    return

label N_CHS001:
    $B = 1
return
label N_CHS002:
    $B = 2
return