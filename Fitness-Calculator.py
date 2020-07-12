def ft_to_cm():
    
    try:
        ft = float(input("\"ft\": "))
        print("\"cm\":", ft*30.48)
    except:
        print("\nInvalid Input!")


def kg_to_lbs():
    try:
        ft = float(input("\"kg\": "))
        print("\"lbs\":", ft*2.205)        
    except:
        print("\nInvalid Input!")




def lbs_to_kg():
    try:
        lbs = float(input("\"lbs\": "))
        print("\"kg\":", lbs/2.205)
    except:
        print("\nInvalid Input!")



def pal():
    print("\n*****/ Physical Activity Level (PAL) \\*****")
    print("    (1) Desk Job / no Exercise")
    print("    (2) Light Exercise 1-2 times/Week")
    print("    (3) Moderate Exercise 2-3 times/Week")
    print("    (4) Hard Exercise 3-5 times/Week")
    print("    (5) Physical job or Hard Exercise 6-7 times/Week")
    print("    (6) Professional Athelete")

    pal = int(input("Enter your (PAL) number: "))
  
        

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


def bmr():
    gender = input("Gender M/F: ")
    age = int(input("Age: "))
    height = float(input("Height \"cm\": "))
    weight = float(input("Weight \"kg\": "))

    

    BMR_Male = 10 * weight + 6.25 * height - 5 * age + 5
    BMR_Female = 10 * weight + 6.25 * height - 5 * age - 161

    if gender == "m" or gender == "M":
        return BMR_Male
    elif gender == "f" or gender == "F":
        return BMR_Female



def macro():
    gender = input("Gender M/F: ")
    age = int(input("Age: "))
    height = float(input("Height \"cm\": "))
    weight = float(input("Weight \"kg\": "))


    print("\n*****/ GOAL \\*****")
    print("    (1) Muscle Gain")
    print("    (2) Maintenance")
    print("    (3) Fat Loss")
    

    goal = int(input("What's your Goal: "))

    BMR_Male = 10 * weight + 6.25 * height - 5 * age + 5
    BMR_Female = 10 * weight + 6.25 * height - 5 * age - 161

    fat_gm = 0.8 * weight
    fat_cal = fat_gm * 9
    protein_gm = 2 * weight
    protein_cal = protein_gm * 4

    if gender == "m" or gender == "M":
        calories = BMR_Male * pal()
        if goal == 1:
            calories += 500
        elif goal == 2:
            calories = calories
        elif goal == 3:
            calories -= 500
        print("\nCalories:", int(calories))
        fat_per = (fat_cal * 100) / calories
        print("Fat     :", str(int(fat_cal))+"cal", "|",
              str(int(fat_gm))+"gm", "|", str(int(fat_per))+"%")
        protein_per = (protein_cal * 100) / calories
        print("Proteins:", str(int(protein_cal))+"cal", "|",
              str(int(protein_gm))+"gm", "|", str(int(protein_per))+"%")
        carb_cal = calories - (fat_cal+protein_cal)
        carb_gm = calories/4
        carb_per = (carb_cal * 100) / calories
        print("Carbs   :", str(int(carb_cal))+"cal", "|",
              str(int(carb_gm))+"gm", "|", str(int(carb_per))+"%")
    elif gender == "f" or gender == "F":
        calories = BMR_Female * pal()
        if goal == 1:
            calories += 500
        elif goal == 2:
            calories = calories
        elif goal == 3:
            calories -= 500
        print("\nCalories:", int(calories))
        fat_per = (fat_cal * 100) / calories
        print("Fat     :", str(int(fat_cal))+"cal", "|",
              str(int(fat_gm))+"gm", "|", str(int(fat_per))+"%")
        protein_per = (protein_cal * 100) / calories
        print("Proteins:", str(int(protein_cal))+"cal", "|",
              str(int(protein_gm))+"gm", "|", str(int(protein_per))+"%")
        carb_cal = calories - (fat_cal+protein_cal)
        carb_gm = calories/4
        carb_per = (carb_cal * 100) / calories
        print("Carbs   :", str(int(carb_cal))+"cal", "|",
              str(int(carb_gm))+"gm", "|", str(int(carb_per))+"%")


while True:
    print()
    print("(1) ft to cm")
    print("(2) kg to lbs")
    print("(3) lbs to kg")
    print("(4) Physical Activity Level (PAL)")
    print("(5) Basal Metabolic Rate (BMR)")
    print("(6) Macro")
    print("(0) exit")

    try:
        a = int(input("Select Option: "))
    except:
        print("\nInvalid Input! Please enter the number")
        break
    

    if a == 1:
        print("\n*****/ ft to cm \\*****")
        ft_to_cm()
        input("\nPress Enter to escape... ")
    elif a == 2:
        print("\n*****/ kg to lbs \\*****")
        kg_to_lbs()
        input("\nPress Enter to escape... ")
    elif a == 3:
        print("\n*****/ lbs to kg \\*****")
        lbs_to_kg()
        input("\nPress Enter to escape... ")
    elif a == 4:
        print("\nPAL:", pal())
        input("\nPress Enter to escape... ")
    elif a == 5:
        print("\n*****/ Basal Metabolic Rate (BMR) \\*****")
        print("\nBMR:", bmr(), "calories")
        input("\nPress Enter to escape... ")
    elif a == 6:
        print("\n*****/ Macro \\*****")
        macro()
        input("\nPress Enter to escape... ")
    elif a == 0:
        break
    else:
        print("\nInvalid Choice! Try Again")
