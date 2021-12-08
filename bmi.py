height = float(input("키 : "))
weight = float(input("몸무게 : "))

BMI = weight/height**2
print("*** 체질량지수 :",format(BMI, ".1f"))
if BMI < 18.5 :
    print("저체중, 건강위험도 높음")
elif BMI < 25 :
    print("정상체중, 건강위험도 낮음")
elif BMI < 30 :
    print("과체중, 건강위험도 낮음")
elif BMI > 30 :
    print("비만, 건강위험도 높음")