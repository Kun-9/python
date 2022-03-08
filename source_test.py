import source_class

s = source_class.SourceList()
'''
s.addSource("쯔유", 1)
s.addSource("간장", 1)
s.addSource("고추장", 1)
s.addSource("물엿", 1)
s.addSource("케찹", 1)
s.addSource("물", 1)
s.addSource("굴소스", 1)
s.addSource("고춧가루", 0)


for a in s.getSourceList():
    a.show_info()

for a in range(6) :
    print(s.current_source_exist[a] , end = " ")
    
s.register_current_source(2, 4)
print()

for a in range(6) :
    print(s.current_source_exist[a] , end = " ")
    
print()

print(s.getCurrentSourceList().pop(1).getName())
'''
s.addSource("간장", 1)
s.register_current_source(1,0)

for a in range(6) :
    print(s.getCurrentSourceList()[a])

newlist = ["a" , "b", "c"]

# newlist.pop(0)

# for a in newlist:
#     print(a)
    

# s.register_current_source(2, 0)

# print()

# s.getCurrentSourceList().pop(1).show_info()

# s.getList().pop(0).show_info()
