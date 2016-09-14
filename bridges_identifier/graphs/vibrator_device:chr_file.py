import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('immvibed','immvibed')
G.edge['immvibed']['immvibed']['write-read'] = '[open open]'
G.add_edge('immvibed','immvibed')
G.edge['immvibed']['immvibed']['write-read'] = '[open open][open open]'
G.add_edge('immvibed','immvibed')
G.edge['immvibed']['immvibed']['write-read'] = '[open open][open open][write read]'
G.edge['immvibed']['immvibed']['fill'] = 'red'
G.add_edge('immvibed','immvibed')
G.edge['immvibed']['immvibed']['write-read'] = '[open open][open open][write read][append read]'
G.add_edge('immvibed','immvibed')
G.edge['immvibed']['immvibed']['write-read'] = '[open open][open open][write read][append read][write read]'
G.edge['immvibed']['immvibed']['fill'] = 'red'
G.add_edge('immvibed','immvibed')
G.edge['immvibed']['immvibed']['write-read'] = '[open open][open open][write read][append read][write read][append read]'
G.add_edge('immvibed','immvibed')
G.edge['immvibed']['immvibed']['write-read'] = '[open open][open open][write read][append read][write read][append read][open open]'
G.add_edge('immvibed','immvibed')
G.edge['immvibed']['immvibed']['write-read'] = '[open open][open open][write read][append read][write read][append read][open open][open open]'
G.add_edge('immvibed','immvibed')
G.edge['immvibed']['immvibed']['write-read'] = '[open open][open open][write read][append read][write read][append read][open open][open open][write read]'
G.edge['immvibed']['immvibed']['fill'] = 'red'
G.add_edge('immvibed','immvibed')
G.edge['immvibed']['immvibed']['write-read'] = '[open open][open open][write read][append read][write read][append read][open open][open open][write read][append read]'
G.add_edge('immvibed','immvibed')
G.edge['immvibed']['immvibed']['write-read'] = '[open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read]'
G.edge['immvibed']['immvibed']['fill'] = 'red'
G.add_edge('immvibed','immvibed')
G.edge['immvibed']['immvibed']['write-read'] = '[open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read]'
G.add_edge('shell','immvibed')
G.edge['shell']['immvibed']['write-read'] = '[write read]'
G.edge['shell']['immvibed']['fill'] = 'red'
G.add_edge('shell','immvibed')
G.edge['shell']['immvibed']['write-read'] = '[write read][append read]'
G.add_edge('shell','immvibed')
G.edge['shell']['immvibed']['write-read'] = '[write read][append read][write read]'
G.edge['shell']['immvibed']['fill'] = 'red'
G.add_edge('shell','immvibed')
G.edge['shell']['immvibed']['write-read'] = '[write read][append read][write read][append read]'
app = Viewer(G)
app.mainloop()