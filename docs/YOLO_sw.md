# YOLOv2 darkflow

[패키지 설치 참고 링크](https://reyrei.tistory.com/16?category=824469)

[darkflow github](https://github.com/thtrieu/darkflow)

[yolov2 cfg, weights](https://pjreddie.com/darknet/yolov2/)



###### 콘다 가상환경에서 flow 실행시 자주 나는 오류

```bash
ImportError: Could not find 'cudnn64_7.dll'. TensorFlow requires that this DLL be installed in a directory that is named in your %PATH% environment variable. Note that installing cuDNN is a separate step from installing CUDA, and this DLL is often found in a different directory from the CUDA DLLs. You may install the necessary DLL by downloading cuDNN 7 from this URL: https://developer.nvidia.com/cudnn
```

- 올바른 버전의 cudnn 설치 후 시스템 환경변수에 경로 설정을 해줬음에도 잡지 못하는 상황

  - cudnn****.dll 설치된 경로를 찾아 직접 입력해주기

  - ```bash
    set PATH={cudnn***.dll 설치경로};%PATH%
    ```

    



## Training own dataset



#### 1. 동일한 모델의 cfg파일과 weights 파일 다운로드

- Tiny YOLO 사용
  - 파일명: yolov2-tiny-voc.weights



#### 2. cfg 파일을 복사하여 수정하기 (기존 파일이 **꼭** 있어야함(바로 수정X 반드시 복사하여 수정할 것))

```
...

[region]
anchors = 1.08,1.19,  3.42,4.41,  6.63,11.38,  9.42,5.11,  16.62,10.52
bias_match=1
classes=3
coords=4
num=5
softmax=1

...
```

- classes = 커스텀 데이터셋의 클래스 개수



```
...

[convolutional]
size=1
stride=1
pad=1
filters=40
activation=linear

[region]
anchors = 1.08,1.19,  3.42,4.41,  6.63,11.38,  9.42,5.11,  16.62,10.52

...
```

- filters = num * (classes + 5)
  - num이 5 이므로 classes 개수가 30개라면 `5 * (30 + 5) = 175`



#### 3. labes.txt 수정하기

```
label1
label2
label3
...
```

- 한 줄에 하나씩 레이블명 넣어주기



- python code

  ```python
  # label.txt 파일 만들기
  import os
  
  training_labels = os.listdir("/Users/multicampus/Desktop/SSAFY/PJT2/SUB_PJT2/음식이미지샘플/")
  f = open("labels.txt", "w")
  for training_label in training_labels:
      f.write(training_label + "\n")
  f.close()
  ```



#### 4. Annotation - xml 파일 생성

- xml 파일 예를 본 후 필요한 정보만 코드로 직접 작성하였음

```xml
<annotation>
    <folder> images </folder>
    <filename>baechukimchi (3).jpg</filename>
    <size> <width>900</width>
        <height>600</height>
        <depth>3</depth></size>
    <segmented>0</segmented>
    <object>
        <name>baechukimchi</name>
        <pose>Left</pose>
        <truncated>1</truncated>
        <difficult>0</difficult>
        <bndbox>
            <xmin>0</xmin>
            <ymin>0</ymin>
            <xmax>900</xmax>
            <ymax>600</ymax>
        </bndbox></object>
</annotation>
```

- 이미지의 비트수준이 8이면 에러 -> 24인 것만 골라서 xml파일 생성

  [비트수준 24인 jpg만 골라내기](https://stackoverflow.com/questions/1996577/how-can-i-get-the-depth-of-a-jpg-file)

- python code

  ```python
  #  Annotation - xml 파일 생성
  from PIL import Image
  import os
  
  
  # mode_to_bpp = {"1": 1, "L": 8, "P": 8, "RGB": 24, "RGBA": 32, "CMYK": 32, "YCbCr": 24, "LAB": 24, "HSV": 24, "I": 32, "F": 32}
  # bpp = mode_to_bpp[im.mode]
  # if bpp == 24:
  
  
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
  ```



#### 5. Training - 명령어를 이용해 학습 시키기

```python
python flow --model cfg/my-tiny.cfg --load bin/yolov2-tiny-voc.weights --train --annotation train/Annotations --dataset train/images --gpu 0.5 --epoch 100 --save 100 --keep 5
```

| arg          | meaning                                                      |
| ------------ | ------------------------------------------------------------ |
| --model      | cfg 파일 지정                                                |
| --load       | pretrained weights 지정 혹은 체크포인트로부터 불러오기 ex) 5150 (ckpt no.) or -1 (가장 최근) |
| --train      | 학습 명령어                                                  |
| --annotation | xml파일이 위치한 Annotation 경로 지정                        |
| --dataset    | 학습시킬 이미지 파일 경로                                    |
| --gpu        | gpu 사용할 값 지정. 0 ~ 1 사이                               |
| --save       | 지정된 수 만큼의 학습 이후 체크포인트 생성                   |
| --keep       | 지정된 수 만큼 마지막으로부터 weight 및 meta정보 유지(저장)  |



- darkflow 실행시 지정해 줄 수 있는 명령어들

  - darkflow/defaults.py 내부 코드

  ```python
      def setDefaults(self):
          self.define('imgdir', './sample_img/', 'path to testing directory with images')
          self.define('binary', './bin/', 'path to .weights directory')
          self.define('config', './cfg/', 'path to .cfg directory')
          self.define('dataset', '../pascal/VOCdevkit/IMG/', 'path to dataset directory')
          self.define('labels', 'labels.txt', 'path to labels file')
          self.define('backup', './ckpt/', 'path to backup folder')
          self.define('summary', '', 'path to TensorBoard summaries directory')
          self.define('annotation', '../pascal/VOCdevkit/ANN/', 'path to annotation directory')
          self.define('threshold', -0.1, 'detection threshold')
          self.define('model', '', 'configuration of choice')
          self.define('trainer', 'rmsprop', 'training algorithm')
          self.define('momentum', 0.0, 'applicable for rmsprop and momentum optimizers')
          self.define('verbalise', True, 'say out loud while building graph')
          self.define('train', False, 'train the whole net')
          self.define('load', '', 'how to initialize the net? Either from .weights or a checkpoint, or even from scratch')
          self.define('savepb', False, 'save net and weight to a .pb file')
          self.define('gpu', 0.0, 'how much gpu (from 0.0 to 1.0)')
          self.define('gpuName', '/gpu:0', 'GPU device name')
          self.define('lr', 1e-5, 'learning rate')
          self.define('keep',20,'Number of most recent training results to save')
          self.define('batch', 16, 'batch size')
          self.define('epoch', 1000, 'number of epoch')
          self.define('save', 2000, 'save checkpoint every ? training examples')
          self.define('demo', '', 'demo on webcam')
          self.define('queue', 1, 'process demo in batch')
          self.define('json', False, 'Outputs bounding box information in json format.')
          self.define('saveVideo', False, 'Records video from input video or camera')
          self.define('pbLoad', '', 'path to .pb protobuf file (metaLoad must also be specified)')
          self.define('metaLoad', '', 'path to .meta file generated during --savepb that corresponds to .pb file')
  ```



#### 6. Test - 명령어 이용 이미지 예측하기

```python
python flow --model cfg/my-tiny.cfg --load -1 --imgdir sample_img --gpu 0.5 --threshold 0.25
```

| args        | meaning                                                      |
| ----------- | ------------------------------------------------------------ |
| --load      | 지정된 ckpt weight 불러오기. -1: 가장 최근                   |
| --imgdir    | 예측할 이미지 파일 경로                                      |
| --threshold | 이미지에 대한 confidence 값이 설정한 임계점 이상일 경우에 라벨링 해줌 |



##### 6-1. save포인트와 load를 이용, 학습시킨 weights를 저장하고 불러올 수 있음

```
python flow --model cfg/my-tiny.cfg --load bin/yolov2-tiny-voc.weights --train --annotation train/Annotations --dataset train/Images --gpu 0.5 --epoch 300 --save 50 --keep 5
```

```python
python flow --model cfg/my-tiny.cfg --load -1 --imgdir sample_img --threshold 0.25
```



#### 7. 학습된 모델 .pb(protobuf file)로 저장하기

[참고링크](https://stackoverflow.com/questions/50618968/converting-checkpoints-generated-to-weights-darkflow)

The trained checkpoint files `yolov2-3c-5500.data` file is actually your weight file. If you want to convert to .pb file, use the below command

```python
python flow --model cfg/Your_ConfigFile.cfg --load Your_required_checkpoint-chkptNumber --savepb
```

flow --model cfg/my-tiny.cfg --load 5151 --savepb

flow --model cfg/my-tiny.cfg --load -1 --savepb



- .pb & .meta 파일을 이용한 예측 명령어

```python
python flow --pbLoad built_graph/my-tiny.pb --metaLoad built_graph/my-tiny.meta --threshold 0.25 --gpu 0.5 --imgdir training
```



#### 8. 저장된 .pb 파일과 .meta 파일을 이용해 이미지 결과 예측값 리턴하기

```python
# 저장된 .pb 파일과 .meta 파일을 이용해 이미지 결과 예측값 리턴하기
from darkflow.net.build import TFNet
import cv2

options = {"pbLoad": "built_graph/my-tiny.pb", "metaLoad": "built_graph/my-tiny.meta", "threshold": 0.2}

tfnet = TFNet(options)

imgcv = cv2.imread("./sample_img/jajangmyun (273).jpg")

# cv2.imshow('image', imgcv)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

result = tfnet.return_predict(imgcv)
print(result)
```





- darkflow\darkflow\dark\darknet.py", line 47
  - def get_weight_src(self, FLAGS):

```python
from ..utils.process import cfg_yielder
from .darkop import create_darkop
from ..utils import loader
import warnings
import time
import os

class Darknet(object):

    _EXT = '.weights'

    def __init__(self, FLAGS):
        self.get_weight_src(FLAGS)
        self.modify = False

        print('Parsing {}'.format(self.src_cfg))
        src_parsed = self.parse_cfg(self.src_cfg, FLAGS)
        self.src_meta, self.src_layers = src_parsed
        
        if self.src_cfg == FLAGS.model:
            self.meta, self.layers = src_parsed
        else: 
        	print('Parsing {}'.format(FLAGS.model))
        	des_parsed = self.parse_cfg(FLAGS.model, FLAGS)
        	self.meta, self.layers = des_parsed

        self.load_weights()

    def get_weight_src(self, FLAGS):
        """
        analyse FLAGS.load to know where is the 
        source binary and what is its config.
        can be: None, FLAGS.model, or some other
        """
        self.src_bin = FLAGS.model + self._EXT
        self.src_bin = FLAGS.binary + self.src_bin
        self.src_bin = os.path.abspath(self.src_bin)
        exist = os.path.isfile(self.src_bin)

        if FLAGS.load == str(): FLAGS.load = int()
        if type(FLAGS.load) is int:
            self.src_cfg = FLAGS.model
            if FLAGS.load: self.src_bin = None
            elif not exist: self.src_bin = None
        else:
            assert os.path.isfile(FLAGS.load +".meta"), \
            '{} not found'.format(FLAGS.load)
            self.src_bin = FLAGS.load
            name = loader.model_name(FLAGS.load)
            cfg_path = os.path.join(FLAGS.config, name + '.cfg')
            if not os.path.isfile(cfg_path):
                warnings.warn(
                    '{} not found, use {} instead'.format(
                    cfg_path, FLAGS.model))
                cfg_path = FLAGS.model
            self.src_cfg = cfg_path
            FLAGS.load = int()


    def parse_cfg(self, model, FLAGS):
        """
        return a list of `layers` objects (darkop.py)
        given path to binaries/ and configs/
        """
        args = [model, FLAGS.binary]
        cfg_layers = cfg_yielder(*args)
        meta = dict(); layers = list()
        for i, info in enumerate(cfg_layers):
            if i == 0: meta = info; continue
            else: new = create_darkop(*info)
            layers.append(new)
        return meta, layers

    def load_weights(self):
        """
        Use `layers` and Loader to load .weights file
        """
        print('Loading {} ...'.format(self.src_bin))
        start = time.time()

        args = [self.src_bin, self.src_layers]
        wgts_loader = loader.create_loader(*args)
        for layer in self.layers: layer.load(wgts_loader)
        
        stop = time.time()
        print('Finished in {}s'.format(stop - start))
```

- .pb 파일 생성할 때 ".meta" 확장자가 붙지 않아 에러:
  - +".meta" 붙여줘 수정
    - 학습시킬 땐 없어야함