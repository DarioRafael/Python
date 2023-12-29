import matplotlib.pyplot as plt 

x = list( range(1, 7) )
y = [3,5,6,2,3,0]
z = [2,3,3,4,2,1]

plt.plot(x,y,marker="o")
plt.plot(x,z,marker="o")

plt.title("Notas matematicas", fontsize=24)
plt.xlabel("Pruebas", fontsize=14)
plt.ylabel("Notas", fontsize=14)
plt.show()