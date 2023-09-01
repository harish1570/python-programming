sec=int(input("enter the second no of second"))
hours=sec//3600
sec=sec % 3600
min = sec // 60
sec = sec % 60


print(hours, min , sec)
