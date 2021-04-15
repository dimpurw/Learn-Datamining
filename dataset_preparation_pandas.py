# NOMER 1
import pandas as pd
df = pd.read_csv('iris.csv')
print(df)


# NOMER 2
Vlama = df[['sepal.length','sepal.width','petal.length','petal.width']]
normalisasi = (Vlama - Vlama.min()) / (Vlama.max() - Vlama.min())
normalisasi = normalisasi.join(df[['variety']])
print(normalisasi)


# NOMER 3 
centroid = lambda centroid: normalisasi[normalisasi['variety'] == centroid].mean()
centroid_setosa = centroid('Setosa')
print(centroid_setosa)
print('=================================')
centroid_versicolor = centroid('Versicolor')
print(centroid_versicolor)
print('=================================')
centroid_virginica = centroid('Virginica')
print(centroid_virginica)
print('=================================')



# NOMER 4
df = pd.read_csv('iristesting.csv')
print(df)
Vlamatest = df[['sepal.length','sepal.width','petal.length','petal.width']]
normalisasitest = (Vlamatest - Vlama.min()) / (Vlama.max() - Vlama.min())
normalisasitest = normalisasitest.join(df[['variety']])
print(normalisasitest)


# NOMER 5
import math
def euclidean_distance(data1,data2):
	distance = 0
	for name, values in data1.iteritems():
		distance += (data1[name] - data2[name])**2
	return math.sqrt(distance)

predictTrue = 0
predictWrong = 0
ss = []
vc = []
vg = []
for index, data2 in normalisasitest.iterrows():
	setosa = euclidean_distance(centroid_setosa,data2)
	versicolor = euclidean_distance(centroid_versicolor,data2)
	virginica = euclidean_distance(centroid_virginica,data2)
	ss.append(setosa)
	vc.append(versicolor)
	vg.append(virginica)
	if setosa < versicolor and setosa < virginica:
		print('setosa')
		if data2['variety'] == 'Setosa':
			predictTrue += 1
		else:
			predictWrong += 1
	elif versicolor < virginica:
		print('versicolor')
		if data2['variety'] == 'Versicolor':
			predictTrue += 1
		else:
			predictWrong += 1
	else:
		print('virginica')
		if data2['variety'] == 'Virginica':
			predictTrue += 1
		else:
			predictWrong += 1
a = pd.DataFrame({
	"Setosa": ss,
	"Versicolor": vc,
	"Virginica": vg
})
print(a)


# NOMER 6
predict = lambda predictTrue,predictWrong: predictTrue/(predictTrue+predictWrong)*100
print(f"hasil presentase prediksi benar adalah",predict(predictTrue,predictWrong),"%")