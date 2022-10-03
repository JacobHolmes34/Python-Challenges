def mintosecs():
    minutes = int(input("Enter how mant minutes to convert?"))
    seconds = minutes*60
    print("It is" +str( seconds) + "seconds")
    

mintosecs()

def addition():
    num1=input("enter a number")
    num2=input("enter a number")
    total = int(num1) + int(num2)
    print(total)


addition()

def celcius():
    fare=input("input the temp in farenheight")
    celcius1=int(fare) - 32
    celcius2 = int(celcius1)/1.8
    print(celcius2)

celcius()
