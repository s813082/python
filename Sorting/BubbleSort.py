number = ["16","25","39","27","12","7","45","63"]
arraylength = len(number)
time = 1
print("Bubble sort : ")
print("Before sort",number)
print("================================================")    
# 左右比大小交換
for m in range(0,arraylength-1):
    for n in range(0,arraylength-1):  
        # 需要注意資料型態的變化 
        if int(number[n])-int(number[n+1])>0:
            tmp = number[n]
            number[n] = number[n+1]
            number[n+1] = tmp
            print("Sort",time,"time : ",number)
            time= time +1        

print("================================================")
print("After sort",number)


