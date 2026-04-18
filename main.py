import math 

class CodeSolver():

	def __init__(self):
		self.rlc = None
		self.value = None
		self.solution = None #pico
		self.unit = None #FHO


	def prompter(self):
		self.rlc : str = input("RLC?:  ").upper()
		self.value : str = input("3 digit code: ").upper()

		if not (self.rlc in {"R","L","C"} and (len(self.value) == 3)):
			print("Bad input, please enter again\n")
			self.prompter()



	def controller(self):
		self.prompter()

		match self.rlc:
			case "C":
				self.unit = "F"
				self.solveCap()
			case "L":
				self.unit = "H"
				self.solveInd() 
			case _:
				self.prompter()

		self.format_output()

		if input("Again? (Y/N):  ") != "Y":
			print("<-")
		else: 
			self.controller()	


	def solveCap(self):
		A,B,C = map(int, self.value)
		self.solution = (10*A + B) * (10**C)

	def solveInd(self):
		A,B,C = map(int, self.value)
		self.solution = (10*A + B) * (10**C) * 1_000_000

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
		self.solution = None
		self.prefixes = ["p", "n", "u", "m", "", "k", "M"]

	def prompter(self):
		self.rlc = input("RLC?: ").upper()  # Model after other prompter
		self.value = int(input("Enter value: "))
		self.prefix = input("Enter prefix: ")

		if not ((self.rlc in {"R","L","C"}) and (self.prefix in self.prefixes)):
			print("Invalid input")
			self.prompter()


	def format_output(self):
		print(f"\n   {self.solution}\n")

	def controller(self):
		self.prompter()

		match self.rlc:
			case "L":
				self.solveInd()
			case "C":
				self.solveCap()
			case _:
				self.prompter()

		self.format_output()

		again = input("Again? (Y/N)")
		if again.upper() != "Y":
			print("<-")
		else: 
			self.controller()

	def solveInd(self):
		for i, prefix in enumerate(self.prefixes):
			if self.prefix == prefix:
				self.solution = f"{self.value}{(i*3)-5}" if self.prefix == "u" else f"{self.value}{(i*3)-6}"
				break

	def solveCap(self):
		for i, prefix in enumerate(self.prefixes):
			if self.prefix == prefix:
				self.solution = f"{self.value}{(i*3)}"
				break

def lead_controller():
	cont = True
	while(cont == True):
		version = input("| 1: Value to code |\n| 2: Code to value |\n| 3: Quit          |\n   ->")
		match version:
			case "1":
				vsolve = ValueSolver()
				vsolve.controller()
			case "2":
				csolve = CodeSolver()
				csolve.controller()
			case "3":
				cont = False
				break
			case _:
				print("Invalid input \n")

lead_controller()
