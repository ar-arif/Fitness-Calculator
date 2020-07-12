from tkinter import *
from PIL import Image, ImageTk


root = Tk()
root.geometry("500x500")
root.title("Fitness-Calculator")
root.wm_iconbitmap("icon.ico")
root.resizable(0, 0)
# root.configure(bg="grey")






def result():
    # user input variable
    name = name_Value.get()
    gender = gender_Value.get()
    age = age_Value.get()
    height = height_Value.get()
    weight = weight_Value.get()
    goal = goal_Value.get()
    pal = pal_Value.get()

    def palF():
        
        if pal == 1:
            return 1.2
        elif pal == 2:
            return 1.4
        elif pal == 3:
            return 1.6
        elif pal == 4:
            return 1.75
        elif pal == 5:
            return 2
        elif pal == 6:
            return 2.4       

    print(name,gender,age,height,goal,pal)

    # algorithm variable
    bmr_Male = 10 * weight + 6.25 * height - 5 * age + 5
    bmr_Female = 10 * weight + 6.25 * height - 5 * age - 161

    fat_gm = 0.8 * weight
    fat_cal = fat_gm * 9
    protein_gm = 2 * weight
    protein_cal = protein_gm * 4

    if gender == 1:
        calories = bmr_Male * palF()
        if goal == 1:
            calories += 500
        elif goal == 2:
            calories = calories
        elif goal == 3:
            calories -= 500
        

        fat_per = (fat_cal * 100) / calories
        protein_per = (protein_cal * 100) / calories
        carb_cal = calories - (fat_cal+protein_cal)
        carb_gm = calories/4
        carb_per = (carb_cal * 100) / calories


        # Label(text=f"Mr. {name} your Result").grid()
        Label(text=f"Calories: {int(calories)}").grid()
        Label(text=f"Fat: {int(fat_cal)}(cal) || {int(fat_gm)}(gm) || {int(fat_per)}(%)").grid()
        Label(text=f"Protein: {int(protein_cal)}(cal) || {int(protein_gm)}(gm) || {int(protein_per)}(%)").grid()
        Label(text=f"Carb: {int(carb_cal)}(cal) || {int(carb_gm)}(gm) || {int(carb_per)}(%)").grid()

        print(f'''        Name: {name}
        Gender: Male
        Age: {age}
        calories: {int(calories)}
        Fat: {int(fat_cal)}(cal) | {int(fat_gm)}(gm) | {int(fat_per)}(%)
        Protein: {int(protein_cal)}(cal) | {int(protein_gm)}(gm) | {int(protein_per)}(%)
        Carb: {int(carb_cal)}(cal) | {int(carb_gm)}(gm) | {int(carb_per)}(%)''')


    elif gender == 2:
        calories = bmr_Female * palF()
        if goal == 1:
            calories += 500
        elif goal == 2:
            calories = calories
        elif goal == 3:
            calories -= 500
        

        fat_per = (fat_cal * 100) / calories
        protein_per = (protein_cal * 100) / calories
        carb_cal = calories - (fat_cal+protein_cal)
        carb_gm = calories/4
        carb_per = (carb_cal * 100) / calories


        # Label(text=f"Ms. {name} your Result").grid()
        Label(text=f"Calories: {int(calories)}").grid()
        Label(text=f"Fat: {int(fat_cal)}(cal) || {int(fat_gm)}(gm) || {int(fat_per)}(%)").grid()
        Label(text=f"Protein: {int(protein_cal)}(cal) || {int(protein_gm)}(gm) || {int(protein_per)}(%)").grid()
        Label(text=f"Carb: {int(carb_cal)}(cal) || {int(carb_gm)}(gm) || {int(carb_per)}(%)").grid()


        print(f'''        Name: {name}
        Gender: Female
        Age: {age}
        calories: {int(calories)}
        Fat: {int(fat_cal)}(cal) | {int(fat_gm)}(gm) | {int(fat_per)}(%)
        Protein: {int(protein_cal)}(cal) | {int(protein_gm)}(gm) | {int(protein_per)}(%)
        Carb: {int(carb_cal)}(cal) | {int(carb_gm)}(gm) | {int(carb_per)}(%)''')

    
















name_Value = StringVar()
gender_Value = IntVar()
age_Value = IntVar()
height_Value = IntVar()
weight_Value = IntVar()
goal_Value = IntVar()
pal_Value = IntVar()


f1 = Frame(root).grid(row=0, column=0)

f2 = Frame(root).grid(row=0, column=1)

Label(f1, text="Name  :", font="arial 10").grid(row=0, column=0)
Label(f1, text="Gender:", font="arial 10").grid(row=1, column=0)
Label(f1, text="Age     :", font="arial 10").grid(row=2, column=0)
Label(f1, text="Height (cm)  :", font="arial 10").grid(row=3, column=0)
Label(f1, text="Weight (kg) :", font="arial 10").grid(row=4, column=0)
Label(f1, text="Goal  :", font="arial 10").grid(row=5, column=0)
Label(f1, text="PAL  :", font="arial 10").grid(row=6, column=0)


Entry(f2, textvariable=name_Value).grid(row=0, column=1)
Radiobutton(f2, text="Male", variable=gender_Value, value=1).grid(row=1, column=1)
Radiobutton(f2, text="Female", variable=gender_Value, value=2).grid(row=1, column=2)
Entry(f2, textvariable=age_Value).grid(row=2, column=1)
Entry(f2, textvariable=height_Value).grid(row=3, column=1)
Entry(f2, textvariable=weight_Value).grid(row=4, column=1)
Radiobutton(f2, text="Muscle Gain", variable=goal_Value, value=1).grid(row=5, column=1)
Radiobutton(f2, text="Maintenance", variable=goal_Value, value=2).grid(row=5, column=2)
Radiobutton(f2, text="Fat Loss", variable=goal_Value, value=3).grid(row=5, column=3)

Radiobutton(f2, text="Desk Job / no Exercise", variable=pal_Value, value=1).grid(row=6, column=1)
Radiobutton(f2, text="Light Exercise 1-2 times/Week", variable=pal_Value, value=2).grid(row=7, column=1)
Radiobutton(f2, text="Moderate Exercise 2-3 times/Week", variable=pal_Value, value=3).grid(row=8, column=1)
Radiobutton(f2, text="Hard Exercise 3-5 times/Week", variable=pal_Value, value=4).grid(row=9, column=1)
Radiobutton(f2, text="Physical job or Hard Exercise 6-7 times/Week", variable=pal_Value, value=5).grid(row=10, column=1)
Radiobutton(f2, text="Professional Athelete", variable=pal_Value, value=6).grid(row=11, column=1)
Button(f2, text="Macro", command=result, padx=10, pady=10).grid(row=12, column=1)






root.mainloop()
