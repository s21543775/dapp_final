import tkinter as tk
from tkinter import ttk
from tkinter import *
import matplotlib
import matplotlib.pyplot as plt
from pandastable import Table, TableModel
import crypto


align_mode = 'nswe'


win = tk.Tk()

datanum = tk.IntVar()
data = tk.StringVar()

win.title('圖片下載器')
win.resizable(False, False)

def search_transection():
    coin1 = spinner_coin1.get()
    coin2 = spinner_coin2.get()
    tpair = coin1 + coin2
    timespace = spinner_time.get()
    #print(tpair,timespace)
    df = crypto.get_all_binance(tpair, timespace)

    plt.close()
    sma1 = df.Close.rolling(20).mean()
    sma2 = df.Close.rolling(60).mean()
    df.Close['2022'].plot()
    sma1['2022'].plot()
    sma2['2022'].plot()

    df.drop(columns=['Close_time', 'Quote_av', 'Trades', 'Tb_base_av', 'Tb_quote_av', 'Ignore'],inplace=True)
    #print(df.tail(datanum.get()))
    data.set(df.tail(datanum.get()))
    df.reset_index(inplace=True)
    pt = Table(f, dataframe=df.tail(datanum.get()), showtoolbar=True, showstatusbar=True)
    pt.show()

    plt.show()
    

    

lbl_title = tk.Label(win,text='加密貨幣交易資料查詢工具桌面版', font=('微軟正黑體', 24))
lbl_title.grid(column=0,row=0,columnspan=4,sticky=align_mode,padx=10,pady=10)

lbl_coin1 = tk.Label(win,text='幣種1', font=('微軟正黑體', 10),width=8)
lbl_coin1.grid(column=0,row=1,sticky=align_mode)

lbl_coin2 = tk.Label(win,text='幣種2', font=('微軟正黑體', 10),width=8)
lbl_coin2.grid(column=1,row=1,sticky=align_mode)

lbl_time = tk.Label(win,text='資料時間間隔', font=('微軟正黑體', 10),width=8)
lbl_time.grid(column=2,row=1,sticky=align_mode)

lbl_dataNum = tk.Label(win,text='輸出資料數量', font=('微軟正黑體', 10),width=8)
lbl_dataNum.grid(column=3,row=1,sticky=align_mode)

spinner_coin1 = ttk.Combobox(win,values=['BTC','USDC','AVAX','ETH','BNB','BUSD','GMT','SOL'],width=6,state='readonly')
spinner_coin1.grid(column=0,row=2,sticky=align_mode,padx=5)

spinner_coin2 = ttk.Combobox(win,values=['USDT','BUSD','BTC','USDC','EUR'],width=6,state='readonly')
spinner_coin2.grid(column=1,row=2,sticky=align_mode,padx=5)

spinner_time = ttk.Combobox(win,values=['4h','6h','8h','1d'],width=6,state='readonly')
spinner_time.grid(column=2,row=2,sticky=align_mode,padx=5)

ent_dataNum = tk.Entry(win,textvariable=datanum,width=4)
ent_dataNum.grid(column=3,row=2,sticky=align_mode,padx=5)

btn_search = tk.Button(win,text="查詢",width=4,command=search_transection)
btn_search.grid(column=4,row=2,sticky=align_mode,padx=10)

f = tk.Frame(win)
f.grid(column=0,row=3,columnspan=5,sticky=align_mode,padx=5,pady=10)

#win.geometry('+1200+500')
win.geometry('+800+300')

### 將視窗設為置頂 ###
win.wm_attributes('-topmost',1)
win.mainloop()