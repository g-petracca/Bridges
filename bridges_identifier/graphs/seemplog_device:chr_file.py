import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('seempd','seempd')
G.edge['seempd']['seempd']['write-read'] = '[open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('seempd','seempd')
G.edge['seempd']['seempd']['write-read'] = '[open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['seempd']['seempd']['fill'] = 'red'
G.add_edge('seempd','seempd')
G.edge['seempd']['seempd']['write-read'] = '[open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
app = Viewer(G)
app.mainloop()