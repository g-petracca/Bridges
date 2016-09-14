import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('appdomain','appdomain')
G.edge['appdomain']['appdomain']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('appdomain','mm-qcamera-daemon')
G.edge['appdomain']['mm-qcamera-daemon']['write-read'] = '[open open][write read][add_name search][remove_name search][open open]'
G.add_edge('appdomain','radio')
G.edge['appdomain']['radio']['write-read'] = '[setattr getattr][open open]'
G.add_edge('appdomain','appdomain')
G.edge['appdomain']['appdomain']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read]'
G.edge['appdomain']['appdomain']['fill'] = 'red'
G.add_edge('appdomain','appdomain')
G.edge['appdomain']['appdomain']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read]'
G.add_edge('appdomain','mm-qcamera-daemon')
G.edge['appdomain']['mm-qcamera-daemon']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['appdomain']['mm-qcamera-daemon']['fill'] = 'red'
G.add_edge('appdomain','mm-qcamera-daemon')
G.edge['appdomain']['mm-qcamera-daemon']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('appdomain','radio')
G.edge['appdomain']['radio']['write-read'] = '[setattr getattr][open open][write read]'
G.edge['appdomain']['radio']['fill'] = 'red'
G.add_edge('appdomain','radio')
G.edge['appdomain']['radio']['write-read'] = '[setattr getattr][open open][write read][append read]'
G.add_edge('mm-qcamera-daemon','appdomain')
G.edge['mm-qcamera-daemon']['appdomain']['write-read'] = '[open open]'
G.add_edge('mm-qcamera-daemon','mm-qcamera-daemon')
G.edge['mm-qcamera-daemon']['mm-qcamera-daemon']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('mm-qcamera-daemon','radio')
G.edge['mm-qcamera-daemon']['radio']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('mm-qcamera-daemon','appdomain')
G.edge['mm-qcamera-daemon']['appdomain']['write-read'] = '[open open][write read]'
G.edge['mm-qcamera-daemon']['appdomain']['fill'] = 'red'
G.add_edge('mm-qcamera-daemon','appdomain')
G.edge['mm-qcamera-daemon']['appdomain']['write-read'] = '[open open][write read][append read]'
G.add_edge('mm-qcamera-daemon','mm-qcamera-daemon')
G.edge['mm-qcamera-daemon']['mm-qcamera-daemon']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['mm-qcamera-daemon']['mm-qcamera-daemon']['fill'] = 'red'
G.add_edge('mm-qcamera-daemon','mm-qcamera-daemon')
G.edge['mm-qcamera-daemon']['mm-qcamera-daemon']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('mm-qcamera-daemon','radio')
G.edge['mm-qcamera-daemon']['radio']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['mm-qcamera-daemon']['radio']['fill'] = 'red'
G.add_edge('mm-qcamera-daemon','radio')
G.edge['mm-qcamera-daemon']['radio']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('radio','appdomain')
G.edge['radio']['appdomain']['write-read'] = '[open open]'
G.add_edge('radio','mm-qcamera-daemon')
G.edge['radio']['mm-qcamera-daemon']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('radio','radio')
G.edge['radio']['radio']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('radio','appdomain')
G.edge['radio']['appdomain']['write-read'] = '[open open][write read]'
G.edge['radio']['appdomain']['fill'] = 'red'
G.add_edge('radio','appdomain')
G.edge['radio']['appdomain']['write-read'] = '[open open][write read][append read]'
G.add_edge('radio','mm-qcamera-daemon')
G.edge['radio']['mm-qcamera-daemon']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['radio']['mm-qcamera-daemon']['fill'] = 'red'
G.add_edge('radio','mm-qcamera-daemon')
G.edge['radio']['mm-qcamera-daemon']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('radio','radio')
G.edge['radio']['radio']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['radio']['radio']['fill'] = 'red'
G.add_edge('radio','radio')
G.edge['radio']['radio']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read]'
app = Viewer(G)
app.mainloop()