import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('drsd','drsd')
G.edge['drsd']['drsd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][relabelto relabelfrom][open open][write read][relabelto relabelfrom][open open][write read][open open][write read][relabelto relabelfrom][open open][write read][relabelto relabelfrom][open open][write read][open open][write read][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open]'
G.add_edge('drsd','drsd')
G.edge['drsd']['drsd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][relabelto relabelfrom][open open][write read][relabelto relabelfrom][open open][write read][open open][write read][relabelto relabelfrom][open open][write read][relabelto relabelfrom][open open][write read][open open][write read][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['drsd']['drsd']['fill'] = 'red'
G.add_edge('drsd','drsd')
G.edge['drsd']['drsd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][relabelto relabelfrom][open open][write read][relabelto relabelfrom][open open][write read][open open][write read][relabelto relabelfrom][open open][write read][relabelto relabelfrom][open open][write read][open open][write read][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][relabelto relabelfrom]'
app = Viewer(G)
app.mainloop()