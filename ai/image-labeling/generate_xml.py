import os
import cv2
from lxml import etree
import xml.etree.cElementTree as ET
cnt = 0

def write_xml(folder, img, objects, tl, br, savedir):
    global cnt
    if not os.path.isdir(savedir):
        os.mkdir(savedir)

    image = cv2.imread(img.path)
    # print(img.path)
    heigth, width, depth = image.shape

    annotation = ET.Element('annotation')
    ET.SubElement(annotation, 'folder').text = folder
    ET.SubElement(annotation, 'filename').text = img_name[cnt]
    ET.SubElement(annotation, 'segmented').text = '0'
    size = ET.SubElement(annotation, 'size')
    ET.SubElement(size, 'width').text = str(width)
    ET.SubElement(size, 'heigth').text = str(heigth)
    ET.SubElement(size, 'depth').text = str(depth)
    for obj, topl, botr in zip(objects, tl, br):
        ob = ET.SubElement(annotation, 'object')
        ET.SubElement(ob, 'name').text = obj
        ET.SubElement(ob, 'pose').text = 'Unspecified'
        ET.SubElement(ob, 'truncated').text = '0'
        ET.SubElement(ob, 'difficult').text = '0'
        bbox = ET.SubElement(ob, 'bndbox')
        ET.SubElement(bbox, 'xmin').text = str(topl[0])
        ET.SubElement(bbox, 'ymin').text = str(topl[1])
        ET.SubElement(bbox, 'xmax').text = str(botr[0])
        ET.SubElement(bbox, 'ymax').text = str(botr[1])

    xml_str = ET.tostring(annotation)
    root = etree.fromstring(xml_str)
    xml_str = etree.tostring(root, pretty_print=True)
    save_path = os.path.join(savedir, img.name.replace('jpg', 'xml'))
    cnt += 1
    with open(save_path, 'wb') as temp_xml:
        temp_xml.write(xml_str)

folder = 'images'
img_name = [name for name in os.listdir('images') if 'Img_047' in name]
# print(img_name)
img = [im for im in os.scandir('images') if 'Img_047' in im.name][0]

# ** 앞과 똑같이 음식 이름 하나만 넣어두면 됨.
objects = ['']    # 바꿔야할 곳

tl = [(10, 10)]
br = [(100, 100)]
savedir = 'annotations'


write_xml(folder, img, objects, tl, br, savedir)