# Python Program - Check Leap Year or Not

num = input("Enter year: ");
if num == 'x':
    exit();
try:
    year = int(num);
except ValueError:
    print("Please, enter year...exiting...");
else:
    if((year%4 == 0) and (year%100 != 0)):
        print(year, "is a Leap Year.");
    elif(year%100 == 0):
    	print(year, "is not a Leap Year.");
    elif(year%400 == 0):
    	print(year, "is a Leap Year.");
    else:
    	print(year, "is not a Leap Year.");