label ccb0009:
    太一 "「さて」"
    "ふぁさぁっと前髪を払う。"
    太一 "「邪魔したな」"
    call gl(1,"TCYM0003|TCYM0003")
    call vsp(1,1)
    with dissolve
    voice "vfccb0009mki000"
    美希 "「おつとめご苦労様です」"
    太一 "「そうだ、美希」"
    "立ち止まる。"
    "大切なことを伝え忘れていた。"
    call gl(1,"TCYM0000|TCYM0000")
    call vsp(1,1)
    with dissolve
    voice "vfccb0009mki001"
    美希 "「はい」"
    太一 "「そろそろ部活、活動再開するってさ」"
    voice "vfccb0009mki002"
    美希 "「部活ですか？」"
    太一 "「どうしても心がきつくなったら、顔を出してみるといい」"
    太一 "「そういうための、部活だろうから」"
    "ゆっくりと、美希の顔に理解がさした。"
    call gl(1,"TCYM0001|TCYM0000")
    call vsp(1,1)
    with dissolve
    voice "vfccb0009mki003"
    美希 "「……はい」"
    hide pic1
    with dissolve
    stop bgm
    menu:
        "喜びだけでないなにかが、そこには混入していた。"
        "教室に行く":
            $B=1
        "屋上に行く":
            $B=2
    return
    #