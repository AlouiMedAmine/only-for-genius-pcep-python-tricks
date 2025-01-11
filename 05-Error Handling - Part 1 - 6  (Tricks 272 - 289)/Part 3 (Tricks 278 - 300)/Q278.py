try:
     value  =  input("Enter a value :  ")
     print(int(value)/int(value))

except ValueError:
     print("Bad input ... ")

except ZeroDivisionError:
     print("Very bad input ... ")

except TypeError:
     print("Very very bad input ... ")

except:
    print("Booo!")