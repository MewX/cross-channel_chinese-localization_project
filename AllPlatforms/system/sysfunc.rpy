label gl(id, filename):
    if len(filename.split("|")) == 2:
        $filename, mask = filename.split("|")
    else:
        $mask = ""
    python:
        try:
            persistent.cg[filename] = True
        except:
            pass
    if mask != "":
        $pic[id]=im.AlphaMask("pic/"+filename+".png",im.MatrixColor("msk/"+mask+".bmp",im.matrix.invert()))
        $renpy.show("pic"+str(id),what = im.AlphaMask("pic/"+filename+".png",im.MatrixColor("msk/"+mask+".bmp",im.matrix.invert())),zorder = 600 - id,at_list=[Transform(alpha=0)])
        return
    elif filename[:2] == "sg" or filename[:7] =="efcc200":
        $pic[id] = im.AlphaMask("pic/"+filename+".png",im.MatrixColor("msk/"+filename+"_msk.bmp",im.matrix.invert()))
        $renpy.show("pic"+str(id),what = im.AlphaMask("pic/"+filename+".png",im.MatrixColor("msk/"+filename+"_msk.bmp",im.matrix.invert())),zorder = 600 - id, at_list=[truecenter,Transform(alpha=0)])
        return
    else:
        $pic[id] = Image("pic/"+filename+".png")
        $renpy.show("pic"+str(id),what = Image("pic/"+filename+".png"),zorder = 600 - id,at_list=[Transform(alpha=0)])
    return
    
    
label vsp(id,status):
    python:
        try:
            renpy.show("pic"+str(id),what = pic[id],at_list=[Transform(alpha=status)])
        except:
            pass
    return
    
label gp(id, x = 0, y=0, t=None):
    if t==None:
        $renpy.show("pic"+str(id),what = At(pic[id],Transform(pos=(x,y))))
    else:
        $renpy.show("pic"+str(id),what = At(pic[id],t))
    return