class Vehicle:
    def __init__(self,speed:int,maximum_mileage:int,motorized:bool) -> None:
        self.speed=speed
        self.maximumMileage=maximum_mileage
        self.motorized=motorized
        self.__scrapMetal=False
        if self.__scrapMetal==False:
            pass
            print('Ready to go!')
            # print(self.speed)
            # print(self.maximumMileage)
            # print(self.motorized)

    def drive(self,km:int):
        if km<0:
            km=-km
        if self.__scrapMetal==False:
            self.maximumMileage-= km
            if self.maximumMileage<=0:
                self.__scrapMetal = True
                print (f'The {self.__class__.__name__} is broken!')
                return False
            else:
                print(f'This {self.__class__.__name__} drive: {km}km!')   
        return True
        

# myVehicle=Vehicle(200,100000,True )
# myVehicle.drive(100001)
# myVehicle.drive(-99999)
