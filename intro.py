class Employee:
    org = 'HDW'
    def __init__(self,name,age,team):
        self.name = name
        self.age = age
        self.team = team
class DB(Employee):
    team = 'Database'
    def __init__(self, name, age):
        super().__init__(name, age,self.team)
class Web(Employee):
    team = 'Web'
    def __init__(self, name, age):
        super().__init__(name, age,self.team)
    def about_yourself(self):
        return f"I am {self.name} and I am {self.age} years old. I am part of the {self.team} at {self.org}"
    def __repr__(self):
        return f'Web(' + self.name + ',' +str(self.age) + ',' +self.team + ')'
class Core(Employee):
    team = 'Core Development'
    def __init__(self, name, age):
        super().__init__(name, age,self.team)

class HR(Employee):
    team = 'Human Resources'
    def __init__(self, name, age):
        super().__init__(name, age,self.team)
        
if __name__ == '__main__':

    ki = DB('Kaushik',22)
    px = Web('Pheonix',23)
    sg = Core('Sage',27)
    br = HR('Brimstone',35)
    
    
    print(px.about_yourself)
