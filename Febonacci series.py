def febonic_series(limit):
    num1=0
    num2=1
    new_number=0
    while new_number<=limit:
        print(new_number)
        new_number = num1 + num2
        num2 = num1
        num1=new_number

limit=int(input("\tInput the limit for Febonic series Series:\n\t\t\t"))
febonic_series(limit)
