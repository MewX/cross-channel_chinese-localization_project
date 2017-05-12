label ccd0013:
    call gl(0,"bgcc0011")
    call vsp(0,1)
    call vsp(1,0)
    with wipeleft
    "さてと。"
    menu:
        "教室":
            $B=1
        "屋上":
            $B=2
        "廊下":
            $B=3
    return
    #