PLUGINNAME = EasyMinimumLabeling
PY_FILES = __init__.py EasyMinimumLabeling.py EasyMinimumLabelingDialog.py ui.py
EXTRAS = icon.png metadata.txt
RESOURCE_FILES = resources.py

default: compile

%.py : %.qrc
	pyrcc4 -o $@ $<
	
%.py : %.ui
	pyrcc4 -o ui_$@ $<
	
deploy: compile
	mkdir -p $(HOME)/.qgis2/python/plugins/$(PLUGINNAME)
	cp -vf $(PY_FILES) $(HOME)/.qgis2/python/plugins/$(PLUGINNAME)
	cp -vf $(RESOURCE_FILES) $(HOME)/.qgis2/python/plugins/$(PLUGINNAME)
	cp -vf $(EXTRAS) $(HOME)/.qgis2/python/plugins/$(PLUGINNAME)
