import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('mm-pp-daemon','location')
G.edge['mm-pp-daemon']['location']['write-read'] = '[open open]'
G.add_edge('mm-pp-daemon','mm-pp-daemon')
G.edge['mm-pp-daemon']['mm-pp-daemon']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open]'
G.add_edge('mm-pp-daemon','sensors')
G.edge['mm-pp-daemon']['sensors']['write-read'] = '[open open]'
G.add_edge('mm-pp-daemon','sensors')
G.edge['mm-pp-daemon']['sensors']['write-read'] = '[open open][setattr getattr]'
G.add_edge('mm-pp-daemon','location')
G.edge['mm-pp-daemon']['location']['write-read'] = '[open open][write read]'
G.edge['mm-pp-daemon']['location']['fill'] = 'red'
G.add_edge('mm-pp-daemon','location')
G.edge['mm-pp-daemon']['location']['write-read'] = '[open open][write read][append read]'
G.add_edge('mm-pp-daemon','mm-pp-daemon')
G.edge['mm-pp-daemon']['mm-pp-daemon']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][write read]'
G.edge['mm-pp-daemon']['mm-pp-daemon']['fill'] = 'red'
G.add_edge('mm-pp-daemon','mm-pp-daemon')
G.edge['mm-pp-daemon']['mm-pp-daemon']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][write read][append read]'
G.add_edge('mm-pp-daemon','mm-qcamerad')
G.edge['mm-pp-daemon']['mm-qcamerad']['write-read'] = '[write read]'
G.edge['mm-pp-daemon']['mm-qcamerad']['fill'] = 'red'
G.add_edge('mm-pp-daemon','sensors')
G.edge['mm-pp-daemon']['sensors']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['mm-pp-daemon']['sensors']['fill'] = 'red'
G.add_edge('mm-pp-daemon','sensors')
G.edge['mm-pp-daemon']['sensors']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('mm-pp-daemon','system_server')
G.edge['mm-pp-daemon']['system_server']['write-read'] = '[write read]'
G.edge['mm-pp-daemon']['system_server']['fill'] = 'red'
G.add_edge('sensors','location')
G.edge['sensors']['location']['write-read'] = '[open open]'
G.add_edge('sensors','mm-pp-daemon')
G.edge['sensors']['mm-pp-daemon']['write-read'] = '[open open]'
G.add_edge('sensors','sensors')
G.edge['sensors']['sensors']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('sensors','sensors')
G.edge['sensors']['sensors']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('sensors','location')
G.edge['sensors']['location']['write-read'] = '[open open][write read]'
G.edge['sensors']['location']['fill'] = 'red'
G.add_edge('sensors','location')
G.edge['sensors']['location']['write-read'] = '[open open][write read][append read]'
G.add_edge('sensors','mm-pp-daemon')
G.edge['sensors']['mm-pp-daemon']['write-read'] = '[open open][write read]'
G.edge['sensors']['mm-pp-daemon']['fill'] = 'red'
G.add_edge('sensors','mm-pp-daemon')
G.edge['sensors']['mm-pp-daemon']['write-read'] = '[open open][write read][append read]'
G.add_edge('sensors','mm-qcamerad')
G.edge['sensors']['mm-qcamerad']['write-read'] = '[open open][write read][add_name search][remove_name search][write read]'
G.edge['sensors']['mm-qcamerad']['fill'] = 'red'
G.add_edge('sensors','sensors')
G.edge['sensors']['sensors']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['sensors']['sensors']['fill'] = 'red'
G.add_edge('sensors','sensors')
G.edge['sensors']['sensors']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('sensors','system_server')
G.edge['sensors']['system_server']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['sensors']['system_server']['fill'] = 'red'
G.add_edge('system_server','location')
G.edge['system_server']['location']['write-read'] = '[open open][write read][add_name search][remove_name search][open open]'
G.add_edge('system_server','mm-pp-daemon')
G.edge['system_server']['mm-pp-daemon']['write-read'] = '[open open]'
G.add_edge('system_server','sensors')
G.edge['system_server']['sensors']['write-read'] = '[add_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('system_server','sensors')
G.edge['system_server']['sensors']['write-read'] = '[add_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('system_server','location')
G.edge['system_server']['location']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['system_server']['location']['fill'] = 'red'
G.add_edge('system_server','location')
G.edge['system_server']['location']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('system_server','mm-pp-daemon')
G.edge['system_server']['mm-pp-daemon']['write-read'] = '[open open][write read]'
G.edge['system_server']['mm-pp-daemon']['fill'] = 'red'
G.add_edge('system_server','mm-pp-daemon')
G.edge['system_server']['mm-pp-daemon']['write-read'] = '[open open][write read][append read]'
G.add_edge('system_server','mm-qcamerad')
G.edge['system_server']['mm-qcamerad']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][remove_name search][write read]'
G.edge['system_server']['mm-qcamerad']['fill'] = 'red'
G.add_edge('system_server','sensors')
G.edge['system_server']['sensors']['write-read'] = '[add_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['system_server']['sensors']['fill'] = 'red'
G.add_edge('system_server','sensors')
G.edge['system_server']['sensors']['write-read'] = '[add_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][setsched getsched][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['system_server']['system_server']['fill'] = 'red'
app = Viewer(G)
app.mainloop()