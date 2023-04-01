class Person:
  age = 12
  height = 159.2
  isMail = True
  name = 'Hlieb'

  def __init__(self, name, age, height):
    self.name = name
    self.age = age
    self.height = height

me = Person('Hlieb', 12, 170)
friend = Person('Anny', 30, 170)

print(me.age)
print(me.height)
print(me.name)
print(me.isMail)
friend.name = 'Anny'
print(friend.name)
print(friend.name)
print(friend.age)
print(friend.height)
