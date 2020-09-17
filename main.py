import sys

input = sys.argv[1]


if input = "hydrogen", "Hydrogen", "h", or "H":
	print("Hydrogen (H):")
	print("Atomic Number: 1")
	print("Average Atomic Mass: 1.01 u")
elif input = "helium", "Helium", "he", or "He":
	print("Helium (He):")
	print("Atomic Number: 2")
	print("Average Atomic Mass: 4 u")
elif input = "help":
	print("Periodic Table Lookup:")
	print("Enter an element identifier (example H, Hydrogen, hydrogen) and a small bit of information will be pulled up.")
else:
	print("Not a proper identifier.")
	print("Examples: H, Hydrogen, hydrogen")