AllowedVehiclesList = [ 'Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan' ]

def cars():
    print(" ")     
    print("********************************")
    print("AutoCountry Vehicle Finder v0.3")
    print("********************************")
    print("Please Enter the following number below from the following menu:")
    print("1. PRINT all Authorized Vehicles")
    print("2. SEARCH for Authorized Vehicle")
    print("3. ADD Authorized Vehicle")
    print("4. Exit")

cars()

finder = int(input("Please Enter a Number: "))

while finder != 4:
    if finder == 1:
        print(" ")
        print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles: ")
        for vehicle in AllowedVehiclesList:
            print(vehicle)
        cars()
        finder = int(input("Please Enter a Number: "))
    elif finder == 2:
        name = input("Please Enter the full Vehicle name: ")
        found = False  
        for vehicle in AllowedVehiclesList:
            if name == vehicle:  
                print(name, "is an authorized vehicle")
                found = True
                break  
        
        if not found:
            print(name, "is not an authorized vehicle, if you received this in error please check the spelling and try again")
        cars()
        finder = int(input("Please Enter a Number: "))

    elif finder == 3:
        Usercar = input ("Please Enter the full Vehicle name you would like to add: ")
        AllowedVehiclesList.append(Usercar)
        print("You have added", Usercar, "as an authorized vehicle")
        cars()
        finder = int(input("Please enter a number: "))
     
        

print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")