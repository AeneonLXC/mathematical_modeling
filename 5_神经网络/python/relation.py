import pandas as pd
import pingouin as pg
path = "./csv/附件2.xlsx"
df = pd.read_excel(path)
pg.partial_corr(data=df, x='时间（min）', y='乙醇转化率(%)', covar='C4烯烃选择性')
resilt = df.pcorr().round(3)
resilt.to_csv("./csv/resilt.csv")
