label ccb0004c:
    太一 "「早いじゃん」"
    冬子 "「……」"
    太一 "「しかもまた私服通学か」"
    "群青に校則はあってなきに等しい。"
    "なにか差し障りがあれば、警備員の出番だ。"
    "学生が自らを律する必要などない。"
    "だから制服着用という決まり事は、まるで意味をなさない。"
    "いかに天下群青とはいえ、年頃の少女をひんむいて制服に着替えさせるわけにはいかないからだ。"
    "他の者と自らを分断するための。"
    "それは冬子の確固とした抵抗に違いなかった。"
    太一 "「萌え萌え制服姿が見たいにゃー」"
    冬子 "「……」"
    "うーん。"
    "こうまで無視が似合うキャラも珍しい。"
    "冬子はこんな状態でいるのが、もっとも絵になるわけで。"
    "俺は隣に座って、じっと横顔を見つめた。"
    "飽くことなく、ずっと。"
    太一 "「……」"
    冬子 "「……」"
    太一 "「…………」"
    冬子 "「…………」"
    太一 "「………………」"
    冬子 "「………………」"
    太一 "「………………………………………………………………」"
    play se "se006"
    call gl(0,"bgcc0006")
    call gl(1,"TCKT0003|TCKT000x")
    call gp(1,t=center)#x=230
    call vsp(0,1)
    call vsp(1,1)
    with Dissolve(500.0/1000.0)
    voice "vfccb0004cfyu005"
    冬子 "「……なんなのよもうっ！」"
    "いきり立った。"
    太一 "「こら、芸術品が喋るな」"
    call gl(1,"TCKT0001|TCKT000x")
    call vsp(1,1)
    with dissolve
    voice "vfccb0004cfyu006"
    冬子 "「何言ってるの？」"
    太一 "「美しくあれ」"
    call gl(1,"TCKT0002|TCKT000x")
    call vsp(1,1)
    with dissolve
    voice "vfccb0004cfyu007"
    冬子 "「わけわかんないっ！」"
    太一 "「おまえは語尾が～だわ、とか～ですわ、とかオバサン臭いんだからあんま喋るなよイメージが崩れる」"
    call gl(1,"TCKT0003|TCKT000x")
    call vsp(1,1)
    with dissolve
    voice "vfccb0004cfyu008"
    冬子 "「ぬぁんですってーっ！？」"
    "ダメだこりゃ。"
    "ぬぁんですってーとか言い出したよ。"
    "芸術の終焉だった。"
    太一 "「フー、興ざめだな」"
    "世界正義という強圧的な概念とともにキレイさっぱり根絶されたであろう米国人のように、肩をすくめてみせた。"
    太一 "「おまえに芸術の破壊者という二つ名を与える」"
    call gl(1,"TCKT0002|TCKT000x")
    call vsp(1,1)
    with dissolve
    voice "vfccb0004cfyu009"
    冬子 "「いらないっ！！」"
    太一 "「よかったな。ピカソもそんなこと言われてたぞ。またすごいのとならんだな」"
    call gl(1,"TCKT0003|TCKT000x")
    call vsp(1,1)
    with dissolve
    voice "vfccb0004cfyu010"
    冬子 "「い！！　ら！！　な！！　いっ！！」"
    "口笛を吹く。"
    太一 "「こわいですわ～」"
    voice "vfccb0004cfyu011"
    冬子 "「ですわなんて言ってないでしょっ！！」"
    太一 "「そうエクスクラメイションマークを二つセットでばかり使うなよ」"
    voice "vfccb0004cfyu012"
    冬子 "「どんな諫めかたなのよ！！」"
    太一 "「ぷっぷくぷー」"
    call gl(1,"TCKT0011|TCKT0011")
    call vsp(1,1)
    with dissolve
    voice "vfccb0004cfyu013"
    冬子 "「バカにしてんのっ！？　バカにしてるのよね！　バカにしてーーーーーっ！！」"
    "着火完了。"
    call gl(1,"TCKT0003|TCKT000x")
    call vsp(1,1)
    with dissolve
    voice "vfccb0004cfyu014"
    冬子 "「ふつー会話ってのは友好の証じゃないわけ？　あんたのはただバカにする目的でアプローチしてるだけじゃないのよ！　おバカなあんたがどうして私をバカにできるの！？　信じられないし信じたくもないし信じさせたくもないわよ！」"
    太一 "「よく燃える」"
    "あなたは最高です。"
    voice "vfccb0004cfyu015"
    冬子 "「○×△□＄＃％＆○×△□＄＃％＆ッッッッッ！！」"
    "うっとりと耳を傾けていると。"
    call vsp(1,0)
    with Dissolve(500.0/1000.0)
    "冬子の右手が霞んだ。"
    "はっ！？"
    stop bgm
    call gl(4,"sgcc0012")
    play se "se105"
    call vsp(4,1)
    with dissolve
    with vpunch
    extend "ばちーん！！"
    太一 "「ぐふっ」"
    "不意の平手うち。"
    "叩き倒される。"
    play se "SE069"
    "座る者のない机と椅子を巻き込んで、盛大にすっ転んだ。"
    play bgm "bgm/bgm013.ogg"
    call vsp(4,0)
    with Dissolve(500.0/1000.0)
    太一 "「いててて」"
    太一 "「さすがは合戦格闘術ハラキリ拳、隙がない」"
    call gl(1,"TCKT0003|TCKT000x")
    call vsp(1,1)
    with dissolve
    voice "vfccb0004cfyu016"
    冬子 "「だいたい、あんたたちみたいなピッパラリーと私は住む世界が違うの！　私がここにいるのは間違いであんたたちが私のそばにいることも間違いなの！」"
    "※ピッパラリー＝冬子語。頭の弱い人たちの意。"
    太一 "「意味が重複していないか？」"
    call gl(1,"TCKT0002|TCKT000x")
    call vsp(1,1)
    with dissolve
    voice "vfccb0004cfyu017"
    冬子 "「るさいっ！」"
    太一 "「非処女のヒステリーは見にくいばかりだぞ」"
    call gl(1,"TCKT0004|TCKT000x")
    call vsp(1,1)
    with dissolve
    voice "vfccb0004cfyu018"
    冬子 "「っっ！？」"
    "顔がひきつった。"
    call gl(1,"TCKT0002|TCKT000x")
    call vsp(1,1)
    with dissolve
    voice "vfccb0004cfyu019"
    冬子 "「あ、あ、あ……あんたが……それを……言うわけ？」"
    太一 "「まずいですかのう？」"
    "耳クソをほじりながらすっとぼける。"
    call gl(1,"TCKT0005|TCKT000x")
    call vsp(1,1)
    with dissolve
    voice "vfccb0004cfyu020"
    冬子 "「まずいもなにも……」"
    "低くくぐもった声で。"
    call gl(1,"TCKT0011|TCKT0011")
    call vsp(1,1)
    with dissolve
    voice "vfccb0004cfyu021"
    冬子 "「遙かなる次元を越えて……」"
    "ゆっくりと顔をあげて。"
    call gl(1,"TCKT0003|TCKT000x")
    call vsp(1,1)
    with dissolve
    voice "vfccb0004cfyu022"
    冬子 "「出て行けーーーーーーーっ！！」"
    stop bgm
    call gl(0,"bgcc0000d")
    call vsp(0,0)
    call vsp(1,0)
    with wipeleft
    "めでたく叩き出された。"
    pause (500.0/1000.0)
    pause (500.0/1000.0)
    return
    #