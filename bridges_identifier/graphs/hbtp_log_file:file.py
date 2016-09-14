import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('hbtp','hbtp')
G.edge['hbtp']['hbtp']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('hbtp','hbtp')
G.edge['hbtp']['hbtp']['write-read'] = '[open open][write read][append read][open open][setattr getattr]'
G.add_edge('hbtp','hbtp')
G.edge['hbtp']['hbtp']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read]'
G.edge['hbtp']['hbtp']['fill'] = 'red'
G.add_edge('hbtp','hbtp')
G.edge['hbtp']['hbtp']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read]'
app = Viewer(G)
app.mainloop()