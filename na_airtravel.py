class Aircraft:
    def __init__(self, registration, model, numRows, numSeatsPerRow):
        self._registration = registration
        self._model = model
        self._numRows = numRows
        self._numSeatsPerRow = numSeatsPerRow


    def registration(self):
        return self._registration


    def model(self):
        return self._model


    def seating_plan(self):
        return(range(1, self._numRows + 1), "ABCDEFGHJK"[:self._numSeatsPerRow])

class AirbusA320(Aircraft):
    pass

class Flight:      #PascalCase
    """A flight with a particular passenger aircraft."""
    def __init__(self, number, aircraft=Aircraft("G-EUPT", "Airbus A319", numRows=21, numSeatsPerRow=6)):
        #establish class invariances

        if not number[:2].isalpha():
            raise ValueError(f"No airline code in '{number}''")
        elif not number[:2].isupper():
            raise ValueError(f"Invalid airline code '{number}''")
        elif not (number[2:].isnumeric() and int(number[2:]) <= 9999):
            raise ValueError(f"Invalid route number '{number}''")

        self._number = number
        self._aircraft = aircraft
        rows, seats = self._aircraft.seating_plan()
        self._seating = [None] + [{letter : None for letter in seats} for _ in rows]

    def _parse_seat(self, seat):
        rows, seats = self._aircraft.seating_plan()
        letter = seat[-1]
        try:
            row = int(seat[:-1])
        except ValueError:
            raise ValueError("Invalid row:", row)

        if letter not in seats or not letter.isupper():
            raise ValueError("Invalid seat letter:", letter)
        elif row not in rows:
            raise ValueError("Invalid row:", row)

        return row, letter

    def number(self):
        return self._number


    def airline(self):
        return self._number[:2]


    def aircraft_model(self):
        return self._aircraft.model()


    def get_seating(self):
        return self._seating


    def get_seat(self, seat):
        row, letter = self._parse_seat(seat)

        return self._seating[row][letter]


    def set_seat(self, seat, passenger):
        row, letter = self._parse_seat(seat)

        if self._seating[row][letter] != None:
            raise ValueError(f"Seat {seat} is already occupied.")

        self._seating[int(row)][letter] = passenger

    def move_passenger(self, src, dst):
        rows, seats = self._aircraft.seating_plan()

        if src[-1] not in seats or not dst[-1].isupper():
            raise ValueError("Invalid seat letter:", src[-1])
        elif int(src[:-1]) not in rows:
            raise ValueError("Invalid row:", src[:-1])
        elif self._seating[int(src[:-1])][src[-1]] == None:
            raise ValueError(f"Seat {src} is empty.")

        if dst[-1] not in seats or not dst[-1].isupper():
            raise ValueError("Invalid seat letter:", dst[-1])
        elif int(dst[:-1]) not in rows:
            raise ValueError("Invalid row:", dst[:-1])
        elif self._seating[int(dst[:-1])][dst[-1]] != None:
            raise ValueError(f"Seat {dst} is already occupied.")

        self._seating[int(dst[:-1])][dst[-1]] = self._seating[int(src[:-1])][src[-1]]
        self._seating[int(src[:-1])][src[-1]] = None


    def num_available_seats(self):
        return sum(sum(1 for x in i.values() if x is None) for i in self.get_seating() if i is not None)


    def make_boarding_cards(self, card_printer):
        for passenger, seat in sorted(self.passenger_seats()):
            card_printer(passenger, seat, self.number(), self.aircraft_model())


    def passenger_seats(self):
        row_numbers, seat_letters = self._aircraft.seating_plan()
        for row in row_numbers:
            for letter in seat_letters:
                passenger = self.get_seat(str(row) + letter)
                if passenger != None:
                    yield (passenger, str(row) + letter)

def make_flight():
    f = Flight("BA758", Aircraft("G-EUPT", "Airbus A319", numRows=10, numSeatsPerRow=5))
    f.set_seat("1A", "Kana Hanazawa")
    f.set_seat("2B", "Sawashiro Moyuki")
    f.set_seat("3C", "Orihara Izaya")
    f.set_seat("4D", "Okabe Rintarou")
    f.set_seat("5E", "Midoriya Izuku")
    # invalid *
    #f.set_seat("1A", "Orihara")
    #f.set_seat("1a", "Matsumoto")
    #f.set_seat("100A", "Matsumoto")
    
    return f

def console_card_printer(passenger, seat, flight_number, aircraft):
    output =    f"| Name: {passenger}"          \
                f"  Flight: {flight_number}"    \
                f"  Seat: {seat}"               \
                f"  Aircraft: {aircraft}"       \
                " |"
    banner =    "+" + "-" * (len(output)-2) + "+"
    border =    "|" + " " * (len(output)-2) + "|"
    lines =     [banner, border, output, border, banner]
    card =      "\n".join(lines)
    print(card)
    print()