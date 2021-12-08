class JSS:
    def __init__(self):
        self.name = input("이름 : ")
    def show(self):
        print(JSS.name)
    def play(self):
        print(JSS.name + "play")

class JSS2(JSS):
    def __init__(self):
        super().__init__()
        self.gender = input("성별 : ")
    def show(self):
        print("이름 {}, 성별 {}".format(self.name, self.gender))

a = JSS2()
a.show()


