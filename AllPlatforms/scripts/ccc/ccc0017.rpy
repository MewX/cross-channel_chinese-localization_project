label ccc0017:
    call gl(1,"TCYM0021|TCYM0021")
    call vsp(1,1)
    with dissolve
    voice "vfCCC0017mki000"
    美希 "「……？」"
    太一 "「そーそー、食い物はちゃんとありますか？」"
    call gl(1,"TCYM0000|TCYM0000")
    call vsp(1,1)
    with dissolve
    voice "vfCCC0017mki001"
    美希 "「はい。全然平気です」"
    call gl(1,"TCYM0003|TCYM0003")
    call vsp(1,1)
    with dissolve
    voice "vfCCC0017mki002"
    美希 "「手料理といいますと、ちとアレなのですが」"
    "苦笑い。"
    太一 "「昼飯は缶詰だったりして」"
    call gl(1,"TCYM0011|TCYM0011")
    call vsp(1,1)
    with dissolve
    voice "vfCCC0017mki003"
    美希 "「まさに食パンと缶詰です」"
    太一 "「……貧乏くさい弁当だな」"
    call gl(1,"TCYM0003|TCYM0003")
    call vsp(1,1)
    with dissolve
    voice "vfCCC0017mki004"
    menu:
        美希 "「たはは」"
        "サンドイッチあげる":
            $B=1
        "あげない":
            $B=2
    return
    #