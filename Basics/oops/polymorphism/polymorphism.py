class ABC:
     def __init__(self,name,phone,email):
        self.name=name
        self.phone=phone
        self.email=email
     name=""
     phone=0
     email=""

     def display(self):
        print(self.name,self.email)
class test:
    std1=ABC("pm",3246545,"vhgfghjkhk")
    std1.display()



        