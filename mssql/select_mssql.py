import pymssql
import config 
 
# server  資料庫伺服器名稱或IP
# user   使用者名稱
# password 密碼
# database 資料庫名稱
def SelectData(phone_number):
    conn = pymssql.connect(config.server,config.user, config.password, config.database)
    cursor = conn.cursor()
    phone_a = '%'+phone_number+'%'
    try:
        cursor.execute("select * from AFC_Account where phone_A like '%s'"%(phone_a))
        
        rows = cursor.fetchall()
        
        print(rows)
        return rows

    except:
        conn.rollback()
    conn.close()




SelectData('1204')