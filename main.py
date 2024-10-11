from datetime import datetime

str1 = input("Input date: ")

datetime_obj = datetime.strptime(str1,"%Y.%m.%d")

print(datetime_obj)
