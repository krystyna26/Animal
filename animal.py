class Animal(object):
    def __init__(self, name,health):
        self.name = name
        self.health = health

    def walk(self):
        self.health -= 1
        print self.name+"'s health after walk:",self.health
        return self

    def run(self):
        self.health += 5
        print self.name+"'s health after run:", self.health
        return self

    def displayHealth(self):
        print self.name+"'s health level:", self.health
        return self

# Create an instance of the Animal
animal1 = Animal("Azor", 8)
animal1.walk().walk().walk()
animal1.run().run()
animal1.displayHealth()
#----------------------------------------------------------------------
class Dog(Animal): # inherits everything from Animal
    def __init__(self, name, health):
        super(Dog, self).__init__(name, health)
        self.health = 150

    def pet(self):
        self.health += 5
        print self.name+"'s health after pet:", self.health
        return self

d = Dog("Doggy", 0)
d.walk().walk().walk()
d.run().run()
d.pet()
d.displayHealth()
#----------------------------------------------------------------------
class Dragon(Animal): #inherits everything from Animal
    def __init__(self, name, health):
        self.name = name
        self.health = 170

    def fly(self):
        self.health += 10
        print self.name+"'s health after fly:",self.health
        return self

    def displayHealth(self): # here self is an instance of the class Animal?
        super(Dragon, self).displayHealth()
        print "I am a Dragon"

dragon1 = Dragon("Great dragon", 0)
dragon1.fly()
dragon1.displayHealth() # <__main__.Dragon object at 0x10de02c10> --> 
# The output we see here gives you information about what class your object belongs to and where it is stored in memory

cat = Animal("Kitty", 5)
cat.walk()
cat.run()
cat.displayHealth()
# cat.pet() --> 'Animal' object has no attribute 'pet'
# cat.fly() --> AttributeError: 'Animal' object has no attribute 'fly'
d.fly()