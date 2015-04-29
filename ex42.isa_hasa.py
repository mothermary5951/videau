class Animal(object):  #  Make a class named Animal that contains 'self' as object
    pass               #  Store the class for now

class Dog(Animal):    # Make a class named Dog that is-a Animal
    def __init__(self, name):  ## class Dog has-a initialization consructor that takes self and name paramaters
        self.name = name  #  from class Animal object 'self' get the name attribute and set it to 'name' variable

class Cat(Animal):  # Make a class Cat that is-a Animal
    def __init__(self, name):  ## class Cat has-a initialization that takes self and name parameters
        self.name = name    #  see 'self.name' above

class Person(object):   # Make a class Person that contains 'self' as object
    def __init__(self, name):  # class Person has-a initialization that takes self and name parameters
        self.name =  name   # from class Person 'self' object get the name attribute and set it to 'name' variable
        self.pet = None  # from class Animal object 'self' get the pet attribute and set it to 'None' variable

class Employee(Person):  # Make a class Employee that is-a Person
    def __init__(self, name, salary):  # class Employee has-a initialization that takes parameters self, name, salary
    
        super(Employee, self).__init__(name)  # from instance 'super' of class Employee & of object self get 
                                              # the __init__ function and call it with parameter self and name
        self.salary = salary  # from self get the salary attribute and set it to 'salary' variable

class Fish(object):  # Make a class Fish that contains self as object
    pass

class Salmon(Fish):  # Make a class Salmon that is-a Fish
    pass

class Halibut(Fish):  # MAke a class Halibut that is-a Fish
    pass

rover = Dog("Rover")  # Set "rover" to an instance of class Dog that takes parameters self and name
satan = Cat("Satan")  # Set 'satan' to an instance of class Cat that takes parameters self and name
mary = Person("Mary")  # Set 'mary' to an instance of class Person that takes parameters self and name
mary.pet = satan  # from instance 'mary' in class Person get the pet attribute and set it to 'satan'
frank = Employee("Frank", 120000) # set 'frank' to an instance of class Employee that takes parameters self and name, salary
frank.pet = rover  # from instance 'frank'in class Person get the pet attribute and set it to 'rover'
flipper = Fish()   # set flipper to an instance of class Fish
crouse = Salmon()  # set crouse to an instance of class Salmon
harry = Halibut()   # set harry to an instance of class Halibut
