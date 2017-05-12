label cca0001:
    scene expression Solid("000000")
    play bgm "bgm/bgm015.ogg"
    call gl(0,"bgcc0000c")
    call vsp(0,1)
    with Dissolve(500.0/1000.0)
    pause (500.0/1000.0)
    pause (500.0/1000.0)
    "最古の記憶は。"
    "日付さえおぼろげな、遠い霞のなか。"
    "貴族的な気品を抱く、豪華な私室。"
    "そこには天蓋つきの寝台も欧羅巴製の椅子もあった。"
    "けど床に座るのが一番好きだった。"
    "こんな日は特に。"
    "窓から見える黒の帳は星月夜。"
    "枠に切り取られた散在する瞬きに目を奪われる。"
    "外界と室内を隔てる窓ガラスに、己の姿が映る。"
    "深窓の令嬢―――"
    "洋風のドレスに身を包む、楚々とした少女。"
    #textoff
    with Dissolve(500.0/1000.0)
    call gl(0,"bgcc0000d")
    call vsp(0,1)
    with Pixellate(600.0/1000.0,8)
    #texton
    with Dissolve(500.0/1000.0)
    "きみはいったい、だれですか？"
    stop bgm
    pause (500.0/1000.0)
    pause (500.0/1000.0)
    voice "vfcca0001you000"
    少女 "「……太一」"
    pause (500.0/1000.0)
    #textoff
    with Dissolve(500.0/1000.0)
    pause (1000.0/1000.0)
    return
    #