from pprint import pprint as pp
from samples.air_travel_1 import Flight, Aircraft
from pprint import pprint as pp


def make_flight():
    f = Flight("BA758", Aircraft("G-EUPT", "Airbus A319",
               num_rows=22, num_seats_per_row=6))
    f.allocate_seat("12A", "Guido van Rosssum")
    f.allocate_seat("15F", "Bjarne Stroustrup")
    f.allocate_seat("15E", "Anders Hejlsberg")
    f.allocate_seat("1C", "John McCarthy")
    f.allocate_seat("1D", "Rich Hickey")
    return f


f = make_flight()

print(pp(f._seating))

f.relocate_seat("12A", "15D")

print(pp(f._seating))


print(f.num_available_seats())


def console_card_printer(passenger, seat, flight_number, aircraft):
    output = f'| Name: {passenger}' \
             f' Flight: {flight_number}' \
             f' Seat: {seat}' \
             f' Aircraft: {aircraft}'\
             " | "
    banner = "+" + "-" * (len(output) - 2) + "+"
    border = "|" + " " * (len(output) - 2) + "|"
    line = [banner, border, output, border, banner]
    card = "\n".join(line)
    print(card)
    print()


f.make_boarding_cards(console_card_printer)
