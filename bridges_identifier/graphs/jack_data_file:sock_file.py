import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('apaservice','apaservice')
G.edge['apaservice']['apaservice']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('apaservice','jackservice')
G.edge['apaservice']['jackservice']['write-read'] = '[open open][add_name search][remove_name search][open open]'
G.add_edge('apaservice','apaservice')
G.edge['apaservice']['apaservice']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr]'
G.add_edge('apaservice','jackservice')
G.edge['apaservice']['jackservice']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('apaservice','apaservice')
G.edge['apaservice']['apaservice']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['apaservice']['apaservice']['fill'] = 'red'
G.add_edge('apaservice','apaservice')
G.edge['apaservice']['apaservice']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('apaservice','jackservice')
G.edge['apaservice']['jackservice']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['apaservice']['jackservice']['fill'] = 'red'
G.add_edge('apaservice','jackservice')
G.edge['apaservice']['jackservice']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('jackservice','apaservice')
G.edge['jackservice']['apaservice']['write-read'] = '[open open][write read][add_name search][remove_name search][open open]'
G.add_edge('jackservice','jackservice')
G.edge['jackservice']['jackservice']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read][append read][open open]'
G.add_edge('jackservice','apaservice')
G.edge['jackservice']['apaservice']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('jackservice','jackservice')
G.edge['jackservice']['jackservice']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read][append read][open open][setattr getattr]'
G.add_edge('jackservice','apaservice')
G.edge['jackservice']['apaservice']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['jackservice']['apaservice']['fill'] = 'red'
G.add_edge('jackservice','apaservice')
G.edge['jackservice']['apaservice']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('jackservice','jackservice')
G.edge['jackservice']['jackservice']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['jackservice']['jackservice']['fill'] = 'red'
G.add_edge('jackservice','jackservice')
G.edge['jackservice']['jackservice']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read][append read][open open][setattr getattr][write read][append read]'
app = Viewer(G)
app.mainloop()