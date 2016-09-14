import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('brcm_patchram_plus','brcm_patchram_plus')
G.edge['brcm_patchram_plus']['brcm_patchram_plus']['write-read'] = '[write read]'
G.edge['brcm_patchram_plus']['brcm_patchram_plus']['fill'] = 'red'
app = Viewer(G)
app.mainloop()