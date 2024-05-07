# import twstock
# twstock.__update_codes()
import requests
import pandas as pd

def get_stock_id():
    res1 = requests.get("https://isin.twse.com.tw/isin/class_main.jsp?market=1&issuetype=1")
    res2 = requests.get("https://isin.twse.com.tw/isin/class_main.jsp?market=2&issuetype=4")
    df1 = pd.read_html(res1.text)[0]
    df2 = pd.read_html(res2.text)[0]

    df1.columns = df1.iloc[0]
    df2.columns = df2.iloc[0]

    df1 = df1.iloc[1:]
    df1 = df1.dropna(thresh=3, axis=0).dropna(thresh=3, axis=1)

    df2 = df2.iloc[1:]
    df2 = df2.dropna(thresh=3, axis=0).dropna(thresh=3, axis=1)

    df1 = df1['有價證券代號']
    df2 = df2['有價證券代號']
    return  pd.concat([df1, df2], axis=0, ignore_index=True) #df1['有價證券代號'].add(df2['有價證券代號'])
allStock = get_stock_id()    
print(allStock)
# 選擇股票代碼
# stock_code = '2330'

# # 使用twstock的Stock類別創建股票對象
# stock = twstock.Stock(stock_code)

# # 獲取最近的股票數據，預設獲取最近31天的數據
# # 如果需要更多的數據，可以使用fetch_from(year, month)方法來獲取特定日期之後的數據
# data = stock.fetch_from(2020, 1)  # 例如，從2020年1月開始獲取數據
# # 輸出數據
# for entry in data:
#     print(entry.date, entry.open, entry.high, entry.low, entry.close, "\n")
