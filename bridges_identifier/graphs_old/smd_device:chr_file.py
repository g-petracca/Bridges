import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('bluetooth','bluetooth')
G.edge['bluetooth']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('bluetooth','init_shell')
G.edge['bluetooth']['init_shell']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('bluetooth','qmuxd')
G.edge['bluetooth']['qmuxd']['write-read'] = '[open open]'
G.add_edge('bluetooth','qti')
G.edge['bluetooth']['qti']['write-read'] = '[open open]'
G.add_edge('bluetooth','radio')
G.edge['bluetooth']['radio']['write-read'] = '[open open]'
G.add_edge('bluetooth','sensors')
G.edge['bluetooth']['sensors']['write-read'] = '[open open]'
G.add_edge('bluetooth','smdexe')
G.edge['bluetooth']['smdexe']['write-read'] = '[open open]'
G.add_edge('bluetooth','system_server')
G.edge['bluetooth']['system_server']['write-read'] = '[open open]'
G.add_edge('bluetooth','bluetooth')
G.edge['bluetooth']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['bluetooth']['bluetooth']['fill'] = 'red'
G.add_edge('bluetooth','bluetooth')
G.edge['bluetooth']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('bluetooth','init_shell')
G.edge['bluetooth']['init_shell']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['bluetooth']['init_shell']['fill'] = 'red'
G.add_edge('bluetooth','init_shell')
G.edge['bluetooth']['init_shell']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('bluetooth','qmuxd')
G.edge['bluetooth']['qmuxd']['write-read'] = '[open open][write read]'
G.edge['bluetooth']['qmuxd']['fill'] = 'red'
G.add_edge('bluetooth','qmuxd')
G.edge['bluetooth']['qmuxd']['write-read'] = '[open open][write read][append read]'
G.add_edge('bluetooth','qti')
G.edge['bluetooth']['qti']['write-read'] = '[open open][write read]'
G.edge['bluetooth']['qti']['fill'] = 'red'
G.add_edge('bluetooth','qti')
G.edge['bluetooth']['qti']['write-read'] = '[open open][write read][append read]'
G.add_edge('bluetooth','radio')
G.edge['bluetooth']['radio']['write-read'] = '[open open][write read]'
G.edge['bluetooth']['radio']['fill'] = 'red'
G.add_edge('bluetooth','radio')
G.edge['bluetooth']['radio']['write-read'] = '[open open][write read][append read]'
G.add_edge('bluetooth','sensors')
G.edge['bluetooth']['sensors']['write-read'] = '[open open][write read]'
G.edge['bluetooth']['sensors']['fill'] = 'red'
G.add_edge('bluetooth','sensors')
G.edge['bluetooth']['sensors']['write-read'] = '[open open][write read][append read]'
G.add_edge('bluetooth','smdexe')
G.edge['bluetooth']['smdexe']['write-read'] = '[open open][write read]'
G.edge['bluetooth']['smdexe']['fill'] = 'red'
G.add_edge('bluetooth','smdexe')
G.edge['bluetooth']['smdexe']['write-read'] = '[open open][write read][append read]'
G.add_edge('bluetooth','system_server')
G.edge['bluetooth']['system_server']['write-read'] = '[open open][write read]'
G.edge['bluetooth']['system_server']['fill'] = 'red'
G.add_edge('bluetooth','system_server')
G.edge['bluetooth']['system_server']['write-read'] = '[open open][write read][append read]'
G.add_edge('init_shell','bluetooth')
G.edge['init_shell']['bluetooth']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('init_shell','init_shell')
G.edge['init_shell']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('init_shell','qmuxd')
G.edge['init_shell']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('init_shell','qti')
G.edge['init_shell']['qti']['write-read'] = '[open open]'
G.add_edge('init_shell','radio')
G.edge['init_shell']['radio']['write-read'] = '[open open]'
G.add_edge('init_shell','sensors')
G.edge['init_shell']['sensors']['write-read'] = '[add_name search][open open]'
G.add_edge('init_shell','smdexe')
G.edge['init_shell']['smdexe']['write-read'] = '[open open]'
G.add_edge('init_shell','system_server')
G.edge['init_shell']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('init_shell','bluetooth')
G.edge['init_shell']['bluetooth']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['init_shell']['bluetooth']['fill'] = 'red'
G.add_edge('init_shell','bluetooth')
G.edge['init_shell']['bluetooth']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('init_shell','init_shell')
G.edge['init_shell']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['init_shell']['init_shell']['fill'] = 'red'
G.add_edge('init_shell','init_shell')
G.edge['init_shell']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('init_shell','qmuxd')
G.edge['init_shell']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['init_shell']['qmuxd']['fill'] = 'red'
G.add_edge('init_shell','qmuxd')
G.edge['init_shell']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('init_shell','qti')
G.edge['init_shell']['qti']['write-read'] = '[open open][write read]'
G.edge['init_shell']['qti']['fill'] = 'red'
G.add_edge('init_shell','qti')
G.edge['init_shell']['qti']['write-read'] = '[open open][write read][append read]'
G.add_edge('init_shell','radio')
G.edge['init_shell']['radio']['write-read'] = '[open open][write read]'
G.edge['init_shell']['radio']['fill'] = 'red'
G.add_edge('init_shell','radio')
G.edge['init_shell']['radio']['write-read'] = '[open open][write read][append read]'
G.add_edge('init_shell','sensors')
G.edge['init_shell']['sensors']['write-read'] = '[add_name search][open open][write read]'
G.edge['init_shell']['sensors']['fill'] = 'red'
G.add_edge('init_shell','sensors')
G.edge['init_shell']['sensors']['write-read'] = '[add_name search][open open][write read][append read]'
G.add_edge('init_shell','smdexe')
G.edge['init_shell']['smdexe']['write-read'] = '[open open][write read]'
G.edge['init_shell']['smdexe']['fill'] = 'red'
G.add_edge('init_shell','smdexe')
G.edge['init_shell']['smdexe']['write-read'] = '[open open][write read][append read]'
G.add_edge('init_shell','system_server')
G.edge['init_shell']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['init_shell']['system_server']['fill'] = 'red'
G.add_edge('init_shell','system_server')
G.edge['init_shell']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('qmuxd','bluetooth')
G.edge['qmuxd']['bluetooth']['write-read'] = '[open open]'
G.add_edge('qmuxd','init_shell')
G.edge['qmuxd']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('qmuxd','qmuxd')
G.edge['qmuxd']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('qmuxd','qti')
G.edge['qmuxd']['qti']['write-read'] = '[open open]'
G.add_edge('qmuxd','radio')
G.edge['qmuxd']['radio']['write-read'] = '[open open]'
G.add_edge('qmuxd','sensors')
G.edge['qmuxd']['sensors']['write-read'] = '[add_name search][open open]'
G.add_edge('qmuxd','smdexe')
G.edge['qmuxd']['smdexe']['write-read'] = '[open open]'
G.add_edge('qmuxd','system_server')
G.edge['qmuxd']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open]'
G.add_edge('qmuxd','bluetooth')
G.edge['qmuxd']['bluetooth']['write-read'] = '[open open][write read]'
G.edge['qmuxd']['bluetooth']['fill'] = 'red'
G.add_edge('qmuxd','bluetooth')
G.edge['qmuxd']['bluetooth']['write-read'] = '[open open][write read][append read]'
G.add_edge('qmuxd','init_shell')
G.edge['qmuxd']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['qmuxd']['init_shell']['fill'] = 'red'
G.add_edge('qmuxd','init_shell')
G.edge['qmuxd']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('qmuxd','qmuxd')
G.edge['qmuxd']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['qmuxd']['qmuxd']['fill'] = 'red'
G.add_edge('qmuxd','qmuxd')
G.edge['qmuxd']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('qmuxd','qti')
G.edge['qmuxd']['qti']['write-read'] = '[open open][write read]'
G.edge['qmuxd']['qti']['fill'] = 'red'
G.add_edge('qmuxd','qti')
G.edge['qmuxd']['qti']['write-read'] = '[open open][write read][append read]'
G.add_edge('qmuxd','radio')
G.edge['qmuxd']['radio']['write-read'] = '[open open][write read]'
G.edge['qmuxd']['radio']['fill'] = 'red'
G.add_edge('qmuxd','radio')
G.edge['qmuxd']['radio']['write-read'] = '[open open][write read][append read]'
G.add_edge('qmuxd','sensors')
G.edge['qmuxd']['sensors']['write-read'] = '[add_name search][open open][write read]'
G.edge['qmuxd']['sensors']['fill'] = 'red'
G.add_edge('qmuxd','sensors')
G.edge['qmuxd']['sensors']['write-read'] = '[add_name search][open open][write read][append read]'
G.add_edge('qmuxd','smdexe')
G.edge['qmuxd']['smdexe']['write-read'] = '[open open][write read]'
G.edge['qmuxd']['smdexe']['fill'] = 'red'
G.add_edge('qmuxd','smdexe')
G.edge['qmuxd']['smdexe']['write-read'] = '[open open][write read][append read]'
G.add_edge('qmuxd','system_server')
G.edge['qmuxd']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read]'
G.edge['qmuxd']['system_server']['fill'] = 'red'
G.add_edge('qmuxd','system_server')
G.edge['qmuxd']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read]'
G.add_edge('qti','bluetooth')
G.edge['qti']['bluetooth']['write-read'] = '[open open]'
G.add_edge('qti','init_shell')
G.edge['qti']['init_shell']['write-read'] = '[open open]'
G.add_edge('qti','qmuxd')
G.edge['qti']['qmuxd']['write-read'] = '[open open]'
G.add_edge('qti','qti')
G.edge['qti']['qti']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('qti','radio')
G.edge['qti']['radio']['write-read'] = '[open open]'
G.add_edge('qti','sensors')
G.edge['qti']['sensors']['write-read'] = '[open open]'
G.add_edge('qti','smdexe')
G.edge['qti']['smdexe']['write-read'] = '[open open]'
G.add_edge('qti','system_server')
G.edge['qti']['system_server']['write-read'] = '[open open]'
G.add_edge('qti','bluetooth')
G.edge['qti']['bluetooth']['write-read'] = '[open open][write read]'
G.edge['qti']['bluetooth']['fill'] = 'red'
G.add_edge('qti','bluetooth')
G.edge['qti']['bluetooth']['write-read'] = '[open open][write read][append read]'
G.add_edge('qti','init_shell')
G.edge['qti']['init_shell']['write-read'] = '[open open][write read]'
G.edge['qti']['init_shell']['fill'] = 'red'
G.add_edge('qti','init_shell')
G.edge['qti']['init_shell']['write-read'] = '[open open][write read][append read]'
G.add_edge('qti','qmuxd')
G.edge['qti']['qmuxd']['write-read'] = '[open open][write read]'
G.edge['qti']['qmuxd']['fill'] = 'red'
G.add_edge('qti','qmuxd')
G.edge['qti']['qmuxd']['write-read'] = '[open open][write read][append read]'
G.add_edge('qti','qti')
G.edge['qti']['qti']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['qti']['qti']['fill'] = 'red'
G.add_edge('qti','qti')
G.edge['qti']['qti']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('qti','radio')
G.edge['qti']['radio']['write-read'] = '[open open][write read]'
G.edge['qti']['radio']['fill'] = 'red'
G.add_edge('qti','radio')
G.edge['qti']['radio']['write-read'] = '[open open][write read][append read]'
G.add_edge('qti','sensors')
G.edge['qti']['sensors']['write-read'] = '[open open][write read]'
G.edge['qti']['sensors']['fill'] = 'red'
G.add_edge('qti','sensors')
G.edge['qti']['sensors']['write-read'] = '[open open][write read][append read]'
G.add_edge('qti','smdexe')
G.edge['qti']['smdexe']['write-read'] = '[open open][write read]'
G.edge['qti']['smdexe']['fill'] = 'red'
G.add_edge('qti','smdexe')
G.edge['qti']['smdexe']['write-read'] = '[open open][write read][append read]'
G.add_edge('qti','system_server')
G.edge['qti']['system_server']['write-read'] = '[open open][write read]'
G.edge['qti']['system_server']['fill'] = 'red'
G.add_edge('qti','system_server')
G.edge['qti']['system_server']['write-read'] = '[open open][write read][append read]'
G.add_edge('radio','bluetooth')
G.edge['radio']['bluetooth']['write-read'] = '[open open]'
G.add_edge('radio','init_shell')
G.edge['radio']['init_shell']['write-read'] = '[add_name search][remove_name search][open open]'
G.add_edge('radio','qmuxd')
G.edge['radio']['qmuxd']['write-read'] = '[open open]'
G.add_edge('radio','qti')
G.edge['radio']['qti']['write-read'] = '[open open]'
G.add_edge('radio','radio')
G.edge['radio']['radio']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('radio','sensors')
G.edge['radio']['sensors']['write-read'] = '[open open]'
G.add_edge('radio','smdexe')
G.edge['radio']['smdexe']['write-read'] = '[open open]'
G.add_edge('radio','system_server')
G.edge['radio']['system_server']['write-read'] = '[add_name search][remove_name search][open open]'
G.add_edge('radio','bluetooth')
G.edge['radio']['bluetooth']['write-read'] = '[open open][write read]'
G.edge['radio']['bluetooth']['fill'] = 'red'
G.add_edge('radio','bluetooth')
G.edge['radio']['bluetooth']['write-read'] = '[open open][write read][append read]'
G.add_edge('radio','init_shell')
G.edge['radio']['init_shell']['write-read'] = '[add_name search][remove_name search][open open][write read]'
G.edge['radio']['init_shell']['fill'] = 'red'
G.add_edge('radio','init_shell')
G.edge['radio']['init_shell']['write-read'] = '[add_name search][remove_name search][open open][write read][append read]'
G.add_edge('radio','qmuxd')
G.edge['radio']['qmuxd']['write-read'] = '[open open][write read]'
G.edge['radio']['qmuxd']['fill'] = 'red'
G.add_edge('radio','qmuxd')
G.edge['radio']['qmuxd']['write-read'] = '[open open][write read][append read]'
G.add_edge('radio','qti')
G.edge['radio']['qti']['write-read'] = '[open open][write read]'
G.edge['radio']['qti']['fill'] = 'red'
G.add_edge('radio','qti')
G.edge['radio']['qti']['write-read'] = '[open open][write read][append read]'
G.add_edge('radio','radio')
G.edge['radio']['radio']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['radio']['radio']['fill'] = 'red'
G.add_edge('radio','radio')
G.edge['radio']['radio']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('radio','sensors')
G.edge['radio']['sensors']['write-read'] = '[open open][write read]'
G.edge['radio']['sensors']['fill'] = 'red'
G.add_edge('radio','sensors')
G.edge['radio']['sensors']['write-read'] = '[open open][write read][append read]'
G.add_edge('radio','smdexe')
G.edge['radio']['smdexe']['write-read'] = '[open open][write read]'
G.edge['radio']['smdexe']['fill'] = 'red'
G.add_edge('radio','smdexe')
G.edge['radio']['smdexe']['write-read'] = '[open open][write read][append read]'
G.add_edge('radio','system_server')
G.edge['radio']['system_server']['write-read'] = '[add_name search][remove_name search][open open][write read]'
G.edge['radio']['system_server']['fill'] = 'red'
G.add_edge('radio','system_server')
G.edge['radio']['system_server']['write-read'] = '[add_name search][remove_name search][open open][write read][append read]'
G.add_edge('sensors','bluetooth')
G.edge['sensors']['bluetooth']['write-read'] = '[open open]'
G.add_edge('sensors','init_shell')
G.edge['sensors']['init_shell']['write-read'] = '[open open]'
G.add_edge('sensors','qmuxd')
G.edge['sensors']['qmuxd']['write-read'] = '[open open]'
G.add_edge('sensors','qti')
G.edge['sensors']['qti']['write-read'] = '[open open]'
G.add_edge('sensors','radio')
G.edge['sensors']['radio']['write-read'] = '[open open]'
G.add_edge('sensors','sensors')
G.edge['sensors']['sensors']['write-read'] = '[open open]'
G.add_edge('sensors','smdexe')
G.edge['sensors']['smdexe']['write-read'] = '[open open]'
G.add_edge('sensors','system_server')
G.edge['sensors']['system_server']['write-read'] = '[open open]'
G.add_edge('sensors','bluetooth')
G.edge['sensors']['bluetooth']['write-read'] = '[open open][write read]'
G.edge['sensors']['bluetooth']['fill'] = 'red'
G.add_edge('sensors','bluetooth')
G.edge['sensors']['bluetooth']['write-read'] = '[open open][write read][append read]'
G.add_edge('sensors','init_shell')
G.edge['sensors']['init_shell']['write-read'] = '[open open][write read]'
G.edge['sensors']['init_shell']['fill'] = 'red'
G.add_edge('sensors','init_shell')
G.edge['sensors']['init_shell']['write-read'] = '[open open][write read][append read]'
G.add_edge('sensors','qmuxd')
G.edge['sensors']['qmuxd']['write-read'] = '[open open][write read]'
G.edge['sensors']['qmuxd']['fill'] = 'red'
G.add_edge('sensors','qmuxd')
G.edge['sensors']['qmuxd']['write-read'] = '[open open][write read][append read]'
G.add_edge('sensors','qti')
G.edge['sensors']['qti']['write-read'] = '[open open][write read]'
G.edge['sensors']['qti']['fill'] = 'red'
G.add_edge('sensors','qti')
G.edge['sensors']['qti']['write-read'] = '[open open][write read][append read]'
G.add_edge('sensors','radio')
G.edge['sensors']['radio']['write-read'] = '[open open][write read]'
G.edge['sensors']['radio']['fill'] = 'red'
G.add_edge('sensors','radio')
G.edge['sensors']['radio']['write-read'] = '[open open][write read][append read]'
G.add_edge('sensors','sensors')
G.edge['sensors']['sensors']['write-read'] = '[open open][write read]'
G.edge['sensors']['sensors']['fill'] = 'red'
G.add_edge('sensors','sensors')
G.edge['sensors']['sensors']['write-read'] = '[open open][write read][append read]'
G.add_edge('sensors','smdexe')
G.edge['sensors']['smdexe']['write-read'] = '[open open][write read]'
G.edge['sensors']['smdexe']['fill'] = 'red'
G.add_edge('sensors','smdexe')
G.edge['sensors']['smdexe']['write-read'] = '[open open][write read][append read]'
G.add_edge('sensors','system_server')
G.edge['sensors']['system_server']['write-read'] = '[open open][write read]'
G.edge['sensors']['system_server']['fill'] = 'red'
G.add_edge('sensors','system_server')
G.edge['sensors']['system_server']['write-read'] = '[open open][write read][append read]'
G.add_edge('smdexe','bluetooth')
G.edge['smdexe']['bluetooth']['write-read'] = '[open open]'
G.add_edge('smdexe','init_shell')
G.edge['smdexe']['init_shell']['write-read'] = '[open open]'
G.add_edge('smdexe','qmuxd')
G.edge['smdexe']['qmuxd']['write-read'] = '[open open]'
G.add_edge('smdexe','qti')
G.edge['smdexe']['qti']['write-read'] = '[open open]'
G.add_edge('smdexe','radio')
G.edge['smdexe']['radio']['write-read'] = '[open open]'
G.add_edge('smdexe','sensors')
G.edge['smdexe']['sensors']['write-read'] = '[open open]'
G.add_edge('smdexe','smdexe')
G.edge['smdexe']['smdexe']['write-read'] = '[open open]'
G.add_edge('smdexe','system_server')
G.edge['smdexe']['system_server']['write-read'] = '[open open]'
G.add_edge('smdexe','bluetooth')
G.edge['smdexe']['bluetooth']['write-read'] = '[open open][write read]'
G.edge['smdexe']['bluetooth']['fill'] = 'red'
G.add_edge('smdexe','bluetooth')
G.edge['smdexe']['bluetooth']['write-read'] = '[open open][write read][append read]'
G.add_edge('smdexe','init_shell')
G.edge['smdexe']['init_shell']['write-read'] = '[open open][write read]'
G.edge['smdexe']['init_shell']['fill'] = 'red'
G.add_edge('smdexe','init_shell')
G.edge['smdexe']['init_shell']['write-read'] = '[open open][write read][append read]'
G.add_edge('smdexe','qmuxd')
G.edge['smdexe']['qmuxd']['write-read'] = '[open open][write read]'
G.edge['smdexe']['qmuxd']['fill'] = 'red'
G.add_edge('smdexe','qmuxd')
G.edge['smdexe']['qmuxd']['write-read'] = '[open open][write read][append read]'
G.add_edge('smdexe','qti')
G.edge['smdexe']['qti']['write-read'] = '[open open][write read]'
G.edge['smdexe']['qti']['fill'] = 'red'
G.add_edge('smdexe','qti')
G.edge['smdexe']['qti']['write-read'] = '[open open][write read][append read]'
G.add_edge('smdexe','radio')
G.edge['smdexe']['radio']['write-read'] = '[open open][write read]'
G.edge['smdexe']['radio']['fill'] = 'red'
G.add_edge('smdexe','radio')
G.edge['smdexe']['radio']['write-read'] = '[open open][write read][append read]'
G.add_edge('smdexe','sensors')
G.edge['smdexe']['sensors']['write-read'] = '[open open][write read]'
G.edge['smdexe']['sensors']['fill'] = 'red'
G.add_edge('smdexe','sensors')
G.edge['smdexe']['sensors']['write-read'] = '[open open][write read][append read]'
G.add_edge('smdexe','smdexe')
G.edge['smdexe']['smdexe']['write-read'] = '[open open][write read]'
G.edge['smdexe']['smdexe']['fill'] = 'red'
G.add_edge('smdexe','smdexe')
G.edge['smdexe']['smdexe']['write-read'] = '[open open][write read][append read]'
G.add_edge('smdexe','system_server')
G.edge['smdexe']['system_server']['write-read'] = '[open open][write read]'
G.edge['smdexe']['system_server']['fill'] = 'red'
G.add_edge('smdexe','system_server')
G.edge['smdexe']['system_server']['write-read'] = '[open open][write read][append read]'
G.add_edge('system_server','bluetooth')
G.edge['system_server']['bluetooth']['write-read'] = '[setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('system_server','init_shell')
G.edge['system_server']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('system_server','qmuxd')
G.edge['system_server']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('system_server','qti')
G.edge['system_server']['qti']['write-read'] = '[open open]'
G.add_edge('system_server','radio')
G.edge['system_server']['radio']['write-read'] = '[open open]'
G.add_edge('system_server','sensors')
G.edge['system_server']['sensors']['write-read'] = '[add_name search][open open]'
G.add_edge('system_server','smdexe')
G.edge['system_server']['smdexe']['write-read'] = '[open open]'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('system_server','bluetooth')
G.edge['system_server']['bluetooth']['write-read'] = '[setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['system_server']['bluetooth']['fill'] = 'red'
G.add_edge('system_server','bluetooth')
G.edge['system_server']['bluetooth']['write-read'] = '[setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('system_server','init_shell')
G.edge['system_server']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['system_server']['init_shell']['fill'] = 'red'
G.add_edge('system_server','init_shell')
G.edge['system_server']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('system_server','qmuxd')
G.edge['system_server']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['system_server']['qmuxd']['fill'] = 'red'
G.add_edge('system_server','qmuxd')
G.edge['system_server']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('system_server','qti')
G.edge['system_server']['qti']['write-read'] = '[open open][write read]'
G.edge['system_server']['qti']['fill'] = 'red'
G.add_edge('system_server','qti')
G.edge['system_server']['qti']['write-read'] = '[open open][write read][append read]'
G.add_edge('system_server','radio')
G.edge['system_server']['radio']['write-read'] = '[open open][write read]'
G.edge['system_server']['radio']['fill'] = 'red'
G.add_edge('system_server','radio')
G.edge['system_server']['radio']['write-read'] = '[open open][write read][append read]'
G.add_edge('system_server','sensors')
G.edge['system_server']['sensors']['write-read'] = '[add_name search][open open][write read]'
G.edge['system_server']['sensors']['fill'] = 'red'
G.add_edge('system_server','sensors')
G.edge['system_server']['sensors']['write-read'] = '[add_name search][open open][write read][append read]'
G.add_edge('system_server','smdexe')
G.edge['system_server']['smdexe']['write-read'] = '[open open][write read]'
G.edge['system_server']['smdexe']['fill'] = 'red'
G.add_edge('system_server','smdexe')
G.edge['system_server']['smdexe']['write-read'] = '[open open][write read][append read]'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['system_server']['system_server']['fill'] = 'red'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read]'
app = Viewer(G)
app.mainloop()