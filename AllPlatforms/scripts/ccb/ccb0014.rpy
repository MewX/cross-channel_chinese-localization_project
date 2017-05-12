label ccb0014:
    call gl(0,"bgcc0006")
    call vsp(1,0)
    call vsp(0,1)
    call vsp(2,0)
    with wipeleft
    pause (500.0/1000.0)
    pause (1000.0/1000.0)
    call gl(1,"evcc0011")
    call vsp(1,1)
    with Dissolve(500.0/1000.0)
    "冬子がいた。"
    play bgm "bgm/bgm013.ogg"
    "というか、いっつも一等賞じゃないか、こいつ。"
    太一 "「おはよ」"
    voice "vfcca0013fyu000"
    冬子 "「……（ぷいり）」"
    "シカト？"
    "シカトですか。"
    太一 "「パンツ……」"
    voice "vfcca0013fyu001"
    冬子 "「くどい」"
    太一 "「パンツ買ってくんない？」"
    call gl(0,"bgcc0006")
    call gl(1,"TCKT0003|TCKT000x")
    play se "se006"
    call gp(1,t=center)#x=230
    call vsp(0,1)
    call vsp(1,1)
    with Dissolve(500.0/1000.0)
    voice "vfcca0013fyu002"
    冬子 "「どーして私があなたのパンツを買わないといけないのっ！」"
    "机をどついて立ちあがる冬子。"
    太一 "「朝からホットだね」"
    "親指を立てる。"
    call gl(1,"TCKT0001|TCKT000x")
    call vsp(1,1)
    with dissolve
    voice "vfcca0013fyu003"
    冬子 "「……」"
    "冬子は親指をぐっとつかんで、ごきっと横に折った。"
    太一 "「ぎえええええええっ！！」"
    太一 "「あほーっ、折れたらどうするのだーっ！　自慰もままならないではないかーっ！」"
    "危うく手首を返したからよかったものの。"
    call gl(1,"TCKT0002|TCKT000x")
    call vsp(1,1)
    with dissolve
    voice "vfcca0013fyu004"
    冬子 "「話しかけないで」"
    太一 "「昨日のテレビ見たぁ？」"
    call gl(1,"TCKT0003|TCKT000x")
    call vsp(1,1)
    with dissolve
    voice "vfcca0013fyu005"
    冬子 "「話しかけないで！」"
    太一 "「……むぅ」"
    "話しかけないでと辛口に言われると、話しかけたくなる。"
    menu:
        "話しかけると、また、話しかけないでと辛口に言われる。"
        "話しかける":
            $B=1
        "部活に行く":
            $B=2
    return
    #