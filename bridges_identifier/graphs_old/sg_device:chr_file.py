import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('qseecomd','qseecomd')
G.edge['qseecomd']['qseecomd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('qseecomd','tee')
G.edge['qseecomd']['tee']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('qseecomd','tee')
G.edge['qseecomd']['tee']['write-read'] = '[open open][write read][append read][open open][setattr getattr]'
G.add_edge('qseecomd','qseecomd')
G.edge['qseecomd']['qseecomd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read]'
G.edge['qseecomd']['qseecomd']['fill'] = 'red'
G.add_edge('qseecomd','qseecomd')
G.edge['qseecomd']['qseecomd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read]'
G.add_edge('qseecomd','tee')
G.edge['qseecomd']['tee']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read]'
G.edge['qseecomd']['tee']['fill'] = 'red'
G.add_edge('qseecomd','tee')
G.edge['qseecomd']['tee']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('tee','qseecomd')
G.edge['tee']['qseecomd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('tee','tee')
G.edge['tee']['tee']['write-read'] = '[write read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open]'
G.add_edge('tee','tee')
G.edge['tee']['tee']['write-read'] = '[write read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][setattr getattr]'
G.add_edge('tee','qseecomd')
G.edge['tee']['qseecomd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read]'
G.edge['tee']['qseecomd']['fill'] = 'red'
G.add_edge('tee','qseecomd')
G.edge['tee']['qseecomd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read]'
G.add_edge('tee','tee')
G.edge['tee']['tee']['write-read'] = '[write read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['tee']['tee']['fill'] = 'red'
G.add_edge('tee','tee')
G.edge['tee']['tee']['write-read'] = '[write read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read]'
app = Viewer(G)
app.mainloop()