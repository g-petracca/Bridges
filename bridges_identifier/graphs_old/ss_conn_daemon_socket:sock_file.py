import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('ss_conn_daemon','ss_conn_daemon')
G.edge['ss_conn_daemon']['ss_conn_daemon']['write-read'] = '[open open]'
G.add_edge('ss_conn_daemon','ss_conn_daemon')
G.edge['ss_conn_daemon']['ss_conn_daemon']['write-read'] = '[open open][setattr getattr]'
G.add_edge('ss_conn_daemon','platform_app')
G.edge['ss_conn_daemon']['platform_app']['write-read'] = '[write read]'
G.edge['ss_conn_daemon']['platform_app']['fill'] = 'red'
G.add_edge('ss_conn_daemon','s_platform_app')
G.edge['ss_conn_daemon']['s_platform_app']['write-read'] = '[write read]'
G.edge['ss_conn_daemon']['s_platform_app']['fill'] = 'red'
G.add_edge('ss_conn_daemon','ss_conn_daemon')
G.edge['ss_conn_daemon']['ss_conn_daemon']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['ss_conn_daemon']['ss_conn_daemon']['fill'] = 'red'
G.add_edge('ss_conn_daemon','ss_conn_daemon')
G.edge['ss_conn_daemon']['ss_conn_daemon']['write-read'] = '[open open][setattr getattr][write read][append read]'
app = Viewer(G)
app.mainloop()