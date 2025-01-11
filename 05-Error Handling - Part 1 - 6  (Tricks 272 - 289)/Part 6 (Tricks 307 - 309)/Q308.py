try:
   raise Exception
except BaseException:
   print("1")
except Exception:
   print("2")
except:
   print("3")