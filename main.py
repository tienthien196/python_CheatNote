import numpy as np
import pandas as pds
class people():

    height  = 190
    width = 80
    def  __init__(self, name, age):
        self.name = name
        self.age = age
    
    def cancought(self):
        print(f"hello {self}")



class tienthien(people):
    def __init__(self, name, age):
        super().__init__(name, age)
if __name__ == "__main__":
    p1 = people("Nguyen Van A", 20)
    p2 = people("Nguyen Van B", 30)
    print(p1.cancought)

