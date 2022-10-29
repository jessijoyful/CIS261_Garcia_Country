import sys

def menu():
    print("COMMAND MENU")
    print("view - View country name")
    print("add - Add a country")
    print("del - Delete a country")
    print("exit - Exit program")

def dictionary():
    country = {'CA' : 'Canada', 'MX' : 'Mexico', 'US' : 'United States'}
    return country

def view(country):
    counter = 0           
    codes = country.keys() 
    print("Country codes: ", end = ' ')
    
    for cd in codes:
        print(cd, end = ' ')
    code = input("\nEnter country code: ")
    
    for cd in codes:
        if code == cd :
            print("Country name: ", country.get(code)) 
            counter = 1;                               
            break;
    
    if counter == 0 :
        print("There is  no country with that code.")

def add(country):
    counter = 0
    codes = country.keys()
    code = input("Enter country code: ")
    
    for cd in codes :
        if code == cd :
            print(country.get(code), "is already using this code") 
            counter = 1          
            break;
    
      
    if counter == 0 :   
        name = input("Enter country name: ")
        country.update({code : name})  
        print(name, " was added.")

def delete(country):
    counter = 0
    codes = country.keys()
    code = input("Enter country code: ")
    for cd in codes :
        if code == cd :  
            counter = 1  
            break;
    
          
    if counter == 1 :
        name = country.get(code) 
        country.pop(code)        
        print(name, " was deleted.")
    else :
        print("No such country code. ")

menu()

country_dic = dictionary()

while True :                    
    cmd = input('\nCommand: ')  
    
    if cmd == "view" :
        view(country_dic)
    elif cmd == "add" :
        add(country_dic)
    elif cmd == "del" :
        delete(country_dic)
    elif cmd == "exit" :
        print("Bye!")
        break
    else :
        print("Not a valid command. Please try again.")
        



