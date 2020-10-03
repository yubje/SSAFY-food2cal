'''
import os

training_labels = os.listdir("/Users/multicampus/Desktop/SSAFY/PJT2/SUB_PJT2/음식이미지샘플/")
f = open("labels.txt", "w")
for training_label in training_labels:
    f.write(training_label + "\n")
f.close()
'''

'''

# xml
from PIL import Image
import os

"""
mode_to_bpp = {"1": 1, "L": 8, "P": 8, "RGB": 24, "RGBA": 32, "CMYK": 32, "YCbCr": 24, "LAB": 24, "HSV": 24, "I": 32, "F": 32}
bpp = mode_to_bpp[im.mode]
if bpp == 24:
"""


absolute_path = "/Users/multicampus/Desktop/SSAFY/PJT2/YOLO2/darkflow/train"
for file in os.listdir(absolute_path + "/images"):
    if file.endswith("jpg"):
        im = Image.open(absolute_path + "/images/" + file)
        if im.mode == "RGB":
            _, _ , w, h  = im.getbbox()
            
            objName, _ = file.split(' ')

            s = "<annotation> <folder> images </folder> <filename>"
            s += file
            s += "</filename> <size> <width>"
            s += str(w)
            s += "</width> <height>"
            s += str(h)
            s += "</height>	<depth>3</depth></size>	<segmented>0</segmented><object><name>"
            s += objName
            s += "</name><pose>Left</pose><truncated>1</truncated><difficult>0</difficult><bndbox><xmin>0</xmin><ymin>0</ymin><xmax>"
            s += str(w)
            s += "</xmax><ymax>"
            s += str(h)
            s += "</ymax>	</bndbox></object>	</annotation>"

            f = open(absolute_path + "/Annotations/" + file + ".xml", "w")
            f.write(s)
            f.close()
'''

'''
# 경로 내 RGB파일 아닌 것 골라내기

from PIL import Image
import os

tmp = []
for file in os.listdir("./images"):
    im = Image.open("./images/" + file)
    if im.mode == "RGB":
        continue
    else:
        tmp.append(file)
else:
    print(tmp)
'''

'''
# 비트 수준 24가 아닌 이미지의 xml 리스트가 확보 된 후,
# annotaions 폴더에 해당 xml 파일들 지워주기
import os

del_lst = ['Img_007_0445.xml', 'Img_023_0015.xml', 'Img_023_0029.xml', 'Img_023_0053.xml', 'Img_023_0114.xml', 'Img_023_0125.xml', 'Img_023_0198.xml', 'Img_023_0238.xml', 'Img_023_0244.xml', 'Img_023_0257.xml', 'Img_023_0259.xml', 'Img_023_0322.xml', 'Img_023_0333.xml', 'Img_023_0412.xml', 'Img_027_0015.xml', 'Img_027_0031.xml', 'Img_027_0043.xml', 'Img_027_0071.xml', 'Img_027_0081.xml', 'Img_027_0100.xml', 'Img_027_0112.xml', 'Img_027_0120.xml', 'Img_027_0151.xml', 'Img_027_0163.xml', 'Img_027_0166.xml', 'Img_027_0178.xml', 'Img_027_0199.xml', 'Img_027_0217.xml', 'Img_027_0219.xml', 'Img_027_0248.xml', 'Img_027_0275.xml', 'Img_027_0285.xml', 'Img_027_0287.xml', 'Img_027_0293.xml', 'Img_027_0298.xml', 'Img_027_0307.xml', 'Img_027_0320.xml', 'Img_027_0324.xml', 'Img_027_0326.xml', 'Img_027_0429.xml', 'Img_027_0433.xml', 'Img_027_0446.xml', 'Img_027_0455.xml', 'Img_027_0457.xml', 'Img_027_0477.xml', 'Img_027_0486.xml', 'Img_028_0027.xml', 'Img_028_0029.xml', 'Img_028_0057.xml', 'Img_028_0124.xml', 'Img_028_0180.xml', 'Img_028_0222.xml', 'Img_028_0250.xml', 'Img_028_0277.xml', 'Img_028_0288.xml', 'Img_028_0289.xml', 'Img_028_0304.xml', 'Img_028_0341.xml', 'Img_028_0363.xml', 'Img_028_0383.xml', 'Img_028_0388.xml', 'Img_028_0417.xml', 'Img_028_0426.xml', 'Img_028_0482.xml', 'Img_033_0110.xml', 'Img_033_0266.xml', 'Img_033_0295.xml', 'Img_033_0302.xml', 'Img_050_0010.xml', 'Img_050_0483.xml', 'Img_050_0487.xml', 'Img_069_0026.xml', 'Img_069_0067.xml', 'Img_069_0074.xml', 'Img_069_0121.xml', 'Img_069_0126.xml', 'Img_069_0129.xml', 'Img_076_0018.xml', 'Img_076_0041.xml', 'Img_076_0102.xml', 'Img_076_0120.xml', 'Img_076_0128.xml', 'Img_076_0202.xml', 'Img_076_0268.xml', 'Img_076_0283.xml', 'Img_098_0353.xml', 'Img_119_0029.xml', 'Img_119_0136.xml', 'Img_119_0171.xml', 'Img_119_0300.xml', 'Img_119_0368.xml', 'Img_119_0397.xml', 'Img_119_0416.xml', 'Img_119_0459.xml', 'Img_119_0490.xml', 'Img_119_0492.xml']
for file in os.listdir('./annotations'):
    file_path = './annotations/' + file
    if os.path.isfile(file_path):
        if file in del_lst:
            print(file)
            os.remove(file_path)
'''