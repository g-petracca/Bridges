import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('rtcc','rtcc')
G.edge['rtcc']['rtcc']['write-read'] = '[open open][write read][add_name search][remove_name search][write read]'
G.edge['rtcc']['rtcc']['fill'] = 'red'
app = Viewer(G)
app.mainloop()