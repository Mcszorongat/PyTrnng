a = "string a"
b = 'string b'
c = "the 'c' string"
d = r"What\you\see\        what\''you\get"
e = str(3.14)
f = "\u00E1"    # unicode hex
g = "\xE1"      # hex
h = "\341"      # octal
i = a + " " + b
j = "; ".join([a, b, c])            # to join the strings use empty as separator: ''.join([str_1, str_2, str_3])
k = j.split("; ")
l = "a,b,c,d".partition(",")
m = "a,b,c,d".rpartition(",")
print(a, b, c, d, e, a[3], type(a[3]), f, g, h)
print("| i =", i, "| j =", j, "| a =", a)
print("| k =", k, "| l =", l, "| m =", m)
print("The temperature is {0}°C today, and the wind speed is {1}km/h.".format(11.5, 23))
print("If the number and order is the same number can be omitted {}°C ... {}km/h.".format(11.5, 23))
print("Changing the order {1}°C ... {0}km/h.".format(11.5, 23))
print("Using an argument more {0}°C ... {0}km/h{1}.".format(11.5, 23))
print("Keywords {temp}°C ... {wind}km/h.".format(temp = 11.5, wind = 23))
print("Using a tuple {tpl[0]} to fill the {tpl[1]} gaps in the {tpl[2]} text".format(tpl=(0, "asd", 5.0)))
print("Floating point formating {0:.3f} or {0:.2f}".format(1.23456))

# fstrings: f"stringgg"
value = 5
print("A line for {val}.".format(val=value))
# f-string
print(f"A line for {value}.")