import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('mmb_apk','mmb_apk')
G.edge['mmb_apk']['mmb_apk']['write-read'] = '[write read]'
G.edge['mmb_apk']['mmb_apk']['fill'] = 'red'
app = Viewer(G)
app.mainloop()