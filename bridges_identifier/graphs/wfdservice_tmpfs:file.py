import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('wfdservice','wfdservice')
G.edge['wfdservice']['wfdservice']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][write read]'
G.edge['wfdservice']['wfdservice']['fill'] = 'red'
app = Viewer(G)
app.mainloop()