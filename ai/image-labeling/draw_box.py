import os
import matplotlib.pyplot as plt
import cv2
from matplotlib.widgets import RectangleSelector
from generate_xml import write_xml
from PIL import Image

# global constants
img = None
tl_list = []
br_list = []
object_list = []

# constants
image_folder = 'images'
savedir = 'annotations'

'''
밥   : 밥(잡곡밥), 김밥
김치 : 배추김치
찌개 : 김치찌개
면   : 라면
고기 : 불고기
전   : 계란말이
기타 : 피자, 후라이드치킨, 양념치킨
'''

# ** 해당 음식 이름 하나로 바꿔서 실행) **
obj = 'fidget_spinner'  # 바꿔야할 곳

def line_select_callback(clk, rls):
    global tl_list
    global br_list
    tl_list.append((int(clk.xdata), int(clk.ydata)))
    br_list.append((int(rls.xdata), int(rls.ydata)))
    # print(clk.xdata, clk.ydata)
    object_list.append(obj)

def onkeypress(event):
    global object_list
    global tl_list
    global br_list
    global img
    if event.key == 'q':
        write_xml(image_folder, img, object_list, tl_list, br_list, savedir)
        # 변수 초기화 & 이미지 닫기
        tl_list = []
        br_list = []
        object_list = []
        img = None


def toggle_selector(event):
    toggle_selector.RS.set_active(True)


for n, image_file in enumerate(os.scandir(image_folder)):
    img = image_file
    fig, ax = plt.subplots(1, figsize=(10.5, 8))
    mngr = plt.get_current_fig_manager()
    mngr.window.setGeometry(250, 40, 800, 600)
    image = cv2.imread(image_file.path)
    # print(image_file.path)
    if 'Img' in image_file.path and image_file.path.endswith("jpg"):
        im = Image.open(image_file.path)
        mode_to_bpp = {"1": 1, "L": 8, "P": 8, "RGB": 24, "RGBA": 32, "CMYK": 32, "YCbCr": 24, "LAB": 24, "HSV": 24, "I": 32, "F": 32}
        bpp = mode_to_bpp[im.mode]
        # 이미지 색상 모드 & 비트 수준 체크
        if im.mode == "RGB" and bpp == 24:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            ax.imshow(image)

            toggle_selector.RS = RectangleSelector(
                ax, line_select_callback,
                drawtype='box', useblit=True,
                # button=[1]: it means left mouse click
                button=[1], minspanx=5, minspany=5,
                spancoords='pixels', interactive=True
            )
            bbox = plt.connect('button_press_event', toggle_selector)
            key = plt.connect('key_press_event', onkeypress)
            plt.show()
            plt.close(fig)