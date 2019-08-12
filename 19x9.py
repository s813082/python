# 我想要一個 19*9 乘法表，然後輸出的順序要是 0, m, 1, m-1, 2, m-2…以此類推，
# 舉例來說，當要輸出 7 的時候會長這樣：
# 7 * 1 = 7
# 7 * 9 = 63
# 7 * 2 = 14
# 7 * 8 = 56
# 7 * 3 = 21
# 7 * 7 = 49
# 7 * 4 = 28
# 7 * 6 = 42
# 7 * 5 = 35
count = 0
for x in range(1,20):
    for y in range(1,9):
        if(y%2 == 0 ):
            y = 10 - count 
            print(x,'x',y,' = ',x*y)
            count = count +1
        else:
            y = y - count
            print(x,'x',y,' = ',x*y)    
    print('=============')
    count = 0