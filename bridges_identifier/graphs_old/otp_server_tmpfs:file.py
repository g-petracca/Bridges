import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('otp_server','otp_server')
G.edge['otp_server']['otp_server']['write-read'] = '[write read][open open][write read][append read][open open][write read][open open][write read][add_name search][remove_name search][write read]'
G.edge['otp_server']['otp_server']['fill'] = 'red'
app = Viewer(G)
app.mainloop()