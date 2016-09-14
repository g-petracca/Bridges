import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('cbd','domain')
G.edge['cbd']['domain']['write-read'] = '[write read][open open]'
G.add_edge('cbd','domain')
G.edge['cbd']['domain']['write-read'] = '[write read][open open][write read]'
G.edge['cbd']['domain']['fill'] = 'red'
G.add_edge('cbd','domain')
G.edge['cbd']['domain']['write-read'] = '[write read][open open][write read][append read]'
G.add_edge('domain','domain')
G.edge['domain']['domain']['write-read'] = '[write read][open open]'
G.add_edge('domain','domain')
G.edge['domain']['domain']['write-read'] = '[write read][open open][write read]'
G.edge['domain']['domain']['fill'] = 'red'
G.add_edge('domain','domain')
G.edge['domain']['domain']['write-read'] = '[write read][open open][write read][append read]'
G.add_edge('domain','domain')
G.edge['domain']['domain']['write-read'] = '[write read][open open][write read][append read][open open]'
G.add_edge('domain','domain')
G.edge['domain']['domain']['write-read'] = '[write read][open open][write read][append read][open open][write read]'
G.edge['domain']['domain']['fill'] = 'red'
G.add_edge('domain','domain')
G.edge['domain']['domain']['write-read'] = '[write read][open open][write read][append read][open open][write read][append read]'
G.add_edge('ime_app','domain')
G.edge['ime_app']['domain']['write-read'] = '[write read][write read]'
G.edge['ime_app']['domain']['fill'] = 'red'
G.add_edge('ime_app','domain')
G.edge['ime_app']['domain']['write-read'] = '[write read][write read][append read]'
G.add_edge('radio','domain')
G.edge['radio']['domain']['write-read'] = '[open open]'
G.add_edge('radio','domain')
G.edge['radio']['domain']['write-read'] = '[open open][write read]'
G.edge['radio']['domain']['fill'] = 'red'
G.add_edge('radio','domain')
G.edge['radio']['domain']['write-read'] = '[open open][write read][append read]'
G.add_edge('rmt_storage','domain')
G.edge['rmt_storage']['domain']['write-read'] = '[write read][write read]'
G.edge['rmt_storage']['domain']['fill'] = 'red'
G.add_edge('rmt_storage','domain')
G.edge['rmt_storage']['domain']['write-read'] = '[write read][write read][append read]'
G.add_edge('shell','domain')
G.edge['shell']['domain']['write-read'] = '[write read][open open]'
G.add_edge('shell','domain')
G.edge['shell']['domain']['write-read'] = '[write read][open open][write read]'
G.edge['shell']['domain']['fill'] = 'red'
G.add_edge('shell','domain')
G.edge['shell']['domain']['write-read'] = '[write read][open open][write read][append read]'
G.add_edge('shell','domain')
G.edge['shell']['domain']['write-read'] = '[write read][open open][write read][append read][write read]'
G.edge['shell']['domain']['fill'] = 'red'
G.add_edge('shell','domain')
G.edge['shell']['domain']['write-read'] = '[write read][open open][write read][append read][write read][append read]'
G.add_edge('s_system_app','domain')
G.edge['s_system_app']['domain']['write-read'] = '[write read][write read]'
G.edge['s_system_app']['domain']['fill'] = 'red'
G.add_edge('s_system_app','domain')
G.edge['s_system_app']['domain']['write-read'] = '[write read][write read][append read]'
G.add_edge('sysprof','domain')
G.edge['sysprof']['domain']['write-read'] = '[open open]'
G.add_edge('sysprof','domain')
G.edge['sysprof']['domain']['write-read'] = '[open open][write read]'
G.edge['sysprof']['domain']['fill'] = 'red'
G.add_edge('sysprof','domain')
G.edge['sysprof']['domain']['write-read'] = '[open open][write read][append read]'
G.add_edge('system_app','domain')
G.edge['system_app']['domain']['write-read'] = '[write read][write read]'
G.edge['system_app']['domain']['fill'] = 'red'
G.add_edge('system_app','domain')
G.edge['system_app']['domain']['write-read'] = '[write read][write read][append read]'
G.add_edge('system_server','domain')
G.edge['system_server']['domain']['write-read'] = '[write read][open open]'
G.add_edge('system_server','domain')
G.edge['system_server']['domain']['write-read'] = '[write read][open open][write read]'
G.edge['system_server']['domain']['fill'] = 'red'
G.add_edge('system_server','domain')
G.edge['system_server']['domain']['write-read'] = '[write read][open open][write read][append read]'
G.add_edge('system_server','domain')
G.edge['system_server']['domain']['write-read'] = '[write read][open open][write read][append read][write read]'
G.edge['system_server']['domain']['fill'] = 'red'
G.add_edge('system_server','domain')
G.edge['system_server']['domain']['write-read'] = '[write read][open open][write read][append read][write read][append read]'
G.add_edge('thermald','domain')
G.edge['thermald']['domain']['write-read'] = '[open open]'
G.add_edge('thermald','domain')
G.edge['thermald']['domain']['write-read'] = '[open open][write read]'
G.edge['thermald']['domain']['fill'] = 'red'
G.add_edge('thermald','domain')
G.edge['thermald']['domain']['write-read'] = '[open open][write read][append read]'
G.add_edge('time_daemon','domain')
G.edge['time_daemon']['domain']['write-read'] = '[write read]'
G.edge['time_daemon']['domain']['fill'] = 'red'
G.add_edge('time_daemon','domain')
G.edge['time_daemon']['domain']['write-read'] = '[write read][append read]'
G.add_edge('zygote','domain')
G.edge['zygote']['domain']['write-read'] = '[write read][write read]'
G.edge['zygote']['domain']['fill'] = 'red'
G.add_edge('zygote','domain')
G.edge['zygote']['domain']['write-read'] = '[write read][write read][append read]'
app = Viewer(G)
app.mainloop()