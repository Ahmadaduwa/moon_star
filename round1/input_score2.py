import pandas as pd #

uri = "round1.xlsx"
df = pd.read_excel(uri)

while (True) :
    print("Enter id_student (enter 0 to stop):")
    student = int(input())
    
    if student == 0:
        print("จบโปรแกรม")
        break
    elif student not in df['id_student'].values:
        print("ไม่พบนักศึกษาคนนี้")
        continue
    else:   
        print("Enter Personality2 (25):")
        score_Personality = int(input())
        print("Enter Expression2 (15):")
        score_Expression = int(input())
        print("Enter charm2 (10)):")
        score_charm = int(input())
        
        row_index = df[df['id_student'] == student].index.values[0]
        df.at[row_index, "Personality2"] = score_Personality
        df.at[row_index, "Expression2"] = score_Expression
        df.at[row_index, "charm2"] = score_charm
        df.to_excel('round1.xlsx', index=False)
        print("ข้อมูลถูกบันทึกแล้ว")