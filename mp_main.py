#coding: utf-8

import io
import time
from mpimageprocessorlib import MPImageProcessor 

#
# main starts here
#

proc = MPImageProcessor()
proc.getPictureFromCamera(2)
proc.getProperties()
proc.selectRegion((500,400,1100,500))
proc.showSelection()
proc.save("cropmeter2.jpg",'selection')

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
