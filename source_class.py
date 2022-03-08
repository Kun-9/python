class Source:
    
    def __init__(self, name,  isLiquid):
        self.name = name    # 멤버
        # self.cartridge_number = cartridge_number
        self.isLiquid = isLiquid
        
    def show_info(self):
        print("이름 : " , self.name , ", 액체 여부 : ", self.isLiquid )
        
    def setName(self, name):
        self.name = name
        
    def getName(self):
        return self.name
        
        
        
class SourceList :
    def __init__(self):
        self.source_list = []
        self.current_source_list = ["", "", "", "", "", "", ""]
        self.current_source_exist = [0,0,0,0,0,0]
        
    def addSource(self, name, isLiquid):
        self.source_list.append(Source(name, isLiquid))
    
    def register_current_source(self, Cartridge_number, source_num):
        if Cartridge_number < 1 or Cartridge_number > 6 :
            print("1 ~ 6까지의 번호만 입력해주세요.")
        else :
            temp = self.source_list[source_num]
            self.current_source_list[Cartridge_number] = temp
            self.current_source_exist[Cartridge_number] = 1
        
    def delet_current_source(self, number):
        self.current_source_list[number] = ""
        self.current_source_exist[number] = 0
    
    
    def getSourceList(self):
        return self.source_list
    
    def getCurrentSourceList(self):
        return self.current_source_list













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
        

    



