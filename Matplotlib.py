import matplotlib.pyplot as plt 
import numpy as np 

xpoints = np.array([0,6])
ypoints= np.array([0,250])

plt.plot(xpoints,ypoints,'or')
plt.show()

x=np.array([1,2,6,8])
y=np.array([3,8,1,10])
plt.plot(x,y,'m')
plt.show()

y1=np.array([3,8,1,10])
plt.plot(y1, marker='*',ms=20, mec='r')
plt.show()


plt.plot(y1,linewidth="20.5")
plt.show()

#Dos graficas 
r1= np.array([3,8,1,10])
r2= np.array([6,2,7,11])

plt.plot(r1)
plt.plot(r2)
plt.show()

#Grafico de lineas 
x=np.array([80,85,90,95,100,105,110,115,120,125])
y=np.array([240,250,260,270,280,290,300,310,320,330])

font1={'family':'serif','color':'blue','size':20}
font2={'family':'serif','color':'darkred','size':20}

plt.plot(x,y)
plt.title("Sports watch Data",fontdict=font1)
plt.xlabel("Average Pulse",fontdict=font2)
plt.ylabel("Calorie Burnage",fontdict=font2)
plt.grid()
plt.show()

#Grafico de barras 
x=["A","B","C"]
y=[3,5,1]

fig, ax=plt.subplots()
#ax.bar(x=x,height=y) #Vertical 
ax.barh(x,width=y) #Horizontal 
plt.show()

#Grafica de pastel 

manzanas=[20,10,25,30]
nombres=["Ana","Juan","Diana","Catalina"]
plt.pie(manzanas,labels=nombres,autopct="%0.1f%%")
plt.axis("equal")
plt.show()