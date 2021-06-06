# Python3 program to add two numbers

#  loopa al options ekle v1
#  başlangıç menüsü ekle v2
## 0.  normal başlangıç user termination v2
## 1.  counter console a yazdır. Kaçıncı döngü gibi. v2
## 2.
## 9.  programdan çıkış v2
#  sonuçlanan sayıyı yorumla : asal , tek/çift v3



# //////////////////////////////////
# sayıları veya sonuçları veritabanına yazabilirim
# OEIS ile ilişkilendirebilirim
# randomness ekleyebilirim
# olasılıksal sayılar ekleyebilirim
# sonuç hakkında yorumlar : asallık , tek çift vs
# //////////////////////////////////

def addTwoNumber():
    number1 = input("First number: \n")
    number2 = input("Second number: ")
    # Adding two numbers
    # User might also enter float numbers
    sum = float(number1) + float(number2)

    # Display the sum
    # will print value in float
    print("The sum of {0} and {1} is {2}".format(number1, number2, sum))
    print("Çıkmak için n ye basın")

def menu():
    print("""
          0 : normal addition
          1 : print Counter (n th step of loop)
          9 : exit
          """)


counter = 0
while True:
    menu()
    selection = input()
    if selection == "0":
        addTwoNumber()
    elif selection =="1":
        print(counter)
        counter += 1
        continue

    elif selection == "9":
        print("çıkılıyor...")
        break
    counter += 1
    exit_string = input("")
    if exit_string ==  "n":
        print("Çıkılıyor...")
        break
    else :
        continue