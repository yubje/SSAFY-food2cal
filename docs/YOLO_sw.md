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

