label splashscreen:
    show expression "sys/CAUTION_0.png" with dissolve
    show expression "sys/CAUTION_1.png" with dissolve
    pause
    show expression "sys/CAUTION_2.png" with dissolve
    pause
    show expression "sys/CAUTION_3.png" with dissolve
    return
label start:
    python:
        #temp_flag定义区
        B = 0
        bgmplaying = 0
        roop = 0
        roopD = 0
        SB_FALSE = 0
        KIRIBAD = 0
        KIRI = 0
        MIKI = 0
        MISATO = 0
        YOKO = 0
        TOKO = 0
        SB_KRI = 0
        SB_MKI = 0
        SB_MSA = 0
        SB_YKO = 0
        SB_TKO = 0
        SB_SKU = 0
        E = 0
        R = 0
        KAISOU = 0
        CIA = 0
        CIB = 0
        CIC = 0
        CID = 0
        C = 0
        P = 0
        END = 0
        PMOVIE = 0
        SYS_MOVIE = 0
        WORK = 0
        firstgame = 0
        fullclear = 0
        pic = {}
    scene expression Solid("000")
    with dissolve
    $in_game = True
label gm_roop:
    if (roop == 0):
        jump lr0001
    if (roop == 1):
        jump lr0002
    if (TOKO != 1):
        jump lr0003
    if (MISATO != 1):
        jump lr0003
    if (KIRI != 1):
        jump lr0003
    if (MIKI != 1):
        jump lr0003
    jump lr0004
label lr0001:
    call cca
    $roop = 1
    jump gm_roop
label lr0002:
    call ccb
    $roop += 1
    jump gm_roop
label lr0003:
    call ccc
    $roop += 1
    jump gm_roop
label lr0004:
    call ccd
    $roop += 1
    jump gm_end
label gm_end:
    $persistent.fullclear = 1
    return
####################################################################################
#game logic begins here
####################################################################################
label cca:
    $save_name = "CROSS✝CHANNEL"
    call cca0001
    call cca0002
    call cca0003
    call cca0004
    if (B == 1):
        jump LA0005A
    if (B == 2):
        jump LA0005B
label LA0005A:
    call cca0005a
    jump LA0006
label LA0005B:
    call cca0005b
    jump LA0006
label LA0006:
    call cca0006
    call cca0007
    call cca0008
    if (B == 1):
        jump LA0009A
    if (B == 2):
        jump LA0009B
label LA0009A:
    call cca0009a
    jump LA0010
label LA0009B:
    call cca0009b
    jump LA0010
label LA0010:
    call cca0009c
    call cca0010
    if (B == 1):
        jump LA0011A
    if (B == 2):
        jump LA0011B
label LA0011A:
    call cca0011a
    jump LA0011C
label LA0011B:
    call cca0011b
    jump LA0011C
label LA0011C:
    call cca0011c
    jump LA0012
label LA0012:
    call cca0012
    call cca0013
    if (B == 1):
        jump LA0014A
    if (B == 2):
        jump LA0014B
label LA0014A:
    call cca0014a
    jump LA0015
label LA0014B:
    call cca0014b
    jump LA0015
label LA0015:
    call cca0015
    call cca0016
    if (B == 1):
        jump LA0017A
    if (B == 2):
        jump LA0017B
label LA0017A:
    call cca0017a
    jump LA0018
label LA0017B:
    call cca0017b
    jump LA0018
label LA0018:
    call cca0018
    call cca0019
    call cca0020
    call cca0021
    call cca0022
    call cca0023
    call cca0024
    if (B == 1):
        jump LA0025A
    if (B == 2):
        jump LA0025D
label LA0025A:
    call cca0025a
    if (B == 1):
        jump LA0025B
    if (B == 2):
        jump LA0025D
label LA0025B:
    call cca0025b
    if (B == 1):
        jump LA0025C
    if (B == 2):
        jump LA0025D
label LA0025C:
    call cca0025c
    $MISATO=1
    jump LA0029
label LA0025D:
    call cca0025d
    jump LA0026
label LA0026:
    call cca0026
    call cca0027
    call cca0028
label LA0029:
    call cca0029
    call cca0030
    $persistent.clear = True
    return
label ccb:
    $save_name = _("崩坏＼纯化")
    call ccb0001
    call ccb0002
    call ccb0003
    if (B == 1):
        jump LB0004B
    if (B == 2):
        jump LB0004C
label LB0004B:
    call ccb0004b
    jump LB0005
label LB0004C:
    call ccb0004c
    jump LB0005
label LB0005:
    call ccb0005
    call ccb0006
    call ccb0007
    if (B == 1):
        jump LB0008A
    if (B == 2):
        jump LB0008B
label LB0008A:
    call ccb0008a
    jump LB0009
label LB0008B:
    call ccb0008b
    jump LB0009
label LB0009:
    call ccb0009
    if (B == 1):
        jump LB0010A
    if (B == 2):
        jump LB1001
label LB0010A:
    call ccb0010a
    if (B == 1):
        jump LB2001
    if (B == 2):
        jump LB1001
label LB2001:
    call ccb2001
    jump LB0011
label LB0010B:
    call ccb0010b
    jump LB1001
label LB1001:
    call ccb1001
    if (B == 1):
        jump LB1002A
    if (B == 2):
        jump LB1002B
label LB1002A:
    call ccb1002a
    jump LB0011
label LB1002B:
    call ccb1002b
    jump LB0011
label LB0011:
    call ccb0011
    call ccb0012
    call ccb0013
    call ccb0014
    if (B == 1):
        jump LB0015AB
    if (B == 2):
        jump LB0015C
label LB0015AB:
    call ccb0015b
    jump RB_TOUKO
label LB0015C:
    call ccb0015c
    jump RB_MISATO
label RB_MISATO:
    $save_name=_("崩坏")
    call ccb1003
    call ccb1004
    call ccb0016
    call ccb1005
    call ccb1006
    if (B == 1):
        jump LB1007A
    if (B == 2):
        jump LB1007B
label LB1007A:
    call ccb1007a
    jump LB1008
label LB1007B:
    call ccb1007b
    jump LB1008
label LB1008:
    call ccb1008
    call ccb0017
    call ccb1009
    call ccb0018
    call ccb1010
    call ccb0019
    call ccb1011
    call ccb1012
    call ccb1013
    if (B == 1):
        jump LB1014A
    if (B == 2):
        jump LB1014D
label LB1014A:
    call ccb1014a
    if (B == 1):
        jump LB1014B
    if (B == 2):
        jump LB1014D
label LB1014B:
    call ccb1014b
    if (B == 1):
        jump LB1101
    if (B == 2):
        jump LB1014D
label LB1101:
    call ccb1101
    $MISATO=1
    jump LB0020
label LB1014D:
    call ccb1014d
    call ccb1015
    jump LB0020
label LB0020:
    call ccb0020
    call ccb0021
    call ccb1016
    call ccb1102
    call ccb0022
    call ccb0023
    $END=1
    jump RB_END
label RB_TOUKO:
    $save_name=_("纯化")
    call ccb2002
    jump LB2003A
label LB2003A:
    call ccb2003a
    jump LB2005
label LB2003B:
    call ccb2003b
    jump LB2005
label LB2005:
    call ccb2005
    call ccb2006
    call ccb0017
    call ccb2007
    call ccb2008
    call ccb2009
    call ccb0018
    call ccb2010
    call ccb2011
    call ccb2012
    call ccb2013
    call ccb2014
    call ccb0019
    call ccb2015
    call ccb2016
    call ccb0020
    call ccb2017
    call ccb2101
    call ccb2019
    call ccb2102
    call ccb2020
    call ccb0022
    call ccb2021
    $TOKO=1
    $END=1
    jump RB_END
label RB_END:
    return
label ccc:
    if roop == 2:
        $save_name ="CROSS+POINT"
    if roop == 3:
        $save_name ="INVISIBLE MURDER\nINVISIBLE TEARS"
    call ccc0000
    if (roop == 2):
        jump RC_0003
    if (roop > 2):
        jump RC_0004
    jump RC_0003
label RC_0003:
    call ccc0001
    call ccc0003a
    if (B == 1):
        jump LC0004A
    if (B == 2):
        jump LC0004B
label LC0004A:
    call ccc0004a
    jump LC0005
label LC0004B:
    call ccc0004b
    jump LC0005
label LC0005:
    call ccc0005
    call ccc0006a
    jump RC_TP0001
label RC_0004:
    call ccc0002
    call ccc0003b
    call ccc0006b
    jump RC_TP0001
label RC_TP0001:
    if (KIRI != 1):
        jump LC0006C
    if (MISATO != 1):
        jump LC0006C
    if (TOKO != 1):
        jump LC0006C
    jump LC0006D
label LC0006C:
    call ccc0006c
    if (B == 1):
        jump RC_KIRI
    if (B == 2):
        jump RC_MF
label LC0006D:
    call ccc0006d
    if (B == 1):
        jump RC_KIRI
    if (B == 2):
        jump RC_MF
    if (B == 3):
        jump RC_MIKI
label RC_KIRI:
    call ccc0007
    if (roop <= 4):
        jump LC0008A
    jump LC0008B
label LC0008A:
    call ccc0008a
    jump LC0010A
label LC0008B:
    call ccc0008b
    jump LC0010A
label LC0010A:
    call ccc0010a
    if (B == 1):
        jump LC0011A
    if (B == 2):
        jump LC0011B
label LC0011A:
    call ccc0011a
    jump LC0015
label LC0011B:
    call ccc0011b
    if (B == 1):
        jump LC0013A
    if (B == 2):
        jump LC0013B
label LC0013A:
    call ccc0013a
    jump LC0014
label LC0013B:
    call ccc0013b
    jump LC0014
label LC0014:
    call ccc0014
label LC0015:
    call ccc0015
    if (B == 1):
        jump LC0016A
    if (B == 2):
        jump LC0016B
label LC0016A:
    call ccc0016a
    jump LC0017
label LC0016B:
    call ccc0016b
    jump LC0017
label LC0017:
    call ccc0017
    if (B == 1):
        jump LC0018A
    if (B == 2):
        jump LC0018B
label LC0018A:
    call ccc0018a
    jump LC0019
label LC0018B:
    call ccc0018b
    jump LC0019
label LC0019:
    call ccc0019
    call ccc0022
    call ccc0020
    call ccc0021
    call ccc3001
    if (roop == 2):
        jump LC0023A
    if (roop >= 2):
        jump LC0023B
label LC0023A:
    call ccc0023a
    jump LC0024
label LC0023B:
    call ccc0023b
    jump LC0024
label LC0024:
    call ccc0024
    call ccc0025
    call ccc0026
    call ccc3002
    call ccc0027
    call ccc0028
    if (B == 1):
        jump LC0029A_1
    if (B == 2):
        jump LC0029B_1
label LC0029A_1:
    call ccc0029a
    jump LC0030_1
label LC0029B_1:
    call ccc0029b
    jump LC0030_1
label LC0030_1:
    call ccc0030
    if (B == 1):
        jump LC0031AB
    if (B == 2):
        jump LC0031C_1
label LC0031AB:
    if (roop == 2):
        jump LC0031A_1
    jump LC0031B_1
label LC0031A_1:
    call ccc0031a
    jump LC0032
label LC0031B_1:
    call ccc0031b
    jump LC3003
label LC0031C_1:
    call ccc0031c
    jump LC0032
label LC0032:
    call ccc0032
    if (B == 1):
        jump LC0033A
    if (B == 2):
        jump LC0033B
label LC0033A:
    call ccc0033a
    jump LC0034
label LC0033B:
    call ccc0033b
    jump LC0034
label LC0034:
    call ccc0034
label LC3003:
    call ccc3003
    call ccc0035a
    call ccc0036a
    call ccc0037
    if (roop == 2):
        jump LC0038A
    jump LC0038B
label LC0038A:
    call ccc0038a
    jump LC0039
label LC0038B:
    call ccc0038b
    jump LC0039
label LC0039:
    call ccc0039
    call ccc0040
    call ccc0041
    call ccc3004
    call ccc3005
    call ccc3006
    call ccc0042
    call ccc3007
    call ccc0043
    call ccc0044
    call ccc3008
    call ccc3009
    call ccc3010
    call ccc0045a
    call ccc3011
    if (B == 1):
        jump LC3012A
    if (B == 2):
        jump LC3012B
label LC3012A:
    call ccc3012a
    $KIRIBAD=0
    jump LC3013
label LC3012B:
    call ccc3012b
    $KIRIBAD=1
    jump LC3013
label LC3013:
    call ccc3013
    call ccc3014
    call ccc3015
    call ccc3016
    call ccc3017
    call ccc3018
    if (B == 1):
        jump LC3019B
    if (B == 2):
        jump LC3019C
label LC3019A:
    jump LC3020
label LC3019B:
    call ccc3019a
    jump LC3020
label LC3019C:
    call ccc3019b
    jump LC3020
label LC3020:
    call ccc3020
    call ccc3021
    call ccc3022
    call ccc3023
    if (B == 1):
        jump LC30XX
    if (B == 2):
        jump LC3024
label LC30XX:
    call ccc0101
    $END=1
    jump RC_END
label LC3024:
    call ccc3024
    jump LC3025
label LC3025:
    call ccc3025
    call ccc3026
    call ccc3027
    call ccc3028
    call ccc3029
    call ccc3030
    $KIRI=1
    $END=1
    jump RC_END
label RC_MIKI:
    call ccc0009
label LC0011C:
    call ccc0011c
    call ccc0022
    call ccc4001
    call ccc0023b
    call ccc4002
    call ccc0026
    call ccc4003
    call ccc0028
    if (B == 1):
        jump LC0029A_2
    if (B == 2):
        jump LC0029C_2
label LC0029A_2:
    call ccc0029a
    jump LC0030_2
label LC0029C_2:
    call ccc0029c
    jump LC0030_2
label LC0030_2:
    call ccc0030
    if (B == 1):
        jump LC0031B_2
    if (B == 2):
        jump LC0031C_2
label LC0031B_2:
    call ccc0031b
    jump LC4004
label LC0031C_2:
    call ccc0031c
    jump LC4004
label LC4004:
    call ccc4004
    call ccc4005
    call ccc0035b
    call ccc0036b
    call ccc0037
    call ccc0038b
    call ccc4006
    call ccc4007
    call ccc4008
    call ccc4009
    call ccc4010
    call ccc4011
    call ccc0042
    call ccc4012
    call ccc0043
    call ccc0044
    call ccc4014
    call ccc4015
    call ccc0045b
    call ccc4016
    call ccc4017
    call ccc4018
    call ccc4019
    call ccc4020
    call ccc4021
    call ccc4022
    call ccc4023
    call ccc4024
    call ccc4025
    $MIKI=1
    $END=1
    jump RC_END
label RC_MF:
    call ccb0003
    if (B == 1):
        jump LB0004B
    if (B == 2):
        jump LB0004C
label LB0004B:
    call ccb0004b
    jump LB0005
label LB0004C:
    call ccb0004c
    jump LB0005
label LB0005:
    call ccb0005
    call ccb0006
    call ccb0007
    if (B == 1):
        jump LB0008A
    if (B == 2):
        jump LB0008B
label LB0008A:
    call ccb0008a
    jump LB0009
label LB0008B:
    call ccb0008b
    jump LB0009
label LB0009:
    call ccb0009
    if (B == 1):
        jump LB0010A
    if (B == 2):
        jump LB1001
label LB0010A:
    call ccb0010a
    if (B == 1):
        jump LB2001
    if (B == 2):
        jump LB1001
label LB2001:
    call ccb2001
    jump LB0011
label LB0010B:
    call ccb0010b
    jump LB1001
label LB1001:
    call ccb1001
    if (B == 1):
        jump LB1002A
    if (B == 2):
        jump LB1002B
label LB1002A:
    call ccb1002a
    jump LB0011
label LB1002B:
    call ccb1002b
    jump LB0011
label LB0011:
    call ccb0011
    call ccb0012
    call ccb0013
    call ccb0014
    if (B == 1):
        jump LB0015AB
    if (B == 2):
        jump LB0015C
label LB0015AB:
    call ccb0015b
    jump RB_TOUKO
label LB0015C:
    call ccb0015c
    jump RB_MISATO
label RB_MISATO:
    call ccb1003
    call ccb1004
    call ccb0016
    call ccb1005
    call ccb1006
    if (B == 1):
        jump LB1007A
    if (B == 2):
        jump LB1007B
label LB1007A:
    call ccb1007a
    jump LB1008
label LB1007B:
    call ccb1007b
    jump LB1008
label LB1008:
    call ccb1008
    call ccb0017
    call ccb1009
    call ccb0018
    call ccb1010
    call ccb0019
    call ccb1011
    call ccb1012
    call ccb1013
    if (B == 1):
        jump LB1014A
    if (B == 2):
        jump LB1014D
label LB1014A:
    call ccb1014a
    if (B == 1):
        jump LB1014B
    if (B == 2):
        jump LB1014D
label LB1014B:
    call ccb1014b
    if (B == 1):
        jump LB1101
    if (B == 2):
        jump LB1014D
label LB1101:
    call ccb1101
    $MISATO=1
    jump LB0020
label LB1014D:
    call ccb1014d
    call ccb1015
    jump LB0020
label LB0020:
    call ccb0020
    call ccb0021
    call ccb1016
    call ccb1102
    call ccb0022
    call ccb0023
    $MISATO=1
    $END=1
    jump RC_END
label RB_TOUKO:
    call ccb2002
    jump LB2003A
label LB2003A:
    call ccb2003a
    jump LB2005
label LB2003B:
    call ccb2003b
    jump LB2005
label LB2005:
    call ccb2005
    call ccb2006
    call ccb0017
    call ccb2007
    call ccb2008
    call ccb2009
    call ccb0018
    call ccb2010
    call ccb2011
    call ccb2012
    call ccb2013
    call ccb2014
    call ccb0019
    call ccb2015
    call ccb2016
    call ccb0020
    call ccb2017
    call ccb2101
    call ccb2019
    call ccb2102
    call ccb2020
    call ccb0022
    call ccb2021
    $TOKO=1
    $END=1
    jump RC_END
label RC_END:
    return
label ccd:
label BK_CCD0001:
    $roopD += 1
    if (roopD == 1):
        jump LD0001
    if (roopD == 2):
        jump LD0002
    jump LD0003
label LD0001:
    $save_name=_("たった一つのもの")
    call ccd0001
    jump LD0003
label LD0002:
    call ccd0002
    jump LD0003
label LD0003:
    call ccd0003
    call ccd0004
label LD0005A:
    call ccd0005a
    call ccd0005c
    call ccd0006
    jump LD0007
label LD0005B:
    call ccd0005b
    jump LD0007
label LD0007:
    call ccd0007
    if (B == 1):
        jump LD0008A
    if (B == 2):
        jump LD0008B
    if (B == 3):
        jump LD0008C
    if (B == 4):
        jump LD0008D
    if (B == 5):
        jump LD0008E
label LD0008A:
    call ccd0008a
    jump LD0009
label LD0008B:
    call ccd0008b
    jump LD0009
label LD0008C:
    call ccd0008c
    jump LD0009
label LD0008D:
    call ccd0008d
    jump LD0009
label LD0008E:
    call ccd0008e
    jump LD0009
label LD0009:
    call ccd0009
    call ccd0010
    call ccd0011
    call ccd0012
    call ccd0013
    if (B == 1):
        jump LD0014A
    if (B == 2):
        jump LD0014B
    if (B == 3):
        jump LD0014C
label LD0014A:
    call ccd0014a
    jump LD0017
label LD0014B:
    call ccd0014b
    jump LD0017
label LD0014C:
    call ccd0014c
    if (B == 1):
        jump LD0015A
    if (B == 2):
        jump LD0015B
label LD0015A:
    call ccd0015a
    jump BK_CCD0001
label LD0015B:
    call ccd0015b
    if (B == 1):
        jump LD0016A
    if (B == 2):
        jump LD0016B
label LD0016A:
    call ccd0016a
    jump LD0017
label LD0016B:
    call ccd0016b
    jump LD0017
label LD0017:
    call ccd0017
    call ccd0018
    call ccd0019
    if (B == 1):
        jump LD0020A
    if (B == 2):
        jump LD0020B
    if (B == 3):
        jump LD0020C
label LD0020A:
    call ccd0020a
    jump LD0021
label LD0020B:
    call ccd0020b
    jump LD0021
label LD0020C:
    call ccd0020c
    jump LD0021
label LD0021:
    call ccd0021
    if (B == 1):
        jump LD0022A
    if (B == 2):
        jump LD0022B
label LD0022A:
    call ccd0022a
    jump BK_CCD0001
label LD0022B:
    call ccd0022b
    jump LD0023
label LD0023:
    call ccd0023
    jump RD_SBACK
label RD_SBACK:
    if (SB_MSA != 1):
        jump LD0101
    if (SB_TKO != 1):
        jump LD0101
    if (SB_KRI != 1):
        jump LD0101
    if (SB_MKI != 1):
        jump LD0101
    if (SB_SKU != 1):
        jump LD0101
    jump RD_YKO
label LD0101:
    call ccd0101
    if (B == 1):
        jump LD0102
    if (B == 2):
        jump RD_MKI
label LD0102:
    call ccd0102
    if (B == 1):
        jump RD_KRI
    if (B == 2):
        jump RD_TKO
    if (B == 3):
        jump RD_MSA
    if (B == 4):
        jump RD_SKU
label RD_MSA:
    $save_name=_("謝りに")
    call ccd1001
    $SB_MSA=1
    jump RD_SBACK
label RD_TKO:
    $save_name=_("Disintegration")
    call ccd2001
    call ccd2002
    $SB_TKO=1
    jump RD_SBACK
label RD_KRI:
    $save_name=_("大切な人")
    call ccd3001
    if (B == 1):
        jump LD3002A
    if (B == 2):
        jump LD3002B
label LD3002A:
    call ccd3002a
    call ccd3099
    if (B == 1):
        jump RD_SBACK
    $END=1
    jump title
label LD3002B:
    call ccd3002b
    call ccd3003
    $SB_KRI=1
    jump RD_SBACK
label RD_MKI:
    $save_name=_("いつか、わたし")
    call ccd4001
    if (B == 2):
        jump LD4002A
    if (B == 1):
        jump LD4002B
label LD4002A:
    call ccd4002a
    call ccd0201
    if (B == 1):
        jump RD_SBACK
    $END=1
    return
label LD4002B:
    call ccd4002b
    call ccd4003
    $SB_MKI=1
    jump RD_SBACK
label RD_SKU:
    $save_name=_("亲友")
    call ccd6001
    $SB_SKU=1
    jump RD_SBACK
label RD_YKO:
    $save_name=_("弱虫")
    call ccd5001
    $SB_YKO=1
    $save_name=_("CROSS X CHANNEL")
    call ccx0001
    $save_name=_("黑须ちゃん+ 寝る")
    call cce0001
    $END=1
    return
label ndemo0001:
    if renpy.android or renpy.ios:
        $renpy.movie_cutscene("mov/ccop_a.mp4")
    else:
        $renpy.movie_cutscene("mov/ccop_a.mpg")
    return
label ndemo0002:
    if renpy.android or renpy.ios:
        $renpy.movie_cutscene("mov/ccop_b.mp4")
    else:
        $renpy.movie_cutscene("mov/ccop_b.mpg")
    return
label ndemoend:
    if renpy.android or renpy.ios:
        $renpy.movie_cutscene("mov/ed.mp4")
    else:
        $renpy.movie_cutscene("mov/ed.mpg")
    return