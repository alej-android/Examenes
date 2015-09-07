def porcentajes(hombres,mujeres):
	"""
	>>> porcentajes(40,60)
	Hombres: 40.0
	Mujeres: 60.0
		
	"""
	sumaTotal = hombres + mujeres
	porH = (100 * hombres) / sumaTotal
	porM = 100 - porH
	
	print ("Hombres: "+str(porH))
	print ("Mujeres: "+str(porM))
	
	
	

if __name__=="__main__":
	import doctest
	doctest.testmod()
		