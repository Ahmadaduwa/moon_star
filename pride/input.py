import pandas as pd 

uri = "pride.xlsx"
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
        print("Enter questions (40): ")
        score_questions = int(input())
        print("Enter aptitude (20): ")
        score_aptitude = int(input())
        print("Enter tone (10)): ")
        score_tone = int(input())
        print("Enter personality (15)): ")
        score_personality = int(input())
        print("Enter Expression (15)): ")
        score_expression = int(input())
        
        row_index = df[df['id_student'] == student].index.values[0]
        df.at[row_index, "questions"] = score_questions
        df.at[row_index, "aptitude"] = score_aptitude
        df.at[row_index, "tone"] = score_tone
        df.at[row_index, "personality"] = score_personality
        df.at[row_index, "Expression"] = score_expression
        df.to_excel('pride.xlsx', index=False)
        print("ข้อมูลถูกบันทึกแล้ว")