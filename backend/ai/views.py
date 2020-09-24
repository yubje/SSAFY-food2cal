# -*- coding: utf-8 -*-
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Nutrition
from .serializers import NutritionSerializer

from keras import optimizers
from keras.models import Sequential
from keras.layers import MaxPooling2D, Conv2D
from keras.layers import Activation, Dropout, Flatten, Dense
import numpy as np
import os
import io

import copy

from PIL import Image
import os, glob
import numpy as np
from sklearn.model_selection import train_test_split
from openpyxl import load_workbook
from urllib.request import urlopen



# Create your views here.
@api_view(['POST'])
def predict(request):


    category = {"0": "후라이드치킨", "1": "갈비탕", "2": "콩자반", "3": "갈비구이", "4": "만두", "5": "식혜", "6": "순대", "7": "새우튀김", "8": "소세지볶음", "9": "수정과", "10": "육회", "11": "깻잎장아찌", "12": "찜닭", "13": "계란찜", "14": "김치찌개", "15": "김밥", "16": "꼬막찜", "17": "갈치구이", "18": "된장찌개", "19": "한과", "20": "떡볶이", "21": "배추김치", "22": "삼계탕", "23": "약과", "24": "해물찜", "25": "족발", "26": "물회", "27": "자장면", "28": "감자채볶음", "29": "피자"}

    
    classes_number = 30

    model = Sequential()
    model.add(Conv2D(32, (3, 3), input_shape=(150, 150, 3), padding='same'))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))

    model.add(Conv2D(32, (3, 3), padding='same'))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Conv2D(64, (3, 3), padding='same'))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))

    model.add(Flatten())    # 벡터형태로 reshape
    model.add(Dense(512))   # 출력
    model.add(Activation('relu'))

    model.add(Dense(128))   # 출력
    model.add(Activation('relu'))
    model.add(Dropout(0.5))

    model.add(Dense(classes_number))
    model.add(Activation('softmax'))

    model.compile(loss='binary_crossentropy',   # 최적화 함수 지정
        optimizer='adam',
        metrics=['accuracy'])

    hdf5_file = "08-0.0872.hdf5"
    model.load_weights("ai/08-0.0872.hdf5")

    try:
        # 업로드 파일 처리 분기

        url = list(dict(request.data).keys())[0]
        print(url)
        res = urlopen(url).read()
      

        image = Image.open(io.BytesIO(res))
        image = image.convert("RGB")
        image = image.resize((150,150))
        image_data = np.asarray(image)
        I = [image_data]
        I = np.array(I)
        I = I.astype("float") / 255
  

        result = model.predict(I)
        idx = result[0].argmax()
        food_name = category[str(idx)]
        nutritions = Nutrition.objects.filter(food_name=food_name)
 
        serializer = NutritionSerializer(nutritions, many=True)
        return Response(serializer.data)


    except Exception as e:
        return {'error': str(e)}