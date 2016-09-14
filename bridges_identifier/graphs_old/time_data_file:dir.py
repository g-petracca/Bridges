import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('time_daemon','time_daemon')
G.edge['time_daemon']['time_daemon']['write-read'] = '[open open]'
G.add_edge('time_daemon','time_daemon')
G.edge['time_daemon']['time_daemon']['write-read'] = '[open open][setattr getattr]'
G.add_edge('time_daemon','time_daemon')
G.edge['time_daemon']['time_daemon']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['time_daemon']['time_daemon']['fill'] = 'red'
G.add_edge('time_daemon','time_daemon')
G.edge['time_daemon']['time_daemon']['write-read'] = '[open open][setattr getattr][write read][write read]'
G.edge['time_daemon']['time_daemon']['fill'] = 'red'
G.add_edge('time_daemon','time_daemon')
G.edge['time_daemon']['time_daemon']['write-read'] = '[open open][setattr getattr][write read][write read][add_name search]'
G.add_edge('time_daemon','time_daemon')
G.edge['time_daemon']['time_daemon']['write-read'] = '[open open][setattr getattr][write read][write read][add_name search][remove_name search]'
G.add_edge('time_daemon','time_daemon')
G.edge['time_daemon']['time_daemon']['write-read'] = '[open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search]'
G.add_edge('time_daemon','time_daemon')
G.edge['time_daemon']['time_daemon']['write-read'] = '[open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][add_name search]'
G.add_edge('time_daemon','time_daemon')
G.edge['time_daemon']['time_daemon']['write-read'] = '[open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][add_name search][remove_name search]'
G.add_edge('time_daemon','time_daemon')
G.edge['time_daemon']['time_daemon']['write-read'] = '[open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][add_name search][remove_name search][add_name search]'
app = Viewer(G)
app.mainloop()