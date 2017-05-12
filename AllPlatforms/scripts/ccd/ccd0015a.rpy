label ccd0015a:
    太一 "「てやー！」"
    "拳を振り上げて接近した。"
    voice "vfCCD0001kri021"
    霧 "「っ！」"
    stop bgm
    play se "SE094"
    with vpunch
    "どきゅっ"
    太一 "「げ……」"
    "矢が心臓に刺さった。"
    "美しく貫いた。"
    太一 "「サックリと……また……」"
    "俺は死んだ。"
    call gl(0,"bgcc0000d")
    call vsp(0,1)
    with Dissolve(500.0/1000.0)
    "……………………。"
    "…………。"
    "……。"
    #textoff
    pause (3000.0/1000.0)
    return
    #