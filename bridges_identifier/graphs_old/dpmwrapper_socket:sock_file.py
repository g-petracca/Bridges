import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('dpmd','dpmd')
G.edge['dpmd']['dpmd']['write-read'] = '[open open]'
G.add_edge('dpmd','dpmd')
G.edge['dpmd']['dpmd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('dpmd','appdomain')
G.edge['dpmd']['appdomain']['write-read'] = '[write read]'
G.edge['dpmd']['appdomain']['fill'] = 'red'
G.add_edge('dpmd','dpmd')
G.edge['dpmd']['dpmd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['dpmd']['dpmd']['fill'] = 'red'
G.add_edge('dpmd','dpmd')
G.edge['dpmd']['dpmd']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('dpmd','netdomain')
G.edge['dpmd']['netdomain']['write-read'] = '[write read]'
G.edge['dpmd']['netdomain']['fill'] = 'red'
app = Viewer(G)
app.mainloop()