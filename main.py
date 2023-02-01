import os
import aspose.words as aw

# create document object
doc = aw.Document()

# create a document builder object
builder = aw.DocumentBuilder(doc)

os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"
from paddleocr import PaddleOCR,draw_ocr
# You can set the parameter `lang` as `ch`, `en`, `fr`, `german`, `korean`, `japan`
ocr = PaddleOCR(use_angle_cls=True, lang='en')
import cv2 
import numpy as np
lines=[]
images=os.listdir("D:\jeyaram\PaddleOCR\pdf_images")
print(images)
os.chdir(r"D:\jeyaram\PaddleOCR\pdf_images")
for image in images:
    img_path =image
    result = ocr.ocr(img_path, cls=True)
    for idx in range(len(result)):
        res = result[idx]
        for line in res:
            #print(line[1][0])
            lines.append(line[1][0])

    string=" ".join(lines)
    STR=string.upper()
    print(STR)
    builder.write(STR)
    STR=None
doc.save("out.docx") 

 

# draw result
from PIL import Image
result = result[0]
image = Image.open(img_path).convert('RGB')
boxes = [line[0] for line in result]
txts = [line[1][0] for line in result]
scores = [line[1][1] for line in result]
im_show = draw_ocr(image, boxes, txts, scores)
im_show = Image.fromarray(im_show)
im_show.save('result1.jpg')