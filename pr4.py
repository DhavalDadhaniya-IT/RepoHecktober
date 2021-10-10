m=int(input("Enter the month: "))
d=int(input("Enter the day: "))

if m in range(1,5):
    print("Winter")
    
if m in range(5,9):
    print("Summer")
    
if m in range(9,13):
    print("Monsoon")