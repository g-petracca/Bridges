import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('qmiproxy','qmiproxy')
G.edge['qmiproxy']['qmiproxy']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read]'
G.edge['qmiproxy']['qmiproxy']['fill'] = 'red'
app = Viewer(G)
app.mainloop()