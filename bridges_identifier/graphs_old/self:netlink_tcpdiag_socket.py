import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('cnd','cnd')
G.edge['cnd']['cnd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read]'
G.edge['cnd']['cnd']['fill'] = 'red'
G.add_edge('cnd','cnd')
G.edge['cnd']['cnd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][write read]'
G.edge['cnd']['cnd']['fill'] = 'red'
G.add_edge('cnd','cnd')
G.edge['cnd']['cnd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][write read][append read]'
G.add_edge('cnd','cnd')
G.edge['cnd']['cnd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][write read][append read][setopt getopt]'
G.add_edge('cnd','cnd')
G.edge['cnd']['cnd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][write read][append read][setopt getopt][setattr getattr]'
G.add_edge('cnd','cnd')
G.edge['cnd']['cnd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][write read][append read][setopt getopt][setattr getattr][write read]'
G.edge['cnd']['cnd']['fill'] = 'red'
G.add_edge('cnd','cnd')
G.edge['cnd']['cnd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][write read][append read][setopt getopt][setattr getattr][write read][write read]'
G.edge['cnd']['cnd']['fill'] = 'red'
G.add_edge('cnd','cnd')
G.edge['cnd']['cnd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][write read][append read][setopt getopt][setattr getattr][write read][write read][append read]'
G.add_edge('cnd','cnd')
G.edge['cnd']['cnd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][write read][append read][setopt getopt][setattr getattr][write read][write read][append read][setopt getopt]'
app = Viewer(G)
app.mainloop()