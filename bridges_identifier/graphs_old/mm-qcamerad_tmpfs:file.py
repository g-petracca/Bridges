import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('mm-qcamerad','mm-qcamerad')
G.edge['mm-qcamerad']['mm-qcamerad']['write-read'] = '[open open][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][add_name search][remove_name search][open open][write read][append read][write read][write read]'
G.edge['mm-qcamerad']['mm-qcamerad']['fill'] = 'red'
app = Viewer(G)
app.mainloop()