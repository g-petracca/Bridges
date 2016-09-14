import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('appdomain','appdomain')
G.edge['appdomain']['appdomain']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('appdomain','appdomain')
G.edge['appdomain']['appdomain']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['appdomain']['appdomain']['fill'] = 'red'
G.add_edge('appdomain','appdomain')
G.edge['appdomain']['appdomain']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('appdomain','otp_server')
G.edge['appdomain']['otp_server']['write-read'] = '[write read]'
G.edge['appdomain']['otp_server']['fill'] = 'red'
G.add_edge('appdomain','tlc_server')
G.edge['appdomain']['tlc_server']['write-read'] = '[write read]'
G.edge['appdomain']['tlc_server']['fill'] = 'red'
G.add_edge('mediaserver','appdomain')
G.edge['mediaserver']['appdomain']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('mediaserver','appdomain')
G.edge['mediaserver']['appdomain']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['mediaserver']['appdomain']['fill'] = 'red'
G.add_edge('mediaserver','appdomain')
G.edge['mediaserver']['appdomain']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('mediaserver','otp_server')
G.edge['mediaserver']['otp_server']['write-read'] = '[write read]'
G.edge['mediaserver']['otp_server']['fill'] = 'red'
G.add_edge('mediaserver','tlc_server')
G.edge['mediaserver']['tlc_server']['write-read'] = '[write read]'
G.edge['mediaserver']['tlc_server']['fill'] = 'red'
G.add_edge('otp_server','appdomain')
G.edge['otp_server']['appdomain']['write-read'] = '[write read]'
G.edge['otp_server']['appdomain']['fill'] = 'red'
G.add_edge('otp_server','appdomain')
G.edge['otp_server']['appdomain']['write-read'] = '[write read][append read]'
G.add_edge('otp_server','otp_server')
G.edge['otp_server']['otp_server']['write-read'] = '[write read]'
G.edge['otp_server']['otp_server']['fill'] = 'red'
G.add_edge('otp_server','tlc_server')
G.edge['otp_server']['tlc_server']['write-read'] = '[write read]'
G.edge['otp_server']['tlc_server']['fill'] = 'red'
G.add_edge('tlc_server','appdomain')
G.edge['tlc_server']['appdomain']['write-read'] = '[write read]'
G.edge['tlc_server']['appdomain']['fill'] = 'red'
G.add_edge('tlc_server','appdomain')
G.edge['tlc_server']['appdomain']['write-read'] = '[write read][append read]'
G.add_edge('tlc_server','otp_server')
G.edge['tlc_server']['otp_server']['write-read'] = '[write read]'
G.edge['tlc_server']['otp_server']['fill'] = 'red'
G.add_edge('tlc_server','tlc_server')
G.edge['tlc_server']['tlc_server']['write-read'] = '[write read]'
G.edge['tlc_server']['tlc_server']['fill'] = 'red'
app = Viewer(G)
app.mainloop()