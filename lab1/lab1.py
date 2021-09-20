from numpy import unique
from numpy import where
from sklearn.datasets import make_classification
from sklearn.datasets import make_blobs
from sklearn.cluster import Birch
from sklearn.cluster import KMeans
from sklearn.cluster import MiniBatchKMeans
from matplotlib import pyplot
import statistics
import numpy

data1X = []
data1Y = []
data2X = []
data2Y = []

# генеруємо перший кластер
data1 = numpy.random.normal(1, 3, size=(1000, 2))
print("First dataset:")
# генеруємо перший кластер
print(data1)
data2 = numpy.random.normal(4, 3, size=(1000, 2))
print("Second dataset:")
print(data2)
# об'єднуємо два кластери в один набір даних
data = numpy.vstack((data1, data2))
# визначаємо модель кластеризаціїї
model = Birch(threshold=0.01, n_clusters=2)
#model = KMeans(n_clusters=2)
#model = MiniBatchKMeans(n_clusters=2)
# навчання моделі
model.fit(data)
# визначення приналежності до кластера
yhat = model.predict(data)
# визначення кількості кластерів
clusters = unique(yhat)

# кластеризація даних за виведення кластерів на графік
for cluster in clusters:
	# визначення індексів елементів певного кластера
	row_ix = where(yhat == cluster)
	# створення діаграми розсіювання для кожного кластера
	pyplot.scatter(data[row_ix, 0], data[row_ix, 1])
    # розділення даних кожного кластера на координати X та Y
	if (cluster == 0):
		data1X = data[row_ix, 0].flatten()
		data1Y = data[row_ix, 1].flatten()
	else:
		data2X = data[row_ix, 0].flatten()
		data2Y = data[row_ix, 1].flatten()
# обчислення середнього значення
print("Mean:")
print("First dataset:")
print(statistics.mean(data1X), "\t", statistics.mean(data1Y))
print("Second dataset:")
print(statistics.mean(data2X), "\t", statistics.mean(data2Y))
print("")

# обчислення моди
print("Mode:")
print("First dataset:")
print(statistics.mode(data1X), "\t", statistics.mode(data1Y))
print("Second dataset:")
print(statistics.mode(data2X), "\t", statistics.mode(data2Y))
print("")

# обчислення медіани
print("Median:")
print("First dataset:")
print(statistics.median(data1X), "\t", statistics.median(data1Y))
print("Second dataset:")
print(statistics.median(data2X), "\t", statistics.median(data2Y))
print("")

# обчислення середньоквадратичного відхилення
print("Stdev:")
print("First dataset:")
print(statistics.stdev(data1X), "\t", statistics.stdev(data1Y))
print("Second dataset:")
print(statistics.stdev(data2X), "\t", statistics.stdev(data2Y))
print("")

# виведення графіка
pyplot.show()

