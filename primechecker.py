print("\t\tA warm welcome to prime number checker")
def prime(number):
    yes_prime = True

    if number== 1:
        yes_prime=False

    for a in range(2,number):
        if number%a == 0:
          yes_prime = False

    if yes_prime:
        print("It's a prime number")
        print("Thank you. Run me again!!!")
    else:
        print("Oooops!Not a prime number")


digitz = int(input("Enter a number: "))
prime(digitz)