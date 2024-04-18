##class Car :
##    model = "bmw"
##    color = "white"
##
##    def speedChange(self,v) :
##        print("speedChange : %d" %v)
##        self.speed = v
##
##bmw = Car()
##bmw.speedChange(20)

##class Car :
##    model = "bmw"
##    color = "white"
##
##bmw = Car()
##benz = Car()
##
##benz.model = "Benz"
##benz.color = "black"
##
##print(bmw.model)
##print(bmw.color)
##
##print(benz.model)
##print(benz.color)

##class Car :
##    model = "bmw"
##    color = "white"
##
##    def speedChange(self,v) :
##        Car.count += 1
##        self.speed = v
##
##bmw = Car()
##benz = Car()
##
##bmw.speedChange(100)
##print("bmw speed :%d",bmw.speed)
##print("number of speedChange :%d", Car.count)
##
##benz.speedChange(120)
##print("Benz speed : %d", benz.speed)
##print("number of speedChange : %d",Car.count)

##class Car :
##
##    def __init__(self,model,color) :
##        self.model = model
##        self.color = color
##
##    def info(self) :
##        print("Model : ",self.model,",Color:",self.color)
##        
##bmw = Car("bmw","white")
##benz = Car("benz","black")
##bmw.info()
##benz.info()
    
class Car :
    def __init__(self,model,color) :
        self.model = model
        self.color = color
    def info(self) :
        print("Model : ", self.model,",color:",self.color)

class CarDrive(Car) :
    def speedChange(self,v) :
        self.speed = v
        print("speedChange :",self.speed)

bmw = CarDrive("bmw","white")
bmw.info()
bmw.speedChange(100)







        










    
