import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('vmware_app','vmware_app')
G.edge['vmware_app']['vmware_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['vmware_app']['vmware_app']['fill'] = 'red'
app = Viewer(G)
app.mainloop()