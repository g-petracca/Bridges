import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('ipacm','ipacm')
G.edge['ipacm']['ipacm']['write-read'] = '[open open][add_name search][remove_name search][write read][write read][open open]'
G.add_edge('ipacm','ipacm')
G.edge['ipacm']['ipacm']['write-read'] = '[open open][add_name search][remove_name search][write read][write read][open open][setattr getattr]'
G.add_edge('ipacm','ipacm')
G.edge['ipacm']['ipacm']['write-read'] = '[open open][add_name search][remove_name search][write read][write read][open open][setattr getattr][write read]'
G.edge['ipacm']['ipacm']['fill'] = 'red'
G.add_edge('ipacm','ipacm')
G.edge['ipacm']['ipacm']['write-read'] = '[open open][add_name search][remove_name search][write read][write read][open open][setattr getattr][write read][append read]'
app = Viewer(G)
app.mainloop()