import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('ssr_setup','ssr_setup')
G.edge['ssr_setup']['ssr_setup']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read]'
G.edge['ssr_setup']['ssr_setup']['fill'] = 'red'
app = Viewer(G)
app.mainloop()