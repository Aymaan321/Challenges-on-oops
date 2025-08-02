class QWERTY():
    def __init__(self, a):
        self.a = a
    def __lt__(self, other):
        if self.a < other.a:
            return "Obj1 is less than Obj2"
        else: 
            return "Obj2 is less than Obj1"
    def __eq__(self, other):
        if self.a == other.a:
            return "Obj1 and Obj2 have the same value"

obj1 =  QWERTY(2)
obj2 = QWERTY(3)

print(f"Passed values: {obj1.a}, {obj2.a}")
print(obj1 < obj2)

obj3 = QWERTY(4)
obj4 = QWERTY(4)

print(f"Passed values: {obj3.a}, {obj4.a}")
print(obj3 == obj4)
