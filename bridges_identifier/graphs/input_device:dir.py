import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('geomagneticd','lpm')
G.edge['geomagneticd']['lpm']['write-read'] = '[open open]'
G.add_edge('geomagneticd','lpm')
G.edge['geomagneticd']['lpm']['write-read'] = '[open open][write read]'
G.edge['geomagneticd']['lpm']['fill'] = 'red'
G.add_edge('geomagneticd','lpm')
G.edge['geomagneticd']['lpm']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('geomagneticd','lpm')
G.edge['geomagneticd']['lpm']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('healthd','lpm')
G.edge['healthd']['lpm']['write-read'] = '[setopt getopt][open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('healthd','lpm')
G.edge['healthd']['lpm']['write-read'] = '[setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read]'
G.edge['healthd']['lpm']['fill'] = 'red'
G.add_edge('healthd','lpm')
G.edge['healthd']['lpm']['write-read'] = '[setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][add_name search]'
G.add_edge('healthd','lpm')
G.edge['healthd']['lpm']['write-read'] = '[setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('lpm','lpm')
G.edge['lpm']['lpm']['write-read'] = '[open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('lpm','lpm')
G.edge['lpm']['lpm']['write-read'] = '[open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][open open][write read]'
G.edge['lpm']['lpm']['fill'] = 'red'
G.add_edge('lpm','lpm')
G.edge['lpm']['lpm']['write-read'] = '[open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search]'
G.add_edge('lpm','lpm')
G.edge['lpm']['lpm']['write-read'] = '[open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('mmi','lpm')
G.edge['mmi']['lpm']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('mmi','lpm')
G.edge['mmi']['lpm']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['mmi']['lpm']['fill'] = 'red'
G.add_edge('mm-qcamera-daemon','lpm')
G.edge['mm-qcamera-daemon']['lpm']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('mm-qcamera-daemon','lpm')
G.edge['mm-qcamera-daemon']['lpm']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read]'
G.edge['mm-qcamera-daemon']['lpm']['fill'] = 'red'
G.add_edge('mm-qcamera-daemon','lpm')
G.edge['mm-qcamera-daemon']['lpm']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][add_name search]'
G.add_edge('mm-qcamera-daemon','lpm')
G.edge['mm-qcamera-daemon']['lpm']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('sensorhubservice','lpm')
G.edge['sensorhubservice']['lpm']['write-read'] = '[open open]'
G.add_edge('sensorhubservice','lpm')
G.edge['sensorhubservice']['lpm']['write-read'] = '[open open][write read]'
G.edge['sensorhubservice']['lpm']['fill'] = 'red'
G.add_edge('sensorhubservice','lpm')
G.edge['sensorhubservice']['lpm']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('sensorhubservice','lpm')
G.edge['sensorhubservice']['lpm']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('shell','lpm')
G.edge['shell']['lpm']['write-read'] = '[open open]'
G.add_edge('shell','lpm')
G.edge['shell']['lpm']['write-read'] = '[open open][write read]'
G.edge['shell']['lpm']['fill'] = 'red'
G.add_edge('shell','lpm')
G.edge['shell']['lpm']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('shell','lpm')
G.edge['shell']['lpm']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('system_server','lpm')
G.edge['system_server']['lpm']['write-read'] = '[setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('system_server','lpm')
G.edge['system_server']['lpm']['write-read'] = '[setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read]'
G.edge['system_server']['lpm']['fill'] = 'red'
G.add_edge('system_server','lpm')
G.edge['system_server']['lpm']['write-read'] = '[setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search]'
G.add_edge('system_server','lpm')
G.edge['system_server']['lpm']['write-read'] = '[setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search]'
app = Viewer(G)
app.mainloop()