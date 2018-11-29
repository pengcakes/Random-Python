

class Animal:
    def setName(self, name):
         self.name = name

    def getName(self):
    	return self.name


cat = Animal()
cat.setName("Tom")

dog = Animal()
dog.setName("Jerry")



nameC = cat.getName()
nameD = dog.getName()

print(nameC, nameD)