import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('bauthserver','at_distributor')
G.edge['bauthserver']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('bauthserver','bauthserver')
G.edge['bauthserver']['bauthserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('bauthserver','bintvoutservice')
G.edge['bauthserver']['bintvoutservice']['write-read'] = '[open open]'
G.add_edge('bauthserver','bluetooth')
G.edge['bauthserver']['bluetooth']['write-read'] = '[open open]'
G.add_edge('bauthserver','cbd')
G.edge['bauthserver']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('bauthserver','cellgeofenced')
G.edge['bauthserver']['cellgeofenced']['write-read'] = '[open open]'
G.add_edge('bauthserver','charger_monitor')
G.edge['bauthserver']['charger_monitor']['write-read'] = '[open open]'
G.add_edge('bauthserver','charger_monitor')
G.edge['bauthserver']['charger_monitor']['write-read'] = '[open open][open open]'
G.add_edge('bauthserver','cnd')
G.edge['bauthserver']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open]'
G.add_edge('bauthserver','connfwexe')
G.edge['bauthserver']['connfwexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('bauthserver','debuggerd')
G.edge['bauthserver']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('bauthserver','diag_uart_log')
G.edge['bauthserver']['diag_uart_log']['write-read'] = '[open open]'
G.add_edge('bauthserver','dumpstate')
G.edge['bauthserver']['dumpstate']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('bauthserver','efsks')
G.edge['bauthserver']['efsks']['write-read'] = '[open open]'
G.add_edge('bauthserver','geomagneticd')
G.edge['bauthserver']['geomagneticd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open]'
G.add_edge('bauthserver','gpsd')
G.edge['bauthserver']['gpsd']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('bauthserver','init_shell')
G.edge['bauthserver']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('bauthserver','kiesexe')
G.edge['bauthserver']['kiesexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('bauthserver','ks')
G.edge['bauthserver']['ks']['write-read'] = '[open open]'
G.add_edge('bauthserver','lhd')
G.edge['bauthserver']['lhd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('bauthserver','lpm')
G.edge['bauthserver']['lpm']['write-read'] = '[open open]'
G.add_edge('bauthserver','macloader')
G.edge['bauthserver']['macloader']['write-read'] = '[open open]'
G.add_edge('bauthserver','mdm_helper')
G.edge['bauthserver']['mdm_helper']['write-read'] = '[open open]'
G.add_edge('bauthserver','mediaserver')
G.edge['bauthserver']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('bauthserver','mlexe')
G.edge['bauthserver']['mlexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('bauthserver','mm-pp-daemon')
G.edge['bauthserver']['mm-pp-daemon']['write-read'] = '[open open]'
G.add_edge('bauthserver','mm-qcamera-daemon')
G.edge['bauthserver']['mm-qcamera-daemon']['write-read'] = '[open open][write read][add_name search][remove_name search][open open]'
G.add_edge('bauthserver','mpdecision')
G.edge['bauthserver']['mpdecision']['write-read'] = '[open open][write read][add_name search][remove_name search][open open]'
G.add_edge('bauthserver','oneseg_mw')
G.edge['bauthserver']['oneseg_mw']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('bauthserver','qcks')
G.edge['bauthserver']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open]'
G.add_edge('bauthserver','qmuxd')
G.edge['bauthserver']['qmuxd']['write-read'] = '[open open]'
G.add_edge('bauthserver','radio')
G.edge['bauthserver']['radio']['write-read'] = '[open open]'
G.add_edge('bauthserver','rild')
G.edge['bauthserver']['rild']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('bauthserver','rmt_storage')
G.edge['bauthserver']['rmt_storage']['write-read'] = '[open open]'
G.add_edge('bauthserver','sec-ril')
G.edge['bauthserver']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('bauthserver','smdexe')
G.edge['bauthserver']['smdexe']['write-read'] = '[open open]'
G.add_edge('bauthserver','ssr_setup')
G.edge['bauthserver']['ssr_setup']['write-read'] = '[open open]'
G.add_edge('bauthserver','sswap')
G.edge['bauthserver']['sswap']['write-read'] = '[open open]'
G.add_edge('bauthserver','surfaceflinger')
G.edge['bauthserver']['surfaceflinger']['write-read'] = '[open open]'
G.add_edge('bauthserver','system_server')
G.edge['bauthserver']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('bauthserver','system_server')
G.edge['bauthserver']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open]'
G.add_edge('bauthserver','thermal-engine')
G.edge['bauthserver']['thermal-engine']['write-read'] = '[open open]'
G.add_edge('bauthserver','ueventd')
G.edge['bauthserver']['ueventd']['write-read'] = '[open open]'
G.add_edge('bauthserver','vm_bms')
G.edge['bauthserver']['vm_bms']['write-read'] = '[open open]'
G.add_edge('bauthserver','vold')
G.edge['bauthserver']['vold']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('bauthserver','init_shell')
G.edge['bauthserver']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('bauthserver','rild')
G.edge['bauthserver']['rild']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('bauthserver','rtcc')
G.edge['bauthserver']['rtcc']['write-read'] = '[setattr getattr]'
G.add_edge('bauthserver','sec-ril')
G.edge['bauthserver']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('bauthserver','system_server')
G.edge['bauthserver']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr]'
G.add_edge('bauthserver','at_distributor')
G.edge['bauthserver']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['bauthserver']['at_distributor']['fill'] = 'red'
G.add_edge('bauthserver','at_distributor')
G.edge['bauthserver']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('bauthserver','bauthserver')
G.edge['bauthserver']['bauthserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['bauthserver']['bauthserver']['fill'] = 'red'
G.add_edge('bauthserver','bauthserver')
G.edge['bauthserver']['bauthserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('bauthserver','bintvoutservice')
G.edge['bauthserver']['bintvoutservice']['write-read'] = '[open open][write read]'
G.edge['bauthserver']['bintvoutservice']['fill'] = 'red'
G.add_edge('bauthserver','bintvoutservice')
G.edge['bauthserver']['bintvoutservice']['write-read'] = '[open open][write read][append read]'
G.add_edge('bauthserver','bluetooth')
G.edge['bauthserver']['bluetooth']['write-read'] = '[open open][write read]'
G.edge['bauthserver']['bluetooth']['fill'] = 'red'
G.add_edge('bauthserver','bluetooth')
G.edge['bauthserver']['bluetooth']['write-read'] = '[open open][write read][append read]'
G.add_edge('bauthserver','bootanim')
G.edge['bauthserver']['bootanim']['write-read'] = '[write read]'
G.edge['bauthserver']['bootanim']['fill'] = 'red'
G.add_edge('bauthserver','cbd')
G.edge['bauthserver']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['bauthserver']['cbd']['fill'] = 'red'
G.add_edge('bauthserver','cbd')
G.edge['bauthserver']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('bauthserver','cellgeofenced')
G.edge['bauthserver']['cellgeofenced']['write-read'] = '[open open][write read]'
G.edge['bauthserver']['cellgeofenced']['fill'] = 'red'
G.add_edge('bauthserver','cellgeofenced')
G.edge['bauthserver']['cellgeofenced']['write-read'] = '[open open][write read][append read]'
G.add_edge('bauthserver','charger_monitor')
G.edge['bauthserver']['charger_monitor']['write-read'] = '[open open][open open][write read]'
G.edge['bauthserver']['charger_monitor']['fill'] = 'red'
G.add_edge('bauthserver','charger_monitor')
G.edge['bauthserver']['charger_monitor']['write-read'] = '[open open][open open][write read][append read]'
G.add_edge('bauthserver','charger_monitor')
G.edge['bauthserver']['charger_monitor']['write-read'] = '[open open][open open][write read][append read][write read]'
G.edge['bauthserver']['charger_monitor']['fill'] = 'red'
G.add_edge('bauthserver','charger_monitor')
G.edge['bauthserver']['charger_monitor']['write-read'] = '[open open][open open][write read][append read][write read][append read]'
G.add_edge('bauthserver','cnd')
G.edge['bauthserver']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['bauthserver']['cnd']['fill'] = 'red'
G.add_edge('bauthserver','cnd')
G.edge['bauthserver']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('bauthserver','connfwexe')
G.edge['bauthserver']['connfwexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['bauthserver']['connfwexe']['fill'] = 'red'
G.add_edge('bauthserver','connfwexe')
G.edge['bauthserver']['connfwexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('bauthserver','debuggerd')
G.edge['bauthserver']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['bauthserver']['debuggerd']['fill'] = 'red'
G.add_edge('bauthserver','debuggerd')
G.edge['bauthserver']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('bauthserver','diag_uart_log')
G.edge['bauthserver']['diag_uart_log']['write-read'] = '[open open][write read]'
G.edge['bauthserver']['diag_uart_log']['fill'] = 'red'
G.add_edge('bauthserver','diag_uart_log')
G.edge['bauthserver']['diag_uart_log']['write-read'] = '[open open][write read][append read]'
G.add_edge('bauthserver','dumpstate')
G.edge['bauthserver']['dumpstate']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read]'
G.edge['bauthserver']['dumpstate']['fill'] = 'red'
G.add_edge('bauthserver','dumpstate')
G.edge['bauthserver']['dumpstate']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('bauthserver','efsks')
G.edge['bauthserver']['efsks']['write-read'] = '[open open][write read]'
G.edge['bauthserver']['efsks']['fill'] = 'red'
G.add_edge('bauthserver','efsks')
G.edge['bauthserver']['efsks']['write-read'] = '[open open][write read][append read]'
G.add_edge('bauthserver','geomagneticd')
G.edge['bauthserver']['geomagneticd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['bauthserver']['geomagneticd']['fill'] = 'red'
G.add_edge('bauthserver','geomagneticd')
G.edge['bauthserver']['geomagneticd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('bauthserver','gpsd')
G.edge['bauthserver']['gpsd']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read]'
G.edge['bauthserver']['gpsd']['fill'] = 'red'
G.add_edge('bauthserver','gpsd')
G.edge['bauthserver']['gpsd']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('bauthserver','healthd')
G.edge['bauthserver']['healthd']['write-read'] = '[write read]'
G.edge['bauthserver']['healthd']['fill'] = 'red'
G.add_edge('bauthserver','init_shell')
G.edge['bauthserver']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['bauthserver']['init_shell']['fill'] = 'red'
G.add_edge('bauthserver','init_shell')
G.edge['bauthserver']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('bauthserver','jackservice')
G.edge['bauthserver']['jackservice']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['bauthserver']['jackservice']['fill'] = 'red'
G.add_edge('bauthserver','kiesexe')
G.edge['bauthserver']['kiesexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['bauthserver']['kiesexe']['fill'] = 'red'
G.add_edge('bauthserver','kiesexe')
G.edge['bauthserver']['kiesexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('bauthserver','ks')
G.edge['bauthserver']['ks']['write-read'] = '[open open][write read]'
G.edge['bauthserver']['ks']['fill'] = 'red'
G.add_edge('bauthserver','ks')
G.edge['bauthserver']['ks']['write-read'] = '[open open][write read][append read]'
G.add_edge('bauthserver','lhd')
G.edge['bauthserver']['lhd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['bauthserver']['lhd']['fill'] = 'red'
G.add_edge('bauthserver','lhd')
G.edge['bauthserver']['lhd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('bauthserver','lmkd')
G.edge['bauthserver']['lmkd']['write-read'] = '[write read]'
G.edge['bauthserver']['lmkd']['fill'] = 'red'
G.add_edge('bauthserver','lpm')
G.edge['bauthserver']['lpm']['write-read'] = '[open open][write read]'
G.edge['bauthserver']['lpm']['fill'] = 'red'
G.add_edge('bauthserver','lpm')
G.edge['bauthserver']['lpm']['write-read'] = '[open open][write read][append read]'
G.add_edge('bauthserver','macloader')
G.edge['bauthserver']['macloader']['write-read'] = '[open open][write read]'
G.edge['bauthserver']['macloader']['fill'] = 'red'
G.add_edge('bauthserver','macloader')
G.edge['bauthserver']['macloader']['write-read'] = '[open open][write read][append read]'
G.add_edge('bauthserver','mdm_helper')
G.edge['bauthserver']['mdm_helper']['write-read'] = '[open open][write read]'
G.edge['bauthserver']['mdm_helper']['fill'] = 'red'
G.add_edge('bauthserver','mediaserver')
G.edge['bauthserver']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['bauthserver']['mediaserver']['fill'] = 'red'
G.add_edge('bauthserver','mediaserver')
G.edge['bauthserver']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('bauthserver','mfgloader')
G.edge['bauthserver']['mfgloader']['write-read'] = '[open open][write read][add_name search][remove_name search][write read]'
G.edge['bauthserver']['mfgloader']['fill'] = 'red'
G.add_edge('bauthserver','mlexe')
G.edge['bauthserver']['mlexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['bauthserver']['mlexe']['fill'] = 'red'
G.add_edge('bauthserver','mlexe')
G.edge['bauthserver']['mlexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('bauthserver','mm-pp-daemon')
G.edge['bauthserver']['mm-pp-daemon']['write-read'] = '[open open][write read]'
G.edge['bauthserver']['mm-pp-daemon']['fill'] = 'red'
G.add_edge('bauthserver','mm-pp-daemon')
G.edge['bauthserver']['mm-pp-daemon']['write-read'] = '[open open][write read][append read]'
G.add_edge('bauthserver','mm-pp-daemon')
G.edge['bauthserver']['mm-pp-daemon']['write-read'] = '[open open][write read][append read][write read]'
G.edge['bauthserver']['mm-pp-daemon']['fill'] = 'red'
G.add_edge('bauthserver','mm-qcamera-daemon')
G.edge['bauthserver']['mm-qcamera-daemon']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['bauthserver']['mm-qcamera-daemon']['fill'] = 'red'
G.add_edge('bauthserver','mm-qcamera-daemon')
G.edge['bauthserver']['mm-qcamera-daemon']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('bauthserver','mpdecision')
G.edge['bauthserver']['mpdecision']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['bauthserver']['mpdecision']['fill'] = 'red'
G.add_edge('bauthserver','mpdecision')
G.edge['bauthserver']['mpdecision']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('bauthserver','mpdecision')
G.edge['bauthserver']['mpdecision']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read][write read]'
G.edge['bauthserver']['mpdecision']['fill'] = 'red'
G.add_edge('bauthserver','netd')
G.edge['bauthserver']['netd']['write-read'] = '[write read]'
G.edge['bauthserver']['netd']['fill'] = 'red'
G.add_edge('bauthserver','netmgrd')
G.edge['bauthserver']['netmgrd']['write-read'] = '[open open][open open][write read][write read][add_name search][add_name search][remove_name search][write read]'
G.edge['bauthserver']['netmgrd']['fill'] = 'red'
G.add_edge('bauthserver','nfc')
G.edge['bauthserver']['nfc']['write-read'] = '[write read]'
G.edge['bauthserver']['nfc']['fill'] = 'red'
G.add_edge('bauthserver','oneseg_mw')
G.edge['bauthserver']['oneseg_mw']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['bauthserver']['oneseg_mw']['fill'] = 'red'
G.add_edge('bauthserver','oneseg_mw')
G.edge['bauthserver']['oneseg_mw']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('bauthserver','perfd')
G.edge['bauthserver']['perfd']['write-read'] = '[write read]'
G.edge['bauthserver']['perfd']['fill'] = 'red'
G.add_edge('bauthserver','qcks')
G.edge['bauthserver']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['bauthserver']['qcks']['fill'] = 'red'
G.add_edge('bauthserver','qcks')
G.edge['bauthserver']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('bauthserver','qmuxd')
G.edge['bauthserver']['qmuxd']['write-read'] = '[open open][write read]'
G.edge['bauthserver']['qmuxd']['fill'] = 'red'
G.add_edge('bauthserver','qmuxd')
G.edge['bauthserver']['qmuxd']['write-read'] = '[open open][write read][append read]'
G.add_edge('bauthserver','qosmgr')
G.edge['bauthserver']['qosmgr']['write-read'] = '[write read]'
G.edge['bauthserver']['qosmgr']['fill'] = 'red'
G.add_edge('bauthserver','radio')
G.edge['bauthserver']['radio']['write-read'] = '[open open][append read]'
G.add_edge('bauthserver','rild')
G.edge['bauthserver']['rild']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['bauthserver']['rild']['fill'] = 'red'
G.add_edge('bauthserver','rild')
G.edge['bauthserver']['rild']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('bauthserver','rmt_storage')
G.edge['bauthserver']['rmt_storage']['write-read'] = '[open open][write read]'
G.edge['bauthserver']['rmt_storage']['fill'] = 'red'
G.add_edge('bauthserver','rmt_storage')
G.edge['bauthserver']['rmt_storage']['write-read'] = '[open open][write read][append read]'
G.add_edge('bauthserver','rtcc')
G.edge['bauthserver']['rtcc']['write-read'] = '[setattr getattr][write read]'
G.edge['bauthserver']['rtcc']['fill'] = 'red'
G.add_edge('bauthserver','sec-ril')
G.edge['bauthserver']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['bauthserver']['sec-ril']['fill'] = 'red'
G.add_edge('bauthserver','sec-ril')
G.edge['bauthserver']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('bauthserver','sensorhubservice')
G.edge['bauthserver']['sensorhubservice']['write-read'] = '[write read]'
G.edge['bauthserver']['sensorhubservice']['fill'] = 'red'
G.add_edge('bauthserver','smdexe')
G.edge['bauthserver']['smdexe']['write-read'] = '[open open][write read]'
G.edge['bauthserver']['smdexe']['fill'] = 'red'
G.add_edge('bauthserver','smdexe')
G.edge['bauthserver']['smdexe']['write-read'] = '[open open][write read][append read]'
G.add_edge('bauthserver','ssr_setup')
G.edge['bauthserver']['ssr_setup']['write-read'] = '[open open][write read]'
G.edge['bauthserver']['ssr_setup']['fill'] = 'red'
G.add_edge('bauthserver','ssr_setup')
G.edge['bauthserver']['ssr_setup']['write-read'] = '[open open][write read][append read]'
G.add_edge('bauthserver','sswap')
G.edge['bauthserver']['sswap']['write-read'] = '[open open][write read]'
G.edge['bauthserver']['sswap']['fill'] = 'red'
G.add_edge('bauthserver','sswap')
G.edge['bauthserver']['sswap']['write-read'] = '[open open][write read][append read]'
G.add_edge('bauthserver','surfaceflinger')
G.edge['bauthserver']['surfaceflinger']['write-read'] = '[open open][write read]'
G.edge['bauthserver']['surfaceflinger']['fill'] = 'red'
G.add_edge('bauthserver','surfaceflinger')
G.edge['bauthserver']['surfaceflinger']['write-read'] = '[open open][write read][append read]'
G.add_edge('bauthserver','surfaceflinger')
G.edge['bauthserver']['surfaceflinger']['write-read'] = '[open open][write read][append read][write read]'
G.edge['bauthserver']['surfaceflinger']['fill'] = 'red'
G.add_edge('bauthserver','system_server')
G.edge['bauthserver']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read]'
G.edge['bauthserver']['system_server']['fill'] = 'red'
G.add_edge('bauthserver','system_server')
G.edge['bauthserver']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][append read]'
G.add_edge('bauthserver','system_server')
G.edge['bauthserver']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][append read][write read]'
G.edge['bauthserver']['system_server']['fill'] = 'red'
G.add_edge('bauthserver','system_server')
G.edge['bauthserver']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][append read][write read][append read]'
G.add_edge('bauthserver','thermald')
G.edge['bauthserver']['thermald']['write-read'] = '[open open][write read][add_name search][remove_name search][write read]'
G.edge['bauthserver']['thermald']['fill'] = 'red'
G.add_edge('bauthserver','thermal-engine')
G.edge['bauthserver']['thermal-engine']['write-read'] = '[open open][write read]'
G.edge['bauthserver']['thermal-engine']['fill'] = 'red'
G.add_edge('bauthserver','thermal-engine')
G.edge['bauthserver']['thermal-engine']['write-read'] = '[open open][write read][append read]'
G.add_edge('bauthserver','thermal-engine')
G.edge['bauthserver']['thermal-engine']['write-read'] = '[open open][write read][append read][write read]'
G.edge['bauthserver']['thermal-engine']['fill'] = 'red'
G.add_edge('bauthserver','ueventd')
G.edge['bauthserver']['ueventd']['write-read'] = '[open open][write read]'
G.edge['bauthserver']['ueventd']['fill'] = 'red'
G.add_edge('bauthserver','ueventd')
G.edge['bauthserver']['ueventd']['write-read'] = '[open open][write read][append read]'
G.add_edge('bauthserver','vm_bms')
G.edge['bauthserver']['vm_bms']['write-read'] = '[open open][write read]'
G.edge['bauthserver']['vm_bms']['fill'] = 'red'
G.add_edge('bauthserver','vm_bms')
G.edge['bauthserver']['vm_bms']['write-read'] = '[open open][write read][append read]'
G.add_edge('bauthserver','vmwared')
G.edge['bauthserver']['vmwared']['write-read'] = '[write read]'
G.edge['bauthserver']['vmwared']['fill'] = 'red'
G.add_edge('bauthserver','vold')
G.edge['bauthserver']['vold']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read]'
G.edge['bauthserver']['vold']['fill'] = 'red'
G.add_edge('bauthserver','vold')
G.edge['bauthserver']['vold']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('bauthserver','zygote')
G.edge['bauthserver']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['bauthserver']['zygote']['fill'] = 'red'
G.add_edge('bluetooth','at_distributor')
G.edge['bluetooth']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('bluetooth','bauthserver')
G.edge['bluetooth']['bauthserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('bluetooth','bintvoutservice')
G.edge['bluetooth']['bintvoutservice']['write-read'] = '[open open]'
G.add_edge('bluetooth','bluetooth')
G.edge['bluetooth']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('bluetooth','cbd')
G.edge['bluetooth']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('bluetooth','cellgeofenced')
G.edge['bluetooth']['cellgeofenced']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('bluetooth','charger_monitor')
G.edge['bluetooth']['charger_monitor']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('bluetooth','charger_monitor')
G.edge['bluetooth']['charger_monitor']['write-read'] = '[open open][write read][append read][open open][open open]'
G.add_edge('bluetooth','cnd')
G.edge['bluetooth']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][append read][open open]'
G.add_edge('bluetooth','connfwexe')
G.edge['bluetooth']['connfwexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('bluetooth','debuggerd')
G.edge['bluetooth']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('bluetooth','diag_uart_log')
G.edge['bluetooth']['diag_uart_log']['write-read'] = '[open open]'
G.add_edge('bluetooth','dumpstate')
G.edge['bluetooth']['dumpstate']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open]'
G.add_edge('bluetooth','efsks')
G.edge['bluetooth']['efsks']['write-read'] = '[open open]'
G.add_edge('bluetooth','geomagneticd')
G.edge['bluetooth']['geomagneticd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open]'
G.add_edge('bluetooth','gpsd')
G.edge['bluetooth']['gpsd']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('bluetooth','init_shell')
G.edge['bluetooth']['init_shell']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('bluetooth','kiesexe')
G.edge['bluetooth']['kiesexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('bluetooth','ks')
G.edge['bluetooth']['ks']['write-read'] = '[open open][append read][open open]'
G.add_edge('bluetooth','lhd')
G.edge['bluetooth']['lhd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('bluetooth','lpm')
G.edge['bluetooth']['lpm']['write-read'] = '[open open]'
G.add_edge('bluetooth','macloader')
G.edge['bluetooth']['macloader']['write-read'] = '[open open]'
G.add_edge('bluetooth','mdm_helper')
G.edge['bluetooth']['mdm_helper']['write-read'] = '[open open][append read][open open]'
G.add_edge('bluetooth','mediaserver')
G.edge['bluetooth']['mediaserver']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read][append read][open open]'
G.add_edge('bluetooth','mlexe')
G.edge['bluetooth']['mlexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('bluetooth','mm-pp-daemon')
G.edge['bluetooth']['mm-pp-daemon']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('bluetooth','mm-qcamera-daemon')
G.edge['bluetooth']['mm-qcamera-daemon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('bluetooth','mpdecision')
G.edge['bluetooth']['mpdecision']['write-read'] = '[open open][write read][add_name search][remove_name search][open open]'
G.add_edge('bluetooth','oneseg_mw')
G.edge['bluetooth']['oneseg_mw']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('bluetooth','qcks')
G.edge['bluetooth']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][append read][open open]'
G.add_edge('bluetooth','qmuxd')
G.edge['bluetooth']['qmuxd']['write-read'] = '[open open][write read][append read][open open][open open][append read][write read][append read][open open]'
G.add_edge('bluetooth','radio')
G.edge['bluetooth']['radio']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open]'
G.add_edge('bluetooth','rild')
G.edge['bluetooth']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('bluetooth','rmt_storage')
G.edge['bluetooth']['rmt_storage']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('bluetooth','sec-ril')
G.edge['bluetooth']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][open open]'
G.add_edge('bluetooth','smdexe')
G.edge['bluetooth']['smdexe']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('bluetooth','ssr_setup')
G.edge['bluetooth']['ssr_setup']['write-read'] = '[open open]'
G.add_edge('bluetooth','sswap')
G.edge['bluetooth']['sswap']['write-read'] = '[open open]'
G.add_edge('bluetooth','surfaceflinger')
G.edge['bluetooth']['surfaceflinger']['write-read'] = '[write read][open open]'
G.add_edge('bluetooth','system_server')
G.edge['bluetooth']['system_server']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][write read][append read][open open]'
G.add_edge('bluetooth','system_server')
G.edge['bluetooth']['system_server']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][write read][append read][open open][open open]'
G.add_edge('bluetooth','thermal-engine')
G.edge['bluetooth']['thermal-engine']['write-read'] = '[open open]'
G.add_edge('bluetooth','ueventd')
G.edge['bluetooth']['ueventd']['write-read'] = '[open open]'
G.add_edge('bluetooth','vm_bms')
G.edge['bluetooth']['vm_bms']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('bluetooth','vold')
G.edge['bluetooth']['vold']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read][append read][open open]'
G.add_edge('bluetooth','init_shell')
G.edge['bluetooth']['init_shell']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('bluetooth','rild')
G.edge['bluetooth']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr]'
G.add_edge('bluetooth','rtcc')
G.edge['bluetooth']['rtcc']['write-read'] = '[setattr getattr]'
G.add_edge('bluetooth','sec-ril')
G.edge['bluetooth']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][open open][setattr getattr]'
G.add_edge('bluetooth','system_server')
G.edge['bluetooth']['system_server']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][write read][append read][open open][open open][setattr getattr]'
G.add_edge('bluetooth','at_distributor')
G.edge['bluetooth']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read]'
G.edge['bluetooth']['at_distributor']['fill'] = 'red'
G.add_edge('bluetooth','at_distributor')
G.edge['bluetooth']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read]'
G.add_edge('bluetooth','bauthserver')
G.edge['bluetooth']['bauthserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['bluetooth']['bauthserver']['fill'] = 'red'
G.add_edge('bluetooth','bauthserver')
G.edge['bluetooth']['bauthserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('bluetooth','bintvoutservice')
G.edge['bluetooth']['bintvoutservice']['write-read'] = '[open open][write read]'
G.edge['bluetooth']['bintvoutservice']['fill'] = 'red'
G.add_edge('bluetooth','bintvoutservice')
G.edge['bluetooth']['bintvoutservice']['write-read'] = '[open open][write read][append read]'
G.add_edge('bluetooth','bluetooth')
G.edge['bluetooth']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['bluetooth']['bluetooth']['fill'] = 'red'
G.add_edge('bluetooth','bluetooth')
G.edge['bluetooth']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('bluetooth','bootanim')
G.edge['bluetooth']['bootanim']['write-read'] = '[write read]'
G.edge['bluetooth']['bootanim']['fill'] = 'red'
G.add_edge('bluetooth','cbd')
G.edge['bluetooth']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['bluetooth']['cbd']['fill'] = 'red'
G.add_edge('bluetooth','cbd')
G.edge['bluetooth']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('bluetooth','cellgeofenced')
G.edge['bluetooth']['cellgeofenced']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['bluetooth']['cellgeofenced']['fill'] = 'red'
G.add_edge('bluetooth','cellgeofenced')
G.edge['bluetooth']['cellgeofenced']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('bluetooth','charger_monitor')
G.edge['bluetooth']['charger_monitor']['write-read'] = '[open open][write read][append read][open open][open open][write read]'
G.edge['bluetooth']['charger_monitor']['fill'] = 'red'
G.add_edge('bluetooth','charger_monitor')
G.edge['bluetooth']['charger_monitor']['write-read'] = '[open open][write read][append read][open open][open open][write read][append read]'
G.add_edge('bluetooth','charger_monitor')
G.edge['bluetooth']['charger_monitor']['write-read'] = '[open open][write read][append read][open open][open open][write read][append read][write read]'
G.edge['bluetooth']['charger_monitor']['fill'] = 'red'
G.add_edge('bluetooth','charger_monitor')
G.edge['bluetooth']['charger_monitor']['write-read'] = '[open open][write read][append read][open open][open open][write read][append read][write read][append read]'
G.add_edge('bluetooth','cnd')
G.edge['bluetooth']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][append read][open open][write read]'
G.edge['bluetooth']['cnd']['fill'] = 'red'
G.add_edge('bluetooth','cnd')
G.edge['bluetooth']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][append read][open open][write read][append read]'
G.add_edge('bluetooth','connfwexe')
G.edge['bluetooth']['connfwexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read]'
G.edge['bluetooth']['connfwexe']['fill'] = 'red'
G.add_edge('bluetooth','connfwexe')
G.edge['bluetooth']['connfwexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read]'
G.add_edge('bluetooth','debuggerd')
G.edge['bluetooth']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['bluetooth']['debuggerd']['fill'] = 'red'
G.add_edge('bluetooth','debuggerd')
G.edge['bluetooth']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('bluetooth','diag_uart_log')
G.edge['bluetooth']['diag_uart_log']['write-read'] = '[open open][write read]'
G.edge['bluetooth']['diag_uart_log']['fill'] = 'red'
G.add_edge('bluetooth','diag_uart_log')
G.edge['bluetooth']['diag_uart_log']['write-read'] = '[open open][write read][append read]'
G.add_edge('bluetooth','dumpstate')
G.edge['bluetooth']['dumpstate']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open][write read]'
G.edge['bluetooth']['dumpstate']['fill'] = 'red'
G.add_edge('bluetooth','dumpstate')
G.edge['bluetooth']['dumpstate']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open][write read][append read]'
G.add_edge('bluetooth','efsks')
G.edge['bluetooth']['efsks']['write-read'] = '[open open][write read]'
G.edge['bluetooth']['efsks']['fill'] = 'red'
G.add_edge('bluetooth','efsks')
G.edge['bluetooth']['efsks']['write-read'] = '[open open][write read][append read]'
G.add_edge('bluetooth','geomagneticd')
G.edge['bluetooth']['geomagneticd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['bluetooth']['geomagneticd']['fill'] = 'red'
G.add_edge('bluetooth','geomagneticd')
G.edge['bluetooth']['geomagneticd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('bluetooth','gpsd')
G.edge['bluetooth']['gpsd']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read]'
G.edge['bluetooth']['gpsd']['fill'] = 'red'
G.add_edge('bluetooth','gpsd')
G.edge['bluetooth']['gpsd']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('bluetooth','healthd')
G.edge['bluetooth']['healthd']['write-read'] = '[open open][write read][append read][write read]'
G.edge['bluetooth']['healthd']['fill'] = 'red'
G.add_edge('bluetooth','init_shell')
G.edge['bluetooth']['init_shell']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['bluetooth']['init_shell']['fill'] = 'red'
G.add_edge('bluetooth','init_shell')
G.edge['bluetooth']['init_shell']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('bluetooth','jackservice')
G.edge['bluetooth']['jackservice']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['bluetooth']['jackservice']['fill'] = 'red'
G.add_edge('bluetooth','kiesexe')
G.edge['bluetooth']['kiesexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['bluetooth']['kiesexe']['fill'] = 'red'
G.add_edge('bluetooth','kiesexe')
G.edge['bluetooth']['kiesexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('bluetooth','ks')
G.edge['bluetooth']['ks']['write-read'] = '[open open][append read][open open][write read]'
G.edge['bluetooth']['ks']['fill'] = 'red'
G.add_edge('bluetooth','ks')
G.edge['bluetooth']['ks']['write-read'] = '[open open][append read][open open][write read][append read]'
G.add_edge('bluetooth','lhd')
G.edge['bluetooth']['lhd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read]'
G.edge['bluetooth']['lhd']['fill'] = 'red'
G.add_edge('bluetooth','lhd')
G.edge['bluetooth']['lhd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read]'
G.add_edge('bluetooth','lmkd')
G.edge['bluetooth']['lmkd']['write-read'] = '[write read]'
G.edge['bluetooth']['lmkd']['fill'] = 'red'
G.add_edge('bluetooth','lpm')
G.edge['bluetooth']['lpm']['write-read'] = '[open open][write read]'
G.edge['bluetooth']['lpm']['fill'] = 'red'
G.add_edge('bluetooth','lpm')
G.edge['bluetooth']['lpm']['write-read'] = '[open open][write read][append read]'
G.add_edge('bluetooth','macloader')
G.edge['bluetooth']['macloader']['write-read'] = '[open open][write read]'
G.edge['bluetooth']['macloader']['fill'] = 'red'
G.add_edge('bluetooth','macloader')
G.edge['bluetooth']['macloader']['write-read'] = '[open open][write read][append read]'
G.add_edge('bluetooth','mdm_helper')
G.edge['bluetooth']['mdm_helper']['write-read'] = '[open open][append read][open open][write read]'
G.edge['bluetooth']['mdm_helper']['fill'] = 'red'
G.add_edge('bluetooth','mediaserver')
G.edge['bluetooth']['mediaserver']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read][append read][open open][write read]'
G.edge['bluetooth']['mediaserver']['fill'] = 'red'
G.add_edge('bluetooth','mediaserver')
G.edge['bluetooth']['mediaserver']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read][append read][open open][write read][append read]'
G.add_edge('bluetooth','mfgloader')
G.edge['bluetooth']['mfgloader']['write-read'] = '[open open][write read][add_name search][remove_name search][write read]'
G.edge['bluetooth']['mfgloader']['fill'] = 'red'
G.add_edge('bluetooth','mlexe')
G.edge['bluetooth']['mlexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['bluetooth']['mlexe']['fill'] = 'red'
G.add_edge('bluetooth','mlexe')
G.edge['bluetooth']['mlexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('bluetooth','mm-pp-daemon')
G.edge['bluetooth']['mm-pp-daemon']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read]'
G.edge['bluetooth']['mm-pp-daemon']['fill'] = 'red'
G.add_edge('bluetooth','mm-pp-daemon')
G.edge['bluetooth']['mm-pp-daemon']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('bluetooth','mm-pp-daemon')
G.edge['bluetooth']['mm-pp-daemon']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][write read]'
G.edge['bluetooth']['mm-pp-daemon']['fill'] = 'red'
G.add_edge('bluetooth','mm-qcamera-daemon')
G.edge['bluetooth']['mm-qcamera-daemon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['bluetooth']['mm-qcamera-daemon']['fill'] = 'red'
G.add_edge('bluetooth','mm-qcamera-daemon')
G.edge['bluetooth']['mm-qcamera-daemon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('bluetooth','mpdecision')
G.edge['bluetooth']['mpdecision']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['bluetooth']['mpdecision']['fill'] = 'red'
G.add_edge('bluetooth','mpdecision')
G.edge['bluetooth']['mpdecision']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('bluetooth','mpdecision')
G.edge['bluetooth']['mpdecision']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read][write read]'
G.edge['bluetooth']['mpdecision']['fill'] = 'red'
G.add_edge('bluetooth','netd')
G.edge['bluetooth']['netd']['write-read'] = '[write read][append read][write read]'
G.edge['bluetooth']['netd']['fill'] = 'red'
G.add_edge('bluetooth','netmgrd')
G.edge['bluetooth']['netmgrd']['write-read'] = '[open open][open open][write read][write read][add_name search][add_name search][remove_name search][write read]'
G.edge['bluetooth']['netmgrd']['fill'] = 'red'
G.add_edge('bluetooth','nfc')
G.edge['bluetooth']['nfc']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['bluetooth']['nfc']['fill'] = 'red'
G.add_edge('bluetooth','oneseg_mw')
G.edge['bluetooth']['oneseg_mw']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['bluetooth']['oneseg_mw']['fill'] = 'red'
G.add_edge('bluetooth','oneseg_mw')
G.edge['bluetooth']['oneseg_mw']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('bluetooth','perfd')
G.edge['bluetooth']['perfd']['write-read'] = '[write read]'
G.edge['bluetooth']['perfd']['fill'] = 'red'
G.add_edge('bluetooth','qcks')
G.edge['bluetooth']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][append read][open open][write read]'
G.edge['bluetooth']['qcks']['fill'] = 'red'
G.add_edge('bluetooth','qcks')
G.edge['bluetooth']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][append read][open open][write read][append read]'
G.add_edge('bluetooth','qmuxd')
G.edge['bluetooth']['qmuxd']['write-read'] = '[open open][write read][append read][open open][open open][append read][write read][append read][open open][write read]'
G.edge['bluetooth']['qmuxd']['fill'] = 'red'
G.add_edge('bluetooth','qmuxd')
G.edge['bluetooth']['qmuxd']['write-read'] = '[open open][write read][append read][open open][open open][append read][write read][append read][open open][write read][append read]'
G.add_edge('bluetooth','qosmgr')
G.edge['bluetooth']['qosmgr']['write-read'] = '[write read]'
G.edge['bluetooth']['qosmgr']['fill'] = 'red'
G.add_edge('bluetooth','radio')
G.edge['bluetooth']['radio']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][append read]'
G.add_edge('bluetooth','rild')
G.edge['bluetooth']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['bluetooth']['rild']['fill'] = 'red'
G.add_edge('bluetooth','rild')
G.edge['bluetooth']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('bluetooth','rmt_storage')
G.edge['bluetooth']['rmt_storage']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['bluetooth']['rmt_storage']['fill'] = 'red'
G.add_edge('bluetooth','rmt_storage')
G.edge['bluetooth']['rmt_storage']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('bluetooth','rtcc')
G.edge['bluetooth']['rtcc']['write-read'] = '[setattr getattr][write read]'
G.edge['bluetooth']['rtcc']['fill'] = 'red'
G.add_edge('bluetooth','sec-ril')
G.edge['bluetooth']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][open open][setattr getattr][write read]'
G.edge['bluetooth']['sec-ril']['fill'] = 'red'
G.add_edge('bluetooth','sec-ril')
G.edge['bluetooth']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][open open][setattr getattr][write read][append read]'
G.add_edge('bluetooth','sensorhubservice')
G.edge['bluetooth']['sensorhubservice']['write-read'] = '[write read]'
G.edge['bluetooth']['sensorhubservice']['fill'] = 'red'
G.add_edge('bluetooth','smdexe')
G.edge['bluetooth']['smdexe']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['bluetooth']['smdexe']['fill'] = 'red'
G.add_edge('bluetooth','smdexe')
G.edge['bluetooth']['smdexe']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('bluetooth','ssr_setup')
G.edge['bluetooth']['ssr_setup']['write-read'] = '[open open][write read]'
G.edge['bluetooth']['ssr_setup']['fill'] = 'red'
G.add_edge('bluetooth','ssr_setup')
G.edge['bluetooth']['ssr_setup']['write-read'] = '[open open][write read][append read]'
G.add_edge('bluetooth','sswap')
G.edge['bluetooth']['sswap']['write-read'] = '[open open][write read]'
G.edge['bluetooth']['sswap']['fill'] = 'red'
G.add_edge('bluetooth','sswap')
G.edge['bluetooth']['sswap']['write-read'] = '[open open][write read][append read]'
G.add_edge('bluetooth','surfaceflinger')
G.edge['bluetooth']['surfaceflinger']['write-read'] = '[write read][open open][write read]'
G.edge['bluetooth']['surfaceflinger']['fill'] = 'red'
G.add_edge('bluetooth','surfaceflinger')
G.edge['bluetooth']['surfaceflinger']['write-read'] = '[write read][open open][write read][append read]'
G.add_edge('bluetooth','surfaceflinger')
G.edge['bluetooth']['surfaceflinger']['write-read'] = '[write read][open open][write read][append read][write read]'
G.edge['bluetooth']['surfaceflinger']['fill'] = 'red'
G.add_edge('bluetooth','system_server')
G.edge['bluetooth']['system_server']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][write read][append read][open open][open open][setattr getattr][write read]'
G.edge['bluetooth']['system_server']['fill'] = 'red'
G.add_edge('bluetooth','system_server')
G.edge['bluetooth']['system_server']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read]'
G.add_edge('bluetooth','system_server')
G.edge['bluetooth']['system_server']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read]'
G.edge['bluetooth']['system_server']['fill'] = 'red'
G.add_edge('bluetooth','system_server')
G.edge['bluetooth']['system_server']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read]'
G.add_edge('bluetooth','thermald')
G.edge['bluetooth']['thermald']['write-read'] = '[open open][write read][add_name search][remove_name search][write read]'
G.edge['bluetooth']['thermald']['fill'] = 'red'
G.add_edge('bluetooth','thermal-engine')
G.edge['bluetooth']['thermal-engine']['write-read'] = '[open open][write read]'
G.edge['bluetooth']['thermal-engine']['fill'] = 'red'
G.add_edge('bluetooth','thermal-engine')
G.edge['bluetooth']['thermal-engine']['write-read'] = '[open open][write read][append read]'
G.add_edge('bluetooth','thermal-engine')
G.edge['bluetooth']['thermal-engine']['write-read'] = '[open open][write read][append read][write read]'
G.edge['bluetooth']['thermal-engine']['fill'] = 'red'
G.add_edge('bluetooth','ueventd')
G.edge['bluetooth']['ueventd']['write-read'] = '[open open][write read]'
G.edge['bluetooth']['ueventd']['fill'] = 'red'
G.add_edge('bluetooth','ueventd')
G.edge['bluetooth']['ueventd']['write-read'] = '[open open][write read][append read]'
G.add_edge('bluetooth','vm_bms')
G.edge['bluetooth']['vm_bms']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['bluetooth']['vm_bms']['fill'] = 'red'
G.add_edge('bluetooth','vm_bms')
G.edge['bluetooth']['vm_bms']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('bluetooth','vmwared')
G.edge['bluetooth']['vmwared']['write-read'] = '[write read]'
G.edge['bluetooth']['vmwared']['fill'] = 'red'
G.add_edge('bluetooth','vold')
G.edge['bluetooth']['vold']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read][append read][open open][write read]'
G.edge['bluetooth']['vold']['fill'] = 'red'
G.add_edge('bluetooth','vold')
G.edge['bluetooth']['vold']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read][append read][open open][write read][append read]'
G.add_edge('bluetooth','zygote')
G.edge['bluetooth']['zygote']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][write read]'
G.edge['bluetooth']['zygote']['fill'] = 'red'
G.add_edge('cellgeofenced','at_distributor')
G.edge['cellgeofenced']['at_distributor']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('cellgeofenced','bauthserver')
G.edge['cellgeofenced']['bauthserver']['write-read'] = '[open open]'
G.add_edge('cellgeofenced','bintvoutservice')
G.edge['cellgeofenced']['bintvoutservice']['write-read'] = '[open open]'
G.add_edge('cellgeofenced','bluetooth')
G.edge['cellgeofenced']['bluetooth']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('cellgeofenced','cbd')
G.edge['cellgeofenced']['cbd']['write-read'] = '[open open]'
G.add_edge('cellgeofenced','cellgeofenced')
G.edge['cellgeofenced']['cellgeofenced']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('cellgeofenced','charger_monitor')
G.edge['cellgeofenced']['charger_monitor']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('cellgeofenced','charger_monitor')
G.edge['cellgeofenced']['charger_monitor']['write-read'] = '[open open][write read][append read][open open][open open]'
G.add_edge('cellgeofenced','cnd')
G.edge['cellgeofenced']['cnd']['write-read'] = '[open open][append read][open open]'
G.add_edge('cellgeofenced','connfwexe')
G.edge['cellgeofenced']['connfwexe']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('cellgeofenced','debuggerd')
G.edge['cellgeofenced']['debuggerd']['write-read'] = '[open open]'
G.add_edge('cellgeofenced','diag_uart_log')
G.edge['cellgeofenced']['diag_uart_log']['write-read'] = '[open open]'
G.add_edge('cellgeofenced','dumpstate')
G.edge['cellgeofenced']['dumpstate']['write-read'] = '[open open]'
G.add_edge('cellgeofenced','efsks')
G.edge['cellgeofenced']['efsks']['write-read'] = '[open open]'
G.add_edge('cellgeofenced','geomagneticd')
G.edge['cellgeofenced']['geomagneticd']['write-read'] = '[open open]'
G.add_edge('cellgeofenced','gpsd')
G.edge['cellgeofenced']['gpsd']['write-read'] = '[open open]'
G.add_edge('cellgeofenced','init_shell')
G.edge['cellgeofenced']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('cellgeofenced','kiesexe')
G.edge['cellgeofenced']['kiesexe']['write-read'] = '[open open]'
G.add_edge('cellgeofenced','ks')
G.edge['cellgeofenced']['ks']['write-read'] = '[open open][append read][open open]'
G.add_edge('cellgeofenced','lhd')
G.edge['cellgeofenced']['lhd']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('cellgeofenced','lpm')
G.edge['cellgeofenced']['lpm']['write-read'] = '[open open]'
G.add_edge('cellgeofenced','macloader')
G.edge['cellgeofenced']['macloader']['write-read'] = '[open open]'
G.add_edge('cellgeofenced','mdm_helper')
G.edge['cellgeofenced']['mdm_helper']['write-read'] = '[open open][append read][open open]'
G.add_edge('cellgeofenced','mediaserver')
G.edge['cellgeofenced']['mediaserver']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('cellgeofenced','mlexe')
G.edge['cellgeofenced']['mlexe']['write-read'] = '[open open]'
G.add_edge('cellgeofenced','mm-pp-daemon')
G.edge['cellgeofenced']['mm-pp-daemon']['write-read'] = '[open open]'
G.add_edge('cellgeofenced','mm-qcamera-daemon')
G.edge['cellgeofenced']['mm-qcamera-daemon']['write-read'] = '[open open]'
G.add_edge('cellgeofenced','mpdecision')
G.edge['cellgeofenced']['mpdecision']['write-read'] = '[open open]'
G.add_edge('cellgeofenced','oneseg_mw')
G.edge['cellgeofenced']['oneseg_mw']['write-read'] = '[open open]'
G.add_edge('cellgeofenced','qcks')
G.edge['cellgeofenced']['qcks']['write-read'] = '[open open][append read][open open]'
G.add_edge('cellgeofenced','qmuxd')
G.edge['cellgeofenced']['qmuxd']['write-read'] = '[open open][open open][append read][write read][append read][open open]'
G.add_edge('cellgeofenced','radio')
G.edge['cellgeofenced']['radio']['write-read'] = '[open open]'
G.add_edge('cellgeofenced','rild')
G.edge['cellgeofenced']['rild']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('cellgeofenced','rmt_storage')
G.edge['cellgeofenced']['rmt_storage']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('cellgeofenced','sec-ril')
G.edge['cellgeofenced']['sec-ril']['write-read'] = '[open open][write read][open open]'
G.add_edge('cellgeofenced','smdexe')
G.edge['cellgeofenced']['smdexe']['write-read'] = '[open open]'
G.add_edge('cellgeofenced','ssr_setup')
G.edge['cellgeofenced']['ssr_setup']['write-read'] = '[open open]'
G.add_edge('cellgeofenced','sswap')
G.edge['cellgeofenced']['sswap']['write-read'] = '[open open]'
G.add_edge('cellgeofenced','surfaceflinger')
G.edge['cellgeofenced']['surfaceflinger']['write-read'] = '[open open]'
G.add_edge('cellgeofenced','system_server')
G.edge['cellgeofenced']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('cellgeofenced','system_server')
G.edge['cellgeofenced']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][open open]'
G.add_edge('cellgeofenced','thermal-engine')
G.edge['cellgeofenced']['thermal-engine']['write-read'] = '[open open]'
G.add_edge('cellgeofenced','ueventd')
G.edge['cellgeofenced']['ueventd']['write-read'] = '[setattr getattr][open open]'
G.add_edge('cellgeofenced','vm_bms')
G.edge['cellgeofenced']['vm_bms']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('cellgeofenced','vold')
G.edge['cellgeofenced']['vold']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('cellgeofenced','init_shell')
G.edge['cellgeofenced']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('cellgeofenced','rild')
G.edge['cellgeofenced']['rild']['write-read'] = '[open open][write read][append read][open open][setattr getattr]'
G.add_edge('cellgeofenced','rtcc')
G.edge['cellgeofenced']['rtcc']['write-read'] = '[setattr getattr][setattr getattr]'
G.add_edge('cellgeofenced','sec-ril')
G.edge['cellgeofenced']['sec-ril']['write-read'] = '[open open][write read][open open][setattr getattr]'
G.add_edge('cellgeofenced','system_server')
G.edge['cellgeofenced']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][open open][setattr getattr]'
G.add_edge('cellgeofenced','at_distributor')
G.edge['cellgeofenced']['at_distributor']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['cellgeofenced']['at_distributor']['fill'] = 'red'
G.add_edge('cellgeofenced','at_distributor')
G.edge['cellgeofenced']['at_distributor']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('cellgeofenced','bauthserver')
G.edge['cellgeofenced']['bauthserver']['write-read'] = '[open open][write read]'
G.edge['cellgeofenced']['bauthserver']['fill'] = 'red'
G.add_edge('cellgeofenced','bauthserver')
G.edge['cellgeofenced']['bauthserver']['write-read'] = '[open open][write read][append read]'
G.add_edge('cellgeofenced','bintvoutservice')
G.edge['cellgeofenced']['bintvoutservice']['write-read'] = '[open open][write read]'
G.edge['cellgeofenced']['bintvoutservice']['fill'] = 'red'
G.add_edge('cellgeofenced','bintvoutservice')
G.edge['cellgeofenced']['bintvoutservice']['write-read'] = '[open open][write read][append read]'
G.add_edge('cellgeofenced','bluetooth')
G.edge['cellgeofenced']['bluetooth']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['cellgeofenced']['bluetooth']['fill'] = 'red'
G.add_edge('cellgeofenced','bluetooth')
G.edge['cellgeofenced']['bluetooth']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('cellgeofenced','bootanim')
G.edge['cellgeofenced']['bootanim']['write-read'] = '[write read]'
G.edge['cellgeofenced']['bootanim']['fill'] = 'red'
G.add_edge('cellgeofenced','cbd')
G.edge['cellgeofenced']['cbd']['write-read'] = '[open open][write read]'
G.edge['cellgeofenced']['cbd']['fill'] = 'red'
G.add_edge('cellgeofenced','cbd')
G.edge['cellgeofenced']['cbd']['write-read'] = '[open open][write read][append read]'
G.add_edge('cellgeofenced','cellgeofenced')
G.edge['cellgeofenced']['cellgeofenced']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read]'
G.edge['cellgeofenced']['cellgeofenced']['fill'] = 'red'
G.add_edge('cellgeofenced','cellgeofenced')
G.edge['cellgeofenced']['cellgeofenced']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read]'
G.add_edge('cellgeofenced','charger_monitor')
G.edge['cellgeofenced']['charger_monitor']['write-read'] = '[open open][write read][append read][open open][open open][write read]'
G.edge['cellgeofenced']['charger_monitor']['fill'] = 'red'
G.add_edge('cellgeofenced','charger_monitor')
G.edge['cellgeofenced']['charger_monitor']['write-read'] = '[open open][write read][append read][open open][open open][write read][append read]'
G.add_edge('cellgeofenced','charger_monitor')
G.edge['cellgeofenced']['charger_monitor']['write-read'] = '[open open][write read][append read][open open][open open][write read][append read][write read]'
G.edge['cellgeofenced']['charger_monitor']['fill'] = 'red'
G.add_edge('cellgeofenced','charger_monitor')
G.edge['cellgeofenced']['charger_monitor']['write-read'] = '[open open][write read][append read][open open][open open][write read][append read][write read][append read]'
G.add_edge('cellgeofenced','cnd')
G.edge['cellgeofenced']['cnd']['write-read'] = '[open open][append read][open open][write read]'
G.edge['cellgeofenced']['cnd']['fill'] = 'red'
G.add_edge('cellgeofenced','cnd')
G.edge['cellgeofenced']['cnd']['write-read'] = '[open open][append read][open open][write read][append read]'
G.add_edge('cellgeofenced','connfwexe')
G.edge['cellgeofenced']['connfwexe']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['cellgeofenced']['connfwexe']['fill'] = 'red'
G.add_edge('cellgeofenced','connfwexe')
G.edge['cellgeofenced']['connfwexe']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('cellgeofenced','debuggerd')
G.edge['cellgeofenced']['debuggerd']['write-read'] = '[open open][write read]'
G.edge['cellgeofenced']['debuggerd']['fill'] = 'red'
G.add_edge('cellgeofenced','debuggerd')
G.edge['cellgeofenced']['debuggerd']['write-read'] = '[open open][write read][append read]'
G.add_edge('cellgeofenced','diag_uart_log')
G.edge['cellgeofenced']['diag_uart_log']['write-read'] = '[open open][write read]'
G.edge['cellgeofenced']['diag_uart_log']['fill'] = 'red'
G.add_edge('cellgeofenced','diag_uart_log')
G.edge['cellgeofenced']['diag_uart_log']['write-read'] = '[open open][write read][append read]'
G.add_edge('cellgeofenced','dumpstate')
G.edge['cellgeofenced']['dumpstate']['write-read'] = '[open open][write read]'
G.edge['cellgeofenced']['dumpstate']['fill'] = 'red'
G.add_edge('cellgeofenced','dumpstate')
G.edge['cellgeofenced']['dumpstate']['write-read'] = '[open open][write read][append read]'
G.add_edge('cellgeofenced','efsks')
G.edge['cellgeofenced']['efsks']['write-read'] = '[open open][write read]'
G.edge['cellgeofenced']['efsks']['fill'] = 'red'
G.add_edge('cellgeofenced','efsks')
G.edge['cellgeofenced']['efsks']['write-read'] = '[open open][write read][append read]'
G.add_edge('cellgeofenced','geomagneticd')
G.edge['cellgeofenced']['geomagneticd']['write-read'] = '[open open][write read]'
G.edge['cellgeofenced']['geomagneticd']['fill'] = 'red'
G.add_edge('cellgeofenced','geomagneticd')
G.edge['cellgeofenced']['geomagneticd']['write-read'] = '[open open][write read][append read]'
G.add_edge('cellgeofenced','gpsd')
G.edge['cellgeofenced']['gpsd']['write-read'] = '[open open][write read]'
G.edge['cellgeofenced']['gpsd']['fill'] = 'red'
G.add_edge('cellgeofenced','gpsd')
G.edge['cellgeofenced']['gpsd']['write-read'] = '[open open][write read][append read]'
G.add_edge('cellgeofenced','healthd')
G.edge['cellgeofenced']['healthd']['write-read'] = '[open open][write read][append read][write read]'
G.edge['cellgeofenced']['healthd']['fill'] = 'red'
G.add_edge('cellgeofenced','init_shell')
G.edge['cellgeofenced']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['cellgeofenced']['init_shell']['fill'] = 'red'
G.add_edge('cellgeofenced','init_shell')
G.edge['cellgeofenced']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('cellgeofenced','jackservice')
G.edge['cellgeofenced']['jackservice']['write-read'] = '[write read]'
G.edge['cellgeofenced']['jackservice']['fill'] = 'red'
G.add_edge('cellgeofenced','kiesexe')
G.edge['cellgeofenced']['kiesexe']['write-read'] = '[open open][write read]'
G.edge['cellgeofenced']['kiesexe']['fill'] = 'red'
G.add_edge('cellgeofenced','kiesexe')
G.edge['cellgeofenced']['kiesexe']['write-read'] = '[open open][write read][append read]'
G.add_edge('cellgeofenced','ks')
G.edge['cellgeofenced']['ks']['write-read'] = '[open open][append read][open open][write read]'
G.edge['cellgeofenced']['ks']['fill'] = 'red'
G.add_edge('cellgeofenced','ks')
G.edge['cellgeofenced']['ks']['write-read'] = '[open open][append read][open open][write read][append read]'
G.add_edge('cellgeofenced','lhd')
G.edge['cellgeofenced']['lhd']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['cellgeofenced']['lhd']['fill'] = 'red'
G.add_edge('cellgeofenced','lhd')
G.edge['cellgeofenced']['lhd']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('cellgeofenced','lmkd')
G.edge['cellgeofenced']['lmkd']['write-read'] = '[write read]'
G.edge['cellgeofenced']['lmkd']['fill'] = 'red'
G.add_edge('cellgeofenced','lpm')
G.edge['cellgeofenced']['lpm']['write-read'] = '[open open][write read]'
G.edge['cellgeofenced']['lpm']['fill'] = 'red'
G.add_edge('cellgeofenced','lpm')
G.edge['cellgeofenced']['lpm']['write-read'] = '[open open][write read][append read]'
G.add_edge('cellgeofenced','macloader')
G.edge['cellgeofenced']['macloader']['write-read'] = '[open open][write read]'
G.edge['cellgeofenced']['macloader']['fill'] = 'red'
G.add_edge('cellgeofenced','macloader')
G.edge['cellgeofenced']['macloader']['write-read'] = '[open open][write read][append read]'
G.add_edge('cellgeofenced','mdm_helper')
G.edge['cellgeofenced']['mdm_helper']['write-read'] = '[open open][append read][open open][write read]'
G.edge['cellgeofenced']['mdm_helper']['fill'] = 'red'
G.add_edge('cellgeofenced','mediaserver')
G.edge['cellgeofenced']['mediaserver']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['cellgeofenced']['mediaserver']['fill'] = 'red'
G.add_edge('cellgeofenced','mediaserver')
G.edge['cellgeofenced']['mediaserver']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('cellgeofenced','mfgloader')
G.edge['cellgeofenced']['mfgloader']['write-read'] = '[write read]'
G.edge['cellgeofenced']['mfgloader']['fill'] = 'red'
G.add_edge('cellgeofenced','mlexe')
G.edge['cellgeofenced']['mlexe']['write-read'] = '[open open][write read]'
G.edge['cellgeofenced']['mlexe']['fill'] = 'red'
G.add_edge('cellgeofenced','mlexe')
G.edge['cellgeofenced']['mlexe']['write-read'] = '[open open][write read][append read]'
G.add_edge('cellgeofenced','mm-pp-daemon')
G.edge['cellgeofenced']['mm-pp-daemon']['write-read'] = '[open open][write read]'
G.edge['cellgeofenced']['mm-pp-daemon']['fill'] = 'red'
G.add_edge('cellgeofenced','mm-pp-daemon')
G.edge['cellgeofenced']['mm-pp-daemon']['write-read'] = '[open open][write read][append read]'
G.add_edge('cellgeofenced','mm-pp-daemon')
G.edge['cellgeofenced']['mm-pp-daemon']['write-read'] = '[open open][write read][append read][write read]'
G.edge['cellgeofenced']['mm-pp-daemon']['fill'] = 'red'
G.add_edge('cellgeofenced','mm-qcamera-daemon')
G.edge['cellgeofenced']['mm-qcamera-daemon']['write-read'] = '[open open][write read]'
G.edge['cellgeofenced']['mm-qcamera-daemon']['fill'] = 'red'
G.add_edge('cellgeofenced','mm-qcamera-daemon')
G.edge['cellgeofenced']['mm-qcamera-daemon']['write-read'] = '[open open][write read][append read]'
G.add_edge('cellgeofenced','mpdecision')
G.edge['cellgeofenced']['mpdecision']['write-read'] = '[open open][write read]'
G.edge['cellgeofenced']['mpdecision']['fill'] = 'red'
G.add_edge('cellgeofenced','mpdecision')
G.edge['cellgeofenced']['mpdecision']['write-read'] = '[open open][write read][append read]'
G.add_edge('cellgeofenced','mpdecision')
G.edge['cellgeofenced']['mpdecision']['write-read'] = '[open open][write read][append read][write read]'
G.edge['cellgeofenced']['mpdecision']['fill'] = 'red'
G.add_edge('cellgeofenced','netd')
G.edge['cellgeofenced']['netd']['write-read'] = '[write read]'
G.edge['cellgeofenced']['netd']['fill'] = 'red'
G.add_edge('cellgeofenced','netmgrd')
G.edge['cellgeofenced']['netmgrd']['write-read'] = '[write read]'
G.edge['cellgeofenced']['netmgrd']['fill'] = 'red'
G.add_edge('cellgeofenced','nfc')
G.edge['cellgeofenced']['nfc']['write-read'] = '[write read]'
G.edge['cellgeofenced']['nfc']['fill'] = 'red'
G.add_edge('cellgeofenced','oneseg_mw')
G.edge['cellgeofenced']['oneseg_mw']['write-read'] = '[open open][write read]'
G.edge['cellgeofenced']['oneseg_mw']['fill'] = 'red'
G.add_edge('cellgeofenced','oneseg_mw')
G.edge['cellgeofenced']['oneseg_mw']['write-read'] = '[open open][write read][append read]'
G.add_edge('cellgeofenced','perfd')
G.edge['cellgeofenced']['perfd']['write-read'] = '[write read]'
G.edge['cellgeofenced']['perfd']['fill'] = 'red'
G.add_edge('cellgeofenced','qcks')
G.edge['cellgeofenced']['qcks']['write-read'] = '[open open][append read][open open][write read]'
G.edge['cellgeofenced']['qcks']['fill'] = 'red'
G.add_edge('cellgeofenced','qcks')
G.edge['cellgeofenced']['qcks']['write-read'] = '[open open][append read][open open][write read][append read]'
G.add_edge('cellgeofenced','qmuxd')
G.edge['cellgeofenced']['qmuxd']['write-read'] = '[open open][open open][append read][write read][append read][open open][write read]'
G.edge['cellgeofenced']['qmuxd']['fill'] = 'red'
G.add_edge('cellgeofenced','qmuxd')
G.edge['cellgeofenced']['qmuxd']['write-read'] = '[open open][open open][append read][write read][append read][open open][write read][append read]'
G.add_edge('cellgeofenced','qosmgr')
G.edge['cellgeofenced']['qosmgr']['write-read'] = '[write read]'
G.edge['cellgeofenced']['qosmgr']['fill'] = 'red'
G.add_edge('cellgeofenced','radio')
G.edge['cellgeofenced']['radio']['write-read'] = '[open open][append read]'
G.add_edge('cellgeofenced','rild')
G.edge['cellgeofenced']['rild']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read]'
G.edge['cellgeofenced']['rild']['fill'] = 'red'
G.add_edge('cellgeofenced','rild')
G.edge['cellgeofenced']['rild']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('cellgeofenced','rmt_storage')
G.edge['cellgeofenced']['rmt_storage']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['cellgeofenced']['rmt_storage']['fill'] = 'red'
G.add_edge('cellgeofenced','rmt_storage')
G.edge['cellgeofenced']['rmt_storage']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('cellgeofenced','rtcc')
G.edge['cellgeofenced']['rtcc']['write-read'] = '[setattr getattr][setattr getattr][write read]'
G.edge['cellgeofenced']['rtcc']['fill'] = 'red'
G.add_edge('cellgeofenced','sec-ril')
G.edge['cellgeofenced']['sec-ril']['write-read'] = '[open open][write read][open open][setattr getattr][write read]'
G.edge['cellgeofenced']['sec-ril']['fill'] = 'red'
G.add_edge('cellgeofenced','sec-ril')
G.edge['cellgeofenced']['sec-ril']['write-read'] = '[open open][write read][open open][setattr getattr][write read][append read]'
G.add_edge('cellgeofenced','sensorhubservice')
G.edge['cellgeofenced']['sensorhubservice']['write-read'] = '[write read]'
G.edge['cellgeofenced']['sensorhubservice']['fill'] = 'red'
G.add_edge('cellgeofenced','smdexe')
G.edge['cellgeofenced']['smdexe']['write-read'] = '[open open][write read]'
G.edge['cellgeofenced']['smdexe']['fill'] = 'red'
G.add_edge('cellgeofenced','smdexe')
G.edge['cellgeofenced']['smdexe']['write-read'] = '[open open][write read][append read]'
G.add_edge('cellgeofenced','ssr_setup')
G.edge['cellgeofenced']['ssr_setup']['write-read'] = '[open open][write read]'
G.edge['cellgeofenced']['ssr_setup']['fill'] = 'red'
G.add_edge('cellgeofenced','ssr_setup')
G.edge['cellgeofenced']['ssr_setup']['write-read'] = '[open open][write read][append read]'
G.add_edge('cellgeofenced','sswap')
G.edge['cellgeofenced']['sswap']['write-read'] = '[open open][write read]'
G.edge['cellgeofenced']['sswap']['fill'] = 'red'
G.add_edge('cellgeofenced','sswap')
G.edge['cellgeofenced']['sswap']['write-read'] = '[open open][write read][append read]'
G.add_edge('cellgeofenced','surfaceflinger')
G.edge['cellgeofenced']['surfaceflinger']['write-read'] = '[open open][write read]'
G.edge['cellgeofenced']['surfaceflinger']['fill'] = 'red'
G.add_edge('cellgeofenced','surfaceflinger')
G.edge['cellgeofenced']['surfaceflinger']['write-read'] = '[open open][write read][append read]'
G.add_edge('cellgeofenced','surfaceflinger')
G.edge['cellgeofenced']['surfaceflinger']['write-read'] = '[open open][write read][append read][write read]'
G.edge['cellgeofenced']['surfaceflinger']['fill'] = 'red'
G.add_edge('cellgeofenced','system_server')
G.edge['cellgeofenced']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][open open][setattr getattr][write read]'
G.edge['cellgeofenced']['system_server']['fill'] = 'red'
G.add_edge('cellgeofenced','system_server')
G.edge['cellgeofenced']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][open open][setattr getattr][write read][append read]'
G.add_edge('cellgeofenced','system_server')
G.edge['cellgeofenced']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][open open][setattr getattr][write read][append read][write read]'
G.edge['cellgeofenced']['system_server']['fill'] = 'red'
G.add_edge('cellgeofenced','system_server')
G.edge['cellgeofenced']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read]'
G.add_edge('cellgeofenced','thermald')
G.edge['cellgeofenced']['thermald']['write-read'] = '[write read]'
G.edge['cellgeofenced']['thermald']['fill'] = 'red'
G.add_edge('cellgeofenced','thermal-engine')
G.edge['cellgeofenced']['thermal-engine']['write-read'] = '[open open][write read]'
G.edge['cellgeofenced']['thermal-engine']['fill'] = 'red'
G.add_edge('cellgeofenced','thermal-engine')
G.edge['cellgeofenced']['thermal-engine']['write-read'] = '[open open][write read][append read]'
G.add_edge('cellgeofenced','thermal-engine')
G.edge['cellgeofenced']['thermal-engine']['write-read'] = '[open open][write read][append read][write read]'
G.edge['cellgeofenced']['thermal-engine']['fill'] = 'red'
G.add_edge('cellgeofenced','ueventd')
G.edge['cellgeofenced']['ueventd']['write-read'] = '[setattr getattr][open open][write read]'
G.edge['cellgeofenced']['ueventd']['fill'] = 'red'
G.add_edge('cellgeofenced','ueventd')
G.edge['cellgeofenced']['ueventd']['write-read'] = '[setattr getattr][open open][write read][append read]'
G.add_edge('cellgeofenced','vm_bms')
G.edge['cellgeofenced']['vm_bms']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['cellgeofenced']['vm_bms']['fill'] = 'red'
G.add_edge('cellgeofenced','vm_bms')
G.edge['cellgeofenced']['vm_bms']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('cellgeofenced','vmwared')
G.edge['cellgeofenced']['vmwared']['write-read'] = '[write read]'
G.edge['cellgeofenced']['vmwared']['fill'] = 'red'
G.add_edge('cellgeofenced','vold')
G.edge['cellgeofenced']['vold']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['cellgeofenced']['vold']['fill'] = 'red'
G.add_edge('cellgeofenced','vold')
G.edge['cellgeofenced']['vold']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('cellgeofenced','zygote')
G.edge['cellgeofenced']['zygote']['write-read'] = '[write read]'
G.edge['cellgeofenced']['zygote']['fill'] = 'red'
G.add_edge('charger_monitor','at_distributor')
G.edge['charger_monitor']['at_distributor']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('charger_monitor','bauthserver')
G.edge['charger_monitor']['bauthserver']['write-read'] = '[open open]'
G.add_edge('charger_monitor','bintvoutservice')
G.edge['charger_monitor']['bintvoutservice']['write-read'] = '[open open]'
G.add_edge('charger_monitor','bluetooth')
G.edge['charger_monitor']['bluetooth']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('charger_monitor','cbd')
G.edge['charger_monitor']['cbd']['write-read'] = '[open open]'
G.add_edge('charger_monitor','cellgeofenced')
G.edge['charger_monitor']['cellgeofenced']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('charger_monitor','charger_monitor')
G.edge['charger_monitor']['charger_monitor']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('charger_monitor','charger_monitor')
G.edge['charger_monitor']['charger_monitor']['write-read'] = '[open open][write read][append read][open open][open open]'
G.add_edge('charger_monitor','cnd')
G.edge['charger_monitor']['cnd']['write-read'] = '[open open][append read][open open]'
G.add_edge('charger_monitor','connfwexe')
G.edge['charger_monitor']['connfwexe']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('charger_monitor','debuggerd')
G.edge['charger_monitor']['debuggerd']['write-read'] = '[open open]'
G.add_edge('charger_monitor','diag_uart_log')
G.edge['charger_monitor']['diag_uart_log']['write-read'] = '[open open]'
G.add_edge('charger_monitor','dumpstate')
G.edge['charger_monitor']['dumpstate']['write-read'] = '[open open]'
G.add_edge('charger_monitor','efsks')
G.edge['charger_monitor']['efsks']['write-read'] = '[open open]'
G.add_edge('charger_monitor','geomagneticd')
G.edge['charger_monitor']['geomagneticd']['write-read'] = '[open open]'
G.add_edge('charger_monitor','gpsd')
G.edge['charger_monitor']['gpsd']['write-read'] = '[open open]'
G.add_edge('charger_monitor','init_shell')
G.edge['charger_monitor']['init_shell']['write-read'] = '[open open]'
G.add_edge('charger_monitor','kiesexe')
G.edge['charger_monitor']['kiesexe']['write-read'] = '[open open]'
G.add_edge('charger_monitor','ks')
G.edge['charger_monitor']['ks']['write-read'] = '[open open][append read][open open]'
G.add_edge('charger_monitor','lhd')
G.edge['charger_monitor']['lhd']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('charger_monitor','lpm')
G.edge['charger_monitor']['lpm']['write-read'] = '[open open]'
G.add_edge('charger_monitor','macloader')
G.edge['charger_monitor']['macloader']['write-read'] = '[open open]'
G.add_edge('charger_monitor','mdm_helper')
G.edge['charger_monitor']['mdm_helper']['write-read'] = '[open open][append read][open open]'
G.add_edge('charger_monitor','mediaserver')
G.edge['charger_monitor']['mediaserver']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('charger_monitor','mlexe')
G.edge['charger_monitor']['mlexe']['write-read'] = '[open open]'
G.add_edge('charger_monitor','mm-pp-daemon')
G.edge['charger_monitor']['mm-pp-daemon']['write-read'] = '[open open]'
G.add_edge('charger_monitor','mm-qcamera-daemon')
G.edge['charger_monitor']['mm-qcamera-daemon']['write-read'] = '[open open]'
G.add_edge('charger_monitor','mpdecision')
G.edge['charger_monitor']['mpdecision']['write-read'] = '[open open]'
G.add_edge('charger_monitor','oneseg_mw')
G.edge['charger_monitor']['oneseg_mw']['write-read'] = '[open open]'
G.add_edge('charger_monitor','qcks')
G.edge['charger_monitor']['qcks']['write-read'] = '[open open][append read][open open]'
G.add_edge('charger_monitor','qmuxd')
G.edge['charger_monitor']['qmuxd']['write-read'] = '[open open][open open][append read][write read][append read][open open]'
G.add_edge('charger_monitor','radio')
G.edge['charger_monitor']['radio']['write-read'] = '[open open]'
G.add_edge('charger_monitor','rild')
G.edge['charger_monitor']['rild']['write-read'] = '[write read][append read][open open][write read][append read][open open]'
G.add_edge('charger_monitor','rmt_storage')
G.edge['charger_monitor']['rmt_storage']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('charger_monitor','sec-ril')
G.edge['charger_monitor']['sec-ril']['write-read'] = '[open open][write read][open open]'
G.add_edge('charger_monitor','smdexe')
G.edge['charger_monitor']['smdexe']['write-read'] = '[open open]'
G.add_edge('charger_monitor','ssr_setup')
G.edge['charger_monitor']['ssr_setup']['write-read'] = '[open open]'
G.add_edge('charger_monitor','sswap')
G.edge['charger_monitor']['sswap']['write-read'] = '[open open]'
G.add_edge('charger_monitor','surfaceflinger')
G.edge['charger_monitor']['surfaceflinger']['write-read'] = '[write read][append read][open open]'
G.add_edge('charger_monitor','system_server')
G.edge['charger_monitor']['system_server']['write-read'] = '[write read][append read][open open][write read][append read][open open]'
G.add_edge('charger_monitor','system_server')
G.edge['charger_monitor']['system_server']['write-read'] = '[write read][append read][open open][write read][append read][open open][open open]'
G.add_edge('charger_monitor','thermal-engine')
G.edge['charger_monitor']['thermal-engine']['write-read'] = '[open open]'
G.add_edge('charger_monitor','ueventd')
G.edge['charger_monitor']['ueventd']['write-read'] = '[write read][append read][open open]'
G.add_edge('charger_monitor','vm_bms')
G.edge['charger_monitor']['vm_bms']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('charger_monitor','vold')
G.edge['charger_monitor']['vold']['write-read'] = '[write read][append read][open open][write read][append read][open open]'
G.add_edge('charger_monitor','init_shell')
G.edge['charger_monitor']['init_shell']['write-read'] = '[open open][setattr getattr]'
G.add_edge('charger_monitor','rild')
G.edge['charger_monitor']['rild']['write-read'] = '[write read][append read][open open][write read][append read][open open][setattr getattr]'
G.add_edge('charger_monitor','rtcc')
G.edge['charger_monitor']['rtcc']['write-read'] = '[setattr getattr]'
G.add_edge('charger_monitor','sec-ril')
G.edge['charger_monitor']['sec-ril']['write-read'] = '[open open][write read][open open][setattr getattr]'
G.add_edge('charger_monitor','system_server')
G.edge['charger_monitor']['system_server']['write-read'] = '[write read][append read][open open][write read][append read][open open][open open][setattr getattr]'
G.add_edge('charger_monitor','at_distributor')
G.edge['charger_monitor']['at_distributor']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['charger_monitor']['at_distributor']['fill'] = 'red'
G.add_edge('charger_monitor','at_distributor')
G.edge['charger_monitor']['at_distributor']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('charger_monitor','bauthserver')
G.edge['charger_monitor']['bauthserver']['write-read'] = '[open open][write read]'
G.edge['charger_monitor']['bauthserver']['fill'] = 'red'
G.add_edge('charger_monitor','bauthserver')
G.edge['charger_monitor']['bauthserver']['write-read'] = '[open open][write read][append read]'
G.add_edge('charger_monitor','bintvoutservice')
G.edge['charger_monitor']['bintvoutservice']['write-read'] = '[open open][write read]'
G.edge['charger_monitor']['bintvoutservice']['fill'] = 'red'
G.add_edge('charger_monitor','bintvoutservice')
G.edge['charger_monitor']['bintvoutservice']['write-read'] = '[open open][write read][append read]'
G.add_edge('charger_monitor','bluetooth')
G.edge['charger_monitor']['bluetooth']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['charger_monitor']['bluetooth']['fill'] = 'red'
G.add_edge('charger_monitor','bluetooth')
G.edge['charger_monitor']['bluetooth']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('charger_monitor','bootanim')
G.edge['charger_monitor']['bootanim']['write-read'] = '[write read]'
G.edge['charger_monitor']['bootanim']['fill'] = 'red'
G.add_edge('charger_monitor','cbd')
G.edge['charger_monitor']['cbd']['write-read'] = '[open open][write read]'
G.edge['charger_monitor']['cbd']['fill'] = 'red'
G.add_edge('charger_monitor','cbd')
G.edge['charger_monitor']['cbd']['write-read'] = '[open open][write read][append read]'
G.add_edge('charger_monitor','cellgeofenced')
G.edge['charger_monitor']['cellgeofenced']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['charger_monitor']['cellgeofenced']['fill'] = 'red'
G.add_edge('charger_monitor','cellgeofenced')
G.edge['charger_monitor']['cellgeofenced']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('charger_monitor','charger_monitor')
G.edge['charger_monitor']['charger_monitor']['write-read'] = '[open open][write read][append read][open open][open open][write read]'
G.edge['charger_monitor']['charger_monitor']['fill'] = 'red'
G.add_edge('charger_monitor','charger_monitor')
G.edge['charger_monitor']['charger_monitor']['write-read'] = '[open open][write read][append read][open open][open open][write read][append read]'
G.add_edge('charger_monitor','charger_monitor')
G.edge['charger_monitor']['charger_monitor']['write-read'] = '[open open][write read][append read][open open][open open][write read][append read][write read]'
G.edge['charger_monitor']['charger_monitor']['fill'] = 'red'
G.add_edge('charger_monitor','charger_monitor')
G.edge['charger_monitor']['charger_monitor']['write-read'] = '[open open][write read][append read][open open][open open][write read][append read][write read][append read]'
G.add_edge('charger_monitor','cnd')
G.edge['charger_monitor']['cnd']['write-read'] = '[open open][append read][open open][write read]'
G.edge['charger_monitor']['cnd']['fill'] = 'red'
G.add_edge('charger_monitor','cnd')
G.edge['charger_monitor']['cnd']['write-read'] = '[open open][append read][open open][write read][append read]'
G.add_edge('charger_monitor','connfwexe')
G.edge['charger_monitor']['connfwexe']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['charger_monitor']['connfwexe']['fill'] = 'red'
G.add_edge('charger_monitor','connfwexe')
G.edge['charger_monitor']['connfwexe']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('charger_monitor','debuggerd')
G.edge['charger_monitor']['debuggerd']['write-read'] = '[open open][write read]'
G.edge['charger_monitor']['debuggerd']['fill'] = 'red'
G.add_edge('charger_monitor','debuggerd')
G.edge['charger_monitor']['debuggerd']['write-read'] = '[open open][write read][append read]'
G.add_edge('charger_monitor','diag_uart_log')
G.edge['charger_monitor']['diag_uart_log']['write-read'] = '[open open][write read]'
G.edge['charger_monitor']['diag_uart_log']['fill'] = 'red'
G.add_edge('charger_monitor','diag_uart_log')
G.edge['charger_monitor']['diag_uart_log']['write-read'] = '[open open][write read][append read]'
G.add_edge('charger_monitor','dumpstate')
G.edge['charger_monitor']['dumpstate']['write-read'] = '[open open][write read]'
G.edge['charger_monitor']['dumpstate']['fill'] = 'red'
G.add_edge('charger_monitor','dumpstate')
G.edge['charger_monitor']['dumpstate']['write-read'] = '[open open][write read][append read]'
G.add_edge('charger_monitor','efsks')
G.edge['charger_monitor']['efsks']['write-read'] = '[open open][write read]'
G.edge['charger_monitor']['efsks']['fill'] = 'red'
G.add_edge('charger_monitor','efsks')
G.edge['charger_monitor']['efsks']['write-read'] = '[open open][write read][append read]'
G.add_edge('charger_monitor','geomagneticd')
G.edge['charger_monitor']['geomagneticd']['write-read'] = '[open open][write read]'
G.edge['charger_monitor']['geomagneticd']['fill'] = 'red'
G.add_edge('charger_monitor','geomagneticd')
G.edge['charger_monitor']['geomagneticd']['write-read'] = '[open open][write read][append read]'
G.add_edge('charger_monitor','gpsd')
G.edge['charger_monitor']['gpsd']['write-read'] = '[open open][write read]'
G.edge['charger_monitor']['gpsd']['fill'] = 'red'
G.add_edge('charger_monitor','gpsd')
G.edge['charger_monitor']['gpsd']['write-read'] = '[open open][write read][append read]'
G.add_edge('charger_monitor','healthd')
G.edge['charger_monitor']['healthd']['write-read'] = '[write read][append read][open open][write read][append read][write read]'
G.edge['charger_monitor']['healthd']['fill'] = 'red'
G.add_edge('charger_monitor','init_shell')
G.edge['charger_monitor']['init_shell']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['charger_monitor']['init_shell']['fill'] = 'red'
G.add_edge('charger_monitor','init_shell')
G.edge['charger_monitor']['init_shell']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('charger_monitor','jackservice')
G.edge['charger_monitor']['jackservice']['write-read'] = '[write read]'
G.edge['charger_monitor']['jackservice']['fill'] = 'red'
G.add_edge('charger_monitor','kiesexe')
G.edge['charger_monitor']['kiesexe']['write-read'] = '[open open][write read]'
G.edge['charger_monitor']['kiesexe']['fill'] = 'red'
G.add_edge('charger_monitor','kiesexe')
G.edge['charger_monitor']['kiesexe']['write-read'] = '[open open][write read][append read]'
G.add_edge('charger_monitor','ks')
G.edge['charger_monitor']['ks']['write-read'] = '[open open][append read][open open][write read]'
G.edge['charger_monitor']['ks']['fill'] = 'red'
G.add_edge('charger_monitor','ks')
G.edge['charger_monitor']['ks']['write-read'] = '[open open][append read][open open][write read][append read]'
G.add_edge('charger_monitor','lhd')
G.edge['charger_monitor']['lhd']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['charger_monitor']['lhd']['fill'] = 'red'
G.add_edge('charger_monitor','lhd')
G.edge['charger_monitor']['lhd']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('charger_monitor','lmkd')
G.edge['charger_monitor']['lmkd']['write-read'] = '[write read]'
G.edge['charger_monitor']['lmkd']['fill'] = 'red'
G.add_edge('charger_monitor','lpm')
G.edge['charger_monitor']['lpm']['write-read'] = '[open open][write read]'
G.edge['charger_monitor']['lpm']['fill'] = 'red'
G.add_edge('charger_monitor','lpm')
G.edge['charger_monitor']['lpm']['write-read'] = '[open open][write read][append read]'
G.add_edge('charger_monitor','macloader')
G.edge['charger_monitor']['macloader']['write-read'] = '[open open][write read]'
G.edge['charger_monitor']['macloader']['fill'] = 'red'
G.add_edge('charger_monitor','macloader')
G.edge['charger_monitor']['macloader']['write-read'] = '[open open][write read][append read]'
G.add_edge('charger_monitor','mdm_helper')
G.edge['charger_monitor']['mdm_helper']['write-read'] = '[open open][append read][open open][write read]'
G.edge['charger_monitor']['mdm_helper']['fill'] = 'red'
G.add_edge('charger_monitor','mediaserver')
G.edge['charger_monitor']['mediaserver']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['charger_monitor']['mediaserver']['fill'] = 'red'
G.add_edge('charger_monitor','mediaserver')
G.edge['charger_monitor']['mediaserver']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('charger_monitor','mfgloader')
G.edge['charger_monitor']['mfgloader']['write-read'] = '[write read]'
G.edge['charger_monitor']['mfgloader']['fill'] = 'red'
G.add_edge('charger_monitor','mlexe')
G.edge['charger_monitor']['mlexe']['write-read'] = '[open open][write read]'
G.edge['charger_monitor']['mlexe']['fill'] = 'red'
G.add_edge('charger_monitor','mlexe')
G.edge['charger_monitor']['mlexe']['write-read'] = '[open open][write read][append read]'
G.add_edge('charger_monitor','mm-pp-daemon')
G.edge['charger_monitor']['mm-pp-daemon']['write-read'] = '[open open][write read]'
G.edge['charger_monitor']['mm-pp-daemon']['fill'] = 'red'
G.add_edge('charger_monitor','mm-pp-daemon')
G.edge['charger_monitor']['mm-pp-daemon']['write-read'] = '[open open][write read][append read]'
G.add_edge('charger_monitor','mm-pp-daemon')
G.edge['charger_monitor']['mm-pp-daemon']['write-read'] = '[open open][write read][append read][write read]'
G.edge['charger_monitor']['mm-pp-daemon']['fill'] = 'red'
G.add_edge('charger_monitor','mm-qcamera-daemon')
G.edge['charger_monitor']['mm-qcamera-daemon']['write-read'] = '[open open][write read]'
G.edge['charger_monitor']['mm-qcamera-daemon']['fill'] = 'red'
G.add_edge('charger_monitor','mm-qcamera-daemon')
G.edge['charger_monitor']['mm-qcamera-daemon']['write-read'] = '[open open][write read][append read]'
G.add_edge('charger_monitor','mpdecision')
G.edge['charger_monitor']['mpdecision']['write-read'] = '[open open][write read]'
G.edge['charger_monitor']['mpdecision']['fill'] = 'red'
G.add_edge('charger_monitor','mpdecision')
G.edge['charger_monitor']['mpdecision']['write-read'] = '[open open][write read][append read]'
G.add_edge('charger_monitor','mpdecision')
G.edge['charger_monitor']['mpdecision']['write-read'] = '[open open][write read][append read][write read]'
G.edge['charger_monitor']['mpdecision']['fill'] = 'red'
G.add_edge('charger_monitor','netd')
G.edge['charger_monitor']['netd']['write-read'] = '[write read][append read][write read]'
G.edge['charger_monitor']['netd']['fill'] = 'red'
G.add_edge('charger_monitor','netmgrd')
G.edge['charger_monitor']['netmgrd']['write-read'] = '[write read]'
G.edge['charger_monitor']['netmgrd']['fill'] = 'red'
G.add_edge('charger_monitor','nfc')
G.edge['charger_monitor']['nfc']['write-read'] = '[write read]'
G.edge['charger_monitor']['nfc']['fill'] = 'red'
G.add_edge('charger_monitor','oneseg_mw')
G.edge['charger_monitor']['oneseg_mw']['write-read'] = '[open open][write read]'
G.edge['charger_monitor']['oneseg_mw']['fill'] = 'red'
G.add_edge('charger_monitor','oneseg_mw')
G.edge['charger_monitor']['oneseg_mw']['write-read'] = '[open open][write read][append read]'
G.add_edge('charger_monitor','perfd')
G.edge['charger_monitor']['perfd']['write-read'] = '[write read]'
G.edge['charger_monitor']['perfd']['fill'] = 'red'
G.add_edge('charger_monitor','qcks')
G.edge['charger_monitor']['qcks']['write-read'] = '[open open][append read][open open][write read]'
G.edge['charger_monitor']['qcks']['fill'] = 'red'
G.add_edge('charger_monitor','qcks')
G.edge['charger_monitor']['qcks']['write-read'] = '[open open][append read][open open][write read][append read]'
G.add_edge('charger_monitor','qmuxd')
G.edge['charger_monitor']['qmuxd']['write-read'] = '[open open][open open][append read][write read][append read][open open][write read]'
G.edge['charger_monitor']['qmuxd']['fill'] = 'red'
G.add_edge('charger_monitor','qmuxd')
G.edge['charger_monitor']['qmuxd']['write-read'] = '[open open][open open][append read][write read][append read][open open][write read][append read]'
G.add_edge('charger_monitor','qosmgr')
G.edge['charger_monitor']['qosmgr']['write-read'] = '[write read]'
G.edge['charger_monitor']['qosmgr']['fill'] = 'red'
G.add_edge('charger_monitor','radio')
G.edge['charger_monitor']['radio']['write-read'] = '[open open][append read]'
G.add_edge('charger_monitor','rild')
G.edge['charger_monitor']['rild']['write-read'] = '[write read][append read][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['charger_monitor']['rild']['fill'] = 'red'
G.add_edge('charger_monitor','rild')
G.edge['charger_monitor']['rild']['write-read'] = '[write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('charger_monitor','rmt_storage')
G.edge['charger_monitor']['rmt_storage']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['charger_monitor']['rmt_storage']['fill'] = 'red'
G.add_edge('charger_monitor','rmt_storage')
G.edge['charger_monitor']['rmt_storage']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('charger_monitor','rtcc')
G.edge['charger_monitor']['rtcc']['write-read'] = '[setattr getattr][write read]'
G.edge['charger_monitor']['rtcc']['fill'] = 'red'
G.add_edge('charger_monitor','sec-ril')
G.edge['charger_monitor']['sec-ril']['write-read'] = '[open open][write read][open open][setattr getattr][write read]'
G.edge['charger_monitor']['sec-ril']['fill'] = 'red'
G.add_edge('charger_monitor','sec-ril')
G.edge['charger_monitor']['sec-ril']['write-read'] = '[open open][write read][open open][setattr getattr][write read][append read]'
G.add_edge('charger_monitor','sensorhubservice')
G.edge['charger_monitor']['sensorhubservice']['write-read'] = '[write read]'
G.edge['charger_monitor']['sensorhubservice']['fill'] = 'red'
G.add_edge('charger_monitor','smdexe')
G.edge['charger_monitor']['smdexe']['write-read'] = '[open open][write read]'
G.edge['charger_monitor']['smdexe']['fill'] = 'red'
G.add_edge('charger_monitor','smdexe')
G.edge['charger_monitor']['smdexe']['write-read'] = '[open open][write read][append read]'
G.add_edge('charger_monitor','ssr_setup')
G.edge['charger_monitor']['ssr_setup']['write-read'] = '[open open][write read]'
G.edge['charger_monitor']['ssr_setup']['fill'] = 'red'
G.add_edge('charger_monitor','ssr_setup')
G.edge['charger_monitor']['ssr_setup']['write-read'] = '[open open][write read][append read]'
G.add_edge('charger_monitor','sswap')
G.edge['charger_monitor']['sswap']['write-read'] = '[open open][write read]'
G.edge['charger_monitor']['sswap']['fill'] = 'red'
G.add_edge('charger_monitor','sswap')
G.edge['charger_monitor']['sswap']['write-read'] = '[open open][write read][append read]'
G.add_edge('charger_monitor','surfaceflinger')
G.edge['charger_monitor']['surfaceflinger']['write-read'] = '[write read][append read][open open][write read]'
G.edge['charger_monitor']['surfaceflinger']['fill'] = 'red'
G.add_edge('charger_monitor','surfaceflinger')
G.edge['charger_monitor']['surfaceflinger']['write-read'] = '[write read][append read][open open][write read][append read]'
G.add_edge('charger_monitor','surfaceflinger')
G.edge['charger_monitor']['surfaceflinger']['write-read'] = '[write read][append read][open open][write read][append read][write read]'
G.edge['charger_monitor']['surfaceflinger']['fill'] = 'red'
G.add_edge('charger_monitor','system_server')
G.edge['charger_monitor']['system_server']['write-read'] = '[write read][append read][open open][write read][append read][open open][open open][setattr getattr][write read]'
G.edge['charger_monitor']['system_server']['fill'] = 'red'
G.add_edge('charger_monitor','system_server')
G.edge['charger_monitor']['system_server']['write-read'] = '[write read][append read][open open][write read][append read][open open][open open][setattr getattr][write read][append read]'
G.add_edge('charger_monitor','system_server')
G.edge['charger_monitor']['system_server']['write-read'] = '[write read][append read][open open][write read][append read][open open][open open][setattr getattr][write read][append read][write read]'
G.edge['charger_monitor']['system_server']['fill'] = 'red'
G.add_edge('charger_monitor','system_server')
G.edge['charger_monitor']['system_server']['write-read'] = '[write read][append read][open open][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read]'
G.add_edge('charger_monitor','thermald')
G.edge['charger_monitor']['thermald']['write-read'] = '[write read]'
G.edge['charger_monitor']['thermald']['fill'] = 'red'
G.add_edge('charger_monitor','thermal-engine')
G.edge['charger_monitor']['thermal-engine']['write-read'] = '[open open][write read]'
G.edge['charger_monitor']['thermal-engine']['fill'] = 'red'
G.add_edge('charger_monitor','thermal-engine')
G.edge['charger_monitor']['thermal-engine']['write-read'] = '[open open][write read][append read]'
G.add_edge('charger_monitor','thermal-engine')
G.edge['charger_monitor']['thermal-engine']['write-read'] = '[open open][write read][append read][write read]'
G.edge['charger_monitor']['thermal-engine']['fill'] = 'red'
G.add_edge('charger_monitor','ueventd')
G.edge['charger_monitor']['ueventd']['write-read'] = '[write read][append read][open open][write read]'
G.edge['charger_monitor']['ueventd']['fill'] = 'red'
G.add_edge('charger_monitor','ueventd')
G.edge['charger_monitor']['ueventd']['write-read'] = '[write read][append read][open open][write read][append read]'
G.add_edge('charger_monitor','vm_bms')
G.edge['charger_monitor']['vm_bms']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['charger_monitor']['vm_bms']['fill'] = 'red'
G.add_edge('charger_monitor','vm_bms')
G.edge['charger_monitor']['vm_bms']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('charger_monitor','vmwared')
G.edge['charger_monitor']['vmwared']['write-read'] = '[write read]'
G.edge['charger_monitor']['vmwared']['fill'] = 'red'
G.add_edge('charger_monitor','vold')
G.edge['charger_monitor']['vold']['write-read'] = '[write read][append read][open open][write read][append read][open open][write read]'
G.edge['charger_monitor']['vold']['fill'] = 'red'
G.add_edge('charger_monitor','vold')
G.edge['charger_monitor']['vold']['write-read'] = '[write read][append read][open open][write read][append read][open open][write read][append read]'
G.add_edge('charger_monitor','zygote')
G.edge['charger_monitor']['zygote']['write-read'] = '[write read]'
G.edge['charger_monitor']['zygote']['fill'] = 'red'
G.add_edge('connfwexe','at_distributor')
G.edge['connfwexe']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('connfwexe','bauthserver')
G.edge['connfwexe']['bauthserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('connfwexe','bintvoutservice')
G.edge['connfwexe']['bintvoutservice']['write-read'] = '[open open]'
G.add_edge('connfwexe','bluetooth')
G.edge['connfwexe']['bluetooth']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('connfwexe','cbd')
G.edge['connfwexe']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('connfwexe','cellgeofenced')
G.edge['connfwexe']['cellgeofenced']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('connfwexe','charger_monitor')
G.edge['connfwexe']['charger_monitor']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('connfwexe','charger_monitor')
G.edge['connfwexe']['charger_monitor']['write-read'] = '[open open][write read][append read][open open][open open]'
G.add_edge('connfwexe','cnd')
G.edge['connfwexe']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][append read][open open]'
G.add_edge('connfwexe','connfwexe')
G.edge['connfwexe']['connfwexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('connfwexe','debuggerd')
G.edge['connfwexe']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('connfwexe','diag_uart_log')
G.edge['connfwexe']['diag_uart_log']['write-read'] = '[open open]'
G.add_edge('connfwexe','dumpstate')
G.edge['connfwexe']['dumpstate']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('connfwexe','efsks')
G.edge['connfwexe']['efsks']['write-read'] = '[open open][write read][add_name search][open open]'
G.add_edge('connfwexe','geomagneticd')
G.edge['connfwexe']['geomagneticd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open]'
G.add_edge('connfwexe','gpsd')
G.edge['connfwexe']['gpsd']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('connfwexe','init_shell')
G.edge['connfwexe']['init_shell']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('connfwexe','kiesexe')
G.edge['connfwexe']['kiesexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('connfwexe','ks')
G.edge['connfwexe']['ks']['write-read'] = '[open open][write read][add_name search][open open][append read][open open]'
G.add_edge('connfwexe','lhd')
G.edge['connfwexe']['lhd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('connfwexe','lpm')
G.edge['connfwexe']['lpm']['write-read'] = '[open open]'
G.add_edge('connfwexe','macloader')
G.edge['connfwexe']['macloader']['write-read'] = '[open open]'
G.add_edge('connfwexe','mdm_helper')
G.edge['connfwexe']['mdm_helper']['write-read'] = '[write read][open open][append read][open open]'
G.add_edge('connfwexe','mediaserver')
G.edge['connfwexe']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('connfwexe','mlexe')
G.edge['connfwexe']['mlexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('connfwexe','mm-pp-daemon')
G.edge['connfwexe']['mm-pp-daemon']['write-read'] = '[open open]'
G.add_edge('connfwexe','mm-qcamera-daemon')
G.edge['connfwexe']['mm-qcamera-daemon']['write-read'] = '[open open][write read][add_name search][remove_name search][open open]'
G.add_edge('connfwexe','mpdecision')
G.edge['connfwexe']['mpdecision']['write-read'] = '[open open][write read][add_name search][remove_name search][open open]'
G.add_edge('connfwexe','oneseg_mw')
G.edge['connfwexe']['oneseg_mw']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('connfwexe','qcks')
G.edge['connfwexe']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][append read][open open]'
G.add_edge('connfwexe','qmuxd')
G.edge['connfwexe']['qmuxd']['write-read'] = '[open open][open open][append read][write read][append read][open open]'
G.add_edge('connfwexe','radio')
G.edge['connfwexe']['radio']['write-read'] = '[open open]'
G.add_edge('connfwexe','rild')
G.edge['connfwexe']['rild']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('connfwexe','rmt_storage')
G.edge['connfwexe']['rmt_storage']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('connfwexe','sec-ril')
G.edge['connfwexe']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][open open]'
G.add_edge('connfwexe','smdexe')
G.edge['connfwexe']['smdexe']['write-read'] = '[open open]'
G.add_edge('connfwexe','ssr_setup')
G.edge['connfwexe']['ssr_setup']['write-read'] = '[open open]'
G.add_edge('connfwexe','sswap')
G.edge['connfwexe']['sswap']['write-read'] = '[open open]'
G.add_edge('connfwexe','surfaceflinger')
G.edge['connfwexe']['surfaceflinger']['write-read'] = '[open open]'
G.add_edge('connfwexe','system_server')
G.edge['connfwexe']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('connfwexe','system_server')
G.edge['connfwexe']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][open open]'
G.add_edge('connfwexe','thermal-engine')
G.edge['connfwexe']['thermal-engine']['write-read'] = '[open open]'
G.add_edge('connfwexe','ueventd')
G.edge['connfwexe']['ueventd']['write-read'] = '[open open]'
G.add_edge('connfwexe','vm_bms')
G.edge['connfwexe']['vm_bms']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('connfwexe','vold')
G.edge['connfwexe']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('connfwexe','init_shell')
G.edge['connfwexe']['init_shell']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('connfwexe','rild')
G.edge['connfwexe']['rild']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr]'
G.add_edge('connfwexe','rtcc')
G.edge['connfwexe']['rtcc']['write-read'] = '[setattr getattr]'
G.add_edge('connfwexe','sec-ril')
G.edge['connfwexe']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][open open][setattr getattr]'
G.add_edge('connfwexe','system_server')
G.edge['connfwexe']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][open open][setattr getattr]'
G.add_edge('connfwexe','at_distributor')
G.edge['connfwexe']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read]'
G.edge['connfwexe']['at_distributor']['fill'] = 'red'
G.add_edge('connfwexe','at_distributor')
G.edge['connfwexe']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read]'
G.add_edge('connfwexe','bauthserver')
G.edge['connfwexe']['bauthserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['connfwexe']['bauthserver']['fill'] = 'red'
G.add_edge('connfwexe','bauthserver')
G.edge['connfwexe']['bauthserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('connfwexe','bintvoutservice')
G.edge['connfwexe']['bintvoutservice']['write-read'] = '[open open][write read]'
G.edge['connfwexe']['bintvoutservice']['fill'] = 'red'
G.add_edge('connfwexe','bintvoutservice')
G.edge['connfwexe']['bintvoutservice']['write-read'] = '[open open][write read][append read]'
G.add_edge('connfwexe','bluetooth')
G.edge['connfwexe']['bluetooth']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['connfwexe']['bluetooth']['fill'] = 'red'
G.add_edge('connfwexe','bluetooth')
G.edge['connfwexe']['bluetooth']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('connfwexe','bootanim')
G.edge['connfwexe']['bootanim']['write-read'] = '[write read]'
G.edge['connfwexe']['bootanim']['fill'] = 'red'
G.add_edge('connfwexe','cbd')
G.edge['connfwexe']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['connfwexe']['cbd']['fill'] = 'red'
G.add_edge('connfwexe','cbd')
G.edge['connfwexe']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('connfwexe','cellgeofenced')
G.edge['connfwexe']['cellgeofenced']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['connfwexe']['cellgeofenced']['fill'] = 'red'
G.add_edge('connfwexe','cellgeofenced')
G.edge['connfwexe']['cellgeofenced']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('connfwexe','charger_monitor')
G.edge['connfwexe']['charger_monitor']['write-read'] = '[open open][write read][append read][open open][open open][write read]'
G.edge['connfwexe']['charger_monitor']['fill'] = 'red'
G.add_edge('connfwexe','charger_monitor')
G.edge['connfwexe']['charger_monitor']['write-read'] = '[open open][write read][append read][open open][open open][write read][append read]'
G.add_edge('connfwexe','charger_monitor')
G.edge['connfwexe']['charger_monitor']['write-read'] = '[open open][write read][append read][open open][open open][write read][append read][write read]'
G.edge['connfwexe']['charger_monitor']['fill'] = 'red'
G.add_edge('connfwexe','charger_monitor')
G.edge['connfwexe']['charger_monitor']['write-read'] = '[open open][write read][append read][open open][open open][write read][append read][write read][append read]'
G.add_edge('connfwexe','cnd')
G.edge['connfwexe']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][append read][open open][write read]'
G.edge['connfwexe']['cnd']['fill'] = 'red'
G.add_edge('connfwexe','cnd')
G.edge['connfwexe']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][append read][open open][write read][append read]'
G.add_edge('connfwexe','connfwexe')
G.edge['connfwexe']['connfwexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read]'
G.edge['connfwexe']['connfwexe']['fill'] = 'red'
G.add_edge('connfwexe','connfwexe')
G.edge['connfwexe']['connfwexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read]'
G.add_edge('connfwexe','debuggerd')
G.edge['connfwexe']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['connfwexe']['debuggerd']['fill'] = 'red'
G.add_edge('connfwexe','debuggerd')
G.edge['connfwexe']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('connfwexe','diag_uart_log')
G.edge['connfwexe']['diag_uart_log']['write-read'] = '[open open][write read]'
G.edge['connfwexe']['diag_uart_log']['fill'] = 'red'
G.add_edge('connfwexe','diag_uart_log')
G.edge['connfwexe']['diag_uart_log']['write-read'] = '[open open][write read][append read]'
G.add_edge('connfwexe','dumpstate')
G.edge['connfwexe']['dumpstate']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read]'
G.edge['connfwexe']['dumpstate']['fill'] = 'red'
G.add_edge('connfwexe','dumpstate')
G.edge['connfwexe']['dumpstate']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('connfwexe','efsks')
G.edge['connfwexe']['efsks']['write-read'] = '[open open][write read][add_name search][open open][write read]'
G.edge['connfwexe']['efsks']['fill'] = 'red'
G.add_edge('connfwexe','efsks')
G.edge['connfwexe']['efsks']['write-read'] = '[open open][write read][add_name search][open open][write read][append read]'
G.add_edge('connfwexe','geomagneticd')
G.edge['connfwexe']['geomagneticd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['connfwexe']['geomagneticd']['fill'] = 'red'
G.add_edge('connfwexe','geomagneticd')
G.edge['connfwexe']['geomagneticd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('connfwexe','gpsd')
G.edge['connfwexe']['gpsd']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read]'
G.edge['connfwexe']['gpsd']['fill'] = 'red'
G.add_edge('connfwexe','gpsd')
G.edge['connfwexe']['gpsd']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('connfwexe','healthd')
G.edge['connfwexe']['healthd']['write-read'] = '[open open][write read][append read][write read]'
G.edge['connfwexe']['healthd']['fill'] = 'red'
G.add_edge('connfwexe','init_shell')
G.edge['connfwexe']['init_shell']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['connfwexe']['init_shell']['fill'] = 'red'
G.add_edge('connfwexe','init_shell')
G.edge['connfwexe']['init_shell']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('connfwexe','jackservice')
G.edge['connfwexe']['jackservice']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['connfwexe']['jackservice']['fill'] = 'red'
G.add_edge('connfwexe','kiesexe')
G.edge['connfwexe']['kiesexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['connfwexe']['kiesexe']['fill'] = 'red'
G.add_edge('connfwexe','kiesexe')
G.edge['connfwexe']['kiesexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('connfwexe','ks')
G.edge['connfwexe']['ks']['write-read'] = '[open open][write read][add_name search][open open][append read][open open][write read]'
G.edge['connfwexe']['ks']['fill'] = 'red'
G.add_edge('connfwexe','ks')
G.edge['connfwexe']['ks']['write-read'] = '[open open][write read][add_name search][open open][append read][open open][write read][append read]'
G.add_edge('connfwexe','lhd')
G.edge['connfwexe']['lhd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read]'
G.edge['connfwexe']['lhd']['fill'] = 'red'
G.add_edge('connfwexe','lhd')
G.edge['connfwexe']['lhd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read]'
G.add_edge('connfwexe','lmkd')
G.edge['connfwexe']['lmkd']['write-read'] = '[write read]'
G.edge['connfwexe']['lmkd']['fill'] = 'red'
G.add_edge('connfwexe','lpm')
G.edge['connfwexe']['lpm']['write-read'] = '[open open][write read]'
G.edge['connfwexe']['lpm']['fill'] = 'red'
G.add_edge('connfwexe','lpm')
G.edge['connfwexe']['lpm']['write-read'] = '[open open][write read][append read]'
G.add_edge('connfwexe','macloader')
G.edge['connfwexe']['macloader']['write-read'] = '[open open][write read]'
G.edge['connfwexe']['macloader']['fill'] = 'red'
G.add_edge('connfwexe','macloader')
G.edge['connfwexe']['macloader']['write-read'] = '[open open][write read][append read]'
G.add_edge('connfwexe','mdm_helper')
G.edge['connfwexe']['mdm_helper']['write-read'] = '[write read][open open][append read][open open][write read]'
G.edge['connfwexe']['mdm_helper']['fill'] = 'red'
G.add_edge('connfwexe','mediaserver')
G.edge['connfwexe']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read]'
G.edge['connfwexe']['mediaserver']['fill'] = 'red'
G.add_edge('connfwexe','mediaserver')
G.edge['connfwexe']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read]'
G.add_edge('connfwexe','mfgloader')
G.edge['connfwexe']['mfgloader']['write-read'] = '[open open][write read][add_name search][remove_name search][write read]'
G.edge['connfwexe']['mfgloader']['fill'] = 'red'
G.add_edge('connfwexe','mlexe')
G.edge['connfwexe']['mlexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['connfwexe']['mlexe']['fill'] = 'red'
G.add_edge('connfwexe','mlexe')
G.edge['connfwexe']['mlexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('connfwexe','mm-pp-daemon')
G.edge['connfwexe']['mm-pp-daemon']['write-read'] = '[open open][write read]'
G.edge['connfwexe']['mm-pp-daemon']['fill'] = 'red'
G.add_edge('connfwexe','mm-pp-daemon')
G.edge['connfwexe']['mm-pp-daemon']['write-read'] = '[open open][write read][append read]'
G.add_edge('connfwexe','mm-pp-daemon')
G.edge['connfwexe']['mm-pp-daemon']['write-read'] = '[open open][write read][append read][write read]'
G.edge['connfwexe']['mm-pp-daemon']['fill'] = 'red'
G.add_edge('connfwexe','mm-qcamera-daemon')
G.edge['connfwexe']['mm-qcamera-daemon']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['connfwexe']['mm-qcamera-daemon']['fill'] = 'red'
G.add_edge('connfwexe','mm-qcamera-daemon')
G.edge['connfwexe']['mm-qcamera-daemon']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('connfwexe','mpdecision')
G.edge['connfwexe']['mpdecision']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['connfwexe']['mpdecision']['fill'] = 'red'
G.add_edge('connfwexe','mpdecision')
G.edge['connfwexe']['mpdecision']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('connfwexe','mpdecision')
G.edge['connfwexe']['mpdecision']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read][write read]'
G.edge['connfwexe']['mpdecision']['fill'] = 'red'
G.add_edge('connfwexe','netd')
G.edge['connfwexe']['netd']['write-read'] = '[write read]'
G.edge['connfwexe']['netd']['fill'] = 'red'
G.add_edge('connfwexe','netmgrd')
G.edge['connfwexe']['netmgrd']['write-read'] = '[open open][open open][write read][write read][add_name search][add_name search][remove_name search][write read]'
G.edge['connfwexe']['netmgrd']['fill'] = 'red'
G.add_edge('connfwexe','nfc')
G.edge['connfwexe']['nfc']['write-read'] = '[write read]'
G.edge['connfwexe']['nfc']['fill'] = 'red'
G.add_edge('connfwexe','oneseg_mw')
G.edge['connfwexe']['oneseg_mw']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['connfwexe']['oneseg_mw']['fill'] = 'red'
G.add_edge('connfwexe','oneseg_mw')
G.edge['connfwexe']['oneseg_mw']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('connfwexe','perfd')
G.edge['connfwexe']['perfd']['write-read'] = '[write read]'
G.edge['connfwexe']['perfd']['fill'] = 'red'
G.add_edge('connfwexe','qcks')
G.edge['connfwexe']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][append read][open open][write read]'
G.edge['connfwexe']['qcks']['fill'] = 'red'
G.add_edge('connfwexe','qcks')
G.edge['connfwexe']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][append read][open open][write read][append read]'
G.add_edge('connfwexe','qmuxd')
G.edge['connfwexe']['qmuxd']['write-read'] = '[open open][open open][append read][write read][append read][open open][write read]'
G.edge['connfwexe']['qmuxd']['fill'] = 'red'
G.add_edge('connfwexe','qmuxd')
G.edge['connfwexe']['qmuxd']['write-read'] = '[open open][open open][append read][write read][append read][open open][write read][append read]'
G.add_edge('connfwexe','qosmgr')
G.edge['connfwexe']['qosmgr']['write-read'] = '[write read]'
G.edge['connfwexe']['qosmgr']['fill'] = 'red'
G.add_edge('connfwexe','radio')
G.edge['connfwexe']['radio']['write-read'] = '[open open][append read]'
G.add_edge('connfwexe','rild')
G.edge['connfwexe']['rild']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['connfwexe']['rild']['fill'] = 'red'
G.add_edge('connfwexe','rild')
G.edge['connfwexe']['rild']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('connfwexe','rmt_storage')
G.edge['connfwexe']['rmt_storage']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['connfwexe']['rmt_storage']['fill'] = 'red'
G.add_edge('connfwexe','rmt_storage')
G.edge['connfwexe']['rmt_storage']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('connfwexe','rtcc')
G.edge['connfwexe']['rtcc']['write-read'] = '[setattr getattr][write read]'
G.edge['connfwexe']['rtcc']['fill'] = 'red'
G.add_edge('connfwexe','sec-ril')
G.edge['connfwexe']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][open open][setattr getattr][write read]'
G.edge['connfwexe']['sec-ril']['fill'] = 'red'
G.add_edge('connfwexe','sec-ril')
G.edge['connfwexe']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][open open][setattr getattr][write read][append read]'
G.add_edge('connfwexe','sensorhubservice')
G.edge['connfwexe']['sensorhubservice']['write-read'] = '[write read]'
G.edge['connfwexe']['sensorhubservice']['fill'] = 'red'
G.add_edge('connfwexe','smdexe')
G.edge['connfwexe']['smdexe']['write-read'] = '[open open][write read]'
G.edge['connfwexe']['smdexe']['fill'] = 'red'
G.add_edge('connfwexe','smdexe')
G.edge['connfwexe']['smdexe']['write-read'] = '[open open][write read][append read]'
G.add_edge('connfwexe','ssr_setup')
G.edge['connfwexe']['ssr_setup']['write-read'] = '[open open][write read]'
G.edge['connfwexe']['ssr_setup']['fill'] = 'red'
G.add_edge('connfwexe','ssr_setup')
G.edge['connfwexe']['ssr_setup']['write-read'] = '[open open][write read][append read]'
G.add_edge('connfwexe','sswap')
G.edge['connfwexe']['sswap']['write-read'] = '[open open][write read]'
G.edge['connfwexe']['sswap']['fill'] = 'red'
G.add_edge('connfwexe','sswap')
G.edge['connfwexe']['sswap']['write-read'] = '[open open][write read][append read]'
G.add_edge('connfwexe','surfaceflinger')
G.edge['connfwexe']['surfaceflinger']['write-read'] = '[open open][write read]'
G.edge['connfwexe']['surfaceflinger']['fill'] = 'red'
G.add_edge('connfwexe','surfaceflinger')
G.edge['connfwexe']['surfaceflinger']['write-read'] = '[open open][write read][append read]'
G.add_edge('connfwexe','surfaceflinger')
G.edge['connfwexe']['surfaceflinger']['write-read'] = '[open open][write read][append read][write read]'
G.edge['connfwexe']['surfaceflinger']['fill'] = 'red'
G.add_edge('connfwexe','system_server')
G.edge['connfwexe']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][open open][setattr getattr][write read]'
G.edge['connfwexe']['system_server']['fill'] = 'red'
G.add_edge('connfwexe','system_server')
G.edge['connfwexe']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][open open][setattr getattr][write read][append read]'
G.add_edge('connfwexe','system_server')
G.edge['connfwexe']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][open open][setattr getattr][write read][append read][write read]'
G.edge['connfwexe']['system_server']['fill'] = 'red'
G.add_edge('connfwexe','system_server')
G.edge['connfwexe']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read]'
G.add_edge('connfwexe','thermald')
G.edge['connfwexe']['thermald']['write-read'] = '[open open][write read][add_name search][remove_name search][write read]'
G.edge['connfwexe']['thermald']['fill'] = 'red'
G.add_edge('connfwexe','thermal-engine')
G.edge['connfwexe']['thermal-engine']['write-read'] = '[open open][write read]'
G.edge['connfwexe']['thermal-engine']['fill'] = 'red'
G.add_edge('connfwexe','thermal-engine')
G.edge['connfwexe']['thermal-engine']['write-read'] = '[open open][write read][append read]'
G.add_edge('connfwexe','thermal-engine')
G.edge['connfwexe']['thermal-engine']['write-read'] = '[open open][write read][append read][write read]'
G.edge['connfwexe']['thermal-engine']['fill'] = 'red'
G.add_edge('connfwexe','ueventd')
G.edge['connfwexe']['ueventd']['write-read'] = '[open open][write read]'
G.edge['connfwexe']['ueventd']['fill'] = 'red'
G.add_edge('connfwexe','ueventd')
G.edge['connfwexe']['ueventd']['write-read'] = '[open open][write read][append read]'
G.add_edge('connfwexe','vm_bms')
G.edge['connfwexe']['vm_bms']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['connfwexe']['vm_bms']['fill'] = 'red'
G.add_edge('connfwexe','vm_bms')
G.edge['connfwexe']['vm_bms']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('connfwexe','vmwared')
G.edge['connfwexe']['vmwared']['write-read'] = '[write read]'
G.edge['connfwexe']['vmwared']['fill'] = 'red'
G.add_edge('connfwexe','vold')
G.edge['connfwexe']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][write read]'
G.edge['connfwexe']['vold']['fill'] = 'red'
G.add_edge('connfwexe','vold')
G.edge['connfwexe']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][write read][append read]'
G.add_edge('connfwexe','zygote')
G.edge['connfwexe']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['connfwexe']['zygote']['fill'] = 'red'
G.add_edge('domain','at_distributor')
G.edge['domain']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('domain','bauthserver')
G.edge['domain']['bauthserver']['write-read'] = '[setattr getattr][add_name search][remove_name search][open open]'
G.add_edge('domain','bintvoutservice')
G.edge['domain']['bintvoutservice']['write-read'] = '[open open]'
G.add_edge('domain','bluetooth')
G.edge['domain']['bluetooth']['write-read'] = '[open open]'
G.add_edge('domain','cbd')
G.edge['domain']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('domain','cellgeofenced')
G.edge['domain']['cellgeofenced']['write-read'] = '[open open][write read][add_name search][remove_name search][open open]'
G.add_edge('domain','charger_monitor')
G.edge['domain']['charger_monitor']['write-read'] = '[open open]'
G.add_edge('domain','charger_monitor')
G.edge['domain']['charger_monitor']['write-read'] = '[open open][open open]'
G.add_edge('domain','cnd')
G.edge['domain']['cnd']['write-read'] = '[add_name search][remove_name search][open open]'
G.add_edge('domain','connfwexe')
G.edge['domain']['connfwexe']['write-read'] = '[setattr getattr][add_name search][remove_name search][open open]'
G.add_edge('domain','debuggerd')
G.edge['domain']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][add_name search][remove_name search][open open]'
G.add_edge('domain','diag_uart_log')
G.edge['domain']['diag_uart_log']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('domain','dumpstate')
G.edge['domain']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][setattr getattr][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('domain','efsks')
G.edge['domain']['efsks']['write-read'] = '[open open]'
G.add_edge('domain','geomagneticd')
G.edge['domain']['geomagneticd']['write-read'] = '[add_name search][remove_name search][open open]'
G.add_edge('domain','gpsd')
G.edge['domain']['gpsd']['write-read'] = '[setattr getattr][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('domain','init_shell')
G.edge['domain']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][setattr getattr][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('domain','kiesexe')
G.edge['domain']['kiesexe']['write-read'] = '[setattr getattr][add_name search][remove_name search][open open]'
G.add_edge('domain','ks')
G.edge['domain']['ks']['write-read'] = '[open open]'
G.add_edge('domain','lhd')
G.edge['domain']['lhd']['write-read'] = '[setattr getattr][add_name search][remove_name search][open open]'
G.add_edge('domain','lpm')
G.edge['domain']['lpm']['write-read'] = '[open open]'
G.add_edge('domain','macloader')
G.edge['domain']['macloader']['write-read'] = '[open open]'
G.add_edge('domain','mdm_helper')
G.edge['domain']['mdm_helper']['write-read'] = '[setattr getattr][write read][append read][open open]'
G.add_edge('domain','mediaserver')
G.edge['domain']['mediaserver']['write-read'] = '[setattr getattr][add_name search][remove_name search][write read][open open]'
G.add_edge('domain','mlexe')
G.edge['domain']['mlexe']['write-read'] = '[setattr getattr][add_name search][remove_name search][open open]'
G.add_edge('domain','mm-pp-daemon')
G.edge['domain']['mm-pp-daemon']['write-read'] = '[open open]'
G.add_edge('domain','mm-qcamera-daemon')
G.edge['domain']['mm-qcamera-daemon']['write-read'] = '[add_name search][remove_name search][open open]'
G.add_edge('domain','mpdecision')
G.edge['domain']['mpdecision']['write-read'] = '[add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('domain','oneseg_mw')
G.edge['domain']['oneseg_mw']['write-read'] = '[setattr getattr][add_name search][remove_name search][open open]'
G.add_edge('domain','qcks')
G.edge['domain']['qcks']['write-read'] = '[add_name search][remove_name search][open open]'
G.add_edge('domain','qmuxd')
G.edge['domain']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('domain','radio')
G.edge['domain']['radio']['write-read'] = '[open open]'
G.add_edge('domain','rild')
G.edge['domain']['rild']['write-read'] = '[write read][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('domain','rmt_storage')
G.edge['domain']['rmt_storage']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('domain','sec-ril')
G.edge['domain']['sec-ril']['write-read'] = '[setattr getattr][add_name search][remove_name search][open open]'
G.add_edge('domain','smdexe')
G.edge['domain']['smdexe']['write-read'] = '[open open]'
G.add_edge('domain','ssr_setup')
G.edge['domain']['ssr_setup']['write-read'] = '[open open]'
G.add_edge('domain','sswap')
G.edge['domain']['sswap']['write-read'] = '[open open]'
G.add_edge('domain','surfaceflinger')
G.edge['domain']['surfaceflinger']['write-read'] = '[open open]'
G.add_edge('domain','system_server')
G.edge['domain']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][add_name search][remove_name search][open open][write read][append read][setattr getattr][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('domain','system_server')
G.edge['domain']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][add_name search][remove_name search][open open][write read][append read][setattr getattr][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open]'
G.add_edge('domain','thermal-engine')
G.edge['domain']['thermal-engine']['write-read'] = '[open open]'
G.add_edge('domain','ueventd')
G.edge['domain']['ueventd']['write-read'] = '[setattr getattr][add_name search][remove_name search][open open]'
G.add_edge('domain','vm_bms')
G.edge['domain']['vm_bms']['write-read'] = '[open open]'
G.add_edge('domain','vold')
G.edge['domain']['vold']['write-read'] = '[setattr getattr][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('domain','init_shell')
G.edge['domain']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][setattr getattr][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('domain','rild')
G.edge['domain']['rild']['write-read'] = '[write read][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr]'
G.add_edge('domain','rtcc')
G.edge['domain']['rtcc']['write-read'] = '[setattr getattr][add_name search][remove_name search][setattr getattr]'
G.add_edge('domain','sec-ril')
G.edge['domain']['sec-ril']['write-read'] = '[setattr getattr][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('domain','system_server')
G.edge['domain']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][add_name search][remove_name search][open open][write read][append read][setattr getattr][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr]'
G.add_edge('domain','at_distributor')
G.edge['domain']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['domain']['at_distributor']['fill'] = 'red'
G.add_edge('domain','at_distributor')
G.edge['domain']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('domain','bauthserver')
G.edge['domain']['bauthserver']['write-read'] = '[setattr getattr][add_name search][remove_name search][open open][write read]'
G.edge['domain']['bauthserver']['fill'] = 'red'
G.add_edge('domain','bauthserver')
G.edge['domain']['bauthserver']['write-read'] = '[setattr getattr][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('domain','bintvoutservice')
G.edge['domain']['bintvoutservice']['write-read'] = '[open open][write read]'
G.edge['domain']['bintvoutservice']['fill'] = 'red'
G.add_edge('domain','bintvoutservice')
G.edge['domain']['bintvoutservice']['write-read'] = '[open open][write read][append read]'
G.add_edge('domain','bluetooth')
G.edge['domain']['bluetooth']['write-read'] = '[open open][write read]'
G.edge['domain']['bluetooth']['fill'] = 'red'
G.add_edge('domain','bluetooth')
G.edge['domain']['bluetooth']['write-read'] = '[open open][write read][append read]'
G.add_edge('domain','bootanim')
G.edge['domain']['bootanim']['write-read'] = '[write read]'
G.edge['domain']['bootanim']['fill'] = 'red'
G.add_edge('domain','cbd')
G.edge['domain']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][add_name search][remove_name search][add_name search][remove_name search][open open][write read]'
G.edge['domain']['cbd']['fill'] = 'red'
G.add_edge('domain','cbd')
G.edge['domain']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('domain','cellgeofenced')
G.edge['domain']['cellgeofenced']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['domain']['cellgeofenced']['fill'] = 'red'
G.add_edge('domain','cellgeofenced')
G.edge['domain']['cellgeofenced']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('domain','charger_monitor')
G.edge['domain']['charger_monitor']['write-read'] = '[open open][open open][write read]'
G.edge['domain']['charger_monitor']['fill'] = 'red'
G.add_edge('domain','charger_monitor')
G.edge['domain']['charger_monitor']['write-read'] = '[open open][open open][write read][append read]'
G.add_edge('domain','charger_monitor')
G.edge['domain']['charger_monitor']['write-read'] = '[open open][open open][write read][append read][write read]'
G.edge['domain']['charger_monitor']['fill'] = 'red'
G.add_edge('domain','charger_monitor')
G.edge['domain']['charger_monitor']['write-read'] = '[open open][open open][write read][append read][write read][append read]'
G.add_edge('domain','cnd')
G.edge['domain']['cnd']['write-read'] = '[add_name search][remove_name search][open open][write read]'
G.edge['domain']['cnd']['fill'] = 'red'
G.add_edge('domain','cnd')
G.edge['domain']['cnd']['write-read'] = '[add_name search][remove_name search][open open][write read][append read]'
G.add_edge('domain','connfwexe')
G.edge['domain']['connfwexe']['write-read'] = '[setattr getattr][add_name search][remove_name search][open open][write read]'
G.edge['domain']['connfwexe']['fill'] = 'red'
G.add_edge('domain','connfwexe')
G.edge['domain']['connfwexe']['write-read'] = '[setattr getattr][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('domain','debuggerd')
G.edge['domain']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][add_name search][remove_name search][open open][write read]'
G.edge['domain']['debuggerd']['fill'] = 'red'
G.add_edge('domain','debuggerd')
G.edge['domain']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('domain','diag_uart_log')
G.edge['domain']['diag_uart_log']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read]'
G.edge['domain']['diag_uart_log']['fill'] = 'red'
G.add_edge('domain','diag_uart_log')
G.edge['domain']['diag_uart_log']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('domain','dumpstate')
G.edge['domain']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][setattr getattr][add_name search][remove_name search][add_name search][remove_name search][open open][write read]'
G.edge['domain']['dumpstate']['fill'] = 'red'
G.add_edge('domain','dumpstate')
G.edge['domain']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][setattr getattr][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('domain','efsks')
G.edge['domain']['efsks']['write-read'] = '[open open][write read]'
G.edge['domain']['efsks']['fill'] = 'red'
G.add_edge('domain','efsks')
G.edge['domain']['efsks']['write-read'] = '[open open][write read][append read]'
G.add_edge('domain','geomagneticd')
G.edge['domain']['geomagneticd']['write-read'] = '[add_name search][remove_name search][open open][write read]'
G.edge['domain']['geomagneticd']['fill'] = 'red'
G.add_edge('domain','geomagneticd')
G.edge['domain']['geomagneticd']['write-read'] = '[add_name search][remove_name search][open open][write read][append read]'
G.add_edge('domain','gpsd')
G.edge['domain']['gpsd']['write-read'] = '[setattr getattr][add_name search][remove_name search][add_name search][remove_name search][open open][write read]'
G.edge['domain']['gpsd']['fill'] = 'red'
G.add_edge('domain','gpsd')
G.edge['domain']['gpsd']['write-read'] = '[setattr getattr][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('domain','healthd')
G.edge['domain']['healthd']['write-read'] = '[add_name search][remove_name search][write read]'
G.edge['domain']['healthd']['fill'] = 'red'
G.add_edge('domain','init_shell')
G.edge['domain']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][setattr getattr][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['domain']['init_shell']['fill'] = 'red'
G.add_edge('domain','init_shell')
G.edge['domain']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][setattr getattr][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('domain','jackservice')
G.edge['domain']['jackservice']['write-read'] = '[add_name search][add_name search][setattr getattr][add_name search][remove_name search][write read]'
G.edge['domain']['jackservice']['fill'] = 'red'
G.add_edge('domain','kiesexe')
G.edge['domain']['kiesexe']['write-read'] = '[setattr getattr][add_name search][remove_name search][open open][write read]'
G.edge['domain']['kiesexe']['fill'] = 'red'
G.add_edge('domain','kiesexe')
G.edge['domain']['kiesexe']['write-read'] = '[setattr getattr][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('domain','ks')
G.edge['domain']['ks']['write-read'] = '[open open][write read]'
G.edge['domain']['ks']['fill'] = 'red'
G.add_edge('domain','ks')
G.edge['domain']['ks']['write-read'] = '[open open][write read][append read]'
G.add_edge('domain','lhd')
G.edge['domain']['lhd']['write-read'] = '[setattr getattr][add_name search][remove_name search][open open][write read]'
G.edge['domain']['lhd']['fill'] = 'red'
G.add_edge('domain','lhd')
G.edge['domain']['lhd']['write-read'] = '[setattr getattr][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('domain','lmkd')
G.edge['domain']['lmkd']['write-read'] = '[remove_name search][remove_name search][write read]'
G.edge['domain']['lmkd']['fill'] = 'red'
G.add_edge('domain','lpm')
G.edge['domain']['lpm']['write-read'] = '[open open][write read]'
G.edge['domain']['lpm']['fill'] = 'red'
G.add_edge('domain','lpm')
G.edge['domain']['lpm']['write-read'] = '[open open][write read][append read]'
G.add_edge('domain','macloader')
G.edge['domain']['macloader']['write-read'] = '[open open][write read]'
G.edge['domain']['macloader']['fill'] = 'red'
G.add_edge('domain','macloader')
G.edge['domain']['macloader']['write-read'] = '[open open][write read][append read]'
G.add_edge('domain','mdm_helper')
G.edge['domain']['mdm_helper']['write-read'] = '[setattr getattr][write read][append read][open open][write read]'
G.edge['domain']['mdm_helper']['fill'] = 'red'
G.add_edge('domain','mediaserver')
G.edge['domain']['mediaserver']['write-read'] = '[setattr getattr][add_name search][remove_name search][write read][open open][write read]'
G.edge['domain']['mediaserver']['fill'] = 'red'
G.add_edge('domain','mediaserver')
G.edge['domain']['mediaserver']['write-read'] = '[setattr getattr][add_name search][remove_name search][write read][open open][write read][append read]'
G.add_edge('domain','mfgloader')
G.edge['domain']['mfgloader']['write-read'] = '[open open][write read][append read][add_name search][remove_name search][write read]'
G.edge['domain']['mfgloader']['fill'] = 'red'
G.add_edge('domain','mlexe')
G.edge['domain']['mlexe']['write-read'] = '[setattr getattr][add_name search][remove_name search][open open][write read]'
G.edge['domain']['mlexe']['fill'] = 'red'
G.add_edge('domain','mlexe')
G.edge['domain']['mlexe']['write-read'] = '[setattr getattr][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('domain','mm-pp-daemon')
G.edge['domain']['mm-pp-daemon']['write-read'] = '[open open][write read]'
G.edge['domain']['mm-pp-daemon']['fill'] = 'red'
G.add_edge('domain','mm-pp-daemon')
G.edge['domain']['mm-pp-daemon']['write-read'] = '[open open][write read][append read]'
G.add_edge('domain','mm-pp-daemon')
G.edge['domain']['mm-pp-daemon']['write-read'] = '[open open][write read][append read][write read]'
G.edge['domain']['mm-pp-daemon']['fill'] = 'red'
G.add_edge('domain','mm-qcamera-daemon')
G.edge['domain']['mm-qcamera-daemon']['write-read'] = '[add_name search][remove_name search][open open][write read]'
G.edge['domain']['mm-qcamera-daemon']['fill'] = 'red'
G.add_edge('domain','mm-qcamera-daemon')
G.edge['domain']['mm-qcamera-daemon']['write-read'] = '[add_name search][remove_name search][open open][write read][append read]'
G.add_edge('domain','mpdecision')
G.edge['domain']['mpdecision']['write-read'] = '[add_name search][remove_name search][add_name search][remove_name search][open open][write read]'
G.edge['domain']['mpdecision']['fill'] = 'red'
G.add_edge('domain','mpdecision')
G.edge['domain']['mpdecision']['write-read'] = '[add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('domain','mpdecision')
G.edge['domain']['mpdecision']['write-read'] = '[add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][write read]'
G.edge['domain']['mpdecision']['fill'] = 'red'
G.add_edge('domain','netd')
G.edge['domain']['netd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][write read][write read]'
G.edge['domain']['netd']['fill'] = 'red'
G.add_edge('domain','netmgrd')
G.edge['domain']['netmgrd']['write-read'] = '[add_name search][add_name search][remove_name search][open open][write read][append read][write read][open open][write read][add_name search][remove_name search][write read]'
G.edge['domain']['netmgrd']['fill'] = 'red'
G.add_edge('domain','nfc')
G.edge['domain']['nfc']['write-read'] = '[write read]'
G.edge['domain']['nfc']['fill'] = 'red'
G.add_edge('domain','oneseg_mw')
G.edge['domain']['oneseg_mw']['write-read'] = '[setattr getattr][add_name search][remove_name search][open open][write read]'
G.edge['domain']['oneseg_mw']['fill'] = 'red'
G.add_edge('domain','oneseg_mw')
G.edge['domain']['oneseg_mw']['write-read'] = '[setattr getattr][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('domain','perfd')
G.edge['domain']['perfd']['write-read'] = '[write read]'
G.edge['domain']['perfd']['fill'] = 'red'
G.add_edge('domain','qcks')
G.edge['domain']['qcks']['write-read'] = '[add_name search][remove_name search][open open][write read]'
G.edge['domain']['qcks']['fill'] = 'red'
G.add_edge('domain','qcks')
G.edge['domain']['qcks']['write-read'] = '[add_name search][remove_name search][open open][write read][append read]'
G.add_edge('domain','qmuxd')
G.edge['domain']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read]'
G.edge['domain']['qmuxd']['fill'] = 'red'
G.add_edge('domain','qmuxd')
G.edge['domain']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('domain','qosmgr')
G.edge['domain']['qosmgr']['write-read'] = '[write read]'
G.edge['domain']['qosmgr']['fill'] = 'red'
G.add_edge('domain','radio')
G.edge['domain']['radio']['write-read'] = '[open open][append read]'
G.add_edge('domain','rild')
G.edge['domain']['rild']['write-read'] = '[write read][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['domain']['rild']['fill'] = 'red'
G.add_edge('domain','rild')
G.edge['domain']['rild']['write-read'] = '[write read][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('domain','rmt_storage')
G.edge['domain']['rmt_storage']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read]'
G.edge['domain']['rmt_storage']['fill'] = 'red'
G.add_edge('domain','rmt_storage')
G.edge['domain']['rmt_storage']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('domain','rtcc')
G.edge['domain']['rtcc']['write-read'] = '[setattr getattr][add_name search][remove_name search][setattr getattr][write read]'
G.edge['domain']['rtcc']['fill'] = 'red'
G.add_edge('domain','sec-ril')
G.edge['domain']['sec-ril']['write-read'] = '[setattr getattr][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['domain']['sec-ril']['fill'] = 'red'
G.add_edge('domain','sec-ril')
G.edge['domain']['sec-ril']['write-read'] = '[setattr getattr][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('domain','sensorhubservice')
G.edge['domain']['sensorhubservice']['write-read'] = '[write read]'
G.edge['domain']['sensorhubservice']['fill'] = 'red'
G.add_edge('domain','smdexe')
G.edge['domain']['smdexe']['write-read'] = '[open open][write read]'
G.edge['domain']['smdexe']['fill'] = 'red'
G.add_edge('domain','smdexe')
G.edge['domain']['smdexe']['write-read'] = '[open open][write read][append read]'
G.add_edge('domain','ssr_setup')
G.edge['domain']['ssr_setup']['write-read'] = '[open open][write read]'
G.edge['domain']['ssr_setup']['fill'] = 'red'
G.add_edge('domain','ssr_setup')
G.edge['domain']['ssr_setup']['write-read'] = '[open open][write read][append read]'
G.add_edge('domain','sswap')
G.edge['domain']['sswap']['write-read'] = '[open open][write read]'
G.edge['domain']['sswap']['fill'] = 'red'
G.add_edge('domain','sswap')
G.edge['domain']['sswap']['write-read'] = '[open open][write read][append read]'
G.add_edge('domain','surfaceflinger')
G.edge['domain']['surfaceflinger']['write-read'] = '[open open][write read]'
G.edge['domain']['surfaceflinger']['fill'] = 'red'
G.add_edge('domain','surfaceflinger')
G.edge['domain']['surfaceflinger']['write-read'] = '[open open][write read][append read]'
G.add_edge('domain','surfaceflinger')
G.edge['domain']['surfaceflinger']['write-read'] = '[open open][write read][append read][write read]'
G.edge['domain']['surfaceflinger']['fill'] = 'red'
G.add_edge('domain','system_server')
G.edge['domain']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][add_name search][remove_name search][open open][write read][append read][setattr getattr][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read]'
G.edge['domain']['system_server']['fill'] = 'red'
G.add_edge('domain','system_server')
G.edge['domain']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][add_name search][remove_name search][open open][write read][append read][setattr getattr][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read]'
G.add_edge('domain','system_server')
G.edge['domain']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][add_name search][remove_name search][open open][write read][append read][setattr getattr][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read]'
G.edge['domain']['system_server']['fill'] = 'red'
G.add_edge('domain','system_server')
G.edge['domain']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][add_name search][remove_name search][open open][write read][append read][setattr getattr][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read]'
G.add_edge('domain','thermald')
G.edge['domain']['thermald']['write-read'] = '[add_name search][remove_name search][write read]'
G.edge['domain']['thermald']['fill'] = 'red'
G.add_edge('domain','thermal-engine')
G.edge['domain']['thermal-engine']['write-read'] = '[open open][write read]'
G.edge['domain']['thermal-engine']['fill'] = 'red'
G.add_edge('domain','thermal-engine')
G.edge['domain']['thermal-engine']['write-read'] = '[open open][write read][append read]'
G.add_edge('domain','thermal-engine')
G.edge['domain']['thermal-engine']['write-read'] = '[open open][write read][append read][write read]'
G.edge['domain']['thermal-engine']['fill'] = 'red'
G.add_edge('domain','ueventd')
G.edge['domain']['ueventd']['write-read'] = '[setattr getattr][add_name search][remove_name search][open open][write read]'
G.edge['domain']['ueventd']['fill'] = 'red'
G.add_edge('domain','ueventd')
G.edge['domain']['ueventd']['write-read'] = '[setattr getattr][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('domain','vm_bms')
G.edge['domain']['vm_bms']['write-read'] = '[open open][write read]'
G.edge['domain']['vm_bms']['fill'] = 'red'
G.add_edge('domain','vm_bms')
G.edge['domain']['vm_bms']['write-read'] = '[open open][write read][append read]'
G.add_edge('domain','vmwared')
G.edge['domain']['vmwared']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read]'
G.edge['domain']['vmwared']['fill'] = 'red'
G.add_edge('domain','vold')
G.edge['domain']['vold']['write-read'] = '[setattr getattr][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][write read]'
G.edge['domain']['vold']['fill'] = 'red'
G.add_edge('domain','vold')
G.edge['domain']['vold']['write-read'] = '[setattr getattr][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('domain','zygote')
G.edge['domain']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][setattr getattr][add_name search][remove_name search][write read]'
G.edge['domain']['zygote']['fill'] = 'red'
G.add_edge('gpsd','at_distributor')
G.edge['gpsd']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('gpsd','bauthserver')
G.edge['gpsd']['bauthserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('gpsd','bintvoutservice')
G.edge['gpsd']['bintvoutservice']['write-read'] = '[open open]'
G.add_edge('gpsd','bluetooth')
G.edge['gpsd']['bluetooth']['write-read'] = '[open open]'
G.add_edge('gpsd','cbd')
G.edge['gpsd']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('gpsd','cellgeofenced')
G.edge['gpsd']['cellgeofenced']['write-read'] = '[open open]'
G.add_edge('gpsd','charger_monitor')
G.edge['gpsd']['charger_monitor']['write-read'] = '[open open]'
G.add_edge('gpsd','charger_monitor')
G.edge['gpsd']['charger_monitor']['write-read'] = '[open open][open open]'
G.add_edge('gpsd','cnd')
G.edge['gpsd']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('gpsd','connfwexe')
G.edge['gpsd']['connfwexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('gpsd','debuggerd')
G.edge['gpsd']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('gpsd','diag_uart_log')
G.edge['gpsd']['diag_uart_log']['write-read'] = '[open open]'
G.add_edge('gpsd','dumpstate')
G.edge['gpsd']['dumpstate']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('gpsd','efsks')
G.edge['gpsd']['efsks']['write-read'] = '[open open]'
G.add_edge('gpsd','geomagneticd')
G.edge['gpsd']['geomagneticd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('gpsd','gpsd')
G.edge['gpsd']['gpsd']['write-read'] = '[open open][setattr getattr][write read][append read][write read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('gpsd','init_shell')
G.edge['gpsd']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open]'
G.add_edge('gpsd','kiesexe')
G.edge['gpsd']['kiesexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('gpsd','ks')
G.edge['gpsd']['ks']['write-read'] = '[open open]'
G.add_edge('gpsd','lhd')
G.edge['gpsd']['lhd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('gpsd','lpm')
G.edge['gpsd']['lpm']['write-read'] = '[open open]'
G.add_edge('gpsd','macloader')
G.edge['gpsd']['macloader']['write-read'] = '[open open]'
G.add_edge('gpsd','mdm_helper')
G.edge['gpsd']['mdm_helper']['write-read'] = '[open open]'
G.add_edge('gpsd','mediaserver')
G.edge['gpsd']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('gpsd','mlexe')
G.edge['gpsd']['mlexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('gpsd','mm-pp-daemon')
G.edge['gpsd']['mm-pp-daemon']['write-read'] = '[open open]'
G.add_edge('gpsd','mm-qcamera-daemon')
G.edge['gpsd']['mm-qcamera-daemon']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('gpsd','mpdecision')
G.edge['gpsd']['mpdecision']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('gpsd','oneseg_mw')
G.edge['gpsd']['oneseg_mw']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('gpsd','qcks')
G.edge['gpsd']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('gpsd','qmuxd')
G.edge['gpsd']['qmuxd']['write-read'] = '[open open]'
G.add_edge('gpsd','radio')
G.edge['gpsd']['radio']['write-read'] = '[open open]'
G.add_edge('gpsd','rild')
G.edge['gpsd']['rild']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('gpsd','rmt_storage')
G.edge['gpsd']['rmt_storage']['write-read'] = '[open open]'
G.add_edge('gpsd','sec-ril')
G.edge['gpsd']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('gpsd','smdexe')
G.edge['gpsd']['smdexe']['write-read'] = '[open open]'
G.add_edge('gpsd','ssr_setup')
G.edge['gpsd']['ssr_setup']['write-read'] = '[open open]'
G.add_edge('gpsd','sswap')
G.edge['gpsd']['sswap']['write-read'] = '[open open]'
G.add_edge('gpsd','surfaceflinger')
G.edge['gpsd']['surfaceflinger']['write-read'] = '[open open]'
G.add_edge('gpsd','system_server')
G.edge['gpsd']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('gpsd','system_server')
G.edge['gpsd']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open]'
G.add_edge('gpsd','thermal-engine')
G.edge['gpsd']['thermal-engine']['write-read'] = '[open open]'
G.add_edge('gpsd','ueventd')
G.edge['gpsd']['ueventd']['write-read'] = '[open open]'
G.add_edge('gpsd','vm_bms')
G.edge['gpsd']['vm_bms']['write-read'] = '[open open]'
G.add_edge('gpsd','vold')
G.edge['gpsd']['vold']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('gpsd','init_shell')
G.edge['gpsd']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr]'
G.add_edge('gpsd','rild')
G.edge['gpsd']['rild']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('gpsd','rtcc')
G.edge['gpsd']['rtcc']['write-read'] = '[setattr getattr]'
G.add_edge('gpsd','sec-ril')
G.edge['gpsd']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('gpsd','system_server')
G.edge['gpsd']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr]'
G.add_edge('gpsd','at_distributor')
G.edge['gpsd']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['gpsd']['at_distributor']['fill'] = 'red'
G.add_edge('gpsd','at_distributor')
G.edge['gpsd']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('gpsd','bauthserver')
G.edge['gpsd']['bauthserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['gpsd']['bauthserver']['fill'] = 'red'
G.add_edge('gpsd','bauthserver')
G.edge['gpsd']['bauthserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('gpsd','bintvoutservice')
G.edge['gpsd']['bintvoutservice']['write-read'] = '[open open][write read]'
G.edge['gpsd']['bintvoutservice']['fill'] = 'red'
G.add_edge('gpsd','bintvoutservice')
G.edge['gpsd']['bintvoutservice']['write-read'] = '[open open][write read][append read]'
G.add_edge('gpsd','bluetooth')
G.edge['gpsd']['bluetooth']['write-read'] = '[open open][write read]'
G.edge['gpsd']['bluetooth']['fill'] = 'red'
G.add_edge('gpsd','bluetooth')
G.edge['gpsd']['bluetooth']['write-read'] = '[open open][write read][append read]'
G.add_edge('gpsd','bootanim')
G.edge['gpsd']['bootanim']['write-read'] = '[write read]'
G.edge['gpsd']['bootanim']['fill'] = 'red'
G.add_edge('gpsd','cbd')
G.edge['gpsd']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['gpsd']['cbd']['fill'] = 'red'
G.add_edge('gpsd','cbd')
G.edge['gpsd']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('gpsd','cellgeofenced')
G.edge['gpsd']['cellgeofenced']['write-read'] = '[open open][write read]'
G.edge['gpsd']['cellgeofenced']['fill'] = 'red'
G.add_edge('gpsd','cellgeofenced')
G.edge['gpsd']['cellgeofenced']['write-read'] = '[open open][write read][append read]'
G.add_edge('gpsd','charger_monitor')
G.edge['gpsd']['charger_monitor']['write-read'] = '[open open][open open][write read]'
G.edge['gpsd']['charger_monitor']['fill'] = 'red'
G.add_edge('gpsd','charger_monitor')
G.edge['gpsd']['charger_monitor']['write-read'] = '[open open][open open][write read][append read]'
G.add_edge('gpsd','charger_monitor')
G.edge['gpsd']['charger_monitor']['write-read'] = '[open open][open open][write read][append read][write read]'
G.edge['gpsd']['charger_monitor']['fill'] = 'red'
G.add_edge('gpsd','charger_monitor')
G.edge['gpsd']['charger_monitor']['write-read'] = '[open open][open open][write read][append read][write read][append read]'
G.add_edge('gpsd','cnd')
G.edge['gpsd']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['gpsd']['cnd']['fill'] = 'red'
G.add_edge('gpsd','cnd')
G.edge['gpsd']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('gpsd','connfwexe')
G.edge['gpsd']['connfwexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['gpsd']['connfwexe']['fill'] = 'red'
G.add_edge('gpsd','connfwexe')
G.edge['gpsd']['connfwexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('gpsd','debuggerd')
G.edge['gpsd']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['gpsd']['debuggerd']['fill'] = 'red'
G.add_edge('gpsd','debuggerd')
G.edge['gpsd']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('gpsd','diag_uart_log')
G.edge['gpsd']['diag_uart_log']['write-read'] = '[open open][write read]'
G.edge['gpsd']['diag_uart_log']['fill'] = 'red'
G.add_edge('gpsd','diag_uart_log')
G.edge['gpsd']['diag_uart_log']['write-read'] = '[open open][write read][append read]'
G.add_edge('gpsd','dumpstate')
G.edge['gpsd']['dumpstate']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read]'
G.edge['gpsd']['dumpstate']['fill'] = 'red'
G.add_edge('gpsd','dumpstate')
G.edge['gpsd']['dumpstate']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('gpsd','efsks')
G.edge['gpsd']['efsks']['write-read'] = '[open open][write read]'
G.edge['gpsd']['efsks']['fill'] = 'red'
G.add_edge('gpsd','efsks')
G.edge['gpsd']['efsks']['write-read'] = '[open open][write read][append read]'
G.add_edge('gpsd','geomagneticd')
G.edge['gpsd']['geomagneticd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['gpsd']['geomagneticd']['fill'] = 'red'
G.add_edge('gpsd','geomagneticd')
G.edge['gpsd']['geomagneticd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('gpsd','gpsd')
G.edge['gpsd']['gpsd']['write-read'] = '[open open][setattr getattr][write read][append read][write read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['gpsd']['gpsd']['fill'] = 'red'
G.add_edge('gpsd','gpsd')
G.edge['gpsd']['gpsd']['write-read'] = '[open open][setattr getattr][write read][append read][write read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('gpsd','healthd')
G.edge['gpsd']['healthd']['write-read'] = '[write read]'
G.edge['gpsd']['healthd']['fill'] = 'red'
G.add_edge('gpsd','init_shell')
G.edge['gpsd']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read]'
G.edge['gpsd']['init_shell']['fill'] = 'red'
G.add_edge('gpsd','init_shell')
G.edge['gpsd']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read]'
G.add_edge('gpsd','jackservice')
G.edge['gpsd']['jackservice']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['gpsd']['jackservice']['fill'] = 'red'
G.add_edge('gpsd','kiesexe')
G.edge['gpsd']['kiesexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['gpsd']['kiesexe']['fill'] = 'red'
G.add_edge('gpsd','kiesexe')
G.edge['gpsd']['kiesexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('gpsd','ks')
G.edge['gpsd']['ks']['write-read'] = '[open open][write read]'
G.edge['gpsd']['ks']['fill'] = 'red'
G.add_edge('gpsd','ks')
G.edge['gpsd']['ks']['write-read'] = '[open open][write read][append read]'
G.add_edge('gpsd','lhd')
G.edge['gpsd']['lhd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['gpsd']['lhd']['fill'] = 'red'
G.add_edge('gpsd','lhd')
G.edge['gpsd']['lhd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('gpsd','lmkd')
G.edge['gpsd']['lmkd']['write-read'] = '[write read]'
G.edge['gpsd']['lmkd']['fill'] = 'red'
G.add_edge('gpsd','lpm')
G.edge['gpsd']['lpm']['write-read'] = '[open open][write read]'
G.edge['gpsd']['lpm']['fill'] = 'red'
G.add_edge('gpsd','lpm')
G.edge['gpsd']['lpm']['write-read'] = '[open open][write read][append read]'
G.add_edge('gpsd','macloader')
G.edge['gpsd']['macloader']['write-read'] = '[open open][write read]'
G.edge['gpsd']['macloader']['fill'] = 'red'
G.add_edge('gpsd','macloader')
G.edge['gpsd']['macloader']['write-read'] = '[open open][write read][append read]'
G.add_edge('gpsd','mdm_helper')
G.edge['gpsd']['mdm_helper']['write-read'] = '[open open][write read]'
G.edge['gpsd']['mdm_helper']['fill'] = 'red'
G.add_edge('gpsd','mediaserver')
G.edge['gpsd']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['gpsd']['mediaserver']['fill'] = 'red'
G.add_edge('gpsd','mediaserver')
G.edge['gpsd']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('gpsd','mfgloader')
G.edge['gpsd']['mfgloader']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read]'
G.edge['gpsd']['mfgloader']['fill'] = 'red'
G.add_edge('gpsd','mlexe')
G.edge['gpsd']['mlexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['gpsd']['mlexe']['fill'] = 'red'
G.add_edge('gpsd','mlexe')
G.edge['gpsd']['mlexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('gpsd','mm-pp-daemon')
G.edge['gpsd']['mm-pp-daemon']['write-read'] = '[open open][write read]'
G.edge['gpsd']['mm-pp-daemon']['fill'] = 'red'
G.add_edge('gpsd','mm-pp-daemon')
G.edge['gpsd']['mm-pp-daemon']['write-read'] = '[open open][write read][append read]'
G.add_edge('gpsd','mm-pp-daemon')
G.edge['gpsd']['mm-pp-daemon']['write-read'] = '[open open][write read][append read][write read]'
G.edge['gpsd']['mm-pp-daemon']['fill'] = 'red'
G.add_edge('gpsd','mm-qcamera-daemon')
G.edge['gpsd']['mm-qcamera-daemon']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['gpsd']['mm-qcamera-daemon']['fill'] = 'red'
G.add_edge('gpsd','mm-qcamera-daemon')
G.edge['gpsd']['mm-qcamera-daemon']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('gpsd','mpdecision')
G.edge['gpsd']['mpdecision']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['gpsd']['mpdecision']['fill'] = 'red'
G.add_edge('gpsd','mpdecision')
G.edge['gpsd']['mpdecision']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('gpsd','mpdecision')
G.edge['gpsd']['mpdecision']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read][write read]'
G.edge['gpsd']['mpdecision']['fill'] = 'red'
G.add_edge('gpsd','netd')
G.edge['gpsd']['netd']['write-read'] = '[write read]'
G.edge['gpsd']['netd']['fill'] = 'red'
G.add_edge('gpsd','netmgrd')
G.edge['gpsd']['netmgrd']['write-read'] = '[open open][open open][write read][write read][add_name search][add_name search][remove_name search][open open][open open][write read][write read][add_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['gpsd']['netmgrd']['fill'] = 'red'
G.add_edge('gpsd','nfc')
G.edge['gpsd']['nfc']['write-read'] = '[write read]'
G.edge['gpsd']['nfc']['fill'] = 'red'
G.add_edge('gpsd','oneseg_mw')
G.edge['gpsd']['oneseg_mw']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['gpsd']['oneseg_mw']['fill'] = 'red'
G.add_edge('gpsd','oneseg_mw')
G.edge['gpsd']['oneseg_mw']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('gpsd','perfd')
G.edge['gpsd']['perfd']['write-read'] = '[write read]'
G.edge['gpsd']['perfd']['fill'] = 'red'
G.add_edge('gpsd','qcks')
G.edge['gpsd']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['gpsd']['qcks']['fill'] = 'red'
G.add_edge('gpsd','qcks')
G.edge['gpsd']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('gpsd','qmuxd')
G.edge['gpsd']['qmuxd']['write-read'] = '[open open][write read]'
G.edge['gpsd']['qmuxd']['fill'] = 'red'
G.add_edge('gpsd','qmuxd')
G.edge['gpsd']['qmuxd']['write-read'] = '[open open][write read][append read]'
G.add_edge('gpsd','qosmgr')
G.edge['gpsd']['qosmgr']['write-read'] = '[write read]'
G.edge['gpsd']['qosmgr']['fill'] = 'red'
G.add_edge('gpsd','radio')
G.edge['gpsd']['radio']['write-read'] = '[open open][append read]'
G.add_edge('gpsd','rild')
G.edge['gpsd']['rild']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['gpsd']['rild']['fill'] = 'red'
G.add_edge('gpsd','rild')
G.edge['gpsd']['rild']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('gpsd','rmt_storage')
G.edge['gpsd']['rmt_storage']['write-read'] = '[open open][write read]'
G.edge['gpsd']['rmt_storage']['fill'] = 'red'
G.add_edge('gpsd','rmt_storage')
G.edge['gpsd']['rmt_storage']['write-read'] = '[open open][write read][append read]'
G.add_edge('gpsd','rtcc')
G.edge['gpsd']['rtcc']['write-read'] = '[setattr getattr][write read]'
G.edge['gpsd']['rtcc']['fill'] = 'red'
G.add_edge('gpsd','sec-ril')
G.edge['gpsd']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['gpsd']['sec-ril']['fill'] = 'red'
G.add_edge('gpsd','sec-ril')
G.edge['gpsd']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('gpsd','sensorhubservice')
G.edge['gpsd']['sensorhubservice']['write-read'] = '[write read]'
G.edge['gpsd']['sensorhubservice']['fill'] = 'red'
G.add_edge('gpsd','smdexe')
G.edge['gpsd']['smdexe']['write-read'] = '[open open][write read]'
G.edge['gpsd']['smdexe']['fill'] = 'red'
G.add_edge('gpsd','smdexe')
G.edge['gpsd']['smdexe']['write-read'] = '[open open][write read][append read]'
G.add_edge('gpsd','ssr_setup')
G.edge['gpsd']['ssr_setup']['write-read'] = '[open open][write read]'
G.edge['gpsd']['ssr_setup']['fill'] = 'red'
G.add_edge('gpsd','ssr_setup')
G.edge['gpsd']['ssr_setup']['write-read'] = '[open open][write read][append read]'
G.add_edge('gpsd','sswap')
G.edge['gpsd']['sswap']['write-read'] = '[open open][write read]'
G.edge['gpsd']['sswap']['fill'] = 'red'
G.add_edge('gpsd','sswap')
G.edge['gpsd']['sswap']['write-read'] = '[open open][write read][append read]'
G.add_edge('gpsd','surfaceflinger')
G.edge['gpsd']['surfaceflinger']['write-read'] = '[open open][write read]'
G.edge['gpsd']['surfaceflinger']['fill'] = 'red'
G.add_edge('gpsd','surfaceflinger')
G.edge['gpsd']['surfaceflinger']['write-read'] = '[open open][write read][append read]'
G.add_edge('gpsd','surfaceflinger')
G.edge['gpsd']['surfaceflinger']['write-read'] = '[open open][write read][append read][write read]'
G.edge['gpsd']['surfaceflinger']['fill'] = 'red'
G.add_edge('gpsd','system_server')
G.edge['gpsd']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read]'
G.edge['gpsd']['system_server']['fill'] = 'red'
G.add_edge('gpsd','system_server')
G.edge['gpsd']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][append read]'
G.add_edge('gpsd','system_server')
G.edge['gpsd']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][append read][write read]'
G.edge['gpsd']['system_server']['fill'] = 'red'
G.add_edge('gpsd','system_server')
G.edge['gpsd']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][append read][write read][append read]'
G.add_edge('gpsd','thermald')
G.edge['gpsd']['thermald']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read]'
G.edge['gpsd']['thermald']['fill'] = 'red'
G.add_edge('gpsd','thermal-engine')
G.edge['gpsd']['thermal-engine']['write-read'] = '[open open][write read]'
G.edge['gpsd']['thermal-engine']['fill'] = 'red'
G.add_edge('gpsd','thermal-engine')
G.edge['gpsd']['thermal-engine']['write-read'] = '[open open][write read][append read]'
G.add_edge('gpsd','thermal-engine')
G.edge['gpsd']['thermal-engine']['write-read'] = '[open open][write read][append read][write read]'
G.edge['gpsd']['thermal-engine']['fill'] = 'red'
G.add_edge('gpsd','ueventd')
G.edge['gpsd']['ueventd']['write-read'] = '[open open][write read]'
G.edge['gpsd']['ueventd']['fill'] = 'red'
G.add_edge('gpsd','ueventd')
G.edge['gpsd']['ueventd']['write-read'] = '[open open][write read][append read]'
G.add_edge('gpsd','vm_bms')
G.edge['gpsd']['vm_bms']['write-read'] = '[open open][write read]'
G.edge['gpsd']['vm_bms']['fill'] = 'red'
G.add_edge('gpsd','vm_bms')
G.edge['gpsd']['vm_bms']['write-read'] = '[open open][write read][append read]'
G.add_edge('gpsd','vmwared')
G.edge['gpsd']['vmwared']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['gpsd']['vmwared']['fill'] = 'red'
G.add_edge('gpsd','vold')
G.edge['gpsd']['vold']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['gpsd']['vold']['fill'] = 'red'
G.add_edge('gpsd','vold')
G.edge['gpsd']['vold']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('gpsd','zygote')
G.edge['gpsd']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['gpsd']['zygote']['fill'] = 'red'
G.add_edge('init_shell','at_distributor')
G.edge['init_shell']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('init_shell','bauthserver')
G.edge['init_shell']['bauthserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('init_shell','bintvoutservice')
G.edge['init_shell']['bintvoutservice']['write-read'] = '[open open]'
G.add_edge('init_shell','bluetooth')
G.edge['init_shell']['bluetooth']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('init_shell','cbd')
G.edge['init_shell']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('init_shell','cellgeofenced')
G.edge['init_shell']['cellgeofenced']['write-read'] = '[open open][write read][add_name search][remove_name search][open open]'
G.add_edge('init_shell','charger_monitor')
G.edge['init_shell']['charger_monitor']['write-read'] = '[open open]'
G.add_edge('init_shell','charger_monitor')
G.edge['init_shell']['charger_monitor']['write-read'] = '[open open][open open]'
G.add_edge('init_shell','cnd')
G.edge['init_shell']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open]'
G.add_edge('init_shell','connfwexe')
G.edge['init_shell']['connfwexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('init_shell','debuggerd')
G.edge['init_shell']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('init_shell','diag_uart_log')
G.edge['init_shell']['diag_uart_log']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('init_shell','dumpstate')
G.edge['init_shell']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('init_shell','efsks')
G.edge['init_shell']['efsks']['write-read'] = '[open open][write read][add_name search][add_name search][open open]'
G.add_edge('init_shell','geomagneticd')
G.edge['init_shell']['geomagneticd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open]'
G.add_edge('init_shell','gpsd')
G.edge['init_shell']['gpsd']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('init_shell','init_shell')
G.edge['init_shell']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('init_shell','kiesexe')
G.edge['init_shell']['kiesexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('init_shell','ks')
G.edge['init_shell']['ks']['write-read'] = '[open open][write read][add_name search][add_name search][open open]'
G.add_edge('init_shell','lhd')
G.edge['init_shell']['lhd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('init_shell','lpm')
G.edge['init_shell']['lpm']['write-read'] = '[open open]'
G.add_edge('init_shell','macloader')
G.edge['init_shell']['macloader']['write-read'] = '[open open]'
G.add_edge('init_shell','mdm_helper')
G.edge['init_shell']['mdm_helper']['write-read'] = '[write read][open open][setattr getattr][write read][append read][setattr getattr][open open]'
G.add_edge('init_shell','mediaserver')
G.edge['init_shell']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('init_shell','mlexe')
G.edge['init_shell']['mlexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('init_shell','mm-pp-daemon')
G.edge['init_shell']['mm-pp-daemon']['write-read'] = '[open open]'
G.add_edge('init_shell','mm-qcamera-daemon')
G.edge['init_shell']['mm-qcamera-daemon']['write-read'] = '[open open][write read][add_name search][remove_name search][open open]'
G.add_edge('init_shell','mpdecision')
G.edge['init_shell']['mpdecision']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('init_shell','oneseg_mw')
G.edge['init_shell']['oneseg_mw']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('init_shell','qcks')
G.edge['init_shell']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][add_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('init_shell','qmuxd')
G.edge['init_shell']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read][append read][write read][append read][open open]'
G.add_edge('init_shell','radio')
G.edge['init_shell']['radio']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('init_shell','rild')
G.edge['init_shell']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][open open][setattr getattr][write read][append read][write read][append read][write read][append read][open open]'
G.add_edge('init_shell','rmt_storage')
G.edge['init_shell']['rmt_storage']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('init_shell','sec-ril')
G.edge['init_shell']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('init_shell','smdexe')
G.edge['init_shell']['smdexe']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('init_shell','ssr_setup')
G.edge['init_shell']['ssr_setup']['write-read'] = '[open open]'
G.add_edge('init_shell','sswap')
G.edge['init_shell']['sswap']['write-read'] = '[open open]'
G.add_edge('init_shell','surfaceflinger')
G.edge['init_shell']['surfaceflinger']['write-read'] = '[open open]'
G.add_edge('init_shell','system_server')
G.edge['init_shell']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('init_shell','system_server')
G.edge['init_shell']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open]'
G.add_edge('init_shell','thermal-engine')
G.edge['init_shell']['thermal-engine']['write-read'] = '[open open]'
G.add_edge('init_shell','ueventd')
G.edge['init_shell']['ueventd']['write-read'] = '[setattr getattr][open open][write read][append read][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('init_shell','vm_bms')
G.edge['init_shell']['vm_bms']['write-read'] = '[open open]'
G.add_edge('init_shell','vold')
G.edge['init_shell']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('init_shell','init_shell')
G.edge['init_shell']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('init_shell','rild')
G.edge['init_shell']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][open open][setattr getattr][write read][append read][write read][append read][write read][append read][open open][setattr getattr]'
G.add_edge('init_shell','rtcc')
G.edge['init_shell']['rtcc']['write-read'] = '[setattr getattr][open open][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('init_shell','sec-ril')
G.edge['init_shell']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('init_shell','system_server')
G.edge['init_shell']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr]'
G.add_edge('init_shell','at_distributor')
G.edge['init_shell']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['init_shell']['at_distributor']['fill'] = 'red'
G.add_edge('init_shell','at_distributor')
G.edge['init_shell']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('init_shell','bauthserver')
G.edge['init_shell']['bauthserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['init_shell']['bauthserver']['fill'] = 'red'
G.add_edge('init_shell','bauthserver')
G.edge['init_shell']['bauthserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('init_shell','bintvoutservice')
G.edge['init_shell']['bintvoutservice']['write-read'] = '[open open][write read]'
G.edge['init_shell']['bintvoutservice']['fill'] = 'red'
G.add_edge('init_shell','bintvoutservice')
G.edge['init_shell']['bintvoutservice']['write-read'] = '[open open][write read][append read]'
G.add_edge('init_shell','bluetooth')
G.edge['init_shell']['bluetooth']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['init_shell']['bluetooth']['fill'] = 'red'
G.add_edge('init_shell','bluetooth')
G.edge['init_shell']['bluetooth']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('init_shell','bootanim')
G.edge['init_shell']['bootanim']['write-read'] = '[write read]'
G.edge['init_shell']['bootanim']['fill'] = 'red'
G.add_edge('init_shell','cbd')
G.edge['init_shell']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['init_shell']['cbd']['fill'] = 'red'
G.add_edge('init_shell','cbd')
G.edge['init_shell']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('init_shell','cellgeofenced')
G.edge['init_shell']['cellgeofenced']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['init_shell']['cellgeofenced']['fill'] = 'red'
G.add_edge('init_shell','cellgeofenced')
G.edge['init_shell']['cellgeofenced']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('init_shell','charger_monitor')
G.edge['init_shell']['charger_monitor']['write-read'] = '[open open][open open][write read]'
G.edge['init_shell']['charger_monitor']['fill'] = 'red'
G.add_edge('init_shell','charger_monitor')
G.edge['init_shell']['charger_monitor']['write-read'] = '[open open][open open][write read][append read]'
G.add_edge('init_shell','charger_monitor')
G.edge['init_shell']['charger_monitor']['write-read'] = '[open open][open open][write read][append read][write read]'
G.edge['init_shell']['charger_monitor']['fill'] = 'red'
G.add_edge('init_shell','charger_monitor')
G.edge['init_shell']['charger_monitor']['write-read'] = '[open open][open open][write read][append read][write read][append read]'
G.add_edge('init_shell','cnd')
G.edge['init_shell']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['init_shell']['cnd']['fill'] = 'red'
G.add_edge('init_shell','cnd')
G.edge['init_shell']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('init_shell','connfwexe')
G.edge['init_shell']['connfwexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['init_shell']['connfwexe']['fill'] = 'red'
G.add_edge('init_shell','connfwexe')
G.edge['init_shell']['connfwexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('init_shell','debuggerd')
G.edge['init_shell']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read]'
G.edge['init_shell']['debuggerd']['fill'] = 'red'
G.add_edge('init_shell','debuggerd')
G.edge['init_shell']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('init_shell','diag_uart_log')
G.edge['init_shell']['diag_uart_log']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['init_shell']['diag_uart_log']['fill'] = 'red'
G.add_edge('init_shell','diag_uart_log')
G.edge['init_shell']['diag_uart_log']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('init_shell','dumpstate')
G.edge['init_shell']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['init_shell']['dumpstate']['fill'] = 'red'
G.add_edge('init_shell','dumpstate')
G.edge['init_shell']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('init_shell','efsks')
G.edge['init_shell']['efsks']['write-read'] = '[open open][write read][add_name search][add_name search][open open][write read]'
G.edge['init_shell']['efsks']['fill'] = 'red'
G.add_edge('init_shell','efsks')
G.edge['init_shell']['efsks']['write-read'] = '[open open][write read][add_name search][add_name search][open open][write read][append read]'
G.add_edge('init_shell','geomagneticd')
G.edge['init_shell']['geomagneticd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['init_shell']['geomagneticd']['fill'] = 'red'
G.add_edge('init_shell','geomagneticd')
G.edge['init_shell']['geomagneticd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('init_shell','gpsd')
G.edge['init_shell']['gpsd']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][write read]'
G.edge['init_shell']['gpsd']['fill'] = 'red'
G.add_edge('init_shell','gpsd')
G.edge['init_shell']['gpsd']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('init_shell','healthd')
G.edge['init_shell']['healthd']['write-read'] = '[write read][add_name search][remove_name search][write read]'
G.edge['init_shell']['healthd']['fill'] = 'red'
G.add_edge('init_shell','init_shell')
G.edge['init_shell']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['init_shell']['init_shell']['fill'] = 'red'
G.add_edge('init_shell','init_shell')
G.edge['init_shell']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('init_shell','jackservice')
G.edge['init_shell']['jackservice']['write-read'] = '[add_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['init_shell']['jackservice']['fill'] = 'red'
G.add_edge('init_shell','kiesexe')
G.edge['init_shell']['kiesexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['init_shell']['kiesexe']['fill'] = 'red'
G.add_edge('init_shell','kiesexe')
G.edge['init_shell']['kiesexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('init_shell','ks')
G.edge['init_shell']['ks']['write-read'] = '[open open][write read][add_name search][add_name search][open open][write read]'
G.edge['init_shell']['ks']['fill'] = 'red'
G.add_edge('init_shell','ks')
G.edge['init_shell']['ks']['write-read'] = '[open open][write read][add_name search][add_name search][open open][write read][append read]'
G.add_edge('init_shell','lhd')
G.edge['init_shell']['lhd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['init_shell']['lhd']['fill'] = 'red'
G.add_edge('init_shell','lhd')
G.edge['init_shell']['lhd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('init_shell','lmkd')
G.edge['init_shell']['lmkd']['write-read'] = '[remove_name search][write read]'
G.edge['init_shell']['lmkd']['fill'] = 'red'
G.add_edge('init_shell','lpm')
G.edge['init_shell']['lpm']['write-read'] = '[open open][write read]'
G.edge['init_shell']['lpm']['fill'] = 'red'
G.add_edge('init_shell','lpm')
G.edge['init_shell']['lpm']['write-read'] = '[open open][write read][append read]'
G.add_edge('init_shell','macloader')
G.edge['init_shell']['macloader']['write-read'] = '[open open][write read]'
G.edge['init_shell']['macloader']['fill'] = 'red'
G.add_edge('init_shell','macloader')
G.edge['init_shell']['macloader']['write-read'] = '[open open][write read][append read]'
G.add_edge('init_shell','mdm_helper')
G.edge['init_shell']['mdm_helper']['write-read'] = '[write read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read]'
G.edge['init_shell']['mdm_helper']['fill'] = 'red'
G.add_edge('init_shell','mediaserver')
G.edge['init_shell']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read]'
G.edge['init_shell']['mediaserver']['fill'] = 'red'
G.add_edge('init_shell','mediaserver')
G.edge['init_shell']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('init_shell','mfgloader')
G.edge['init_shell']['mfgloader']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][remove_name search][write read]'
G.edge['init_shell']['mfgloader']['fill'] = 'red'
G.add_edge('init_shell','mlexe')
G.edge['init_shell']['mlexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['init_shell']['mlexe']['fill'] = 'red'
G.add_edge('init_shell','mlexe')
G.edge['init_shell']['mlexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('init_shell','mm-pp-daemon')
G.edge['init_shell']['mm-pp-daemon']['write-read'] = '[open open][write read]'
G.edge['init_shell']['mm-pp-daemon']['fill'] = 'red'
G.add_edge('init_shell','mm-pp-daemon')
G.edge['init_shell']['mm-pp-daemon']['write-read'] = '[open open][write read][append read]'
G.add_edge('init_shell','mm-pp-daemon')
G.edge['init_shell']['mm-pp-daemon']['write-read'] = '[open open][write read][append read][write read]'
G.edge['init_shell']['mm-pp-daemon']['fill'] = 'red'
G.add_edge('init_shell','mm-qcamera-daemon')
G.edge['init_shell']['mm-qcamera-daemon']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['init_shell']['mm-qcamera-daemon']['fill'] = 'red'
G.add_edge('init_shell','mm-qcamera-daemon')
G.edge['init_shell']['mm-qcamera-daemon']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('init_shell','mpdecision')
G.edge['init_shell']['mpdecision']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['init_shell']['mpdecision']['fill'] = 'red'
G.add_edge('init_shell','mpdecision')
G.edge['init_shell']['mpdecision']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('init_shell','mpdecision')
G.edge['init_shell']['mpdecision']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read][write read]'
G.edge['init_shell']['mpdecision']['fill'] = 'red'
G.add_edge('init_shell','netd')
G.edge['init_shell']['netd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][write read]'
G.edge['init_shell']['netd']['fill'] = 'red'
G.add_edge('init_shell','netmgrd')
G.edge['init_shell']['netmgrd']['write-read'] = '[open open][open open][write read][write read][add_name search][add_name search][remove_name search][add_name search][remove_name search][write read]'
G.edge['init_shell']['netmgrd']['fill'] = 'red'
G.add_edge('init_shell','nfc')
G.edge['init_shell']['nfc']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['init_shell']['nfc']['fill'] = 'red'
G.add_edge('init_shell','oneseg_mw')
G.edge['init_shell']['oneseg_mw']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['init_shell']['oneseg_mw']['fill'] = 'red'
G.add_edge('init_shell','oneseg_mw')
G.edge['init_shell']['oneseg_mw']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('init_shell','perfd')
G.edge['init_shell']['perfd']['write-read'] = '[write read]'
G.edge['init_shell']['perfd']['fill'] = 'red'
G.add_edge('init_shell','qcks')
G.edge['init_shell']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][add_name search][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['init_shell']['qcks']['fill'] = 'red'
G.add_edge('init_shell','qcks')
G.edge['init_shell']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][add_name search][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('init_shell','qmuxd')
G.edge['init_shell']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read][append read][write read][append read][open open][write read]'
G.edge['init_shell']['qmuxd']['fill'] = 'red'
G.add_edge('init_shell','qmuxd')
G.edge['init_shell']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read][append read][write read][append read][open open][write read][append read]'
G.add_edge('init_shell','qosmgr')
G.edge['init_shell']['qosmgr']['write-read'] = '[write read]'
G.edge['init_shell']['qosmgr']['fill'] = 'red'
G.add_edge('init_shell','radio')
G.edge['init_shell']['radio']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][append read]'
G.add_edge('init_shell','rild')
G.edge['init_shell']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][open open][setattr getattr][write read][append read][write read][append read][write read][append read][open open][setattr getattr][write read]'
G.edge['init_shell']['rild']['fill'] = 'red'
G.add_edge('init_shell','rild')
G.edge['init_shell']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][open open][setattr getattr][write read][append read][write read][append read][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('init_shell','rmt_storage')
G.edge['init_shell']['rmt_storage']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['init_shell']['rmt_storage']['fill'] = 'red'
G.add_edge('init_shell','rmt_storage')
G.edge['init_shell']['rmt_storage']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('init_shell','rtcc')
G.edge['init_shell']['rtcc']['write-read'] = '[setattr getattr][open open][write read][add_name search][remove_name search][setattr getattr][write read]'
G.edge['init_shell']['rtcc']['fill'] = 'red'
G.add_edge('init_shell','sec-ril')
G.edge['init_shell']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['init_shell']['sec-ril']['fill'] = 'red'
G.add_edge('init_shell','sec-ril')
G.edge['init_shell']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('init_shell','sensorhubservice')
G.edge['init_shell']['sensorhubservice']['write-read'] = '[write read]'
G.edge['init_shell']['sensorhubservice']['fill'] = 'red'
G.add_edge('init_shell','smdexe')
G.edge['init_shell']['smdexe']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['init_shell']['smdexe']['fill'] = 'red'
G.add_edge('init_shell','smdexe')
G.edge['init_shell']['smdexe']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('init_shell','ssr_setup')
G.edge['init_shell']['ssr_setup']['write-read'] = '[open open][write read]'
G.edge['init_shell']['ssr_setup']['fill'] = 'red'
G.add_edge('init_shell','ssr_setup')
G.edge['init_shell']['ssr_setup']['write-read'] = '[open open][write read][append read]'
G.add_edge('init_shell','sswap')
G.edge['init_shell']['sswap']['write-read'] = '[open open][write read]'
G.edge['init_shell']['sswap']['fill'] = 'red'
G.add_edge('init_shell','sswap')
G.edge['init_shell']['sswap']['write-read'] = '[open open][write read][append read]'
G.add_edge('init_shell','surfaceflinger')
G.edge['init_shell']['surfaceflinger']['write-read'] = '[open open][write read]'
G.edge['init_shell']['surfaceflinger']['fill'] = 'red'
G.add_edge('init_shell','surfaceflinger')
G.edge['init_shell']['surfaceflinger']['write-read'] = '[open open][write read][append read]'
G.add_edge('init_shell','surfaceflinger')
G.edge['init_shell']['surfaceflinger']['write-read'] = '[open open][write read][append read][write read]'
G.edge['init_shell']['surfaceflinger']['fill'] = 'red'
G.add_edge('init_shell','system_server')
G.edge['init_shell']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read]'
G.edge['init_shell']['system_server']['fill'] = 'red'
G.add_edge('init_shell','system_server')
G.edge['init_shell']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read]'
G.add_edge('init_shell','system_server')
G.edge['init_shell']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read]'
G.edge['init_shell']['system_server']['fill'] = 'red'
G.add_edge('init_shell','system_server')
G.edge['init_shell']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read]'
G.add_edge('init_shell','thermald')
G.edge['init_shell']['thermald']['write-read'] = '[open open][write read][add_name search][remove_name search][write read]'
G.edge['init_shell']['thermald']['fill'] = 'red'
G.add_edge('init_shell','thermal-engine')
G.edge['init_shell']['thermal-engine']['write-read'] = '[open open][write read]'
G.edge['init_shell']['thermal-engine']['fill'] = 'red'
G.add_edge('init_shell','thermal-engine')
G.edge['init_shell']['thermal-engine']['write-read'] = '[open open][write read][append read]'
G.add_edge('init_shell','thermal-engine')
G.edge['init_shell']['thermal-engine']['write-read'] = '[open open][write read][append read][write read]'
G.edge['init_shell']['thermal-engine']['fill'] = 'red'
G.add_edge('init_shell','ueventd')
G.edge['init_shell']['ueventd']['write-read'] = '[setattr getattr][open open][write read][append read][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['init_shell']['ueventd']['fill'] = 'red'
G.add_edge('init_shell','ueventd')
G.edge['init_shell']['ueventd']['write-read'] = '[setattr getattr][open open][write read][append read][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('init_shell','vm_bms')
G.edge['init_shell']['vm_bms']['write-read'] = '[open open][write read]'
G.edge['init_shell']['vm_bms']['fill'] = 'red'
G.add_edge('init_shell','vm_bms')
G.edge['init_shell']['vm_bms']['write-read'] = '[open open][write read][append read]'
G.add_edge('init_shell','vmwared')
G.edge['init_shell']['vmwared']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][add_name search][remove_name search][write read]'
G.edge['init_shell']['vmwared']['fill'] = 'red'
G.add_edge('init_shell','vold')
G.edge['init_shell']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read]'
G.edge['init_shell']['vold']['fill'] = 'red'
G.add_edge('init_shell','vold')
G.edge['init_shell']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('init_shell','zygote')
G.edge['init_shell']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][write read]'
G.edge['init_shell']['zygote']['fill'] = 'red'
G.add_edge('kernel','ueventd')
G.edge['kernel']['ueventd']['write-read'] = '[relabelto relabelfrom][open open][setattr getattr][write read][append read][relabelto relabelfrom]'
G.add_edge('ks','at_distributor')
G.edge['ks']['at_distributor']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('ks','bauthserver')
G.edge['ks']['bauthserver']['write-read'] = '[open open]'
G.add_edge('ks','bintvoutservice')
G.edge['ks']['bintvoutservice']['write-read'] = '[open open]'
G.add_edge('ks','bluetooth')
G.edge['ks']['bluetooth']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('ks','cbd')
G.edge['ks']['cbd']['write-read'] = '[open open]'
G.add_edge('ks','cellgeofenced')
G.edge['ks']['cellgeofenced']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('ks','charger_monitor')
G.edge['ks']['charger_monitor']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('ks','charger_monitor')
G.edge['ks']['charger_monitor']['write-read'] = '[open open][write read][append read][open open][open open]'
G.add_edge('ks','cnd')
G.edge['ks']['cnd']['write-read'] = '[open open][append read][open open]'
G.add_edge('ks','connfwexe')
G.edge['ks']['connfwexe']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('ks','debuggerd')
G.edge['ks']['debuggerd']['write-read'] = '[open open]'
G.add_edge('ks','diag_uart_log')
G.edge['ks']['diag_uart_log']['write-read'] = '[open open]'
G.add_edge('ks','dumpstate')
G.edge['ks']['dumpstate']['write-read'] = '[open open]'
G.add_edge('ks','efsks')
G.edge['ks']['efsks']['write-read'] = '[open open][write read][add_name search][open open][write read][add_name search][open open]'
G.add_edge('ks','geomagneticd')
G.edge['ks']['geomagneticd']['write-read'] = '[open open]'
G.add_edge('ks','gpsd')
G.edge['ks']['gpsd']['write-read'] = '[open open]'
G.add_edge('ks','init_shell')
G.edge['ks']['init_shell']['write-read'] = '[open open][write read][add_name search][remove_name search][write read][open open]'
G.add_edge('ks','kiesexe')
G.edge['ks']['kiesexe']['write-read'] = '[open open]'
G.add_edge('ks','ks')
G.edge['ks']['ks']['write-read'] = '[open open][write read][add_name search][open open][write read][add_name search][open open][append read][open open]'
G.add_edge('ks','lhd')
G.edge['ks']['lhd']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('ks','lpm')
G.edge['ks']['lpm']['write-read'] = '[open open]'
G.add_edge('ks','macloader')
G.edge['ks']['macloader']['write-read'] = '[open open]'
G.add_edge('ks','mdm_helper')
G.edge['ks']['mdm_helper']['write-read'] = '[write read][open open][append read][open open]'
G.add_edge('ks','mediaserver')
G.edge['ks']['mediaserver']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('ks','mlexe')
G.edge['ks']['mlexe']['write-read'] = '[open open]'
G.add_edge('ks','mm-pp-daemon')
G.edge['ks']['mm-pp-daemon']['write-read'] = '[open open]'
G.add_edge('ks','mm-qcamera-daemon')
G.edge['ks']['mm-qcamera-daemon']['write-read'] = '[open open]'
G.add_edge('ks','mpdecision')
G.edge['ks']['mpdecision']['write-read'] = '[open open]'
G.add_edge('ks','oneseg_mw')
G.edge['ks']['oneseg_mw']['write-read'] = '[open open]'
G.add_edge('ks','qcks')
G.edge['ks']['qcks']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][open open][append read][open open]'
G.add_edge('ks','qmuxd')
G.edge['ks']['qmuxd']['write-read'] = '[open open][open open][append read][write read][append read][open open]'
G.add_edge('ks','radio')
G.edge['ks']['radio']['write-read'] = '[open open]'
G.add_edge('ks','rild')
G.edge['ks']['rild']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('ks','rmt_storage')
G.edge['ks']['rmt_storage']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('ks','sec-ril')
G.edge['ks']['sec-ril']['write-read'] = '[open open][write read][open open]'
G.add_edge('ks','smdexe')
G.edge['ks']['smdexe']['write-read'] = '[open open]'
G.add_edge('ks','ssr_setup')
G.edge['ks']['ssr_setup']['write-read'] = '[open open]'
G.add_edge('ks','sswap')
G.edge['ks']['sswap']['write-read'] = '[open open]'
G.add_edge('ks','surfaceflinger')
G.edge['ks']['surfaceflinger']['write-read'] = '[open open]'
G.add_edge('ks','system_server')
G.edge['ks']['system_server']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('ks','system_server')
G.edge['ks']['system_server']['write-read'] = '[open open][write read][append read][open open][open open]'
G.add_edge('ks','thermal-engine')
G.edge['ks']['thermal-engine']['write-read'] = '[open open]'
G.add_edge('ks','ueventd')
G.edge['ks']['ueventd']['write-read'] = '[open open]'
G.add_edge('ks','vm_bms')
G.edge['ks']['vm_bms']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('ks','vold')
G.edge['ks']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('ks','init_shell')
G.edge['ks']['init_shell']['write-read'] = '[open open][write read][add_name search][remove_name search][write read][open open][setattr getattr]'
G.add_edge('ks','rild')
G.edge['ks']['rild']['write-read'] = '[open open][write read][append read][open open][setattr getattr]'
G.add_edge('ks','rtcc')
G.edge['ks']['rtcc']['write-read'] = '[setattr getattr]'
G.add_edge('ks','sec-ril')
G.edge['ks']['sec-ril']['write-read'] = '[open open][write read][open open][setattr getattr]'
G.add_edge('ks','system_server')
G.edge['ks']['system_server']['write-read'] = '[open open][write read][append read][open open][open open][setattr getattr]'
G.add_edge('ks','at_distributor')
G.edge['ks']['at_distributor']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['ks']['at_distributor']['fill'] = 'red'
G.add_edge('ks','at_distributor')
G.edge['ks']['at_distributor']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('ks','bauthserver')
G.edge['ks']['bauthserver']['write-read'] = '[open open][write read]'
G.edge['ks']['bauthserver']['fill'] = 'red'
G.add_edge('ks','bauthserver')
G.edge['ks']['bauthserver']['write-read'] = '[open open][write read][append read]'
G.add_edge('ks','bintvoutservice')
G.edge['ks']['bintvoutservice']['write-read'] = '[open open][write read]'
G.edge['ks']['bintvoutservice']['fill'] = 'red'
G.add_edge('ks','bintvoutservice')
G.edge['ks']['bintvoutservice']['write-read'] = '[open open][write read][append read]'
G.add_edge('ks','bluetooth')
G.edge['ks']['bluetooth']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['ks']['bluetooth']['fill'] = 'red'
G.add_edge('ks','bluetooth')
G.edge['ks']['bluetooth']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('ks','bootanim')
G.edge['ks']['bootanim']['write-read'] = '[write read]'
G.edge['ks']['bootanim']['fill'] = 'red'
G.add_edge('ks','cbd')
G.edge['ks']['cbd']['write-read'] = '[open open][write read]'
G.edge['ks']['cbd']['fill'] = 'red'
G.add_edge('ks','cbd')
G.edge['ks']['cbd']['write-read'] = '[open open][write read][append read]'
G.add_edge('ks','cellgeofenced')
G.edge['ks']['cellgeofenced']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['ks']['cellgeofenced']['fill'] = 'red'
G.add_edge('ks','cellgeofenced')
G.edge['ks']['cellgeofenced']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('ks','charger_monitor')
G.edge['ks']['charger_monitor']['write-read'] = '[open open][write read][append read][open open][open open][write read]'
G.edge['ks']['charger_monitor']['fill'] = 'red'
G.add_edge('ks','charger_monitor')
G.edge['ks']['charger_monitor']['write-read'] = '[open open][write read][append read][open open][open open][write read][append read]'
G.add_edge('ks','charger_monitor')
G.edge['ks']['charger_monitor']['write-read'] = '[open open][write read][append read][open open][open open][write read][append read][write read]'
G.edge['ks']['charger_monitor']['fill'] = 'red'
G.add_edge('ks','charger_monitor')
G.edge['ks']['charger_monitor']['write-read'] = '[open open][write read][append read][open open][open open][write read][append read][write read][append read]'
G.add_edge('ks','cnd')
G.edge['ks']['cnd']['write-read'] = '[open open][append read][open open][write read]'
G.edge['ks']['cnd']['fill'] = 'red'
G.add_edge('ks','cnd')
G.edge['ks']['cnd']['write-read'] = '[open open][append read][open open][write read][append read]'
G.add_edge('ks','connfwexe')
G.edge['ks']['connfwexe']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['ks']['connfwexe']['fill'] = 'red'
G.add_edge('ks','connfwexe')
G.edge['ks']['connfwexe']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('ks','debuggerd')
G.edge['ks']['debuggerd']['write-read'] = '[open open][write read]'
G.edge['ks']['debuggerd']['fill'] = 'red'
G.add_edge('ks','debuggerd')
G.edge['ks']['debuggerd']['write-read'] = '[open open][write read][append read]'
G.add_edge('ks','diag_uart_log')
G.edge['ks']['diag_uart_log']['write-read'] = '[open open][write read]'
G.edge['ks']['diag_uart_log']['fill'] = 'red'
G.add_edge('ks','diag_uart_log')
G.edge['ks']['diag_uart_log']['write-read'] = '[open open][write read][append read]'
G.add_edge('ks','dumpstate')
G.edge['ks']['dumpstate']['write-read'] = '[open open][write read]'
G.edge['ks']['dumpstate']['fill'] = 'red'
G.add_edge('ks','dumpstate')
G.edge['ks']['dumpstate']['write-read'] = '[open open][write read][append read]'
G.add_edge('ks','efsks')
G.edge['ks']['efsks']['write-read'] = '[open open][write read][add_name search][open open][write read][add_name search][open open][write read]'
G.edge['ks']['efsks']['fill'] = 'red'
G.add_edge('ks','efsks')
G.edge['ks']['efsks']['write-read'] = '[open open][write read][add_name search][open open][write read][add_name search][open open][write read][append read]'
G.add_edge('ks','geomagneticd')
G.edge['ks']['geomagneticd']['write-read'] = '[open open][write read]'
G.edge['ks']['geomagneticd']['fill'] = 'red'
G.add_edge('ks','geomagneticd')
G.edge['ks']['geomagneticd']['write-read'] = '[open open][write read][append read]'
G.add_edge('ks','gpsd')
G.edge['ks']['gpsd']['write-read'] = '[open open][write read]'
G.edge['ks']['gpsd']['fill'] = 'red'
G.add_edge('ks','gpsd')
G.edge['ks']['gpsd']['write-read'] = '[open open][write read][append read]'
G.add_edge('ks','healthd')
G.edge['ks']['healthd']['write-read'] = '[open open][write read][append read][write read]'
G.edge['ks']['healthd']['fill'] = 'red'
G.add_edge('ks','init_shell')
G.edge['ks']['init_shell']['write-read'] = '[open open][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read]'
G.edge['ks']['init_shell']['fill'] = 'red'
G.add_edge('ks','init_shell')
G.edge['ks']['init_shell']['write-read'] = '[open open][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read]'
G.add_edge('ks','jackservice')
G.edge['ks']['jackservice']['write-read'] = '[write read]'
G.edge['ks']['jackservice']['fill'] = 'red'
G.add_edge('ks','kiesexe')
G.edge['ks']['kiesexe']['write-read'] = '[open open][write read]'
G.edge['ks']['kiesexe']['fill'] = 'red'
G.add_edge('ks','kiesexe')
G.edge['ks']['kiesexe']['write-read'] = '[open open][write read][append read]'
G.add_edge('ks','ks')
G.edge['ks']['ks']['write-read'] = '[open open][write read][add_name search][open open][write read][add_name search][open open][append read][open open][write read]'
G.edge['ks']['ks']['fill'] = 'red'
G.add_edge('ks','ks')
G.edge['ks']['ks']['write-read'] = '[open open][write read][add_name search][open open][write read][add_name search][open open][append read][open open][write read][append read]'
G.add_edge('ks','lhd')
G.edge['ks']['lhd']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['ks']['lhd']['fill'] = 'red'
G.add_edge('ks','lhd')
G.edge['ks']['lhd']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('ks','lmkd')
G.edge['ks']['lmkd']['write-read'] = '[write read]'
G.edge['ks']['lmkd']['fill'] = 'red'
G.add_edge('ks','lpm')
G.edge['ks']['lpm']['write-read'] = '[open open][write read]'
G.edge['ks']['lpm']['fill'] = 'red'
G.add_edge('ks','lpm')
G.edge['ks']['lpm']['write-read'] = '[open open][write read][append read]'
G.add_edge('ks','macloader')
G.edge['ks']['macloader']['write-read'] = '[open open][write read]'
G.edge['ks']['macloader']['fill'] = 'red'
G.add_edge('ks','macloader')
G.edge['ks']['macloader']['write-read'] = '[open open][write read][append read]'
G.add_edge('ks','mdm_helper')
G.edge['ks']['mdm_helper']['write-read'] = '[write read][open open][append read][open open][write read]'
G.edge['ks']['mdm_helper']['fill'] = 'red'
G.add_edge('ks','mediaserver')
G.edge['ks']['mediaserver']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['ks']['mediaserver']['fill'] = 'red'
G.add_edge('ks','mediaserver')
G.edge['ks']['mediaserver']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('ks','mfgloader')
G.edge['ks']['mfgloader']['write-read'] = '[write read]'
G.edge['ks']['mfgloader']['fill'] = 'red'
G.add_edge('ks','mlexe')
G.edge['ks']['mlexe']['write-read'] = '[open open][write read]'
G.edge['ks']['mlexe']['fill'] = 'red'
G.add_edge('ks','mlexe')
G.edge['ks']['mlexe']['write-read'] = '[open open][write read][append read]'
G.add_edge('ks','mm-pp-daemon')
G.edge['ks']['mm-pp-daemon']['write-read'] = '[open open][write read]'
G.edge['ks']['mm-pp-daemon']['fill'] = 'red'
G.add_edge('ks','mm-pp-daemon')
G.edge['ks']['mm-pp-daemon']['write-read'] = '[open open][write read][append read]'
G.add_edge('ks','mm-pp-daemon')
G.edge['ks']['mm-pp-daemon']['write-read'] = '[open open][write read][append read][write read]'
G.edge['ks']['mm-pp-daemon']['fill'] = 'red'
G.add_edge('ks','mm-qcamera-daemon')
G.edge['ks']['mm-qcamera-daemon']['write-read'] = '[open open][write read]'
G.edge['ks']['mm-qcamera-daemon']['fill'] = 'red'
G.add_edge('ks','mm-qcamera-daemon')
G.edge['ks']['mm-qcamera-daemon']['write-read'] = '[open open][write read][append read]'
G.add_edge('ks','mpdecision')
G.edge['ks']['mpdecision']['write-read'] = '[open open][write read]'
G.edge['ks']['mpdecision']['fill'] = 'red'
G.add_edge('ks','mpdecision')
G.edge['ks']['mpdecision']['write-read'] = '[open open][write read][append read]'
G.add_edge('ks','mpdecision')
G.edge['ks']['mpdecision']['write-read'] = '[open open][write read][append read][write read]'
G.edge['ks']['mpdecision']['fill'] = 'red'
G.add_edge('ks','netd')
G.edge['ks']['netd']['write-read'] = '[write read]'
G.edge['ks']['netd']['fill'] = 'red'
G.add_edge('ks','netmgrd')
G.edge['ks']['netmgrd']['write-read'] = '[write read]'
G.edge['ks']['netmgrd']['fill'] = 'red'
G.add_edge('ks','nfc')
G.edge['ks']['nfc']['write-read'] = '[write read]'
G.edge['ks']['nfc']['fill'] = 'red'
G.add_edge('ks','oneseg_mw')
G.edge['ks']['oneseg_mw']['write-read'] = '[open open][write read]'
G.edge['ks']['oneseg_mw']['fill'] = 'red'
G.add_edge('ks','oneseg_mw')
G.edge['ks']['oneseg_mw']['write-read'] = '[open open][write read][append read]'
G.add_edge('ks','perfd')
G.edge['ks']['perfd']['write-read'] = '[write read]'
G.edge['ks']['perfd']['fill'] = 'red'
G.add_edge('ks','qcks')
G.edge['ks']['qcks']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][open open][append read][open open][write read]'
G.edge['ks']['qcks']['fill'] = 'red'
G.add_edge('ks','qcks')
G.edge['ks']['qcks']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][open open][append read][open open][write read][append read]'
G.add_edge('ks','qmuxd')
G.edge['ks']['qmuxd']['write-read'] = '[open open][open open][append read][write read][append read][open open][write read]'
G.edge['ks']['qmuxd']['fill'] = 'red'
G.add_edge('ks','qmuxd')
G.edge['ks']['qmuxd']['write-read'] = '[open open][open open][append read][write read][append read][open open][write read][append read]'
G.add_edge('ks','qosmgr')
G.edge['ks']['qosmgr']['write-read'] = '[write read]'
G.edge['ks']['qosmgr']['fill'] = 'red'
G.add_edge('ks','radio')
G.edge['ks']['radio']['write-read'] = '[open open][append read]'
G.add_edge('ks','rild')
G.edge['ks']['rild']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read]'
G.edge['ks']['rild']['fill'] = 'red'
G.add_edge('ks','rild')
G.edge['ks']['rild']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('ks','rmt_storage')
G.edge['ks']['rmt_storage']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['ks']['rmt_storage']['fill'] = 'red'
G.add_edge('ks','rmt_storage')
G.edge['ks']['rmt_storage']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('ks','rtcc')
G.edge['ks']['rtcc']['write-read'] = '[setattr getattr][write read]'
G.edge['ks']['rtcc']['fill'] = 'red'
G.add_edge('ks','sec-ril')
G.edge['ks']['sec-ril']['write-read'] = '[open open][write read][open open][setattr getattr][write read]'
G.edge['ks']['sec-ril']['fill'] = 'red'
G.add_edge('ks','sec-ril')
G.edge['ks']['sec-ril']['write-read'] = '[open open][write read][open open][setattr getattr][write read][append read]'
G.add_edge('ks','sensorhubservice')
G.edge['ks']['sensorhubservice']['write-read'] = '[write read]'
G.edge['ks']['sensorhubservice']['fill'] = 'red'
G.add_edge('ks','smdexe')
G.edge['ks']['smdexe']['write-read'] = '[open open][write read]'
G.edge['ks']['smdexe']['fill'] = 'red'
G.add_edge('ks','smdexe')
G.edge['ks']['smdexe']['write-read'] = '[open open][write read][append read]'
G.add_edge('ks','ssr_setup')
G.edge['ks']['ssr_setup']['write-read'] = '[open open][write read]'
G.edge['ks']['ssr_setup']['fill'] = 'red'
G.add_edge('ks','ssr_setup')
G.edge['ks']['ssr_setup']['write-read'] = '[open open][write read][append read]'
G.add_edge('ks','sswap')
G.edge['ks']['sswap']['write-read'] = '[open open][write read]'
G.edge['ks']['sswap']['fill'] = 'red'
G.add_edge('ks','sswap')
G.edge['ks']['sswap']['write-read'] = '[open open][write read][append read]'
G.add_edge('ks','surfaceflinger')
G.edge['ks']['surfaceflinger']['write-read'] = '[open open][write read]'
G.edge['ks']['surfaceflinger']['fill'] = 'red'
G.add_edge('ks','surfaceflinger')
G.edge['ks']['surfaceflinger']['write-read'] = '[open open][write read][append read]'
G.add_edge('ks','surfaceflinger')
G.edge['ks']['surfaceflinger']['write-read'] = '[open open][write read][append read][write read]'
G.edge['ks']['surfaceflinger']['fill'] = 'red'
G.add_edge('ks','system_server')
G.edge['ks']['system_server']['write-read'] = '[open open][write read][append read][open open][open open][setattr getattr][write read]'
G.edge['ks']['system_server']['fill'] = 'red'
G.add_edge('ks','system_server')
G.edge['ks']['system_server']['write-read'] = '[open open][write read][append read][open open][open open][setattr getattr][write read][append read]'
G.add_edge('ks','system_server')
G.edge['ks']['system_server']['write-read'] = '[open open][write read][append read][open open][open open][setattr getattr][write read][append read][write read]'
G.edge['ks']['system_server']['fill'] = 'red'
G.add_edge('ks','system_server')
G.edge['ks']['system_server']['write-read'] = '[open open][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read]'
G.add_edge('ks','thermald')
G.edge['ks']['thermald']['write-read'] = '[write read]'
G.edge['ks']['thermald']['fill'] = 'red'
G.add_edge('ks','thermal-engine')
G.edge['ks']['thermal-engine']['write-read'] = '[open open][write read]'
G.edge['ks']['thermal-engine']['fill'] = 'red'
G.add_edge('ks','thermal-engine')
G.edge['ks']['thermal-engine']['write-read'] = '[open open][write read][append read]'
G.add_edge('ks','thermal-engine')
G.edge['ks']['thermal-engine']['write-read'] = '[open open][write read][append read][write read]'
G.edge['ks']['thermal-engine']['fill'] = 'red'
G.add_edge('ks','ueventd')
G.edge['ks']['ueventd']['write-read'] = '[open open][write read]'
G.edge['ks']['ueventd']['fill'] = 'red'
G.add_edge('ks','ueventd')
G.edge['ks']['ueventd']['write-read'] = '[open open][write read][append read]'
G.add_edge('ks','vm_bms')
G.edge['ks']['vm_bms']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['ks']['vm_bms']['fill'] = 'red'
G.add_edge('ks','vm_bms')
G.edge['ks']['vm_bms']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('ks','vmwared')
G.edge['ks']['vmwared']['write-read'] = '[write read]'
G.edge['ks']['vmwared']['fill'] = 'red'
G.add_edge('ks','vold')
G.edge['ks']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read]'
G.edge['ks']['vold']['fill'] = 'red'
G.add_edge('ks','vold')
G.edge['ks']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read]'
G.add_edge('ks','zygote')
G.edge['ks']['zygote']['write-read'] = '[write read]'
G.edge['ks']['zygote']['fill'] = 'red'
G.add_edge('lhd','at_distributor')
G.edge['lhd']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('lhd','bauthserver')
G.edge['lhd']['bauthserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('lhd','bintvoutservice')
G.edge['lhd']['bintvoutservice']['write-read'] = '[open open]'
G.add_edge('lhd','bluetooth')
G.edge['lhd']['bluetooth']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('lhd','cbd')
G.edge['lhd']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('lhd','cellgeofenced')
G.edge['lhd']['cellgeofenced']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('lhd','charger_monitor')
G.edge['lhd']['charger_monitor']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('lhd','charger_monitor')
G.edge['lhd']['charger_monitor']['write-read'] = '[open open][write read][append read][open open][open open]'
G.add_edge('lhd','cnd')
G.edge['lhd']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][append read][open open]'
G.add_edge('lhd','connfwexe')
G.edge['lhd']['connfwexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('lhd','debuggerd')
G.edge['lhd']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('lhd','diag_uart_log')
G.edge['lhd']['diag_uart_log']['write-read'] = '[open open]'
G.add_edge('lhd','dumpstate')
G.edge['lhd']['dumpstate']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('lhd','efsks')
G.edge['lhd']['efsks']['write-read'] = '[open open]'
G.add_edge('lhd','geomagneticd')
G.edge['lhd']['geomagneticd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open]'
G.add_edge('lhd','gpsd')
G.edge['lhd']['gpsd']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('lhd','init_shell')
G.edge['lhd']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('lhd','kiesexe')
G.edge['lhd']['kiesexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('lhd','ks')
G.edge['lhd']['ks']['write-read'] = '[open open][append read][open open]'
G.add_edge('lhd','lhd')
G.edge['lhd']['lhd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('lhd','lpm')
G.edge['lhd']['lpm']['write-read'] = '[open open]'
G.add_edge('lhd','macloader')
G.edge['lhd']['macloader']['write-read'] = '[open open]'
G.add_edge('lhd','mdm_helper')
G.edge['lhd']['mdm_helper']['write-read'] = '[open open][append read][open open]'
G.add_edge('lhd','mediaserver')
G.edge['lhd']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('lhd','mlexe')
G.edge['lhd']['mlexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('lhd','mm-pp-daemon')
G.edge['lhd']['mm-pp-daemon']['write-read'] = '[open open]'
G.add_edge('lhd','mm-qcamera-daemon')
G.edge['lhd']['mm-qcamera-daemon']['write-read'] = '[open open][write read][add_name search][remove_name search][open open]'
G.add_edge('lhd','mpdecision')
G.edge['lhd']['mpdecision']['write-read'] = '[open open][write read][add_name search][remove_name search][open open]'
G.add_edge('lhd','oneseg_mw')
G.edge['lhd']['oneseg_mw']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('lhd','qcks')
G.edge['lhd']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][append read][open open]'
G.add_edge('lhd','qmuxd')
G.edge['lhd']['qmuxd']['write-read'] = '[open open][open open][append read][write read][append read][open open]'
G.add_edge('lhd','radio')
G.edge['lhd']['radio']['write-read'] = '[open open]'
G.add_edge('lhd','rild')
G.edge['lhd']['rild']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('lhd','rmt_storage')
G.edge['lhd']['rmt_storage']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('lhd','sec-ril')
G.edge['lhd']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][open open]'
G.add_edge('lhd','smdexe')
G.edge['lhd']['smdexe']['write-read'] = '[open open]'
G.add_edge('lhd','ssr_setup')
G.edge['lhd']['ssr_setup']['write-read'] = '[open open]'
G.add_edge('lhd','sswap')
G.edge['lhd']['sswap']['write-read'] = '[open open]'
G.add_edge('lhd','surfaceflinger')
G.edge['lhd']['surfaceflinger']['write-read'] = '[open open]'
G.add_edge('lhd','system_server')
G.edge['lhd']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('lhd','system_server')
G.edge['lhd']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][open open]'
G.add_edge('lhd','thermal-engine')
G.edge['lhd']['thermal-engine']['write-read'] = '[open open]'
G.add_edge('lhd','ueventd')
G.edge['lhd']['ueventd']['write-read'] = '[open open]'
G.add_edge('lhd','vm_bms')
G.edge['lhd']['vm_bms']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('lhd','vold')
G.edge['lhd']['vold']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('lhd','init_shell')
G.edge['lhd']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('lhd','rild')
G.edge['lhd']['rild']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr]'
G.add_edge('lhd','rtcc')
G.edge['lhd']['rtcc']['write-read'] = '[setattr getattr]'
G.add_edge('lhd','sec-ril')
G.edge['lhd']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][open open][setattr getattr]'
G.add_edge('lhd','system_server')
G.edge['lhd']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][open open][setattr getattr]'
G.add_edge('lhd','at_distributor')
G.edge['lhd']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read]'
G.edge['lhd']['at_distributor']['fill'] = 'red'
G.add_edge('lhd','at_distributor')
G.edge['lhd']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read]'
G.add_edge('lhd','bauthserver')
G.edge['lhd']['bauthserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['lhd']['bauthserver']['fill'] = 'red'
G.add_edge('lhd','bauthserver')
G.edge['lhd']['bauthserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('lhd','bintvoutservice')
G.edge['lhd']['bintvoutservice']['write-read'] = '[open open][write read]'
G.edge['lhd']['bintvoutservice']['fill'] = 'red'
G.add_edge('lhd','bintvoutservice')
G.edge['lhd']['bintvoutservice']['write-read'] = '[open open][write read][append read]'
G.add_edge('lhd','bluetooth')
G.edge['lhd']['bluetooth']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['lhd']['bluetooth']['fill'] = 'red'
G.add_edge('lhd','bluetooth')
G.edge['lhd']['bluetooth']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('lhd','bootanim')
G.edge['lhd']['bootanim']['write-read'] = '[write read]'
G.edge['lhd']['bootanim']['fill'] = 'red'
G.add_edge('lhd','cbd')
G.edge['lhd']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['lhd']['cbd']['fill'] = 'red'
G.add_edge('lhd','cbd')
G.edge['lhd']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('lhd','cellgeofenced')
G.edge['lhd']['cellgeofenced']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['lhd']['cellgeofenced']['fill'] = 'red'
G.add_edge('lhd','cellgeofenced')
G.edge['lhd']['cellgeofenced']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('lhd','charger_monitor')
G.edge['lhd']['charger_monitor']['write-read'] = '[open open][write read][append read][open open][open open][write read]'
G.edge['lhd']['charger_monitor']['fill'] = 'red'
G.add_edge('lhd','charger_monitor')
G.edge['lhd']['charger_monitor']['write-read'] = '[open open][write read][append read][open open][open open][write read][append read]'
G.add_edge('lhd','charger_monitor')
G.edge['lhd']['charger_monitor']['write-read'] = '[open open][write read][append read][open open][open open][write read][append read][write read]'
G.edge['lhd']['charger_monitor']['fill'] = 'red'
G.add_edge('lhd','charger_monitor')
G.edge['lhd']['charger_monitor']['write-read'] = '[open open][write read][append read][open open][open open][write read][append read][write read][append read]'
G.add_edge('lhd','cnd')
G.edge['lhd']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][append read][open open][write read]'
G.edge['lhd']['cnd']['fill'] = 'red'
G.add_edge('lhd','cnd')
G.edge['lhd']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][append read][open open][write read][append read]'
G.add_edge('lhd','connfwexe')
G.edge['lhd']['connfwexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read]'
G.edge['lhd']['connfwexe']['fill'] = 'red'
G.add_edge('lhd','connfwexe')
G.edge['lhd']['connfwexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read]'
G.add_edge('lhd','debuggerd')
G.edge['lhd']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['lhd']['debuggerd']['fill'] = 'red'
G.add_edge('lhd','debuggerd')
G.edge['lhd']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('lhd','diag_uart_log')
G.edge['lhd']['diag_uart_log']['write-read'] = '[open open][write read]'
G.edge['lhd']['diag_uart_log']['fill'] = 'red'
G.add_edge('lhd','diag_uart_log')
G.edge['lhd']['diag_uart_log']['write-read'] = '[open open][write read][append read]'
G.add_edge('lhd','dumpstate')
G.edge['lhd']['dumpstate']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read]'
G.edge['lhd']['dumpstate']['fill'] = 'red'
G.add_edge('lhd','dumpstate')
G.edge['lhd']['dumpstate']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('lhd','efsks')
G.edge['lhd']['efsks']['write-read'] = '[open open][write read]'
G.edge['lhd']['efsks']['fill'] = 'red'
G.add_edge('lhd','efsks')
G.edge['lhd']['efsks']['write-read'] = '[open open][write read][append read]'
G.add_edge('lhd','geomagneticd')
G.edge['lhd']['geomagneticd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['lhd']['geomagneticd']['fill'] = 'red'
G.add_edge('lhd','geomagneticd')
G.edge['lhd']['geomagneticd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('lhd','gpsd')
G.edge['lhd']['gpsd']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read]'
G.edge['lhd']['gpsd']['fill'] = 'red'
G.add_edge('lhd','gpsd')
G.edge['lhd']['gpsd']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('lhd','healthd')
G.edge['lhd']['healthd']['write-read'] = '[open open][write read][append read][write read]'
G.edge['lhd']['healthd']['fill'] = 'red'
G.add_edge('lhd','init_shell')
G.edge['lhd']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['lhd']['init_shell']['fill'] = 'red'
G.add_edge('lhd','init_shell')
G.edge['lhd']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('lhd','jackservice')
G.edge['lhd']['jackservice']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['lhd']['jackservice']['fill'] = 'red'
G.add_edge('lhd','kiesexe')
G.edge['lhd']['kiesexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['lhd']['kiesexe']['fill'] = 'red'
G.add_edge('lhd','kiesexe')
G.edge['lhd']['kiesexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('lhd','ks')
G.edge['lhd']['ks']['write-read'] = '[open open][append read][open open][write read]'
G.edge['lhd']['ks']['fill'] = 'red'
G.add_edge('lhd','ks')
G.edge['lhd']['ks']['write-read'] = '[open open][append read][open open][write read][append read]'
G.add_edge('lhd','lhd')
G.edge['lhd']['lhd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read]'
G.edge['lhd']['lhd']['fill'] = 'red'
G.add_edge('lhd','lhd')
G.edge['lhd']['lhd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read]'
G.add_edge('lhd','lmkd')
G.edge['lhd']['lmkd']['write-read'] = '[write read]'
G.edge['lhd']['lmkd']['fill'] = 'red'
G.add_edge('lhd','lpm')
G.edge['lhd']['lpm']['write-read'] = '[open open][write read]'
G.edge['lhd']['lpm']['fill'] = 'red'
G.add_edge('lhd','lpm')
G.edge['lhd']['lpm']['write-read'] = '[open open][write read][append read]'
G.add_edge('lhd','macloader')
G.edge['lhd']['macloader']['write-read'] = '[open open][write read]'
G.edge['lhd']['macloader']['fill'] = 'red'
G.add_edge('lhd','macloader')
G.edge['lhd']['macloader']['write-read'] = '[open open][write read][append read]'
G.add_edge('lhd','mdm_helper')
G.edge['lhd']['mdm_helper']['write-read'] = '[open open][append read][open open][write read]'
G.edge['lhd']['mdm_helper']['fill'] = 'red'
G.add_edge('lhd','mediaserver')
G.edge['lhd']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read]'
G.edge['lhd']['mediaserver']['fill'] = 'red'
G.add_edge('lhd','mediaserver')
G.edge['lhd']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read]'
G.add_edge('lhd','mfgloader')
G.edge['lhd']['mfgloader']['write-read'] = '[open open][write read][add_name search][remove_name search][write read]'
G.edge['lhd']['mfgloader']['fill'] = 'red'
G.add_edge('lhd','mlexe')
G.edge['lhd']['mlexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['lhd']['mlexe']['fill'] = 'red'
G.add_edge('lhd','mlexe')
G.edge['lhd']['mlexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('lhd','mm-pp-daemon')
G.edge['lhd']['mm-pp-daemon']['write-read'] = '[open open][write read]'
G.edge['lhd']['mm-pp-daemon']['fill'] = 'red'
G.add_edge('lhd','mm-pp-daemon')
G.edge['lhd']['mm-pp-daemon']['write-read'] = '[open open][write read][append read]'
G.add_edge('lhd','mm-pp-daemon')
G.edge['lhd']['mm-pp-daemon']['write-read'] = '[open open][write read][append read][write read]'
G.edge['lhd']['mm-pp-daemon']['fill'] = 'red'
G.add_edge('lhd','mm-qcamera-daemon')
G.edge['lhd']['mm-qcamera-daemon']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['lhd']['mm-qcamera-daemon']['fill'] = 'red'
G.add_edge('lhd','mm-qcamera-daemon')
G.edge['lhd']['mm-qcamera-daemon']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('lhd','mpdecision')
G.edge['lhd']['mpdecision']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['lhd']['mpdecision']['fill'] = 'red'
G.add_edge('lhd','mpdecision')
G.edge['lhd']['mpdecision']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('lhd','mpdecision')
G.edge['lhd']['mpdecision']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read][write read]'
G.edge['lhd']['mpdecision']['fill'] = 'red'
G.add_edge('lhd','netd')
G.edge['lhd']['netd']['write-read'] = '[write read]'
G.edge['lhd']['netd']['fill'] = 'red'
G.add_edge('lhd','netmgrd')
G.edge['lhd']['netmgrd']['write-read'] = '[open open][open open][write read][write read][add_name search][add_name search][remove_name search][write read]'
G.edge['lhd']['netmgrd']['fill'] = 'red'
G.add_edge('lhd','nfc')
G.edge['lhd']['nfc']['write-read'] = '[write read]'
G.edge['lhd']['nfc']['fill'] = 'red'
G.add_edge('lhd','oneseg_mw')
G.edge['lhd']['oneseg_mw']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['lhd']['oneseg_mw']['fill'] = 'red'
G.add_edge('lhd','oneseg_mw')
G.edge['lhd']['oneseg_mw']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('lhd','perfd')
G.edge['lhd']['perfd']['write-read'] = '[write read]'
G.edge['lhd']['perfd']['fill'] = 'red'
G.add_edge('lhd','qcks')
G.edge['lhd']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][append read][open open][write read]'
G.edge['lhd']['qcks']['fill'] = 'red'
G.add_edge('lhd','qcks')
G.edge['lhd']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][append read][open open][write read][append read]'
G.add_edge('lhd','qmuxd')
G.edge['lhd']['qmuxd']['write-read'] = '[open open][open open][append read][write read][append read][open open][write read]'
G.edge['lhd']['qmuxd']['fill'] = 'red'
G.add_edge('lhd','qmuxd')
G.edge['lhd']['qmuxd']['write-read'] = '[open open][open open][append read][write read][append read][open open][write read][append read]'
G.add_edge('lhd','qosmgr')
G.edge['lhd']['qosmgr']['write-read'] = '[write read]'
G.edge['lhd']['qosmgr']['fill'] = 'red'
G.add_edge('lhd','radio')
G.edge['lhd']['radio']['write-read'] = '[open open][append read]'
G.add_edge('lhd','rild')
G.edge['lhd']['rild']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['lhd']['rild']['fill'] = 'red'
G.add_edge('lhd','rild')
G.edge['lhd']['rild']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('lhd','rmt_storage')
G.edge['lhd']['rmt_storage']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['lhd']['rmt_storage']['fill'] = 'red'
G.add_edge('lhd','rmt_storage')
G.edge['lhd']['rmt_storage']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('lhd','rtcc')
G.edge['lhd']['rtcc']['write-read'] = '[setattr getattr][write read]'
G.edge['lhd']['rtcc']['fill'] = 'red'
G.add_edge('lhd','sec-ril')
G.edge['lhd']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][open open][setattr getattr][write read]'
G.edge['lhd']['sec-ril']['fill'] = 'red'
G.add_edge('lhd','sec-ril')
G.edge['lhd']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][open open][setattr getattr][write read][append read]'
G.add_edge('lhd','sensorhubservice')
G.edge['lhd']['sensorhubservice']['write-read'] = '[write read]'
G.edge['lhd']['sensorhubservice']['fill'] = 'red'
G.add_edge('lhd','smdexe')
G.edge['lhd']['smdexe']['write-read'] = '[open open][write read]'
G.edge['lhd']['smdexe']['fill'] = 'red'
G.add_edge('lhd','smdexe')
G.edge['lhd']['smdexe']['write-read'] = '[open open][write read][append read]'
G.add_edge('lhd','ssr_setup')
G.edge['lhd']['ssr_setup']['write-read'] = '[open open][write read]'
G.edge['lhd']['ssr_setup']['fill'] = 'red'
G.add_edge('lhd','ssr_setup')
G.edge['lhd']['ssr_setup']['write-read'] = '[open open][write read][append read]'
G.add_edge('lhd','sswap')
G.edge['lhd']['sswap']['write-read'] = '[open open][write read]'
G.edge['lhd']['sswap']['fill'] = 'red'
G.add_edge('lhd','sswap')
G.edge['lhd']['sswap']['write-read'] = '[open open][write read][append read]'
G.add_edge('lhd','surfaceflinger')
G.edge['lhd']['surfaceflinger']['write-read'] = '[open open][write read]'
G.edge['lhd']['surfaceflinger']['fill'] = 'red'
G.add_edge('lhd','surfaceflinger')
G.edge['lhd']['surfaceflinger']['write-read'] = '[open open][write read][append read]'
G.add_edge('lhd','surfaceflinger')
G.edge['lhd']['surfaceflinger']['write-read'] = '[open open][write read][append read][write read]'
G.edge['lhd']['surfaceflinger']['fill'] = 'red'
G.add_edge('lhd','system_server')
G.edge['lhd']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][open open][setattr getattr][write read]'
G.edge['lhd']['system_server']['fill'] = 'red'
G.add_edge('lhd','system_server')
G.edge['lhd']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][open open][setattr getattr][write read][append read]'
G.add_edge('lhd','system_server')
G.edge['lhd']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][open open][setattr getattr][write read][append read][write read]'
G.edge['lhd']['system_server']['fill'] = 'red'
G.add_edge('lhd','system_server')
G.edge['lhd']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read]'
G.add_edge('lhd','thermald')
G.edge['lhd']['thermald']['write-read'] = '[open open][write read][add_name search][remove_name search][write read]'
G.edge['lhd']['thermald']['fill'] = 'red'
G.add_edge('lhd','thermal-engine')
G.edge['lhd']['thermal-engine']['write-read'] = '[open open][write read]'
G.edge['lhd']['thermal-engine']['fill'] = 'red'
G.add_edge('lhd','thermal-engine')
G.edge['lhd']['thermal-engine']['write-read'] = '[open open][write read][append read]'
G.add_edge('lhd','thermal-engine')
G.edge['lhd']['thermal-engine']['write-read'] = '[open open][write read][append read][write read]'
G.edge['lhd']['thermal-engine']['fill'] = 'red'
G.add_edge('lhd','ueventd')
G.edge['lhd']['ueventd']['write-read'] = '[open open][write read]'
G.edge['lhd']['ueventd']['fill'] = 'red'
G.add_edge('lhd','ueventd')
G.edge['lhd']['ueventd']['write-read'] = '[open open][write read][append read]'
G.add_edge('lhd','vm_bms')
G.edge['lhd']['vm_bms']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['lhd']['vm_bms']['fill'] = 'red'
G.add_edge('lhd','vm_bms')
G.edge['lhd']['vm_bms']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('lhd','vmwared')
G.edge['lhd']['vmwared']['write-read'] = '[write read]'
G.edge['lhd']['vmwared']['fill'] = 'red'
G.add_edge('lhd','vold')
G.edge['lhd']['vold']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][write read]'
G.edge['lhd']['vold']['fill'] = 'red'
G.add_edge('lhd','vold')
G.edge['lhd']['vold']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][write read][append read]'
G.add_edge('lhd','zygote')
G.edge['lhd']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['lhd']['zygote']['fill'] = 'red'
G.add_edge('lpm','at_distributor')
G.edge['lpm']['at_distributor']['write-read'] = '[open open]'
G.add_edge('lpm','bauthserver')
G.edge['lpm']['bauthserver']['write-read'] = '[open open]'
G.add_edge('lpm','bintvoutservice')
G.edge['lpm']['bintvoutservice']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('lpm','bluetooth')
G.edge['lpm']['bluetooth']['write-read'] = '[open open]'
G.add_edge('lpm','cbd')
G.edge['lpm']['cbd']['write-read'] = '[open open]'
G.add_edge('lpm','cellgeofenced')
G.edge['lpm']['cellgeofenced']['write-read'] = '[open open]'
G.add_edge('lpm','charger_monitor')
G.edge['lpm']['charger_monitor']['write-read'] = '[open open]'
G.add_edge('lpm','charger_monitor')
G.edge['lpm']['charger_monitor']['write-read'] = '[open open][open open]'
G.add_edge('lpm','cnd')
G.edge['lpm']['cnd']['write-read'] = '[open open]'
G.add_edge('lpm','connfwexe')
G.edge['lpm']['connfwexe']['write-read'] = '[open open]'
G.add_edge('lpm','debuggerd')
G.edge['lpm']['debuggerd']['write-read'] = '[open open]'
G.add_edge('lpm','diag_uart_log')
G.edge['lpm']['diag_uart_log']['write-read'] = '[open open]'
G.add_edge('lpm','dumpstate')
G.edge['lpm']['dumpstate']['write-read'] = '[open open]'
G.add_edge('lpm','efsks')
G.edge['lpm']['efsks']['write-read'] = '[open open][write read][add_name search][open open]'
G.add_edge('lpm','geomagneticd')
G.edge['lpm']['geomagneticd']['write-read'] = '[open open]'
G.add_edge('lpm','gpsd')
G.edge['lpm']['gpsd']['write-read'] = '[open open]'
G.add_edge('lpm','init_shell')
G.edge['lpm']['init_shell']['write-read'] = '[open open][write read][add_name search][remove_name search][open open]'
G.add_edge('lpm','kiesexe')
G.edge['lpm']['kiesexe']['write-read'] = '[open open]'
G.add_edge('lpm','ks')
G.edge['lpm']['ks']['write-read'] = '[open open][write read][add_name search][open open]'
G.add_edge('lpm','lhd')
G.edge['lpm']['lhd']['write-read'] = '[open open]'
G.add_edge('lpm','lpm')
G.edge['lpm']['lpm']['write-read'] = '[open open][write read][append read][write read][open open][write read][append read][open open]'
G.add_edge('lpm','macloader')
G.edge['lpm']['macloader']['write-read'] = '[open open]'
G.add_edge('lpm','mdm_helper')
G.edge['lpm']['mdm_helper']['write-read'] = '[write read][open open]'
G.add_edge('lpm','mediaserver')
G.edge['lpm']['mediaserver']['write-read'] = '[open open]'
G.add_edge('lpm','mlexe')
G.edge['lpm']['mlexe']['write-read'] = '[open open]'
G.add_edge('lpm','mm-pp-daemon')
G.edge['lpm']['mm-pp-daemon']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('lpm','mm-qcamera-daemon')
G.edge['lpm']['mm-qcamera-daemon']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('lpm','mpdecision')
G.edge['lpm']['mpdecision']['write-read'] = '[open open]'
G.add_edge('lpm','oneseg_mw')
G.edge['lpm']['oneseg_mw']['write-read'] = '[open open]'
G.add_edge('lpm','qcks')
G.edge['lpm']['qcks']['write-read'] = '[open open]'
G.add_edge('lpm','qmuxd')
G.edge['lpm']['qmuxd']['write-read'] = '[open open]'
G.add_edge('lpm','radio')
G.edge['lpm']['radio']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('lpm','rild')
G.edge['lpm']['rild']['write-read'] = '[write read][append read][open open]'
G.add_edge('lpm','rmt_storage')
G.edge['lpm']['rmt_storage']['write-read'] = '[open open]'
G.add_edge('lpm','sec-ril')
G.edge['lpm']['sec-ril']['write-read'] = '[open open]'
G.add_edge('lpm','smdexe')
G.edge['lpm']['smdexe']['write-read'] = '[open open]'
G.add_edge('lpm','ssr_setup')
G.edge['lpm']['ssr_setup']['write-read'] = '[open open]'
G.add_edge('lpm','sswap')
G.edge['lpm']['sswap']['write-read'] = '[open open]'
G.add_edge('lpm','surfaceflinger')
G.edge['lpm']['surfaceflinger']['write-read'] = '[write read][append read][open open][write read][append read][open open]'
G.add_edge('lpm','system_server')
G.edge['lpm']['system_server']['write-read'] = '[write read][append read][open open][write read][append read][open open]'
G.add_edge('lpm','system_server')
G.edge['lpm']['system_server']['write-read'] = '[write read][append read][open open][write read][append read][open open][open open]'
G.add_edge('lpm','thermal-engine')
G.edge['lpm']['thermal-engine']['write-read'] = '[open open]'
G.add_edge('lpm','ueventd')
G.edge['lpm']['ueventd']['write-read'] = '[write read][append read][open open]'
G.add_edge('lpm','vm_bms')
G.edge['lpm']['vm_bms']['write-read'] = '[open open]'
G.add_edge('lpm','vold')
G.edge['lpm']['vold']['write-read'] = '[write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('lpm','init_shell')
G.edge['lpm']['init_shell']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('lpm','rild')
G.edge['lpm']['rild']['write-read'] = '[write read][append read][open open][setattr getattr]'
G.add_edge('lpm','rtcc')
G.edge['lpm']['rtcc']['write-read'] = '[setattr getattr]'
G.add_edge('lpm','sec-ril')
G.edge['lpm']['sec-ril']['write-read'] = '[open open][setattr getattr]'
G.add_edge('lpm','system_server')
G.edge['lpm']['system_server']['write-read'] = '[write read][append read][open open][write read][append read][open open][open open][setattr getattr]'
G.add_edge('lpm','at_distributor')
G.edge['lpm']['at_distributor']['write-read'] = '[open open][write read]'
G.edge['lpm']['at_distributor']['fill'] = 'red'
G.add_edge('lpm','at_distributor')
G.edge['lpm']['at_distributor']['write-read'] = '[open open][write read][append read]'
G.add_edge('lpm','bauthserver')
G.edge['lpm']['bauthserver']['write-read'] = '[open open][write read]'
G.edge['lpm']['bauthserver']['fill'] = 'red'
G.add_edge('lpm','bauthserver')
G.edge['lpm']['bauthserver']['write-read'] = '[open open][write read][append read]'
G.add_edge('lpm','bintvoutservice')
G.edge['lpm']['bintvoutservice']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['lpm']['bintvoutservice']['fill'] = 'red'
G.add_edge('lpm','bintvoutservice')
G.edge['lpm']['bintvoutservice']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('lpm','bluetooth')
G.edge['lpm']['bluetooth']['write-read'] = '[open open][write read]'
G.edge['lpm']['bluetooth']['fill'] = 'red'
G.add_edge('lpm','bluetooth')
G.edge['lpm']['bluetooth']['write-read'] = '[open open][write read][append read]'
G.add_edge('lpm','bootanim')
G.edge['lpm']['bootanim']['write-read'] = '[open open][write read][append read][write read]'
G.edge['lpm']['bootanim']['fill'] = 'red'
G.add_edge('lpm','cbd')
G.edge['lpm']['cbd']['write-read'] = '[open open][write read]'
G.edge['lpm']['cbd']['fill'] = 'red'
G.add_edge('lpm','cbd')
G.edge['lpm']['cbd']['write-read'] = '[open open][write read][append read]'
G.add_edge('lpm','cellgeofenced')
G.edge['lpm']['cellgeofenced']['write-read'] = '[open open][write read]'
G.edge['lpm']['cellgeofenced']['fill'] = 'red'
G.add_edge('lpm','cellgeofenced')
G.edge['lpm']['cellgeofenced']['write-read'] = '[open open][write read][append read]'
G.add_edge('lpm','charger_monitor')
G.edge['lpm']['charger_monitor']['write-read'] = '[open open][open open][write read]'
G.edge['lpm']['charger_monitor']['fill'] = 'red'
G.add_edge('lpm','charger_monitor')
G.edge['lpm']['charger_monitor']['write-read'] = '[open open][open open][write read][append read]'
G.add_edge('lpm','charger_monitor')
G.edge['lpm']['charger_monitor']['write-read'] = '[open open][open open][write read][append read][write read]'
G.edge['lpm']['charger_monitor']['fill'] = 'red'
G.add_edge('lpm','charger_monitor')
G.edge['lpm']['charger_monitor']['write-read'] = '[open open][open open][write read][append read][write read][append read]'
G.add_edge('lpm','cnd')
G.edge['lpm']['cnd']['write-read'] = '[open open][write read]'
G.edge['lpm']['cnd']['fill'] = 'red'
G.add_edge('lpm','cnd')
G.edge['lpm']['cnd']['write-read'] = '[open open][write read][append read]'
G.add_edge('lpm','connfwexe')
G.edge['lpm']['connfwexe']['write-read'] = '[open open][write read]'
G.edge['lpm']['connfwexe']['fill'] = 'red'
G.add_edge('lpm','connfwexe')
G.edge['lpm']['connfwexe']['write-read'] = '[open open][write read][append read]'
G.add_edge('lpm','debuggerd')
G.edge['lpm']['debuggerd']['write-read'] = '[open open][write read]'
G.edge['lpm']['debuggerd']['fill'] = 'red'
G.add_edge('lpm','debuggerd')
G.edge['lpm']['debuggerd']['write-read'] = '[open open][write read][append read]'
G.add_edge('lpm','diag_uart_log')
G.edge['lpm']['diag_uart_log']['write-read'] = '[open open][write read]'
G.edge['lpm']['diag_uart_log']['fill'] = 'red'
G.add_edge('lpm','diag_uart_log')
G.edge['lpm']['diag_uart_log']['write-read'] = '[open open][write read][append read]'
G.add_edge('lpm','dumpstate')
G.edge['lpm']['dumpstate']['write-read'] = '[open open][write read]'
G.edge['lpm']['dumpstate']['fill'] = 'red'
G.add_edge('lpm','dumpstate')
G.edge['lpm']['dumpstate']['write-read'] = '[open open][write read][append read]'
G.add_edge('lpm','efsks')
G.edge['lpm']['efsks']['write-read'] = '[open open][write read][add_name search][open open][write read]'
G.edge['lpm']['efsks']['fill'] = 'red'
G.add_edge('lpm','efsks')
G.edge['lpm']['efsks']['write-read'] = '[open open][write read][add_name search][open open][write read][append read]'
G.add_edge('lpm','geomagneticd')
G.edge['lpm']['geomagneticd']['write-read'] = '[open open][write read]'
G.edge['lpm']['geomagneticd']['fill'] = 'red'
G.add_edge('lpm','geomagneticd')
G.edge['lpm']['geomagneticd']['write-read'] = '[open open][write read][append read]'
G.add_edge('lpm','gpsd')
G.edge['lpm']['gpsd']['write-read'] = '[open open][write read]'
G.edge['lpm']['gpsd']['fill'] = 'red'
G.add_edge('lpm','gpsd')
G.edge['lpm']['gpsd']['write-read'] = '[open open][write read][append read]'
G.add_edge('lpm','healthd')
G.edge['lpm']['healthd']['write-read'] = '[write read][append read][open open][write read][append read][open open][write read][append read][write read]'
G.edge['lpm']['healthd']['fill'] = 'red'
G.add_edge('lpm','init_shell')
G.edge['lpm']['init_shell']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['lpm']['init_shell']['fill'] = 'red'
G.add_edge('lpm','init_shell')
G.edge['lpm']['init_shell']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('lpm','jackservice')
G.edge['lpm']['jackservice']['write-read'] = '[write read]'
G.edge['lpm']['jackservice']['fill'] = 'red'
G.add_edge('lpm','kiesexe')
G.edge['lpm']['kiesexe']['write-read'] = '[open open][write read]'
G.edge['lpm']['kiesexe']['fill'] = 'red'
G.add_edge('lpm','kiesexe')
G.edge['lpm']['kiesexe']['write-read'] = '[open open][write read][append read]'
G.add_edge('lpm','ks')
G.edge['lpm']['ks']['write-read'] = '[open open][write read][add_name search][open open][write read]'
G.edge['lpm']['ks']['fill'] = 'red'
G.add_edge('lpm','ks')
G.edge['lpm']['ks']['write-read'] = '[open open][write read][add_name search][open open][write read][append read]'
G.add_edge('lpm','lhd')
G.edge['lpm']['lhd']['write-read'] = '[open open][write read]'
G.edge['lpm']['lhd']['fill'] = 'red'
G.add_edge('lpm','lhd')
G.edge['lpm']['lhd']['write-read'] = '[open open][write read][append read]'
G.add_edge('lpm','lmkd')
G.edge['lpm']['lmkd']['write-read'] = '[write read]'
G.edge['lpm']['lmkd']['fill'] = 'red'
G.add_edge('lpm','lpm')
G.edge['lpm']['lpm']['write-read'] = '[open open][write read][append read][write read][open open][write read][append read][open open][write read]'
G.edge['lpm']['lpm']['fill'] = 'red'
G.add_edge('lpm','lpm')
G.edge['lpm']['lpm']['write-read'] = '[open open][write read][append read][write read][open open][write read][append read][open open][write read][append read]'
G.add_edge('lpm','macloader')
G.edge['lpm']['macloader']['write-read'] = '[open open][write read]'
G.edge['lpm']['macloader']['fill'] = 'red'
G.add_edge('lpm','macloader')
G.edge['lpm']['macloader']['write-read'] = '[open open][write read][append read]'
G.add_edge('lpm','mdm_helper')
G.edge['lpm']['mdm_helper']['write-read'] = '[write read][open open][write read]'
G.edge['lpm']['mdm_helper']['fill'] = 'red'
G.add_edge('lpm','mediaserver')
G.edge['lpm']['mediaserver']['write-read'] = '[open open][write read]'
G.edge['lpm']['mediaserver']['fill'] = 'red'
G.add_edge('lpm','mediaserver')
G.edge['lpm']['mediaserver']['write-read'] = '[open open][write read][append read]'
G.add_edge('lpm','mfgloader')
G.edge['lpm']['mfgloader']['write-read'] = '[write read]'
G.edge['lpm']['mfgloader']['fill'] = 'red'
G.add_edge('lpm','mlexe')
G.edge['lpm']['mlexe']['write-read'] = '[open open][write read]'
G.edge['lpm']['mlexe']['fill'] = 'red'
G.add_edge('lpm','mlexe')
G.edge['lpm']['mlexe']['write-read'] = '[open open][write read][append read]'
G.add_edge('lpm','mm-pp-daemon')
G.edge['lpm']['mm-pp-daemon']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['lpm']['mm-pp-daemon']['fill'] = 'red'
G.add_edge('lpm','mm-pp-daemon')
G.edge['lpm']['mm-pp-daemon']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('lpm','mm-pp-daemon')
G.edge['lpm']['mm-pp-daemon']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read]'
G.edge['lpm']['mm-pp-daemon']['fill'] = 'red'
G.add_edge('lpm','mm-qcamera-daemon')
G.edge['lpm']['mm-qcamera-daemon']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['lpm']['mm-qcamera-daemon']['fill'] = 'red'
G.add_edge('lpm','mm-qcamera-daemon')
G.edge['lpm']['mm-qcamera-daemon']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('lpm','mpdecision')
G.edge['lpm']['mpdecision']['write-read'] = '[open open][write read]'
G.edge['lpm']['mpdecision']['fill'] = 'red'
G.add_edge('lpm','mpdecision')
G.edge['lpm']['mpdecision']['write-read'] = '[open open][write read][append read]'
G.add_edge('lpm','mpdecision')
G.edge['lpm']['mpdecision']['write-read'] = '[open open][write read][append read][write read]'
G.edge['lpm']['mpdecision']['fill'] = 'red'
G.add_edge('lpm','netd')
G.edge['lpm']['netd']['write-read'] = '[write read][append read][write read]'
G.edge['lpm']['netd']['fill'] = 'red'
G.add_edge('lpm','netmgrd')
G.edge['lpm']['netmgrd']['write-read'] = '[write read]'
G.edge['lpm']['netmgrd']['fill'] = 'red'
G.add_edge('lpm','nfc')
G.edge['lpm']['nfc']['write-read'] = '[write read]'
G.edge['lpm']['nfc']['fill'] = 'red'
G.add_edge('lpm','oneseg_mw')
G.edge['lpm']['oneseg_mw']['write-read'] = '[open open][write read]'
G.edge['lpm']['oneseg_mw']['fill'] = 'red'
G.add_edge('lpm','oneseg_mw')
G.edge['lpm']['oneseg_mw']['write-read'] = '[open open][write read][append read]'
G.add_edge('lpm','perfd')
G.edge['lpm']['perfd']['write-read'] = '[write read]'
G.edge['lpm']['perfd']['fill'] = 'red'
G.add_edge('lpm','qcks')
G.edge['lpm']['qcks']['write-read'] = '[open open][write read]'
G.edge['lpm']['qcks']['fill'] = 'red'
G.add_edge('lpm','qcks')
G.edge['lpm']['qcks']['write-read'] = '[open open][write read][append read]'
G.add_edge('lpm','qmuxd')
G.edge['lpm']['qmuxd']['write-read'] = '[open open][write read]'
G.edge['lpm']['qmuxd']['fill'] = 'red'
G.add_edge('lpm','qmuxd')
G.edge['lpm']['qmuxd']['write-read'] = '[open open][write read][append read]'
G.add_edge('lpm','qosmgr')
G.edge['lpm']['qosmgr']['write-read'] = '[write read]'
G.edge['lpm']['qosmgr']['fill'] = 'red'
G.add_edge('lpm','radio')
G.edge['lpm']['radio']['write-read'] = '[open open][write read][append read][open open][append read]'
G.add_edge('lpm','rild')
G.edge['lpm']['rild']['write-read'] = '[write read][append read][open open][setattr getattr][write read]'
G.edge['lpm']['rild']['fill'] = 'red'
G.add_edge('lpm','rild')
G.edge['lpm']['rild']['write-read'] = '[write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('lpm','rmt_storage')
G.edge['lpm']['rmt_storage']['write-read'] = '[open open][write read]'
G.edge['lpm']['rmt_storage']['fill'] = 'red'
G.add_edge('lpm','rmt_storage')
G.edge['lpm']['rmt_storage']['write-read'] = '[open open][write read][append read]'
G.add_edge('lpm','rtcc')
G.edge['lpm']['rtcc']['write-read'] = '[setattr getattr][write read]'
G.edge['lpm']['rtcc']['fill'] = 'red'
G.add_edge('lpm','sec-ril')
G.edge['lpm']['sec-ril']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['lpm']['sec-ril']['fill'] = 'red'
G.add_edge('lpm','sec-ril')
G.edge['lpm']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('lpm','sensorhubservice')
G.edge['lpm']['sensorhubservice']['write-read'] = '[write read]'
G.edge['lpm']['sensorhubservice']['fill'] = 'red'
G.add_edge('lpm','smdexe')
G.edge['lpm']['smdexe']['write-read'] = '[open open][write read]'
G.edge['lpm']['smdexe']['fill'] = 'red'
G.add_edge('lpm','smdexe')
G.edge['lpm']['smdexe']['write-read'] = '[open open][write read][append read]'
G.add_edge('lpm','ssr_setup')
G.edge['lpm']['ssr_setup']['write-read'] = '[open open][write read]'
G.edge['lpm']['ssr_setup']['fill'] = 'red'
G.add_edge('lpm','ssr_setup')
G.edge['lpm']['ssr_setup']['write-read'] = '[open open][write read][append read]'
G.add_edge('lpm','sswap')
G.edge['lpm']['sswap']['write-read'] = '[open open][write read]'
G.edge['lpm']['sswap']['fill'] = 'red'
G.add_edge('lpm','sswap')
G.edge['lpm']['sswap']['write-read'] = '[open open][write read][append read]'
G.add_edge('lpm','surfaceflinger')
G.edge['lpm']['surfaceflinger']['write-read'] = '[write read][append read][open open][write read][append read][open open][write read]'
G.edge['lpm']['surfaceflinger']['fill'] = 'red'
G.add_edge('lpm','surfaceflinger')
G.edge['lpm']['surfaceflinger']['write-read'] = '[write read][append read][open open][write read][append read][open open][write read][append read]'
G.add_edge('lpm','surfaceflinger')
G.edge['lpm']['surfaceflinger']['write-read'] = '[write read][append read][open open][write read][append read][open open][write read][append read][write read]'
G.edge['lpm']['surfaceflinger']['fill'] = 'red'
G.add_edge('lpm','system_server')
G.edge['lpm']['system_server']['write-read'] = '[write read][append read][open open][write read][append read][open open][open open][setattr getattr][write read]'
G.edge['lpm']['system_server']['fill'] = 'red'
G.add_edge('lpm','system_server')
G.edge['lpm']['system_server']['write-read'] = '[write read][append read][open open][write read][append read][open open][open open][setattr getattr][write read][append read]'
G.add_edge('lpm','system_server')
G.edge['lpm']['system_server']['write-read'] = '[write read][append read][open open][write read][append read][open open][open open][setattr getattr][write read][append read][write read]'
G.edge['lpm']['system_server']['fill'] = 'red'
G.add_edge('lpm','system_server')
G.edge['lpm']['system_server']['write-read'] = '[write read][append read][open open][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read]'
G.add_edge('lpm','thermald')
G.edge['lpm']['thermald']['write-read'] = '[write read]'
G.edge['lpm']['thermald']['fill'] = 'red'
G.add_edge('lpm','thermal-engine')
G.edge['lpm']['thermal-engine']['write-read'] = '[open open][write read]'
G.edge['lpm']['thermal-engine']['fill'] = 'red'
G.add_edge('lpm','thermal-engine')
G.edge['lpm']['thermal-engine']['write-read'] = '[open open][write read][append read]'
G.add_edge('lpm','thermal-engine')
G.edge['lpm']['thermal-engine']['write-read'] = '[open open][write read][append read][write read]'
G.edge['lpm']['thermal-engine']['fill'] = 'red'
G.add_edge('lpm','ueventd')
G.edge['lpm']['ueventd']['write-read'] = '[write read][append read][open open][write read]'
G.edge['lpm']['ueventd']['fill'] = 'red'
G.add_edge('lpm','ueventd')
G.edge['lpm']['ueventd']['write-read'] = '[write read][append read][open open][write read][append read]'
G.add_edge('lpm','vm_bms')
G.edge['lpm']['vm_bms']['write-read'] = '[open open][write read]'
G.edge['lpm']['vm_bms']['fill'] = 'red'
G.add_edge('lpm','vm_bms')
G.edge['lpm']['vm_bms']['write-read'] = '[open open][write read][append read]'
G.add_edge('lpm','vmwared')
G.edge['lpm']['vmwared']['write-read'] = '[write read]'
G.edge['lpm']['vmwared']['fill'] = 'red'
G.add_edge('lpm','vold')
G.edge['lpm']['vold']['write-read'] = '[write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read]'
G.edge['lpm']['vold']['fill'] = 'red'
G.add_edge('lpm','vold')
G.edge['lpm']['vold']['write-read'] = '[write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read]'
G.add_edge('lpm','zygote')
G.edge['lpm']['zygote']['write-read'] = '[open open][write read][append read][write read]'
G.edge['lpm']['zygote']['fill'] = 'red'
G.add_edge('macloader','at_distributor')
G.edge['macloader']['at_distributor']['write-read'] = '[open open]'
G.add_edge('macloader','bauthserver')
G.edge['macloader']['bauthserver']['write-read'] = '[open open]'
G.add_edge('macloader','bintvoutservice')
G.edge['macloader']['bintvoutservice']['write-read'] = '[open open]'
G.add_edge('macloader','bluetooth')
G.edge['macloader']['bluetooth']['write-read'] = '[open open]'
G.add_edge('macloader','cbd')
G.edge['macloader']['cbd']['write-read'] = '[open open]'
G.add_edge('macloader','cellgeofenced')
G.edge['macloader']['cellgeofenced']['write-read'] = '[open open]'
G.add_edge('macloader','charger_monitor')
G.edge['macloader']['charger_monitor']['write-read'] = '[open open]'
G.add_edge('macloader','charger_monitor')
G.edge['macloader']['charger_monitor']['write-read'] = '[open open][open open]'
G.add_edge('macloader','cnd')
G.edge['macloader']['cnd']['write-read'] = '[open open]'
G.add_edge('macloader','connfwexe')
G.edge['macloader']['connfwexe']['write-read'] = '[open open]'
G.add_edge('macloader','debuggerd')
G.edge['macloader']['debuggerd']['write-read'] = '[open open]'
G.add_edge('macloader','diag_uart_log')
G.edge['macloader']['diag_uart_log']['write-read'] = '[open open]'
G.add_edge('macloader','dumpstate')
G.edge['macloader']['dumpstate']['write-read'] = '[open open]'
G.add_edge('macloader','efsks')
G.edge['macloader']['efsks']['write-read'] = '[open open]'
G.add_edge('macloader','geomagneticd')
G.edge['macloader']['geomagneticd']['write-read'] = '[open open]'
G.add_edge('macloader','gpsd')
G.edge['macloader']['gpsd']['write-read'] = '[open open]'
G.add_edge('macloader','init_shell')
G.edge['macloader']['init_shell']['write-read'] = '[open open]'
G.add_edge('macloader','kiesexe')
G.edge['macloader']['kiesexe']['write-read'] = '[open open]'
G.add_edge('macloader','ks')
G.edge['macloader']['ks']['write-read'] = '[open open]'
G.add_edge('macloader','lhd')
G.edge['macloader']['lhd']['write-read'] = '[open open]'
G.add_edge('macloader','lpm')
G.edge['macloader']['lpm']['write-read'] = '[open open]'
G.add_edge('macloader','macloader')
G.edge['macloader']['macloader']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('macloader','mdm_helper')
G.edge['macloader']['mdm_helper']['write-read'] = '[open open]'
G.add_edge('macloader','mediaserver')
G.edge['macloader']['mediaserver']['write-read'] = '[open open]'
G.add_edge('macloader','mlexe')
G.edge['macloader']['mlexe']['write-read'] = '[open open]'
G.add_edge('macloader','mm-pp-daemon')
G.edge['macloader']['mm-pp-daemon']['write-read'] = '[open open]'
G.add_edge('macloader','mm-qcamera-daemon')
G.edge['macloader']['mm-qcamera-daemon']['write-read'] = '[open open]'
G.add_edge('macloader','mpdecision')
G.edge['macloader']['mpdecision']['write-read'] = '[open open]'
G.add_edge('macloader','oneseg_mw')
G.edge['macloader']['oneseg_mw']['write-read'] = '[open open]'
G.add_edge('macloader','qcks')
G.edge['macloader']['qcks']['write-read'] = '[open open]'
G.add_edge('macloader','qmuxd')
G.edge['macloader']['qmuxd']['write-read'] = '[open open]'
G.add_edge('macloader','radio')
G.edge['macloader']['radio']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('macloader','rild')
G.edge['macloader']['rild']['write-read'] = '[open open]'
G.add_edge('macloader','rmt_storage')
G.edge['macloader']['rmt_storage']['write-read'] = '[open open]'
G.add_edge('macloader','sec-ril')
G.edge['macloader']['sec-ril']['write-read'] = '[open open]'
G.add_edge('macloader','smdexe')
G.edge['macloader']['smdexe']['write-read'] = '[open open]'
G.add_edge('macloader','ssr_setup')
G.edge['macloader']['ssr_setup']['write-read'] = '[open open]'
G.add_edge('macloader','sswap')
G.edge['macloader']['sswap']['write-read'] = '[open open]'
G.add_edge('macloader','surfaceflinger')
G.edge['macloader']['surfaceflinger']['write-read'] = '[open open]'
G.add_edge('macloader','system_server')
G.edge['macloader']['system_server']['write-read'] = '[open open]'
G.add_edge('macloader','system_server')
G.edge['macloader']['system_server']['write-read'] = '[open open][open open]'
G.add_edge('macloader','thermal-engine')
G.edge['macloader']['thermal-engine']['write-read'] = '[open open]'
G.add_edge('macloader','ueventd')
G.edge['macloader']['ueventd']['write-read'] = '[open open]'
G.add_edge('macloader','vm_bms')
G.edge['macloader']['vm_bms']['write-read'] = '[open open]'
G.add_edge('macloader','vold')
G.edge['macloader']['vold']['write-read'] = '[open open]'
G.add_edge('macloader','init_shell')
G.edge['macloader']['init_shell']['write-read'] = '[open open][setattr getattr]'
G.add_edge('macloader','rild')
G.edge['macloader']['rild']['write-read'] = '[open open][setattr getattr]'
G.add_edge('macloader','rtcc')
G.edge['macloader']['rtcc']['write-read'] = '[setattr getattr]'
G.add_edge('macloader','sec-ril')
G.edge['macloader']['sec-ril']['write-read'] = '[open open][setattr getattr]'
G.add_edge('macloader','system_server')
G.edge['macloader']['system_server']['write-read'] = '[open open][open open][setattr getattr]'
G.add_edge('macloader','at_distributor')
G.edge['macloader']['at_distributor']['write-read'] = '[open open][write read]'
G.edge['macloader']['at_distributor']['fill'] = 'red'
G.add_edge('macloader','at_distributor')
G.edge['macloader']['at_distributor']['write-read'] = '[open open][write read][append read]'
G.add_edge('macloader','bauthserver')
G.edge['macloader']['bauthserver']['write-read'] = '[open open][write read]'
G.edge['macloader']['bauthserver']['fill'] = 'red'
G.add_edge('macloader','bauthserver')
G.edge['macloader']['bauthserver']['write-read'] = '[open open][write read][append read]'
G.add_edge('macloader','bintvoutservice')
G.edge['macloader']['bintvoutservice']['write-read'] = '[open open][write read]'
G.edge['macloader']['bintvoutservice']['fill'] = 'red'
G.add_edge('macloader','bintvoutservice')
G.edge['macloader']['bintvoutservice']['write-read'] = '[open open][write read][append read]'
G.add_edge('macloader','bluetooth')
G.edge['macloader']['bluetooth']['write-read'] = '[open open][write read]'
G.edge['macloader']['bluetooth']['fill'] = 'red'
G.add_edge('macloader','bluetooth')
G.edge['macloader']['bluetooth']['write-read'] = '[open open][write read][append read]'
G.add_edge('macloader','bootanim')
G.edge['macloader']['bootanim']['write-read'] = '[write read]'
G.edge['macloader']['bootanim']['fill'] = 'red'
G.add_edge('macloader','cbd')
G.edge['macloader']['cbd']['write-read'] = '[open open][write read]'
G.edge['macloader']['cbd']['fill'] = 'red'
G.add_edge('macloader','cbd')
G.edge['macloader']['cbd']['write-read'] = '[open open][write read][append read]'
G.add_edge('macloader','cellgeofenced')
G.edge['macloader']['cellgeofenced']['write-read'] = '[open open][write read]'
G.edge['macloader']['cellgeofenced']['fill'] = 'red'
G.add_edge('macloader','cellgeofenced')
G.edge['macloader']['cellgeofenced']['write-read'] = '[open open][write read][append read]'
G.add_edge('macloader','charger_monitor')
G.edge['macloader']['charger_monitor']['write-read'] = '[open open][open open][write read]'
G.edge['macloader']['charger_monitor']['fill'] = 'red'
G.add_edge('macloader','charger_monitor')
G.edge['macloader']['charger_monitor']['write-read'] = '[open open][open open][write read][append read]'
G.add_edge('macloader','charger_monitor')
G.edge['macloader']['charger_monitor']['write-read'] = '[open open][open open][write read][append read][write read]'
G.edge['macloader']['charger_monitor']['fill'] = 'red'
G.add_edge('macloader','charger_monitor')
G.edge['macloader']['charger_monitor']['write-read'] = '[open open][open open][write read][append read][write read][append read]'
G.add_edge('macloader','cnd')
G.edge['macloader']['cnd']['write-read'] = '[open open][write read]'
G.edge['macloader']['cnd']['fill'] = 'red'
G.add_edge('macloader','cnd')
G.edge['macloader']['cnd']['write-read'] = '[open open][write read][append read]'
G.add_edge('macloader','connfwexe')
G.edge['macloader']['connfwexe']['write-read'] = '[open open][write read]'
G.edge['macloader']['connfwexe']['fill'] = 'red'
G.add_edge('macloader','connfwexe')
G.edge['macloader']['connfwexe']['write-read'] = '[open open][write read][append read]'
G.add_edge('macloader','debuggerd')
G.edge['macloader']['debuggerd']['write-read'] = '[open open][write read]'
G.edge['macloader']['debuggerd']['fill'] = 'red'
G.add_edge('macloader','debuggerd')
G.edge['macloader']['debuggerd']['write-read'] = '[open open][write read][append read]'
G.add_edge('macloader','diag_uart_log')
G.edge['macloader']['diag_uart_log']['write-read'] = '[open open][write read]'
G.edge['macloader']['diag_uart_log']['fill'] = 'red'
G.add_edge('macloader','diag_uart_log')
G.edge['macloader']['diag_uart_log']['write-read'] = '[open open][write read][append read]'
G.add_edge('macloader','dumpstate')
G.edge['macloader']['dumpstate']['write-read'] = '[open open][write read]'
G.edge['macloader']['dumpstate']['fill'] = 'red'
G.add_edge('macloader','dumpstate')
G.edge['macloader']['dumpstate']['write-read'] = '[open open][write read][append read]'
G.add_edge('macloader','efsks')
G.edge['macloader']['efsks']['write-read'] = '[open open][write read]'
G.edge['macloader']['efsks']['fill'] = 'red'
G.add_edge('macloader','efsks')
G.edge['macloader']['efsks']['write-read'] = '[open open][write read][append read]'
G.add_edge('macloader','geomagneticd')
G.edge['macloader']['geomagneticd']['write-read'] = '[open open][write read]'
G.edge['macloader']['geomagneticd']['fill'] = 'red'
G.add_edge('macloader','geomagneticd')
G.edge['macloader']['geomagneticd']['write-read'] = '[open open][write read][append read]'
G.add_edge('macloader','gpsd')
G.edge['macloader']['gpsd']['write-read'] = '[open open][write read]'
G.edge['macloader']['gpsd']['fill'] = 'red'
G.add_edge('macloader','gpsd')
G.edge['macloader']['gpsd']['write-read'] = '[open open][write read][append read]'
G.add_edge('macloader','healthd')
G.edge['macloader']['healthd']['write-read'] = '[write read]'
G.edge['macloader']['healthd']['fill'] = 'red'
G.add_edge('macloader','init_shell')
G.edge['macloader']['init_shell']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['macloader']['init_shell']['fill'] = 'red'
G.add_edge('macloader','init_shell')
G.edge['macloader']['init_shell']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('macloader','jackservice')
G.edge['macloader']['jackservice']['write-read'] = '[write read]'
G.edge['macloader']['jackservice']['fill'] = 'red'
G.add_edge('macloader','kiesexe')
G.edge['macloader']['kiesexe']['write-read'] = '[open open][write read]'
G.edge['macloader']['kiesexe']['fill'] = 'red'
G.add_edge('macloader','kiesexe')
G.edge['macloader']['kiesexe']['write-read'] = '[open open][write read][append read]'
G.add_edge('macloader','ks')
G.edge['macloader']['ks']['write-read'] = '[open open][write read]'
G.edge['macloader']['ks']['fill'] = 'red'
G.add_edge('macloader','ks')
G.edge['macloader']['ks']['write-read'] = '[open open][write read][append read]'
G.add_edge('macloader','lhd')
G.edge['macloader']['lhd']['write-read'] = '[open open][write read]'
G.edge['macloader']['lhd']['fill'] = 'red'
G.add_edge('macloader','lhd')
G.edge['macloader']['lhd']['write-read'] = '[open open][write read][append read]'
G.add_edge('macloader','lmkd')
G.edge['macloader']['lmkd']['write-read'] = '[write read]'
G.edge['macloader']['lmkd']['fill'] = 'red'
G.add_edge('macloader','lpm')
G.edge['macloader']['lpm']['write-read'] = '[open open][write read]'
G.edge['macloader']['lpm']['fill'] = 'red'
G.add_edge('macloader','lpm')
G.edge['macloader']['lpm']['write-read'] = '[open open][write read][append read]'
G.add_edge('macloader','macloader')
G.edge['macloader']['macloader']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['macloader']['macloader']['fill'] = 'red'
G.add_edge('macloader','macloader')
G.edge['macloader']['macloader']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('macloader','mdm_helper')
G.edge['macloader']['mdm_helper']['write-read'] = '[open open][write read]'
G.edge['macloader']['mdm_helper']['fill'] = 'red'
G.add_edge('macloader','mediaserver')
G.edge['macloader']['mediaserver']['write-read'] = '[open open][write read]'
G.edge['macloader']['mediaserver']['fill'] = 'red'
G.add_edge('macloader','mediaserver')
G.edge['macloader']['mediaserver']['write-read'] = '[open open][write read][append read]'
G.add_edge('macloader','mfgloader')
G.edge['macloader']['mfgloader']['write-read'] = '[open open][setattr getattr][write read][append read][write read]'
G.edge['macloader']['mfgloader']['fill'] = 'red'
G.add_edge('macloader','mlexe')
G.edge['macloader']['mlexe']['write-read'] = '[open open][write read]'
G.edge['macloader']['mlexe']['fill'] = 'red'
G.add_edge('macloader','mlexe')
G.edge['macloader']['mlexe']['write-read'] = '[open open][write read][append read]'
G.add_edge('macloader','mm-pp-daemon')
G.edge['macloader']['mm-pp-daemon']['write-read'] = '[open open][write read]'
G.edge['macloader']['mm-pp-daemon']['fill'] = 'red'
G.add_edge('macloader','mm-pp-daemon')
G.edge['macloader']['mm-pp-daemon']['write-read'] = '[open open][write read][append read]'
G.add_edge('macloader','mm-pp-daemon')
G.edge['macloader']['mm-pp-daemon']['write-read'] = '[open open][write read][append read][write read]'
G.edge['macloader']['mm-pp-daemon']['fill'] = 'red'
G.add_edge('macloader','mm-qcamera-daemon')
G.edge['macloader']['mm-qcamera-daemon']['write-read'] = '[open open][write read]'
G.edge['macloader']['mm-qcamera-daemon']['fill'] = 'red'
G.add_edge('macloader','mm-qcamera-daemon')
G.edge['macloader']['mm-qcamera-daemon']['write-read'] = '[open open][write read][append read]'
G.add_edge('macloader','mpdecision')
G.edge['macloader']['mpdecision']['write-read'] = '[open open][write read]'
G.edge['macloader']['mpdecision']['fill'] = 'red'
G.add_edge('macloader','mpdecision')
G.edge['macloader']['mpdecision']['write-read'] = '[open open][write read][append read]'
G.add_edge('macloader','mpdecision')
G.edge['macloader']['mpdecision']['write-read'] = '[open open][write read][append read][write read]'
G.edge['macloader']['mpdecision']['fill'] = 'red'
G.add_edge('macloader','netd')
G.edge['macloader']['netd']['write-read'] = '[write read]'
G.edge['macloader']['netd']['fill'] = 'red'
G.add_edge('macloader','netmgrd')
G.edge['macloader']['netmgrd']['write-read'] = '[write read]'
G.edge['macloader']['netmgrd']['fill'] = 'red'
G.add_edge('macloader','nfc')
G.edge['macloader']['nfc']['write-read'] = '[write read]'
G.edge['macloader']['nfc']['fill'] = 'red'
G.add_edge('macloader','oneseg_mw')
G.edge['macloader']['oneseg_mw']['write-read'] = '[open open][write read]'
G.edge['macloader']['oneseg_mw']['fill'] = 'red'
G.add_edge('macloader','oneseg_mw')
G.edge['macloader']['oneseg_mw']['write-read'] = '[open open][write read][append read]'
G.add_edge('macloader','perfd')
G.edge['macloader']['perfd']['write-read'] = '[write read]'
G.edge['macloader']['perfd']['fill'] = 'red'
G.add_edge('macloader','qcks')
G.edge['macloader']['qcks']['write-read'] = '[open open][write read]'
G.edge['macloader']['qcks']['fill'] = 'red'
G.add_edge('macloader','qcks')
G.edge['macloader']['qcks']['write-read'] = '[open open][write read][append read]'
G.add_edge('macloader','qmuxd')
G.edge['macloader']['qmuxd']['write-read'] = '[open open][write read]'
G.edge['macloader']['qmuxd']['fill'] = 'red'
G.add_edge('macloader','qmuxd')
G.edge['macloader']['qmuxd']['write-read'] = '[open open][write read][append read]'
G.add_edge('macloader','qosmgr')
G.edge['macloader']['qosmgr']['write-read'] = '[write read]'
G.edge['macloader']['qosmgr']['fill'] = 'red'
G.add_edge('macloader','radio')
G.edge['macloader']['radio']['write-read'] = '[open open][setattr getattr][write read][append read][open open][append read]'
G.add_edge('macloader','rild')
G.edge['macloader']['rild']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['macloader']['rild']['fill'] = 'red'
G.add_edge('macloader','rild')
G.edge['macloader']['rild']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('macloader','rmt_storage')
G.edge['macloader']['rmt_storage']['write-read'] = '[open open][write read]'
G.edge['macloader']['rmt_storage']['fill'] = 'red'
G.add_edge('macloader','rmt_storage')
G.edge['macloader']['rmt_storage']['write-read'] = '[open open][write read][append read]'
G.add_edge('macloader','rtcc')
G.edge['macloader']['rtcc']['write-read'] = '[setattr getattr][write read]'
G.edge['macloader']['rtcc']['fill'] = 'red'
G.add_edge('macloader','sec-ril')
G.edge['macloader']['sec-ril']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['macloader']['sec-ril']['fill'] = 'red'
G.add_edge('macloader','sec-ril')
G.edge['macloader']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('macloader','sensorhubservice')
G.edge['macloader']['sensorhubservice']['write-read'] = '[write read]'
G.edge['macloader']['sensorhubservice']['fill'] = 'red'
G.add_edge('macloader','smdexe')
G.edge['macloader']['smdexe']['write-read'] = '[open open][write read]'
G.edge['macloader']['smdexe']['fill'] = 'red'
G.add_edge('macloader','smdexe')
G.edge['macloader']['smdexe']['write-read'] = '[open open][write read][append read]'
G.add_edge('macloader','ssr_setup')
G.edge['macloader']['ssr_setup']['write-read'] = '[open open][write read]'
G.edge['macloader']['ssr_setup']['fill'] = 'red'
G.add_edge('macloader','ssr_setup')
G.edge['macloader']['ssr_setup']['write-read'] = '[open open][write read][append read]'
G.add_edge('macloader','sswap')
G.edge['macloader']['sswap']['write-read'] = '[open open][write read]'
G.edge['macloader']['sswap']['fill'] = 'red'
G.add_edge('macloader','sswap')
G.edge['macloader']['sswap']['write-read'] = '[open open][write read][append read]'
G.add_edge('macloader','surfaceflinger')
G.edge['macloader']['surfaceflinger']['write-read'] = '[open open][write read]'
G.edge['macloader']['surfaceflinger']['fill'] = 'red'
G.add_edge('macloader','surfaceflinger')
G.edge['macloader']['surfaceflinger']['write-read'] = '[open open][write read][append read]'
G.add_edge('macloader','surfaceflinger')
G.edge['macloader']['surfaceflinger']['write-read'] = '[open open][write read][append read][write read]'
G.edge['macloader']['surfaceflinger']['fill'] = 'red'
G.add_edge('macloader','system_server')
G.edge['macloader']['system_server']['write-read'] = '[open open][open open][setattr getattr][write read]'
G.edge['macloader']['system_server']['fill'] = 'red'
G.add_edge('macloader','system_server')
G.edge['macloader']['system_server']['write-read'] = '[open open][open open][setattr getattr][write read][append read]'
G.add_edge('macloader','system_server')
G.edge['macloader']['system_server']['write-read'] = '[open open][open open][setattr getattr][write read][append read][write read]'
G.edge['macloader']['system_server']['fill'] = 'red'
G.add_edge('macloader','system_server')
G.edge['macloader']['system_server']['write-read'] = '[open open][open open][setattr getattr][write read][append read][write read][append read]'
G.add_edge('macloader','thermald')
G.edge['macloader']['thermald']['write-read'] = '[write read]'
G.edge['macloader']['thermald']['fill'] = 'red'
G.add_edge('macloader','thermal-engine')
G.edge['macloader']['thermal-engine']['write-read'] = '[open open][write read]'
G.edge['macloader']['thermal-engine']['fill'] = 'red'
G.add_edge('macloader','thermal-engine')
G.edge['macloader']['thermal-engine']['write-read'] = '[open open][write read][append read]'
G.add_edge('macloader','thermal-engine')
G.edge['macloader']['thermal-engine']['write-read'] = '[open open][write read][append read][write read]'
G.edge['macloader']['thermal-engine']['fill'] = 'red'
G.add_edge('macloader','ueventd')
G.edge['macloader']['ueventd']['write-read'] = '[open open][write read]'
G.edge['macloader']['ueventd']['fill'] = 'red'
G.add_edge('macloader','ueventd')
G.edge['macloader']['ueventd']['write-read'] = '[open open][write read][append read]'
G.add_edge('macloader','vm_bms')
G.edge['macloader']['vm_bms']['write-read'] = '[open open][write read]'
G.edge['macloader']['vm_bms']['fill'] = 'red'
G.add_edge('macloader','vm_bms')
G.edge['macloader']['vm_bms']['write-read'] = '[open open][write read][append read]'
G.add_edge('macloader','vmwared')
G.edge['macloader']['vmwared']['write-read'] = '[write read]'
G.edge['macloader']['vmwared']['fill'] = 'red'
G.add_edge('macloader','vold')
G.edge['macloader']['vold']['write-read'] = '[open open][write read]'
G.edge['macloader']['vold']['fill'] = 'red'
G.add_edge('macloader','vold')
G.edge['macloader']['vold']['write-read'] = '[open open][write read][append read]'
G.add_edge('macloader','zygote')
G.edge['macloader']['zygote']['write-read'] = '[write read]'
G.edge['macloader']['zygote']['fill'] = 'red'
G.add_edge('mdm_helper','at_distributor')
G.edge['mdm_helper']['at_distributor']['write-read'] = '[open open]'
G.add_edge('mdm_helper','bauthserver')
G.edge['mdm_helper']['bauthserver']['write-read'] = '[open open]'
G.add_edge('mdm_helper','bintvoutservice')
G.edge['mdm_helper']['bintvoutservice']['write-read'] = '[open open]'
G.add_edge('mdm_helper','bluetooth')
G.edge['mdm_helper']['bluetooth']['write-read'] = '[open open]'
G.add_edge('mdm_helper','cbd')
G.edge['mdm_helper']['cbd']['write-read'] = '[open open]'
G.add_edge('mdm_helper','cellgeofenced')
G.edge['mdm_helper']['cellgeofenced']['write-read'] = '[open open]'
G.add_edge('mdm_helper','charger_monitor')
G.edge['mdm_helper']['charger_monitor']['write-read'] = '[open open]'
G.add_edge('mdm_helper','charger_monitor')
G.edge['mdm_helper']['charger_monitor']['write-read'] = '[open open][open open]'
G.add_edge('mdm_helper','cnd')
G.edge['mdm_helper']['cnd']['write-read'] = '[open open]'
G.add_edge('mdm_helper','connfwexe')
G.edge['mdm_helper']['connfwexe']['write-read'] = '[open open]'
G.add_edge('mdm_helper','debuggerd')
G.edge['mdm_helper']['debuggerd']['write-read'] = '[open open]'
G.add_edge('mdm_helper','diag_uart_log')
G.edge['mdm_helper']['diag_uart_log']['write-read'] = '[open open]'
G.add_edge('mdm_helper','dumpstate')
G.edge['mdm_helper']['dumpstate']['write-read'] = '[open open]'
G.add_edge('mdm_helper','efsks')
G.edge['mdm_helper']['efsks']['write-read'] = '[add_name search][open open]'
G.add_edge('mdm_helper','geomagneticd')
G.edge['mdm_helper']['geomagneticd']['write-read'] = '[open open]'
G.add_edge('mdm_helper','gpsd')
G.edge['mdm_helper']['gpsd']['write-read'] = '[open open]'
G.add_edge('mdm_helper','init_shell')
G.edge['mdm_helper']['init_shell']['write-read'] = '[add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('mdm_helper','kiesexe')
G.edge['mdm_helper']['kiesexe']['write-read'] = '[open open]'
G.add_edge('mdm_helper','ks')
G.edge['mdm_helper']['ks']['write-read'] = '[add_name search][open open]'
G.add_edge('mdm_helper','lhd')
G.edge['mdm_helper']['lhd']['write-read'] = '[open open]'
G.add_edge('mdm_helper','lpm')
G.edge['mdm_helper']['lpm']['write-read'] = '[open open]'
G.add_edge('mdm_helper','macloader')
G.edge['mdm_helper']['macloader']['write-read'] = '[open open]'
G.add_edge('mdm_helper','mdm_helper')
G.edge['mdm_helper']['mdm_helper']['write-read'] = '[open open][setattr getattr][write read][append read][write read][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('mdm_helper','mediaserver')
G.edge['mdm_helper']['mediaserver']['write-read'] = '[write read][open open]'
G.add_edge('mdm_helper','mlexe')
G.edge['mdm_helper']['mlexe']['write-read'] = '[open open]'
G.add_edge('mdm_helper','mm-pp-daemon')
G.edge['mdm_helper']['mm-pp-daemon']['write-read'] = '[open open]'
G.add_edge('mdm_helper','mm-qcamera-daemon')
G.edge['mdm_helper']['mm-qcamera-daemon']['write-read'] = '[open open]'
G.add_edge('mdm_helper','mpdecision')
G.edge['mdm_helper']['mpdecision']['write-read'] = '[open open]'
G.add_edge('mdm_helper','oneseg_mw')
G.edge['mdm_helper']['oneseg_mw']['write-read'] = '[open open]'
G.add_edge('mdm_helper','qcks')
G.edge['mdm_helper']['qcks']['write-read'] = '[open open]'
G.add_edge('mdm_helper','qmuxd')
G.edge['mdm_helper']['qmuxd']['write-read'] = '[open open]'
G.add_edge('mdm_helper','radio')
G.edge['mdm_helper']['radio']['write-read'] = '[open open]'
G.add_edge('mdm_helper','rild')
G.edge['mdm_helper']['rild']['write-read'] = '[open open]'
G.add_edge('mdm_helper','rmt_storage')
G.edge['mdm_helper']['rmt_storage']['write-read'] = '[open open]'
G.add_edge('mdm_helper','sec-ril')
G.edge['mdm_helper']['sec-ril']['write-read'] = '[open open]'
G.add_edge('mdm_helper','smdexe')
G.edge['mdm_helper']['smdexe']['write-read'] = '[open open]'
G.add_edge('mdm_helper','ssr_setup')
G.edge['mdm_helper']['ssr_setup']['write-read'] = '[open open]'
G.add_edge('mdm_helper','sswap')
G.edge['mdm_helper']['sswap']['write-read'] = '[open open]'
G.add_edge('mdm_helper','surfaceflinger')
G.edge['mdm_helper']['surfaceflinger']['write-read'] = '[open open]'
G.add_edge('mdm_helper','system_server')
G.edge['mdm_helper']['system_server']['write-read'] = '[open open]'
G.add_edge('mdm_helper','system_server')
G.edge['mdm_helper']['system_server']['write-read'] = '[open open][open open]'
G.add_edge('mdm_helper','thermal-engine')
G.edge['mdm_helper']['thermal-engine']['write-read'] = '[open open]'
G.add_edge('mdm_helper','ueventd')
G.edge['mdm_helper']['ueventd']['write-read'] = '[open open]'
G.add_edge('mdm_helper','vm_bms')
G.edge['mdm_helper']['vm_bms']['write-read'] = '[open open]'
G.add_edge('mdm_helper','vold')
G.edge['mdm_helper']['vold']['write-read'] = '[setattr getattr][add_name search][remove_name search][open open]'
G.add_edge('mdm_helper','init_shell')
G.edge['mdm_helper']['init_shell']['write-read'] = '[add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('mdm_helper','rild')
G.edge['mdm_helper']['rild']['write-read'] = '[open open][setattr getattr]'
G.add_edge('mdm_helper','rtcc')
G.edge['mdm_helper']['rtcc']['write-read'] = '[setattr getattr]'
G.add_edge('mdm_helper','sec-ril')
G.edge['mdm_helper']['sec-ril']['write-read'] = '[open open][setattr getattr]'
G.add_edge('mdm_helper','system_server')
G.edge['mdm_helper']['system_server']['write-read'] = '[open open][open open][setattr getattr]'
G.add_edge('mdm_helper','at_distributor')
G.edge['mdm_helper']['at_distributor']['write-read'] = '[open open][write read]'
G.edge['mdm_helper']['at_distributor']['fill'] = 'red'
G.add_edge('mdm_helper','at_distributor')
G.edge['mdm_helper']['at_distributor']['write-read'] = '[open open][write read][append read]'
G.add_edge('mdm_helper','bauthserver')
G.edge['mdm_helper']['bauthserver']['write-read'] = '[open open][write read]'
G.edge['mdm_helper']['bauthserver']['fill'] = 'red'
G.add_edge('mdm_helper','bauthserver')
G.edge['mdm_helper']['bauthserver']['write-read'] = '[open open][write read][append read]'
G.add_edge('mdm_helper','bintvoutservice')
G.edge['mdm_helper']['bintvoutservice']['write-read'] = '[open open][write read]'
G.edge['mdm_helper']['bintvoutservice']['fill'] = 'red'
G.add_edge('mdm_helper','bintvoutservice')
G.edge['mdm_helper']['bintvoutservice']['write-read'] = '[open open][write read][append read]'
G.add_edge('mdm_helper','bluetooth')
G.edge['mdm_helper']['bluetooth']['write-read'] = '[open open][write read]'
G.edge['mdm_helper']['bluetooth']['fill'] = 'red'
G.add_edge('mdm_helper','bluetooth')
G.edge['mdm_helper']['bluetooth']['write-read'] = '[open open][write read][append read]'
G.add_edge('mdm_helper','bootanim')
G.edge['mdm_helper']['bootanim']['write-read'] = '[write read]'
G.edge['mdm_helper']['bootanim']['fill'] = 'red'
G.add_edge('mdm_helper','cbd')
G.edge['mdm_helper']['cbd']['write-read'] = '[open open][write read]'
G.edge['mdm_helper']['cbd']['fill'] = 'red'
G.add_edge('mdm_helper','cbd')
G.edge['mdm_helper']['cbd']['write-read'] = '[open open][write read][append read]'
G.add_edge('mdm_helper','cellgeofenced')
G.edge['mdm_helper']['cellgeofenced']['write-read'] = '[open open][write read]'
G.edge['mdm_helper']['cellgeofenced']['fill'] = 'red'
G.add_edge('mdm_helper','cellgeofenced')
G.edge['mdm_helper']['cellgeofenced']['write-read'] = '[open open][write read][append read]'
G.add_edge('mdm_helper','charger_monitor')
G.edge['mdm_helper']['charger_monitor']['write-read'] = '[open open][open open][write read]'
G.edge['mdm_helper']['charger_monitor']['fill'] = 'red'
G.add_edge('mdm_helper','charger_monitor')
G.edge['mdm_helper']['charger_monitor']['write-read'] = '[open open][open open][write read][append read]'
G.add_edge('mdm_helper','charger_monitor')
G.edge['mdm_helper']['charger_monitor']['write-read'] = '[open open][open open][write read][append read][write read]'
G.edge['mdm_helper']['charger_monitor']['fill'] = 'red'
G.add_edge('mdm_helper','charger_monitor')
G.edge['mdm_helper']['charger_monitor']['write-read'] = '[open open][open open][write read][append read][write read][append read]'
G.add_edge('mdm_helper','cnd')
G.edge['mdm_helper']['cnd']['write-read'] = '[open open][write read]'
G.edge['mdm_helper']['cnd']['fill'] = 'red'
G.add_edge('mdm_helper','cnd')
G.edge['mdm_helper']['cnd']['write-read'] = '[open open][write read][append read]'
G.add_edge('mdm_helper','connfwexe')
G.edge['mdm_helper']['connfwexe']['write-read'] = '[open open][write read]'
G.edge['mdm_helper']['connfwexe']['fill'] = 'red'
G.add_edge('mdm_helper','connfwexe')
G.edge['mdm_helper']['connfwexe']['write-read'] = '[open open][write read][append read]'
G.add_edge('mdm_helper','debuggerd')
G.edge['mdm_helper']['debuggerd']['write-read'] = '[open open][write read]'
G.edge['mdm_helper']['debuggerd']['fill'] = 'red'
G.add_edge('mdm_helper','debuggerd')
G.edge['mdm_helper']['debuggerd']['write-read'] = '[open open][write read][append read]'
G.add_edge('mdm_helper','diag_uart_log')
G.edge['mdm_helper']['diag_uart_log']['write-read'] = '[open open][write read]'
G.edge['mdm_helper']['diag_uart_log']['fill'] = 'red'
G.add_edge('mdm_helper','diag_uart_log')
G.edge['mdm_helper']['diag_uart_log']['write-read'] = '[open open][write read][append read]'
G.add_edge('mdm_helper','dumpstate')
G.edge['mdm_helper']['dumpstate']['write-read'] = '[open open][write read]'
G.edge['mdm_helper']['dumpstate']['fill'] = 'red'
G.add_edge('mdm_helper','dumpstate')
G.edge['mdm_helper']['dumpstate']['write-read'] = '[open open][write read][append read]'
G.add_edge('mdm_helper','efsks')
G.edge['mdm_helper']['efsks']['write-read'] = '[add_name search][open open][write read]'
G.edge['mdm_helper']['efsks']['fill'] = 'red'
G.add_edge('mdm_helper','efsks')
G.edge['mdm_helper']['efsks']['write-read'] = '[add_name search][open open][write read][append read]'
G.add_edge('mdm_helper','geomagneticd')
G.edge['mdm_helper']['geomagneticd']['write-read'] = '[open open][write read]'
G.edge['mdm_helper']['geomagneticd']['fill'] = 'red'
G.add_edge('mdm_helper','geomagneticd')
G.edge['mdm_helper']['geomagneticd']['write-read'] = '[open open][write read][append read]'
G.add_edge('mdm_helper','gpsd')
G.edge['mdm_helper']['gpsd']['write-read'] = '[open open][write read]'
G.edge['mdm_helper']['gpsd']['fill'] = 'red'
G.add_edge('mdm_helper','gpsd')
G.edge['mdm_helper']['gpsd']['write-read'] = '[open open][write read][append read]'
G.add_edge('mdm_helper','healthd')
G.edge['mdm_helper']['healthd']['write-read'] = '[write read]'
G.edge['mdm_helper']['healthd']['fill'] = 'red'
G.add_edge('mdm_helper','init_shell')
G.edge['mdm_helper']['init_shell']['write-read'] = '[add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['mdm_helper']['init_shell']['fill'] = 'red'
G.add_edge('mdm_helper','init_shell')
G.edge['mdm_helper']['init_shell']['write-read'] = '[add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('mdm_helper','jackservice')
G.edge['mdm_helper']['jackservice']['write-read'] = '[write read]'
G.edge['mdm_helper']['jackservice']['fill'] = 'red'
G.add_edge('mdm_helper','kiesexe')
G.edge['mdm_helper']['kiesexe']['write-read'] = '[open open][write read]'
G.edge['mdm_helper']['kiesexe']['fill'] = 'red'
G.add_edge('mdm_helper','kiesexe')
G.edge['mdm_helper']['kiesexe']['write-read'] = '[open open][write read][append read]'
G.add_edge('mdm_helper','ks')
G.edge['mdm_helper']['ks']['write-read'] = '[add_name search][open open][write read]'
G.edge['mdm_helper']['ks']['fill'] = 'red'
G.add_edge('mdm_helper','ks')
G.edge['mdm_helper']['ks']['write-read'] = '[add_name search][open open][write read][append read]'
G.add_edge('mdm_helper','lhd')
G.edge['mdm_helper']['lhd']['write-read'] = '[open open][write read]'
G.edge['mdm_helper']['lhd']['fill'] = 'red'
G.add_edge('mdm_helper','lhd')
G.edge['mdm_helper']['lhd']['write-read'] = '[open open][write read][append read]'
G.add_edge('mdm_helper','lmkd')
G.edge['mdm_helper']['lmkd']['write-read'] = '[write read]'
G.edge['mdm_helper']['lmkd']['fill'] = 'red'
G.add_edge('mdm_helper','lpm')
G.edge['mdm_helper']['lpm']['write-read'] = '[open open][write read]'
G.edge['mdm_helper']['lpm']['fill'] = 'red'
G.add_edge('mdm_helper','lpm')
G.edge['mdm_helper']['lpm']['write-read'] = '[open open][write read][append read]'
G.add_edge('mdm_helper','macloader')
G.edge['mdm_helper']['macloader']['write-read'] = '[open open][write read]'
G.edge['mdm_helper']['macloader']['fill'] = 'red'
G.add_edge('mdm_helper','macloader')
G.edge['mdm_helper']['macloader']['write-read'] = '[open open][write read][append read]'
G.add_edge('mdm_helper','mdm_helper')
G.edge['mdm_helper']['mdm_helper']['write-read'] = '[open open][setattr getattr][write read][append read][write read][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['mdm_helper']['mdm_helper']['fill'] = 'red'
G.add_edge('mdm_helper','mediaserver')
G.edge['mdm_helper']['mediaserver']['write-read'] = '[write read][open open][write read]'
G.edge['mdm_helper']['mediaserver']['fill'] = 'red'
G.add_edge('mdm_helper','mediaserver')
G.edge['mdm_helper']['mediaserver']['write-read'] = '[write read][open open][write read][append read]'
G.add_edge('mdm_helper','mfgloader')
G.edge['mdm_helper']['mfgloader']['write-read'] = '[write read]'
G.edge['mdm_helper']['mfgloader']['fill'] = 'red'
G.add_edge('mdm_helper','mlexe')
G.edge['mdm_helper']['mlexe']['write-read'] = '[open open][write read]'
G.edge['mdm_helper']['mlexe']['fill'] = 'red'
G.add_edge('mdm_helper','mlexe')
G.edge['mdm_helper']['mlexe']['write-read'] = '[open open][write read][append read]'
G.add_edge('mdm_helper','mm-pp-daemon')
G.edge['mdm_helper']['mm-pp-daemon']['write-read'] = '[open open][write read]'
G.edge['mdm_helper']['mm-pp-daemon']['fill'] = 'red'
G.add_edge('mdm_helper','mm-pp-daemon')
G.edge['mdm_helper']['mm-pp-daemon']['write-read'] = '[open open][write read][append read]'
G.add_edge('mdm_helper','mm-pp-daemon')
G.edge['mdm_helper']['mm-pp-daemon']['write-read'] = '[open open][write read][append read][write read]'
G.edge['mdm_helper']['mm-pp-daemon']['fill'] = 'red'
G.add_edge('mdm_helper','mm-qcamera-daemon')
G.edge['mdm_helper']['mm-qcamera-daemon']['write-read'] = '[open open][write read]'
G.edge['mdm_helper']['mm-qcamera-daemon']['fill'] = 'red'
G.add_edge('mdm_helper','mm-qcamera-daemon')
G.edge['mdm_helper']['mm-qcamera-daemon']['write-read'] = '[open open][write read][append read]'
G.add_edge('mdm_helper','mpdecision')
G.edge['mdm_helper']['mpdecision']['write-read'] = '[open open][write read]'
G.edge['mdm_helper']['mpdecision']['fill'] = 'red'
G.add_edge('mdm_helper','mpdecision')
G.edge['mdm_helper']['mpdecision']['write-read'] = '[open open][write read][append read]'
G.add_edge('mdm_helper','mpdecision')
G.edge['mdm_helper']['mpdecision']['write-read'] = '[open open][write read][append read][write read]'
G.edge['mdm_helper']['mpdecision']['fill'] = 'red'
G.add_edge('mdm_helper','netd')
G.edge['mdm_helper']['netd']['write-read'] = '[write read]'
G.edge['mdm_helper']['netd']['fill'] = 'red'
G.add_edge('mdm_helper','netmgrd')
G.edge['mdm_helper']['netmgrd']['write-read'] = '[write read]'
G.edge['mdm_helper']['netmgrd']['fill'] = 'red'
G.add_edge('mdm_helper','nfc')
G.edge['mdm_helper']['nfc']['write-read'] = '[write read]'
G.edge['mdm_helper']['nfc']['fill'] = 'red'
G.add_edge('mdm_helper','oneseg_mw')
G.edge['mdm_helper']['oneseg_mw']['write-read'] = '[open open][write read]'
G.edge['mdm_helper']['oneseg_mw']['fill'] = 'red'
G.add_edge('mdm_helper','oneseg_mw')
G.edge['mdm_helper']['oneseg_mw']['write-read'] = '[open open][write read][append read]'
G.add_edge('mdm_helper','perfd')
G.edge['mdm_helper']['perfd']['write-read'] = '[write read]'
G.edge['mdm_helper']['perfd']['fill'] = 'red'
G.add_edge('mdm_helper','qcks')
G.edge['mdm_helper']['qcks']['write-read'] = '[open open][write read]'
G.edge['mdm_helper']['qcks']['fill'] = 'red'
G.add_edge('mdm_helper','qcks')
G.edge['mdm_helper']['qcks']['write-read'] = '[open open][write read][append read]'
G.add_edge('mdm_helper','qmuxd')
G.edge['mdm_helper']['qmuxd']['write-read'] = '[open open][write read]'
G.edge['mdm_helper']['qmuxd']['fill'] = 'red'
G.add_edge('mdm_helper','qmuxd')
G.edge['mdm_helper']['qmuxd']['write-read'] = '[open open][write read][append read]'
G.add_edge('mdm_helper','qosmgr')
G.edge['mdm_helper']['qosmgr']['write-read'] = '[write read]'
G.edge['mdm_helper']['qosmgr']['fill'] = 'red'
G.add_edge('mdm_helper','radio')
G.edge['mdm_helper']['radio']['write-read'] = '[open open][append read]'
G.add_edge('mdm_helper','rild')
G.edge['mdm_helper']['rild']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['mdm_helper']['rild']['fill'] = 'red'
G.add_edge('mdm_helper','rild')
G.edge['mdm_helper']['rild']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('mdm_helper','rmt_storage')
G.edge['mdm_helper']['rmt_storage']['write-read'] = '[open open][write read]'
G.edge['mdm_helper']['rmt_storage']['fill'] = 'red'
G.add_edge('mdm_helper','rmt_storage')
G.edge['mdm_helper']['rmt_storage']['write-read'] = '[open open][write read][append read]'
G.add_edge('mdm_helper','rtcc')
G.edge['mdm_helper']['rtcc']['write-read'] = '[setattr getattr][write read]'
G.edge['mdm_helper']['rtcc']['fill'] = 'red'
G.add_edge('mdm_helper','sec-ril')
G.edge['mdm_helper']['sec-ril']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['mdm_helper']['sec-ril']['fill'] = 'red'
G.add_edge('mdm_helper','sec-ril')
G.edge['mdm_helper']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('mdm_helper','sensorhubservice')
G.edge['mdm_helper']['sensorhubservice']['write-read'] = '[write read]'
G.edge['mdm_helper']['sensorhubservice']['fill'] = 'red'
G.add_edge('mdm_helper','smdexe')
G.edge['mdm_helper']['smdexe']['write-read'] = '[open open][write read]'
G.edge['mdm_helper']['smdexe']['fill'] = 'red'
G.add_edge('mdm_helper','smdexe')
G.edge['mdm_helper']['smdexe']['write-read'] = '[open open][write read][append read]'
G.add_edge('mdm_helper','ssr_setup')
G.edge['mdm_helper']['ssr_setup']['write-read'] = '[open open][write read]'
G.edge['mdm_helper']['ssr_setup']['fill'] = 'red'
G.add_edge('mdm_helper','ssr_setup')
G.edge['mdm_helper']['ssr_setup']['write-read'] = '[open open][write read][append read]'
G.add_edge('mdm_helper','sswap')
G.edge['mdm_helper']['sswap']['write-read'] = '[open open][write read]'
G.edge['mdm_helper']['sswap']['fill'] = 'red'
G.add_edge('mdm_helper','sswap')
G.edge['mdm_helper']['sswap']['write-read'] = '[open open][write read][append read]'
G.add_edge('mdm_helper','surfaceflinger')
G.edge['mdm_helper']['surfaceflinger']['write-read'] = '[open open][write read]'
G.edge['mdm_helper']['surfaceflinger']['fill'] = 'red'
G.add_edge('mdm_helper','surfaceflinger')
G.edge['mdm_helper']['surfaceflinger']['write-read'] = '[open open][write read][append read]'
G.add_edge('mdm_helper','surfaceflinger')
G.edge['mdm_helper']['surfaceflinger']['write-read'] = '[open open][write read][append read][write read]'
G.edge['mdm_helper']['surfaceflinger']['fill'] = 'red'
G.add_edge('mdm_helper','system_server')
G.edge['mdm_helper']['system_server']['write-read'] = '[open open][open open][setattr getattr][write read]'
G.edge['mdm_helper']['system_server']['fill'] = 'red'
G.add_edge('mdm_helper','system_server')
G.edge['mdm_helper']['system_server']['write-read'] = '[open open][open open][setattr getattr][write read][append read]'
G.add_edge('mdm_helper','system_server')
G.edge['mdm_helper']['system_server']['write-read'] = '[open open][open open][setattr getattr][write read][append read][write read]'
G.edge['mdm_helper']['system_server']['fill'] = 'red'
G.add_edge('mdm_helper','system_server')
G.edge['mdm_helper']['system_server']['write-read'] = '[open open][open open][setattr getattr][write read][append read][write read][append read]'
G.add_edge('mdm_helper','thermald')
G.edge['mdm_helper']['thermald']['write-read'] = '[write read]'
G.edge['mdm_helper']['thermald']['fill'] = 'red'
G.add_edge('mdm_helper','thermal-engine')
G.edge['mdm_helper']['thermal-engine']['write-read'] = '[open open][write read]'
G.edge['mdm_helper']['thermal-engine']['fill'] = 'red'
G.add_edge('mdm_helper','thermal-engine')
G.edge['mdm_helper']['thermal-engine']['write-read'] = '[open open][write read][append read]'
G.add_edge('mdm_helper','thermal-engine')
G.edge['mdm_helper']['thermal-engine']['write-read'] = '[open open][write read][append read][write read]'
G.edge['mdm_helper']['thermal-engine']['fill'] = 'red'
G.add_edge('mdm_helper','ueventd')
G.edge['mdm_helper']['ueventd']['write-read'] = '[open open][write read]'
G.edge['mdm_helper']['ueventd']['fill'] = 'red'
G.add_edge('mdm_helper','ueventd')
G.edge['mdm_helper']['ueventd']['write-read'] = '[open open][write read][append read]'
G.add_edge('mdm_helper','vm_bms')
G.edge['mdm_helper']['vm_bms']['write-read'] = '[open open][write read]'
G.edge['mdm_helper']['vm_bms']['fill'] = 'red'
G.add_edge('mdm_helper','vm_bms')
G.edge['mdm_helper']['vm_bms']['write-read'] = '[open open][write read][append read]'
G.add_edge('mdm_helper','vmwared')
G.edge['mdm_helper']['vmwared']['write-read'] = '[write read]'
G.edge['mdm_helper']['vmwared']['fill'] = 'red'
G.add_edge('mdm_helper','vold')
G.edge['mdm_helper']['vold']['write-read'] = '[setattr getattr][add_name search][remove_name search][open open][write read]'
G.edge['mdm_helper']['vold']['fill'] = 'red'
G.add_edge('mdm_helper','vold')
G.edge['mdm_helper']['vold']['write-read'] = '[setattr getattr][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('mdm_helper','zygote')
G.edge['mdm_helper']['zygote']['write-read'] = '[write read]'
G.edge['mdm_helper']['zygote']['fill'] = 'red'
G.add_edge('mediaserver','at_distributor')
G.edge['mediaserver']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('mediaserver','bauthserver')
G.edge['mediaserver']['bauthserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('mediaserver','bintvoutservice')
G.edge['mediaserver']['bintvoutservice']['write-read'] = '[open open]'
G.add_edge('mediaserver','bluetooth')
G.edge['mediaserver']['bluetooth']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read][open open]'
G.add_edge('mediaserver','cbd')
G.edge['mediaserver']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('mediaserver','cellgeofenced')
G.edge['mediaserver']['cellgeofenced']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('mediaserver','charger_monitor')
G.edge['mediaserver']['charger_monitor']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('mediaserver','charger_monitor')
G.edge['mediaserver']['charger_monitor']['write-read'] = '[open open][write read][append read][open open][open open]'
G.add_edge('mediaserver','cnd')
G.edge['mediaserver']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][append read][open open]'
G.add_edge('mediaserver','connfwexe')
G.edge['mediaserver']['connfwexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('mediaserver','debuggerd')
G.edge['mediaserver']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('mediaserver','diag_uart_log')
G.edge['mediaserver']['diag_uart_log']['write-read'] = '[open open]'
G.add_edge('mediaserver','dumpstate')
G.edge['mediaserver']['dumpstate']['write-read'] = '[open open][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('mediaserver','efsks')
G.edge['mediaserver']['efsks']['write-read'] = '[open open]'
G.add_edge('mediaserver','geomagneticd')
G.edge['mediaserver']['geomagneticd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open]'
G.add_edge('mediaserver','gpsd')
G.edge['mediaserver']['gpsd']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('mediaserver','init_shell')
G.edge['mediaserver']['init_shell']['write-read'] = '[open open][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][write read][append read][open open]'
G.add_edge('mediaserver','kiesexe')
G.edge['mediaserver']['kiesexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('mediaserver','ks')
G.edge['mediaserver']['ks']['write-read'] = '[open open][append read][open open]'
G.add_edge('mediaserver','lhd')
G.edge['mediaserver']['lhd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('mediaserver','lpm')
G.edge['mediaserver']['lpm']['write-read'] = '[open open]'
G.add_edge('mediaserver','macloader')
G.edge['mediaserver']['macloader']['write-read'] = '[open open]'
G.add_edge('mediaserver','mdm_helper')
G.edge['mediaserver']['mdm_helper']['write-read'] = '[open open][append read][open open]'
G.add_edge('mediaserver','mediaserver')
G.edge['mediaserver']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('mediaserver','mlexe')
G.edge['mediaserver']['mlexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('mediaserver','mm-pp-daemon')
G.edge['mediaserver']['mm-pp-daemon']['write-read'] = '[open open]'
G.add_edge('mediaserver','mm-qcamera-daemon')
G.edge['mediaserver']['mm-qcamera-daemon']['write-read'] = '[open open][write read][add_name search][remove_name search][open open]'
G.add_edge('mediaserver','mpdecision')
G.edge['mediaserver']['mpdecision']['write-read'] = '[open open][write read][add_name search][remove_name search][open open]'
G.add_edge('mediaserver','oneseg_mw')
G.edge['mediaserver']['oneseg_mw']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('mediaserver','qcks')
G.edge['mediaserver']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][append read][open open]'
G.add_edge('mediaserver','qmuxd')
G.edge['mediaserver']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][append read][write read][append read][open open]'
G.add_edge('mediaserver','radio')
G.edge['mediaserver']['radio']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open]'
G.add_edge('mediaserver','rild')
G.edge['mediaserver']['rild']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('mediaserver','rmt_storage')
G.edge['mediaserver']['rmt_storage']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('mediaserver','sec-ril')
G.edge['mediaserver']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][open open]'
G.add_edge('mediaserver','smdexe')
G.edge['mediaserver']['smdexe']['write-read'] = '[open open]'
G.add_edge('mediaserver','ssr_setup')
G.edge['mediaserver']['ssr_setup']['write-read'] = '[open open]'
G.add_edge('mediaserver','sswap')
G.edge['mediaserver']['sswap']['write-read'] = '[open open]'
G.add_edge('mediaserver','surfaceflinger')
G.edge['mediaserver']['surfaceflinger']['write-read'] = '[open open][write read][append read][write read][open open][write read][append read][open open]'
G.add_edge('mediaserver','system_server')
G.edge['mediaserver']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open]'
G.add_edge('mediaserver','system_server')
G.edge['mediaserver']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][open open]'
G.add_edge('mediaserver','thermal-engine')
G.edge['mediaserver']['thermal-engine']['write-read'] = '[open open]'
G.add_edge('mediaserver','ueventd')
G.edge['mediaserver']['ueventd']['write-read'] = '[open open]'
G.add_edge('mediaserver','vm_bms')
G.edge['mediaserver']['vm_bms']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('mediaserver','vold')
G.edge['mediaserver']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][append read][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('mediaserver','init_shell')
G.edge['mediaserver']['init_shell']['write-read'] = '[open open][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('mediaserver','rild')
G.edge['mediaserver']['rild']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr]'
G.add_edge('mediaserver','rtcc')
G.edge['mediaserver']['rtcc']['write-read'] = '[setattr getattr]'
G.add_edge('mediaserver','sec-ril')
G.edge['mediaserver']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][open open][setattr getattr]'
G.add_edge('mediaserver','system_server')
G.edge['mediaserver']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][open open][setattr getattr]'
G.add_edge('mediaserver','at_distributor')
G.edge['mediaserver']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read]'
G.edge['mediaserver']['at_distributor']['fill'] = 'red'
G.add_edge('mediaserver','at_distributor')
G.edge['mediaserver']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read]'
G.add_edge('mediaserver','bauthserver')
G.edge['mediaserver']['bauthserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['mediaserver']['bauthserver']['fill'] = 'red'
G.add_edge('mediaserver','bauthserver')
G.edge['mediaserver']['bauthserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('mediaserver','bintvoutservice')
G.edge['mediaserver']['bintvoutservice']['write-read'] = '[open open][write read]'
G.edge['mediaserver']['bintvoutservice']['fill'] = 'red'
G.add_edge('mediaserver','bintvoutservice')
G.edge['mediaserver']['bintvoutservice']['write-read'] = '[open open][write read][append read]'
G.add_edge('mediaserver','bluetooth')
G.edge['mediaserver']['bluetooth']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read][open open][write read]'
G.edge['mediaserver']['bluetooth']['fill'] = 'red'
G.add_edge('mediaserver','bluetooth')
G.edge['mediaserver']['bluetooth']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read][open open][write read][append read]'
G.add_edge('mediaserver','bootanim')
G.edge['mediaserver']['bootanim']['write-read'] = '[open open][write read][append read][write read]'
G.edge['mediaserver']['bootanim']['fill'] = 'red'
G.add_edge('mediaserver','cbd')
G.edge['mediaserver']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['mediaserver']['cbd']['fill'] = 'red'
G.add_edge('mediaserver','cbd')
G.edge['mediaserver']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('mediaserver','cellgeofenced')
G.edge['mediaserver']['cellgeofenced']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['mediaserver']['cellgeofenced']['fill'] = 'red'
G.add_edge('mediaserver','cellgeofenced')
G.edge['mediaserver']['cellgeofenced']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('mediaserver','charger_monitor')
G.edge['mediaserver']['charger_monitor']['write-read'] = '[open open][write read][append read][open open][open open][write read]'
G.edge['mediaserver']['charger_monitor']['fill'] = 'red'
G.add_edge('mediaserver','charger_monitor')
G.edge['mediaserver']['charger_monitor']['write-read'] = '[open open][write read][append read][open open][open open][write read][append read]'
G.add_edge('mediaserver','charger_monitor')
G.edge['mediaserver']['charger_monitor']['write-read'] = '[open open][write read][append read][open open][open open][write read][append read][write read]'
G.edge['mediaserver']['charger_monitor']['fill'] = 'red'
G.add_edge('mediaserver','charger_monitor')
G.edge['mediaserver']['charger_monitor']['write-read'] = '[open open][write read][append read][open open][open open][write read][append read][write read][append read]'
G.add_edge('mediaserver','cnd')
G.edge['mediaserver']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][append read][open open][write read]'
G.edge['mediaserver']['cnd']['fill'] = 'red'
G.add_edge('mediaserver','cnd')
G.edge['mediaserver']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][append read][open open][write read][append read]'
G.add_edge('mediaserver','connfwexe')
G.edge['mediaserver']['connfwexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read]'
G.edge['mediaserver']['connfwexe']['fill'] = 'red'
G.add_edge('mediaserver','connfwexe')
G.edge['mediaserver']['connfwexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read]'
G.add_edge('mediaserver','debuggerd')
G.edge['mediaserver']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read]'
G.edge['mediaserver']['debuggerd']['fill'] = 'red'
G.add_edge('mediaserver','debuggerd')
G.edge['mediaserver']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('mediaserver','diag_uart_log')
G.edge['mediaserver']['diag_uart_log']['write-read'] = '[open open][write read]'
G.edge['mediaserver']['diag_uart_log']['fill'] = 'red'
G.add_edge('mediaserver','diag_uart_log')
G.edge['mediaserver']['diag_uart_log']['write-read'] = '[open open][write read][append read]'
G.add_edge('mediaserver','dumpstate')
G.edge['mediaserver']['dumpstate']['write-read'] = '[open open][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['mediaserver']['dumpstate']['fill'] = 'red'
G.add_edge('mediaserver','dumpstate')
G.edge['mediaserver']['dumpstate']['write-read'] = '[open open][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('mediaserver','efsks')
G.edge['mediaserver']['efsks']['write-read'] = '[open open][write read]'
G.edge['mediaserver']['efsks']['fill'] = 'red'
G.add_edge('mediaserver','efsks')
G.edge['mediaserver']['efsks']['write-read'] = '[open open][write read][append read]'
G.add_edge('mediaserver','geomagneticd')
G.edge['mediaserver']['geomagneticd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['mediaserver']['geomagneticd']['fill'] = 'red'
G.add_edge('mediaserver','geomagneticd')
G.edge['mediaserver']['geomagneticd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('mediaserver','gpsd')
G.edge['mediaserver']['gpsd']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read]'
G.edge['mediaserver']['gpsd']['fill'] = 'red'
G.add_edge('mediaserver','gpsd')
G.edge['mediaserver']['gpsd']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('mediaserver','healthd')
G.edge['mediaserver']['healthd']['write-read'] = '[open open][write read][append read][write read]'
G.edge['mediaserver']['healthd']['fill'] = 'red'
G.add_edge('mediaserver','init_shell')
G.edge['mediaserver']['init_shell']['write-read'] = '[open open][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['mediaserver']['init_shell']['fill'] = 'red'
G.add_edge('mediaserver','init_shell')
G.edge['mediaserver']['init_shell']['write-read'] = '[open open][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('mediaserver','jackservice')
G.edge['mediaserver']['jackservice']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['mediaserver']['jackservice']['fill'] = 'red'
G.add_edge('mediaserver','kiesexe')
G.edge['mediaserver']['kiesexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['mediaserver']['kiesexe']['fill'] = 'red'
G.add_edge('mediaserver','kiesexe')
G.edge['mediaserver']['kiesexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('mediaserver','ks')
G.edge['mediaserver']['ks']['write-read'] = '[open open][append read][open open][write read]'
G.edge['mediaserver']['ks']['fill'] = 'red'
G.add_edge('mediaserver','ks')
G.edge['mediaserver']['ks']['write-read'] = '[open open][append read][open open][write read][append read]'
G.add_edge('mediaserver','lhd')
G.edge['mediaserver']['lhd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read]'
G.edge['mediaserver']['lhd']['fill'] = 'red'
G.add_edge('mediaserver','lhd')
G.edge['mediaserver']['lhd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read]'
G.add_edge('mediaserver','lmkd')
G.edge['mediaserver']['lmkd']['write-read'] = '[write read]'
G.edge['mediaserver']['lmkd']['fill'] = 'red'
G.add_edge('mediaserver','lpm')
G.edge['mediaserver']['lpm']['write-read'] = '[open open][write read]'
G.edge['mediaserver']['lpm']['fill'] = 'red'
G.add_edge('mediaserver','lpm')
G.edge['mediaserver']['lpm']['write-read'] = '[open open][write read][append read]'
G.add_edge('mediaserver','macloader')
G.edge['mediaserver']['macloader']['write-read'] = '[open open][write read]'
G.edge['mediaserver']['macloader']['fill'] = 'red'
G.add_edge('mediaserver','macloader')
G.edge['mediaserver']['macloader']['write-read'] = '[open open][write read][append read]'
G.add_edge('mediaserver','mdm_helper')
G.edge['mediaserver']['mdm_helper']['write-read'] = '[open open][append read][open open][write read]'
G.edge['mediaserver']['mdm_helper']['fill'] = 'red'
G.add_edge('mediaserver','mediaserver')
G.edge['mediaserver']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['mediaserver']['mediaserver']['fill'] = 'red'
G.add_edge('mediaserver','mediaserver')
G.edge['mediaserver']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('mediaserver','mfgloader')
G.edge['mediaserver']['mfgloader']['write-read'] = '[open open][write read][add_name search][remove_name search][write read]'
G.edge['mediaserver']['mfgloader']['fill'] = 'red'
G.add_edge('mediaserver','mlexe')
G.edge['mediaserver']['mlexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['mediaserver']['mlexe']['fill'] = 'red'
G.add_edge('mediaserver','mlexe')
G.edge['mediaserver']['mlexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('mediaserver','mm-pp-daemon')
G.edge['mediaserver']['mm-pp-daemon']['write-read'] = '[open open][write read]'
G.edge['mediaserver']['mm-pp-daemon']['fill'] = 'red'
G.add_edge('mediaserver','mm-pp-daemon')
G.edge['mediaserver']['mm-pp-daemon']['write-read'] = '[open open][write read][append read]'
G.add_edge('mediaserver','mm-pp-daemon')
G.edge['mediaserver']['mm-pp-daemon']['write-read'] = '[open open][write read][append read][write read]'
G.edge['mediaserver']['mm-pp-daemon']['fill'] = 'red'
G.add_edge('mediaserver','mm-qcamera-daemon')
G.edge['mediaserver']['mm-qcamera-daemon']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['mediaserver']['mm-qcamera-daemon']['fill'] = 'red'
G.add_edge('mediaserver','mm-qcamera-daemon')
G.edge['mediaserver']['mm-qcamera-daemon']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('mediaserver','mpdecision')
G.edge['mediaserver']['mpdecision']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['mediaserver']['mpdecision']['fill'] = 'red'
G.add_edge('mediaserver','mpdecision')
G.edge['mediaserver']['mpdecision']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('mediaserver','mpdecision')
G.edge['mediaserver']['mpdecision']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read][write read]'
G.edge['mediaserver']['mpdecision']['fill'] = 'red'
G.add_edge('mediaserver','netd')
G.edge['mediaserver']['netd']['write-read'] = '[open open][write read][append read][write read]'
G.edge['mediaserver']['netd']['fill'] = 'red'
G.add_edge('mediaserver','netmgrd')
G.edge['mediaserver']['netmgrd']['write-read'] = '[open open][open open][write read][write read][add_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][write read]'
G.edge['mediaserver']['netmgrd']['fill'] = 'red'
G.add_edge('mediaserver','nfc')
G.edge['mediaserver']['nfc']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['mediaserver']['nfc']['fill'] = 'red'
G.add_edge('mediaserver','oneseg_mw')
G.edge['mediaserver']['oneseg_mw']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['mediaserver']['oneseg_mw']['fill'] = 'red'
G.add_edge('mediaserver','oneseg_mw')
G.edge['mediaserver']['oneseg_mw']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('mediaserver','perfd')
G.edge['mediaserver']['perfd']['write-read'] = '[write read]'
G.edge['mediaserver']['perfd']['fill'] = 'red'
G.add_edge('mediaserver','qcks')
G.edge['mediaserver']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][append read][open open][write read]'
G.edge['mediaserver']['qcks']['fill'] = 'red'
G.add_edge('mediaserver','qcks')
G.edge['mediaserver']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][append read][open open][write read][append read]'
G.add_edge('mediaserver','qmuxd')
G.edge['mediaserver']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][append read][write read][append read][open open][write read]'
G.edge['mediaserver']['qmuxd']['fill'] = 'red'
G.add_edge('mediaserver','qmuxd')
G.edge['mediaserver']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][append read][write read][append read][open open][write read][append read]'
G.add_edge('mediaserver','qosmgr')
G.edge['mediaserver']['qosmgr']['write-read'] = '[write read]'
G.edge['mediaserver']['qosmgr']['fill'] = 'red'
G.add_edge('mediaserver','radio')
G.edge['mediaserver']['radio']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][append read]'
G.add_edge('mediaserver','rild')
G.edge['mediaserver']['rild']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['mediaserver']['rild']['fill'] = 'red'
G.add_edge('mediaserver','rild')
G.edge['mediaserver']['rild']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('mediaserver','rmt_storage')
G.edge['mediaserver']['rmt_storage']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['mediaserver']['rmt_storage']['fill'] = 'red'
G.add_edge('mediaserver','rmt_storage')
G.edge['mediaserver']['rmt_storage']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('mediaserver','rtcc')
G.edge['mediaserver']['rtcc']['write-read'] = '[setattr getattr][write read]'
G.edge['mediaserver']['rtcc']['fill'] = 'red'
G.add_edge('mediaserver','sec-ril')
G.edge['mediaserver']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][open open][setattr getattr][write read]'
G.edge['mediaserver']['sec-ril']['fill'] = 'red'
G.add_edge('mediaserver','sec-ril')
G.edge['mediaserver']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][open open][setattr getattr][write read][append read]'
G.add_edge('mediaserver','sensorhubservice')
G.edge['mediaserver']['sensorhubservice']['write-read'] = '[write read]'
G.edge['mediaserver']['sensorhubservice']['fill'] = 'red'
G.add_edge('mediaserver','smdexe')
G.edge['mediaserver']['smdexe']['write-read'] = '[open open][write read]'
G.edge['mediaserver']['smdexe']['fill'] = 'red'
G.add_edge('mediaserver','smdexe')
G.edge['mediaserver']['smdexe']['write-read'] = '[open open][write read][append read]'
G.add_edge('mediaserver','ssr_setup')
G.edge['mediaserver']['ssr_setup']['write-read'] = '[open open][write read]'
G.edge['mediaserver']['ssr_setup']['fill'] = 'red'
G.add_edge('mediaserver','ssr_setup')
G.edge['mediaserver']['ssr_setup']['write-read'] = '[open open][write read][append read]'
G.add_edge('mediaserver','sswap')
G.edge['mediaserver']['sswap']['write-read'] = '[open open][write read]'
G.edge['mediaserver']['sswap']['fill'] = 'red'
G.add_edge('mediaserver','sswap')
G.edge['mediaserver']['sswap']['write-read'] = '[open open][write read][append read]'
G.add_edge('mediaserver','surfaceflinger')
G.edge['mediaserver']['surfaceflinger']['write-read'] = '[open open][write read][append read][write read][open open][write read][append read][open open][write read]'
G.edge['mediaserver']['surfaceflinger']['fill'] = 'red'
G.add_edge('mediaserver','surfaceflinger')
G.edge['mediaserver']['surfaceflinger']['write-read'] = '[open open][write read][append read][write read][open open][write read][append read][open open][write read][append read]'
G.add_edge('mediaserver','surfaceflinger')
G.edge['mediaserver']['surfaceflinger']['write-read'] = '[open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][write read]'
G.edge['mediaserver']['surfaceflinger']['fill'] = 'red'
G.add_edge('mediaserver','system_server')
G.edge['mediaserver']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][open open][setattr getattr][write read]'
G.edge['mediaserver']['system_server']['fill'] = 'red'
G.add_edge('mediaserver','system_server')
G.edge['mediaserver']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][open open][setattr getattr][write read][append read]'
G.add_edge('mediaserver','system_server')
G.edge['mediaserver']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][open open][setattr getattr][write read][append read][write read]'
G.edge['mediaserver']['system_server']['fill'] = 'red'
G.add_edge('mediaserver','system_server')
G.edge['mediaserver']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][open open][setattr getattr][write read][append read][write read][append read]'
G.add_edge('mediaserver','thermald')
G.edge['mediaserver']['thermald']['write-read'] = '[open open][write read][add_name search][remove_name search][write read]'
G.edge['mediaserver']['thermald']['fill'] = 'red'
G.add_edge('mediaserver','thermal-engine')
G.edge['mediaserver']['thermal-engine']['write-read'] = '[open open][write read]'
G.edge['mediaserver']['thermal-engine']['fill'] = 'red'
G.add_edge('mediaserver','thermal-engine')
G.edge['mediaserver']['thermal-engine']['write-read'] = '[open open][write read][append read]'
G.add_edge('mediaserver','thermal-engine')
G.edge['mediaserver']['thermal-engine']['write-read'] = '[open open][write read][append read][write read]'
G.edge['mediaserver']['thermal-engine']['fill'] = 'red'
G.add_edge('mediaserver','ueventd')
G.edge['mediaserver']['ueventd']['write-read'] = '[open open][write read]'
G.edge['mediaserver']['ueventd']['fill'] = 'red'
G.add_edge('mediaserver','ueventd')
G.edge['mediaserver']['ueventd']['write-read'] = '[open open][write read][append read]'
G.add_edge('mediaserver','vm_bms')
G.edge['mediaserver']['vm_bms']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['mediaserver']['vm_bms']['fill'] = 'red'
G.add_edge('mediaserver','vm_bms')
G.edge['mediaserver']['vm_bms']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('mediaserver','vmwared')
G.edge['mediaserver']['vmwared']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][write read]'
G.edge['mediaserver']['vmwared']['fill'] = 'red'
G.add_edge('mediaserver','vold')
G.edge['mediaserver']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][append read][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read]'
G.edge['mediaserver']['vold']['fill'] = 'red'
G.add_edge('mediaserver','vold')
G.edge['mediaserver']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][append read][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read]'
G.add_edge('mediaserver','zygote')
G.edge['mediaserver']['zygote']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][write read][write read]'
G.edge['mediaserver']['zygote']['fill'] = 'red'
G.add_edge('mm-pp-daemon','at_distributor')
G.edge['mm-pp-daemon']['at_distributor']['write-read'] = '[open open]'
G.add_edge('mm-pp-daemon','bauthserver')
G.edge['mm-pp-daemon']['bauthserver']['write-read'] = '[open open]'
G.add_edge('mm-pp-daemon','bintvoutservice')
G.edge['mm-pp-daemon']['bintvoutservice']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('mm-pp-daemon','bluetooth')
G.edge['mm-pp-daemon']['bluetooth']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('mm-pp-daemon','cbd')
G.edge['mm-pp-daemon']['cbd']['write-read'] = '[open open]'
G.add_edge('mm-pp-daemon','cellgeofenced')
G.edge['mm-pp-daemon']['cellgeofenced']['write-read'] = '[open open]'
G.add_edge('mm-pp-daemon','charger_monitor')
G.edge['mm-pp-daemon']['charger_monitor']['write-read'] = '[open open]'
G.add_edge('mm-pp-daemon','charger_monitor')
G.edge['mm-pp-daemon']['charger_monitor']['write-read'] = '[open open][open open]'
G.add_edge('mm-pp-daemon','cnd')
G.edge['mm-pp-daemon']['cnd']['write-read'] = '[open open]'
G.add_edge('mm-pp-daemon','connfwexe')
G.edge['mm-pp-daemon']['connfwexe']['write-read'] = '[open open]'
G.add_edge('mm-pp-daemon','debuggerd')
G.edge['mm-pp-daemon']['debuggerd']['write-read'] = '[open open]'
G.add_edge('mm-pp-daemon','diag_uart_log')
G.edge['mm-pp-daemon']['diag_uart_log']['write-read'] = '[open open]'
G.add_edge('mm-pp-daemon','dumpstate')
G.edge['mm-pp-daemon']['dumpstate']['write-read'] = '[open open]'
G.add_edge('mm-pp-daemon','efsks')
G.edge['mm-pp-daemon']['efsks']['write-read'] = '[open open]'
G.add_edge('mm-pp-daemon','geomagneticd')
G.edge['mm-pp-daemon']['geomagneticd']['write-read'] = '[open open]'
G.add_edge('mm-pp-daemon','gpsd')
G.edge['mm-pp-daemon']['gpsd']['write-read'] = '[open open]'
G.add_edge('mm-pp-daemon','init_shell')
G.edge['mm-pp-daemon']['init_shell']['write-read'] = '[open open]'
G.add_edge('mm-pp-daemon','kiesexe')
G.edge['mm-pp-daemon']['kiesexe']['write-read'] = '[open open]'
G.add_edge('mm-pp-daemon','ks')
G.edge['mm-pp-daemon']['ks']['write-read'] = '[open open]'
G.add_edge('mm-pp-daemon','lhd')
G.edge['mm-pp-daemon']['lhd']['write-read'] = '[open open]'
G.add_edge('mm-pp-daemon','lpm')
G.edge['mm-pp-daemon']['lpm']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('mm-pp-daemon','macloader')
G.edge['mm-pp-daemon']['macloader']['write-read'] = '[open open]'
G.add_edge('mm-pp-daemon','mdm_helper')
G.edge['mm-pp-daemon']['mdm_helper']['write-read'] = '[open open]'
G.add_edge('mm-pp-daemon','mediaserver')
G.edge['mm-pp-daemon']['mediaserver']['write-read'] = '[open open]'
G.add_edge('mm-pp-daemon','mlexe')
G.edge['mm-pp-daemon']['mlexe']['write-read'] = '[open open]'
G.add_edge('mm-pp-daemon','mm-pp-daemon')
G.edge['mm-pp-daemon']['mm-pp-daemon']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][write read][append read][open open]'
G.add_edge('mm-pp-daemon','mm-qcamera-daemon')
G.edge['mm-pp-daemon']['mm-qcamera-daemon']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('mm-pp-daemon','mpdecision')
G.edge['mm-pp-daemon']['mpdecision']['write-read'] = '[open open]'
G.add_edge('mm-pp-daemon','oneseg_mw')
G.edge['mm-pp-daemon']['oneseg_mw']['write-read'] = '[open open]'
G.add_edge('mm-pp-daemon','qcks')
G.edge['mm-pp-daemon']['qcks']['write-read'] = '[open open]'
G.add_edge('mm-pp-daemon','qmuxd')
G.edge['mm-pp-daemon']['qmuxd']['write-read'] = '[open open]'
G.add_edge('mm-pp-daemon','radio')
G.edge['mm-pp-daemon']['radio']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('mm-pp-daemon','rild')
G.edge['mm-pp-daemon']['rild']['write-read'] = '[open open]'
G.add_edge('mm-pp-daemon','rmt_storage')
G.edge['mm-pp-daemon']['rmt_storage']['write-read'] = '[open open]'
G.add_edge('mm-pp-daemon','sec-ril')
G.edge['mm-pp-daemon']['sec-ril']['write-read'] = '[open open]'
G.add_edge('mm-pp-daemon','smdexe')
G.edge['mm-pp-daemon']['smdexe']['write-read'] = '[open open]'
G.add_edge('mm-pp-daemon','ssr_setup')
G.edge['mm-pp-daemon']['ssr_setup']['write-read'] = '[open open]'
G.add_edge('mm-pp-daemon','sswap')
G.edge['mm-pp-daemon']['sswap']['write-read'] = '[open open]'
G.add_edge('mm-pp-daemon','surfaceflinger')
G.edge['mm-pp-daemon']['surfaceflinger']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('mm-pp-daemon','system_server')
G.edge['mm-pp-daemon']['system_server']['write-read'] = '[write read][open open]'
G.add_edge('mm-pp-daemon','system_server')
G.edge['mm-pp-daemon']['system_server']['write-read'] = '[write read][open open][open open]'
G.add_edge('mm-pp-daemon','thermal-engine')
G.edge['mm-pp-daemon']['thermal-engine']['write-read'] = '[open open]'
G.add_edge('mm-pp-daemon','ueventd')
G.edge['mm-pp-daemon']['ueventd']['write-read'] = '[open open]'
G.add_edge('mm-pp-daemon','vm_bms')
G.edge['mm-pp-daemon']['vm_bms']['write-read'] = '[open open]'
G.add_edge('mm-pp-daemon','vold')
G.edge['mm-pp-daemon']['vold']['write-read'] = '[open open]'
G.add_edge('mm-pp-daemon','init_shell')
G.edge['mm-pp-daemon']['init_shell']['write-read'] = '[open open][setattr getattr]'
G.add_edge('mm-pp-daemon','rild')
G.edge['mm-pp-daemon']['rild']['write-read'] = '[open open][setattr getattr]'
G.add_edge('mm-pp-daemon','rtcc')
G.edge['mm-pp-daemon']['rtcc']['write-read'] = '[setattr getattr]'
G.add_edge('mm-pp-daemon','sec-ril')
G.edge['mm-pp-daemon']['sec-ril']['write-read'] = '[open open][setattr getattr]'
G.add_edge('mm-pp-daemon','system_server')
G.edge['mm-pp-daemon']['system_server']['write-read'] = '[write read][open open][open open][setattr getattr]'
G.add_edge('mm-pp-daemon','at_distributor')
G.edge['mm-pp-daemon']['at_distributor']['write-read'] = '[open open][write read]'
G.edge['mm-pp-daemon']['at_distributor']['fill'] = 'red'
G.add_edge('mm-pp-daemon','at_distributor')
G.edge['mm-pp-daemon']['at_distributor']['write-read'] = '[open open][write read][append read]'
G.add_edge('mm-pp-daemon','bauthserver')
G.edge['mm-pp-daemon']['bauthserver']['write-read'] = '[open open][write read]'
G.edge['mm-pp-daemon']['bauthserver']['fill'] = 'red'
G.add_edge('mm-pp-daemon','bauthserver')
G.edge['mm-pp-daemon']['bauthserver']['write-read'] = '[open open][write read][append read]'
G.add_edge('mm-pp-daemon','bintvoutservice')
G.edge['mm-pp-daemon']['bintvoutservice']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['mm-pp-daemon']['bintvoutservice']['fill'] = 'red'
G.add_edge('mm-pp-daemon','bintvoutservice')
G.edge['mm-pp-daemon']['bintvoutservice']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('mm-pp-daemon','bluetooth')
G.edge['mm-pp-daemon']['bluetooth']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['mm-pp-daemon']['bluetooth']['fill'] = 'red'
G.add_edge('mm-pp-daemon','bluetooth')
G.edge['mm-pp-daemon']['bluetooth']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('mm-pp-daemon','bootanim')
G.edge['mm-pp-daemon']['bootanim']['write-read'] = '[open open][write read][append read][write read]'
G.edge['mm-pp-daemon']['bootanim']['fill'] = 'red'
G.add_edge('mm-pp-daemon','cbd')
G.edge['mm-pp-daemon']['cbd']['write-read'] = '[open open][write read]'
G.edge['mm-pp-daemon']['cbd']['fill'] = 'red'
G.add_edge('mm-pp-daemon','cbd')
G.edge['mm-pp-daemon']['cbd']['write-read'] = '[open open][write read][append read]'
G.add_edge('mm-pp-daemon','cellgeofenced')
G.edge['mm-pp-daemon']['cellgeofenced']['write-read'] = '[open open][write read]'
G.edge['mm-pp-daemon']['cellgeofenced']['fill'] = 'red'
G.add_edge('mm-pp-daemon','cellgeofenced')
G.edge['mm-pp-daemon']['cellgeofenced']['write-read'] = '[open open][write read][append read]'
G.add_edge('mm-pp-daemon','charger_monitor')
G.edge['mm-pp-daemon']['charger_monitor']['write-read'] = '[open open][open open][write read]'
G.edge['mm-pp-daemon']['charger_monitor']['fill'] = 'red'
G.add_edge('mm-pp-daemon','charger_monitor')
G.edge['mm-pp-daemon']['charger_monitor']['write-read'] = '[open open][open open][write read][append read]'
G.add_edge('mm-pp-daemon','charger_monitor')
G.edge['mm-pp-daemon']['charger_monitor']['write-read'] = '[open open][open open][write read][append read][write read]'
G.edge['mm-pp-daemon']['charger_monitor']['fill'] = 'red'
G.add_edge('mm-pp-daemon','charger_monitor')
G.edge['mm-pp-daemon']['charger_monitor']['write-read'] = '[open open][open open][write read][append read][write read][append read]'
G.add_edge('mm-pp-daemon','cnd')
G.edge['mm-pp-daemon']['cnd']['write-read'] = '[open open][write read]'
G.edge['mm-pp-daemon']['cnd']['fill'] = 'red'
G.add_edge('mm-pp-daemon','cnd')
G.edge['mm-pp-daemon']['cnd']['write-read'] = '[open open][write read][append read]'
G.add_edge('mm-pp-daemon','connfwexe')
G.edge['mm-pp-daemon']['connfwexe']['write-read'] = '[open open][write read]'
G.edge['mm-pp-daemon']['connfwexe']['fill'] = 'red'
G.add_edge('mm-pp-daemon','connfwexe')
G.edge['mm-pp-daemon']['connfwexe']['write-read'] = '[open open][write read][append read]'
G.add_edge('mm-pp-daemon','debuggerd')
G.edge['mm-pp-daemon']['debuggerd']['write-read'] = '[open open][write read]'
G.edge['mm-pp-daemon']['debuggerd']['fill'] = 'red'
G.add_edge('mm-pp-daemon','debuggerd')
G.edge['mm-pp-daemon']['debuggerd']['write-read'] = '[open open][write read][append read]'
G.add_edge('mm-pp-daemon','diag_uart_log')
G.edge['mm-pp-daemon']['diag_uart_log']['write-read'] = '[open open][write read]'
G.edge['mm-pp-daemon']['diag_uart_log']['fill'] = 'red'
G.add_edge('mm-pp-daemon','diag_uart_log')
G.edge['mm-pp-daemon']['diag_uart_log']['write-read'] = '[open open][write read][append read]'
G.add_edge('mm-pp-daemon','dumpstate')
G.edge['mm-pp-daemon']['dumpstate']['write-read'] = '[open open][write read]'
G.edge['mm-pp-daemon']['dumpstate']['fill'] = 'red'
G.add_edge('mm-pp-daemon','dumpstate')
G.edge['mm-pp-daemon']['dumpstate']['write-read'] = '[open open][write read][append read]'
G.add_edge('mm-pp-daemon','efsks')
G.edge['mm-pp-daemon']['efsks']['write-read'] = '[open open][write read]'
G.edge['mm-pp-daemon']['efsks']['fill'] = 'red'
G.add_edge('mm-pp-daemon','efsks')
G.edge['mm-pp-daemon']['efsks']['write-read'] = '[open open][write read][append read]'
G.add_edge('mm-pp-daemon','geomagneticd')
G.edge['mm-pp-daemon']['geomagneticd']['write-read'] = '[open open][write read]'
G.edge['mm-pp-daemon']['geomagneticd']['fill'] = 'red'
G.add_edge('mm-pp-daemon','geomagneticd')
G.edge['mm-pp-daemon']['geomagneticd']['write-read'] = '[open open][write read][append read]'
G.add_edge('mm-pp-daemon','gpsd')
G.edge['mm-pp-daemon']['gpsd']['write-read'] = '[open open][write read]'
G.edge['mm-pp-daemon']['gpsd']['fill'] = 'red'
G.add_edge('mm-pp-daemon','gpsd')
G.edge['mm-pp-daemon']['gpsd']['write-read'] = '[open open][write read][append read]'
G.add_edge('mm-pp-daemon','healthd')
G.edge['mm-pp-daemon']['healthd']['write-read'] = '[open open][write read][append read][write read]'
G.edge['mm-pp-daemon']['healthd']['fill'] = 'red'
G.add_edge('mm-pp-daemon','init_shell')
G.edge['mm-pp-daemon']['init_shell']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['mm-pp-daemon']['init_shell']['fill'] = 'red'
G.add_edge('mm-pp-daemon','init_shell')
G.edge['mm-pp-daemon']['init_shell']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('mm-pp-daemon','jackservice')
G.edge['mm-pp-daemon']['jackservice']['write-read'] = '[write read]'
G.edge['mm-pp-daemon']['jackservice']['fill'] = 'red'
G.add_edge('mm-pp-daemon','kiesexe')
G.edge['mm-pp-daemon']['kiesexe']['write-read'] = '[open open][write read]'
G.edge['mm-pp-daemon']['kiesexe']['fill'] = 'red'
G.add_edge('mm-pp-daemon','kiesexe')
G.edge['mm-pp-daemon']['kiesexe']['write-read'] = '[open open][write read][append read]'
G.add_edge('mm-pp-daemon','ks')
G.edge['mm-pp-daemon']['ks']['write-read'] = '[open open][write read]'
G.edge['mm-pp-daemon']['ks']['fill'] = 'red'
G.add_edge('mm-pp-daemon','ks')
G.edge['mm-pp-daemon']['ks']['write-read'] = '[open open][write read][append read]'
G.add_edge('mm-pp-daemon','lhd')
G.edge['mm-pp-daemon']['lhd']['write-read'] = '[open open][write read]'
G.edge['mm-pp-daemon']['lhd']['fill'] = 'red'
G.add_edge('mm-pp-daemon','lhd')
G.edge['mm-pp-daemon']['lhd']['write-read'] = '[open open][write read][append read]'
G.add_edge('mm-pp-daemon','lmkd')
G.edge['mm-pp-daemon']['lmkd']['write-read'] = '[write read]'
G.edge['mm-pp-daemon']['lmkd']['fill'] = 'red'
G.add_edge('mm-pp-daemon','lpm')
G.edge['mm-pp-daemon']['lpm']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['mm-pp-daemon']['lpm']['fill'] = 'red'
G.add_edge('mm-pp-daemon','lpm')
G.edge['mm-pp-daemon']['lpm']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('mm-pp-daemon','macloader')
G.edge['mm-pp-daemon']['macloader']['write-read'] = '[open open][write read]'
G.edge['mm-pp-daemon']['macloader']['fill'] = 'red'
G.add_edge('mm-pp-daemon','macloader')
G.edge['mm-pp-daemon']['macloader']['write-read'] = '[open open][write read][append read]'
G.add_edge('mm-pp-daemon','mdm_helper')
G.edge['mm-pp-daemon']['mdm_helper']['write-read'] = '[open open][write read]'
G.edge['mm-pp-daemon']['mdm_helper']['fill'] = 'red'
G.add_edge('mm-pp-daemon','mediaserver')
G.edge['mm-pp-daemon']['mediaserver']['write-read'] = '[open open][write read]'
G.edge['mm-pp-daemon']['mediaserver']['fill'] = 'red'
G.add_edge('mm-pp-daemon','mediaserver')
G.edge['mm-pp-daemon']['mediaserver']['write-read'] = '[open open][write read][append read]'
G.add_edge('mm-pp-daemon','mfgloader')
G.edge['mm-pp-daemon']['mfgloader']['write-read'] = '[write read]'
G.edge['mm-pp-daemon']['mfgloader']['fill'] = 'red'
G.add_edge('mm-pp-daemon','mlexe')
G.edge['mm-pp-daemon']['mlexe']['write-read'] = '[open open][write read]'
G.edge['mm-pp-daemon']['mlexe']['fill'] = 'red'
G.add_edge('mm-pp-daemon','mlexe')
G.edge['mm-pp-daemon']['mlexe']['write-read'] = '[open open][write read][append read]'
G.add_edge('mm-pp-daemon','mm-pp-daemon')
G.edge['mm-pp-daemon']['mm-pp-daemon']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][write read][append read][open open][write read]'
G.edge['mm-pp-daemon']['mm-pp-daemon']['fill'] = 'red'
G.add_edge('mm-pp-daemon','mm-pp-daemon')
G.edge['mm-pp-daemon']['mm-pp-daemon']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][write read][append read][open open][write read][append read]'
G.add_edge('mm-pp-daemon','mm-pp-daemon')
G.edge['mm-pp-daemon']['mm-pp-daemon']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][write read][append read][open open][write read][append read][write read]'
G.edge['mm-pp-daemon']['mm-pp-daemon']['fill'] = 'red'
G.add_edge('mm-pp-daemon','mm-qcamera-daemon')
G.edge['mm-pp-daemon']['mm-qcamera-daemon']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['mm-pp-daemon']['mm-qcamera-daemon']['fill'] = 'red'
G.add_edge('mm-pp-daemon','mm-qcamera-daemon')
G.edge['mm-pp-daemon']['mm-qcamera-daemon']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('mm-pp-daemon','mpdecision')
G.edge['mm-pp-daemon']['mpdecision']['write-read'] = '[open open][write read]'
G.edge['mm-pp-daemon']['mpdecision']['fill'] = 'red'
G.add_edge('mm-pp-daemon','mpdecision')
G.edge['mm-pp-daemon']['mpdecision']['write-read'] = '[open open][write read][append read]'
G.add_edge('mm-pp-daemon','mpdecision')
G.edge['mm-pp-daemon']['mpdecision']['write-read'] = '[open open][write read][append read][write read]'
G.edge['mm-pp-daemon']['mpdecision']['fill'] = 'red'
G.add_edge('mm-pp-daemon','netd')
G.edge['mm-pp-daemon']['netd']['write-read'] = '[write read]'
G.edge['mm-pp-daemon']['netd']['fill'] = 'red'
G.add_edge('mm-pp-daemon','netmgrd')
G.edge['mm-pp-daemon']['netmgrd']['write-read'] = '[write read]'
G.edge['mm-pp-daemon']['netmgrd']['fill'] = 'red'
G.add_edge('mm-pp-daemon','nfc')
G.edge['mm-pp-daemon']['nfc']['write-read'] = '[write read]'
G.edge['mm-pp-daemon']['nfc']['fill'] = 'red'
G.add_edge('mm-pp-daemon','oneseg_mw')
G.edge['mm-pp-daemon']['oneseg_mw']['write-read'] = '[open open][write read]'
G.edge['mm-pp-daemon']['oneseg_mw']['fill'] = 'red'
G.add_edge('mm-pp-daemon','oneseg_mw')
G.edge['mm-pp-daemon']['oneseg_mw']['write-read'] = '[open open][write read][append read]'
G.add_edge('mm-pp-daemon','perfd')
G.edge['mm-pp-daemon']['perfd']['write-read'] = '[write read]'
G.edge['mm-pp-daemon']['perfd']['fill'] = 'red'
G.add_edge('mm-pp-daemon','qcks')
G.edge['mm-pp-daemon']['qcks']['write-read'] = '[open open][write read]'
G.edge['mm-pp-daemon']['qcks']['fill'] = 'red'
G.add_edge('mm-pp-daemon','qcks')
G.edge['mm-pp-daemon']['qcks']['write-read'] = '[open open][write read][append read]'
G.add_edge('mm-pp-daemon','qmuxd')
G.edge['mm-pp-daemon']['qmuxd']['write-read'] = '[open open][write read]'
G.edge['mm-pp-daemon']['qmuxd']['fill'] = 'red'
G.add_edge('mm-pp-daemon','qmuxd')
G.edge['mm-pp-daemon']['qmuxd']['write-read'] = '[open open][write read][append read]'
G.add_edge('mm-pp-daemon','qosmgr')
G.edge['mm-pp-daemon']['qosmgr']['write-read'] = '[write read]'
G.edge['mm-pp-daemon']['qosmgr']['fill'] = 'red'
G.add_edge('mm-pp-daemon','radio')
G.edge['mm-pp-daemon']['radio']['write-read'] = '[open open][write read][append read][open open][append read]'
G.add_edge('mm-pp-daemon','rild')
G.edge['mm-pp-daemon']['rild']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['mm-pp-daemon']['rild']['fill'] = 'red'
G.add_edge('mm-pp-daemon','rild')
G.edge['mm-pp-daemon']['rild']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('mm-pp-daemon','rmt_storage')
G.edge['mm-pp-daemon']['rmt_storage']['write-read'] = '[open open][write read]'
G.edge['mm-pp-daemon']['rmt_storage']['fill'] = 'red'
G.add_edge('mm-pp-daemon','rmt_storage')
G.edge['mm-pp-daemon']['rmt_storage']['write-read'] = '[open open][write read][append read]'
G.add_edge('mm-pp-daemon','rtcc')
G.edge['mm-pp-daemon']['rtcc']['write-read'] = '[setattr getattr][write read]'
G.edge['mm-pp-daemon']['rtcc']['fill'] = 'red'
G.add_edge('mm-pp-daemon','sec-ril')
G.edge['mm-pp-daemon']['sec-ril']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['mm-pp-daemon']['sec-ril']['fill'] = 'red'
G.add_edge('mm-pp-daemon','sec-ril')
G.edge['mm-pp-daemon']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('mm-pp-daemon','sensorhubservice')
G.edge['mm-pp-daemon']['sensorhubservice']['write-read'] = '[write read]'
G.edge['mm-pp-daemon']['sensorhubservice']['fill'] = 'red'
G.add_edge('mm-pp-daemon','smdexe')
G.edge['mm-pp-daemon']['smdexe']['write-read'] = '[open open][write read]'
G.edge['mm-pp-daemon']['smdexe']['fill'] = 'red'
G.add_edge('mm-pp-daemon','smdexe')
G.edge['mm-pp-daemon']['smdexe']['write-read'] = '[open open][write read][append read]'
G.add_edge('mm-pp-daemon','ssr_setup')
G.edge['mm-pp-daemon']['ssr_setup']['write-read'] = '[open open][write read]'
G.edge['mm-pp-daemon']['ssr_setup']['fill'] = 'red'
G.add_edge('mm-pp-daemon','ssr_setup')
G.edge['mm-pp-daemon']['ssr_setup']['write-read'] = '[open open][write read][append read]'
G.add_edge('mm-pp-daemon','sswap')
G.edge['mm-pp-daemon']['sswap']['write-read'] = '[open open][write read]'
G.edge['mm-pp-daemon']['sswap']['fill'] = 'red'
G.add_edge('mm-pp-daemon','sswap')
G.edge['mm-pp-daemon']['sswap']['write-read'] = '[open open][write read][append read]'
G.add_edge('mm-pp-daemon','surfaceflinger')
G.edge['mm-pp-daemon']['surfaceflinger']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['mm-pp-daemon']['surfaceflinger']['fill'] = 'red'
G.add_edge('mm-pp-daemon','surfaceflinger')
G.edge['mm-pp-daemon']['surfaceflinger']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('mm-pp-daemon','surfaceflinger')
G.edge['mm-pp-daemon']['surfaceflinger']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read]'
G.edge['mm-pp-daemon']['surfaceflinger']['fill'] = 'red'
G.add_edge('mm-pp-daemon','system_server')
G.edge['mm-pp-daemon']['system_server']['write-read'] = '[write read][open open][open open][setattr getattr][write read]'
G.edge['mm-pp-daemon']['system_server']['fill'] = 'red'
G.add_edge('mm-pp-daemon','system_server')
G.edge['mm-pp-daemon']['system_server']['write-read'] = '[write read][open open][open open][setattr getattr][write read][append read]'
G.add_edge('mm-pp-daemon','system_server')
G.edge['mm-pp-daemon']['system_server']['write-read'] = '[write read][open open][open open][setattr getattr][write read][append read][write read]'
G.edge['mm-pp-daemon']['system_server']['fill'] = 'red'
G.add_edge('mm-pp-daemon','system_server')
G.edge['mm-pp-daemon']['system_server']['write-read'] = '[write read][open open][open open][setattr getattr][write read][append read][write read][append read]'
G.add_edge('mm-pp-daemon','thermald')
G.edge['mm-pp-daemon']['thermald']['write-read'] = '[write read]'
G.edge['mm-pp-daemon']['thermald']['fill'] = 'red'
G.add_edge('mm-pp-daemon','thermal-engine')
G.edge['mm-pp-daemon']['thermal-engine']['write-read'] = '[open open][write read]'
G.edge['mm-pp-daemon']['thermal-engine']['fill'] = 'red'
G.add_edge('mm-pp-daemon','thermal-engine')
G.edge['mm-pp-daemon']['thermal-engine']['write-read'] = '[open open][write read][append read]'
G.add_edge('mm-pp-daemon','thermal-engine')
G.edge['mm-pp-daemon']['thermal-engine']['write-read'] = '[open open][write read][append read][write read]'
G.edge['mm-pp-daemon']['thermal-engine']['fill'] = 'red'
G.add_edge('mm-pp-daemon','ueventd')
G.edge['mm-pp-daemon']['ueventd']['write-read'] = '[open open][write read]'
G.edge['mm-pp-daemon']['ueventd']['fill'] = 'red'
G.add_edge('mm-pp-daemon','ueventd')
G.edge['mm-pp-daemon']['ueventd']['write-read'] = '[open open][write read][append read]'
G.add_edge('mm-pp-daemon','vm_bms')
G.edge['mm-pp-daemon']['vm_bms']['write-read'] = '[open open][write read]'
G.edge['mm-pp-daemon']['vm_bms']['fill'] = 'red'
G.add_edge('mm-pp-daemon','vm_bms')
G.edge['mm-pp-daemon']['vm_bms']['write-read'] = '[open open][write read][append read]'
G.add_edge('mm-pp-daemon','vmwared')
G.edge['mm-pp-daemon']['vmwared']['write-read'] = '[write read]'
G.edge['mm-pp-daemon']['vmwared']['fill'] = 'red'
G.add_edge('mm-pp-daemon','vold')
G.edge['mm-pp-daemon']['vold']['write-read'] = '[open open][write read]'
G.edge['mm-pp-daemon']['vold']['fill'] = 'red'
G.add_edge('mm-pp-daemon','vold')
G.edge['mm-pp-daemon']['vold']['write-read'] = '[open open][write read][append read]'
G.add_edge('mm-pp-daemon','zygote')
G.edge['mm-pp-daemon']['zygote']['write-read'] = '[open open][write read][append read][write read]'
G.edge['mm-pp-daemon']['zygote']['fill'] = 'red'
G.add_edge('mm-qcamera-daemon','at_distributor')
G.edge['mm-qcamera-daemon']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('mm-qcamera-daemon','bauthserver')
G.edge['mm-qcamera-daemon']['bauthserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('mm-qcamera-daemon','bintvoutservice')
G.edge['mm-qcamera-daemon']['bintvoutservice']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('mm-qcamera-daemon','bluetooth')
G.edge['mm-qcamera-daemon']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('mm-qcamera-daemon','cbd')
G.edge['mm-qcamera-daemon']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('mm-qcamera-daemon','cellgeofenced')
G.edge['mm-qcamera-daemon']['cellgeofenced']['write-read'] = '[open open]'
G.add_edge('mm-qcamera-daemon','charger_monitor')
G.edge['mm-qcamera-daemon']['charger_monitor']['write-read'] = '[open open]'
G.add_edge('mm-qcamera-daemon','charger_monitor')
G.edge['mm-qcamera-daemon']['charger_monitor']['write-read'] = '[open open][open open]'
G.add_edge('mm-qcamera-daemon','cnd')
G.edge['mm-qcamera-daemon']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open]'
G.add_edge('mm-qcamera-daemon','connfwexe')
G.edge['mm-qcamera-daemon']['connfwexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('mm-qcamera-daemon','debuggerd')
G.edge['mm-qcamera-daemon']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('mm-qcamera-daemon','diag_uart_log')
G.edge['mm-qcamera-daemon']['diag_uart_log']['write-read'] = '[open open]'
G.add_edge('mm-qcamera-daemon','dumpstate')
G.edge['mm-qcamera-daemon']['dumpstate']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('mm-qcamera-daemon','efsks')
G.edge['mm-qcamera-daemon']['efsks']['write-read'] = '[open open]'
G.add_edge('mm-qcamera-daemon','geomagneticd')
G.edge['mm-qcamera-daemon']['geomagneticd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open]'
G.add_edge('mm-qcamera-daemon','gpsd')
G.edge['mm-qcamera-daemon']['gpsd']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('mm-qcamera-daemon','init_shell')
G.edge['mm-qcamera-daemon']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('mm-qcamera-daemon','kiesexe')
G.edge['mm-qcamera-daemon']['kiesexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('mm-qcamera-daemon','ks')
G.edge['mm-qcamera-daemon']['ks']['write-read'] = '[open open]'
G.add_edge('mm-qcamera-daemon','lhd')
G.edge['mm-qcamera-daemon']['lhd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('mm-qcamera-daemon','lpm')
G.edge['mm-qcamera-daemon']['lpm']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('mm-qcamera-daemon','macloader')
G.edge['mm-qcamera-daemon']['macloader']['write-read'] = '[open open]'
G.add_edge('mm-qcamera-daemon','mdm_helper')
G.edge['mm-qcamera-daemon']['mdm_helper']['write-read'] = '[open open]'
G.add_edge('mm-qcamera-daemon','mediaserver')
G.edge['mm-qcamera-daemon']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('mm-qcamera-daemon','mlexe')
G.edge['mm-qcamera-daemon']['mlexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('mm-qcamera-daemon','mm-pp-daemon')
G.edge['mm-qcamera-daemon']['mm-pp-daemon']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('mm-qcamera-daemon','mm-qcamera-daemon')
G.edge['mm-qcamera-daemon']['mm-qcamera-daemon']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('mm-qcamera-daemon','mpdecision')
G.edge['mm-qcamera-daemon']['mpdecision']['write-read'] = '[open open][write read][add_name search][remove_name search][open open]'
G.add_edge('mm-qcamera-daemon','oneseg_mw')
G.edge['mm-qcamera-daemon']['oneseg_mw']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('mm-qcamera-daemon','qcks')
G.edge['mm-qcamera-daemon']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open]'
G.add_edge('mm-qcamera-daemon','qmuxd')
G.edge['mm-qcamera-daemon']['qmuxd']['write-read'] = '[open open]'
G.add_edge('mm-qcamera-daemon','radio')
G.edge['mm-qcamera-daemon']['radio']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('mm-qcamera-daemon','rild')
G.edge['mm-qcamera-daemon']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('mm-qcamera-daemon','rmt_storage')
G.edge['mm-qcamera-daemon']['rmt_storage']['write-read'] = '[open open]'
G.add_edge('mm-qcamera-daemon','sec-ril')
G.edge['mm-qcamera-daemon']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('mm-qcamera-daemon','smdexe')
G.edge['mm-qcamera-daemon']['smdexe']['write-read'] = '[open open]'
G.add_edge('mm-qcamera-daemon','ssr_setup')
G.edge['mm-qcamera-daemon']['ssr_setup']['write-read'] = '[open open]'
G.add_edge('mm-qcamera-daemon','sswap')
G.edge['mm-qcamera-daemon']['sswap']['write-read'] = '[open open]'
G.add_edge('mm-qcamera-daemon','surfaceflinger')
G.edge['mm-qcamera-daemon']['surfaceflinger']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('mm-qcamera-daemon','system_server')
G.edge['mm-qcamera-daemon']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('mm-qcamera-daemon','system_server')
G.edge['mm-qcamera-daemon']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open]'
G.add_edge('mm-qcamera-daemon','thermal-engine')
G.edge['mm-qcamera-daemon']['thermal-engine']['write-read'] = '[open open]'
G.add_edge('mm-qcamera-daemon','ueventd')
G.edge['mm-qcamera-daemon']['ueventd']['write-read'] = '[open open]'
G.add_edge('mm-qcamera-daemon','vm_bms')
G.edge['mm-qcamera-daemon']['vm_bms']['write-read'] = '[open open]'
G.add_edge('mm-qcamera-daemon','vold')
G.edge['mm-qcamera-daemon']['vold']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('mm-qcamera-daemon','init_shell')
G.edge['mm-qcamera-daemon']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('mm-qcamera-daemon','rild')
G.edge['mm-qcamera-daemon']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('mm-qcamera-daemon','rtcc')
G.edge['mm-qcamera-daemon']['rtcc']['write-read'] = '[setattr getattr]'
G.add_edge('mm-qcamera-daemon','sec-ril')
G.edge['mm-qcamera-daemon']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('mm-qcamera-daemon','system_server')
G.edge['mm-qcamera-daemon']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr]'
G.add_edge('mm-qcamera-daemon','at_distributor')
G.edge['mm-qcamera-daemon']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['mm-qcamera-daemon']['at_distributor']['fill'] = 'red'
G.add_edge('mm-qcamera-daemon','at_distributor')
G.edge['mm-qcamera-daemon']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('mm-qcamera-daemon','bauthserver')
G.edge['mm-qcamera-daemon']['bauthserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['mm-qcamera-daemon']['bauthserver']['fill'] = 'red'
G.add_edge('mm-qcamera-daemon','bauthserver')
G.edge['mm-qcamera-daemon']['bauthserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('mm-qcamera-daemon','bintvoutservice')
G.edge['mm-qcamera-daemon']['bintvoutservice']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['mm-qcamera-daemon']['bintvoutservice']['fill'] = 'red'
G.add_edge('mm-qcamera-daemon','bintvoutservice')
G.edge['mm-qcamera-daemon']['bintvoutservice']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('mm-qcamera-daemon','bluetooth')
G.edge['mm-qcamera-daemon']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['mm-qcamera-daemon']['bluetooth']['fill'] = 'red'
G.add_edge('mm-qcamera-daemon','bluetooth')
G.edge['mm-qcamera-daemon']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('mm-qcamera-daemon','bootanim')
G.edge['mm-qcamera-daemon']['bootanim']['write-read'] = '[open open][write read][append read][write read]'
G.edge['mm-qcamera-daemon']['bootanim']['fill'] = 'red'
G.add_edge('mm-qcamera-daemon','cbd')
G.edge['mm-qcamera-daemon']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['mm-qcamera-daemon']['cbd']['fill'] = 'red'
G.add_edge('mm-qcamera-daemon','cbd')
G.edge['mm-qcamera-daemon']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('mm-qcamera-daemon','cellgeofenced')
G.edge['mm-qcamera-daemon']['cellgeofenced']['write-read'] = '[open open][write read]'
G.edge['mm-qcamera-daemon']['cellgeofenced']['fill'] = 'red'
G.add_edge('mm-qcamera-daemon','cellgeofenced')
G.edge['mm-qcamera-daemon']['cellgeofenced']['write-read'] = '[open open][write read][append read]'
G.add_edge('mm-qcamera-daemon','charger_monitor')
G.edge['mm-qcamera-daemon']['charger_monitor']['write-read'] = '[open open][open open][write read]'
G.edge['mm-qcamera-daemon']['charger_monitor']['fill'] = 'red'
G.add_edge('mm-qcamera-daemon','charger_monitor')
G.edge['mm-qcamera-daemon']['charger_monitor']['write-read'] = '[open open][open open][write read][append read]'
G.add_edge('mm-qcamera-daemon','charger_monitor')
G.edge['mm-qcamera-daemon']['charger_monitor']['write-read'] = '[open open][open open][write read][append read][write read]'
G.edge['mm-qcamera-daemon']['charger_monitor']['fill'] = 'red'
G.add_edge('mm-qcamera-daemon','charger_monitor')
G.edge['mm-qcamera-daemon']['charger_monitor']['write-read'] = '[open open][open open][write read][append read][write read][append read]'
G.add_edge('mm-qcamera-daemon','cnd')
G.edge['mm-qcamera-daemon']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['mm-qcamera-daemon']['cnd']['fill'] = 'red'
G.add_edge('mm-qcamera-daemon','cnd')
G.edge['mm-qcamera-daemon']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('mm-qcamera-daemon','connfwexe')
G.edge['mm-qcamera-daemon']['connfwexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['mm-qcamera-daemon']['connfwexe']['fill'] = 'red'
G.add_edge('mm-qcamera-daemon','connfwexe')
G.edge['mm-qcamera-daemon']['connfwexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('mm-qcamera-daemon','debuggerd')
G.edge['mm-qcamera-daemon']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['mm-qcamera-daemon']['debuggerd']['fill'] = 'red'
G.add_edge('mm-qcamera-daemon','debuggerd')
G.edge['mm-qcamera-daemon']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('mm-qcamera-daemon','diag_uart_log')
G.edge['mm-qcamera-daemon']['diag_uart_log']['write-read'] = '[open open][write read]'
G.edge['mm-qcamera-daemon']['diag_uart_log']['fill'] = 'red'
G.add_edge('mm-qcamera-daemon','diag_uart_log')
G.edge['mm-qcamera-daemon']['diag_uart_log']['write-read'] = '[open open][write read][append read]'
G.add_edge('mm-qcamera-daemon','dumpstate')
G.edge['mm-qcamera-daemon']['dumpstate']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read]'
G.edge['mm-qcamera-daemon']['dumpstate']['fill'] = 'red'
G.add_edge('mm-qcamera-daemon','dumpstate')
G.edge['mm-qcamera-daemon']['dumpstate']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('mm-qcamera-daemon','efsks')
G.edge['mm-qcamera-daemon']['efsks']['write-read'] = '[open open][write read]'
G.edge['mm-qcamera-daemon']['efsks']['fill'] = 'red'
G.add_edge('mm-qcamera-daemon','efsks')
G.edge['mm-qcamera-daemon']['efsks']['write-read'] = '[open open][write read][append read]'
G.add_edge('mm-qcamera-daemon','geomagneticd')
G.edge['mm-qcamera-daemon']['geomagneticd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['mm-qcamera-daemon']['geomagneticd']['fill'] = 'red'
G.add_edge('mm-qcamera-daemon','geomagneticd')
G.edge['mm-qcamera-daemon']['geomagneticd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('mm-qcamera-daemon','gpsd')
G.edge['mm-qcamera-daemon']['gpsd']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read]'
G.edge['mm-qcamera-daemon']['gpsd']['fill'] = 'red'
G.add_edge('mm-qcamera-daemon','gpsd')
G.edge['mm-qcamera-daemon']['gpsd']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('mm-qcamera-daemon','healthd')
G.edge['mm-qcamera-daemon']['healthd']['write-read'] = '[open open][write read][append read][write read]'
G.edge['mm-qcamera-daemon']['healthd']['fill'] = 'red'
G.add_edge('mm-qcamera-daemon','init_shell')
G.edge['mm-qcamera-daemon']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['mm-qcamera-daemon']['init_shell']['fill'] = 'red'
G.add_edge('mm-qcamera-daemon','init_shell')
G.edge['mm-qcamera-daemon']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('mm-qcamera-daemon','jackservice')
G.edge['mm-qcamera-daemon']['jackservice']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['mm-qcamera-daemon']['jackservice']['fill'] = 'red'
G.add_edge('mm-qcamera-daemon','kiesexe')
G.edge['mm-qcamera-daemon']['kiesexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['mm-qcamera-daemon']['kiesexe']['fill'] = 'red'
G.add_edge('mm-qcamera-daemon','kiesexe')
G.edge['mm-qcamera-daemon']['kiesexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('mm-qcamera-daemon','ks')
G.edge['mm-qcamera-daemon']['ks']['write-read'] = '[open open][write read]'
G.edge['mm-qcamera-daemon']['ks']['fill'] = 'red'
G.add_edge('mm-qcamera-daemon','ks')
G.edge['mm-qcamera-daemon']['ks']['write-read'] = '[open open][write read][append read]'
G.add_edge('mm-qcamera-daemon','lhd')
G.edge['mm-qcamera-daemon']['lhd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['mm-qcamera-daemon']['lhd']['fill'] = 'red'
G.add_edge('mm-qcamera-daemon','lhd')
G.edge['mm-qcamera-daemon']['lhd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('mm-qcamera-daemon','lmkd')
G.edge['mm-qcamera-daemon']['lmkd']['write-read'] = '[write read]'
G.edge['mm-qcamera-daemon']['lmkd']['fill'] = 'red'
G.add_edge('mm-qcamera-daemon','lpm')
G.edge['mm-qcamera-daemon']['lpm']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['mm-qcamera-daemon']['lpm']['fill'] = 'red'
G.add_edge('mm-qcamera-daemon','lpm')
G.edge['mm-qcamera-daemon']['lpm']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('mm-qcamera-daemon','macloader')
G.edge['mm-qcamera-daemon']['macloader']['write-read'] = '[open open][write read]'
G.edge['mm-qcamera-daemon']['macloader']['fill'] = 'red'
G.add_edge('mm-qcamera-daemon','macloader')
G.edge['mm-qcamera-daemon']['macloader']['write-read'] = '[open open][write read][append read]'
G.add_edge('mm-qcamera-daemon','mdm_helper')
G.edge['mm-qcamera-daemon']['mdm_helper']['write-read'] = '[open open][write read]'
G.edge['mm-qcamera-daemon']['mdm_helper']['fill'] = 'red'
G.add_edge('mm-qcamera-daemon','mediaserver')
G.edge['mm-qcamera-daemon']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['mm-qcamera-daemon']['mediaserver']['fill'] = 'red'
G.add_edge('mm-qcamera-daemon','mediaserver')
G.edge['mm-qcamera-daemon']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('mm-qcamera-daemon','mfgloader')
G.edge['mm-qcamera-daemon']['mfgloader']['write-read'] = '[open open][write read][add_name search][remove_name search][write read]'
G.edge['mm-qcamera-daemon']['mfgloader']['fill'] = 'red'
G.add_edge('mm-qcamera-daemon','mlexe')
G.edge['mm-qcamera-daemon']['mlexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['mm-qcamera-daemon']['mlexe']['fill'] = 'red'
G.add_edge('mm-qcamera-daemon','mlexe')
G.edge['mm-qcamera-daemon']['mlexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('mm-qcamera-daemon','mm-pp-daemon')
G.edge['mm-qcamera-daemon']['mm-pp-daemon']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['mm-qcamera-daemon']['mm-pp-daemon']['fill'] = 'red'
G.add_edge('mm-qcamera-daemon','mm-pp-daemon')
G.edge['mm-qcamera-daemon']['mm-pp-daemon']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('mm-qcamera-daemon','mm-pp-daemon')
G.edge['mm-qcamera-daemon']['mm-pp-daemon']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read]'
G.edge['mm-qcamera-daemon']['mm-pp-daemon']['fill'] = 'red'
G.add_edge('mm-qcamera-daemon','mm-qcamera-daemon')
G.edge['mm-qcamera-daemon']['mm-qcamera-daemon']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read]'
G.edge['mm-qcamera-daemon']['mm-qcamera-daemon']['fill'] = 'red'
G.add_edge('mm-qcamera-daemon','mm-qcamera-daemon')
G.edge['mm-qcamera-daemon']['mm-qcamera-daemon']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read]'
G.add_edge('mm-qcamera-daemon','mpdecision')
G.edge['mm-qcamera-daemon']['mpdecision']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['mm-qcamera-daemon']['mpdecision']['fill'] = 'red'
G.add_edge('mm-qcamera-daemon','mpdecision')
G.edge['mm-qcamera-daemon']['mpdecision']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('mm-qcamera-daemon','mpdecision')
G.edge['mm-qcamera-daemon']['mpdecision']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read][write read]'
G.edge['mm-qcamera-daemon']['mpdecision']['fill'] = 'red'
G.add_edge('mm-qcamera-daemon','netd')
G.edge['mm-qcamera-daemon']['netd']['write-read'] = '[write read]'
G.edge['mm-qcamera-daemon']['netd']['fill'] = 'red'
G.add_edge('mm-qcamera-daemon','netmgrd')
G.edge['mm-qcamera-daemon']['netmgrd']['write-read'] = '[open open][open open][write read][write read][add_name search][add_name search][remove_name search][write read]'
G.edge['mm-qcamera-daemon']['netmgrd']['fill'] = 'red'
G.add_edge('mm-qcamera-daemon','nfc')
G.edge['mm-qcamera-daemon']['nfc']['write-read'] = '[write read]'
G.edge['mm-qcamera-daemon']['nfc']['fill'] = 'red'
G.add_edge('mm-qcamera-daemon','oneseg_mw')
G.edge['mm-qcamera-daemon']['oneseg_mw']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['mm-qcamera-daemon']['oneseg_mw']['fill'] = 'red'
G.add_edge('mm-qcamera-daemon','oneseg_mw')
G.edge['mm-qcamera-daemon']['oneseg_mw']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('mm-qcamera-daemon','perfd')
G.edge['mm-qcamera-daemon']['perfd']['write-read'] = '[write read]'
G.edge['mm-qcamera-daemon']['perfd']['fill'] = 'red'
G.add_edge('mm-qcamera-daemon','qcks')
G.edge['mm-qcamera-daemon']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['mm-qcamera-daemon']['qcks']['fill'] = 'red'
G.add_edge('mm-qcamera-daemon','qcks')
G.edge['mm-qcamera-daemon']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('mm-qcamera-daemon','qmuxd')
G.edge['mm-qcamera-daemon']['qmuxd']['write-read'] = '[open open][write read]'
G.edge['mm-qcamera-daemon']['qmuxd']['fill'] = 'red'
G.add_edge('mm-qcamera-daemon','qmuxd')
G.edge['mm-qcamera-daemon']['qmuxd']['write-read'] = '[open open][write read][append read]'
G.add_edge('mm-qcamera-daemon','qosmgr')
G.edge['mm-qcamera-daemon']['qosmgr']['write-read'] = '[write read]'
G.edge['mm-qcamera-daemon']['qosmgr']['fill'] = 'red'
G.add_edge('mm-qcamera-daemon','radio')
G.edge['mm-qcamera-daemon']['radio']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][append read]'
G.add_edge('mm-qcamera-daemon','rild')
G.edge['mm-qcamera-daemon']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['mm-qcamera-daemon']['rild']['fill'] = 'red'
G.add_edge('mm-qcamera-daemon','rild')
G.edge['mm-qcamera-daemon']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('mm-qcamera-daemon','rmt_storage')
G.edge['mm-qcamera-daemon']['rmt_storage']['write-read'] = '[open open][write read]'
G.edge['mm-qcamera-daemon']['rmt_storage']['fill'] = 'red'
G.add_edge('mm-qcamera-daemon','rmt_storage')
G.edge['mm-qcamera-daemon']['rmt_storage']['write-read'] = '[open open][write read][append read]'
G.add_edge('mm-qcamera-daemon','rtcc')
G.edge['mm-qcamera-daemon']['rtcc']['write-read'] = '[setattr getattr][write read]'
G.edge['mm-qcamera-daemon']['rtcc']['fill'] = 'red'
G.add_edge('mm-qcamera-daemon','sec-ril')
G.edge['mm-qcamera-daemon']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['mm-qcamera-daemon']['sec-ril']['fill'] = 'red'
G.add_edge('mm-qcamera-daemon','sec-ril')
G.edge['mm-qcamera-daemon']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('mm-qcamera-daemon','sensorhubservice')
G.edge['mm-qcamera-daemon']['sensorhubservice']['write-read'] = '[write read]'
G.edge['mm-qcamera-daemon']['sensorhubservice']['fill'] = 'red'
G.add_edge('mm-qcamera-daemon','smdexe')
G.edge['mm-qcamera-daemon']['smdexe']['write-read'] = '[open open][write read]'
G.edge['mm-qcamera-daemon']['smdexe']['fill'] = 'red'
G.add_edge('mm-qcamera-daemon','smdexe')
G.edge['mm-qcamera-daemon']['smdexe']['write-read'] = '[open open][write read][append read]'
G.add_edge('mm-qcamera-daemon','ssr_setup')
G.edge['mm-qcamera-daemon']['ssr_setup']['write-read'] = '[open open][write read]'
G.edge['mm-qcamera-daemon']['ssr_setup']['fill'] = 'red'
G.add_edge('mm-qcamera-daemon','ssr_setup')
G.edge['mm-qcamera-daemon']['ssr_setup']['write-read'] = '[open open][write read][append read]'
G.add_edge('mm-qcamera-daemon','sswap')
G.edge['mm-qcamera-daemon']['sswap']['write-read'] = '[open open][write read]'
G.edge['mm-qcamera-daemon']['sswap']['fill'] = 'red'
G.add_edge('mm-qcamera-daemon','sswap')
G.edge['mm-qcamera-daemon']['sswap']['write-read'] = '[open open][write read][append read]'
G.add_edge('mm-qcamera-daemon','surfaceflinger')
G.edge['mm-qcamera-daemon']['surfaceflinger']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['mm-qcamera-daemon']['surfaceflinger']['fill'] = 'red'
G.add_edge('mm-qcamera-daemon','surfaceflinger')
G.edge['mm-qcamera-daemon']['surfaceflinger']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('mm-qcamera-daemon','surfaceflinger')
G.edge['mm-qcamera-daemon']['surfaceflinger']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read]'
G.edge['mm-qcamera-daemon']['surfaceflinger']['fill'] = 'red'
G.add_edge('mm-qcamera-daemon','system_server')
G.edge['mm-qcamera-daemon']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read]'
G.edge['mm-qcamera-daemon']['system_server']['fill'] = 'red'
G.add_edge('mm-qcamera-daemon','system_server')
G.edge['mm-qcamera-daemon']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][append read]'
G.add_edge('mm-qcamera-daemon','system_server')
G.edge['mm-qcamera-daemon']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][append read][write read]'
G.edge['mm-qcamera-daemon']['system_server']['fill'] = 'red'
G.add_edge('mm-qcamera-daemon','system_server')
G.edge['mm-qcamera-daemon']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][append read][write read][append read]'
G.add_edge('mm-qcamera-daemon','thermald')
G.edge['mm-qcamera-daemon']['thermald']['write-read'] = '[open open][write read][add_name search][remove_name search][write read]'
G.edge['mm-qcamera-daemon']['thermald']['fill'] = 'red'
G.add_edge('mm-qcamera-daemon','thermal-engine')
G.edge['mm-qcamera-daemon']['thermal-engine']['write-read'] = '[open open][write read]'
G.edge['mm-qcamera-daemon']['thermal-engine']['fill'] = 'red'
G.add_edge('mm-qcamera-daemon','thermal-engine')
G.edge['mm-qcamera-daemon']['thermal-engine']['write-read'] = '[open open][write read][append read]'
G.add_edge('mm-qcamera-daemon','thermal-engine')
G.edge['mm-qcamera-daemon']['thermal-engine']['write-read'] = '[open open][write read][append read][write read]'
G.edge['mm-qcamera-daemon']['thermal-engine']['fill'] = 'red'
G.add_edge('mm-qcamera-daemon','ueventd')
G.edge['mm-qcamera-daemon']['ueventd']['write-read'] = '[open open][write read]'
G.edge['mm-qcamera-daemon']['ueventd']['fill'] = 'red'
G.add_edge('mm-qcamera-daemon','ueventd')
G.edge['mm-qcamera-daemon']['ueventd']['write-read'] = '[open open][write read][append read]'
G.add_edge('mm-qcamera-daemon','vm_bms')
G.edge['mm-qcamera-daemon']['vm_bms']['write-read'] = '[open open][write read]'
G.edge['mm-qcamera-daemon']['vm_bms']['fill'] = 'red'
G.add_edge('mm-qcamera-daemon','vm_bms')
G.edge['mm-qcamera-daemon']['vm_bms']['write-read'] = '[open open][write read][append read]'
G.add_edge('mm-qcamera-daemon','vmwared')
G.edge['mm-qcamera-daemon']['vmwared']['write-read'] = '[write read]'
G.edge['mm-qcamera-daemon']['vmwared']['fill'] = 'red'
G.add_edge('mm-qcamera-daemon','vold')
G.edge['mm-qcamera-daemon']['vold']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read]'
G.edge['mm-qcamera-daemon']['vold']['fill'] = 'red'
G.add_edge('mm-qcamera-daemon','vold')
G.edge['mm-qcamera-daemon']['vold']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('mm-qcamera-daemon','zygote')
G.edge['mm-qcamera-daemon']['zygote']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['mm-qcamera-daemon']['zygote']['fill'] = 'red'
G.add_edge('mpdecision','at_distributor')
G.edge['mpdecision']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('mpdecision','bauthserver')
G.edge['mpdecision']['bauthserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('mpdecision','bintvoutservice')
G.edge['mpdecision']['bintvoutservice']['write-read'] = '[open open]'
G.add_edge('mpdecision','bluetooth')
G.edge['mpdecision']['bluetooth']['write-read'] = '[open open]'
G.add_edge('mpdecision','cbd')
G.edge['mpdecision']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('mpdecision','cellgeofenced')
G.edge['mpdecision']['cellgeofenced']['write-read'] = '[open open]'
G.add_edge('mpdecision','charger_monitor')
G.edge['mpdecision']['charger_monitor']['write-read'] = '[open open]'
G.add_edge('mpdecision','charger_monitor')
G.edge['mpdecision']['charger_monitor']['write-read'] = '[open open][open open]'
G.add_edge('mpdecision','cnd')
G.edge['mpdecision']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open]'
G.add_edge('mpdecision','connfwexe')
G.edge['mpdecision']['connfwexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('mpdecision','debuggerd')
G.edge['mpdecision']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('mpdecision','diag_uart_log')
G.edge['mpdecision']['diag_uart_log']['write-read'] = '[open open]'
G.add_edge('mpdecision','dumpstate')
G.edge['mpdecision']['dumpstate']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('mpdecision','efsks')
G.edge['mpdecision']['efsks']['write-read'] = '[open open]'
G.add_edge('mpdecision','geomagneticd')
G.edge['mpdecision']['geomagneticd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open]'
G.add_edge('mpdecision','gpsd')
G.edge['mpdecision']['gpsd']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('mpdecision','init_shell')
G.edge['mpdecision']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('mpdecision','kiesexe')
G.edge['mpdecision']['kiesexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('mpdecision','ks')
G.edge['mpdecision']['ks']['write-read'] = '[open open]'
G.add_edge('mpdecision','lhd')
G.edge['mpdecision']['lhd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('mpdecision','lpm')
G.edge['mpdecision']['lpm']['write-read'] = '[open open]'
G.add_edge('mpdecision','macloader')
G.edge['mpdecision']['macloader']['write-read'] = '[open open]'
G.add_edge('mpdecision','mdm_helper')
G.edge['mpdecision']['mdm_helper']['write-read'] = '[open open]'
G.add_edge('mpdecision','mediaserver')
G.edge['mpdecision']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('mpdecision','mlexe')
G.edge['mpdecision']['mlexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('mpdecision','mm-pp-daemon')
G.edge['mpdecision']['mm-pp-daemon']['write-read'] = '[open open]'
G.add_edge('mpdecision','mm-qcamera-daemon')
G.edge['mpdecision']['mm-qcamera-daemon']['write-read'] = '[open open][write read][add_name search][remove_name search][open open]'
G.add_edge('mpdecision','mpdecision')
G.edge['mpdecision']['mpdecision']['write-read'] = '[write read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('mpdecision','oneseg_mw')
G.edge['mpdecision']['oneseg_mw']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('mpdecision','qcks')
G.edge['mpdecision']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open]'
G.add_edge('mpdecision','qmuxd')
G.edge['mpdecision']['qmuxd']['write-read'] = '[open open]'
G.add_edge('mpdecision','radio')
G.edge['mpdecision']['radio']['write-read'] = '[open open]'
G.add_edge('mpdecision','rild')
G.edge['mpdecision']['rild']['write-read'] = '[write read][append read][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('mpdecision','rmt_storage')
G.edge['mpdecision']['rmt_storage']['write-read'] = '[open open]'
G.add_edge('mpdecision','sec-ril')
G.edge['mpdecision']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('mpdecision','smdexe')
G.edge['mpdecision']['smdexe']['write-read'] = '[open open]'
G.add_edge('mpdecision','ssr_setup')
G.edge['mpdecision']['ssr_setup']['write-read'] = '[open open]'
G.add_edge('mpdecision','sswap')
G.edge['mpdecision']['sswap']['write-read'] = '[open open]'
G.add_edge('mpdecision','surfaceflinger')
G.edge['mpdecision']['surfaceflinger']['write-read'] = '[write read][append read][write read][append read][open open]'
G.add_edge('mpdecision','system_server')
G.edge['mpdecision']['system_server']['write-read'] = '[write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('mpdecision','system_server')
G.edge['mpdecision']['system_server']['write-read'] = '[write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][open open]'
G.add_edge('mpdecision','thermal-engine')
G.edge['mpdecision']['thermal-engine']['write-read'] = '[write read][open open]'
G.add_edge('mpdecision','ueventd')
G.edge['mpdecision']['ueventd']['write-read'] = '[write read][append read][write read][append read][write read][add_name search][remove_name search][open open]'
G.add_edge('mpdecision','vm_bms')
G.edge['mpdecision']['vm_bms']['write-read'] = '[open open]'
G.add_edge('mpdecision','vold')
G.edge['mpdecision']['vold']['write-read'] = '[write read][append read][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('mpdecision','init_shell')
G.edge['mpdecision']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('mpdecision','rild')
G.edge['mpdecision']['rild']['write-read'] = '[write read][append read][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('mpdecision','rtcc')
G.edge['mpdecision']['rtcc']['write-read'] = '[open open][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('mpdecision','sec-ril')
G.edge['mpdecision']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('mpdecision','system_server')
G.edge['mpdecision']['system_server']['write-read'] = '[write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][open open][setattr getattr]'
G.add_edge('mpdecision','at_distributor')
G.edge['mpdecision']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['mpdecision']['at_distributor']['fill'] = 'red'
G.add_edge('mpdecision','at_distributor')
G.edge['mpdecision']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('mpdecision','bauthserver')
G.edge['mpdecision']['bauthserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['mpdecision']['bauthserver']['fill'] = 'red'
G.add_edge('mpdecision','bauthserver')
G.edge['mpdecision']['bauthserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('mpdecision','bintvoutservice')
G.edge['mpdecision']['bintvoutservice']['write-read'] = '[open open][write read]'
G.edge['mpdecision']['bintvoutservice']['fill'] = 'red'
G.add_edge('mpdecision','bintvoutservice')
G.edge['mpdecision']['bintvoutservice']['write-read'] = '[open open][write read][append read]'
G.add_edge('mpdecision','bluetooth')
G.edge['mpdecision']['bluetooth']['write-read'] = '[open open][write read]'
G.edge['mpdecision']['bluetooth']['fill'] = 'red'
G.add_edge('mpdecision','bluetooth')
G.edge['mpdecision']['bluetooth']['write-read'] = '[open open][write read][append read]'
G.add_edge('mpdecision','bootanim')
G.edge['mpdecision']['bootanim']['write-read'] = '[write read]'
G.edge['mpdecision']['bootanim']['fill'] = 'red'
G.add_edge('mpdecision','cbd')
G.edge['mpdecision']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['mpdecision']['cbd']['fill'] = 'red'
G.add_edge('mpdecision','cbd')
G.edge['mpdecision']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('mpdecision','cellgeofenced')
G.edge['mpdecision']['cellgeofenced']['write-read'] = '[open open][write read]'
G.edge['mpdecision']['cellgeofenced']['fill'] = 'red'
G.add_edge('mpdecision','cellgeofenced')
G.edge['mpdecision']['cellgeofenced']['write-read'] = '[open open][write read][append read]'
G.add_edge('mpdecision','charger_monitor')
G.edge['mpdecision']['charger_monitor']['write-read'] = '[open open][open open][write read]'
G.edge['mpdecision']['charger_monitor']['fill'] = 'red'
G.add_edge('mpdecision','charger_monitor')
G.edge['mpdecision']['charger_monitor']['write-read'] = '[open open][open open][write read][append read]'
G.add_edge('mpdecision','charger_monitor')
G.edge['mpdecision']['charger_monitor']['write-read'] = '[open open][open open][write read][append read][write read]'
G.edge['mpdecision']['charger_monitor']['fill'] = 'red'
G.add_edge('mpdecision','charger_monitor')
G.edge['mpdecision']['charger_monitor']['write-read'] = '[open open][open open][write read][append read][write read][append read]'
G.add_edge('mpdecision','cnd')
G.edge['mpdecision']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['mpdecision']['cnd']['fill'] = 'red'
G.add_edge('mpdecision','cnd')
G.edge['mpdecision']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('mpdecision','connfwexe')
G.edge['mpdecision']['connfwexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['mpdecision']['connfwexe']['fill'] = 'red'
G.add_edge('mpdecision','connfwexe')
G.edge['mpdecision']['connfwexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('mpdecision','debuggerd')
G.edge['mpdecision']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['mpdecision']['debuggerd']['fill'] = 'red'
G.add_edge('mpdecision','debuggerd')
G.edge['mpdecision']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('mpdecision','diag_uart_log')
G.edge['mpdecision']['diag_uart_log']['write-read'] = '[open open][write read]'
G.edge['mpdecision']['diag_uart_log']['fill'] = 'red'
G.add_edge('mpdecision','diag_uart_log')
G.edge['mpdecision']['diag_uart_log']['write-read'] = '[open open][write read][append read]'
G.add_edge('mpdecision','dumpstate')
G.edge['mpdecision']['dumpstate']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read]'
G.edge['mpdecision']['dumpstate']['fill'] = 'red'
G.add_edge('mpdecision','dumpstate')
G.edge['mpdecision']['dumpstate']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('mpdecision','efsks')
G.edge['mpdecision']['efsks']['write-read'] = '[open open][write read]'
G.edge['mpdecision']['efsks']['fill'] = 'red'
G.add_edge('mpdecision','efsks')
G.edge['mpdecision']['efsks']['write-read'] = '[open open][write read][append read]'
G.add_edge('mpdecision','geomagneticd')
G.edge['mpdecision']['geomagneticd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['mpdecision']['geomagneticd']['fill'] = 'red'
G.add_edge('mpdecision','geomagneticd')
G.edge['mpdecision']['geomagneticd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('mpdecision','gpsd')
G.edge['mpdecision']['gpsd']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read]'
G.edge['mpdecision']['gpsd']['fill'] = 'red'
G.add_edge('mpdecision','gpsd')
G.edge['mpdecision']['gpsd']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('mpdecision','healthd')
G.edge['mpdecision']['healthd']['write-read'] = '[write read][append read][write read][append read][write read][add_name search][remove_name search][write read]'
G.edge['mpdecision']['healthd']['fill'] = 'red'
G.add_edge('mpdecision','init_shell')
G.edge['mpdecision']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['mpdecision']['init_shell']['fill'] = 'red'
G.add_edge('mpdecision','init_shell')
G.edge['mpdecision']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('mpdecision','jackservice')
G.edge['mpdecision']['jackservice']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['mpdecision']['jackservice']['fill'] = 'red'
G.add_edge('mpdecision','kiesexe')
G.edge['mpdecision']['kiesexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['mpdecision']['kiesexe']['fill'] = 'red'
G.add_edge('mpdecision','kiesexe')
G.edge['mpdecision']['kiesexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('mpdecision','ks')
G.edge['mpdecision']['ks']['write-read'] = '[open open][write read]'
G.edge['mpdecision']['ks']['fill'] = 'red'
G.add_edge('mpdecision','ks')
G.edge['mpdecision']['ks']['write-read'] = '[open open][write read][append read]'
G.add_edge('mpdecision','lhd')
G.edge['mpdecision']['lhd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['mpdecision']['lhd']['fill'] = 'red'
G.add_edge('mpdecision','lhd')
G.edge['mpdecision']['lhd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('mpdecision','lmkd')
G.edge['mpdecision']['lmkd']['write-read'] = '[write read]'
G.edge['mpdecision']['lmkd']['fill'] = 'red'
G.add_edge('mpdecision','lpm')
G.edge['mpdecision']['lpm']['write-read'] = '[open open][write read]'
G.edge['mpdecision']['lpm']['fill'] = 'red'
G.add_edge('mpdecision','lpm')
G.edge['mpdecision']['lpm']['write-read'] = '[open open][write read][append read]'
G.add_edge('mpdecision','macloader')
G.edge['mpdecision']['macloader']['write-read'] = '[open open][write read]'
G.edge['mpdecision']['macloader']['fill'] = 'red'
G.add_edge('mpdecision','macloader')
G.edge['mpdecision']['macloader']['write-read'] = '[open open][write read][append read]'
G.add_edge('mpdecision','mdm_helper')
G.edge['mpdecision']['mdm_helper']['write-read'] = '[open open][write read]'
G.edge['mpdecision']['mdm_helper']['fill'] = 'red'
G.add_edge('mpdecision','mediaserver')
G.edge['mpdecision']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['mpdecision']['mediaserver']['fill'] = 'red'
G.add_edge('mpdecision','mediaserver')
G.edge['mpdecision']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('mpdecision','mfgloader')
G.edge['mpdecision']['mfgloader']['write-read'] = '[open open][write read][add_name search][remove_name search][write read]'
G.edge['mpdecision']['mfgloader']['fill'] = 'red'
G.add_edge('mpdecision','mlexe')
G.edge['mpdecision']['mlexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['mpdecision']['mlexe']['fill'] = 'red'
G.add_edge('mpdecision','mlexe')
G.edge['mpdecision']['mlexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('mpdecision','mm-pp-daemon')
G.edge['mpdecision']['mm-pp-daemon']['write-read'] = '[open open][write read]'
G.edge['mpdecision']['mm-pp-daemon']['fill'] = 'red'
G.add_edge('mpdecision','mm-pp-daemon')
G.edge['mpdecision']['mm-pp-daemon']['write-read'] = '[open open][write read][append read]'
G.add_edge('mpdecision','mm-pp-daemon')
G.edge['mpdecision']['mm-pp-daemon']['write-read'] = '[open open][write read][append read][write read]'
G.edge['mpdecision']['mm-pp-daemon']['fill'] = 'red'
G.add_edge('mpdecision','mm-qcamera-daemon')
G.edge['mpdecision']['mm-qcamera-daemon']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['mpdecision']['mm-qcamera-daemon']['fill'] = 'red'
G.add_edge('mpdecision','mm-qcamera-daemon')
G.edge['mpdecision']['mm-qcamera-daemon']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('mpdecision','mpdecision')
G.edge['mpdecision']['mpdecision']['write-read'] = '[write read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['mpdecision']['mpdecision']['fill'] = 'red'
G.add_edge('mpdecision','mpdecision')
G.edge['mpdecision']['mpdecision']['write-read'] = '[write read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('mpdecision','mpdecision')
G.edge['mpdecision']['mpdecision']['write-read'] = '[write read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][write read]'
G.edge['mpdecision']['mpdecision']['fill'] = 'red'
G.add_edge('mpdecision','netd')
G.edge['mpdecision']['netd']['write-read'] = '[write read][append read][write read][append read][write read]'
G.edge['mpdecision']['netd']['fill'] = 'red'
G.add_edge('mpdecision','netmgrd')
G.edge['mpdecision']['netmgrd']['write-read'] = '[open open][open open][write read][write read][add_name search][add_name search][remove_name search][write read]'
G.edge['mpdecision']['netmgrd']['fill'] = 'red'
G.add_edge('mpdecision','nfc')
G.edge['mpdecision']['nfc']['write-read'] = '[write read]'
G.edge['mpdecision']['nfc']['fill'] = 'red'
G.add_edge('mpdecision','oneseg_mw')
G.edge['mpdecision']['oneseg_mw']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['mpdecision']['oneseg_mw']['fill'] = 'red'
G.add_edge('mpdecision','oneseg_mw')
G.edge['mpdecision']['oneseg_mw']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('mpdecision','perfd')
G.edge['mpdecision']['perfd']['write-read'] = '[write read]'
G.edge['mpdecision']['perfd']['fill'] = 'red'
G.add_edge('mpdecision','qcks')
G.edge['mpdecision']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['mpdecision']['qcks']['fill'] = 'red'
G.add_edge('mpdecision','qcks')
G.edge['mpdecision']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('mpdecision','qmuxd')
G.edge['mpdecision']['qmuxd']['write-read'] = '[open open][write read]'
G.edge['mpdecision']['qmuxd']['fill'] = 'red'
G.add_edge('mpdecision','qmuxd')
G.edge['mpdecision']['qmuxd']['write-read'] = '[open open][write read][append read]'
G.add_edge('mpdecision','qosmgr')
G.edge['mpdecision']['qosmgr']['write-read'] = '[write read]'
G.edge['mpdecision']['qosmgr']['fill'] = 'red'
G.add_edge('mpdecision','radio')
G.edge['mpdecision']['radio']['write-read'] = '[open open][append read]'
G.add_edge('mpdecision','rild')
G.edge['mpdecision']['rild']['write-read'] = '[write read][append read][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['mpdecision']['rild']['fill'] = 'red'
G.add_edge('mpdecision','rild')
G.edge['mpdecision']['rild']['write-read'] = '[write read][append read][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('mpdecision','rmt_storage')
G.edge['mpdecision']['rmt_storage']['write-read'] = '[open open][write read]'
G.edge['mpdecision']['rmt_storage']['fill'] = 'red'
G.add_edge('mpdecision','rmt_storage')
G.edge['mpdecision']['rmt_storage']['write-read'] = '[open open][write read][append read]'
G.add_edge('mpdecision','rtcc')
G.edge['mpdecision']['rtcc']['write-read'] = '[open open][write read][add_name search][remove_name search][setattr getattr][write read]'
G.edge['mpdecision']['rtcc']['fill'] = 'red'
G.add_edge('mpdecision','sec-ril')
G.edge['mpdecision']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['mpdecision']['sec-ril']['fill'] = 'red'
G.add_edge('mpdecision','sec-ril')
G.edge['mpdecision']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('mpdecision','sensorhubservice')
G.edge['mpdecision']['sensorhubservice']['write-read'] = '[write read]'
G.edge['mpdecision']['sensorhubservice']['fill'] = 'red'
G.add_edge('mpdecision','smdexe')
G.edge['mpdecision']['smdexe']['write-read'] = '[open open][write read]'
G.edge['mpdecision']['smdexe']['fill'] = 'red'
G.add_edge('mpdecision','smdexe')
G.edge['mpdecision']['smdexe']['write-read'] = '[open open][write read][append read]'
G.add_edge('mpdecision','ssr_setup')
G.edge['mpdecision']['ssr_setup']['write-read'] = '[open open][write read]'
G.edge['mpdecision']['ssr_setup']['fill'] = 'red'
G.add_edge('mpdecision','ssr_setup')
G.edge['mpdecision']['ssr_setup']['write-read'] = '[open open][write read][append read]'
G.add_edge('mpdecision','sswap')
G.edge['mpdecision']['sswap']['write-read'] = '[open open][write read]'
G.edge['mpdecision']['sswap']['fill'] = 'red'
G.add_edge('mpdecision','sswap')
G.edge['mpdecision']['sswap']['write-read'] = '[open open][write read][append read]'
G.add_edge('mpdecision','surfaceflinger')
G.edge['mpdecision']['surfaceflinger']['write-read'] = '[write read][append read][write read][append read][open open][write read]'
G.edge['mpdecision']['surfaceflinger']['fill'] = 'red'
G.add_edge('mpdecision','surfaceflinger')
G.edge['mpdecision']['surfaceflinger']['write-read'] = '[write read][append read][write read][append read][open open][write read][append read]'
G.add_edge('mpdecision','surfaceflinger')
G.edge['mpdecision']['surfaceflinger']['write-read'] = '[write read][append read][write read][append read][open open][write read][append read][write read]'
G.edge['mpdecision']['surfaceflinger']['fill'] = 'red'
G.add_edge('mpdecision','system_server')
G.edge['mpdecision']['system_server']['write-read'] = '[write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][open open][setattr getattr][write read]'
G.edge['mpdecision']['system_server']['fill'] = 'red'
G.add_edge('mpdecision','system_server')
G.edge['mpdecision']['system_server']['write-read'] = '[write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][open open][setattr getattr][write read][append read]'
G.add_edge('mpdecision','system_server')
G.edge['mpdecision']['system_server']['write-read'] = '[write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][open open][setattr getattr][write read][append read][write read]'
G.edge['mpdecision']['system_server']['fill'] = 'red'
G.add_edge('mpdecision','system_server')
G.edge['mpdecision']['system_server']['write-read'] = '[write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read]'
G.add_edge('mpdecision','thermald')
G.edge['mpdecision']['thermald']['write-read'] = '[open open][write read][add_name search][remove_name search][write read]'
G.edge['mpdecision']['thermald']['fill'] = 'red'
G.add_edge('mpdecision','thermal-engine')
G.edge['mpdecision']['thermal-engine']['write-read'] = '[write read][open open][write read]'
G.edge['mpdecision']['thermal-engine']['fill'] = 'red'
G.add_edge('mpdecision','thermal-engine')
G.edge['mpdecision']['thermal-engine']['write-read'] = '[write read][open open][write read][append read]'
G.add_edge('mpdecision','thermal-engine')
G.edge['mpdecision']['thermal-engine']['write-read'] = '[write read][open open][write read][append read][write read]'
G.edge['mpdecision']['thermal-engine']['fill'] = 'red'
G.add_edge('mpdecision','ueventd')
G.edge['mpdecision']['ueventd']['write-read'] = '[write read][append read][write read][append read][write read][add_name search][remove_name search][open open][write read]'
G.edge['mpdecision']['ueventd']['fill'] = 'red'
G.add_edge('mpdecision','ueventd')
G.edge['mpdecision']['ueventd']['write-read'] = '[write read][append read][write read][append read][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('mpdecision','vm_bms')
G.edge['mpdecision']['vm_bms']['write-read'] = '[open open][write read]'
G.edge['mpdecision']['vm_bms']['fill'] = 'red'
G.add_edge('mpdecision','vm_bms')
G.edge['mpdecision']['vm_bms']['write-read'] = '[open open][write read][append read]'
G.add_edge('mpdecision','vmwared')
G.edge['mpdecision']['vmwared']['write-read'] = '[write read]'
G.edge['mpdecision']['vmwared']['fill'] = 'red'
G.add_edge('mpdecision','vold')
G.edge['mpdecision']['vold']['write-read'] = '[write read][append read][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read]'
G.edge['mpdecision']['vold']['fill'] = 'red'
G.add_edge('mpdecision','vold')
G.edge['mpdecision']['vold']['write-read'] = '[write read][append read][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('mpdecision','zygote')
G.edge['mpdecision']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['mpdecision']['zygote']['fill'] = 'red'
G.add_edge('rild','at_distributor')
G.edge['rild']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open]'
G.add_edge('rild','bauthserver')
G.edge['rild']['bauthserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open]'
G.add_edge('rild','bintvoutservice')
G.edge['rild']['bintvoutservice']['write-read'] = '[open open]'
G.add_edge('rild','bluetooth')
G.edge['rild']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('rild','cbd')
G.edge['rild']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('rild','cellgeofenced')
G.edge['rild']['cellgeofenced']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('rild','charger_monitor')
G.edge['rild']['charger_monitor']['write-read'] = '[setopt getopt][open open][write read][append read][open open]'
G.add_edge('rild','charger_monitor')
G.edge['rild']['charger_monitor']['write-read'] = '[setopt getopt][open open][write read][append read][open open][open open]'
G.add_edge('rild','cnd')
G.edge['rild']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][append read][open open]'
G.add_edge('rild','connfwexe')
G.edge['rild']['connfwexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('rild','debuggerd')
G.edge['rild']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('rild','diag_uart_log')
G.edge['rild']['diag_uart_log']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('rild','dumpstate')
G.edge['rild']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('rild','efsks')
G.edge['rild']['efsks']['write-read'] = '[open open][write read][add_name search][open open]'
G.add_edge('rild','geomagneticd')
G.edge['rild']['geomagneticd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open]'
G.add_edge('rild','gpsd')
G.edge['rild']['gpsd']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('rild','init_shell')
G.edge['rild']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('rild','kiesexe')
G.edge['rild']['kiesexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open]'
G.add_edge('rild','ks')
G.edge['rild']['ks']['write-read'] = '[open open][write read][add_name search][open open][append read][open open]'
G.add_edge('rild','lhd')
G.edge['rild']['lhd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('rild','lpm')
G.edge['rild']['lpm']['write-read'] = '[setopt getopt][open open]'
G.add_edge('rild','macloader')
G.edge['rild']['macloader']['write-read'] = '[open open]'
G.add_edge('rild','mdm_helper')
G.edge['rild']['mdm_helper']['write-read'] = '[write read][open open][append read][open open]'
G.add_edge('rild','mediaserver')
G.edge['rild']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('rild','mlexe')
G.edge['rild']['mlexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open]'
G.add_edge('rild','mm-pp-daemon')
G.edge['rild']['mm-pp-daemon']['write-read'] = '[open open]'
G.add_edge('rild','mm-qcamera-daemon')
G.edge['rild']['mm-qcamera-daemon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open]'
G.add_edge('rild','mpdecision')
G.edge['rild']['mpdecision']['write-read'] = '[setopt getopt][setopt getopt][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('rild','oneseg_mw')
G.edge['rild']['oneseg_mw']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('rild','qcks')
G.edge['rild']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][append read][open open]'
G.add_edge('rild','qmuxd')
G.edge['rild']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][open open][append read][write read][append read][open open]'
G.add_edge('rild','radio')
G.edge['rild']['radio']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('rild','rild')
G.edge['rild']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][open open][setattr getattr][write read][append read][write read][append read][write read][append read][open open][open open][open open][setattr getattr][write read][append read][write read][append read][write read][append read][open open][write read][append read][open open]'
G.add_edge('rild','rmt_storage')
G.edge['rild']['rmt_storage']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('rild','sec-ril')
G.edge['rild']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][add_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][open open]'
G.add_edge('rild','smdexe')
G.edge['rild']['smdexe']['write-read'] = '[open open]'
G.add_edge('rild','ssr_setup')
G.edge['rild']['ssr_setup']['write-read'] = '[open open]'
G.add_edge('rild','sswap')
G.edge['rild']['sswap']['write-read'] = '[open open]'
G.add_edge('rild','surfaceflinger')
G.edge['rild']['surfaceflinger']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open]'
G.add_edge('rild','system_server')
G.edge['rild']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('rild','system_server')
G.edge['rild']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][open open]'
G.add_edge('rild','thermal-engine')
G.edge['rild']['thermal-engine']['write-read'] = '[setopt getopt][open open]'
G.add_edge('rild','ueventd')
G.edge['rild']['ueventd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][write read][add_name search][remove_name search][open open]'
G.add_edge('rild','vm_bms')
G.edge['rild']['vm_bms']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('rild','vold')
G.edge['rild']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('rild','init_shell')
G.edge['rild']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('rild','rild')
G.edge['rild']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][open open][setattr getattr][write read][append read][write read][append read][write read][append read][open open][open open][open open][setattr getattr][write read][append read][write read][append read][write read][append read][open open][write read][append read][open open][setattr getattr]'
G.add_edge('rild','rtcc')
G.edge['rild']['rtcc']['write-read'] = '[open open][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('rild','sec-ril')
G.edge['rild']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][add_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][open open][setattr getattr]'
G.add_edge('rild','system_server')
G.edge['rild']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][open open][setattr getattr]'
G.add_edge('rild','at_distributor')
G.edge['rild']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read]'
G.edge['rild']['at_distributor']['fill'] = 'red'
G.add_edge('rild','at_distributor')
G.edge['rild']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read]'
G.add_edge('rild','bauthserver')
G.edge['rild']['bauthserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read]'
G.edge['rild']['bauthserver']['fill'] = 'red'
G.add_edge('rild','bauthserver')
G.edge['rild']['bauthserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('rild','bintvoutservice')
G.edge['rild']['bintvoutservice']['write-read'] = '[open open][write read]'
G.edge['rild']['bintvoutservice']['fill'] = 'red'
G.add_edge('rild','bintvoutservice')
G.edge['rild']['bintvoutservice']['write-read'] = '[open open][write read][append read]'
G.add_edge('rild','bluetooth')
G.edge['rild']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read]'
G.edge['rild']['bluetooth']['fill'] = 'red'
G.add_edge('rild','bluetooth')
G.edge['rild']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read]'
G.add_edge('rild','bootanim')
G.edge['rild']['bootanim']['write-read'] = '[write read]'
G.edge['rild']['bootanim']['fill'] = 'red'
G.add_edge('rild','cbd')
G.edge['rild']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['rild']['cbd']['fill'] = 'red'
G.add_edge('rild','cbd')
G.edge['rild']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('rild','cellgeofenced')
G.edge['rild']['cellgeofenced']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['rild']['cellgeofenced']['fill'] = 'red'
G.add_edge('rild','cellgeofenced')
G.edge['rild']['cellgeofenced']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('rild','charger_monitor')
G.edge['rild']['charger_monitor']['write-read'] = '[setopt getopt][open open][write read][append read][open open][open open][write read]'
G.edge['rild']['charger_monitor']['fill'] = 'red'
G.add_edge('rild','charger_monitor')
G.edge['rild']['charger_monitor']['write-read'] = '[setopt getopt][open open][write read][append read][open open][open open][write read][append read]'
G.add_edge('rild','charger_monitor')
G.edge['rild']['charger_monitor']['write-read'] = '[setopt getopt][open open][write read][append read][open open][open open][write read][append read][write read]'
G.edge['rild']['charger_monitor']['fill'] = 'red'
G.add_edge('rild','charger_monitor')
G.edge['rild']['charger_monitor']['write-read'] = '[setopt getopt][open open][write read][append read][open open][open open][write read][append read][write read][append read]'
G.add_edge('rild','cnd')
G.edge['rild']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][append read][open open][write read]'
G.edge['rild']['cnd']['fill'] = 'red'
G.add_edge('rild','cnd')
G.edge['rild']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][append read][open open][write read][append read]'
G.add_edge('rild','connfwexe')
G.edge['rild']['connfwexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read][append read][open open][write read]'
G.edge['rild']['connfwexe']['fill'] = 'red'
G.add_edge('rild','connfwexe')
G.edge['rild']['connfwexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read][append read][open open][write read][append read]'
G.add_edge('rild','debuggerd')
G.edge['rild']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['rild']['debuggerd']['fill'] = 'red'
G.add_edge('rild','debuggerd')
G.edge['rild']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('rild','diag_uart_log')
G.edge['rild']['diag_uart_log']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['rild']['diag_uart_log']['fill'] = 'red'
G.add_edge('rild','diag_uart_log')
G.edge['rild']['diag_uart_log']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('rild','dumpstate')
G.edge['rild']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['rild']['dumpstate']['fill'] = 'red'
G.add_edge('rild','dumpstate')
G.edge['rild']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('rild','efsks')
G.edge['rild']['efsks']['write-read'] = '[open open][write read][add_name search][open open][write read]'
G.edge['rild']['efsks']['fill'] = 'red'
G.add_edge('rild','efsks')
G.edge['rild']['efsks']['write-read'] = '[open open][write read][add_name search][open open][write read][append read]'
G.add_edge('rild','geomagneticd')
G.edge['rild']['geomagneticd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read]'
G.edge['rild']['geomagneticd']['fill'] = 'red'
G.add_edge('rild','geomagneticd')
G.edge['rild']['geomagneticd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('rild','gpsd')
G.edge['rild']['gpsd']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['rild']['gpsd']['fill'] = 'red'
G.add_edge('rild','gpsd')
G.edge['rild']['gpsd']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('rild','healthd')
G.edge['rild']['healthd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][write read][add_name search][remove_name search][open open][write read][append read][write read]'
G.edge['rild']['healthd']['fill'] = 'red'
G.add_edge('rild','init_shell')
G.edge['rild']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['rild']['init_shell']['fill'] = 'red'
G.add_edge('rild','init_shell')
G.edge['rild']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('rild','jackservice')
G.edge['rild']['jackservice']['write-read'] = '[add_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['rild']['jackservice']['fill'] = 'red'
G.add_edge('rild','kiesexe')
G.edge['rild']['kiesexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read]'
G.edge['rild']['kiesexe']['fill'] = 'red'
G.add_edge('rild','kiesexe')
G.edge['rild']['kiesexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('rild','ks')
G.edge['rild']['ks']['write-read'] = '[open open][write read][add_name search][open open][append read][open open][write read]'
G.edge['rild']['ks']['fill'] = 'red'
G.add_edge('rild','ks')
G.edge['rild']['ks']['write-read'] = '[open open][write read][add_name search][open open][append read][open open][write read][append read]'
G.add_edge('rild','lhd')
G.edge['rild']['lhd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read][append read][open open][write read]'
G.edge['rild']['lhd']['fill'] = 'red'
G.add_edge('rild','lhd')
G.edge['rild']['lhd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read][append read][open open][write read][append read]'
G.add_edge('rild','lmkd')
G.edge['rild']['lmkd']['write-read'] = '[remove_name search][write read]'
G.edge['rild']['lmkd']['fill'] = 'red'
G.add_edge('rild','lpm')
G.edge['rild']['lpm']['write-read'] = '[setopt getopt][open open][write read]'
G.edge['rild']['lpm']['fill'] = 'red'
G.add_edge('rild','lpm')
G.edge['rild']['lpm']['write-read'] = '[setopt getopt][open open][write read][append read]'
G.add_edge('rild','macloader')
G.edge['rild']['macloader']['write-read'] = '[open open][write read]'
G.edge['rild']['macloader']['fill'] = 'red'
G.add_edge('rild','macloader')
G.edge['rild']['macloader']['write-read'] = '[open open][write read][append read]'
G.add_edge('rild','mdm_helper')
G.edge['rild']['mdm_helper']['write-read'] = '[write read][open open][append read][open open][write read]'
G.edge['rild']['mdm_helper']['fill'] = 'red'
G.add_edge('rild','mediaserver')
G.edge['rild']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read]'
G.edge['rild']['mediaserver']['fill'] = 'red'
G.add_edge('rild','mediaserver')
G.edge['rild']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read]'
G.add_edge('rild','mfgloader')
G.edge['rild']['mfgloader']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read]'
G.edge['rild']['mfgloader']['fill'] = 'red'
G.add_edge('rild','mlexe')
G.edge['rild']['mlexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read]'
G.edge['rild']['mlexe']['fill'] = 'red'
G.add_edge('rild','mlexe')
G.edge['rild']['mlexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('rild','mm-pp-daemon')
G.edge['rild']['mm-pp-daemon']['write-read'] = '[open open][write read]'
G.edge['rild']['mm-pp-daemon']['fill'] = 'red'
G.add_edge('rild','mm-pp-daemon')
G.edge['rild']['mm-pp-daemon']['write-read'] = '[open open][write read][append read]'
G.add_edge('rild','mm-pp-daemon')
G.edge['rild']['mm-pp-daemon']['write-read'] = '[open open][write read][append read][write read]'
G.edge['rild']['mm-pp-daemon']['fill'] = 'red'
G.add_edge('rild','mm-qcamera-daemon')
G.edge['rild']['mm-qcamera-daemon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read]'
G.edge['rild']['mm-qcamera-daemon']['fill'] = 'red'
G.add_edge('rild','mm-qcamera-daemon')
G.edge['rild']['mm-qcamera-daemon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('rild','mpdecision')
G.edge['rild']['mpdecision']['write-read'] = '[setopt getopt][setopt getopt][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['rild']['mpdecision']['fill'] = 'red'
G.add_edge('rild','mpdecision')
G.edge['rild']['mpdecision']['write-read'] = '[setopt getopt][setopt getopt][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('rild','mpdecision')
G.edge['rild']['mpdecision']['write-read'] = '[setopt getopt][setopt getopt][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read][write read]'
G.edge['rild']['mpdecision']['fill'] = 'red'
G.add_edge('rild','netd')
G.edge['rild']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['rild']['netd']['fill'] = 'red'
G.add_edge('rild','netmgrd')
G.edge['rild']['netmgrd']['write-read'] = '[open open][open open][write read][write read][add_name search][add_name search][remove_name search][open open][open open][write read][write read][add_name search][add_name search][remove_name search][open open][open open][add_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['rild']['netmgrd']['fill'] = 'red'
G.add_edge('rild','nfc')
G.edge['rild']['nfc']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['rild']['nfc']['fill'] = 'red'
G.add_edge('rild','oneseg_mw')
G.edge['rild']['oneseg_mw']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['rild']['oneseg_mw']['fill'] = 'red'
G.add_edge('rild','oneseg_mw')
G.edge['rild']['oneseg_mw']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('rild','perfd')
G.edge['rild']['perfd']['write-read'] = '[setopt getopt][write read]'
G.edge['rild']['perfd']['fill'] = 'red'
G.add_edge('rild','qcks')
G.edge['rild']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][append read][open open][write read]'
G.edge['rild']['qcks']['fill'] = 'red'
G.add_edge('rild','qcks')
G.edge['rild']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][append read][open open][write read][append read]'
G.add_edge('rild','qmuxd')
G.edge['rild']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][open open][append read][write read][append read][open open][write read]'
G.edge['rild']['qmuxd']['fill'] = 'red'
G.add_edge('rild','qmuxd')
G.edge['rild']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][open open][append read][write read][append read][open open][write read][append read]'
G.add_edge('rild','qosmgr')
G.edge['rild']['qosmgr']['write-read'] = '[write read]'
G.edge['rild']['qosmgr']['fill'] = 'red'
G.add_edge('rild','radio')
G.edge['rild']['radio']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][append read]'
G.add_edge('rild','rild')
G.edge['rild']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][open open][setattr getattr][write read][append read][write read][append read][write read][append read][open open][open open][open open][setattr getattr][write read][append read][write read][append read][write read][append read][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['rild']['rild']['fill'] = 'red'
G.add_edge('rild','rild')
G.edge['rild']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][open open][setattr getattr][write read][append read][write read][append read][write read][append read][open open][open open][open open][setattr getattr][write read][append read][write read][append read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('rild','rmt_storage')
G.edge['rild']['rmt_storage']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read]'
G.edge['rild']['rmt_storage']['fill'] = 'red'
G.add_edge('rild','rmt_storage')
G.edge['rild']['rmt_storage']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read]'
G.add_edge('rild','rtcc')
G.edge['rild']['rtcc']['write-read'] = '[open open][write read][add_name search][remove_name search][setattr getattr][write read]'
G.edge['rild']['rtcc']['fill'] = 'red'
G.add_edge('rild','sec-ril')
G.edge['rild']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][add_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][open open][setattr getattr][write read]'
G.edge['rild']['sec-ril']['fill'] = 'red'
G.add_edge('rild','sec-ril')
G.edge['rild']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][add_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][open open][setattr getattr][write read][append read]'
G.add_edge('rild','sensorhubservice')
G.edge['rild']['sensorhubservice']['write-read'] = '[write read]'
G.edge['rild']['sensorhubservice']['fill'] = 'red'
G.add_edge('rild','smdexe')
G.edge['rild']['smdexe']['write-read'] = '[open open][write read]'
G.edge['rild']['smdexe']['fill'] = 'red'
G.add_edge('rild','smdexe')
G.edge['rild']['smdexe']['write-read'] = '[open open][write read][append read]'
G.add_edge('rild','ssr_setup')
G.edge['rild']['ssr_setup']['write-read'] = '[open open][write read]'
G.edge['rild']['ssr_setup']['fill'] = 'red'
G.add_edge('rild','ssr_setup')
G.edge['rild']['ssr_setup']['write-read'] = '[open open][write read][append read]'
G.add_edge('rild','sswap')
G.edge['rild']['sswap']['write-read'] = '[open open][write read]'
G.edge['rild']['sswap']['fill'] = 'red'
G.add_edge('rild','sswap')
G.edge['rild']['sswap']['write-read'] = '[open open][write read][append read]'
G.add_edge('rild','surfaceflinger')
G.edge['rild']['surfaceflinger']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][write read]'
G.edge['rild']['surfaceflinger']['fill'] = 'red'
G.add_edge('rild','surfaceflinger')
G.edge['rild']['surfaceflinger']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][write read][append read]'
G.add_edge('rild','surfaceflinger')
G.edge['rild']['surfaceflinger']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][write read][append read][write read]'
G.edge['rild']['surfaceflinger']['fill'] = 'red'
G.add_edge('rild','system_server')
G.edge['rild']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][open open][setattr getattr][write read]'
G.edge['rild']['system_server']['fill'] = 'red'
G.add_edge('rild','system_server')
G.edge['rild']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][open open][setattr getattr][write read][append read]'
G.add_edge('rild','system_server')
G.edge['rild']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][open open][setattr getattr][write read][append read][write read]'
G.edge['rild']['system_server']['fill'] = 'red'
G.add_edge('rild','system_server')
G.edge['rild']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read]'
G.add_edge('rild','thermald')
G.edge['rild']['thermald']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read]'
G.edge['rild']['thermald']['fill'] = 'red'
G.add_edge('rild','thermal-engine')
G.edge['rild']['thermal-engine']['write-read'] = '[setopt getopt][open open][write read]'
G.edge['rild']['thermal-engine']['fill'] = 'red'
G.add_edge('rild','thermal-engine')
G.edge['rild']['thermal-engine']['write-read'] = '[setopt getopt][open open][write read][append read]'
G.add_edge('rild','thermal-engine')
G.edge['rild']['thermal-engine']['write-read'] = '[setopt getopt][open open][write read][append read][write read]'
G.edge['rild']['thermal-engine']['fill'] = 'red'
G.add_edge('rild','ueventd')
G.edge['rild']['ueventd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][write read][add_name search][remove_name search][open open][write read]'
G.edge['rild']['ueventd']['fill'] = 'red'
G.add_edge('rild','ueventd')
G.edge['rild']['ueventd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('rild','vm_bms')
G.edge['rild']['vm_bms']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['rild']['vm_bms']['fill'] = 'red'
G.add_edge('rild','vm_bms')
G.edge['rild']['vm_bms']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('rild','vmwared')
G.edge['rild']['vmwared']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['rild']['vmwared']['fill'] = 'red'
G.add_edge('rild','vold')
G.edge['rild']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read]'
G.edge['rild']['vold']['fill'] = 'red'
G.add_edge('rild','vold')
G.edge['rild']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read]'
G.add_edge('rild','zygote')
G.edge['rild']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['rild']['zygote']['fill'] = 'red'
G.add_edge('sec-ril','at_distributor')
G.edge['sec-ril']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open]'
G.add_edge('sec-ril','bauthserver')
G.edge['sec-ril']['bauthserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('sec-ril','bintvoutservice')
G.edge['sec-ril']['bintvoutservice']['write-read'] = '[open open]'
G.add_edge('sec-ril','bluetooth')
G.edge['sec-ril']['bluetooth']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('sec-ril','cbd')
G.edge['sec-ril']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('sec-ril','cellgeofenced')
G.edge['sec-ril']['cellgeofenced']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('sec-ril','charger_monitor')
G.edge['sec-ril']['charger_monitor']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('sec-ril','charger_monitor')
G.edge['sec-ril']['charger_monitor']['write-read'] = '[open open][write read][append read][open open][open open]'
G.add_edge('sec-ril','cnd')
G.edge['sec-ril']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][append read][open open]'
G.add_edge('sec-ril','connfwexe')
G.edge['sec-ril']['connfwexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('sec-ril','debuggerd')
G.edge['sec-ril']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('sec-ril','diag_uart_log')
G.edge['sec-ril']['diag_uart_log']['write-read'] = '[open open]'
G.add_edge('sec-ril','dumpstate')
G.edge['sec-ril']['dumpstate']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('sec-ril','efsks')
G.edge['sec-ril']['efsks']['write-read'] = '[open open]'
G.add_edge('sec-ril','geomagneticd')
G.edge['sec-ril']['geomagneticd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open]'
G.add_edge('sec-ril','gpsd')
G.edge['sec-ril']['gpsd']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('sec-ril','init_shell')
G.edge['sec-ril']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open]'
G.add_edge('sec-ril','kiesexe')
G.edge['sec-ril']['kiesexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('sec-ril','ks')
G.edge['sec-ril']['ks']['write-read'] = '[open open][append read][open open]'
G.add_edge('sec-ril','lhd')
G.edge['sec-ril']['lhd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('sec-ril','lpm')
G.edge['sec-ril']['lpm']['write-read'] = '[open open]'
G.add_edge('sec-ril','macloader')
G.edge['sec-ril']['macloader']['write-read'] = '[open open]'
G.add_edge('sec-ril','mdm_helper')
G.edge['sec-ril']['mdm_helper']['write-read'] = '[open open][append read][open open]'
G.add_edge('sec-ril','mediaserver')
G.edge['sec-ril']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('sec-ril','mlexe')
G.edge['sec-ril']['mlexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('sec-ril','mm-pp-daemon')
G.edge['sec-ril']['mm-pp-daemon']['write-read'] = '[open open]'
G.add_edge('sec-ril','mm-qcamera-daemon')
G.edge['sec-ril']['mm-qcamera-daemon']['write-read'] = '[open open][write read][add_name search][remove_name search][open open]'
G.add_edge('sec-ril','mpdecision')
G.edge['sec-ril']['mpdecision']['write-read'] = '[open open][write read][add_name search][remove_name search][open open]'
G.add_edge('sec-ril','oneseg_mw')
G.edge['sec-ril']['oneseg_mw']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('sec-ril','qcks')
G.edge['sec-ril']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][append read][open open]'
G.add_edge('sec-ril','qmuxd')
G.edge['sec-ril']['qmuxd']['write-read'] = '[open open][open open][append read][write read][append read][open open]'
G.add_edge('sec-ril','radio')
G.edge['sec-ril']['radio']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('sec-ril','rild')
G.edge['sec-ril']['rild']['write-read'] = '[write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][open open][setattr getattr][write read][append read][write read][append read][write read][append read][open open][write read][append read][open open]'
G.add_edge('sec-ril','rmt_storage')
G.edge['sec-ril']['rmt_storage']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('sec-ril','sec-ril')
G.edge['sec-ril']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][open open]'
G.add_edge('sec-ril','smdexe')
G.edge['sec-ril']['smdexe']['write-read'] = '[open open]'
G.add_edge('sec-ril','ssr_setup')
G.edge['sec-ril']['ssr_setup']['write-read'] = '[open open]'
G.add_edge('sec-ril','sswap')
G.edge['sec-ril']['sswap']['write-read'] = '[open open]'
G.add_edge('sec-ril','surfaceflinger')
G.edge['sec-ril']['surfaceflinger']['write-read'] = '[open open]'
G.add_edge('sec-ril','system_server')
G.edge['sec-ril']['system_server']['write-read'] = '[write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('sec-ril','system_server')
G.edge['sec-ril']['system_server']['write-read'] = '[write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][open open]'
G.add_edge('sec-ril','thermal-engine')
G.edge['sec-ril']['thermal-engine']['write-read'] = '[open open]'
G.add_edge('sec-ril','ueventd')
G.edge['sec-ril']['ueventd']['write-read'] = '[open open]'
G.add_edge('sec-ril','vm_bms')
G.edge['sec-ril']['vm_bms']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('sec-ril','vold')
G.edge['sec-ril']['vold']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('sec-ril','init_shell')
G.edge['sec-ril']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('sec-ril','rild')
G.edge['sec-ril']['rild']['write-read'] = '[write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][open open][setattr getattr][write read][append read][write read][append read][write read][append read][open open][write read][append read][open open][setattr getattr]'
G.add_edge('sec-ril','rtcc')
G.edge['sec-ril']['rtcc']['write-read'] = '[setattr getattr]'
G.add_edge('sec-ril','sec-ril')
G.edge['sec-ril']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][open open][setattr getattr]'
G.add_edge('sec-ril','system_server')
G.edge['sec-ril']['system_server']['write-read'] = '[write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][open open][setattr getattr]'
G.add_edge('sec-ril','at_distributor')
G.edge['sec-ril']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read]'
G.edge['sec-ril']['at_distributor']['fill'] = 'red'
G.add_edge('sec-ril','at_distributor')
G.edge['sec-ril']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read]'
G.add_edge('sec-ril','bauthserver')
G.edge['sec-ril']['bauthserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['sec-ril']['bauthserver']['fill'] = 'red'
G.add_edge('sec-ril','bauthserver')
G.edge['sec-ril']['bauthserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('sec-ril','bintvoutservice')
G.edge['sec-ril']['bintvoutservice']['write-read'] = '[open open][write read]'
G.edge['sec-ril']['bintvoutservice']['fill'] = 'red'
G.add_edge('sec-ril','bintvoutservice')
G.edge['sec-ril']['bintvoutservice']['write-read'] = '[open open][write read][append read]'
G.add_edge('sec-ril','bluetooth')
G.edge['sec-ril']['bluetooth']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['sec-ril']['bluetooth']['fill'] = 'red'
G.add_edge('sec-ril','bluetooth')
G.edge['sec-ril']['bluetooth']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('sec-ril','bootanim')
G.edge['sec-ril']['bootanim']['write-read'] = '[write read]'
G.edge['sec-ril']['bootanim']['fill'] = 'red'
G.add_edge('sec-ril','cbd')
G.edge['sec-ril']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['sec-ril']['cbd']['fill'] = 'red'
G.add_edge('sec-ril','cbd')
G.edge['sec-ril']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('sec-ril','cellgeofenced')
G.edge['sec-ril']['cellgeofenced']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['sec-ril']['cellgeofenced']['fill'] = 'red'
G.add_edge('sec-ril','cellgeofenced')
G.edge['sec-ril']['cellgeofenced']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('sec-ril','charger_monitor')
G.edge['sec-ril']['charger_monitor']['write-read'] = '[open open][write read][append read][open open][open open][write read]'
G.edge['sec-ril']['charger_monitor']['fill'] = 'red'
G.add_edge('sec-ril','charger_monitor')
G.edge['sec-ril']['charger_monitor']['write-read'] = '[open open][write read][append read][open open][open open][write read][append read]'
G.add_edge('sec-ril','charger_monitor')
G.edge['sec-ril']['charger_monitor']['write-read'] = '[open open][write read][append read][open open][open open][write read][append read][write read]'
G.edge['sec-ril']['charger_monitor']['fill'] = 'red'
G.add_edge('sec-ril','charger_monitor')
G.edge['sec-ril']['charger_monitor']['write-read'] = '[open open][write read][append read][open open][open open][write read][append read][write read][append read]'
G.add_edge('sec-ril','cnd')
G.edge['sec-ril']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][append read][open open][write read]'
G.edge['sec-ril']['cnd']['fill'] = 'red'
G.add_edge('sec-ril','cnd')
G.edge['sec-ril']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][append read][open open][write read][append read]'
G.add_edge('sec-ril','connfwexe')
G.edge['sec-ril']['connfwexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read]'
G.edge['sec-ril']['connfwexe']['fill'] = 'red'
G.add_edge('sec-ril','connfwexe')
G.edge['sec-ril']['connfwexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read]'
G.add_edge('sec-ril','debuggerd')
G.edge['sec-ril']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['sec-ril']['debuggerd']['fill'] = 'red'
G.add_edge('sec-ril','debuggerd')
G.edge['sec-ril']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('sec-ril','diag_uart_log')
G.edge['sec-ril']['diag_uart_log']['write-read'] = '[open open][write read]'
G.edge['sec-ril']['diag_uart_log']['fill'] = 'red'
G.add_edge('sec-ril','diag_uart_log')
G.edge['sec-ril']['diag_uart_log']['write-read'] = '[open open][write read][append read]'
G.add_edge('sec-ril','dumpstate')
G.edge['sec-ril']['dumpstate']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read]'
G.edge['sec-ril']['dumpstate']['fill'] = 'red'
G.add_edge('sec-ril','dumpstate')
G.edge['sec-ril']['dumpstate']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('sec-ril','efsks')
G.edge['sec-ril']['efsks']['write-read'] = '[open open][write read]'
G.edge['sec-ril']['efsks']['fill'] = 'red'
G.add_edge('sec-ril','efsks')
G.edge['sec-ril']['efsks']['write-read'] = '[open open][write read][append read]'
G.add_edge('sec-ril','geomagneticd')
G.edge['sec-ril']['geomagneticd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['sec-ril']['geomagneticd']['fill'] = 'red'
G.add_edge('sec-ril','geomagneticd')
G.edge['sec-ril']['geomagneticd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('sec-ril','gpsd')
G.edge['sec-ril']['gpsd']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['sec-ril']['gpsd']['fill'] = 'red'
G.add_edge('sec-ril','gpsd')
G.edge['sec-ril']['gpsd']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('sec-ril','healthd')
G.edge['sec-ril']['healthd']['write-read'] = '[open open][write read][append read][write read]'
G.edge['sec-ril']['healthd']['fill'] = 'red'
G.add_edge('sec-ril','init_shell')
G.edge['sec-ril']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['sec-ril']['init_shell']['fill'] = 'red'
G.add_edge('sec-ril','init_shell')
G.edge['sec-ril']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('sec-ril','jackservice')
G.edge['sec-ril']['jackservice']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['sec-ril']['jackservice']['fill'] = 'red'
G.add_edge('sec-ril','kiesexe')
G.edge['sec-ril']['kiesexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['sec-ril']['kiesexe']['fill'] = 'red'
G.add_edge('sec-ril','kiesexe')
G.edge['sec-ril']['kiesexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('sec-ril','ks')
G.edge['sec-ril']['ks']['write-read'] = '[open open][append read][open open][write read]'
G.edge['sec-ril']['ks']['fill'] = 'red'
G.add_edge('sec-ril','ks')
G.edge['sec-ril']['ks']['write-read'] = '[open open][append read][open open][write read][append read]'
G.add_edge('sec-ril','lhd')
G.edge['sec-ril']['lhd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read]'
G.edge['sec-ril']['lhd']['fill'] = 'red'
G.add_edge('sec-ril','lhd')
G.edge['sec-ril']['lhd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read]'
G.add_edge('sec-ril','lmkd')
G.edge['sec-ril']['lmkd']['write-read'] = '[write read]'
G.edge['sec-ril']['lmkd']['fill'] = 'red'
G.add_edge('sec-ril','lpm')
G.edge['sec-ril']['lpm']['write-read'] = '[open open][write read]'
G.edge['sec-ril']['lpm']['fill'] = 'red'
G.add_edge('sec-ril','lpm')
G.edge['sec-ril']['lpm']['write-read'] = '[open open][write read][append read]'
G.add_edge('sec-ril','macloader')
G.edge['sec-ril']['macloader']['write-read'] = '[open open][write read]'
G.edge['sec-ril']['macloader']['fill'] = 'red'
G.add_edge('sec-ril','macloader')
G.edge['sec-ril']['macloader']['write-read'] = '[open open][write read][append read]'
G.add_edge('sec-ril','mdm_helper')
G.edge['sec-ril']['mdm_helper']['write-read'] = '[open open][append read][open open][write read]'
G.edge['sec-ril']['mdm_helper']['fill'] = 'red'
G.add_edge('sec-ril','mediaserver')
G.edge['sec-ril']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read]'
G.edge['sec-ril']['mediaserver']['fill'] = 'red'
G.add_edge('sec-ril','mediaserver')
G.edge['sec-ril']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read]'
G.add_edge('sec-ril','mfgloader')
G.edge['sec-ril']['mfgloader']['write-read'] = '[open open][write read][add_name search][remove_name search][write read]'
G.edge['sec-ril']['mfgloader']['fill'] = 'red'
G.add_edge('sec-ril','mlexe')
G.edge['sec-ril']['mlexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['sec-ril']['mlexe']['fill'] = 'red'
G.add_edge('sec-ril','mlexe')
G.edge['sec-ril']['mlexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('sec-ril','mm-pp-daemon')
G.edge['sec-ril']['mm-pp-daemon']['write-read'] = '[open open][write read]'
G.edge['sec-ril']['mm-pp-daemon']['fill'] = 'red'
G.add_edge('sec-ril','mm-pp-daemon')
G.edge['sec-ril']['mm-pp-daemon']['write-read'] = '[open open][write read][append read]'
G.add_edge('sec-ril','mm-pp-daemon')
G.edge['sec-ril']['mm-pp-daemon']['write-read'] = '[open open][write read][append read][write read]'
G.edge['sec-ril']['mm-pp-daemon']['fill'] = 'red'
G.add_edge('sec-ril','mm-qcamera-daemon')
G.edge['sec-ril']['mm-qcamera-daemon']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['sec-ril']['mm-qcamera-daemon']['fill'] = 'red'
G.add_edge('sec-ril','mm-qcamera-daemon')
G.edge['sec-ril']['mm-qcamera-daemon']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('sec-ril','mpdecision')
G.edge['sec-ril']['mpdecision']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['sec-ril']['mpdecision']['fill'] = 'red'
G.add_edge('sec-ril','mpdecision')
G.edge['sec-ril']['mpdecision']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('sec-ril','mpdecision')
G.edge['sec-ril']['mpdecision']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read][write read]'
G.edge['sec-ril']['mpdecision']['fill'] = 'red'
G.add_edge('sec-ril','netd')
G.edge['sec-ril']['netd']['write-read'] = '[write read]'
G.edge['sec-ril']['netd']['fill'] = 'red'
G.add_edge('sec-ril','netmgrd')
G.edge['sec-ril']['netmgrd']['write-read'] = '[open open][open open][write read][write read][add_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['sec-ril']['netmgrd']['fill'] = 'red'
G.add_edge('sec-ril','nfc')
G.edge['sec-ril']['nfc']['write-read'] = '[open open][setattr getattr][write read][append read][write read]'
G.edge['sec-ril']['nfc']['fill'] = 'red'
G.add_edge('sec-ril','oneseg_mw')
G.edge['sec-ril']['oneseg_mw']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['sec-ril']['oneseg_mw']['fill'] = 'red'
G.add_edge('sec-ril','oneseg_mw')
G.edge['sec-ril']['oneseg_mw']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('sec-ril','perfd')
G.edge['sec-ril']['perfd']['write-read'] = '[write read]'
G.edge['sec-ril']['perfd']['fill'] = 'red'
G.add_edge('sec-ril','qcks')
G.edge['sec-ril']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][append read][open open][write read]'
G.edge['sec-ril']['qcks']['fill'] = 'red'
G.add_edge('sec-ril','qcks')
G.edge['sec-ril']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][append read][open open][write read][append read]'
G.add_edge('sec-ril','qmuxd')
G.edge['sec-ril']['qmuxd']['write-read'] = '[open open][open open][append read][write read][append read][open open][write read]'
G.edge['sec-ril']['qmuxd']['fill'] = 'red'
G.add_edge('sec-ril','qmuxd')
G.edge['sec-ril']['qmuxd']['write-read'] = '[open open][open open][append read][write read][append read][open open][write read][append read]'
G.add_edge('sec-ril','qosmgr')
G.edge['sec-ril']['qosmgr']['write-read'] = '[write read]'
G.edge['sec-ril']['qosmgr']['fill'] = 'red'
G.add_edge('sec-ril','radio')
G.edge['sec-ril']['radio']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][append read]'
G.add_edge('sec-ril','rild')
G.edge['sec-ril']['rild']['write-read'] = '[write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][open open][setattr getattr][write read][append read][write read][append read][write read][append read][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['sec-ril']['rild']['fill'] = 'red'
G.add_edge('sec-ril','rild')
G.edge['sec-ril']['rild']['write-read'] = '[write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][open open][setattr getattr][write read][append read][write read][append read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('sec-ril','rmt_storage')
G.edge['sec-ril']['rmt_storage']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['sec-ril']['rmt_storage']['fill'] = 'red'
G.add_edge('sec-ril','rmt_storage')
G.edge['sec-ril']['rmt_storage']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('sec-ril','rtcc')
G.edge['sec-ril']['rtcc']['write-read'] = '[setattr getattr][write read]'
G.edge['sec-ril']['rtcc']['fill'] = 'red'
G.add_edge('sec-ril','sec-ril')
G.edge['sec-ril']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][open open][setattr getattr][write read]'
G.edge['sec-ril']['sec-ril']['fill'] = 'red'
G.add_edge('sec-ril','sec-ril')
G.edge['sec-ril']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][open open][setattr getattr][write read][append read]'
G.add_edge('sec-ril','sensorhubservice')
G.edge['sec-ril']['sensorhubservice']['write-read'] = '[write read]'
G.edge['sec-ril']['sensorhubservice']['fill'] = 'red'
G.add_edge('sec-ril','smdexe')
G.edge['sec-ril']['smdexe']['write-read'] = '[open open][write read]'
G.edge['sec-ril']['smdexe']['fill'] = 'red'
G.add_edge('sec-ril','smdexe')
G.edge['sec-ril']['smdexe']['write-read'] = '[open open][write read][append read]'
G.add_edge('sec-ril','ssr_setup')
G.edge['sec-ril']['ssr_setup']['write-read'] = '[open open][write read]'
G.edge['sec-ril']['ssr_setup']['fill'] = 'red'
G.add_edge('sec-ril','ssr_setup')
G.edge['sec-ril']['ssr_setup']['write-read'] = '[open open][write read][append read]'
G.add_edge('sec-ril','sswap')
G.edge['sec-ril']['sswap']['write-read'] = '[open open][write read]'
G.edge['sec-ril']['sswap']['fill'] = 'red'
G.add_edge('sec-ril','sswap')
G.edge['sec-ril']['sswap']['write-read'] = '[open open][write read][append read]'
G.add_edge('sec-ril','surfaceflinger')
G.edge['sec-ril']['surfaceflinger']['write-read'] = '[open open][write read]'
G.edge['sec-ril']['surfaceflinger']['fill'] = 'red'
G.add_edge('sec-ril','surfaceflinger')
G.edge['sec-ril']['surfaceflinger']['write-read'] = '[open open][write read][append read]'
G.add_edge('sec-ril','surfaceflinger')
G.edge['sec-ril']['surfaceflinger']['write-read'] = '[open open][write read][append read][write read]'
G.edge['sec-ril']['surfaceflinger']['fill'] = 'red'
G.add_edge('sec-ril','system_server')
G.edge['sec-ril']['system_server']['write-read'] = '[write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][open open][setattr getattr][write read]'
G.edge['sec-ril']['system_server']['fill'] = 'red'
G.add_edge('sec-ril','system_server')
G.edge['sec-ril']['system_server']['write-read'] = '[write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][open open][setattr getattr][write read][append read]'
G.add_edge('sec-ril','system_server')
G.edge['sec-ril']['system_server']['write-read'] = '[write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][open open][setattr getattr][write read][append read][write read]'
G.edge['sec-ril']['system_server']['fill'] = 'red'
G.add_edge('sec-ril','system_server')
G.edge['sec-ril']['system_server']['write-read'] = '[write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read]'
G.add_edge('sec-ril','thermald')
G.edge['sec-ril']['thermald']['write-read'] = '[open open][write read][add_name search][remove_name search][write read]'
G.edge['sec-ril']['thermald']['fill'] = 'red'
G.add_edge('sec-ril','thermal-engine')
G.edge['sec-ril']['thermal-engine']['write-read'] = '[open open][write read]'
G.edge['sec-ril']['thermal-engine']['fill'] = 'red'
G.add_edge('sec-ril','thermal-engine')
G.edge['sec-ril']['thermal-engine']['write-read'] = '[open open][write read][append read]'
G.add_edge('sec-ril','thermal-engine')
G.edge['sec-ril']['thermal-engine']['write-read'] = '[open open][write read][append read][write read]'
G.edge['sec-ril']['thermal-engine']['fill'] = 'red'
G.add_edge('sec-ril','ueventd')
G.edge['sec-ril']['ueventd']['write-read'] = '[open open][write read]'
G.edge['sec-ril']['ueventd']['fill'] = 'red'
G.add_edge('sec-ril','ueventd')
G.edge['sec-ril']['ueventd']['write-read'] = '[open open][write read][append read]'
G.add_edge('sec-ril','vm_bms')
G.edge['sec-ril']['vm_bms']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['sec-ril']['vm_bms']['fill'] = 'red'
G.add_edge('sec-ril','vm_bms')
G.edge['sec-ril']['vm_bms']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('sec-ril','vmwared')
G.edge['sec-ril']['vmwared']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['sec-ril']['vmwared']['fill'] = 'red'
G.add_edge('sec-ril','vold')
G.edge['sec-ril']['vold']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read]'
G.edge['sec-ril']['vold']['fill'] = 'red'
G.add_edge('sec-ril','vold')
G.edge['sec-ril']['vold']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read]'
G.add_edge('sec-ril','zygote')
G.edge['sec-ril']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['sec-ril']['zygote']['fill'] = 'red'
G.add_edge('smdexe','at_distributor')
G.edge['smdexe']['at_distributor']['write-read'] = '[open open]'
G.add_edge('smdexe','bauthserver')
G.edge['smdexe']['bauthserver']['write-read'] = '[open open]'
G.add_edge('smdexe','bintvoutservice')
G.edge['smdexe']['bintvoutservice']['write-read'] = '[open open]'
G.add_edge('smdexe','bluetooth')
G.edge['smdexe']['bluetooth']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('smdexe','cbd')
G.edge['smdexe']['cbd']['write-read'] = '[open open]'
G.add_edge('smdexe','cellgeofenced')
G.edge['smdexe']['cellgeofenced']['write-read'] = '[open open]'
G.add_edge('smdexe','charger_monitor')
G.edge['smdexe']['charger_monitor']['write-read'] = '[open open]'
G.add_edge('smdexe','charger_monitor')
G.edge['smdexe']['charger_monitor']['write-read'] = '[open open][open open]'
G.add_edge('smdexe','cnd')
G.edge['smdexe']['cnd']['write-read'] = '[open open]'
G.add_edge('smdexe','connfwexe')
G.edge['smdexe']['connfwexe']['write-read'] = '[open open]'
G.add_edge('smdexe','debuggerd')
G.edge['smdexe']['debuggerd']['write-read'] = '[open open]'
G.add_edge('smdexe','diag_uart_log')
G.edge['smdexe']['diag_uart_log']['write-read'] = '[open open]'
G.add_edge('smdexe','dumpstate')
G.edge['smdexe']['dumpstate']['write-read'] = '[open open]'
G.add_edge('smdexe','efsks')
G.edge['smdexe']['efsks']['write-read'] = '[open open]'
G.add_edge('smdexe','geomagneticd')
G.edge['smdexe']['geomagneticd']['write-read'] = '[open open]'
G.add_edge('smdexe','gpsd')
G.edge['smdexe']['gpsd']['write-read'] = '[open open]'
G.add_edge('smdexe','init_shell')
G.edge['smdexe']['init_shell']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('smdexe','kiesexe')
G.edge['smdexe']['kiesexe']['write-read'] = '[open open]'
G.add_edge('smdexe','ks')
G.edge['smdexe']['ks']['write-read'] = '[open open]'
G.add_edge('smdexe','lhd')
G.edge['smdexe']['lhd']['write-read'] = '[open open]'
G.add_edge('smdexe','lpm')
G.edge['smdexe']['lpm']['write-read'] = '[open open]'
G.add_edge('smdexe','macloader')
G.edge['smdexe']['macloader']['write-read'] = '[open open]'
G.add_edge('smdexe','mdm_helper')
G.edge['smdexe']['mdm_helper']['write-read'] = '[open open]'
G.add_edge('smdexe','mediaserver')
G.edge['smdexe']['mediaserver']['write-read'] = '[open open]'
G.add_edge('smdexe','mlexe')
G.edge['smdexe']['mlexe']['write-read'] = '[open open]'
G.add_edge('smdexe','mm-pp-daemon')
G.edge['smdexe']['mm-pp-daemon']['write-read'] = '[open open]'
G.add_edge('smdexe','mm-qcamera-daemon')
G.edge['smdexe']['mm-qcamera-daemon']['write-read'] = '[open open]'
G.add_edge('smdexe','mpdecision')
G.edge['smdexe']['mpdecision']['write-read'] = '[open open]'
G.add_edge('smdexe','oneseg_mw')
G.edge['smdexe']['oneseg_mw']['write-read'] = '[open open]'
G.add_edge('smdexe','qcks')
G.edge['smdexe']['qcks']['write-read'] = '[open open]'
G.add_edge('smdexe','qmuxd')
G.edge['smdexe']['qmuxd']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('smdexe','radio')
G.edge['smdexe']['radio']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('smdexe','rild')
G.edge['smdexe']['rild']['write-read'] = '[open open]'
G.add_edge('smdexe','rmt_storage')
G.edge['smdexe']['rmt_storage']['write-read'] = '[open open]'
G.add_edge('smdexe','sec-ril')
G.edge['smdexe']['sec-ril']['write-read'] = '[open open]'
G.add_edge('smdexe','smdexe')
G.edge['smdexe']['smdexe']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('smdexe','ssr_setup')
G.edge['smdexe']['ssr_setup']['write-read'] = '[open open]'
G.add_edge('smdexe','sswap')
G.edge['smdexe']['sswap']['write-read'] = '[open open]'
G.add_edge('smdexe','surfaceflinger')
G.edge['smdexe']['surfaceflinger']['write-read'] = '[open open]'
G.add_edge('smdexe','system_server')
G.edge['smdexe']['system_server']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('smdexe','system_server')
G.edge['smdexe']['system_server']['write-read'] = '[open open][write read][append read][open open][open open]'
G.add_edge('smdexe','thermal-engine')
G.edge['smdexe']['thermal-engine']['write-read'] = '[open open]'
G.add_edge('smdexe','ueventd')
G.edge['smdexe']['ueventd']['write-read'] = '[open open]'
G.add_edge('smdexe','vm_bms')
G.edge['smdexe']['vm_bms']['write-read'] = '[open open]'
G.add_edge('smdexe','vold')
G.edge['smdexe']['vold']['write-read'] = '[open open]'
G.add_edge('smdexe','init_shell')
G.edge['smdexe']['init_shell']['write-read'] = '[open open][write read][append read][open open][setattr getattr]'
G.add_edge('smdexe','rild')
G.edge['smdexe']['rild']['write-read'] = '[open open][setattr getattr]'
G.add_edge('smdexe','rtcc')
G.edge['smdexe']['rtcc']['write-read'] = '[setattr getattr]'
G.add_edge('smdexe','sec-ril')
G.edge['smdexe']['sec-ril']['write-read'] = '[open open][setattr getattr]'
G.add_edge('smdexe','system_server')
G.edge['smdexe']['system_server']['write-read'] = '[open open][write read][append read][open open][open open][setattr getattr]'
G.add_edge('smdexe','at_distributor')
G.edge['smdexe']['at_distributor']['write-read'] = '[open open][write read]'
G.edge['smdexe']['at_distributor']['fill'] = 'red'
G.add_edge('smdexe','at_distributor')
G.edge['smdexe']['at_distributor']['write-read'] = '[open open][write read][append read]'
G.add_edge('smdexe','bauthserver')
G.edge['smdexe']['bauthserver']['write-read'] = '[open open][write read]'
G.edge['smdexe']['bauthserver']['fill'] = 'red'
G.add_edge('smdexe','bauthserver')
G.edge['smdexe']['bauthserver']['write-read'] = '[open open][write read][append read]'
G.add_edge('smdexe','bintvoutservice')
G.edge['smdexe']['bintvoutservice']['write-read'] = '[open open][write read]'
G.edge['smdexe']['bintvoutservice']['fill'] = 'red'
G.add_edge('smdexe','bintvoutservice')
G.edge['smdexe']['bintvoutservice']['write-read'] = '[open open][write read][append read]'
G.add_edge('smdexe','bluetooth')
G.edge['smdexe']['bluetooth']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['smdexe']['bluetooth']['fill'] = 'red'
G.add_edge('smdexe','bluetooth')
G.edge['smdexe']['bluetooth']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('smdexe','bootanim')
G.edge['smdexe']['bootanim']['write-read'] = '[write read]'
G.edge['smdexe']['bootanim']['fill'] = 'red'
G.add_edge('smdexe','cbd')
G.edge['smdexe']['cbd']['write-read'] = '[open open][write read]'
G.edge['smdexe']['cbd']['fill'] = 'red'
G.add_edge('smdexe','cbd')
G.edge['smdexe']['cbd']['write-read'] = '[open open][write read][append read]'
G.add_edge('smdexe','cellgeofenced')
G.edge['smdexe']['cellgeofenced']['write-read'] = '[open open][write read]'
G.edge['smdexe']['cellgeofenced']['fill'] = 'red'
G.add_edge('smdexe','cellgeofenced')
G.edge['smdexe']['cellgeofenced']['write-read'] = '[open open][write read][append read]'
G.add_edge('smdexe','charger_monitor')
G.edge['smdexe']['charger_monitor']['write-read'] = '[open open][open open][write read]'
G.edge['smdexe']['charger_monitor']['fill'] = 'red'
G.add_edge('smdexe','charger_monitor')
G.edge['smdexe']['charger_monitor']['write-read'] = '[open open][open open][write read][append read]'
G.add_edge('smdexe','charger_monitor')
G.edge['smdexe']['charger_monitor']['write-read'] = '[open open][open open][write read][append read][write read]'
G.edge['smdexe']['charger_monitor']['fill'] = 'red'
G.add_edge('smdexe','charger_monitor')
G.edge['smdexe']['charger_monitor']['write-read'] = '[open open][open open][write read][append read][write read][append read]'
G.add_edge('smdexe','cnd')
G.edge['smdexe']['cnd']['write-read'] = '[open open][write read]'
G.edge['smdexe']['cnd']['fill'] = 'red'
G.add_edge('smdexe','cnd')
G.edge['smdexe']['cnd']['write-read'] = '[open open][write read][append read]'
G.add_edge('smdexe','connfwexe')
G.edge['smdexe']['connfwexe']['write-read'] = '[open open][write read]'
G.edge['smdexe']['connfwexe']['fill'] = 'red'
G.add_edge('smdexe','connfwexe')
G.edge['smdexe']['connfwexe']['write-read'] = '[open open][write read][append read]'
G.add_edge('smdexe','debuggerd')
G.edge['smdexe']['debuggerd']['write-read'] = '[open open][write read]'
G.edge['smdexe']['debuggerd']['fill'] = 'red'
G.add_edge('smdexe','debuggerd')
G.edge['smdexe']['debuggerd']['write-read'] = '[open open][write read][append read]'
G.add_edge('smdexe','diag_uart_log')
G.edge['smdexe']['diag_uart_log']['write-read'] = '[open open][write read]'
G.edge['smdexe']['diag_uart_log']['fill'] = 'red'
G.add_edge('smdexe','diag_uart_log')
G.edge['smdexe']['diag_uart_log']['write-read'] = '[open open][write read][append read]'
G.add_edge('smdexe','dumpstate')
G.edge['smdexe']['dumpstate']['write-read'] = '[open open][write read]'
G.edge['smdexe']['dumpstate']['fill'] = 'red'
G.add_edge('smdexe','dumpstate')
G.edge['smdexe']['dumpstate']['write-read'] = '[open open][write read][append read]'
G.add_edge('smdexe','efsks')
G.edge['smdexe']['efsks']['write-read'] = '[open open][write read]'
G.edge['smdexe']['efsks']['fill'] = 'red'
G.add_edge('smdexe','efsks')
G.edge['smdexe']['efsks']['write-read'] = '[open open][write read][append read]'
G.add_edge('smdexe','geomagneticd')
G.edge['smdexe']['geomagneticd']['write-read'] = '[open open][write read]'
G.edge['smdexe']['geomagneticd']['fill'] = 'red'
G.add_edge('smdexe','geomagneticd')
G.edge['smdexe']['geomagneticd']['write-read'] = '[open open][write read][append read]'
G.add_edge('smdexe','gpsd')
G.edge['smdexe']['gpsd']['write-read'] = '[open open][write read]'
G.edge['smdexe']['gpsd']['fill'] = 'red'
G.add_edge('smdexe','gpsd')
G.edge['smdexe']['gpsd']['write-read'] = '[open open][write read][append read]'
G.add_edge('smdexe','healthd')
G.edge['smdexe']['healthd']['write-read'] = '[write read]'
G.edge['smdexe']['healthd']['fill'] = 'red'
G.add_edge('smdexe','init_shell')
G.edge['smdexe']['init_shell']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read]'
G.edge['smdexe']['init_shell']['fill'] = 'red'
G.add_edge('smdexe','init_shell')
G.edge['smdexe']['init_shell']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('smdexe','jackservice')
G.edge['smdexe']['jackservice']['write-read'] = '[write read]'
G.edge['smdexe']['jackservice']['fill'] = 'red'
G.add_edge('smdexe','kiesexe')
G.edge['smdexe']['kiesexe']['write-read'] = '[open open][write read]'
G.edge['smdexe']['kiesexe']['fill'] = 'red'
G.add_edge('smdexe','kiesexe')
G.edge['smdexe']['kiesexe']['write-read'] = '[open open][write read][append read]'
G.add_edge('smdexe','ks')
G.edge['smdexe']['ks']['write-read'] = '[open open][write read]'
G.edge['smdexe']['ks']['fill'] = 'red'
G.add_edge('smdexe','ks')
G.edge['smdexe']['ks']['write-read'] = '[open open][write read][append read]'
G.add_edge('smdexe','lhd')
G.edge['smdexe']['lhd']['write-read'] = '[open open][write read]'
G.edge['smdexe']['lhd']['fill'] = 'red'
G.add_edge('smdexe','lhd')
G.edge['smdexe']['lhd']['write-read'] = '[open open][write read][append read]'
G.add_edge('smdexe','lmkd')
G.edge['smdexe']['lmkd']['write-read'] = '[write read]'
G.edge['smdexe']['lmkd']['fill'] = 'red'
G.add_edge('smdexe','lpm')
G.edge['smdexe']['lpm']['write-read'] = '[open open][write read]'
G.edge['smdexe']['lpm']['fill'] = 'red'
G.add_edge('smdexe','lpm')
G.edge['smdexe']['lpm']['write-read'] = '[open open][write read][append read]'
G.add_edge('smdexe','macloader')
G.edge['smdexe']['macloader']['write-read'] = '[open open][write read]'
G.edge['smdexe']['macloader']['fill'] = 'red'
G.add_edge('smdexe','macloader')
G.edge['smdexe']['macloader']['write-read'] = '[open open][write read][append read]'
G.add_edge('smdexe','mdm_helper')
G.edge['smdexe']['mdm_helper']['write-read'] = '[open open][write read]'
G.edge['smdexe']['mdm_helper']['fill'] = 'red'
G.add_edge('smdexe','mediaserver')
G.edge['smdexe']['mediaserver']['write-read'] = '[open open][write read]'
G.edge['smdexe']['mediaserver']['fill'] = 'red'
G.add_edge('smdexe','mediaserver')
G.edge['smdexe']['mediaserver']['write-read'] = '[open open][write read][append read]'
G.add_edge('smdexe','mfgloader')
G.edge['smdexe']['mfgloader']['write-read'] = '[write read]'
G.edge['smdexe']['mfgloader']['fill'] = 'red'
G.add_edge('smdexe','mlexe')
G.edge['smdexe']['mlexe']['write-read'] = '[open open][write read]'
G.edge['smdexe']['mlexe']['fill'] = 'red'
G.add_edge('smdexe','mlexe')
G.edge['smdexe']['mlexe']['write-read'] = '[open open][write read][append read]'
G.add_edge('smdexe','mm-pp-daemon')
G.edge['smdexe']['mm-pp-daemon']['write-read'] = '[open open][write read]'
G.edge['smdexe']['mm-pp-daemon']['fill'] = 'red'
G.add_edge('smdexe','mm-pp-daemon')
G.edge['smdexe']['mm-pp-daemon']['write-read'] = '[open open][write read][append read]'
G.add_edge('smdexe','mm-pp-daemon')
G.edge['smdexe']['mm-pp-daemon']['write-read'] = '[open open][write read][append read][write read]'
G.edge['smdexe']['mm-pp-daemon']['fill'] = 'red'
G.add_edge('smdexe','mm-qcamera-daemon')
G.edge['smdexe']['mm-qcamera-daemon']['write-read'] = '[open open][write read]'
G.edge['smdexe']['mm-qcamera-daemon']['fill'] = 'red'
G.add_edge('smdexe','mm-qcamera-daemon')
G.edge['smdexe']['mm-qcamera-daemon']['write-read'] = '[open open][write read][append read]'
G.add_edge('smdexe','mpdecision')
G.edge['smdexe']['mpdecision']['write-read'] = '[open open][write read]'
G.edge['smdexe']['mpdecision']['fill'] = 'red'
G.add_edge('smdexe','mpdecision')
G.edge['smdexe']['mpdecision']['write-read'] = '[open open][write read][append read]'
G.add_edge('smdexe','mpdecision')
G.edge['smdexe']['mpdecision']['write-read'] = '[open open][write read][append read][write read]'
G.edge['smdexe']['mpdecision']['fill'] = 'red'
G.add_edge('smdexe','netd')
G.edge['smdexe']['netd']['write-read'] = '[write read]'
G.edge['smdexe']['netd']['fill'] = 'red'
G.add_edge('smdexe','netmgrd')
G.edge['smdexe']['netmgrd']['write-read'] = '[write read]'
G.edge['smdexe']['netmgrd']['fill'] = 'red'
G.add_edge('smdexe','nfc')
G.edge['smdexe']['nfc']['write-read'] = '[write read]'
G.edge['smdexe']['nfc']['fill'] = 'red'
G.add_edge('smdexe','oneseg_mw')
G.edge['smdexe']['oneseg_mw']['write-read'] = '[open open][write read]'
G.edge['smdexe']['oneseg_mw']['fill'] = 'red'
G.add_edge('smdexe','oneseg_mw')
G.edge['smdexe']['oneseg_mw']['write-read'] = '[open open][write read][append read]'
G.add_edge('smdexe','perfd')
G.edge['smdexe']['perfd']['write-read'] = '[write read]'
G.edge['smdexe']['perfd']['fill'] = 'red'
G.add_edge('smdexe','qcks')
G.edge['smdexe']['qcks']['write-read'] = '[open open][write read]'
G.edge['smdexe']['qcks']['fill'] = 'red'
G.add_edge('smdexe','qcks')
G.edge['smdexe']['qcks']['write-read'] = '[open open][write read][append read]'
G.add_edge('smdexe','qmuxd')
G.edge['smdexe']['qmuxd']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['smdexe']['qmuxd']['fill'] = 'red'
G.add_edge('smdexe','qmuxd')
G.edge['smdexe']['qmuxd']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('smdexe','qosmgr')
G.edge['smdexe']['qosmgr']['write-read'] = '[write read]'
G.edge['smdexe']['qosmgr']['fill'] = 'red'
G.add_edge('smdexe','radio')
G.edge['smdexe']['radio']['write-read'] = '[open open][write read][append read][open open][append read]'
G.add_edge('smdexe','rild')
G.edge['smdexe']['rild']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['smdexe']['rild']['fill'] = 'red'
G.add_edge('smdexe','rild')
G.edge['smdexe']['rild']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('smdexe','rmt_storage')
G.edge['smdexe']['rmt_storage']['write-read'] = '[open open][write read]'
G.edge['smdexe']['rmt_storage']['fill'] = 'red'
G.add_edge('smdexe','rmt_storage')
G.edge['smdexe']['rmt_storage']['write-read'] = '[open open][write read][append read]'
G.add_edge('smdexe','rtcc')
G.edge['smdexe']['rtcc']['write-read'] = '[setattr getattr][write read]'
G.edge['smdexe']['rtcc']['fill'] = 'red'
G.add_edge('smdexe','sec-ril')
G.edge['smdexe']['sec-ril']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['smdexe']['sec-ril']['fill'] = 'red'
G.add_edge('smdexe','sec-ril')
G.edge['smdexe']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('smdexe','sensorhubservice')
G.edge['smdexe']['sensorhubservice']['write-read'] = '[write read]'
G.edge['smdexe']['sensorhubservice']['fill'] = 'red'
G.add_edge('smdexe','smdexe')
G.edge['smdexe']['smdexe']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read]'
G.edge['smdexe']['smdexe']['fill'] = 'red'
G.add_edge('smdexe','smdexe')
G.edge['smdexe']['smdexe']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][append read]'
G.add_edge('smdexe','ssr_setup')
G.edge['smdexe']['ssr_setup']['write-read'] = '[open open][write read]'
G.edge['smdexe']['ssr_setup']['fill'] = 'red'
G.add_edge('smdexe','ssr_setup')
G.edge['smdexe']['ssr_setup']['write-read'] = '[open open][write read][append read]'
G.add_edge('smdexe','sswap')
G.edge['smdexe']['sswap']['write-read'] = '[open open][write read]'
G.edge['smdexe']['sswap']['fill'] = 'red'
G.add_edge('smdexe','sswap')
G.edge['smdexe']['sswap']['write-read'] = '[open open][write read][append read]'
G.add_edge('smdexe','surfaceflinger')
G.edge['smdexe']['surfaceflinger']['write-read'] = '[open open][write read]'
G.edge['smdexe']['surfaceflinger']['fill'] = 'red'
G.add_edge('smdexe','surfaceflinger')
G.edge['smdexe']['surfaceflinger']['write-read'] = '[open open][write read][append read]'
G.add_edge('smdexe','surfaceflinger')
G.edge['smdexe']['surfaceflinger']['write-read'] = '[open open][write read][append read][write read]'
G.edge['smdexe']['surfaceflinger']['fill'] = 'red'
G.add_edge('smdexe','system_server')
G.edge['smdexe']['system_server']['write-read'] = '[open open][write read][append read][open open][open open][setattr getattr][write read]'
G.edge['smdexe']['system_server']['fill'] = 'red'
G.add_edge('smdexe','system_server')
G.edge['smdexe']['system_server']['write-read'] = '[open open][write read][append read][open open][open open][setattr getattr][write read][append read]'
G.add_edge('smdexe','system_server')
G.edge['smdexe']['system_server']['write-read'] = '[open open][write read][append read][open open][open open][setattr getattr][write read][append read][write read]'
G.edge['smdexe']['system_server']['fill'] = 'red'
G.add_edge('smdexe','system_server')
G.edge['smdexe']['system_server']['write-read'] = '[open open][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read]'
G.add_edge('smdexe','thermald')
G.edge['smdexe']['thermald']['write-read'] = '[write read]'
G.edge['smdexe']['thermald']['fill'] = 'red'
G.add_edge('smdexe','thermal-engine')
G.edge['smdexe']['thermal-engine']['write-read'] = '[open open][write read]'
G.edge['smdexe']['thermal-engine']['fill'] = 'red'
G.add_edge('smdexe','thermal-engine')
G.edge['smdexe']['thermal-engine']['write-read'] = '[open open][write read][append read]'
G.add_edge('smdexe','thermal-engine')
G.edge['smdexe']['thermal-engine']['write-read'] = '[open open][write read][append read][write read]'
G.edge['smdexe']['thermal-engine']['fill'] = 'red'
G.add_edge('smdexe','ueventd')
G.edge['smdexe']['ueventd']['write-read'] = '[open open][write read]'
G.edge['smdexe']['ueventd']['fill'] = 'red'
G.add_edge('smdexe','ueventd')
G.edge['smdexe']['ueventd']['write-read'] = '[open open][write read][append read]'
G.add_edge('smdexe','vm_bms')
G.edge['smdexe']['vm_bms']['write-read'] = '[open open][write read]'
G.edge['smdexe']['vm_bms']['fill'] = 'red'
G.add_edge('smdexe','vm_bms')
G.edge['smdexe']['vm_bms']['write-read'] = '[open open][write read][append read]'
G.add_edge('smdexe','vmwared')
G.edge['smdexe']['vmwared']['write-read'] = '[write read]'
G.edge['smdexe']['vmwared']['fill'] = 'red'
G.add_edge('smdexe','vold')
G.edge['smdexe']['vold']['write-read'] = '[open open][write read]'
G.edge['smdexe']['vold']['fill'] = 'red'
G.add_edge('smdexe','vold')
G.edge['smdexe']['vold']['write-read'] = '[open open][write read][append read]'
G.add_edge('smdexe','zygote')
G.edge['smdexe']['zygote']['write-read'] = '[write read]'
G.edge['smdexe']['zygote']['fill'] = 'red'
G.add_edge('surfaceflinger','at_distributor')
G.edge['surfaceflinger']['at_distributor']['write-read'] = '[open open]'
G.add_edge('surfaceflinger','bauthserver')
G.edge['surfaceflinger']['bauthserver']['write-read'] = '[open open]'
G.add_edge('surfaceflinger','bintvoutservice')
G.edge['surfaceflinger']['bintvoutservice']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('surfaceflinger','bluetooth')
G.edge['surfaceflinger']['bluetooth']['write-read'] = '[write read][open open]'
G.add_edge('surfaceflinger','cbd')
G.edge['surfaceflinger']['cbd']['write-read'] = '[open open]'
G.add_edge('surfaceflinger','cellgeofenced')
G.edge['surfaceflinger']['cellgeofenced']['write-read'] = '[open open]'
G.add_edge('surfaceflinger','charger_monitor')
G.edge['surfaceflinger']['charger_monitor']['write-read'] = '[setopt getopt][open open]'
G.add_edge('surfaceflinger','charger_monitor')
G.edge['surfaceflinger']['charger_monitor']['write-read'] = '[setopt getopt][open open][open open]'
G.add_edge('surfaceflinger','cnd')
G.edge['surfaceflinger']['cnd']['write-read'] = '[open open]'
G.add_edge('surfaceflinger','connfwexe')
G.edge['surfaceflinger']['connfwexe']['write-read'] = '[open open]'
G.add_edge('surfaceflinger','debuggerd')
G.edge['surfaceflinger']['debuggerd']['write-read'] = '[open open]'
G.add_edge('surfaceflinger','diag_uart_log')
G.edge['surfaceflinger']['diag_uart_log']['write-read'] = '[open open]'
G.add_edge('surfaceflinger','dumpstate')
G.edge['surfaceflinger']['dumpstate']['write-read'] = '[open open][write read][append read][write read][append read][open open]'
G.add_edge('surfaceflinger','efsks')
G.edge['surfaceflinger']['efsks']['write-read'] = '[open open]'
G.add_edge('surfaceflinger','geomagneticd')
G.edge['surfaceflinger']['geomagneticd']['write-read'] = '[open open]'
G.add_edge('surfaceflinger','gpsd')
G.edge['surfaceflinger']['gpsd']['write-read'] = '[open open]'
G.add_edge('surfaceflinger','init_shell')
G.edge['surfaceflinger']['init_shell']['write-read'] = '[open open]'
G.add_edge('surfaceflinger','kiesexe')
G.edge['surfaceflinger']['kiesexe']['write-read'] = '[open open]'
G.add_edge('surfaceflinger','ks')
G.edge['surfaceflinger']['ks']['write-read'] = '[open open]'
G.add_edge('surfaceflinger','lhd')
G.edge['surfaceflinger']['lhd']['write-read'] = '[open open]'
G.add_edge('surfaceflinger','lpm')
G.edge['surfaceflinger']['lpm']['write-read'] = '[setopt getopt][open open][write read][append read][open open]'
G.add_edge('surfaceflinger','macloader')
G.edge['surfaceflinger']['macloader']['write-read'] = '[open open]'
G.add_edge('surfaceflinger','mdm_helper')
G.edge['surfaceflinger']['mdm_helper']['write-read'] = '[open open]'
G.add_edge('surfaceflinger','mediaserver')
G.edge['surfaceflinger']['mediaserver']['write-read'] = '[open open][write read][append read][write read][append read][open open][write read][append read][open open]'
G.add_edge('surfaceflinger','mlexe')
G.edge['surfaceflinger']['mlexe']['write-read'] = '[open open]'
G.add_edge('surfaceflinger','mm-pp-daemon')
G.edge['surfaceflinger']['mm-pp-daemon']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('surfaceflinger','mm-qcamera-daemon')
G.edge['surfaceflinger']['mm-qcamera-daemon']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('surfaceflinger','mpdecision')
G.edge['surfaceflinger']['mpdecision']['write-read'] = '[setopt getopt][setopt getopt][open open]'
G.add_edge('surfaceflinger','oneseg_mw')
G.edge['surfaceflinger']['oneseg_mw']['write-read'] = '[open open]'
G.add_edge('surfaceflinger','qcks')
G.edge['surfaceflinger']['qcks']['write-read'] = '[open open]'
G.add_edge('surfaceflinger','qmuxd')
G.edge['surfaceflinger']['qmuxd']['write-read'] = '[open open]'
G.add_edge('surfaceflinger','radio')
G.edge['surfaceflinger']['radio']['write-read'] = '[open open][write read][append read][write read][open open]'
G.add_edge('surfaceflinger','rild')
G.edge['surfaceflinger']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open]'
G.add_edge('surfaceflinger','rmt_storage')
G.edge['surfaceflinger']['rmt_storage']['write-read'] = '[open open]'
G.add_edge('surfaceflinger','sec-ril')
G.edge['surfaceflinger']['sec-ril']['write-read'] = '[open open]'
G.add_edge('surfaceflinger','smdexe')
G.edge['surfaceflinger']['smdexe']['write-read'] = '[open open]'
G.add_edge('surfaceflinger','ssr_setup')
G.edge['surfaceflinger']['ssr_setup']['write-read'] = '[open open]'
G.add_edge('surfaceflinger','sswap')
G.edge['surfaceflinger']['sswap']['write-read'] = '[open open]'
G.add_edge('surfaceflinger','surfaceflinger')
G.edge['surfaceflinger']['surfaceflinger']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open]'
G.add_edge('surfaceflinger','system_server')
G.edge['surfaceflinger']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][write read][append read][open open]'
G.add_edge('surfaceflinger','system_server')
G.edge['surfaceflinger']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][write read][append read][open open][open open]'
G.add_edge('surfaceflinger','thermal-engine')
G.edge['surfaceflinger']['thermal-engine']['write-read'] = '[setopt getopt][open open]'
G.add_edge('surfaceflinger','ueventd')
G.edge['surfaceflinger']['ueventd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open]'
G.add_edge('surfaceflinger','vm_bms')
G.edge['surfaceflinger']['vm_bms']['write-read'] = '[open open]'
G.add_edge('surfaceflinger','vold')
G.edge['surfaceflinger']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][write read][append read][open open]'
G.add_edge('surfaceflinger','init_shell')
G.edge['surfaceflinger']['init_shell']['write-read'] = '[open open][setattr getattr]'
G.add_edge('surfaceflinger','rild')
G.edge['surfaceflinger']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr]'
G.add_edge('surfaceflinger','rtcc')
G.edge['surfaceflinger']['rtcc']['write-read'] = '[setattr getattr]'
G.add_edge('surfaceflinger','sec-ril')
G.edge['surfaceflinger']['sec-ril']['write-read'] = '[open open][setattr getattr]'
G.add_edge('surfaceflinger','system_server')
G.edge['surfaceflinger']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][write read][append read][open open][open open][setattr getattr]'
G.add_edge('surfaceflinger','at_distributor')
G.edge['surfaceflinger']['at_distributor']['write-read'] = '[open open][write read]'
G.edge['surfaceflinger']['at_distributor']['fill'] = 'red'
G.add_edge('surfaceflinger','at_distributor')
G.edge['surfaceflinger']['at_distributor']['write-read'] = '[open open][write read][append read]'
G.add_edge('surfaceflinger','bauthserver')
G.edge['surfaceflinger']['bauthserver']['write-read'] = '[open open][write read]'
G.edge['surfaceflinger']['bauthserver']['fill'] = 'red'
G.add_edge('surfaceflinger','bauthserver')
G.edge['surfaceflinger']['bauthserver']['write-read'] = '[open open][write read][append read]'
G.add_edge('surfaceflinger','bintvoutservice')
G.edge['surfaceflinger']['bintvoutservice']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read]'
G.edge['surfaceflinger']['bintvoutservice']['fill'] = 'red'
G.add_edge('surfaceflinger','bintvoutservice')
G.edge['surfaceflinger']['bintvoutservice']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][append read]'
G.add_edge('surfaceflinger','bluetooth')
G.edge['surfaceflinger']['bluetooth']['write-read'] = '[write read][open open][write read]'
G.edge['surfaceflinger']['bluetooth']['fill'] = 'red'
G.add_edge('surfaceflinger','bluetooth')
G.edge['surfaceflinger']['bluetooth']['write-read'] = '[write read][open open][write read][append read]'
G.add_edge('surfaceflinger','bootanim')
G.edge['surfaceflinger']['bootanim']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read]'
G.edge['surfaceflinger']['bootanim']['fill'] = 'red'
G.add_edge('surfaceflinger','cbd')
G.edge['surfaceflinger']['cbd']['write-read'] = '[open open][write read]'
G.edge['surfaceflinger']['cbd']['fill'] = 'red'
G.add_edge('surfaceflinger','cbd')
G.edge['surfaceflinger']['cbd']['write-read'] = '[open open][write read][append read]'
G.add_edge('surfaceflinger','cellgeofenced')
G.edge['surfaceflinger']['cellgeofenced']['write-read'] = '[open open][write read]'
G.edge['surfaceflinger']['cellgeofenced']['fill'] = 'red'
G.add_edge('surfaceflinger','cellgeofenced')
G.edge['surfaceflinger']['cellgeofenced']['write-read'] = '[open open][write read][append read]'
G.add_edge('surfaceflinger','charger_monitor')
G.edge['surfaceflinger']['charger_monitor']['write-read'] = '[setopt getopt][open open][open open][write read]'
G.edge['surfaceflinger']['charger_monitor']['fill'] = 'red'
G.add_edge('surfaceflinger','charger_monitor')
G.edge['surfaceflinger']['charger_monitor']['write-read'] = '[setopt getopt][open open][open open][write read][append read]'
G.add_edge('surfaceflinger','charger_monitor')
G.edge['surfaceflinger']['charger_monitor']['write-read'] = '[setopt getopt][open open][open open][write read][append read][write read]'
G.edge['surfaceflinger']['charger_monitor']['fill'] = 'red'
G.add_edge('surfaceflinger','charger_monitor')
G.edge['surfaceflinger']['charger_monitor']['write-read'] = '[setopt getopt][open open][open open][write read][append read][write read][append read]'
G.add_edge('surfaceflinger','cnd')
G.edge['surfaceflinger']['cnd']['write-read'] = '[open open][write read]'
G.edge['surfaceflinger']['cnd']['fill'] = 'red'
G.add_edge('surfaceflinger','cnd')
G.edge['surfaceflinger']['cnd']['write-read'] = '[open open][write read][append read]'
G.add_edge('surfaceflinger','connfwexe')
G.edge['surfaceflinger']['connfwexe']['write-read'] = '[open open][write read]'
G.edge['surfaceflinger']['connfwexe']['fill'] = 'red'
G.add_edge('surfaceflinger','connfwexe')
G.edge['surfaceflinger']['connfwexe']['write-read'] = '[open open][write read][append read]'
G.add_edge('surfaceflinger','debuggerd')
G.edge['surfaceflinger']['debuggerd']['write-read'] = '[open open][write read]'
G.edge['surfaceflinger']['debuggerd']['fill'] = 'red'
G.add_edge('surfaceflinger','debuggerd')
G.edge['surfaceflinger']['debuggerd']['write-read'] = '[open open][write read][append read]'
G.add_edge('surfaceflinger','diag_uart_log')
G.edge['surfaceflinger']['diag_uart_log']['write-read'] = '[open open][write read]'
G.edge['surfaceflinger']['diag_uart_log']['fill'] = 'red'
G.add_edge('surfaceflinger','diag_uart_log')
G.edge['surfaceflinger']['diag_uart_log']['write-read'] = '[open open][write read][append read]'
G.add_edge('surfaceflinger','dumpstate')
G.edge['surfaceflinger']['dumpstate']['write-read'] = '[open open][write read][append read][write read][append read][open open][write read]'
G.edge['surfaceflinger']['dumpstate']['fill'] = 'red'
G.add_edge('surfaceflinger','dumpstate')
G.edge['surfaceflinger']['dumpstate']['write-read'] = '[open open][write read][append read][write read][append read][open open][write read][append read]'
G.add_edge('surfaceflinger','efsks')
G.edge['surfaceflinger']['efsks']['write-read'] = '[open open][write read]'
G.edge['surfaceflinger']['efsks']['fill'] = 'red'
G.add_edge('surfaceflinger','efsks')
G.edge['surfaceflinger']['efsks']['write-read'] = '[open open][write read][append read]'
G.add_edge('surfaceflinger','geomagneticd')
G.edge['surfaceflinger']['geomagneticd']['write-read'] = '[open open][write read]'
G.edge['surfaceflinger']['geomagneticd']['fill'] = 'red'
G.add_edge('surfaceflinger','geomagneticd')
G.edge['surfaceflinger']['geomagneticd']['write-read'] = '[open open][write read][append read]'
G.add_edge('surfaceflinger','gpsd')
G.edge['surfaceflinger']['gpsd']['write-read'] = '[open open][write read]'
G.edge['surfaceflinger']['gpsd']['fill'] = 'red'
G.add_edge('surfaceflinger','gpsd')
G.edge['surfaceflinger']['gpsd']['write-read'] = '[open open][write read][append read]'
G.add_edge('surfaceflinger','healthd')
G.edge['surfaceflinger']['healthd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][write read]'
G.edge['surfaceflinger']['healthd']['fill'] = 'red'
G.add_edge('surfaceflinger','init_shell')
G.edge['surfaceflinger']['init_shell']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['surfaceflinger']['init_shell']['fill'] = 'red'
G.add_edge('surfaceflinger','init_shell')
G.edge['surfaceflinger']['init_shell']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('surfaceflinger','jackservice')
G.edge['surfaceflinger']['jackservice']['write-read'] = '[write read]'
G.edge['surfaceflinger']['jackservice']['fill'] = 'red'
G.add_edge('surfaceflinger','kiesexe')
G.edge['surfaceflinger']['kiesexe']['write-read'] = '[open open][write read]'
G.edge['surfaceflinger']['kiesexe']['fill'] = 'red'
G.add_edge('surfaceflinger','kiesexe')
G.edge['surfaceflinger']['kiesexe']['write-read'] = '[open open][write read][append read]'
G.add_edge('surfaceflinger','ks')
G.edge['surfaceflinger']['ks']['write-read'] = '[open open][write read]'
G.edge['surfaceflinger']['ks']['fill'] = 'red'
G.add_edge('surfaceflinger','ks')
G.edge['surfaceflinger']['ks']['write-read'] = '[open open][write read][append read]'
G.add_edge('surfaceflinger','lhd')
G.edge['surfaceflinger']['lhd']['write-read'] = '[open open][write read]'
G.edge['surfaceflinger']['lhd']['fill'] = 'red'
G.add_edge('surfaceflinger','lhd')
G.edge['surfaceflinger']['lhd']['write-read'] = '[open open][write read][append read]'
G.add_edge('surfaceflinger','lmkd')
G.edge['surfaceflinger']['lmkd']['write-read'] = '[write read]'
G.edge['surfaceflinger']['lmkd']['fill'] = 'red'
G.add_edge('surfaceflinger','lpm')
G.edge['surfaceflinger']['lpm']['write-read'] = '[setopt getopt][open open][write read][append read][open open][write read]'
G.edge['surfaceflinger']['lpm']['fill'] = 'red'
G.add_edge('surfaceflinger','lpm')
G.edge['surfaceflinger']['lpm']['write-read'] = '[setopt getopt][open open][write read][append read][open open][write read][append read]'
G.add_edge('surfaceflinger','macloader')
G.edge['surfaceflinger']['macloader']['write-read'] = '[open open][write read]'
G.edge['surfaceflinger']['macloader']['fill'] = 'red'
G.add_edge('surfaceflinger','macloader')
G.edge['surfaceflinger']['macloader']['write-read'] = '[open open][write read][append read]'
G.add_edge('surfaceflinger','mdm_helper')
G.edge['surfaceflinger']['mdm_helper']['write-read'] = '[open open][write read]'
G.edge['surfaceflinger']['mdm_helper']['fill'] = 'red'
G.add_edge('surfaceflinger','mediaserver')
G.edge['surfaceflinger']['mediaserver']['write-read'] = '[open open][write read][append read][write read][append read][open open][write read][append read][open open][write read]'
G.edge['surfaceflinger']['mediaserver']['fill'] = 'red'
G.add_edge('surfaceflinger','mediaserver')
G.edge['surfaceflinger']['mediaserver']['write-read'] = '[open open][write read][append read][write read][append read][open open][write read][append read][open open][write read][append read]'
G.add_edge('surfaceflinger','mfgloader')
G.edge['surfaceflinger']['mfgloader']['write-read'] = '[write read]'
G.edge['surfaceflinger']['mfgloader']['fill'] = 'red'
G.add_edge('surfaceflinger','mlexe')
G.edge['surfaceflinger']['mlexe']['write-read'] = '[open open][write read]'
G.edge['surfaceflinger']['mlexe']['fill'] = 'red'
G.add_edge('surfaceflinger','mlexe')
G.edge['surfaceflinger']['mlexe']['write-read'] = '[open open][write read][append read]'
G.add_edge('surfaceflinger','mm-pp-daemon')
G.edge['surfaceflinger']['mm-pp-daemon']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['surfaceflinger']['mm-pp-daemon']['fill'] = 'red'
G.add_edge('surfaceflinger','mm-pp-daemon')
G.edge['surfaceflinger']['mm-pp-daemon']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('surfaceflinger','mm-pp-daemon')
G.edge['surfaceflinger']['mm-pp-daemon']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read]'
G.edge['surfaceflinger']['mm-pp-daemon']['fill'] = 'red'
G.add_edge('surfaceflinger','mm-qcamera-daemon')
G.edge['surfaceflinger']['mm-qcamera-daemon']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['surfaceflinger']['mm-qcamera-daemon']['fill'] = 'red'
G.add_edge('surfaceflinger','mm-qcamera-daemon')
G.edge['surfaceflinger']['mm-qcamera-daemon']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('surfaceflinger','mpdecision')
G.edge['surfaceflinger']['mpdecision']['write-read'] = '[setopt getopt][setopt getopt][open open][write read]'
G.edge['surfaceflinger']['mpdecision']['fill'] = 'red'
G.add_edge('surfaceflinger','mpdecision')
G.edge['surfaceflinger']['mpdecision']['write-read'] = '[setopt getopt][setopt getopt][open open][write read][append read]'
G.add_edge('surfaceflinger','mpdecision')
G.edge['surfaceflinger']['mpdecision']['write-read'] = '[setopt getopt][setopt getopt][open open][write read][append read][write read]'
G.edge['surfaceflinger']['mpdecision']['fill'] = 'red'
G.add_edge('surfaceflinger','netd')
G.edge['surfaceflinger']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][write read]'
G.edge['surfaceflinger']['netd']['fill'] = 'red'
G.add_edge('surfaceflinger','netmgrd')
G.edge['surfaceflinger']['netmgrd']['write-read'] = '[write read]'
G.edge['surfaceflinger']['netmgrd']['fill'] = 'red'
G.add_edge('surfaceflinger','nfc')
G.edge['surfaceflinger']['nfc']['write-read'] = '[write read]'
G.edge['surfaceflinger']['nfc']['fill'] = 'red'
G.add_edge('surfaceflinger','oneseg_mw')
G.edge['surfaceflinger']['oneseg_mw']['write-read'] = '[open open][write read]'
G.edge['surfaceflinger']['oneseg_mw']['fill'] = 'red'
G.add_edge('surfaceflinger','oneseg_mw')
G.edge['surfaceflinger']['oneseg_mw']['write-read'] = '[open open][write read][append read]'
G.add_edge('surfaceflinger','perfd')
G.edge['surfaceflinger']['perfd']['write-read'] = '[setopt getopt][write read]'
G.edge['surfaceflinger']['perfd']['fill'] = 'red'
G.add_edge('surfaceflinger','qcks')
G.edge['surfaceflinger']['qcks']['write-read'] = '[open open][write read]'
G.edge['surfaceflinger']['qcks']['fill'] = 'red'
G.add_edge('surfaceflinger','qcks')
G.edge['surfaceflinger']['qcks']['write-read'] = '[open open][write read][append read]'
G.add_edge('surfaceflinger','qmuxd')
G.edge['surfaceflinger']['qmuxd']['write-read'] = '[open open][write read]'
G.edge['surfaceflinger']['qmuxd']['fill'] = 'red'
G.add_edge('surfaceflinger','qmuxd')
G.edge['surfaceflinger']['qmuxd']['write-read'] = '[open open][write read][append read]'
G.add_edge('surfaceflinger','qosmgr')
G.edge['surfaceflinger']['qosmgr']['write-read'] = '[write read]'
G.edge['surfaceflinger']['qosmgr']['fill'] = 'red'
G.add_edge('surfaceflinger','radio')
G.edge['surfaceflinger']['radio']['write-read'] = '[open open][write read][append read][write read][open open][append read]'
G.add_edge('surfaceflinger','rild')
G.edge['surfaceflinger']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read]'
G.edge['surfaceflinger']['rild']['fill'] = 'red'
G.add_edge('surfaceflinger','rild')
G.edge['surfaceflinger']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read]'
G.add_edge('surfaceflinger','rmt_storage')
G.edge['surfaceflinger']['rmt_storage']['write-read'] = '[open open][write read]'
G.edge['surfaceflinger']['rmt_storage']['fill'] = 'red'
G.add_edge('surfaceflinger','rmt_storage')
G.edge['surfaceflinger']['rmt_storage']['write-read'] = '[open open][write read][append read]'
G.add_edge('surfaceflinger','rtcc')
G.edge['surfaceflinger']['rtcc']['write-read'] = '[setattr getattr][write read]'
G.edge['surfaceflinger']['rtcc']['fill'] = 'red'
G.add_edge('surfaceflinger','sec-ril')
G.edge['surfaceflinger']['sec-ril']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['surfaceflinger']['sec-ril']['fill'] = 'red'
G.add_edge('surfaceflinger','sec-ril')
G.edge['surfaceflinger']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('surfaceflinger','sensorhubservice')
G.edge['surfaceflinger']['sensorhubservice']['write-read'] = '[write read]'
G.edge['surfaceflinger']['sensorhubservice']['fill'] = 'red'
G.add_edge('surfaceflinger','smdexe')
G.edge['surfaceflinger']['smdexe']['write-read'] = '[open open][write read]'
G.edge['surfaceflinger']['smdexe']['fill'] = 'red'
G.add_edge('surfaceflinger','smdexe')
G.edge['surfaceflinger']['smdexe']['write-read'] = '[open open][write read][append read]'
G.add_edge('surfaceflinger','ssr_setup')
G.edge['surfaceflinger']['ssr_setup']['write-read'] = '[open open][write read]'
G.edge['surfaceflinger']['ssr_setup']['fill'] = 'red'
G.add_edge('surfaceflinger','ssr_setup')
G.edge['surfaceflinger']['ssr_setup']['write-read'] = '[open open][write read][append read]'
G.add_edge('surfaceflinger','sswap')
G.edge['surfaceflinger']['sswap']['write-read'] = '[open open][write read]'
G.edge['surfaceflinger']['sswap']['fill'] = 'red'
G.add_edge('surfaceflinger','sswap')
G.edge['surfaceflinger']['sswap']['write-read'] = '[open open][write read][append read]'
G.add_edge('surfaceflinger','surfaceflinger')
G.edge['surfaceflinger']['surfaceflinger']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][write read]'
G.edge['surfaceflinger']['surfaceflinger']['fill'] = 'red'
G.add_edge('surfaceflinger','surfaceflinger')
G.edge['surfaceflinger']['surfaceflinger']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][write read][append read]'
G.add_edge('surfaceflinger','surfaceflinger')
G.edge['surfaceflinger']['surfaceflinger']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][write read]'
G.edge['surfaceflinger']['surfaceflinger']['fill'] = 'red'
G.add_edge('surfaceflinger','system_server')
G.edge['surfaceflinger']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][write read][append read][open open][open open][setattr getattr][write read]'
G.edge['surfaceflinger']['system_server']['fill'] = 'red'
G.add_edge('surfaceflinger','system_server')
G.edge['surfaceflinger']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read]'
G.add_edge('surfaceflinger','system_server')
G.edge['surfaceflinger']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read]'
G.edge['surfaceflinger']['system_server']['fill'] = 'red'
G.add_edge('surfaceflinger','system_server')
G.edge['surfaceflinger']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read]'
G.add_edge('surfaceflinger','thermald')
G.edge['surfaceflinger']['thermald']['write-read'] = '[write read]'
G.edge['surfaceflinger']['thermald']['fill'] = 'red'
G.add_edge('surfaceflinger','thermal-engine')
G.edge['surfaceflinger']['thermal-engine']['write-read'] = '[setopt getopt][open open][write read]'
G.edge['surfaceflinger']['thermal-engine']['fill'] = 'red'
G.add_edge('surfaceflinger','thermal-engine')
G.edge['surfaceflinger']['thermal-engine']['write-read'] = '[setopt getopt][open open][write read][append read]'
G.add_edge('surfaceflinger','thermal-engine')
G.edge['surfaceflinger']['thermal-engine']['write-read'] = '[setopt getopt][open open][write read][append read][write read]'
G.edge['surfaceflinger']['thermal-engine']['fill'] = 'red'
G.add_edge('surfaceflinger','ueventd')
G.edge['surfaceflinger']['ueventd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read]'
G.edge['surfaceflinger']['ueventd']['fill'] = 'red'
G.add_edge('surfaceflinger','ueventd')
G.edge['surfaceflinger']['ueventd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read]'
G.add_edge('surfaceflinger','vm_bms')
G.edge['surfaceflinger']['vm_bms']['write-read'] = '[open open][write read]'
G.edge['surfaceflinger']['vm_bms']['fill'] = 'red'
G.add_edge('surfaceflinger','vm_bms')
G.edge['surfaceflinger']['vm_bms']['write-read'] = '[open open][write read][append read]'
G.add_edge('surfaceflinger','vmwared')
G.edge['surfaceflinger']['vmwared']['write-read'] = '[write read]'
G.edge['surfaceflinger']['vmwared']['fill'] = 'red'
G.add_edge('surfaceflinger','vold')
G.edge['surfaceflinger']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][write read][append read][open open][write read]'
G.edge['surfaceflinger']['vold']['fill'] = 'red'
G.add_edge('surfaceflinger','vold')
G.edge['surfaceflinger']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][write read][append read][open open][write read][append read]'
G.add_edge('surfaceflinger','zygote')
G.edge['surfaceflinger']['zygote']['write-read'] = '[open open][write read][append read][write read]'
G.edge['surfaceflinger']['zygote']['fill'] = 'red'
G.add_edge('system_server','at_distributor')
G.edge['system_server']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('system_server','bauthserver')
G.edge['system_server']['bauthserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('system_server','bintvoutservice')
G.edge['system_server']['bintvoutservice']['write-read'] = '[open open]'
G.add_edge('system_server','bluetooth')
G.edge['system_server']['bluetooth']['write-read'] = '[setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open]'
G.add_edge('system_server','cbd')
G.edge['system_server']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('system_server','cellgeofenced')
G.edge['system_server']['cellgeofenced']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('system_server','charger_monitor')
G.edge['system_server']['charger_monitor']['write-read'] = '[setopt getopt][open open][write read][append read][open open]'
G.add_edge('system_server','charger_monitor')
G.edge['system_server']['charger_monitor']['write-read'] = '[setopt getopt][open open][write read][append read][open open][open open]'
G.add_edge('system_server','cnd')
G.edge['system_server']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][append read][open open]'
G.add_edge('system_server','connfwexe')
G.edge['system_server']['connfwexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('system_server','debuggerd')
G.edge['system_server']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('system_server','diag_uart_log')
G.edge['system_server']['diag_uart_log']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('system_server','dumpstate')
G.edge['system_server']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read][setattr getattr][write read][append read][open open]'
G.add_edge('system_server','efsks')
G.edge['system_server']['efsks']['write-read'] = '[add_name search][open open]'
G.add_edge('system_server','geomagneticd')
G.edge['system_server']['geomagneticd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open]'
G.add_edge('system_server','gpsd')
G.edge['system_server']['gpsd']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][add_name search][remove_name search][open open]'
G.add_edge('system_server','init_shell')
G.edge['system_server']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('system_server','kiesexe')
G.edge['system_server']['kiesexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('system_server','ks')
G.edge['system_server']['ks']['write-read'] = '[add_name search][open open][append read][open open]'
G.add_edge('system_server','lhd')
G.edge['system_server']['lhd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('system_server','lpm')
G.edge['system_server']['lpm']['write-read'] = '[setopt getopt][open open][write read][append read][open open]'
G.add_edge('system_server','macloader')
G.edge['system_server']['macloader']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('system_server','mdm_helper')
G.edge['system_server']['mdm_helper']['write-read'] = '[open open][append read][open open]'
G.add_edge('system_server','mediaserver')
G.edge['system_server']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][setattr getattr][write read][append read][open open]'
G.add_edge('system_server','mlexe')
G.edge['system_server']['mlexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('system_server','mm-pp-daemon')
G.edge['system_server']['mm-pp-daemon']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('system_server','mm-qcamera-daemon')
G.edge['system_server']['mm-qcamera-daemon']['write-read'] = '[open open][write read][add_name search][remove_name search][open open]'
G.add_edge('system_server','mpdecision')
G.edge['system_server']['mpdecision']['write-read'] = '[setopt getopt][setopt getopt][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('system_server','oneseg_mw')
G.edge['system_server']['oneseg_mw']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('system_server','qcks')
G.edge['system_server']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][append read][open open]'
G.add_edge('system_server','qmuxd')
G.edge['system_server']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][open open][append read][write read][append read][open open]'
G.add_edge('system_server','radio')
G.edge['system_server']['radio']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][setattr getattr][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('system_server','rild')
G.edge['system_server']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('system_server','rmt_storage')
G.edge['system_server']['rmt_storage']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('system_server','sec-ril')
G.edge['system_server']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][add_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][write read][open open]'
G.add_edge('system_server','smdexe')
G.edge['system_server']['smdexe']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('system_server','ssr_setup')
G.edge['system_server']['ssr_setup']['write-read'] = '[open open]'
G.add_edge('system_server','sswap')
G.edge['system_server']['sswap']['write-read'] = '[open open]'
G.add_edge('system_server','surfaceflinger')
G.edge['system_server']['surfaceflinger']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][write read][open open]'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][setsched getsched][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][setsched getsched][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][open open]'
G.add_edge('system_server','thermal-engine')
G.edge['system_server']['thermal-engine']['write-read'] = '[setopt getopt][write read][open open]'
G.add_edge('system_server','ueventd')
G.edge['system_server']['ueventd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('system_server','vm_bms')
G.edge['system_server']['vm_bms']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('system_server','vold')
G.edge['system_server']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('system_server','init_shell')
G.edge['system_server']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('system_server','rild')
G.edge['system_server']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr]'
G.add_edge('system_server','rtcc')
G.edge['system_server']['rtcc']['write-read'] = '[setattr getattr][open open][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('system_server','sec-ril')
G.edge['system_server']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][add_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][write read][open open][setattr getattr]'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][setsched getsched][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][open open][setattr getattr]'
G.add_edge('system_server','at_distributor')
G.edge['system_server']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read]'
G.edge['system_server']['at_distributor']['fill'] = 'red'
G.add_edge('system_server','at_distributor')
G.edge['system_server']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read]'
G.add_edge('system_server','bauthserver')
G.edge['system_server']['bauthserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['system_server']['bauthserver']['fill'] = 'red'
G.add_edge('system_server','bauthserver')
G.edge['system_server']['bauthserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('system_server','bintvoutservice')
G.edge['system_server']['bintvoutservice']['write-read'] = '[open open][write read]'
G.edge['system_server']['bintvoutservice']['fill'] = 'red'
G.add_edge('system_server','bintvoutservice')
G.edge['system_server']['bintvoutservice']['write-read'] = '[open open][write read][append read]'
G.add_edge('system_server','bluetooth')
G.edge['system_server']['bluetooth']['write-read'] = '[setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read]'
G.edge['system_server']['bluetooth']['fill'] = 'red'
G.add_edge('system_server','bluetooth')
G.edge['system_server']['bluetooth']['write-read'] = '[setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][append read]'
G.add_edge('system_server','bootanim')
G.edge['system_server']['bootanim']['write-read'] = '[open open][write read][append read][write read]'
G.edge['system_server']['bootanim']['fill'] = 'red'
G.add_edge('system_server','cbd')
G.edge['system_server']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['system_server']['cbd']['fill'] = 'red'
G.add_edge('system_server','cbd')
G.edge['system_server']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('system_server','cellgeofenced')
G.edge['system_server']['cellgeofenced']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read]'
G.edge['system_server']['cellgeofenced']['fill'] = 'red'
G.add_edge('system_server','cellgeofenced')
G.edge['system_server']['cellgeofenced']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read]'
G.add_edge('system_server','charger_monitor')
G.edge['system_server']['charger_monitor']['write-read'] = '[setopt getopt][open open][write read][append read][open open][open open][write read]'
G.edge['system_server']['charger_monitor']['fill'] = 'red'
G.add_edge('system_server','charger_monitor')
G.edge['system_server']['charger_monitor']['write-read'] = '[setopt getopt][open open][write read][append read][open open][open open][write read][append read]'
G.add_edge('system_server','charger_monitor')
G.edge['system_server']['charger_monitor']['write-read'] = '[setopt getopt][open open][write read][append read][open open][open open][write read][append read][write read]'
G.edge['system_server']['charger_monitor']['fill'] = 'red'
G.add_edge('system_server','charger_monitor')
G.edge['system_server']['charger_monitor']['write-read'] = '[setopt getopt][open open][write read][append read][open open][open open][write read][append read][write read][append read]'
G.add_edge('system_server','cnd')
G.edge['system_server']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][append read][open open][write read]'
G.edge['system_server']['cnd']['fill'] = 'red'
G.add_edge('system_server','cnd')
G.edge['system_server']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][append read][open open][write read][append read]'
G.add_edge('system_server','connfwexe')
G.edge['system_server']['connfwexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read]'
G.edge['system_server']['connfwexe']['fill'] = 'red'
G.add_edge('system_server','connfwexe')
G.edge['system_server']['connfwexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read]'
G.add_edge('system_server','debuggerd')
G.edge['system_server']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['system_server']['debuggerd']['fill'] = 'red'
G.add_edge('system_server','debuggerd')
G.edge['system_server']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('system_server','diag_uart_log')
G.edge['system_server']['diag_uart_log']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['system_server']['diag_uart_log']['fill'] = 'red'
G.add_edge('system_server','diag_uart_log')
G.edge['system_server']['diag_uart_log']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('system_server','dumpstate')
G.edge['system_server']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read][setattr getattr][write read][append read][open open][write read]'
G.edge['system_server']['dumpstate']['fill'] = 'red'
G.add_edge('system_server','dumpstate')
G.edge['system_server']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('system_server','efsks')
G.edge['system_server']['efsks']['write-read'] = '[add_name search][open open][write read]'
G.edge['system_server']['efsks']['fill'] = 'red'
G.add_edge('system_server','efsks')
G.edge['system_server']['efsks']['write-read'] = '[add_name search][open open][write read][append read]'
G.add_edge('system_server','geomagneticd')
G.edge['system_server']['geomagneticd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['system_server']['geomagneticd']['fill'] = 'red'
G.add_edge('system_server','geomagneticd')
G.edge['system_server']['geomagneticd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('system_server','gpsd')
G.edge['system_server']['gpsd']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][add_name search][remove_name search][open open][write read]'
G.edge['system_server']['gpsd']['fill'] = 'red'
G.add_edge('system_server','gpsd')
G.edge['system_server']['gpsd']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('system_server','healthd')
G.edge['system_server']['healthd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][write read][add_name search][remove_name search][open open][write read][append read][write read]'
G.edge['system_server']['healthd']['fill'] = 'red'
G.add_edge('system_server','init_shell')
G.edge['system_server']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['system_server']['init_shell']['fill'] = 'red'
G.add_edge('system_server','init_shell')
G.edge['system_server']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('system_server','jackservice')
G.edge['system_server']['jackservice']['write-read'] = '[add_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['system_server']['jackservice']['fill'] = 'red'
G.add_edge('system_server','kiesexe')
G.edge['system_server']['kiesexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['system_server']['kiesexe']['fill'] = 'red'
G.add_edge('system_server','kiesexe')
G.edge['system_server']['kiesexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('system_server','ks')
G.edge['system_server']['ks']['write-read'] = '[add_name search][open open][append read][open open][write read]'
G.edge['system_server']['ks']['fill'] = 'red'
G.add_edge('system_server','ks')
G.edge['system_server']['ks']['write-read'] = '[add_name search][open open][append read][open open][write read][append read]'
G.add_edge('system_server','lhd')
G.edge['system_server']['lhd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read]'
G.edge['system_server']['lhd']['fill'] = 'red'
G.add_edge('system_server','lhd')
G.edge['system_server']['lhd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read]'
G.add_edge('system_server','lmkd')
G.edge['system_server']['lmkd']['write-read'] = '[remove_name search][write read]'
G.edge['system_server']['lmkd']['fill'] = 'red'
G.add_edge('system_server','lpm')
G.edge['system_server']['lpm']['write-read'] = '[setopt getopt][open open][write read][append read][open open][write read]'
G.edge['system_server']['lpm']['fill'] = 'red'
G.add_edge('system_server','lpm')
G.edge['system_server']['lpm']['write-read'] = '[setopt getopt][open open][write read][append read][open open][write read][append read]'
G.add_edge('system_server','macloader')
G.edge['system_server']['macloader']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['system_server']['macloader']['fill'] = 'red'
G.add_edge('system_server','macloader')
G.edge['system_server']['macloader']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('system_server','mdm_helper')
G.edge['system_server']['mdm_helper']['write-read'] = '[open open][append read][open open][write read]'
G.edge['system_server']['mdm_helper']['fill'] = 'red'
G.add_edge('system_server','mediaserver')
G.edge['system_server']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][setattr getattr][write read][append read][open open][write read]'
G.edge['system_server']['mediaserver']['fill'] = 'red'
G.add_edge('system_server','mediaserver')
G.edge['system_server']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('system_server','mfgloader')
G.edge['system_server']['mfgloader']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read]'
G.edge['system_server']['mfgloader']['fill'] = 'red'
G.add_edge('system_server','mlexe')
G.edge['system_server']['mlexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['system_server']['mlexe']['fill'] = 'red'
G.add_edge('system_server','mlexe')
G.edge['system_server']['mlexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('system_server','mm-pp-daemon')
G.edge['system_server']['mm-pp-daemon']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['system_server']['mm-pp-daemon']['fill'] = 'red'
G.add_edge('system_server','mm-pp-daemon')
G.edge['system_server']['mm-pp-daemon']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('system_server','mm-pp-daemon')
G.edge['system_server']['mm-pp-daemon']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read]'
G.edge['system_server']['mm-pp-daemon']['fill'] = 'red'
G.add_edge('system_server','mm-qcamera-daemon')
G.edge['system_server']['mm-qcamera-daemon']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['system_server']['mm-qcamera-daemon']['fill'] = 'red'
G.add_edge('system_server','mm-qcamera-daemon')
G.edge['system_server']['mm-qcamera-daemon']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('system_server','mpdecision')
G.edge['system_server']['mpdecision']['write-read'] = '[setopt getopt][setopt getopt][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['system_server']['mpdecision']['fill'] = 'red'
G.add_edge('system_server','mpdecision')
G.edge['system_server']['mpdecision']['write-read'] = '[setopt getopt][setopt getopt][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('system_server','mpdecision')
G.edge['system_server']['mpdecision']['write-read'] = '[setopt getopt][setopt getopt][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][write read]'
G.edge['system_server']['mpdecision']['fill'] = 'red'
G.add_edge('system_server','netd')
G.edge['system_server']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][write read]'
G.edge['system_server']['netd']['fill'] = 'red'
G.add_edge('system_server','netmgrd')
G.edge['system_server']['netmgrd']['write-read'] = '[open open][open open][write read][write read][add_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['system_server']['netmgrd']['fill'] = 'red'
G.add_edge('system_server','nfc')
G.edge['system_server']['nfc']['write-read'] = '[open open][setattr getattr][write read][append read][write read]'
G.edge['system_server']['nfc']['fill'] = 'red'
G.add_edge('system_server','oneseg_mw')
G.edge['system_server']['oneseg_mw']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['system_server']['oneseg_mw']['fill'] = 'red'
G.add_edge('system_server','oneseg_mw')
G.edge['system_server']['oneseg_mw']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('system_server','perfd')
G.edge['system_server']['perfd']['write-read'] = '[setopt getopt][write read]'
G.edge['system_server']['perfd']['fill'] = 'red'
G.add_edge('system_server','qcks')
G.edge['system_server']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][append read][open open][write read]'
G.edge['system_server']['qcks']['fill'] = 'red'
G.add_edge('system_server','qcks')
G.edge['system_server']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][append read][open open][write read][append read]'
G.add_edge('system_server','qmuxd')
G.edge['system_server']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][open open][append read][write read][append read][open open][write read]'
G.edge['system_server']['qmuxd']['fill'] = 'red'
G.add_edge('system_server','qmuxd')
G.edge['system_server']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][open open][append read][write read][append read][open open][write read][append read]'
G.add_edge('system_server','qosmgr')
G.edge['system_server']['qosmgr']['write-read'] = '[write read]'
G.edge['system_server']['qosmgr']['fill'] = 'red'
G.add_edge('system_server','radio')
G.edge['system_server']['radio']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][append read]'
G.add_edge('system_server','rild')
G.edge['system_server']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['system_server']['rild']['fill'] = 'red'
G.add_edge('system_server','rild')
G.edge['system_server']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('system_server','rmt_storage')
G.edge['system_server']['rmt_storage']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read]'
G.edge['system_server']['rmt_storage']['fill'] = 'red'
G.add_edge('system_server','rmt_storage')
G.edge['system_server']['rmt_storage']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read]'
G.add_edge('system_server','rtcc')
G.edge['system_server']['rtcc']['write-read'] = '[setattr getattr][open open][write read][add_name search][remove_name search][setattr getattr][write read]'
G.edge['system_server']['rtcc']['fill'] = 'red'
G.add_edge('system_server','sec-ril')
G.edge['system_server']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][add_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][write read][open open][setattr getattr][write read]'
G.edge['system_server']['sec-ril']['fill'] = 'red'
G.add_edge('system_server','sec-ril')
G.edge['system_server']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][add_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][write read][open open][setattr getattr][write read][append read]'
G.add_edge('system_server','sensorhubservice')
G.edge['system_server']['sensorhubservice']['write-read'] = '[write read]'
G.edge['system_server']['sensorhubservice']['fill'] = 'red'
G.add_edge('system_server','smdexe')
G.edge['system_server']['smdexe']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['system_server']['smdexe']['fill'] = 'red'
G.add_edge('system_server','smdexe')
G.edge['system_server']['smdexe']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('system_server','ssr_setup')
G.edge['system_server']['ssr_setup']['write-read'] = '[open open][write read]'
G.edge['system_server']['ssr_setup']['fill'] = 'red'
G.add_edge('system_server','ssr_setup')
G.edge['system_server']['ssr_setup']['write-read'] = '[open open][write read][append read]'
G.add_edge('system_server','sswap')
G.edge['system_server']['sswap']['write-read'] = '[open open][write read]'
G.edge['system_server']['sswap']['fill'] = 'red'
G.add_edge('system_server','sswap')
G.edge['system_server']['sswap']['write-read'] = '[open open][write read][append read]'
G.add_edge('system_server','surfaceflinger')
G.edge['system_server']['surfaceflinger']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][write read][open open][write read]'
G.edge['system_server']['surfaceflinger']['fill'] = 'red'
G.add_edge('system_server','surfaceflinger')
G.edge['system_server']['surfaceflinger']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][write read][open open][write read][append read]'
G.add_edge('system_server','surfaceflinger')
G.edge['system_server']['surfaceflinger']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][write read][open open][write read][append read][write read]'
G.edge['system_server']['surfaceflinger']['fill'] = 'red'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][setsched getsched][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read]'
G.edge['system_server']['system_server']['fill'] = 'red'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][setsched getsched][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][append read]'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][setsched getsched][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][append read][write read]'
G.edge['system_server']['system_server']['fill'] = 'red'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][setsched getsched][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][append read][write read][append read]'
G.add_edge('system_server','thermald')
G.edge['system_server']['thermald']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read]'
G.edge['system_server']['thermald']['fill'] = 'red'
G.add_edge('system_server','thermal-engine')
G.edge['system_server']['thermal-engine']['write-read'] = '[setopt getopt][write read][open open][write read]'
G.edge['system_server']['thermal-engine']['fill'] = 'red'
G.add_edge('system_server','thermal-engine')
G.edge['system_server']['thermal-engine']['write-read'] = '[setopt getopt][write read][open open][write read][append read]'
G.add_edge('system_server','thermal-engine')
G.edge['system_server']['thermal-engine']['write-read'] = '[setopt getopt][write read][open open][write read][append read][write read]'
G.edge['system_server']['thermal-engine']['fill'] = 'red'
G.add_edge('system_server','ueventd')
G.edge['system_server']['ueventd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['system_server']['ueventd']['fill'] = 'red'
G.add_edge('system_server','ueventd')
G.edge['system_server']['ueventd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('system_server','vm_bms')
G.edge['system_server']['vm_bms']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['system_server']['vm_bms']['fill'] = 'red'
G.add_edge('system_server','vm_bms')
G.edge['system_server']['vm_bms']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('system_server','vmwared')
G.edge['system_server']['vmwared']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['system_server']['vmwared']['fill'] = 'red'
G.add_edge('system_server','vold')
G.edge['system_server']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read]'
G.edge['system_server']['vold']['fill'] = 'red'
G.add_edge('system_server','vold')
G.edge['system_server']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read]'
G.add_edge('system_server','zygote')
G.edge['system_server']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][write read][write read]'
G.edge['system_server']['zygote']['fill'] = 'red'
G.add_edge('system_server','at_distributor')
G.edge['system_server']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('system_server','bauthserver')
G.edge['system_server']['bauthserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('system_server','bintvoutservice')
G.edge['system_server']['bintvoutservice']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('system_server','bluetooth')
G.edge['system_server']['bluetooth']['write-read'] = '[setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open]'
G.add_edge('system_server','cbd')
G.edge['system_server']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('system_server','cellgeofenced')
G.edge['system_server']['cellgeofenced']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('system_server','charger_monitor')
G.edge['system_server']['charger_monitor']['write-read'] = '[setopt getopt][open open][write read][append read][open open][open open][write read][append read][write read][append read][open open]'
G.add_edge('system_server','charger_monitor')
G.edge['system_server']['charger_monitor']['write-read'] = '[setopt getopt][open open][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open]'
G.add_edge('system_server','cnd')
G.edge['system_server']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][append read][open open][write read][append read][open open]'
G.add_edge('system_server','connfwexe')
G.edge['system_server']['connfwexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('system_server','debuggerd')
G.edge['system_server']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('system_server','diag_uart_log')
G.edge['system_server']['diag_uart_log']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('system_server','dumpstate')
G.edge['system_server']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read][setattr getattr][write read][append read][open open][write read][append read][open open]'
G.add_edge('system_server','efsks')
G.edge['system_server']['efsks']['write-read'] = '[add_name search][open open][write read][append read][open open]'
G.add_edge('system_server','geomagneticd')
G.edge['system_server']['geomagneticd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('system_server','gpsd')
G.edge['system_server']['gpsd']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('system_server','init_shell')
G.edge['system_server']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('system_server','kiesexe')
G.edge['system_server']['kiesexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('system_server','ks')
G.edge['system_server']['ks']['write-read'] = '[add_name search][open open][append read][open open][write read][append read][open open]'
G.add_edge('system_server','lhd')
G.edge['system_server']['lhd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('system_server','lpm')
G.edge['system_server']['lpm']['write-read'] = '[setopt getopt][open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('system_server','macloader')
G.edge['system_server']['macloader']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('system_server','mdm_helper')
G.edge['system_server']['mdm_helper']['write-read'] = '[open open][append read][open open][write read][open open]'
G.add_edge('system_server','mediaserver')
G.edge['system_server']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][setattr getattr][write read][append read][open open][write read][append read][open open]'
G.add_edge('system_server','mlexe')
G.edge['system_server']['mlexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('system_server','mm-pp-daemon')
G.edge['system_server']['mm-pp-daemon']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read][open open]'
G.add_edge('system_server','mm-qcamera-daemon')
G.edge['system_server']['mm-qcamera-daemon']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('system_server','mpdecision')
G.edge['system_server']['mpdecision']['write-read'] = '[setopt getopt][setopt getopt][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][write read][open open]'
G.add_edge('system_server','oneseg_mw')
G.edge['system_server']['oneseg_mw']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('system_server','qcks')
G.edge['system_server']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][append read][open open][write read][append read][open open]'
G.add_edge('system_server','qmuxd')
G.edge['system_server']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][open open][append read][write read][append read][open open][write read][append read][open open]'
G.add_edge('system_server','radio')
G.edge['system_server']['radio']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][append read][open open]'
G.add_edge('system_server','rild')
G.edge['system_server']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('system_server','rmt_storage')
G.edge['system_server']['rmt_storage']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('system_server','sec-ril')
G.edge['system_server']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][add_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('system_server','smdexe')
G.edge['system_server']['smdexe']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('system_server','ssr_setup')
G.edge['system_server']['ssr_setup']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('system_server','sswap')
G.edge['system_server']['sswap']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('system_server','surfaceflinger')
G.edge['system_server']['surfaceflinger']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][write read][open open][write read][append read][write read][open open]'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][setsched getsched][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][append read][write read][append read][open open]'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][setsched getsched][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open]'
G.add_edge('system_server','thermal-engine')
G.edge['system_server']['thermal-engine']['write-read'] = '[setopt getopt][write read][open open][write read][append read][write read][open open]'
G.add_edge('system_server','ueventd')
G.edge['system_server']['ueventd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('system_server','vm_bms')
G.edge['system_server']['vm_bms']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('system_server','vold')
G.edge['system_server']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('system_server','init_shell')
G.edge['system_server']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('system_server','rild')
G.edge['system_server']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('system_server','rtcc')
G.edge['system_server']['rtcc']['write-read'] = '[setattr getattr][open open][write read][add_name search][remove_name search][setattr getattr][write read][setattr getattr]'
G.add_edge('system_server','sec-ril')
G.edge['system_server']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][add_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][write read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][setsched getsched][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr]'
G.add_edge('system_server','at_distributor')
G.edge['system_server']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read]'
G.edge['system_server']['at_distributor']['fill'] = 'red'
G.add_edge('system_server','at_distributor')
G.edge['system_server']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read]'
G.add_edge('system_server','bauthserver')
G.edge['system_server']['bauthserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read]'
G.edge['system_server']['bauthserver']['fill'] = 'red'
G.add_edge('system_server','bauthserver')
G.edge['system_server']['bauthserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read]'
G.add_edge('system_server','bintvoutservice')
G.edge['system_server']['bintvoutservice']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['system_server']['bintvoutservice']['fill'] = 'red'
G.add_edge('system_server','bintvoutservice')
G.edge['system_server']['bintvoutservice']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('system_server','bluetooth')
G.edge['system_server']['bluetooth']['write-read'] = '[setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][write read]'
G.edge['system_server']['bluetooth']['fill'] = 'red'
G.add_edge('system_server','bluetooth')
G.edge['system_server']['bluetooth']['write-read'] = '[setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][write read][append read]'
G.add_edge('system_server','bootanim')
G.edge['system_server']['bootanim']['write-read'] = '[open open][write read][append read][write read][write read]'
G.edge['system_server']['bootanim']['fill'] = 'red'
G.add_edge('system_server','cbd')
G.edge['system_server']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read]'
G.edge['system_server']['cbd']['fill'] = 'red'
G.add_edge('system_server','cbd')
G.edge['system_server']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read]'
G.add_edge('system_server','cellgeofenced')
G.edge['system_server']['cellgeofenced']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read]'
G.edge['system_server']['cellgeofenced']['fill'] = 'red'
G.add_edge('system_server','cellgeofenced')
G.edge['system_server']['cellgeofenced']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read]'
G.add_edge('system_server','charger_monitor')
G.edge['system_server']['charger_monitor']['write-read'] = '[setopt getopt][open open][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read]'
G.edge['system_server']['charger_monitor']['fill'] = 'red'
G.add_edge('system_server','charger_monitor')
G.edge['system_server']['charger_monitor']['write-read'] = '[setopt getopt][open open][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read]'
G.add_edge('system_server','charger_monitor')
G.edge['system_server']['charger_monitor']['write-read'] = '[setopt getopt][open open][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read]'
G.edge['system_server']['charger_monitor']['fill'] = 'red'
G.add_edge('system_server','charger_monitor')
G.edge['system_server']['charger_monitor']['write-read'] = '[setopt getopt][open open][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read]'
G.add_edge('system_server','cnd')
G.edge['system_server']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][append read][open open][write read][append read][open open][write read]'
G.edge['system_server']['cnd']['fill'] = 'red'
G.add_edge('system_server','cnd')
G.edge['system_server']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][append read][open open][write read][append read][open open][write read][append read]'
G.add_edge('system_server','connfwexe')
G.edge['system_server']['connfwexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read]'
G.edge['system_server']['connfwexe']['fill'] = 'red'
G.add_edge('system_server','connfwexe')
G.edge['system_server']['connfwexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read]'
G.add_edge('system_server','debuggerd')
G.edge['system_server']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read]'
G.edge['system_server']['debuggerd']['fill'] = 'red'
G.add_edge('system_server','debuggerd')
G.edge['system_server']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read]'
G.add_edge('system_server','diag_uart_log')
G.edge['system_server']['diag_uart_log']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read]'
G.edge['system_server']['diag_uart_log']['fill'] = 'red'
G.add_edge('system_server','diag_uart_log')
G.edge['system_server']['diag_uart_log']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read]'
G.add_edge('system_server','dumpstate')
G.edge['system_server']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read][setattr getattr][write read][append read][open open][write read][append read][open open][write read]'
G.edge['system_server']['dumpstate']['fill'] = 'red'
G.add_edge('system_server','dumpstate')
G.edge['system_server']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read]'
G.add_edge('system_server','efsks')
G.edge['system_server']['efsks']['write-read'] = '[add_name search][open open][write read][append read][open open][write read]'
G.edge['system_server']['efsks']['fill'] = 'red'
G.add_edge('system_server','efsks')
G.edge['system_server']['efsks']['write-read'] = '[add_name search][open open][write read][append read][open open][write read][append read]'
G.add_edge('system_server','geomagneticd')
G.edge['system_server']['geomagneticd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read]'
G.edge['system_server']['geomagneticd']['fill'] = 'red'
G.add_edge('system_server','geomagneticd')
G.edge['system_server']['geomagneticd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read]'
G.add_edge('system_server','gpsd')
G.edge['system_server']['gpsd']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][add_name search][remove_name search][open open][write read][append read][open open][write read]'
G.edge['system_server']['gpsd']['fill'] = 'red'
G.add_edge('system_server','gpsd')
G.edge['system_server']['gpsd']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read]'
G.add_edge('system_server','healthd')
G.edge['system_server']['healthd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][write read][add_name search][remove_name search][open open][write read][append read][write read][write read]'
G.edge['system_server']['healthd']['fill'] = 'red'
G.add_edge('system_server','init_shell')
G.edge['system_server']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['system_server']['init_shell']['fill'] = 'red'
G.add_edge('system_server','init_shell')
G.edge['system_server']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('system_server','jackservice')
G.edge['system_server']['jackservice']['write-read'] = '[add_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][write read]'
G.edge['system_server']['jackservice']['fill'] = 'red'
G.add_edge('system_server','kiesexe')
G.edge['system_server']['kiesexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read]'
G.edge['system_server']['kiesexe']['fill'] = 'red'
G.add_edge('system_server','kiesexe')
G.edge['system_server']['kiesexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read]'
G.add_edge('system_server','ks')
G.edge['system_server']['ks']['write-read'] = '[add_name search][open open][append read][open open][write read][append read][open open][write read]'
G.edge['system_server']['ks']['fill'] = 'red'
G.add_edge('system_server','ks')
G.edge['system_server']['ks']['write-read'] = '[add_name search][open open][append read][open open][write read][append read][open open][write read][append read]'
G.add_edge('system_server','lhd')
G.edge['system_server']['lhd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read]'
G.edge['system_server']['lhd']['fill'] = 'red'
G.add_edge('system_server','lhd')
G.edge['system_server']['lhd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read]'
G.add_edge('system_server','lmkd')
G.edge['system_server']['lmkd']['write-read'] = '[remove_name search][write read][write read]'
G.edge['system_server']['lmkd']['fill'] = 'red'
G.add_edge('system_server','lpm')
G.edge['system_server']['lpm']['write-read'] = '[setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read]'
G.edge['system_server']['lpm']['fill'] = 'red'
G.add_edge('system_server','lpm')
G.edge['system_server']['lpm']['write-read'] = '[setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read]'
G.add_edge('system_server','macloader')
G.edge['system_server']['macloader']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read]'
G.edge['system_server']['macloader']['fill'] = 'red'
G.add_edge('system_server','macloader')
G.edge['system_server']['macloader']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][append read]'
G.add_edge('system_server','mdm_helper')
G.edge['system_server']['mdm_helper']['write-read'] = '[open open][append read][open open][write read][open open][write read]'
G.edge['system_server']['mdm_helper']['fill'] = 'red'
G.add_edge('system_server','mediaserver')
G.edge['system_server']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][setattr getattr][write read][append read][open open][write read][append read][open open][write read]'
G.edge['system_server']['mediaserver']['fill'] = 'red'
G.add_edge('system_server','mediaserver')
G.edge['system_server']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read]'
G.add_edge('system_server','mfgloader')
G.edge['system_server']['mfgloader']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read][write read]'
G.edge['system_server']['mfgloader']['fill'] = 'red'
G.add_edge('system_server','mlexe')
G.edge['system_server']['mlexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read]'
G.edge['system_server']['mlexe']['fill'] = 'red'
G.add_edge('system_server','mlexe')
G.edge['system_server']['mlexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read]'
G.add_edge('system_server','mm-pp-daemon')
G.edge['system_server']['mm-pp-daemon']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read][open open][write read]'
G.edge['system_server']['mm-pp-daemon']['fill'] = 'red'
G.add_edge('system_server','mm-pp-daemon')
G.edge['system_server']['mm-pp-daemon']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read][open open][write read][append read]'
G.add_edge('system_server','mm-pp-daemon')
G.edge['system_server']['mm-pp-daemon']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][write read]'
G.edge['system_server']['mm-pp-daemon']['fill'] = 'red'
G.add_edge('system_server','mm-qcamera-daemon')
G.edge['system_server']['mm-qcamera-daemon']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read]'
G.edge['system_server']['mm-qcamera-daemon']['fill'] = 'red'
G.add_edge('system_server','mm-qcamera-daemon')
G.edge['system_server']['mm-qcamera-daemon']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read]'
G.add_edge('system_server','mpdecision')
G.edge['system_server']['mpdecision']['write-read'] = '[setopt getopt][setopt getopt][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][write read][open open][write read]'
G.edge['system_server']['mpdecision']['fill'] = 'red'
G.add_edge('system_server','mpdecision')
G.edge['system_server']['mpdecision']['write-read'] = '[setopt getopt][setopt getopt][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][write read][open open][write read][append read]'
G.add_edge('system_server','mpdecision')
G.edge['system_server']['mpdecision']['write-read'] = '[setopt getopt][setopt getopt][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][write read][open open][write read][append read][write read]'
G.edge['system_server']['mpdecision']['fill'] = 'red'
G.add_edge('system_server','netd')
G.edge['system_server']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][write read][write read]'
G.edge['system_server']['netd']['fill'] = 'red'
G.add_edge('system_server','netmgrd')
G.edge['system_server']['netmgrd']['write-read'] = '[open open][open open][write read][write read][add_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][write read][write read]'
G.edge['system_server']['netmgrd']['fill'] = 'red'
G.add_edge('system_server','nfc')
G.edge['system_server']['nfc']['write-read'] = '[open open][setattr getattr][write read][append read][write read][write read]'
G.edge['system_server']['nfc']['fill'] = 'red'
G.add_edge('system_server','oneseg_mw')
G.edge['system_server']['oneseg_mw']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read]'
G.edge['system_server']['oneseg_mw']['fill'] = 'red'
G.add_edge('system_server','oneseg_mw')
G.edge['system_server']['oneseg_mw']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read]'
G.add_edge('system_server','perfd')
G.edge['system_server']['perfd']['write-read'] = '[setopt getopt][write read][write read]'
G.edge['system_server']['perfd']['fill'] = 'red'
G.add_edge('system_server','qcks')
G.edge['system_server']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][append read][open open][write read][append read][open open][write read]'
G.edge['system_server']['qcks']['fill'] = 'red'
G.add_edge('system_server','qcks')
G.edge['system_server']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][append read][open open][write read][append read][open open][write read][append read]'
G.add_edge('system_server','qmuxd')
G.edge['system_server']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][open open][append read][write read][append read][open open][write read][append read][open open][write read]'
G.edge['system_server']['qmuxd']['fill'] = 'red'
G.add_edge('system_server','qmuxd')
G.edge['system_server']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][open open][append read][write read][append read][open open][write read][append read][open open][write read][append read]'
G.add_edge('system_server','qosmgr')
G.edge['system_server']['qosmgr']['write-read'] = '[write read][write read]'
G.edge['system_server']['qosmgr']['fill'] = 'red'
G.add_edge('system_server','radio')
G.edge['system_server']['radio']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][append read][open open][append read]'
G.add_edge('system_server','rild')
G.edge['system_server']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['system_server']['rild']['fill'] = 'red'
G.add_edge('system_server','rild')
G.edge['system_server']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('system_server','rmt_storage')
G.edge['system_server']['rmt_storage']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read]'
G.edge['system_server']['rmt_storage']['fill'] = 'red'
G.add_edge('system_server','rmt_storage')
G.edge['system_server']['rmt_storage']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read]'
G.add_edge('system_server','rtcc')
G.edge['system_server']['rtcc']['write-read'] = '[setattr getattr][open open][write read][add_name search][remove_name search][setattr getattr][write read][setattr getattr][write read]'
G.edge['system_server']['rtcc']['fill'] = 'red'
G.add_edge('system_server','sec-ril')
G.edge['system_server']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][add_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['system_server']['sec-ril']['fill'] = 'red'
G.add_edge('system_server','sec-ril')
G.edge['system_server']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][add_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('system_server','sensorhubservice')
G.edge['system_server']['sensorhubservice']['write-read'] = '[write read][write read]'
G.edge['system_server']['sensorhubservice']['fill'] = 'red'
G.add_edge('system_server','smdexe')
G.edge['system_server']['smdexe']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read]'
G.edge['system_server']['smdexe']['fill'] = 'red'
G.add_edge('system_server','smdexe')
G.edge['system_server']['smdexe']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][append read]'
G.add_edge('system_server','ssr_setup')
G.edge['system_server']['ssr_setup']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['system_server']['ssr_setup']['fill'] = 'red'
G.add_edge('system_server','ssr_setup')
G.edge['system_server']['ssr_setup']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('system_server','sswap')
G.edge['system_server']['sswap']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['system_server']['sswap']['fill'] = 'red'
G.add_edge('system_server','sswap')
G.edge['system_server']['sswap']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('system_server','surfaceflinger')
G.edge['system_server']['surfaceflinger']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][write read][open open][write read][append read][write read][open open][write read]'
G.edge['system_server']['surfaceflinger']['fill'] = 'red'
G.add_edge('system_server','surfaceflinger')
G.edge['system_server']['surfaceflinger']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][write read][open open][write read][append read][write read][open open][write read][append read]'
G.add_edge('system_server','surfaceflinger')
G.edge['system_server']['surfaceflinger']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][write read][open open][write read][append read][write read][open open][write read][append read][write read]'
G.edge['system_server']['surfaceflinger']['fill'] = 'red'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][setsched getsched][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read]'
G.edge['system_server']['system_server']['fill'] = 'red'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][setsched getsched][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read]'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][setsched getsched][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read]'
G.edge['system_server']['system_server']['fill'] = 'red'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][setsched getsched][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read]'
G.add_edge('system_server','thermald')
G.edge['system_server']['thermald']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][write read]'
G.edge['system_server']['thermald']['fill'] = 'red'
G.add_edge('system_server','thermal-engine')
G.edge['system_server']['thermal-engine']['write-read'] = '[setopt getopt][write read][open open][write read][append read][write read][open open][write read]'
G.edge['system_server']['thermal-engine']['fill'] = 'red'
G.add_edge('system_server','thermal-engine')
G.edge['system_server']['thermal-engine']['write-read'] = '[setopt getopt][write read][open open][write read][append read][write read][open open][write read][append read]'
G.add_edge('system_server','thermal-engine')
G.edge['system_server']['thermal-engine']['write-read'] = '[setopt getopt][write read][open open][write read][append read][write read][open open][write read][append read][write read]'
G.edge['system_server']['thermal-engine']['fill'] = 'red'
G.add_edge('system_server','ueventd')
G.edge['system_server']['ueventd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read]'
G.edge['system_server']['ueventd']['fill'] = 'red'
G.add_edge('system_server','ueventd')
G.edge['system_server']['ueventd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read]'
G.add_edge('system_server','vm_bms')
G.edge['system_server']['vm_bms']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read]'
G.edge['system_server']['vm_bms']['fill'] = 'red'
G.add_edge('system_server','vm_bms')
G.edge['system_server']['vm_bms']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][append read]'
G.add_edge('system_server','vmwared')
G.edge['system_server']['vmwared']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][write read][write read]'
G.edge['system_server']['vmwared']['fill'] = 'red'
G.add_edge('system_server','vold')
G.edge['system_server']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read]'
G.edge['system_server']['vold']['fill'] = 'red'
G.add_edge('system_server','vold')
G.edge['system_server']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read]'
G.add_edge('system_server','zygote')
G.edge['system_server']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][write read][write read][write read]'
G.edge['system_server']['zygote']['fill'] = 'red'
G.add_edge('ueventd','at_distributor')
G.edge['ueventd']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('ueventd','bauthserver')
G.edge['ueventd']['bauthserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('ueventd','bintvoutservice')
G.edge['ueventd']['bintvoutservice']['write-read'] = '[open open]'
G.add_edge('ueventd','bluetooth')
G.edge['ueventd']['bluetooth']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('ueventd','cbd')
G.edge['ueventd']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('ueventd','cellgeofenced')
G.edge['ueventd']['cellgeofenced']['write-read'] = '[open open]'
G.add_edge('ueventd','charger_monitor')
G.edge['ueventd']['charger_monitor']['write-read'] = '[setopt getopt][open open]'
G.add_edge('ueventd','charger_monitor')
G.edge['ueventd']['charger_monitor']['write-read'] = '[setopt getopt][open open][open open]'
G.add_edge('ueventd','cnd')
G.edge['ueventd']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open]'
G.add_edge('ueventd','connfwexe')
G.edge['ueventd']['connfwexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('ueventd','debuggerd')
G.edge['ueventd']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('ueventd','diag_uart_log')
G.edge['ueventd']['diag_uart_log']['write-read'] = '[open open]'
G.add_edge('ueventd','dumpstate')
G.edge['ueventd']['dumpstate']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('ueventd','efsks')
G.edge['ueventd']['efsks']['write-read'] = '[open open]'
G.add_edge('ueventd','geomagneticd')
G.edge['ueventd']['geomagneticd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open]'
G.add_edge('ueventd','gpsd')
G.edge['ueventd']['gpsd']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('ueventd','init_shell')
G.edge['ueventd']['init_shell']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('ueventd','kiesexe')
G.edge['ueventd']['kiesexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('ueventd','ks')
G.edge['ueventd']['ks']['write-read'] = '[open open]'
G.add_edge('ueventd','lhd')
G.edge['ueventd']['lhd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('ueventd','lpm')
G.edge['ueventd']['lpm']['write-read'] = '[setopt getopt][open open]'
G.add_edge('ueventd','macloader')
G.edge['ueventd']['macloader']['write-read'] = '[open open]'
G.add_edge('ueventd','mdm_helper')
G.edge['ueventd']['mdm_helper']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('ueventd','mediaserver')
G.edge['ueventd']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read][open open]'
G.add_edge('ueventd','mlexe')
G.edge['ueventd']['mlexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('ueventd','mm-pp-daemon')
G.edge['ueventd']['mm-pp-daemon']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('ueventd','mm-qcamera-daemon')
G.edge['ueventd']['mm-qcamera-daemon']['write-read'] = '[open open][write read][add_name search][remove_name search][open open]'
G.add_edge('ueventd','mpdecision')
G.edge['ueventd']['mpdecision']['write-read'] = '[setopt getopt][setopt getopt][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('ueventd','oneseg_mw')
G.edge['ueventd']['oneseg_mw']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('ueventd','qcks')
G.edge['ueventd']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('ueventd','qmuxd')
G.edge['ueventd']['qmuxd']['write-read'] = '[open open]'
G.add_edge('ueventd','radio')
G.edge['ueventd']['radio']['write-read'] = '[open open]'
G.add_edge('ueventd','rild')
G.edge['ueventd']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('ueventd','rmt_storage')
G.edge['ueventd']['rmt_storage']['write-read'] = '[open open]'
G.add_edge('ueventd','sec-ril')
G.edge['ueventd']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('ueventd','smdexe')
G.edge['ueventd']['smdexe']['write-read'] = '[open open]'
G.add_edge('ueventd','ssr_setup')
G.edge['ueventd']['ssr_setup']['write-read'] = '[open open]'
G.add_edge('ueventd','sswap')
G.edge['ueventd']['sswap']['write-read'] = '[open open]'
G.add_edge('ueventd','surfaceflinger')
G.edge['ueventd']['surfaceflinger']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open]'
G.add_edge('ueventd','system_server')
G.edge['ueventd']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('ueventd','system_server')
G.edge['ueventd']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open]'
G.add_edge('ueventd','thermal-engine')
G.edge['ueventd']['thermal-engine']['write-read'] = '[setopt getopt][open open]'
G.add_edge('ueventd','ueventd')
G.edge['ueventd']['ueventd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][setattr getattr][relabelto relabelfrom][relabelto relabelfrom][relabelto relabelfrom][relabelto relabelfrom][open open][setattr getattr][relabelto relabelfrom][open open][write read][append read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('ueventd','vm_bms')
G.edge['ueventd']['vm_bms']['write-read'] = '[open open]'
G.add_edge('ueventd','vold')
G.edge['ueventd']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][append read][add_name search][remove_name search][open open]'
G.add_edge('ueventd','init_shell')
G.edge['ueventd']['init_shell']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('ueventd','rild')
G.edge['ueventd']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('ueventd','rtcc')
G.edge['ueventd']['rtcc']['write-read'] = '[setattr getattr]'
G.add_edge('ueventd','sec-ril')
G.edge['ueventd']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('ueventd','system_server')
G.edge['ueventd']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr]'
G.add_edge('ueventd','at_distributor')
G.edge['ueventd']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['ueventd']['at_distributor']['fill'] = 'red'
G.add_edge('ueventd','at_distributor')
G.edge['ueventd']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('ueventd','bauthserver')
G.edge['ueventd']['bauthserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['ueventd']['bauthserver']['fill'] = 'red'
G.add_edge('ueventd','bauthserver')
G.edge['ueventd']['bauthserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('ueventd','bintvoutservice')
G.edge['ueventd']['bintvoutservice']['write-read'] = '[open open][write read]'
G.edge['ueventd']['bintvoutservice']['fill'] = 'red'
G.add_edge('ueventd','bintvoutservice')
G.edge['ueventd']['bintvoutservice']['write-read'] = '[open open][write read][append read]'
G.add_edge('ueventd','bluetooth')
G.edge['ueventd']['bluetooth']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['ueventd']['bluetooth']['fill'] = 'red'
G.add_edge('ueventd','bluetooth')
G.edge['ueventd']['bluetooth']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('ueventd','bootanim')
G.edge['ueventd']['bootanim']['write-read'] = '[write read]'
G.edge['ueventd']['bootanim']['fill'] = 'red'
G.add_edge('ueventd','cbd')
G.edge['ueventd']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['ueventd']['cbd']['fill'] = 'red'
G.add_edge('ueventd','cbd')
G.edge['ueventd']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('ueventd','cellgeofenced')
G.edge['ueventd']['cellgeofenced']['write-read'] = '[open open][write read]'
G.edge['ueventd']['cellgeofenced']['fill'] = 'red'
G.add_edge('ueventd','cellgeofenced')
G.edge['ueventd']['cellgeofenced']['write-read'] = '[open open][write read][append read]'
G.add_edge('ueventd','charger_monitor')
G.edge['ueventd']['charger_monitor']['write-read'] = '[setopt getopt][open open][open open][write read]'
G.edge['ueventd']['charger_monitor']['fill'] = 'red'
G.add_edge('ueventd','charger_monitor')
G.edge['ueventd']['charger_monitor']['write-read'] = '[setopt getopt][open open][open open][write read][append read]'
G.add_edge('ueventd','charger_monitor')
G.edge['ueventd']['charger_monitor']['write-read'] = '[setopt getopt][open open][open open][write read][append read][write read]'
G.edge['ueventd']['charger_monitor']['fill'] = 'red'
G.add_edge('ueventd','charger_monitor')
G.edge['ueventd']['charger_monitor']['write-read'] = '[setopt getopt][open open][open open][write read][append read][write read][append read]'
G.add_edge('ueventd','cnd')
G.edge['ueventd']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['ueventd']['cnd']['fill'] = 'red'
G.add_edge('ueventd','cnd')
G.edge['ueventd']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('ueventd','connfwexe')
G.edge['ueventd']['connfwexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['ueventd']['connfwexe']['fill'] = 'red'
G.add_edge('ueventd','connfwexe')
G.edge['ueventd']['connfwexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('ueventd','debuggerd')
G.edge['ueventd']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read]'
G.edge['ueventd']['debuggerd']['fill'] = 'red'
G.add_edge('ueventd','debuggerd')
G.edge['ueventd']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('ueventd','diag_uart_log')
G.edge['ueventd']['diag_uart_log']['write-read'] = '[open open][write read]'
G.edge['ueventd']['diag_uart_log']['fill'] = 'red'
G.add_edge('ueventd','diag_uart_log')
G.edge['ueventd']['diag_uart_log']['write-read'] = '[open open][write read][append read]'
G.add_edge('ueventd','dumpstate')
G.edge['ueventd']['dumpstate']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][write read]'
G.edge['ueventd']['dumpstate']['fill'] = 'red'
G.add_edge('ueventd','dumpstate')
G.edge['ueventd']['dumpstate']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('ueventd','efsks')
G.edge['ueventd']['efsks']['write-read'] = '[open open][write read]'
G.edge['ueventd']['efsks']['fill'] = 'red'
G.add_edge('ueventd','efsks')
G.edge['ueventd']['efsks']['write-read'] = '[open open][write read][append read]'
G.add_edge('ueventd','geomagneticd')
G.edge['ueventd']['geomagneticd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['ueventd']['geomagneticd']['fill'] = 'red'
G.add_edge('ueventd','geomagneticd')
G.edge['ueventd']['geomagneticd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('ueventd','gpsd')
G.edge['ueventd']['gpsd']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read]'
G.edge['ueventd']['gpsd']['fill'] = 'red'
G.add_edge('ueventd','gpsd')
G.edge['ueventd']['gpsd']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('ueventd','healthd')
G.edge['ueventd']['healthd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read]'
G.edge['ueventd']['healthd']['fill'] = 'red'
G.add_edge('ueventd','init_shell')
G.edge['ueventd']['init_shell']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['ueventd']['init_shell']['fill'] = 'red'
G.add_edge('ueventd','init_shell')
G.edge['ueventd']['init_shell']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('ueventd','jackservice')
G.edge['ueventd']['jackservice']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['ueventd']['jackservice']['fill'] = 'red'
G.add_edge('ueventd','kiesexe')
G.edge['ueventd']['kiesexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['ueventd']['kiesexe']['fill'] = 'red'
G.add_edge('ueventd','kiesexe')
G.edge['ueventd']['kiesexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('ueventd','ks')
G.edge['ueventd']['ks']['write-read'] = '[open open][write read]'
G.edge['ueventd']['ks']['fill'] = 'red'
G.add_edge('ueventd','ks')
G.edge['ueventd']['ks']['write-read'] = '[open open][write read][append read]'
G.add_edge('ueventd','lhd')
G.edge['ueventd']['lhd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['ueventd']['lhd']['fill'] = 'red'
G.add_edge('ueventd','lhd')
G.edge['ueventd']['lhd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('ueventd','lmkd')
G.edge['ueventd']['lmkd']['write-read'] = '[write read]'
G.edge['ueventd']['lmkd']['fill'] = 'red'
G.add_edge('ueventd','lpm')
G.edge['ueventd']['lpm']['write-read'] = '[setopt getopt][open open][write read]'
G.edge['ueventd']['lpm']['fill'] = 'red'
G.add_edge('ueventd','lpm')
G.edge['ueventd']['lpm']['write-read'] = '[setopt getopt][open open][write read][append read]'
G.add_edge('ueventd','macloader')
G.edge['ueventd']['macloader']['write-read'] = '[open open][write read]'
G.edge['ueventd']['macloader']['fill'] = 'red'
G.add_edge('ueventd','macloader')
G.edge['ueventd']['macloader']['write-read'] = '[open open][write read][append read]'
G.add_edge('ueventd','mdm_helper')
G.edge['ueventd']['mdm_helper']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read]'
G.edge['ueventd']['mdm_helper']['fill'] = 'red'
G.add_edge('ueventd','mediaserver')
G.edge['ueventd']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read]'
G.edge['ueventd']['mediaserver']['fill'] = 'red'
G.add_edge('ueventd','mediaserver')
G.edge['ueventd']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read][append read]'
G.add_edge('ueventd','mfgloader')
G.edge['ueventd']['mfgloader']['write-read'] = '[open open][write read][add_name search][remove_name search][write read]'
G.edge['ueventd']['mfgloader']['fill'] = 'red'
G.add_edge('ueventd','mlexe')
G.edge['ueventd']['mlexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['ueventd']['mlexe']['fill'] = 'red'
G.add_edge('ueventd','mlexe')
G.edge['ueventd']['mlexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('ueventd','mm-pp-daemon')
G.edge['ueventd']['mm-pp-daemon']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read]'
G.edge['ueventd']['mm-pp-daemon']['fill'] = 'red'
G.add_edge('ueventd','mm-pp-daemon')
G.edge['ueventd']['mm-pp-daemon']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('ueventd','mm-pp-daemon')
G.edge['ueventd']['mm-pp-daemon']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][write read]'
G.edge['ueventd']['mm-pp-daemon']['fill'] = 'red'
G.add_edge('ueventd','mm-qcamera-daemon')
G.edge['ueventd']['mm-qcamera-daemon']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['ueventd']['mm-qcamera-daemon']['fill'] = 'red'
G.add_edge('ueventd','mm-qcamera-daemon')
G.edge['ueventd']['mm-qcamera-daemon']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('ueventd','mpdecision')
G.edge['ueventd']['mpdecision']['write-read'] = '[setopt getopt][setopt getopt][open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['ueventd']['mpdecision']['fill'] = 'red'
G.add_edge('ueventd','mpdecision')
G.edge['ueventd']['mpdecision']['write-read'] = '[setopt getopt][setopt getopt][open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('ueventd','mpdecision')
G.edge['ueventd']['mpdecision']['write-read'] = '[setopt getopt][setopt getopt][open open][write read][add_name search][remove_name search][open open][write read][append read][write read]'
G.edge['ueventd']['mpdecision']['fill'] = 'red'
G.add_edge('ueventd','netd')
G.edge['ueventd']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][add_name search][remove_name search][add_name search][remove_name search][write read]'
G.edge['ueventd']['netd']['fill'] = 'red'
G.add_edge('ueventd','netmgrd')
G.edge['ueventd']['netmgrd']['write-read'] = '[open open][open open][write read][write read][add_name search][add_name search][remove_name search][write read]'
G.edge['ueventd']['netmgrd']['fill'] = 'red'
G.add_edge('ueventd','nfc')
G.edge['ueventd']['nfc']['write-read'] = '[write read]'
G.edge['ueventd']['nfc']['fill'] = 'red'
G.add_edge('ueventd','oneseg_mw')
G.edge['ueventd']['oneseg_mw']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['ueventd']['oneseg_mw']['fill'] = 'red'
G.add_edge('ueventd','oneseg_mw')
G.edge['ueventd']['oneseg_mw']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('ueventd','perfd')
G.edge['ueventd']['perfd']['write-read'] = '[setopt getopt][write read]'
G.edge['ueventd']['perfd']['fill'] = 'red'
G.add_edge('ueventd','qcks')
G.edge['ueventd']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['ueventd']['qcks']['fill'] = 'red'
G.add_edge('ueventd','qcks')
G.edge['ueventd']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('ueventd','qmuxd')
G.edge['ueventd']['qmuxd']['write-read'] = '[open open][write read]'
G.edge['ueventd']['qmuxd']['fill'] = 'red'
G.add_edge('ueventd','qmuxd')
G.edge['ueventd']['qmuxd']['write-read'] = '[open open][write read][append read]'
G.add_edge('ueventd','qosmgr')
G.edge['ueventd']['qosmgr']['write-read'] = '[write read]'
G.edge['ueventd']['qosmgr']['fill'] = 'red'
G.add_edge('ueventd','radio')
G.edge['ueventd']['radio']['write-read'] = '[open open][append read]'
G.add_edge('ueventd','rild')
G.edge['ueventd']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['ueventd']['rild']['fill'] = 'red'
G.add_edge('ueventd','rild')
G.edge['ueventd']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('ueventd','rmt_storage')
G.edge['ueventd']['rmt_storage']['write-read'] = '[open open][write read]'
G.edge['ueventd']['rmt_storage']['fill'] = 'red'
G.add_edge('ueventd','rmt_storage')
G.edge['ueventd']['rmt_storage']['write-read'] = '[open open][write read][append read]'
G.add_edge('ueventd','rtcc')
G.edge['ueventd']['rtcc']['write-read'] = '[setattr getattr][write read]'
G.edge['ueventd']['rtcc']['fill'] = 'red'
G.add_edge('ueventd','sec-ril')
G.edge['ueventd']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['ueventd']['sec-ril']['fill'] = 'red'
G.add_edge('ueventd','sec-ril')
G.edge['ueventd']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('ueventd','sensorhubservice')
G.edge['ueventd']['sensorhubservice']['write-read'] = '[write read]'
G.edge['ueventd']['sensorhubservice']['fill'] = 'red'
G.add_edge('ueventd','smdexe')
G.edge['ueventd']['smdexe']['write-read'] = '[open open][write read]'
G.edge['ueventd']['smdexe']['fill'] = 'red'
G.add_edge('ueventd','smdexe')
G.edge['ueventd']['smdexe']['write-read'] = '[open open][write read][append read]'
G.add_edge('ueventd','ssr_setup')
G.edge['ueventd']['ssr_setup']['write-read'] = '[open open][write read]'
G.edge['ueventd']['ssr_setup']['fill'] = 'red'
G.add_edge('ueventd','ssr_setup')
G.edge['ueventd']['ssr_setup']['write-read'] = '[open open][write read][append read]'
G.add_edge('ueventd','sswap')
G.edge['ueventd']['sswap']['write-read'] = '[open open][write read]'
G.edge['ueventd']['sswap']['fill'] = 'red'
G.add_edge('ueventd','sswap')
G.edge['ueventd']['sswap']['write-read'] = '[open open][write read][append read]'
G.add_edge('ueventd','surfaceflinger')
G.edge['ueventd']['surfaceflinger']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read]'
G.edge['ueventd']['surfaceflinger']['fill'] = 'red'
G.add_edge('ueventd','surfaceflinger')
G.edge['ueventd']['surfaceflinger']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read]'
G.add_edge('ueventd','surfaceflinger')
G.edge['ueventd']['surfaceflinger']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][write read]'
G.edge['ueventd']['surfaceflinger']['fill'] = 'red'
G.add_edge('ueventd','system_server')
G.edge['ueventd']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read]'
G.edge['ueventd']['system_server']['fill'] = 'red'
G.add_edge('ueventd','system_server')
G.edge['ueventd']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][append read]'
G.add_edge('ueventd','system_server')
G.edge['ueventd']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][append read][write read]'
G.edge['ueventd']['system_server']['fill'] = 'red'
G.add_edge('ueventd','system_server')
G.edge['ueventd']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][append read][write read][append read]'
G.add_edge('ueventd','thermald')
G.edge['ueventd']['thermald']['write-read'] = '[open open][write read][add_name search][remove_name search][write read]'
G.edge['ueventd']['thermald']['fill'] = 'red'
G.add_edge('ueventd','thermal-engine')
G.edge['ueventd']['thermal-engine']['write-read'] = '[setopt getopt][open open][write read]'
G.edge['ueventd']['thermal-engine']['fill'] = 'red'
G.add_edge('ueventd','thermal-engine')
G.edge['ueventd']['thermal-engine']['write-read'] = '[setopt getopt][open open][write read][append read]'
G.add_edge('ueventd','thermal-engine')
G.edge['ueventd']['thermal-engine']['write-read'] = '[setopt getopt][open open][write read][append read][write read]'
G.edge['ueventd']['thermal-engine']['fill'] = 'red'
G.add_edge('ueventd','ueventd')
G.edge['ueventd']['ueventd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][setattr getattr][relabelto relabelfrom][relabelto relabelfrom][relabelto relabelfrom][relabelto relabelfrom][open open][setattr getattr][relabelto relabelfrom][open open][write read][append read][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['ueventd']['ueventd']['fill'] = 'red'
G.add_edge('ueventd','ueventd')
G.edge['ueventd']['ueventd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][setattr getattr][relabelto relabelfrom][relabelto relabelfrom][relabelto relabelfrom][relabelto relabelfrom][open open][setattr getattr][relabelto relabelfrom][open open][write read][append read][write read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('ueventd','vm_bms')
G.edge['ueventd']['vm_bms']['write-read'] = '[open open][write read]'
G.edge['ueventd']['vm_bms']['fill'] = 'red'
G.add_edge('ueventd','vm_bms')
G.edge['ueventd']['vm_bms']['write-read'] = '[open open][write read][append read]'
G.add_edge('ueventd','vmwared')
G.edge['ueventd']['vmwared']['write-read'] = '[write read]'
G.edge['ueventd']['vmwared']['fill'] = 'red'
G.add_edge('ueventd','vold')
G.edge['ueventd']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][append read][add_name search][remove_name search][open open][write read]'
G.edge['ueventd']['vold']['fill'] = 'red'
G.add_edge('ueventd','vold')
G.edge['ueventd']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][append read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('ueventd','zygote')
G.edge['ueventd']['zygote']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['ueventd']['zygote']['fill'] = 'red'
G.add_edge('ueventd','ueventd')
G.edge['ueventd']['ueventd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][setattr getattr][relabelto relabelfrom][relabelto relabelfrom][relabelto relabelfrom][relabelto relabelfrom][open open][setattr getattr][relabelto relabelfrom][open open][write read][append read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][relabelto relabelfrom]'
G.add_edge('vm_bms','at_distributor')
G.edge['vm_bms']['at_distributor']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('vm_bms','bauthserver')
G.edge['vm_bms']['bauthserver']['write-read'] = '[open open]'
G.add_edge('vm_bms','bintvoutservice')
G.edge['vm_bms']['bintvoutservice']['write-read'] = '[open open]'
G.add_edge('vm_bms','bluetooth')
G.edge['vm_bms']['bluetooth']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('vm_bms','cbd')
G.edge['vm_bms']['cbd']['write-read'] = '[open open]'
G.add_edge('vm_bms','cellgeofenced')
G.edge['vm_bms']['cellgeofenced']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('vm_bms','charger_monitor')
G.edge['vm_bms']['charger_monitor']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('vm_bms','charger_monitor')
G.edge['vm_bms']['charger_monitor']['write-read'] = '[open open][write read][append read][open open][open open]'
G.add_edge('vm_bms','cnd')
G.edge['vm_bms']['cnd']['write-read'] = '[open open][append read][open open]'
G.add_edge('vm_bms','connfwexe')
G.edge['vm_bms']['connfwexe']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('vm_bms','debuggerd')
G.edge['vm_bms']['debuggerd']['write-read'] = '[open open]'
G.add_edge('vm_bms','diag_uart_log')
G.edge['vm_bms']['diag_uart_log']['write-read'] = '[open open]'
G.add_edge('vm_bms','dumpstate')
G.edge['vm_bms']['dumpstate']['write-read'] = '[open open]'
G.add_edge('vm_bms','efsks')
G.edge['vm_bms']['efsks']['write-read'] = '[open open]'
G.add_edge('vm_bms','geomagneticd')
G.edge['vm_bms']['geomagneticd']['write-read'] = '[open open]'
G.add_edge('vm_bms','gpsd')
G.edge['vm_bms']['gpsd']['write-read'] = '[open open]'
G.add_edge('vm_bms','init_shell')
G.edge['vm_bms']['init_shell']['write-read'] = '[open open]'
G.add_edge('vm_bms','kiesexe')
G.edge['vm_bms']['kiesexe']['write-read'] = '[open open]'
G.add_edge('vm_bms','ks')
G.edge['vm_bms']['ks']['write-read'] = '[open open][append read][open open]'
G.add_edge('vm_bms','lhd')
G.edge['vm_bms']['lhd']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('vm_bms','lpm')
G.edge['vm_bms']['lpm']['write-read'] = '[open open]'
G.add_edge('vm_bms','macloader')
G.edge['vm_bms']['macloader']['write-read'] = '[open open]'
G.add_edge('vm_bms','mdm_helper')
G.edge['vm_bms']['mdm_helper']['write-read'] = '[open open][append read][open open]'
G.add_edge('vm_bms','mediaserver')
G.edge['vm_bms']['mediaserver']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('vm_bms','mlexe')
G.edge['vm_bms']['mlexe']['write-read'] = '[open open]'
G.add_edge('vm_bms','mm-pp-daemon')
G.edge['vm_bms']['mm-pp-daemon']['write-read'] = '[open open]'
G.add_edge('vm_bms','mm-qcamera-daemon')
G.edge['vm_bms']['mm-qcamera-daemon']['write-read'] = '[open open]'
G.add_edge('vm_bms','mpdecision')
G.edge['vm_bms']['mpdecision']['write-read'] = '[open open]'
G.add_edge('vm_bms','oneseg_mw')
G.edge['vm_bms']['oneseg_mw']['write-read'] = '[open open]'
G.add_edge('vm_bms','qcks')
G.edge['vm_bms']['qcks']['write-read'] = '[open open][append read][open open]'
G.add_edge('vm_bms','qmuxd')
G.edge['vm_bms']['qmuxd']['write-read'] = '[open open][open open][append read][write read][append read][open open]'
G.add_edge('vm_bms','radio')
G.edge['vm_bms']['radio']['write-read'] = '[open open]'
G.add_edge('vm_bms','rild')
G.edge['vm_bms']['rild']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('vm_bms','rmt_storage')
G.edge['vm_bms']['rmt_storage']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('vm_bms','sec-ril')
G.edge['vm_bms']['sec-ril']['write-read'] = '[open open][write read][open open]'
G.add_edge('vm_bms','smdexe')
G.edge['vm_bms']['smdexe']['write-read'] = '[open open]'
G.add_edge('vm_bms','ssr_setup')
G.edge['vm_bms']['ssr_setup']['write-read'] = '[open open]'
G.add_edge('vm_bms','sswap')
G.edge['vm_bms']['sswap']['write-read'] = '[open open]'
G.add_edge('vm_bms','surfaceflinger')
G.edge['vm_bms']['surfaceflinger']['write-read'] = '[open open]'
G.add_edge('vm_bms','system_server')
G.edge['vm_bms']['system_server']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('vm_bms','system_server')
G.edge['vm_bms']['system_server']['write-read'] = '[open open][write read][append read][open open][open open]'
G.add_edge('vm_bms','thermal-engine')
G.edge['vm_bms']['thermal-engine']['write-read'] = '[open open]'
G.add_edge('vm_bms','ueventd')
G.edge['vm_bms']['ueventd']['write-read'] = '[open open]'
G.add_edge('vm_bms','vm_bms')
G.edge['vm_bms']['vm_bms']['write-read'] = '[write read][open open][write read][append read][open open]'
G.add_edge('vm_bms','vold')
G.edge['vm_bms']['vold']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('vm_bms','init_shell')
G.edge['vm_bms']['init_shell']['write-read'] = '[open open][setattr getattr]'
G.add_edge('vm_bms','rild')
G.edge['vm_bms']['rild']['write-read'] = '[open open][write read][append read][open open][setattr getattr]'
G.add_edge('vm_bms','rtcc')
G.edge['vm_bms']['rtcc']['write-read'] = '[setattr getattr]'
G.add_edge('vm_bms','sec-ril')
G.edge['vm_bms']['sec-ril']['write-read'] = '[open open][write read][open open][setattr getattr]'
G.add_edge('vm_bms','system_server')
G.edge['vm_bms']['system_server']['write-read'] = '[open open][write read][append read][open open][open open][setattr getattr]'
G.add_edge('vm_bms','at_distributor')
G.edge['vm_bms']['at_distributor']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['vm_bms']['at_distributor']['fill'] = 'red'
G.add_edge('vm_bms','at_distributor')
G.edge['vm_bms']['at_distributor']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('vm_bms','bauthserver')
G.edge['vm_bms']['bauthserver']['write-read'] = '[open open][write read]'
G.edge['vm_bms']['bauthserver']['fill'] = 'red'
G.add_edge('vm_bms','bauthserver')
G.edge['vm_bms']['bauthserver']['write-read'] = '[open open][write read][append read]'
G.add_edge('vm_bms','bintvoutservice')
G.edge['vm_bms']['bintvoutservice']['write-read'] = '[open open][write read]'
G.edge['vm_bms']['bintvoutservice']['fill'] = 'red'
G.add_edge('vm_bms','bintvoutservice')
G.edge['vm_bms']['bintvoutservice']['write-read'] = '[open open][write read][append read]'
G.add_edge('vm_bms','bluetooth')
G.edge['vm_bms']['bluetooth']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['vm_bms']['bluetooth']['fill'] = 'red'
G.add_edge('vm_bms','bluetooth')
G.edge['vm_bms']['bluetooth']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('vm_bms','bootanim')
G.edge['vm_bms']['bootanim']['write-read'] = '[write read]'
G.edge['vm_bms']['bootanim']['fill'] = 'red'
G.add_edge('vm_bms','cbd')
G.edge['vm_bms']['cbd']['write-read'] = '[open open][write read]'
G.edge['vm_bms']['cbd']['fill'] = 'red'
G.add_edge('vm_bms','cbd')
G.edge['vm_bms']['cbd']['write-read'] = '[open open][write read][append read]'
G.add_edge('vm_bms','cellgeofenced')
G.edge['vm_bms']['cellgeofenced']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['vm_bms']['cellgeofenced']['fill'] = 'red'
G.add_edge('vm_bms','cellgeofenced')
G.edge['vm_bms']['cellgeofenced']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('vm_bms','charger_monitor')
G.edge['vm_bms']['charger_monitor']['write-read'] = '[open open][write read][append read][open open][open open][write read]'
G.edge['vm_bms']['charger_monitor']['fill'] = 'red'
G.add_edge('vm_bms','charger_monitor')
G.edge['vm_bms']['charger_monitor']['write-read'] = '[open open][write read][append read][open open][open open][write read][append read]'
G.add_edge('vm_bms','charger_monitor')
G.edge['vm_bms']['charger_monitor']['write-read'] = '[open open][write read][append read][open open][open open][write read][append read][write read]'
G.edge['vm_bms']['charger_monitor']['fill'] = 'red'
G.add_edge('vm_bms','charger_monitor')
G.edge['vm_bms']['charger_monitor']['write-read'] = '[open open][write read][append read][open open][open open][write read][append read][write read][append read]'
G.add_edge('vm_bms','cnd')
G.edge['vm_bms']['cnd']['write-read'] = '[open open][append read][open open][write read]'
G.edge['vm_bms']['cnd']['fill'] = 'red'
G.add_edge('vm_bms','cnd')
G.edge['vm_bms']['cnd']['write-read'] = '[open open][append read][open open][write read][append read]'
G.add_edge('vm_bms','connfwexe')
G.edge['vm_bms']['connfwexe']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['vm_bms']['connfwexe']['fill'] = 'red'
G.add_edge('vm_bms','connfwexe')
G.edge['vm_bms']['connfwexe']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('vm_bms','debuggerd')
G.edge['vm_bms']['debuggerd']['write-read'] = '[open open][write read]'
G.edge['vm_bms']['debuggerd']['fill'] = 'red'
G.add_edge('vm_bms','debuggerd')
G.edge['vm_bms']['debuggerd']['write-read'] = '[open open][write read][append read]'
G.add_edge('vm_bms','diag_uart_log')
G.edge['vm_bms']['diag_uart_log']['write-read'] = '[open open][write read]'
G.edge['vm_bms']['diag_uart_log']['fill'] = 'red'
G.add_edge('vm_bms','diag_uart_log')
G.edge['vm_bms']['diag_uart_log']['write-read'] = '[open open][write read][append read]'
G.add_edge('vm_bms','dumpstate')
G.edge['vm_bms']['dumpstate']['write-read'] = '[open open][write read]'
G.edge['vm_bms']['dumpstate']['fill'] = 'red'
G.add_edge('vm_bms','dumpstate')
G.edge['vm_bms']['dumpstate']['write-read'] = '[open open][write read][append read]'
G.add_edge('vm_bms','efsks')
G.edge['vm_bms']['efsks']['write-read'] = '[open open][write read]'
G.edge['vm_bms']['efsks']['fill'] = 'red'
G.add_edge('vm_bms','efsks')
G.edge['vm_bms']['efsks']['write-read'] = '[open open][write read][append read]'
G.add_edge('vm_bms','geomagneticd')
G.edge['vm_bms']['geomagneticd']['write-read'] = '[open open][write read]'
G.edge['vm_bms']['geomagneticd']['fill'] = 'red'
G.add_edge('vm_bms','geomagneticd')
G.edge['vm_bms']['geomagneticd']['write-read'] = '[open open][write read][append read]'
G.add_edge('vm_bms','gpsd')
G.edge['vm_bms']['gpsd']['write-read'] = '[open open][write read]'
G.edge['vm_bms']['gpsd']['fill'] = 'red'
G.add_edge('vm_bms','gpsd')
G.edge['vm_bms']['gpsd']['write-read'] = '[open open][write read][append read]'
G.add_edge('vm_bms','healthd')
G.edge['vm_bms']['healthd']['write-read'] = '[open open][write read][append read][write read]'
G.edge['vm_bms']['healthd']['fill'] = 'red'
G.add_edge('vm_bms','init_shell')
G.edge['vm_bms']['init_shell']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['vm_bms']['init_shell']['fill'] = 'red'
G.add_edge('vm_bms','init_shell')
G.edge['vm_bms']['init_shell']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('vm_bms','jackservice')
G.edge['vm_bms']['jackservice']['write-read'] = '[write read]'
G.edge['vm_bms']['jackservice']['fill'] = 'red'
G.add_edge('vm_bms','kiesexe')
G.edge['vm_bms']['kiesexe']['write-read'] = '[open open][write read]'
G.edge['vm_bms']['kiesexe']['fill'] = 'red'
G.add_edge('vm_bms','kiesexe')
G.edge['vm_bms']['kiesexe']['write-read'] = '[open open][write read][append read]'
G.add_edge('vm_bms','ks')
G.edge['vm_bms']['ks']['write-read'] = '[open open][append read][open open][write read]'
G.edge['vm_bms']['ks']['fill'] = 'red'
G.add_edge('vm_bms','ks')
G.edge['vm_bms']['ks']['write-read'] = '[open open][append read][open open][write read][append read]'
G.add_edge('vm_bms','lhd')
G.edge['vm_bms']['lhd']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['vm_bms']['lhd']['fill'] = 'red'
G.add_edge('vm_bms','lhd')
G.edge['vm_bms']['lhd']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('vm_bms','lmkd')
G.edge['vm_bms']['lmkd']['write-read'] = '[write read]'
G.edge['vm_bms']['lmkd']['fill'] = 'red'
G.add_edge('vm_bms','lpm')
G.edge['vm_bms']['lpm']['write-read'] = '[open open][write read]'
G.edge['vm_bms']['lpm']['fill'] = 'red'
G.add_edge('vm_bms','lpm')
G.edge['vm_bms']['lpm']['write-read'] = '[open open][write read][append read]'
G.add_edge('vm_bms','macloader')
G.edge['vm_bms']['macloader']['write-read'] = '[open open][write read]'
G.edge['vm_bms']['macloader']['fill'] = 'red'
G.add_edge('vm_bms','macloader')
G.edge['vm_bms']['macloader']['write-read'] = '[open open][write read][append read]'
G.add_edge('vm_bms','mdm_helper')
G.edge['vm_bms']['mdm_helper']['write-read'] = '[open open][append read][open open][write read]'
G.edge['vm_bms']['mdm_helper']['fill'] = 'red'
G.add_edge('vm_bms','mediaserver')
G.edge['vm_bms']['mediaserver']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['vm_bms']['mediaserver']['fill'] = 'red'
G.add_edge('vm_bms','mediaserver')
G.edge['vm_bms']['mediaserver']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('vm_bms','mfgloader')
G.edge['vm_bms']['mfgloader']['write-read'] = '[write read]'
G.edge['vm_bms']['mfgloader']['fill'] = 'red'
G.add_edge('vm_bms','mlexe')
G.edge['vm_bms']['mlexe']['write-read'] = '[open open][write read]'
G.edge['vm_bms']['mlexe']['fill'] = 'red'
G.add_edge('vm_bms','mlexe')
G.edge['vm_bms']['mlexe']['write-read'] = '[open open][write read][append read]'
G.add_edge('vm_bms','mm-pp-daemon')
G.edge['vm_bms']['mm-pp-daemon']['write-read'] = '[open open][write read]'
G.edge['vm_bms']['mm-pp-daemon']['fill'] = 'red'
G.add_edge('vm_bms','mm-pp-daemon')
G.edge['vm_bms']['mm-pp-daemon']['write-read'] = '[open open][write read][append read]'
G.add_edge('vm_bms','mm-pp-daemon')
G.edge['vm_bms']['mm-pp-daemon']['write-read'] = '[open open][write read][append read][write read]'
G.edge['vm_bms']['mm-pp-daemon']['fill'] = 'red'
G.add_edge('vm_bms','mm-qcamera-daemon')
G.edge['vm_bms']['mm-qcamera-daemon']['write-read'] = '[open open][write read]'
G.edge['vm_bms']['mm-qcamera-daemon']['fill'] = 'red'
G.add_edge('vm_bms','mm-qcamera-daemon')
G.edge['vm_bms']['mm-qcamera-daemon']['write-read'] = '[open open][write read][append read]'
G.add_edge('vm_bms','mpdecision')
G.edge['vm_bms']['mpdecision']['write-read'] = '[open open][write read]'
G.edge['vm_bms']['mpdecision']['fill'] = 'red'
G.add_edge('vm_bms','mpdecision')
G.edge['vm_bms']['mpdecision']['write-read'] = '[open open][write read][append read]'
G.add_edge('vm_bms','mpdecision')
G.edge['vm_bms']['mpdecision']['write-read'] = '[open open][write read][append read][write read]'
G.edge['vm_bms']['mpdecision']['fill'] = 'red'
G.add_edge('vm_bms','netd')
G.edge['vm_bms']['netd']['write-read'] = '[write read]'
G.edge['vm_bms']['netd']['fill'] = 'red'
G.add_edge('vm_bms','netmgrd')
G.edge['vm_bms']['netmgrd']['write-read'] = '[write read]'
G.edge['vm_bms']['netmgrd']['fill'] = 'red'
G.add_edge('vm_bms','nfc')
G.edge['vm_bms']['nfc']['write-read'] = '[write read]'
G.edge['vm_bms']['nfc']['fill'] = 'red'
G.add_edge('vm_bms','oneseg_mw')
G.edge['vm_bms']['oneseg_mw']['write-read'] = '[open open][write read]'
G.edge['vm_bms']['oneseg_mw']['fill'] = 'red'
G.add_edge('vm_bms','oneseg_mw')
G.edge['vm_bms']['oneseg_mw']['write-read'] = '[open open][write read][append read]'
G.add_edge('vm_bms','perfd')
G.edge['vm_bms']['perfd']['write-read'] = '[write read]'
G.edge['vm_bms']['perfd']['fill'] = 'red'
G.add_edge('vm_bms','qcks')
G.edge['vm_bms']['qcks']['write-read'] = '[open open][append read][open open][write read]'
G.edge['vm_bms']['qcks']['fill'] = 'red'
G.add_edge('vm_bms','qcks')
G.edge['vm_bms']['qcks']['write-read'] = '[open open][append read][open open][write read][append read]'
G.add_edge('vm_bms','qmuxd')
G.edge['vm_bms']['qmuxd']['write-read'] = '[open open][open open][append read][write read][append read][open open][write read]'
G.edge['vm_bms']['qmuxd']['fill'] = 'red'
G.add_edge('vm_bms','qmuxd')
G.edge['vm_bms']['qmuxd']['write-read'] = '[open open][open open][append read][write read][append read][open open][write read][append read]'
G.add_edge('vm_bms','qosmgr')
G.edge['vm_bms']['qosmgr']['write-read'] = '[write read]'
G.edge['vm_bms']['qosmgr']['fill'] = 'red'
G.add_edge('vm_bms','radio')
G.edge['vm_bms']['radio']['write-read'] = '[open open][append read]'
G.add_edge('vm_bms','rild')
G.edge['vm_bms']['rild']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read]'
G.edge['vm_bms']['rild']['fill'] = 'red'
G.add_edge('vm_bms','rild')
G.edge['vm_bms']['rild']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('vm_bms','rmt_storage')
G.edge['vm_bms']['rmt_storage']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['vm_bms']['rmt_storage']['fill'] = 'red'
G.add_edge('vm_bms','rmt_storage')
G.edge['vm_bms']['rmt_storage']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('vm_bms','rtcc')
G.edge['vm_bms']['rtcc']['write-read'] = '[setattr getattr][write read]'
G.edge['vm_bms']['rtcc']['fill'] = 'red'
G.add_edge('vm_bms','sec-ril')
G.edge['vm_bms']['sec-ril']['write-read'] = '[open open][write read][open open][setattr getattr][write read]'
G.edge['vm_bms']['sec-ril']['fill'] = 'red'
G.add_edge('vm_bms','sec-ril')
G.edge['vm_bms']['sec-ril']['write-read'] = '[open open][write read][open open][setattr getattr][write read][append read]'
G.add_edge('vm_bms','sensorhubservice')
G.edge['vm_bms']['sensorhubservice']['write-read'] = '[write read]'
G.edge['vm_bms']['sensorhubservice']['fill'] = 'red'
G.add_edge('vm_bms','smdexe')
G.edge['vm_bms']['smdexe']['write-read'] = '[open open][write read]'
G.edge['vm_bms']['smdexe']['fill'] = 'red'
G.add_edge('vm_bms','smdexe')
G.edge['vm_bms']['smdexe']['write-read'] = '[open open][write read][append read]'
G.add_edge('vm_bms','ssr_setup')
G.edge['vm_bms']['ssr_setup']['write-read'] = '[open open][write read]'
G.edge['vm_bms']['ssr_setup']['fill'] = 'red'
G.add_edge('vm_bms','ssr_setup')
G.edge['vm_bms']['ssr_setup']['write-read'] = '[open open][write read][append read]'
G.add_edge('vm_bms','sswap')
G.edge['vm_bms']['sswap']['write-read'] = '[open open][write read]'
G.edge['vm_bms']['sswap']['fill'] = 'red'
G.add_edge('vm_bms','sswap')
G.edge['vm_bms']['sswap']['write-read'] = '[open open][write read][append read]'
G.add_edge('vm_bms','surfaceflinger')
G.edge['vm_bms']['surfaceflinger']['write-read'] = '[open open][write read]'
G.edge['vm_bms']['surfaceflinger']['fill'] = 'red'
G.add_edge('vm_bms','surfaceflinger')
G.edge['vm_bms']['surfaceflinger']['write-read'] = '[open open][write read][append read]'
G.add_edge('vm_bms','surfaceflinger')
G.edge['vm_bms']['surfaceflinger']['write-read'] = '[open open][write read][append read][write read]'
G.edge['vm_bms']['surfaceflinger']['fill'] = 'red'
G.add_edge('vm_bms','system_server')
G.edge['vm_bms']['system_server']['write-read'] = '[open open][write read][append read][open open][open open][setattr getattr][write read]'
G.edge['vm_bms']['system_server']['fill'] = 'red'
G.add_edge('vm_bms','system_server')
G.edge['vm_bms']['system_server']['write-read'] = '[open open][write read][append read][open open][open open][setattr getattr][write read][append read]'
G.add_edge('vm_bms','system_server')
G.edge['vm_bms']['system_server']['write-read'] = '[open open][write read][append read][open open][open open][setattr getattr][write read][append read][write read]'
G.edge['vm_bms']['system_server']['fill'] = 'red'
G.add_edge('vm_bms','system_server')
G.edge['vm_bms']['system_server']['write-read'] = '[open open][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read]'
G.add_edge('vm_bms','thermald')
G.edge['vm_bms']['thermald']['write-read'] = '[write read]'
G.edge['vm_bms']['thermald']['fill'] = 'red'
G.add_edge('vm_bms','thermal-engine')
G.edge['vm_bms']['thermal-engine']['write-read'] = '[open open][write read]'
G.edge['vm_bms']['thermal-engine']['fill'] = 'red'
G.add_edge('vm_bms','thermal-engine')
G.edge['vm_bms']['thermal-engine']['write-read'] = '[open open][write read][append read]'
G.add_edge('vm_bms','thermal-engine')
G.edge['vm_bms']['thermal-engine']['write-read'] = '[open open][write read][append read][write read]'
G.edge['vm_bms']['thermal-engine']['fill'] = 'red'
G.add_edge('vm_bms','ueventd')
G.edge['vm_bms']['ueventd']['write-read'] = '[open open][write read]'
G.edge['vm_bms']['ueventd']['fill'] = 'red'
G.add_edge('vm_bms','ueventd')
G.edge['vm_bms']['ueventd']['write-read'] = '[open open][write read][append read]'
G.add_edge('vm_bms','vm_bms')
G.edge['vm_bms']['vm_bms']['write-read'] = '[write read][open open][write read][append read][open open][write read]'
G.edge['vm_bms']['vm_bms']['fill'] = 'red'
G.add_edge('vm_bms','vm_bms')
G.edge['vm_bms']['vm_bms']['write-read'] = '[write read][open open][write read][append read][open open][write read][append read]'
G.add_edge('vm_bms','vmwared')
G.edge['vm_bms']['vmwared']['write-read'] = '[write read]'
G.edge['vm_bms']['vmwared']['fill'] = 'red'
G.add_edge('vm_bms','vold')
G.edge['vm_bms']['vold']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['vm_bms']['vold']['fill'] = 'red'
G.add_edge('vm_bms','vold')
G.edge['vm_bms']['vold']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('vm_bms','zygote')
G.edge['vm_bms']['zygote']['write-read'] = '[write read]'
G.edge['vm_bms']['zygote']['fill'] = 'red'
G.add_edge('vold','at_distributor')
G.edge['vold']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('vold','bauthserver')
G.edge['vold']['bauthserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('vold','bintvoutservice')
G.edge['vold']['bintvoutservice']['write-read'] = '[open open]'
G.add_edge('vold','bluetooth')
G.edge['vold']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read][open open]'
G.add_edge('vold','cbd')
G.edge['vold']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('vold','cellgeofenced')
G.edge['vold']['cellgeofenced']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('vold','charger_monitor')
G.edge['vold']['charger_monitor']['write-read'] = '[setopt getopt][open open][write read][append read][open open]'
G.add_edge('vold','charger_monitor')
G.edge['vold']['charger_monitor']['write-read'] = '[setopt getopt][open open][write read][append read][open open][open open]'
G.add_edge('vold','cnd')
G.edge['vold']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][append read][open open]'
G.add_edge('vold','connfwexe')
G.edge['vold']['connfwexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('vold','debuggerd')
G.edge['vold']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('vold','diag_uart_log')
G.edge['vold']['diag_uart_log']['write-read'] = '[open open]'
G.add_edge('vold','dumpstate')
G.edge['vold']['dumpstate']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('vold','efsks')
G.edge['vold']['efsks']['write-read'] = '[open open][write read][add_name search][open open]'
G.add_edge('vold','geomagneticd')
G.edge['vold']['geomagneticd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('vold','gpsd')
G.edge['vold']['gpsd']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('vold','init_shell')
G.edge['vold']['init_shell']['write-read'] = '[open open][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open]'
G.add_edge('vold','kiesexe')
G.edge['vold']['kiesexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('vold','ks')
G.edge['vold']['ks']['write-read'] = '[open open][write read][add_name search][open open][append read][open open]'
G.add_edge('vold','lhd')
G.edge['vold']['lhd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('vold','lpm')
G.edge['vold']['lpm']['write-read'] = '[setopt getopt][open open][write read][append read][open open]'
G.add_edge('vold','macloader')
G.edge['vold']['macloader']['write-read'] = '[open open]'
G.add_edge('vold','mdm_helper')
G.edge['vold']['mdm_helper']['write-read'] = '[write read][open open][append read][open open]'
G.add_edge('vold','mediaserver')
G.edge['vold']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('vold','mlexe')
G.edge['vold']['mlexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('vold','mm-pp-daemon')
G.edge['vold']['mm-pp-daemon']['write-read'] = '[open open]'
G.add_edge('vold','mm-qcamera-daemon')
G.edge['vold']['mm-qcamera-daemon']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('vold','mpdecision')
G.edge['vold']['mpdecision']['write-read'] = '[setopt getopt][setopt getopt][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('vold','oneseg_mw')
G.edge['vold']['oneseg_mw']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('vold','qcks')
G.edge['vold']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][append read][open open]'
G.add_edge('vold','qmuxd')
G.edge['vold']['qmuxd']['write-read'] = '[open open][open open][append read][write read][append read][open open]'
G.add_edge('vold','radio')
G.edge['vold']['radio']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read][open open]'
G.add_edge('vold','rild')
G.edge['vold']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('vold','rmt_storage')
G.edge['vold']['rmt_storage']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('vold','sec-ril')
G.edge['vold']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][open open]'
G.add_edge('vold','smdexe')
G.edge['vold']['smdexe']['write-read'] = '[open open]'
G.add_edge('vold','ssr_setup')
G.edge['vold']['ssr_setup']['write-read'] = '[open open]'
G.add_edge('vold','sswap')
G.edge['vold']['sswap']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('vold','surfaceflinger')
G.edge['vold']['surfaceflinger']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][open open][write read][append read][open open]'
G.add_edge('vold','system_server')
G.edge['vold']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('vold','system_server')
G.edge['vold']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][open open]'
G.add_edge('vold','thermal-engine')
G.edge['vold']['thermal-engine']['write-read'] = '[setopt getopt][open open]'
G.add_edge('vold','ueventd')
G.edge['vold']['ueventd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][add_name search][remove_name search][open open]'
G.add_edge('vold','vm_bms')
G.edge['vold']['vm_bms']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('vold','vold')
G.edge['vold']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][relabelto relabelfrom][relabelto relabelfrom][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('vold','init_shell')
G.edge['vold']['init_shell']['write-read'] = '[open open][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr]'
G.add_edge('vold','rild')
G.edge['vold']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr]'
G.add_edge('vold','rtcc')
G.edge['vold']['rtcc']['write-read'] = '[open open][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('vold','sec-ril')
G.edge['vold']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][open open][setattr getattr]'
G.add_edge('vold','system_server')
G.edge['vold']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][open open][setattr getattr]'
G.add_edge('vold','at_distributor')
G.edge['vold']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read]'
G.edge['vold']['at_distributor']['fill'] = 'red'
G.add_edge('vold','at_distributor')
G.edge['vold']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read]'
G.add_edge('vold','bauthserver')
G.edge['vold']['bauthserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['vold']['bauthserver']['fill'] = 'red'
G.add_edge('vold','bauthserver')
G.edge['vold']['bauthserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('vold','bintvoutservice')
G.edge['vold']['bintvoutservice']['write-read'] = '[open open][write read]'
G.edge['vold']['bintvoutservice']['fill'] = 'red'
G.add_edge('vold','bintvoutservice')
G.edge['vold']['bintvoutservice']['write-read'] = '[open open][write read][append read]'
G.add_edge('vold','bluetooth')
G.edge['vold']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read][open open][write read]'
G.edge['vold']['bluetooth']['fill'] = 'red'
G.add_edge('vold','bluetooth')
G.edge['vold']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read][open open][write read][append read]'
G.add_edge('vold','bootanim')
G.edge['vold']['bootanim']['write-read'] = '[write read]'
G.edge['vold']['bootanim']['fill'] = 'red'
G.add_edge('vold','cbd')
G.edge['vold']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['vold']['cbd']['fill'] = 'red'
G.add_edge('vold','cbd')
G.edge['vold']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('vold','cellgeofenced')
G.edge['vold']['cellgeofenced']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['vold']['cellgeofenced']['fill'] = 'red'
G.add_edge('vold','cellgeofenced')
G.edge['vold']['cellgeofenced']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('vold','charger_monitor')
G.edge['vold']['charger_monitor']['write-read'] = '[setopt getopt][open open][write read][append read][open open][open open][write read]'
G.edge['vold']['charger_monitor']['fill'] = 'red'
G.add_edge('vold','charger_monitor')
G.edge['vold']['charger_monitor']['write-read'] = '[setopt getopt][open open][write read][append read][open open][open open][write read][append read]'
G.add_edge('vold','charger_monitor')
G.edge['vold']['charger_monitor']['write-read'] = '[setopt getopt][open open][write read][append read][open open][open open][write read][append read][write read]'
G.edge['vold']['charger_monitor']['fill'] = 'red'
G.add_edge('vold','charger_monitor')
G.edge['vold']['charger_monitor']['write-read'] = '[setopt getopt][open open][write read][append read][open open][open open][write read][append read][write read][append read]'
G.add_edge('vold','cnd')
G.edge['vold']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][append read][open open][write read]'
G.edge['vold']['cnd']['fill'] = 'red'
G.add_edge('vold','cnd')
G.edge['vold']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][append read][open open][write read][append read]'
G.add_edge('vold','connfwexe')
G.edge['vold']['connfwexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read]'
G.edge['vold']['connfwexe']['fill'] = 'red'
G.add_edge('vold','connfwexe')
G.edge['vold']['connfwexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read]'
G.add_edge('vold','debuggerd')
G.edge['vold']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read]'
G.edge['vold']['debuggerd']['fill'] = 'red'
G.add_edge('vold','debuggerd')
G.edge['vold']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('vold','diag_uart_log')
G.edge['vold']['diag_uart_log']['write-read'] = '[open open][write read]'
G.edge['vold']['diag_uart_log']['fill'] = 'red'
G.add_edge('vold','diag_uart_log')
G.edge['vold']['diag_uart_log']['write-read'] = '[open open][write read][append read]'
G.add_edge('vold','dumpstate')
G.edge['vold']['dumpstate']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read]'
G.edge['vold']['dumpstate']['fill'] = 'red'
G.add_edge('vold','dumpstate')
G.edge['vold']['dumpstate']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read]'
G.add_edge('vold','efsks')
G.edge['vold']['efsks']['write-read'] = '[open open][write read][add_name search][open open][write read]'
G.edge['vold']['efsks']['fill'] = 'red'
G.add_edge('vold','efsks')
G.edge['vold']['efsks']['write-read'] = '[open open][write read][add_name search][open open][write read][append read]'
G.add_edge('vold','geomagneticd')
G.edge['vold']['geomagneticd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['vold']['geomagneticd']['fill'] = 'red'
G.add_edge('vold','geomagneticd')
G.edge['vold']['geomagneticd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('vold','gpsd')
G.edge['vold']['gpsd']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read]'
G.edge['vold']['gpsd']['fill'] = 'red'
G.add_edge('vold','gpsd')
G.edge['vold']['gpsd']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('vold','healthd')
G.edge['vold']['healthd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][write read][add_name search][remove_name search][open open][write read][append read][write read]'
G.edge['vold']['healthd']['fill'] = 'red'
G.add_edge('vold','init_shell')
G.edge['vold']['init_shell']['write-read'] = '[open open][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read]'
G.edge['vold']['init_shell']['fill'] = 'red'
G.add_edge('vold','init_shell')
G.edge['vold']['init_shell']['write-read'] = '[open open][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read]'
G.add_edge('vold','jackservice')
G.edge['vold']['jackservice']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['vold']['jackservice']['fill'] = 'red'
G.add_edge('vold','kiesexe')
G.edge['vold']['kiesexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['vold']['kiesexe']['fill'] = 'red'
G.add_edge('vold','kiesexe')
G.edge['vold']['kiesexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('vold','ks')
G.edge['vold']['ks']['write-read'] = '[open open][write read][add_name search][open open][append read][open open][write read]'
G.edge['vold']['ks']['fill'] = 'red'
G.add_edge('vold','ks')
G.edge['vold']['ks']['write-read'] = '[open open][write read][add_name search][open open][append read][open open][write read][append read]'
G.add_edge('vold','lhd')
G.edge['vold']['lhd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read]'
G.edge['vold']['lhd']['fill'] = 'red'
G.add_edge('vold','lhd')
G.edge['vold']['lhd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read]'
G.add_edge('vold','lmkd')
G.edge['vold']['lmkd']['write-read'] = '[write read]'
G.edge['vold']['lmkd']['fill'] = 'red'
G.add_edge('vold','lpm')
G.edge['vold']['lpm']['write-read'] = '[setopt getopt][open open][write read][append read][open open][write read]'
G.edge['vold']['lpm']['fill'] = 'red'
G.add_edge('vold','lpm')
G.edge['vold']['lpm']['write-read'] = '[setopt getopt][open open][write read][append read][open open][write read][append read]'
G.add_edge('vold','macloader')
G.edge['vold']['macloader']['write-read'] = '[open open][write read]'
G.edge['vold']['macloader']['fill'] = 'red'
G.add_edge('vold','macloader')
G.edge['vold']['macloader']['write-read'] = '[open open][write read][append read]'
G.add_edge('vold','mdm_helper')
G.edge['vold']['mdm_helper']['write-read'] = '[write read][open open][append read][open open][write read]'
G.edge['vold']['mdm_helper']['fill'] = 'red'
G.add_edge('vold','mediaserver')
G.edge['vold']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read]'
G.edge['vold']['mediaserver']['fill'] = 'red'
G.add_edge('vold','mediaserver')
G.edge['vold']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read]'
G.add_edge('vold','mfgloader')
G.edge['vold']['mfgloader']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read]'
G.edge['vold']['mfgloader']['fill'] = 'red'
G.add_edge('vold','mlexe')
G.edge['vold']['mlexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['vold']['mlexe']['fill'] = 'red'
G.add_edge('vold','mlexe')
G.edge['vold']['mlexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('vold','mm-pp-daemon')
G.edge['vold']['mm-pp-daemon']['write-read'] = '[open open][write read]'
G.edge['vold']['mm-pp-daemon']['fill'] = 'red'
G.add_edge('vold','mm-pp-daemon')
G.edge['vold']['mm-pp-daemon']['write-read'] = '[open open][write read][append read]'
G.add_edge('vold','mm-pp-daemon')
G.edge['vold']['mm-pp-daemon']['write-read'] = '[open open][write read][append read][write read]'
G.edge['vold']['mm-pp-daemon']['fill'] = 'red'
G.add_edge('vold','mm-qcamera-daemon')
G.edge['vold']['mm-qcamera-daemon']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['vold']['mm-qcamera-daemon']['fill'] = 'red'
G.add_edge('vold','mm-qcamera-daemon')
G.edge['vold']['mm-qcamera-daemon']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('vold','mpdecision')
G.edge['vold']['mpdecision']['write-read'] = '[setopt getopt][setopt getopt][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['vold']['mpdecision']['fill'] = 'red'
G.add_edge('vold','mpdecision')
G.edge['vold']['mpdecision']['write-read'] = '[setopt getopt][setopt getopt][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('vold','mpdecision')
G.edge['vold']['mpdecision']['write-read'] = '[setopt getopt][setopt getopt][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read][write read]'
G.edge['vold']['mpdecision']['fill'] = 'red'
G.add_edge('vold','netd')
G.edge['vold']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][write read]'
G.edge['vold']['netd']['fill'] = 'red'
G.add_edge('vold','netmgrd')
G.edge['vold']['netmgrd']['write-read'] = '[open open][open open][write read][write read][add_name search][add_name search][remove_name search][open open][open open][write read][write read][add_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][write read]'
G.edge['vold']['netmgrd']['fill'] = 'red'
G.add_edge('vold','nfc')
G.edge['vold']['nfc']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['vold']['nfc']['fill'] = 'red'
G.add_edge('vold','oneseg_mw')
G.edge['vold']['oneseg_mw']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['vold']['oneseg_mw']['fill'] = 'red'
G.add_edge('vold','oneseg_mw')
G.edge['vold']['oneseg_mw']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('vold','perfd')
G.edge['vold']['perfd']['write-read'] = '[setopt getopt][write read]'
G.edge['vold']['perfd']['fill'] = 'red'
G.add_edge('vold','qcks')
G.edge['vold']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][append read][open open][write read]'
G.edge['vold']['qcks']['fill'] = 'red'
G.add_edge('vold','qcks')
G.edge['vold']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][append read][open open][write read][append read]'
G.add_edge('vold','qmuxd')
G.edge['vold']['qmuxd']['write-read'] = '[open open][open open][append read][write read][append read][open open][write read]'
G.edge['vold']['qmuxd']['fill'] = 'red'
G.add_edge('vold','qmuxd')
G.edge['vold']['qmuxd']['write-read'] = '[open open][open open][append read][write read][append read][open open][write read][append read]'
G.add_edge('vold','qosmgr')
G.edge['vold']['qosmgr']['write-read'] = '[write read]'
G.edge['vold']['qosmgr']['fill'] = 'red'
G.add_edge('vold','radio')
G.edge['vold']['radio']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][append read]'
G.add_edge('vold','rild')
G.edge['vold']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['vold']['rild']['fill'] = 'red'
G.add_edge('vold','rild')
G.edge['vold']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('vold','rmt_storage')
G.edge['vold']['rmt_storage']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['vold']['rmt_storage']['fill'] = 'red'
G.add_edge('vold','rmt_storage')
G.edge['vold']['rmt_storage']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('vold','rtcc')
G.edge['vold']['rtcc']['write-read'] = '[open open][write read][add_name search][remove_name search][setattr getattr][write read]'
G.edge['vold']['rtcc']['fill'] = 'red'
G.add_edge('vold','sec-ril')
G.edge['vold']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][open open][setattr getattr][write read]'
G.edge['vold']['sec-ril']['fill'] = 'red'
G.add_edge('vold','sec-ril')
G.edge['vold']['sec-ril']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][open open][setattr getattr][write read][append read]'
G.add_edge('vold','sensorhubservice')
G.edge['vold']['sensorhubservice']['write-read'] = '[write read]'
G.edge['vold']['sensorhubservice']['fill'] = 'red'
G.add_edge('vold','smdexe')
G.edge['vold']['smdexe']['write-read'] = '[open open][write read]'
G.edge['vold']['smdexe']['fill'] = 'red'
G.add_edge('vold','smdexe')
G.edge['vold']['smdexe']['write-read'] = '[open open][write read][append read]'
G.add_edge('vold','ssr_setup')
G.edge['vold']['ssr_setup']['write-read'] = '[open open][write read]'
G.edge['vold']['ssr_setup']['fill'] = 'red'
G.add_edge('vold','ssr_setup')
G.edge['vold']['ssr_setup']['write-read'] = '[open open][write read][append read]'
G.add_edge('vold','sswap')
G.edge['vold']['sswap']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['vold']['sswap']['fill'] = 'red'
G.add_edge('vold','sswap')
G.edge['vold']['sswap']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('vold','surfaceflinger')
G.edge['vold']['surfaceflinger']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][open open][write read][append read][open open][write read]'
G.edge['vold']['surfaceflinger']['fill'] = 'red'
G.add_edge('vold','surfaceflinger')
G.edge['vold']['surfaceflinger']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][open open][write read][append read][open open][write read][append read]'
G.add_edge('vold','surfaceflinger')
G.edge['vold']['surfaceflinger']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][open open][write read][append read][open open][write read][append read][write read]'
G.edge['vold']['surfaceflinger']['fill'] = 'red'
G.add_edge('vold','system_server')
G.edge['vold']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][open open][setattr getattr][write read]'
G.edge['vold']['system_server']['fill'] = 'red'
G.add_edge('vold','system_server')
G.edge['vold']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][open open][setattr getattr][write read][append read]'
G.add_edge('vold','system_server')
G.edge['vold']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][open open][setattr getattr][write read][append read][write read]'
G.edge['vold']['system_server']['fill'] = 'red'
G.add_edge('vold','system_server')
G.edge['vold']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read]'
G.add_edge('vold','thermald')
G.edge['vold']['thermald']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read]'
G.edge['vold']['thermald']['fill'] = 'red'
G.add_edge('vold','thermal-engine')
G.edge['vold']['thermal-engine']['write-read'] = '[setopt getopt][open open][write read]'
G.edge['vold']['thermal-engine']['fill'] = 'red'
G.add_edge('vold','thermal-engine')
G.edge['vold']['thermal-engine']['write-read'] = '[setopt getopt][open open][write read][append read]'
G.add_edge('vold','thermal-engine')
G.edge['vold']['thermal-engine']['write-read'] = '[setopt getopt][open open][write read][append read][write read]'
G.edge['vold']['thermal-engine']['fill'] = 'red'
G.add_edge('vold','ueventd')
G.edge['vold']['ueventd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][add_name search][remove_name search][open open][write read]'
G.edge['vold']['ueventd']['fill'] = 'red'
G.add_edge('vold','ueventd')
G.edge['vold']['ueventd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('vold','vm_bms')
G.edge['vold']['vm_bms']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['vold']['vm_bms']['fill'] = 'red'
G.add_edge('vold','vm_bms')
G.edge['vold']['vm_bms']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('vold','vmwared')
G.edge['vold']['vmwared']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][write read]'
G.edge['vold']['vmwared']['fill'] = 'red'
G.add_edge('vold','vold')
G.edge['vold']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][relabelto relabelfrom][relabelto relabelfrom][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read]'
G.edge['vold']['vold']['fill'] = 'red'
G.add_edge('vold','vold')
G.edge['vold']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][relabelto relabelfrom][relabelto relabelfrom][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read]'
G.add_edge('vold','zygote')
G.edge['vold']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][write read]'
G.edge['vold']['zygote']['fill'] = 'red'
app = Viewer(G)
app.mainloop()