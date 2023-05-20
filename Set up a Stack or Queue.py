#STACKS & Q'S

List =[0,2,3,22,12] #Defined list already

    
restart = True #Reset variable = True


sq = input("Do you want to use an QUEUE or use a STACK? (Q/S)") #Asks user if they want a choose a stack or queue
print(List) #Prints out the list
while restart == True: #When the variabe restart is 'true'
    if sq == "STACK": #  If the users input to the question above was stack runs through this sub routine
        Ans = input("Do you want to PUSH or POP") #Asks user if they want to PUSH or POP
        if Ans == "PUSH": # User selects PUSH
            print("What number do you want to add?") #Asks user what number to push
            function = input() #Saves answer to a variable called function
            List.append(int(function)) #Converts the user anser from string into an integer using 'int()' and appends it to the list
            print(List) #Prints out updated this with the new number

        if Ans == "POP": #If the user selects POP
            length = len(List) #Finds the length of the list and save it to the variable length
            length-=1 #Length variable gets one taken away from it
            List.remove(List[length]) #removes a number from the list by using the index from length
            print(List) #Print updated list
            if length == 0: # If the length is equal to 0
                print("Stack Empty") #Print stack is empty

    if sq == "QUEUE" :#If the user's input to the question above was queue runs through this sub routine
        Ans = input("Do you want to PUSH or POP") # Asks user if they want to PUSH or POP
        if Ans == "PUSH": #User selects PUSH
            inp = input(int("What number do you want to add?")) # saves the users string and converts into an integer using the 'int' and saves it as a variable called inp
            List.append(inp) # append inp to the list
            print(List) #Prints updated list

        if Ans == "POP": # User selects POP
            length = len(List) #Finds the length of the list and save it to the variable length
            length-=1 #Length variable gets one taken away from it
            List.remove(List[0]) #Removes the first index of the list
            print(List) #Prints out updated list
            if length == 0: # If the length is equal to 0
                print("Stack Empty") #Print stack is empty


print("Would you like to restart?(Y/N)") #Asks user if they would like to restart
choice = input(" ") # saves answer as choice
if choice == "Y": #If chouces equals Y
        restart= True #Restart = true
if choice == "N": #If choice equals N
        restart = False #Restart = false
        exit() #Exit's program

