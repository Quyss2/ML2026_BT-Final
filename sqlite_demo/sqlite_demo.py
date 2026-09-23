import sqlite3
import pandas as pd
try:
    sqliteConnection = sqlite3.connect('../databases/23_09_26_DataSQL/Chinook_Sqlite.sqlite')
    cursor = sqliteConnection.cursor()
    print('chucmungthanglon kết nối DB')
    query = 'SELECT * FROM Customer LIMIT 5'
    cursor.execute(query)
    df = pd.DataFrame(cursor.fetchall())
    print(df)
    cursor.close()
except sqlite3.Error as error:
    print('Lỗi rồi chú em',error)
finally:
    if sqliteConnection:
        sqliteConnection.close()
        print('đã hủy kết nối database rồi chú')