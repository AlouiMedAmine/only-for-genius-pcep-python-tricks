try:
     first_prompt  =  input("Enter the first value :  ")
     a =  len(first_prompt)
     second_prompt = input("Enter the second value : ")
     b = len(second_prompt) * 2
     print(a/b)

except ZeroDivisionError:
     print("Do not divide by zero ! ")

except ValueError:
     print("Wrong value.")

except:
    print("Error.Error.Error.")