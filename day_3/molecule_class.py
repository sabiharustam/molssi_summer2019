class Molecule:
	# Init is the method to build the object.
	# Since python is dictionary based. init needs to know where it is coming from.
	def __init__(self, name, symbols, charge=0.0):
		if isinstance(name, str):
			self.name = name
		else:
			raise TypeError(F'Expects string object, instead {type(name)} is passed')
		self.charge  = charge
		self.symbols = symbols
	
	
	def __str__(self):
		return 'name: '+ self.name + '\ncharge: ' + str(self.charge) + '\nsymbols: ' + str(self.symbols)

water = Molecule("water_molecule", ["O", "H", "H"])
print(water)
print(water.__dict__)

helium = Molecule("helium", ["He"], charge = "0.0")
print(helium)
print(helium.__dict__)

# hydrogen = Molecule(0.0, 0.0, ["H"])

		