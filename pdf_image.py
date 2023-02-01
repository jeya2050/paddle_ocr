from pdf2image import convert_from_path
import os
print(os.getcwd())
# incase of Linux we don't have to provide the popper_path parameter
images = convert_from_path('deep_learning.pdf', poppler_path=r"D:\jeyaram\PaddleOCR_work\poppler-22.12.0\Library\bin")
os.chdir(r"D:\jeyaram\PaddleOCR_work\pdf_images")
for i in range(len(images)):
	# Save pages as images in the pdf
    images[i].save(f'image_{i+1}.png', 'PNG')