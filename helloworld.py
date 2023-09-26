# oliver long 26/09/23

for x in range(10):
    print("hello world")

class test:
    def __init__(self,test):
        self.test = test
    
    def display(self):
        return self.test
    
a = test("aa")

print(a.display())