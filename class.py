class Car:
    def __init__(self, name, color):
        self.name = name    # 멤버
        self.color = color
        
    def show_info(self):
        print("이름 : " , self.name , " 색 : ", self.color)
        
    def setName(self, name):
        self.name = name
        
    def __del__(self):
        print("인스턴스 소멸")
    


class Unit:
    def __init__(self, name, power):
        self.name = name
        self.power = power
        
    def attack(self):
        self.atkMsg = str(self.name) + "이(가) 공격, 전투력 " + str(self.power)
        print(self.atkMsg)
    
    
    
class Monster(Unit):
    def __init__(self, name, power, type):
        self.name = name
        self.power = power
        self.type = type
        
    def show_info(self):
        print("몬스터 이름", self.name)
        
    def attack(self):
        return super().attack()
        

    
monster = Monster("슬라임", 10, "초급")
monster.show_info()
monster.attack()


