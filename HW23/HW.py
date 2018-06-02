#HW23
var = 1
get_detail =''
fruit_dic = {}
temp = 'fruit name'
while(var == 1):
	get_detail = input('輸入水果跟數量吧:')

	temp = get_detail.split(" ") #split input to temp[0] fruit name and temp[1] fruit_number
	
	if temp[0] != 'exit':
		if temp[0] in fruit_dic: #check if this fruit is exit or not
			temp[1] = int(temp[1]) # change string to int
			fruit_dic[temp[0]] += temp[1] # if exit add number
		else:
			temp[1] = int(temp[1]) # change string to int
			fruit_dic[temp[0]] = temp[1] #add key value in dictionary
	else:
		for k, v in fruit_dic.items():
			print("we have",k ,end=" ")
			print(v)
		print('good bye')
		break
	











	
	



