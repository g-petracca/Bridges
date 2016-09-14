import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('ptt_socket_app','ptt_socket_app')
G.edge['ptt_socket_app']['ptt_socket_app']['write-read'] = '[write read]'
G.edge['ptt_socket_app']['ptt_socket_app']['fill'] = 'red'
app = Viewer(G)
app.mainloop()