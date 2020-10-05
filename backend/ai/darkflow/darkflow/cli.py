from .defaults import argHandler #Import the default arguments
import os
from .net.build import TFNet
import json
import cv2

def cliHandler(image_url):
    FLAGS = argHandler()
    FLAGS.setDefaults()
    # FLAGS.parseArgs(args)

    # make sure all necessary dirs exist
    def _get_dir(dirs):
        for d in dirs:
            this = os.path.abspath(os.path.join(os.path.curdir, d))
            if not os.path.exists(this): os.makedirs(this)
    
    requiredDirectories = [FLAGS.imgdir, FLAGS.binary, FLAGS.backup, os.path.join(FLAGS.imgdir,'out')]
    if FLAGS.summary:
        requiredDirectories.append(FLAGS.summary)

    _get_dir(requiredDirectories)

    # fix FLAGS.load to appropriate type
    try: FLAGS.load = int(FLAGS.load)
    except: pass

    tfnet = TFNet(FLAGS)
    
    if FLAGS.demo:
        tfnet.camera()
        exit('Demo stopped, exit.')

    if FLAGS.train:
        print('Enter training ...'); tfnet.train()
        if not FLAGS.savepb: 
            exit('Training finished, exit.')

    if FLAGS.savepb:
        print('Rebuild a constant version ...')
        tfnet.savepb(); exit('Done')

    # tfnet.predict()
    # im = '이미지가 들어있는 폴더 경로' + str(image_name) # 이미지가 저장된 폴더 위치 + POST 요청과 함께 받은 이미지 이름
    im = 'yolo/sample.jpg'

    print(image_url)
    im = urlopen(image_url).read()
    # image = Image.open(io.BytesIO(res))
    result = tfnet.return_predict(cv2.imread(im))
    print(result)
    # result = json.dumps(result)
    return result