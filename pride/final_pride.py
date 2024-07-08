import pandas as pd #รวมคะแนนรอบคัดเลือก

uri = "pride.xlsx"
df = pd.read_excel(uri)
df = df.fillna(0)

for idx, row in df.iterrows():
    df.at[idx, "Sum"] = df.at[idx, "questions"] + df.at[idx, "aptitude"] + df.at[idx, "tone"] + df.at[idx, "personality"] + df.at[idx, "Expression"]
df.to_excel('pride.xlsx', index=False)
        
df = df.sort_values(by=['Sum'], ascending=False)
print("เรียงลำดับ pride")
print(df.head(10), "\n")