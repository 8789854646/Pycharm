class Employee:
    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay
    @property
    def fname(self):
        return self._fname
    @fname.setter
    def fname(self, value):
        if len(value)>5:
            raise Exception("fname cannot be more than 5 characters")
        self._fname = value
    @property
    def lname(self):
        return self._lname
    @lname.setter
    def lname(self, value):
        if len(value)>5:
            raise Exception("Lname cannot be more than 5 characters")
        self._lname = value
    @property
    def pay(self):
        return self._pay
    @pay.setter
    def pay(self, value):
        if not isinstance(value, (int, float)):
            raise Exception("pay should be a number")
        self._pay = value
    def pay_raise(self, percent):
        hike_amt = self._pay * percent/100
        self._pay+= hike_amt

e = Employee("vivek","kumar",2000)
print(e.__dict__)

