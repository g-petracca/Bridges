import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('installd','installd')
G.edge['installd']['installd']['write-read'] = '[setattr getattr]'
G.add_edge('installd','radio')
G.edge['installd']['radio']['write-read'] = '[setattr getattr]'
G.add_edge('installd','installd')
G.edge['installd']['installd']['write-read'] = '[setattr getattr][relabelto relabelfrom]'
G.add_edge('radio','radio')
G.edge['radio']['radio']['write-read'] = '[open open]'
G.add_edge('radio','installd')
G.edge['radio']['installd']['write-read'] = '[setattr getattr]'
G.add_edge('radio','radio')
G.edge['radio']['radio']['write-read'] = '[open open][setattr getattr]'
G.add_edge('radio','radio')
G.edge['radio']['radio']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['radio']['radio']['fill'] = 'red'
G.add_edge('radio','radio')
G.edge['radio']['radio']['write-read'] = '[open open][setattr getattr][write read][append read]'
app = Viewer(G)
app.mainloop()