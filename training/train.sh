#!/bin/bash

tesseract meter.MeterChar.exp0.jpg meter.MeterChar.exp0.box nobatch box.train
 
unicharset_extractor meter.MeterChar.exp0.box
 
# font name <italic> <bold> <fixed> <serif> <fraktur>
echo "MeterChar 0 0 0 0 0" > font_properties
 
shapeclustering -F font_properties -U meter.MeterChar.exp0.box.tr
 
mftraining -F font_properties -U unicharset -O meter.unicharset meter.MeterChar.exp0.box.tr
 
cntraining meter.MeterChar.exp0.box.tr
 
 
# prefix "relevant" files with our language code
mv inttemp meter.inttemp
mv normproto meter.normproto
mv pffmtable meter.pffmtable
mv shapetable meter.shapetable
combine_tessdata meter.
 
# copy the created meter.traineddata to the tessdata folder
# so tesseract is able to find it
sudo cp meter.traineddata /usr/local/share/tessdata/
