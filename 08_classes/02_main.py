from samples.air_travel_0 import Aircraft

aircraft = Aircraft("G-EUPT", "Airbus A319", num_rows=22, num_seats_per_row=6)


print(aircraft.registration(), aircraft.model(), aircraft.seating_plan())
