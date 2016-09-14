import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('usb_uicc_daemon','usb_uicc_daemon')
G.edge['usb_uicc_daemon']['usb_uicc_daemon']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open]'
G.add_edge('usb_uicc_daemon','usb_uicc_daemon')
G.edge['usb_uicc_daemon']['usb_uicc_daemon']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read]'
G.edge['usb_uicc_daemon']['usb_uicc_daemon']['fill'] = 'red'
G.add_edge('usb_uicc_daemon','usb_uicc_daemon')
G.edge['usb_uicc_daemon']['usb_uicc_daemon']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read]'
app = Viewer(G)
app.mainloop()