import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('uncrypt','uncrypt')
G.edge['uncrypt']['uncrypt']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read]'
G.edge['uncrypt']['uncrypt']['fill'] = 'red'
app = Viewer(G)
app.mainloop()