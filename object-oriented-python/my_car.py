from vehicle import Car, Vehicle

my_car = Car("Shira", "nai")

print(f"The car is of type: {type(my_car)}")
print(f"The model is {my_car.model}")
print(f"The make is {my_car.make}")
print(my_car.__str__())
print(my_car.__repr__())
print(my_car.value_var, "is the value in instance variable")

print(Car.value_var)
Car.value_var = 100
print(Car.value_var)

print(my_car.value_var, "is the value in instance variable")
