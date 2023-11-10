import pandas as pd

# 读取CSV文件
#df = pd.read_csv('./read_m4a.csv',encoding='ISO-8859-1')
df = pd.read_csv('./read_m4a.csv',encoding='utf-8')
1/0
# 如果"txt"列存在
if 'txt' in df.columns:
    # 将"txt"列的每个值添加字符串"good"并存储到新列"txt_corr"
    df['txt_corr'] = df['txt'] + ' good'

    # 保存修改后的DataFrame回CSV文件
    df.to_csv('./read_m4a_corr.csv', index=False,encoding='ISO-8859-1')
else:
    print("'txt' 列不存在")
