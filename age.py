#this program says hello and asks you your name and age tells you how old you will be by the year 2030
import sys
while True:
    print("hello! nice to meet you!,\n ")
    greetings = str(input("how are you??: "))
    name = str(input("what's your name: "))
    age = float(input("how old are you?: "))
    year = float(input("in which year you were born?: "))
    print(" great! then by the year 2030 you'll be,\n ")
    future = (int("2030") - year)
    print(future)
    print("")
    again = input("\n want to calculate for other person or again?, \n\n y for yes or, \n q for quit, \n\n ")
    if again.upper() == "y":
        continue
    elif again.upper() == "q":
        break
sys.exit( "bye! thx 👋👋👋") 

   # 2030 = 2030 - year
    # print(2030)
    # # it cuts from here and never runs the bellow commands!! but why?? to do it i have to store the users input answer as a variable.
    # # nums =float("2030")
    # print("then by the year 2030 you'll be,\n")
     
