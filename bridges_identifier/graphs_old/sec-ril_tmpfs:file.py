import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('sec-ril','sec-ril')
G.edge['sec-ril']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read]'
G.edge['sec-ril']['sec-ril']['fill'] = 'red'
app = Viewer(G)
app.mainloop()