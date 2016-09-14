import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('cnd','lmkd')
G.edge['cnd']['lmkd']['write-read'] = '[write read][write read]'
G.edge['cnd']['lmkd']['fill'] = 'red'
G.add_edge('lmkd','lmkd')
G.edge['lmkd']['lmkd']['write-read'] = '[open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][write read]'
G.edge['lmkd']['lmkd']['fill'] = 'red'
G.add_edge('mpdecision','lmkd')
G.edge['mpdecision']['lmkd']['write-read'] = '[write read][open open][write read][append read][write read]'
G.edge['mpdecision']['lmkd']['fill'] = 'red'
G.add_edge('perfd','lmkd')
G.edge['perfd']['lmkd']['write-read'] = '[write read]'
G.edge['perfd']['lmkd']['fill'] = 'red'
G.add_edge('servicemanager','lmkd')
G.edge['servicemanager']['lmkd']['write-read'] = '[open open][write read][append read][open open][write read][append read][add_name search][remove_name search][add_name search][remove_name search][write read]'
G.edge['servicemanager']['lmkd']['fill'] = 'red'
app = Viewer(G)
app.mainloop()