import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('mmi','mmi')
G.edge['mmi']['mmi']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('mmi','nfc')
G.edge['mmi']['nfc']['write-read'] = '[open open]'
G.add_edge('mmi','sem')
G.edge['mmi']['sem']['write-read'] = '[open open]'
G.add_edge('mmi','mmi')
G.edge['mmi']['mmi']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read]'
G.edge['mmi']['mmi']['fill'] = 'red'
G.add_edge('mmi','mmi')
G.edge['mmi']['mmi']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read]'
G.add_edge('mmi','nfc')
G.edge['mmi']['nfc']['write-read'] = '[open open][write read]'
G.edge['mmi']['nfc']['fill'] = 'red'
G.add_edge('mmi','nfc')
G.edge['mmi']['nfc']['write-read'] = '[open open][write read][append read]'
G.add_edge('mmi','sem')
G.edge['mmi']['sem']['write-read'] = '[open open][write read]'
G.edge['mmi']['sem']['fill'] = 'red'
G.add_edge('mmi','sem')
G.edge['mmi']['sem']['write-read'] = '[open open][write read][append read]'
G.add_edge('nfc','mmi')
G.edge['nfc']['mmi']['write-read'] = '[open open]'
G.add_edge('nfc','nfc')
G.edge['nfc']['nfc']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('nfc','sem')
G.edge['nfc']['sem']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('nfc','mmi')
G.edge['nfc']['mmi']['write-read'] = '[open open][write read]'
G.edge['nfc']['mmi']['fill'] = 'red'
G.add_edge('nfc','mmi')
G.edge['nfc']['mmi']['write-read'] = '[open open][write read][append read]'
G.add_edge('nfc','nfc')
G.edge['nfc']['nfc']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['nfc']['nfc']['fill'] = 'red'
G.add_edge('nfc','nfc')
G.edge['nfc']['nfc']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('nfc','sem')
G.edge['nfc']['sem']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['nfc']['sem']['fill'] = 'red'
G.add_edge('nfc','sem')
G.edge['nfc']['sem']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('sem','mmi')
G.edge['sem']['mmi']['write-read'] = '[open open]'
G.add_edge('sem','nfc')
G.edge['sem']['nfc']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('sem','sem')
G.edge['sem']['sem']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('sem','mmi')
G.edge['sem']['mmi']['write-read'] = '[open open][write read]'
G.edge['sem']['mmi']['fill'] = 'red'
G.add_edge('sem','mmi')
G.edge['sem']['mmi']['write-read'] = '[open open][write read][append read]'
G.add_edge('sem','nfc')
G.edge['sem']['nfc']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['sem']['nfc']['fill'] = 'red'
G.add_edge('sem','nfc')
G.edge['sem']['nfc']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('sem','sem')
G.edge['sem']['sem']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['sem']['sem']['fill'] = 'red'
G.add_edge('sem','sem')
G.edge['sem']['sem']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][write read][add_name search][remove_name search][open open][write read][append read]'
app = Viewer(G)
app.mainloop()