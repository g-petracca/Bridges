import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('msm_irqbalanced','msm_irqbalanced')
G.edge['msm_irqbalanced']['msm_irqbalanced']['write-read'] = '[write read]'
G.edge['msm_irqbalanced']['msm_irqbalanced']['fill'] = 'red'
app = Viewer(G)
app.mainloop()