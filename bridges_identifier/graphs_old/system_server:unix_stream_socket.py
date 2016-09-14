import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('appdomain','appdomain')
G.edge['appdomain']['appdomain']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][write read][setattr getattr][write read][append read][setopt getopt][write read][open open][write read][append read][write read][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][setattr getattr][open execmod][write read][open open][open open][write read][append read][append read][open open][open open][write read][append read][append read][open open][write read][append read][open open][write read][append read][write read][write read][write read][write read][setopt getopt][setopt getopt][open open][setattr getattr][open execmod][write read][write read][open open][setattr getattr][write read][append read][write read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][add_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read][open open][write read][append read][open open][write read][append read][write read]'
G.edge['appdomain']['appdomain']['fill'] = 'red'
G.add_edge('appdomain','location')
G.edge['appdomain']['location']['write-read'] = '[write read]'
G.edge['appdomain']['location']['fill'] = 'red'
G.add_edge('appdomain','mm-pp-daemon')
G.edge['appdomain']['mm-pp-daemon']['write-read'] = '[write read]'
G.edge['appdomain']['mm-pp-daemon']['fill'] = 'red'
G.add_edge('appdomain','mm-qcamerad')
G.edge['appdomain']['mm-qcamerad']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][remove_name search][open open][open execmod][write read]'
G.edge['appdomain']['mm-qcamerad']['fill'] = 'red'
G.add_edge('appdomain','appdomain')
G.edge['appdomain']['appdomain']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][write read][setattr getattr][write read][append read][setopt getopt][write read][open open][write read][append read][write read][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][setattr getattr][open execmod][write read][open open][open open][write read][append read][append read][open open][open open][write read][append read][append read][open open][write read][append read][open open][write read][append read][write read][write read][write read][write read][setopt getopt][setopt getopt][open open][setattr getattr][open execmod][write read][write read][open open][setattr getattr][write read][append read][write read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][add_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read][open open][write read][append read][open open][write read][append read][write read][setopt getopt]'
G.add_edge('location','appdomain')
G.edge['location']['appdomain']['write-read'] = '[write read]'
G.edge['location']['appdomain']['fill'] = 'red'
G.add_edge('location','location')
G.edge['location']['location']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][write read][write read]'
G.edge['location']['location']['fill'] = 'red'
G.add_edge('location','mm-pp-daemon')
G.edge['location']['mm-pp-daemon']['write-read'] = '[write read]'
G.edge['location']['mm-pp-daemon']['fill'] = 'red'
G.add_edge('location','mm-qcamerad')
G.edge['location']['mm-qcamerad']['write-read'] = '[open open][write read][append read][write read]'
G.edge['location']['mm-qcamerad']['fill'] = 'red'
G.add_edge('mm-pp-daemon','appdomain')
G.edge['mm-pp-daemon']['appdomain']['write-read'] = '[write read]'
G.edge['mm-pp-daemon']['appdomain']['fill'] = 'red'
G.add_edge('mm-pp-daemon','location')
G.edge['mm-pp-daemon']['location']['write-read'] = '[open open][write read][append read][write read]'
G.edge['mm-pp-daemon']['location']['fill'] = 'red'
G.add_edge('mm-pp-daemon','mm-pp-daemon')
G.edge['mm-pp-daemon']['mm-pp-daemon']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][write read][append read][open open][write read][append read][write read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][write read]'
G.edge['mm-pp-daemon']['mm-pp-daemon']['fill'] = 'red'
G.add_edge('mm-pp-daemon','mm-qcamerad')
G.edge['mm-pp-daemon']['mm-qcamerad']['write-read'] = '[write read][open open][write read][append read][write read]'
G.edge['mm-pp-daemon']['mm-qcamerad']['fill'] = 'red'
G.add_edge('mm-qcamerad','appdomain')
G.edge['mm-qcamerad']['appdomain']['write-read'] = '[open open][write read][append read][write read]'
G.edge['mm-qcamerad']['appdomain']['fill'] = 'red'
G.add_edge('mm-qcamerad','location')
G.edge['mm-qcamerad']['location']['write-read'] = '[write read]'
G.edge['mm-qcamerad']['location']['fill'] = 'red'
G.add_edge('mm-qcamerad','mm-pp-daemon')
G.edge['mm-qcamerad']['mm-pp-daemon']['write-read'] = '[write read]'
G.edge['mm-qcamerad']['mm-pp-daemon']['fill'] = 'red'
G.add_edge('mm-qcamerad','mm-qcamerad')
G.edge['mm-qcamerad']['mm-qcamerad']['write-read'] = '[open open][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][add_name search][remove_name search][open open][write read][append read][write read]'
G.edge['mm-qcamerad']['mm-qcamerad']['fill'] = 'red'
app = Viewer(G)
app.mainloop()