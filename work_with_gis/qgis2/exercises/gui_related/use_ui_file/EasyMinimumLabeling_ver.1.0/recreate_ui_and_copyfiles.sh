#!/bin/bash

cd /home/tao/Documents/qgis/development/test/exercises/gui_related/use_ui_file/EasyMinimumLabeling/linux_ui/dialog/
pyuic4 -o ui_ver2.0.py EasyMinimumLabeling_ver2.0_seperate.ui
cp ./ui_ver2.0.py ../../ui.py

cd ../../
cp -r ./* /home/tao/.qgis2/python/plugins/EasyMinimumLabeling/