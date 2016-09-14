import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('netmgrd','netmgrd')
G.edge['netmgrd']['netmgrd']['write-read'] = '[open open]'
G.add_edge('netmgrd','netmgrd')
G.edge['netmgrd']['netmgrd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('netmgrd','netmgrd')
G.edge['netmgrd']['netmgrd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['netmgrd']['netmgrd']['fill'] = 'red'
G.add_edge('netmgrd','netmgrd')
G.edge['netmgrd']['netmgrd']['write-read'] = '[open open][setattr getattr][write read][append read]'
app = Viewer(G)
app.mainloop()