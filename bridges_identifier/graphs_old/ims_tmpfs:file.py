import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('ims','ims')
G.edge['ims']['ims']['write-read'] = '[open open][add_name search][remove_name search][open open][write read][append read][write read]'
G.edge['ims']['ims']['fill'] = 'red'
app = Viewer(G)
app.mainloop()