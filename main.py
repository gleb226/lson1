import time
class Person:
  age = 12
  height = 159.2
  isMail = True
  money = 0
  name = 'Hlieb'

  def __init__(self, name, age, height):
    self.name = name
    self.age = age
    self.height = height

  def work(self, days):
    while days != 0:
      time.sleep(5)
      self.money += 15
      days -= 1

  def rest(self, days):
    while days != 0:
      time.sleep(5)
      self.money -=10
      days -=1

me = Person('Hlieb', 12, 170)
friend = Person('Anny', 30, 170)

print(me.money)
me.work(5)
print(me.money)
me.rest(2)
print(me.money)

# print(me.age)
# print(me.height)
# print(me.name)
# print(me.isMail)
# friend.name = 'Anny'
# print(friend.name)
# print(friend.name)
# print(friend.age)
# print(friend.height)
