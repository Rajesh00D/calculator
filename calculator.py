class Calculator:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def output(self):
        pass
class add(Calculator):
    def output(self):
        return self.a +self.b
class sub(Calculator):
    def output(self):
        return self.a - self.b
class multiple(Calculator):
    def output(self):
        return self.a * self.b
class divide(Calculator):
    def output(self):
        return self.a / self.b
    
cal = divide(1,3).output()
print(cal)
