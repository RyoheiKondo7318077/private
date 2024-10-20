import pandas as pd
import glob
import os

#para = "PSU_in_v"
para = "stack_cycles"

# パスで指定したファイルの一覧をリスト形式で取得. （ここでは一階層下のtestファイル以下）
csv_files = glob.glob('tsurumi/*.csv')

# 時間順でソート
csv_files.sort(key=os.path.getmtime, reverse=False)

#読み込むファイルのリストを表示
for a in csv_files:
    print(a)

#csvファイルの中身を追加していくリストを用意
data_list = []

#読み込むファイルのリストを走査
for file in csv_files:
    data_list.append(pd.read_csv(file, usecols=[para]))

#リストを全て行方向に結合
#axis=0:行方向に結合, sort
df = pd.concat(data_list, axis=1)

df.columns =["EL1-1","EL1-2","EL1-3","EL1-4","EL2-1","EL2-2","EL2-3","EL2-4"]

df.to_csv(para+".csv")
