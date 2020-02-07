def main ():
  file = getAFile()
  image = makeImage(file)
  changeDot(image)
  displayImage(image)
  #showInfo(image)

def changeDot(image):
  pixel_1 = getPixel(image, 100, 102)
  pixel_2 = getPixel(image, 101, 103)
  pixel_3 = getPixel(image, 20, 20)
  pixel_4 = getPixel(image, 40, 40)
  newColor = makeColor (255, 255, 255)
  
  setColor(pixel_1, newColor)
  setColor(pixel_2, newColor)
  setColor(pixel_3, newColor)
  setColor(pixel_4, newColor)
def getAFile():
  file = pickAFile()
  return file  

def makeImage(file):
  image = makePicture(file)
  return image

def displayImage(image):
  show(image)
      
def showInfo(image):
  printNow("beach.jpn")
  printNow(getWidth(image))
  printNow(getHeight(image))
  
  pixel= getPixel (image, 150, 80)
  printNow(pixel)
  printNow(getColor(pixel))
main()