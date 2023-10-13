def main():
    number  = geet()
    number2 = geet1()
    operation(number,number2)
    is_true()
    
def geet():
    
        n = int(input("Enter your first number: "))
        return n
    
def geet1():
    
        a = int(input("Enter your first number: "))
        return a
def operation(a,b):
    calc = input("What do you want to do? ")
    if calc == "+":    
      n = a + b
      print(f"The sum is: {n}" )
    if calc == "-":
          n  = a - b
          print(f"The difference is: {n} ")
    if calc == "*":
          n = a * b
          print(f"The product is: {n}")
    if calc == "/":
          n = a/b
          print(f"The division is: {n}")
    if calc == "%":
          n = a % b
          print(f"The remainder is: {n}")
          

def is_true():
      while True:
            x =input("Do you want to continue? ")
            if x.lower().capitalize() == "YES":
                  main()
            else:
                  break         
main()



        

