import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('lhd','lhd')
G.edge['lhd']['lhd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][write read][append read][open open]'
G.add_edge('lhd','lhd')
G.edge['lhd']['lhd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][write read][append read][open open][write read]'
G.edge['lhd']['lhd']['fill'] = 'red'
G.add_edge('lhd','lhd')
G.edge['lhd']['lhd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][write read][append read][open open][write read][append read]'
app = Viewer(G)
app.mainloop()