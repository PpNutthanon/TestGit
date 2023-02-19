#Match => รับ Parameter ในรูปแบบ String (เรื่มจากอักขระตัวแรก)
#Contains => ไม่จำเป็นต้องเริ่มจากอักขระตัวแรก
import pandas as pd
df=pd.read_excel("dataupdates.xlsx","weather",encoding="utf-8",index_col="Day")
print(df[df.Event.str.match("ฝนตก")])
print(df[df.Event.str.contains("ก")])
