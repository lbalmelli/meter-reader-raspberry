#coding: utf-8
from picamera import PiCamera
from time import sleep
try:
    import Image
except ImportError:
    from PIL import Image
import sys
import pytesseract
import io
import time

pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

class ImageProcessor(object):

    def __init__(self, imgname=""):
        self.imgname = imgname
        self.img = None
        self.loaded = False
        self.size = (0,0)
        self.height = 0
        self.selection = None
        self.cameraSet = False
        self.camera = None
    
    def loadandshow(self, name=""):
        self.open(name)
        self.img.show()
        
    def show(self):
        if self.loaded == True:
            self.img.show()
        else:
            print("No image loaded")

    def showSelection(self):
        if self.loaded == True and self.selection != None:
            self.selection.show()
        else:
            print("No image loaded or region selected")
            
    def getProperties(self):
        if self.loaded == True:
            print("Name: %s"%self.imgname)
            print("Width, Height:",self.size)
        else:
            print("getProperties: No image loaded")

    def open(self, name=""):
        if name != "":
            self.imgname = name
        else:
            if self.imgname == "":
                print("No filename available")

        # We have a valid filename here
        print("loading name %s..."%self.imgname)
        try:
            self.img = Image.open(self.imgname)
            self.loaded = True
            self.size = self.img.size
        except IOError as err:
            print("IOError Exception: Filename is invalid!")

    def selectRegion(self,regionbox):
        if self.loaded == True:
            self.selection = self.img.crop(regionbox)
        else:
            print("getProperties: No image loaded")
       
    def readMeter(self):
        if self.loaded == True:
            if self.selection != None:
                # If there is a selection, read characters on the selection
                print(pytesseract.image_to_string(self.selection))
            else:
                # else read characters on the main image
                print(pytesseract.image_to_string(self.img,
                                                  lang=meteer,
                                                  config='--psm 7'))
        else:
            print("No image loaded or region selected")
        
    def save(self,filename ="", imgtype=""):
        if filename == "":
            print("No filename available")
        else:
            if imgtype == 'selection':
                self.selection.save(filename)
            elif imgtype == 'original':
                self.img.save(filename)
            else:
                print("Use 'selection' or 'original' to specify image to save to file.")

    def setCamera(self,camera=None):
        try:
            self.camera = PiCamera()
            self.cameraSet = True
            return self.camera
        except PiCameraError:
            print("Camera not available")
            
    def getPictureFromCamera(self):
        self.setCamera();
        stream = io.BytesIO()
        with self.camera:
            self.camera.start_preview()
            time.sleep(2)
            self.camera.capture(stream, format='jpeg')
        # rewind stream to beginning
        stream.seek(0)
        self.img = Image.open(stream)
        self.imgname = "picamera"
        self.loaded = True


#
# main starts here
#

proc = ImageProcessor()
proc.getPictureFromCamera()
proc.getProperties()
proc.selectRegion((500,400,1100,500))
proc.showSelection()
proc.save("pics/cropmeter2.jpg",'selection')
proc.readMeter()

#img = ImageProcessor("./pics/ugigasmeterG4.jpg")
#img = ImageProcessor("./pics/b5A7j.png")

#img.open()
#img.getProperties()
#img.show()
#img.selectRegion((280,360,635,415))
#img.showSelection()
#img.readMeter()
#img.save("pics/cropmeter.jpg",'selection')


#from PIL import Image


#pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'
#tessdata_dir_config = '--tessdata-dir "/usr/bin/"'
# use this quote: ' 
#

#print sys.getdefaultencoding()

#

#camera.rotation = 180
#camera.start_preview()
#sleep(5)
#camera.capture('/home/pi/Laurent/Dev/PiCamera/pics/img1.jpg')
#filenames = []
#filenames.append('/home/pi/Laurent/Dev/PiCamera/pics/img1.jpg')
#img = Image.open('/home/pi/Laurent/Dev/PiCamera/pytesseract/src/test.png')
#img.load()
#print pytesseract.image_to_string(img,config='outputbase digits')
#print pytesseract.image_to_string(img)
#camera.stop_preview()

