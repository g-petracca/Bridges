import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('bootanim','bootanim')
G.edge['bootanim']['bootanim']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][write read][open open][write read][append read][open open]'
G.add_edge('bootanim','domain')
G.edge['bootanim']['domain']['write-read'] = '[open open]'
G.add_edge('bootanim','mediaserver')
G.edge['bootanim']['mediaserver']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('bootanim','bootanim')
G.edge['bootanim']['bootanim']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][write read][open open][write read][append read][open open][write read]'
G.edge['bootanim']['bootanim']['fill'] = 'red'
G.add_edge('bootanim','bootanim')
G.edge['bootanim']['bootanim']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][write read][open open][write read][append read][open open][write read][append read]'
G.add_edge('bootanim','domain')
G.edge['bootanim']['domain']['write-read'] = '[open open][write read]'
G.edge['bootanim']['domain']['fill'] = 'red'
G.add_edge('bootanim','domain')
G.edge['bootanim']['domain']['write-read'] = '[open open][write read][append read]'
G.add_edge('bootanim','mediaserver')
G.edge['bootanim']['mediaserver']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read]'
G.edge['bootanim']['mediaserver']['fill'] = 'red'
G.add_edge('bootanim','mediaserver')
G.edge['bootanim']['mediaserver']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read]'
G.add_edge('domain','bootanim')
G.edge['domain']['bootanim']['write-read'] = '[write read][open open]'
G.add_edge('domain','domain')
G.edge['domain']['domain']['write-read'] = '[write read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][setpgid getpgid][setcap getcap][setsched getsched][open open][write read][append read][open open]'
G.add_edge('domain','mediaserver')
G.edge['domain']['mediaserver']['write-read'] = '[setattr getattr][add_name search][remove_name search][write read][open open][write read][append read][write read][setattr getattr][write read][append read][open open]'
G.add_edge('domain','bootanim')
G.edge['domain']['bootanim']['write-read'] = '[write read][open open][write read]'
G.edge['domain']['bootanim']['fill'] = 'red'
G.add_edge('domain','bootanim')
G.edge['domain']['bootanim']['write-read'] = '[write read][open open][write read][append read]'
G.add_edge('domain','domain')
G.edge['domain']['domain']['write-read'] = '[write read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][setpgid getpgid][setcap getcap][setsched getsched][open open][write read][append read][open open][write read]'
G.edge['domain']['domain']['fill'] = 'red'
G.add_edge('domain','domain')
G.edge['domain']['domain']['write-read'] = '[write read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][setpgid getpgid][setcap getcap][setsched getsched][open open][write read][append read][open open][write read][append read]'
G.add_edge('domain','mediaserver')
G.edge['domain']['mediaserver']['write-read'] = '[setattr getattr][add_name search][remove_name search][write read][open open][write read][append read][write read][setattr getattr][write read][append read][open open][write read]'
G.edge['domain']['mediaserver']['fill'] = 'red'
G.add_edge('domain','mediaserver')
G.edge['domain']['mediaserver']['write-read'] = '[setattr getattr][add_name search][remove_name search][write read][open open][write read][append read][write read][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('mediaserver','bootanim')
G.edge['mediaserver']['bootanim']['write-read'] = '[open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('mediaserver','domain')
G.edge['mediaserver']['domain']['write-read'] = '[open open]'
G.add_edge('mediaserver','mediaserver')
G.edge['mediaserver']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][write read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][open open]'
G.add_edge('mediaserver','bootanim')
G.edge['mediaserver']['bootanim']['write-read'] = '[open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][open open][write read]'
G.edge['mediaserver']['bootanim']['fill'] = 'red'
G.add_edge('mediaserver','bootanim')
G.edge['mediaserver']['bootanim']['write-read'] = '[open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][open open][write read][append read]'
G.add_edge('mediaserver','domain')
G.edge['mediaserver']['domain']['write-read'] = '[open open][write read]'
G.edge['mediaserver']['domain']['fill'] = 'red'
G.add_edge('mediaserver','domain')
G.edge['mediaserver']['domain']['write-read'] = '[open open][write read][append read]'
G.add_edge('mediaserver','mediaserver')
G.edge['mediaserver']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][write read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][open open][write read]'
G.edge['mediaserver']['mediaserver']['fill'] = 'red'
G.add_edge('mediaserver','mediaserver')
G.edge['mediaserver']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][write read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][open open][write read][append read]'
app = Viewer(G)
app.mainloop()