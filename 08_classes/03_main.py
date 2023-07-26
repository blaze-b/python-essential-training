from pprint import pprint as pp
from samples.air_travel_1 import Flight, Aircraft

flight = Flight("BA758", Aircraft("G-EUPT", "Airbus A319",
                num_rows=22, num_seats_per_row=6))

print(flight.aircraft_model(), flight.aircraft_seating_plan())

print(pp(flight._seating))

flight.allocate_seat("12A", "Guido van Ross")

flight.allocate_seat("13A", "Brian")

flight.allocate_seat("22A", "Brian")

print(pp(flight._seating))
