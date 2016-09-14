import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('qcks','qcks')
G.edge['qcks']['qcks']['write-read'] = '[open open][write read][append read][open open][add_name search][remove_name search][open open][write read][add_name search][write read]'
G.edge['qcks']['qcks']['fill'] = 'red'
app = Viewer(G)
app.mainloop()