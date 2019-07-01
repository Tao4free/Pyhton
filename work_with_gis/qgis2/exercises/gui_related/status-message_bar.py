from qgis.gui import *
#status bar
# show
iface.mainWindow().statusBar().showMessage("Please wait...")

# clear
iface.mainWindow().statusBar().clearMessage()


# message bar
# create a message without a title
# messageBar.pushMessage(text, level=QsgMessageBar.INFO, duration=None
# duration is in second
iface.messageBar().pushMessage("Hello World",
level=QgsMessageBar.INFO, duration=10)

# include a title, use the following method signature:
#messageBar.pushMessage(title, text, level=QgsMessageBar.INFO, duration=None)

# QgsMessageBar.INFO--->
# QgsMessageBar.WARNING, or QgsMessageBar.CRITICAL, 
iface.messageBar().clearWidgets()




