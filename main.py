class Person:
  age = 12
  height = 159.2
  isMail = True
  name = 'Hlieb'

  def __init__(self, name, age):
    self.name = name
    self.age = age


me = Person()
friend = Person()

print(me.age)
print(me.height)
print(me.name)
print(me.isMail)
friend.name = 'Anny'
print(friend.name)
