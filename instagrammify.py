from PIL import Image
import os

def instagrammify(imgsrc,imgname):
    
    img = Image.open(imgsrc,'r')
    img_w, img_h = img.size
    if img_w > img_h :
        aspect = round(img_w)
    else:
        aspect = round(img_h)
        
    whitebg = Image.new('RGB',(aspect,aspect),(255,255,255))
    bg_w, bg_h = whitebg.size

    print (bg_w,bg_h)

    centre = (int((bg_w - img_w)/2), int((bg_h - img_h)/2))

    whitebg.paste(img,centre)

    # create folder if !exists:

    SaveLocation = imgsrc.replace(imgname,"") + "instagrammify/"
    if not os.path.exists(SaveLocation):
        os.makedirs(SaveLocation)
    
    whitebg.save(SaveLocation+imgname)


if __name__ == "__main__":

    no_of_images = int(input("Enter no. of pictures to instagrammify: "))
    for i in range (1,no_of_images+1):
        imgsrc = (input("Enter PATH of image " + str(i) + " : ")).replace("\\","/")
        imgname = imgsrc[imgsrc.rindex('/')+1:]
        instagrammify(imgsrc,imgname)
        
