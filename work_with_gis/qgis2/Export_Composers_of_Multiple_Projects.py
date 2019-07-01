from PyQt4.QtCore import QFileInfo
import os

projectPaths = []
root = 'C:/Users/share1/Documents/lu_temp/qgis_batch/hira/projects/'
path = os.listdir(root)
for file in path:
    if file.endswith(".qgs"):
        projectPaths.append(root + file)
#print projectPaths
#print len(path_list)


# Your settings

folder = 'C:/Users/share1/Documents/lu_temp/qgis_batch/hira/img/'#'/path/to/export_folder/'
extension = '.png' # Any extension supported by the plugin

# Some useful object instances that we need
mp = qgis.utils.plugins['MapsPrinter']
project = QgsProject.instance()

# Do the work!
for projectPath in projectPaths:
    iface.newProject() # Needed to reset composer manager
    project.read( QFileInfo( projectPath ) )
    for composer in iface.activeComposers():
        title = composer.composerWindow().windowTitle()
        mp.exportCompo( composer, folder, title, extension )

