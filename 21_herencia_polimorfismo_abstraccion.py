from typing import override


class Vehicle:
    def __init__(self, brand: str, model: str, price: int):
        self.brand: str = brand
        self.model: str = model
        self.price: int = price
        self.is_available: bool = True

    def sell(self):
        if self.is_available:
            self.is_available = False
            print(f"{self.brand} {self.model} has been sold.")
        else:
            print(f"{self.brand} {self.model} is not available for sale.")

    def check_availability(self):
        return self.is_available

    def get_price(self):
        return self.price

    def start_engine(self) -> str | None:
        raise NotImplementedError("Subclasses must implement start_engine method.")

    def stop_engine(self) -> str | None:
        raise NotImplementedError("Subclasses must implement start_engine method.")


class Car(Vehicle):
    @override
    def start_engine(self) -> str | None:
        if not self.is_available:
            return f"Car {self.brand} engine is started"
        else:
            return f"Car {self.brand} is not available"

    @override
    def stop_engine(self) -> str | None:
        if not self.is_available:
            return f"Car {self.brand} engine is stopped"
        else:
            return f"Car {self.brand} is not available"


class Motorcycle(Vehicle):
    @override
    def start_engine(self) -> str | None:
        if not self.is_available:
            return f"Motorcycle {self.brand} engine is started"
        else:
            return f"Motorcycle {self.brand} is not available"

    @override
    def stop_engine(self) -> str | None:
        if not self.is_available:
            return f"Motorcycle {self.brand} engine is stopped"
        else:
            return f"Motorcycle {self.brand} is not available"


class Bike(Vehicle):
    @override
    def start_engine(self) -> str | None:
        if not self.is_available:
            return f"Bike {self.brand} is on the move"
        else:
            return f"Bike {self.brand} is not available"

    @override
    def stop_engine(self) -> str | None:
        if not self.is_available:
            return f"Bike {self.brand} is stopped"
        else:
            return f"Bike {self.brand} is not available"


class Customer:
    def __init__(self, name: str):
        self.name: str = name
        self.vehicles: list[Vehicle] = []

    def buy_vehicle(self, vehicle: Vehicle):
        if vehicle.check_availability():
            vehicle.sell()
            self.vehicles.append(vehicle)
            print(f"{self.name} has bought {vehicle.brand} {vehicle.model}.")
        else:
            print(
                f"{self.name} cannot buy {vehicle.brand} {vehicle.model} is not available."
            )

    def inquire_vehicle(self, vehicle: Vehicle):
        availability = "available" if vehicle.check_availability() else "not available"
        print(
            f"{self.name} can inquire about {vehicle.brand} {vehicle.model}, which is {availability}."
        )

    def get_vehicles(self):
        print("Available Vehicles for Customer:")
        for vehicle in range(0, len(self.vehicles)):
            print(
                f"{self.vehicles[vehicle].brand} {self.vehicles[vehicle].model} - ${self.vehicles[vehicle].get_price()}"
            )


class Dealership:
    def __init__(self):
        self.customers: list[Customer] = []
        self.vehicles: list[Vehicle] = []

    def add_vehicle(self, vehicle: Vehicle):
        self.vehicles.append(vehicle)

    def register_customer(self, customer: Customer):
        self.customers.append(customer)
        print(f"{customer.name} has been registered.")

    def show_available_vehicles(self):
        print("Available Vehicles:")
        for vehicle in self.vehicles:
            if vehicle.check_availability():
                print(f"{vehicle.brand} {vehicle.model} - ${vehicle.get_price()}")


# Crear instancias de los carros
car1 = Car("Toyota", "Corolla", 20000)
car2 = Car("Honda", "Civic", 22000)
car3 = Car("Ford", "Mustang", 35000)
bike1 = Bike("Honda", "CBR500R", 15000)
bike2 = Bike("Yamaha", "YZF-R6", 20000)
mt1 = Motorcycle("Harley-Davidson", "Sportster Iron 883", 25000)
mt2 = Motorcycle("Ducati", "Panigale V4", 30000)

# Crear instancia de Cliente
c1 = Customer("John Doe")

# Crear instancia de DealerShip
d1 = Dealership()

# Agregar carros al DealerShip
d1.add_vehicle(car1)
d1.add_vehicle(car2)
d1.add_vehicle(car3)
d1.add_vehicle(mt1)
d1.add_vehicle(mt2)
d1.add_vehicle(bike1)
d1.add_vehicle(bike2)

# Registrar cliente en DealerShip
d1.register_customer(c1)

# Mostrar carros disponibles en DealerShip

print(">>>>>>> Available Vehicles >>>>>>>>")
d1.show_available_vehicles()
print(">>>>>>> Available Vehicles >>>>>>>>")

# Cliente compra un carro
c1.buy_vehicle(car1)
c1.buy_vehicle(mt1)
c1.buy_vehicle(bike1)
# Cliente pregunta por un carro
c1.inquire_vehicle(car2)

print(">>>>>>> Customer Vehicles >>>>>>>>")
c1.get_vehicles()
print("<<<<<<< Customer Vehicles <<<<<<<<")

# DealerShip muestra carros disponibles
d1.show_available_vehicles()
