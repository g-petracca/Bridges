import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('mobexdaemon','mobexdaemon')
G.edge['mobexdaemon']['mobexdaemon']['write-read'] = '[write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read]'
G.edge['mobexdaemon']['mobexdaemon']['fill'] = 'red'
app = Viewer(G)
app.mainloop()