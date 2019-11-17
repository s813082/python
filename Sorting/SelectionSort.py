number = [16,25,39,27,12,7,45,63]
arraylength = len(number)
time = 1
originplace = 0

for m in range(0,arraylength-1):
    # 找出最小的數字
    print("需交換第",m+1,"個數字")
    minnumber = number[m]
    for n in range(m,arraylength-1):    
        arraynumber = number[n]
        if(minnumber - arraynumber > 0):
            minnumber = arraynumber
            # 紀錄原本最小值所在的位置 需要跟第一個位置的數字做互換
            originplace = n 
            number[originplace] = number[m]
            number[m]=minnumber
    print(number)
            
