# Quadratic equation Algorthm
# Autor: Joao Luis


def cls():
    import os
    os.system('cls')

def pause():
    import os
    os.system('pause')

           
#Equation
def main():

    a = float(input("Quadratic equation: \nWhat is the value of a? "))

    if a == 0:
        print ("\"a\" can't be zero.")
        restart()
    else:  
        b = float(input("What is the value of b? "))
        c = float(input("What is the value of c? "))
        
        delta = b**2 - 4*a*c

        if delta < 0:
            print("Don't exist real root of x")
            pause()
            cls()
            restart()
        else:

            x1 = (-b + (delta)**(1/2))/(2*a)
            x2 = (-b - (delta)**(1/2))/(2*a)

            result_x1 = a*x1**2 + b*x1 + c
            result_x2 = a*x2**2 + b*x2 + c

        
            print("x1 is: %.2f " %x1)
            print("x2 is: %.2f " %x2)
            print("replacing x1 in the quadratic equation the result is: %.2f" %result_x1)
            print("Replacing x2 in the quadratic equation the result is: %.2f" %result_x2)

#Menu restart
def restart():
    print()
    an = input("Wish to restart? type: (y/n) ")
    print()
    if an == 'y':
        main()
    elif an == 'n':
        print("Thank you. ")
    else:
        cls()
        print("invalid digit.")
        return restart()

#main manu
while True:
    main()
    restart()     
    cls()
    break
                    

    
    

            



 



