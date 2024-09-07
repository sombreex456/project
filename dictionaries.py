# details={"name":"Aryan","age":"seventeen","city":"London"}
# print(details,details["age"])

country_dictionary={}
while True:
    print("1.Insert") 
    print("2. Display the countries")
    print("3.Display the capitals")

    choice=int(input("Please enter  a choice"))
    if choice ==1:
        country=input("please enter a country")
        capital=input("please enter a capital")
        country_dictionary[country]=capital
    elif choice ==2:
        print(country_dictionary.keys())

    elif choice ==3:
        print(country_dictionary.values())
    
    elif choice ==4:
        country=input("please enter a country")
        print(country_dictionary[country])
    else:
        break   
