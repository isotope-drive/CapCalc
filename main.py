import math 

class CodeSolver():

	def __init__(self):
		self.rlc = None
		self.value = None
		self.solution = None #pico
		self.unit = None #FHO


		self.prompter()
		self.controller()


	def prompter(self):
		self.rlc : str = input("RLC?:  ").upper()
		self.value : str = input("3 digit code: ").upper()

		if self.rlc.upper() in {"R","L","C"} and (len(self.value) == 3):
			self.rlc = self.rlc #secret area, not sure what to do in this situation
		else:
			print("Bad input, please enter again\n")
			self.prompter()


	def controller(self):

		match self.rlc:
			case "C":
				self.unit = "F"
				self.solveCap()
			case "L":
				self.unit = "H"
				self.solveCap() #it works the same. If you want to fix the naming please do. 


		self.format_output()

		if input("Again? (Y/N):  ") != "Y":
			print("<-")
		else: 
			self.rlc = input("RLC?: ")
			self.value = input("3 digit value: ")
			self.controller()	


	def solveCap(self):
		A,B,C = map(int, self.value)
		self.solution = (10*A + B) * (10**C)

	def format_output(self):
		prefixes = ["p", "n", "u", "m", "", "k", "M"]

		for i, prefix in enumerate(prefixes):
		    value = self.solution / (10 ** (3 * i))
		    if 1 <= value < 1000:
		        print(f"\n{value:.3g} {prefix}{self.unit}\n")
		        break


class ValueSolver():

	def __init__(self):
		self.rlc = None	#str
		self.value = None #str
		self.prefix = None #str
		self.base_value = None #float
		self.PREFIXES = {
		    "p": 1e-12,
		    "n": 1e-9,
		    "u": 1e-6,
		    "m": 1e-3,
		    "": 1,
		    "k": 1e3,
		    "M": 1e6
		}
		self.solution = None

		self.controller()

	def prompter(self):
		self.rlc = input("RLC?: ")
		self.value = input("Enter value: ")
		self.prefix = input("Enter prefix: ")

	def normalize(self): #Used Claude Code for this and encode
	    prefix = self.prefix or ""
	    multiplier = self.PREFIXES.get(prefix, 1)
	    base_value = float(self.value) * multiplier  # value in base units (Farads)

	    # Convert to picofarads for encoding
	    self.base_value = base_value * 1e12

	def encode(self):
	    # base_value is now in picofarads
	    pf = self.base_value

	    exponent = int(math.floor(math.log10(pf))) - 1
	    significand = int(round(pf / (10 ** exponent)))

	    # Handle rounding edge case (e.g. significand hits 100)
	    if significand >= 100:
	        significand //= 10
	        exponent += 1

	    self.solution = f"{significand:02d}{exponent}"

	def format_output(self):
		print(f"{self.solution}")

	def controller(self):
		self.prompter()
		self.normalize()
		self.encode()
		self.format_output()

		again = input("Again? (Y/N)")
		if again.upper() != "Y":
			print("<-")
		else: 
			self.controller()


def lead_controller():
	cont = True
	while(cont == True):
		version = input("1: Value to code\n2: Code to value\n3: Quit\n   ->")
		if version == "1":
			vsolve = ValueSolver()
		elif version == "2":
			csolve = CodeSolver()
		elif version == "3":
			print("Goodbye")
			cont = False
		else:
			"Invalid input \n "

lead_controller()
