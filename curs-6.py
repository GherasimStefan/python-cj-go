print("curs 6 is here")

class Animal(object):
    def __init__(self, age):
        self.years = age
        self.name = None

    def get_age(self):
        return self.years

    def get_name(self):
        return self.name

    def set_age(self, new_age):
        self.years = new_age

    def set_name(self, new_name):
        self.name = new_name

    def __str__(self):
        return "animal: " + str(self.name) + ":" + str(self.years)

class Cat(Animal):
    def speak(self):
        print("miau")

    def __str__(self):
        return  "cat: " + str(self.name) + ":" + str(self.years)


class Person(object):
    pass


class Person(Animal):
    def __init__(self, name, age):
        Animal.__init__(self, age)
        self.set_name(name)
        self.friends  = []

    def get_friends(self):
        return self.friends

    def add_friend(self, friend_name):
        if friend_name not in self.friends
            self.friends.append(friend_name)

    def spek(self):
        print("hello!")

    def age_diff(self, other):
        diff = self.age - other.years
        print(diff), "year difference")

    def __str__(self):
        return "cat: " + str(self.name) + ":" + str(self.years)

#dog = Animal(4)
#print(dog.years)
#dog.years = 5
#dog.new_attribute = "ceva"
#print(dog.new_attribute)
#dog.set_name("Lucky")
#print(dog.get_name())
#print(dog)

dog = Animal(4)
cat = Cat(5)
cat.set_name("Tom")
cat.set_age(8)

print(dog)
print(cat)

p1 = Person("Ion", 30)
p2 = Person("Maria", 25)

print(p1.get_name())
print(p2.get_name())

print(p1)
print(p2)