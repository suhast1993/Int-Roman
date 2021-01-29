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




































'''

import math

romans = ["I","V","X","L","C","D","M"]


def rformat(R, n):
	if n == 0:
		return ""
	if n == 1:
		return R
	if n == 2:
		return R+R
	if n ==3:
		return R+R+R
	if n ==4:
		idx = romans.index(R)
		if math.log(romans[idx])%10=0 and romans[idx+1]/romans[idx] in [5,10]:
				N = romans[idx+1]
				return R+N
		else:
			return 


	

def inttoroman(x):
	x = int(x)
	M = x//1000
	Mr = x%1000
	D = Mr//500
	Dr = Mr%500
	C = Dr//100
	Cr = Dr%100
	L = Cr//50
	Lr = Cr%50
	X = Lr//10
	Xr = Lr%10
	V = Xr//5
	Vr = Xr%5
	I = Vr//1

	print(M,D,C,L,X,V,I)
	print(Mr,Dr,Cr,Lr,Xr,Vr)

	romans = [["M", M],["D", D],["C", C],["L", L],["X", X],["V", V],["I", I]]

	finalroman = ""

	for item in romans:
		finalroman = finalroman + str(rformat(item[0], item[1]))

	print(finalroman)




inttoroman(99)
'''