import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('commonplatformappdomain','commonplatformappdomain')
G.edge['commonplatformappdomain']['commonplatformappdomain']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('commonplatformappdomain','commonplatformappdomain')
G.edge['commonplatformappdomain']['commonplatformappdomain']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['commonplatformappdomain']['commonplatformappdomain']['fill'] = 'red'
G.add_edge('commonplatformappdomain','commonplatformappdomain')
G.edge['commonplatformappdomain']['commonplatformappdomain']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
app = Viewer(G)
app.mainloop()