import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('ppp','ppp')
G.edge['ppp']['ppp']['write-read'] = '[open open][write read][append read][setattr getattr]'
G.add_edge('ppp','pppoewrapper')
G.edge['ppp']['pppoewrapper']['write-read'] = '[open open][write read][append read][setattr getattr]'
G.add_edge('ppp','ppp')
G.edge['ppp']['ppp']['write-read'] = '[open open][write read][append read][setattr getattr][write read]'
G.edge['ppp']['ppp']['fill'] = 'red'
G.add_edge('ppp','ppp')
G.edge['ppp']['ppp']['write-read'] = '[open open][write read][append read][setattr getattr][write read][append read]'
G.add_edge('ppp','pppoewrapper')
G.edge['ppp']['pppoewrapper']['write-read'] = '[open open][write read][append read][setattr getattr][write read]'
G.edge['ppp']['pppoewrapper']['fill'] = 'red'
G.add_edge('ppp','pppoewrapper')
G.edge['ppp']['pppoewrapper']['write-read'] = '[open open][write read][append read][setattr getattr][write read][append read]'
G.add_edge('ppp','ppp')
G.edge['ppp']['ppp']['write-read'] = '[open open][write read][append read][setattr getattr][write read][append read][setopt getopt]'
G.add_edge('ppp','pppoewrapper')
G.edge['ppp']['pppoewrapper']['write-read'] = '[open open][write read][append read][setattr getattr][write read][append read][setopt getopt]'
G.add_edge('pppoewrapper','ppp')
G.edge['pppoewrapper']['ppp']['write-read'] = '[open open][write read][append read][setattr getattr]'
G.add_edge('pppoewrapper','pppoewrapper')
G.edge['pppoewrapper']['pppoewrapper']['write-read'] = '[write read][open open][write read][append read][setattr getattr]'
G.add_edge('pppoewrapper','ppp')
G.edge['pppoewrapper']['ppp']['write-read'] = '[open open][write read][append read][setattr getattr][write read]'
G.edge['pppoewrapper']['ppp']['fill'] = 'red'
G.add_edge('pppoewrapper','ppp')
G.edge['pppoewrapper']['ppp']['write-read'] = '[open open][write read][append read][setattr getattr][write read][append read]'
G.add_edge('pppoewrapper','pppoewrapper')
G.edge['pppoewrapper']['pppoewrapper']['write-read'] = '[write read][open open][write read][append read][setattr getattr][write read]'
G.edge['pppoewrapper']['pppoewrapper']['fill'] = 'red'
G.add_edge('pppoewrapper','pppoewrapper')
G.edge['pppoewrapper']['pppoewrapper']['write-read'] = '[write read][open open][write read][append read][setattr getattr][write read][append read]'
G.add_edge('pppoewrapper','ppp')
G.edge['pppoewrapper']['ppp']['write-read'] = '[open open][write read][append read][setattr getattr][write read][append read][setopt getopt]'
G.add_edge('pppoewrapper','pppoewrapper')
G.edge['pppoewrapper']['pppoewrapper']['write-read'] = '[write read][open open][write read][append read][setattr getattr][write read][append read][setopt getopt]'
app = Viewer(G)
app.mainloop()