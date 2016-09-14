import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('ss_conn_daemon','ss_conn_daemon')
G.edge['ss_conn_daemon']['ss_conn_daemon']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read]'
G.edge['ss_conn_daemon']['ss_conn_daemon']['fill'] = 'red'
app = Viewer(G)
app.mainloop()