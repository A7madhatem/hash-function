# بسم الله الرحمن الرحيم
# صلي علي النبي

# 0- Take an input from the user
ValueList = input("Enter a list of values separated by space: ").split()
ValueList = [int(num) for num in ValueList] 

# 1- This is the function that create a hash table using hash function
def hashTable(lst):
    hash_dict = {}
    for value in lst:
        key = value % len(lst)
        if key in hash_dict:
            hash_dict[key].append(value)
        else:
            hash_dict[key] = [value]
    return hash_dict

# 2- The main function that contain the main program
def mainProgram():
    while True:
        hTable = hashTable(ValueList)
        print("\n----------------------------------------------------------------\n")
        print("\nChoose the operation that you want to perform : ")
        choice = int(input("\nChoice number 1: Construct the whole hash table using the function defined in Q1\nChoice number 2: Add a new element to the hash table\nChoice number 3: Update a value of a certain key\nChoice number 4: Delete an element from the hash table\nChoice number 5: Search for an element in the hash table\nChoice number 6: print All elements with their keys of the hash table\n7: exit\n\nYour Choice : "))
        
        # Activate the function of the hash table
        if choice == 1:
            print(hashTable(ValueList))

        # Add a new element to the table 
        elif choice == 2:
            newElement = int(input("\nEnter the new element that you want to add : "))
            key = newElement % len(hTable)
            if key in hTable:
                hTable[key].append(newElement)
            else:
                hTable[key] = [newElement]
            print(hTable)

        # Update a cerain value
        elif choice == 3:
            newKey = int(input("\nEnter the key that you want to update : "))
            if newKey in hTable:
                newElement = int(input("Enter the new element : "))
                if newElement % len(ValueList) == newKey:
                    hTable[newKey] = [newElement]
                    print(hTable)
                else:
                    print("\nThe value that you just entered is not valid ")
            else:
                print("\nThis key doesn't exist in the table ")

        # Delete a specific value    
        elif choice == 4:
            theKey = int(input("\nEnter the key of the element that you want to delete : "))
            if theKey in hTable:
                del(hTable[theKey])
                print(hTable)
            else:
                print("\nThe key you just entered doesn't exist in the table ")

        # Search for a value and return it's key
        elif choice == 5:
            listOfValues = list(hTable.values())
            values = [item for sublist in listOfValues for item in sublist]
            theValue = int(input("\nEnter the value that you want to search for : "))
            if theValue in values:
                for key in list(hTable.keys()):
                    if theValue in hTable[key]:
                        print(f"\nThe element exist and it's key = {key}")
                        break                     
            else:
                print("\nThe value doesn't exist ")

        # Just to print the table
        elif choice == 6:
            print(hTable)

        # End the program
        elif choice == 7:
            break
            
mainProgram()
