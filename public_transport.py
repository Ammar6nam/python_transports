from vehicle import Vehicle
class PublicTransport(Vehicle):
    def __init__(self, speed: int, maximum_mileage: int, motorized = True) -> None:
        super().__init__(speed, maximum_mileage, motorized)
        self.__current_passengers=0
    # def __init__(self,motorized=None) -> None:
    #     self.__current_passengers=0
    #     super().__init__(None,None,motorized)
        # if speed == None:
        #     self.speed=super().speed
        # if maximum_mileage==None:
        #     self.maximumMileage=super().maximumMileage 
        # if motorized==None:
        #     self.motorized=True
        # print(f'The speed is :{self.speed}')
        # print(f'Maximum mileage: {self.maximumMileage}')
        # print(f'Motorized? {self.motorized}')

    def enter_passengers(self,num:int):
        self.__current_passengers+=num

    def exit_passengers(self,num:int):
        self.__current_passengers-=num

    def get_current_passengers(self):
        return self.__current_passengers
    

# myPublicTransport=PublicTransport()
# (myPublicTransport.enter_passengers(15))
# myPublicTransport.exit_passengers(5)
# print(f'The current passengers are: {myPublicTransport.get_current_passengers()}')