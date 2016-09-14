import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('tee','tee')
G.edge['tee']['tee']['write-read'] = '[write read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('tee','tee')
G.edge['tee']['tee']['write-read'] = '[write read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('tee','tee')
G.edge['tee']['tee']['write-read'] = '[write read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['tee']['tee']['fill'] = 'red'
G.add_edge('tee','tee')
G.edge['tee']['tee']['write-read'] = '[write read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
app = Viewer(G)
app.mainloop()