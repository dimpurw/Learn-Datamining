# NOMER 4
import xlrd
import numpy as np
path = "datasetiris.xlsx"
i = xlrd.open_workbook(path)
a = i.sheet_by_name('Sheet1')
a = i.sheet_by_index(0)
data_setosa = np.empty([0,7])
data_virginica = np.empty([0,7])
data_versicolor = np.empty([0,7])
data_unknown = np.empty([0,7])
for i in range(4,a.nrows):
	if i < 49:
		data_setosa = np.concatenate((data_setosa,[a.row_values(i,3)]))
	elif i > 48 and i < 94:
		data_virginica = np.concatenate((data_virginica,[a.row_values(i,3)]))
	elif i > 93 and i < 139:
		data_versicolor = np.concatenate((data_versicolor,[a.row_values(i,3)]))
	elif i > 138 and i < 154:
		data_unknown = np.concatenate((data_unknown,[a.row_values(i,3)]))
setosa = data_setosa[:,:4].astype(float)
virginica = data_virginica[:,:4].astype(float)
versicolor = data_versicolor[:,:4].astype(float)
unknown = data_unknown[:,:4].astype(float)
print(setosa)
print('================================================')
print(virginica)
print('================================================')
print(versicolor)
print('================================================')
print(unknown)

# NOMER 5
import matplotlib.pyplot as plt
plt.scatter(setosa[:,3], setosa[:,0], color = 'red', label='Setosa')
plt.scatter(versicolor[:,3], versicolor[:,0], color = 'green', label='Versicolor')
plt.scatter(virginica[:,3], virginica[:,0], color = 'blue', label='Virginica')
plt.scatter(unknown[:,3], unknown[:,0], color = 'yellow', label='Unknown')
plt.title("Sepal Length dan Petal Width")
plt.xlabel("Sepal Length")
plt.ylabel("Petal Width")
plt.legend()
plt.show()

plt.scatter(setosa[:,2], setosa[:,1], color = 'red', label='Setosa')
plt.scatter(versicolor[:,2], versicolor[:,1], color = 'green', label='Versicolor')
plt.scatter(virginica[:,2], virginica[:,1], color = 'blue', label='Virginica')
plt.scatter(unknown[:,2], unknown[:,1], color = 'yellow', label='Unknown')
plt.title("Sepal Width dan Petal Length")
plt.xlabel("Sepal Width")
plt.ylabel("Petal Length")
plt.legend()
plt.show()

plt.scatter(setosa[:,3], setosa[:,0], color = 'red', label='Setosa')
plt.scatter(versicolor[:,3], versicolor[:,0], color = 'green', label='Versicolor')
plt.scatter(virginica[:,3], virginica[:,0], color = 'blue', label='Virginica')
plt.scatter(unknown[:,3], unknown[:,0], color = 'yellow', label='Unknown')
plt.title("Sepal Length dan Petal Width")
plt.xlabel("Sepal Length")
plt.ylabel("Petal Width")
plt.legend()
plt.show()

plt.scatter(setosa[:,3], setosa[:,1], color = 'red', label='Setosa')
plt.scatter(versicolor[:,3], versicolor[:,1], color = 'green', label='Versicolor')
plt.scatter(virginica[:,3], virginica[:,1], color = 'blue', label='Virginica')
plt.scatter(unknown[:,3], unknown[:,1], color = 'yellow', label='Unknown')
plt.title("Sepal Length dan Petal Length")
plt.xlabel("Sepal Length")
plt.ylabel("Petal Length")
plt.legend()
plt.show()


# NOMER 8
import matplotlib.pyplot as plt
label = np.array(['Petal Width','Petal Length','Sepal Width','Sepal Length'])
ysetosa = [setosa[1:,0],setosa[1:,1],setosa[1:,2],setosa[1:,3]]
plt.plot(label, ysetosa, color = 'red')

yversicolor = [versicolor[1:,0],versicolor[1:,1],versicolor[1:,2],versicolor[1:,3]]
plt.plot(label, yversicolor, color = 'green')

yvirginica = [virginica[1:,0],virginica[1:,1],virginica[1:,2],virginica[1:,3]]
plt.plot(label, yvirginica, color = 'blue')
plt.show()