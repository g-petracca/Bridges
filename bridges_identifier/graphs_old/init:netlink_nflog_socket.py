import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('init_shell','init_shell')
G.edge['init_shell']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['init_shell']['init_shell']['fill'] = 'red'
app = Viewer(G)
app.mainloop()