import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('actlmand','efsks')
G.edge['actlmand']['efsks']['write-read'] = '[open open][write read][add_name search][open open]'
G.add_edge('actlmand','flash_recovery')
G.edge['actlmand']['flash_recovery']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open]'
G.add_edge('actlmand','ks')
G.edge['actlmand']['ks']['write-read'] = '[open open][write read][add_name search][open open]'
G.add_edge('actlmand','qcks')
G.edge['actlmand']['qcks']['write-read'] = '[open open][add_name search][remove_name search][open open]'
G.add_edge('actlmand','efsks')
G.edge['actlmand']['efsks']['write-read'] = '[open open][write read][add_name search][open open][write read]'
G.edge['actlmand']['efsks']['fill'] = 'red'
G.add_edge('actlmand','flash_recovery')
G.edge['actlmand']['flash_recovery']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read]'
G.edge['actlmand']['flash_recovery']['fill'] = 'red'
G.add_edge('actlmand','init_shell')
G.edge['actlmand']['init_shell']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read]'
G.edge['actlmand']['init_shell']['fill'] = 'red'
G.add_edge('actlmand','ks')
G.edge['actlmand']['ks']['write-read'] = '[open open][write read][add_name search][open open][write read]'
G.edge['actlmand']['ks']['fill'] = 'red'
G.add_edge('actlmand','qcks')
G.edge['actlmand']['qcks']['write-read'] = '[open open][add_name search][remove_name search][open open][write read]'
G.edge['actlmand']['qcks']['fill'] = 'red'
G.add_edge('actlmand','efsks')
G.edge['actlmand']['efsks']['write-read'] = '[open open][write read][add_name search][open open][write read][add_name search]'
G.add_edge('actlmand','flash_recovery')
G.edge['actlmand']['flash_recovery']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('actlmand','ks')
G.edge['actlmand']['ks']['write-read'] = '[open open][write read][add_name search][open open][write read][add_name search]'
G.add_edge('actlmand','qcks')
G.edge['actlmand']['qcks']['write-read'] = '[open open][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('efsks','efsks')
G.edge['efsks']['efsks']['write-read'] = '[open open][write read][add_name search][write read][open open]'
G.add_edge('efsks','flash_recovery')
G.edge['efsks']['flash_recovery']['write-read'] = '[open open][write read][add_name search][remove_name search][open open]'
G.add_edge('efsks','ks')
G.edge['efsks']['ks']['write-read'] = '[open open][write read][add_name search][open open]'
G.add_edge('efsks','qcks')
G.edge['efsks']['qcks']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('efsks','efsks')
G.edge['efsks']['efsks']['write-read'] = '[open open][write read][add_name search][write read][open open][write read]'
G.edge['efsks']['efsks']['fill'] = 'red'
G.add_edge('efsks','flash_recovery')
G.edge['efsks']['flash_recovery']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['efsks']['flash_recovery']['fill'] = 'red'
G.add_edge('efsks','init_shell')
G.edge['efsks']['init_shell']['write-read'] = '[open open][write read][add_name search][remove_name search][write read]'
G.edge['efsks']['init_shell']['fill'] = 'red'
G.add_edge('efsks','ks')
G.edge['efsks']['ks']['write-read'] = '[open open][write read][add_name search][open open][write read]'
G.edge['efsks']['ks']['fill'] = 'red'
G.add_edge('efsks','qcks')
G.edge['efsks']['qcks']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['efsks']['qcks']['fill'] = 'red'
G.add_edge('efsks','efsks')
G.edge['efsks']['efsks']['write-read'] = '[open open][write read][add_name search][write read][open open][write read][add_name search]'
G.add_edge('efsks','flash_recovery')
G.edge['efsks']['flash_recovery']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('efsks','ks')
G.edge['efsks']['ks']['write-read'] = '[open open][write read][add_name search][open open][write read][add_name search]'
G.add_edge('efsks','qcks')
G.edge['efsks']['qcks']['write-read'] = '[open open][write read][append read][open open][write read][add_name search]'
G.add_edge('flash_recovery','efsks')
G.edge['flash_recovery']['efsks']['write-read'] = '[open open][write read][add_name search][open open]'
G.add_edge('flash_recovery','flash_recovery')
G.edge['flash_recovery']['flash_recovery']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('flash_recovery','ks')
G.edge['flash_recovery']['ks']['write-read'] = '[open open][write read][add_name search][open open]'
G.add_edge('flash_recovery','qcks')
G.edge['flash_recovery']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open]'
G.add_edge('flash_recovery','efsks')
G.edge['flash_recovery']['efsks']['write-read'] = '[open open][write read][add_name search][open open][write read]'
G.edge['flash_recovery']['efsks']['fill'] = 'red'
G.add_edge('flash_recovery','flash_recovery')
G.edge['flash_recovery']['flash_recovery']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['flash_recovery']['flash_recovery']['fill'] = 'red'
G.add_edge('flash_recovery','init_shell')
G.edge['flash_recovery']['init_shell']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['flash_recovery']['init_shell']['fill'] = 'red'
G.add_edge('flash_recovery','ks')
G.edge['flash_recovery']['ks']['write-read'] = '[open open][write read][add_name search][open open][write read]'
G.edge['flash_recovery']['ks']['fill'] = 'red'
G.add_edge('flash_recovery','qcks')
G.edge['flash_recovery']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['flash_recovery']['qcks']['fill'] = 'red'
G.add_edge('flash_recovery','efsks')
G.edge['flash_recovery']['efsks']['write-read'] = '[open open][write read][add_name search][open open][write read][add_name search]'
G.add_edge('flash_recovery','flash_recovery')
G.edge['flash_recovery']['flash_recovery']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('flash_recovery','ks')
G.edge['flash_recovery']['ks']['write-read'] = '[open open][write read][add_name search][open open][write read][add_name search]'
G.add_edge('flash_recovery','qcks')
G.edge['flash_recovery']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('ime_app','efsks')
G.edge['ime_app']['efsks']['write-read'] = '[open open]'
G.add_edge('ime_app','flash_recovery')
G.edge['ime_app']['flash_recovery']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('ime_app','ks')
G.edge['ime_app']['ks']['write-read'] = '[open open]'
G.add_edge('ime_app','qcks')
G.edge['ime_app']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open]'
G.add_edge('ime_app','efsks')
G.edge['ime_app']['efsks']['write-read'] = '[open open][write read]'
G.edge['ime_app']['efsks']['fill'] = 'red'
G.add_edge('ime_app','flash_recovery')
G.edge['ime_app']['flash_recovery']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['ime_app']['flash_recovery']['fill'] = 'red'
G.add_edge('ime_app','init_shell')
G.edge['ime_app']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['ime_app']['init_shell']['fill'] = 'red'
G.add_edge('ime_app','ks')
G.edge['ime_app']['ks']['write-read'] = '[open open][write read]'
G.edge['ime_app']['ks']['fill'] = 'red'
G.add_edge('ime_app','qcks')
G.edge['ime_app']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['ime_app']['qcks']['fill'] = 'red'
G.add_edge('ime_app','efsks')
G.edge['ime_app']['efsks']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('ime_app','flash_recovery')
G.edge['ime_app']['flash_recovery']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('ime_app','ks')
G.edge['ime_app']['ks']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('ime_app','qcks')
G.edge['ime_app']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('init_shell','efsks')
G.edge['init_shell']['efsks']['write-read'] = '[open open][write read][add_name search][add_name search]'
G.add_edge('init_shell','flash_recovery')
G.edge['init_shell']['flash_recovery']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search]'
G.add_edge('init_shell','ks')
G.edge['init_shell']['ks']['write-read'] = '[open open][write read][add_name search][add_name search]'
G.add_edge('init_shell','qcks')
G.edge['init_shell']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][add_name search]'
G.add_edge('ks','efsks')
G.edge['ks']['efsks']['write-read'] = '[open open][write read][add_name search][open open]'
G.add_edge('ks','flash_recovery')
G.edge['ks']['flash_recovery']['write-read'] = '[open open][write read][add_name search][remove_name search][open open]'
G.add_edge('ks','ks')
G.edge['ks']['ks']['write-read'] = '[open open][write read][add_name search][open open]'
G.add_edge('ks','qcks')
G.edge['ks']['qcks']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('ks','efsks')
G.edge['ks']['efsks']['write-read'] = '[open open][write read][add_name search][open open][write read]'
G.edge['ks']['efsks']['fill'] = 'red'
G.add_edge('ks','flash_recovery')
G.edge['ks']['flash_recovery']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['ks']['flash_recovery']['fill'] = 'red'
G.add_edge('ks','init_shell')
G.edge['ks']['init_shell']['write-read'] = '[open open][write read][add_name search][remove_name search][write read]'
G.edge['ks']['init_shell']['fill'] = 'red'
G.add_edge('ks','ks')
G.edge['ks']['ks']['write-read'] = '[open open][write read][add_name search][open open][write read]'
G.edge['ks']['ks']['fill'] = 'red'
G.add_edge('ks','qcks')
G.edge['ks']['qcks']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['ks']['qcks']['fill'] = 'red'
G.add_edge('ks','efsks')
G.edge['ks']['efsks']['write-read'] = '[open open][write read][add_name search][open open][write read][add_name search]'
G.add_edge('ks','flash_recovery')
G.edge['ks']['flash_recovery']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('ks','ks')
G.edge['ks']['ks']['write-read'] = '[open open][write read][add_name search][open open][write read][add_name search]'
G.add_edge('ks','qcks')
G.edge['ks']['qcks']['write-read'] = '[open open][write read][append read][open open][write read][add_name search]'
G.add_edge('qcks','efsks')
G.edge['qcks']['efsks']['write-read'] = '[open open][write read][add_name search][open open]'
G.add_edge('qcks','flash_recovery')
G.edge['qcks']['flash_recovery']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open]'
G.add_edge('qcks','ks')
G.edge['qcks']['ks']['write-read'] = '[open open][write read][add_name search][open open]'
G.add_edge('qcks','qcks')
G.edge['qcks']['qcks']['write-read'] = '[open open][write read][append read][open open][add_name search][remove_name search][open open]'
G.add_edge('qcks','efsks')
G.edge['qcks']['efsks']['write-read'] = '[open open][write read][add_name search][open open][write read]'
G.edge['qcks']['efsks']['fill'] = 'red'
G.add_edge('qcks','flash_recovery')
G.edge['qcks']['flash_recovery']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read]'
G.edge['qcks']['flash_recovery']['fill'] = 'red'
G.add_edge('qcks','init_shell')
G.edge['qcks']['init_shell']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['qcks']['init_shell']['fill'] = 'red'
G.add_edge('qcks','ks')
G.edge['qcks']['ks']['write-read'] = '[open open][write read][add_name search][open open][write read]'
G.edge['qcks']['ks']['fill'] = 'red'
G.add_edge('qcks','qcks')
G.edge['qcks']['qcks']['write-read'] = '[open open][write read][append read][open open][add_name search][remove_name search][open open][write read]'
G.edge['qcks']['qcks']['fill'] = 'red'
G.add_edge('qcks','efsks')
G.edge['qcks']['efsks']['write-read'] = '[open open][write read][add_name search][open open][write read][add_name search]'
G.add_edge('qcks','flash_recovery')
G.edge['qcks']['flash_recovery']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('qcks','ks')
G.edge['qcks']['ks']['write-read'] = '[open open][write read][add_name search][open open][write read][add_name search]'
G.add_edge('qcks','qcks')
G.edge['qcks']['qcks']['write-read'] = '[open open][write read][append read][open open][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('s_system_app','efsks')
G.edge['s_system_app']['efsks']['write-read'] = '[open open]'
G.add_edge('s_system_app','flash_recovery')
G.edge['s_system_app']['flash_recovery']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('s_system_app','ks')
G.edge['s_system_app']['ks']['write-read'] = '[open open]'
G.add_edge('s_system_app','qcks')
G.edge['s_system_app']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open]'
G.add_edge('s_system_app','efsks')
G.edge['s_system_app']['efsks']['write-read'] = '[open open][write read]'
G.edge['s_system_app']['efsks']['fill'] = 'red'
G.add_edge('s_system_app','flash_recovery')
G.edge['s_system_app']['flash_recovery']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['s_system_app']['flash_recovery']['fill'] = 'red'
G.add_edge('s_system_app','init_shell')
G.edge['s_system_app']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['s_system_app']['init_shell']['fill'] = 'red'
G.add_edge('s_system_app','ks')
G.edge['s_system_app']['ks']['write-read'] = '[open open][write read]'
G.edge['s_system_app']['ks']['fill'] = 'red'
G.add_edge('s_system_app','qcks')
G.edge['s_system_app']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['s_system_app']['qcks']['fill'] = 'red'
G.add_edge('s_system_app','efsks')
G.edge['s_system_app']['efsks']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('s_system_app','flash_recovery')
G.edge['s_system_app']['flash_recovery']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('s_system_app','ks')
G.edge['s_system_app']['ks']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('s_system_app','qcks')
G.edge['s_system_app']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('system_app','efsks')
G.edge['system_app']['efsks']['write-read'] = '[open open]'
G.add_edge('system_app','flash_recovery')
G.edge['system_app']['flash_recovery']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('system_app','ks')
G.edge['system_app']['ks']['write-read'] = '[open open]'
G.add_edge('system_app','qcks')
G.edge['system_app']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open]'
G.add_edge('system_app','efsks')
G.edge['system_app']['efsks']['write-read'] = '[open open][write read]'
G.edge['system_app']['efsks']['fill'] = 'red'
G.add_edge('system_app','flash_recovery')
G.edge['system_app']['flash_recovery']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['system_app']['flash_recovery']['fill'] = 'red'
G.add_edge('system_app','init_shell')
G.edge['system_app']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['system_app']['init_shell']['fill'] = 'red'
G.add_edge('system_app','ks')
G.edge['system_app']['ks']['write-read'] = '[open open][write read]'
G.edge['system_app']['ks']['fill'] = 'red'
G.add_edge('system_app','qcks')
G.edge['system_app']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['system_app']['qcks']['fill'] = 'red'
G.add_edge('system_app','efsks')
G.edge['system_app']['efsks']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('system_app','flash_recovery')
G.edge['system_app']['flash_recovery']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('system_app','ks')
G.edge['system_app']['ks']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('system_app','qcks')
G.edge['system_app']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search]'
app = Viewer(G)
app.mainloop()