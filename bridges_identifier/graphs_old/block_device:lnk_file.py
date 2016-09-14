import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('connfwexe','prepare_param')
G.edge['connfwexe']['prepare_param']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('connfwexe','ueventd')
G.edge['connfwexe']['ueventd']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('connfwexe','prepare_param')
G.edge['connfwexe']['prepare_param']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('connfwexe','prepare_param')
G.edge['connfwexe']['prepare_param']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['connfwexe']['prepare_param']['fill'] = 'red'
G.add_edge('connfwexe','prepare_param')
G.edge['connfwexe']['prepare_param']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('ime_app','prepare_param')
G.edge['ime_app']['prepare_param']['write-read'] = '[open open]'
G.add_edge('ime_app','ueventd')
G.edge['ime_app']['ueventd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('ime_app','prepare_param')
G.edge['ime_app']['prepare_param']['write-read'] = '[open open][setattr getattr]'
G.add_edge('ime_app','prepare_param')
G.edge['ime_app']['prepare_param']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['ime_app']['prepare_param']['fill'] = 'red'
G.add_edge('ime_app','prepare_param')
G.edge['ime_app']['prepare_param']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('init_shell','prepare_param')
G.edge['init_shell']['prepare_param']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('init_shell','ueventd')
G.edge['init_shell']['ueventd']['write-read'] = '[setattr getattr][open open][write read][append read][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][open open][write read][append read][write read][append read][open open]'
G.add_edge('init_shell','prepare_param')
G.edge['init_shell']['prepare_param']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('init_shell','prepare_param')
G.edge['init_shell']['prepare_param']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['init_shell']['prepare_param']['fill'] = 'red'
G.add_edge('init_shell','prepare_param')
G.edge['init_shell']['prepare_param']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('init_shell','prepare_param')
G.edge['init_shell']['prepare_param']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('ks','prepare_param')
G.edge['ks']['prepare_param']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('ks','ueventd')
G.edge['ks']['ueventd']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('ks','prepare_param')
G.edge['ks']['prepare_param']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('ks','prepare_param')
G.edge['ks']['prepare_param']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['ks']['prepare_param']['fill'] = 'red'
G.add_edge('ks','prepare_param')
G.edge['ks']['prepare_param']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('prepare_param','prepare_param')
G.edge['prepare_param']['prepare_param']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('prepare_param','ueventd')
G.edge['prepare_param']['ueventd']['write-read'] = '[open open]'
G.add_edge('prepare_param','prepare_param')
G.edge['prepare_param']['prepare_param']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('prepare_param','prepare_param')
G.edge['prepare_param']['prepare_param']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['prepare_param']['prepare_param']['fill'] = 'red'
G.add_edge('prepare_param','prepare_param')
G.edge['prepare_param']['prepare_param']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('qcks','prepare_param')
G.edge['qcks']['prepare_param']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('qcks','ueventd')
G.edge['qcks']['ueventd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('qcks','prepare_param')
G.edge['qcks']['prepare_param']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('qcks','prepare_param')
G.edge['qcks']['prepare_param']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['qcks']['prepare_param']['fill'] = 'red'
G.add_edge('qcks','prepare_param')
G.edge['qcks']['prepare_param']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('rmt_storage','prepare_param')
G.edge['rmt_storage']['prepare_param']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('rmt_storage','ueventd')
G.edge['rmt_storage']['ueventd']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('rmt_storage','prepare_param')
G.edge['rmt_storage']['prepare_param']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('rmt_storage','prepare_param')
G.edge['rmt_storage']['prepare_param']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['rmt_storage']['prepare_param']['fill'] = 'red'
G.add_edge('rmt_storage','prepare_param')
G.edge['rmt_storage']['prepare_param']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('s_system_app','prepare_param')
G.edge['s_system_app']['prepare_param']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('s_system_app','ueventd')
G.edge['s_system_app']['ueventd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('s_system_app','prepare_param')
G.edge['s_system_app']['prepare_param']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('s_system_app','prepare_param')
G.edge['s_system_app']['prepare_param']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['s_system_app']['prepare_param']['fill'] = 'red'
G.add_edge('s_system_app','prepare_param')
G.edge['s_system_app']['prepare_param']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('syscope_app','prepare_param')
G.edge['syscope_app']['prepare_param']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('syscope_app','ueventd')
G.edge['syscope_app']['ueventd']['write-read'] = '[open open]'
G.add_edge('syscope_app','prepare_param')
G.edge['syscope_app']['prepare_param']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('syscope_app','prepare_param')
G.edge['syscope_app']['prepare_param']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['syscope_app']['prepare_param']['fill'] = 'red'
G.add_edge('syscope_app','prepare_param')
G.edge['syscope_app']['prepare_param']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('system_app','prepare_param')
G.edge['system_app']['prepare_param']['write-read'] = '[open open]'
G.add_edge('system_app','ueventd')
G.edge['system_app']['ueventd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('system_app','prepare_param')
G.edge['system_app']['prepare_param']['write-read'] = '[open open][setattr getattr]'
G.add_edge('system_app','prepare_param')
G.edge['system_app']['prepare_param']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['system_app']['prepare_param']['fill'] = 'red'
G.add_edge('system_app','prepare_param')
G.edge['system_app']['prepare_param']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('ueventd','prepare_param')
G.edge['ueventd']['prepare_param']['write-read'] = '[open open]'
G.add_edge('ueventd','ueventd')
G.edge['ueventd']['ueventd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][setattr getattr][relabelto relabelfrom][relabelto relabelfrom][relabelto relabelfrom][relabelto relabelfrom][open open][setattr getattr][relabelto relabelfrom][open open][write read][append read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][relabelto relabelfrom][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][setattr getattr][relabelto relabelfrom][open open][write read][append read][open open][open open][write read][append read][write read][append read][open open]'
G.add_edge('ueventd','prepare_param')
G.edge['ueventd']['prepare_param']['write-read'] = '[open open][setattr getattr]'
G.add_edge('ueventd','prepare_param')
G.edge['ueventd']['prepare_param']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['ueventd']['prepare_param']['fill'] = 'red'
G.add_edge('ueventd','prepare_param')
G.edge['ueventd']['prepare_param']['write-read'] = '[open open][setattr getattr][write read][append read]'
app = Viewer(G)
app.mainloop()