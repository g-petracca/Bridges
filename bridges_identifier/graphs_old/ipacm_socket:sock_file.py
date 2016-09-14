import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('ipacm-diag','ipacm-diag')
G.edge['ipacm-diag']['ipacm-diag']['write-read'] = '[write read][open open][open open][write read][write read][add_name search][add_name search][remove_name search][open open][open open][write read][write read][add_name search][add_name search][remove_name search][open open]'
G.add_edge('ipacm-diag','ipacm-diag')
G.edge['ipacm-diag']['ipacm-diag']['write-read'] = '[write read][open open][open open][write read][write read][add_name search][add_name search][remove_name search][open open][open open][write read][write read][add_name search][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('ipacm-diag','ipacm-diag')
G.edge['ipacm-diag']['ipacm-diag']['write-read'] = '[write read][open open][open open][write read][write read][add_name search][add_name search][remove_name search][open open][open open][write read][write read][add_name search][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['ipacm-diag']['ipacm-diag']['fill'] = 'red'
G.add_edge('ipacm-diag','ipacm-diag')
G.edge['ipacm-diag']['ipacm-diag']['write-read'] = '[write read][open open][open open][write read][write read][add_name search][add_name search][remove_name search][open open][open open][write read][write read][add_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('ipacm-diag','ipacm')
G.edge['ipacm-diag']['ipacm']['write-read'] = '[write read]'
G.edge['ipacm-diag']['ipacm']['fill'] = 'red'
app = Viewer(G)
app.mainloop()