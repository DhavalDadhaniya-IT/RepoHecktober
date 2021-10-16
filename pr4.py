m=int(input("Enter the month: "))
d=int(input("Enter the day: "))

if m in range(1,5):
    print("Winter")
    
if m in range(5,9):
    print("Summer")
    
if m in range(9,13):
    print("Monsoon")
    
    # Python Program to calculate the square root

# Note: change this value for a different result
num = 8 

# To take the input from the user
#num = float(input('Enter a number: '))

num_sqrt = num ** 0.5
print('The square root of %0.3f is %0.3f'%(num ,num_sqrt))
