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
images=os.listdir("D:\jeyaram\PaddleOCR_work\pdf_images")
print(images)
images=sorted(images, key=lambda fname: int(fname.split('.')[0]))
print(images)

os.chdir(r"D:\jeyaram\PaddleOCR_work\pdf_images")
for image in images:
    print("image",image)
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

 

