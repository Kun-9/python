class Person:
    def __init__(self, name):
        self.name = name
    
    def say_hello(self, to_name):
        print("안녕" , self.name," 나는",to_name)
        
    def introduce(self):
        print("hell")
        
class Police(Person):    
    def arrest(self, to_arrest):
        print(to_arrest + "를 체포한다")
        
class Programmer(Person):        
    def programming(self, to_program):
        print(to_program + "을 프로그래밍한다")
        

    
    