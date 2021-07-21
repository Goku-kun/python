class Vehicle:
    value_var = 10

    def __init__(self, make, model, fuel="gas") -> None:
        self.make = make
        self.model = model
        self.fuel = fuel
        print(self.value_var)
        self.value_var = 110

    def __repr__(self, type_vehicle) -> str:
        return f"{type_vehicle}('{self.make}','{self.model}','{self.fuel}')"


class Car(Vehicle):

    def __init__(self, make, model, fuel="gas") -> None:
        super().__init__(make, model, fuel=fuel)
        print("Car has been allotted.")

    def __repr__(self) -> str:
        return super().__repr__("Car")
