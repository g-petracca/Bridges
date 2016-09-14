import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('charger_monitor','charger_monitor')
G.edge['charger_monitor']['charger_monitor']['write-read'] = '[open open][write read][append read][open open][open open][write read][append read][write read][append read][open open][write read][append read][open open][write read][append read][write read]'
G.edge['charger_monitor']['charger_monitor']['fill'] = 'red'
app = Viewer(G)
app.mainloop()