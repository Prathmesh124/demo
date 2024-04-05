#access specfiers
class Userdetails:
    __username="pm"
    __password="123456"

    def show(self):
        print("show method",self.__username)

class Login(Userdetails):
    user1=Userdetails()
    user1.show()
    
