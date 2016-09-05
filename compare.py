from PIL import Image as pImage
import numpy

TRESHOLD = 60
BLOCK_SIZE = 20
BASE_DIR = '/'

def load(filename):
	img = pImage.open(filename)
	small = img.resize((BLOCK_SIZE, BLOCK_SIZE),pImage.BILINEAR)
	t_data = numpy.array([sum(list(x)) for x in small.getdata()])
	del img, small
	return t_data

def compareImages(first, second):
	return sum(1 for x in first - second if abs(x) > TRESHOLD)

def doit(n):
	first = load(BASE_DIR + str(n.pop()))
	second = load(BASE_DIR + str(n.pop()))
	result = compareImages(first, second)

	if result == 0:
		return "This is identical images"
	if result < 240:
		return "This is similar images"
	else:
		return "This isn't similar images"
