import numpy as np
#Array de una dimension

al=np.array([1,2,3])
print(al)

#Array de dos dimensiones 
a2=np.array([[1,2,3],[4,5,6]])
print(a2)

#Array de 3 dimensiones 
a3=np.array([[[1,2,3,],[4,5,6]],[[7,8,9],[10,11,12]]])
print(a3)

#Matriz de cero 
a=np.zeros((2,3))
print(a)

#Matriz identidad 
i=np.identity(3)
print(i)

print(np.arange(1,10,2))

print(np.linspace(0,10,5))

print(np.ones((3,3)))

i.dtype
i.shape

#acceder a los elementos de un array
vector=np.array([[1,2,3],[4,5,6]])
print(vector[1,1])
print(vector[1],[1])
print(vector[:,0:2])
print(vector[(vector%2==0) & (vector>2)])