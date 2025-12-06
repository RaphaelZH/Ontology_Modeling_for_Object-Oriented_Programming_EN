class A1:
    def __init__(self):
        self.a1 = ""
    
    def get_a1(self):
        return self.a1
    
    def set_a1(self, value):
        self.a1 = value
        
d = A1()
d.set_a1("Hello")
print(d.get_a1())
