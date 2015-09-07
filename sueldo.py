def comicion(sueldo, *ventas):
	"""
	>>> comicion(10,35,56)
	19.1
		
	"""
	sueldoFinal = 0
	sueldoFinal += sueldo
	for v in ventas:
		sueldoFinal += (v * .10)
	
	print (sueldoFinal)
	
	
	

if __name__=="__main__":
	import doctest
	doctest.testmod()
		