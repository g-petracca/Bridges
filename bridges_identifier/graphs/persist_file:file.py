import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('bluetooth','bluetooth')
G.edge['bluetooth']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('bluetooth','mm-pp-daemon')
G.edge['bluetooth']['mm-pp-daemon']['write-read'] = '[open open]'
G.add_edge('bluetooth','mm-pp-daemon')
G.edge['bluetooth']['mm-pp-daemon']['write-read'] = '[open open][setattr getattr]'
G.add_edge('bluetooth','bluetooth')
G.edge['bluetooth']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read]'
G.edge['bluetooth']['bluetooth']['fill'] = 'red'
G.add_edge('bluetooth','bluetooth')
G.edge['bluetooth']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read]'
G.add_edge('bluetooth','mm-pp-daemon')
G.edge['bluetooth']['mm-pp-daemon']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['bluetooth']['mm-pp-daemon']['fill'] = 'red'
G.add_edge('bluetooth','mm-pp-daemon')
G.edge['bluetooth']['mm-pp-daemon']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('mm-pp-daemon','bluetooth')
G.edge['mm-pp-daemon']['bluetooth']['write-read'] = '[open open]'
G.add_edge('mm-pp-daemon','mm-pp-daemon')
G.edge['mm-pp-daemon']['mm-pp-daemon']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('mm-pp-daemon','mm-pp-daemon')
G.edge['mm-pp-daemon']['mm-pp-daemon']['write-read'] = '[open open][write read][append read][open open][setattr getattr]'
G.add_edge('mm-pp-daemon','bluetooth')
G.edge['mm-pp-daemon']['bluetooth']['write-read'] = '[open open][write read]'
G.edge['mm-pp-daemon']['bluetooth']['fill'] = 'red'
G.add_edge('mm-pp-daemon','bluetooth')
G.edge['mm-pp-daemon']['bluetooth']['write-read'] = '[open open][write read][append read]'
G.add_edge('mm-pp-daemon','mm-pp-daemon')
G.edge['mm-pp-daemon']['mm-pp-daemon']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read]'
G.edge['mm-pp-daemon']['mm-pp-daemon']['fill'] = 'red'
G.add_edge('mm-pp-daemon','mm-pp-daemon')
G.edge['mm-pp-daemon']['mm-pp-daemon']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('shell','bluetooth')
G.edge['shell']['bluetooth']['write-read'] = '[setopt getopt][open open]'
G.add_edge('shell','mm-pp-daemon')
G.edge['shell']['mm-pp-daemon']['write-read'] = '[open open]'
G.add_edge('shell','mm-pp-daemon')
G.edge['shell']['mm-pp-daemon']['write-read'] = '[open open][setattr getattr]'
G.add_edge('shell','bluetooth')
G.edge['shell']['bluetooth']['write-read'] = '[setopt getopt][open open][write read]'
G.edge['shell']['bluetooth']['fill'] = 'red'
G.add_edge('shell','bluetooth')
G.edge['shell']['bluetooth']['write-read'] = '[setopt getopt][open open][write read][append read]'
G.add_edge('shell','mm-pp-daemon')
G.edge['shell']['mm-pp-daemon']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['shell']['mm-pp-daemon']['fill'] = 'red'
G.add_edge('shell','mm-pp-daemon')
G.edge['shell']['mm-pp-daemon']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('ueventd','bluetooth')
G.edge['ueventd']['bluetooth']['write-read'] = '[open open]'
G.add_edge('ueventd','mm-pp-daemon')
G.edge['ueventd']['mm-pp-daemon']['write-read'] = '[open open]'
G.add_edge('ueventd','mm-pp-daemon')
G.edge['ueventd']['mm-pp-daemon']['write-read'] = '[open open][setattr getattr]'
G.add_edge('ueventd','bluetooth')
G.edge['ueventd']['bluetooth']['write-read'] = '[open open][write read]'
G.edge['ueventd']['bluetooth']['fill'] = 'red'
G.add_edge('ueventd','bluetooth')
G.edge['ueventd']['bluetooth']['write-read'] = '[open open][write read][append read]'
G.add_edge('ueventd','mm-pp-daemon')
G.edge['ueventd']['mm-pp-daemon']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['ueventd']['mm-pp-daemon']['fill'] = 'red'
G.add_edge('ueventd','mm-pp-daemon')
G.edge['ueventd']['mm-pp-daemon']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('usf','bluetooth')
G.edge['usf']['bluetooth']['write-read'] = '[open open]'
G.add_edge('usf','mm-pp-daemon')
G.edge['usf']['mm-pp-daemon']['write-read'] = '[open open]'
G.add_edge('usf','mm-pp-daemon')
G.edge['usf']['mm-pp-daemon']['write-read'] = '[open open][setattr getattr]'
G.add_edge('usf','bluetooth')
G.edge['usf']['bluetooth']['write-read'] = '[open open][write read]'
G.edge['usf']['bluetooth']['fill'] = 'red'
G.add_edge('usf','bluetooth')
G.edge['usf']['bluetooth']['write-read'] = '[open open][write read][append read]'
G.add_edge('usf','mm-pp-daemon')
G.edge['usf']['mm-pp-daemon']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['usf']['mm-pp-daemon']['fill'] = 'red'
G.add_edge('usf','mm-pp-daemon')
G.edge['usf']['mm-pp-daemon']['write-read'] = '[open open][setattr getattr][write read][append read]'
app = Viewer(G)
app.mainloop()