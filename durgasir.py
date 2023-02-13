
# # Core Python
# # ---------------------------
# # # Python as a Functional Language/Functional Programming # #
# # # Python as a scripting language # #
# # ---------------------------
# # Concepts
# # Language fundamentals
# # Operators
# # Input/Output statements
# # Flow control_labelsStrings
# # Data structures - List, Tuple, Set, Dictionary
# # Function
# # Module
# # Packages


# # # Advanced Python
# # # ----------------
# # # Exceptional handling
# # # Logging module
# # # Assertions
# # # File Handling
# # # OOPS
# # # Regular expressions
# # # Multi threading
# # # PDBC (Python Database connectivity)
# # # Decorators
# # # generators
# # # Intro to Web app development using Django




# # # OOPs
# # # ---------------------------------
# # # 1.Class - group of methods, its a template, its a blueprint, Class will take some memory
# # # 2.Object - Instance of a Class, Objects will take some memory
# # # 3.Reference Variable(Reference variable of the object) && Self variable - (Inside the class,  Value given by PVM, current object variable)
# # # 4.Constructor and Instance Method
# # # 5. 3 types of variables inside class
# # #          --1. Instance variable - (different copies for different objects(self.x))
# # #          --2. Static variables - (Only one copy for all objects in class)
# # #          --3. Local variable -(Inside a particular method)
# # # 6. 3 types of methods inside class
# # #          --1. Instance Method / Object related method - Should be called by Reference variable of the object
# # #          --2. Class Method   / Class level information (@classmethod) - Should be called by Class name
# # #          --3. Static Method /General utility method (@staticmethod) -Can be called either by Reference variable of the object/ or by Class name


# # # -----------------------------------
# # # eg: 1000Floor building construction
# # # Architect --> Plan(Class)--> Based on the plan we can construct N number of Buildings(Objects) in Pune, Bangalore(200 different villas on same plan)
# # # Sony tv design model(Class) --> Multiple TVs(Object) --> Remote(Reference variable) which performs operations on/points to TV(Object)
# # #  class & Object --> One to many relation
# # #  Object & Reference variable --> One to One / One to Many relation(For same object there may be case of multiple reference variables pointing to)

# class student:
#     '''here comes the doc string - this is a demo class'''
#     def __init__(self,rollno,name):  # Defining a constructor method
#         self.rollno = rollno
#         self.name = name
#     def talk(self):        # Defining an instance method
#         print("Hello my name is ", self.name)
#         print("My rollno is ", self.rollno)

# s1 = student(100,'Sridhar')  # Reference varaibale(must required) = Object
# print(s1.name)
# print(s1.rollno)
# s1.talk()
# print(student.__doc__)   # # To print the doc string of the class
# help(student)   # # # To get the complete information about the class
# s2 = student(200,'Sasi')
# s2.talk()
# s3 = student(300,'Pravin')
# s3.talk()

# # ----------------------------------------------------------------------------------------------

# class employee:
#     '''doc string(documentation)'''
#     def __init__(self,eno,ename,esalary,eaddr):   # #__init__(double underscore)  # # constructor method
#         self.eno=eno
#         self.ename=ename
#         self.esalary=esalary
#         self.eaddr=eaddr
#     def info(self):                               # # instance method/
#         print("*"*20)
#         print("Employee Number:",self.eno)
#         print("Employee Name:", self.ename)
#         print("Employee Salary:", self.esalary)
#         print("Employee address:", self.eaddr)
#         print("*"*20)
# e1 = employee(100,"Sridhar",10000,"Hyd")
# print(e1.ename)
# e2 = employee(200,"Sasi",20000,"Chennai")
# e1.info()
# e2.info()

# # # ----------------------------------------------------------------------------------------------
# # # self variable - its a "variable inside class", which always points to current object ( to refer current object whin a class)
# # # Within the python class if you want to refer current object, then "self variable" is used
# # # The first argument for instance method/ constructor method should always be "self"(self is not a predefined word, whatever we use as first argument, python will consider it as a self variable))
# # # PVM(Python Virtual Maching) is responsible for providing the arguments while calling from the object for "self" arguments and we arenot required to provide explicitly
# # # "Self variable" is a refrence variable which is always pointing to current object
# # # We can either declare/ access properties or arguments using "self" variable
# # # By using "self" variable, we can declare instance variables( in constructor method)
# # # By using "self" variable, we can declare instance variables ( in Instance method)
# # # Self is used to differentiate local variable & current object variable
# # #
# # # Variables outside class
# # # within the class we can refer using "self variable"=reference variable, outside the class, we can refer using "reference variable"


# class student:
#     '''Self variable docs'''
#     def __init__(self):        # # __init__ is a constructor  , whenever we are calling a object of a particular class, the constructor in that particular class will execute automatically
#         print(id(self))
# s1=student()
# print(id(s1))   # #if both s1(reference variable outside class) and self(reference variable inside class) is pointing to the same object, then the adress of both has to be same
# s2=student()
# print(id(s2))    # #if both s2 and self are pointing to the same object,


# # # Whenever we are calling an object the "self" constructor will be executed and the arguments are.......
# # # ........assigned with the values of the object used for calling

# # # ---------------------------------------------------------------------------------------
# class student:
#     '''Self variable docs'''
#     def __init__(self):        # # __init__ is a constructor  , whenever we are calling a object of a particular class, the constructor in that particular class will execute automatically
#         print(id(self))
#     def m1(self, x):
#         print("The value is :", x)
# s1=student()
# print(id(s1))   # #if both s1(reference variable outside class) and self(reference variable inside class) is pointing to the same object, then the adress of both has to be same
# s2=student()
# s2.m1(444)
# print(id(s2))    # #if both s2 and self are pointing to the same object,

# # # ---------------------------------------------------------------------------------------


# class employee:
#     '''doc string(documentation)'''
#     def __init__(self,empnumber,empname,empsalary,empaddr):   # #__init__(double underscore)  # # constructor method
#         self.eno=empnumber
#         self.ename=empname
#         self.esalary=empsalary
#         self.eaddr=empaddr
#     def info(self):                               # # instance method/
#         print("*"*20)
#         empnumber1=888
#         print("Employee Number:",self.eno)
#         print("Employee Number:",empnumber1)                # # "Self" is used to differentiate local variable and current object variable
#         print("Employee Name:", self.ename)
#         print("Employee Salary:", self.esalary)
#         print("Employee address:", self.eaddr)
#         print("*"*20)
# e1 = employee(100,"Sridhar",10000,"Hyd")
# print(e1.ename)
# e2 = employee(200,"Sasi",20000,"Chennai")
# e3 = employee(200,20000,"Sasi","Chennai")        # # Dynamically typed programming language( Type of the variable is determined only during runtime )
# e4 = employee(empnumber=200,empsalary=20000,empname="Sasi",empaddr="Chennai")
# e1.info()
# e2.info()
# e3.info()
# e4.info()
# # # ---------------------------------------------------------------------------------------



# # # The first argument for instance method/ constructor method should always be "self"(self is not a predefined word, whatever we use as first argument, python will consider it as a self variable))
# # # Self is an implicit variable which is always provided by PVM
# class employee:
#     '''doc string(documentation)'''
#     def __init__(x,empnumber,empname,empsalary,empaddr):   # #__init__(double underscore)  # # constructor method
#         x.eno=empnumber
#         x.ename=empname
#         x.esalary=empsalary
#         x.eaddr=empaddr
#     def info(y):                               # # instance method/
#         print("*"*20)
#         empnumber1=888
#         print("Employee Number:",y.eno)
#         print("Employee Number:",empnumber1)                # # "y" is used to differentiate local variable and current object variable
#         print("Employee Name:", y.ename)
#         print("Employee Salary:", y.esalary)
#         print("Employee address:", y.eaddr)
#         print("*"*20)
# e1 = employee(100,"Sridhar",10000,"Hyd")
# print(e1.ename)
# e2 = employee(200,"Sasi",20000,"Chennai")
# e3 = employee(200,20000,"Sasi","Chennai")        # # Dynamically typed programming language( Type of the variable is determined only during runtime )
# e4 = employee(empnumber=200,empsalary=20000,empname="Sasi",empaddr="Chennai")
# e1.info()
# e2.info()
# e3.info()
# e4.info()
# # # # ---------------------------------------------------------------------------------------


# # # Constructor:
# ----------------
# # # Constructor is a special method in python
# # # The name should be always : __init__()
# # # Whenever we are creating a object, constructor will be executed automatically and we are not required to call explicitly
# # # The main purpose of the constructor:  is to declare & initialize the instance variables related to that object
# # # For every object, constructor will be executed only once
# # # Constructor must use self argument
# # #Constructor is mandatory for every class( if we dont write any constructor, PVM will provide a default constructor)

# class test:
#     def __init__(self):
#         print("Constructor execution...........")
#         print("No arguments...........")
# s = test()
# x = test()
# y = test()


# # class test:
# #     def __init__(self):
# #         print("Constructor execution...........")          # # This constructor method will not be considered once you put the second constructor method
# #         print("No arguments...........")
# #     def __init__(self,x):
# #         print("Constructor execution...........")
# #         print("One arguments...........")
# # # s = test()
# # x = test(10)
# # y = test(20)
# # # Two methods with the same name but with different arguments = Overloaded constructors, In Python method overloading/ Constructor overloading comcepts are not available
# # # Whenever we are creating the second method the first one will be nomore or overwritten or will not be considered or will consider only the last constructor created
# # # Object creation****** has to be done outside of the class

# class student:
#     def __init__(self, name, rollno):
#         print("Constructor method execution.......To declare and initialize an instance method variable...Can be executed once per object....Constructor method name can be : __init__()")
#         print("Will be executed automatically, if we are creating an object")
#         self.n = name
#         self.r = rollno
#     def display(self):
#         print("Instance method execution......To perform some business logic....Can be executed any number of times for an object.....Instance method name can be anything")
#         print("Will be executed only if we call")
#         print("Hello myself is", self.n)
#         print("My rollno is:", self.r)
# s=student("sridhar",100)
# s.__init__("Sasi",100)
# s.__init__("Sasi",100)
# s.__init__
# s.__init__
# s.display()


# # # Types of variables & Methods
# # # -----------------------------------------------
# # # Only 3 types of variables allowed inside the class:( All the three are public variables(not private variables))
# # # 1. Instance variables / Object level variables (Seperate copy of variables for every object)
# # # 2. Static variables / Class level variables (Only one copy of a variable for all objects)
# # # 3. Local variables / Variable inside the method /method variables

# # # Only 3 types of Methods allowed inside the class:
# # # 1. Instance Method
# # # 2. Class Method
# # # 3. Static Method

# # # Instance variables
# # # ----------------------------------------------
# # # For every student seperate name and seperate roll number
# # # The value of the variable varies from object to Object= Instance variables/Object level variables
# # # Eg: 600 students( 600 names & 600 roll numbers)
# # # Should be declared inside constructor method using self

# class student:
#     '''here comes the doc string - this is a demo class'''
#     def __init__(self,x,y):  # Defining a constructor method (x & y are local variables)
#         self.rollno = x                               # # #  Instance variable (Self.name & self.rollno)
#         self.name = y                                   # # #  Instance variable
#     def talk(self):        # Defining an instance method
#         print("Hello my name is ", self.name)
#         print("My rollno is ", self.rollno)
# s1 = student(100,'Sridhar')
# s2 = student(200,'Sasi')
# s3 = student(300,'Elakkiya')
# s1.talk()
# s2.talk()
# s3.talk()

# # # Static varibles
# # # ----------------------------------------------
# # # Consider all the students are studying with different roll number but in the same school( School can be declared as a static variable)
# # # Class level variables which is common for all the objects

# class student:
#     '''here comes the doc string - this is a demo class'''
#     schoolname = "Durgasoft"
#     def __init__(self,x,y):  # Defining a constructor method (x & y are local variables)
#         self.rollno = x                               # # #  Instance variable
#         self.name = y                                   # # #  Instance variable
#     def talk(self):        # Defining an instance method
#         print("Hello my name is ", self.name)
#         print("My rollno is ", self.rollno)
# s1 = student(100,'Sridhar')
# s2 = student(200,'Sasi')
# s3 = student(300,'Elakkiya')
# s1.talk()
# s2.talk()
# s3.talk()
# print(s1.schoolname)
# print(s2.schoolname)
# print(s3.schoolname)
# print(id(s1.schoolname))
# print(id(s2.schoolname))
# print(id(s3.schoolname))
# print(id(s1.name))
# print(id(s2.name))
# print(id(s3.name))

# # # ----------------------------------------------------------------------------------------------------------------------------------------
# # # Only 3 types of Methods allowed inside the class:
# # # 1. Instance Method / Object related method - Should be called by Reference variable of the object
# # # 2. Class Method   / Class level information (@classmethod) - Should be called by Class name
# # # 3. Static Method /General utility method (@staticmethod) -Can be called either by Reference variable of the object/ or by Class name

# # # 1. Instance Method
# # # ---------------------------------------------------------------------
# # # Inside a method if we are accessing instance variables, then it always related to particular object
# class student:
#     '''here comes the doc string - this is a demo class'''
#     schoolname = "Durgasoft"
#     def __init__(self,x,y):                       # Defining a constructor method (x & y are local variables)
#         self.rollno = x                                     # # #  Instance variable
#         self.name = y                                       # # #  Instance variable
#      # #  # Below is the Instance method(Should have self variable)
#     def talk(self):
#        print("Hello my name is ", self.name)      # Defining an instance method
#        print("My rollno is ", self.rollno)
#         #  # Below is the Instance method(Should have self variable)
#         #  # For every class, to hold class level information, one class object will be created.
#         # # The reference variable for the class object will be maintained by PVM
#     @classmethod                          # Decorator @Classmethod (mandatory) has to be used to show that it is a class method
#     def getSchoolName(cls):                                    #
#         print("College name is ", cls.schoolname)  #cls is not predefined(like self) We can name it in different ways also
#     # # # # @classmethod                          # Decorator @Classmethod (mandatory) has to be used to show that it is a class method
#     # # # # def getSchoolName(x):                                    #
#     # # # #     print("College name is ", x.name)  #cls is not predefined(like self) We can name it in different ways also
#     # # #-------------------------------------------------------------------
#     # # #Static method:
#     # # # No self/cls variable for static method
#     # # # Below method(static method) never talks about object level/ Class level variables. Its just a utility method which is called static method
#     # # # Static method can be called using either reference variable or Class name
#     @staticmethod                            # Decorator @staticmethod (mandatory(optional/not mandatory- if we call using the class name)) has to be used to show that it is a static method. Else this method will be treated as Instance method
#     def findAverage(x,y):
#         print("Average:",(x+y)/2)
# s1 = student(100,'Sridhar')
# s2 = student(200,'Sasi')
# s3 = student(300,'Elakkiya')
# s1.talk()
# s2.talk()
# s3.talk()
# student.getSchoolName()
# s1.findAverage(10,20)
# student.findAverage(10,20)
# # # -------------------------------------------------------------------------------------------------------------------------------------------------
# # # Instance variables
# # #--------------------
# # # If the value of the variables varies from Object to Object
# # # For every object a seperate copy will be created
# # # Where we have to declare instance variables
# # # -------------------------------------------
# # # 1. Inside constructor by using "self"
# # # 2. Inside instance method by using "self"
# # # 3. From outside of the class by using reference variable of the object
# class student:
#     '''here comes the doc string - this is a demo class'''
#     schoolname = "Durgasoft"
#     def __init__(self,x,y):                       # Defining a constructor method (x & y are local variables)
#         self.rollno = x                                     # # #  Instance variable
#         self.name = y
#     def talk(self):
#         self.marks=60                               # # # 2. Inside instance method by using "self"
#         marks=99                                       # # # This line is a local variable
#         print("Hello my name is ", self.name)      # Defining an instance method
#         print("My rollno is ", self.rollno)
#     @classmethod
#     def getSchoolName(cls):
#         print("College name is ", cls.schoolname)
#     @staticmethod
#     def findAverage(x,y):
#         print("Average:",(x+y)/2)
# s1 = student(100,'Sridhar')
# print(s1.__dict__)
# s1.talk()                                          # # # For the current object self.marks is considered a instance variable
# print(s1.__dict__)                                # # # Object related Dictionary
# s1.age=24                                           # # # 3. From outside of the class by using reference variable of the object(in case if age is already mentioned inside the class as self.age, it will be replaced)
# print(s1.__dict__)
# s2 = student(200,'Sasi')
# print(s2.__dict__)
# s2.talk()                                          # # # For the current object self.marks is considered a instance variable
# print(s2.__dict__)                                # # # Object related Dictionary
# s2.age=33                                           # # # 3. From outside of the class by using reference variable of the object(in case if age is already mentioned inside the class as self.age, it will be replaced)
# s2.wife="Sasi"
# print(s2.__dict__)
# s3 = student(300,'Elakkiya')
# s1.talk()
# s2.talk()
# s3.talk()
# student.getSchoolName()
# s1.findAverage(10,20)
# student.findAverage(10,20)
# # #--------------------------------------------------------------------------------------------------

# class test:
#     def __init__(self):
#         self.a=10
#         self.b=20
#         self.c=30
#     def m1(self):
#         self.d=40
#     def m2(self):
#         self.e=50
#         self.f=60
# t1=test()
# t1.m1()
# t2=test()
# t2.m2()
# t2.s=200
# t2.y=300
# print(t1.__dict__)
# print(t2.__dict__)
# # #--------------------------------------------------------------------------------------------------
# # # How to access instance variables
# # #--------------------------------------------------------------------------------------------------
# # # 1. Within the class(in Instance method) by using self
# # # 2. From outside of the class by using object reference (Reference variable of the object)

# class student:
#     '''here comes the doc string - this is a demo class'''
#     schoolname = "Durgasoft"
#     def __init__(self,x,y):
#         self.rollno = x
#         self.name = y
#     def talk(self):
#         print("Hello my name is ", self.name)        # # # 1. Within the class(in Instance method) by using self
#         print("My rollno is ", self.rollno)
# s1 = student(100,'Sridhar')
# s1.talk()
# print(s1.name, s1.rollno)                        # # # 2. From outside of the class by using object reference (Reference variable of the object)

# # #--------------------------------------------------------------------------------------------------
# # # How to delete instance variables
# # #--------------------------------------------------------------------------------------------------
# # # 1. Delete Within the class "del self.variablename"
# # # 2. Delete From outside of the class by using "del objectreference.variablename" (Reference variable of the object)

# class student:
#     '''here comes the doc string - this is a demo class'''
#     schoolname = "Durgasoft"
#     def __init__(self,x,y,xx,yy):
#         self.rollno = x
#         self.name = y
#         self.a=xx
#         self.b=yy
#     def talk(self):
#         del self.b
#         print("Hello my name is ", self.name)        # # # 1. Delete Within the class "del self.variablename"
#         print("My rollno is ", self.rollno)
# s1 = student(100,'Sridhar',10,20)
# print(s1.__dict__)
# s1.talk()
# print(s1.__dict__)
# del s1.a
# print(s1.__dict__)
# # # # The instance variable deleted in one object maynot be deleted in another object, because every object has its own seperate copy of instance variables
# s2 = student(101,'Sasi',30,40)
# print(s2.__dict__)
# s2.talk()
# print(s2.__dict__)
# del s2.name                 # # #  it doesnot just delete the value of the variable. It deletes the variable itself for that particular object
# print("Just Testing", s1.name)                 # # #  s1.name works
# print("Just Testing", s2.name)                 # # #  s2.name willnot work
# print(s2.__dict__)
# s1.a=888
# s1.b=999
# print(s1.a, s1.b)
# print(s2.a)



# # # -------------------------------------------------------------------------------------------------------------------------------------------------
# # # Static variables - For all objects only one copy of the variable is maintained
# # #--------------------
# class student:
#     '''here comes the doc string - this is a demo class'''
#     schoolname = "Durgasoft"
#     def __init__(self,x,y):
#         self.rollno = x
#         self.name = y
#     def talk(self):
#         self.marks=60
#         marks=99
#         print("Hello my name is ", self.name)
#         print("My rollno is ", self.rollno)
#     @classmethod
#     def getSchoolName(cls):
#         print("College name is ", cls.schoolname)
#     @staticmethod
#     def findAverage(x,y):
#         print("Average:",(x+y)/2)
# s1 = student(100,'Sridhar')
# print(s1.name,s1.rollno,student.schoolname)
# s2 = student(101,'Sasi')
# print(s2.name,s2.rollno,student.schoolname)
# print(s1.__dict__)       # # #This will not show the Static/Class variable
# print(s2.__dict__)       # # #This will not show the Static/Class variable

# # # If 900(Mechanical)/1000 students having same value and If 100(Civil)/1000 students having another set of same values - In this case only Instance variables can be used/Static variable cannot be used
# # # ---------------------------------------------------------------------------------------------------------------------------
# # #  What are the various places to declare static variables?
# # # -------------------------------------------------------------
# # # 1. Within the class(outside the methods) directly
# # # 2. Inside Constructor method by using classname
# # # 3. Inside Instance method by using classname
# # # 4. Inside Classmethod by using classname or cls variable
# # # 5. Inside Static method by using classname
# # # 6. From outside of class by using classname
# class Test:
#     a=10
#     def __init__(self):
#         self.aa=1
#         Test.v=10
#     def m1(self):
#         Test.b=20
#     @classmethod
#     def m2(cls):
#         cls.c=111
#         Test.d=2123
#     @staticmethod
#     def m3(self):
#         Test.f=2342
# Test.g=1212
# t1 = Test()
# t1.m2()
# print(t1.__dict__)
# print(Test.__dict__)
# # # # What are the static variables in the above program?2(a & g) only
# t1=Test()
# print(Test.__dict__)
# t1.m1()                                 # # # t1.m1()..self not considers & Test.m1(1)..self is considered as a variable --> No error
# print(Test.__dict__)                    # # # t1.m1() ..cls not considers & Test.m1()..cls is not considered as a variable --> No error
# Test.m2(1)
# print(Test.__dict__)
# t1.m3(1)
# print(Test.__dict__)

# # # ---------------------------------------------------------------------------------------------------------------------------
# # #  How to access static variables?
# # # We can access static variables either by classname or by object reference
# # # -------------------------------------------------------------
# # # 1. Within the class we can access by using------ classname,self,cls
# # # 2. But inside class method, we can "also" use cls variable
# # # 3. From outside of class by only using -------------classname(Recomended), Objectreference
# class Test:
#     a=10
#     def __init__(self):
#         print("Inside constructor method...")
#         print(Test.a)
#         print(self.a)
#     def m1(self):
#         print("Inside Instance method...")
#         print(Test.a)
#         print(self.a)
#     @classmethod
#     def m2(cls):
#         print("Inside Class method...")
#         print(Test.a)
#         print(cls.a)
#     @staticmethod
#     def m3():
#         print("Inside Static method...")
#         print(Test.a)
# t=Test()
# t.m1()
# t.m2()
# t.m3()
# print("From outside of the class", Test.a, t.a)

# # # # ---------------------------------------------------------------------------------------------------------------------------
# class Test:
#     a=10
#     def __init__(self):
#         print("Inside constructor method...")
#         print(Test.a)
#         print(self.a)
#     def m1(self,b):
#         self.x=b
#         print("Inside Instance method...")
#         print(Test.a)
#         print(self.x)
#     @classmethod
#     def m2(cls):
#         print("Inside Class method...")
#         print(Test.a)
#         print(cls.a)
#     @staticmethod
#     def m3():
#         print("Inside Static method...")
#         print(Test.a)
# t=Test()
# t.m1(6)
# t.m2()
# t.m3()
# print("From outside of the class", Test.a, t.a)

# # # ----------------------------------------------------------------------------------------
# # #  How to modify static variables?
# # # Within the class we should use ----classname, cls
# # # Outside of the class --------------only classname    (Self is not applicable for static variable)

# class Test:
#     a=10
#     def __init__(self):
#         self.a=20
# t=Test()
# print(Test.a)
# print(t.a)
# # # # # ---------------------------------------------------------------------------------------------------------------------------
# class Test:
#     a=10
#     def __init__(self):
#         Test.a=20
# t=Test()
# print(Test.a)
# print(t.a)
# # # # ---------------------------------------------------------------------------------------------------------------------------
# class Test:
#     a=10
#     def __init__(self):
#         self.a=333
#         print("Inside constructor method...")
#         print(Test.a)
#         print(self.a)
#     def m1(self):
#         print("Inside Instance method...")
#         print(Test.a)
#         print(self.a)
#     @classmethod
#     def m2(cls):
#         cls.a=30
#         Test.a=40
#         print("Inside Class method...")
#         print(Test.a)
#         print(cls.a)                            # # # # printing 40
#     @staticmethod
#     def m3():
#         Test.a=55
#         print("Inside Static method...")
#         print(Test.a)
# t=Test()
# t.m1()
# t.m3()
# t.m2()
# Test.a = 77
# print("From outside of the class", Test.a, t.a)    # # # # printing 77 333

# # # ---------------------------------------------------------------------------------------------------------------------------
# # #  How to delete static variables?
# # # Within the class we should use ----classname, cls
# # # Outside of the class --------------only classname    (Self is not applicable for static variable)

# class Test:
#     a=10
#     def __init__(self):
#         self.a=20
#         del Test.a
# t=Test()
# print(Test.__dict__)
# Test.a = 33
# print(Test.__dict__)
# print(Test.a)
# print(t.a)

# # # ---------------------------------------------------------------------------------------------------------------------------
# class Test:
#     x=10
#     def __init__(self):
#         self.y=20
# t1=Test()
# t2=Test()
# t1.x = 888
# t1.y = 999
# print(t1.x, t1.y)
# print(t2.x, t2.y)
# # # ---------------------------------------------------------------------------------------------------------------------------
# class Test:
#     x=10
#     def m1(self):
#         self.y=20
# t1=Test()
# t2=Test()
# t1.x = 888
# t1.y = 999
# print(t1.x, t1.y)
# print(t2.x, t2.y)   # # We will get the error as the instance method is not called and attribute "y" is not defined outside class
# # # -------------------------------------------------------------------------------------------------
# class Test:
#     x=10
#     def __init__(self):
#         self.y=20
# t1=Test()
# t2=Test()
# Test.x = 888
# t1.y = 999
# print(t1.x, t1.y)
# print(t2.x, t2.y)
# # # -----------------------------------------------------------------------------------------------
# # # *******************Its always recommended to use ObjectReference for Instance variables & to use ClassName for Static/Class Variables*****************************
# # # -----------------------------------------------------------------------------------------------

# # # Local variables
# # # ----------------------------------------------------------------------------------------------
# # # To meet the temporary requirements of a Programmer
# # # We shouldnot use self,cls
# # # Local variables Cannot access outside the method( where the local variable is declared)
# class Test:
#     def m1(self):
#         a=100
#         c=234
#         print(a)
#         print(c)
#     def m2(self):
#         b=200
#         c=432
#         print(b)
#         print(c)
#         # print(a)
# t=Test()
# t.m1()
# t.m2()
# # # ----------------------------------------------------------------------------------------------
# class Test:
#     def average(self,list):
#         result=sum(list)/len(list)                # #result(a temporary/local variable) to hold the value temporarily for a particular object
#         print("The Average value is:", result)
# t=Test()
# t.average([10,20,30,40,60])
# # # ----------------------------------------------------------------------------------------------
# # # # ----------------------------------------------------------------------------------------------
# class Test:
#     @staticmethod
#     def average(list):
#         result=sum(list)/len(list)                # #result(a temporary/local variable) to hold the value temporarily for a particular object
#         print("The Average value is:", result)
# Test.average([10,20,30,40,60])
# # # ----------------------------------------------------------------------------------------------
# # # Global variables can be used inside the class also
# x=100         # # # x=100 is a global variable since it is declared outside the class
# class Test:
#     def m1(self):
#         print(x)
#     def m2(self):
#         print(x)
# t=Test()
# t.m1()
# t.m2()
# # # ----------------------------------------------------------------------------------------------
# x=100         # # # x=100 is a global variable since it is declared outside the class,
# print(x)
# class Test:
#     print(x)
#     def m1(self):
#         global x   # # # Value of global variable can be changed inside the class,
#         x=888
#         print(x)
#     def m2(self):
#         print(x)
# t=Test()
# t.m1()
# t.m2()
# print(x)
# # # # ----------------------------------------------------------------------------------------------
# # # Is it possible to declare global keyword inside a method? Yes (by using global keyword)
# # # From the class, can we access global variable directly.
# # # # ----------------------------------------------------------------------------------------------
# # # # ----------------------------------------------------------------------------------------------
# # # # Bank Application
# # # # ----------------------------------------------------------------------------------------------
# # # # ----Bank name, Customername, Bank balance, zero balance account, deposit operation, withdrawal operation
# # # # ----------------------------------------------------------------------------------------------
# class customer:
#     '''Customer class with bank related operations'''
#     bankname="Srisha Bank"
#     def __init__(self, customername, balance=0):
#         self.cname=customername
#         self.bal=balance
#     def deposit(self,amount):
#         self.bal=self.bal+amount
#         print("After deposit, of {amount}, the balance is :",self.bal)
#     def withdraw(self,amount):
#         if amount > self.bal:
#             print("Insufficinet funds, cannot perform this operation")
#             sys.exit()                  # # # PVM will stop( but we have to import the module )
#         else
#             self.bal=self.bal-amount
#             print("After withdrawal, of {amount}, the balance is :",self.bal)

# print("Welcome to {customer.bankname}")
# name=input("Enter your name:")
# c=customer(customername)
# While True:
#     print("Welcome {c}")
#     print("d-Deposit\nw-Withdraw\ne-Exit")
#     option=input("Choose your option:")
#         amount=float(input("Enter the amount  to deposit:"))
#         c.deposit(amount)
#         amount=float(input("Enter the amount to withdraw:"))
#         c.withdraw(amount)
#         print("Thanks for banking with us")
#         sys.exit()
#     else:
#         print("Choose a valid option")


# # # # Bank Application
# # # # ----------------------------------------------------------------------------------------------
# # # # ----Bank name, Customername, Bank balance, zero balance account, deposit operation, withdrawal operation
# # # # ----------------------------------------------------------------------------------------------
# import sys
# class customer:
#     '''Customer class with bank related operations'''
#     bankname="Srisha Bank"
#     def __init__(self, customername, balance=0):
#         self.cname=customername
#         self.bal=balance
#     def deposit(self,amount):
#         self.bal=self.bal+amount
#         print("After deposit, of "+str(amount) +" the balance is :",self.bal)
#     def withdraw(self,amount):
#         if amount > self.bal:
#             print("Insufficinet funds, cannot perform this operation")
#             sys.exit()                  # # # PVM will stop( but we have to import the module )
#         self.bal=self.bal-amount
#         print("After withdrawal, of "+str(amount) +" the balance is :",self.bal)
# print("Welcome to",customer.bankname)
# name=input("Enter your name:")
# c=customer(name)
# while True:
#     print("Welcome",name)
#     print("d-Deposit\nw-Withdraw\ne-Exit")
#     option=input("Choose your option:")
#     if option.lower()=="d":
#         amount=float(input("Enter the amount  to deposit:"))
#         c.deposit(amount)
#     elif option.lower()=="w":
#         amount=float(input("Enter the amount to withdraw:"))
#         c.withdraw(amount)
#     elif option.lower()=="e":
#         print("Thanks for banking with us")
#         sys.exit()
#     else:
#         print("Choose a valid option")

# # # # Bank Application
# # # # ----------------------------------------------------------------------------------------------
# # # # ----Bank name, Customername, Bank balance, zero balance account, deposit operation, withdrawal operation
# # # # ----------------------------------------------------------------------------------------------
# import sys
# class customer:
#     '''Customer class with bank related operations'''
#     bankname="Srisha Bank"
#     def __init__(self, customername, balance=0):
#         self.cname=customername
#         self.bal=balance
#     def deposit(self,amount):
#         self.bal=self.bal+amount
#         print("After deposit, of "+str(amount) +" the balance is :",self.bal)
#     def withdraw(self,amount):
#         if amount > self.bal:
#             print("Insufficinet funds, cannot perform this operation")
#             sys.exit()                  # # # PVM will stop( but we have to import the module )
#         elif
#             self.bal=self.bal-amount
#             print("After withdrawal, of "+str(amount) +" the balance is :",self.bal)
# print("Welcome to",customer.bankname)
# name=input("Enter your name:")
# c=customer(name)
# while True:
#     print("Welcome",name)
#     print("d-Deposit\nw-Withdraw\ne-Exit")
#     option=input("Choose your option:")
#     if option=="d" or option=="D":
#         amount=float(input("Enter the amount  to deposit:"))
#         c.deposit(amount)
#     elif option=="w" or option=="W":
#         amount=float(input("Enter the amount to withdraw:"))
#         c.withdraw(amount)
#     elif option=="e" or option=="E":
#         print("Thanks for banking with us")
#         sys.exit()
#     else:
#         print("Choose a valid option")

# # # # ----------------------------------------------------------------------------------------------
# # # # ----------------------------------------------------------------------------------------------
# # # # ----------------------------------------------------------------------------------------------
# # 3 Types of methods
# # # # ----------------------------------------------------------------------------------------------
# # 1. Instance method
# # 2. Class method
# # 3. Static method
# # When we have to use which method?
# # # # ----------------------------------------------------------------------------------------------
# # # Thumb rule
# # # # ---------
# # # 1. If we are using atleast one instance variable(inside method body) (Always related to particular object only)- Instance method
# # # # ---------def m1(self):  # # In bank application, deposit is instance method because balance is instance variable
# # # # ---------self.x
# # # # ---------s1=student(name, marks) --Time taking work using setter and getter method
# # # # ---------s1.x                    --Object creation= time taking operation

# # # 2. If we are using only static variables but not instance variable (Nowhere related to particular object)- Class method
# # #-----Inside method body, if we are accesing only class level data, then what is the need of declaring an instance method
# # # # ---------@classmethod
# # # # ---------def m1(cls):
# # # # ---------cls.x
# # # # ---------no need to create the the object. Just by using class name, we can call the method
# # # # ---------student.m1()

# # # 3. If we are not using any instance or  static variables - Static method /General utility method
# # # # ---------@staticmethod
# # # # ---------def add():
# # # # ---------x=y=8
# # # # ---------print(x*y)


# # # 1. Instance method
# # # ----------------------------------------------------------------------------------------------
# class student:
#     '''here comes the doc string - this is a demo class'''
#     def __init__(self,name,marks):
#         self.marks = marks
#         self.name = name
#     def display(self):                           # Defining an instance method
#         print("Hello ", self.name)                  # Instance variable used in this line, so choose instance method
#         print("Your mark is ", self.marks)
#     def grade(self):                           # Defining an instance method
#         if self.marks >= 60:
#             print("First grade")
#         elif self.marks >= 50:
#             print("Second grade")
#         elif self.marks >= 35:
#             print("Third grade")
#         else:
#             print("You are failed")
# n = int(input ("Enter number of students:"))   # # # The return type of input is always string
# for i in range(n):                             # # use for loop if you know the number of iterations already, if not use while loop + count
#     name = input("Enter student name:")
#     marks= int(input ("Enter marks: "))     # # The return type of input is always string
#     s= student(name,marks)
#     s.display()
#     s.grade()
#     print("*"*20)

# # # ----------------------------------------------------------------------------------------------
# # # Setter & Getter Methods: ---# # # Industry standards
# # # ----------------------------------------------------------------------------------------------
# # # For update operations(we shouldnot directly go and edit the main value).
# # # & Security purposes &
# # # When object wants to travel from oneplace to another place
# # # These are not builtin methods
# # # Setter method - to set the data to the object , (alternative to constructor method)
# # # Getter method - to get the data from the object, (alternative to constructor method)
## #  Hiding data behind methods = Encapsulation(security reasons)--Drawback(length of the code more, readability less, minor performance effect(slows down execution) is also there)
# # # if the variable is "age", then compulsory the name of the method should be "setAge(self,age)" -Industry standard terminology
# # # age (recommended)
# # # def setAge(self,age):
# # #       self.age = age
# # # ----------------------------------------------------------------------------------------------
# # #age (Not recommended)
# # # def setAge(self,x):
# # #       self.age = x
# # #
# # # ----------------------------------------------------------------------------------------------
#     def __init__(self,name,marks):                  # Defining a constructor method
#         self.marks = marks
#         self.name = name
# s= student(name,marks)
# # # Constructor basic purpose is initialisation(not for validation(but its possible to validate in constructor method))
# # # ----------------------------------------------------------------------------------------------
# #     def __init__(self,name,marks):                  # Defining a constructor method
# #         self.marks = marks
# #         self.name = name
# # s= student()
# # s.setName("Sridhar")
# # s.setMarks(100)
# # print("student name:",s.getName())
# # # ----------------------------------------------------------------------------------------------
# # # Syntax: Setter method
# # # ------------------------------------------------
        # def setVariableName(self, variableName):
        #     self.variableName=variableName
# # # -------------------------------------------------
        # def setMarks(self, marks):
        #     self.marks=marks
# # # ------------------------------------------------
        # def getMarks(self):
        #     return self.marks
# # # ----------------------------------------------------------------------------------------------
# # # If 2 instance variables are there, then (2 setter methods & 2 getter methods are required )
# # # Always the number of setter methods = the number of getter methods
# # # Always Get & set will come with individual variables
# # # ----------------------------------------------------------------------------------------------

# class student:                               # # # Python will automatically generate the constructor as we are not providing the constructor
#     def setName(self, name):                  # # # The getter and setter methods created here are instance methods related to student objects
#         self.name=name
#     def getName(self):
#         return self.name
#     def setMarks(self, marks):
#         self.marks=marks
#     def getMarks(self):
#         return self.marks

# n = int(input ("Enter number of students:"))   # # # The return type of input is always string
# for i in range(n):                             # # use for loop if you know the number of iterations already, if not use while loop + count
#     name = input("Enter student name:")
#     marks= int(input ("Enter marks: "))     # # The return type of input is always string
#     s= student()                       # # #****************************************************************
#     s.setName(name)
#     s.setMarks(marks)
#     print("hi",s.getName())
#     print("Your marks are: ",s.getMarks())
#     print("*"*20)
# print(s.name)                   # # #Both the statements are same (here, no validation - direct access)
# print(s.getName())               # # #Both the statements are same (here, validation - like authentication)

# # # ----------------------------------------------------------------------------------------------
# # # Instance method vs Class method:
# # # ----------------------------------------------------------------------------------------------
# # # Calling instance method: (Time taking/Costly operation)
# # # 1. create object
# # # 2. call using the object reference
# # # # # # self--> Reference variable to currect object --> used to access instance variables
# # # # # # Inside instance method, we can access both instance variables and static variables
# # #
# # # Calling Class method:
# # # 1. call directly using classname(recommended) or by using object reference
# # # # # # cls --> Reference variable to current class object--> used to access static variables
# # # # # # But Inside class method, we can access only static variables (not instance variables)
# # # ----------------------------------------------------------------------------------------------
# # # @classmethod
# # # def m1(cls):
# # #         print(cls.collegename)
# # #         print(cls.bankname)

# # # # ----------------------------------------------------------------------------------------------
# # 3 Types of methods
# # # # ----------------------------------------------------------------------------------------------
# # 1. Instance method
# # 2. Class method
# # 3. Static method
# # When we have to use which method?
# # # # ----------------------------------------------------------------------------------------------
# # # Thumb rule
# # # # ---------
# # # 1. If we are using atleast one instance variable(inside method body) (Always related to particular object only)- Instance method
# # # # ---------def m1(self):  # # In bank application, deposit is instance method because balance is instance variable
# # # # ---------self.x
# # # # ---------s1=student(name, marks) --Time taking work using setter and getter method
# # # # ---------s1.x                    --Object creation= time taking operation

# # # 2. If we are using only static variables but not instance variable (Nowhere related to particular object)- Class method
# # #-----Inside method body, if we are accesing only class level data, then what is the need of declaring an instance method
# # # # ---------@classmethod
# # # # ---------def m1(cls):
# # # # ---------cls.x
# # # # ---------no need to create the the object. Just by using class name, we can call the method
# # # # ---------student.m1()

# # # 3. If we are not using any instance or  static variables - Static method /General utility method
# # # # ---------@staticmethod
# # # # ---------def add():
# # # # ---------x=y=8
# # # # ---------print(x*y)
# # # # ----------------------------------------------------------------------------------------------
# # # class method works if only ( there is no object and all local variables use the same static variable
# # # Static variables - common for all objects. Legs=4(common copy for all objects) common for all animals( but sound is not common for all animals= instance variable(Instance method))
# class animal:
#         legs=4
#         @classmethod
#         def walk(cls,name):
#                 print("{} walks with {} legs".format(name, animal.legs))
# animal.walk("lion")
# animal.walk("tiger")
# animal.walk("cat")
# # # # ----------------------------------------------------------------------------------------------
# # # Write a program to track number of objects for a class
# class test:
#         count = 0
#         def __init__(self):

#                 test.count = test.count + 1
#         @classmethod
#         def noofobjects(cls):
#                 print("No of objects created for class:", test.count)
# t1=test()
# t2=test()
# t3=test()
# t4=test()
# t5=test()
# test.noofobjects()
# # # # ----------------------------------------------------------------------------------------------
# # # complicated example:
# # # # ----------------------------------------------------------------------------------------------
# class test:
#         def m1(cls, self):                                 # # # # cls is self variable, self is local variable here
#                 cls.x =10
#                 print("This is instance method:",cls.x, self)
# t=test()
# t.m1("Sridhar")
# # # # ----------------------------------------------------------------------------------------------
# class test:
#         def m1(self, name):                                 # # # # cls is self variable, self is local variable here
#                 self.x =10
#                 print("This is instance method:",self.x, name)
# t=test()
# t.m1("Sridhar")
# # # # ----------------------------------------------------------------------------------------------
# # # Static method:
# # # # ----------------------------------------------------------------------------------------------
# # # 1. static method nowhere related to static variables
# # # 2. when you are not using any instance variables or static variables
# # # 3. Just general utility method/ helper method
# # # 4. Calling static method/ helper method:

# class test:
#         @staticmethod
#         def sum(x,y):
#                 print("The sum is:", x+y)
# test.sum(10,15)
# test.sum(10,16)
# # # # ----------------------------------------------------------------------------------------------
# class test:
#         @staticmethod
#         def sum(x,y):
#                 print("The sum is:", x+y)
#         @staticmethod
#         def product(x,y):
#                 print("The product is:", x*y)
#         @staticmethod
#         def average(x,y):
#                 print("The average is:", (x+y)/2)
# test.sum(10,15)
# test.product(10,15)
# test.average(10,15)
# # # # ----------------------------------------------------------------------------------------------
# # # if we are not using any decorator: then it may be instance method or static method
# # # # ----------------------------------------------------------------------------------------------
# # #  For class method -- @classmethod decorator is mandatory, cls variable
# # #  For static method -- @classmethod decorator is optional or No decorator(called by using classname), no self/ cls variable
# # #  For instance method -- No decorator (Called by using objectreference), self variable
# # # # ----------------------------------------------------------------------------------------------
# # # example 1:
# # # -------------
# class test:
#         def m1():
#                 print ("some method")
# t=test()
# t.m1()
# # # Typeerror: m1() takes 0 positional arguments but 1 was given
# # #  In the above example, python will consider the method as instance method, but we are not declaring self variable. Hence we are getting the error
# # # # ----------------------------------------------------------------------------------------------
# # # example 2:
# # # -------------
# class test:
#         def m1():
#                 print ("some method")
# test.m1()
# # # It is valid and python will consider this method as static method
# # # # ----------------------------------------------------------------------------------------------
# # # example 3:
# # # -------------
# class test:
#         @staticmethod
#         def m1():
#                 print ("some method")
# t=test()
# t.m1()
# # # # ----------------------------------------------------------------------------------------------
# # example 4:
# # -------------
# class test:
#         def m1(x):
#                 print ("some method:",x)
# t=test()
# t.m1(10)
# # # Invalid
# # # Typeerrori: m1() takes 1 positional arguments but 2 were given
# # # # ----------------------------------------------------------------------------------------------
# # # # ----------------------------------------------------------------------------------------------
# # # # Inner class:
# # # # ------------1.How to access members of one class inside another class
# # # # ----------------------------------------------------------------------------------------------
# class employee:
#         def __init__(self, eno, ename, esalary):
#                 self.eno = eno
#                 self.ename = ename
#                 self.esalary = esalary
#         def display(self):
#                 print("Employee number:",self.eno)
#                 print("Employee name:",self.ename)
#                 print("Employee esalary:",self.esalary)
# class test:
#         def modify(emp):                               # # # instead of "self", "emp" is taken
#                 emp.esalary = emp.esalary + 10000
#                 emp.display()
# e = employee(1,"Sridhar", 15000)
# test.modify(e)
# # # # ----------------------------------------------------------------------------------------------
# # # # How to access members of one class inside another class?
# # # # ----------------------------------------------------------------------------------------------
# # # # # # # Inner class:
# # # # -------------------
# What? The class which is declared inside another class.
# When we should go for inner class?
# If there is no chance of exisiting another type of object, without exsisting one type of object, then we should go for inner classes
#  Without exsisting one type of object, If there is no chance of exisiting another type of object, then we should go for inner classes

# Without car, engine cannot exsist alone. Engine is the part of the car
# class car: (Outer class)
#         # ------
#         class engine: (engine always inner part of the car only--> So only inner claas)

# class University: (It contains department)
#         class department: (Its a part of university)

# class human: (It contains head)
#         class head: (Its a part of human)
# # # Without exsisting outer class object, there is no chance of exsisting inner class object.
# Inner class  object is always associated with outer class object
# # # # ----------------------------------------------------------------------------------------------
# class outer:
#         def __init__(self):
#                 print("Outer class object creation")
#         class inner:
#                 def __init__(self):
#                         print("Inner class object creation")
#                 def m1(self):
#                         print("Inner class method")
# # Outer class contains constructor & inner class. Inner class contains constructor & instance method
# # We cannot access inner class method directly. Outer class object --> Inner class object --> Inner class method
# o=outer()               # We are creating object here = outer class object
# i=o.inner()
# i.m1()
# # #*************** or
# i=outer().inner()
# i.m1()
# # #*************** or
# outer().inner().m1()
# # # # ----------------------------------------------------------------------------------------------
# class outer:
#         def __init__(self):
#                 print("Outer class object creation")
#         def m2(self):
#                 print("Outer class method")
#         class inner:
#                 def __init__(self):
#                         print("Inner class object creation")
#                 def m1(self):
#                         print("Inner class method")
# # Outer class contains constructor & inner class. Inner class contains constructor & instance method
# # We cannot access inner class method directly. Outer class object --> Inner class object --> Inner class method
# o=outer()               # We are creating object here = outer class object
# i=o.inner()
# i.m1()
# o.m2()
# # # # ----------------------------------------------------------------------------------------------
# # # # Person
# # # #         name
# # # #         dob
# # # #      DOB
# # # #         dd
# # # #         mm
# # # #         yyyy
# # # # # ----------------------------------------------------------------------------------------------
# class person:
#         def __init__(self):
#             self.name = "Sridhar"
#             self.dob = self.DOB()            # # # DOB()- creating the object using instance variable(not reference variable) for the "class DOB:"
#         def display(self):                   # # # or.....current outer class object.... associated inner class object....creation
#                 print("Name: ", self.name)
#                 print("printing outer class instance method")
#                 self.dob.display()
#         class DOB:
#                 def __init__(self):
#                         self.dd= 16
#                         self.mm= 11
#                         self.yyyy= 1996
#                 def display(self):
#                         print("printing inner class instance method")
#                         print("DOB={}/{}/{}".format(self.dd, self.mm, self.yyyy))
# p=person()
# p.display()
# # # # # ----------------------------------------------------------------------------------------------
# class person:
#         def __init__(self):
#             self.name = "Sridhar"
#             self.dob = self.DOB()            # # # DOB()- creating the object using instance variable(not reference variable) for the "class DOB:"
#         def display(self):                   # # # or.....current outer class object.... associated inner class object....creation
#                 print("Name: ", self.name)
#                 print("printing outer class instance method")
#                 self.dob.display()
#         class DOB:
#                 def __init__(self):
#                         self.dd= 16
#                         self.mm= 11
#                         self.yyyy= 1996
#                 def display(self):
#                         print("printing inner class instance method")
#                         print("DOB={}/{}/{}".format(self.dd, self.mm, self.yyyy))
# p=person()
# p.display()
# # # # # ----------------------------------------------------------------------------------------------
# class person:
#         def __init__(self):
#             self.name = "Sridhar"
#             self.dob = self.DOB()            # # # DOB()- creating the object using instance variable(not reference variable) for the "class DOB:"
#         def display(self):                   # # # or.....current outer class object.... associated inner class object....creation
#                 print("Name: ", self.name)
#                 print("printing outer class instance method")
#                 self.dob.display()
#         class DOB:
#                 def __init__(self):
#                         self.dd= 16
#                         self.mm= 11
#                         self.yyyy= 1996
#                 def display(self):
#                         print("printing inner class instance method")
#                         print("DOB={}/{}/{}".format(self.dd, self.mm, self.yyyy))
# p=person()
# p.display()
# # # # # ----------------------------------------------------------------------------------------------
# class person:
#         def __init__(self):
#             self.name = "Sridhar"
#             self.dob = self.DOB()            # # # DOB()- creating the object using instance variable(not reference variable) for the "class DOB:"
#         def display(self):                   # # # or.....current outer class object.... associated inner class object....creation
#                 print("Name: ", self.name)
#                 print("printing outer class instance method")
#                 self.dob.display()
#         class DOB:
#                 def __init__(self):
#                         self.dd= 16
#                         self.mm= 11
#                         self.yyyy= 1996
#                 def display(self):
#                         print("printing inner class instance method")
#                         print("DOB={}/{}/{}".format(self.dd, self.mm, self.yyyy))
# p=person()
# p.display()
# # # # # ----------------------------------------------------------------------------------------------
# class person:
#         def __init__(self):
#             self.name = "Sridhar"
#             self.dob = self.DOB()            # # # DOB()- creating the object using instance variable(not reference variable) for the "class DOB:"
#         def display(self):                   # # # or.....current outer class object.... associated inner class object....creation
#                 print("Name: ", self.name)
#                 print("printing outer class instance method")
#                 self.dob.display()
#         class DOB:
#                 def __init__(self):
#                         self.dd= 16
#                         self.mm= 11
#                         self.yyyy= 1996
#                 def display(self):
#                         print("printing inner class instance method")
#                         print("DOB={}/{}/{}".format(self.dd, self.mm, self.yyyy))
# p=person()
# p.display()
# # # # # # ----------------------------------------------------------------------------------------------
# class person:
#         def __init__(self, name, dd, mm, yyyy):
#             self.name = name
#             self.dob = self.DOB(dd,mm,yyyy)            # # # DOB()- creating the object using instance variable(not reference variable) for the "class DOB:"
#         def display(self):                   # # # or.....current outer class object.... associated inner class object....creation
#                 print("Name: ", self.name)
#                 print("printing outer class instance method")
#                 self.dob.displaydob()
#         class DOB:
#                 def __init__(self, dd, mm, yyyy):
#                         self.dd= dd
#                         self.mm= mm
#                         self.yyyy= yyyy
#                 def displaydob(self):
#                         print("printing inner class instance method")
#                         print("DOB={}/{}/{}".format(self.dd, self.mm, self.yyyy))
# p=person("Sridhar", 16,11,1996)
# p.display()
# p.dob.displaydob()
# # # # # ----------------------------------------------------------------------------------------------
# class person:
#         def __init__(self):
#             self.name = "Sridhar"
#             self.dob = self.DOB()            # # # DOB()- creating the object using instance variable(not reference variable) for the "class DOB:"
#         def display(self):                   # # # or.....current outer class object.... associated inner class object....creation
#                 print("Name: ", self.name)
#                 print("printing outer class instance method")
#         class DOB:
#                 def __init__(self):
#                         self.dd= 16
#                         self.mm= 11
#                         self.yyyy= 1996
#                 def display(self):
#                         print("printing inner class instance method")
#                         print("DOB={}/{}/{}".format(self.dd, self.mm, self.yyyy))
# p=person()
# p.display()
# d=p.DOB()
# d.display()

# # # # Can we use outer class method inside inner class method? Yes.(Because Inner class is always associated with outer class method)
# # # # We can take inner class as a method. So you are preferring inner class instead of method.
# # # #  # # # 1. DOB is available for every person
# # # #  # # # 2. DOB has multiple properties and DOB requires methods to show that properties, so inner class is required instead of method in the outer class
# class human:
#         def __init__(self):
#                 self.head = self.Head()
#                 self.brain = self.brain()
#         class Head:
#                 def talk():
#                 class Brain:
#                         def think():
# # # #  Inner class(head) can have another inner class(brain) inside it
# # # # -------------------------------------------------------------------------------------------------------------------------------
# class Human:
#         def __init__(self):
#                 self.name = "Sridhar"
#                 self.head = self.Head()
#         def display(self):
#                 print("Name:", self.name)
#                 self.head.talk()
#                 self.head.brain.think()
#         class Head:
#                 def __init__(self):
#                         self.brain=self.Brain()
#                 def talk(self):
#                         print("Talking.....")
#                 class Brain:
#                         def think(self):
#                                 print("Thinking......")
# h=Human()
# h.display()
# # # # -------------------------------------------------------------------------------------------------------------------------------
# # # # Nested methods:
# # # # -----------------
# # # # What is nested method?
# # # # When to use nested methods?
# # # # How to declare nested methods?
# # # # -----------------
# # # # Inside a method, some functionality/code is repeatedly required again and again
# # # # Also this functionality/code is required only inside that particular method, then go for nested methods
# # # # The biggest advantage is code reusability./ Duplicate code wont be there
# # # # -------------------------------------------------------------------------------------------------------------------------------
# # # def m1():
# # #         xxxxx
# # #         xxxxx //1000 lines of code
# # #         xxxxx

# # #         xxxxx
# # #         xxxxx //1000 lines of code
# # #         xxxxx

# # #         xxxxx
# # #         xxxxx //1000 lines of code
# # #         xxxxx

# # # # # # # -------------------------------------------------------------------------------------------------------------------------------
# # # def m1():
# # #         def m2():
# # #                 xxxxx
# # #                 xxxxx //1000 lines of code
# # #                 xxxxx
# # #         m2() ...inside m1() whenever the functionality is required, just call m2()
# # #         m2() ...inside m1() whenever the functionality is required, just call m2()
# # #         m2() ...inside m1() whenever the functionality is required, just call m2()
# # # # # # # -------------------------------------------------------------------------------------------------------------------------------
# class Test:
#         def m1(self):
#                 def sum(a,b):
#                         print("First argument: ", a)
#                         print("Second argument: ", b)
#                         print("The sum: ", a+b)
#                         print("The product:", a*b )
#                         print("*"*20)
#                 sum(10,20)
#                 sum(23,54)
# t=Test()
# t.m1()
# # # # # # # # -------------------------------------------------------------------------------------------------------------------------------
# # # # # Garbage collector(Part of PVM):
# # # # #---------------------
# # # # # Invoked by PVM
# # # # # Programmer is responsible for creating and deleting object(if no longer required)..
# # # # # By deleting the object --> Free memory by default will be available. But programmer used to neglect it / postpone it.
# # # # # At certain point, the free memory may not be available, which makes the application down.
# # # # # Programmers are provided the assistance to delete the object = Garbage collector (to avoid memory problems) --> to destroy useless objects.
# # # # # # # # -------------------------------------------------------------------------------------------------------------------------------
# # # s= Student() --> Not eligible for garbage collection
# # # s = None --> Eligible for garbage collection (If the object doesnt contain any reference variable)
# # # # # # # # -------------------------------------------------------------------------------------------------------------------------------
# # Based on our requirements, we can enable/ disbale Garbage collector
# # Destructor(__del__) - Before destroying any object, if the object having any cleanup activities or resorce reallocation activities, Destructor is going to take care
# # # # #---------------------
# # # # # import gc  
# # # # #---------------------
# # #  # 1. gc.isenabled()   --True(by enabled by default) 
# # #  # 2. gc.disenable()
# # #  # 3. gc.enable()
# # # # #---------------------
# import gc
# print(gc.isenabled())
# gc.disable()
# print(gc.isenabled())
# gc.enable()
# print(gc.isenabled())
# # # # # # # # -------------------------------------------------------------------------------------------------------------------------------
# # # # # Destructor method: __del__(self)
# # # # #----------------------------------
# # # # GC eligible - If the object doesnot contain any reference variable
# # # # GC will come (to destroy this object) - GC asks for lastwish before destroying
# # # # Object will say...One DB & one Network connection attached with me....Can you pls close these connections(__del__) and destroy me
# # # # Destructor method will be executed to close DB conection and Network connection, then GC will destory the object.
# # # # GC will call destructor directly/automatically, just before destroying the object( to release the associated resources) to perform cleanup/resourcece reallocation activities.
# # # # Once destuctor is executes, then GC will destroy the object.
# # # # 1. GC is the daemon threat(background executing process), as GC is executing in the background.
# # # # 2. If we are not writing destructor, Object class destructor(of parent class) will be executed which wont do anything(unless called by GC).
# # # # # # # # -------------------------------------------------------------------------------------------------------------------------------
# import time
# import gc
# class Test:
#         def __init__(self):
#                 print("Object Initialisation...(not object creation)")
#         def __del__(self):
#                 print("Performing cleanup activities...")
# t1 = Test()
# t1 = None   # # not equal to "del t1" # # means t1 not pointing to any object. the object will be there without any reference ="Immediately" Eligile for GC & (Also without any reference variable, the object will not be used by any resources)
# time.sleep(10)
# print("End of application")
# # # # # # # # -------------------------------------------------------------------------------------------------------------------------------
# import time
# import gc
# class Test:
#         def __init__(self):
#                 print("Object Initialisation...(not object creation)")
#         def __del__(self):
#                 print("Performing cleanup activities...")
# t1 = Test()
# time.sleep(10)
# print("End of application")
# # # # # # # ------------------------------------------------------------------------------
# -------------------------------------------------
# # # # While the program is in exection, GC will not destroy this object. 
# # # # After completing print("End of application")....The program will be stopped. Before terminating the program, destructor will be called(and it will destory every objects created)
# # # # Once the program is terminated, then all the objects already destructed.(It happens even if we didnot write a __del__function)
# # # # # # # # -------------------------------------------------------------------------------------------------------------------------------
# import time
# import gc
# class Test:
#         def __init__(self):
#                 print("Object Initialisation...(not object creation)")
#         def __del__(self):
#                 print("Performing cleanup activities...")
# gc.disable()
# print(gc.isenabled()) # # # # Even if we disable, the object will be deleted (depends on the platofrm we are using - windows/ mac/linux)
# t1 = Test()
# time.sleep(10)
# print("End of application")
# # # # # # # -------------------------------------------------------------------------------------------------------------------------------
# import time
# import gc
# class Test:
#         def __init__(self):
#                 print("Object Initialisation...(not object creation)")
#         def __del__(self):
#                 print("Performing cleanup activities...")
# gc.disable()
# print(gc.isenabled()) # # # # Even if we disable, the object will be deleted (depends on the platofrm we are using - windows/ mac/linux)
# t1 = Test()
# t1 = None   # # not equal to "del t1" # # means t1 not pointing to any object. the object will be there without any reference ="Immediately" Eligile for GC & (Also without any reference variable, the object will not be used by any resources)
# time.sleep(10)
# print("End of application")
# # # # # # # # -------------------------------------------------------------------------------------------------------------------------------
# # # # # # # # 1. The purpose of GC is to destroy useless objects
# # # # # # # # 2. The purpose of destructor is to perform cleanup activities before destroying an object
# # # # # # # # -------------------------------------------------------------------------------------------------------------------------------
# import time
# class Test:
#         def __init__(self):
#                 print("Object Initialisation...(not object creation)")
#         def __del__(self):
#                 print("Performing cleanup activities...")
# t1 = Test()
# t2 = t1
# t3 = t2
# t4 = t3 
# del t1
# time.sleep(10)
# print("After deleting t1, object not destroyed")
# del t2
# del t3
# time.sleep(10)
# print("After deleting t1,t2,t3, object not destroyed")
# time.sleep(10)
# print("End of application")

# # # # # # # # -------------------------------------------------------------------------------------------------------------------------------
# # # # # How many objects are there totally? - 1
# # # # # How many reference variables are there totally? - 4 (poiniting to the same object)
# # # # # Even is a single reference variable is pointing to the object, then it will not be eligible for GC
# # # # # To be eligible for GC, the object shouldnot have a reference variable
# # # # # # # # # -------------------------------------------------------------------------------------------------------------------------------
# import sys
# import time
# class Test:
#         def __init__(self):
#                 print("Object Initialisation...(not object creation)")
#         def __del__(self):
#                 print("Performing cleanup activities...")
# t1 = Test()
# t2 = t1
# t3 = t2
# t4 = t3
# print(sys.getrefcount(t1))                                      # # # (4 + self)  = 5
# del t1
# time.sleep(10)
# print("After deleting t1, object not destroyed")
# del t2
# del t3
# time.sleep(10)
# print("After deleting t1,t2,t3, object not destroyed")
# del t4
# print("After deleting t1,t2,t3 & t4, object eligible for GC")
# time.sleep(10)
# print("End of application")
# # # # # # # # # -------------------------------------------------------------------------------------------------------------------------------
# import time
# class Test:
#         def __init__(self):
#                 print("Object Initialisation...(not object creation)")
#         def __del__(self):
#                 print("Performing cleanup activities...")
# list=[Test(), Test(), Test()] # # # # 3 objects are there, Constructor will be executed 3 times
# time.sleep(10)
# list = None # #Now all the objects will be eligible for GC
# time.sleep(10)
# print("End of application")
# # # # # # # # # # -------------------------------------------------------------------------------------------------------------------------------
# import time
# class Test:
#         def __init__(self):
#                 print("Object Initialisation...(not object creation)")
#         def __del__(self):
#                 print("Performing cleanup activities...")
# list=[Test(), Test(), Test()] # # # # 3 objects are there, Constructor will be executed 3 times
# time.sleep(10)
# print("End of application")
# # # # # # # # # # -------------------------------------------------------------------------------------------------------------------------------
# # # # # How may references available for a particular object - How to find? print(sys.getrefcount(t1))
# # # # # # # # # # -------------------------------------------------------------------------------------------------------------------------------
# class Test:
#         def __init__(self):
#                 print("Object Initialisation...(not object creation)")
#         def __del__(self):
#                 print("Performing cleanup activities...")
# t1 = Test()
# t1 = 150     # # # Then Test() object be will set free(Eligible for GC). the variable t1 will have value 150
# # # # # # # # # # -------------------------------------------------------------------------------------------------------------------------------
# For every python, there is a default object class, from which default constructor & destructor will come(Even if we dont provide explicitly)
# # # # # # # # # # -------------------------------------------------------------------------------------------------------------------------------

# # # Completed
# # # # ------------
# # # # Class
# # # # object
# # # # reference variable
# # # # types of variables
# # # # types of methods
# # # # constructors
# # # # self/cls variable
# # # # inner class
# # # # nested methods
# # # # setter & getter
# # # # GC & destructors


# # # # # # # # # # -------------------------------------------------------------------------------------------------------------------------------
# # # # Polymorphism module:
# # # # ----------------
# # # # 1. what is polymorphism
# # # # 2. Duck typing phylosophy of python
# # # # 3. Overloading - (Operator overloading - In python), (Method overloading,Constructor overloading - Not in python)
# # # # 4. Overriding - (Method overriding, Constructor overriding - IN python)
# # # # # # # # # # -------------------------------------------------------------------------------------------------------------------------------
# # # # 1. what is polymorphism - many shape/ many forms, One name but multiple forms

# # # # Operator overloading: We can use any Python operators for our own purposes also.
# # # Operator overloading concepts internally implemented using magic methods
# # #  for + --> __add__()
# ( Same operator but multiple behaviours- different purposes)
# # # # ----------------
# # # print(10 + 20)         # # arithmetic purpose (+)
# # # print("Durga"+"Soft")  # # string concatenation purpose
# # # print(10*3)
# # # print("Durga"*3)       # # String repetition purpose 
# # # # ----------------
# # # # Any python operators(<,>,<=,>=). We can use any Python operators for our own purposes also.


# # # # # # # # # # -------------------------------------------------------------------------------------------------------------------------------
# # # # Method overloading: ( Same operator but multiple argument types)
# # # # ---------------
# # # deposit(cash)
# # # deposit(cheque)           # # Same method but different argument types = Method overloading
# # # deposit(dd)

# # # abs(int i)
# # # abs(long i)           # # Same method but different argument types = Method overloading
# # # abs(float i)
# # # # # # # # # # -------------------------------------------------------------------------------------------------------------------------------

# class Book:
#         def __init__(self, pages):
#                 self.pages = pages
# b1=Book(100)
# b2=Book(200)
# print(b1+b2) #Error---> For Book objects, we are using + operator. (Invalid)....Expected output =300
# # # # # # # # # # -------------------------------------------------------------------------------------------------------------------------------
# # #  for + --> __add__(self,other) --> the returned value of this method(magic method) will be taken...........Operator overloading...
# # # # # # # # # # -------------------------------------------------------------------------------------------------------------------------------
# class Book:
#         def __init__(self, pages):
#                 self.pages = pages
#         def __add__(self, other):
#                 return self.pages + other.pages
# b1=Book(100)
# b2=Book(200)
# print(b1+b2)
# # # # # # # # # # -------------------------------------------------------------------------------------------------------------------------------
# # # # # def __add__ is called by PVM
# # # # # For every operator available in python the corresponding magic methods are there.
# Overriding those magic methods, we can use any python operator for our own class objects also
# # # Employee object( says salary) * Time object( says Working days) = Salary
# # # # # # # # # # -------------------------------------------------------------------------------------------------------------------------------
# class Book:
#         def __init__(self, pages):
#                 self.pages = pages
#         def __add__(self, other):
#                 return self.pages + other.pages
#         def __sub__(self, other):
#                 return self.pages + other.pages
#         def __mul__(self, other):
#                 return self.pages + other.pages
#         def __div__(self, other):
#                 return self.pages + other.pages
# b1=Book(100)
# b2=Book(200)
# b3 =Book(700)
# print(b2)
# print(b1+b2)
# print(type(b1+b2))
# print(b1+b3)
# print(b2+b3)            # # #  Arguments are already fixed to 2 only:
# # print(b1+b2+b3)       # # # TypeError: unsupported operand type(s) for +: 'int' and 'Book'
# print(b1-b2)
# print(b1*b2)
# # # # # # # # # # -------------------------------------------------------------------------------------------------------------------------------
# # # # Magic methods::: to implement operator overloading
# # # # Predefined names....cant be edited(__dict__, if underscore comes, then it is python specific word, we cannot change that with userdefined)
# # # # # # # # # # -------------------------------------------------------------------------------------------------------------------------------
# # # # # # # # # # # ----
# # # +   ---->  __add__()
# # # -   ---->  __sub__()
# # # *   ---->  __mul__()
# # # /   ---->  __div__()
# # # %   ---->  __mod__()
# # # //   ---->  __floordiv__()
# # # **   ---->  __pow__()


# # # +=   ---->  __iadd__()
# # # -=   ---->  __isub__()
# # # *=   ---->  __imul__()
# # # /=   ---->  __idiv__()
# # # %=   ---->  __imod__()
# # # //=  ---->  __ifloordiv__()
# # # **=   ---->  __ipow__()

# # # >    ---->  __gt__()
# # # >=    ---->  __ge__()
# # # <    ---->  __lt__()
# # # <=    ---->  __le__()
# # # ==    ---->  __eq__()
# # # !=    ---->  __ne__()

# # # Whenever we are trying to "print" any object reference, internally "__str__() method" will be called
# # # # # # # # # # -------------------------------------------------------------------------------------------------------------------------------
# class Book:
#         def __init__(self, pages):
#                 self.pages = pages
#         def __str__(self):
#                 return "The number of pages:" + str(self.pages)
#         def __add__(self):
#                 return self.pages + other.pages 
# b1=Book(100)
# b2=Book(200)
# print(b1+b2)
# # # # # # # # # # -------------------------------------------------------------------------------------------------------------------------------
# class Book:
#         def __init__(self, pages):
#                 self.pages = pages
#         def __str__(self):
#                 return "The number of pages:" + str(self.pages)
#         def __add__(self,other):
#                total = self.pages + other.pages 
#                b =Book(total)   # # Book() 
#                return b
# b1=Book(100)
# b2=Book(200)
# b3=Book(300)
# print(b1+b2+b3)    # # #Converting b1+b2 return type as a "Book Object" instead of "int"  + b3 
# # # # # # # # # # -------------------------------------------------------------------------------------------------------------------------------
# class Book:
#         def __init__(self, pages):
#                 self.pages = pages
#         def __str__(self):
#                 return "The number of pages:" + str(self.pages)
#         def __add__(self,other):
#                total = self.pages + other.pages 
#                b =Book(total)   # # Book() 
#                return b                                        # # The return type is Book()
# b1=Book(100)
# b2=Book(200)
# b3=Book(300)
# b4=Book(1000)
# b5=Book(2000)
# print(b1+b2+b3+b4+b5)    # # # Converting b1+b2 return type as a "Book Object" instead of "int"  + b3 
# # # # # # # # # # -------------------------------------------------------------------------------------------------------------------------------
# # # # # # # flow is
# # # # # # # -->b=b1+b2 returned as Book() type --> b+b3 or b1+b2+b3 returned as Book() type --> b+b4 or b1+b2+b3+b4 returned as Book() type returned as Book() type 
# # # # # # # print will go to str("Number of pages is printed")
# # # # # # # # # # -------------------------------------------------------------------------------------------------------------------------------
# # # # # # # # # # Whenever we are calling + operator then __add__() method will be called
# # # # # # # # # # Whenever we are printing Book Object reference then __str__() method will be called
# # # # # # # # # # -------------------------------------------------------------------------------------------------------------------------------
# class Book:
#         def __init__(self, pages):
#                 self.pages = pages
#         def __str__(self):
#                 return "The number of pages:" + str(self.pages)                # # # Final return type is str (To get the meaningful ouputs)
#         def __add__(self,other):
#                total = self.pages + other.pages 
#                b =Book(total)   # # Book() 
#                return b                                        # # The return type is Book()
#         def __mul__(self,other):
#                total = self.pages*other.pages 
#                b =Book(total)   # # Book() 
#                return b                                        # # The return type is Book()
# b1=Book(100)
# b2=Book(200)
# b3=Book(300)
# b4=Book(1000)
# b5=Book(2000)
# print(b1)
# print(b2)
# print(b3)
# print(b1+b2+b3+b4+b5)    # # # Converting b1+b2 return type as a "Book Object" instead of "int"  + b3 
# b1+b2*b3*b4+b5                # # # Final return type is Book() object
# print(b1+b2*b3*b4+b5)         # # # Final return type is str
# # # # # # # # # # -------------------------------------------------------------------------------------------------------------------------------
# class Book:
#         def __init__(self, pages):
#                 self.pages = pages
#         def __add__(self,other):
#                total = self.pages + other.pages 
#                b =Book(total)   # # Book() 
#                return b                                        # # The return type is Book() object
#         def __mul__(self,other):
#                total = self.pages*other.pages 
#                b =Book(total)   # # Book() 
#                return b                                        # # The return type is Book() object
# b1=Book(100)
# b2=Book(200)
# b3=Book(300)
# b4=Book(1000)
# b5=Book(2000)
# print(b1)
# print(b2)
# print(b3)
# print(b1+b2+b3+b4+b5)    # # # Converting b1+b2 return type as a "Book Object" instead of "int"  + b3 
# b1+b2*b3*b4+b5                # # # Final return type is Book() object
# print(b1+b2*b3*b4+b5)         # # # Final return type is Book() object
# # # # # # # # # # -------------------------------------------------------------------------------------------------------------------------------
# class student:
#         def __init__(self, name, marks):
#                 self.name = name
#                 self.marks = marks
#         def __lt__(self, other):
#                 return self.marks<other.marks
# s1=student("Sridhar",100)
# s2=student("Ravi",200)
# print(s1<s2)
# print(s2<s1)
# # # # # # # # # # # -------------------------------------------------------------------------------------------------------------------------------
# class Employee:
#         def __init__(self, name, salary):
#                 self.name = name
#                 self.salary = salary
#         def __mul__(self, other):               
#                 return self.salary*other.days
# class Timesheet:
#         def __init__(self, name, days):
#                 self.name = name
#                 self.days = days
# e=Employee("Sridhar",1000)
# t=Timesheet("Sridhar",25)
# print("This month salary", e*t)   # # # # "e" comes before "t", so put the __mul__() magic method in "e".........if you put in "t", it will throw an error
# # # # # # # # # # # # -------------------------------------------------------------------------------------------------------------------------------
# # # # # # # # # # # # Since employee() object & Timesheet object are not printed....__str__() method is not used here
# # # # # # # # # # # # -------------------------------------------------------------------------------------------------------------------------------
# class Employee:
#         def __init__(self, name, salary):
#                 self.name = name
#                 self.salary = salary
# class Timesheet:
#         def __init__(self, name, days):
#                 self.name = name
#                 self.days = days
#         def __mul__(self, other):               
#                 return self.days*other.salary
# e=Employee("Sridhar",1000)
# t=Timesheet("Sridhar",25)
# print("This month salary", t*e)   # # # # "t" comes before "e", so put the __mul__() magic method in "t".........if you put in "e", it will throw an error
# # # # # # # # # # # -------------------------------------------------------------------------------------------------------------------------------
# class Employee:
#         def __init__(self, name, salary):
#                 self.name = name
#                 self.salary = salary
#         def __mul__(self, other):               
#                 return self.salary*other.days
# class Timesheet:
#         def __init__(self, name, days):
#                 self.name = name
#                 self.days = days
#         def __mul__(self, other):               
#                 return self.days*other.salary
# e=Employee("Sridhar",1000)
# t=Timesheet("Sridhar",25)
# print("This month salary", e*t)       # # # extending "*" operator for our own class objects is called operator overloading
# print("This month salary", t*e)
# # # # # # # # # # # -------------------------------------------------------------------------------------------------------------------------------




# # # # # # # # Method Overloading:
# # # # # # # # -------------------------------------------------------------------------------------------------------------------------------
# # # # # # # # Two methods having the same name but different argument types = Method overloading
# # # # # # # #  Why? Method overloading is not supported in Python - we don't use data types, then how come the concept of method overloading
# # # # # # # # Even if you declare multiple methods. Python will always consider the most recent method declared, without worrying about the number of parameters. The previous method will be forgotten 
# # # # # # # # For constructor methods also. If you declare multiple constructor methods. The recent constructor method is considered 
# # # # # # # # -------------------------------------------------------------------------------------------------------------------------------
# class Test:
#         def m1(self):
#                 print("No argument method")
#         def m1(self,x):                                               # # # Most recent method is considered                                          
#                 print("One argument method")
#                 print(x)
# t=Test()
# # # t.m1()   # # # TypeError: Test.m1() missing 1 required positional argument: 'x'
# t.m1(10)
# t.m1("Sridhar")
# t.m1(10.5)
# # # # # # # # -------------------------------------------------------------------------------------------------------------------------------
# # # # # # # - OKay. Multiple data types not considered in python
# # # # # # # ***************But if I want to send multiple argunments, then python is supporting with (default argumants, variable length arguments) 
# # # # # # # # -------------------------------------------------------------------------------------------------------------------------------
# # # # # # # # default argumants
# # # # # # # # -----------------
# class Test:
#         def sum(self, a=None, b=None, c=None):                # # # # #None means its not pointing to any variable. "None" doesnot mean "value 0"
#                 if a!=None and b!=None and c!=None:
#                         print("The sum of 3 numbers:", a+b+c)
#                 elif a!=None and b!=None:
#                         print("The sum of 2 numbers:", a+b)
#                 else:
#                         print("Please provide 2 or 3 arguments only")
# t=Test()
# t.sum(10,20)
# t.sum(10)
# t.sum(10,20,30)
# # # # # # # # -------------------------------------------------------------------------------------------------------------------------------
# # # # # # # # Variable length arguments (represented as a tuple)- incade of 10 or 50 or lakhs of arguments
# # # # # # # # -----------------
# class Test:
#         def sum(self, *a):                # # # # #
#                 total = 0                  # # # # # in case of string (total = " ")   
#                 for x in a:
#                         total=total+x
#                 print("The sum is:",total)
                
# t=Test()
# t.sum(10,20)
# t.sum(10)
# t.sum()
# t.sum(10,20,30,40,50,50,60,60,34,234,234,232,4,24,24,2,2)
# # # #t.sum(10,20,"Durga")                 # # # Error
# # # # # # # # -------------------------------------------------------------------------------------------------------------------------------
# class Test:
#         def sum(self, *a):                # # # # #
#                 total = " "                  # # # # # in case of string (total = " ")   
#                 for x in a:
#                         total=total+x
#                 print("The Result:",total)
                
# t=Test()
# t.sum("Sri","sha")
# t.sum()
# t.sum("Sri","sha","India")
# # #t.sum(10,20,"Durga")                 # # # Error
# # # # # # # # -------------------------------------------------------------------------------------------------------------------------------
# # # # # # # # Constructor with default arguments & Variable length arguments are possible
# # # # # # # # -------------------------------------------------------------------------------------------------------------------------------
# class Test:
#         def __init__(self, *a):                # # # # # Constructor method
#                 total = 0                  # # # # # in case of string (total = " ")   
#                 for x in a:
#                         total=total+x
#                 print("The sum is:",total)
# t=Test(10,20)
# t=Test(10,20,30,40,50,50,60,60,34,234,234,232,4,24,24,2,2)
# # # # # # # # -------------------------------------------------------------------------------------------------------------------------------

