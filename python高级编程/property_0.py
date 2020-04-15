import pdb

class Student(object):

    def __init__(self):
        self._birth = 10

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2014 - self._birth


if __name__=="__main__":

    s1 = Student()
    pdb.set_trace()
    print()