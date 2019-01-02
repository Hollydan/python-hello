
"""
class Robot:

    population = 0

    def __init__(self, name):
        self.name = name
        print('(initializing {})'.format(self.name))
        Robot.population += 1

    def die(self):
        print('{} is being destroyed'.format(self.name))
        Robot.population -= 1

        if Robot.population == 0:
            print('{} was the last one '.format(self.name))
        else:
            print('there are still {:d} robots'.format(Robot.population))

    def say_hi(self):
        print('hi,my name is ', self.name)

    @classmethod
    def how_many(cls):
        print('we have {:d} robots'.format(cls.population))

king = Robot('king')
king.say_hi()
Robot.how_many()

water = Robot('water')
water.say_hi()
Robot.how_many()

king.die()
water.die()
Robot.how_many()
"""

class SchoolMember:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def tell(self):
        print('Name: {}, Age: {}, '.format(self.name, self.age), end='')

class Teacher(SchoolMember):

    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary

    def tell(self):
        SchoolMember.tell(self)
        print('Salary: {:d}'.format(self.salary))

class Student(SchoolMember):
    
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks

    def tell(self):
        SchoolMember.tell(self)
        print('Marks: {}'.format(self.marks))


t = Teacher('Mrs', 32, 7000)
s = Student('Ren', 23, 98)

members= [t, s]

for member in members:
    member.tell()

'''t.tell()
s.tell()'''








