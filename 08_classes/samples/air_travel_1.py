class Aircraft:

    def __init__(self, registration, model, num_rows, num_seats_per_row):
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_row = num_seats_per_row

    def registration(self):
        return self._registration

    def model(self):
        return self._model

    def seating_plan(self):
        return (range(1, self._num_rows + 1), "ABCDEFGHJK"[:self._num_seats_per_row])


class Flight:
    """A class object to handle all the flight related queries
    """

    def __init__(self, number, aircraft):
        # _ is mandatory for the self._
        if not number[:2].isalpha():
            raise ValueError(f'No airline code in {number}')
        if not number[:2].isupper():
            raise ValueError(f'Invalid airline code {number}')
        if not number[2:].isdigit() and int(number[2:] <= 999):
            raise ValueError(f'Invalid route number {number}')
        self._number = number
        self._aircraft = aircraft
        rows, seats = self._aircraft.seating_plan()
        self._seating = [None] + \
            [{letter: None for letter in seats} for _ in rows]

    def number(self):
        return self._number

    def airline(self):
        return self._number[:2]

    def aircraft_model(self):
        return self._aircraft.model()

    def aircraft_seating_plan(self):
        return self._aircraft.seating_plan()

    def _parse_seat(self, seat):
        """_ should be used before the method for accessing from the same class
        """
        rows, seats = self._aircraft.seating_plan()
        letter = seat[-1]
        if letter not in seats:
            raise ValueError(f'Invalid seat letter {letter}')
        row_text = seat[:-1]
        try:
            row = int(row_text)
        except ValueError:
            raise ValueError(f'Invalid seat row {row_text}')
        if row not in rows:
            raise ValueError(f'Invalid row number {row}')
        return row, letter

    def allocate_seat(self, seat, passenger):
        row, letter = self._parse_seat(seat)
        if self._seating[row][letter] is not None:
            raise ValueError(f'Seat {seat} already occupied')
        self._seating[row][letter] = passenger

    def relocate_seat(self, from_seat, to_seat):
        from_row, from_letter = self._parse_seat(from_seat)
        if self._seating[from_row][from_letter] is None:
            raise ValueError(f"No passenger to relocate in seat {from_seat}")
        to_row, to_letter = self._parse_seat(to_seat)
        if self._seating[to_row][to_letter] is None:
            return ValueError(f"No passenger to relocate in seat {to_seat}")
        # Swap seats
        self._seating[to_row][to_letter] = self._seating[from_row][from_letter]
        self._seating[from_row][from_letter] = None

    def num_available_seats(self):
        return sum(sum(1 for s in row.values() if s is None)
                   for row in self._seating
                   if row is not None)

    def make_boarding_cards(self, card_printer):
        for passenger, seat in sorted(self._passenger_seats()):
            card_printer(passenger, seat, self.number(), self.aircraft_model())

    def _passenger_seats(self):
        row_numbers, seat_letters = self._aircraft.seating_plan()
        for row in row_numbers:
            for letter in seat_letters:
                passenger = self._seating[row][letter]
                if passenger is not None:
                    yield (passenger, f'{row} {letter}')
