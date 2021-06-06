# Python3 program to add two numbers

#  loopa al options ekle v1




while True:
    number1 = input("First number: ")
    number2 = input("\nSecond number: ")

    # Adding two numbers
    # User might also enter float numbers
    sum = float(number1) + float(number2)

    # Display the sum
    # will print value in float
    print("The sum of {0} and {1} is {2}".format(number1, number2, sum))
    print("Çıkmak için N/n ye basın")
    exit_string = input("")
    if exit_string == "N" or "n":
        print("Çıkılıyor...")
        break
    else :
        continue