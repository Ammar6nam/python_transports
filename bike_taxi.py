from bike import Bike
from public_transport import PublicTransport


class BikeTaxi(Bike,PublicTransport):
    def __init__(self, speed=20, maximum_mileage=600, motorized=False) -> None:
        super().__init__(speed, maximum_mileage, motorized)
    # def __init__(self, speed: int, maximum_mileage: int, motorized=True) -> None:
    #     super().__init__(speed, maximum_mileage, motorized)
    # def __init__(self, motorized=None) -> None:
    #     super().__init__(motorized)

    # def __init__(self,speed,maximum_mileage, motorized) -> None:
    #     super().__init__(speed,maximum_mileage,motorized)
        print(f'motorized {motorized}')
        print(f'speed: {self.speed}')
        print(f'self.motorized {self.motorized}')
        # self.speed=Bike().speed #solving the problem
        # self.motorized=motorized #solving the problem
        # print(f'The speed is :{self.speed}')
        # print(f'Maximum mileage: {self.maximumMileage}')
        # print(f'Motorized? {self.motorized}')
        if self.motorized==True:
            self.capacity=4
            self.speed=30
        if self.motorized==False:
            self.capacity=2
            self.speed=18
        print(f'the capacity is {self.capacity}, The maximum speed is: {self.speed}')
    # def enter_passengers(self,num:int):
    #     self.__current_passengers=num

myTaxiBike=BikeTaxi(False)
# print(BikeTaxi.__mro__)
