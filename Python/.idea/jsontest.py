class annimal:
    name = ''
    sex = ''

    def __init__(self,name,sex,age=0,):
        self.age = age
        self.name = name
        self.sex = sex

    def showinfo(self):
        print("My name is "+self.name+",and my sex is "+self.sex+",meanwhile my age is "+ str(self.age))

cat1 = annimal(name="小黄",sex="母")
cat1.showinfo()
