from vehicle import Vehicle

class test (Vehicle):
    def __init__(self, speed: int, maximum_mileage: int, motorized: bool) -> None:
        super().__init__(speed, maximum_mileage, motorized)

    def print (self):
        print(f'The speed is :{self.speed}')
        print(f'Maximum mileage: {self.maximumMileage}')
        print(f'Motorized? {self.motorized}')

test99=test(280,50000,False)
test99.print()