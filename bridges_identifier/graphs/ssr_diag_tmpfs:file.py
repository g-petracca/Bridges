import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('ssr_diag','ssr_diag')
G.edge['ssr_diag']['ssr_diag']['write-read'] = '[write read]'
G.edge['ssr_diag']['ssr_diag']['fill'] = 'red'
app = Viewer(G)
app.mainloop()