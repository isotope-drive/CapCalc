#pylint: disable=W0311
#pylint: disable=C0303

"""
CapCalc, for all (some of) your RLC code needs!
"""

class CodeSolver():
	"""
	Class: CodeSolver()
	Methods: init, prompter, controller, solve_res, solve_cap, solve ind, format_output
	"""

	def __init__(self):
		self.rlc = None
		self.value = None
		self.solution = None #pico
		self.unit = None #FHO
		self.bands = None #List[str]
		self.colors = ["bl","br","r","o","y","gr","b","v","g","w","go"]

	def prompter(self):
		"""
		Method: prompter()
		Params: 
		Description: Controls input loop, calls no functions, deals in class variables
		"""
		self.rlc : str = input("RLC?:  ").upper()

		if self.rlc == "R":
			self.bands : str = input(f"{self.colors} \n Enter color bands (comma seperated): ").split(",")

		else:
			self.value : str = input("3 digit code: ").upper()


	def controller(self):
		"""
		Method: controller()
		Params: 
		Description: Controls class functionality and is interface with lead_controller()
		"""

		self.prompter()

		match self.rlc:
			case "C":
				self.unit = "F"
				self.solve_cap()
			case "L":
				self.unit = "H"
				self.solve_ind() 
			case "R":
				self.unit = "Ohm"
				self.solve_res()
			case _:
				self.prompter()
		self.format_output()

		if input("Again? (Y/N):  ") != "Y":
			print("<-")
		else: 
			self.controller()	

	def solve_res(self):
		"""
		Method: solve_res()
		Params:	
		Description: Solves for resistor value
		"""
		for i, color in enumerate(self.bands): 
			self.bands[i] = self.colors.index(color)
		a,b,c = self.bands
		self.solution = (10*a + b) * (10**c)


	def solve_cap(self):
		"""
		Method: solve_cap()
		Params: 
		Description: Solves for capacitor value
		"""
		a,b,c = map(int, self.value)
		self.solution = (10*a + b) * (10**c)

	def solve_ind(self):
		"""
		Method: solve_ind()
		Params: 
		Description: Solves for inductor values
		"""
		a,b,c = map(int, self.value)
		self.solution = (10*a + b) * (10**c) * 100_000

	def format_output(self):
		"""
		Method: fromat_output()
		Params: 
		Description: formats and prints correct output for corrosponding solution
		"""
		prefixes = ["p", "n", "u", "m", ""]
		r_prefixes = ["","k","M"]

		if self.rlc == "R":
			for i, prefix in enumerate(r_prefixes):
				value = self.solution / (10 ** (3 * i))
				if 1 <= value < 1000:
					print(f"\n{value:.3g} {prefix}{self.unit}\n")
					break

		else:
			for i, prefix in enumerate(prefixes):
			    value = self.solution / (10 ** (3 * i))
			    if 1 <= value < 1000:
			        print(f"\n{value:.3g} {prefix}{self.unit}\n")
			        break


class ValueSolver():
	"""
	Class: ValueSolver()
	Methods: init, prompter, format_output, controller, solve_ind, solve_cap
	Description: Class for Value -> Code
	"""
	def __init__(self):
		self.rlc = None	#str
		self.value = None #str
		self.prefix = None #str
		self.solution = None
		self.prefixes = ["p", "n", "u", "m", "", "k", "M"]
		self.colors = ["bl","br","r","o","y","gr","b","v","g","w","go"]

	def prompter(self):
		"""
		Method: prompter()
		Params: 
		Description: Controls input loop
		"""
		self.rlc = input("RLC?: ").upper()  # Model after other prompter
		self.value = int(input("Enter value: "))
		self.prefix = input("Enter prefix: ")

		if not ((self.rlc in {"R","L","C"}) and (self.prefix in self.prefixes)):
			print("Invalid input")
			self.prompter()


	def format_output(self):
		"""
		Method: format_output()
		Params: 
		Description: Prints solution
		"""
		print(f"\n   {self.solution}\n")

	def controller(self):

		'''
		Method: controller()
		Params:
		Description: Control loop 
		'''
		self.prompter()

		match self.rlc:
			case "L":
				self.solve_ind()
			case "C":
				self.solve_cap()
			case _:
				self.prompter()

		self.format_output()

		again = input("Again? (Y/N)")
		if again.upper() != "Y":
			print("<-")
		else: 
			self.controller()

	def solve_ind(self):
		"""
		Method: solve_ind()
		Params: 
		Description: solve for code for inductor
		"""
		for i, prefix in enumerate(self.prefixes):
			if self.prefix == prefix:
				self.solution = f"{self.value}{(i*3)-5}" if self.prefix == "u" else f"{self.value}{(i*3)-6}"
				break

	def solve_cap(self):
		"""
		Method: solve_cap()
		Params: 
		Description: solve for code for capacitor 
		"""
		for i, prefix in enumerate(self.prefixes):
			if self.prefix == prefix:
				self.solution = f"{self.value}{(i*3)}"
				break

def lead_controller():
	"""
	Function: lead_controller()
	Params:
	Description: main control loop for program.
	"""
	cont = True
	while cont:
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
