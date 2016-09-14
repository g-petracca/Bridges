import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('appdomain','cnd')
G.edge['appdomain']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('appdomain','appdomain')
G.edge['appdomain']['appdomain']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][write read][setattr getattr][write read][append read][setopt getopt][write read][open open][write read][append read][write read][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][setattr getattr][open execmod][write read]'
G.edge['appdomain']['appdomain']['fill'] = 'red'
G.add_edge('appdomain','cnd')
G.edge['appdomain']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][setattr getattr][write read]'
G.edge['appdomain']['cnd']['fill'] = 'red'
G.add_edge('appdomain','cnd')
G.edge['appdomain']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][setattr getattr][write read][append read]'
G.add_edge('appdomain','dpmd')
G.edge['appdomain']['dpmd']['write-read'] = '[write read]'
G.edge['appdomain']['dpmd']['fill'] = 'red'
G.add_edge('appdomain','cnd')
G.edge['appdomain']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt]'
G.add_edge('appdomain','dpmd')
G.edge['appdomain']['dpmd']['write-read'] = '[write read][setopt getopt]'
G.add_edge('cnd','cnd')
G.edge['cnd']['cnd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][write read][append read][setopt getopt][setattr getattr][write read][write read][append read][setopt getopt][open open][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][setopt getopt][add_name search][remove_name search][setattr getattr]'
G.add_edge('cnd','appdomain')
G.edge['cnd']['appdomain']['write-read'] = '[write read]'
G.edge['cnd']['appdomain']['fill'] = 'red'
G.add_edge('cnd','cnd')
G.edge['cnd']['cnd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][write read][append read][setopt getopt][setattr getattr][write read][write read][append read][setopt getopt][open open][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][setopt getopt][add_name search][remove_name search][setattr getattr][write read]'
G.edge['cnd']['cnd']['fill'] = 'red'
G.add_edge('cnd','cnd')
G.edge['cnd']['cnd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][write read][append read][setopt getopt][setattr getattr][write read][write read][append read][setopt getopt][open open][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][setopt getopt][add_name search][remove_name search][setattr getattr][write read][append read]'
G.add_edge('cnd','dpmd')
G.edge['cnd']['dpmd']['write-read'] = '[open open][setattr getattr][write read][append read][write read]'
G.edge['cnd']['dpmd']['fill'] = 'red'
G.add_edge('cnd','cnd')
G.edge['cnd']['cnd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][write read][append read][setopt getopt][setattr getattr][write read][write read][append read][setopt getopt][open open][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][setopt getopt][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt]'
G.add_edge('cnd','dpmd')
G.edge['cnd']['dpmd']['write-read'] = '[open open][setattr getattr][write read][append read][write read][setopt getopt]'
G.add_edge('dpmd','cnd')
G.edge['dpmd']['cnd']['write-read'] = '[open open][append read][open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('dpmd','appdomain')
G.edge['dpmd']['appdomain']['write-read'] = '[write read][write read]'
G.edge['dpmd']['appdomain']['fill'] = 'red'
G.add_edge('dpmd','cnd')
G.edge['dpmd']['cnd']['write-read'] = '[open open][append read][open open][setattr getattr][write read][append read][setattr getattr][write read]'
G.edge['dpmd']['cnd']['fill'] = 'red'
G.add_edge('dpmd','cnd')
G.edge['dpmd']['cnd']['write-read'] = '[open open][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read]'
G.add_edge('dpmd','dpmd')
G.edge['dpmd']['dpmd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read]'
G.edge['dpmd']['dpmd']['fill'] = 'red'
G.add_edge('dpmd','cnd')
G.edge['dpmd']['cnd']['write-read'] = '[open open][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][setopt getopt]'
G.add_edge('dpmd','dpmd')
G.edge['dpmd']['dpmd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][setopt getopt]'
app = Viewer(G)
app.mainloop()