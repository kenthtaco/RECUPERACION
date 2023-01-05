from pprint import pprint
from account import Account
from accountDriver import Driver
from accountUser import User
from car import Car
from payment import Payment
from paymentCard import PaymentCard
from paymentCash import PaymentCash
from paymentTransfer import PaymentTransfer
from route import Route
from trip import Trip
from uberXL import UberXL
from uberConfort import UberConfort
from uberX import UberX

if __name__ == "__main__":
    usuario1 = User(1, "Douglas Quilumba", "Masculino", 99999999, 20)
    print(vars(usuario1))

    usuario2 = User(2, "Kenth Taco", "Masculino", 99999999, 30)
    print(vars(usuario2))

    driver1 = Driver(3, "Douglas Quilumba", "Masculino", 9999999, 20, "Licencia111")
    print(vars(driver1))
    
    driver2 = Driver(6, "Kenth Taco", "Masculino", 99989999, 20, "Licencia113")
    print(vars(driver2))


    carro1 = Car("PBC-555555", "Chevrolet Corsa", "Gris", 2015, Driver(3, "Kenth Taco", "Masculino", 9999999, 20, "Licencia111"))
    print(vars(carro1))
    print(vars(carro1.driver))
    
    carro2 = Car("PBC-555555", "Suzuki Forza", "Azul", 2019, Driver(7, "Alisson Egas", "Femenino", 99889479999, 19, "Licencia03"))
    print(vars(carro1))

    uberX1   = UberX("XLX-5599", "Chevrolet Corsa", "Gris", 2015, Driver(3, "Alexander Flores", "Masculino", 9999999, 29, "Licencia111"))
    print(vars(uberX1))
    print(vars(uberX1.driver))

    uberConfort1 = UberConfort("PCV-1115", "Hiunday-Tucson", "Negro", 2019, Driver(5, "Jose Alban", "Masculino", 99999999, 25, "Licencia0005"), True, 5, "Cuero")
    print(vars(uberConfort1))
    print(vars(uberConfort1.driver))

    pago001 = PaymentTransfer(1, 5.0, "13-12-2022", 5555555, "Pichincha")
    print(vars(pago001))
    
    pago002 = PaymentCard(2, 6.9, "13-12-2022", 11123456, "Pacifico", [1712332132, "Noviembre 2023", "Kenth Taco", 559])
    print(vars(pago002))
    
    pago003 = Payment(3, 7.3, "13-12-2022")
    print(vars(pago003))
    
    pago004 = Payment(4, 17.3, "13-12-2022")
    print(vars(pago003))
    
    route001  = Route([-0.21885831940848277, -78.51114957623152], [-0.2143, -78.5017], 5, 20)
    print(vars(route001))
    
    trip001 = Trip(1, User(1, "Kenth Taco", "Masculino", 99999999, 29), Driver(3, "Douglas Quilumba", "Masculino", 9999999, 29, "Licencia111"), Car("PBC-555555", "Chevrolet Corsa", "Gris", 2015, Driver(3, "Alexander Flores", "Masculino", 9999999, 29, "Licencia111")), Route([-0.21885831940848277, -78.51114957623152], [-0.2143, -78.5017], 5, 20), Payment(3, 7.3, "13-12-2022"))
    print(vars(trip001))
    print(vars(trip001.car))
    print(vars(trip001.car.driver))
    print(vars(trip001.driver))
    print(vars(trip001.user))
    print(vars(trip001.route))
    print(vars(trip001.payment))
    
    trip002 = Trip(2, usuario2, driver2, carro2, route001, pago004)
    print(vars(trip002))
    print(vars(trip002.car))
    print(vars(trip002.car.driver))
    print(vars(trip002.driver))
    print(vars(trip002.user))
    print(vars(trip002.route))
    print(vars(trip002.payment))