import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('adbd','adbd')
G.edge['adbd']['adbd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][open open][open open][write read][append read][write read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][open open][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['adbd']['adbd']['fill'] = 'red'
G.add_edge('adbd','androidshmservice')
G.edge['adbd']['androidshmservice']['write-read'] = '[write read]'
G.edge['adbd']['androidshmservice']['fill'] = 'red'
G.add_edge('adbd','apaservice')
G.edge['adbd']['apaservice']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][write read]'
G.edge['adbd']['apaservice']['fill'] = 'red'
G.add_edge('adbd','appdomain')
G.edge['adbd']['appdomain']['write-read'] = '[open open][write read][append read][write read][open open][setattr getattr][open open][open open][write read][append read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][add_name search][remove_name search][open open][write read][add_name search][open open][setattr getattr][write read][append read][write read]'
G.edge['adbd']['appdomain']['fill'] = 'red'
G.add_edge('adbd','bintvoutservice')
G.edge['adbd']['bintvoutservice']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][add_name search][remove_name search][write read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['adbd']['bintvoutservice']['fill'] = 'red'
G.add_edge('adbd','bluetooth')
G.edge['adbd']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['adbd']['bluetooth']['fill'] = 'red'
G.add_edge('adbd','bugreport')
G.edge['adbd']['bugreport']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read]'
G.edge['adbd']['bugreport']['fill'] = 'red'
G.add_edge('adbd','charon')
G.edge['adbd']['charon']['write-read'] = '[write read]'
G.edge['adbd']['charon']['fill'] = 'red'
G.add_edge('adbd','drmserver')
G.edge['adbd']['drmserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['adbd']['drmserver']['fill'] = 'red'
G.add_edge('adbd','dumpstate')
G.edge['adbd']['dumpstate']['write-read'] = '[open open][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['adbd']['dumpstate']['fill'] = 'red'
G.add_edge('adbd','dumpsys')
G.edge['adbd']['dumpsys']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][write read]'
G.edge['adbd']['dumpsys']['fill'] = 'red'
G.add_edge('adbd','fixmo_app')
G.edge['adbd']['fixmo_app']['write-read'] = '[open open][write read][append read][open open][setattr getattr][open open][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read]'
G.edge['adbd']['fixmo_app']['fill'] = 'red'
G.add_edge('adbd','good_app')
G.edge['adbd']['good_app']['write-read'] = '[open open][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][open open][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read]'
G.edge['adbd']['good_app']['fill'] = 'red'
G.add_edge('adbd','healthd')
G.edge['adbd']['healthd']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read][write read]'
G.edge['adbd']['healthd']['fill'] = 'red'
G.add_edge('adbd','init_shell')
G.edge['adbd']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['adbd']['init_shell']['fill'] = 'red'
G.add_edge('adbd','init_shell')
G.edge['adbd']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][write read]'
G.edge['adbd']['init_shell']['fill'] = 'red'
G.add_edge('adbd','isolated_app')
G.edge['adbd']['isolated_app']['write-read'] = '[open open][setattr getattr][append read][write read]'
G.edge['adbd']['isolated_app']['fill'] = 'red'
G.add_edge('adbd','jackservice')
G.edge['adbd']['jackservice']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][write read]'
G.edge['adbd']['jackservice']['fill'] = 'red'
G.add_edge('adbd','keystore')
G.edge['adbd']['keystore']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][write read]'
G.edge['adbd']['keystore']['fill'] = 'red'
G.add_edge('adbd','mediaserver')
G.edge['adbd']['mediaserver']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['adbd']['mediaserver']['fill'] = 'red'
G.add_edge('adbd','nfc')
G.edge['adbd']['nfc']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['adbd']['nfc']['fill'] = 'red'
G.add_edge('adbd','oneseg_mw')
G.edge['adbd']['oneseg_mw']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['adbd']['oneseg_mw']['fill'] = 'red'
G.add_edge('adbd','radio')
G.edge['adbd']['radio']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['adbd']['radio']['fill'] = 'red'
G.add_edge('adbd','sensorhubservice')
G.edge['adbd']['sensorhubservice']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['adbd']['sensorhubservice']['fill'] = 'red'
G.add_edge('adbd','surfaceflinger')
G.edge['adbd']['surfaceflinger']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['adbd']['surfaceflinger']['fill'] = 'red'
G.add_edge('adbd','system_server')
G.edge['adbd']['system_server']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][write read][open open][setattr getattr][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][write read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['adbd']['system_server']['fill'] = 'red'
G.add_edge('adbd','zygote')
G.edge['adbd']['zygote']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['adbd']['zygote']['fill'] = 'red'
G.add_edge('androidshmservice','adbd')
G.edge['androidshmservice']['adbd']['write-read'] = '[write read]'
G.edge['androidshmservice']['adbd']['fill'] = 'red'
G.add_edge('androidshmservice','androidshmservice')
G.edge['androidshmservice']['androidshmservice']['write-read'] = '[write read]'
G.edge['androidshmservice']['androidshmservice']['fill'] = 'red'
G.add_edge('androidshmservice','apaservice')
G.edge['androidshmservice']['apaservice']['write-read'] = '[write read]'
G.edge['androidshmservice']['apaservice']['fill'] = 'red'
G.add_edge('androidshmservice','appdomain')
G.edge['androidshmservice']['appdomain']['write-read'] = '[write read]'
G.edge['androidshmservice']['appdomain']['fill'] = 'red'
G.add_edge('androidshmservice','bintvoutservice')
G.edge['androidshmservice']['bintvoutservice']['write-read'] = '[write read]'
G.edge['androidshmservice']['bintvoutservice']['fill'] = 'red'
G.add_edge('androidshmservice','bluetooth')
G.edge['androidshmservice']['bluetooth']['write-read'] = '[write read]'
G.edge['androidshmservice']['bluetooth']['fill'] = 'red'
G.add_edge('androidshmservice','bugreport')
G.edge['androidshmservice']['bugreport']['write-read'] = '[write read]'
G.edge['androidshmservice']['bugreport']['fill'] = 'red'
G.add_edge('androidshmservice','charon')
G.edge['androidshmservice']['charon']['write-read'] = '[write read]'
G.edge['androidshmservice']['charon']['fill'] = 'red'
G.add_edge('androidshmservice','drmserver')
G.edge['androidshmservice']['drmserver']['write-read'] = '[write read]'
G.edge['androidshmservice']['drmserver']['fill'] = 'red'
G.add_edge('androidshmservice','dumpstate')
G.edge['androidshmservice']['dumpstate']['write-read'] = '[write read]'
G.edge['androidshmservice']['dumpstate']['fill'] = 'red'
G.add_edge('androidshmservice','dumpsys')
G.edge['androidshmservice']['dumpsys']['write-read'] = '[write read]'
G.edge['androidshmservice']['dumpsys']['fill'] = 'red'
G.add_edge('androidshmservice','fixmo_app')
G.edge['androidshmservice']['fixmo_app']['write-read'] = '[write read]'
G.edge['androidshmservice']['fixmo_app']['fill'] = 'red'
G.add_edge('androidshmservice','good_app')
G.edge['androidshmservice']['good_app']['write-read'] = '[write read]'
G.edge['androidshmservice']['good_app']['fill'] = 'red'
G.add_edge('androidshmservice','healthd')
G.edge['androidshmservice']['healthd']['write-read'] = '[write read]'
G.edge['androidshmservice']['healthd']['fill'] = 'red'
G.add_edge('androidshmservice','init_shell')
G.edge['androidshmservice']['init_shell']['write-read'] = '[write read]'
G.edge['androidshmservice']['init_shell']['fill'] = 'red'
G.add_edge('androidshmservice','init_shell')
G.edge['androidshmservice']['init_shell']['write-read'] = '[write read][write read]'
G.edge['androidshmservice']['init_shell']['fill'] = 'red'
G.add_edge('androidshmservice','isolated_app')
G.edge['androidshmservice']['isolated_app']['write-read'] = '[write read]'
G.edge['androidshmservice']['isolated_app']['fill'] = 'red'
G.add_edge('androidshmservice','jackservice')
G.edge['androidshmservice']['jackservice']['write-read'] = '[write read]'
G.edge['androidshmservice']['jackservice']['fill'] = 'red'
G.add_edge('androidshmservice','keystore')
G.edge['androidshmservice']['keystore']['write-read'] = '[write read]'
G.edge['androidshmservice']['keystore']['fill'] = 'red'
G.add_edge('androidshmservice','mediaserver')
G.edge['androidshmservice']['mediaserver']['write-read'] = '[write read]'
G.edge['androidshmservice']['mediaserver']['fill'] = 'red'
G.add_edge('androidshmservice','nfc')
G.edge['androidshmservice']['nfc']['write-read'] = '[write read]'
G.edge['androidshmservice']['nfc']['fill'] = 'red'
G.add_edge('androidshmservice','oneseg_mw')
G.edge['androidshmservice']['oneseg_mw']['write-read'] = '[write read]'
G.edge['androidshmservice']['oneseg_mw']['fill'] = 'red'
G.add_edge('androidshmservice','radio')
G.edge['androidshmservice']['radio']['write-read'] = '[write read]'
G.edge['androidshmservice']['radio']['fill'] = 'red'
G.add_edge('androidshmservice','sensorhubservice')
G.edge['androidshmservice']['sensorhubservice']['write-read'] = '[write read]'
G.edge['androidshmservice']['sensorhubservice']['fill'] = 'red'
G.add_edge('androidshmservice','surfaceflinger')
G.edge['androidshmservice']['surfaceflinger']['write-read'] = '[write read]'
G.edge['androidshmservice']['surfaceflinger']['fill'] = 'red'
G.add_edge('androidshmservice','system_server')
G.edge['androidshmservice']['system_server']['write-read'] = '[write read]'
G.edge['androidshmservice']['system_server']['fill'] = 'red'
G.add_edge('androidshmservice','zygote')
G.edge['androidshmservice']['zygote']['write-read'] = '[write read]'
G.edge['androidshmservice']['zygote']['fill'] = 'red'
G.add_edge('apaservice','adbd')
G.edge['apaservice']['adbd']['write-read'] = '[open open][add_name search][remove_name search][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][write read]'
G.edge['apaservice']['adbd']['fill'] = 'red'
G.add_edge('apaservice','androidshmservice')
G.edge['apaservice']['androidshmservice']['write-read'] = '[write read]'
G.edge['apaservice']['androidshmservice']['fill'] = 'red'
G.add_edge('apaservice','apaservice')
G.edge['apaservice']['apaservice']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['apaservice']['apaservice']['fill'] = 'red'
G.add_edge('apaservice','appdomain')
G.edge['apaservice']['appdomain']['write-read'] = '[open open][setattr getattr][open open][setattr getattr][write read][append read][write read][write read]'
G.edge['apaservice']['appdomain']['fill'] = 'red'
G.add_edge('apaservice','bintvoutservice')
G.edge['apaservice']['bintvoutservice']['write-read'] = '[write read][write read]'
G.edge['apaservice']['bintvoutservice']['fill'] = 'red'
G.add_edge('apaservice','bluetooth')
G.edge['apaservice']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['apaservice']['bluetooth']['fill'] = 'red'
G.add_edge('apaservice','bugreport')
G.edge['apaservice']['bugreport']['write-read'] = '[open open][setattr getattr][write read][append read][write read]'
G.edge['apaservice']['bugreport']['fill'] = 'red'
G.add_edge('apaservice','charon')
G.edge['apaservice']['charon']['write-read'] = '[write read]'
G.edge['apaservice']['charon']['fill'] = 'red'
G.add_edge('apaservice','drmserver')
G.edge['apaservice']['drmserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][write read][write read]'
G.edge['apaservice']['drmserver']['fill'] = 'red'
G.add_edge('apaservice','dumpstate')
G.edge['apaservice']['dumpstate']['write-read'] = '[open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['apaservice']['dumpstate']['fill'] = 'red'
G.add_edge('apaservice','dumpsys')
G.edge['apaservice']['dumpsys']['write-read'] = '[open open][setattr getattr][write read][append read][write read]'
G.edge['apaservice']['dumpsys']['fill'] = 'red'
G.add_edge('apaservice','fixmo_app')
G.edge['apaservice']['fixmo_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read]'
G.edge['apaservice']['fixmo_app']['fill'] = 'red'
G.add_edge('apaservice','good_app')
G.edge['apaservice']['good_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read]'
G.edge['apaservice']['good_app']['fill'] = 'red'
G.add_edge('apaservice','healthd')
G.edge['apaservice']['healthd']['write-read'] = '[open open][write read][append read][write read]'
G.edge['apaservice']['healthd']['fill'] = 'red'
G.add_edge('apaservice','init_shell')
G.edge['apaservice']['init_shell']['write-read'] = '[open open][open open][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][open open][setattr getattr][write read][append read][write read]'
G.edge['apaservice']['init_shell']['fill'] = 'red'
G.add_edge('apaservice','init_shell')
G.edge['apaservice']['init_shell']['write-read'] = '[open open][open open][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][open open][setattr getattr][write read][append read][write read][write read]'
G.edge['apaservice']['init_shell']['fill'] = 'red'
G.add_edge('apaservice','isolated_app')
G.edge['apaservice']['isolated_app']['write-read'] = '[write read]'
G.edge['apaservice']['isolated_app']['fill'] = 'red'
G.add_edge('apaservice','jackservice')
G.edge['apaservice']['jackservice']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['apaservice']['jackservice']['fill'] = 'red'
G.add_edge('apaservice','keystore')
G.edge['apaservice']['keystore']['write-read'] = '[open open][write read][append read][write read]'
G.edge['apaservice']['keystore']['fill'] = 'red'
G.add_edge('apaservice','mediaserver')
G.edge['apaservice']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['apaservice']['mediaserver']['fill'] = 'red'
G.add_edge('apaservice','nfc')
G.edge['apaservice']['nfc']['write-read'] = '[write read]'
G.edge['apaservice']['nfc']['fill'] = 'red'
G.add_edge('apaservice','oneseg_mw')
G.edge['apaservice']['oneseg_mw']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][write read]'
G.edge['apaservice']['oneseg_mw']['fill'] = 'red'
G.add_edge('apaservice','radio')
G.edge['apaservice']['radio']['write-read'] = '[open open][write read][append read][write read]'
G.edge['apaservice']['radio']['fill'] = 'red'
G.add_edge('apaservice','sensorhubservice')
G.edge['apaservice']['sensorhubservice']['write-read'] = '[open open][write read][append read][write read]'
G.edge['apaservice']['sensorhubservice']['fill'] = 'red'
G.add_edge('apaservice','surfaceflinger')
G.edge['apaservice']['surfaceflinger']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][write read]'
G.edge['apaservice']['surfaceflinger']['fill'] = 'red'
G.add_edge('apaservice','system_server')
G.edge['apaservice']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][write read][write read]'
G.edge['apaservice']['system_server']['fill'] = 'red'
G.add_edge('apaservice','zygote')
G.edge['apaservice']['zygote']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read]'
G.edge['apaservice']['zygote']['fill'] = 'red'
G.add_edge('appdomain','adbd')
G.edge['appdomain']['adbd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open][write read][open open][write read][append read][open open][open open][open execmod][open execmod][setattr getattr][write read][append read][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read]'
G.edge['appdomain']['adbd']['fill'] = 'red'
G.add_edge('appdomain','androidshmservice')
G.edge['appdomain']['androidshmservice']['write-read'] = '[write read]'
G.edge['appdomain']['androidshmservice']['fill'] = 'red'
G.add_edge('appdomain','apaservice')
G.edge['appdomain']['apaservice']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][open execmod][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read]'
G.edge['appdomain']['apaservice']['fill'] = 'red'
G.add_edge('appdomain','appdomain')
G.edge['appdomain']['appdomain']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][write read][setattr getattr][write read][append read][setopt getopt][write read][open open][write read][append read][write read][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][setattr getattr][open execmod][write read][open open][open open][write read][append read][append read][open open][open open][write read][append read][append read][open open][write read][append read][open open][write read][append read][write read][write read][write read][write read][setopt getopt][setopt getopt][open open][setattr getattr][open execmod][write read][write read][open open][setattr getattr][write read][append read][write read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][add_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read][open open][write read][append read][open open][write read][append read][write read][setopt getopt][open open][write read][append read][write read]'
G.edge['appdomain']['appdomain']['fill'] = 'red'
G.add_edge('appdomain','bintvoutservice')
G.edge['appdomain']['bintvoutservice']['write-read'] = '[open open][write read][append read][write read]'
G.edge['appdomain']['bintvoutservice']['fill'] = 'red'
G.add_edge('appdomain','bluetooth')
G.edge['appdomain']['bluetooth']['write-read'] = '[write read][open open][open open][write read][append read][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][open open][write read][add_name search][remove_name search][add_name search][remove_name search][write read]'
G.edge['appdomain']['bluetooth']['fill'] = 'red'
G.add_edge('appdomain','bugreport')
G.edge['appdomain']['bugreport']['write-read'] = '[write read][append read][setattr getattr][write read][append read][write read]'
G.edge['appdomain']['bugreport']['fill'] = 'red'
G.add_edge('appdomain','charon')
G.edge['appdomain']['charon']['write-read'] = '[open open][write read][append read][write read]'
G.edge['appdomain']['charon']['fill'] = 'red'
G.add_edge('appdomain','drmserver')
G.edge['appdomain']['drmserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open execmod][open open][open execmod][setattr getattr][write read][append read][write read][append read][write read]'
G.edge['appdomain']['drmserver']['fill'] = 'red'
G.add_edge('appdomain','dumpstate')
G.edge['appdomain']['dumpstate']['write-read'] = '[open open][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][write read][append read][open open][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open execmod][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][write read]'
G.edge['appdomain']['dumpstate']['fill'] = 'red'
G.add_edge('appdomain','dumpsys')
G.edge['appdomain']['dumpsys']['write-read'] = '[write read][append read][setattr getattr][write read][append read][open open][write read][append read][write read]'
G.edge['appdomain']['dumpsys']['fill'] = 'red'
G.add_edge('appdomain','fixmo_app')
G.edge['appdomain']['fixmo_app']['write-read'] = '[open open][append read][open open][setattr getattr][open execmod][open open][append read][open open][append read][write read][write read][setopt getopt][open open][setattr getattr][open execmod][write read][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][write read]'
G.edge['appdomain']['fixmo_app']['fill'] = 'red'
G.add_edge('appdomain','good_app')
G.edge['appdomain']['good_app']['write-read'] = '[open open][append read][open open][setattr getattr][open execmod][open open][append read][open open][append read][write read][write read][setopt getopt][open open][setattr getattr][open execmod][write read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][write read]'
G.edge['appdomain']['good_app']['fill'] = 'red'
G.add_edge('appdomain','healthd')
G.edge['appdomain']['healthd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][write read]'
G.edge['appdomain']['healthd']['fill'] = 'red'
G.add_edge('appdomain','init_shell')
G.edge['appdomain']['init_shell']['write-read'] = '[setattr getattr][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open execmod][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][open execmod][write read]'
G.edge['appdomain']['init_shell']['fill'] = 'red'
G.add_edge('appdomain','init_shell')
G.edge['appdomain']['init_shell']['write-read'] = '[setattr getattr][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open execmod][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][open execmod][write read][write read]'
G.edge['appdomain']['init_shell']['fill'] = 'red'
G.add_edge('appdomain','isolated_app')
G.edge['appdomain']['isolated_app']['write-read'] = '[write read]'
G.edge['appdomain']['isolated_app']['fill'] = 'red'
G.add_edge('appdomain','jackservice')
G.edge['appdomain']['jackservice']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read]'
G.edge['appdomain']['jackservice']['fill'] = 'red'
G.add_edge('appdomain','keystore')
G.edge['appdomain']['keystore']['write-read'] = '[open open][write read][append read][write read]'
G.edge['appdomain']['keystore']['fill'] = 'red'
G.add_edge('appdomain','mediaserver')
G.edge['appdomain']['mediaserver']['write-read'] = '[open open][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open execmod][write read][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read]'
G.edge['appdomain']['mediaserver']['fill'] = 'red'
G.add_edge('appdomain','nfc')
G.edge['appdomain']['nfc']['write-read'] = '[open open][write read][append read][write read]'
G.edge['appdomain']['nfc']['fill'] = 'red'
G.add_edge('appdomain','oneseg_mw')
G.edge['appdomain']['oneseg_mw']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open execmod][setattr getattr][write read][append read][open open][write read][append read][write read]'
G.edge['appdomain']['oneseg_mw']['fill'] = 'red'
G.add_edge('appdomain','radio')
G.edge['appdomain']['radio']['write-read'] = '[setattr getattr][open open][write read][append read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][write read]'
G.edge['appdomain']['radio']['fill'] = 'red'
G.add_edge('appdomain','sensorhubservice')
G.edge['appdomain']['sensorhubservice']['write-read'] = '[open open][write read][append read][write read]'
G.edge['appdomain']['sensorhubservice']['fill'] = 'red'
G.add_edge('appdomain','surfaceflinger')
G.edge['appdomain']['surfaceflinger']['write-read'] = '[open open][write read][append read][write read][open open][open execmod][write read][append read][open open][write read][append read][open open][write read][append read][write read][write read]'
G.edge['appdomain']['surfaceflinger']['fill'] = 'red'
G.add_edge('appdomain','system_server')
G.edge['appdomain']['system_server']['write-read'] = '[open open][write read][append read][setattr getattr][add_name search][remove_name search][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open execmod][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][setattr getattr][write read][append read][open open][write read][append read][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open execmod][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][write read][write read][setopt getopt][open open][open execmod][open open][setattr getattr][write read][add_name search][remove_name search][open execmod][setattr getattr][write read][append read][write read][append read][write read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][write read][append read][write read]'
G.edge['appdomain']['system_server']['fill'] = 'red'
G.add_edge('appdomain','zygote')
G.edge['appdomain']['zygote']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][append read][write read][open open][write read][append read][open open][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][append read][write read]'
G.edge['appdomain']['zygote']['fill'] = 'red'
G.add_edge('appdomain','fixmo_app')
G.edge['appdomain']['fixmo_app']['write-read'] = '[open open][append read][open open][setattr getattr][open execmod][open open][append read][open open][append read][write read][write read][setopt getopt][open open][setattr getattr][open execmod][write read][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][write read][setopt getopt]'
G.add_edge('appdomain','good_app')
G.edge['appdomain']['good_app']['write-read'] = '[open open][append read][open open][setattr getattr][open execmod][open open][append read][open open][append read][write read][write read][setopt getopt][open open][setattr getattr][open execmod][write read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][write read][setopt getopt]'
G.add_edge('appdomain','ime_app')
G.edge['appdomain']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][add_name search][remove_name search][add_name search][setopt getopt]'
G.add_edge('appdomain','nfc')
G.edge['appdomain']['nfc']['write-read'] = '[open open][write read][append read][write read][setopt getopt]'
G.add_edge('appdomain','platformappdomain')
G.edge['appdomain']['platformappdomain']['write-read'] = '[write read][setopt getopt]'
G.add_edge('appdomain','radio')
G.edge['appdomain']['radio']['write-read'] = '[setattr getattr][open open][write read][append read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][write read][setopt getopt]'
G.add_edge('appdomain','samsung_app')
G.edge['appdomain']['samsung_app']['write-read'] = '[write read][append read][open open][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][setopt getopt]'
G.add_edge('appdomain','s_system_app')
G.edge['appdomain']['s_system_app']['write-read'] = '[setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open execmod][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][open open][open execmod][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][add_name search][remove_name search][add_name search][setopt getopt]'
G.add_edge('appdomain','system_app')
G.edge['appdomain']['system_app']['write-read'] = '[setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open execmod][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][open open][open execmod][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][add_name search][remove_name search][add_name search][setopt getopt]'
G.add_edge('appdomain','system_server')
G.edge['appdomain']['system_server']['write-read'] = '[open open][write read][append read][setattr getattr][add_name search][remove_name search][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open execmod][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][setattr getattr][write read][append read][open open][write read][append read][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open execmod][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][write read][write read][setopt getopt][open open][open execmod][open open][setattr getattr][write read][add_name search][remove_name search][open execmod][setattr getattr][write read][append read][write read][append read][write read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][write read][append read][write read][setopt getopt]'
G.add_edge('appdomain','untrusteddomain')
G.edge['appdomain']['untrusteddomain']['write-read'] = '[write read][append read][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][setopt getopt]'
G.add_edge('bintvoutservice','adbd')
G.edge['bintvoutservice']['adbd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['bintvoutservice']['adbd']['fill'] = 'red'
G.add_edge('bintvoutservice','androidshmservice')
G.edge['bintvoutservice']['androidshmservice']['write-read'] = '[write read]'
G.edge['bintvoutservice']['androidshmservice']['fill'] = 'red'
G.add_edge('bintvoutservice','apaservice')
G.edge['bintvoutservice']['apaservice']['write-read'] = '[write read]'
G.edge['bintvoutservice']['apaservice']['fill'] = 'red'
G.add_edge('bintvoutservice','appdomain')
G.edge['bintvoutservice']['appdomain']['write-read'] = '[open open][write read][append read][write read]'
G.edge['bintvoutservice']['appdomain']['fill'] = 'red'
G.add_edge('bintvoutservice','bintvoutservice')
G.edge['bintvoutservice']['bintvoutservice']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['bintvoutservice']['bintvoutservice']['fill'] = 'red'
G.add_edge('bintvoutservice','bluetooth')
G.edge['bintvoutservice']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['bintvoutservice']['bluetooth']['fill'] = 'red'
G.add_edge('bintvoutservice','bugreport')
G.edge['bintvoutservice']['bugreport']['write-read'] = '[write read]'
G.edge['bintvoutservice']['bugreport']['fill'] = 'red'
G.add_edge('bintvoutservice','charon')
G.edge['bintvoutservice']['charon']['write-read'] = '[write read]'
G.edge['bintvoutservice']['charon']['fill'] = 'red'
G.add_edge('bintvoutservice','drmserver')
G.edge['bintvoutservice']['drmserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['bintvoutservice']['drmserver']['fill'] = 'red'
G.add_edge('bintvoutservice','dumpstate')
G.edge['bintvoutservice']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['bintvoutservice']['dumpstate']['fill'] = 'red'
G.add_edge('bintvoutservice','dumpsys')
G.edge['bintvoutservice']['dumpsys']['write-read'] = '[write read]'
G.edge['bintvoutservice']['dumpsys']['fill'] = 'red'
G.add_edge('bintvoutservice','fixmo_app')
G.edge['bintvoutservice']['fixmo_app']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read]'
G.edge['bintvoutservice']['fixmo_app']['fill'] = 'red'
G.add_edge('bintvoutservice','good_app')
G.edge['bintvoutservice']['good_app']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read]'
G.edge['bintvoutservice']['good_app']['fill'] = 'red'
G.add_edge('bintvoutservice','healthd')
G.edge['bintvoutservice']['healthd']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read]'
G.edge['bintvoutservice']['healthd']['fill'] = 'red'
G.add_edge('bintvoutservice','init_shell')
G.edge['bintvoutservice']['init_shell']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['bintvoutservice']['init_shell']['fill'] = 'red'
G.add_edge('bintvoutservice','init_shell')
G.edge['bintvoutservice']['init_shell']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][write read]'
G.edge['bintvoutservice']['init_shell']['fill'] = 'red'
G.add_edge('bintvoutservice','isolated_app')
G.edge['bintvoutservice']['isolated_app']['write-read'] = '[open open][setattr getattr][append read][write read]'
G.edge['bintvoutservice']['isolated_app']['fill'] = 'red'
G.add_edge('bintvoutservice','jackservice')
G.edge['bintvoutservice']['jackservice']['write-read'] = '[write read][write read]'
G.edge['bintvoutservice']['jackservice']['fill'] = 'red'
G.add_edge('bintvoutservice','keystore')
G.edge['bintvoutservice']['keystore']['write-read'] = '[write read]'
G.edge['bintvoutservice']['keystore']['fill'] = 'red'
G.add_edge('bintvoutservice','mediaserver')
G.edge['bintvoutservice']['mediaserver']['write-read'] = '[open open][open open][setattr getattr][write read][append read][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['bintvoutservice']['mediaserver']['fill'] = 'red'
G.add_edge('bintvoutservice','nfc')
G.edge['bintvoutservice']['nfc']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['bintvoutservice']['nfc']['fill'] = 'red'
G.add_edge('bintvoutservice','oneseg_mw')
G.edge['bintvoutservice']['oneseg_mw']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['bintvoutservice']['oneseg_mw']['fill'] = 'red'
G.add_edge('bintvoutservice','radio')
G.edge['bintvoutservice']['radio']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['bintvoutservice']['radio']['fill'] = 'red'
G.add_edge('bintvoutservice','sensorhubservice')
G.edge['bintvoutservice']['sensorhubservice']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['bintvoutservice']['sensorhubservice']['fill'] = 'red'
G.add_edge('bintvoutservice','surfaceflinger')
G.edge['bintvoutservice']['surfaceflinger']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['bintvoutservice']['surfaceflinger']['fill'] = 'red'
G.add_edge('bintvoutservice','system_server')
G.edge['bintvoutservice']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['bintvoutservice']['system_server']['fill'] = 'red'
G.add_edge('bintvoutservice','zygote')
G.edge['bintvoutservice']['zygote']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['bintvoutservice']['zygote']['fill'] = 'red'
G.add_edge('bluetooth','adbd')
G.edge['bluetooth']['adbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][open open][write read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['bluetooth']['adbd']['fill'] = 'red'
G.add_edge('bluetooth','androidshmservice')
G.edge['bluetooth']['androidshmservice']['write-read'] = '[write read]'
G.edge['bluetooth']['androidshmservice']['fill'] = 'red'
G.add_edge('bluetooth','apaservice')
G.edge['bluetooth']['apaservice']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read]'
G.edge['bluetooth']['apaservice']['fill'] = 'red'
G.add_edge('bluetooth','appdomain')
G.edge['bluetooth']['appdomain']['write-read'] = '[write read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][add_name search][write read]'
G.edge['bluetooth']['appdomain']['fill'] = 'red'
G.add_edge('bluetooth','bintvoutservice')
G.edge['bluetooth']['bintvoutservice']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['bluetooth']['bintvoutservice']['fill'] = 'red'
G.add_edge('bluetooth','bluetooth')
G.edge['bluetooth']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][write read][open open][write read][setattr getattr][write read][append read][setopt getopt][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][write read][append read][open open][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][write read][write read]'
G.edge['bluetooth']['bluetooth']['fill'] = 'red'
G.add_edge('bluetooth','bugreport')
G.edge['bluetooth']['bugreport']['write-read'] = '[write read][append read][open open][setattr getattr][write read][append read][write read]'
G.edge['bluetooth']['bugreport']['fill'] = 'red'
G.add_edge('bluetooth','charon')
G.edge['bluetooth']['charon']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read]'
G.edge['bluetooth']['charon']['fill'] = 'red'
G.add_edge('bluetooth','drmserver')
G.edge['bluetooth']['drmserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['bluetooth']['drmserver']['fill'] = 'red'
G.add_edge('bluetooth','dumpstate')
G.edge['bluetooth']['dumpstate']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['bluetooth']['dumpstate']['fill'] = 'red'
G.add_edge('bluetooth','dumpsys')
G.edge['bluetooth']['dumpsys']['write-read'] = '[write read][append read][open open][setattr getattr][write read][append read][write read]'
G.edge['bluetooth']['dumpsys']['fill'] = 'red'
G.add_edge('bluetooth','fixmo_app')
G.edge['bluetooth']['fixmo_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read]'
G.edge['bluetooth']['fixmo_app']['fill'] = 'red'
G.add_edge('bluetooth','good_app')
G.edge['bluetooth']['good_app']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read]'
G.edge['bluetooth']['good_app']['fill'] = 'red'
G.add_edge('bluetooth','healthd')
G.edge['bluetooth']['healthd']['write-read'] = '[open open][write read][append read][write read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][write read]'
G.edge['bluetooth']['healthd']['fill'] = 'red'
G.add_edge('bluetooth','init_shell')
G.edge['bluetooth']['init_shell']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['bluetooth']['init_shell']['fill'] = 'red'
G.add_edge('bluetooth','init_shell')
G.edge['bluetooth']['init_shell']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][write read]'
G.edge['bluetooth']['init_shell']['fill'] = 'red'
G.add_edge('bluetooth','isolated_app')
G.edge['bluetooth']['isolated_app']['write-read'] = '[write read]'
G.edge['bluetooth']['isolated_app']['fill'] = 'red'
G.add_edge('bluetooth','jackservice')
G.edge['bluetooth']['jackservice']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][write read][open open][setattr getattr][write read][append read][write read]'
G.edge['bluetooth']['jackservice']['fill'] = 'red'
G.add_edge('bluetooth','keystore')
G.edge['bluetooth']['keystore']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read]'
G.edge['bluetooth']['keystore']['fill'] = 'red'
G.add_edge('bluetooth','mediaserver')
G.edge['bluetooth']['mediaserver']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read][append read][open open][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read][open open][setattr getattr][write read][append read][write read][write read][open open][setattr getattr][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][write read][write read]'
G.edge['bluetooth']['mediaserver']['fill'] = 'red'
G.add_edge('bluetooth','nfc')
G.edge['bluetooth']['nfc']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['bluetooth']['nfc']['fill'] = 'red'
G.add_edge('bluetooth','oneseg_mw')
G.edge['bluetooth']['oneseg_mw']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['bluetooth']['oneseg_mw']['fill'] = 'red'
G.add_edge('bluetooth','radio')
G.edge['bluetooth']['radio']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][write read][write read]'
G.edge['bluetooth']['radio']['fill'] = 'red'
G.add_edge('bluetooth','sensorhubservice')
G.edge['bluetooth']['sensorhubservice']['write-read'] = '[write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['bluetooth']['sensorhubservice']['fill'] = 'red'
G.add_edge('bluetooth','surfaceflinger')
G.edge['bluetooth']['surfaceflinger']['write-read'] = '[write read][open open][write read][append read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['bluetooth']['surfaceflinger']['fill'] = 'red'
G.add_edge('bluetooth','system_server')
G.edge['bluetooth']['system_server']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][setopt getopt][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][write read][write read]'
G.edge['bluetooth']['system_server']['fill'] = 'red'
G.add_edge('bluetooth','zygote')
G.edge['bluetooth']['zygote']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['bluetooth']['zygote']['fill'] = 'red'
G.add_edge('bugreport','adbd')
G.edge['bugreport']['adbd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][write read]'
G.edge['bugreport']['adbd']['fill'] = 'red'
G.add_edge('bugreport','androidshmservice')
G.edge['bugreport']['androidshmservice']['write-read'] = '[write read]'
G.edge['bugreport']['androidshmservice']['fill'] = 'red'
G.add_edge('bugreport','apaservice')
G.edge['bugreport']['apaservice']['write-read'] = '[open open][setattr getattr][write read][append read][write read]'
G.edge['bugreport']['apaservice']['fill'] = 'red'
G.add_edge('bugreport','appdomain')
G.edge['bugreport']['appdomain']['write-read'] = '[write read][write read]'
G.edge['bugreport']['appdomain']['fill'] = 'red'
G.add_edge('bugreport','bintvoutservice')
G.edge['bugreport']['bintvoutservice']['write-read'] = '[open open][write read][append read][write read]'
G.edge['bugreport']['bintvoutservice']['fill'] = 'red'
G.add_edge('bugreport','bluetooth')
G.edge['bugreport']['bluetooth']['write-read'] = '[write read][open open][setattr getattr][write read][append read][write read]'
G.edge['bugreport']['bluetooth']['fill'] = 'red'
G.add_edge('bugreport','bugreport')
G.edge['bugreport']['bugreport']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read]'
G.edge['bugreport']['bugreport']['fill'] = 'red'
G.add_edge('bugreport','charon')
G.edge['bugreport']['charon']['write-read'] = '[write read]'
G.edge['bugreport']['charon']['fill'] = 'red'
G.add_edge('bugreport','drmserver')
G.edge['bugreport']['drmserver']['write-read'] = '[open open][setattr getattr][write read][append read][write read][open open][open open][setattr getattr][write read][append read][write read][append read][write read]'
G.edge['bugreport']['drmserver']['fill'] = 'red'
G.add_edge('bugreport','dumpstate')
G.edge['bugreport']['dumpstate']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read]'
G.edge['bugreport']['dumpstate']['fill'] = 'red'
G.add_edge('bugreport','dumpsys')
G.edge['bugreport']['dumpsys']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read]'
G.edge['bugreport']['dumpsys']['fill'] = 'red'
G.add_edge('bugreport','fixmo_app')
G.edge['bugreport']['fixmo_app']['write-read'] = '[open open][setattr getattr][write read][append read][write read]'
G.edge['bugreport']['fixmo_app']['fill'] = 'red'
G.add_edge('bugreport','good_app')
G.edge['bugreport']['good_app']['write-read'] = '[write read]'
G.edge['bugreport']['good_app']['fill'] = 'red'
G.add_edge('bugreport','healthd')
G.edge['bugreport']['healthd']['write-read'] = '[write read]'
G.edge['bugreport']['healthd']['fill'] = 'red'
G.add_edge('bugreport','init_shell')
G.edge['bugreport']['init_shell']['write-read'] = '[write read]'
G.edge['bugreport']['init_shell']['fill'] = 'red'
G.add_edge('bugreport','init_shell')
G.edge['bugreport']['init_shell']['write-read'] = '[write read][write read]'
G.edge['bugreport']['init_shell']['fill'] = 'red'
G.add_edge('bugreport','isolated_app')
G.edge['bugreport']['isolated_app']['write-read'] = '[write read]'
G.edge['bugreport']['isolated_app']['fill'] = 'red'
G.add_edge('bugreport','jackservice')
G.edge['bugreport']['jackservice']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read]'
G.edge['bugreport']['jackservice']['fill'] = 'red'
G.add_edge('bugreport','keystore')
G.edge['bugreport']['keystore']['write-read'] = '[open open][setattr getattr][write read][append read][write read]'
G.edge['bugreport']['keystore']['fill'] = 'red'
G.add_edge('bugreport','mediaserver')
G.edge['bugreport']['mediaserver']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][write read]'
G.edge['bugreport']['mediaserver']['fill'] = 'red'
G.add_edge('bugreport','nfc')
G.edge['bugreport']['nfc']['write-read'] = '[open open][write read][append read][write read]'
G.edge['bugreport']['nfc']['fill'] = 'red'
G.add_edge('bugreport','oneseg_mw')
G.edge['bugreport']['oneseg_mw']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read]'
G.edge['bugreport']['oneseg_mw']['fill'] = 'red'
G.add_edge('bugreport','radio')
G.edge['bugreport']['radio']['write-read'] = '[write read][open open][setattr getattr][write read][append read][write read][write read]'
G.edge['bugreport']['radio']['fill'] = 'red'
G.add_edge('bugreport','sensorhubservice')
G.edge['bugreport']['sensorhubservice']['write-read'] = '[open open][write read][append read][write read]'
G.edge['bugreport']['sensorhubservice']['fill'] = 'red'
G.add_edge('bugreport','surfaceflinger')
G.edge['bugreport']['surfaceflinger']['write-read'] = '[write read][open open][write read][append read][write read]'
G.edge['bugreport']['surfaceflinger']['fill'] = 'red'
G.add_edge('bugreport','system_server')
G.edge['bugreport']['system_server']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][write read][write read]'
G.edge['bugreport']['system_server']['fill'] = 'red'
G.add_edge('bugreport','zygote')
G.edge['bugreport']['zygote']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read]'
G.edge['bugreport']['zygote']['fill'] = 'red'
G.add_edge('charon','adbd')
G.edge['charon']['adbd']['write-read'] = '[write read][add_name search][write read][write read]'
G.edge['charon']['adbd']['fill'] = 'red'
G.add_edge('charon','androidshmservice')
G.edge['charon']['androidshmservice']['write-read'] = '[write read]'
G.edge['charon']['androidshmservice']['fill'] = 'red'
G.add_edge('charon','apaservice')
G.edge['charon']['apaservice']['write-read'] = '[write read]'
G.edge['charon']['apaservice']['fill'] = 'red'
G.add_edge('charon','appdomain')
G.edge['charon']['appdomain']['write-read'] = '[write read][open open][write read][append read][write read]'
G.edge['charon']['appdomain']['fill'] = 'red'
G.add_edge('charon','bintvoutservice')
G.edge['charon']['bintvoutservice']['write-read'] = '[write read]'
G.edge['charon']['bintvoutservice']['fill'] = 'red'
G.add_edge('charon','bluetooth')
G.edge['charon']['bluetooth']['write-read'] = '[open open][open open][write read][append read][write read][append read][write read][open open][append read][write read]'
G.edge['charon']['bluetooth']['fill'] = 'red'
G.add_edge('charon','bugreport')
G.edge['charon']['bugreport']['write-read'] = '[write read][write read]'
G.edge['charon']['bugreport']['fill'] = 'red'
G.add_edge('charon','charon')
G.edge['charon']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['charon']['charon']['fill'] = 'red'
G.add_edge('charon','drmserver')
G.edge['charon']['drmserver']['write-read'] = '[open open][write read][append read][write read]'
G.edge['charon']['drmserver']['fill'] = 'red'
G.add_edge('charon','dumpstate')
G.edge['charon']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read][write read]'
G.edge['charon']['dumpstate']['fill'] = 'red'
G.add_edge('charon','dumpsys')
G.edge['charon']['dumpsys']['write-read'] = '[write read]'
G.edge['charon']['dumpsys']['fill'] = 'red'
G.add_edge('charon','fixmo_app')
G.edge['charon']['fixmo_app']['write-read'] = '[open open][write read][append read][write read]'
G.edge['charon']['fixmo_app']['fill'] = 'red'
G.add_edge('charon','good_app')
G.edge['charon']['good_app']['write-read'] = '[open open][write read][append read][write read]'
G.edge['charon']['good_app']['fill'] = 'red'
G.add_edge('charon','healthd')
G.edge['charon']['healthd']['write-read'] = '[write read][write read]'
G.edge['charon']['healthd']['fill'] = 'red'
G.add_edge('charon','init_shell')
G.edge['charon']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][write read]'
G.edge['charon']['init_shell']['fill'] = 'red'
G.add_edge('charon','init_shell')
G.edge['charon']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][write read][write read]'
G.edge['charon']['init_shell']['fill'] = 'red'
G.add_edge('charon','isolated_app')
G.edge['charon']['isolated_app']['write-read'] = '[write read]'
G.edge['charon']['isolated_app']['fill'] = 'red'
G.add_edge('charon','jackservice')
G.edge['charon']['jackservice']['write-read'] = '[add_name search][write read]'
G.edge['charon']['jackservice']['fill'] = 'red'
G.add_edge('charon','keystore')
G.edge['charon']['keystore']['write-read'] = '[open open][write read][append read][write read]'
G.edge['charon']['keystore']['fill'] = 'red'
G.add_edge('charon','mediaserver')
G.edge['charon']['mediaserver']['write-read'] = '[write read][write read][write read]'
G.edge['charon']['mediaserver']['fill'] = 'red'
G.add_edge('charon','nfc')
G.edge['charon']['nfc']['write-read'] = '[open open][write read][append read][write read][write read]'
G.edge['charon']['nfc']['fill'] = 'red'
G.add_edge('charon','oneseg_mw')
G.edge['charon']['oneseg_mw']['write-read'] = '[write read]'
G.edge['charon']['oneseg_mw']['fill'] = 'red'
G.add_edge('charon','radio')
G.edge['charon']['radio']['write-read'] = '[write read][write read]'
G.edge['charon']['radio']['fill'] = 'red'
G.add_edge('charon','sensorhubservice')
G.edge['charon']['sensorhubservice']['write-read'] = '[write read]'
G.edge['charon']['sensorhubservice']['fill'] = 'red'
G.add_edge('charon','surfaceflinger')
G.edge['charon']['surfaceflinger']['write-read'] = '[write read][write read]'
G.edge['charon']['surfaceflinger']['fill'] = 'red'
G.add_edge('charon','system_server')
G.edge['charon']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][write read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['charon']['system_server']['fill'] = 'red'
G.add_edge('charon','zygote')
G.edge['charon']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read][write read][write read][write read]'
G.edge['charon']['zygote']['fill'] = 'red'
G.add_edge('drmserver','adbd')
G.edge['drmserver']['adbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['drmserver']['adbd']['fill'] = 'red'
G.add_edge('drmserver','androidshmservice')
G.edge['drmserver']['androidshmservice']['write-read'] = '[write read]'
G.edge['drmserver']['androidshmservice']['fill'] = 'red'
G.add_edge('drmserver','apaservice')
G.edge['drmserver']['apaservice']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][write read][append read][write read]'
G.edge['drmserver']['apaservice']['fill'] = 'red'
G.add_edge('drmserver','appdomain')
G.edge['drmserver']['appdomain']['write-read'] = '[write read]'
G.edge['drmserver']['appdomain']['fill'] = 'red'
G.add_edge('drmserver','bintvoutservice')
G.edge['drmserver']['bintvoutservice']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][write read][append read][write read][write read][write read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['drmserver']['bintvoutservice']['fill'] = 'red'
G.add_edge('drmserver','bluetooth')
G.edge['drmserver']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['drmserver']['bluetooth']['fill'] = 'red'
G.add_edge('drmserver','bugreport')
G.edge['drmserver']['bugreport']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read]'
G.edge['drmserver']['bugreport']['fill'] = 'red'
G.add_edge('drmserver','charon')
G.edge['drmserver']['charon']['write-read'] = '[write read]'
G.edge['drmserver']['charon']['fill'] = 'red'
G.add_edge('drmserver','drmserver')
G.edge['drmserver']['drmserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][write read][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read]'
G.edge['drmserver']['drmserver']['fill'] = 'red'
G.add_edge('drmserver','dumpstate')
G.edge['drmserver']['dumpstate']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['drmserver']['dumpstate']['fill'] = 'red'
G.add_edge('drmserver','dumpsys')
G.edge['drmserver']['dumpsys']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][write read]'
G.edge['drmserver']['dumpsys']['fill'] = 'red'
G.add_edge('drmserver','fixmo_app')
G.edge['drmserver']['fixmo_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read]'
G.edge['drmserver']['fixmo_app']['fill'] = 'red'
G.add_edge('drmserver','good_app')
G.edge['drmserver']['good_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][write read]'
G.edge['drmserver']['good_app']['fill'] = 'red'
G.add_edge('drmserver','healthd')
G.edge['drmserver']['healthd']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read][append read][write read]'
G.edge['drmserver']['healthd']['fill'] = 'red'
G.add_edge('drmserver','init_shell')
G.edge['drmserver']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][setattr getattr][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][open open][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['drmserver']['init_shell']['fill'] = 'red'
G.add_edge('drmserver','init_shell')
G.edge['drmserver']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][setattr getattr][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][open open][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][write read]'
G.edge['drmserver']['init_shell']['fill'] = 'red'
G.add_edge('drmserver','isolated_app')
G.edge['drmserver']['isolated_app']['write-read'] = '[write read]'
G.edge['drmserver']['isolated_app']['fill'] = 'red'
G.add_edge('drmserver','jackservice')
G.edge['drmserver']['jackservice']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][write read][append read][write read]'
G.edge['drmserver']['jackservice']['fill'] = 'red'
G.add_edge('drmserver','keystore')
G.edge['drmserver']['keystore']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][append read][open open][write read][append read][write read]'
G.edge['drmserver']['keystore']['fill'] = 'red'
G.add_edge('drmserver','mediaserver')
G.edge['drmserver']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read][write read][open open][setattr getattr][write read][append read][write read][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read]'
G.edge['drmserver']['mediaserver']['fill'] = 'red'
G.add_edge('drmserver','nfc')
G.edge['drmserver']['nfc']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['drmserver']['nfc']['fill'] = 'red'
G.add_edge('drmserver','oneseg_mw')
G.edge['drmserver']['oneseg_mw']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['drmserver']['oneseg_mw']['fill'] = 'red'
G.add_edge('drmserver','radio')
G.edge['drmserver']['radio']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['drmserver']['radio']['fill'] = 'red'
G.add_edge('drmserver','sensorhubservice')
G.edge['drmserver']['sensorhubservice']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][write read][append read][open open][write read][append read][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['drmserver']['sensorhubservice']['fill'] = 'red'
G.add_edge('drmserver','surfaceflinger')
G.edge['drmserver']['surfaceflinger']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][write read][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['drmserver']['surfaceflinger']['fill'] = 'red'
G.add_edge('drmserver','system_server')
G.edge['drmserver']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][write read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][write read][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read]'
G.edge['drmserver']['system_server']['fill'] = 'red'
G.add_edge('drmserver','zygote')
G.edge['drmserver']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][add_name search][remove_name search][add_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['drmserver']['zygote']['fill'] = 'red'
G.add_edge('dumpstate','adbd')
G.edge['dumpstate']['adbd']['write-read'] = '[write read][add_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['dumpstate']['adbd']['fill'] = 'red'
G.add_edge('dumpstate','androidshmservice')
G.edge['dumpstate']['androidshmservice']['write-read'] = '[write read]'
G.edge['dumpstate']['androidshmservice']['fill'] = 'red'
G.add_edge('dumpstate','apaservice')
G.edge['dumpstate']['apaservice']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read]'
G.edge['dumpstate']['apaservice']['fill'] = 'red'
G.add_edge('dumpstate','appdomain')
G.edge['dumpstate']['appdomain']['write-read'] = '[open open][write read][append read][write read][setattr getattr][write read][append read][setopt getopt][open open][open open][write read][append read][append read][open open][write read][add_name search][open open][write read][add_name search][open open][setattr getattr][write read][append read][open open][write read][append read][write read]'
G.edge['dumpstate']['appdomain']['fill'] = 'red'
G.add_edge('dumpstate','bintvoutservice')
G.edge['dumpstate']['bintvoutservice']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['dumpstate']['bintvoutservice']['fill'] = 'red'
G.add_edge('dumpstate','bluetooth')
G.edge['dumpstate']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['dumpstate']['bluetooth']['fill'] = 'red'
G.add_edge('dumpstate','bugreport')
G.edge['dumpstate']['bugreport']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read]'
G.edge['dumpstate']['bugreport']['fill'] = 'red'
G.add_edge('dumpstate','charon')
G.edge['dumpstate']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['dumpstate']['charon']['fill'] = 'red'
G.add_edge('dumpstate','drmserver')
G.edge['dumpstate']['drmserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['dumpstate']['drmserver']['fill'] = 'red'
G.add_edge('dumpstate','dumpstate')
G.edge['dumpstate']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][open open][write read][append read][open open][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][write read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][open open][write read][append read][write read][open open][open open][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['dumpstate']['dumpstate']['fill'] = 'red'
G.add_edge('dumpstate','dumpsys')
G.edge['dumpstate']['dumpsys']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][write read]'
G.edge['dumpstate']['dumpsys']['fill'] = 'red'
G.add_edge('dumpstate','fixmo_app')
G.edge['dumpstate']['fixmo_app']['write-read'] = '[open open][append read][setattr getattr][open open][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][write read]'
G.edge['dumpstate']['fixmo_app']['fill'] = 'red'
G.add_edge('dumpstate','good_app')
G.edge['dumpstate']['good_app']['write-read'] = '[open open][append read][setattr getattr][open open][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][write read]'
G.edge['dumpstate']['good_app']['fill'] = 'red'
G.add_edge('dumpstate','healthd')
G.edge['dumpstate']['healthd']['write-read'] = '[open open][write read][append read][write read][write read]'
G.edge['dumpstate']['healthd']['fill'] = 'red'
G.add_edge('dumpstate','init_shell')
G.edge['dumpstate']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['dumpstate']['init_shell']['fill'] = 'red'
G.add_edge('dumpstate','init_shell')
G.edge['dumpstate']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][write read]'
G.edge['dumpstate']['init_shell']['fill'] = 'red'
G.add_edge('dumpstate','isolated_app')
G.edge['dumpstate']['isolated_app']['write-read'] = '[write read]'
G.edge['dumpstate']['isolated_app']['fill'] = 'red'
G.add_edge('dumpstate','jackservice')
G.edge['dumpstate']['jackservice']['write-read'] = '[add_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read]'
G.edge['dumpstate']['jackservice']['fill'] = 'red'
G.add_edge('dumpstate','keystore')
G.edge['dumpstate']['keystore']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][write read]'
G.edge['dumpstate']['keystore']['fill'] = 'red'
G.add_edge('dumpstate','mediaserver')
G.edge['dumpstate']['mediaserver']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read]'
G.edge['dumpstate']['mediaserver']['fill'] = 'red'
G.add_edge('dumpstate','nfc')
G.edge['dumpstate']['nfc']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['dumpstate']['nfc']['fill'] = 'red'
G.add_edge('dumpstate','oneseg_mw')
G.edge['dumpstate']['oneseg_mw']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['dumpstate']['oneseg_mw']['fill'] = 'red'
G.add_edge('dumpstate','radio')
G.edge['dumpstate']['radio']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['dumpstate']['radio']['fill'] = 'red'
G.add_edge('dumpstate','sensorhubservice')
G.edge['dumpstate']['sensorhubservice']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['dumpstate']['sensorhubservice']['fill'] = 'red'
G.add_edge('dumpstate','surfaceflinger')
G.edge['dumpstate']['surfaceflinger']['write-read'] = '[open open][write read][append read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['dumpstate']['surfaceflinger']['fill'] = 'red'
G.add_edge('dumpstate','system_server')
G.edge['dumpstate']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read][open open][setattr getattr][write read][append read][add_name search][remove_name search][open open][write read][append read][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read][write read]'
G.edge['dumpstate']['system_server']['fill'] = 'red'
G.add_edge('dumpstate','zygote')
G.edge['dumpstate']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][write read][open open][setattr getattr][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['dumpstate']['zygote']['fill'] = 'red'
G.add_edge('dumpsys','adbd')
G.edge['dumpsys']['adbd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][write read]'
G.edge['dumpsys']['adbd']['fill'] = 'red'
G.add_edge('dumpsys','androidshmservice')
G.edge['dumpsys']['androidshmservice']['write-read'] = '[write read]'
G.edge['dumpsys']['androidshmservice']['fill'] = 'red'
G.add_edge('dumpsys','apaservice')
G.edge['dumpsys']['apaservice']['write-read'] = '[open open][setattr getattr][write read][append read][write read]'
G.edge['dumpsys']['apaservice']['fill'] = 'red'
G.add_edge('dumpsys','appdomain')
G.edge['dumpsys']['appdomain']['write-read'] = '[write read][open open][setattr getattr][write read][append read][write read]'
G.edge['dumpsys']['appdomain']['fill'] = 'red'
G.add_edge('dumpsys','bintvoutservice')
G.edge['dumpsys']['bintvoutservice']['write-read'] = '[open open][write read][append read][write read]'
G.edge['dumpsys']['bintvoutservice']['fill'] = 'red'
G.add_edge('dumpsys','bluetooth')
G.edge['dumpsys']['bluetooth']['write-read'] = '[write read][open open][setattr getattr][write read][append read][write read]'
G.edge['dumpsys']['bluetooth']['fill'] = 'red'
G.add_edge('dumpsys','bugreport')
G.edge['dumpsys']['bugreport']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read]'
G.edge['dumpsys']['bugreport']['fill'] = 'red'
G.add_edge('dumpsys','charon')
G.edge['dumpsys']['charon']['write-read'] = '[write read]'
G.edge['dumpsys']['charon']['fill'] = 'red'
G.add_edge('dumpsys','drmserver')
G.edge['dumpsys']['drmserver']['write-read'] = '[open open][setattr getattr][write read][append read][write read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][write read][append read][write read]'
G.edge['dumpsys']['drmserver']['fill'] = 'red'
G.add_edge('dumpsys','dumpstate')
G.edge['dumpsys']['dumpstate']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][write read][open open][write read][append read][write read]'
G.edge['dumpsys']['dumpstate']['fill'] = 'red'
G.add_edge('dumpsys','dumpsys')
G.edge['dumpsys']['dumpsys']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][write read]'
G.edge['dumpsys']['dumpsys']['fill'] = 'red'
G.add_edge('dumpsys','fixmo_app')
G.edge['dumpsys']['fixmo_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read]'
G.edge['dumpsys']['fixmo_app']['fill'] = 'red'
G.add_edge('dumpsys','good_app')
G.edge['dumpsys']['good_app']['write-read'] = '[open open][setattr getattr][write read][append read][write read]'
G.edge['dumpsys']['good_app']['fill'] = 'red'
G.add_edge('dumpsys','healthd')
G.edge['dumpsys']['healthd']['write-read'] = '[write read][write read]'
G.edge['dumpsys']['healthd']['fill'] = 'red'
G.add_edge('dumpsys','init_shell')
G.edge['dumpsys']['init_shell']['write-read'] = '[open open][write read][append read][write read]'
G.edge['dumpsys']['init_shell']['fill'] = 'red'
G.add_edge('dumpsys','init_shell')
G.edge['dumpsys']['init_shell']['write-read'] = '[open open][write read][append read][write read][write read]'
G.edge['dumpsys']['init_shell']['fill'] = 'red'
G.add_edge('dumpsys','isolated_app')
G.edge['dumpsys']['isolated_app']['write-read'] = '[write read]'
G.edge['dumpsys']['isolated_app']['fill'] = 'red'
G.add_edge('dumpsys','jackservice')
G.edge['dumpsys']['jackservice']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read]'
G.edge['dumpsys']['jackservice']['fill'] = 'red'
G.add_edge('dumpsys','keystore')
G.edge['dumpsys']['keystore']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][write read]'
G.edge['dumpsys']['keystore']['fill'] = 'red'
G.add_edge('dumpsys','mediaserver')
G.edge['dumpsys']['mediaserver']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][write read]'
G.edge['dumpsys']['mediaserver']['fill'] = 'red'
G.add_edge('dumpsys','nfc')
G.edge['dumpsys']['nfc']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read]'
G.edge['dumpsys']['nfc']['fill'] = 'red'
G.add_edge('dumpsys','oneseg_mw')
G.edge['dumpsys']['oneseg_mw']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read]'
G.edge['dumpsys']['oneseg_mw']['fill'] = 'red'
G.add_edge('dumpsys','radio')
G.edge['dumpsys']['radio']['write-read'] = '[write read][open open][setattr getattr][write read][append read][write read]'
G.edge['dumpsys']['radio']['fill'] = 'red'
G.add_edge('dumpsys','sensorhubservice')
G.edge['dumpsys']['sensorhubservice']['write-read'] = '[open open][write read][append read][write read]'
G.edge['dumpsys']['sensorhubservice']['fill'] = 'red'
G.add_edge('dumpsys','surfaceflinger')
G.edge['dumpsys']['surfaceflinger']['write-read'] = '[write read][open open][write read][append read][write read][write read]'
G.edge['dumpsys']['surfaceflinger']['fill'] = 'red'
G.add_edge('dumpsys','system_server')
G.edge['dumpsys']['system_server']['write-read'] = '[open open][write read][append read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read]'
G.edge['dumpsys']['system_server']['fill'] = 'red'
G.add_edge('dumpsys','zygote')
G.edge['dumpsys']['zygote']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read]'
G.edge['dumpsys']['zygote']['fill'] = 'red'
G.add_edge('fixmo_app','adbd')
G.edge['fixmo_app']['adbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read]'
G.edge['fixmo_app']['adbd']['fill'] = 'red'
G.add_edge('fixmo_app','androidshmservice')
G.edge['fixmo_app']['androidshmservice']['write-read'] = '[write read]'
G.edge['fixmo_app']['androidshmservice']['fill'] = 'red'
G.add_edge('fixmo_app','apaservice')
G.edge['fixmo_app']['apaservice']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read]'
G.edge['fixmo_app']['apaservice']['fill'] = 'red'
G.add_edge('fixmo_app','appdomain')
G.edge['fixmo_app']['appdomain']['write-read'] = '[write read][open open][setattr getattr][open execmod][open open][open open][write read][write read][setopt getopt][setopt getopt][open open][setattr getattr][open execmod][write read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][open open][setattr getattr][write read][append read][open open][write read][append read][write read]'
G.edge['fixmo_app']['appdomain']['fill'] = 'red'
G.add_edge('fixmo_app','bintvoutservice')
G.edge['fixmo_app']['bintvoutservice']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][append read][write read]'
G.edge['fixmo_app']['bintvoutservice']['fill'] = 'red'
G.add_edge('fixmo_app','bluetooth')
G.edge['fixmo_app']['bluetooth']['write-read'] = '[setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][add_name search][remove_name search][write read]'
G.edge['fixmo_app']['bluetooth']['fill'] = 'red'
G.add_edge('fixmo_app','bugreport')
G.edge['fixmo_app']['bugreport']['write-read'] = '[open open][setattr getattr][write read][append read][write read]'
G.edge['fixmo_app']['bugreport']['fill'] = 'red'
G.add_edge('fixmo_app','charon')
G.edge['fixmo_app']['charon']['write-read'] = '[open open][write read][append read][write read]'
G.edge['fixmo_app']['charon']['fill'] = 'red'
G.add_edge('fixmo_app','drmserver')
G.edge['fixmo_app']['drmserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open execmod][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][write read]'
G.edge['fixmo_app']['drmserver']['fill'] = 'red'
G.add_edge('fixmo_app','dumpstate')
G.edge['fixmo_app']['dumpstate']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][open open][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][write read]'
G.edge['fixmo_app']['dumpstate']['fill'] = 'red'
G.add_edge('fixmo_app','dumpsys')
G.edge['fixmo_app']['dumpsys']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][write read]'
G.edge['fixmo_app']['dumpsys']['fill'] = 'red'
G.add_edge('fixmo_app','fixmo_app')
G.edge['fixmo_app']['fixmo_app']['write-read'] = '[write read][setopt getopt][write read][setopt getopt][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][write read][setopt getopt][setattr getattr][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][setopt getopt][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][open execmod][open open][write read][setopt getopt][open open][setattr getattr][open execmod][write read][setopt getopt][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][write read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read]'
G.edge['fixmo_app']['fixmo_app']['fill'] = 'red'
G.add_edge('fixmo_app','good_app')
G.edge['fixmo_app']['good_app']['write-read'] = '[write read][setopt getopt][write read][setopt getopt][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][write read][setopt getopt][write read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][add_name search][remove_name search][write read][setopt getopt][open open][write read][append read][open open][write read][setopt getopt][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][open execmod][open open][write read][setopt getopt][open open][setattr getattr][open execmod][write read][setopt getopt][open open][write read][append read][open open][write read][append read][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][write read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read]'
G.edge['fixmo_app']['good_app']['fill'] = 'red'
G.add_edge('fixmo_app','healthd')
G.edge['fixmo_app']['healthd']['write-read'] = '[open open][write read][append read][write read][write read]'
G.edge['fixmo_app']['healthd']['fill'] = 'red'
G.add_edge('fixmo_app','init_shell')
G.edge['fixmo_app']['init_shell']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open execmod][open open][setattr getattr][write read][append read][open open][open open][add_name search][remove_name search][add_name search][remove_name search][write read]'
G.edge['fixmo_app']['init_shell']['fill'] = 'red'
G.add_edge('fixmo_app','init_shell')
G.edge['fixmo_app']['init_shell']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open execmod][open open][setattr getattr][write read][append read][open open][open open][add_name search][remove_name search][add_name search][remove_name search][write read][write read]'
G.edge['fixmo_app']['init_shell']['fill'] = 'red'
G.add_edge('fixmo_app','isolated_app')
G.edge['fixmo_app']['isolated_app']['write-read'] = '[open open][setattr getattr][append read][write read]'
G.edge['fixmo_app']['isolated_app']['fill'] = 'red'
G.add_edge('fixmo_app','jackservice')
G.edge['fixmo_app']['jackservice']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read]'
G.edge['fixmo_app']['jackservice']['fill'] = 'red'
G.add_edge('fixmo_app','keystore')
G.edge['fixmo_app']['keystore']['write-read'] = '[write read]'
G.edge['fixmo_app']['keystore']['fill'] = 'red'
G.add_edge('fixmo_app','mediaserver')
G.edge['fixmo_app']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][add_name search][remove_name search][setattr getattr][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read][setopt getopt][open open][setattr getattr][write read][append read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][write read]'
G.edge['fixmo_app']['mediaserver']['fill'] = 'red'
G.add_edge('fixmo_app','nfc')
G.edge['fixmo_app']['nfc']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read]'
G.edge['fixmo_app']['nfc']['fill'] = 'red'
G.add_edge('fixmo_app','oneseg_mw')
G.edge['fixmo_app']['oneseg_mw']['write-read'] = '[write read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][write read]'
G.edge['fixmo_app']['oneseg_mw']['fill'] = 'red'
G.add_edge('fixmo_app','radio')
G.edge['fixmo_app']['radio']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read][setopt getopt][open open][write read][append read][open open][write read][append read][write read]'
G.edge['fixmo_app']['radio']['fill'] = 'red'
G.add_edge('fixmo_app','sensorhubservice')
G.edge['fixmo_app']['sensorhubservice']['write-read'] = '[open open][write read][append read][write read]'
G.edge['fixmo_app']['sensorhubservice']['fill'] = 'red'
G.add_edge('fixmo_app','surfaceflinger')
G.edge['fixmo_app']['surfaceflinger']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][write read]'
G.edge['fixmo_app']['surfaceflinger']['fill'] = 'red'
G.add_edge('fixmo_app','system_server')
G.edge['fixmo_app']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open execmod][open open][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open execmod][open open][setattr getattr][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open execmod][write read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][write read]'
G.edge['fixmo_app']['system_server']['fill'] = 'red'
G.add_edge('fixmo_app','zygote')
G.edge['fixmo_app']['zygote']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][add_name search][remove_name search][append read][write read][open open][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['fixmo_app']['zygote']['fill'] = 'red'
G.add_edge('fixmo_app','fixmo_app')
G.edge['fixmo_app']['fixmo_app']['write-read'] = '[write read][setopt getopt][write read][setopt getopt][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][write read][setopt getopt][setattr getattr][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][setopt getopt][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][open execmod][open open][write read][setopt getopt][open open][setattr getattr][open execmod][write read][setopt getopt][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][write read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read][setopt getopt]'
G.add_edge('fixmo_app','good_app')
G.edge['fixmo_app']['good_app']['write-read'] = '[write read][setopt getopt][write read][setopt getopt][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][write read][setopt getopt][write read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][add_name search][remove_name search][write read][setopt getopt][open open][write read][append read][open open][write read][setopt getopt][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][open execmod][open open][write read][setopt getopt][open open][setattr getattr][open execmod][write read][setopt getopt][open open][write read][append read][open open][write read][append read][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][write read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][setopt getopt]'
G.add_edge('fixmo_app','ime_app')
G.edge['fixmo_app']['ime_app']['write-read'] = '[open open][write read][append read][open open][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][open open][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][setopt getopt]'
G.add_edge('fixmo_app','nfc')
G.edge['fixmo_app']['nfc']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read][setopt getopt]'
G.add_edge('fixmo_app','platformappdomain')
G.edge['fixmo_app']['platformappdomain']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setopt getopt]'
G.add_edge('fixmo_app','radio')
G.edge['fixmo_app']['radio']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read][setopt getopt][open open][write read][append read][open open][write read][append read][write read][setopt getopt]'
G.add_edge('fixmo_app','samsung_app')
G.edge['fixmo_app']['samsung_app']['write-read'] = '[open open][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setopt getopt]'
G.add_edge('fixmo_app','s_system_app')
G.edge['fixmo_app']['s_system_app']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open execmod][open open][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][open open][setattr getattr][write read][add_name search][remove_name search][setopt getopt]'
G.add_edge('fixmo_app','system_app')
G.edge['fixmo_app']['system_app']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open execmod][open open][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][open open][setattr getattr][write read][add_name search][remove_name search][setopt getopt]'
G.add_edge('fixmo_app','system_server')
G.edge['fixmo_app']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open execmod][open open][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open execmod][open open][setattr getattr][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open execmod][write read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][write read][setopt getopt]'
G.add_edge('fixmo_app','untrusteddomain')
G.edge['fixmo_app']['untrusteddomain']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][setattr getattr][write read][append read][setopt getopt][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][setopt getopt]'
G.add_edge('good_app','adbd')
G.edge['good_app']['adbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read][setattr getattr][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read]'
G.edge['good_app']['adbd']['fill'] = 'red'
G.add_edge('good_app','androidshmservice')
G.edge['good_app']['androidshmservice']['write-read'] = '[write read]'
G.edge['good_app']['androidshmservice']['fill'] = 'red'
G.add_edge('good_app','apaservice')
G.edge['good_app']['apaservice']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][write read]'
G.edge['good_app']['apaservice']['fill'] = 'red'
G.add_edge('good_app','appdomain')
G.edge['good_app']['appdomain']['write-read'] = '[write read][open open][setattr getattr][open execmod][open open][open open][write read][write read][setopt getopt][setopt getopt][open open][setattr getattr][open execmod][write read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][open open][setattr getattr][write read][append read][open open][write read][append read][write read]'
G.edge['good_app']['appdomain']['fill'] = 'red'
G.add_edge('good_app','bintvoutservice')
G.edge['good_app']['bintvoutservice']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][write read]'
G.edge['good_app']['bintvoutservice']['fill'] = 'red'
G.add_edge('good_app','bluetooth')
G.edge['good_app']['bluetooth']['write-read'] = '[setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][add_name search][remove_name search][write read]'
G.edge['good_app']['bluetooth']['fill'] = 'red'
G.add_edge('good_app','bugreport')
G.edge['good_app']['bugreport']['write-read'] = '[open open][setattr getattr][write read][append read][write read]'
G.edge['good_app']['bugreport']['fill'] = 'red'
G.add_edge('good_app','charon')
G.edge['good_app']['charon']['write-read'] = '[open open][write read][append read][write read]'
G.edge['good_app']['charon']['fill'] = 'red'
G.add_edge('good_app','drmserver')
G.edge['good_app']['drmserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open execmod][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][write read][write read]'
G.edge['good_app']['drmserver']['fill'] = 'red'
G.add_edge('good_app','dumpstate')
G.edge['good_app']['dumpstate']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][open open][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][write read]'
G.edge['good_app']['dumpstate']['fill'] = 'red'
G.add_edge('good_app','dumpsys')
G.edge['good_app']['dumpsys']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][write read]'
G.edge['good_app']['dumpsys']['fill'] = 'red'
G.add_edge('good_app','fixmo_app')
G.edge['good_app']['fixmo_app']['write-read'] = '[write read][setopt getopt][write read][setopt getopt][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][write read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][setopt getopt][open open][write read][append read][open open][write read][setopt getopt][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][open execmod][open open][write read][setopt getopt][open open][setattr getattr][open execmod][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][write read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read]'
G.edge['good_app']['fixmo_app']['fill'] = 'red'
G.add_edge('good_app','good_app')
G.edge['good_app']['good_app']['write-read'] = '[write read][setopt getopt][write read][setopt getopt][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][write read][setopt getopt][write read][setopt getopt][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][setopt getopt][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][open execmod][open open][write read][setopt getopt][open open][setattr getattr][open execmod][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][write read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read]'
G.edge['good_app']['good_app']['fill'] = 'red'
G.add_edge('good_app','healthd')
G.edge['good_app']['healthd']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read][write read]'
G.edge['good_app']['healthd']['fill'] = 'red'
G.add_edge('good_app','init_shell')
G.edge['good_app']['init_shell']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open execmod][open open][setattr getattr][write read][append read][open open][open open][add_name search][remove_name search][add_name search][remove_name search][write read]'
G.edge['good_app']['init_shell']['fill'] = 'red'
G.add_edge('good_app','init_shell')
G.edge['good_app']['init_shell']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open execmod][open open][setattr getattr][write read][append read][open open][open open][add_name search][remove_name search][add_name search][remove_name search][write read][write read]'
G.edge['good_app']['init_shell']['fill'] = 'red'
G.add_edge('good_app','isolated_app')
G.edge['good_app']['isolated_app']['write-read'] = '[open open][setattr getattr][append read][write read]'
G.edge['good_app']['isolated_app']['fill'] = 'red'
G.add_edge('good_app','jackservice')
G.edge['good_app']['jackservice']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][write read]'
G.edge['good_app']['jackservice']['fill'] = 'red'
G.add_edge('good_app','keystore')
G.edge['good_app']['keystore']['write-read'] = '[open open][write read][append read][write read]'
G.edge['good_app']['keystore']['fill'] = 'red'
G.add_edge('good_app','mediaserver')
G.edge['good_app']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][write read][append read][open open][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][write read]'
G.edge['good_app']['mediaserver']['fill'] = 'red'
G.add_edge('good_app','nfc')
G.edge['good_app']['nfc']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read]'
G.edge['good_app']['nfc']['fill'] = 'red'
G.add_edge('good_app','oneseg_mw')
G.edge['good_app']['oneseg_mw']['write-read'] = '[write read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read]'
G.edge['good_app']['oneseg_mw']['fill'] = 'red'
G.add_edge('good_app','radio')
G.edge['good_app']['radio']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read]'
G.edge['good_app']['radio']['fill'] = 'red'
G.add_edge('good_app','sensorhubservice')
G.edge['good_app']['sensorhubservice']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read]'
G.edge['good_app']['sensorhubservice']['fill'] = 'red'
G.add_edge('good_app','surfaceflinger')
G.edge['good_app']['surfaceflinger']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][write read]'
G.edge['good_app']['surfaceflinger']['fill'] = 'red'
G.add_edge('good_app','system_server')
G.edge['good_app']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open execmod][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open execmod][open open][setattr getattr][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open execmod][write read][open open][setattr getattr][write read][append read][write read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][write read]'
G.edge['good_app']['system_server']['fill'] = 'red'
G.add_edge('good_app','zygote')
G.edge['good_app']['zygote']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][append read][write read][open open][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read]'
G.edge['good_app']['zygote']['fill'] = 'red'
G.add_edge('good_app','fixmo_app')
G.edge['good_app']['fixmo_app']['write-read'] = '[write read][setopt getopt][write read][setopt getopt][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][write read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][setopt getopt][open open][write read][append read][open open][write read][setopt getopt][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][open execmod][open open][write read][setopt getopt][open open][setattr getattr][open execmod][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][write read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][setopt getopt]'
G.add_edge('good_app','good_app')
G.edge['good_app']['good_app']['write-read'] = '[write read][setopt getopt][write read][setopt getopt][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][write read][setopt getopt][write read][setopt getopt][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][setopt getopt][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][open execmod][open open][write read][setopt getopt][open open][setattr getattr][open execmod][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][write read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][setopt getopt]'
G.add_edge('good_app','ime_app')
G.edge['good_app']['ime_app']['write-read'] = '[open open][write read][append read][open open][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][open open][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][setopt getopt]'
G.add_edge('good_app','nfc')
G.edge['good_app']['nfc']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read][setopt getopt]'
G.add_edge('good_app','platformappdomain')
G.edge['good_app']['platformappdomain']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setopt getopt]'
G.add_edge('good_app','radio')
G.edge['good_app']['radio']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][setopt getopt]'
G.add_edge('good_app','samsung_app')
G.edge['good_app']['samsung_app']['write-read'] = '[open open][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setopt getopt]'
G.add_edge('good_app','s_system_app')
G.edge['good_app']['s_system_app']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open execmod][open open][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][setopt getopt]'
G.add_edge('good_app','system_app')
G.edge['good_app']['system_app']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open execmod][open open][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][setopt getopt]'
G.add_edge('good_app','system_server')
G.edge['good_app']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open execmod][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open execmod][open open][setattr getattr][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open execmod][write read][open open][setattr getattr][write read][append read][write read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][write read][setopt getopt]'
G.add_edge('good_app','untrusteddomain')
G.edge['good_app']['untrusteddomain']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][setattr getattr][write read][append read][setopt getopt][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][setopt getopt]'
G.add_edge('healthd','adbd')
G.edge['healthd']['adbd']['write-read'] = '[open open][write read][write read]'
G.edge['healthd']['adbd']['fill'] = 'red'
G.add_edge('healthd','androidshmservice')
G.edge['healthd']['androidshmservice']['write-read'] = '[write read]'
G.edge['healthd']['androidshmservice']['fill'] = 'red'
G.add_edge('healthd','apaservice')
G.edge['healthd']['apaservice']['write-read'] = '[write read]'
G.edge['healthd']['apaservice']['fill'] = 'red'
G.add_edge('healthd','appdomain')
G.edge['healthd']['appdomain']['write-read'] = '[open open][write read][append read][write read]'
G.edge['healthd']['appdomain']['fill'] = 'red'
G.add_edge('healthd','bintvoutservice')
G.edge['healthd']['bintvoutservice']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['healthd']['bintvoutservice']['fill'] = 'red'
G.add_edge('healthd','bluetooth')
G.edge['healthd']['bluetooth']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][write read]'
G.edge['healthd']['bluetooth']['fill'] = 'red'
G.add_edge('healthd','bugreport')
G.edge['healthd']['bugreport']['write-read'] = '[write read]'
G.edge['healthd']['bugreport']['fill'] = 'red'
G.add_edge('healthd','charon')
G.edge['healthd']['charon']['write-read'] = '[write read]'
G.edge['healthd']['charon']['fill'] = 'red'
G.add_edge('healthd','drmserver')
G.edge['healthd']['drmserver']['write-read'] = '[write read]'
G.edge['healthd']['drmserver']['fill'] = 'red'
G.add_edge('healthd','dumpstate')
G.edge['healthd']['dumpstate']['write-read'] = '[open open][write read][append read][write read]'
G.edge['healthd']['dumpstate']['fill'] = 'red'
G.add_edge('healthd','dumpsys')
G.edge['healthd']['dumpsys']['write-read'] = '[write read]'
G.edge['healthd']['dumpsys']['fill'] = 'red'
G.add_edge('healthd','fixmo_app')
G.edge['healthd']['fixmo_app']['write-read'] = '[open open][write read][append read][write read]'
G.edge['healthd']['fixmo_app']['fill'] = 'red'
G.add_edge('healthd','good_app')
G.edge['healthd']['good_app']['write-read'] = '[open open][write read][append read][write read]'
G.edge['healthd']['good_app']['fill'] = 'red'
G.add_edge('healthd','healthd')
G.edge['healthd']['healthd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][write read][write read][write read]'
G.edge['healthd']['healthd']['fill'] = 'red'
G.add_edge('healthd','init_shell')
G.edge['healthd']['init_shell']['write-read'] = '[open open][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][write read][append read][open open][write read][append read][write read]'
G.edge['healthd']['init_shell']['fill'] = 'red'
G.add_edge('healthd','init_shell')
G.edge['healthd']['init_shell']['write-read'] = '[open open][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][write read][append read][open open][write read][append read][write read][write read]'
G.edge['healthd']['init_shell']['fill'] = 'red'
G.add_edge('healthd','isolated_app')
G.edge['healthd']['isolated_app']['write-read'] = '[open open][setattr getattr][append read][write read]'
G.edge['healthd']['isolated_app']['fill'] = 'red'
G.add_edge('healthd','jackservice')
G.edge['healthd']['jackservice']['write-read'] = '[write read][write read]'
G.edge['healthd']['jackservice']['fill'] = 'red'
G.add_edge('healthd','keystore')
G.edge['healthd']['keystore']['write-read'] = '[write read]'
G.edge['healthd']['keystore']['fill'] = 'red'
G.add_edge('healthd','mediaserver')
G.edge['healthd']['mediaserver']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][write read]'
G.edge['healthd']['mediaserver']['fill'] = 'red'
G.add_edge('healthd','nfc')
G.edge['healthd']['nfc']['write-read'] = '[open open][write read][append read][write read]'
G.edge['healthd']['nfc']['fill'] = 'red'
G.add_edge('healthd','oneseg_mw')
G.edge['healthd']['oneseg_mw']['write-read'] = '[write read]'
G.edge['healthd']['oneseg_mw']['fill'] = 'red'
G.add_edge('healthd','radio')
G.edge['healthd']['radio']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][write read]'
G.edge['healthd']['radio']['fill'] = 'red'
G.add_edge('healthd','sensorhubservice')
G.edge['healthd']['sensorhubservice']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read]'
G.edge['healthd']['sensorhubservice']['fill'] = 'red'
G.add_edge('healthd','surfaceflinger')
G.edge['healthd']['surfaceflinger']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][write read]'
G.edge['healthd']['surfaceflinger']['fill'] = 'red'
G.add_edge('healthd','system_server')
G.edge['healthd']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read]'
G.edge['healthd']['system_server']['fill'] = 'red'
G.add_edge('healthd','zygote')
G.edge['healthd']['zygote']['write-read'] = '[open open][write read][append read][write read]'
G.edge['healthd']['zygote']['fill'] = 'red'
G.add_edge('init_shell','adbd')
G.edge['init_shell']['adbd']['write-read'] = '[write read][add_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['init_shell']['adbd']['fill'] = 'red'
G.add_edge('init_shell','androidshmservice')
G.edge['init_shell']['androidshmservice']['write-read'] = '[write read]'
G.edge['init_shell']['androidshmservice']['fill'] = 'red'
G.add_edge('init_shell','apaservice')
G.edge['init_shell']['apaservice']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][write read]'
G.edge['init_shell']['apaservice']['fill'] = 'red'
G.add_edge('init_shell','appdomain')
G.edge['init_shell']['appdomain']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][append read][write read]'
G.edge['init_shell']['appdomain']['fill'] = 'red'
G.add_edge('init_shell','bintvoutservice')
G.edge['init_shell']['bintvoutservice']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['init_shell']['bintvoutservice']['fill'] = 'red'
G.add_edge('init_shell','bluetooth')
G.edge['init_shell']['bluetooth']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][add_name search][remove_name search][open open][write read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['init_shell']['bluetooth']['fill'] = 'red'
G.add_edge('init_shell','bugreport')
G.edge['init_shell']['bugreport']['write-read'] = '[write read]'
G.edge['init_shell']['bugreport']['fill'] = 'red'
G.add_edge('init_shell','charon')
G.edge['init_shell']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read]'
G.edge['init_shell']['charon']['fill'] = 'red'
G.add_edge('init_shell','drmserver')
G.edge['init_shell']['drmserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['init_shell']['drmserver']['fill'] = 'red'
G.add_edge('init_shell','dumpstate')
G.edge['init_shell']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['init_shell']['dumpstate']['fill'] = 'red'
G.add_edge('init_shell','dumpsys')
G.edge['init_shell']['dumpsys']['write-read'] = '[open open][write read][append read][write read]'
G.edge['init_shell']['dumpsys']['fill'] = 'red'
G.add_edge('init_shell','fixmo_app')
G.edge['init_shell']['fixmo_app']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['init_shell']['fixmo_app']['fill'] = 'red'
G.add_edge('init_shell','good_app')
G.edge['init_shell']['good_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][write read]'
G.edge['init_shell']['good_app']['fill'] = 'red'
G.add_edge('init_shell','healthd')
G.edge['init_shell']['healthd']['write-read'] = '[write read][add_name search][remove_name search][write read][write read][write read]'
G.edge['init_shell']['healthd']['fill'] = 'red'
G.add_edge('init_shell','init_shell')
G.edge['init_shell']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][write read][open open][open open][write read]'
G.edge['init_shell']['init_shell']['fill'] = 'red'
G.add_edge('init_shell','init_shell')
G.edge['init_shell']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][write read][open open][open open][write read][write read]'
G.edge['init_shell']['init_shell']['fill'] = 'red'
G.add_edge('init_shell','isolated_app')
G.edge['init_shell']['isolated_app']['write-read'] = '[write read]'
G.edge['init_shell']['isolated_app']['fill'] = 'red'
G.add_edge('init_shell','jackservice')
G.edge['init_shell']['jackservice']['write-read'] = '[add_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][write read]'
G.edge['init_shell']['jackservice']['fill'] = 'red'
G.add_edge('init_shell','keystore')
G.edge['init_shell']['keystore']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read]'
G.edge['init_shell']['keystore']['fill'] = 'red'
G.add_edge('init_shell','mediaserver')
G.edge['init_shell']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read]'
G.edge['init_shell']['mediaserver']['fill'] = 'red'
G.add_edge('init_shell','nfc')
G.edge['init_shell']['nfc']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['init_shell']['nfc']['fill'] = 'red'
G.add_edge('init_shell','oneseg_mw')
G.edge['init_shell']['oneseg_mw']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['init_shell']['oneseg_mw']['fill'] = 'red'
G.add_edge('init_shell','radio')
G.edge['init_shell']['radio']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['init_shell']['radio']['fill'] = 'red'
G.add_edge('init_shell','sensorhubservice')
G.edge['init_shell']['sensorhubservice']['write-read'] = '[write read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['init_shell']['sensorhubservice']['fill'] = 'red'
G.add_edge('init_shell','surfaceflinger')
G.edge['init_shell']['surfaceflinger']['write-read'] = '[open open][write read][append read][write read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['init_shell']['surfaceflinger']['fill'] = 'red'
G.add_edge('init_shell','system_server')
G.edge['init_shell']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][write read][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read]'
G.edge['init_shell']['system_server']['fill'] = 'red'
G.add_edge('init_shell','zygote')
G.edge['init_shell']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][write read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][write read][add_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['init_shell']['zygote']['fill'] = 'red'
G.add_edge('init_shell','adbd')
G.edge['init_shell']['adbd']['write-read'] = '[write read][add_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][write read]'
G.edge['init_shell']['adbd']['fill'] = 'red'
G.add_edge('init_shell','androidshmservice')
G.edge['init_shell']['androidshmservice']['write-read'] = '[write read][write read]'
G.edge['init_shell']['androidshmservice']['fill'] = 'red'
G.add_edge('init_shell','apaservice')
G.edge['init_shell']['apaservice']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][write read][write read]'
G.edge['init_shell']['apaservice']['fill'] = 'red'
G.add_edge('init_shell','appdomain')
G.edge['init_shell']['appdomain']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][write read]'
G.edge['init_shell']['appdomain']['fill'] = 'red'
G.add_edge('init_shell','bintvoutservice')
G.edge['init_shell']['bintvoutservice']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][write read]'
G.edge['init_shell']['bintvoutservice']['fill'] = 'red'
G.add_edge('init_shell','bluetooth')
G.edge['init_shell']['bluetooth']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][add_name search][remove_name search][open open][write read][open open][setattr getattr][write read][add_name search][remove_name search][write read][write read]'
G.edge['init_shell']['bluetooth']['fill'] = 'red'
G.add_edge('init_shell','bugreport')
G.edge['init_shell']['bugreport']['write-read'] = '[write read][write read]'
G.edge['init_shell']['bugreport']['fill'] = 'red'
G.add_edge('init_shell','charon')
G.edge['init_shell']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read][write read]'
G.edge['init_shell']['charon']['fill'] = 'red'
G.add_edge('init_shell','drmserver')
G.edge['init_shell']['drmserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][write read]'
G.edge['init_shell']['drmserver']['fill'] = 'red'
G.add_edge('init_shell','dumpstate')
G.edge['init_shell']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][write read][write read]'
G.edge['init_shell']['dumpstate']['fill'] = 'red'
G.add_edge('init_shell','dumpsys')
G.edge['init_shell']['dumpsys']['write-read'] = '[open open][write read][append read][write read][write read]'
G.edge['init_shell']['dumpsys']['fill'] = 'red'
G.add_edge('init_shell','fixmo_app')
G.edge['init_shell']['fixmo_app']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][write read]'
G.edge['init_shell']['fixmo_app']['fill'] = 'red'
G.add_edge('init_shell','good_app')
G.edge['init_shell']['good_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][write read][write read]'
G.edge['init_shell']['good_app']['fill'] = 'red'
G.add_edge('init_shell','healthd')
G.edge['init_shell']['healthd']['write-read'] = '[write read][add_name search][remove_name search][write read][write read][write read][write read]'
G.edge['init_shell']['healthd']['fill'] = 'red'
G.add_edge('init_shell','init_shell')
G.edge['init_shell']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][write read][open open][open open][write read][write read][write read]'
G.edge['init_shell']['init_shell']['fill'] = 'red'
G.add_edge('init_shell','init_shell')
G.edge['init_shell']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][write read][open open][open open][write read][write read][write read][write read]'
G.edge['init_shell']['init_shell']['fill'] = 'red'
G.add_edge('init_shell','isolated_app')
G.edge['init_shell']['isolated_app']['write-read'] = '[write read][write read]'
G.edge['init_shell']['isolated_app']['fill'] = 'red'
G.add_edge('init_shell','jackservice')
G.edge['init_shell']['jackservice']['write-read'] = '[add_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][write read][write read]'
G.edge['init_shell']['jackservice']['fill'] = 'red'
G.add_edge('init_shell','keystore')
G.edge['init_shell']['keystore']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][write read]'
G.edge['init_shell']['keystore']['fill'] = 'red'
G.add_edge('init_shell','mediaserver')
G.edge['init_shell']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][write read]'
G.edge['init_shell']['mediaserver']['fill'] = 'red'
G.add_edge('init_shell','nfc')
G.edge['init_shell']['nfc']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][write read][write read]'
G.edge['init_shell']['nfc']['fill'] = 'red'
G.add_edge('init_shell','oneseg_mw')
G.edge['init_shell']['oneseg_mw']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][write read]'
G.edge['init_shell']['oneseg_mw']['fill'] = 'red'
G.add_edge('init_shell','radio')
G.edge['init_shell']['radio']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][write read]'
G.edge['init_shell']['radio']['fill'] = 'red'
G.add_edge('init_shell','sensorhubservice')
G.edge['init_shell']['sensorhubservice']['write-read'] = '[write read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][write read]'
G.edge['init_shell']['sensorhubservice']['fill'] = 'red'
G.add_edge('init_shell','surfaceflinger')
G.edge['init_shell']['surfaceflinger']['write-read'] = '[open open][write read][append read][write read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][write read]'
G.edge['init_shell']['surfaceflinger']['fill'] = 'red'
G.add_edge('init_shell','system_server')
G.edge['init_shell']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][write read][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][write read]'
G.edge['init_shell']['system_server']['fill'] = 'red'
G.add_edge('init_shell','zygote')
G.edge['init_shell']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][write read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][write read][add_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][write read]'
G.edge['init_shell']['zygote']['fill'] = 'red'
G.add_edge('isolated_app','adbd')
G.edge['isolated_app']['adbd']['write-read'] = '[write read]'
G.edge['isolated_app']['adbd']['fill'] = 'red'
G.add_edge('isolated_app','androidshmservice')
G.edge['isolated_app']['androidshmservice']['write-read'] = '[write read]'
G.edge['isolated_app']['androidshmservice']['fill'] = 'red'
G.add_edge('isolated_app','apaservice')
G.edge['isolated_app']['apaservice']['write-read'] = '[write read]'
G.edge['isolated_app']['apaservice']['fill'] = 'red'
G.add_edge('isolated_app','appdomain')
G.edge['isolated_app']['appdomain']['write-read'] = '[write read]'
G.edge['isolated_app']['appdomain']['fill'] = 'red'
G.add_edge('isolated_app','bintvoutservice')
G.edge['isolated_app']['bintvoutservice']['write-read'] = '[open open][write read]'
G.edge['isolated_app']['bintvoutservice']['fill'] = 'red'
G.add_edge('isolated_app','bluetooth')
G.edge['isolated_app']['bluetooth']['write-read'] = '[write read]'
G.edge['isolated_app']['bluetooth']['fill'] = 'red'
G.add_edge('isolated_app','bugreport')
G.edge['isolated_app']['bugreport']['write-read'] = '[write read]'
G.edge['isolated_app']['bugreport']['fill'] = 'red'
G.add_edge('isolated_app','charon')
G.edge['isolated_app']['charon']['write-read'] = '[write read]'
G.edge['isolated_app']['charon']['fill'] = 'red'
G.add_edge('isolated_app','drmserver')
G.edge['isolated_app']['drmserver']['write-read'] = '[write read]'
G.edge['isolated_app']['drmserver']['fill'] = 'red'
G.add_edge('isolated_app','dumpstate')
G.edge['isolated_app']['dumpstate']['write-read'] = '[write read][write read]'
G.edge['isolated_app']['dumpstate']['fill'] = 'red'
G.add_edge('isolated_app','dumpsys')
G.edge['isolated_app']['dumpsys']['write-read'] = '[write read]'
G.edge['isolated_app']['dumpsys']['fill'] = 'red'
G.add_edge('isolated_app','fixmo_app')
G.edge['isolated_app']['fixmo_app']['write-read'] = '[open open][write read]'
G.edge['isolated_app']['fixmo_app']['fill'] = 'red'
G.add_edge('isolated_app','good_app')
G.edge['isolated_app']['good_app']['write-read'] = '[open open][write read]'
G.edge['isolated_app']['good_app']['fill'] = 'red'
G.add_edge('isolated_app','healthd')
G.edge['isolated_app']['healthd']['write-read'] = '[open open][write read]'
G.edge['isolated_app']['healthd']['fill'] = 'red'
G.add_edge('isolated_app','init_shell')
G.edge['isolated_app']['init_shell']['write-read'] = '[write read]'
G.edge['isolated_app']['init_shell']['fill'] = 'red'
G.add_edge('isolated_app','init_shell')
G.edge['isolated_app']['init_shell']['write-read'] = '[write read][write read]'
G.edge['isolated_app']['init_shell']['fill'] = 'red'
G.add_edge('isolated_app','isolated_app')
G.edge['isolated_app']['isolated_app']['write-read'] = '[open open][setattr getattr][write read][write read][write read][write read]'
G.edge['isolated_app']['isolated_app']['fill'] = 'red'
G.add_edge('isolated_app','jackservice')
G.edge['isolated_app']['jackservice']['write-read'] = '[write read]'
G.edge['isolated_app']['jackservice']['fill'] = 'red'
G.add_edge('isolated_app','keystore')
G.edge['isolated_app']['keystore']['write-read'] = '[write read]'
G.edge['isolated_app']['keystore']['fill'] = 'red'
G.add_edge('isolated_app','mediaserver')
G.edge['isolated_app']['mediaserver']['write-read'] = '[write read][append read][write read]'
G.edge['isolated_app']['mediaserver']['fill'] = 'red'
G.add_edge('isolated_app','nfc')
G.edge['isolated_app']['nfc']['write-read'] = '[write read]'
G.edge['isolated_app']['nfc']['fill'] = 'red'
G.add_edge('isolated_app','oneseg_mw')
G.edge['isolated_app']['oneseg_mw']['write-read'] = '[write read]'
G.edge['isolated_app']['oneseg_mw']['fill'] = 'red'
G.add_edge('isolated_app','radio')
G.edge['isolated_app']['radio']['write-read'] = '[open open][write read]'
G.edge['isolated_app']['radio']['fill'] = 'red'
G.add_edge('isolated_app','sensorhubservice')
G.edge['isolated_app']['sensorhubservice']['write-read'] = '[write read]'
G.edge['isolated_app']['sensorhubservice']['fill'] = 'red'
G.add_edge('isolated_app','surfaceflinger')
G.edge['isolated_app']['surfaceflinger']['write-read'] = '[open open][write read][write read]'
G.edge['isolated_app']['surfaceflinger']['fill'] = 'red'
G.add_edge('isolated_app','system_server')
G.edge['isolated_app']['system_server']['write-read'] = '[write read]'
G.edge['isolated_app']['system_server']['fill'] = 'red'
G.add_edge('isolated_app','zygote')
G.edge['isolated_app']['zygote']['write-read'] = '[open open][write read]'
G.edge['isolated_app']['zygote']['fill'] = 'red'
G.add_edge('isolated_app','fixmo_app')
G.edge['isolated_app']['fixmo_app']['write-read'] = '[open open][write read][setopt getopt]'
G.add_edge('isolated_app','good_app')
G.edge['isolated_app']['good_app']['write-read'] = '[open open][write read][setopt getopt]'
G.add_edge('isolated_app','ime_app')
G.edge['isolated_app']['ime_app']['write-read'] = '[open open][setopt getopt]'
G.add_edge('isolated_app','nfc')
G.edge['isolated_app']['nfc']['write-read'] = '[write read][setopt getopt]'
G.add_edge('isolated_app','platformappdomain')
G.edge['isolated_app']['platformappdomain']['write-read'] = '[setopt getopt]'
G.add_edge('isolated_app','radio')
G.edge['isolated_app']['radio']['write-read'] = '[open open][write read][setopt getopt]'
G.add_edge('isolated_app','samsung_app')
G.edge['isolated_app']['samsung_app']['write-read'] = '[setopt getopt]'
G.add_edge('isolated_app','s_system_app')
G.edge['isolated_app']['s_system_app']['write-read'] = '[open open][setopt getopt]'
G.add_edge('isolated_app','system_app')
G.edge['isolated_app']['system_app']['write-read'] = '[open open][setopt getopt]'
G.add_edge('isolated_app','system_server')
G.edge['isolated_app']['system_server']['write-read'] = '[write read][setopt getopt]'
G.add_edge('isolated_app','untrusteddomain')
G.edge['isolated_app']['untrusteddomain']['write-read'] = '[setopt getopt]'
G.add_edge('jackservice','adbd')
G.edge['jackservice']['adbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][write read]'
G.edge['jackservice']['adbd']['fill'] = 'red'
G.add_edge('jackservice','androidshmservice')
G.edge['jackservice']['androidshmservice']['write-read'] = '[write read]'
G.edge['jackservice']['androidshmservice']['fill'] = 'red'
G.add_edge('jackservice','apaservice')
G.edge['jackservice']['apaservice']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['jackservice']['apaservice']['fill'] = 'red'
G.add_edge('jackservice','appdomain')
G.edge['jackservice']['appdomain']['write-read'] = '[open open][setattr getattr][write read][append read][write read][write read]'
G.edge['jackservice']['appdomain']['fill'] = 'red'
G.add_edge('jackservice','bintvoutservice')
G.edge['jackservice']['bintvoutservice']['write-read'] = '[open open][write read][append read][write read][write read]'
G.edge['jackservice']['bintvoutservice']['fill'] = 'red'
G.add_edge('jackservice','bluetooth')
G.edge['jackservice']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read]'
G.edge['jackservice']['bluetooth']['fill'] = 'red'
G.add_edge('jackservice','bugreport')
G.edge['jackservice']['bugreport']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read]'
G.edge['jackservice']['bugreport']['fill'] = 'red'
G.add_edge('jackservice','charon')
G.edge['jackservice']['charon']['write-read'] = '[write read]'
G.edge['jackservice']['charon']['fill'] = 'red'
G.add_edge('jackservice','drmserver')
G.edge['jackservice']['drmserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][write read][write read]'
G.edge['jackservice']['drmserver']['fill'] = 'red'
G.add_edge('jackservice','dumpstate')
G.edge['jackservice']['dumpstate']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read]'
G.edge['jackservice']['dumpstate']['fill'] = 'red'
G.add_edge('jackservice','dumpsys')
G.edge['jackservice']['dumpsys']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read]'
G.edge['jackservice']['dumpsys']['fill'] = 'red'
G.add_edge('jackservice','fixmo_app')
G.edge['jackservice']['fixmo_app']['write-read'] = '[open open][setattr getattr][write read][append read][write read]'
G.edge['jackservice']['fixmo_app']['fill'] = 'red'
G.add_edge('jackservice','good_app')
G.edge['jackservice']['good_app']['write-read'] = '[open open][setattr getattr][write read][append read][write read]'
G.edge['jackservice']['good_app']['fill'] = 'red'
G.add_edge('jackservice','healthd')
G.edge['jackservice']['healthd']['write-read'] = '[open open][write read][append read][write read]'
G.edge['jackservice']['healthd']['fill'] = 'red'
G.add_edge('jackservice','init_shell')
G.edge['jackservice']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['jackservice']['init_shell']['fill'] = 'red'
G.add_edge('jackservice','init_shell')
G.edge['jackservice']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][write read]'
G.edge['jackservice']['init_shell']['fill'] = 'red'
G.add_edge('jackservice','isolated_app')
G.edge['jackservice']['isolated_app']['write-read'] = '[write read]'
G.edge['jackservice']['isolated_app']['fill'] = 'red'
G.add_edge('jackservice','jackservice')
G.edge['jackservice']['jackservice']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['jackservice']['jackservice']['fill'] = 'red'
G.add_edge('jackservice','keystore')
G.edge['jackservice']['keystore']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][write read]'
G.edge['jackservice']['keystore']['fill'] = 'red'
G.add_edge('jackservice','mediaserver')
G.edge['jackservice']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][write read]'
G.edge['jackservice']['mediaserver']['fill'] = 'red'
G.add_edge('jackservice','nfc')
G.edge['jackservice']['nfc']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read]'
G.edge['jackservice']['nfc']['fill'] = 'red'
G.add_edge('jackservice','oneseg_mw')
G.edge['jackservice']['oneseg_mw']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][write read]'
G.edge['jackservice']['oneseg_mw']['fill'] = 'red'
G.add_edge('jackservice','radio')
G.edge['jackservice']['radio']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][write read]'
G.edge['jackservice']['radio']['fill'] = 'red'
G.add_edge('jackservice','sensorhubservice')
G.edge['jackservice']['sensorhubservice']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read]'
G.edge['jackservice']['sensorhubservice']['fill'] = 'red'
G.add_edge('jackservice','surfaceflinger')
G.edge['jackservice']['surfaceflinger']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read][write read]'
G.edge['jackservice']['surfaceflinger']['fill'] = 'red'
G.add_edge('jackservice','system_server')
G.edge['jackservice']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][write read][write read]'
G.edge['jackservice']['system_server']['fill'] = 'red'
G.add_edge('jackservice','zygote')
G.edge['jackservice']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read]'
G.edge['jackservice']['zygote']['fill'] = 'red'
G.add_edge('keystore','adbd')
G.edge['keystore']['adbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][write read]'
G.edge['keystore']['adbd']['fill'] = 'red'
G.add_edge('keystore','androidshmservice')
G.edge['keystore']['androidshmservice']['write-read'] = '[write read]'
G.edge['keystore']['androidshmservice']['fill'] = 'red'
G.add_edge('keystore','apaservice')
G.edge['keystore']['apaservice']['write-read'] = '[open open][write read][append read][write read]'
G.edge['keystore']['apaservice']['fill'] = 'red'
G.add_edge('keystore','appdomain')
G.edge['keystore']['appdomain']['write-read'] = '[open open][write read][append read][write read]'
G.edge['keystore']['appdomain']['fill'] = 'red'
G.add_edge('keystore','bintvoutservice')
G.edge['keystore']['bintvoutservice']['write-read'] = '[open open][write read][append read][write read][write read]'
G.edge['keystore']['bintvoutservice']['fill'] = 'red'
G.add_edge('keystore','bluetooth')
G.edge['keystore']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][write read]'
G.edge['keystore']['bluetooth']['fill'] = 'red'
G.add_edge('keystore','bugreport')
G.edge['keystore']['bugreport']['write-read'] = '[write read][open open][setattr getattr][write read][append read][write read]'
G.edge['keystore']['bugreport']['fill'] = 'red'
G.add_edge('keystore','charon')
G.edge['keystore']['charon']['write-read'] = '[open open][write read][append read][write read]'
G.edge['keystore']['charon']['fill'] = 'red'
G.add_edge('keystore','drmserver')
G.edge['keystore']['drmserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][write read][append read][write read]'
G.edge['keystore']['drmserver']['fill'] = 'red'
G.add_edge('keystore','dumpstate')
G.edge['keystore']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][write read]'
G.edge['keystore']['dumpstate']['fill'] = 'red'
G.add_edge('keystore','dumpsys')
G.edge['keystore']['dumpsys']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][write read]'
G.edge['keystore']['dumpsys']['fill'] = 'red'
G.add_edge('keystore','fixmo_app')
G.edge['keystore']['fixmo_app']['write-read'] = '[write read]'
G.edge['keystore']['fixmo_app']['fill'] = 'red'
G.add_edge('keystore','good_app')
G.edge['keystore']['good_app']['write-read'] = '[open open][setattr getattr][write read][append read][write read]'
G.edge['keystore']['good_app']['fill'] = 'red'
G.add_edge('keystore','healthd')
G.edge['keystore']['healthd']['write-read'] = '[write read][open open][write read][append read][write read]'
G.edge['keystore']['healthd']['fill'] = 'red'
G.add_edge('keystore','init_shell')
G.edge['keystore']['init_shell']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read][open open][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][write read][append read][write read]'
G.edge['keystore']['init_shell']['fill'] = 'red'
G.add_edge('keystore','init_shell')
G.edge['keystore']['init_shell']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read][open open][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][write read][append read][write read][write read]'
G.edge['keystore']['init_shell']['fill'] = 'red'
G.add_edge('keystore','isolated_app')
G.edge['keystore']['isolated_app']['write-read'] = '[write read]'
G.edge['keystore']['isolated_app']['fill'] = 'red'
G.add_edge('keystore','jackservice')
G.edge['keystore']['jackservice']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][write read]'
G.edge['keystore']['jackservice']['fill'] = 'red'
G.add_edge('keystore','keystore')
G.edge['keystore']['keystore']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read]'
G.edge['keystore']['keystore']['fill'] = 'red'
G.add_edge('keystore','mediaserver')
G.edge['keystore']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read][open open][setattr getattr][write read][append read][write read][open open][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][write read][append read][write read]'
G.edge['keystore']['mediaserver']['fill'] = 'red'
G.add_edge('keystore','nfc')
G.edge['keystore']['nfc']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read][open open][write read][append read][write read]'
G.edge['keystore']['nfc']['fill'] = 'red'
G.add_edge('keystore','oneseg_mw')
G.edge['keystore']['oneseg_mw']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][write read]'
G.edge['keystore']['oneseg_mw']['fill'] = 'red'
G.add_edge('keystore','radio')
G.edge['keystore']['radio']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][write read]'
G.edge['keystore']['radio']['fill'] = 'red'
G.add_edge('keystore','sensorhubservice')
G.edge['keystore']['sensorhubservice']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read]'
G.edge['keystore']['sensorhubservice']['fill'] = 'red'
G.add_edge('keystore','surfaceflinger')
G.edge['keystore']['surfaceflinger']['write-read'] = '[open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][write read][write read]'
G.edge['keystore']['surfaceflinger']['fill'] = 'red'
G.add_edge('keystore','system_server')
G.edge['keystore']['system_server']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][write read]'
G.edge['keystore']['system_server']['fill'] = 'red'
G.add_edge('keystore','zygote')
G.edge['keystore']['zygote']['write-read'] = '[open open][write read][append read][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][open open][write read][append read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read]'
G.edge['keystore']['zygote']['fill'] = 'red'
G.add_edge('mediaserver','adbd')
G.edge['mediaserver']['adbd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['mediaserver']['adbd']['fill'] = 'red'
G.add_edge('mediaserver','androidshmservice')
G.edge['mediaserver']['androidshmservice']['write-read'] = '[write read]'
G.edge['mediaserver']['androidshmservice']['fill'] = 'red'
G.add_edge('mediaserver','apaservice')
G.edge['mediaserver']['apaservice']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][write read]'
G.edge['mediaserver']['apaservice']['fill'] = 'red'
G.add_edge('mediaserver','appdomain')
G.edge['mediaserver']['appdomain']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read]'
G.edge['mediaserver']['appdomain']['fill'] = 'red'
G.add_edge('mediaserver','bintvoutservice')
G.edge['mediaserver']['bintvoutservice']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][write read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['mediaserver']['bintvoutservice']['fill'] = 'red'
G.add_edge('mediaserver','bluetooth')
G.edge['mediaserver']['bluetooth']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][write read][write read]'
G.edge['mediaserver']['bluetooth']['fill'] = 'red'
G.add_edge('mediaserver','bugreport')
G.edge['mediaserver']['bugreport']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read]'
G.edge['mediaserver']['bugreport']['fill'] = 'red'
G.add_edge('mediaserver','charon')
G.edge['mediaserver']['charon']['write-read'] = '[write read]'
G.edge['mediaserver']['charon']['fill'] = 'red'
G.add_edge('mediaserver','drmserver')
G.edge['mediaserver']['drmserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['mediaserver']['drmserver']['fill'] = 'red'
G.add_edge('mediaserver','dumpstate')
G.edge['mediaserver']['dumpstate']['write-read'] = '[open open][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['mediaserver']['dumpstate']['fill'] = 'red'
G.add_edge('mediaserver','dumpsys')
G.edge['mediaserver']['dumpsys']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][write read]'
G.edge['mediaserver']['dumpsys']['fill'] = 'red'
G.add_edge('mediaserver','fixmo_app')
G.edge['mediaserver']['fixmo_app']['write-read'] = '[write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][write read]'
G.edge['mediaserver']['fixmo_app']['fill'] = 'red'
G.add_edge('mediaserver','good_app')
G.edge['mediaserver']['good_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][write read]'
G.edge['mediaserver']['good_app']['fill'] = 'red'
G.add_edge('mediaserver','healthd')
G.edge['mediaserver']['healthd']['write-read'] = '[open open][write read][append read][write read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read]'
G.edge['mediaserver']['healthd']['fill'] = 'red'
G.add_edge('mediaserver','init_shell')
G.edge['mediaserver']['init_shell']['write-read'] = '[open open][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read]'
G.edge['mediaserver']['init_shell']['fill'] = 'red'
G.add_edge('mediaserver','init_shell')
G.edge['mediaserver']['init_shell']['write-read'] = '[open open][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read][write read]'
G.edge['mediaserver']['init_shell']['fill'] = 'red'
G.add_edge('mediaserver','isolated_app')
G.edge['mediaserver']['isolated_app']['write-read'] = '[write read][write read][write read]'
G.edge['mediaserver']['isolated_app']['fill'] = 'red'
G.add_edge('mediaserver','jackservice')
G.edge['mediaserver']['jackservice']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read][append read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][write read]'
G.edge['mediaserver']['jackservice']['fill'] = 'red'
G.add_edge('mediaserver','keystore')
G.edge['mediaserver']['keystore']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read]'
G.edge['mediaserver']['keystore']['fill'] = 'red'
G.add_edge('mediaserver','mediaserver')
G.edge['mediaserver']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][write read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][write read][append read][setattr getattr][write read][write read][open open][setattr getattr][write read][append read][write read]'
G.edge['mediaserver']['mediaserver']['fill'] = 'red'
G.add_edge('mediaserver','nfc')
G.edge['mediaserver']['nfc']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['mediaserver']['nfc']['fill'] = 'red'
G.add_edge('mediaserver','oneseg_mw')
G.edge['mediaserver']['oneseg_mw']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read]'
G.edge['mediaserver']['oneseg_mw']['fill'] = 'red'
G.add_edge('mediaserver','radio')
G.edge['mediaserver']['radio']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][write read][write read]'
G.edge['mediaserver']['radio']['fill'] = 'red'
G.add_edge('mediaserver','sensorhubservice')
G.edge['mediaserver']['sensorhubservice']['write-read'] = '[write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['mediaserver']['sensorhubservice']['fill'] = 'red'
G.add_edge('mediaserver','surfaceflinger')
G.edge['mediaserver']['surfaceflinger']['write-read'] = '[open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][write read][open open][setattr getattr][write read][append read][write read][open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read]'
G.edge['mediaserver']['surfaceflinger']['fill'] = 'red'
G.add_edge('mediaserver','system_server')
G.edge['mediaserver']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][write read][append read][write read][open open][setattr getattr][write read][append read][write read][write read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][open open][write read][append read][write read][append read][write read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][setattr getattr][write read][write read][write read]'
G.edge['mediaserver']['system_server']['fill'] = 'red'
G.add_edge('mediaserver','zygote')
G.edge['mediaserver']['zygote']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][write read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['mediaserver']['zygote']['fill'] = 'red'
G.add_edge('nfc','adbd')
G.edge['nfc']['adbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['nfc']['adbd']['fill'] = 'red'
G.add_edge('nfc','androidshmservice')
G.edge['nfc']['androidshmservice']['write-read'] = '[write read]'
G.edge['nfc']['androidshmservice']['fill'] = 'red'
G.add_edge('nfc','apaservice')
G.edge['nfc']['apaservice']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read]'
G.edge['nfc']['apaservice']['fill'] = 'red'
G.add_edge('nfc','appdomain')
G.edge['nfc']['appdomain']['write-read'] = '[write read]'
G.edge['nfc']['appdomain']['fill'] = 'red'
G.add_edge('nfc','bintvoutservice')
G.edge['nfc']['bintvoutservice']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['nfc']['bintvoutservice']['fill'] = 'red'
G.add_edge('nfc','bluetooth')
G.edge['nfc']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['nfc']['bluetooth']['fill'] = 'red'
G.add_edge('nfc','bugreport')
G.edge['nfc']['bugreport']['write-read'] = '[setattr getattr][write read]'
G.edge['nfc']['bugreport']['fill'] = 'red'
G.add_edge('nfc','charon')
G.edge['nfc']['charon']['write-read'] = '[write read]'
G.edge['nfc']['charon']['fill'] = 'red'
G.add_edge('nfc','drmserver')
G.edge['nfc']['drmserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['nfc']['drmserver']['fill'] = 'red'
G.add_edge('nfc','dumpstate')
G.edge['nfc']['dumpstate']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['nfc']['dumpstate']['fill'] = 'red'
G.add_edge('nfc','dumpsys')
G.edge['nfc']['dumpsys']['write-read'] = '[setattr getattr][write read]'
G.edge['nfc']['dumpsys']['fill'] = 'red'
G.add_edge('nfc','fixmo_app')
G.edge['nfc']['fixmo_app']['write-read'] = '[write read]'
G.edge['nfc']['fixmo_app']['fill'] = 'red'
G.add_edge('nfc','good_app')
G.edge['nfc']['good_app']['write-read'] = '[write read]'
G.edge['nfc']['good_app']['fill'] = 'red'
G.add_edge('nfc','healthd')
G.edge['nfc']['healthd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][write read]'
G.edge['nfc']['healthd']['fill'] = 'red'
G.add_edge('nfc','init_shell')
G.edge['nfc']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['nfc']['init_shell']['fill'] = 'red'
G.add_edge('nfc','init_shell')
G.edge['nfc']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][write read]'
G.edge['nfc']['init_shell']['fill'] = 'red'
G.add_edge('nfc','isolated_app')
G.edge['nfc']['isolated_app']['write-read'] = '[write read]'
G.edge['nfc']['isolated_app']['fill'] = 'red'
G.add_edge('nfc','jackservice')
G.edge['nfc']['jackservice']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][setattr getattr][write read]'
G.edge['nfc']['jackservice']['fill'] = 'red'
G.add_edge('nfc','keystore')
G.edge['nfc']['keystore']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read]'
G.edge['nfc']['keystore']['fill'] = 'red'
G.add_edge('nfc','mediaserver')
G.edge['nfc']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['nfc']['mediaserver']['fill'] = 'red'
G.add_edge('nfc','nfc')
G.edge['nfc']['nfc']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['nfc']['nfc']['fill'] = 'red'
G.add_edge('nfc','oneseg_mw')
G.edge['nfc']['oneseg_mw']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['nfc']['oneseg_mw']['fill'] = 'red'
G.add_edge('nfc','radio')
G.edge['nfc']['radio']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['nfc']['radio']['fill'] = 'red'
G.add_edge('nfc','sensorhubservice')
G.edge['nfc']['sensorhubservice']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['nfc']['sensorhubservice']['fill'] = 'red'
G.add_edge('nfc','surfaceflinger')
G.edge['nfc']['surfaceflinger']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['nfc']['surfaceflinger']['fill'] = 'red'
G.add_edge('nfc','system_server')
G.edge['nfc']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['nfc']['system_server']['fill'] = 'red'
G.add_edge('nfc','zygote')
G.edge['nfc']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['nfc']['zygote']['fill'] = 'red'
G.add_edge('oneseg_mw','adbd')
G.edge['oneseg_mw']['adbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['oneseg_mw']['adbd']['fill'] = 'red'
G.add_edge('oneseg_mw','androidshmservice')
G.edge['oneseg_mw']['androidshmservice']['write-read'] = '[write read]'
G.edge['oneseg_mw']['androidshmservice']['fill'] = 'red'
G.add_edge('oneseg_mw','apaservice')
G.edge['oneseg_mw']['apaservice']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read]'
G.edge['oneseg_mw']['apaservice']['fill'] = 'red'
G.add_edge('oneseg_mw','appdomain')
G.edge['oneseg_mw']['appdomain']['write-read'] = '[open open][write read][append read][write read]'
G.edge['oneseg_mw']['appdomain']['fill'] = 'red'
G.add_edge('oneseg_mw','bintvoutservice')
G.edge['oneseg_mw']['bintvoutservice']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['oneseg_mw']['bintvoutservice']['fill'] = 'red'
G.add_edge('oneseg_mw','bluetooth')
G.edge['oneseg_mw']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['oneseg_mw']['bluetooth']['fill'] = 'red'
G.add_edge('oneseg_mw','bugreport')
G.edge['oneseg_mw']['bugreport']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read]'
G.edge['oneseg_mw']['bugreport']['fill'] = 'red'
G.add_edge('oneseg_mw','charon')
G.edge['oneseg_mw']['charon']['write-read'] = '[write read]'
G.edge['oneseg_mw']['charon']['fill'] = 'red'
G.add_edge('oneseg_mw','drmserver')
G.edge['oneseg_mw']['drmserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][setattr getattr][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['oneseg_mw']['drmserver']['fill'] = 'red'
G.add_edge('oneseg_mw','dumpstate')
G.edge['oneseg_mw']['dumpstate']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['oneseg_mw']['dumpstate']['fill'] = 'red'
G.add_edge('oneseg_mw','dumpsys')
G.edge['oneseg_mw']['dumpsys']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read]'
G.edge['oneseg_mw']['dumpsys']['fill'] = 'red'
G.add_edge('oneseg_mw','fixmo_app')
G.edge['oneseg_mw']['fixmo_app']['write-read'] = '[write read][append read][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][append read][open open][write read][append read][write read]'
G.edge['oneseg_mw']['fixmo_app']['fill'] = 'red'
G.add_edge('oneseg_mw','good_app')
G.edge['oneseg_mw']['good_app']['write-read'] = '[write read][append read][write read][append read][open open][write read][append read][open open][write read][append read][write read]'
G.edge['oneseg_mw']['good_app']['fill'] = 'red'
G.add_edge('oneseg_mw','healthd')
G.edge['oneseg_mw']['healthd']['write-read'] = '[write read]'
G.edge['oneseg_mw']['healthd']['fill'] = 'red'
G.add_edge('oneseg_mw','init_shell')
G.edge['oneseg_mw']['init_shell']['write-read'] = '[add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['oneseg_mw']['init_shell']['fill'] = 'red'
G.add_edge('oneseg_mw','init_shell')
G.edge['oneseg_mw']['init_shell']['write-read'] = '[add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][write read]'
G.edge['oneseg_mw']['init_shell']['fill'] = 'red'
G.add_edge('oneseg_mw','isolated_app')
G.edge['oneseg_mw']['isolated_app']['write-read'] = '[write read]'
G.edge['oneseg_mw']['isolated_app']['fill'] = 'red'
G.add_edge('oneseg_mw','jackservice')
G.edge['oneseg_mw']['jackservice']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read]'
G.edge['oneseg_mw']['jackservice']['fill'] = 'red'
G.add_edge('oneseg_mw','keystore')
G.edge['oneseg_mw']['keystore']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][write read]'
G.edge['oneseg_mw']['keystore']['fill'] = 'red'
G.add_edge('oneseg_mw','mediaserver')
G.edge['oneseg_mw']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][append read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read]'
G.edge['oneseg_mw']['mediaserver']['fill'] = 'red'
G.add_edge('oneseg_mw','nfc')
G.edge['oneseg_mw']['nfc']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['oneseg_mw']['nfc']['fill'] = 'red'
G.add_edge('oneseg_mw','oneseg_mw')
G.edge['oneseg_mw']['oneseg_mw']['write-read'] = '[open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read]'
G.edge['oneseg_mw']['oneseg_mw']['fill'] = 'red'
G.add_edge('oneseg_mw','radio')
G.edge['oneseg_mw']['radio']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['oneseg_mw']['radio']['fill'] = 'red'
G.add_edge('oneseg_mw','sensorhubservice')
G.edge['oneseg_mw']['sensorhubservice']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['oneseg_mw']['sensorhubservice']['fill'] = 'red'
G.add_edge('oneseg_mw','surfaceflinger')
G.edge['oneseg_mw']['surfaceflinger']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read]'
G.edge['oneseg_mw']['surfaceflinger']['fill'] = 'red'
G.add_edge('oneseg_mw','system_server')
G.edge['oneseg_mw']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read]'
G.edge['oneseg_mw']['system_server']['fill'] = 'red'
G.add_edge('oneseg_mw','zygote')
G.edge['oneseg_mw']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['oneseg_mw']['zygote']['fill'] = 'red'
G.add_edge('radio','adbd')
G.edge['radio']['adbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['radio']['adbd']['fill'] = 'red'
G.add_edge('radio','androidshmservice')
G.edge['radio']['androidshmservice']['write-read'] = '[write read]'
G.edge['radio']['androidshmservice']['fill'] = 'red'
G.add_edge('radio','apaservice')
G.edge['radio']['apaservice']['write-read'] = '[open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][write read]'
G.edge['radio']['apaservice']['fill'] = 'red'
G.add_edge('radio','appdomain')
G.edge['radio']['appdomain']['write-read'] = '[open open][write read][append read][write read][write read][append read][open open][setattr getattr][open open][write read][append read][open open][write read][append read][write read]'
G.edge['radio']['appdomain']['fill'] = 'red'
G.add_edge('radio','bintvoutservice')
G.edge['radio']['bintvoutservice']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['radio']['bintvoutservice']['fill'] = 'red'
G.add_edge('radio','bluetooth')
G.edge['radio']['bluetooth']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][write read][write read]'
G.edge['radio']['bluetooth']['fill'] = 'red'
G.add_edge('radio','bugreport')
G.edge['radio']['bugreport']['write-read'] = '[write read][append read][open open][setattr getattr][write read][append read][write read]'
G.edge['radio']['bugreport']['fill'] = 'red'
G.add_edge('radio','charon')
G.edge['radio']['charon']['write-read'] = '[write read]'
G.edge['radio']['charon']['fill'] = 'red'
G.add_edge('radio','drmserver')
G.edge['radio']['drmserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][open open][setattr getattr][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['radio']['drmserver']['fill'] = 'red'
G.add_edge('radio','dumpstate')
G.edge['radio']['dumpstate']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['radio']['dumpstate']['fill'] = 'red'
G.add_edge('radio','dumpsys')
G.edge['radio']['dumpsys']['write-read'] = '[write read][append read][open open][setattr getattr][write read][append read][write read]'
G.edge['radio']['dumpsys']['fill'] = 'red'
G.add_edge('radio','fixmo_app')
G.edge['radio']['fixmo_app']['write-read'] = '[open open][write read][append read][write read][open open][setattr getattr][open open][write read][append read][open open][write read][append read][write read]'
G.edge['radio']['fixmo_app']['fill'] = 'red'
G.add_edge('radio','good_app')
G.edge['radio']['good_app']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][write read]'
G.edge['radio']['good_app']['fill'] = 'red'
G.add_edge('radio','healthd')
G.edge['radio']['healthd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][write read][open open][write read][append read][write read]'
G.edge['radio']['healthd']['fill'] = 'red'
G.add_edge('radio','init_shell')
G.edge['radio']['init_shell']['write-read'] = '[add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][add_name search][remove_name search][setattr getattr][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['radio']['init_shell']['fill'] = 'red'
G.add_edge('radio','init_shell')
G.edge['radio']['init_shell']['write-read'] = '[add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][add_name search][remove_name search][setattr getattr][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][write read]'
G.edge['radio']['init_shell']['fill'] = 'red'
G.add_edge('radio','isolated_app')
G.edge['radio']['isolated_app']['write-read'] = '[open open][setattr getattr][append read][write read]'
G.edge['radio']['isolated_app']['fill'] = 'red'
G.add_edge('radio','jackservice')
G.edge['radio']['jackservice']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][write read][append read][write read]'
G.edge['radio']['jackservice']['fill'] = 'red'
G.add_edge('radio','keystore')
G.edge['radio']['keystore']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][write read]'
G.edge['radio']['keystore']['fill'] = 'red'
G.add_edge('radio','mediaserver')
G.edge['radio']['mediaserver']['write-read'] = '[add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][write read][write read]'
G.edge['radio']['mediaserver']['fill'] = 'red'
G.add_edge('radio','nfc')
G.edge['radio']['nfc']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['radio']['nfc']['fill'] = 'red'
G.add_edge('radio','oneseg_mw')
G.edge['radio']['oneseg_mw']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['radio']['oneseg_mw']['fill'] = 'red'
G.add_edge('radio','radio')
G.edge['radio']['radio']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][write read][open open][setattr getattr][write read][append read][write read]'
G.edge['radio']['radio']['fill'] = 'red'
G.add_edge('radio','sensorhubservice')
G.edge['radio']['sensorhubservice']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['radio']['sensorhubservice']['fill'] = 'red'
G.add_edge('radio','surfaceflinger')
G.edge['radio']['surfaceflinger']['write-read'] = '[open open][write read][append read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['radio']['surfaceflinger']['fill'] = 'red'
G.add_edge('radio','system_server')
G.edge['radio']['system_server']['write-read'] = '[add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][write read][write read]'
G.edge['radio']['system_server']['fill'] = 'red'
G.add_edge('radio','zygote')
G.edge['radio']['zygote']['write-read'] = '[open open][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['radio']['zygote']['fill'] = 'red'
G.add_edge('sensorhubservice','adbd')
G.edge['sensorhubservice']['adbd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['sensorhubservice']['adbd']['fill'] = 'red'
G.add_edge('sensorhubservice','androidshmservice')
G.edge['sensorhubservice']['androidshmservice']['write-read'] = '[write read]'
G.edge['sensorhubservice']['androidshmservice']['fill'] = 'red'
G.add_edge('sensorhubservice','apaservice')
G.edge['sensorhubservice']['apaservice']['write-read'] = '[write read]'
G.edge['sensorhubservice']['apaservice']['fill'] = 'red'
G.add_edge('sensorhubservice','appdomain')
G.edge['sensorhubservice']['appdomain']['write-read'] = '[open open][write read][append read][write read]'
G.edge['sensorhubservice']['appdomain']['fill'] = 'red'
G.add_edge('sensorhubservice','bintvoutservice')
G.edge['sensorhubservice']['bintvoutservice']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['sensorhubservice']['bintvoutservice']['fill'] = 'red'
G.add_edge('sensorhubservice','bluetooth')
G.edge['sensorhubservice']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['sensorhubservice']['bluetooth']['fill'] = 'red'
G.add_edge('sensorhubservice','bugreport')
G.edge['sensorhubservice']['bugreport']['write-read'] = '[write read]'
G.edge['sensorhubservice']['bugreport']['fill'] = 'red'
G.add_edge('sensorhubservice','charon')
G.edge['sensorhubservice']['charon']['write-read'] = '[write read]'
G.edge['sensorhubservice']['charon']['fill'] = 'red'
G.add_edge('sensorhubservice','drmserver')
G.edge['sensorhubservice']['drmserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['sensorhubservice']['drmserver']['fill'] = 'red'
G.add_edge('sensorhubservice','dumpstate')
G.edge['sensorhubservice']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['sensorhubservice']['dumpstate']['fill'] = 'red'
G.add_edge('sensorhubservice','dumpsys')
G.edge['sensorhubservice']['dumpsys']['write-read'] = '[write read]'
G.edge['sensorhubservice']['dumpsys']['fill'] = 'red'
G.add_edge('sensorhubservice','fixmo_app')
G.edge['sensorhubservice']['fixmo_app']['write-read'] = '[write read]'
G.edge['sensorhubservice']['fixmo_app']['fill'] = 'red'
G.add_edge('sensorhubservice','good_app')
G.edge['sensorhubservice']['good_app']['write-read'] = '[write read]'
G.edge['sensorhubservice']['good_app']['fill'] = 'red'
G.add_edge('sensorhubservice','healthd')
G.edge['sensorhubservice']['healthd']['write-read'] = '[open open][write read][append read][write read]'
G.edge['sensorhubservice']['healthd']['fill'] = 'red'
G.add_edge('sensorhubservice','init_shell')
G.edge['sensorhubservice']['init_shell']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['sensorhubservice']['init_shell']['fill'] = 'red'
G.add_edge('sensorhubservice','init_shell')
G.edge['sensorhubservice']['init_shell']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][write read]'
G.edge['sensorhubservice']['init_shell']['fill'] = 'red'
G.add_edge('sensorhubservice','isolated_app')
G.edge['sensorhubservice']['isolated_app']['write-read'] = '[write read]'
G.edge['sensorhubservice']['isolated_app']['fill'] = 'red'
G.add_edge('sensorhubservice','jackservice')
G.edge['sensorhubservice']['jackservice']['write-read'] = '[write read][write read]'
G.edge['sensorhubservice']['jackservice']['fill'] = 'red'
G.add_edge('sensorhubservice','keystore')
G.edge['sensorhubservice']['keystore']['write-read'] = '[write read]'
G.edge['sensorhubservice']['keystore']['fill'] = 'red'
G.add_edge('sensorhubservice','mediaserver')
G.edge['sensorhubservice']['mediaserver']['write-read'] = '[open open][open open][setattr getattr][write read][append read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['sensorhubservice']['mediaserver']['fill'] = 'red'
G.add_edge('sensorhubservice','nfc')
G.edge['sensorhubservice']['nfc']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['sensorhubservice']['nfc']['fill'] = 'red'
G.add_edge('sensorhubservice','oneseg_mw')
G.edge['sensorhubservice']['oneseg_mw']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['sensorhubservice']['oneseg_mw']['fill'] = 'red'
G.add_edge('sensorhubservice','radio')
G.edge['sensorhubservice']['radio']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['sensorhubservice']['radio']['fill'] = 'red'
G.add_edge('sensorhubservice','sensorhubservice')
G.edge['sensorhubservice']['sensorhubservice']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['sensorhubservice']['sensorhubservice']['fill'] = 'red'
G.add_edge('sensorhubservice','surfaceflinger')
G.edge['sensorhubservice']['surfaceflinger']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['sensorhubservice']['surfaceflinger']['fill'] = 'red'
G.add_edge('sensorhubservice','system_server')
G.edge['sensorhubservice']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['sensorhubservice']['system_server']['fill'] = 'red'
G.add_edge('sensorhubservice','zygote')
G.edge['sensorhubservice']['zygote']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['sensorhubservice']['zygote']['fill'] = 'red'
G.add_edge('surfaceflinger','adbd')
G.edge['surfaceflinger']['adbd']['write-read'] = '[open open][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['surfaceflinger']['adbd']['fill'] = 'red'
G.add_edge('surfaceflinger','androidshmservice')
G.edge['surfaceflinger']['androidshmservice']['write-read'] = '[write read]'
G.edge['surfaceflinger']['androidshmservice']['fill'] = 'red'
G.add_edge('surfaceflinger','apaservice')
G.edge['surfaceflinger']['apaservice']['write-read'] = '[open open][setattr getattr][write read][append read][write read][append read][write read]'
G.edge['surfaceflinger']['apaservice']['fill'] = 'red'
G.add_edge('surfaceflinger','appdomain')
G.edge['surfaceflinger']['appdomain']['write-read'] = '[open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][write read]'
G.edge['surfaceflinger']['appdomain']['fill'] = 'red'
G.add_edge('surfaceflinger','bintvoutservice')
G.edge['surfaceflinger']['bintvoutservice']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][add_name search][remove_name search][write read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['surfaceflinger']['bintvoutservice']['fill'] = 'red'
G.add_edge('surfaceflinger','bluetooth')
G.edge['surfaceflinger']['bluetooth']['write-read'] = '[write read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['surfaceflinger']['bluetooth']['fill'] = 'red'
G.add_edge('surfaceflinger','bugreport')
G.edge['surfaceflinger']['bugreport']['write-read'] = '[write read][append read][write read]'
G.edge['surfaceflinger']['bugreport']['fill'] = 'red'
G.add_edge('surfaceflinger','charon')
G.edge['surfaceflinger']['charon']['write-read'] = '[write read]'
G.edge['surfaceflinger']['charon']['fill'] = 'red'
G.add_edge('surfaceflinger','drmserver')
G.edge['surfaceflinger']['drmserver']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['surfaceflinger']['drmserver']['fill'] = 'red'
G.add_edge('surfaceflinger','dumpstate')
G.edge['surfaceflinger']['dumpstate']['write-read'] = '[open open][write read][append read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['surfaceflinger']['dumpstate']['fill'] = 'red'
G.add_edge('surfaceflinger','dumpsys')
G.edge['surfaceflinger']['dumpsys']['write-read'] = '[write read][append read][write read]'
G.edge['surfaceflinger']['dumpsys']['fill'] = 'red'
G.add_edge('surfaceflinger','fixmo_app')
G.edge['surfaceflinger']['fixmo_app']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read]'
G.edge['surfaceflinger']['fixmo_app']['fill'] = 'red'
G.add_edge('surfaceflinger','good_app')
G.edge['surfaceflinger']['good_app']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read]'
G.edge['surfaceflinger']['good_app']['fill'] = 'red'
G.add_edge('surfaceflinger','healthd')
G.edge['surfaceflinger']['healthd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][write read][open open][write read][append read][write read][append read][write read]'
G.edge['surfaceflinger']['healthd']['fill'] = 'red'
G.add_edge('surfaceflinger','init_shell')
G.edge['surfaceflinger']['init_shell']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['surfaceflinger']['init_shell']['fill'] = 'red'
G.add_edge('surfaceflinger','init_shell')
G.edge['surfaceflinger']['init_shell']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][write read]'
G.edge['surfaceflinger']['init_shell']['fill'] = 'red'
G.add_edge('surfaceflinger','isolated_app')
G.edge['surfaceflinger']['isolated_app']['write-read'] = '[open open][setattr getattr][append read][write read]'
G.edge['surfaceflinger']['isolated_app']['fill'] = 'red'
G.add_edge('surfaceflinger','jackservice')
G.edge['surfaceflinger']['jackservice']['write-read'] = '[write read][write read][write read][append read][write read]'
G.edge['surfaceflinger']['jackservice']['fill'] = 'red'
G.add_edge('surfaceflinger','keystore')
G.edge['surfaceflinger']['keystore']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read][append read][write read]'
G.edge['surfaceflinger']['keystore']['fill'] = 'red'
G.add_edge('surfaceflinger','mediaserver')
G.edge['surfaceflinger']['mediaserver']['write-read'] = '[open open][write read][append read][write read][append read][open open][write read][append read][open open][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][add_name search][remove_name search][write read][append read][write read][append read][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read]'
G.edge['surfaceflinger']['mediaserver']['fill'] = 'red'
G.add_edge('surfaceflinger','nfc')
G.edge['surfaceflinger']['nfc']['write-read'] = '[write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['surfaceflinger']['nfc']['fill'] = 'red'
G.add_edge('surfaceflinger','oneseg_mw')
G.edge['surfaceflinger']['oneseg_mw']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read]'
G.edge['surfaceflinger']['oneseg_mw']['fill'] = 'red'
G.add_edge('surfaceflinger','radio')
G.edge['surfaceflinger']['radio']['write-read'] = '[open open][write read][append read][write read][open open][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['surfaceflinger']['radio']['fill'] = 'red'
G.add_edge('surfaceflinger','sensorhubservice')
G.edge['surfaceflinger']['sensorhubservice']['write-read'] = '[write read][open open][setattr getattr][write read][append read][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['surfaceflinger']['sensorhubservice']['fill'] = 'red'
G.add_edge('surfaceflinger','surfaceflinger')
G.edge['surfaceflinger']['surfaceflinger']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][write read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][append read][write read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][write read]'
G.edge['surfaceflinger']['surfaceflinger']['fill'] = 'red'
G.add_edge('surfaceflinger','system_server')
G.edge['surfaceflinger']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][append read][write read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read]'
G.edge['surfaceflinger']['system_server']['fill'] = 'red'
G.add_edge('surfaceflinger','zygote')
G.edge['surfaceflinger']['zygote']['write-read'] = '[open open][write read][append read][write read][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['surfaceflinger']['zygote']['fill'] = 'red'
G.add_edge('system_server','adbd')
G.edge['system_server']['adbd']['write-read'] = '[write read][add_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][open open][open open][setattr getattr][write read][append read][write read][append read][setattr getattr][write read][append read][write read][append read][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][setsched getsched][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['system_server']['adbd']['fill'] = 'red'
G.add_edge('system_server','androidshmservice')
G.edge['system_server']['androidshmservice']['write-read'] = '[write read]'
G.edge['system_server']['androidshmservice']['fill'] = 'red'
G.add_edge('system_server','apaservice')
G.edge['system_server']['apaservice']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][write read][append read][write read][append read][write read]'
G.edge['system_server']['apaservice']['fill'] = 'red'
G.add_edge('system_server','appdomain')
G.edge['system_server']['appdomain']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][setopt getopt][write read][append read][write read][open open][write read][append read][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][open open][open open][write read][append read][append read][open open][write read][append read][write read][write read][open open][setattr getattr][write read][write read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read][open open][write read][append read][write read]'
G.edge['system_server']['appdomain']['fill'] = 'red'
G.add_edge('system_server','bintvoutservice')
G.edge['system_server']['bintvoutservice']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][write read][write read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['system_server']['bintvoutservice']['fill'] = 'red'
G.add_edge('system_server','bluetooth')
G.edge['system_server']['bluetooth']['write-read'] = '[setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][write read][append read][open open][write read][setattr getattr][write read][append read][setopt getopt][open open][open open][write read][append read][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][write read][write read]'
G.edge['system_server']['bluetooth']['fill'] = 'red'
G.add_edge('system_server','bugreport')
G.edge['system_server']['bugreport']['write-read'] = '[open open][write read][append read][open open][write read][append read][setattr getattr][write read][append read][write read][write read]'
G.edge['system_server']['bugreport']['fill'] = 'red'
G.add_edge('system_server','charon')
G.edge['system_server']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['system_server']['charon']['fill'] = 'red'
G.add_edge('system_server','drmserver')
G.edge['system_server']['drmserver']['write-read'] = '[open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][write read][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['system_server']['drmserver']['fill'] = 'red'
G.add_edge('system_server','dumpstate')
G.edge['system_server']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][setopt getopt][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][setattr getattr][write read][add_name search][remove_name search][open open][open open][write read][append read][write read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][write read]'
G.edge['system_server']['dumpstate']['fill'] = 'red'
G.add_edge('system_server','dumpsys')
G.edge['system_server']['dumpsys']['write-read'] = '[open open][write read][append read][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][write read]'
G.edge['system_server']['dumpsys']['fill'] = 'red'
G.add_edge('system_server','fixmo_app')
G.edge['system_server']['fixmo_app']['write-read'] = '[open open][append read][open open][setattr getattr][open open][append read][write read][open open][setattr getattr][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][write read]'
G.edge['system_server']['fixmo_app']['fill'] = 'red'
G.add_edge('system_server','good_app')
G.edge['system_server']['good_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][append read][open open][setattr getattr][open open][append read][write read][open open][setattr getattr][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][write read]'
G.edge['system_server']['good_app']['fill'] = 'red'
G.add_edge('system_server','healthd')
G.edge['system_server']['healthd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][write read][add_name search][remove_name search][open open][write read][append read][write read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][write read][open open][write read][append read][write read][append read][write read][write read]'
G.edge['system_server']['healthd']['fill'] = 'red'
G.add_edge('system_server','init_shell')
G.edge['system_server']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setattr getattr][setattr getattr][open open][write read][append read][open open][write read][append read][open open][open open][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][setsched getsched][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read]'
G.edge['system_server']['init_shell']['fill'] = 'red'
G.add_edge('system_server','init_shell')
G.edge['system_server']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setattr getattr][setattr getattr][open open][write read][append read][open open][write read][append read][open open][open open][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][setsched getsched][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read][write read]'
G.edge['system_server']['init_shell']['fill'] = 'red'
G.add_edge('system_server','isolated_app')
G.edge['system_server']['isolated_app']['write-read'] = '[write read]'
G.edge['system_server']['isolated_app']['fill'] = 'red'
G.add_edge('system_server','jackservice')
G.edge['system_server']['jackservice']['write-read'] = '[add_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][write read][open open][write read][append read][write read][setattr getattr][write read][append read][open open][write read][append read][write read][append read][write read]'
G.edge['system_server']['jackservice']['fill'] = 'red'
G.add_edge('system_server','keystore')
G.edge['system_server']['keystore']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][append read][open open][write read][append read][write read]'
G.edge['system_server']['keystore']['fill'] = 'red'
G.add_edge('system_server','mediaserver')
G.edge['system_server']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][write read][add_name search][remove_name search][open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][write read][write read][write read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][setattr getattr][write read][append read][write read][append read][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][setattr getattr][write read][write read][write read]'
G.edge['system_server']['mediaserver']['fill'] = 'red'
G.add_edge('system_server','nfc')
G.edge['system_server']['nfc']['write-read'] = '[open open][setattr getattr][write read][append read][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['system_server']['nfc']['fill'] = 'red'
G.add_edge('system_server','oneseg_mw')
G.edge['system_server']['oneseg_mw']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][write read][append read][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read][write read]'
G.edge['system_server']['oneseg_mw']['fill'] = 'red'
G.add_edge('system_server','radio')
G.edge['system_server']['radio']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][append read][open open][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][write read][write read][write read]'
G.edge['system_server']['radio']['fill'] = 'red'
G.add_edge('system_server','sensorhubservice')
G.edge['system_server']['sensorhubservice']['write-read'] = '[write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['system_server']['sensorhubservice']['fill'] = 'red'
G.add_edge('system_server','surfaceflinger')
G.edge['system_server']['surfaceflinger']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][write read][open open][write read][append read][write read][open open][write read][append read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][write read][append read][open open][write read][append read][write read][write read][append read][write read][open open][write read][append read][open open][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read]'
G.edge['system_server']['surfaceflinger']['fill'] = 'red'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][setsched getsched][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setopt getopt][write read][setattr getattr][setattr getattr][write read][append read][write read][append read][setopt getopt][setopt getopt][setattr getattr][setattr getattr][write read][append read][write read][append read][setopt getopt][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][append read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][setsched getsched][open open][setattr getattr][write read][append read][open open][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][write read][append read][write read][open open][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][write read][setattr getattr][write read][append read][write read][open open][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][write read][setopt getopt][open open][open open][write read][append read][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][write read][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][setopt getopt][setsched getsched][setsched getsched][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][setsched getsched][setsched getsched][open open][write read][append read][relabelto relabelfrom][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][setattr getattr][write read][write read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][write read]'
G.edge['system_server']['system_server']['fill'] = 'red'
G.add_edge('system_server','zygote')
G.edge['system_server']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][write read][write read][write read][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][append read][write read][open open][write read][append read][open open][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['system_server']['zygote']['fill'] = 'red'
G.add_edge('system_server','fixmo_app')
G.edge['system_server']['fixmo_app']['write-read'] = '[open open][append read][open open][setattr getattr][open open][append read][write read][open open][setattr getattr][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][write read][setopt getopt]'
G.add_edge('system_server','good_app')
G.edge['system_server']['good_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][append read][open open][setattr getattr][open open][append read][write read][open open][setattr getattr][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][write read][setopt getopt]'
G.add_edge('system_server','ime_app')
G.edge['system_server']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][add_name search][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][append read][setsched getsched][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][setopt getopt]'
G.add_edge('system_server','nfc')
G.edge['system_server']['nfc']['write-read'] = '[open open][setattr getattr][write read][append read][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt]'
G.add_edge('system_server','platformappdomain')
G.edge['system_server']['platformappdomain']['write-read'] = '[open open][setattr getattr][write read][append read][write read][write read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][setopt getopt]'
G.add_edge('system_server','radio')
G.edge['system_server']['radio']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][append read][open open][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][write read][write read][write read][setopt getopt]'
G.add_edge('system_server','samsung_app')
G.edge['system_server']['samsung_app']['write-read'] = '[setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setopt getopt]'
G.add_edge('system_server','s_system_app')
G.edge['system_server']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][add_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read][append read][write read][open open][setattr getattr][write read][append read][setattr getattr][setattr getattr][open open][setattr getattr][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][write read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][open open][setattr getattr][setattr getattr][append read][write read][append read][write read][setsched getsched][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][setopt getopt]'
G.add_edge('system_server','system_app')
G.edge['system_server']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][add_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][append read][setsched getsched][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][setopt getopt]'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][setsched getsched][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setopt getopt][write read][setattr getattr][setattr getattr][write read][append read][write read][append read][setopt getopt][setopt getopt][setattr getattr][setattr getattr][write read][append read][write read][append read][setopt getopt][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][append read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][setsched getsched][open open][setattr getattr][write read][append read][open open][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][write read][append read][write read][open open][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][write read][setattr getattr][write read][append read][write read][open open][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][write read][setopt getopt][open open][open open][write read][append read][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][write read][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][setopt getopt][setsched getsched][setsched getsched][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][setsched getsched][setsched getsched][open open][write read][append read][relabelto relabelfrom][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][setattr getattr][write read][write read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][write read][setopt getopt]'
G.add_edge('system_server','untrusteddomain')
G.edge['system_server']['untrusteddomain']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setopt getopt][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][write read][add_name search][remove_name search][setsched getsched][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][setopt getopt]'
G.add_edge('zygote','adbd')
G.edge['zygote']['adbd']['write-read'] = '[write read][add_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['zygote']['adbd']['fill'] = 'red'
G.add_edge('zygote','androidshmservice')
G.edge['zygote']['androidshmservice']['write-read'] = '[write read]'
G.edge['zygote']['androidshmservice']['fill'] = 'red'
G.add_edge('zygote','apaservice')
G.edge['zygote']['apaservice']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][write read]'
G.edge['zygote']['apaservice']['fill'] = 'red'
G.add_edge('zygote','appdomain')
G.edge['zygote']['appdomain']['write-read'] = '[open open][write read][append read][open open][setattr getattr][open open][open open][write read][append read][append read][open open][setattr getattr][write read]'
G.edge['zygote']['appdomain']['fill'] = 'red'
G.add_edge('zygote','bintvoutservice')
G.edge['zygote']['bintvoutservice']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['zygote']['bintvoutservice']['fill'] = 'red'
G.add_edge('zygote','bluetooth')
G.edge['zygote']['bluetooth']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['zygote']['bluetooth']['fill'] = 'red'
G.add_edge('zygote','bugreport')
G.edge['zygote']['bugreport']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read]'
G.edge['zygote']['bugreport']['fill'] = 'red'
G.add_edge('zygote','charon')
G.edge['zygote']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['zygote']['charon']['fill'] = 'red'
G.add_edge('zygote','drmserver')
G.edge['zygote']['drmserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['zygote']['drmserver']['fill'] = 'red'
G.add_edge('zygote','dumpstate')
G.edge['zygote']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['zygote']['dumpstate']['fill'] = 'red'
G.add_edge('zygote','dumpsys')
G.edge['zygote']['dumpsys']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read]'
G.edge['zygote']['dumpsys']['fill'] = 'red'
G.add_edge('zygote','fixmo_app')
G.edge['zygote']['fixmo_app']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][open open][append read][open open][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['zygote']['fixmo_app']['fill'] = 'red'
G.add_edge('zygote','good_app')
G.edge['zygote']['good_app']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][open open][append read][open open][setattr getattr][open open][setattr getattr][write read][append read][write read]'
G.edge['zygote']['good_app']['fill'] = 'red'
G.add_edge('zygote','healthd')
G.edge['zygote']['healthd']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read]'
G.edge['zygote']['healthd']['fill'] = 'red'
G.add_edge('zygote','init_shell')
G.edge['zygote']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['zygote']['init_shell']['fill'] = 'red'
G.add_edge('zygote','init_shell')
G.edge['zygote']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][write read]'
G.edge['zygote']['init_shell']['fill'] = 'red'
G.add_edge('zygote','isolated_app')
G.edge['zygote']['isolated_app']['write-read'] = '[open open][setattr getattr][append read][write read]'
G.edge['zygote']['isolated_app']['fill'] = 'red'
G.add_edge('zygote','jackservice')
G.edge['zygote']['jackservice']['write-read'] = '[add_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][write read]'
G.edge['zygote']['jackservice']['fill'] = 'red'
G.add_edge('zygote','keystore')
G.edge['zygote']['keystore']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][write read]'
G.edge['zygote']['keystore']['fill'] = 'red'
G.add_edge('zygote','mediaserver')
G.edge['zygote']['mediaserver']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][setattr getattr][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['zygote']['mediaserver']['fill'] = 'red'
G.add_edge('zygote','nfc')
G.edge['zygote']['nfc']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['zygote']['nfc']['fill'] = 'red'
G.add_edge('zygote','oneseg_mw')
G.edge['zygote']['oneseg_mw']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['zygote']['oneseg_mw']['fill'] = 'red'
G.add_edge('zygote','radio')
G.edge['zygote']['radio']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['zygote']['radio']['fill'] = 'red'
G.add_edge('zygote','sensorhubservice')
G.edge['zygote']['sensorhubservice']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['zygote']['sensorhubservice']['fill'] = 'red'
G.add_edge('zygote','surfaceflinger')
G.edge['zygote']['surfaceflinger']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['zygote']['surfaceflinger']['fill'] = 'red'
G.add_edge('zygote','system_server')
G.edge['zygote']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][write read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['zygote']['system_server']['fill'] = 'red'
G.add_edge('zygote','zygote')
G.edge['zygote']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][setpgid getpgid][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][add_name search][remove_name search][add_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][append read][write read][open open][write read][append read][setpgid getpgid][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][add_name search][add_name search][open open][setattr getattr][write read][add_name search][remove_name search][setpgid getpgid][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read]'
G.edge['zygote']['zygote']['fill'] = 'red'
app = Viewer(G)
app.mainloop()