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


# ImageProcess Class
# 
# Description:
#
#   This class is a general use image process based on the PIL, pytesseract and the
#   picamera libraries. It allows high-level operations on images that can be loaded
#   in the class or acquired from the Pi Camera.
#
#   An imageprocessor is created for each image. In addition to the image, it can record
#   the selection of a subimage. It records it attributes such as name and size. It can
#   also save the image or its selection on the drive.


class MPImageProcessor(object):

    def __init__(self, imgname=""):
        self.imgname = imgname
        self.img = None
        self.loaded = False
        self.size = (0,0)
        self.height = 0
        self.selection = None
        self.cameraSet = False
        self.camera = None

    #
    # Loads and displays an image. If no file name is give, it uses the current
    # image in memory.
    
    def loadandshow(self, name=""):
        self.open(name)
        self.img.show()
    
    #
    # Display the image in memory. Returns an error if none is available.
    
    def show(self):
        if self.loaded == True:
            self.img.show()
        else:
            print("No image loaded")

    #
    # Display the current selection if one if available. Returns an error if none is available. 
        
    def showSelection(self):
        if self.loaded == True and self.selection != None:
            self.selection.show()
        else:
            print("No image loaded or region selected")
    
    #
    # Returns the name of the image in memory and the size
    
    def getProperties(self):
        if self.loaded == True:
            print("Name: %s"%self.imgname)
            print("Width, Height:",self.size)
        else:
            print("getProperties: No image loaded")

    #
    # Opens an image given a path name
    
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

    #
    # Selects a regions in the image given a regionbox, e.g. (500,400,1100,500)

    def selectRegion(self,regionbox):
        if self.loaded == True:
            self.selection = self.img.crop(regionbox)
        else:
            print("getProperties: No image loaded")
    
    #
    # Finds a series of number digits in the image. 
       
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
            
    #
    # Saves the images given a path name

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

    #
    # Sets the Pi Camera if one is available on the RPi

    def setCamera(self,camera=None):
        try:
            self.camera = PiCamera()
            self.cameraSet = True
            return self.camera
        except PiCameraError:
            print("Camera not available")

    #
    # Takes a picture from the PiCamera. The image is given a default name 'picamera'
    # The recording format is JPEG.
            
    def getPictureFromCamera(self,sleeptime=2):
        self.setCamera();
        stream = io.BytesIO()
        with self.camera:
            self.camera.start_preview()
            time.sleep(sleeptime)
            self.camera.capture(stream, format='jpeg')
        # rewind stream to beginning
        stream.seek(0)
        self.img = Image.open(stream)
        self.imgname = "picamera"
        self.loaded = True

#
########################################

# MPImageProcessorTest Class
# 
# Description:
# 
# This class is a tester for ImageProcessor that execute a set of scenarios. The 
# scenario are:
#
#   - Read a test image form the disk and extract the number from it
#   - Start the Pi Camera and attempts to record an image
#
#

class MPImageProcessorTest(object):
    
    def __init__(self):
        # define the test data
        self.imageTestName1 = 'pics/'
        self.MPImageProcessor(self.imageTestName1);
        #self.imageTestName2


    #def ReadTestImageandRecognizeNumber(self):

        
            



        





    

