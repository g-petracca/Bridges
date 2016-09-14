import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('tee','tee')
G.edge['tee']['tee']['write-read'] = '[write read][open open][write read][append read][open open]'
G.add_edge('tee','tzdaemon')
G.edge['tee']['tzdaemon']['write-read'] = '[write read][add_name search][open open]'
G.add_edge('tee','tzdaemon')
G.edge['tee']['tzdaemon']['write-read'] = '[write read][add_name search][open open][setattr getattr]'
G.add_edge('tee','tee')
G.edge['tee']['tee']['write-read'] = '[write read][open open][write read][append read][open open][write read]'
G.edge['tee']['tee']['fill'] = 'red'
G.add_edge('tee','tzdaemon')
G.edge['tee']['tzdaemon']['write-read'] = '[write read][add_name search][open open][setattr getattr][write read]'
G.edge['tee']['tzdaemon']['fill'] = 'red'
G.add_edge('tee','tee')
G.edge['tee']['tee']['write-read'] = '[write read][open open][write read][append read][open open][write read][add_name search]'
G.add_edge('tee','tee')
G.edge['tee']['tee']['write-read'] = '[write read][open open][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('tee','tzdaemon')
G.edge['tee']['tzdaemon']['write-read'] = '[write read][add_name search][open open][setattr getattr][write read][add_name search]'
G.add_edge('tee','tzdaemon')
G.edge['tee']['tzdaemon']['write-read'] = '[write read][add_name search][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('tzdaemon','tee')
G.edge['tzdaemon']['tee']['write-read'] = '[open open]'
G.add_edge('tzdaemon','tzdaemon')
G.edge['tzdaemon']['tzdaemon']['write-read'] = '[open open]'
G.add_edge('tzdaemon','tzdaemon')
G.edge['tzdaemon']['tzdaemon']['write-read'] = '[open open][setattr getattr]'
G.add_edge('tzdaemon','tee')
G.edge['tzdaemon']['tee']['write-read'] = '[open open][write read]'
G.edge['tzdaemon']['tee']['fill'] = 'red'
G.add_edge('tzdaemon','tzdaemon')
G.edge['tzdaemon']['tzdaemon']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['tzdaemon']['tzdaemon']['fill'] = 'red'
G.add_edge('tzdaemon','tee')
G.edge['tzdaemon']['tee']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('tzdaemon','tee')
G.edge['tzdaemon']['tee']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('tzdaemon','tzdaemon')
G.edge['tzdaemon']['tzdaemon']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('tzdaemon','tzdaemon')
G.edge['tzdaemon']['tzdaemon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
app = Viewer(G)
app.mainloop()