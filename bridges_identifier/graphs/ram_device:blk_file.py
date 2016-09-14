import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('kernel','kernel')
G.edge['kernel']['kernel']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open]'
G.add_edge('kernel','rtcc')
G.edge['kernel']['rtcc']['write-read'] = '[open open]'
G.add_edge('kernel','kernel')
G.edge['kernel']['kernel']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr]'
G.add_edge('kernel','kernel')
G.edge['kernel']['kernel']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['kernel']['kernel']['fill'] = 'red'
G.add_edge('kernel','kernel')
G.edge['kernel']['kernel']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('kernel','rtcc')
G.edge['kernel']['rtcc']['write-read'] = '[open open][write read]'
G.edge['kernel']['rtcc']['fill'] = 'red'
G.add_edge('kernel','rtcc')
G.edge['kernel']['rtcc']['write-read'] = '[open open][write read][append read]'
G.add_edge('rtcc','kernel')
G.edge['rtcc']['kernel']['write-read'] = '[open open]'
G.add_edge('rtcc','rtcc')
G.edge['rtcc']['rtcc']['write-read'] = '[open open][write read][add_name search][remove_name search][write read][open open]'
G.add_edge('rtcc','kernel')
G.edge['rtcc']['kernel']['write-read'] = '[open open][setattr getattr]'
G.add_edge('rtcc','kernel')
G.edge['rtcc']['kernel']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['rtcc']['kernel']['fill'] = 'red'
G.add_edge('rtcc','kernel')
G.edge['rtcc']['kernel']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('rtcc','rtcc')
G.edge['rtcc']['rtcc']['write-read'] = '[open open][write read][add_name search][remove_name search][write read][open open][write read]'
G.edge['rtcc']['rtcc']['fill'] = 'red'
G.add_edge('rtcc','rtcc')
G.edge['rtcc']['rtcc']['write-read'] = '[open open][write read][add_name search][remove_name search][write read][open open][write read][append read]'
app = Viewer(G)
app.mainloop()