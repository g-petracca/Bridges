import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('oneseg_mw','oneseg_mw')
G.edge['oneseg_mw']['oneseg_mw']['write-read'] = '[open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][append read][write read]'
G.edge['oneseg_mw']['oneseg_mw']['fill'] = 'red'
app = Viewer(G)
app.mainloop()