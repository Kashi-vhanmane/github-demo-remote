#add implementation
def add(x,y):
	return x+y
#subtract implementation
def subract(x,y):
	return x-y  # on master branch
#multiplay implementation
def multiplay(x,y):
	return x*y  #on bug456
#divide implementation
def divide(x,y):
	if y==0:
		return DIVIDE_BY_0_ERROR
	else:
		return x/y   #on master branch
		
#Square implementation		
def square(x):
	return x*x