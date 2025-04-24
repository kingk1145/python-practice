def main():
    try:
        a=int(input("Hey enter a number: "))
        print(a)
        print("Great choice")
        return
    
    except ValueError as v :
        print("HEy WhAt ThE HeLL you are doing")
        return
    
    finally:
        print("I am inside finally")

main()