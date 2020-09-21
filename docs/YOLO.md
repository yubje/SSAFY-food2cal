# YOLO

[yolov2 설치 참고 링크](https://reyrei.tistory.com/16)



​	[YOLO 공식문서](https://pjreddie.com/)

* YOLO와 호환이 가능하 면서 주로 사용되는 3가지 프레임 워크

  `Darknet`,	`Darkflow`,	`OpenCV`

  * Darknet

    > YOLO 개발자가 만든 프레임워크, YOLO를 위해 특별히 제작

    장점: 빠르다, GPU 또는 CPU와 함께 사용 가능

    단점: 리눅스에서만 호환가능

  * Darkflow 

    > Darknet을 텐서플로우에 적용한 것

    장점: 빠르다, GPU 또는 CPU와 함께 사용 가능, 리눅스, 윈도우, 맥에서 호환 가능

    단점: 설치가 복잡하다

  * OpenCV

    > 조건: 최소 3.4.2 버전 필요

    장점: OpenCV 외에 설치할 것이 없다

    단점: CPU에서만 작동하기 때문에 비디오를 실시간으로 처리하는데 속도가 느림



[ YOLO와 Python을 이용한 object detection](https://reyrei.tistory.com/16)



```python
# 주피터 노트북 실행
$ jupyter notebook

# 현재 가상환경을 jupyter notebook 커널에 추가
$ python -m ipykernel install --user --name {venv name} --display-name "{kernal name on jn}"
```





## 라이브러리, 패키지 버전

* conda 가상환경 설정 및 설치할 라이브러리

```python
# 가상환경 생성
conda create -n YOLOdark python=3.6 pip 


```



* CUDA, cuDNN

**Tensorflow 1.5 버전은 CUDA 9.0이 필요**하고, 1.3 버전부터는 **cuDNN 6 버전이 필요**

**CUDA 9.0 버전은 cuDNN 7.0이 필요**

[CUDA 9.0](https://developer.nvidia.com/cuda-90-download-archive?target_os=Windows&target_arch=x86_64&target_version=10)

[cuDNN v7.1.4 for CUDA 9.0](https://developer.nvidia.com/rdp/cudnn-archive#a-collapse714-9)



* Darkflow

Windows 10 환경에서 진행하여 darkflow를 사용했다.

Git을 통해서 레포를 그대로 받는다. [다운은 여기](https://github.com/thtrieu/darkflow)





## 이슈

* Microsoft Visual C++ 14.0이 필요하다는 에러

>error: Microsoft Visual C++ 14.0 is required. Get it with "Build Tools for Visual Studio": https://visualstudio.microsoft.com/downloads/

=> 필요한 패키지가 없어서 나는 것 [여기](https://m.blog.naver.com/beacon71/221872094394)를 참조하여 따라가서 해결 



* jupyter notebook에서 importError

  ```python
  > ImportError: cannot import name 'abs'
  ```

1. 깃허브에 나온 방법([링크](https://github.com/tensorflow/tensorflow/issues/20778))

   ```python
   # 1. uninstalling tensorflow
   pip uninstall tensorflow
   # 2. uninstalling protobuf
   pip uninstall protobuf
   # 3. 1. 3. reinstalling tensorlfow (which should come along with the correct protobuf version.
   pip install tensorflow==1.5. tensorflow==1.5
   ```

2. 이외 체크할 사안

   `tensorflow`와 `tensorflow-gpu`의 버전이 같은지!!



* `cv2.cvtColor` 함수 에러

  ```python
  OpenCV(4.1.0) C:\projects\opencv-python\opencv\modules\imgproc\src\color.cpp:182: error: (-215:Assertion failed) !_src.empty() in function 'cv::cvtColor'
  ```

  => 경로에 이미지가 없어서 `cv2.imread`에서는 에러가 안나고 `cv2.cvtColor`에서 변환할 때 아무 정보도 없어서 에러가 난 것이었다.



* ~~cmd에서 `make` 명령 사용할 수 있게 세팅~~ (리눅스 명령어라서 안먹음)

  ```cmd
  C:\Users\multicampus\Desktop\darknet>make
  'make'은(는) 내부 또는 외부 명령, 실행할 수 있는 프로그램, 또는
  배치 파일이 아닙니다.
  ```

  => GNU Make를 설치하면 끝나는 문제, 다운은 [여기](http://gnuwin32.sourceforge.net/packages/make.htm)에서 `Complete package, except sources`이라고 설명이 되어있는 부분을 받아서 설치!

  => 추가적으로 환경 변수 설정을 해줘야한다. 시스템 변수중 Path에 C드라이브 내에 `GnuWin32`가 설치된 폴더를 찾아 bin 폴더의 위치(`C:\Program Files (x86)\GnuWin32\bin`)를 등록하면 된다.

  => cmd에서 make -v를 입력했을 때, 버전 정보가 출력된다면 정상적으로 설치 완료된 것!

  



## 참조했던 다른 링크, 라이브러리들

1. [텐서플로우 객체 감지](https://www.tensorflow.org/hub/tutorials/object_detection#more_images)
2. [텐서플로우 객체 감지 colab](https://colab.research.google.com/github/tensorflow/hub/blob/master/examples/colab/object_detection.ipynb#scrollTo=D9IwDpOtpIHW)
3. [텐서플로우 이미지 분류 for IT](https://www.tensorflow.org/lite/models/image_classification/overview)
4. [labelimg 라이브러리](https://github.com/tzutalin/labelImg/tree/v1.8.3)