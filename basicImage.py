from matplotlib import pyplot
from matplotlib.image import imread
folder = "../intput/dogs-vs-cats.test1.zip/"
for i in range (9):
    pyplot.subplot(330 + 1 + i)
    filename = folder +'dog' + str(i) + '.jpg'
    image = imread(filename)
    pyplot.imshow(image)
pyplot.show()
