import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('syscope_app','syscope_app')
G.edge['syscope_app']['syscope_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read]'
G.edge['syscope_app']['syscope_app']['fill'] = 'red'
app = Viewer(G)
app.mainloop()