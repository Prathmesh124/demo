from abc import ABC,abstractmethod,abstractclassmethod,ABCMeta,abstractproperty
class car(ABC):
    @abstractmethod
    def engine(self):
        pass
    @abstractmethod
    def chasis(self):
        pass
    @abstractmethod
    def controles(self):
        pass
    @abstractmethod
    def fuel_type(self):
        print("fuel is petrol")
    
    def run(self):
        print("car is running")



class tata(car):
    def engine(self):
        print("V8 engine")
    def chasis(self):
        print("hatchback")
    def controles(self):
        print("automatic")
    def fuel_type(self): 
        return super().fuel_type()

class honda(car):
    def engine(self):
        print("V4 engine")
    def chasis(self):
        print("sedan")
    def controles(self):
        print("semi-auto")
    def fuel_type(self):
        print("electric")
    def run(self):
        print("honda is running")
class test:
    nano=tata()
    nano.engine()
    nano.fuel_type()
    city=honda()
    city.engine()
    city.fuel_type()
    city.run()
    nano.run()