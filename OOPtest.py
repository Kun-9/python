class User :
    
    userCount = 0
    def __init__(self, name, pw, email):
        self.name = name
        self.pw = pw
        self.email = email
        User.userCount+=1
    
    def checkPw(self, pw) :
        if self.pw == pw :
            print("pass")
        else :
            print("fail")
    
    def printAll(self) :
        print(self.pw, self.name, self. email)
        
    def __str__(self) :
        return "hello"
    
    @classmethod
    def check_user_count(cls) :
        return cls.userCount
    
    @staticmethod
    def static_method(param1, param2):
        return param1+param2



class newClass:
    def __init__(self, name, pw):
        self.name = name
        self._pw = pw
    
    @property
    def pwr(self):
        return "can not display"
    
    @pwr.setter
    def pw(self, new_password):
        self._pw = new_password

# cl = newClass("이름", "1111")
cl = newClass("name", 1112)
cl.pw = 1111
print(cl.pw)
