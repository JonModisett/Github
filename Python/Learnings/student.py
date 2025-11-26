#using a property to (indirectly) acess data in an object

class Student():

    def __init__(self, name, startingGrade=0):
        self.__name = name
        self.grade = startingGrade

        @property
        def grade(self):
            return self.__grade
