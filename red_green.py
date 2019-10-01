from PIL import Image

def getcolor(filename):
	im=Image.open(filename)
	pix=im.load()
	imtuple=im.size
	l=imtuple[0]
	b=imtuple[1]
	countred=0
	countgreen=0
	# Introduced error margin to reduce the error.
	errormargin=25
	for i in range(l):
		for j in range(b):
			temptuple=pix[i,j]
			#pixel[i,j] return (R,G,B)
			if(temptuple[0]>temptuple[1]+errormargin):
				countred=countred+1
			if(errormargin+temptuple[0]<temptuple[1]):
				countgreen=countgreen+1
	# print("countred=",countred)
	# print("countgreen=",countgreen)
	if(countred>=countgreen):
		return "RED"
	else:
		return "GREEN"

# print(getcolor("./data/good/7.jpg"))
# print(getcolor("./data/good/12.jpg"))
# print(getcolor("./data/good/3.jpg"))
# print(getcolor("./data/good/48.jpg"))
# print(getcolor("./data/good/32.jpg"))
# print(getcolor("./data/good/33.jpg"))
