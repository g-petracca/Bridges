import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('netmgrd','netmgrd')
G.edge['netmgrd']['netmgrd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][write read][add_name search][add_name search][remove_name search][open open][open open][write read][write read][add_name search][add_name search][remove_name search][write read]'
G.edge['netmgrd']['netmgrd']['fill'] = 'red'
app = Viewer(G)
app.mainloop()