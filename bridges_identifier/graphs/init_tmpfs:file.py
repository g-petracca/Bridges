import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('appdomain','init')
G.edge['appdomain']['init']['write-read'] = '[write read]'
G.edge['appdomain']['init']['fill'] = 'red'
G.add_edge('bluetooth','init')
G.edge['bluetooth']['init']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read]'
G.edge['bluetooth']['init']['fill'] = 'red'
G.add_edge('init','init')
G.edge['init']['init']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['init']['init']['fill'] = 'red'
G.add_edge('isolated_app','init')
G.edge['isolated_app']['init']['write-read'] = '[write read]'
G.edge['isolated_app']['init']['fill'] = 'red'
G.add_edge('knox_untrusted_app','init')
G.edge['knox_untrusted_app']['init']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['knox_untrusted_app']['init']['fill'] = 'red'
G.add_edge('nfc','init')
G.edge['nfc']['init']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read]'
G.edge['nfc']['init']['fill'] = 'red'
G.add_edge('platformappdomain','init')
G.edge['platformappdomain']['init']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read]'
G.edge['platformappdomain']['init']['fill'] = 'red'
G.add_edge('radio','init')
G.edge['radio']['init']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['radio']['init']['fill'] = 'red'
G.add_edge('samsung_app','init')
G.edge['samsung_app']['init']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read]'
G.edge['samsung_app']['init']['fill'] = 'red'
app = Viewer(G)
app.mainloop()