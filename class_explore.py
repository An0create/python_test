class A:
   def __init__(self, c):
       print("---------Inside class A----------")
       self.c = c
   print("Print inside A.")

   def alpha(self):
       c = self.c + 1
       return c

print(dir(A))
print("Instantiating A..")


class B:
   def __init__(self, a):
       print("---------Inside class B----------")
       self.a = a


   d = 5



print("Instantiating B..")
