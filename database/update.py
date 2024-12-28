import sqlite3

con = sqlite3.connect("sample.db")
cursor = con.cursor()

# 以下はSQL Injection攻撃に対して脆弱なのでやらないこと
target_name = input("whose 'age' do you want to update?")
new_age = input("Tell me new age")
# 以下はSQL Injection攻撃に対して脆弱なのでやらないこと
# 例えばnew_ageに"50; DROP TABLE User;"とするとテーブルを削除できてしまう
# update_query = f"UPDATE User SET age = {new_age} WHERE name = '{target_name}'"
# cursor.executescript(update_query)

# placeholderである'?'と，execute()の第二引数(タプル)を使う
update_query = 'UPDATE User SET age = ? WHERE name= ?'
cursor.execute(update_query, (new_age, target_name))
# 引数が一つでもタプルで
# cursor.execute(update_query, (new_age,))
con.commit()