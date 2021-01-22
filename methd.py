class stud:
    def __init__(self,fname,lname,age):
        self.fname=fname
        self.lname=lname
        self.age=age
    def emailgen(self):
        return "{}.{}@school.com".format(self.fname,self.lname)

stud1=stud('siddharth','dixit',25)

print(stud1.emailgen())