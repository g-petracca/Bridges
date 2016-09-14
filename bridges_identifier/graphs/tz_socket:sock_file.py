import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('tzdaemon','tzdaemon')
G.edge['tzdaemon']['tzdaemon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('tzdaemon','radio')
G.edge['tzdaemon']['radio']['write-read'] = '[write read]'
G.edge['tzdaemon']['radio']['fill'] = 'red'
G.add_edge('tzdaemon','system_server')
G.edge['tzdaemon']['system_server']['write-read'] = '[write read]'
G.edge['tzdaemon']['system_server']['fill'] = 'red'
G.add_edge('tzdaemon','tzdaemon')
G.edge['tzdaemon']['tzdaemon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read]'
G.edge['tzdaemon']['tzdaemon']['fill'] = 'red'
G.add_edge('tzdaemon','tzdaemon')
G.edge['tzdaemon']['tzdaemon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read]'
app = Viewer(G)
app.mainloop()