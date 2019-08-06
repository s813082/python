import pymssql
import config 
 
# server  資料庫伺服器名稱或IP
# user   使用者名稱
# password 密碼
# database 資料庫名稱
conn = pymssql.connect(config.server,config.user, config.password, config.database)
 
cursor = conn.cursor()

try:
    cursor.execute("update AFC_Account set phone_a ='8511-1204' where name = '熊岳鵬'")
    conn.commit()

except:
    conn.rollback()
    
conn.close()