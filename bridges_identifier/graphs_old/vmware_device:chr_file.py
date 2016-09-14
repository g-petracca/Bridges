import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('vmwared','vmwared')
G.edge['vmwared']['vmwared']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('vmwared','vmwared')
G.edge['vmwared']['vmwared']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('vmwared','vmwared')
G.edge['vmwared']['vmwared']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['vmwared']['vmwared']['fill'] = 'red'
G.add_edge('vmwared','vmwared')
G.edge['vmwared']['vmwared']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
app = Viewer(G)
app.mainloop()