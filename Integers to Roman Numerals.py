#Script to Convert Roman Numerals to Integers for 5500 Form Project

def inttoroman(Inputnumber):

	romanstring = ""

	romandict = {1000: "M",
				900: "CM",
				500: "D",
				400: "CD",
				100: "C",
				90: "XC",
				50: "L",
				40: "XL",
				10: "X",
				9: "IX",
				5: "V",
				1: "I",
				0: ""}

	values = [1000,900,500,400,100,90,50,40,10,9,5,1]

	coefficients = [0,0,0,0,0,0,0,0,0,0,0,0]

	for value in values:
		x = Inputnumber//value
		coefficients[values.index(value)] = x
		Inputnumber = Inputnumber%value

	for value in values:
		romanstring = romanstring + romandict[value]*coefficients[values.index(value)]

	return(romanstring)
