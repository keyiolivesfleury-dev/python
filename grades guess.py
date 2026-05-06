# grade calculator
#first of all i have set range wrongly
# grade_A = 85-90
# grade_B = 75-84 
# grade_C = 65-74 
# grade_D = 50-64 
# grade_E = 25-49 
# grade_F = 0-24
def grades():
    A = 90
    B = 80 
    C = 70
    D = 60 
    E = 50 
    F = 0
    print("\n let's see your grade!")
    marks = float(input("enter your marks: "))
    print("\n then your grade is, \n")
    if marks >= 90:
        print("A") # you forget those "" then python prints the value of the letter or other thing you have typed in.
    elif marks >= 80:
        print("B")
    elif marks >= 70:
        print("C")
    elif marks >= 60:
        print("D")
    elif marks >= 50:
        print("E")
    else:
        print("F")

    while True:
        again = input("\n to run again, \n enter..., \n r for run, \n to close enter, \n c for closing. ")
        if again == "r":
            return grades()
        elif again == "c":
            print(" thanks for using the app! ")
            break
        else:
            print(" you have to choose between r and c ")
            
grades()
# for x in user_in_put:
#     print(x)