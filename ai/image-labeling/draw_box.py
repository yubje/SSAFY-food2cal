import os
import matplotlib.pyplot as plt
import cv2
from matplotlib.widgets import RectangleSelector
from generate_xml import write_xml

# global constants
img = None
tl_list = []
br_list = []
object_list = []

# constants
image_folder = 'images'
savedir = 'annotations'
obj = 'fidget_spinner'

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
    key = plt.connet('key_press_event', onkeypress)
    plt.show()
    plt.close(fig)