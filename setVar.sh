#!/bin/bash

# set variable for tesseract to find local training data
echo Setting variables for Tesseract...
export TESSDATA_PREFIX=/usr/local/share/tessdata

#
# Test with Tesseract
#

# tesseract pics/cropmeter.jpg output -l meter

