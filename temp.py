class Source:
    
    def __init__(self, name,  isLiquid):
        self.name = name    # 멤버
        # self.cartridge_number = cartridge_number
        self.isLiquid = isLiquid
        
    def show_info(self):
        return ("이름 : " , self.name , ", 액체 여부 : ", self.isLiquid )
    
    def getName(self):
        return self.name
        
    def setName(self, name):
        self.name = name
    
        
class SourceList :
    def __init__(self):
        self.source_list = []
        self.current_source_list = [6]
        # self.current_source_exist = [0,0,0,0,0,0]
        
    def addSource(self, name, isLiquid):
        self.source_list.append(Source(name, isLiquid))
    
    def register_current_source(self, number, source_num):
        if number < 1 or number > 6 :
            print("1 ~ 6까지의 번호만 입력해주세요.")
        else :
            temp = self.source_list.pop(source_num)
            self.current_source_list.insert(number-1, temp)
            # self.current_source_exist[source_num] = 1
    
    def delet_current_source(self, number):
        self.current_source_list.pop(number-1)
        # self.current_source_exist[number] = 0
    
    def getSourceList(self):
        return self.source_list
    
    def getCurrentSourceList(self):
        return self.current_source_list
