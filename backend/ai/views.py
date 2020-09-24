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

from PIL import Image
import os, glob
import numpy as np
from sklearn.model_selection import train_test_split
from openpyxl import load_workbook
from urllib.request import urlopen

# Create your views here.
@api_view(['GET'])
def predict(request):
    if __name__ == '__main__':
        category = ['후라이드치킨', '갈비탕', '콩자반', '갈비구이', '만두', '식혜', '순대', '새우튀김', '소세지볶음', '수정과', '육회', '깻잎장아찌', '찜닭', '계란찜', '김치찌개', '김밥', '꼬막찜', '갈치구이', '된장찌개', '한과', '떡볶이', '배추김치', '삼계탕', '약과', '해물찜', '족발', '물회', '자장면', '감자채볶음', '피자']
        classes_number = len(category)
        
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

        hdf5_file = "./08-0.0872.hdf5"
        model.load_weights(hdf5_file)

    try:
        # 업로드 파일 처리 분기
        url = list(request.form.to_dict().keys())[0]
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
        food_name = category[idx]
        nutritions = Nutrition.objects.filter(food_name=food_name)
        serializer = NutritionSerializer(nutritions, many=True)
        print(serializer.data)
        return Response(serializer.data)
        # data = {'result': category[idx]}
        # return data

    except Exception as e:
        return {'error': str(e)}