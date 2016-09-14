import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('healthd','healthd')
G.edge['healthd']['healthd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][write read][write read]'
G.edge['healthd']['healthd']['fill'] = 'red'
G.add_edge('healthd','init_shell')
G.edge['healthd']['init_shell']['write-read'] = '[open open][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][write read]'
G.edge['healthd']['init_shell']['fill'] = 'red'
G.add_edge('healthd','init_shell')
G.edge['healthd']['init_shell']['write-read'] = '[open open][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][write read][append read]'
G.add_edge('healthd','playready')
G.edge['healthd']['playready']['write-read'] = '[write read]'
G.edge['healthd']['playready']['fill'] = 'red'
G.add_edge('healthd','playready')
G.edge['healthd']['playready']['write-read'] = '[write read][append read]'
G.add_edge('healthd','ueventd')
G.edge['healthd']['ueventd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read]'
G.edge['healthd']['ueventd']['fill'] = 'red'
G.add_edge('healthd','ueventd')
G.edge['healthd']['ueventd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][append read]'
G.add_edge('healthd','undefined_service')
G.edge['healthd']['undefined_service']['write-read'] = '[write read]'
G.edge['healthd']['undefined_service']['fill'] = 'red'
G.add_edge('healthd','vm_bms')
G.edge['healthd']['vm_bms']['write-read'] = '[open open][write read][append read][write read]'
G.edge['healthd']['vm_bms']['fill'] = 'red'
G.add_edge('init_shell','init_shell')
G.edge['init_shell']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('init_shell','playready')
G.edge['init_shell']['playready']['write-read'] = '[open open]'
G.add_edge('init_shell','ueventd')
G.edge['init_shell']['ueventd']['write-read'] = '[setattr getattr][open open][write read][append read][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('init_shell','healthd')
G.edge['init_shell']['healthd']['write-read'] = '[write read][add_name search][remove_name search][write read][write read]'
G.edge['init_shell']['healthd']['fill'] = 'red'
G.add_edge('init_shell','init_shell')
G.edge['init_shell']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open][write read]'
G.edge['init_shell']['init_shell']['fill'] = 'red'
G.add_edge('init_shell','init_shell')
G.edge['init_shell']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('init_shell','playready')
G.edge['init_shell']['playready']['write-read'] = '[open open][write read]'
G.edge['init_shell']['playready']['fill'] = 'red'
G.add_edge('init_shell','playready')
G.edge['init_shell']['playready']['write-read'] = '[open open][write read][append read]'
G.add_edge('init_shell','ueventd')
G.edge['init_shell']['ueventd']['write-read'] = '[setattr getattr][open open][write read][append read][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['init_shell']['ueventd']['fill'] = 'red'
G.add_edge('init_shell','ueventd')
G.edge['init_shell']['ueventd']['write-read'] = '[setattr getattr][open open][write read][append read][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('init_shell','undefined_service')
G.edge['init_shell']['undefined_service']['write-read'] = '[write read]'
G.edge['init_shell']['undefined_service']['fill'] = 'red'
G.add_edge('init_shell','vm_bms')
G.edge['init_shell']['vm_bms']['write-read'] = '[open open][write read][append read][write read]'
G.edge['init_shell']['vm_bms']['fill'] = 'red'
G.add_edge('playready','init_shell')
G.edge['playready']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('playready','playready')
G.edge['playready']['playready']['write-read'] = '[open open][setattr getattr][write read][append read][write read][open open]'
G.add_edge('playready','ueventd')
G.edge['playready']['ueventd']['write-read'] = '[open open]'
G.add_edge('playready','healthd')
G.edge['playready']['healthd']['write-read'] = '[write read]'
G.edge['playready']['healthd']['fill'] = 'red'
G.add_edge('playready','init_shell')
G.edge['playready']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['playready']['init_shell']['fill'] = 'red'
G.add_edge('playready','init_shell')
G.edge['playready']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('playready','playready')
G.edge['playready']['playready']['write-read'] = '[open open][setattr getattr][write read][append read][write read][open open][write read]'
G.edge['playready']['playready']['fill'] = 'red'
G.add_edge('playready','playready')
G.edge['playready']['playready']['write-read'] = '[open open][setattr getattr][write read][append read][write read][open open][write read][append read]'
G.add_edge('playready','ueventd')
G.edge['playready']['ueventd']['write-read'] = '[open open][write read]'
G.edge['playready']['ueventd']['fill'] = 'red'
G.add_edge('playready','ueventd')
G.edge['playready']['ueventd']['write-read'] = '[open open][write read][append read]'
G.add_edge('playready','undefined_service')
G.edge['playready']['undefined_service']['write-read'] = '[write read]'
G.edge['playready']['undefined_service']['fill'] = 'red'
G.add_edge('playready','vm_bms')
G.edge['playready']['vm_bms']['write-read'] = '[write read]'
G.edge['playready']['vm_bms']['fill'] = 'red'
G.add_edge('ueventd','init_shell')
G.edge['ueventd']['init_shell']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][add_name search][remove_name search][open open]'
G.add_edge('ueventd','playready')
G.edge['ueventd']['playready']['write-read'] = '[open open]'
G.add_edge('ueventd','ueventd')
G.edge['ueventd']['ueventd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][setattr getattr][relabelto relabelfrom][relabelto relabelfrom][relabelto relabelfrom][relabelto relabelfrom][open open][setattr getattr][relabelto relabelfrom][open open][write read][append read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][relabelto relabelfrom][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][setattr getattr][relabelto relabelfrom][open open]'
G.add_edge('ueventd','healthd')
G.edge['ueventd']['healthd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][open open][write read][append read][write read]'
G.edge['ueventd']['healthd']['fill'] = 'red'
G.add_edge('ueventd','init_shell')
G.edge['ueventd']['init_shell']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][add_name search][remove_name search][open open][write read]'
G.edge['ueventd']['init_shell']['fill'] = 'red'
G.add_edge('ueventd','init_shell')
G.edge['ueventd']['init_shell']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('ueventd','playready')
G.edge['ueventd']['playready']['write-read'] = '[open open][write read]'
G.edge['ueventd']['playready']['fill'] = 'red'
G.add_edge('ueventd','playready')
G.edge['ueventd']['playready']['write-read'] = '[open open][write read][append read]'
G.add_edge('ueventd','ueventd')
G.edge['ueventd']['ueventd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][setattr getattr][relabelto relabelfrom][relabelto relabelfrom][relabelto relabelfrom][relabelto relabelfrom][open open][setattr getattr][relabelto relabelfrom][open open][write read][append read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][relabelto relabelfrom][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][setattr getattr][relabelto relabelfrom][open open][write read]'
G.edge['ueventd']['ueventd']['fill'] = 'red'
G.add_edge('ueventd','ueventd')
G.edge['ueventd']['ueventd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][setattr getattr][relabelto relabelfrom][relabelto relabelfrom][relabelto relabelfrom][relabelto relabelfrom][open open][setattr getattr][relabelto relabelfrom][open open][write read][append read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][relabelto relabelfrom][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][setattr getattr][relabelto relabelfrom][open open][write read][append read]'
G.add_edge('ueventd','undefined_service')
G.edge['ueventd']['undefined_service']['write-read'] = '[write read]'
G.edge['ueventd']['undefined_service']['fill'] = 'red'
G.add_edge('ueventd','vm_bms')
G.edge['ueventd']['vm_bms']['write-read'] = '[open open][write read][append read][write read]'
G.edge['ueventd']['vm_bms']['fill'] = 'red'
G.add_edge('vm_bms','healthd')
G.edge['vm_bms']['healthd']['write-read'] = '[open open][write read][append read][write read][write read]'
G.edge['vm_bms']['healthd']['fill'] = 'red'
G.add_edge('vm_bms','init_shell')
G.edge['vm_bms']['init_shell']['write-read'] = '[open open][setattr getattr][write read][append read][write read]'
G.edge['vm_bms']['init_shell']['fill'] = 'red'
G.add_edge('vm_bms','init_shell')
G.edge['vm_bms']['init_shell']['write-read'] = '[open open][setattr getattr][write read][append read][write read][append read]'
G.add_edge('vm_bms','playready')
G.edge['vm_bms']['playready']['write-read'] = '[write read]'
G.edge['vm_bms']['playready']['fill'] = 'red'
G.add_edge('vm_bms','playready')
G.edge['vm_bms']['playready']['write-read'] = '[write read][append read]'
G.add_edge('vm_bms','ueventd')
G.edge['vm_bms']['ueventd']['write-read'] = '[open open][write read][append read][write read]'
G.edge['vm_bms']['ueventd']['fill'] = 'red'
G.add_edge('vm_bms','ueventd')
G.edge['vm_bms']['ueventd']['write-read'] = '[open open][write read][append read][write read][append read]'
G.add_edge('vm_bms','undefined_service')
G.edge['vm_bms']['undefined_service']['write-read'] = '[write read]'
G.edge['vm_bms']['undefined_service']['fill'] = 'red'
G.add_edge('vm_bms','vm_bms')
G.edge['vm_bms']['vm_bms']['write-read'] = '[write read][open open][write read][append read][open open][write read][append read][open open][write read][open open][write read][write read]'
G.edge['vm_bms']['vm_bms']['fill'] = 'red'
app = Viewer(G)
app.mainloop()