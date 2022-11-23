def calculator():

    def titlecard():
        print("""
         _____       _            _       _             
        /  __ \     | |          | |     | |            
        | /  \/ __ _| | ___ _   _| | __ _| |_ ___  _ __ 
        | |    / _` | |/ __| | | | |/ _` | __/ _ \| '__|
        | \__/\ (_| | | (__| |_| | | (_| | || (_) | |   
        \____/\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   
                                                        
         Guide:
         Add
         Subtract
         Multiply
         Divide
         Help                                       
        
        """)

    def calculations():

        userinput = str.lower(input("Pick an operation: "))
        operations = ["add", "subtract","multiply","divide", "help"]
    
        if userinput in operations:
            
            if userinput == "add":    
                def add():
                    try:
                        numberone = float(input("Please insert the first number you want to add: "))
                        numbertwo = float(input("Please insert the second number you want to add: "))
                        additionresult = numberone + numbertwo 
                        print(additionresult)
                    except ValueError:
                        print("Expected a float value.")
                
                add()
            
            if userinput =="subtract":
                def subtract():
                    try:
                        numberone = float(input("Please insert the first number you want to subtract: "))
                        numbertwo = float(input("Please insert the second number you want to subtract: "))
                        subtractionresult = numberone - numbertwo
                        print(subtractionresult)
                    except ValueError:
                        print("Expected a float value.")
                
                subtract()
            
            if userinput =="multiply":
                def multiplication():
                    try:
                        numberone = float(input("Please insert the first number you want to multiply: "))
                        numbertwo = float(input("Please insert the second number you want to multiply: "))
                        multiplicationresult = numberone * numbertwo
                        print(multiplicationresult)
                    except ValueError:
                        print("Expected a float value.")
                
                multiplication()
            
            if userinput =="divide":
                def division():
                    try:
                        numberone = float(input("Please insert the first number you want to divide: "))
                        numbertwo = float(input("Please insert the second number you want to divide: "))
                        divisionresult = numberone / numbertwo
                        print(divisionresult)
                    except ZeroDivisionError:
                        print("You divided by zero silly.")
                    except ValueError:
                        print("Expected a float value.")
            
                division()
            
            if userinput == "help":
                def help():
                 
                    print("""
                        Syntax for Calculator:
                        add
                        subtract
                        multiply 
                        divide
                        ~When entering an operator you will be prompted with numerical input.
                        """)
                    
                help()
        
        else:
            print("Invalid Operation")
    
    
    titlecard()
    calculations()
calculator()