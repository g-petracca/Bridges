import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('at_distributor','at_distributor')
G.edge['at_distributor']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('at_distributor','bluetooth')
G.edge['at_distributor']['bluetooth']['write-read'] = '[open open]'
G.add_edge('at_distributor','cellgeofenced')
G.edge['at_distributor']['cellgeofenced']['write-read'] = '[open open]'
G.add_edge('at_distributor','charger_monitor')
G.edge['at_distributor']['charger_monitor']['write-read'] = '[open open]'
G.add_edge('at_distributor','cnd')
G.edge['at_distributor']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open]'
G.add_edge('at_distributor','connfwexe')
G.edge['at_distributor']['connfwexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('at_distributor','dpmd')
G.edge['at_distributor']['dpmd']['write-read'] = '[open open]'
G.add_edge('at_distributor','healthd')
G.edge['at_distributor']['healthd']['write-read'] = '[open open]'
G.add_edge('at_distributor','imsd')
G.edge['at_distributor']['imsd']['write-read'] = '[open open]'
G.add_edge('at_distributor','ks')
G.edge['at_distributor']['ks']['write-read'] = '[open open][write read][add_name search][open open]'
G.add_edge('at_distributor','lhd')
G.edge['at_distributor']['lhd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('at_distributor','mdm_helper')
G.edge['at_distributor']['mdm_helper']['write-read'] = '[write read][open open]'
G.add_edge('at_distributor','mediaserver')
G.edge['at_distributor']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('at_distributor','mmi')
G.edge['at_distributor']['mmi']['write-read'] = '[open open]'
G.add_edge('at_distributor','qcks')
G.edge['at_distributor']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open]'
G.add_edge('at_distributor','qlogd')
G.edge['at_distributor']['qlogd']['write-read'] = '[write read][add_name search][open open]'
G.add_edge('at_distributor','qmuxd')
G.edge['at_distributor']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('at_distributor','qmuxd')
G.edge['at_distributor']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open]'
G.add_edge('at_distributor','rfs_access')
G.edge['at_distributor']['rfs_access']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('at_distributor','rild')
G.edge['at_distributor']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][open open][setattr getattr][write read][append read][write read][append read][write read][append read][open open]'
G.add_edge('at_distributor','rmt_storage')
G.edge['at_distributor']['rmt_storage']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('at_distributor','sec-ril')
G.edge['at_distributor']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('at_distributor','sensors')
G.edge['at_distributor']['sensors']['write-read'] = '[add_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('at_distributor','system_server')
G.edge['at_distributor']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('at_distributor','vm_bms')
G.edge['at_distributor']['vm_bms']['write-read'] = '[open open]'
G.add_edge('at_distributor','vold')
G.edge['at_distributor']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('at_distributor','at_distributor')
G.edge['at_distributor']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['at_distributor']['at_distributor']['fill'] = 'red'
G.add_edge('at_distributor','at_distributor')
G.edge['at_distributor']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('at_distributor','bluetooth')
G.edge['at_distributor']['bluetooth']['write-read'] = '[open open][write read]'
G.edge['at_distributor']['bluetooth']['fill'] = 'red'
G.add_edge('at_distributor','bluetooth')
G.edge['at_distributor']['bluetooth']['write-read'] = '[open open][write read][append read]'
G.add_edge('at_distributor','cellgeofenced')
G.edge['at_distributor']['cellgeofenced']['write-read'] = '[open open][write read]'
G.edge['at_distributor']['cellgeofenced']['fill'] = 'red'
G.add_edge('at_distributor','cellgeofenced')
G.edge['at_distributor']['cellgeofenced']['write-read'] = '[open open][write read][append read]'
G.add_edge('at_distributor','charger_monitor')
G.edge['at_distributor']['charger_monitor']['write-read'] = '[open open][write read]'
G.edge['at_distributor']['charger_monitor']['fill'] = 'red'
G.add_edge('at_distributor','charger_monitor')
G.edge['at_distributor']['charger_monitor']['write-read'] = '[open open][write read][append read]'
G.add_edge('at_distributor','cnd')
G.edge['at_distributor']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][append read]'
G.add_edge('at_distributor','connfwexe')
G.edge['at_distributor']['connfwexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['at_distributor']['connfwexe']['fill'] = 'red'
G.add_edge('at_distributor','connfwexe')
G.edge['at_distributor']['connfwexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('at_distributor','daemon_app_process')
G.edge['at_distributor']['daemon_app_process']['write-read'] = '[write read]'
G.edge['at_distributor']['daemon_app_process']['fill'] = 'red'
G.add_edge('at_distributor','dpmd')
G.edge['at_distributor']['dpmd']['write-read'] = '[open open][write read]'
G.edge['at_distributor']['dpmd']['fill'] = 'red'
G.add_edge('at_distributor','dpmd')
G.edge['at_distributor']['dpmd']['write-read'] = '[open open][write read][append read]'
G.add_edge('at_distributor','healthd')
G.edge['at_distributor']['healthd']['write-read'] = '[open open][write read]'
G.edge['at_distributor']['healthd']['fill'] = 'red'
G.add_edge('at_distributor','healthd')
G.edge['at_distributor']['healthd']['write-read'] = '[open open][write read][append read]'
G.add_edge('at_distributor','imsd')
G.edge['at_distributor']['imsd']['write-read'] = '[open open][write read]'
G.edge['at_distributor']['imsd']['fill'] = 'red'
G.add_edge('at_distributor','imsd')
G.edge['at_distributor']['imsd']['write-read'] = '[open open][write read][append read]'
G.add_edge('at_distributor','ks')
G.edge['at_distributor']['ks']['write-read'] = '[open open][write read][add_name search][open open][append read]'
G.add_edge('at_distributor','lhd')
G.edge['at_distributor']['lhd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['at_distributor']['lhd']['fill'] = 'red'
G.add_edge('at_distributor','lhd')
G.edge['at_distributor']['lhd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('at_distributor','mdm_helper')
G.edge['at_distributor']['mdm_helper']['write-read'] = '[write read][open open][append read]'
G.add_edge('at_distributor','mediaserver')
G.edge['at_distributor']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['at_distributor']['mediaserver']['fill'] = 'red'
G.add_edge('at_distributor','mediaserver')
G.edge['at_distributor']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('at_distributor','mmi')
G.edge['at_distributor']['mmi']['write-read'] = '[open open][write read]'
G.edge['at_distributor']['mmi']['fill'] = 'red'
G.add_edge('at_distributor','mmi')
G.edge['at_distributor']['mmi']['write-read'] = '[open open][write read][append read]'
G.add_edge('at_distributor','qcks')
G.edge['at_distributor']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][append read]'
G.add_edge('at_distributor','qlogd')
G.edge['at_distributor']['qlogd']['write-read'] = '[write read][add_name search][open open][append read]'
G.add_edge('at_distributor','qmuxd')
G.edge['at_distributor']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][append read]'
G.add_edge('at_distributor','qmuxd')
G.edge['at_distributor']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][append read][write read]'
G.edge['at_distributor']['qmuxd']['fill'] = 'red'
G.add_edge('at_distributor','qmuxd')
G.edge['at_distributor']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][append read][write read][append read]'
G.add_edge('at_distributor','rfs_access')
G.edge['at_distributor']['rfs_access']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['at_distributor']['rfs_access']['fill'] = 'red'
G.add_edge('at_distributor','rfs_access')
G.edge['at_distributor']['rfs_access']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('at_distributor','rild')
G.edge['at_distributor']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][open open][setattr getattr][write read][append read][write read][append read][write read][append read][open open][write read]'
G.edge['at_distributor']['rild']['fill'] = 'red'
G.add_edge('at_distributor','rild')
G.edge['at_distributor']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][open open][setattr getattr][write read][append read][write read][append read][write read][append read][open open][write read][append read]'
G.add_edge('at_distributor','rmt_storage')
G.edge['at_distributor']['rmt_storage']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['at_distributor']['rmt_storage']['fill'] = 'red'
G.add_edge('at_distributor','rmt_storage')
G.edge['at_distributor']['rmt_storage']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('at_distributor','sec-ril')
G.edge['at_distributor']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['at_distributor']['sec-ril']['fill'] = 'red'
G.add_edge('at_distributor','sensors')
G.edge['at_distributor']['sensors']['write-read'] = '[add_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['at_distributor']['sensors']['fill'] = 'red'
G.add_edge('at_distributor','sensors')
G.edge['at_distributor']['sensors']['write-read'] = '[add_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('at_distributor','system_server')
G.edge['at_distributor']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['at_distributor']['system_server']['fill'] = 'red'
G.add_edge('at_distributor','system_server')
G.edge['at_distributor']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('at_distributor','tsdaemon')
G.edge['at_distributor']['tsdaemon']['write-read'] = '[write read]'
G.edge['at_distributor']['tsdaemon']['fill'] = 'red'
G.add_edge('at_distributor','vdc')
G.edge['at_distributor']['vdc']['write-read'] = '[write read]'
G.edge['at_distributor']['vdc']['fill'] = 'red'
G.add_edge('at_distributor','vm_bms')
G.edge['at_distributor']['vm_bms']['write-read'] = '[open open][write read]'
G.edge['at_distributor']['vm_bms']['fill'] = 'red'
G.add_edge('at_distributor','vm_bms')
G.edge['at_distributor']['vm_bms']['write-read'] = '[open open][write read][append read]'
G.add_edge('at_distributor','vold')
G.edge['at_distributor']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read]'
G.edge['at_distributor']['vold']['fill'] = 'red'
G.add_edge('at_distributor','vold')
G.edge['at_distributor']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('at_distributor','vpnclientd')
G.edge['at_distributor']['vpnclientd']['write-read'] = '[write read]'
G.edge['at_distributor']['vpnclientd']['fill'] = 'red'
G.add_edge('bluetooth','at_distributor')
G.edge['bluetooth']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('bluetooth','bluetooth')
G.edge['bluetooth']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('bluetooth','cellgeofenced')
G.edge['bluetooth']['cellgeofenced']['write-read'] = '[open open]'
G.add_edge('bluetooth','charger_monitor')
G.edge['bluetooth']['charger_monitor']['write-read'] = '[open open]'
G.add_edge('bluetooth','cnd')
G.edge['bluetooth']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open]'
G.add_edge('bluetooth','connfwexe')
G.edge['bluetooth']['connfwexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('bluetooth','dpmd')
G.edge['bluetooth']['dpmd']['write-read'] = '[open open]'
G.add_edge('bluetooth','healthd')
G.edge['bluetooth']['healthd']['write-read'] = '[open open]'
G.add_edge('bluetooth','imsd')
G.edge['bluetooth']['imsd']['write-read'] = '[open open]'
G.add_edge('bluetooth','ks')
G.edge['bluetooth']['ks']['write-read'] = '[open open]'
G.add_edge('bluetooth','lhd')
G.edge['bluetooth']['lhd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('bluetooth','mdm_helper')
G.edge['bluetooth']['mdm_helper']['write-read'] = '[open open]'
G.add_edge('bluetooth','mediaserver')
G.edge['bluetooth']['mediaserver']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('bluetooth','mmi')
G.edge['bluetooth']['mmi']['write-read'] = '[open open]'
G.add_edge('bluetooth','qcks')
G.edge['bluetooth']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open]'
G.add_edge('bluetooth','qlogd')
G.edge['bluetooth']['qlogd']['write-read'] = '[write read][add_name search][open open]'
G.add_edge('bluetooth','qmuxd')
G.edge['bluetooth']['qmuxd']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('bluetooth','qmuxd')
G.edge['bluetooth']['qmuxd']['write-read'] = '[open open][write read][append read][open open][open open]'
G.add_edge('bluetooth','rfs_access')
G.edge['bluetooth']['rfs_access']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('bluetooth','rild')
G.edge['bluetooth']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('bluetooth','rmt_storage')
G.edge['bluetooth']['rmt_storage']['write-read'] = '[open open]'
G.add_edge('bluetooth','sec-ril')
G.edge['bluetooth']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('bluetooth','sensors')
G.edge['bluetooth']['sensors']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('bluetooth','system_server')
G.edge['bluetooth']['system_server']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('bluetooth','vm_bms')
G.edge['bluetooth']['vm_bms']['write-read'] = '[open open]'
G.add_edge('bluetooth','vold')
G.edge['bluetooth']['vold']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('bluetooth','at_distributor')
G.edge['bluetooth']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['bluetooth']['at_distributor']['fill'] = 'red'
G.add_edge('bluetooth','at_distributor')
G.edge['bluetooth']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('bluetooth','bluetooth')
G.edge['bluetooth']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read]'
G.edge['bluetooth']['bluetooth']['fill'] = 'red'
G.add_edge('bluetooth','bluetooth')
G.edge['bluetooth']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read]'
G.add_edge('bluetooth','cellgeofenced')
G.edge['bluetooth']['cellgeofenced']['write-read'] = '[open open][write read]'
G.edge['bluetooth']['cellgeofenced']['fill'] = 'red'
G.add_edge('bluetooth','cellgeofenced')
G.edge['bluetooth']['cellgeofenced']['write-read'] = '[open open][write read][append read]'
G.add_edge('bluetooth','charger_monitor')
G.edge['bluetooth']['charger_monitor']['write-read'] = '[open open][write read]'
G.edge['bluetooth']['charger_monitor']['fill'] = 'red'
G.add_edge('bluetooth','charger_monitor')
G.edge['bluetooth']['charger_monitor']['write-read'] = '[open open][write read][append read]'
G.add_edge('bluetooth','cnd')
G.edge['bluetooth']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][append read]'
G.add_edge('bluetooth','connfwexe')
G.edge['bluetooth']['connfwexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['bluetooth']['connfwexe']['fill'] = 'red'
G.add_edge('bluetooth','connfwexe')
G.edge['bluetooth']['connfwexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('bluetooth','daemon_app_process')
G.edge['bluetooth']['daemon_app_process']['write-read'] = '[write read]'
G.edge['bluetooth']['daemon_app_process']['fill'] = 'red'
G.add_edge('bluetooth','dpmd')
G.edge['bluetooth']['dpmd']['write-read'] = '[open open][write read]'
G.edge['bluetooth']['dpmd']['fill'] = 'red'
G.add_edge('bluetooth','dpmd')
G.edge['bluetooth']['dpmd']['write-read'] = '[open open][write read][append read]'
G.add_edge('bluetooth','healthd')
G.edge['bluetooth']['healthd']['write-read'] = '[open open][write read]'
G.edge['bluetooth']['healthd']['fill'] = 'red'
G.add_edge('bluetooth','healthd')
G.edge['bluetooth']['healthd']['write-read'] = '[open open][write read][append read]'
G.add_edge('bluetooth','imsd')
G.edge['bluetooth']['imsd']['write-read'] = '[open open][write read]'
G.edge['bluetooth']['imsd']['fill'] = 'red'
G.add_edge('bluetooth','imsd')
G.edge['bluetooth']['imsd']['write-read'] = '[open open][write read][append read]'
G.add_edge('bluetooth','ks')
G.edge['bluetooth']['ks']['write-read'] = '[open open][append read]'
G.add_edge('bluetooth','lhd')
G.edge['bluetooth']['lhd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['bluetooth']['lhd']['fill'] = 'red'
G.add_edge('bluetooth','lhd')
G.edge['bluetooth']['lhd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('bluetooth','mdm_helper')
G.edge['bluetooth']['mdm_helper']['write-read'] = '[open open][append read]'
G.add_edge('bluetooth','mediaserver')
G.edge['bluetooth']['mediaserver']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['bluetooth']['mediaserver']['fill'] = 'red'
G.add_edge('bluetooth','mediaserver')
G.edge['bluetooth']['mediaserver']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('bluetooth','mmi')
G.edge['bluetooth']['mmi']['write-read'] = '[open open][write read]'
G.edge['bluetooth']['mmi']['fill'] = 'red'
G.add_edge('bluetooth','mmi')
G.edge['bluetooth']['mmi']['write-read'] = '[open open][write read][append read]'
G.add_edge('bluetooth','qcks')
G.edge['bluetooth']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][append read]'
G.add_edge('bluetooth','qlogd')
G.edge['bluetooth']['qlogd']['write-read'] = '[write read][add_name search][open open][append read]'
G.add_edge('bluetooth','qmuxd')
G.edge['bluetooth']['qmuxd']['write-read'] = '[open open][write read][append read][open open][open open][append read]'
G.add_edge('bluetooth','qmuxd')
G.edge['bluetooth']['qmuxd']['write-read'] = '[open open][write read][append read][open open][open open][append read][write read]'
G.edge['bluetooth']['qmuxd']['fill'] = 'red'
G.add_edge('bluetooth','qmuxd')
G.edge['bluetooth']['qmuxd']['write-read'] = '[open open][write read][append read][open open][open open][append read][write read][append read]'
G.add_edge('bluetooth','rfs_access')
G.edge['bluetooth']['rfs_access']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['bluetooth']['rfs_access']['fill'] = 'red'
G.add_edge('bluetooth','rfs_access')
G.edge['bluetooth']['rfs_access']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('bluetooth','rild')
G.edge['bluetooth']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read]'
G.edge['bluetooth']['rild']['fill'] = 'red'
G.add_edge('bluetooth','rild')
G.edge['bluetooth']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('bluetooth','rmt_storage')
G.edge['bluetooth']['rmt_storage']['write-read'] = '[open open][write read]'
G.edge['bluetooth']['rmt_storage']['fill'] = 'red'
G.add_edge('bluetooth','rmt_storage')
G.edge['bluetooth']['rmt_storage']['write-read'] = '[open open][write read][append read]'
G.add_edge('bluetooth','sec-ril')
G.edge['bluetooth']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['bluetooth']['sec-ril']['fill'] = 'red'
G.add_edge('bluetooth','sensors')
G.edge['bluetooth']['sensors']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['bluetooth']['sensors']['fill'] = 'red'
G.add_edge('bluetooth','sensors')
G.edge['bluetooth']['sensors']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('bluetooth','system_server')
G.edge['bluetooth']['system_server']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read]'
G.edge['bluetooth']['system_server']['fill'] = 'red'
G.add_edge('bluetooth','system_server')
G.edge['bluetooth']['system_server']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read]'
G.add_edge('bluetooth','tsdaemon')
G.edge['bluetooth']['tsdaemon']['write-read'] = '[write read]'
G.edge['bluetooth']['tsdaemon']['fill'] = 'red'
G.add_edge('bluetooth','vdc')
G.edge['bluetooth']['vdc']['write-read'] = '[write read]'
G.edge['bluetooth']['vdc']['fill'] = 'red'
G.add_edge('bluetooth','vm_bms')
G.edge['bluetooth']['vm_bms']['write-read'] = '[open open][write read]'
G.edge['bluetooth']['vm_bms']['fill'] = 'red'
G.add_edge('bluetooth','vm_bms')
G.edge['bluetooth']['vm_bms']['write-read'] = '[open open][write read][append read]'
G.add_edge('bluetooth','vold')
G.edge['bluetooth']['vold']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['bluetooth']['vold']['fill'] = 'red'
G.add_edge('bluetooth','vold')
G.edge['bluetooth']['vold']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('bluetooth','vpnclientd')
G.edge['bluetooth']['vpnclientd']['write-read'] = '[write read]'
G.edge['bluetooth']['vpnclientd']['fill'] = 'red'
G.add_edge('cellgeofenced','at_distributor')
G.edge['cellgeofenced']['at_distributor']['write-read'] = '[open open]'
G.add_edge('cellgeofenced','bluetooth')
G.edge['cellgeofenced']['bluetooth']['write-read'] = '[open open]'
G.add_edge('cellgeofenced','cellgeofenced')
G.edge['cellgeofenced']['cellgeofenced']['write-read'] = '[open open][write read][add_name search][remove_name search][open open]'
G.add_edge('cellgeofenced','charger_monitor')
G.edge['cellgeofenced']['charger_monitor']['write-read'] = '[open open]'
G.add_edge('cellgeofenced','cnd')
G.edge['cellgeofenced']['cnd']['write-read'] = '[open open]'
G.add_edge('cellgeofenced','connfwexe')
G.edge['cellgeofenced']['connfwexe']['write-read'] = '[open open]'
G.add_edge('cellgeofenced','dpmd')
G.edge['cellgeofenced']['dpmd']['write-read'] = '[open open]'
G.add_edge('cellgeofenced','healthd')
G.edge['cellgeofenced']['healthd']['write-read'] = '[open open]'
G.add_edge('cellgeofenced','imsd')
G.edge['cellgeofenced']['imsd']['write-read'] = '[open open]'
G.add_edge('cellgeofenced','ks')
G.edge['cellgeofenced']['ks']['write-read'] = '[open open]'
G.add_edge('cellgeofenced','lhd')
G.edge['cellgeofenced']['lhd']['write-read'] = '[open open]'
G.add_edge('cellgeofenced','mdm_helper')
G.edge['cellgeofenced']['mdm_helper']['write-read'] = '[open open]'
G.add_edge('cellgeofenced','mediaserver')
G.edge['cellgeofenced']['mediaserver']['write-read'] = '[open open]'
G.add_edge('cellgeofenced','mmi')
G.edge['cellgeofenced']['mmi']['write-read'] = '[open open]'
G.add_edge('cellgeofenced','qcks')
G.edge['cellgeofenced']['qcks']['write-read'] = '[open open]'
G.add_edge('cellgeofenced','qlogd')
G.edge['cellgeofenced']['qlogd']['write-read'] = '[open open]'
G.add_edge('cellgeofenced','qmuxd')
G.edge['cellgeofenced']['qmuxd']['write-read'] = '[open open]'
G.add_edge('cellgeofenced','qmuxd')
G.edge['cellgeofenced']['qmuxd']['write-read'] = '[open open][open open]'
G.add_edge('cellgeofenced','rfs_access')
G.edge['cellgeofenced']['rfs_access']['write-read'] = '[open open]'
G.add_edge('cellgeofenced','rild')
G.edge['cellgeofenced']['rild']['write-read'] = '[open open]'
G.add_edge('cellgeofenced','rmt_storage')
G.edge['cellgeofenced']['rmt_storage']['write-read'] = '[open open]'
G.add_edge('cellgeofenced','sec-ril')
G.edge['cellgeofenced']['sec-ril']['write-read'] = '[open open]'
G.add_edge('cellgeofenced','sensors')
G.edge['cellgeofenced']['sensors']['write-read'] = '[open open]'
G.add_edge('cellgeofenced','system_server')
G.edge['cellgeofenced']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('cellgeofenced','vm_bms')
G.edge['cellgeofenced']['vm_bms']['write-read'] = '[open open]'
G.add_edge('cellgeofenced','vold')
G.edge['cellgeofenced']['vold']['write-read'] = '[open open]'
G.add_edge('cellgeofenced','at_distributor')
G.edge['cellgeofenced']['at_distributor']['write-read'] = '[open open][write read]'
G.edge['cellgeofenced']['at_distributor']['fill'] = 'red'
G.add_edge('cellgeofenced','at_distributor')
G.edge['cellgeofenced']['at_distributor']['write-read'] = '[open open][write read][append read]'
G.add_edge('cellgeofenced','bluetooth')
G.edge['cellgeofenced']['bluetooth']['write-read'] = '[open open][write read]'
G.edge['cellgeofenced']['bluetooth']['fill'] = 'red'
G.add_edge('cellgeofenced','bluetooth')
G.edge['cellgeofenced']['bluetooth']['write-read'] = '[open open][write read][append read]'
G.add_edge('cellgeofenced','cellgeofenced')
G.edge['cellgeofenced']['cellgeofenced']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['cellgeofenced']['cellgeofenced']['fill'] = 'red'
G.add_edge('cellgeofenced','cellgeofenced')
G.edge['cellgeofenced']['cellgeofenced']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('cellgeofenced','charger_monitor')
G.edge['cellgeofenced']['charger_monitor']['write-read'] = '[open open][write read]'
G.edge['cellgeofenced']['charger_monitor']['fill'] = 'red'
G.add_edge('cellgeofenced','charger_monitor')
G.edge['cellgeofenced']['charger_monitor']['write-read'] = '[open open][write read][append read]'
G.add_edge('cellgeofenced','cnd')
G.edge['cellgeofenced']['cnd']['write-read'] = '[open open][append read]'
G.add_edge('cellgeofenced','connfwexe')
G.edge['cellgeofenced']['connfwexe']['write-read'] = '[open open][write read]'
G.edge['cellgeofenced']['connfwexe']['fill'] = 'red'
G.add_edge('cellgeofenced','connfwexe')
G.edge['cellgeofenced']['connfwexe']['write-read'] = '[open open][write read][append read]'
G.add_edge('cellgeofenced','daemon_app_process')
G.edge['cellgeofenced']['daemon_app_process']['write-read'] = '[write read]'
G.edge['cellgeofenced']['daemon_app_process']['fill'] = 'red'
G.add_edge('cellgeofenced','dpmd')
G.edge['cellgeofenced']['dpmd']['write-read'] = '[open open][write read]'
G.edge['cellgeofenced']['dpmd']['fill'] = 'red'
G.add_edge('cellgeofenced','dpmd')
G.edge['cellgeofenced']['dpmd']['write-read'] = '[open open][write read][append read]'
G.add_edge('cellgeofenced','healthd')
G.edge['cellgeofenced']['healthd']['write-read'] = '[open open][write read]'
G.edge['cellgeofenced']['healthd']['fill'] = 'red'
G.add_edge('cellgeofenced','healthd')
G.edge['cellgeofenced']['healthd']['write-read'] = '[open open][write read][append read]'
G.add_edge('cellgeofenced','imsd')
G.edge['cellgeofenced']['imsd']['write-read'] = '[open open][write read]'
G.edge['cellgeofenced']['imsd']['fill'] = 'red'
G.add_edge('cellgeofenced','imsd')
G.edge['cellgeofenced']['imsd']['write-read'] = '[open open][write read][append read]'
G.add_edge('cellgeofenced','ks')
G.edge['cellgeofenced']['ks']['write-read'] = '[open open][append read]'
G.add_edge('cellgeofenced','lhd')
G.edge['cellgeofenced']['lhd']['write-read'] = '[open open][write read]'
G.edge['cellgeofenced']['lhd']['fill'] = 'red'
G.add_edge('cellgeofenced','lhd')
G.edge['cellgeofenced']['lhd']['write-read'] = '[open open][write read][append read]'
G.add_edge('cellgeofenced','mdm_helper')
G.edge['cellgeofenced']['mdm_helper']['write-read'] = '[open open][append read]'
G.add_edge('cellgeofenced','mediaserver')
G.edge['cellgeofenced']['mediaserver']['write-read'] = '[open open][write read]'
G.edge['cellgeofenced']['mediaserver']['fill'] = 'red'
G.add_edge('cellgeofenced','mediaserver')
G.edge['cellgeofenced']['mediaserver']['write-read'] = '[open open][write read][append read]'
G.add_edge('cellgeofenced','mmi')
G.edge['cellgeofenced']['mmi']['write-read'] = '[open open][write read]'
G.edge['cellgeofenced']['mmi']['fill'] = 'red'
G.add_edge('cellgeofenced','mmi')
G.edge['cellgeofenced']['mmi']['write-read'] = '[open open][write read][append read]'
G.add_edge('cellgeofenced','qcks')
G.edge['cellgeofenced']['qcks']['write-read'] = '[open open][append read]'
G.add_edge('cellgeofenced','qlogd')
G.edge['cellgeofenced']['qlogd']['write-read'] = '[open open][append read]'
G.add_edge('cellgeofenced','qmuxd')
G.edge['cellgeofenced']['qmuxd']['write-read'] = '[open open][open open][append read]'
G.add_edge('cellgeofenced','qmuxd')
G.edge['cellgeofenced']['qmuxd']['write-read'] = '[open open][open open][append read][write read]'
G.edge['cellgeofenced']['qmuxd']['fill'] = 'red'
G.add_edge('cellgeofenced','qmuxd')
G.edge['cellgeofenced']['qmuxd']['write-read'] = '[open open][open open][append read][write read][append read]'
G.add_edge('cellgeofenced','rfs_access')
G.edge['cellgeofenced']['rfs_access']['write-read'] = '[open open][write read]'
G.edge['cellgeofenced']['rfs_access']['fill'] = 'red'
G.add_edge('cellgeofenced','rfs_access')
G.edge['cellgeofenced']['rfs_access']['write-read'] = '[open open][write read][append read]'
G.add_edge('cellgeofenced','rild')
G.edge['cellgeofenced']['rild']['write-read'] = '[open open][write read]'
G.edge['cellgeofenced']['rild']['fill'] = 'red'
G.add_edge('cellgeofenced','rild')
G.edge['cellgeofenced']['rild']['write-read'] = '[open open][write read][append read]'
G.add_edge('cellgeofenced','rmt_storage')
G.edge['cellgeofenced']['rmt_storage']['write-read'] = '[open open][write read]'
G.edge['cellgeofenced']['rmt_storage']['fill'] = 'red'
G.add_edge('cellgeofenced','rmt_storage')
G.edge['cellgeofenced']['rmt_storage']['write-read'] = '[open open][write read][append read]'
G.add_edge('cellgeofenced','sec-ril')
G.edge['cellgeofenced']['sec-ril']['write-read'] = '[open open][write read]'
G.edge['cellgeofenced']['sec-ril']['fill'] = 'red'
G.add_edge('cellgeofenced','sensors')
G.edge['cellgeofenced']['sensors']['write-read'] = '[open open][write read]'
G.edge['cellgeofenced']['sensors']['fill'] = 'red'
G.add_edge('cellgeofenced','sensors')
G.edge['cellgeofenced']['sensors']['write-read'] = '[open open][write read][append read]'
G.add_edge('cellgeofenced','system_server')
G.edge['cellgeofenced']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['cellgeofenced']['system_server']['fill'] = 'red'
G.add_edge('cellgeofenced','system_server')
G.edge['cellgeofenced']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('cellgeofenced','tsdaemon')
G.edge['cellgeofenced']['tsdaemon']['write-read'] = '[write read]'
G.edge['cellgeofenced']['tsdaemon']['fill'] = 'red'
G.add_edge('cellgeofenced','vdc')
G.edge['cellgeofenced']['vdc']['write-read'] = '[write read]'
G.edge['cellgeofenced']['vdc']['fill'] = 'red'
G.add_edge('cellgeofenced','vm_bms')
G.edge['cellgeofenced']['vm_bms']['write-read'] = '[open open][write read]'
G.edge['cellgeofenced']['vm_bms']['fill'] = 'red'
G.add_edge('cellgeofenced','vm_bms')
G.edge['cellgeofenced']['vm_bms']['write-read'] = '[open open][write read][append read]'
G.add_edge('cellgeofenced','vold')
G.edge['cellgeofenced']['vold']['write-read'] = '[open open][write read]'
G.edge['cellgeofenced']['vold']['fill'] = 'red'
G.add_edge('cellgeofenced','vold')
G.edge['cellgeofenced']['vold']['write-read'] = '[open open][write read][append read]'
G.add_edge('cellgeofenced','vpnclientd')
G.edge['cellgeofenced']['vpnclientd']['write-read'] = '[write read]'
G.edge['cellgeofenced']['vpnclientd']['fill'] = 'red'
G.add_edge('charger_monitor','at_distributor')
G.edge['charger_monitor']['at_distributor']['write-read'] = '[open open]'
G.add_edge('charger_monitor','bluetooth')
G.edge['charger_monitor']['bluetooth']['write-read'] = '[open open]'
G.add_edge('charger_monitor','cellgeofenced')
G.edge['charger_monitor']['cellgeofenced']['write-read'] = '[open open]'
G.add_edge('charger_monitor','charger_monitor')
G.edge['charger_monitor']['charger_monitor']['write-read'] = '[open open]'
G.add_edge('charger_monitor','cnd')
G.edge['charger_monitor']['cnd']['write-read'] = '[open open]'
G.add_edge('charger_monitor','connfwexe')
G.edge['charger_monitor']['connfwexe']['write-read'] = '[open open]'
G.add_edge('charger_monitor','dpmd')
G.edge['charger_monitor']['dpmd']['write-read'] = '[open open]'
G.add_edge('charger_monitor','healthd')
G.edge['charger_monitor']['healthd']['write-read'] = '[write read][append read][open open]'
G.add_edge('charger_monitor','imsd')
G.edge['charger_monitor']['imsd']['write-read'] = '[open open]'
G.add_edge('charger_monitor','ks')
G.edge['charger_monitor']['ks']['write-read'] = '[open open]'
G.add_edge('charger_monitor','lhd')
G.edge['charger_monitor']['lhd']['write-read'] = '[open open]'
G.add_edge('charger_monitor','mdm_helper')
G.edge['charger_monitor']['mdm_helper']['write-read'] = '[open open]'
G.add_edge('charger_monitor','mediaserver')
G.edge['charger_monitor']['mediaserver']['write-read'] = '[open open]'
G.add_edge('charger_monitor','mmi')
G.edge['charger_monitor']['mmi']['write-read'] = '[open open]'
G.add_edge('charger_monitor','qcks')
G.edge['charger_monitor']['qcks']['write-read'] = '[open open]'
G.add_edge('charger_monitor','qlogd')
G.edge['charger_monitor']['qlogd']['write-read'] = '[open open]'
G.add_edge('charger_monitor','qmuxd')
G.edge['charger_monitor']['qmuxd']['write-read'] = '[open open]'
G.add_edge('charger_monitor','qmuxd')
G.edge['charger_monitor']['qmuxd']['write-read'] = '[open open][open open]'
G.add_edge('charger_monitor','rfs_access')
G.edge['charger_monitor']['rfs_access']['write-read'] = '[open open]'
G.add_edge('charger_monitor','rild')
G.edge['charger_monitor']['rild']['write-read'] = '[write read][append read][open open]'
G.add_edge('charger_monitor','rmt_storage')
G.edge['charger_monitor']['rmt_storage']['write-read'] = '[open open]'
G.add_edge('charger_monitor','sec-ril')
G.edge['charger_monitor']['sec-ril']['write-read'] = '[open open]'
G.add_edge('charger_monitor','sensors')
G.edge['charger_monitor']['sensors']['write-read'] = '[open open]'
G.add_edge('charger_monitor','system_server')
G.edge['charger_monitor']['system_server']['write-read'] = '[write read][append read][open open]'
G.add_edge('charger_monitor','vm_bms')
G.edge['charger_monitor']['vm_bms']['write-read'] = '[open open]'
G.add_edge('charger_monitor','vold')
G.edge['charger_monitor']['vold']['write-read'] = '[write read][append read][open open]'
G.add_edge('charger_monitor','at_distributor')
G.edge['charger_monitor']['at_distributor']['write-read'] = '[open open][write read]'
G.edge['charger_monitor']['at_distributor']['fill'] = 'red'
G.add_edge('charger_monitor','at_distributor')
G.edge['charger_monitor']['at_distributor']['write-read'] = '[open open][write read][append read]'
G.add_edge('charger_monitor','bluetooth')
G.edge['charger_monitor']['bluetooth']['write-read'] = '[open open][write read]'
G.edge['charger_monitor']['bluetooth']['fill'] = 'red'
G.add_edge('charger_monitor','bluetooth')
G.edge['charger_monitor']['bluetooth']['write-read'] = '[open open][write read][append read]'
G.add_edge('charger_monitor','cellgeofenced')
G.edge['charger_monitor']['cellgeofenced']['write-read'] = '[open open][write read]'
G.edge['charger_monitor']['cellgeofenced']['fill'] = 'red'
G.add_edge('charger_monitor','cellgeofenced')
G.edge['charger_monitor']['cellgeofenced']['write-read'] = '[open open][write read][append read]'
G.add_edge('charger_monitor','charger_monitor')
G.edge['charger_monitor']['charger_monitor']['write-read'] = '[open open][write read]'
G.edge['charger_monitor']['charger_monitor']['fill'] = 'red'
G.add_edge('charger_monitor','charger_monitor')
G.edge['charger_monitor']['charger_monitor']['write-read'] = '[open open][write read][append read]'
G.add_edge('charger_monitor','cnd')
G.edge['charger_monitor']['cnd']['write-read'] = '[open open][append read]'
G.add_edge('charger_monitor','connfwexe')
G.edge['charger_monitor']['connfwexe']['write-read'] = '[open open][write read]'
G.edge['charger_monitor']['connfwexe']['fill'] = 'red'
G.add_edge('charger_monitor','connfwexe')
G.edge['charger_monitor']['connfwexe']['write-read'] = '[open open][write read][append read]'
G.add_edge('charger_monitor','daemon_app_process')
G.edge['charger_monitor']['daemon_app_process']['write-read'] = '[write read]'
G.edge['charger_monitor']['daemon_app_process']['fill'] = 'red'
G.add_edge('charger_monitor','dpmd')
G.edge['charger_monitor']['dpmd']['write-read'] = '[open open][write read]'
G.edge['charger_monitor']['dpmd']['fill'] = 'red'
G.add_edge('charger_monitor','dpmd')
G.edge['charger_monitor']['dpmd']['write-read'] = '[open open][write read][append read]'
G.add_edge('charger_monitor','healthd')
G.edge['charger_monitor']['healthd']['write-read'] = '[write read][append read][open open][write read]'
G.edge['charger_monitor']['healthd']['fill'] = 'red'
G.add_edge('charger_monitor','healthd')
G.edge['charger_monitor']['healthd']['write-read'] = '[write read][append read][open open][write read][append read]'
G.add_edge('charger_monitor','imsd')
G.edge['charger_monitor']['imsd']['write-read'] = '[open open][write read]'
G.edge['charger_monitor']['imsd']['fill'] = 'red'
G.add_edge('charger_monitor','imsd')
G.edge['charger_monitor']['imsd']['write-read'] = '[open open][write read][append read]'
G.add_edge('charger_monitor','ks')
G.edge['charger_monitor']['ks']['write-read'] = '[open open][append read]'
G.add_edge('charger_monitor','lhd')
G.edge['charger_monitor']['lhd']['write-read'] = '[open open][write read]'
G.edge['charger_monitor']['lhd']['fill'] = 'red'
G.add_edge('charger_monitor','lhd')
G.edge['charger_monitor']['lhd']['write-read'] = '[open open][write read][append read]'
G.add_edge('charger_monitor','mdm_helper')
G.edge['charger_monitor']['mdm_helper']['write-read'] = '[open open][append read]'
G.add_edge('charger_monitor','mediaserver')
G.edge['charger_monitor']['mediaserver']['write-read'] = '[open open][write read]'
G.edge['charger_monitor']['mediaserver']['fill'] = 'red'
G.add_edge('charger_monitor','mediaserver')
G.edge['charger_monitor']['mediaserver']['write-read'] = '[open open][write read][append read]'
G.add_edge('charger_monitor','mmi')
G.edge['charger_monitor']['mmi']['write-read'] = '[open open][write read]'
G.edge['charger_monitor']['mmi']['fill'] = 'red'
G.add_edge('charger_monitor','mmi')
G.edge['charger_monitor']['mmi']['write-read'] = '[open open][write read][append read]'
G.add_edge('charger_monitor','qcks')
G.edge['charger_monitor']['qcks']['write-read'] = '[open open][append read]'
G.add_edge('charger_monitor','qlogd')
G.edge['charger_monitor']['qlogd']['write-read'] = '[open open][append read]'
G.add_edge('charger_monitor','qmuxd')
G.edge['charger_monitor']['qmuxd']['write-read'] = '[open open][open open][append read]'
G.add_edge('charger_monitor','qmuxd')
G.edge['charger_monitor']['qmuxd']['write-read'] = '[open open][open open][append read][write read]'
G.edge['charger_monitor']['qmuxd']['fill'] = 'red'
G.add_edge('charger_monitor','qmuxd')
G.edge['charger_monitor']['qmuxd']['write-read'] = '[open open][open open][append read][write read][append read]'
G.add_edge('charger_monitor','rfs_access')
G.edge['charger_monitor']['rfs_access']['write-read'] = '[open open][write read]'
G.edge['charger_monitor']['rfs_access']['fill'] = 'red'
G.add_edge('charger_monitor','rfs_access')
G.edge['charger_monitor']['rfs_access']['write-read'] = '[open open][write read][append read]'
G.add_edge('charger_monitor','rild')
G.edge['charger_monitor']['rild']['write-read'] = '[write read][append read][open open][write read]'
G.edge['charger_monitor']['rild']['fill'] = 'red'
G.add_edge('charger_monitor','rild')
G.edge['charger_monitor']['rild']['write-read'] = '[write read][append read][open open][write read][append read]'
G.add_edge('charger_monitor','rmt_storage')
G.edge['charger_monitor']['rmt_storage']['write-read'] = '[open open][write read]'
G.edge['charger_monitor']['rmt_storage']['fill'] = 'red'
G.add_edge('charger_monitor','rmt_storage')
G.edge['charger_monitor']['rmt_storage']['write-read'] = '[open open][write read][append read]'
G.add_edge('charger_monitor','sec-ril')
G.edge['charger_monitor']['sec-ril']['write-read'] = '[open open][write read]'
G.edge['charger_monitor']['sec-ril']['fill'] = 'red'
G.add_edge('charger_monitor','sensors')
G.edge['charger_monitor']['sensors']['write-read'] = '[open open][write read]'
G.edge['charger_monitor']['sensors']['fill'] = 'red'
G.add_edge('charger_monitor','sensors')
G.edge['charger_monitor']['sensors']['write-read'] = '[open open][write read][append read]'
G.add_edge('charger_monitor','system_server')
G.edge['charger_monitor']['system_server']['write-read'] = '[write read][append read][open open][write read]'
G.edge['charger_monitor']['system_server']['fill'] = 'red'
G.add_edge('charger_monitor','system_server')
G.edge['charger_monitor']['system_server']['write-read'] = '[write read][append read][open open][write read][append read]'
G.add_edge('charger_monitor','tsdaemon')
G.edge['charger_monitor']['tsdaemon']['write-read'] = '[write read]'
G.edge['charger_monitor']['tsdaemon']['fill'] = 'red'
G.add_edge('charger_monitor','vdc')
G.edge['charger_monitor']['vdc']['write-read'] = '[write read]'
G.edge['charger_monitor']['vdc']['fill'] = 'red'
G.add_edge('charger_monitor','vm_bms')
G.edge['charger_monitor']['vm_bms']['write-read'] = '[open open][write read]'
G.edge['charger_monitor']['vm_bms']['fill'] = 'red'
G.add_edge('charger_monitor','vm_bms')
G.edge['charger_monitor']['vm_bms']['write-read'] = '[open open][write read][append read]'
G.add_edge('charger_monitor','vold')
G.edge['charger_monitor']['vold']['write-read'] = '[write read][append read][open open][write read]'
G.edge['charger_monitor']['vold']['fill'] = 'red'
G.add_edge('charger_monitor','vold')
G.edge['charger_monitor']['vold']['write-read'] = '[write read][append read][open open][write read][append read]'
G.add_edge('charger_monitor','vpnclientd')
G.edge['charger_monitor']['vpnclientd']['write-read'] = '[write read]'
G.edge['charger_monitor']['vpnclientd']['fill'] = 'red'
G.add_edge('connfwexe','at_distributor')
G.edge['connfwexe']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('connfwexe','bluetooth')
G.edge['connfwexe']['bluetooth']['write-read'] = '[open open]'
G.add_edge('connfwexe','cellgeofenced')
G.edge['connfwexe']['cellgeofenced']['write-read'] = '[open open]'
G.add_edge('connfwexe','charger_monitor')
G.edge['connfwexe']['charger_monitor']['write-read'] = '[open open]'
G.add_edge('connfwexe','cnd')
G.edge['connfwexe']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open]'
G.add_edge('connfwexe','connfwexe')
G.edge['connfwexe']['connfwexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('connfwexe','dpmd')
G.edge['connfwexe']['dpmd']['write-read'] = '[open open]'
G.add_edge('connfwexe','healthd')
G.edge['connfwexe']['healthd']['write-read'] = '[open open]'
G.add_edge('connfwexe','imsd')
G.edge['connfwexe']['imsd']['write-read'] = '[open open]'
G.add_edge('connfwexe','ks')
G.edge['connfwexe']['ks']['write-read'] = '[open open][write read][add_name search][open open]'
G.add_edge('connfwexe','lhd')
G.edge['connfwexe']['lhd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('connfwexe','mdm_helper')
G.edge['connfwexe']['mdm_helper']['write-read'] = '[write read][open open]'
G.add_edge('connfwexe','mediaserver')
G.edge['connfwexe']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('connfwexe','mmi')
G.edge['connfwexe']['mmi']['write-read'] = '[open open]'
G.add_edge('connfwexe','qcks')
G.edge['connfwexe']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open]'
G.add_edge('connfwexe','qlogd')
G.edge['connfwexe']['qlogd']['write-read'] = '[write read][add_name search][open open]'
G.add_edge('connfwexe','qmuxd')
G.edge['connfwexe']['qmuxd']['write-read'] = '[open open]'
G.add_edge('connfwexe','qmuxd')
G.edge['connfwexe']['qmuxd']['write-read'] = '[open open][open open]'
G.add_edge('connfwexe','rfs_access')
G.edge['connfwexe']['rfs_access']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('connfwexe','rild')
G.edge['connfwexe']['rild']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('connfwexe','rmt_storage')
G.edge['connfwexe']['rmt_storage']['write-read'] = '[open open]'
G.add_edge('connfwexe','sec-ril')
G.edge['connfwexe']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('connfwexe','sensors')
G.edge['connfwexe']['sensors']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('connfwexe','system_server')
G.edge['connfwexe']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('connfwexe','vm_bms')
G.edge['connfwexe']['vm_bms']['write-read'] = '[open open]'
G.add_edge('connfwexe','vold')
G.edge['connfwexe']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('connfwexe','at_distributor')
G.edge['connfwexe']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['connfwexe']['at_distributor']['fill'] = 'red'
G.add_edge('connfwexe','at_distributor')
G.edge['connfwexe']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('connfwexe','bluetooth')
G.edge['connfwexe']['bluetooth']['write-read'] = '[open open][write read]'
G.edge['connfwexe']['bluetooth']['fill'] = 'red'
G.add_edge('connfwexe','bluetooth')
G.edge['connfwexe']['bluetooth']['write-read'] = '[open open][write read][append read]'
G.add_edge('connfwexe','cellgeofenced')
G.edge['connfwexe']['cellgeofenced']['write-read'] = '[open open][write read]'
G.edge['connfwexe']['cellgeofenced']['fill'] = 'red'
G.add_edge('connfwexe','cellgeofenced')
G.edge['connfwexe']['cellgeofenced']['write-read'] = '[open open][write read][append read]'
G.add_edge('connfwexe','charger_monitor')
G.edge['connfwexe']['charger_monitor']['write-read'] = '[open open][write read]'
G.edge['connfwexe']['charger_monitor']['fill'] = 'red'
G.add_edge('connfwexe','charger_monitor')
G.edge['connfwexe']['charger_monitor']['write-read'] = '[open open][write read][append read]'
G.add_edge('connfwexe','cnd')
G.edge['connfwexe']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][append read]'
G.add_edge('connfwexe','connfwexe')
G.edge['connfwexe']['connfwexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['connfwexe']['connfwexe']['fill'] = 'red'
G.add_edge('connfwexe','connfwexe')
G.edge['connfwexe']['connfwexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('connfwexe','daemon_app_process')
G.edge['connfwexe']['daemon_app_process']['write-read'] = '[write read]'
G.edge['connfwexe']['daemon_app_process']['fill'] = 'red'
G.add_edge('connfwexe','dpmd')
G.edge['connfwexe']['dpmd']['write-read'] = '[open open][write read]'
G.edge['connfwexe']['dpmd']['fill'] = 'red'
G.add_edge('connfwexe','dpmd')
G.edge['connfwexe']['dpmd']['write-read'] = '[open open][write read][append read]'
G.add_edge('connfwexe','healthd')
G.edge['connfwexe']['healthd']['write-read'] = '[open open][write read]'
G.edge['connfwexe']['healthd']['fill'] = 'red'
G.add_edge('connfwexe','healthd')
G.edge['connfwexe']['healthd']['write-read'] = '[open open][write read][append read]'
G.add_edge('connfwexe','imsd')
G.edge['connfwexe']['imsd']['write-read'] = '[open open][write read]'
G.edge['connfwexe']['imsd']['fill'] = 'red'
G.add_edge('connfwexe','imsd')
G.edge['connfwexe']['imsd']['write-read'] = '[open open][write read][append read]'
G.add_edge('connfwexe','ks')
G.edge['connfwexe']['ks']['write-read'] = '[open open][write read][add_name search][open open][append read]'
G.add_edge('connfwexe','lhd')
G.edge['connfwexe']['lhd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['connfwexe']['lhd']['fill'] = 'red'
G.add_edge('connfwexe','lhd')
G.edge['connfwexe']['lhd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('connfwexe','mdm_helper')
G.edge['connfwexe']['mdm_helper']['write-read'] = '[write read][open open][append read]'
G.add_edge('connfwexe','mediaserver')
G.edge['connfwexe']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['connfwexe']['mediaserver']['fill'] = 'red'
G.add_edge('connfwexe','mediaserver')
G.edge['connfwexe']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('connfwexe','mmi')
G.edge['connfwexe']['mmi']['write-read'] = '[open open][write read]'
G.edge['connfwexe']['mmi']['fill'] = 'red'
G.add_edge('connfwexe','mmi')
G.edge['connfwexe']['mmi']['write-read'] = '[open open][write read][append read]'
G.add_edge('connfwexe','qcks')
G.edge['connfwexe']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][append read]'
G.add_edge('connfwexe','qlogd')
G.edge['connfwexe']['qlogd']['write-read'] = '[write read][add_name search][open open][append read]'
G.add_edge('connfwexe','qmuxd')
G.edge['connfwexe']['qmuxd']['write-read'] = '[open open][open open][append read]'
G.add_edge('connfwexe','qmuxd')
G.edge['connfwexe']['qmuxd']['write-read'] = '[open open][open open][append read][write read]'
G.edge['connfwexe']['qmuxd']['fill'] = 'red'
G.add_edge('connfwexe','qmuxd')
G.edge['connfwexe']['qmuxd']['write-read'] = '[open open][open open][append read][write read][append read]'
G.add_edge('connfwexe','rfs_access')
G.edge['connfwexe']['rfs_access']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['connfwexe']['rfs_access']['fill'] = 'red'
G.add_edge('connfwexe','rfs_access')
G.edge['connfwexe']['rfs_access']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('connfwexe','rild')
G.edge['connfwexe']['rild']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read]'
G.edge['connfwexe']['rild']['fill'] = 'red'
G.add_edge('connfwexe','rild')
G.edge['connfwexe']['rild']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('connfwexe','rmt_storage')
G.edge['connfwexe']['rmt_storage']['write-read'] = '[open open][write read]'
G.edge['connfwexe']['rmt_storage']['fill'] = 'red'
G.add_edge('connfwexe','rmt_storage')
G.edge['connfwexe']['rmt_storage']['write-read'] = '[open open][write read][append read]'
G.add_edge('connfwexe','sec-ril')
G.edge['connfwexe']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['connfwexe']['sec-ril']['fill'] = 'red'
G.add_edge('connfwexe','sensors')
G.edge['connfwexe']['sensors']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['connfwexe']['sensors']['fill'] = 'red'
G.add_edge('connfwexe','sensors')
G.edge['connfwexe']['sensors']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('connfwexe','system_server')
G.edge['connfwexe']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['connfwexe']['system_server']['fill'] = 'red'
G.add_edge('connfwexe','system_server')
G.edge['connfwexe']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('connfwexe','tsdaemon')
G.edge['connfwexe']['tsdaemon']['write-read'] = '[write read]'
G.edge['connfwexe']['tsdaemon']['fill'] = 'red'
G.add_edge('connfwexe','vdc')
G.edge['connfwexe']['vdc']['write-read'] = '[write read]'
G.edge['connfwexe']['vdc']['fill'] = 'red'
G.add_edge('connfwexe','vm_bms')
G.edge['connfwexe']['vm_bms']['write-read'] = '[open open][write read]'
G.edge['connfwexe']['vm_bms']['fill'] = 'red'
G.add_edge('connfwexe','vm_bms')
G.edge['connfwexe']['vm_bms']['write-read'] = '[open open][write read][append read]'
G.add_edge('connfwexe','vold')
G.edge['connfwexe']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read]'
G.edge['connfwexe']['vold']['fill'] = 'red'
G.add_edge('connfwexe','vold')
G.edge['connfwexe']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('connfwexe','vpnclientd')
G.edge['connfwexe']['vpnclientd']['write-read'] = '[write read]'
G.edge['connfwexe']['vpnclientd']['fill'] = 'red'
G.add_edge('dpmd','at_distributor')
G.edge['dpmd']['at_distributor']['write-read'] = '[open open]'
G.add_edge('dpmd','bluetooth')
G.edge['dpmd']['bluetooth']['write-read'] = '[open open]'
G.add_edge('dpmd','cellgeofenced')
G.edge['dpmd']['cellgeofenced']['write-read'] = '[open open]'
G.add_edge('dpmd','charger_monitor')
G.edge['dpmd']['charger_monitor']['write-read'] = '[open open]'
G.add_edge('dpmd','cnd')
G.edge['dpmd']['cnd']['write-read'] = '[open open]'
G.add_edge('dpmd','connfwexe')
G.edge['dpmd']['connfwexe']['write-read'] = '[open open]'
G.add_edge('dpmd','dpmd')
G.edge['dpmd']['dpmd']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('dpmd','healthd')
G.edge['dpmd']['healthd']['write-read'] = '[open open]'
G.add_edge('dpmd','imsd')
G.edge['dpmd']['imsd']['write-read'] = '[open open]'
G.add_edge('dpmd','ks')
G.edge['dpmd']['ks']['write-read'] = '[open open]'
G.add_edge('dpmd','lhd')
G.edge['dpmd']['lhd']['write-read'] = '[open open]'
G.add_edge('dpmd','mdm_helper')
G.edge['dpmd']['mdm_helper']['write-read'] = '[open open]'
G.add_edge('dpmd','mediaserver')
G.edge['dpmd']['mediaserver']['write-read'] = '[open open]'
G.add_edge('dpmd','mmi')
G.edge['dpmd']['mmi']['write-read'] = '[open open]'
G.add_edge('dpmd','qcks')
G.edge['dpmd']['qcks']['write-read'] = '[open open]'
G.add_edge('dpmd','qlogd')
G.edge['dpmd']['qlogd']['write-read'] = '[open open]'
G.add_edge('dpmd','qmuxd')
G.edge['dpmd']['qmuxd']['write-read'] = '[open open]'
G.add_edge('dpmd','qmuxd')
G.edge['dpmd']['qmuxd']['write-read'] = '[open open][open open]'
G.add_edge('dpmd','rfs_access')
G.edge['dpmd']['rfs_access']['write-read'] = '[open open]'
G.add_edge('dpmd','rild')
G.edge['dpmd']['rild']['write-read'] = '[open open]'
G.add_edge('dpmd','rmt_storage')
G.edge['dpmd']['rmt_storage']['write-read'] = '[open open]'
G.add_edge('dpmd','sec-ril')
G.edge['dpmd']['sec-ril']['write-read'] = '[open open]'
G.add_edge('dpmd','sensors')
G.edge['dpmd']['sensors']['write-read'] = '[open open]'
G.add_edge('dpmd','system_server')
G.edge['dpmd']['system_server']['write-read'] = '[open open]'
G.add_edge('dpmd','vm_bms')
G.edge['dpmd']['vm_bms']['write-read'] = '[open open]'
G.add_edge('dpmd','vold')
G.edge['dpmd']['vold']['write-read'] = '[open open]'
G.add_edge('dpmd','at_distributor')
G.edge['dpmd']['at_distributor']['write-read'] = '[open open][write read]'
G.edge['dpmd']['at_distributor']['fill'] = 'red'
G.add_edge('dpmd','at_distributor')
G.edge['dpmd']['at_distributor']['write-read'] = '[open open][write read][append read]'
G.add_edge('dpmd','bluetooth')
G.edge['dpmd']['bluetooth']['write-read'] = '[open open][write read]'
G.edge['dpmd']['bluetooth']['fill'] = 'red'
G.add_edge('dpmd','bluetooth')
G.edge['dpmd']['bluetooth']['write-read'] = '[open open][write read][append read]'
G.add_edge('dpmd','cellgeofenced')
G.edge['dpmd']['cellgeofenced']['write-read'] = '[open open][write read]'
G.edge['dpmd']['cellgeofenced']['fill'] = 'red'
G.add_edge('dpmd','cellgeofenced')
G.edge['dpmd']['cellgeofenced']['write-read'] = '[open open][write read][append read]'
G.add_edge('dpmd','charger_monitor')
G.edge['dpmd']['charger_monitor']['write-read'] = '[open open][write read]'
G.edge['dpmd']['charger_monitor']['fill'] = 'red'
G.add_edge('dpmd','charger_monitor')
G.edge['dpmd']['charger_monitor']['write-read'] = '[open open][write read][append read]'
G.add_edge('dpmd','cnd')
G.edge['dpmd']['cnd']['write-read'] = '[open open][append read]'
G.add_edge('dpmd','connfwexe')
G.edge['dpmd']['connfwexe']['write-read'] = '[open open][write read]'
G.edge['dpmd']['connfwexe']['fill'] = 'red'
G.add_edge('dpmd','connfwexe')
G.edge['dpmd']['connfwexe']['write-read'] = '[open open][write read][append read]'
G.add_edge('dpmd','daemon_app_process')
G.edge['dpmd']['daemon_app_process']['write-read'] = '[write read]'
G.edge['dpmd']['daemon_app_process']['fill'] = 'red'
G.add_edge('dpmd','dpmd')
G.edge['dpmd']['dpmd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read]'
G.edge['dpmd']['dpmd']['fill'] = 'red'
G.add_edge('dpmd','dpmd')
G.edge['dpmd']['dpmd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('dpmd','healthd')
G.edge['dpmd']['healthd']['write-read'] = '[open open][write read]'
G.edge['dpmd']['healthd']['fill'] = 'red'
G.add_edge('dpmd','healthd')
G.edge['dpmd']['healthd']['write-read'] = '[open open][write read][append read]'
G.add_edge('dpmd','imsd')
G.edge['dpmd']['imsd']['write-read'] = '[open open][write read]'
G.edge['dpmd']['imsd']['fill'] = 'red'
G.add_edge('dpmd','imsd')
G.edge['dpmd']['imsd']['write-read'] = '[open open][write read][append read]'
G.add_edge('dpmd','ks')
G.edge['dpmd']['ks']['write-read'] = '[open open][append read]'
G.add_edge('dpmd','lhd')
G.edge['dpmd']['lhd']['write-read'] = '[open open][write read]'
G.edge['dpmd']['lhd']['fill'] = 'red'
G.add_edge('dpmd','lhd')
G.edge['dpmd']['lhd']['write-read'] = '[open open][write read][append read]'
G.add_edge('dpmd','mdm_helper')
G.edge['dpmd']['mdm_helper']['write-read'] = '[open open][append read]'
G.add_edge('dpmd','mediaserver')
G.edge['dpmd']['mediaserver']['write-read'] = '[open open][write read]'
G.edge['dpmd']['mediaserver']['fill'] = 'red'
G.add_edge('dpmd','mediaserver')
G.edge['dpmd']['mediaserver']['write-read'] = '[open open][write read][append read]'
G.add_edge('dpmd','mmi')
G.edge['dpmd']['mmi']['write-read'] = '[open open][write read]'
G.edge['dpmd']['mmi']['fill'] = 'red'
G.add_edge('dpmd','mmi')
G.edge['dpmd']['mmi']['write-read'] = '[open open][write read][append read]'
G.add_edge('dpmd','qcks')
G.edge['dpmd']['qcks']['write-read'] = '[open open][append read]'
G.add_edge('dpmd','qlogd')
G.edge['dpmd']['qlogd']['write-read'] = '[open open][append read]'
G.add_edge('dpmd','qmuxd')
G.edge['dpmd']['qmuxd']['write-read'] = '[open open][open open][append read]'
G.add_edge('dpmd','qmuxd')
G.edge['dpmd']['qmuxd']['write-read'] = '[open open][open open][append read][write read]'
G.edge['dpmd']['qmuxd']['fill'] = 'red'
G.add_edge('dpmd','qmuxd')
G.edge['dpmd']['qmuxd']['write-read'] = '[open open][open open][append read][write read][append read]'
G.add_edge('dpmd','rfs_access')
G.edge['dpmd']['rfs_access']['write-read'] = '[open open][write read]'
G.edge['dpmd']['rfs_access']['fill'] = 'red'
G.add_edge('dpmd','rfs_access')
G.edge['dpmd']['rfs_access']['write-read'] = '[open open][write read][append read]'
G.add_edge('dpmd','rild')
G.edge['dpmd']['rild']['write-read'] = '[open open][write read]'
G.edge['dpmd']['rild']['fill'] = 'red'
G.add_edge('dpmd','rild')
G.edge['dpmd']['rild']['write-read'] = '[open open][write read][append read]'
G.add_edge('dpmd','rmt_storage')
G.edge['dpmd']['rmt_storage']['write-read'] = '[open open][write read]'
G.edge['dpmd']['rmt_storage']['fill'] = 'red'
G.add_edge('dpmd','rmt_storage')
G.edge['dpmd']['rmt_storage']['write-read'] = '[open open][write read][append read]'
G.add_edge('dpmd','sec-ril')
G.edge['dpmd']['sec-ril']['write-read'] = '[open open][write read]'
G.edge['dpmd']['sec-ril']['fill'] = 'red'
G.add_edge('dpmd','sensors')
G.edge['dpmd']['sensors']['write-read'] = '[open open][write read]'
G.edge['dpmd']['sensors']['fill'] = 'red'
G.add_edge('dpmd','sensors')
G.edge['dpmd']['sensors']['write-read'] = '[open open][write read][append read]'
G.add_edge('dpmd','system_server')
G.edge['dpmd']['system_server']['write-read'] = '[open open][write read]'
G.edge['dpmd']['system_server']['fill'] = 'red'
G.add_edge('dpmd','system_server')
G.edge['dpmd']['system_server']['write-read'] = '[open open][write read][append read]'
G.add_edge('dpmd','tsdaemon')
G.edge['dpmd']['tsdaemon']['write-read'] = '[write read]'
G.edge['dpmd']['tsdaemon']['fill'] = 'red'
G.add_edge('dpmd','vdc')
G.edge['dpmd']['vdc']['write-read'] = '[write read]'
G.edge['dpmd']['vdc']['fill'] = 'red'
G.add_edge('dpmd','vm_bms')
G.edge['dpmd']['vm_bms']['write-read'] = '[open open][write read]'
G.edge['dpmd']['vm_bms']['fill'] = 'red'
G.add_edge('dpmd','vm_bms')
G.edge['dpmd']['vm_bms']['write-read'] = '[open open][write read][append read]'
G.add_edge('dpmd','vold')
G.edge['dpmd']['vold']['write-read'] = '[open open][write read]'
G.edge['dpmd']['vold']['fill'] = 'red'
G.add_edge('dpmd','vold')
G.edge['dpmd']['vold']['write-read'] = '[open open][write read][append read]'
G.add_edge('dpmd','vpnclientd')
G.edge['dpmd']['vpnclientd']['write-read'] = '[write read]'
G.edge['dpmd']['vpnclientd']['fill'] = 'red'
G.add_edge('healthd','at_distributor')
G.edge['healthd']['at_distributor']['write-read'] = '[open open]'
G.add_edge('healthd','bluetooth')
G.edge['healthd']['bluetooth']['write-read'] = '[open open]'
G.add_edge('healthd','cellgeofenced')
G.edge['healthd']['cellgeofenced']['write-read'] = '[open open]'
G.add_edge('healthd','charger_monitor')
G.edge['healthd']['charger_monitor']['write-read'] = '[setopt getopt][open open]'
G.add_edge('healthd','cnd')
G.edge['healthd']['cnd']['write-read'] = '[open open]'
G.add_edge('healthd','connfwexe')
G.edge['healthd']['connfwexe']['write-read'] = '[open open]'
G.add_edge('healthd','dpmd')
G.edge['healthd']['dpmd']['write-read'] = '[open open]'
G.add_edge('healthd','healthd')
G.edge['healthd']['healthd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('healthd','imsd')
G.edge['healthd']['imsd']['write-read'] = '[open open]'
G.add_edge('healthd','ks')
G.edge['healthd']['ks']['write-read'] = '[open open]'
G.add_edge('healthd','lhd')
G.edge['healthd']['lhd']['write-read'] = '[open open]'
G.add_edge('healthd','mdm_helper')
G.edge['healthd']['mdm_helper']['write-read'] = '[open open]'
G.add_edge('healthd','mediaserver')
G.edge['healthd']['mediaserver']['write-read'] = '[open open]'
G.add_edge('healthd','mmi')
G.edge['healthd']['mmi']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('healthd','qcks')
G.edge['healthd']['qcks']['write-read'] = '[open open]'
G.add_edge('healthd','qlogd')
G.edge['healthd']['qlogd']['write-read'] = '[open open]'
G.add_edge('healthd','qmuxd')
G.edge['healthd']['qmuxd']['write-read'] = '[open open]'
G.add_edge('healthd','qmuxd')
G.edge['healthd']['qmuxd']['write-read'] = '[open open][open open]'
G.add_edge('healthd','rfs_access')
G.edge['healthd']['rfs_access']['write-read'] = '[open open]'
G.add_edge('healthd','rild')
G.edge['healthd']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open]'
G.add_edge('healthd','rmt_storage')
G.edge['healthd']['rmt_storage']['write-read'] = '[open open]'
G.add_edge('healthd','sec-ril')
G.edge['healthd']['sec-ril']['write-read'] = '[open open]'
G.add_edge('healthd','sensors')
G.edge['healthd']['sensors']['write-read'] = '[open open]'
G.add_edge('healthd','system_server')
G.edge['healthd']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open]'
G.add_edge('healthd','vm_bms')
G.edge['healthd']['vm_bms']['write-read'] = '[open open]'
G.add_edge('healthd','vold')
G.edge['healthd']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open]'
G.add_edge('healthd','at_distributor')
G.edge['healthd']['at_distributor']['write-read'] = '[open open][write read]'
G.edge['healthd']['at_distributor']['fill'] = 'red'
G.add_edge('healthd','at_distributor')
G.edge['healthd']['at_distributor']['write-read'] = '[open open][write read][append read]'
G.add_edge('healthd','bluetooth')
G.edge['healthd']['bluetooth']['write-read'] = '[open open][write read]'
G.edge['healthd']['bluetooth']['fill'] = 'red'
G.add_edge('healthd','bluetooth')
G.edge['healthd']['bluetooth']['write-read'] = '[open open][write read][append read]'
G.add_edge('healthd','cellgeofenced')
G.edge['healthd']['cellgeofenced']['write-read'] = '[open open][write read]'
G.edge['healthd']['cellgeofenced']['fill'] = 'red'
G.add_edge('healthd','cellgeofenced')
G.edge['healthd']['cellgeofenced']['write-read'] = '[open open][write read][append read]'
G.add_edge('healthd','charger_monitor')
G.edge['healthd']['charger_monitor']['write-read'] = '[setopt getopt][open open][write read]'
G.edge['healthd']['charger_monitor']['fill'] = 'red'
G.add_edge('healthd','charger_monitor')
G.edge['healthd']['charger_monitor']['write-read'] = '[setopt getopt][open open][write read][append read]'
G.add_edge('healthd','cnd')
G.edge['healthd']['cnd']['write-read'] = '[open open][append read]'
G.add_edge('healthd','connfwexe')
G.edge['healthd']['connfwexe']['write-read'] = '[open open][write read]'
G.edge['healthd']['connfwexe']['fill'] = 'red'
G.add_edge('healthd','connfwexe')
G.edge['healthd']['connfwexe']['write-read'] = '[open open][write read][append read]'
G.add_edge('healthd','daemon_app_process')
G.edge['healthd']['daemon_app_process']['write-read'] = '[write read]'
G.edge['healthd']['daemon_app_process']['fill'] = 'red'
G.add_edge('healthd','dpmd')
G.edge['healthd']['dpmd']['write-read'] = '[open open][write read]'
G.edge['healthd']['dpmd']['fill'] = 'red'
G.add_edge('healthd','dpmd')
G.edge['healthd']['dpmd']['write-read'] = '[open open][write read][append read]'
G.add_edge('healthd','healthd')
G.edge['healthd']['healthd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['healthd']['healthd']['fill'] = 'red'
G.add_edge('healthd','healthd')
G.edge['healthd']['healthd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('healthd','imsd')
G.edge['healthd']['imsd']['write-read'] = '[open open][write read]'
G.edge['healthd']['imsd']['fill'] = 'red'
G.add_edge('healthd','imsd')
G.edge['healthd']['imsd']['write-read'] = '[open open][write read][append read]'
G.add_edge('healthd','ks')
G.edge['healthd']['ks']['write-read'] = '[open open][append read]'
G.add_edge('healthd','lhd')
G.edge['healthd']['lhd']['write-read'] = '[open open][write read]'
G.edge['healthd']['lhd']['fill'] = 'red'
G.add_edge('healthd','lhd')
G.edge['healthd']['lhd']['write-read'] = '[open open][write read][append read]'
G.add_edge('healthd','mdm_helper')
G.edge['healthd']['mdm_helper']['write-read'] = '[open open][append read]'
G.add_edge('healthd','mediaserver')
G.edge['healthd']['mediaserver']['write-read'] = '[open open][write read]'
G.edge['healthd']['mediaserver']['fill'] = 'red'
G.add_edge('healthd','mediaserver')
G.edge['healthd']['mediaserver']['write-read'] = '[open open][write read][append read]'
G.add_edge('healthd','mmi')
G.edge['healthd']['mmi']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['healthd']['mmi']['fill'] = 'red'
G.add_edge('healthd','mmi')
G.edge['healthd']['mmi']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('healthd','qcks')
G.edge['healthd']['qcks']['write-read'] = '[open open][append read]'
G.add_edge('healthd','qlogd')
G.edge['healthd']['qlogd']['write-read'] = '[open open][append read]'
G.add_edge('healthd','qmuxd')
G.edge['healthd']['qmuxd']['write-read'] = '[open open][open open][append read]'
G.add_edge('healthd','qmuxd')
G.edge['healthd']['qmuxd']['write-read'] = '[open open][open open][append read][write read]'
G.edge['healthd']['qmuxd']['fill'] = 'red'
G.add_edge('healthd','qmuxd')
G.edge['healthd']['qmuxd']['write-read'] = '[open open][open open][append read][write read][append read]'
G.add_edge('healthd','rfs_access')
G.edge['healthd']['rfs_access']['write-read'] = '[open open][write read]'
G.edge['healthd']['rfs_access']['fill'] = 'red'
G.add_edge('healthd','rfs_access')
G.edge['healthd']['rfs_access']['write-read'] = '[open open][write read][append read]'
G.add_edge('healthd','rild')
G.edge['healthd']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read]'
G.edge['healthd']['rild']['fill'] = 'red'
G.add_edge('healthd','rild')
G.edge['healthd']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read]'
G.add_edge('healthd','rmt_storage')
G.edge['healthd']['rmt_storage']['write-read'] = '[open open][write read]'
G.edge['healthd']['rmt_storage']['fill'] = 'red'
G.add_edge('healthd','rmt_storage')
G.edge['healthd']['rmt_storage']['write-read'] = '[open open][write read][append read]'
G.add_edge('healthd','sec-ril')
G.edge['healthd']['sec-ril']['write-read'] = '[open open][write read]'
G.edge['healthd']['sec-ril']['fill'] = 'red'
G.add_edge('healthd','sensors')
G.edge['healthd']['sensors']['write-read'] = '[open open][write read]'
G.edge['healthd']['sensors']['fill'] = 'red'
G.add_edge('healthd','sensors')
G.edge['healthd']['sensors']['write-read'] = '[open open][write read][append read]'
G.add_edge('healthd','system_server')
G.edge['healthd']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read]'
G.edge['healthd']['system_server']['fill'] = 'red'
G.add_edge('healthd','system_server')
G.edge['healthd']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read]'
G.add_edge('healthd','tsdaemon')
G.edge['healthd']['tsdaemon']['write-read'] = '[write read]'
G.edge['healthd']['tsdaemon']['fill'] = 'red'
G.add_edge('healthd','vdc')
G.edge['healthd']['vdc']['write-read'] = '[write read]'
G.edge['healthd']['vdc']['fill'] = 'red'
G.add_edge('healthd','vm_bms')
G.edge['healthd']['vm_bms']['write-read'] = '[open open][write read]'
G.edge['healthd']['vm_bms']['fill'] = 'red'
G.add_edge('healthd','vm_bms')
G.edge['healthd']['vm_bms']['write-read'] = '[open open][write read][append read]'
G.add_edge('healthd','vold')
G.edge['healthd']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read]'
G.edge['healthd']['vold']['fill'] = 'red'
G.add_edge('healthd','vold')
G.edge['healthd']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read]'
G.add_edge('healthd','vpnclientd')
G.edge['healthd']['vpnclientd']['write-read'] = '[write read]'
G.edge['healthd']['vpnclientd']['fill'] = 'red'
G.add_edge('imsd','at_distributor')
G.edge['imsd']['at_distributor']['write-read'] = '[open open]'
G.add_edge('imsd','bluetooth')
G.edge['imsd']['bluetooth']['write-read'] = '[open open]'
G.add_edge('imsd','cellgeofenced')
G.edge['imsd']['cellgeofenced']['write-read'] = '[open open]'
G.add_edge('imsd','charger_monitor')
G.edge['imsd']['charger_monitor']['write-read'] = '[open open]'
G.add_edge('imsd','cnd')
G.edge['imsd']['cnd']['write-read'] = '[open open]'
G.add_edge('imsd','connfwexe')
G.edge['imsd']['connfwexe']['write-read'] = '[open open]'
G.add_edge('imsd','dpmd')
G.edge['imsd']['dpmd']['write-read'] = '[open open]'
G.add_edge('imsd','healthd')
G.edge['imsd']['healthd']['write-read'] = '[open open]'
G.add_edge('imsd','imsd')
G.edge['imsd']['imsd']['write-read'] = '[write read][open open]'
G.add_edge('imsd','ks')
G.edge['imsd']['ks']['write-read'] = '[open open]'
G.add_edge('imsd','lhd')
G.edge['imsd']['lhd']['write-read'] = '[open open]'
G.add_edge('imsd','mdm_helper')
G.edge['imsd']['mdm_helper']['write-read'] = '[open open]'
G.add_edge('imsd','mediaserver')
G.edge['imsd']['mediaserver']['write-read'] = '[open open]'
G.add_edge('imsd','mmi')
G.edge['imsd']['mmi']['write-read'] = '[open open]'
G.add_edge('imsd','qcks')
G.edge['imsd']['qcks']['write-read'] = '[open open]'
G.add_edge('imsd','qlogd')
G.edge['imsd']['qlogd']['write-read'] = '[open open]'
G.add_edge('imsd','qmuxd')
G.edge['imsd']['qmuxd']['write-read'] = '[open open]'
G.add_edge('imsd','qmuxd')
G.edge['imsd']['qmuxd']['write-read'] = '[open open][open open]'
G.add_edge('imsd','rfs_access')
G.edge['imsd']['rfs_access']['write-read'] = '[open open]'
G.add_edge('imsd','rild')
G.edge['imsd']['rild']['write-read'] = '[open open]'
G.add_edge('imsd','rmt_storage')
G.edge['imsd']['rmt_storage']['write-read'] = '[open open]'
G.add_edge('imsd','sec-ril')
G.edge['imsd']['sec-ril']['write-read'] = '[open open]'
G.add_edge('imsd','sensors')
G.edge['imsd']['sensors']['write-read'] = '[open open]'
G.add_edge('imsd','system_server')
G.edge['imsd']['system_server']['write-read'] = '[open open]'
G.add_edge('imsd','vm_bms')
G.edge['imsd']['vm_bms']['write-read'] = '[open open]'
G.add_edge('imsd','vold')
G.edge['imsd']['vold']['write-read'] = '[open open]'
G.add_edge('imsd','at_distributor')
G.edge['imsd']['at_distributor']['write-read'] = '[open open][write read]'
G.edge['imsd']['at_distributor']['fill'] = 'red'
G.add_edge('imsd','at_distributor')
G.edge['imsd']['at_distributor']['write-read'] = '[open open][write read][append read]'
G.add_edge('imsd','bluetooth')
G.edge['imsd']['bluetooth']['write-read'] = '[open open][write read]'
G.edge['imsd']['bluetooth']['fill'] = 'red'
G.add_edge('imsd','bluetooth')
G.edge['imsd']['bluetooth']['write-read'] = '[open open][write read][append read]'
G.add_edge('imsd','cellgeofenced')
G.edge['imsd']['cellgeofenced']['write-read'] = '[open open][write read]'
G.edge['imsd']['cellgeofenced']['fill'] = 'red'
G.add_edge('imsd','cellgeofenced')
G.edge['imsd']['cellgeofenced']['write-read'] = '[open open][write read][append read]'
G.add_edge('imsd','charger_monitor')
G.edge['imsd']['charger_monitor']['write-read'] = '[open open][write read]'
G.edge['imsd']['charger_monitor']['fill'] = 'red'
G.add_edge('imsd','charger_monitor')
G.edge['imsd']['charger_monitor']['write-read'] = '[open open][write read][append read]'
G.add_edge('imsd','cnd')
G.edge['imsd']['cnd']['write-read'] = '[open open][append read]'
G.add_edge('imsd','connfwexe')
G.edge['imsd']['connfwexe']['write-read'] = '[open open][write read]'
G.edge['imsd']['connfwexe']['fill'] = 'red'
G.add_edge('imsd','connfwexe')
G.edge['imsd']['connfwexe']['write-read'] = '[open open][write read][append read]'
G.add_edge('imsd','daemon_app_process')
G.edge['imsd']['daemon_app_process']['write-read'] = '[write read]'
G.edge['imsd']['daemon_app_process']['fill'] = 'red'
G.add_edge('imsd','dpmd')
G.edge['imsd']['dpmd']['write-read'] = '[open open][write read]'
G.edge['imsd']['dpmd']['fill'] = 'red'
G.add_edge('imsd','dpmd')
G.edge['imsd']['dpmd']['write-read'] = '[open open][write read][append read]'
G.add_edge('imsd','healthd')
G.edge['imsd']['healthd']['write-read'] = '[open open][write read]'
G.edge['imsd']['healthd']['fill'] = 'red'
G.add_edge('imsd','healthd')
G.edge['imsd']['healthd']['write-read'] = '[open open][write read][append read]'
G.add_edge('imsd','imsd')
G.edge['imsd']['imsd']['write-read'] = '[write read][open open][write read]'
G.edge['imsd']['imsd']['fill'] = 'red'
G.add_edge('imsd','imsd')
G.edge['imsd']['imsd']['write-read'] = '[write read][open open][write read][append read]'
G.add_edge('imsd','ks')
G.edge['imsd']['ks']['write-read'] = '[open open][append read]'
G.add_edge('imsd','lhd')
G.edge['imsd']['lhd']['write-read'] = '[open open][write read]'
G.edge['imsd']['lhd']['fill'] = 'red'
G.add_edge('imsd','lhd')
G.edge['imsd']['lhd']['write-read'] = '[open open][write read][append read]'
G.add_edge('imsd','mdm_helper')
G.edge['imsd']['mdm_helper']['write-read'] = '[open open][append read]'
G.add_edge('imsd','mediaserver')
G.edge['imsd']['mediaserver']['write-read'] = '[open open][write read]'
G.edge['imsd']['mediaserver']['fill'] = 'red'
G.add_edge('imsd','mediaserver')
G.edge['imsd']['mediaserver']['write-read'] = '[open open][write read][append read]'
G.add_edge('imsd','mmi')
G.edge['imsd']['mmi']['write-read'] = '[open open][write read]'
G.edge['imsd']['mmi']['fill'] = 'red'
G.add_edge('imsd','mmi')
G.edge['imsd']['mmi']['write-read'] = '[open open][write read][append read]'
G.add_edge('imsd','qcks')
G.edge['imsd']['qcks']['write-read'] = '[open open][append read]'
G.add_edge('imsd','qlogd')
G.edge['imsd']['qlogd']['write-read'] = '[open open][append read]'
G.add_edge('imsd','qmuxd')
G.edge['imsd']['qmuxd']['write-read'] = '[open open][open open][append read]'
G.add_edge('imsd','qmuxd')
G.edge['imsd']['qmuxd']['write-read'] = '[open open][open open][append read][write read]'
G.edge['imsd']['qmuxd']['fill'] = 'red'
G.add_edge('imsd','qmuxd')
G.edge['imsd']['qmuxd']['write-read'] = '[open open][open open][append read][write read][append read]'
G.add_edge('imsd','rfs_access')
G.edge['imsd']['rfs_access']['write-read'] = '[open open][write read]'
G.edge['imsd']['rfs_access']['fill'] = 'red'
G.add_edge('imsd','rfs_access')
G.edge['imsd']['rfs_access']['write-read'] = '[open open][write read][append read]'
G.add_edge('imsd','rild')
G.edge['imsd']['rild']['write-read'] = '[open open][write read]'
G.edge['imsd']['rild']['fill'] = 'red'
G.add_edge('imsd','rild')
G.edge['imsd']['rild']['write-read'] = '[open open][write read][append read]'
G.add_edge('imsd','rmt_storage')
G.edge['imsd']['rmt_storage']['write-read'] = '[open open][write read]'
G.edge['imsd']['rmt_storage']['fill'] = 'red'
G.add_edge('imsd','rmt_storage')
G.edge['imsd']['rmt_storage']['write-read'] = '[open open][write read][append read]'
G.add_edge('imsd','sec-ril')
G.edge['imsd']['sec-ril']['write-read'] = '[open open][write read]'
G.edge['imsd']['sec-ril']['fill'] = 'red'
G.add_edge('imsd','sensors')
G.edge['imsd']['sensors']['write-read'] = '[open open][write read]'
G.edge['imsd']['sensors']['fill'] = 'red'
G.add_edge('imsd','sensors')
G.edge['imsd']['sensors']['write-read'] = '[open open][write read][append read]'
G.add_edge('imsd','system_server')
G.edge['imsd']['system_server']['write-read'] = '[open open][write read]'
G.edge['imsd']['system_server']['fill'] = 'red'
G.add_edge('imsd','system_server')
G.edge['imsd']['system_server']['write-read'] = '[open open][write read][append read]'
G.add_edge('imsd','tsdaemon')
G.edge['imsd']['tsdaemon']['write-read'] = '[write read]'
G.edge['imsd']['tsdaemon']['fill'] = 'red'
G.add_edge('imsd','vdc')
G.edge['imsd']['vdc']['write-read'] = '[write read]'
G.edge['imsd']['vdc']['fill'] = 'red'
G.add_edge('imsd','vm_bms')
G.edge['imsd']['vm_bms']['write-read'] = '[open open][write read]'
G.edge['imsd']['vm_bms']['fill'] = 'red'
G.add_edge('imsd','vm_bms')
G.edge['imsd']['vm_bms']['write-read'] = '[open open][write read][append read]'
G.add_edge('imsd','vold')
G.edge['imsd']['vold']['write-read'] = '[open open][write read]'
G.edge['imsd']['vold']['fill'] = 'red'
G.add_edge('imsd','vold')
G.edge['imsd']['vold']['write-read'] = '[open open][write read][append read]'
G.add_edge('imsd','vpnclientd')
G.edge['imsd']['vpnclientd']['write-read'] = '[write read]'
G.edge['imsd']['vpnclientd']['fill'] = 'red'
G.add_edge('ks','at_distributor')
G.edge['ks']['at_distributor']['write-read'] = '[open open]'
G.add_edge('ks','bluetooth')
G.edge['ks']['bluetooth']['write-read'] = '[open open]'
G.add_edge('ks','cellgeofenced')
G.edge['ks']['cellgeofenced']['write-read'] = '[open open]'
G.add_edge('ks','charger_monitor')
G.edge['ks']['charger_monitor']['write-read'] = '[open open]'
G.add_edge('ks','cnd')
G.edge['ks']['cnd']['write-read'] = '[open open]'
G.add_edge('ks','connfwexe')
G.edge['ks']['connfwexe']['write-read'] = '[open open]'
G.add_edge('ks','dpmd')
G.edge['ks']['dpmd']['write-read'] = '[open open]'
G.add_edge('ks','healthd')
G.edge['ks']['healthd']['write-read'] = '[open open]'
G.add_edge('ks','imsd')
G.edge['ks']['imsd']['write-read'] = '[open open]'
G.add_edge('ks','ks')
G.edge['ks']['ks']['write-read'] = '[open open][write read][add_name search][open open][write read][add_name search][open open]'
G.add_edge('ks','lhd')
G.edge['ks']['lhd']['write-read'] = '[open open]'
G.add_edge('ks','mdm_helper')
G.edge['ks']['mdm_helper']['write-read'] = '[write read][open open]'
G.add_edge('ks','mediaserver')
G.edge['ks']['mediaserver']['write-read'] = '[open open]'
G.add_edge('ks','mmi')
G.edge['ks']['mmi']['write-read'] = '[open open]'
G.add_edge('ks','qcks')
G.edge['ks']['qcks']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][open open]'
G.add_edge('ks','qlogd')
G.edge['ks']['qlogd']['write-read'] = '[open open]'
G.add_edge('ks','qmuxd')
G.edge['ks']['qmuxd']['write-read'] = '[open open]'
G.add_edge('ks','qmuxd')
G.edge['ks']['qmuxd']['write-read'] = '[open open][open open]'
G.add_edge('ks','rfs_access')
G.edge['ks']['rfs_access']['write-read'] = '[open open]'
G.add_edge('ks','rild')
G.edge['ks']['rild']['write-read'] = '[open open]'
G.add_edge('ks','rmt_storage')
G.edge['ks']['rmt_storage']['write-read'] = '[open open]'
G.add_edge('ks','sec-ril')
G.edge['ks']['sec-ril']['write-read'] = '[open open]'
G.add_edge('ks','sensors')
G.edge['ks']['sensors']['write-read'] = '[open open]'
G.add_edge('ks','system_server')
G.edge['ks']['system_server']['write-read'] = '[open open]'
G.add_edge('ks','vm_bms')
G.edge['ks']['vm_bms']['write-read'] = '[open open]'
G.add_edge('ks','vold')
G.edge['ks']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('ks','at_distributor')
G.edge['ks']['at_distributor']['write-read'] = '[open open][write read]'
G.edge['ks']['at_distributor']['fill'] = 'red'
G.add_edge('ks','at_distributor')
G.edge['ks']['at_distributor']['write-read'] = '[open open][write read][append read]'
G.add_edge('ks','bluetooth')
G.edge['ks']['bluetooth']['write-read'] = '[open open][write read]'
G.edge['ks']['bluetooth']['fill'] = 'red'
G.add_edge('ks','bluetooth')
G.edge['ks']['bluetooth']['write-read'] = '[open open][write read][append read]'
G.add_edge('ks','cellgeofenced')
G.edge['ks']['cellgeofenced']['write-read'] = '[open open][write read]'
G.edge['ks']['cellgeofenced']['fill'] = 'red'
G.add_edge('ks','cellgeofenced')
G.edge['ks']['cellgeofenced']['write-read'] = '[open open][write read][append read]'
G.add_edge('ks','charger_monitor')
G.edge['ks']['charger_monitor']['write-read'] = '[open open][write read]'
G.edge['ks']['charger_monitor']['fill'] = 'red'
G.add_edge('ks','charger_monitor')
G.edge['ks']['charger_monitor']['write-read'] = '[open open][write read][append read]'
G.add_edge('ks','cnd')
G.edge['ks']['cnd']['write-read'] = '[open open][append read]'
G.add_edge('ks','connfwexe')
G.edge['ks']['connfwexe']['write-read'] = '[open open][write read]'
G.edge['ks']['connfwexe']['fill'] = 'red'
G.add_edge('ks','connfwexe')
G.edge['ks']['connfwexe']['write-read'] = '[open open][write read][append read]'
G.add_edge('ks','daemon_app_process')
G.edge['ks']['daemon_app_process']['write-read'] = '[write read]'
G.edge['ks']['daemon_app_process']['fill'] = 'red'
G.add_edge('ks','dpmd')
G.edge['ks']['dpmd']['write-read'] = '[open open][write read]'
G.edge['ks']['dpmd']['fill'] = 'red'
G.add_edge('ks','dpmd')
G.edge['ks']['dpmd']['write-read'] = '[open open][write read][append read]'
G.add_edge('ks','healthd')
G.edge['ks']['healthd']['write-read'] = '[open open][write read]'
G.edge['ks']['healthd']['fill'] = 'red'
G.add_edge('ks','healthd')
G.edge['ks']['healthd']['write-read'] = '[open open][write read][append read]'
G.add_edge('ks','imsd')
G.edge['ks']['imsd']['write-read'] = '[open open][write read]'
G.edge['ks']['imsd']['fill'] = 'red'
G.add_edge('ks','imsd')
G.edge['ks']['imsd']['write-read'] = '[open open][write read][append read]'
G.add_edge('ks','ks')
G.edge['ks']['ks']['write-read'] = '[open open][write read][add_name search][open open][write read][add_name search][open open][append read]'
G.add_edge('ks','lhd')
G.edge['ks']['lhd']['write-read'] = '[open open][write read]'
G.edge['ks']['lhd']['fill'] = 'red'
G.add_edge('ks','lhd')
G.edge['ks']['lhd']['write-read'] = '[open open][write read][append read]'
G.add_edge('ks','mdm_helper')
G.edge['ks']['mdm_helper']['write-read'] = '[write read][open open][append read]'
G.add_edge('ks','mediaserver')
G.edge['ks']['mediaserver']['write-read'] = '[open open][write read]'
G.edge['ks']['mediaserver']['fill'] = 'red'
G.add_edge('ks','mediaserver')
G.edge['ks']['mediaserver']['write-read'] = '[open open][write read][append read]'
G.add_edge('ks','mmi')
G.edge['ks']['mmi']['write-read'] = '[open open][write read]'
G.edge['ks']['mmi']['fill'] = 'red'
G.add_edge('ks','mmi')
G.edge['ks']['mmi']['write-read'] = '[open open][write read][append read]'
G.add_edge('ks','qcks')
G.edge['ks']['qcks']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][open open][append read]'
G.add_edge('ks','qlogd')
G.edge['ks']['qlogd']['write-read'] = '[open open][append read]'
G.add_edge('ks','qmuxd')
G.edge['ks']['qmuxd']['write-read'] = '[open open][open open][append read]'
G.add_edge('ks','qmuxd')
G.edge['ks']['qmuxd']['write-read'] = '[open open][open open][append read][write read]'
G.edge['ks']['qmuxd']['fill'] = 'red'
G.add_edge('ks','qmuxd')
G.edge['ks']['qmuxd']['write-read'] = '[open open][open open][append read][write read][append read]'
G.add_edge('ks','rfs_access')
G.edge['ks']['rfs_access']['write-read'] = '[open open][write read]'
G.edge['ks']['rfs_access']['fill'] = 'red'
G.add_edge('ks','rfs_access')
G.edge['ks']['rfs_access']['write-read'] = '[open open][write read][append read]'
G.add_edge('ks','rild')
G.edge['ks']['rild']['write-read'] = '[open open][write read]'
G.edge['ks']['rild']['fill'] = 'red'
G.add_edge('ks','rild')
G.edge['ks']['rild']['write-read'] = '[open open][write read][append read]'
G.add_edge('ks','rmt_storage')
G.edge['ks']['rmt_storage']['write-read'] = '[open open][write read]'
G.edge['ks']['rmt_storage']['fill'] = 'red'
G.add_edge('ks','rmt_storage')
G.edge['ks']['rmt_storage']['write-read'] = '[open open][write read][append read]'
G.add_edge('ks','sec-ril')
G.edge['ks']['sec-ril']['write-read'] = '[open open][write read]'
G.edge['ks']['sec-ril']['fill'] = 'red'
G.add_edge('ks','sensors')
G.edge['ks']['sensors']['write-read'] = '[open open][write read]'
G.edge['ks']['sensors']['fill'] = 'red'
G.add_edge('ks','sensors')
G.edge['ks']['sensors']['write-read'] = '[open open][write read][append read]'
G.add_edge('ks','system_server')
G.edge['ks']['system_server']['write-read'] = '[open open][write read]'
G.edge['ks']['system_server']['fill'] = 'red'
G.add_edge('ks','system_server')
G.edge['ks']['system_server']['write-read'] = '[open open][write read][append read]'
G.add_edge('ks','tsdaemon')
G.edge['ks']['tsdaemon']['write-read'] = '[write read]'
G.edge['ks']['tsdaemon']['fill'] = 'red'
G.add_edge('ks','vdc')
G.edge['ks']['vdc']['write-read'] = '[write read]'
G.edge['ks']['vdc']['fill'] = 'red'
G.add_edge('ks','vm_bms')
G.edge['ks']['vm_bms']['write-read'] = '[open open][write read]'
G.edge['ks']['vm_bms']['fill'] = 'red'
G.add_edge('ks','vm_bms')
G.edge['ks']['vm_bms']['write-read'] = '[open open][write read][append read]'
G.add_edge('ks','vold')
G.edge['ks']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['ks']['vold']['fill'] = 'red'
G.add_edge('ks','vold')
G.edge['ks']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('ks','vpnclientd')
G.edge['ks']['vpnclientd']['write-read'] = '[write read]'
G.edge['ks']['vpnclientd']['fill'] = 'red'
G.add_edge('lhd','at_distributor')
G.edge['lhd']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('lhd','bluetooth')
G.edge['lhd']['bluetooth']['write-read'] = '[open open]'
G.add_edge('lhd','cellgeofenced')
G.edge['lhd']['cellgeofenced']['write-read'] = '[open open]'
G.add_edge('lhd','charger_monitor')
G.edge['lhd']['charger_monitor']['write-read'] = '[open open]'
G.add_edge('lhd','cnd')
G.edge['lhd']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open]'
G.add_edge('lhd','connfwexe')
G.edge['lhd']['connfwexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('lhd','dpmd')
G.edge['lhd']['dpmd']['write-read'] = '[open open]'
G.add_edge('lhd','healthd')
G.edge['lhd']['healthd']['write-read'] = '[open open]'
G.add_edge('lhd','imsd')
G.edge['lhd']['imsd']['write-read'] = '[open open]'
G.add_edge('lhd','ks')
G.edge['lhd']['ks']['write-read'] = '[open open]'
G.add_edge('lhd','lhd')
G.edge['lhd']['lhd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('lhd','mdm_helper')
G.edge['lhd']['mdm_helper']['write-read'] = '[open open]'
G.add_edge('lhd','mediaserver')
G.edge['lhd']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('lhd','mmi')
G.edge['lhd']['mmi']['write-read'] = '[open open]'
G.add_edge('lhd','qcks')
G.edge['lhd']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open]'
G.add_edge('lhd','qlogd')
G.edge['lhd']['qlogd']['write-read'] = '[write read][add_name search][open open]'
G.add_edge('lhd','qmuxd')
G.edge['lhd']['qmuxd']['write-read'] = '[open open]'
G.add_edge('lhd','qmuxd')
G.edge['lhd']['qmuxd']['write-read'] = '[open open][open open]'
G.add_edge('lhd','rfs_access')
G.edge['lhd']['rfs_access']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('lhd','rild')
G.edge['lhd']['rild']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('lhd','rmt_storage')
G.edge['lhd']['rmt_storage']['write-read'] = '[open open]'
G.add_edge('lhd','sec-ril')
G.edge['lhd']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('lhd','sensors')
G.edge['lhd']['sensors']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('lhd','system_server')
G.edge['lhd']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('lhd','vm_bms')
G.edge['lhd']['vm_bms']['write-read'] = '[open open]'
G.add_edge('lhd','vold')
G.edge['lhd']['vold']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('lhd','at_distributor')
G.edge['lhd']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['lhd']['at_distributor']['fill'] = 'red'
G.add_edge('lhd','at_distributor')
G.edge['lhd']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('lhd','bluetooth')
G.edge['lhd']['bluetooth']['write-read'] = '[open open][write read]'
G.edge['lhd']['bluetooth']['fill'] = 'red'
G.add_edge('lhd','bluetooth')
G.edge['lhd']['bluetooth']['write-read'] = '[open open][write read][append read]'
G.add_edge('lhd','cellgeofenced')
G.edge['lhd']['cellgeofenced']['write-read'] = '[open open][write read]'
G.edge['lhd']['cellgeofenced']['fill'] = 'red'
G.add_edge('lhd','cellgeofenced')
G.edge['lhd']['cellgeofenced']['write-read'] = '[open open][write read][append read]'
G.add_edge('lhd','charger_monitor')
G.edge['lhd']['charger_monitor']['write-read'] = '[open open][write read]'
G.edge['lhd']['charger_monitor']['fill'] = 'red'
G.add_edge('lhd','charger_monitor')
G.edge['lhd']['charger_monitor']['write-read'] = '[open open][write read][append read]'
G.add_edge('lhd','cnd')
G.edge['lhd']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][append read]'
G.add_edge('lhd','connfwexe')
G.edge['lhd']['connfwexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['lhd']['connfwexe']['fill'] = 'red'
G.add_edge('lhd','connfwexe')
G.edge['lhd']['connfwexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('lhd','daemon_app_process')
G.edge['lhd']['daemon_app_process']['write-read'] = '[write read]'
G.edge['lhd']['daemon_app_process']['fill'] = 'red'
G.add_edge('lhd','dpmd')
G.edge['lhd']['dpmd']['write-read'] = '[open open][write read]'
G.edge['lhd']['dpmd']['fill'] = 'red'
G.add_edge('lhd','dpmd')
G.edge['lhd']['dpmd']['write-read'] = '[open open][write read][append read]'
G.add_edge('lhd','healthd')
G.edge['lhd']['healthd']['write-read'] = '[open open][write read]'
G.edge['lhd']['healthd']['fill'] = 'red'
G.add_edge('lhd','healthd')
G.edge['lhd']['healthd']['write-read'] = '[open open][write read][append read]'
G.add_edge('lhd','imsd')
G.edge['lhd']['imsd']['write-read'] = '[open open][write read]'
G.edge['lhd']['imsd']['fill'] = 'red'
G.add_edge('lhd','imsd')
G.edge['lhd']['imsd']['write-read'] = '[open open][write read][append read]'
G.add_edge('lhd','ks')
G.edge['lhd']['ks']['write-read'] = '[open open][append read]'
G.add_edge('lhd','lhd')
G.edge['lhd']['lhd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['lhd']['lhd']['fill'] = 'red'
G.add_edge('lhd','lhd')
G.edge['lhd']['lhd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('lhd','mdm_helper')
G.edge['lhd']['mdm_helper']['write-read'] = '[open open][append read]'
G.add_edge('lhd','mediaserver')
G.edge['lhd']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['lhd']['mediaserver']['fill'] = 'red'
G.add_edge('lhd','mediaserver')
G.edge['lhd']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('lhd','mmi')
G.edge['lhd']['mmi']['write-read'] = '[open open][write read]'
G.edge['lhd']['mmi']['fill'] = 'red'
G.add_edge('lhd','mmi')
G.edge['lhd']['mmi']['write-read'] = '[open open][write read][append read]'
G.add_edge('lhd','qcks')
G.edge['lhd']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][append read]'
G.add_edge('lhd','qlogd')
G.edge['lhd']['qlogd']['write-read'] = '[write read][add_name search][open open][append read]'
G.add_edge('lhd','qmuxd')
G.edge['lhd']['qmuxd']['write-read'] = '[open open][open open][append read]'
G.add_edge('lhd','qmuxd')
G.edge['lhd']['qmuxd']['write-read'] = '[open open][open open][append read][write read]'
G.edge['lhd']['qmuxd']['fill'] = 'red'
G.add_edge('lhd','qmuxd')
G.edge['lhd']['qmuxd']['write-read'] = '[open open][open open][append read][write read][append read]'
G.add_edge('lhd','rfs_access')
G.edge['lhd']['rfs_access']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['lhd']['rfs_access']['fill'] = 'red'
G.add_edge('lhd','rfs_access')
G.edge['lhd']['rfs_access']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('lhd','rild')
G.edge['lhd']['rild']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read]'
G.edge['lhd']['rild']['fill'] = 'red'
G.add_edge('lhd','rild')
G.edge['lhd']['rild']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('lhd','rmt_storage')
G.edge['lhd']['rmt_storage']['write-read'] = '[open open][write read]'
G.edge['lhd']['rmt_storage']['fill'] = 'red'
G.add_edge('lhd','rmt_storage')
G.edge['lhd']['rmt_storage']['write-read'] = '[open open][write read][append read]'
G.add_edge('lhd','sec-ril')
G.edge['lhd']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['lhd']['sec-ril']['fill'] = 'red'
G.add_edge('lhd','sensors')
G.edge['lhd']['sensors']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['lhd']['sensors']['fill'] = 'red'
G.add_edge('lhd','sensors')
G.edge['lhd']['sensors']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('lhd','system_server')
G.edge['lhd']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['lhd']['system_server']['fill'] = 'red'
G.add_edge('lhd','system_server')
G.edge['lhd']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('lhd','tsdaemon')
G.edge['lhd']['tsdaemon']['write-read'] = '[write read]'
G.edge['lhd']['tsdaemon']['fill'] = 'red'
G.add_edge('lhd','vdc')
G.edge['lhd']['vdc']['write-read'] = '[write read]'
G.edge['lhd']['vdc']['fill'] = 'red'
G.add_edge('lhd','vm_bms')
G.edge['lhd']['vm_bms']['write-read'] = '[open open][write read]'
G.edge['lhd']['vm_bms']['fill'] = 'red'
G.add_edge('lhd','vm_bms')
G.edge['lhd']['vm_bms']['write-read'] = '[open open][write read][append read]'
G.add_edge('lhd','vold')
G.edge['lhd']['vold']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read]'
G.edge['lhd']['vold']['fill'] = 'red'
G.add_edge('lhd','vold')
G.edge['lhd']['vold']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('lhd','vpnclientd')
G.edge['lhd']['vpnclientd']['write-read'] = '[write read]'
G.edge['lhd']['vpnclientd']['fill'] = 'red'
G.add_edge('mediaserver','at_distributor')
G.edge['mediaserver']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('mediaserver','bluetooth')
G.edge['mediaserver']['bluetooth']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('mediaserver','cellgeofenced')
G.edge['mediaserver']['cellgeofenced']['write-read'] = '[open open]'
G.add_edge('mediaserver','charger_monitor')
G.edge['mediaserver']['charger_monitor']['write-read'] = '[open open]'
G.add_edge('mediaserver','cnd')
G.edge['mediaserver']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open]'
G.add_edge('mediaserver','connfwexe')
G.edge['mediaserver']['connfwexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('mediaserver','dpmd')
G.edge['mediaserver']['dpmd']['write-read'] = '[open open]'
G.add_edge('mediaserver','healthd')
G.edge['mediaserver']['healthd']['write-read'] = '[open open]'
G.add_edge('mediaserver','imsd')
G.edge['mediaserver']['imsd']['write-read'] = '[open open]'
G.add_edge('mediaserver','ks')
G.edge['mediaserver']['ks']['write-read'] = '[open open]'
G.add_edge('mediaserver','lhd')
G.edge['mediaserver']['lhd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('mediaserver','mdm_helper')
G.edge['mediaserver']['mdm_helper']['write-read'] = '[open open]'
G.add_edge('mediaserver','mediaserver')
G.edge['mediaserver']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('mediaserver','mmi')
G.edge['mediaserver']['mmi']['write-read'] = '[open open]'
G.add_edge('mediaserver','qcks')
G.edge['mediaserver']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open]'
G.add_edge('mediaserver','qlogd')
G.edge['mediaserver']['qlogd']['write-read'] = '[write read][add_name search][open open]'
G.add_edge('mediaserver','qmuxd')
G.edge['mediaserver']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('mediaserver','qmuxd')
G.edge['mediaserver']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open]'
G.add_edge('mediaserver','rfs_access')
G.edge['mediaserver']['rfs_access']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('mediaserver','rild')
G.edge['mediaserver']['rild']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('mediaserver','rmt_storage')
G.edge['mediaserver']['rmt_storage']['write-read'] = '[open open]'
G.add_edge('mediaserver','sec-ril')
G.edge['mediaserver']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('mediaserver','sensors')
G.edge['mediaserver']['sensors']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('mediaserver','system_server')
G.edge['mediaserver']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][write read][append read][open open]'
G.add_edge('mediaserver','vm_bms')
G.edge['mediaserver']['vm_bms']['write-read'] = '[open open]'
G.add_edge('mediaserver','vold')
G.edge['mediaserver']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][append read][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('mediaserver','at_distributor')
G.edge['mediaserver']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['mediaserver']['at_distributor']['fill'] = 'red'
G.add_edge('mediaserver','at_distributor')
G.edge['mediaserver']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('mediaserver','bluetooth')
G.edge['mediaserver']['bluetooth']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['mediaserver']['bluetooth']['fill'] = 'red'
G.add_edge('mediaserver','bluetooth')
G.edge['mediaserver']['bluetooth']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('mediaserver','cellgeofenced')
G.edge['mediaserver']['cellgeofenced']['write-read'] = '[open open][write read]'
G.edge['mediaserver']['cellgeofenced']['fill'] = 'red'
G.add_edge('mediaserver','cellgeofenced')
G.edge['mediaserver']['cellgeofenced']['write-read'] = '[open open][write read][append read]'
G.add_edge('mediaserver','charger_monitor')
G.edge['mediaserver']['charger_monitor']['write-read'] = '[open open][write read]'
G.edge['mediaserver']['charger_monitor']['fill'] = 'red'
G.add_edge('mediaserver','charger_monitor')
G.edge['mediaserver']['charger_monitor']['write-read'] = '[open open][write read][append read]'
G.add_edge('mediaserver','cnd')
G.edge['mediaserver']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][append read]'
G.add_edge('mediaserver','connfwexe')
G.edge['mediaserver']['connfwexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['mediaserver']['connfwexe']['fill'] = 'red'
G.add_edge('mediaserver','connfwexe')
G.edge['mediaserver']['connfwexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('mediaserver','daemon_app_process')
G.edge['mediaserver']['daemon_app_process']['write-read'] = '[write read]'
G.edge['mediaserver']['daemon_app_process']['fill'] = 'red'
G.add_edge('mediaserver','dpmd')
G.edge['mediaserver']['dpmd']['write-read'] = '[open open][write read]'
G.edge['mediaserver']['dpmd']['fill'] = 'red'
G.add_edge('mediaserver','dpmd')
G.edge['mediaserver']['dpmd']['write-read'] = '[open open][write read][append read]'
G.add_edge('mediaserver','healthd')
G.edge['mediaserver']['healthd']['write-read'] = '[open open][write read]'
G.edge['mediaserver']['healthd']['fill'] = 'red'
G.add_edge('mediaserver','healthd')
G.edge['mediaserver']['healthd']['write-read'] = '[open open][write read][append read]'
G.add_edge('mediaserver','imsd')
G.edge['mediaserver']['imsd']['write-read'] = '[open open][write read]'
G.edge['mediaserver']['imsd']['fill'] = 'red'
G.add_edge('mediaserver','imsd')
G.edge['mediaserver']['imsd']['write-read'] = '[open open][write read][append read]'
G.add_edge('mediaserver','ks')
G.edge['mediaserver']['ks']['write-read'] = '[open open][append read]'
G.add_edge('mediaserver','lhd')
G.edge['mediaserver']['lhd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['mediaserver']['lhd']['fill'] = 'red'
G.add_edge('mediaserver','lhd')
G.edge['mediaserver']['lhd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('mediaserver','mdm_helper')
G.edge['mediaserver']['mdm_helper']['write-read'] = '[open open][append read]'
G.add_edge('mediaserver','mediaserver')
G.edge['mediaserver']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read]'
G.edge['mediaserver']['mediaserver']['fill'] = 'red'
G.add_edge('mediaserver','mediaserver')
G.edge['mediaserver']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('mediaserver','mmi')
G.edge['mediaserver']['mmi']['write-read'] = '[open open][write read]'
G.edge['mediaserver']['mmi']['fill'] = 'red'
G.add_edge('mediaserver','mmi')
G.edge['mediaserver']['mmi']['write-read'] = '[open open][write read][append read]'
G.add_edge('mediaserver','qcks')
G.edge['mediaserver']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][append read]'
G.add_edge('mediaserver','qlogd')
G.edge['mediaserver']['qlogd']['write-read'] = '[write read][add_name search][open open][append read]'
G.add_edge('mediaserver','qmuxd')
G.edge['mediaserver']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][append read]'
G.add_edge('mediaserver','qmuxd')
G.edge['mediaserver']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][append read][write read]'
G.edge['mediaserver']['qmuxd']['fill'] = 'red'
G.add_edge('mediaserver','qmuxd')
G.edge['mediaserver']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][append read][write read][append read]'
G.add_edge('mediaserver','rfs_access')
G.edge['mediaserver']['rfs_access']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['mediaserver']['rfs_access']['fill'] = 'red'
G.add_edge('mediaserver','rfs_access')
G.edge['mediaserver']['rfs_access']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('mediaserver','rild')
G.edge['mediaserver']['rild']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read]'
G.edge['mediaserver']['rild']['fill'] = 'red'
G.add_edge('mediaserver','rild')
G.edge['mediaserver']['rild']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('mediaserver','rmt_storage')
G.edge['mediaserver']['rmt_storage']['write-read'] = '[open open][write read]'
G.edge['mediaserver']['rmt_storage']['fill'] = 'red'
G.add_edge('mediaserver','rmt_storage')
G.edge['mediaserver']['rmt_storage']['write-read'] = '[open open][write read][append read]'
G.add_edge('mediaserver','sec-ril')
G.edge['mediaserver']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read]'
G.edge['mediaserver']['sec-ril']['fill'] = 'red'
G.add_edge('mediaserver','sensors')
G.edge['mediaserver']['sensors']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['mediaserver']['sensors']['fill'] = 'red'
G.add_edge('mediaserver','sensors')
G.edge['mediaserver']['sensors']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('mediaserver','system_server')
G.edge['mediaserver']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][write read][append read][open open][write read]'
G.edge['mediaserver']['system_server']['fill'] = 'red'
G.add_edge('mediaserver','system_server')
G.edge['mediaserver']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('mediaserver','tsdaemon')
G.edge['mediaserver']['tsdaemon']['write-read'] = '[write read]'
G.edge['mediaserver']['tsdaemon']['fill'] = 'red'
G.add_edge('mediaserver','vdc')
G.edge['mediaserver']['vdc']['write-read'] = '[write read]'
G.edge['mediaserver']['vdc']['fill'] = 'red'
G.add_edge('mediaserver','vm_bms')
G.edge['mediaserver']['vm_bms']['write-read'] = '[open open][write read]'
G.edge['mediaserver']['vm_bms']['fill'] = 'red'
G.add_edge('mediaserver','vm_bms')
G.edge['mediaserver']['vm_bms']['write-read'] = '[open open][write read][append read]'
G.add_edge('mediaserver','vold')
G.edge['mediaserver']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][append read][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read]'
G.edge['mediaserver']['vold']['fill'] = 'red'
G.add_edge('mediaserver','vold')
G.edge['mediaserver']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][append read][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('mediaserver','vpnclientd')
G.edge['mediaserver']['vpnclientd']['write-read'] = '[write read]'
G.edge['mediaserver']['vpnclientd']['fill'] = 'red'
G.add_edge('mmi','at_distributor')
G.edge['mmi']['at_distributor']['write-read'] = '[open open]'
G.add_edge('mmi','bluetooth')
G.edge['mmi']['bluetooth']['write-read'] = '[open open]'
G.add_edge('mmi','cellgeofenced')
G.edge['mmi']['cellgeofenced']['write-read'] = '[open open]'
G.add_edge('mmi','charger_monitor')
G.edge['mmi']['charger_monitor']['write-read'] = '[open open]'
G.add_edge('mmi','cnd')
G.edge['mmi']['cnd']['write-read'] = '[open open]'
G.add_edge('mmi','connfwexe')
G.edge['mmi']['connfwexe']['write-read'] = '[open open]'
G.add_edge('mmi','dpmd')
G.edge['mmi']['dpmd']['write-read'] = '[open open]'
G.add_edge('mmi','healthd')
G.edge['mmi']['healthd']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('mmi','imsd')
G.edge['mmi']['imsd']['write-read'] = '[open open]'
G.add_edge('mmi','ks')
G.edge['mmi']['ks']['write-read'] = '[open open]'
G.add_edge('mmi','lhd')
G.edge['mmi']['lhd']['write-read'] = '[open open]'
G.add_edge('mmi','mdm_helper')
G.edge['mmi']['mdm_helper']['write-read'] = '[open open]'
G.add_edge('mmi','mediaserver')
G.edge['mmi']['mediaserver']['write-read'] = '[open open]'
G.add_edge('mmi','mmi')
G.edge['mmi']['mmi']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('mmi','qcks')
G.edge['mmi']['qcks']['write-read'] = '[open open]'
G.add_edge('mmi','qlogd')
G.edge['mmi']['qlogd']['write-read'] = '[open open]'
G.add_edge('mmi','qmuxd')
G.edge['mmi']['qmuxd']['write-read'] = '[open open]'
G.add_edge('mmi','qmuxd')
G.edge['mmi']['qmuxd']['write-read'] = '[open open][open open]'
G.add_edge('mmi','rfs_access')
G.edge['mmi']['rfs_access']['write-read'] = '[open open]'
G.add_edge('mmi','rild')
G.edge['mmi']['rild']['write-read'] = '[open open]'
G.add_edge('mmi','rmt_storage')
G.edge['mmi']['rmt_storage']['write-read'] = '[open open]'
G.add_edge('mmi','sec-ril')
G.edge['mmi']['sec-ril']['write-read'] = '[open open]'
G.add_edge('mmi','sensors')
G.edge['mmi']['sensors']['write-read'] = '[open open]'
G.add_edge('mmi','system_server')
G.edge['mmi']['system_server']['write-read'] = '[open open]'
G.add_edge('mmi','vm_bms')
G.edge['mmi']['vm_bms']['write-read'] = '[open open]'
G.add_edge('mmi','vold')
G.edge['mmi']['vold']['write-read'] = '[open open]'
G.add_edge('mmi','at_distributor')
G.edge['mmi']['at_distributor']['write-read'] = '[open open][write read]'
G.edge['mmi']['at_distributor']['fill'] = 'red'
G.add_edge('mmi','at_distributor')
G.edge['mmi']['at_distributor']['write-read'] = '[open open][write read][append read]'
G.add_edge('mmi','bluetooth')
G.edge['mmi']['bluetooth']['write-read'] = '[open open][write read]'
G.edge['mmi']['bluetooth']['fill'] = 'red'
G.add_edge('mmi','bluetooth')
G.edge['mmi']['bluetooth']['write-read'] = '[open open][write read][append read]'
G.add_edge('mmi','cellgeofenced')
G.edge['mmi']['cellgeofenced']['write-read'] = '[open open][write read]'
G.edge['mmi']['cellgeofenced']['fill'] = 'red'
G.add_edge('mmi','cellgeofenced')
G.edge['mmi']['cellgeofenced']['write-read'] = '[open open][write read][append read]'
G.add_edge('mmi','charger_monitor')
G.edge['mmi']['charger_monitor']['write-read'] = '[open open][write read]'
G.edge['mmi']['charger_monitor']['fill'] = 'red'
G.add_edge('mmi','charger_monitor')
G.edge['mmi']['charger_monitor']['write-read'] = '[open open][write read][append read]'
G.add_edge('mmi','cnd')
G.edge['mmi']['cnd']['write-read'] = '[open open][append read]'
G.add_edge('mmi','connfwexe')
G.edge['mmi']['connfwexe']['write-read'] = '[open open][write read]'
G.edge['mmi']['connfwexe']['fill'] = 'red'
G.add_edge('mmi','connfwexe')
G.edge['mmi']['connfwexe']['write-read'] = '[open open][write read][append read]'
G.add_edge('mmi','daemon_app_process')
G.edge['mmi']['daemon_app_process']['write-read'] = '[write read]'
G.edge['mmi']['daemon_app_process']['fill'] = 'red'
G.add_edge('mmi','dpmd')
G.edge['mmi']['dpmd']['write-read'] = '[open open][write read]'
G.edge['mmi']['dpmd']['fill'] = 'red'
G.add_edge('mmi','dpmd')
G.edge['mmi']['dpmd']['write-read'] = '[open open][write read][append read]'
G.add_edge('mmi','healthd')
G.edge['mmi']['healthd']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['mmi']['healthd']['fill'] = 'red'
G.add_edge('mmi','healthd')
G.edge['mmi']['healthd']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('mmi','imsd')
G.edge['mmi']['imsd']['write-read'] = '[open open][write read]'
G.edge['mmi']['imsd']['fill'] = 'red'
G.add_edge('mmi','imsd')
G.edge['mmi']['imsd']['write-read'] = '[open open][write read][append read]'
G.add_edge('mmi','ks')
G.edge['mmi']['ks']['write-read'] = '[open open][append read]'
G.add_edge('mmi','lhd')
G.edge['mmi']['lhd']['write-read'] = '[open open][write read]'
G.edge['mmi']['lhd']['fill'] = 'red'
G.add_edge('mmi','lhd')
G.edge['mmi']['lhd']['write-read'] = '[open open][write read][append read]'
G.add_edge('mmi','mdm_helper')
G.edge['mmi']['mdm_helper']['write-read'] = '[open open][append read]'
G.add_edge('mmi','mediaserver')
G.edge['mmi']['mediaserver']['write-read'] = '[open open][write read]'
G.edge['mmi']['mediaserver']['fill'] = 'red'
G.add_edge('mmi','mediaserver')
G.edge['mmi']['mediaserver']['write-read'] = '[open open][write read][append read]'
G.add_edge('mmi','mmi')
G.edge['mmi']['mmi']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['mmi']['mmi']['fill'] = 'red'
G.add_edge('mmi','mmi')
G.edge['mmi']['mmi']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('mmi','qcks')
G.edge['mmi']['qcks']['write-read'] = '[open open][append read]'
G.add_edge('mmi','qlogd')
G.edge['mmi']['qlogd']['write-read'] = '[open open][append read]'
G.add_edge('mmi','qmuxd')
G.edge['mmi']['qmuxd']['write-read'] = '[open open][open open][append read]'
G.add_edge('mmi','qmuxd')
G.edge['mmi']['qmuxd']['write-read'] = '[open open][open open][append read][write read]'
G.edge['mmi']['qmuxd']['fill'] = 'red'
G.add_edge('mmi','qmuxd')
G.edge['mmi']['qmuxd']['write-read'] = '[open open][open open][append read][write read][append read]'
G.add_edge('mmi','rfs_access')
G.edge['mmi']['rfs_access']['write-read'] = '[open open][write read]'
G.edge['mmi']['rfs_access']['fill'] = 'red'
G.add_edge('mmi','rfs_access')
G.edge['mmi']['rfs_access']['write-read'] = '[open open][write read][append read]'
G.add_edge('mmi','rild')
G.edge['mmi']['rild']['write-read'] = '[open open][write read]'
G.edge['mmi']['rild']['fill'] = 'red'
G.add_edge('mmi','rild')
G.edge['mmi']['rild']['write-read'] = '[open open][write read][append read]'
G.add_edge('mmi','rmt_storage')
G.edge['mmi']['rmt_storage']['write-read'] = '[open open][write read]'
G.edge['mmi']['rmt_storage']['fill'] = 'red'
G.add_edge('mmi','rmt_storage')
G.edge['mmi']['rmt_storage']['write-read'] = '[open open][write read][append read]'
G.add_edge('mmi','sec-ril')
G.edge['mmi']['sec-ril']['write-read'] = '[open open][write read]'
G.edge['mmi']['sec-ril']['fill'] = 'red'
G.add_edge('mmi','sensors')
G.edge['mmi']['sensors']['write-read'] = '[open open][write read]'
G.edge['mmi']['sensors']['fill'] = 'red'
G.add_edge('mmi','sensors')
G.edge['mmi']['sensors']['write-read'] = '[open open][write read][append read]'
G.add_edge('mmi','system_server')
G.edge['mmi']['system_server']['write-read'] = '[open open][write read]'
G.edge['mmi']['system_server']['fill'] = 'red'
G.add_edge('mmi','system_server')
G.edge['mmi']['system_server']['write-read'] = '[open open][write read][append read]'
G.add_edge('mmi','tsdaemon')
G.edge['mmi']['tsdaemon']['write-read'] = '[write read]'
G.edge['mmi']['tsdaemon']['fill'] = 'red'
G.add_edge('mmi','vdc')
G.edge['mmi']['vdc']['write-read'] = '[write read]'
G.edge['mmi']['vdc']['fill'] = 'red'
G.add_edge('mmi','vm_bms')
G.edge['mmi']['vm_bms']['write-read'] = '[open open][write read]'
G.edge['mmi']['vm_bms']['fill'] = 'red'
G.add_edge('mmi','vm_bms')
G.edge['mmi']['vm_bms']['write-read'] = '[open open][write read][append read]'
G.add_edge('mmi','vold')
G.edge['mmi']['vold']['write-read'] = '[open open][write read]'
G.edge['mmi']['vold']['fill'] = 'red'
G.add_edge('mmi','vold')
G.edge['mmi']['vold']['write-read'] = '[open open][write read][append read]'
G.add_edge('mmi','vpnclientd')
G.edge['mmi']['vpnclientd']['write-read'] = '[write read]'
G.edge['mmi']['vpnclientd']['fill'] = 'red'
G.add_edge('qcks','at_distributor')
G.edge['qcks']['at_distributor']['write-read'] = '[open open][add_name search][remove_name search][open open]'
G.add_edge('qcks','bluetooth')
G.edge['qcks']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('qcks','cellgeofenced')
G.edge['qcks']['cellgeofenced']['write-read'] = '[open open]'
G.add_edge('qcks','charger_monitor')
G.edge['qcks']['charger_monitor']['write-read'] = '[open open]'
G.add_edge('qcks','cnd')
G.edge['qcks']['cnd']['write-read'] = '[open open][add_name search][remove_name search][open open]'
G.add_edge('qcks','connfwexe')
G.edge['qcks']['connfwexe']['write-read'] = '[open open][add_name search][remove_name search][open open]'
G.add_edge('qcks','dpmd')
G.edge['qcks']['dpmd']['write-read'] = '[open open]'
G.add_edge('qcks','healthd')
G.edge['qcks']['healthd']['write-read'] = '[open open]'
G.add_edge('qcks','imsd')
G.edge['qcks']['imsd']['write-read'] = '[open open]'
G.add_edge('qcks','ks')
G.edge['qcks']['ks']['write-read'] = '[open open][write read][add_name search][open open][write read][add_name search][open open]'
G.add_edge('qcks','lhd')
G.edge['qcks']['lhd']['write-read'] = '[open open][add_name search][remove_name search][open open]'
G.add_edge('qcks','mdm_helper')
G.edge['qcks']['mdm_helper']['write-read'] = '[write read][open open]'
G.add_edge('qcks','mediaserver')
G.edge['qcks']['mediaserver']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('qcks','mmi')
G.edge['qcks']['mmi']['write-read'] = '[open open]'
G.add_edge('qcks','qcks')
G.edge['qcks']['qcks']['write-read'] = '[open open][write read][append read][open open][add_name search][remove_name search][open open][write read][add_name search][write read][open open]'
G.add_edge('qcks','qlogd')
G.edge['qcks']['qlogd']['write-read'] = '[add_name search][open open]'
G.add_edge('qcks','qmuxd')
G.edge['qcks']['qmuxd']['write-read'] = '[open open]'
G.add_edge('qcks','qmuxd')
G.edge['qcks']['qmuxd']['write-read'] = '[open open][open open]'
G.add_edge('qcks','rfs_access')
G.edge['qcks']['rfs_access']['write-read'] = '[open open][add_name search][remove_name search][open open]'
G.add_edge('qcks','rild')
G.edge['qcks']['rild']['write-read'] = '[open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('qcks','rmt_storage')
G.edge['qcks']['rmt_storage']['write-read'] = '[open open]'
G.add_edge('qcks','sec-ril')
G.edge['qcks']['sec-ril']['write-read'] = '[open open][add_name search][remove_name search][open open]'
G.add_edge('qcks','sensors')
G.edge['qcks']['sensors']['write-read'] = '[open open][add_name search][remove_name search][open open]'
G.add_edge('qcks','system_server')
G.edge['qcks']['system_server']['write-read'] = '[open open][add_name search][remove_name search][open open]'
G.add_edge('qcks','vm_bms')
G.edge['qcks']['vm_bms']['write-read'] = '[open open]'
G.add_edge('qcks','vold')
G.edge['qcks']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('qcks','at_distributor')
G.edge['qcks']['at_distributor']['write-read'] = '[open open][add_name search][remove_name search][open open][write read]'
G.edge['qcks']['at_distributor']['fill'] = 'red'
G.add_edge('qcks','at_distributor')
G.edge['qcks']['at_distributor']['write-read'] = '[open open][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('qcks','bluetooth')
G.edge['qcks']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['qcks']['bluetooth']['fill'] = 'red'
G.add_edge('qcks','bluetooth')
G.edge['qcks']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('qcks','cellgeofenced')
G.edge['qcks']['cellgeofenced']['write-read'] = '[open open][write read]'
G.edge['qcks']['cellgeofenced']['fill'] = 'red'
G.add_edge('qcks','cellgeofenced')
G.edge['qcks']['cellgeofenced']['write-read'] = '[open open][write read][append read]'
G.add_edge('qcks','charger_monitor')
G.edge['qcks']['charger_monitor']['write-read'] = '[open open][write read]'
G.edge['qcks']['charger_monitor']['fill'] = 'red'
G.add_edge('qcks','charger_monitor')
G.edge['qcks']['charger_monitor']['write-read'] = '[open open][write read][append read]'
G.add_edge('qcks','cnd')
G.edge['qcks']['cnd']['write-read'] = '[open open][add_name search][remove_name search][open open][append read]'
G.add_edge('qcks','connfwexe')
G.edge['qcks']['connfwexe']['write-read'] = '[open open][add_name search][remove_name search][open open][write read]'
G.edge['qcks']['connfwexe']['fill'] = 'red'
G.add_edge('qcks','connfwexe')
G.edge['qcks']['connfwexe']['write-read'] = '[open open][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('qcks','daemon_app_process')
G.edge['qcks']['daemon_app_process']['write-read'] = '[write read]'
G.edge['qcks']['daemon_app_process']['fill'] = 'red'
G.add_edge('qcks','dpmd')
G.edge['qcks']['dpmd']['write-read'] = '[open open][write read]'
G.edge['qcks']['dpmd']['fill'] = 'red'
G.add_edge('qcks','dpmd')
G.edge['qcks']['dpmd']['write-read'] = '[open open][write read][append read]'
G.add_edge('qcks','healthd')
G.edge['qcks']['healthd']['write-read'] = '[open open][write read]'
G.edge['qcks']['healthd']['fill'] = 'red'
G.add_edge('qcks','healthd')
G.edge['qcks']['healthd']['write-read'] = '[open open][write read][append read]'
G.add_edge('qcks','imsd')
G.edge['qcks']['imsd']['write-read'] = '[open open][write read]'
G.edge['qcks']['imsd']['fill'] = 'red'
G.add_edge('qcks','imsd')
G.edge['qcks']['imsd']['write-read'] = '[open open][write read][append read]'
G.add_edge('qcks','ks')
G.edge['qcks']['ks']['write-read'] = '[open open][write read][add_name search][open open][write read][add_name search][open open][append read]'
G.add_edge('qcks','lhd')
G.edge['qcks']['lhd']['write-read'] = '[open open][add_name search][remove_name search][open open][write read]'
G.edge['qcks']['lhd']['fill'] = 'red'
G.add_edge('qcks','lhd')
G.edge['qcks']['lhd']['write-read'] = '[open open][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('qcks','mdm_helper')
G.edge['qcks']['mdm_helper']['write-read'] = '[write read][open open][append read]'
G.add_edge('qcks','mediaserver')
G.edge['qcks']['mediaserver']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['qcks']['mediaserver']['fill'] = 'red'
G.add_edge('qcks','mediaserver')
G.edge['qcks']['mediaserver']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('qcks','mmi')
G.edge['qcks']['mmi']['write-read'] = '[open open][write read]'
G.edge['qcks']['mmi']['fill'] = 'red'
G.add_edge('qcks','mmi')
G.edge['qcks']['mmi']['write-read'] = '[open open][write read][append read]'
G.add_edge('qcks','qcks')
G.edge['qcks']['qcks']['write-read'] = '[open open][write read][append read][open open][add_name search][remove_name search][open open][write read][add_name search][write read][open open][append read]'
G.add_edge('qcks','qlogd')
G.edge['qcks']['qlogd']['write-read'] = '[add_name search][open open][append read]'
G.add_edge('qcks','qmuxd')
G.edge['qcks']['qmuxd']['write-read'] = '[open open][open open][append read]'
G.add_edge('qcks','qmuxd')
G.edge['qcks']['qmuxd']['write-read'] = '[open open][open open][append read][write read]'
G.edge['qcks']['qmuxd']['fill'] = 'red'
G.add_edge('qcks','qmuxd')
G.edge['qcks']['qmuxd']['write-read'] = '[open open][open open][append read][write read][append read]'
G.add_edge('qcks','rfs_access')
G.edge['qcks']['rfs_access']['write-read'] = '[open open][add_name search][remove_name search][open open][write read]'
G.edge['qcks']['rfs_access']['fill'] = 'red'
G.add_edge('qcks','rfs_access')
G.edge['qcks']['rfs_access']['write-read'] = '[open open][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('qcks','rild')
G.edge['qcks']['rild']['write-read'] = '[open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open][write read]'
G.edge['qcks']['rild']['fill'] = 'red'
G.add_edge('qcks','rild')
G.edge['qcks']['rild']['write-read'] = '[open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('qcks','rmt_storage')
G.edge['qcks']['rmt_storage']['write-read'] = '[open open][write read]'
G.edge['qcks']['rmt_storage']['fill'] = 'red'
G.add_edge('qcks','rmt_storage')
G.edge['qcks']['rmt_storage']['write-read'] = '[open open][write read][append read]'
G.add_edge('qcks','sec-ril')
G.edge['qcks']['sec-ril']['write-read'] = '[open open][add_name search][remove_name search][open open][write read]'
G.edge['qcks']['sec-ril']['fill'] = 'red'
G.add_edge('qcks','sensors')
G.edge['qcks']['sensors']['write-read'] = '[open open][add_name search][remove_name search][open open][write read]'
G.edge['qcks']['sensors']['fill'] = 'red'
G.add_edge('qcks','sensors')
G.edge['qcks']['sensors']['write-read'] = '[open open][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('qcks','system_server')
G.edge['qcks']['system_server']['write-read'] = '[open open][add_name search][remove_name search][open open][write read]'
G.edge['qcks']['system_server']['fill'] = 'red'
G.add_edge('qcks','system_server')
G.edge['qcks']['system_server']['write-read'] = '[open open][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('qcks','tsdaemon')
G.edge['qcks']['tsdaemon']['write-read'] = '[write read]'
G.edge['qcks']['tsdaemon']['fill'] = 'red'
G.add_edge('qcks','vdc')
G.edge['qcks']['vdc']['write-read'] = '[write read]'
G.edge['qcks']['vdc']['fill'] = 'red'
G.add_edge('qcks','vm_bms')
G.edge['qcks']['vm_bms']['write-read'] = '[open open][write read]'
G.edge['qcks']['vm_bms']['fill'] = 'red'
G.add_edge('qcks','vm_bms')
G.edge['qcks']['vm_bms']['write-read'] = '[open open][write read][append read]'
G.add_edge('qcks','vold')
G.edge['qcks']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['qcks']['vold']['fill'] = 'red'
G.add_edge('qcks','vold')
G.edge['qcks']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('qcks','vpnclientd')
G.edge['qcks']['vpnclientd']['write-read'] = '[write read]'
G.edge['qcks']['vpnclientd']['fill'] = 'red'
G.add_edge('qlogd','at_distributor')
G.edge['qlogd']['at_distributor']['write-read'] = '[open open]'
G.add_edge('qlogd','bluetooth')
G.edge['qlogd']['bluetooth']['write-read'] = '[open open]'
G.add_edge('qlogd','cellgeofenced')
G.edge['qlogd']['cellgeofenced']['write-read'] = '[open open]'
G.add_edge('qlogd','charger_monitor')
G.edge['qlogd']['charger_monitor']['write-read'] = '[open open]'
G.add_edge('qlogd','cnd')
G.edge['qlogd']['cnd']['write-read'] = '[open open]'
G.add_edge('qlogd','connfwexe')
G.edge['qlogd']['connfwexe']['write-read'] = '[open open]'
G.add_edge('qlogd','dpmd')
G.edge['qlogd']['dpmd']['write-read'] = '[open open]'
G.add_edge('qlogd','healthd')
G.edge['qlogd']['healthd']['write-read'] = '[write read][add_name search][remove_name search][open open]'
G.add_edge('qlogd','imsd')
G.edge['qlogd']['imsd']['write-read'] = '[open open]'
G.add_edge('qlogd','ks')
G.edge['qlogd']['ks']['write-read'] = '[open open]'
G.add_edge('qlogd','lhd')
G.edge['qlogd']['lhd']['write-read'] = '[open open]'
G.add_edge('qlogd','mdm_helper')
G.edge['qlogd']['mdm_helper']['write-read'] = '[open open]'
G.add_edge('qlogd','mediaserver')
G.edge['qlogd']['mediaserver']['write-read'] = '[open open]'
G.add_edge('qlogd','mmi')
G.edge['qlogd']['mmi']['write-read'] = '[open open]'
G.add_edge('qlogd','qcks')
G.edge['qlogd']['qcks']['write-read'] = '[open open]'
G.add_edge('qlogd','qlogd')
G.edge['qlogd']['qlogd']['write-read'] = '[open open][setattr getattr][write read][append read][setopt getopt][write read][open open]'
G.add_edge('qlogd','qmuxd')
G.edge['qlogd']['qmuxd']['write-read'] = '[open open]'
G.add_edge('qlogd','qmuxd')
G.edge['qlogd']['qmuxd']['write-read'] = '[open open][open open]'
G.add_edge('qlogd','rfs_access')
G.edge['qlogd']['rfs_access']['write-read'] = '[open open]'
G.add_edge('qlogd','rild')
G.edge['qlogd']['rild']['write-read'] = '[setopt getopt][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('qlogd','rmt_storage')
G.edge['qlogd']['rmt_storage']['write-read'] = '[open open]'
G.add_edge('qlogd','sec-ril')
G.edge['qlogd']['sec-ril']['write-read'] = '[open open]'
G.add_edge('qlogd','sensors')
G.edge['qlogd']['sensors']['write-read'] = '[open open]'
G.add_edge('qlogd','system_server')
G.edge['qlogd']['system_server']['write-read'] = '[setopt getopt][open open]'
G.add_edge('qlogd','vm_bms')
G.edge['qlogd']['vm_bms']['write-read'] = '[open open]'
G.add_edge('qlogd','vold')
G.edge['qlogd']['vold']['write-read'] = '[open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('qlogd','at_distributor')
G.edge['qlogd']['at_distributor']['write-read'] = '[open open][write read]'
G.edge['qlogd']['at_distributor']['fill'] = 'red'
G.add_edge('qlogd','at_distributor')
G.edge['qlogd']['at_distributor']['write-read'] = '[open open][write read][append read]'
G.add_edge('qlogd','bluetooth')
G.edge['qlogd']['bluetooth']['write-read'] = '[open open][write read]'
G.edge['qlogd']['bluetooth']['fill'] = 'red'
G.add_edge('qlogd','bluetooth')
G.edge['qlogd']['bluetooth']['write-read'] = '[open open][write read][append read]'
G.add_edge('qlogd','cellgeofenced')
G.edge['qlogd']['cellgeofenced']['write-read'] = '[open open][write read]'
G.edge['qlogd']['cellgeofenced']['fill'] = 'red'
G.add_edge('qlogd','cellgeofenced')
G.edge['qlogd']['cellgeofenced']['write-read'] = '[open open][write read][append read]'
G.add_edge('qlogd','charger_monitor')
G.edge['qlogd']['charger_monitor']['write-read'] = '[open open][write read]'
G.edge['qlogd']['charger_monitor']['fill'] = 'red'
G.add_edge('qlogd','charger_monitor')
G.edge['qlogd']['charger_monitor']['write-read'] = '[open open][write read][append read]'
G.add_edge('qlogd','cnd')
G.edge['qlogd']['cnd']['write-read'] = '[open open][append read]'
G.add_edge('qlogd','connfwexe')
G.edge['qlogd']['connfwexe']['write-read'] = '[open open][write read]'
G.edge['qlogd']['connfwexe']['fill'] = 'red'
G.add_edge('qlogd','connfwexe')
G.edge['qlogd']['connfwexe']['write-read'] = '[open open][write read][append read]'
G.add_edge('qlogd','daemon_app_process')
G.edge['qlogd']['daemon_app_process']['write-read'] = '[write read]'
G.edge['qlogd']['daemon_app_process']['fill'] = 'red'
G.add_edge('qlogd','dpmd')
G.edge['qlogd']['dpmd']['write-read'] = '[open open][write read]'
G.edge['qlogd']['dpmd']['fill'] = 'red'
G.add_edge('qlogd','dpmd')
G.edge['qlogd']['dpmd']['write-read'] = '[open open][write read][append read]'
G.add_edge('qlogd','healthd')
G.edge['qlogd']['healthd']['write-read'] = '[write read][add_name search][remove_name search][open open][write read]'
G.edge['qlogd']['healthd']['fill'] = 'red'
G.add_edge('qlogd','healthd')
G.edge['qlogd']['healthd']['write-read'] = '[write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('qlogd','imsd')
G.edge['qlogd']['imsd']['write-read'] = '[open open][write read]'
G.edge['qlogd']['imsd']['fill'] = 'red'
G.add_edge('qlogd','imsd')
G.edge['qlogd']['imsd']['write-read'] = '[open open][write read][append read]'
G.add_edge('qlogd','ks')
G.edge['qlogd']['ks']['write-read'] = '[open open][append read]'
G.add_edge('qlogd','lhd')
G.edge['qlogd']['lhd']['write-read'] = '[open open][write read]'
G.edge['qlogd']['lhd']['fill'] = 'red'
G.add_edge('qlogd','lhd')
G.edge['qlogd']['lhd']['write-read'] = '[open open][write read][append read]'
G.add_edge('qlogd','mdm_helper')
G.edge['qlogd']['mdm_helper']['write-read'] = '[open open][append read]'
G.add_edge('qlogd','mediaserver')
G.edge['qlogd']['mediaserver']['write-read'] = '[open open][write read]'
G.edge['qlogd']['mediaserver']['fill'] = 'red'
G.add_edge('qlogd','mediaserver')
G.edge['qlogd']['mediaserver']['write-read'] = '[open open][write read][append read]'
G.add_edge('qlogd','mmi')
G.edge['qlogd']['mmi']['write-read'] = '[open open][write read]'
G.edge['qlogd']['mmi']['fill'] = 'red'
G.add_edge('qlogd','mmi')
G.edge['qlogd']['mmi']['write-read'] = '[open open][write read][append read]'
G.add_edge('qlogd','qcks')
G.edge['qlogd']['qcks']['write-read'] = '[open open][append read]'
G.add_edge('qlogd','qlogd')
G.edge['qlogd']['qlogd']['write-read'] = '[open open][setattr getattr][write read][append read][setopt getopt][write read][open open][append read]'
G.add_edge('qlogd','qmuxd')
G.edge['qlogd']['qmuxd']['write-read'] = '[open open][open open][append read]'
G.add_edge('qlogd','qmuxd')
G.edge['qlogd']['qmuxd']['write-read'] = '[open open][open open][append read][write read]'
G.edge['qlogd']['qmuxd']['fill'] = 'red'
G.add_edge('qlogd','qmuxd')
G.edge['qlogd']['qmuxd']['write-read'] = '[open open][open open][append read][write read][append read]'
G.add_edge('qlogd','rfs_access')
G.edge['qlogd']['rfs_access']['write-read'] = '[open open][write read]'
G.edge['qlogd']['rfs_access']['fill'] = 'red'
G.add_edge('qlogd','rfs_access')
G.edge['qlogd']['rfs_access']['write-read'] = '[open open][write read][append read]'
G.add_edge('qlogd','rild')
G.edge['qlogd']['rild']['write-read'] = '[setopt getopt][open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['qlogd']['rild']['fill'] = 'red'
G.add_edge('qlogd','rild')
G.edge['qlogd']['rild']['write-read'] = '[setopt getopt][open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('qlogd','rmt_storage')
G.edge['qlogd']['rmt_storage']['write-read'] = '[open open][write read]'
G.edge['qlogd']['rmt_storage']['fill'] = 'red'
G.add_edge('qlogd','rmt_storage')
G.edge['qlogd']['rmt_storage']['write-read'] = '[open open][write read][append read]'
G.add_edge('qlogd','sec-ril')
G.edge['qlogd']['sec-ril']['write-read'] = '[open open][write read]'
G.edge['qlogd']['sec-ril']['fill'] = 'red'
G.add_edge('qlogd','sensors')
G.edge['qlogd']['sensors']['write-read'] = '[open open][write read]'
G.edge['qlogd']['sensors']['fill'] = 'red'
G.add_edge('qlogd','sensors')
G.edge['qlogd']['sensors']['write-read'] = '[open open][write read][append read]'
G.add_edge('qlogd','system_server')
G.edge['qlogd']['system_server']['write-read'] = '[setopt getopt][open open][write read]'
G.edge['qlogd']['system_server']['fill'] = 'red'
G.add_edge('qlogd','system_server')
G.edge['qlogd']['system_server']['write-read'] = '[setopt getopt][open open][write read][append read]'
G.add_edge('qlogd','tsdaemon')
G.edge['qlogd']['tsdaemon']['write-read'] = '[write read]'
G.edge['qlogd']['tsdaemon']['fill'] = 'red'
G.add_edge('qlogd','vdc')
G.edge['qlogd']['vdc']['write-read'] = '[write read]'
G.edge['qlogd']['vdc']['fill'] = 'red'
G.add_edge('qlogd','vm_bms')
G.edge['qlogd']['vm_bms']['write-read'] = '[open open][write read]'
G.edge['qlogd']['vm_bms']['fill'] = 'red'
G.add_edge('qlogd','vm_bms')
G.edge['qlogd']['vm_bms']['write-read'] = '[open open][write read][append read]'
G.add_edge('qlogd','vold')
G.edge['qlogd']['vold']['write-read'] = '[open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read]'
G.edge['qlogd']['vold']['fill'] = 'red'
G.add_edge('qlogd','vold')
G.edge['qlogd']['vold']['write-read'] = '[open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('qlogd','vpnclientd')
G.edge['qlogd']['vpnclientd']['write-read'] = '[write read]'
G.edge['qlogd']['vpnclientd']['fill'] = 'red'
G.add_edge('qmuxd','at_distributor')
G.edge['qmuxd']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('qmuxd','bluetooth')
G.edge['qmuxd']['bluetooth']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('qmuxd','cellgeofenced')
G.edge['qmuxd']['cellgeofenced']['write-read'] = '[open open]'
G.add_edge('qmuxd','charger_monitor')
G.edge['qmuxd']['charger_monitor']['write-read'] = '[open open]'
G.add_edge('qmuxd','cnd')
G.edge['qmuxd']['cnd']['write-read'] = '[open open][add_name search][remove_name search][open open]'
G.add_edge('qmuxd','connfwexe')
G.edge['qmuxd']['connfwexe']['write-read'] = '[open open]'
G.add_edge('qmuxd','dpmd')
G.edge['qmuxd']['dpmd']['write-read'] = '[open open]'
G.add_edge('qmuxd','healthd')
G.edge['qmuxd']['healthd']['write-read'] = '[open open]'
G.add_edge('qmuxd','imsd')
G.edge['qmuxd']['imsd']['write-read'] = '[open open]'
G.add_edge('qmuxd','ks')
G.edge['qmuxd']['ks']['write-read'] = '[open open]'
G.add_edge('qmuxd','lhd')
G.edge['qmuxd']['lhd']['write-read'] = '[open open]'
G.add_edge('qmuxd','mdm_helper')
G.edge['qmuxd']['mdm_helper']['write-read'] = '[open open]'
G.add_edge('qmuxd','mediaserver')
G.edge['qmuxd']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('qmuxd','mmi')
G.edge['qmuxd']['mmi']['write-read'] = '[open open]'
G.add_edge('qmuxd','qcks')
G.edge['qmuxd']['qcks']['write-read'] = '[open open]'
G.add_edge('qmuxd','qlogd')
G.edge['qmuxd']['qlogd']['write-read'] = '[open open]'
G.add_edge('qmuxd','qmuxd')
G.edge['qmuxd']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][add_name search][remove_name search][open open][add_name search][remove_name search][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open]'
G.add_edge('qmuxd','qmuxd')
G.edge['qmuxd']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][add_name search][remove_name search][open open][add_name search][remove_name search][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open]'
G.add_edge('qmuxd','rfs_access')
G.edge['qmuxd']['rfs_access']['write-read'] = '[open open]'
G.add_edge('qmuxd','rild')
G.edge['qmuxd']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open]'
G.add_edge('qmuxd','rmt_storage')
G.edge['qmuxd']['rmt_storage']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('qmuxd','sec-ril')
G.edge['qmuxd']['sec-ril']['write-read'] = '[add_name search][open open]'
G.add_edge('qmuxd','sensors')
G.edge['qmuxd']['sensors']['write-read'] = '[add_name search][open open][write read][append read][open open]'
G.add_edge('qmuxd','system_server')
G.edge['qmuxd']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][open open]'
G.add_edge('qmuxd','vm_bms')
G.edge['qmuxd']['vm_bms']['write-read'] = '[open open]'
G.add_edge('qmuxd','vold')
G.edge['qmuxd']['vold']['write-read'] = '[open open]'
G.add_edge('qmuxd','at_distributor')
G.edge['qmuxd']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['qmuxd']['at_distributor']['fill'] = 'red'
G.add_edge('qmuxd','at_distributor')
G.edge['qmuxd']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('qmuxd','bluetooth')
G.edge['qmuxd']['bluetooth']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['qmuxd']['bluetooth']['fill'] = 'red'
G.add_edge('qmuxd','bluetooth')
G.edge['qmuxd']['bluetooth']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('qmuxd','cellgeofenced')
G.edge['qmuxd']['cellgeofenced']['write-read'] = '[open open][write read]'
G.edge['qmuxd']['cellgeofenced']['fill'] = 'red'
G.add_edge('qmuxd','cellgeofenced')
G.edge['qmuxd']['cellgeofenced']['write-read'] = '[open open][write read][append read]'
G.add_edge('qmuxd','charger_monitor')
G.edge['qmuxd']['charger_monitor']['write-read'] = '[open open][write read]'
G.edge['qmuxd']['charger_monitor']['fill'] = 'red'
G.add_edge('qmuxd','charger_monitor')
G.edge['qmuxd']['charger_monitor']['write-read'] = '[open open][write read][append read]'
G.add_edge('qmuxd','cnd')
G.edge['qmuxd']['cnd']['write-read'] = '[open open][add_name search][remove_name search][open open][append read]'
G.add_edge('qmuxd','connfwexe')
G.edge['qmuxd']['connfwexe']['write-read'] = '[open open][write read]'
G.edge['qmuxd']['connfwexe']['fill'] = 'red'
G.add_edge('qmuxd','connfwexe')
G.edge['qmuxd']['connfwexe']['write-read'] = '[open open][write read][append read]'
G.add_edge('qmuxd','daemon_app_process')
G.edge['qmuxd']['daemon_app_process']['write-read'] = '[write read]'
G.edge['qmuxd']['daemon_app_process']['fill'] = 'red'
G.add_edge('qmuxd','dpmd')
G.edge['qmuxd']['dpmd']['write-read'] = '[open open][write read]'
G.edge['qmuxd']['dpmd']['fill'] = 'red'
G.add_edge('qmuxd','dpmd')
G.edge['qmuxd']['dpmd']['write-read'] = '[open open][write read][append read]'
G.add_edge('qmuxd','healthd')
G.edge['qmuxd']['healthd']['write-read'] = '[open open][write read]'
G.edge['qmuxd']['healthd']['fill'] = 'red'
G.add_edge('qmuxd','healthd')
G.edge['qmuxd']['healthd']['write-read'] = '[open open][write read][append read]'
G.add_edge('qmuxd','imsd')
G.edge['qmuxd']['imsd']['write-read'] = '[open open][write read]'
G.edge['qmuxd']['imsd']['fill'] = 'red'
G.add_edge('qmuxd','imsd')
G.edge['qmuxd']['imsd']['write-read'] = '[open open][write read][append read]'
G.add_edge('qmuxd','ks')
G.edge['qmuxd']['ks']['write-read'] = '[open open][append read]'
G.add_edge('qmuxd','lhd')
G.edge['qmuxd']['lhd']['write-read'] = '[open open][write read]'
G.edge['qmuxd']['lhd']['fill'] = 'red'
G.add_edge('qmuxd','lhd')
G.edge['qmuxd']['lhd']['write-read'] = '[open open][write read][append read]'
G.add_edge('qmuxd','mdm_helper')
G.edge['qmuxd']['mdm_helper']['write-read'] = '[open open][append read]'
G.add_edge('qmuxd','mediaserver')
G.edge['qmuxd']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read]'
G.edge['qmuxd']['mediaserver']['fill'] = 'red'
G.add_edge('qmuxd','mediaserver')
G.edge['qmuxd']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('qmuxd','mmi')
G.edge['qmuxd']['mmi']['write-read'] = '[open open][write read]'
G.edge['qmuxd']['mmi']['fill'] = 'red'
G.add_edge('qmuxd','mmi')
G.edge['qmuxd']['mmi']['write-read'] = '[open open][write read][append read]'
G.add_edge('qmuxd','qcks')
G.edge['qmuxd']['qcks']['write-read'] = '[open open][append read]'
G.add_edge('qmuxd','qlogd')
G.edge['qmuxd']['qlogd']['write-read'] = '[open open][append read]'
G.add_edge('qmuxd','qmuxd')
G.edge['qmuxd']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][add_name search][remove_name search][open open][add_name search][remove_name search][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][append read]'
G.add_edge('qmuxd','qmuxd')
G.edge['qmuxd']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][add_name search][remove_name search][open open][add_name search][remove_name search][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][append read][write read]'
G.edge['qmuxd']['qmuxd']['fill'] = 'red'
G.add_edge('qmuxd','qmuxd')
G.edge['qmuxd']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][add_name search][remove_name search][open open][add_name search][remove_name search][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][append read][write read][append read]'
G.add_edge('qmuxd','rfs_access')
G.edge['qmuxd']['rfs_access']['write-read'] = '[open open][write read]'
G.edge['qmuxd']['rfs_access']['fill'] = 'red'
G.add_edge('qmuxd','rfs_access')
G.edge['qmuxd']['rfs_access']['write-read'] = '[open open][write read][append read]'
G.add_edge('qmuxd','rild')
G.edge['qmuxd']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read]'
G.edge['qmuxd']['rild']['fill'] = 'red'
G.add_edge('qmuxd','rild')
G.edge['qmuxd']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('qmuxd','rmt_storage')
G.edge['qmuxd']['rmt_storage']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['qmuxd']['rmt_storage']['fill'] = 'red'
G.add_edge('qmuxd','rmt_storage')
G.edge['qmuxd']['rmt_storage']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('qmuxd','sec-ril')
G.edge['qmuxd']['sec-ril']['write-read'] = '[add_name search][open open][write read]'
G.edge['qmuxd']['sec-ril']['fill'] = 'red'
G.add_edge('qmuxd','sensors')
G.edge['qmuxd']['sensors']['write-read'] = '[add_name search][open open][write read][append read][open open][write read]'
G.edge['qmuxd']['sensors']['fill'] = 'red'
G.add_edge('qmuxd','sensors')
G.edge['qmuxd']['sensors']['write-read'] = '[add_name search][open open][write read][append read][open open][write read][append read]'
G.add_edge('qmuxd','system_server')
G.edge['qmuxd']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][open open][write read]'
G.edge['qmuxd']['system_server']['fill'] = 'red'
G.add_edge('qmuxd','system_server')
G.edge['qmuxd']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('qmuxd','tsdaemon')
G.edge['qmuxd']['tsdaemon']['write-read'] = '[write read]'
G.edge['qmuxd']['tsdaemon']['fill'] = 'red'
G.add_edge('qmuxd','vdc')
G.edge['qmuxd']['vdc']['write-read'] = '[write read]'
G.edge['qmuxd']['vdc']['fill'] = 'red'
G.add_edge('qmuxd','vm_bms')
G.edge['qmuxd']['vm_bms']['write-read'] = '[open open][write read]'
G.edge['qmuxd']['vm_bms']['fill'] = 'red'
G.add_edge('qmuxd','vm_bms')
G.edge['qmuxd']['vm_bms']['write-read'] = '[open open][write read][append read]'
G.add_edge('qmuxd','vold')
G.edge['qmuxd']['vold']['write-read'] = '[open open][write read]'
G.edge['qmuxd']['vold']['fill'] = 'red'
G.add_edge('qmuxd','vold')
G.edge['qmuxd']['vold']['write-read'] = '[open open][write read][append read]'
G.add_edge('qmuxd','vpnclientd')
G.edge['qmuxd']['vpnclientd']['write-read'] = '[write read]'
G.edge['qmuxd']['vpnclientd']['fill'] = 'red'
G.add_edge('rfs_access','at_distributor')
G.edge['rfs_access']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('rfs_access','bluetooth')
G.edge['rfs_access']['bluetooth']['write-read'] = '[open open]'
G.add_edge('rfs_access','cellgeofenced')
G.edge['rfs_access']['cellgeofenced']['write-read'] = '[open open]'
G.add_edge('rfs_access','charger_monitor')
G.edge['rfs_access']['charger_monitor']['write-read'] = '[open open]'
G.add_edge('rfs_access','cnd')
G.edge['rfs_access']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open]'
G.add_edge('rfs_access','connfwexe')
G.edge['rfs_access']['connfwexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('rfs_access','dpmd')
G.edge['rfs_access']['dpmd']['write-read'] = '[open open]'
G.add_edge('rfs_access','healthd')
G.edge['rfs_access']['healthd']['write-read'] = '[open open]'
G.add_edge('rfs_access','imsd')
G.edge['rfs_access']['imsd']['write-read'] = '[open open]'
G.add_edge('rfs_access','ks')
G.edge['rfs_access']['ks']['write-read'] = '[open open]'
G.add_edge('rfs_access','lhd')
G.edge['rfs_access']['lhd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('rfs_access','mdm_helper')
G.edge['rfs_access']['mdm_helper']['write-read'] = '[open open]'
G.add_edge('rfs_access','mediaserver')
G.edge['rfs_access']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('rfs_access','mmi')
G.edge['rfs_access']['mmi']['write-read'] = '[open open]'
G.add_edge('rfs_access','qcks')
G.edge['rfs_access']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open]'
G.add_edge('rfs_access','qlogd')
G.edge['rfs_access']['qlogd']['write-read'] = '[write read][add_name search][open open]'
G.add_edge('rfs_access','qmuxd')
G.edge['rfs_access']['qmuxd']['write-read'] = '[open open]'
G.add_edge('rfs_access','qmuxd')
G.edge['rfs_access']['qmuxd']['write-read'] = '[open open][open open]'
G.add_edge('rfs_access','rfs_access')
G.edge['rfs_access']['rfs_access']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('rfs_access','rild')
G.edge['rfs_access']['rild']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('rfs_access','rmt_storage')
G.edge['rfs_access']['rmt_storage']['write-read'] = '[open open]'
G.add_edge('rfs_access','sec-ril')
G.edge['rfs_access']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('rfs_access','sensors')
G.edge['rfs_access']['sensors']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('rfs_access','system_server')
G.edge['rfs_access']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('rfs_access','vm_bms')
G.edge['rfs_access']['vm_bms']['write-read'] = '[open open]'
G.add_edge('rfs_access','vold')
G.edge['rfs_access']['vold']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('rfs_access','at_distributor')
G.edge['rfs_access']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['rfs_access']['at_distributor']['fill'] = 'red'
G.add_edge('rfs_access','at_distributor')
G.edge['rfs_access']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('rfs_access','bluetooth')
G.edge['rfs_access']['bluetooth']['write-read'] = '[open open][write read]'
G.edge['rfs_access']['bluetooth']['fill'] = 'red'
G.add_edge('rfs_access','bluetooth')
G.edge['rfs_access']['bluetooth']['write-read'] = '[open open][write read][append read]'
G.add_edge('rfs_access','cellgeofenced')
G.edge['rfs_access']['cellgeofenced']['write-read'] = '[open open][write read]'
G.edge['rfs_access']['cellgeofenced']['fill'] = 'red'
G.add_edge('rfs_access','cellgeofenced')
G.edge['rfs_access']['cellgeofenced']['write-read'] = '[open open][write read][append read]'
G.add_edge('rfs_access','charger_monitor')
G.edge['rfs_access']['charger_monitor']['write-read'] = '[open open][write read]'
G.edge['rfs_access']['charger_monitor']['fill'] = 'red'
G.add_edge('rfs_access','charger_monitor')
G.edge['rfs_access']['charger_monitor']['write-read'] = '[open open][write read][append read]'
G.add_edge('rfs_access','cnd')
G.edge['rfs_access']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][append read]'
G.add_edge('rfs_access','connfwexe')
G.edge['rfs_access']['connfwexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['rfs_access']['connfwexe']['fill'] = 'red'
G.add_edge('rfs_access','connfwexe')
G.edge['rfs_access']['connfwexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('rfs_access','daemon_app_process')
G.edge['rfs_access']['daemon_app_process']['write-read'] = '[write read]'
G.edge['rfs_access']['daemon_app_process']['fill'] = 'red'
G.add_edge('rfs_access','dpmd')
G.edge['rfs_access']['dpmd']['write-read'] = '[open open][write read]'
G.edge['rfs_access']['dpmd']['fill'] = 'red'
G.add_edge('rfs_access','dpmd')
G.edge['rfs_access']['dpmd']['write-read'] = '[open open][write read][append read]'
G.add_edge('rfs_access','healthd')
G.edge['rfs_access']['healthd']['write-read'] = '[open open][write read]'
G.edge['rfs_access']['healthd']['fill'] = 'red'
G.add_edge('rfs_access','healthd')
G.edge['rfs_access']['healthd']['write-read'] = '[open open][write read][append read]'
G.add_edge('rfs_access','imsd')
G.edge['rfs_access']['imsd']['write-read'] = '[open open][write read]'
G.edge['rfs_access']['imsd']['fill'] = 'red'
G.add_edge('rfs_access','imsd')
G.edge['rfs_access']['imsd']['write-read'] = '[open open][write read][append read]'
G.add_edge('rfs_access','ks')
G.edge['rfs_access']['ks']['write-read'] = '[open open][append read]'
G.add_edge('rfs_access','lhd')
G.edge['rfs_access']['lhd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['rfs_access']['lhd']['fill'] = 'red'
G.add_edge('rfs_access','lhd')
G.edge['rfs_access']['lhd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('rfs_access','mdm_helper')
G.edge['rfs_access']['mdm_helper']['write-read'] = '[open open][append read]'
G.add_edge('rfs_access','mediaserver')
G.edge['rfs_access']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['rfs_access']['mediaserver']['fill'] = 'red'
G.add_edge('rfs_access','mediaserver')
G.edge['rfs_access']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('rfs_access','mmi')
G.edge['rfs_access']['mmi']['write-read'] = '[open open][write read]'
G.edge['rfs_access']['mmi']['fill'] = 'red'
G.add_edge('rfs_access','mmi')
G.edge['rfs_access']['mmi']['write-read'] = '[open open][write read][append read]'
G.add_edge('rfs_access','qcks')
G.edge['rfs_access']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][append read]'
G.add_edge('rfs_access','qlogd')
G.edge['rfs_access']['qlogd']['write-read'] = '[write read][add_name search][open open][append read]'
G.add_edge('rfs_access','qmuxd')
G.edge['rfs_access']['qmuxd']['write-read'] = '[open open][open open][append read]'
G.add_edge('rfs_access','qmuxd')
G.edge['rfs_access']['qmuxd']['write-read'] = '[open open][open open][append read][write read]'
G.edge['rfs_access']['qmuxd']['fill'] = 'red'
G.add_edge('rfs_access','qmuxd')
G.edge['rfs_access']['qmuxd']['write-read'] = '[open open][open open][append read][write read][append read]'
G.add_edge('rfs_access','rfs_access')
G.edge['rfs_access']['rfs_access']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['rfs_access']['rfs_access']['fill'] = 'red'
G.add_edge('rfs_access','rfs_access')
G.edge['rfs_access']['rfs_access']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('rfs_access','rild')
G.edge['rfs_access']['rild']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read]'
G.edge['rfs_access']['rild']['fill'] = 'red'
G.add_edge('rfs_access','rild')
G.edge['rfs_access']['rild']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('rfs_access','rmt_storage')
G.edge['rfs_access']['rmt_storage']['write-read'] = '[open open][write read]'
G.edge['rfs_access']['rmt_storage']['fill'] = 'red'
G.add_edge('rfs_access','rmt_storage')
G.edge['rfs_access']['rmt_storage']['write-read'] = '[open open][write read][append read]'
G.add_edge('rfs_access','sec-ril')
G.edge['rfs_access']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['rfs_access']['sec-ril']['fill'] = 'red'
G.add_edge('rfs_access','sensors')
G.edge['rfs_access']['sensors']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['rfs_access']['sensors']['fill'] = 'red'
G.add_edge('rfs_access','sensors')
G.edge['rfs_access']['sensors']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('rfs_access','system_server')
G.edge['rfs_access']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['rfs_access']['system_server']['fill'] = 'red'
G.add_edge('rfs_access','system_server')
G.edge['rfs_access']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('rfs_access','tsdaemon')
G.edge['rfs_access']['tsdaemon']['write-read'] = '[write read]'
G.edge['rfs_access']['tsdaemon']['fill'] = 'red'
G.add_edge('rfs_access','vdc')
G.edge['rfs_access']['vdc']['write-read'] = '[write read]'
G.edge['rfs_access']['vdc']['fill'] = 'red'
G.add_edge('rfs_access','vm_bms')
G.edge['rfs_access']['vm_bms']['write-read'] = '[open open][write read]'
G.edge['rfs_access']['vm_bms']['fill'] = 'red'
G.add_edge('rfs_access','vm_bms')
G.edge['rfs_access']['vm_bms']['write-read'] = '[open open][write read][append read]'
G.add_edge('rfs_access','vold')
G.edge['rfs_access']['vold']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read]'
G.edge['rfs_access']['vold']['fill'] = 'red'
G.add_edge('rfs_access','vold')
G.edge['rfs_access']['vold']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('rfs_access','vpnclientd')
G.edge['rfs_access']['vpnclientd']['write-read'] = '[write read]'
G.edge['rfs_access']['vpnclientd']['fill'] = 'red'
G.add_edge('rild','at_distributor')
G.edge['rild']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('rild','bluetooth')
G.edge['rild']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('rild','cellgeofenced')
G.edge['rild']['cellgeofenced']['write-read'] = '[open open]'
G.add_edge('rild','charger_monitor')
G.edge['rild']['charger_monitor']['write-read'] = '[setopt getopt][open open]'
G.add_edge('rild','cnd')
G.edge['rild']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('rild','connfwexe')
G.edge['rild']['connfwexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open]'
G.add_edge('rild','dpmd')
G.edge['rild']['dpmd']['write-read'] = '[open open]'
G.add_edge('rild','healthd')
G.edge['rild']['healthd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][write read][add_name search][remove_name search][open open]'
G.add_edge('rild','imsd')
G.edge['rild']['imsd']['write-read'] = '[open open]'
G.add_edge('rild','ks')
G.edge['rild']['ks']['write-read'] = '[open open][write read][add_name search][open open]'
G.add_edge('rild','lhd')
G.edge['rild']['lhd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open]'
G.add_edge('rild','mdm_helper')
G.edge['rild']['mdm_helper']['write-read'] = '[write read][open open]'
G.add_edge('rild','mediaserver')
G.edge['rild']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('rild','mmi')
G.edge['rild']['mmi']['write-read'] = '[open open]'
G.add_edge('rild','qcks')
G.edge['rild']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open]'
G.add_edge('rild','qlogd')
G.edge['rild']['qlogd']['write-read'] = '[setopt getopt][write read][add_name search][write read][add_name search][add_name search][open open]'
G.add_edge('rild','qmuxd')
G.edge['rild']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('rild','qmuxd')
G.edge['rild']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][open open]'
G.add_edge('rild','rfs_access')
G.edge['rild']['rfs_access']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open]'
G.add_edge('rild','rild')
G.edge['rild']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][open open][setattr getattr][write read][append read][write read][append read][write read][append read][open open][open open][open open][setattr getattr][write read][append read][write read][append read][write read][append read][open open]'
G.add_edge('rild','rmt_storage')
G.edge['rild']['rmt_storage']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('rild','sec-ril')
G.edge['rild']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][add_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('rild','sensors')
G.edge['rild']['sensors']['write-read'] = '[add_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open]'
G.add_edge('rild','system_server')
G.edge['rild']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('rild','vm_bms')
G.edge['rild']['vm_bms']['write-read'] = '[open open]'
G.add_edge('rild','vold')
G.edge['rild']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('rild','at_distributor')
G.edge['rild']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['rild']['at_distributor']['fill'] = 'red'
G.add_edge('rild','at_distributor')
G.edge['rild']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('rild','bluetooth')
G.edge['rild']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['rild']['bluetooth']['fill'] = 'red'
G.add_edge('rild','bluetooth')
G.edge['rild']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('rild','cellgeofenced')
G.edge['rild']['cellgeofenced']['write-read'] = '[open open][write read]'
G.edge['rild']['cellgeofenced']['fill'] = 'red'
G.add_edge('rild','cellgeofenced')
G.edge['rild']['cellgeofenced']['write-read'] = '[open open][write read][append read]'
G.add_edge('rild','charger_monitor')
G.edge['rild']['charger_monitor']['write-read'] = '[setopt getopt][open open][write read]'
G.edge['rild']['charger_monitor']['fill'] = 'red'
G.add_edge('rild','charger_monitor')
G.edge['rild']['charger_monitor']['write-read'] = '[setopt getopt][open open][write read][append read]'
G.add_edge('rild','cnd')
G.edge['rild']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][append read]'
G.add_edge('rild','connfwexe')
G.edge['rild']['connfwexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read]'
G.edge['rild']['connfwexe']['fill'] = 'red'
G.add_edge('rild','connfwexe')
G.edge['rild']['connfwexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('rild','daemon_app_process')
G.edge['rild']['daemon_app_process']['write-read'] = '[write read]'
G.edge['rild']['daemon_app_process']['fill'] = 'red'
G.add_edge('rild','dpmd')
G.edge['rild']['dpmd']['write-read'] = '[open open][write read]'
G.edge['rild']['dpmd']['fill'] = 'red'
G.add_edge('rild','dpmd')
G.edge['rild']['dpmd']['write-read'] = '[open open][write read][append read]'
G.add_edge('rild','healthd')
G.edge['rild']['healthd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][write read][add_name search][remove_name search][open open][write read]'
G.edge['rild']['healthd']['fill'] = 'red'
G.add_edge('rild','healthd')
G.edge['rild']['healthd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('rild','imsd')
G.edge['rild']['imsd']['write-read'] = '[open open][write read]'
G.edge['rild']['imsd']['fill'] = 'red'
G.add_edge('rild','imsd')
G.edge['rild']['imsd']['write-read'] = '[open open][write read][append read]'
G.add_edge('rild','ks')
G.edge['rild']['ks']['write-read'] = '[open open][write read][add_name search][open open][append read]'
G.add_edge('rild','lhd')
G.edge['rild']['lhd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read]'
G.edge['rild']['lhd']['fill'] = 'red'
G.add_edge('rild','lhd')
G.edge['rild']['lhd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('rild','mdm_helper')
G.edge['rild']['mdm_helper']['write-read'] = '[write read][open open][append read]'
G.add_edge('rild','mediaserver')
G.edge['rild']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['rild']['mediaserver']['fill'] = 'red'
G.add_edge('rild','mediaserver')
G.edge['rild']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('rild','mmi')
G.edge['rild']['mmi']['write-read'] = '[open open][write read]'
G.edge['rild']['mmi']['fill'] = 'red'
G.add_edge('rild','mmi')
G.edge['rild']['mmi']['write-read'] = '[open open][write read][append read]'
G.add_edge('rild','qcks')
G.edge['rild']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][append read]'
G.add_edge('rild','qlogd')
G.edge['rild']['qlogd']['write-read'] = '[setopt getopt][write read][add_name search][write read][add_name search][add_name search][open open][append read]'
G.add_edge('rild','qmuxd')
G.edge['rild']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][open open][append read]'
G.add_edge('rild','qmuxd')
G.edge['rild']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][open open][append read][write read]'
G.edge['rild']['qmuxd']['fill'] = 'red'
G.add_edge('rild','qmuxd')
G.edge['rild']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][open open][append read][write read][append read]'
G.add_edge('rild','rfs_access')
G.edge['rild']['rfs_access']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read]'
G.edge['rild']['rfs_access']['fill'] = 'red'
G.add_edge('rild','rfs_access')
G.edge['rild']['rfs_access']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('rild','rild')
G.edge['rild']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][open open][setattr getattr][write read][append read][write read][append read][write read][append read][open open][open open][open open][setattr getattr][write read][append read][write read][append read][write read][append read][open open][write read]'
G.edge['rild']['rild']['fill'] = 'red'
G.add_edge('rild','rild')
G.edge['rild']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][open open][setattr getattr][write read][append read][write read][append read][write read][append read][open open][open open][open open][setattr getattr][write read][append read][write read][append read][write read][append read][open open][write read][append read]'
G.add_edge('rild','rmt_storage')
G.edge['rild']['rmt_storage']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['rild']['rmt_storage']['fill'] = 'red'
G.add_edge('rild','rmt_storage')
G.edge['rild']['rmt_storage']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('rild','sec-ril')
G.edge['rild']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][add_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['rild']['sec-ril']['fill'] = 'red'
G.add_edge('rild','sensors')
G.edge['rild']['sensors']['write-read'] = '[add_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read]'
G.edge['rild']['sensors']['fill'] = 'red'
G.add_edge('rild','sensors')
G.edge['rild']['sensors']['write-read'] = '[add_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('rild','system_server')
G.edge['rild']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['rild']['system_server']['fill'] = 'red'
G.add_edge('rild','system_server')
G.edge['rild']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('rild','tsdaemon')
G.edge['rild']['tsdaemon']['write-read'] = '[write read]'
G.edge['rild']['tsdaemon']['fill'] = 'red'
G.add_edge('rild','vdc')
G.edge['rild']['vdc']['write-read'] = '[write read]'
G.edge['rild']['vdc']['fill'] = 'red'
G.add_edge('rild','vm_bms')
G.edge['rild']['vm_bms']['write-read'] = '[open open][write read]'
G.edge['rild']['vm_bms']['fill'] = 'red'
G.add_edge('rild','vm_bms')
G.edge['rild']['vm_bms']['write-read'] = '[open open][write read][append read]'
G.add_edge('rild','vold')
G.edge['rild']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['rild']['vold']['fill'] = 'red'
G.add_edge('rild','vold')
G.edge['rild']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('rild','vpnclientd')
G.edge['rild']['vpnclientd']['write-read'] = '[write read]'
G.edge['rild']['vpnclientd']['fill'] = 'red'
G.add_edge('rmt_storage','at_distributor')
G.edge['rmt_storage']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('rmt_storage','bluetooth')
G.edge['rmt_storage']['bluetooth']['write-read'] = '[open open]'
G.add_edge('rmt_storage','cellgeofenced')
G.edge['rmt_storage']['cellgeofenced']['write-read'] = '[open open]'
G.add_edge('rmt_storage','charger_monitor')
G.edge['rmt_storage']['charger_monitor']['write-read'] = '[open open]'
G.add_edge('rmt_storage','cnd')
G.edge['rmt_storage']['cnd']['write-read'] = '[open open]'
G.add_edge('rmt_storage','connfwexe')
G.edge['rmt_storage']['connfwexe']['write-read'] = '[open open]'
G.add_edge('rmt_storage','dpmd')
G.edge['rmt_storage']['dpmd']['write-read'] = '[open open]'
G.add_edge('rmt_storage','healthd')
G.edge['rmt_storage']['healthd']['write-read'] = '[open open]'
G.add_edge('rmt_storage','imsd')
G.edge['rmt_storage']['imsd']['write-read'] = '[open open]'
G.add_edge('rmt_storage','ks')
G.edge['rmt_storage']['ks']['write-read'] = '[open open][write read][add_name search][open open]'
G.add_edge('rmt_storage','lhd')
G.edge['rmt_storage']['lhd']['write-read'] = '[open open]'
G.add_edge('rmt_storage','mdm_helper')
G.edge['rmt_storage']['mdm_helper']['write-read'] = '[write read][open open]'
G.add_edge('rmt_storage','mediaserver')
G.edge['rmt_storage']['mediaserver']['write-read'] = '[open open]'
G.add_edge('rmt_storage','mmi')
G.edge['rmt_storage']['mmi']['write-read'] = '[open open]'
G.add_edge('rmt_storage','qcks')
G.edge['rmt_storage']['qcks']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('rmt_storage','qlogd')
G.edge['rmt_storage']['qlogd']['write-read'] = '[open open]'
G.add_edge('rmt_storage','qmuxd')
G.edge['rmt_storage']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('rmt_storage','qmuxd')
G.edge['rmt_storage']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open]'
G.add_edge('rmt_storage','rfs_access')
G.edge['rmt_storage']['rfs_access']['write-read'] = '[open open]'
G.add_edge('rmt_storage','rild')
G.edge['rmt_storage']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('rmt_storage','rmt_storage')
G.edge['rmt_storage']['rmt_storage']['write-read'] = '[open open][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('rmt_storage','sec-ril')
G.edge['rmt_storage']['sec-ril']['write-read'] = '[open open]'
G.add_edge('rmt_storage','sensors')
G.edge['rmt_storage']['sensors']['write-read'] = '[add_name search][open open]'
G.add_edge('rmt_storage','system_server')
G.edge['rmt_storage']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open]'
G.add_edge('rmt_storage','vm_bms')
G.edge['rmt_storage']['vm_bms']['write-read'] = '[open open]'
G.add_edge('rmt_storage','vold')
G.edge['rmt_storage']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('rmt_storage','at_distributor')
G.edge['rmt_storage']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['rmt_storage']['at_distributor']['fill'] = 'red'
G.add_edge('rmt_storage','at_distributor')
G.edge['rmt_storage']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('rmt_storage','bluetooth')
G.edge['rmt_storage']['bluetooth']['write-read'] = '[open open][write read]'
G.edge['rmt_storage']['bluetooth']['fill'] = 'red'
G.add_edge('rmt_storage','bluetooth')
G.edge['rmt_storage']['bluetooth']['write-read'] = '[open open][write read][append read]'
G.add_edge('rmt_storage','cellgeofenced')
G.edge['rmt_storage']['cellgeofenced']['write-read'] = '[open open][write read]'
G.edge['rmt_storage']['cellgeofenced']['fill'] = 'red'
G.add_edge('rmt_storage','cellgeofenced')
G.edge['rmt_storage']['cellgeofenced']['write-read'] = '[open open][write read][append read]'
G.add_edge('rmt_storage','charger_monitor')
G.edge['rmt_storage']['charger_monitor']['write-read'] = '[open open][write read]'
G.edge['rmt_storage']['charger_monitor']['fill'] = 'red'
G.add_edge('rmt_storage','charger_monitor')
G.edge['rmt_storage']['charger_monitor']['write-read'] = '[open open][write read][append read]'
G.add_edge('rmt_storage','cnd')
G.edge['rmt_storage']['cnd']['write-read'] = '[open open][append read]'
G.add_edge('rmt_storage','connfwexe')
G.edge['rmt_storage']['connfwexe']['write-read'] = '[open open][write read]'
G.edge['rmt_storage']['connfwexe']['fill'] = 'red'
G.add_edge('rmt_storage','connfwexe')
G.edge['rmt_storage']['connfwexe']['write-read'] = '[open open][write read][append read]'
G.add_edge('rmt_storage','daemon_app_process')
G.edge['rmt_storage']['daemon_app_process']['write-read'] = '[write read]'
G.edge['rmt_storage']['daemon_app_process']['fill'] = 'red'
G.add_edge('rmt_storage','dpmd')
G.edge['rmt_storage']['dpmd']['write-read'] = '[open open][write read]'
G.edge['rmt_storage']['dpmd']['fill'] = 'red'
G.add_edge('rmt_storage','dpmd')
G.edge['rmt_storage']['dpmd']['write-read'] = '[open open][write read][append read]'
G.add_edge('rmt_storage','healthd')
G.edge['rmt_storage']['healthd']['write-read'] = '[open open][write read]'
G.edge['rmt_storage']['healthd']['fill'] = 'red'
G.add_edge('rmt_storage','healthd')
G.edge['rmt_storage']['healthd']['write-read'] = '[open open][write read][append read]'
G.add_edge('rmt_storage','imsd')
G.edge['rmt_storage']['imsd']['write-read'] = '[open open][write read]'
G.edge['rmt_storage']['imsd']['fill'] = 'red'
G.add_edge('rmt_storage','imsd')
G.edge['rmt_storage']['imsd']['write-read'] = '[open open][write read][append read]'
G.add_edge('rmt_storage','ks')
G.edge['rmt_storage']['ks']['write-read'] = '[open open][write read][add_name search][open open][append read]'
G.add_edge('rmt_storage','lhd')
G.edge['rmt_storage']['lhd']['write-read'] = '[open open][write read]'
G.edge['rmt_storage']['lhd']['fill'] = 'red'
G.add_edge('rmt_storage','lhd')
G.edge['rmt_storage']['lhd']['write-read'] = '[open open][write read][append read]'
G.add_edge('rmt_storage','mdm_helper')
G.edge['rmt_storage']['mdm_helper']['write-read'] = '[write read][open open][append read]'
G.add_edge('rmt_storage','mediaserver')
G.edge['rmt_storage']['mediaserver']['write-read'] = '[open open][write read]'
G.edge['rmt_storage']['mediaserver']['fill'] = 'red'
G.add_edge('rmt_storage','mediaserver')
G.edge['rmt_storage']['mediaserver']['write-read'] = '[open open][write read][append read]'
G.add_edge('rmt_storage','mmi')
G.edge['rmt_storage']['mmi']['write-read'] = '[open open][write read]'
G.edge['rmt_storage']['mmi']['fill'] = 'red'
G.add_edge('rmt_storage','mmi')
G.edge['rmt_storage']['mmi']['write-read'] = '[open open][write read][append read]'
G.add_edge('rmt_storage','qcks')
G.edge['rmt_storage']['qcks']['write-read'] = '[open open][write read][append read][open open][append read]'
G.add_edge('rmt_storage','qlogd')
G.edge['rmt_storage']['qlogd']['write-read'] = '[open open][append read]'
G.add_edge('rmt_storage','qmuxd')
G.edge['rmt_storage']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][append read]'
G.add_edge('rmt_storage','qmuxd')
G.edge['rmt_storage']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][append read][write read]'
G.edge['rmt_storage']['qmuxd']['fill'] = 'red'
G.add_edge('rmt_storage','qmuxd')
G.edge['rmt_storage']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][append read][write read][append read]'
G.add_edge('rmt_storage','rfs_access')
G.edge['rmt_storage']['rfs_access']['write-read'] = '[open open][write read]'
G.edge['rmt_storage']['rfs_access']['fill'] = 'red'
G.add_edge('rmt_storage','rfs_access')
G.edge['rmt_storage']['rfs_access']['write-read'] = '[open open][write read][append read]'
G.add_edge('rmt_storage','rild')
G.edge['rmt_storage']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['rmt_storage']['rild']['fill'] = 'red'
G.add_edge('rmt_storage','rild')
G.edge['rmt_storage']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('rmt_storage','rmt_storage')
G.edge['rmt_storage']['rmt_storage']['write-read'] = '[open open][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['rmt_storage']['rmt_storage']['fill'] = 'red'
G.add_edge('rmt_storage','rmt_storage')
G.edge['rmt_storage']['rmt_storage']['write-read'] = '[open open][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('rmt_storage','sec-ril')
G.edge['rmt_storage']['sec-ril']['write-read'] = '[open open][write read]'
G.edge['rmt_storage']['sec-ril']['fill'] = 'red'
G.add_edge('rmt_storage','sensors')
G.edge['rmt_storage']['sensors']['write-read'] = '[add_name search][open open][write read]'
G.edge['rmt_storage']['sensors']['fill'] = 'red'
G.add_edge('rmt_storage','sensors')
G.edge['rmt_storage']['sensors']['write-read'] = '[add_name search][open open][write read][append read]'
G.add_edge('rmt_storage','system_server')
G.edge['rmt_storage']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read]'
G.edge['rmt_storage']['system_server']['fill'] = 'red'
G.add_edge('rmt_storage','system_server')
G.edge['rmt_storage']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read]'
G.add_edge('rmt_storage','tsdaemon')
G.edge['rmt_storage']['tsdaemon']['write-read'] = '[write read]'
G.edge['rmt_storage']['tsdaemon']['fill'] = 'red'
G.add_edge('rmt_storage','vdc')
G.edge['rmt_storage']['vdc']['write-read'] = '[write read]'
G.edge['rmt_storage']['vdc']['fill'] = 'red'
G.add_edge('rmt_storage','vm_bms')
G.edge['rmt_storage']['vm_bms']['write-read'] = '[open open][write read]'
G.edge['rmt_storage']['vm_bms']['fill'] = 'red'
G.add_edge('rmt_storage','vm_bms')
G.edge['rmt_storage']['vm_bms']['write-read'] = '[open open][write read][append read]'
G.add_edge('rmt_storage','vold')
G.edge['rmt_storage']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['rmt_storage']['vold']['fill'] = 'red'
G.add_edge('rmt_storage','vold')
G.edge['rmt_storage']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('rmt_storage','vpnclientd')
G.edge['rmt_storage']['vpnclientd']['write-read'] = '[write read]'
G.edge['rmt_storage']['vpnclientd']['fill'] = 'red'
G.add_edge('sec-ril','at_distributor')
G.edge['sec-ril']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('sec-ril','bluetooth')
G.edge['sec-ril']['bluetooth']['write-read'] = '[open open]'
G.add_edge('sec-ril','cellgeofenced')
G.edge['sec-ril']['cellgeofenced']['write-read'] = '[open open]'
G.add_edge('sec-ril','charger_monitor')
G.edge['sec-ril']['charger_monitor']['write-read'] = '[open open]'
G.add_edge('sec-ril','cnd')
G.edge['sec-ril']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open]'
G.add_edge('sec-ril','connfwexe')
G.edge['sec-ril']['connfwexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('sec-ril','dpmd')
G.edge['sec-ril']['dpmd']['write-read'] = '[open open]'
G.add_edge('sec-ril','healthd')
G.edge['sec-ril']['healthd']['write-read'] = '[open open]'
G.add_edge('sec-ril','imsd')
G.edge['sec-ril']['imsd']['write-read'] = '[open open]'
G.add_edge('sec-ril','ks')
G.edge['sec-ril']['ks']['write-read'] = '[open open]'
G.add_edge('sec-ril','lhd')
G.edge['sec-ril']['lhd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('sec-ril','mdm_helper')
G.edge['sec-ril']['mdm_helper']['write-read'] = '[open open]'
G.add_edge('sec-ril','mediaserver')
G.edge['sec-ril']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('sec-ril','mmi')
G.edge['sec-ril']['mmi']['write-read'] = '[open open]'
G.add_edge('sec-ril','qcks')
G.edge['sec-ril']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open]'
G.add_edge('sec-ril','qlogd')
G.edge['sec-ril']['qlogd']['write-read'] = '[write read][add_name search][open open]'
G.add_edge('sec-ril','qmuxd')
G.edge['sec-ril']['qmuxd']['write-read'] = '[open open]'
G.add_edge('sec-ril','qmuxd')
G.edge['sec-ril']['qmuxd']['write-read'] = '[open open][open open]'
G.add_edge('sec-ril','rfs_access')
G.edge['sec-ril']['rfs_access']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('sec-ril','rild')
G.edge['sec-ril']['rild']['write-read'] = '[write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][open open][setattr getattr][write read][append read][write read][append read][write read][append read][open open]'
G.add_edge('sec-ril','rmt_storage')
G.edge['sec-ril']['rmt_storage']['write-read'] = '[open open]'
G.add_edge('sec-ril','sec-ril')
G.edge['sec-ril']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('sec-ril','sensors')
G.edge['sec-ril']['sensors']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('sec-ril','system_server')
G.edge['sec-ril']['system_server']['write-read'] = '[write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('sec-ril','vm_bms')
G.edge['sec-ril']['vm_bms']['write-read'] = '[open open]'
G.add_edge('sec-ril','vold')
G.edge['sec-ril']['vold']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('sec-ril','at_distributor')
G.edge['sec-ril']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['sec-ril']['at_distributor']['fill'] = 'red'
G.add_edge('sec-ril','at_distributor')
G.edge['sec-ril']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('sec-ril','bluetooth')
G.edge['sec-ril']['bluetooth']['write-read'] = '[open open][write read]'
G.edge['sec-ril']['bluetooth']['fill'] = 'red'
G.add_edge('sec-ril','bluetooth')
G.edge['sec-ril']['bluetooth']['write-read'] = '[open open][write read][append read]'
G.add_edge('sec-ril','cellgeofenced')
G.edge['sec-ril']['cellgeofenced']['write-read'] = '[open open][write read]'
G.edge['sec-ril']['cellgeofenced']['fill'] = 'red'
G.add_edge('sec-ril','cellgeofenced')
G.edge['sec-ril']['cellgeofenced']['write-read'] = '[open open][write read][append read]'
G.add_edge('sec-ril','charger_monitor')
G.edge['sec-ril']['charger_monitor']['write-read'] = '[open open][write read]'
G.edge['sec-ril']['charger_monitor']['fill'] = 'red'
G.add_edge('sec-ril','charger_monitor')
G.edge['sec-ril']['charger_monitor']['write-read'] = '[open open][write read][append read]'
G.add_edge('sec-ril','cnd')
G.edge['sec-ril']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][append read]'
G.add_edge('sec-ril','connfwexe')
G.edge['sec-ril']['connfwexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['sec-ril']['connfwexe']['fill'] = 'red'
G.add_edge('sec-ril','connfwexe')
G.edge['sec-ril']['connfwexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('sec-ril','daemon_app_process')
G.edge['sec-ril']['daemon_app_process']['write-read'] = '[write read]'
G.edge['sec-ril']['daemon_app_process']['fill'] = 'red'
G.add_edge('sec-ril','dpmd')
G.edge['sec-ril']['dpmd']['write-read'] = '[open open][write read]'
G.edge['sec-ril']['dpmd']['fill'] = 'red'
G.add_edge('sec-ril','dpmd')
G.edge['sec-ril']['dpmd']['write-read'] = '[open open][write read][append read]'
G.add_edge('sec-ril','healthd')
G.edge['sec-ril']['healthd']['write-read'] = '[open open][write read]'
G.edge['sec-ril']['healthd']['fill'] = 'red'
G.add_edge('sec-ril','healthd')
G.edge['sec-ril']['healthd']['write-read'] = '[open open][write read][append read]'
G.add_edge('sec-ril','imsd')
G.edge['sec-ril']['imsd']['write-read'] = '[open open][write read]'
G.edge['sec-ril']['imsd']['fill'] = 'red'
G.add_edge('sec-ril','imsd')
G.edge['sec-ril']['imsd']['write-read'] = '[open open][write read][append read]'
G.add_edge('sec-ril','ks')
G.edge['sec-ril']['ks']['write-read'] = '[open open][append read]'
G.add_edge('sec-ril','lhd')
G.edge['sec-ril']['lhd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['sec-ril']['lhd']['fill'] = 'red'
G.add_edge('sec-ril','lhd')
G.edge['sec-ril']['lhd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('sec-ril','mdm_helper')
G.edge['sec-ril']['mdm_helper']['write-read'] = '[open open][append read]'
G.add_edge('sec-ril','mediaserver')
G.edge['sec-ril']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['sec-ril']['mediaserver']['fill'] = 'red'
G.add_edge('sec-ril','mediaserver')
G.edge['sec-ril']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('sec-ril','mmi')
G.edge['sec-ril']['mmi']['write-read'] = '[open open][write read]'
G.edge['sec-ril']['mmi']['fill'] = 'red'
G.add_edge('sec-ril','mmi')
G.edge['sec-ril']['mmi']['write-read'] = '[open open][write read][append read]'
G.add_edge('sec-ril','qcks')
G.edge['sec-ril']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][append read]'
G.add_edge('sec-ril','qlogd')
G.edge['sec-ril']['qlogd']['write-read'] = '[write read][add_name search][open open][append read]'
G.add_edge('sec-ril','qmuxd')
G.edge['sec-ril']['qmuxd']['write-read'] = '[open open][open open][append read]'
G.add_edge('sec-ril','qmuxd')
G.edge['sec-ril']['qmuxd']['write-read'] = '[open open][open open][append read][write read]'
G.edge['sec-ril']['qmuxd']['fill'] = 'red'
G.add_edge('sec-ril','qmuxd')
G.edge['sec-ril']['qmuxd']['write-read'] = '[open open][open open][append read][write read][append read]'
G.add_edge('sec-ril','rfs_access')
G.edge['sec-ril']['rfs_access']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['sec-ril']['rfs_access']['fill'] = 'red'
G.add_edge('sec-ril','rfs_access')
G.edge['sec-ril']['rfs_access']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('sec-ril','rild')
G.edge['sec-ril']['rild']['write-read'] = '[write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][open open][setattr getattr][write read][append read][write read][append read][write read][append read][open open][write read]'
G.edge['sec-ril']['rild']['fill'] = 'red'
G.add_edge('sec-ril','rild')
G.edge['sec-ril']['rild']['write-read'] = '[write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][open open][setattr getattr][write read][append read][write read][append read][write read][append read][open open][write read][append read]'
G.add_edge('sec-ril','rmt_storage')
G.edge['sec-ril']['rmt_storage']['write-read'] = '[open open][write read]'
G.edge['sec-ril']['rmt_storage']['fill'] = 'red'
G.add_edge('sec-ril','rmt_storage')
G.edge['sec-ril']['rmt_storage']['write-read'] = '[open open][write read][append read]'
G.add_edge('sec-ril','sec-ril')
G.edge['sec-ril']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['sec-ril']['sec-ril']['fill'] = 'red'
G.add_edge('sec-ril','sensors')
G.edge['sec-ril']['sensors']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['sec-ril']['sensors']['fill'] = 'red'
G.add_edge('sec-ril','sensors')
G.edge['sec-ril']['sensors']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('sec-ril','system_server')
G.edge['sec-ril']['system_server']['write-read'] = '[write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['sec-ril']['system_server']['fill'] = 'red'
G.add_edge('sec-ril','system_server')
G.edge['sec-ril']['system_server']['write-read'] = '[write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('sec-ril','tsdaemon')
G.edge['sec-ril']['tsdaemon']['write-read'] = '[write read]'
G.edge['sec-ril']['tsdaemon']['fill'] = 'red'
G.add_edge('sec-ril','vdc')
G.edge['sec-ril']['vdc']['write-read'] = '[write read]'
G.edge['sec-ril']['vdc']['fill'] = 'red'
G.add_edge('sec-ril','vm_bms')
G.edge['sec-ril']['vm_bms']['write-read'] = '[open open][write read]'
G.edge['sec-ril']['vm_bms']['fill'] = 'red'
G.add_edge('sec-ril','vm_bms')
G.edge['sec-ril']['vm_bms']['write-read'] = '[open open][write read][append read]'
G.add_edge('sec-ril','vold')
G.edge['sec-ril']['vold']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['sec-ril']['vold']['fill'] = 'red'
G.add_edge('sec-ril','vold')
G.edge['sec-ril']['vold']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('sec-ril','vpnclientd')
G.edge['sec-ril']['vpnclientd']['write-read'] = '[write read]'
G.edge['sec-ril']['vpnclientd']['fill'] = 'red'
G.add_edge('sensors','at_distributor')
G.edge['sensors']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('sensors','bluetooth')
G.edge['sensors']['bluetooth']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('sensors','cellgeofenced')
G.edge['sensors']['cellgeofenced']['write-read'] = '[open open]'
G.add_edge('sensors','charger_monitor')
G.edge['sensors']['charger_monitor']['write-read'] = '[open open]'
G.add_edge('sensors','cnd')
G.edge['sensors']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open]'
G.add_edge('sensors','connfwexe')
G.edge['sensors']['connfwexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('sensors','dpmd')
G.edge['sensors']['dpmd']['write-read'] = '[open open]'
G.add_edge('sensors','healthd')
G.edge['sensors']['healthd']['write-read'] = '[open open]'
G.add_edge('sensors','imsd')
G.edge['sensors']['imsd']['write-read'] = '[open open]'
G.add_edge('sensors','ks')
G.edge['sensors']['ks']['write-read'] = '[open open]'
G.add_edge('sensors','lhd')
G.edge['sensors']['lhd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('sensors','mdm_helper')
G.edge['sensors']['mdm_helper']['write-read'] = '[open open]'
G.add_edge('sensors','mediaserver')
G.edge['sensors']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('sensors','mmi')
G.edge['sensors']['mmi']['write-read'] = '[open open]'
G.add_edge('sensors','qcks')
G.edge['sensors']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open]'
G.add_edge('sensors','qlogd')
G.edge['sensors']['qlogd']['write-read'] = '[write read][add_name search][open open]'
G.add_edge('sensors','qmuxd')
G.edge['sensors']['qmuxd']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('sensors','qmuxd')
G.edge['sensors']['qmuxd']['write-read'] = '[open open][write read][append read][open open][open open]'
G.add_edge('sensors','rfs_access')
G.edge['sensors']['rfs_access']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('sensors','rild')
G.edge['sensors']['rild']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('sensors','rmt_storage')
G.edge['sensors']['rmt_storage']['write-read'] = '[open open]'
G.add_edge('sensors','sec-ril')
G.edge['sensors']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('sensors','sensors')
G.edge['sensors']['sensors']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read][open open]'
G.add_edge('sensors','system_server')
G.edge['sensors']['system_server']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open]'
G.add_edge('sensors','vm_bms')
G.edge['sensors']['vm_bms']['write-read'] = '[open open]'
G.add_edge('sensors','vold')
G.edge['sensors']['vold']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('sensors','at_distributor')
G.edge['sensors']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['sensors']['at_distributor']['fill'] = 'red'
G.add_edge('sensors','at_distributor')
G.edge['sensors']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('sensors','bluetooth')
G.edge['sensors']['bluetooth']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['sensors']['bluetooth']['fill'] = 'red'
G.add_edge('sensors','bluetooth')
G.edge['sensors']['bluetooth']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('sensors','cellgeofenced')
G.edge['sensors']['cellgeofenced']['write-read'] = '[open open][write read]'
G.edge['sensors']['cellgeofenced']['fill'] = 'red'
G.add_edge('sensors','cellgeofenced')
G.edge['sensors']['cellgeofenced']['write-read'] = '[open open][write read][append read]'
G.add_edge('sensors','charger_monitor')
G.edge['sensors']['charger_monitor']['write-read'] = '[open open][write read]'
G.edge['sensors']['charger_monitor']['fill'] = 'red'
G.add_edge('sensors','charger_monitor')
G.edge['sensors']['charger_monitor']['write-read'] = '[open open][write read][append read]'
G.add_edge('sensors','cnd')
G.edge['sensors']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][append read]'
G.add_edge('sensors','connfwexe')
G.edge['sensors']['connfwexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['sensors']['connfwexe']['fill'] = 'red'
G.add_edge('sensors','connfwexe')
G.edge['sensors']['connfwexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('sensors','daemon_app_process')
G.edge['sensors']['daemon_app_process']['write-read'] = '[write read]'
G.edge['sensors']['daemon_app_process']['fill'] = 'red'
G.add_edge('sensors','dpmd')
G.edge['sensors']['dpmd']['write-read'] = '[open open][write read]'
G.edge['sensors']['dpmd']['fill'] = 'red'
G.add_edge('sensors','dpmd')
G.edge['sensors']['dpmd']['write-read'] = '[open open][write read][append read]'
G.add_edge('sensors','healthd')
G.edge['sensors']['healthd']['write-read'] = '[open open][write read]'
G.edge['sensors']['healthd']['fill'] = 'red'
G.add_edge('sensors','healthd')
G.edge['sensors']['healthd']['write-read'] = '[open open][write read][append read]'
G.add_edge('sensors','imsd')
G.edge['sensors']['imsd']['write-read'] = '[open open][write read]'
G.edge['sensors']['imsd']['fill'] = 'red'
G.add_edge('sensors','imsd')
G.edge['sensors']['imsd']['write-read'] = '[open open][write read][append read]'
G.add_edge('sensors','ks')
G.edge['sensors']['ks']['write-read'] = '[open open][append read]'
G.add_edge('sensors','lhd')
G.edge['sensors']['lhd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['sensors']['lhd']['fill'] = 'red'
G.add_edge('sensors','lhd')
G.edge['sensors']['lhd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('sensors','mdm_helper')
G.edge['sensors']['mdm_helper']['write-read'] = '[open open][append read]'
G.add_edge('sensors','mediaserver')
G.edge['sensors']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['sensors']['mediaserver']['fill'] = 'red'
G.add_edge('sensors','mediaserver')
G.edge['sensors']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('sensors','mmi')
G.edge['sensors']['mmi']['write-read'] = '[open open][write read]'
G.edge['sensors']['mmi']['fill'] = 'red'
G.add_edge('sensors','mmi')
G.edge['sensors']['mmi']['write-read'] = '[open open][write read][append read]'
G.add_edge('sensors','qcks')
G.edge['sensors']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][append read]'
G.add_edge('sensors','qlogd')
G.edge['sensors']['qlogd']['write-read'] = '[write read][add_name search][open open][append read]'
G.add_edge('sensors','qmuxd')
G.edge['sensors']['qmuxd']['write-read'] = '[open open][write read][append read][open open][open open][append read]'
G.add_edge('sensors','qmuxd')
G.edge['sensors']['qmuxd']['write-read'] = '[open open][write read][append read][open open][open open][append read][write read]'
G.edge['sensors']['qmuxd']['fill'] = 'red'
G.add_edge('sensors','qmuxd')
G.edge['sensors']['qmuxd']['write-read'] = '[open open][write read][append read][open open][open open][append read][write read][append read]'
G.add_edge('sensors','rfs_access')
G.edge['sensors']['rfs_access']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['sensors']['rfs_access']['fill'] = 'red'
G.add_edge('sensors','rfs_access')
G.edge['sensors']['rfs_access']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('sensors','rild')
G.edge['sensors']['rild']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read]'
G.edge['sensors']['rild']['fill'] = 'red'
G.add_edge('sensors','rild')
G.edge['sensors']['rild']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('sensors','rmt_storage')
G.edge['sensors']['rmt_storage']['write-read'] = '[open open][write read]'
G.edge['sensors']['rmt_storage']['fill'] = 'red'
G.add_edge('sensors','rmt_storage')
G.edge['sensors']['rmt_storage']['write-read'] = '[open open][write read][append read]'
G.add_edge('sensors','sec-ril')
G.edge['sensors']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['sensors']['sec-ril']['fill'] = 'red'
G.add_edge('sensors','sensors')
G.edge['sensors']['sensors']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read][open open][write read]'
G.edge['sensors']['sensors']['fill'] = 'red'
G.add_edge('sensors','sensors')
G.edge['sensors']['sensors']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read][open open][write read][append read]'
G.add_edge('sensors','system_server')
G.edge['sensors']['system_server']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read]'
G.edge['sensors']['system_server']['fill'] = 'red'
G.add_edge('sensors','system_server')
G.edge['sensors']['system_server']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read][append read]'
G.add_edge('sensors','tsdaemon')
G.edge['sensors']['tsdaemon']['write-read'] = '[write read]'
G.edge['sensors']['tsdaemon']['fill'] = 'red'
G.add_edge('sensors','vdc')
G.edge['sensors']['vdc']['write-read'] = '[write read]'
G.edge['sensors']['vdc']['fill'] = 'red'
G.add_edge('sensors','vm_bms')
G.edge['sensors']['vm_bms']['write-read'] = '[open open][write read]'
G.edge['sensors']['vm_bms']['fill'] = 'red'
G.add_edge('sensors','vm_bms')
G.edge['sensors']['vm_bms']['write-read'] = '[open open][write read][append read]'
G.add_edge('sensors','vold')
G.edge['sensors']['vold']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read]'
G.edge['sensors']['vold']['fill'] = 'red'
G.add_edge('sensors','vold')
G.edge['sensors']['vold']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('sensors','vpnclientd')
G.edge['sensors']['vpnclientd']['write-read'] = '[write read]'
G.edge['sensors']['vpnclientd']['fill'] = 'red'
G.add_edge('system_server','at_distributor')
G.edge['system_server']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('system_server','bluetooth')
G.edge['system_server']['bluetooth']['write-read'] = '[setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('system_server','cellgeofenced')
G.edge['system_server']['cellgeofenced']['write-read'] = '[open open][write read][add_name search][remove_name search][open open]'
G.add_edge('system_server','charger_monitor')
G.edge['system_server']['charger_monitor']['write-read'] = '[setopt getopt][open open]'
G.add_edge('system_server','cnd')
G.edge['system_server']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('system_server','connfwexe')
G.edge['system_server']['connfwexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('system_server','dpmd')
G.edge['system_server']['dpmd']['write-read'] = '[open open]'
G.add_edge('system_server','healthd')
G.edge['system_server']['healthd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][write read][add_name search][remove_name search][open open]'
G.add_edge('system_server','imsd')
G.edge['system_server']['imsd']['write-read'] = '[open open]'
G.add_edge('system_server','ks')
G.edge['system_server']['ks']['write-read'] = '[add_name search][open open]'
G.add_edge('system_server','lhd')
G.edge['system_server']['lhd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('system_server','mdm_helper')
G.edge['system_server']['mdm_helper']['write-read'] = '[open open]'
G.add_edge('system_server','mediaserver')
G.edge['system_server']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][add_name search][remove_name search][open open]'
G.add_edge('system_server','mmi')
G.edge['system_server']['mmi']['write-read'] = '[open open]'
G.add_edge('system_server','qcks')
G.edge['system_server']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open]'
G.add_edge('system_server','qlogd')
G.edge['system_server']['qlogd']['write-read'] = '[setopt getopt][write read][add_name search][open open]'
G.add_edge('system_server','qmuxd')
G.edge['system_server']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('system_server','qmuxd')
G.edge['system_server']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][open open]'
G.add_edge('system_server','rfs_access')
G.edge['system_server']['rfs_access']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('system_server','rild')
G.edge['system_server']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('system_server','rmt_storage')
G.edge['system_server']['rmt_storage']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('system_server','sec-ril')
G.edge['system_server']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][add_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('system_server','sensors')
G.edge['system_server']['sensors']['write-read'] = '[add_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][setsched getsched][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][write read][append read][open open]'
G.add_edge('system_server','vm_bms')
G.edge['system_server']['vm_bms']['write-read'] = '[open open]'
G.add_edge('system_server','vold')
G.edge['system_server']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('system_server','at_distributor')
G.edge['system_server']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['system_server']['at_distributor']['fill'] = 'red'
G.add_edge('system_server','at_distributor')
G.edge['system_server']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('system_server','bluetooth')
G.edge['system_server']['bluetooth']['write-read'] = '[setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read]'
G.edge['system_server']['bluetooth']['fill'] = 'red'
G.add_edge('system_server','bluetooth')
G.edge['system_server']['bluetooth']['write-read'] = '[setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read]'
G.add_edge('system_server','cellgeofenced')
G.edge['system_server']['cellgeofenced']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['system_server']['cellgeofenced']['fill'] = 'red'
G.add_edge('system_server','cellgeofenced')
G.edge['system_server']['cellgeofenced']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('system_server','charger_monitor')
G.edge['system_server']['charger_monitor']['write-read'] = '[setopt getopt][open open][write read]'
G.edge['system_server']['charger_monitor']['fill'] = 'red'
G.add_edge('system_server','charger_monitor')
G.edge['system_server']['charger_monitor']['write-read'] = '[setopt getopt][open open][write read][append read]'
G.add_edge('system_server','cnd')
G.edge['system_server']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][append read]'
G.add_edge('system_server','connfwexe')
G.edge['system_server']['connfwexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['system_server']['connfwexe']['fill'] = 'red'
G.add_edge('system_server','connfwexe')
G.edge['system_server']['connfwexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('system_server','daemon_app_process')
G.edge['system_server']['daemon_app_process']['write-read'] = '[write read]'
G.edge['system_server']['daemon_app_process']['fill'] = 'red'
G.add_edge('system_server','dpmd')
G.edge['system_server']['dpmd']['write-read'] = '[open open][write read]'
G.edge['system_server']['dpmd']['fill'] = 'red'
G.add_edge('system_server','dpmd')
G.edge['system_server']['dpmd']['write-read'] = '[open open][write read][append read]'
G.add_edge('system_server','healthd')
G.edge['system_server']['healthd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][write read][add_name search][remove_name search][open open][write read]'
G.edge['system_server']['healthd']['fill'] = 'red'
G.add_edge('system_server','healthd')
G.edge['system_server']['healthd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('system_server','imsd')
G.edge['system_server']['imsd']['write-read'] = '[open open][write read]'
G.edge['system_server']['imsd']['fill'] = 'red'
G.add_edge('system_server','imsd')
G.edge['system_server']['imsd']['write-read'] = '[open open][write read][append read]'
G.add_edge('system_server','ks')
G.edge['system_server']['ks']['write-read'] = '[add_name search][open open][append read]'
G.add_edge('system_server','lhd')
G.edge['system_server']['lhd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['system_server']['lhd']['fill'] = 'red'
G.add_edge('system_server','lhd')
G.edge['system_server']['lhd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('system_server','mdm_helper')
G.edge['system_server']['mdm_helper']['write-read'] = '[open open][append read]'
G.add_edge('system_server','mediaserver')
G.edge['system_server']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][add_name search][remove_name search][open open][write read]'
G.edge['system_server']['mediaserver']['fill'] = 'red'
G.add_edge('system_server','mediaserver')
G.edge['system_server']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('system_server','mmi')
G.edge['system_server']['mmi']['write-read'] = '[open open][write read]'
G.edge['system_server']['mmi']['fill'] = 'red'
G.add_edge('system_server','mmi')
G.edge['system_server']['mmi']['write-read'] = '[open open][write read][append read]'
G.add_edge('system_server','qcks')
G.edge['system_server']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][append read]'
G.add_edge('system_server','qlogd')
G.edge['system_server']['qlogd']['write-read'] = '[setopt getopt][write read][add_name search][open open][append read]'
G.add_edge('system_server','qmuxd')
G.edge['system_server']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][open open][append read]'
G.add_edge('system_server','qmuxd')
G.edge['system_server']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][open open][append read][write read]'
G.edge['system_server']['qmuxd']['fill'] = 'red'
G.add_edge('system_server','qmuxd')
G.edge['system_server']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][open open][append read][write read][append read]'
G.add_edge('system_server','rfs_access')
G.edge['system_server']['rfs_access']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['system_server']['rfs_access']['fill'] = 'red'
G.add_edge('system_server','rfs_access')
G.edge['system_server']['rfs_access']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('system_server','rild')
G.edge['system_server']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['system_server']['rild']['fill'] = 'red'
G.add_edge('system_server','rild')
G.edge['system_server']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('system_server','rmt_storage')
G.edge['system_server']['rmt_storage']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['system_server']['rmt_storage']['fill'] = 'red'
G.add_edge('system_server','rmt_storage')
G.edge['system_server']['rmt_storage']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('system_server','sec-ril')
G.edge['system_server']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][add_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['system_server']['sec-ril']['fill'] = 'red'
G.add_edge('system_server','sensors')
G.edge['system_server']['sensors']['write-read'] = '[add_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['system_server']['sensors']['fill'] = 'red'
G.add_edge('system_server','sensors')
G.edge['system_server']['sensors']['write-read'] = '[add_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][setsched getsched][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][write read][append read][open open][write read]'
G.edge['system_server']['system_server']['fill'] = 'red'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][setsched getsched][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][write read][append read][open open][write read][append read]'
G.add_edge('system_server','tsdaemon')
G.edge['system_server']['tsdaemon']['write-read'] = '[write read]'
G.edge['system_server']['tsdaemon']['fill'] = 'red'
G.add_edge('system_server','vdc')
G.edge['system_server']['vdc']['write-read'] = '[write read]'
G.edge['system_server']['vdc']['fill'] = 'red'
G.add_edge('system_server','vm_bms')
G.edge['system_server']['vm_bms']['write-read'] = '[open open][write read]'
G.edge['system_server']['vm_bms']['fill'] = 'red'
G.add_edge('system_server','vm_bms')
G.edge['system_server']['vm_bms']['write-read'] = '[open open][write read][append read]'
G.add_edge('system_server','vold')
G.edge['system_server']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['system_server']['vold']['fill'] = 'red'
G.add_edge('system_server','vold')
G.edge['system_server']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('system_server','vpnclientd')
G.edge['system_server']['vpnclientd']['write-read'] = '[write read]'
G.edge['system_server']['vpnclientd']['fill'] = 'red'
G.add_edge('vm_bms','at_distributor')
G.edge['vm_bms']['at_distributor']['write-read'] = '[open open]'
G.add_edge('vm_bms','bluetooth')
G.edge['vm_bms']['bluetooth']['write-read'] = '[open open]'
G.add_edge('vm_bms','cellgeofenced')
G.edge['vm_bms']['cellgeofenced']['write-read'] = '[open open]'
G.add_edge('vm_bms','charger_monitor')
G.edge['vm_bms']['charger_monitor']['write-read'] = '[open open]'
G.add_edge('vm_bms','cnd')
G.edge['vm_bms']['cnd']['write-read'] = '[open open]'
G.add_edge('vm_bms','connfwexe')
G.edge['vm_bms']['connfwexe']['write-read'] = '[open open]'
G.add_edge('vm_bms','dpmd')
G.edge['vm_bms']['dpmd']['write-read'] = '[open open]'
G.add_edge('vm_bms','healthd')
G.edge['vm_bms']['healthd']['write-read'] = '[open open]'
G.add_edge('vm_bms','imsd')
G.edge['vm_bms']['imsd']['write-read'] = '[open open]'
G.add_edge('vm_bms','ks')
G.edge['vm_bms']['ks']['write-read'] = '[open open]'
G.add_edge('vm_bms','lhd')
G.edge['vm_bms']['lhd']['write-read'] = '[open open]'
G.add_edge('vm_bms','mdm_helper')
G.edge['vm_bms']['mdm_helper']['write-read'] = '[open open]'
G.add_edge('vm_bms','mediaserver')
G.edge['vm_bms']['mediaserver']['write-read'] = '[open open]'
G.add_edge('vm_bms','mmi')
G.edge['vm_bms']['mmi']['write-read'] = '[open open]'
G.add_edge('vm_bms','qcks')
G.edge['vm_bms']['qcks']['write-read'] = '[open open]'
G.add_edge('vm_bms','qlogd')
G.edge['vm_bms']['qlogd']['write-read'] = '[open open]'
G.add_edge('vm_bms','qmuxd')
G.edge['vm_bms']['qmuxd']['write-read'] = '[open open]'
G.add_edge('vm_bms','qmuxd')
G.edge['vm_bms']['qmuxd']['write-read'] = '[open open][open open]'
G.add_edge('vm_bms','rfs_access')
G.edge['vm_bms']['rfs_access']['write-read'] = '[open open]'
G.add_edge('vm_bms','rild')
G.edge['vm_bms']['rild']['write-read'] = '[open open]'
G.add_edge('vm_bms','rmt_storage')
G.edge['vm_bms']['rmt_storage']['write-read'] = '[open open]'
G.add_edge('vm_bms','sec-ril')
G.edge['vm_bms']['sec-ril']['write-read'] = '[open open]'
G.add_edge('vm_bms','sensors')
G.edge['vm_bms']['sensors']['write-read'] = '[open open]'
G.add_edge('vm_bms','system_server')
G.edge['vm_bms']['system_server']['write-read'] = '[open open]'
G.add_edge('vm_bms','vm_bms')
G.edge['vm_bms']['vm_bms']['write-read'] = '[write read][open open]'
G.add_edge('vm_bms','vold')
G.edge['vm_bms']['vold']['write-read'] = '[open open]'
G.add_edge('vm_bms','at_distributor')
G.edge['vm_bms']['at_distributor']['write-read'] = '[open open][write read]'
G.edge['vm_bms']['at_distributor']['fill'] = 'red'
G.add_edge('vm_bms','at_distributor')
G.edge['vm_bms']['at_distributor']['write-read'] = '[open open][write read][append read]'
G.add_edge('vm_bms','bluetooth')
G.edge['vm_bms']['bluetooth']['write-read'] = '[open open][write read]'
G.edge['vm_bms']['bluetooth']['fill'] = 'red'
G.add_edge('vm_bms','bluetooth')
G.edge['vm_bms']['bluetooth']['write-read'] = '[open open][write read][append read]'
G.add_edge('vm_bms','cellgeofenced')
G.edge['vm_bms']['cellgeofenced']['write-read'] = '[open open][write read]'
G.edge['vm_bms']['cellgeofenced']['fill'] = 'red'
G.add_edge('vm_bms','cellgeofenced')
G.edge['vm_bms']['cellgeofenced']['write-read'] = '[open open][write read][append read]'
G.add_edge('vm_bms','charger_monitor')
G.edge['vm_bms']['charger_monitor']['write-read'] = '[open open][write read]'
G.edge['vm_bms']['charger_monitor']['fill'] = 'red'
G.add_edge('vm_bms','charger_monitor')
G.edge['vm_bms']['charger_monitor']['write-read'] = '[open open][write read][append read]'
G.add_edge('vm_bms','cnd')
G.edge['vm_bms']['cnd']['write-read'] = '[open open][append read]'
G.add_edge('vm_bms','connfwexe')
G.edge['vm_bms']['connfwexe']['write-read'] = '[open open][write read]'
G.edge['vm_bms']['connfwexe']['fill'] = 'red'
G.add_edge('vm_bms','connfwexe')
G.edge['vm_bms']['connfwexe']['write-read'] = '[open open][write read][append read]'
G.add_edge('vm_bms','daemon_app_process')
G.edge['vm_bms']['daemon_app_process']['write-read'] = '[write read]'
G.edge['vm_bms']['daemon_app_process']['fill'] = 'red'
G.add_edge('vm_bms','dpmd')
G.edge['vm_bms']['dpmd']['write-read'] = '[open open][write read]'
G.edge['vm_bms']['dpmd']['fill'] = 'red'
G.add_edge('vm_bms','dpmd')
G.edge['vm_bms']['dpmd']['write-read'] = '[open open][write read][append read]'
G.add_edge('vm_bms','healthd')
G.edge['vm_bms']['healthd']['write-read'] = '[open open][write read]'
G.edge['vm_bms']['healthd']['fill'] = 'red'
G.add_edge('vm_bms','healthd')
G.edge['vm_bms']['healthd']['write-read'] = '[open open][write read][append read]'
G.add_edge('vm_bms','imsd')
G.edge['vm_bms']['imsd']['write-read'] = '[open open][write read]'
G.edge['vm_bms']['imsd']['fill'] = 'red'
G.add_edge('vm_bms','imsd')
G.edge['vm_bms']['imsd']['write-read'] = '[open open][write read][append read]'
G.add_edge('vm_bms','ks')
G.edge['vm_bms']['ks']['write-read'] = '[open open][append read]'
G.add_edge('vm_bms','lhd')
G.edge['vm_bms']['lhd']['write-read'] = '[open open][write read]'
G.edge['vm_bms']['lhd']['fill'] = 'red'
G.add_edge('vm_bms','lhd')
G.edge['vm_bms']['lhd']['write-read'] = '[open open][write read][append read]'
G.add_edge('vm_bms','mdm_helper')
G.edge['vm_bms']['mdm_helper']['write-read'] = '[open open][append read]'
G.add_edge('vm_bms','mediaserver')
G.edge['vm_bms']['mediaserver']['write-read'] = '[open open][write read]'
G.edge['vm_bms']['mediaserver']['fill'] = 'red'
G.add_edge('vm_bms','mediaserver')
G.edge['vm_bms']['mediaserver']['write-read'] = '[open open][write read][append read]'
G.add_edge('vm_bms','mmi')
G.edge['vm_bms']['mmi']['write-read'] = '[open open][write read]'
G.edge['vm_bms']['mmi']['fill'] = 'red'
G.add_edge('vm_bms','mmi')
G.edge['vm_bms']['mmi']['write-read'] = '[open open][write read][append read]'
G.add_edge('vm_bms','qcks')
G.edge['vm_bms']['qcks']['write-read'] = '[open open][append read]'
G.add_edge('vm_bms','qlogd')
G.edge['vm_bms']['qlogd']['write-read'] = '[open open][append read]'
G.add_edge('vm_bms','qmuxd')
G.edge['vm_bms']['qmuxd']['write-read'] = '[open open][open open][append read]'
G.add_edge('vm_bms','qmuxd')
G.edge['vm_bms']['qmuxd']['write-read'] = '[open open][open open][append read][write read]'
G.edge['vm_bms']['qmuxd']['fill'] = 'red'
G.add_edge('vm_bms','qmuxd')
G.edge['vm_bms']['qmuxd']['write-read'] = '[open open][open open][append read][write read][append read]'
G.add_edge('vm_bms','rfs_access')
G.edge['vm_bms']['rfs_access']['write-read'] = '[open open][write read]'
G.edge['vm_bms']['rfs_access']['fill'] = 'red'
G.add_edge('vm_bms','rfs_access')
G.edge['vm_bms']['rfs_access']['write-read'] = '[open open][write read][append read]'
G.add_edge('vm_bms','rild')
G.edge['vm_bms']['rild']['write-read'] = '[open open][write read]'
G.edge['vm_bms']['rild']['fill'] = 'red'
G.add_edge('vm_bms','rild')
G.edge['vm_bms']['rild']['write-read'] = '[open open][write read][append read]'
G.add_edge('vm_bms','rmt_storage')
G.edge['vm_bms']['rmt_storage']['write-read'] = '[open open][write read]'
G.edge['vm_bms']['rmt_storage']['fill'] = 'red'
G.add_edge('vm_bms','rmt_storage')
G.edge['vm_bms']['rmt_storage']['write-read'] = '[open open][write read][append read]'
G.add_edge('vm_bms','sec-ril')
G.edge['vm_bms']['sec-ril']['write-read'] = '[open open][write read]'
G.edge['vm_bms']['sec-ril']['fill'] = 'red'
G.add_edge('vm_bms','sensors')
G.edge['vm_bms']['sensors']['write-read'] = '[open open][write read]'
G.edge['vm_bms']['sensors']['fill'] = 'red'
G.add_edge('vm_bms','sensors')
G.edge['vm_bms']['sensors']['write-read'] = '[open open][write read][append read]'
G.add_edge('vm_bms','system_server')
G.edge['vm_bms']['system_server']['write-read'] = '[open open][write read]'
G.edge['vm_bms']['system_server']['fill'] = 'red'
G.add_edge('vm_bms','system_server')
G.edge['vm_bms']['system_server']['write-read'] = '[open open][write read][append read]'
G.add_edge('vm_bms','tsdaemon')
G.edge['vm_bms']['tsdaemon']['write-read'] = '[write read]'
G.edge['vm_bms']['tsdaemon']['fill'] = 'red'
G.add_edge('vm_bms','vdc')
G.edge['vm_bms']['vdc']['write-read'] = '[write read]'
G.edge['vm_bms']['vdc']['fill'] = 'red'
G.add_edge('vm_bms','vm_bms')
G.edge['vm_bms']['vm_bms']['write-read'] = '[write read][open open][write read]'
G.edge['vm_bms']['vm_bms']['fill'] = 'red'
G.add_edge('vm_bms','vm_bms')
G.edge['vm_bms']['vm_bms']['write-read'] = '[write read][open open][write read][append read]'
G.add_edge('vm_bms','vold')
G.edge['vm_bms']['vold']['write-read'] = '[open open][write read]'
G.edge['vm_bms']['vold']['fill'] = 'red'
G.add_edge('vm_bms','vold')
G.edge['vm_bms']['vold']['write-read'] = '[open open][write read][append read]'
G.add_edge('vm_bms','vpnclientd')
G.edge['vm_bms']['vpnclientd']['write-read'] = '[write read]'
G.edge['vm_bms']['vpnclientd']['fill'] = 'red'
G.add_edge('vold','at_distributor')
G.edge['vold']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('vold','bluetooth')
G.edge['vold']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('vold','cellgeofenced')
G.edge['vold']['cellgeofenced']['write-read'] = '[open open]'
G.add_edge('vold','charger_monitor')
G.edge['vold']['charger_monitor']['write-read'] = '[setopt getopt][open open]'
G.add_edge('vold','cnd')
G.edge['vold']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('vold','connfwexe')
G.edge['vold']['connfwexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('vold','dpmd')
G.edge['vold']['dpmd']['write-read'] = '[open open]'
G.add_edge('vold','healthd')
G.edge['vold']['healthd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][write read][add_name search][remove_name search][open open]'
G.add_edge('vold','imsd')
G.edge['vold']['imsd']['write-read'] = '[open open]'
G.add_edge('vold','ks')
G.edge['vold']['ks']['write-read'] = '[open open][write read][add_name search][open open]'
G.add_edge('vold','lhd')
G.edge['vold']['lhd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('vold','mdm_helper')
G.edge['vold']['mdm_helper']['write-read'] = '[write read][open open]'
G.add_edge('vold','mediaserver')
G.edge['vold']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('vold','mmi')
G.edge['vold']['mmi']['write-read'] = '[open open]'
G.add_edge('vold','qcks')
G.edge['vold']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('vold','qlogd')
G.edge['vold']['qlogd']['write-read'] = '[write read][add_name search][write read][add_name search][open open]'
G.add_edge('vold','qmuxd')
G.edge['vold']['qmuxd']['write-read'] = '[open open]'
G.add_edge('vold','qmuxd')
G.edge['vold']['qmuxd']['write-read'] = '[open open][open open]'
G.add_edge('vold','rfs_access')
G.edge['vold']['rfs_access']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('vold','rild')
G.edge['vold']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('vold','rmt_storage')
G.edge['vold']['rmt_storage']['write-read'] = '[open open]'
G.add_edge('vold','sec-ril')
G.edge['vold']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('vold','sensors')
G.edge['vold']['sensors']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('vold','system_server')
G.edge['vold']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('vold','vm_bms')
G.edge['vold']['vm_bms']['write-read'] = '[open open]'
G.add_edge('vold','vold')
G.edge['vold']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][relabelto relabelfrom][relabelto relabelfrom][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('vold','at_distributor')
G.edge['vold']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['vold']['at_distributor']['fill'] = 'red'
G.add_edge('vold','at_distributor')
G.edge['vold']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('vold','bluetooth')
G.edge['vold']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['vold']['bluetooth']['fill'] = 'red'
G.add_edge('vold','bluetooth')
G.edge['vold']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('vold','cellgeofenced')
G.edge['vold']['cellgeofenced']['write-read'] = '[open open][write read]'
G.edge['vold']['cellgeofenced']['fill'] = 'red'
G.add_edge('vold','cellgeofenced')
G.edge['vold']['cellgeofenced']['write-read'] = '[open open][write read][append read]'
G.add_edge('vold','charger_monitor')
G.edge['vold']['charger_monitor']['write-read'] = '[setopt getopt][open open][write read]'
G.edge['vold']['charger_monitor']['fill'] = 'red'
G.add_edge('vold','charger_monitor')
G.edge['vold']['charger_monitor']['write-read'] = '[setopt getopt][open open][write read][append read]'
G.add_edge('vold','cnd')
G.edge['vold']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][append read]'
G.add_edge('vold','connfwexe')
G.edge['vold']['connfwexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['vold']['connfwexe']['fill'] = 'red'
G.add_edge('vold','connfwexe')
G.edge['vold']['connfwexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('vold','daemon_app_process')
G.edge['vold']['daemon_app_process']['write-read'] = '[write read]'
G.edge['vold']['daemon_app_process']['fill'] = 'red'
G.add_edge('vold','dpmd')
G.edge['vold']['dpmd']['write-read'] = '[open open][write read]'
G.edge['vold']['dpmd']['fill'] = 'red'
G.add_edge('vold','dpmd')
G.edge['vold']['dpmd']['write-read'] = '[open open][write read][append read]'
G.add_edge('vold','healthd')
G.edge['vold']['healthd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][write read][add_name search][remove_name search][open open][write read]'
G.edge['vold']['healthd']['fill'] = 'red'
G.add_edge('vold','healthd')
G.edge['vold']['healthd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('vold','imsd')
G.edge['vold']['imsd']['write-read'] = '[open open][write read]'
G.edge['vold']['imsd']['fill'] = 'red'
G.add_edge('vold','imsd')
G.edge['vold']['imsd']['write-read'] = '[open open][write read][append read]'
G.add_edge('vold','ks')
G.edge['vold']['ks']['write-read'] = '[open open][write read][add_name search][open open][append read]'
G.add_edge('vold','lhd')
G.edge['vold']['lhd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['vold']['lhd']['fill'] = 'red'
G.add_edge('vold','lhd')
G.edge['vold']['lhd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('vold','mdm_helper')
G.edge['vold']['mdm_helper']['write-read'] = '[write read][open open][append read]'
G.add_edge('vold','mediaserver')
G.edge['vold']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read]'
G.edge['vold']['mediaserver']['fill'] = 'red'
G.add_edge('vold','mediaserver')
G.edge['vold']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('vold','mmi')
G.edge['vold']['mmi']['write-read'] = '[open open][write read]'
G.edge['vold']['mmi']['fill'] = 'red'
G.add_edge('vold','mmi')
G.edge['vold']['mmi']['write-read'] = '[open open][write read][append read]'
G.add_edge('vold','qcks')
G.edge['vold']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][append read]'
G.add_edge('vold','qlogd')
G.edge['vold']['qlogd']['write-read'] = '[write read][add_name search][write read][add_name search][open open][append read]'
G.add_edge('vold','qmuxd')
G.edge['vold']['qmuxd']['write-read'] = '[open open][open open][append read]'
G.add_edge('vold','qmuxd')
G.edge['vold']['qmuxd']['write-read'] = '[open open][open open][append read][write read]'
G.edge['vold']['qmuxd']['fill'] = 'red'
G.add_edge('vold','qmuxd')
G.edge['vold']['qmuxd']['write-read'] = '[open open][open open][append read][write read][append read]'
G.add_edge('vold','rfs_access')
G.edge['vold']['rfs_access']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['vold']['rfs_access']['fill'] = 'red'
G.add_edge('vold','rfs_access')
G.edge['vold']['rfs_access']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('vold','rild')
G.edge['vold']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read]'
G.edge['vold']['rild']['fill'] = 'red'
G.add_edge('vold','rild')
G.edge['vold']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('vold','rmt_storage')
G.edge['vold']['rmt_storage']['write-read'] = '[open open][write read]'
G.edge['vold']['rmt_storage']['fill'] = 'red'
G.add_edge('vold','rmt_storage')
G.edge['vold']['rmt_storage']['write-read'] = '[open open][write read][append read]'
G.add_edge('vold','sec-ril')
G.edge['vold']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read]'
G.edge['vold']['sec-ril']['fill'] = 'red'
G.add_edge('vold','sensors')
G.edge['vold']['sensors']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['vold']['sensors']['fill'] = 'red'
G.add_edge('vold','sensors')
G.edge['vold']['sensors']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('vold','system_server')
G.edge['vold']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read]'
G.edge['vold']['system_server']['fill'] = 'red'
G.add_edge('vold','system_server')
G.edge['vold']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('vold','tsdaemon')
G.edge['vold']['tsdaemon']['write-read'] = '[write read]'
G.edge['vold']['tsdaemon']['fill'] = 'red'
G.add_edge('vold','vdc')
G.edge['vold']['vdc']['write-read'] = '[write read]'
G.edge['vold']['vdc']['fill'] = 'red'
G.add_edge('vold','vm_bms')
G.edge['vold']['vm_bms']['write-read'] = '[open open][write read]'
G.edge['vold']['vm_bms']['fill'] = 'red'
G.add_edge('vold','vm_bms')
G.edge['vold']['vm_bms']['write-read'] = '[open open][write read][append read]'
G.add_edge('vold','vold')
G.edge['vold']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][relabelto relabelfrom][relabelto relabelfrom][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read]'
G.edge['vold']['vold']['fill'] = 'red'
G.add_edge('vold','vold')
G.edge['vold']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][relabelto relabelfrom][relabelto relabelfrom][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('vold','vpnclientd')
G.edge['vold']['vpnclientd']['write-read'] = '[write read]'
G.edge['vold']['vpnclientd']['fill'] = 'red'
app = Viewer(G)
app.mainloop()