import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('oneseg_apk','oneseg_apk')
G.edge['oneseg_apk']['oneseg_apk']['write-read'] = '[write read]'
G.edge['oneseg_apk']['oneseg_apk']['fill'] = 'red'
app = Viewer(G)
app.mainloop()