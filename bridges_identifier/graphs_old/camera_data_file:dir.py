import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('mediaserver','mm-qcamerad')
G.edge['mediaserver']['mm-qcamerad']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][remove_name search][write read]'
G.edge['mediaserver']['mm-qcamerad']['fill'] = 'red'
G.add_edge('mediaserver','mm-qcamerad')
G.edge['mediaserver']['mm-qcamerad']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][remove_name search][write read][add_name search]'
G.add_edge('mediaserver','mm-qcamerad')
G.edge['mediaserver']['mm-qcamerad']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][remove_name search][write read][add_name search][remove_name search]'
G.add_edge('mm-qcamerad','mm-qcamerad')
G.edge['mm-qcamerad']['mm-qcamerad']['write-read'] = '[open open][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][add_name search][remove_name search][add_name search]'
G.add_edge('mm-qcamerad','mm-qcamerad')
G.edge['mm-qcamerad']['mm-qcamerad']['write-read'] = '[open open][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][add_name search][remove_name search][add_name search][remove_name search]'
app = Viewer(G)
app.mainloop()