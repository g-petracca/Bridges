import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('geomagneticd','geomagneticd')
G.edge['geomagneticd']['geomagneticd']['write-read'] = '[open open][add_name search][remove_name search][write read]'
G.edge['geomagneticd']['geomagneticd']['fill'] = 'red'
app = Viewer(G)
app.mainloop()