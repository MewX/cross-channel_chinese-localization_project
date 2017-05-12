label ccd0007:
    call gl(0,"bgcc0011")
    call vsp(0,1)
    call vsp(1,0)
    call vsp(2,0)
    call vsp(3,0)
    with wipeleft
    "学校についた。"
    "どうしよ……。"
    "とにかく徘徊してみよう。"
label SET_0001:
    menu:
        "とにかく徘徊してみよう。"
        "部室":
            $B = 1
        "一年教室":
            $B = 2
        "廊下":
            $B = 3
        "選択肢、次ページへ":
            $B = 4
    if B == 4:
        jump SET_0002
    jump SET_END
label SET_0002:
    menu:
        "とにかく徘徊してみよう。"
        "二年教室":
            $B = 4
        "屋上":
            $B = 5
        "選択肢、前ページへ":
            $B = 3
    if B == 3:
        jump SET_0001
label SET_END:
    return
    #