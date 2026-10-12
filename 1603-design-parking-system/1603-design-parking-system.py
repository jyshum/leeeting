class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big = big # of big spaces
        self.medium = medium # of medium spaces
        self.small = small # of small spaces

    def addCar(self, carType: int) -> bool:
        # 1 = big
        # 2 = medium
        # 3 = small
        if carType == 1:
            # big car, check for number of big spaces
            if self.big > 0:
                self.big -= 1 # take up one space, 1 less big space 
                return True
            else:
                return False
        elif carType == 2:
            # medium car
            if self.medium > 0:
                self.medium -= 1
                return True
            else:
                return False
        else:
            if self.small > 0:
                self.small -= 1
                return True
            else:
                return False

        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)