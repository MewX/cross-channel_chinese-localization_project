label ccc4003:
    voice "vfCCC4003kri000"
    霧 "「な―――ッ！？」"
    "霧が戦慄する。"
    voice "vfCCC4003kri001"
    霧 "「なんて下着を……」"
    "俺は昨日、美希に装着された（履かされた、よりしっくりくる表現）ぞうさんパンツのままだった。"
    voice "vfCCC4003mki000"
    美希 "「あれ？　先輩おふろ入ってないんですか？」"
    太一 "「うん」"
    voice "vfCCC4003mki001"
    美希 "「きちゃなーい！」"
    voice "vfCCC4003kri002"
    霧 "「不潔……」"
    "くっ、衛生的な小娘どもめ。"
    "そろって人を責め立てる。"
    voice "vfCCC4003mki002"
    美希 "「夏場なのですよ？」"
    voice "vfCCC4003kri003"
    霧 "「……人格がアレだと、身だしなみもアレに」"
    太一 "「汚いヤツは罪人扱いですか」"
    voice "vfCCC4003kri004"
    霧 "「ここで始末しておいた方がいいのかもしれない……」"
    太一 "「待てや！」"
    voice "vfCCC4003mki003"
    美希 "「むー。先輩のカブはおおいに下がりましたよ」"
    太一 "「一日だけじゃん？　二日にいっぺん入るよ？」"
    voice "vfCCC4003kri005"
    霧 "「何もわかってない……」"
    voice "vfCCC4003mki004"
    美希 "「毎日入らないと並以下なんです」"
    太一 "「えっ、そうなの？　曜子ちゃんそんなこと言わなかった……教えてくれなかった……」"
    "こういうことは、同世代の友人間で情報を交換しないと独自性が保持されたまま成人してしまうことも多々あるのだ！"
    "普通の人、というのは大変難しいことなのだ！"
    stop bgm
    voice "vfCCC4003mki005"
    美希 "「どうする、霧ちん」"
    voice "vfCCC4003kri006"
    霧 "「やばいよ、美希」"
    voice "vfCCC4003mki006"
    美希 "「うん、やばいね」"
    "示し合う二人。"
    voice "vfCCC4003kri007"
    霧 "「おかしいとは思っていたけど、まさかこれほどまでとは……」"
    voice "vfCCC4003mki007"
    美希 "「やるしかないんじゃないかな、これ」"
    voice "vfCCC4003kri008"
    霧 "「仕方ないけど、そうだね」"
    voice "vfCCC4003mki008"
    美希 "「だってこの人と部活しないといけないんだから」"
    voice "vfCCC4003kri009"
    霧 "「ん。どこでやる？」"
    太一 "「『やる』って何の相談してるの？」"
    "二人は無視して、話し合っている。"
    "小声。断片的に聞こえる。"
    voice "vfCCC4003mki009"
    美希 "「人目につかないところ」"
    voice "vfCCC4003kri010"
    霧 "「ひっそりと」"
    voice "vfCCC4003mki010"
    美希 "「強い薬で」"
    voice "vfCCC4003kri011"
    霧 "「ひと思いにやれば」"
    "なに話し合ってんだコイツラは。"
    太一 "「……やばそうな雰囲気……」"
    "逃げようかな。"
    voice "vfCCC4003kri012"
    霧 "「動くな！」"
    太一 "「ひぃっ？」"
    "ダメだ。逃げられない。"
    "これ以上、霧を刺激するのもまずい。"
    voice "vfCCC4003mki011"
    美希 "「先輩、あなたの処遇が決まりました」"
    太一 "「……ズホン履いていいかな？」"
    voice "vfCCC4003mki012"
    美希 "「だめです」"
    太一 "「鬼か」"
    voice "vfCCC4003mki013"
    美希 "「我々に同行してもらいますよ」"
    "我々とか言う美希。"
    太一 "「わかった……だがたかが風呂に一日入らなかったくらいでこの仕打ち……」"
    voice "vfCCC4003mki014"
    美希 "「ありえません。だいたい先輩は何の取り柄もないんですから、清潔にするのはもはや義務ですよ」"
    voice "vfCCC4003mki015"
    美希 "「けど先輩は怠った」"
    voice "vfCCC4003kri013"
    霧 "「あなたは異常です……いろんな意味で」"
    "異常者扱い。"
    voice "vfCCC4003mki016"
    美希 "「行きましょう」"
    extend "連行された。"
    call gl(0,"bgcc0000d")
    call vsp(0,1)
    call vsp(1,0)
    call vsp(2,0)
    with Dissolve(500.0/1000.0)
    call gl(0,"bgcc0007")
    call vsp(0,1)
    with wipeleft
    "で"
    太一 "「……え、なにされるの俺？」"
    "めっちゃ不安。"
    "先輩はまだ来ていない。"
    "助けてくれる人は誰もいないということだ。"
    "美希がプレハブからホースを持ってきた。"
    "霧はクロスボウで俺を監視している。"
    call gl(1,"TCYM0001|TCYM0000")
    call gp(1,t=center)#x=180
    call vsp(1,1)
    with dissolve
    voice "vfCCC4003mki017"
    美希 "「せんぱい、服脱いで」"
    太一 "「この上さらに」"
    霧 "「……」"
    "チャキ、とクロスボウでスナイプされる。"
    太一 "「……ハヒ」"
    "脱ぐ。"
    "シャツを脱ぐ。"
    "もう限りなくぞうさんパンツだけの俺だった。"
    太一 "「……これも、か」"
    call gl(1,"TCYM0000|TCYM0000")
    call vsp(1,1)
    with dissolve
    voice "vfCCC4003mki018"
    美希 "「うーん、まあそれは勘弁してあげます」"
    "そして美希は、ホースに装着されたホルダーの弁を解放した。"
    play se "se093"
    voice "vfCCC4003mki019"
    美希 "「じゃー！」"
    play bgm "bgm/bgm011.ogg"
    "強烈な水流が、俺を襲う。"
    太一 "「うぷっ」"
    call gl(1,"TCYM0003|TCYM0003")
    call vsp(1,1)
    with dissolve
    voice "vfCCC4003mki020"
    美希 "「そらそらー」"
    "こういうことか。"
    "強制クリーニング。"
    "ああ、せめて強制性感マッサージであったなら。"
    call gl(1,"TCYM0001|TCYM0000")
    call vsp(1,1)
    with dissolve
    voice "vfCCC4003mki021"
    美希 "「霧ちん、薬を！」"
    call gl(2,"TCSK0000|TCSK000x")
    call gp(2,t=left)#x=40
    call gp(1,t=right)#x=340
    call vsp(1,1)
    call vsp(2,1)
    with Dissolve(500.0/1000.0)
    voice "vfCCC4003kri015"
    霧 "「ＯＫ」"
    "霧がなにかを射出してきた。"
    太一 "「うっ、こ、これは？」"
    "むっとするシトラスミント。"
    "ボディソープか。"
    "ボトルを握って、俺に浴びせかけてくる。"
    call gl(1,"TCYM0003|TCYM0003")
    call vsp(1,1)
    with dissolve
    voice "vfCCC4003mki022"
    美希 "「そしてそして」"
    "二人はデッキブラシを持って……デッキブラシっ！"
    voice "vfCCC4003mki023"
    美希 "「いけーーーっ！」"
    call gl(2,"TCSK0001|TCSK000x")
    call vsp(1,1)
    with dissolve
    voice "vfCCC4003kri016"
    霧 "「えいっ、えいっ」"
    "俺は甲板のように洗われる。"
    太一 "「いててててててててっ！？」"
    "ちくちくする！　ちくちくするよ！"
    太一 "「俺は甲板じゃないぞ！」"
    "くそう、これも朝からカンパンなんて食べたせいか！"
    "世界ギャグか。"
    call gl(1,"TCYM0000|TCYM0000")
    call vsp(1,1)
    with dissolve
    voice "vfCCC4003mki024"
    美希 "「ソープ、ソープソープ！」"
    voice "vfCCC4003kri017"
    霧 "「ソープ、えいっ！」"
    "ソープ連呼。"
    "ちょっとドキドキ。"
    "俺は、おまえらを、ソープで、ソープに、ソー婦に……。"
    "再びデッキブラシ。"
    "苦痛に慣れると、どうでもよくなってきた。"
    "むしろ、ちくちくとした感触が清々しくさえある"
    call gl(2,"TCSK0003|TCSK0003")
    call vsp(2,1)
    with dissolve
    voice "vfCCC4003kri018"
    霧 "「み、美希！　ぞ、ぞうがっ！？」"
    play se "SE064"
    call gl(1,"TCYM0004|TCYM0002")
    call vsp(1,1)
    with dissolve
    voice "vfCCC4003mki025"
    美希 "「う、うわーーーーーっ！？　ぞうがいなないたーっ！」"
    "放水。"
    call gl(2,"TCSK0007|TCSK000x")
    call vsp(2,1)
    with dissolve
    voice "vfCCC4003kri019"
    霧 "「変態！　変態！！」"
    太一 "「こ、これは刺激を受けたからで……しかたな……うぷっ」"
    call gl(1,"TCYM0001|TCYM0000")
    call vsp(1,1)
    with dissolve
    voice "vfCCC4003mki026"
    美希 "「ごしごしごしごしーっ！」"
    "ムキになって擦ってくる。"
    call gl(2,"TCSK0003|TCSK0003")
    call vsp(2,1)
    with dissolve
    voice "vfCCC4003kri020"
    霧 "「きゃあっ、取れたよ、ぞう！」"
    "水流で取れてしまった。"
    call gl(1,"TCYM0004|TCYM0002")
    call vsp(1,1)
    with dissolve
    voice "vfCCC4003mki027"
    美希 "「アトミック雑貨で買ったぞうカバーがっ！？」"
    "やはりアトミック雑貨か……。"
    "あの店主（女性·美人·２５歳）、自身も変態だから見境無く売るな。"
    voice "vfCCC4003mki028"
    美希 "「見て霧ちん、まるで別の生き物のよう！」"
    call gl(2,"TCSK0002|TCSK000x")
    call vsp(2,1)
    with dissolve
    voice "vfCCC4003kri021"
    霧 "「見ちゃだめ！　目が腐る！」"
    "おまえら小学生か。"
    call gl(1,"TCYM0001|TCYM0000")
    call vsp(1,1)
    with dissolve
    voice "vfCCC4003mki029"
    美希 "「ぎにゃー、今ぶるんってなったー！？」"
    voice "vfCCC4003kri022"
    霧 "「きゃーーーーーーーーーーーっ！！」"
    call vsp(1,0)
    call vsp(2,0)
    with Dissolve(500.0/1000.0)
    "逃げ出す。"
    "全裸で一人残される俺。"
    太一 "「……フ」"
    "目尻に涙。"
    call gl(3,"TCMM0011|TCMM0011")
    call gp(3,t=center)#x=225
    call vsp(3,1)
    with dissolve
    voice "vfCCC4003msa000"
    見里 "「ふぁー、さて今日も頑張って……ん？」"
    call gl(3,"TCMM0004|TCMM000x")
    call vsp(3,1)
    with dissolve
    voice "vfCCC4003msa001"
    見里 "「きゃあぁぁぁぁぁぁぁぁぁぁぁぁぁぁぁぁぁっ！？」"
    hide pic3
    with dissolve
    "あの反応、処女だな。"
    太一 "「フ」"
    "ほろ苦ぇ……。"
    太一 "「うっうっうっ」"
    "泣いておくことにした。"
    play se "se080"
    "ばさっ"
    "そんな俺に、バスタオルがかけられた。"
    call gl(1,"TCYM0000|TCYM0000")
    call gp(1,t=center)#x=180
    call vsp(1,1)
    with dissolve
    voice "vfCCC4003mki030"
    美希 "「……いやー、逃げちゃいました、すいません」"
    voice "vfCCC4003mki031"
    美希 "「乙女には刺激強すぎましたね。はいコレ」"
    "新しい下着と、制服。"
    太一 "「うっ、美希……いいやつ」"
    "着る。"
    call gl(1,"TCYM0003|TCYM0003")
    call vsp(1,1)
    with dissolve
    voice "vfCCC4003mki032"
    美希 "「きれいになったし、バッチリですね」"
    太一 "「全身ヒリヒリするけどね」"
    call gl(1,"TCYM0000|TCYM0000")
    call vsp(1,1)
    with dissolve
    voice "vfCCC4003mki033"
    美希 "「霧っちー、みみ先輩、終わりましたよー」"
    voice "vfCCC4003kri023"
    霧 "「……本当～？」"
    "怯えながら出てくる二人。"
    voice "vfCCC4003mki034"
    美希 "「ということで、部活しましょ」"
    "にっこりと、笑った。"
    call gl(0,"bgcc0000a")
    call vsp(0,1)
    call vsp(1,0)
    call vsp(2,0)
    call vsp(3,0)
    with Dissolve(500.0/1000.0)
    "そして俺たちは部活に励んだ。"
    "ああ、こんな簡単だったんだ。"
    "結束って。"
    "俺が苦労して実施した、合宿はなんだったのだろう。"
    "やり方が悪かったのか、強引すぎたのか。"
    "人はどうやって触れあえばいいのか。"
    "わからないことだらけだ。"
    stop bgm
    return
    #