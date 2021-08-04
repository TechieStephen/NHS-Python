class Student:
    is_graduate = False

    def __init__(self, name, age, student_class):
        self.name = name
        self.age = age
        self.student_class = student_class

    def graduate(self):
        if self.age > 29:
            is_graduate = True
        else:
            is_graduate = False
        return is_graduate


