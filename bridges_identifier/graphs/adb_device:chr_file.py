import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('adbd','adbd')
G.edge['adbd']['adbd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][open open][open open][write read][append read][write read][open open]'
G.add_edge('adbd','adbd')
G.edge['adbd']['adbd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][open open][open open][write read][append read][write read][open open][write read]'
G.edge['adbd']['adbd']['fill'] = 'red'
G.add_edge('adbd','adbd')
G.edge['adbd']['adbd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][open open][open open][write read][append read][write read][open open][write read][append read]'
G.add_edge('shell','adbd')
G.edge['shell']['adbd']['write-read'] = '[write read][add_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read]'
G.edge['shell']['adbd']['fill'] = 'red'
G.add_edge('shell','adbd')
G.edge['shell']['adbd']['write-read'] = '[write read][add_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][append read]'
app = Viewer(G)
app.mainloop()