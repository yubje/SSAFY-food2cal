import os
import cv2
from lxml import etree
import xml.etree.cElementTree as ET

def modify_xml(savedir):
    pass
    # doc = ET.parse(file_name)
    # root = doc.getroot()

# img_name = [name for name in os.listdir('images') if 'Img_' in name]
anno_name = [name for name in os.listdir('annotations') if '.xml' in name]
# print(anno_name)

exceptiong_lst = []
for one_anno in anno_name:
    target_path = './annotations/' + one_anno
    doc = ET.parse(target_path)
    root = doc.getroot()
    # target_tag = root.iter('name')
    # print(target_tag)
    # ===============================
    test = root.find('object')
    try:
        target_tag = test.find('name')
        target_tag.text = 'yangnyeomchicken'
        print(target_path)
        # target_tag.text = 'deonjang'
        doc.write(target_path)
    except:
        exceptiong_lst.append(target_path)
print(exceptiong_lst)