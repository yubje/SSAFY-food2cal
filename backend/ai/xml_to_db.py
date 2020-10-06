import sys
import mysql.connector
# from .models import Nutrition
import openpyxl
import os
import django

# os.environ.setdefault("DJANGO_SETTIINGS_MODULE", "backend.settings")
# django.setup()


# wb = openpyxl.load_workbook('nutrition.xlsx')
# sheet = wb['Sheet1']
# rows = sheet['A2':'U2660']


# for row in rows:
#     if row[5].value not in category:
#         continue
#     dict = {}
#     # dict['id'] = row[0].value
#     dict['foodname'] = row[5].value
#     dict['ammount'] = row[10].value
#     dict['calorie'] = row[14].value
#     dict['carbohydrate'] = row[20].value
#     dict['protein'] = row[18].value
#     dict['fat'] = row[19].value
#     print(dict)
#     Nutrition(**dict).save()

# -*- coding: utf-8 -*-

import openpyxl
import mysql.connector
import os
import sys

result = []

# 엑셀 데이터를 tuple 형식으로 저장 학번이 201600000 일 경우 16만 저장하도록 파싱


def excel_to_list(filename):
	wb = openpyxl.load_workbook(filename)
	ws = wb.active
	tmp_data = []
	db_list = []
	category = ["불고기", "계란말이", "후라이드치킨", "쌀밥", "김밥", "김치", "김치찌개", "피자", "라면", "양념치킨"]
	for row in ws.rows:
		if row[5].value in category and row[5].value not in db_list:
			print(row[5].value)
			id = row[0].value
			food_name = row[5].value
			amount = row[10].value
			calorie = row[14].value
			carbohydrate = row[20].value
			protein = row[18].value
			fat = row[19].value

			# tmp_data.append(id)
			tmp_data.append(food_name)
			tmp_data.append(amount)
			tmp_data.append(calorie)
			tmp_data.append(carbohydrate)
			tmp_data.append(protein)
			tmp_data.append(fat)

			result.append(tuple(tmp_data))
			tmp_data = []
			db_list.append(food_name)

# mysql 테이블에 튜플 데이터 삽입
def mysql_insert(db,table,data):
	try:
		cursor = db.cursor()
		sql = "INSERT INTO "+table+" (food_name, amount, calorie, carbohydrate, protein, fat) VALUES (%s, %s, %s, %s, %s, %s)"
		cursor.executemany(sql,data)
		db.commit()
		print("[+] Insertion success\n")
	except:
		print("[ERROR] Insertion failed\n")

# mysql 테이블의 기존 데이터를 삭제
def table_clear(db,table):
	try:
		cursor = db.cursor()
		cursor.execute("TRUNCATE TABLE "+table)
	except:
		print("[ERROR] Truncate failed\n")

# 파일이 존재하는지 체크
# return : True or False
def fileCheck(filename):
	return os.path.isfile("./"+filename)

def main():
	db = mysql.connector.connect(
		host="database.cxu3damrm7bj.ap-northeast-2.rds.amazonaws.com",
		user="admin",
		passwd="ssafya411",
		database="food2cal"
	)
	print("* * * * * * Excel to DB * * * * * *")
	print("[*] exit 입력 시 종료됩니다.")
	print("[*] 엑셀 파일은 .py 파일과 같은 디렉토리에 존재해야 합니다.")
	print("[*] 테이블이 존재하지 않을 경우 생성 후 가능합니다.\n")
	while True:
		filename = input("1. 엑셀 파일명 입력 : ")
		if fileCheck(filename) is True:
			table = input("3. 데이터베이스 테이블명 입력 : ")
			excel_to_list(filename)
			answer = input("[*] 테이블 내 기존 데이터가 삭제됩니다. 진행하시겠습니까? (Y,n) : ")
			if answer == "Y":
				table_clear(db,table)
				mysql_insert(db,table,result)
				break
			else:
				continue
		elif filename == "exit":
			db.close()
			sys.exit(1)
		else:
			print("[ERROR] 파일이 존재하지 않습니다.")
			continue
		print("\n")

	sys.exit(1)

if __name__ == "__main__":
    main()
