height = input("請輸入你的身高 : (m)")
weight = input("請輸入你的體重 : (kg)")

BMI = int(weight)/(float(height)*float(height))

if BMI<18.5:
    print("你的BMI ",BMI," 是過輕的")
elif 18.5<=BMI<24:
    print("你的BMI ",BMI," 是正常的")
else:
    print("你的BMI ",BMI," 是過重的")