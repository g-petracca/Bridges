import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('ipruleset','ipruleset')
G.edge['ipruleset']['ipruleset']['write-read'] = '[write read]'
G.edge['ipruleset']['ipruleset']['fill'] = 'red'
app = Viewer(G)
app.mainloop()