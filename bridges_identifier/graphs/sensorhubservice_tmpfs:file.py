import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('sensorhubservice','sensorhubservice')
G.edge['sensorhubservice']['sensorhubservice']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][write read]'
G.edge['sensorhubservice']['sensorhubservice']['fill'] = 'red'
app = Viewer(G)
app.mainloop()