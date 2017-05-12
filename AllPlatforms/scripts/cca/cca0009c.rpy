label cca0009c:
    "旅立つ。"
    太一 "「そうだ、美希」"
    "立ち止まる。"
    "大切なことを伝え忘れていた。"
    voice "vfcca0010mki000"
    美希 "「はい」"
    stop bgm
    太一 "「そろそろ部活、活動再開するってさ」"
    pause (500.0/1000.0)
    call gl(0,"bgcc0000")
    call vsp(0,0)
    call vsp(1,0)
    with wipeleft
    pause (1000.0/1000.0)
    stop se
    #dwavestop 3
    return
    #