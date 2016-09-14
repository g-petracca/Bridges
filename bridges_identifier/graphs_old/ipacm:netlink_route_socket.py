import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('ipacm','ipacm')
G.edge['ipacm']['ipacm']['write-read'] = '[open open][add_name search][remove_name search][write read][write read][open open][setattr getattr][write read][append read][setopt getopt]'
app = Viewer(G)
app.mainloop()