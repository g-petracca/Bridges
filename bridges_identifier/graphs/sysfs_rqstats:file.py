import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('msm_irqbalanced','mpdecision')
G.edge['msm_irqbalanced']['mpdecision']['write-read'] = '[open open]'
G.add_edge('msm_irqbalanced','mpdecision')
G.edge['msm_irqbalanced']['mpdecision']['write-read'] = '[open open][write read]'
G.edge['msm_irqbalanced']['mpdecision']['fill'] = 'red'
G.add_edge('msm_irqbalanced','mpdecision')
G.edge['msm_irqbalanced']['mpdecision']['write-read'] = '[open open][write read][append read]'
app = Viewer(G)
app.mainloop()