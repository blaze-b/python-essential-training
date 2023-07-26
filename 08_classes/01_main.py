from samples.air_travel_0 import Flight

flight = Flight("SN060")

print(type(flight))

print(flight.number())

# Not recomended
print(flight._number)

flight = Flight("060")

flight = Flight("sm060")

flight = Flight("snanbe")
