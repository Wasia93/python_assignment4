def main():
    print("This program adds two numbers.", flush=True) 

    num1 = int(input("Enter first number: "))  
    num2 = int(input("Enter second number: "))  

    total = num1 + num2  

    print(f"The total is {total}.", flush=True)


if __name__ == '__main__':
    main()