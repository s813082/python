number = [25,39,16,27,7,12,45,63]
arraylength = len(number)

for n in range (1,arraylength):
    tmp = number[n]
    m = n - 1
    print(m)
    # 如果左邊數字大於現在的數字則進行搬數字動作
    while m>=0 and number[m]> tmp:
        # 將數字往右移
        number[m+1] = number[m] 
        m = m-1
    print(m)
    number[m+1] = tmp
    print(number)


    
                