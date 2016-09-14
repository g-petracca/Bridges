import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('bluetooth','mm-pp-daemon')
G.edge['bluetooth']['mm-pp-daemon']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][write read][add_name search]'
G.add_edge('bluetooth','mm-pp-daemon')
G.edge['bluetooth']['mm-pp-daemon']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][write read][add_name search][remove_name search]'
G.add_edge('mm-pp-daemon','mm-pp-daemon')
G.edge['mm-pp-daemon']['mm-pp-daemon']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][write read][append read][open open][write read][append read][write read][open open]'
G.add_edge('mm-pp-daemon','mm-pp-daemon')
G.edge['mm-pp-daemon']['mm-pp-daemon']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][write read][append read][open open][write read][append read][write read][open open][write read]'
G.edge['mm-pp-daemon']['mm-pp-daemon']['fill'] = 'red'
G.add_edge('mm-pp-daemon','mm-pp-daemon')
G.edge['mm-pp-daemon']['mm-pp-daemon']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][write read][append read][open open][write read][append read][write read][open open][write read][add_name search]'
G.add_edge('mm-pp-daemon','mm-pp-daemon')
G.edge['mm-pp-daemon']['mm-pp-daemon']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][write read][append read][open open][write read][append read][write read][open open][write read][add_name search][remove_name search]'
G.add_edge('sensors','mm-pp-daemon')
G.edge['sensors']['mm-pp-daemon']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('sensors','mm-pp-daemon')
G.edge['sensors']['mm-pp-daemon']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['sensors']['mm-pp-daemon']['fill'] = 'red'
G.add_edge('sensors','mm-pp-daemon')
G.edge['sensors']['mm-pp-daemon']['write-read'] = '[open open][write read][append read][open open][write read][add_name search]'
G.add_edge('sensors','mm-pp-daemon')
G.edge['sensors']['mm-pp-daemon']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('shell','mm-pp-daemon')
G.edge['shell']['mm-pp-daemon']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('shell','mm-pp-daemon')
G.edge['shell']['mm-pp-daemon']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read]'
G.edge['shell']['mm-pp-daemon']['fill'] = 'red'
G.add_edge('shell','mm-pp-daemon')
G.edge['shell']['mm-pp-daemon']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search]'
G.add_edge('shell','mm-pp-daemon')
G.edge['shell']['mm-pp-daemon']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('system_server','mm-pp-daemon')
G.edge['system_server']['mm-pp-daemon']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][write read][add_name search]'
G.add_edge('system_server','mm-pp-daemon')
G.edge['system_server']['mm-pp-daemon']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][write read][add_name search][remove_name search]'
G.add_edge('tee','mm-pp-daemon')
G.edge['tee']['mm-pp-daemon']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('tee','mm-pp-daemon')
G.edge['tee']['mm-pp-daemon']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['tee']['mm-pp-daemon']['fill'] = 'red'
G.add_edge('tee','mm-pp-daemon')
G.edge['tee']['mm-pp-daemon']['write-read'] = '[open open][write read][append read][open open][write read][add_name search]'
G.add_edge('tee','mm-pp-daemon')
G.edge['tee']['mm-pp-daemon']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('ueventd','mm-pp-daemon')
G.edge['ueventd']['mm-pp-daemon']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][write read][add_name search]'
G.add_edge('ueventd','mm-pp-daemon')
G.edge['ueventd']['mm-pp-daemon']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][write read][add_name search][remove_name search]'
G.add_edge('usf','mm-pp-daemon')
G.edge['usf']['mm-pp-daemon']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('usf','mm-pp-daemon')
G.edge['usf']['mm-pp-daemon']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read]'
G.edge['usf']['mm-pp-daemon']['fill'] = 'red'
G.add_edge('usf','mm-pp-daemon')
G.edge['usf']['mm-pp-daemon']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search]'
G.add_edge('usf','mm-pp-daemon')
G.edge['usf']['mm-pp-daemon']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('wcnss_service','mm-pp-daemon')
G.edge['wcnss_service']['mm-pp-daemon']['write-read'] = '[open open]'
G.add_edge('wcnss_service','mm-pp-daemon')
G.edge['wcnss_service']['mm-pp-daemon']['write-read'] = '[open open][write read]'
G.edge['wcnss_service']['mm-pp-daemon']['fill'] = 'red'
G.add_edge('wcnss_service','mm-pp-daemon')
G.edge['wcnss_service']['mm-pp-daemon']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('wcnss_service','mm-pp-daemon')
G.edge['wcnss_service']['mm-pp-daemon']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('wpa','mm-pp-daemon')
G.edge['wpa']['mm-pp-daemon']['write-read'] = '[add_name search]'
G.add_edge('wpa','mm-pp-daemon')
G.edge['wpa']['mm-pp-daemon']['write-read'] = '[add_name search][remove_name search]'
app = Viewer(G)
app.mainloop()