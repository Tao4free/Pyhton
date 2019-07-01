lyr=iface.activeLayer()
def myFunction(selFeatures):
    print str(len(selFeatures)) + " features were selected: " + str(selFeatures)

lyr.selectionChanged.connect(myFunction)