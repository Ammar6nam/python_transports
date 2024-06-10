from vehicle import Vehicle
class Bike(Vehicle):
    def __init__(self,speed=20,maximum_mileage=600,motorized=False) -> None:
            self._mileage_until_next_repair=200
            super().__init__(speed, maximum_mileage,motorized)
            # if speed == None:
            #     self.speed=20

            # if motorized==None:
            #      self.motorized=False
            # match motorized:
            #     case None:
            #           self.motorized=False
            #           print(self.motorized)
            #     case False:
            #           self.motorized=False
            #           print(self.motorized)
            #     case True:
            #           self.motorized=True
            #           print(self.motorized)
            # print(f'The speed is :{self.speed}')
            # print(f'Maximum mileage: {self.maximumMileage}')
            # print(f'Motorized? {self.motorized}')
    def repair(self):
        self._mileage_until_next_repair=200

    def drive(self,km:int):
                    
        # if self._mileage_until_next_repair<=0:
        #      self._mileage_until_next_repair=0
        #      print('The bike need to be repaired again! ')
        if self._mileage_until_next_repair>0:
            self._mileage_until_next_repair-=km
            super().drive(km)
            print(f'Need to be repaired after {self._mileage_until_next_repair}km!')
        return True

# myBike=Bike(motorized=True)
# myBike.drive(220)