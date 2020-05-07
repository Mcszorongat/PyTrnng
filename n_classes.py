import na_airtravel, pprint

f1 = na_airtravel.Flight("SN060")
print(type(f1), f1._number, f1.number(), f1.airline())

a1 = na_airtravel.Aircraft("G-EUPT", "Airbus A319", 22, 6)
print(type(a1))
print(a1.model())
print(a1.registration())
print(a1.seating_plan())

f2 = na_airtravel.make_flight()

pprint.pprint(f2.get_seating())

print(f2.get_seat("1A"))

f2.move_passenger("1A", "6A")

pprint.pprint(f2.get_seating())

print(f2.num_available_seats(), 10*5-5)

f2.make_boarding_cards(na_airtravel.console_card_printer)