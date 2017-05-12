label ccd0102:
    "さて。"
label K_ON1:
    if SB_KRI == 1:
        jump T_ON1
    if SB_TKO == 0:
        jump K_T_ON1
    if SB_MSA == 0:
        jump K_M_ON1
    if SB_SKU == 0:
        jump K_S_ON1
    $B = 1
    jump C_END
label K_T_ON1:
    if SB_MSA == 0:
        jump K_T_M_ON1
    if SB_SKU == 0:
        jump K_T_S_ON1
    menu:
        "一年教室":
            $B=1
        "二年教室":
            $B=2
    jump C_END
label K_M_ON1:
    if SB_SKU == 0:
        jump K_M_S_ON1
    menu:
        "一年教室":
            $B=1
        "屋上":
            $B=2
    if B == 2:
        $B=3
    jump C_END
label K_S_ON1:
    menu:
        "一年教室":
            $B=1
        "学食":
            $B=2
    if B == 2:
        $B=4
    jump C_END
label K_T_M_ON1:
    if SB_SKU == 0:
        jump K_T_M_S_ON1
    menu:
        "一年教室":
            $B=1
        "二年教室":
            $B=2
        "屋上":
            $B=3
    jump C_END
label K_T_S_ON1:
    menu:
        "一年教室":
            $B=1
        "二年教室":
            $B=2
        "学食":
            $B=3
    if B == 3:
        $B=4
    jump C_END
label K_M_S_ON1:
    menu:
        "一年教室":
            $B=1
        "屋上":
            $B=2
        "学食":
            $B=3
    if B == 3:
        $B=4
    if B == 2:
        $B=3
    jump C_END
label K_T_M_S_ON1:
    menu:
        "一年教室":
            $B=1
        "二年教室":
            $B=2
        "屋上":
            $B=3
        "学食":
            $B=4
    jump C_END
label T_ON1:
    if SB_TKO == 1:
        jump M_ON1
    if SB_MSA == 0:
        jump T_M_ON1
    if SB_SKU == 0:
        jump T_S_ON1
    $B = 2
    jump C_END
label T_M_ON1:
    if SB_SKU == 0:
        jump T_M_S_ON1
    menu:
        "二年教室":
            $B=1
        "屋上":
            $B=2
    if B == 2:
        $B=3
    if B == 1:
        $B=2
    jump C_END
label T_S_ON1:
    menu:
        "二年教室":
            $B=1
        "学食":
            $B=2
    if B == 2:
        $B=4
    if B == 1:
        $B=2
    jump C_END
label T_M_S_ON1:
    menu:
        "二年教室":
            $B=1
        "屋上":
            $B=2
        "学食":
            $B=3
    if B == 3:
        $B=4
    if B == 2:
        $B=3
    if B == 1:
        $B=2
    jump C_END
label M_ON1:
    if SB_MSA == 1:
        jump S_ON1
    if SB_SKU == 0:
        jump M_S_ON1
    $B = 3
    jump C_END
label M_S_ON1:
    menu:
        "屋上":
            $B=1
        "学食":
            $B=2
    if B == 2:
        $B=4
    if B == 1:
        $B=3
    jump C_END
label S_ON1:
    $B = 4
    jump C_END
label C_END:
    return
    #