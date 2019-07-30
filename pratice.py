#!/usr/bin/env python
# coding: utf-8

# In[19]:


a = 10
b = 2
print(a+b)


# In[8]:


import os
path = "myDir"
os.mkdir(path) # 建立目錄
os.rmdir(path) # 移除目錄
os.system("mkdir dir123456") #執行作業系統命令
os.rename('test_change3.txt', 'test_change4.txt')
os.
print("當前目錄位置--->",os.getcwd())


# In[20]:


import os
os.chdir('D:\Wistron')
file = "重設ie瀏覽器、新增信任網站.pdf"
print("完整路徑名稱--->",os.path.abspath(file))  # 完整路徑名稱
print(file," 是否存在--->",os.path.exists(file)) # 是否存在
print(file," 檔案大小--->",os.path.getsize(file)) #取得檔案大小


# In[22]:


content = '''Python first   
測試中文
第三行
'''  # '''...'''  保留原本的格式
f = open('firstFile.txt','wt') # 寫入模式，檔案如果已經存在會被覆蓋
f.write(content)
f.close()


# In[1]:


from selenium import webdriver
#使用chrome的webdriver
browser = webdriver.Chrome()
#開啟google首頁
browser.get('http://google.com/')
#如果需要執行完自動關閉，就要加上下面這一行
#browser.close()

