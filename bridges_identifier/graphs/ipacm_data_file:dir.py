import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('ipacm','ipacm')
G.edge['ipacm']['ipacm']['write-read'] = '[open open]'
G.add_edge('ipacm','ipacm')
G.edge['ipacm']['ipacm']['write-read'] = '[open open][add_name search]'
G.add_edge('ipacm','ipacm')
G.edge['ipacm']['ipacm']['write-read'] = '[open open][add_name search][remove_name search]'
app = Viewer(G)
app.mainloop()