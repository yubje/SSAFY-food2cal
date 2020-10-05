# -*- coding: utf-8 -*-
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Nutrition
from .serializers import NutritionSerializer

# from keras import optimizers
# from keras.models import Sequential
# from keras.layers import MaxPooling2D, Conv2D
# from keras.layers import Activation, Dropout, Flatten, Dense
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

from ai.darkflow.darkflow.cli import cliHandler
from django.http import HttpResponse

from django.db.models import Q

category = {"bulgogi": "불고기", "eggroll": "계란말이", "friedchicken": "후라이드치킨", "jobgokbab": "쌀밥", "kimbap": "김밥", "kimchi": "김치", "kimchijjigae": "김치찌개", "pizza": "피자", "ramen": "라면", "yangnyeomchicken": "양념치킨"}

@api_view(['GET'])
def index(request):
    image_url = list(dict(request.data).keys())[0]
    # image_url = 'https://photo-storage-ftc.s3.ap-northeast-2.amazonaws.com/image/2020106202418636.jpeg'
    print(image_url)
    result = cliHandler(image_url)
    food_list = []
    for data in result:
        food_list.append(category[data["label"]])
    print(food_list)
    context = []
    for food in set(food_list):
        nutritions = Nutrition.objects.filter(food_name=food)
        serializer = NutritionSerializer(nutritions, many=True)
        context.append(serializer.data)
    return Response(context)

# Create your views here.
# @api_view(['POST'])
# def predict(request):

#     category = {"0": "만두", "1": "콩자반", "2": "깻잎장아찌", "3": "갈비탕", "4": "꼬막찜", "5": "새우튀김", "6": "배추김치", "7": "갈비구이", "8": "된장찌개", "9": "육회", "10": "물회", "11": "김치찌개", "12": "소세지볶음", "13": "김밥", "14": "찜닭", "15": "갈치구이", "16": "후라이드치킨", "17": "자장면", "18": "수정과", "19": "삼계탕", "20": "순대", "21": "해물찜", "22": "피자", "23": "족발", "24": "계란찜", "25": "떡볶이", "26": "한과", "27": "감자채볶음", "28": "식혜", "29": "약과"}


#     classes_number = 30

#     model = Sequential()
#     model.add(Conv2D(32, (3, 3), input_shape=(150, 150, 3), padding='same'))
#     model.add(Activation('relu'))
#     model.add(MaxPooling2D(pool_size=(2, 2)))
#     model.add(Dropout(0.25))

#     model.add(Conv2D(32, (3, 3), padding='same'))
#     model.add(Activation('relu'))
#     model.add(MaxPooling2D(pool_size=(2, 2)))

#     model.add(Conv2D(64, (3, 3), padding='same'))
#     model.add(Activation('relu'))
#     model.add(MaxPooling2D(pool_size=(2, 2)))
#     model.add(Dropout(0.25))

#     model.add(Flatten())    # 벡터형태로 reshape
#     model.add(Dense(512))   # 출력
#     model.add(Activation('relu'))

#     model.add(Dense(128))   # 출력
#     model.add(Activation('relu'))
#     model.add(Dropout(0.5))

#     model.add(Dense(classes_number))
#     model.add(Activation('softmax'))

#     model.compile(loss='binary_crossentropy',   # 최적화 함수 지정
#         optimizer='adam',
#         metrics=['accuracy'])

#     hdf5_file = "07-0.0896.hdf5"
#     model.load_weights("ai/07-0.0896.hdf5")

#     try:
#         # 업로드 파일 처리 분기

#         url = list(dict(request.data).keys())[0]
#         print(url)
#         res = urlopen(url).read()
      

#         image = Image.open(io.BytesIO(res))
#         image = image.convert("RGB")
#         image = image.resize((150,150))
#         image_data = np.asarray(image)
#         I = [image_data]
#         I = np.array(I)
#         I = I.reshape(-1, 150, 150, 3)
#         I = I.astype("float") / 255.
  

#         result = model.predict(I)
#         idx = result[0].argmax()
#         food_name = category[str(idx)]
#         nutritions = Nutrition.objects.filter(food_name=food_name)
 
#         serializer = NutritionSerializer(nutritions, many=True)
#         return Response(serializer.data)


#     except Exception as e:
#         return {'error': str(e)}