import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('domain','vold')
G.edge['domain']['vold']['write-read'] = '[setattr getattr][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr]'
app = Viewer(G)
app.mainloop()