import pandas as pd #รวมคะแนนรอบคัดเลือก

uri = "round1.xlsx"
df = pd.read_excel(uri)
df = df.fillna(0)

for idx, row in df.iterrows():
    df.at[idx, "Sum"] = df.at[idx, "Personality"] + df.at[idx, "Expression"] + df.at[idx, "Speaking"] + df.at[idx, "charm"] + df.at[idx, "Personality2"] + df.at[idx, "Expression2"] + df.at[idx, "charm2"]
df.to_excel('round1.xlsx', index=False)

female_df = df[df['gender'] == 'female']
male_df = df[df['gender'] == 'male']
        
df = df.sort_values(by=['Sum'], ascending=False)
print("เรียงลำดับ pride")
print(df.head(10), "\n")

male_df = male_df.sort_values(by=['Sum'], ascending=False)
print("เรียงลำดับ male")
print(male_df.head(10), "\n")

female_df = female_df.sort_values(by=['Sum'], ascending=False)
print("เรียงลำดับ female")
print(female_df.head(10), "\n")
