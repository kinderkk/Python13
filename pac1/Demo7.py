# 面向对象
# 封装、继承、多态

# 定义类
# 封装方法和变量（类的属性）
# object是所有类的基类，相当有java中Object
class Person(object):
    # 构造
    # 类中的所有方法的第一个参数都是self：代表对象本身  相当于java中的this
    def __init__(self, id, name, gender):
        # 定义了类的属性并进行赋值
        self.id = id
        self.name = name
        self.gender = gender
        #如果定义的属性不想直接被获取，可以在前面加__
        self.__secrect

    def info(self):
        print(self.id, self.name, self.gender)

    # 相当于Java中的toString，在使用print函数打印该类的对象时会自动调用
    def __str__(self):
        return "person类的对象 %s" % self.name


# 创建对象
ja = Person('001', 'jack', 'male')
print(ja)
print(ja.id)
print(ja.name)


class Teacher(Person):
    def __init__(self, id, name, gender):
        # 调用父类的构造方法
        super(Teacher, self).__init__(id, name, gender)
        self.professional = 'compute'

    def __str__(self):
        print("Teacher", self.id, self.name, self.gender, self.professional)


t1 = Teacher("mrs Z", "24", "male")
print(t1.id)
print(t1.age)
print(t1.gender)


class student(Person):
    def __init__(self, id, name, gender):
        super(student, self).__init__(id, name, gender)
        self.skill = 'play game!'

    def info(self):
        print("student", self.id, self.name, self.gender, self.skill)

