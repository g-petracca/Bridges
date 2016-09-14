import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('keystore','keystore')
G.edge['keystore']['keystore']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read][open open]'
G.add_edge('keystore','tzdaemon')
G.edge['keystore']['tzdaemon']['write-read'] = '[open open]'
G.add_edge('keystore','keystore')
G.edge['keystore']['keystore']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read][open open][write read]'
G.edge['keystore']['keystore']['fill'] = 'red'
G.add_edge('keystore','keystore')
G.edge['keystore']['keystore']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read][open open][write read][append read]'
G.add_edge('keystore','tzdaemon')
G.edge['keystore']['tzdaemon']['write-read'] = '[open open][write read]'
G.edge['keystore']['tzdaemon']['fill'] = 'red'
G.add_edge('keystore','tzdaemon')
G.edge['keystore']['tzdaemon']['write-read'] = '[open open][write read][append read]'
G.add_edge('tzdaemon','keystore')
G.edge['tzdaemon']['keystore']['write-read'] = '[open open]'
G.add_edge('tzdaemon','tzdaemon')
G.edge['tzdaemon']['tzdaemon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('tzdaemon','keystore')
G.edge['tzdaemon']['keystore']['write-read'] = '[open open][write read]'
G.edge['tzdaemon']['keystore']['fill'] = 'red'
G.add_edge('tzdaemon','keystore')
G.edge['tzdaemon']['keystore']['write-read'] = '[open open][write read][append read]'
G.add_edge('tzdaemon','tzdaemon')
G.edge['tzdaemon']['tzdaemon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['tzdaemon']['tzdaemon']['fill'] = 'red'
G.add_edge('tzdaemon','tzdaemon')
G.edge['tzdaemon']['tzdaemon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
app = Viewer(G)
app.mainloop()