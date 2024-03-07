#Classwork 6
#Name: Chiang Shang-en, Sean
#SID: 57159310

year=int(input("Enter a year: "))



if year % 4==0:
    if year % 100 == 0 and year%400!=0: 
        print(f"Year {year} is not a leap year.")
    else: 
        print(f"Year {year} is a leap year.")
else:
    print(f"Year {year} is not a leap year.")
    
input("\nPress ENTER to exit.")
