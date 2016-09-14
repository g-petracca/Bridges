import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('adbd','bintvoutservice')
G.edge['adbd']['bintvoutservice']['write-read'] = '[open open]'
G.add_edge('adbd','bootanim')
G.edge['adbd']['bootanim']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('adbd','commonplatformappdomain')
G.edge['adbd']['commonplatformappdomain']['write-read'] = '[open open]'
G.add_edge('adbd','fixmo_app')
G.edge['adbd']['fixmo_app']['write-read'] = '[open open]'
G.add_edge('adbd','good_app')
G.edge['adbd']['good_app']['write-read'] = '[open open]'
G.add_edge('adbd','healthd')
G.edge['adbd']['healthd']['write-read'] = '[open open]'
G.add_edge('adbd','ime_app')
G.edge['adbd']['ime_app']['write-read'] = '[open open]'
G.add_edge('adbd','isolated_app')
G.edge['adbd']['isolated_app']['write-read'] = '[open open]'
G.add_edge('adbd','untrusted_app')
G.edge['adbd']['untrusted_app']['write-read'] = '[open open]'
G.add_edge('adbd','umcagent_app')
G.edge['adbd']['umcagent_app']['write-read'] = '[open open]'
G.add_edge('adbd','vpn_untrusted_app')
G.edge['adbd']['vpn_untrusted_app']['write-read'] = '[open open]'
G.add_edge('adbd','trustonicpartner_app')
G.edge['adbd']['trustonicpartner_app']['write-read'] = '[open open]'
G.add_edge('adbd','llk_untrusted_app')
G.edge['adbd']['llk_untrusted_app']['write-read'] = '[open open]'
G.add_edge('adbd','filtered_untrusted_app')
G.edge['adbd']['filtered_untrusted_app']['write-read'] = '[open open]'
G.add_edge('adbd','filtered_google_app')
G.edge['adbd']['filtered_google_app']['write-read'] = '[open open]'
G.add_edge('adbd','knox_untrusted_app')
G.edge['adbd']['knox_untrusted_app']['write-read'] = '[open open]'
G.add_edge('adbd','irm_app')
G.edge['adbd']['irm_app']['write-read'] = '[open open]'
G.add_edge('adbd','gad_untrusted_app')
G.edge['adbd']['gad_untrusted_app']['write-read'] = '[open open]'
G.add_edge('adbd','carrier_app')
G.edge['adbd']['carrier_app']['write-read'] = '[open open]'
G.add_edge('adbd','lpm')
G.edge['adbd']['lpm']['write-read'] = '[open open]'
G.add_edge('adbd','mmi')
G.edge['adbd']['mmi']['write-read'] = '[open open]'
G.add_edge('adbd','mm-pp-daemon')
G.edge['adbd']['mm-pp-daemon']['write-read'] = '[open open]'
G.add_edge('adbd','mm-qcamera-daemon')
G.edge['adbd']['mm-qcamera-daemon']['write-read'] = '[open open]'
G.add_edge('adbd','newAttr96')
G.edge['adbd']['newAttr96']['write-read'] = '[open open]'
G.add_edge('adbd','radio')
G.edge['adbd']['radio']['write-read'] = '[open open]'
G.add_edge('adbd','s_system_app')
G.edge['adbd']['s_system_app']['write-read'] = '[open open]'
G.add_edge('adbd','surfaceflinger')
G.edge['adbd']['surfaceflinger']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('adbd','system_app')
G.edge['adbd']['system_app']['write-read'] = '[open open]'
G.add_edge('adbd','wfd_app')
G.edge['adbd']['wfd_app']['write-read'] = '[open open]'
G.add_edge('adbd','wfdservice')
G.edge['adbd']['wfdservice']['write-read'] = '[open open]'
G.add_edge('adbd','zygote')
G.edge['adbd']['zygote']['write-read'] = '[open open]'
G.add_edge('adbd','isolated_app')
G.edge['adbd']['isolated_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('adbd','untrusted_app')
G.edge['adbd']['untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('adbd','umcagent_app')
G.edge['adbd']['umcagent_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('adbd','vpn_untrusted_app')
G.edge['adbd']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('adbd','trustonicpartner_app')
G.edge['adbd']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('adbd','llk_untrusted_app')
G.edge['adbd']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('adbd','filtered_untrusted_app')
G.edge['adbd']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('adbd','filtered_google_app')
G.edge['adbd']['filtered_google_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('adbd','knox_untrusted_app')
G.edge['adbd']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('adbd','irm_app')
G.edge['adbd']['irm_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('adbd','gad_untrusted_app')
G.edge['adbd']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('adbd','carrier_app')
G.edge['adbd']['carrier_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('adbd','newAttr96')
G.edge['adbd']['newAttr96']['write-read'] = '[open open][setattr getattr]'
G.add_edge('adbd','bintvoutservice')
G.edge['adbd']['bintvoutservice']['write-read'] = '[open open][write read]'
G.edge['adbd']['bintvoutservice']['fill'] = 'red'
G.add_edge('adbd','bintvoutservice')
G.edge['adbd']['bintvoutservice']['write-read'] = '[open open][write read][append read]'
G.add_edge('adbd','bootanim')
G.edge['adbd']['bootanim']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['adbd']['bootanim']['fill'] = 'red'
G.add_edge('adbd','bootanim')
G.edge['adbd']['bootanim']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('adbd','commonplatformappdomain')
G.edge['adbd']['commonplatformappdomain']['write-read'] = '[open open][write read]'
G.edge['adbd']['commonplatformappdomain']['fill'] = 'red'
G.add_edge('adbd','commonplatformappdomain')
G.edge['adbd']['commonplatformappdomain']['write-read'] = '[open open][write read][append read]'
G.add_edge('adbd','fixmo_app')
G.edge['adbd']['fixmo_app']['write-read'] = '[open open][write read]'
G.edge['adbd']['fixmo_app']['fill'] = 'red'
G.add_edge('adbd','fixmo_app')
G.edge['adbd']['fixmo_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('adbd','good_app')
G.edge['adbd']['good_app']['write-read'] = '[open open][write read]'
G.edge['adbd']['good_app']['fill'] = 'red'
G.add_edge('adbd','good_app')
G.edge['adbd']['good_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('adbd','healthd')
G.edge['adbd']['healthd']['write-read'] = '[open open][write read]'
G.edge['adbd']['healthd']['fill'] = 'red'
G.add_edge('adbd','healthd')
G.edge['adbd']['healthd']['write-read'] = '[open open][write read][append read]'
G.add_edge('adbd','ime_app')
G.edge['adbd']['ime_app']['write-read'] = '[open open][write read]'
G.edge['adbd']['ime_app']['fill'] = 'red'
G.add_edge('adbd','ime_app')
G.edge['adbd']['ime_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('adbd','isolated_app')
G.edge['adbd']['isolated_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('adbd','untrusted_app')
G.edge['adbd']['untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('adbd','umcagent_app')
G.edge['adbd']['umcagent_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('adbd','vpn_untrusted_app')
G.edge['adbd']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('adbd','trustonicpartner_app')
G.edge['adbd']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('adbd','llk_untrusted_app')
G.edge['adbd']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('adbd','filtered_untrusted_app')
G.edge['adbd']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('adbd','filtered_google_app')
G.edge['adbd']['filtered_google_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('adbd','knox_untrusted_app')
G.edge['adbd']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('adbd','irm_app')
G.edge['adbd']['irm_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('adbd','gad_untrusted_app')
G.edge['adbd']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('adbd','carrier_app')
G.edge['adbd']['carrier_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('adbd','lpm')
G.edge['adbd']['lpm']['write-read'] = '[open open][write read]'
G.edge['adbd']['lpm']['fill'] = 'red'
G.add_edge('adbd','lpm')
G.edge['adbd']['lpm']['write-read'] = '[open open][write read][append read]'
G.add_edge('adbd','mmi')
G.edge['adbd']['mmi']['write-read'] = '[open open][write read]'
G.edge['adbd']['mmi']['fill'] = 'red'
G.add_edge('adbd','mmi')
G.edge['adbd']['mmi']['write-read'] = '[open open][write read][append read]'
G.add_edge('adbd','mm-pp-daemon')
G.edge['adbd']['mm-pp-daemon']['write-read'] = '[open open][write read]'
G.edge['adbd']['mm-pp-daemon']['fill'] = 'red'
G.add_edge('adbd','mm-pp-daemon')
G.edge['adbd']['mm-pp-daemon']['write-read'] = '[open open][write read][append read]'
G.add_edge('adbd','mm-qcamera-daemon')
G.edge['adbd']['mm-qcamera-daemon']['write-read'] = '[open open][write read]'
G.edge['adbd']['mm-qcamera-daemon']['fill'] = 'red'
G.add_edge('adbd','mm-qcamera-daemon')
G.edge['adbd']['mm-qcamera-daemon']['write-read'] = '[open open][write read][append read]'
G.add_edge('adbd','newAttr96')
G.edge['adbd']['newAttr96']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['adbd']['newAttr96']['fill'] = 'red'
G.add_edge('adbd','newAttr96')
G.edge['adbd']['newAttr96']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('adbd','radio')
G.edge['adbd']['radio']['write-read'] = '[open open][write read]'
G.edge['adbd']['radio']['fill'] = 'red'
G.add_edge('adbd','radio')
G.edge['adbd']['radio']['write-read'] = '[open open][write read][append read]'
G.add_edge('adbd','s_system_app')
G.edge['adbd']['s_system_app']['write-read'] = '[open open][write read]'
G.edge['adbd']['s_system_app']['fill'] = 'red'
G.add_edge('adbd','s_system_app')
G.edge['adbd']['s_system_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('adbd','surfaceflinger')
G.edge['adbd']['surfaceflinger']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['adbd']['surfaceflinger']['fill'] = 'red'
G.add_edge('adbd','surfaceflinger')
G.edge['adbd']['surfaceflinger']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('adbd','system_app')
G.edge['adbd']['system_app']['write-read'] = '[open open][write read]'
G.edge['adbd']['system_app']['fill'] = 'red'
G.add_edge('adbd','system_app')
G.edge['adbd']['system_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('adbd','wfd_app')
G.edge['adbd']['wfd_app']['write-read'] = '[open open][write read]'
G.edge['adbd']['wfd_app']['fill'] = 'red'
G.add_edge('adbd','wfd_app')
G.edge['adbd']['wfd_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('adbd','wfdservice')
G.edge['adbd']['wfdservice']['write-read'] = '[open open][write read]'
G.edge['adbd']['wfdservice']['fill'] = 'red'
G.add_edge('adbd','wfdservice')
G.edge['adbd']['wfdservice']['write-read'] = '[open open][write read][append read]'
G.add_edge('adbd','zygote')
G.edge['adbd']['zygote']['write-read'] = '[open open][write read]'
G.edge['adbd']['zygote']['fill'] = 'red'
G.add_edge('adbd','zygote')
G.edge['adbd']['zygote']['write-read'] = '[open open][write read][append read]'
G.add_edge('bintvoutservice','bintvoutservice')
G.edge['bintvoutservice']['bintvoutservice']['write-read'] = '[open open]'
G.add_edge('bintvoutservice','bootanim')
G.edge['bintvoutservice']['bootanim']['write-read'] = '[open open]'
G.add_edge('bintvoutservice','commonplatformappdomain')
G.edge['bintvoutservice']['commonplatformappdomain']['write-read'] = '[open open]'
G.add_edge('bintvoutservice','fixmo_app')
G.edge['bintvoutservice']['fixmo_app']['write-read'] = '[open open]'
G.add_edge('bintvoutservice','good_app')
G.edge['bintvoutservice']['good_app']['write-read'] = '[open open]'
G.add_edge('bintvoutservice','healthd')
G.edge['bintvoutservice']['healthd']['write-read'] = '[open open]'
G.add_edge('bintvoutservice','ime_app')
G.edge['bintvoutservice']['ime_app']['write-read'] = '[open open]'
G.add_edge('bintvoutservice','isolated_app')
G.edge['bintvoutservice']['isolated_app']['write-read'] = '[open open]'
G.add_edge('bintvoutservice','untrusted_app')
G.edge['bintvoutservice']['untrusted_app']['write-read'] = '[open open]'
G.add_edge('bintvoutservice','umcagent_app')
G.edge['bintvoutservice']['umcagent_app']['write-read'] = '[open open]'
G.add_edge('bintvoutservice','vpn_untrusted_app')
G.edge['bintvoutservice']['vpn_untrusted_app']['write-read'] = '[open open]'
G.add_edge('bintvoutservice','trustonicpartner_app')
G.edge['bintvoutservice']['trustonicpartner_app']['write-read'] = '[open open]'
G.add_edge('bintvoutservice','llk_untrusted_app')
G.edge['bintvoutservice']['llk_untrusted_app']['write-read'] = '[open open]'
G.add_edge('bintvoutservice','filtered_untrusted_app')
G.edge['bintvoutservice']['filtered_untrusted_app']['write-read'] = '[open open]'
G.add_edge('bintvoutservice','filtered_google_app')
G.edge['bintvoutservice']['filtered_google_app']['write-read'] = '[open open]'
G.add_edge('bintvoutservice','knox_untrusted_app')
G.edge['bintvoutservice']['knox_untrusted_app']['write-read'] = '[open open]'
G.add_edge('bintvoutservice','irm_app')
G.edge['bintvoutservice']['irm_app']['write-read'] = '[open open]'
G.add_edge('bintvoutservice','gad_untrusted_app')
G.edge['bintvoutservice']['gad_untrusted_app']['write-read'] = '[open open]'
G.add_edge('bintvoutservice','carrier_app')
G.edge['bintvoutservice']['carrier_app']['write-read'] = '[open open]'
G.add_edge('bintvoutservice','lpm')
G.edge['bintvoutservice']['lpm']['write-read'] = '[open open]'
G.add_edge('bintvoutservice','mmi')
G.edge['bintvoutservice']['mmi']['write-read'] = '[open open]'
G.add_edge('bintvoutservice','mm-pp-daemon')
G.edge['bintvoutservice']['mm-pp-daemon']['write-read'] = '[open open]'
G.add_edge('bintvoutservice','mm-qcamera-daemon')
G.edge['bintvoutservice']['mm-qcamera-daemon']['write-read'] = '[open open]'
G.add_edge('bintvoutservice','newAttr96')
G.edge['bintvoutservice']['newAttr96']['write-read'] = '[open open]'
G.add_edge('bintvoutservice','radio')
G.edge['bintvoutservice']['radio']['write-read'] = '[open open]'
G.add_edge('bintvoutservice','s_system_app')
G.edge['bintvoutservice']['s_system_app']['write-read'] = '[open open]'
G.add_edge('bintvoutservice','surfaceflinger')
G.edge['bintvoutservice']['surfaceflinger']['write-read'] = '[open open]'
G.add_edge('bintvoutservice','system_app')
G.edge['bintvoutservice']['system_app']['write-read'] = '[open open]'
G.add_edge('bintvoutservice','wfd_app')
G.edge['bintvoutservice']['wfd_app']['write-read'] = '[open open]'
G.add_edge('bintvoutservice','wfdservice')
G.edge['bintvoutservice']['wfdservice']['write-read'] = '[open open]'
G.add_edge('bintvoutservice','zygote')
G.edge['bintvoutservice']['zygote']['write-read'] = '[open open]'
G.add_edge('bintvoutservice','isolated_app')
G.edge['bintvoutservice']['isolated_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('bintvoutservice','untrusted_app')
G.edge['bintvoutservice']['untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('bintvoutservice','umcagent_app')
G.edge['bintvoutservice']['umcagent_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('bintvoutservice','vpn_untrusted_app')
G.edge['bintvoutservice']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('bintvoutservice','trustonicpartner_app')
G.edge['bintvoutservice']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('bintvoutservice','llk_untrusted_app')
G.edge['bintvoutservice']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('bintvoutservice','filtered_untrusted_app')
G.edge['bintvoutservice']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('bintvoutservice','filtered_google_app')
G.edge['bintvoutservice']['filtered_google_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('bintvoutservice','knox_untrusted_app')
G.edge['bintvoutservice']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('bintvoutservice','irm_app')
G.edge['bintvoutservice']['irm_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('bintvoutservice','gad_untrusted_app')
G.edge['bintvoutservice']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('bintvoutservice','carrier_app')
G.edge['bintvoutservice']['carrier_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('bintvoutservice','newAttr96')
G.edge['bintvoutservice']['newAttr96']['write-read'] = '[open open][setattr getattr]'
G.add_edge('bintvoutservice','bintvoutservice')
G.edge['bintvoutservice']['bintvoutservice']['write-read'] = '[open open][write read]'
G.edge['bintvoutservice']['bintvoutservice']['fill'] = 'red'
G.add_edge('bintvoutservice','bintvoutservice')
G.edge['bintvoutservice']['bintvoutservice']['write-read'] = '[open open][write read][append read]'
G.add_edge('bintvoutservice','bootanim')
G.edge['bintvoutservice']['bootanim']['write-read'] = '[open open][write read]'
G.edge['bintvoutservice']['bootanim']['fill'] = 'red'
G.add_edge('bintvoutservice','bootanim')
G.edge['bintvoutservice']['bootanim']['write-read'] = '[open open][write read][append read]'
G.add_edge('bintvoutservice','commonplatformappdomain')
G.edge['bintvoutservice']['commonplatformappdomain']['write-read'] = '[open open][write read]'
G.edge['bintvoutservice']['commonplatformappdomain']['fill'] = 'red'
G.add_edge('bintvoutservice','commonplatformappdomain')
G.edge['bintvoutservice']['commonplatformappdomain']['write-read'] = '[open open][write read][append read]'
G.add_edge('bintvoutservice','fixmo_app')
G.edge['bintvoutservice']['fixmo_app']['write-read'] = '[open open][write read]'
G.edge['bintvoutservice']['fixmo_app']['fill'] = 'red'
G.add_edge('bintvoutservice','fixmo_app')
G.edge['bintvoutservice']['fixmo_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('bintvoutservice','good_app')
G.edge['bintvoutservice']['good_app']['write-read'] = '[open open][write read]'
G.edge['bintvoutservice']['good_app']['fill'] = 'red'
G.add_edge('bintvoutservice','good_app')
G.edge['bintvoutservice']['good_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('bintvoutservice','healthd')
G.edge['bintvoutservice']['healthd']['write-read'] = '[open open][write read]'
G.edge['bintvoutservice']['healthd']['fill'] = 'red'
G.add_edge('bintvoutservice','healthd')
G.edge['bintvoutservice']['healthd']['write-read'] = '[open open][write read][append read]'
G.add_edge('bintvoutservice','ime_app')
G.edge['bintvoutservice']['ime_app']['write-read'] = '[open open][write read]'
G.edge['bintvoutservice']['ime_app']['fill'] = 'red'
G.add_edge('bintvoutservice','ime_app')
G.edge['bintvoutservice']['ime_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('bintvoutservice','isolated_app')
G.edge['bintvoutservice']['isolated_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('bintvoutservice','untrusted_app')
G.edge['bintvoutservice']['untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('bintvoutservice','umcagent_app')
G.edge['bintvoutservice']['umcagent_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('bintvoutservice','vpn_untrusted_app')
G.edge['bintvoutservice']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('bintvoutservice','trustonicpartner_app')
G.edge['bintvoutservice']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('bintvoutservice','llk_untrusted_app')
G.edge['bintvoutservice']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('bintvoutservice','filtered_untrusted_app')
G.edge['bintvoutservice']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('bintvoutservice','filtered_google_app')
G.edge['bintvoutservice']['filtered_google_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('bintvoutservice','knox_untrusted_app')
G.edge['bintvoutservice']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('bintvoutservice','irm_app')
G.edge['bintvoutservice']['irm_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('bintvoutservice','gad_untrusted_app')
G.edge['bintvoutservice']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('bintvoutservice','carrier_app')
G.edge['bintvoutservice']['carrier_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('bintvoutservice','lpm')
G.edge['bintvoutservice']['lpm']['write-read'] = '[open open][write read]'
G.edge['bintvoutservice']['lpm']['fill'] = 'red'
G.add_edge('bintvoutservice','lpm')
G.edge['bintvoutservice']['lpm']['write-read'] = '[open open][write read][append read]'
G.add_edge('bintvoutservice','mmi')
G.edge['bintvoutservice']['mmi']['write-read'] = '[open open][write read]'
G.edge['bintvoutservice']['mmi']['fill'] = 'red'
G.add_edge('bintvoutservice','mmi')
G.edge['bintvoutservice']['mmi']['write-read'] = '[open open][write read][append read]'
G.add_edge('bintvoutservice','mm-pp-daemon')
G.edge['bintvoutservice']['mm-pp-daemon']['write-read'] = '[open open][write read]'
G.edge['bintvoutservice']['mm-pp-daemon']['fill'] = 'red'
G.add_edge('bintvoutservice','mm-pp-daemon')
G.edge['bintvoutservice']['mm-pp-daemon']['write-read'] = '[open open][write read][append read]'
G.add_edge('bintvoutservice','mm-qcamera-daemon')
G.edge['bintvoutservice']['mm-qcamera-daemon']['write-read'] = '[open open][write read]'
G.edge['bintvoutservice']['mm-qcamera-daemon']['fill'] = 'red'
G.add_edge('bintvoutservice','mm-qcamera-daemon')
G.edge['bintvoutservice']['mm-qcamera-daemon']['write-read'] = '[open open][write read][append read]'
G.add_edge('bintvoutservice','newAttr96')
G.edge['bintvoutservice']['newAttr96']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['bintvoutservice']['newAttr96']['fill'] = 'red'
G.add_edge('bintvoutservice','newAttr96')
G.edge['bintvoutservice']['newAttr96']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('bintvoutservice','radio')
G.edge['bintvoutservice']['radio']['write-read'] = '[open open][write read]'
G.edge['bintvoutservice']['radio']['fill'] = 'red'
G.add_edge('bintvoutservice','radio')
G.edge['bintvoutservice']['radio']['write-read'] = '[open open][write read][append read]'
G.add_edge('bintvoutservice','s_system_app')
G.edge['bintvoutservice']['s_system_app']['write-read'] = '[open open][write read]'
G.edge['bintvoutservice']['s_system_app']['fill'] = 'red'
G.add_edge('bintvoutservice','s_system_app')
G.edge['bintvoutservice']['s_system_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('bintvoutservice','surfaceflinger')
G.edge['bintvoutservice']['surfaceflinger']['write-read'] = '[open open][write read]'
G.edge['bintvoutservice']['surfaceflinger']['fill'] = 'red'
G.add_edge('bintvoutservice','surfaceflinger')
G.edge['bintvoutservice']['surfaceflinger']['write-read'] = '[open open][write read][append read]'
G.add_edge('bintvoutservice','system_app')
G.edge['bintvoutservice']['system_app']['write-read'] = '[open open][write read]'
G.edge['bintvoutservice']['system_app']['fill'] = 'red'
G.add_edge('bintvoutservice','system_app')
G.edge['bintvoutservice']['system_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('bintvoutservice','wfd_app')
G.edge['bintvoutservice']['wfd_app']['write-read'] = '[open open][write read]'
G.edge['bintvoutservice']['wfd_app']['fill'] = 'red'
G.add_edge('bintvoutservice','wfd_app')
G.edge['bintvoutservice']['wfd_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('bintvoutservice','wfdservice')
G.edge['bintvoutservice']['wfdservice']['write-read'] = '[open open][write read]'
G.edge['bintvoutservice']['wfdservice']['fill'] = 'red'
G.add_edge('bintvoutservice','wfdservice')
G.edge['bintvoutservice']['wfdservice']['write-read'] = '[open open][write read][append read]'
G.add_edge('bintvoutservice','zygote')
G.edge['bintvoutservice']['zygote']['write-read'] = '[open open][write read]'
G.edge['bintvoutservice']['zygote']['fill'] = 'red'
G.add_edge('bintvoutservice','zygote')
G.edge['bintvoutservice']['zygote']['write-read'] = '[open open][write read][append read]'
G.add_edge('bootanim','bintvoutservice')
G.edge['bootanim']['bintvoutservice']['write-read'] = '[open open]'
G.add_edge('bootanim','bootanim')
G.edge['bootanim']['bootanim']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('bootanim','commonplatformappdomain')
G.edge['bootanim']['commonplatformappdomain']['write-read'] = '[open open]'
G.add_edge('bootanim','fixmo_app')
G.edge['bootanim']['fixmo_app']['write-read'] = '[open open]'
G.add_edge('bootanim','good_app')
G.edge['bootanim']['good_app']['write-read'] = '[open open]'
G.add_edge('bootanim','healthd')
G.edge['bootanim']['healthd']['write-read'] = '[open open]'
G.add_edge('bootanim','ime_app')
G.edge['bootanim']['ime_app']['write-read'] = '[open open]'
G.add_edge('bootanim','isolated_app')
G.edge['bootanim']['isolated_app']['write-read'] = '[open open]'
G.add_edge('bootanim','untrusted_app')
G.edge['bootanim']['untrusted_app']['write-read'] = '[open open]'
G.add_edge('bootanim','umcagent_app')
G.edge['bootanim']['umcagent_app']['write-read'] = '[open open]'
G.add_edge('bootanim','vpn_untrusted_app')
G.edge['bootanim']['vpn_untrusted_app']['write-read'] = '[open open]'
G.add_edge('bootanim','trustonicpartner_app')
G.edge['bootanim']['trustonicpartner_app']['write-read'] = '[open open]'
G.add_edge('bootanim','llk_untrusted_app')
G.edge['bootanim']['llk_untrusted_app']['write-read'] = '[open open]'
G.add_edge('bootanim','filtered_untrusted_app')
G.edge['bootanim']['filtered_untrusted_app']['write-read'] = '[open open]'
G.add_edge('bootanim','filtered_google_app')
G.edge['bootanim']['filtered_google_app']['write-read'] = '[open open]'
G.add_edge('bootanim','knox_untrusted_app')
G.edge['bootanim']['knox_untrusted_app']['write-read'] = '[open open]'
G.add_edge('bootanim','irm_app')
G.edge['bootanim']['irm_app']['write-read'] = '[open open]'
G.add_edge('bootanim','gad_untrusted_app')
G.edge['bootanim']['gad_untrusted_app']['write-read'] = '[open open]'
G.add_edge('bootanim','carrier_app')
G.edge['bootanim']['carrier_app']['write-read'] = '[open open]'
G.add_edge('bootanim','lpm')
G.edge['bootanim']['lpm']['write-read'] = '[open open]'
G.add_edge('bootanim','mmi')
G.edge['bootanim']['mmi']['write-read'] = '[open open]'
G.add_edge('bootanim','mm-pp-daemon')
G.edge['bootanim']['mm-pp-daemon']['write-read'] = '[open open]'
G.add_edge('bootanim','mm-qcamera-daemon')
G.edge['bootanim']['mm-qcamera-daemon']['write-read'] = '[open open]'
G.add_edge('bootanim','newAttr96')
G.edge['bootanim']['newAttr96']['write-read'] = '[open open]'
G.add_edge('bootanim','radio')
G.edge['bootanim']['radio']['write-read'] = '[open open]'
G.add_edge('bootanim','s_system_app')
G.edge['bootanim']['s_system_app']['write-read'] = '[open open]'
G.add_edge('bootanim','surfaceflinger')
G.edge['bootanim']['surfaceflinger']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('bootanim','system_app')
G.edge['bootanim']['system_app']['write-read'] = '[open open]'
G.add_edge('bootanim','wfd_app')
G.edge['bootanim']['wfd_app']['write-read'] = '[open open]'
G.add_edge('bootanim','wfdservice')
G.edge['bootanim']['wfdservice']['write-read'] = '[open open]'
G.add_edge('bootanim','zygote')
G.edge['bootanim']['zygote']['write-read'] = '[open open]'
G.add_edge('bootanim','isolated_app')
G.edge['bootanim']['isolated_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('bootanim','untrusted_app')
G.edge['bootanim']['untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('bootanim','umcagent_app')
G.edge['bootanim']['umcagent_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('bootanim','vpn_untrusted_app')
G.edge['bootanim']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('bootanim','trustonicpartner_app')
G.edge['bootanim']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('bootanim','llk_untrusted_app')
G.edge['bootanim']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('bootanim','filtered_untrusted_app')
G.edge['bootanim']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('bootanim','filtered_google_app')
G.edge['bootanim']['filtered_google_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('bootanim','knox_untrusted_app')
G.edge['bootanim']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('bootanim','irm_app')
G.edge['bootanim']['irm_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('bootanim','gad_untrusted_app')
G.edge['bootanim']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('bootanim','carrier_app')
G.edge['bootanim']['carrier_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('bootanim','newAttr96')
G.edge['bootanim']['newAttr96']['write-read'] = '[open open][setattr getattr]'
G.add_edge('bootanim','bintvoutservice')
G.edge['bootanim']['bintvoutservice']['write-read'] = '[open open][write read]'
G.edge['bootanim']['bintvoutservice']['fill'] = 'red'
G.add_edge('bootanim','bintvoutservice')
G.edge['bootanim']['bintvoutservice']['write-read'] = '[open open][write read][append read]'
G.add_edge('bootanim','bootanim')
G.edge['bootanim']['bootanim']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['bootanim']['bootanim']['fill'] = 'red'
G.add_edge('bootanim','bootanim')
G.edge['bootanim']['bootanim']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('bootanim','commonplatformappdomain')
G.edge['bootanim']['commonplatformappdomain']['write-read'] = '[open open][write read]'
G.edge['bootanim']['commonplatformappdomain']['fill'] = 'red'
G.add_edge('bootanim','commonplatformappdomain')
G.edge['bootanim']['commonplatformappdomain']['write-read'] = '[open open][write read][append read]'
G.add_edge('bootanim','fixmo_app')
G.edge['bootanim']['fixmo_app']['write-read'] = '[open open][write read]'
G.edge['bootanim']['fixmo_app']['fill'] = 'red'
G.add_edge('bootanim','fixmo_app')
G.edge['bootanim']['fixmo_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('bootanim','good_app')
G.edge['bootanim']['good_app']['write-read'] = '[open open][write read]'
G.edge['bootanim']['good_app']['fill'] = 'red'
G.add_edge('bootanim','good_app')
G.edge['bootanim']['good_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('bootanim','healthd')
G.edge['bootanim']['healthd']['write-read'] = '[open open][write read]'
G.edge['bootanim']['healthd']['fill'] = 'red'
G.add_edge('bootanim','healthd')
G.edge['bootanim']['healthd']['write-read'] = '[open open][write read][append read]'
G.add_edge('bootanim','ime_app')
G.edge['bootanim']['ime_app']['write-read'] = '[open open][write read]'
G.edge['bootanim']['ime_app']['fill'] = 'red'
G.add_edge('bootanim','ime_app')
G.edge['bootanim']['ime_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('bootanim','isolated_app')
G.edge['bootanim']['isolated_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('bootanim','untrusted_app')
G.edge['bootanim']['untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('bootanim','umcagent_app')
G.edge['bootanim']['umcagent_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('bootanim','vpn_untrusted_app')
G.edge['bootanim']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('bootanim','trustonicpartner_app')
G.edge['bootanim']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('bootanim','llk_untrusted_app')
G.edge['bootanim']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('bootanim','filtered_untrusted_app')
G.edge['bootanim']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('bootanim','filtered_google_app')
G.edge['bootanim']['filtered_google_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('bootanim','knox_untrusted_app')
G.edge['bootanim']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('bootanim','irm_app')
G.edge['bootanim']['irm_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('bootanim','gad_untrusted_app')
G.edge['bootanim']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('bootanim','carrier_app')
G.edge['bootanim']['carrier_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('bootanim','lpm')
G.edge['bootanim']['lpm']['write-read'] = '[open open][write read]'
G.edge['bootanim']['lpm']['fill'] = 'red'
G.add_edge('bootanim','lpm')
G.edge['bootanim']['lpm']['write-read'] = '[open open][write read][append read]'
G.add_edge('bootanim','mmi')
G.edge['bootanim']['mmi']['write-read'] = '[open open][write read]'
G.edge['bootanim']['mmi']['fill'] = 'red'
G.add_edge('bootanim','mmi')
G.edge['bootanim']['mmi']['write-read'] = '[open open][write read][append read]'
G.add_edge('bootanim','mm-pp-daemon')
G.edge['bootanim']['mm-pp-daemon']['write-read'] = '[open open][write read]'
G.edge['bootanim']['mm-pp-daemon']['fill'] = 'red'
G.add_edge('bootanim','mm-pp-daemon')
G.edge['bootanim']['mm-pp-daemon']['write-read'] = '[open open][write read][append read]'
G.add_edge('bootanim','mm-qcamera-daemon')
G.edge['bootanim']['mm-qcamera-daemon']['write-read'] = '[open open][write read]'
G.edge['bootanim']['mm-qcamera-daemon']['fill'] = 'red'
G.add_edge('bootanim','mm-qcamera-daemon')
G.edge['bootanim']['mm-qcamera-daemon']['write-read'] = '[open open][write read][append read]'
G.add_edge('bootanim','newAttr96')
G.edge['bootanim']['newAttr96']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['bootanim']['newAttr96']['fill'] = 'red'
G.add_edge('bootanim','newAttr96')
G.edge['bootanim']['newAttr96']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('bootanim','radio')
G.edge['bootanim']['radio']['write-read'] = '[open open][write read]'
G.edge['bootanim']['radio']['fill'] = 'red'
G.add_edge('bootanim','radio')
G.edge['bootanim']['radio']['write-read'] = '[open open][write read][append read]'
G.add_edge('bootanim','s_system_app')
G.edge['bootanim']['s_system_app']['write-read'] = '[open open][write read]'
G.edge['bootanim']['s_system_app']['fill'] = 'red'
G.add_edge('bootanim','s_system_app')
G.edge['bootanim']['s_system_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('bootanim','surfaceflinger')
G.edge['bootanim']['surfaceflinger']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['bootanim']['surfaceflinger']['fill'] = 'red'
G.add_edge('bootanim','surfaceflinger')
G.edge['bootanim']['surfaceflinger']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('bootanim','system_app')
G.edge['bootanim']['system_app']['write-read'] = '[open open][write read]'
G.edge['bootanim']['system_app']['fill'] = 'red'
G.add_edge('bootanim','system_app')
G.edge['bootanim']['system_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('bootanim','wfd_app')
G.edge['bootanim']['wfd_app']['write-read'] = '[open open][write read]'
G.edge['bootanim']['wfd_app']['fill'] = 'red'
G.add_edge('bootanim','wfd_app')
G.edge['bootanim']['wfd_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('bootanim','wfdservice')
G.edge['bootanim']['wfdservice']['write-read'] = '[open open][write read]'
G.edge['bootanim']['wfdservice']['fill'] = 'red'
G.add_edge('bootanim','wfdservice')
G.edge['bootanim']['wfdservice']['write-read'] = '[open open][write read][append read]'
G.add_edge('bootanim','zygote')
G.edge['bootanim']['zygote']['write-read'] = '[open open][write read]'
G.edge['bootanim']['zygote']['fill'] = 'red'
G.add_edge('bootanim','zygote')
G.edge['bootanim']['zygote']['write-read'] = '[open open][write read][append read]'
G.add_edge('commonplatformappdomain','bintvoutservice')
G.edge['commonplatformappdomain']['bintvoutservice']['write-read'] = '[open open]'
G.add_edge('commonplatformappdomain','bootanim')
G.edge['commonplatformappdomain']['bootanim']['write-read'] = '[open open]'
G.add_edge('commonplatformappdomain','commonplatformappdomain')
G.edge['commonplatformappdomain']['commonplatformappdomain']['write-read'] = '[open open]'
G.add_edge('commonplatformappdomain','fixmo_app')
G.edge['commonplatformappdomain']['fixmo_app']['write-read'] = '[open open]'
G.add_edge('commonplatformappdomain','good_app')
G.edge['commonplatformappdomain']['good_app']['write-read'] = '[open open]'
G.add_edge('commonplatformappdomain','healthd')
G.edge['commonplatformappdomain']['healthd']['write-read'] = '[write read][append read][open open]'
G.add_edge('commonplatformappdomain','ime_app')
G.edge['commonplatformappdomain']['ime_app']['write-read'] = '[open open]'
G.add_edge('commonplatformappdomain','isolated_app')
G.edge['commonplatformappdomain']['isolated_app']['write-read'] = '[open open]'
G.add_edge('commonplatformappdomain','untrusted_app')
G.edge['commonplatformappdomain']['untrusted_app']['write-read'] = '[open open]'
G.add_edge('commonplatformappdomain','umcagent_app')
G.edge['commonplatformappdomain']['umcagent_app']['write-read'] = '[open open]'
G.add_edge('commonplatformappdomain','vpn_untrusted_app')
G.edge['commonplatformappdomain']['vpn_untrusted_app']['write-read'] = '[open open]'
G.add_edge('commonplatformappdomain','trustonicpartner_app')
G.edge['commonplatformappdomain']['trustonicpartner_app']['write-read'] = '[open open]'
G.add_edge('commonplatformappdomain','llk_untrusted_app')
G.edge['commonplatformappdomain']['llk_untrusted_app']['write-read'] = '[open open]'
G.add_edge('commonplatformappdomain','filtered_untrusted_app')
G.edge['commonplatformappdomain']['filtered_untrusted_app']['write-read'] = '[open open]'
G.add_edge('commonplatformappdomain','filtered_google_app')
G.edge['commonplatformappdomain']['filtered_google_app']['write-read'] = '[open open]'
G.add_edge('commonplatformappdomain','knox_untrusted_app')
G.edge['commonplatformappdomain']['knox_untrusted_app']['write-read'] = '[open open]'
G.add_edge('commonplatformappdomain','irm_app')
G.edge['commonplatformappdomain']['irm_app']['write-read'] = '[open open]'
G.add_edge('commonplatformappdomain','gad_untrusted_app')
G.edge['commonplatformappdomain']['gad_untrusted_app']['write-read'] = '[open open]'
G.add_edge('commonplatformappdomain','carrier_app')
G.edge['commonplatformappdomain']['carrier_app']['write-read'] = '[open open]'
G.add_edge('commonplatformappdomain','lpm')
G.edge['commonplatformappdomain']['lpm']['write-read'] = '[open open]'
G.add_edge('commonplatformappdomain','mmi')
G.edge['commonplatformappdomain']['mmi']['write-read'] = '[open open]'
G.add_edge('commonplatformappdomain','mm-pp-daemon')
G.edge['commonplatformappdomain']['mm-pp-daemon']['write-read'] = '[open open]'
G.add_edge('commonplatformappdomain','mm-qcamera-daemon')
G.edge['commonplatformappdomain']['mm-qcamera-daemon']['write-read'] = '[open open]'
G.add_edge('commonplatformappdomain','newAttr96')
G.edge['commonplatformappdomain']['newAttr96']['write-read'] = '[open open]'
G.add_edge('commonplatformappdomain','radio')
G.edge['commonplatformappdomain']['radio']['write-read'] = '[open open]'
G.add_edge('commonplatformappdomain','s_system_app')
G.edge['commonplatformappdomain']['s_system_app']['write-read'] = '[open open]'
G.add_edge('commonplatformappdomain','surfaceflinger')
G.edge['commonplatformappdomain']['surfaceflinger']['write-read'] = '[write read][append read][open open]'
G.add_edge('commonplatformappdomain','system_app')
G.edge['commonplatformappdomain']['system_app']['write-read'] = '[open open]'
G.add_edge('commonplatformappdomain','wfd_app')
G.edge['commonplatformappdomain']['wfd_app']['write-read'] = '[open open]'
G.add_edge('commonplatformappdomain','wfdservice')
G.edge['commonplatformappdomain']['wfdservice']['write-read'] = '[write read][append read][open open]'
G.add_edge('commonplatformappdomain','zygote')
G.edge['commonplatformappdomain']['zygote']['write-read'] = '[open open]'
G.add_edge('commonplatformappdomain','isolated_app')
G.edge['commonplatformappdomain']['isolated_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('commonplatformappdomain','untrusted_app')
G.edge['commonplatformappdomain']['untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('commonplatformappdomain','umcagent_app')
G.edge['commonplatformappdomain']['umcagent_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('commonplatformappdomain','vpn_untrusted_app')
G.edge['commonplatformappdomain']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('commonplatformappdomain','trustonicpartner_app')
G.edge['commonplatformappdomain']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('commonplatformappdomain','llk_untrusted_app')
G.edge['commonplatformappdomain']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('commonplatformappdomain','filtered_untrusted_app')
G.edge['commonplatformappdomain']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('commonplatformappdomain','filtered_google_app')
G.edge['commonplatformappdomain']['filtered_google_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('commonplatformappdomain','knox_untrusted_app')
G.edge['commonplatformappdomain']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('commonplatformappdomain','irm_app')
G.edge['commonplatformappdomain']['irm_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('commonplatformappdomain','gad_untrusted_app')
G.edge['commonplatformappdomain']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('commonplatformappdomain','carrier_app')
G.edge['commonplatformappdomain']['carrier_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('commonplatformappdomain','newAttr96')
G.edge['commonplatformappdomain']['newAttr96']['write-read'] = '[open open][setattr getattr]'
G.add_edge('commonplatformappdomain','bintvoutservice')
G.edge['commonplatformappdomain']['bintvoutservice']['write-read'] = '[open open][write read]'
G.edge['commonplatformappdomain']['bintvoutservice']['fill'] = 'red'
G.add_edge('commonplatformappdomain','bintvoutservice')
G.edge['commonplatformappdomain']['bintvoutservice']['write-read'] = '[open open][write read][append read]'
G.add_edge('commonplatformappdomain','bootanim')
G.edge['commonplatformappdomain']['bootanim']['write-read'] = '[open open][write read]'
G.edge['commonplatformappdomain']['bootanim']['fill'] = 'red'
G.add_edge('commonplatformappdomain','bootanim')
G.edge['commonplatformappdomain']['bootanim']['write-read'] = '[open open][write read][append read]'
G.add_edge('commonplatformappdomain','commonplatformappdomain')
G.edge['commonplatformappdomain']['commonplatformappdomain']['write-read'] = '[open open][write read]'
G.edge['commonplatformappdomain']['commonplatformappdomain']['fill'] = 'red'
G.add_edge('commonplatformappdomain','commonplatformappdomain')
G.edge['commonplatformappdomain']['commonplatformappdomain']['write-read'] = '[open open][write read][append read]'
G.add_edge('commonplatformappdomain','fixmo_app')
G.edge['commonplatformappdomain']['fixmo_app']['write-read'] = '[open open][write read]'
G.edge['commonplatformappdomain']['fixmo_app']['fill'] = 'red'
G.add_edge('commonplatformappdomain','fixmo_app')
G.edge['commonplatformappdomain']['fixmo_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('commonplatformappdomain','good_app')
G.edge['commonplatformappdomain']['good_app']['write-read'] = '[open open][write read]'
G.edge['commonplatformappdomain']['good_app']['fill'] = 'red'
G.add_edge('commonplatformappdomain','good_app')
G.edge['commonplatformappdomain']['good_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('commonplatformappdomain','healthd')
G.edge['commonplatformappdomain']['healthd']['write-read'] = '[write read][append read][open open][write read]'
G.edge['commonplatformappdomain']['healthd']['fill'] = 'red'
G.add_edge('commonplatformappdomain','healthd')
G.edge['commonplatformappdomain']['healthd']['write-read'] = '[write read][append read][open open][write read][append read]'
G.add_edge('commonplatformappdomain','ime_app')
G.edge['commonplatformappdomain']['ime_app']['write-read'] = '[open open][write read]'
G.edge['commonplatformappdomain']['ime_app']['fill'] = 'red'
G.add_edge('commonplatformappdomain','ime_app')
G.edge['commonplatformappdomain']['ime_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('commonplatformappdomain','isolated_app')
G.edge['commonplatformappdomain']['isolated_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('commonplatformappdomain','untrusted_app')
G.edge['commonplatformappdomain']['untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('commonplatformappdomain','umcagent_app')
G.edge['commonplatformappdomain']['umcagent_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('commonplatformappdomain','vpn_untrusted_app')
G.edge['commonplatformappdomain']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('commonplatformappdomain','trustonicpartner_app')
G.edge['commonplatformappdomain']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('commonplatformappdomain','llk_untrusted_app')
G.edge['commonplatformappdomain']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('commonplatformappdomain','filtered_untrusted_app')
G.edge['commonplatformappdomain']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('commonplatformappdomain','filtered_google_app')
G.edge['commonplatformappdomain']['filtered_google_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('commonplatformappdomain','knox_untrusted_app')
G.edge['commonplatformappdomain']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('commonplatformappdomain','irm_app')
G.edge['commonplatformappdomain']['irm_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('commonplatformappdomain','gad_untrusted_app')
G.edge['commonplatformappdomain']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('commonplatformappdomain','carrier_app')
G.edge['commonplatformappdomain']['carrier_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('commonplatformappdomain','lpm')
G.edge['commonplatformappdomain']['lpm']['write-read'] = '[open open][write read]'
G.edge['commonplatformappdomain']['lpm']['fill'] = 'red'
G.add_edge('commonplatformappdomain','lpm')
G.edge['commonplatformappdomain']['lpm']['write-read'] = '[open open][write read][append read]'
G.add_edge('commonplatformappdomain','mmi')
G.edge['commonplatformappdomain']['mmi']['write-read'] = '[open open][write read]'
G.edge['commonplatformappdomain']['mmi']['fill'] = 'red'
G.add_edge('commonplatformappdomain','mmi')
G.edge['commonplatformappdomain']['mmi']['write-read'] = '[open open][write read][append read]'
G.add_edge('commonplatformappdomain','mm-pp-daemon')
G.edge['commonplatformappdomain']['mm-pp-daemon']['write-read'] = '[open open][write read]'
G.edge['commonplatformappdomain']['mm-pp-daemon']['fill'] = 'red'
G.add_edge('commonplatformappdomain','mm-pp-daemon')
G.edge['commonplatformappdomain']['mm-pp-daemon']['write-read'] = '[open open][write read][append read]'
G.add_edge('commonplatformappdomain','mm-qcamera-daemon')
G.edge['commonplatformappdomain']['mm-qcamera-daemon']['write-read'] = '[open open][write read]'
G.edge['commonplatformappdomain']['mm-qcamera-daemon']['fill'] = 'red'
G.add_edge('commonplatformappdomain','mm-qcamera-daemon')
G.edge['commonplatformappdomain']['mm-qcamera-daemon']['write-read'] = '[open open][write read][append read]'
G.add_edge('commonplatformappdomain','newAttr96')
G.edge['commonplatformappdomain']['newAttr96']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['commonplatformappdomain']['newAttr96']['fill'] = 'red'
G.add_edge('commonplatformappdomain','newAttr96')
G.edge['commonplatformappdomain']['newAttr96']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('commonplatformappdomain','radio')
G.edge['commonplatformappdomain']['radio']['write-read'] = '[open open][write read]'
G.edge['commonplatformappdomain']['radio']['fill'] = 'red'
G.add_edge('commonplatformappdomain','radio')
G.edge['commonplatformappdomain']['radio']['write-read'] = '[open open][write read][append read]'
G.add_edge('commonplatformappdomain','s_system_app')
G.edge['commonplatformappdomain']['s_system_app']['write-read'] = '[open open][write read]'
G.edge['commonplatformappdomain']['s_system_app']['fill'] = 'red'
G.add_edge('commonplatformappdomain','s_system_app')
G.edge['commonplatformappdomain']['s_system_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('commonplatformappdomain','surfaceflinger')
G.edge['commonplatformappdomain']['surfaceflinger']['write-read'] = '[write read][append read][open open][write read]'
G.edge['commonplatformappdomain']['surfaceflinger']['fill'] = 'red'
G.add_edge('commonplatformappdomain','surfaceflinger')
G.edge['commonplatformappdomain']['surfaceflinger']['write-read'] = '[write read][append read][open open][write read][append read]'
G.add_edge('commonplatformappdomain','system_app')
G.edge['commonplatformappdomain']['system_app']['write-read'] = '[open open][write read]'
G.edge['commonplatformappdomain']['system_app']['fill'] = 'red'
G.add_edge('commonplatformappdomain','system_app')
G.edge['commonplatformappdomain']['system_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('commonplatformappdomain','wfd_app')
G.edge['commonplatformappdomain']['wfd_app']['write-read'] = '[open open][write read]'
G.edge['commonplatformappdomain']['wfd_app']['fill'] = 'red'
G.add_edge('commonplatformappdomain','wfd_app')
G.edge['commonplatformappdomain']['wfd_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('commonplatformappdomain','wfdservice')
G.edge['commonplatformappdomain']['wfdservice']['write-read'] = '[write read][append read][open open][write read]'
G.edge['commonplatformappdomain']['wfdservice']['fill'] = 'red'
G.add_edge('commonplatformappdomain','wfdservice')
G.edge['commonplatformappdomain']['wfdservice']['write-read'] = '[write read][append read][open open][write read][append read]'
G.add_edge('commonplatformappdomain','zygote')
G.edge['commonplatformappdomain']['zygote']['write-read'] = '[open open][write read]'
G.edge['commonplatformappdomain']['zygote']['fill'] = 'red'
G.add_edge('commonplatformappdomain','zygote')
G.edge['commonplatformappdomain']['zygote']['write-read'] = '[open open][write read][append read]'
G.add_edge('fixmo_app','bintvoutservice')
G.edge['fixmo_app']['bintvoutservice']['write-read'] = '[open open]'
G.add_edge('fixmo_app','bootanim')
G.edge['fixmo_app']['bootanim']['write-read'] = '[open open]'
G.add_edge('fixmo_app','commonplatformappdomain')
G.edge['fixmo_app']['commonplatformappdomain']['write-read'] = '[open open]'
G.add_edge('fixmo_app','fixmo_app')
G.edge['fixmo_app']['fixmo_app']['write-read'] = '[write read][setopt getopt][write read][setopt getopt][open open]'
G.add_edge('fixmo_app','good_app')
G.edge['fixmo_app']['good_app']['write-read'] = '[write read][setopt getopt][write read][setopt getopt][open open]'
G.add_edge('fixmo_app','healthd')
G.edge['fixmo_app']['healthd']['write-read'] = '[open open]'
G.add_edge('fixmo_app','ime_app')
G.edge['fixmo_app']['ime_app']['write-read'] = '[open open]'
G.add_edge('fixmo_app','isolated_app')
G.edge['fixmo_app']['isolated_app']['write-read'] = '[open open]'
G.add_edge('fixmo_app','untrusted_app')
G.edge['fixmo_app']['untrusted_app']['write-read'] = '[open open]'
G.add_edge('fixmo_app','umcagent_app')
G.edge['fixmo_app']['umcagent_app']['write-read'] = '[open open]'
G.add_edge('fixmo_app','vpn_untrusted_app')
G.edge['fixmo_app']['vpn_untrusted_app']['write-read'] = '[open open]'
G.add_edge('fixmo_app','trustonicpartner_app')
G.edge['fixmo_app']['trustonicpartner_app']['write-read'] = '[open open]'
G.add_edge('fixmo_app','llk_untrusted_app')
G.edge['fixmo_app']['llk_untrusted_app']['write-read'] = '[open open]'
G.add_edge('fixmo_app','filtered_untrusted_app')
G.edge['fixmo_app']['filtered_untrusted_app']['write-read'] = '[open open]'
G.add_edge('fixmo_app','filtered_google_app')
G.edge['fixmo_app']['filtered_google_app']['write-read'] = '[open open]'
G.add_edge('fixmo_app','knox_untrusted_app')
G.edge['fixmo_app']['knox_untrusted_app']['write-read'] = '[open open]'
G.add_edge('fixmo_app','irm_app')
G.edge['fixmo_app']['irm_app']['write-read'] = '[open open]'
G.add_edge('fixmo_app','gad_untrusted_app')
G.edge['fixmo_app']['gad_untrusted_app']['write-read'] = '[open open]'
G.add_edge('fixmo_app','carrier_app')
G.edge['fixmo_app']['carrier_app']['write-read'] = '[open open]'
G.add_edge('fixmo_app','lpm')
G.edge['fixmo_app']['lpm']['write-read'] = '[open open]'
G.add_edge('fixmo_app','mmi')
G.edge['fixmo_app']['mmi']['write-read'] = '[open open]'
G.add_edge('fixmo_app','mm-pp-daemon')
G.edge['fixmo_app']['mm-pp-daemon']['write-read'] = '[open open]'
G.add_edge('fixmo_app','mm-qcamera-daemon')
G.edge['fixmo_app']['mm-qcamera-daemon']['write-read'] = '[open open]'
G.add_edge('fixmo_app','newAttr96')
G.edge['fixmo_app']['newAttr96']['write-read'] = '[open open]'
G.add_edge('fixmo_app','radio')
G.edge['fixmo_app']['radio']['write-read'] = '[open open]'
G.add_edge('fixmo_app','s_system_app')
G.edge['fixmo_app']['s_system_app']['write-read'] = '[open open]'
G.add_edge('fixmo_app','surfaceflinger')
G.edge['fixmo_app']['surfaceflinger']['write-read'] = '[open open]'
G.add_edge('fixmo_app','system_app')
G.edge['fixmo_app']['system_app']['write-read'] = '[open open]'
G.add_edge('fixmo_app','wfd_app')
G.edge['fixmo_app']['wfd_app']['write-read'] = '[open open]'
G.add_edge('fixmo_app','wfdservice')
G.edge['fixmo_app']['wfdservice']['write-read'] = '[open open]'
G.add_edge('fixmo_app','zygote')
G.edge['fixmo_app']['zygote']['write-read'] = '[open open]'
G.add_edge('fixmo_app','isolated_app')
G.edge['fixmo_app']['isolated_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('fixmo_app','untrusted_app')
G.edge['fixmo_app']['untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('fixmo_app','umcagent_app')
G.edge['fixmo_app']['umcagent_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('fixmo_app','vpn_untrusted_app')
G.edge['fixmo_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('fixmo_app','trustonicpartner_app')
G.edge['fixmo_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('fixmo_app','llk_untrusted_app')
G.edge['fixmo_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('fixmo_app','filtered_untrusted_app')
G.edge['fixmo_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('fixmo_app','filtered_google_app')
G.edge['fixmo_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('fixmo_app','knox_untrusted_app')
G.edge['fixmo_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('fixmo_app','irm_app')
G.edge['fixmo_app']['irm_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('fixmo_app','gad_untrusted_app')
G.edge['fixmo_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('fixmo_app','carrier_app')
G.edge['fixmo_app']['carrier_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('fixmo_app','newAttr96')
G.edge['fixmo_app']['newAttr96']['write-read'] = '[open open][setattr getattr]'
G.add_edge('fixmo_app','bintvoutservice')
G.edge['fixmo_app']['bintvoutservice']['write-read'] = '[open open][write read]'
G.edge['fixmo_app']['bintvoutservice']['fill'] = 'red'
G.add_edge('fixmo_app','bintvoutservice')
G.edge['fixmo_app']['bintvoutservice']['write-read'] = '[open open][write read][append read]'
G.add_edge('fixmo_app','bootanim')
G.edge['fixmo_app']['bootanim']['write-read'] = '[open open][write read]'
G.edge['fixmo_app']['bootanim']['fill'] = 'red'
G.add_edge('fixmo_app','bootanim')
G.edge['fixmo_app']['bootanim']['write-read'] = '[open open][write read][append read]'
G.add_edge('fixmo_app','commonplatformappdomain')
G.edge['fixmo_app']['commonplatformappdomain']['write-read'] = '[open open][write read]'
G.edge['fixmo_app']['commonplatformappdomain']['fill'] = 'red'
G.add_edge('fixmo_app','commonplatformappdomain')
G.edge['fixmo_app']['commonplatformappdomain']['write-read'] = '[open open][write read][append read]'
G.add_edge('fixmo_app','fixmo_app')
G.edge['fixmo_app']['fixmo_app']['write-read'] = '[write read][setopt getopt][write read][setopt getopt][open open][write read]'
G.edge['fixmo_app']['fixmo_app']['fill'] = 'red'
G.add_edge('fixmo_app','fixmo_app')
G.edge['fixmo_app']['fixmo_app']['write-read'] = '[write read][setopt getopt][write read][setopt getopt][open open][write read][append read]'
G.add_edge('fixmo_app','good_app')
G.edge['fixmo_app']['good_app']['write-read'] = '[write read][setopt getopt][write read][setopt getopt][open open][write read]'
G.edge['fixmo_app']['good_app']['fill'] = 'red'
G.add_edge('fixmo_app','good_app')
G.edge['fixmo_app']['good_app']['write-read'] = '[write read][setopt getopt][write read][setopt getopt][open open][write read][append read]'
G.add_edge('fixmo_app','healthd')
G.edge['fixmo_app']['healthd']['write-read'] = '[open open][write read]'
G.edge['fixmo_app']['healthd']['fill'] = 'red'
G.add_edge('fixmo_app','healthd')
G.edge['fixmo_app']['healthd']['write-read'] = '[open open][write read][append read]'
G.add_edge('fixmo_app','ime_app')
G.edge['fixmo_app']['ime_app']['write-read'] = '[open open][write read]'
G.edge['fixmo_app']['ime_app']['fill'] = 'red'
G.add_edge('fixmo_app','ime_app')
G.edge['fixmo_app']['ime_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('fixmo_app','isolated_app')
G.edge['fixmo_app']['isolated_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('fixmo_app','untrusted_app')
G.edge['fixmo_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('fixmo_app','umcagent_app')
G.edge['fixmo_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('fixmo_app','vpn_untrusted_app')
G.edge['fixmo_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('fixmo_app','trustonicpartner_app')
G.edge['fixmo_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('fixmo_app','llk_untrusted_app')
G.edge['fixmo_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('fixmo_app','filtered_untrusted_app')
G.edge['fixmo_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('fixmo_app','filtered_google_app')
G.edge['fixmo_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('fixmo_app','knox_untrusted_app')
G.edge['fixmo_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('fixmo_app','irm_app')
G.edge['fixmo_app']['irm_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('fixmo_app','gad_untrusted_app')
G.edge['fixmo_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('fixmo_app','carrier_app')
G.edge['fixmo_app']['carrier_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('fixmo_app','lpm')
G.edge['fixmo_app']['lpm']['write-read'] = '[open open][write read]'
G.edge['fixmo_app']['lpm']['fill'] = 'red'
G.add_edge('fixmo_app','lpm')
G.edge['fixmo_app']['lpm']['write-read'] = '[open open][write read][append read]'
G.add_edge('fixmo_app','mmi')
G.edge['fixmo_app']['mmi']['write-read'] = '[open open][write read]'
G.edge['fixmo_app']['mmi']['fill'] = 'red'
G.add_edge('fixmo_app','mmi')
G.edge['fixmo_app']['mmi']['write-read'] = '[open open][write read][append read]'
G.add_edge('fixmo_app','mm-pp-daemon')
G.edge['fixmo_app']['mm-pp-daemon']['write-read'] = '[open open][write read]'
G.edge['fixmo_app']['mm-pp-daemon']['fill'] = 'red'
G.add_edge('fixmo_app','mm-pp-daemon')
G.edge['fixmo_app']['mm-pp-daemon']['write-read'] = '[open open][write read][append read]'
G.add_edge('fixmo_app','mm-qcamera-daemon')
G.edge['fixmo_app']['mm-qcamera-daemon']['write-read'] = '[open open][write read]'
G.edge['fixmo_app']['mm-qcamera-daemon']['fill'] = 'red'
G.add_edge('fixmo_app','mm-qcamera-daemon')
G.edge['fixmo_app']['mm-qcamera-daemon']['write-read'] = '[open open][write read][append read]'
G.add_edge('fixmo_app','newAttr96')
G.edge['fixmo_app']['newAttr96']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['fixmo_app']['newAttr96']['fill'] = 'red'
G.add_edge('fixmo_app','newAttr96')
G.edge['fixmo_app']['newAttr96']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('fixmo_app','radio')
G.edge['fixmo_app']['radio']['write-read'] = '[open open][write read]'
G.edge['fixmo_app']['radio']['fill'] = 'red'
G.add_edge('fixmo_app','radio')
G.edge['fixmo_app']['radio']['write-read'] = '[open open][write read][append read]'
G.add_edge('fixmo_app','s_system_app')
G.edge['fixmo_app']['s_system_app']['write-read'] = '[open open][write read]'
G.edge['fixmo_app']['s_system_app']['fill'] = 'red'
G.add_edge('fixmo_app','s_system_app')
G.edge['fixmo_app']['s_system_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('fixmo_app','surfaceflinger')
G.edge['fixmo_app']['surfaceflinger']['write-read'] = '[open open][write read]'
G.edge['fixmo_app']['surfaceflinger']['fill'] = 'red'
G.add_edge('fixmo_app','surfaceflinger')
G.edge['fixmo_app']['surfaceflinger']['write-read'] = '[open open][write read][append read]'
G.add_edge('fixmo_app','system_app')
G.edge['fixmo_app']['system_app']['write-read'] = '[open open][write read]'
G.edge['fixmo_app']['system_app']['fill'] = 'red'
G.add_edge('fixmo_app','system_app')
G.edge['fixmo_app']['system_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('fixmo_app','wfd_app')
G.edge['fixmo_app']['wfd_app']['write-read'] = '[open open][write read]'
G.edge['fixmo_app']['wfd_app']['fill'] = 'red'
G.add_edge('fixmo_app','wfd_app')
G.edge['fixmo_app']['wfd_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('fixmo_app','wfdservice')
G.edge['fixmo_app']['wfdservice']['write-read'] = '[open open][write read]'
G.edge['fixmo_app']['wfdservice']['fill'] = 'red'
G.add_edge('fixmo_app','wfdservice')
G.edge['fixmo_app']['wfdservice']['write-read'] = '[open open][write read][append read]'
G.add_edge('fixmo_app','zygote')
G.edge['fixmo_app']['zygote']['write-read'] = '[open open][write read]'
G.edge['fixmo_app']['zygote']['fill'] = 'red'
G.add_edge('fixmo_app','zygote')
G.edge['fixmo_app']['zygote']['write-read'] = '[open open][write read][append read]'
G.add_edge('good_app','bintvoutservice')
G.edge['good_app']['bintvoutservice']['write-read'] = '[open open]'
G.add_edge('good_app','bootanim')
G.edge['good_app']['bootanim']['write-read'] = '[open open]'
G.add_edge('good_app','commonplatformappdomain')
G.edge['good_app']['commonplatformappdomain']['write-read'] = '[open open]'
G.add_edge('good_app','fixmo_app')
G.edge['good_app']['fixmo_app']['write-read'] = '[write read][setopt getopt][write read][setopt getopt][open open]'
G.add_edge('good_app','good_app')
G.edge['good_app']['good_app']['write-read'] = '[write read][setopt getopt][write read][setopt getopt][setattr getattr][write read][append read][setopt getopt][open open]'
G.add_edge('good_app','healthd')
G.edge['good_app']['healthd']['write-read'] = '[open open]'
G.add_edge('good_app','ime_app')
G.edge['good_app']['ime_app']['write-read'] = '[open open]'
G.add_edge('good_app','isolated_app')
G.edge['good_app']['isolated_app']['write-read'] = '[open open]'
G.add_edge('good_app','untrusted_app')
G.edge['good_app']['untrusted_app']['write-read'] = '[open open]'
G.add_edge('good_app','umcagent_app')
G.edge['good_app']['umcagent_app']['write-read'] = '[open open]'
G.add_edge('good_app','vpn_untrusted_app')
G.edge['good_app']['vpn_untrusted_app']['write-read'] = '[open open]'
G.add_edge('good_app','trustonicpartner_app')
G.edge['good_app']['trustonicpartner_app']['write-read'] = '[open open]'
G.add_edge('good_app','llk_untrusted_app')
G.edge['good_app']['llk_untrusted_app']['write-read'] = '[open open]'
G.add_edge('good_app','filtered_untrusted_app')
G.edge['good_app']['filtered_untrusted_app']['write-read'] = '[open open]'
G.add_edge('good_app','filtered_google_app')
G.edge['good_app']['filtered_google_app']['write-read'] = '[open open]'
G.add_edge('good_app','knox_untrusted_app')
G.edge['good_app']['knox_untrusted_app']['write-read'] = '[open open]'
G.add_edge('good_app','irm_app')
G.edge['good_app']['irm_app']['write-read'] = '[open open]'
G.add_edge('good_app','gad_untrusted_app')
G.edge['good_app']['gad_untrusted_app']['write-read'] = '[open open]'
G.add_edge('good_app','carrier_app')
G.edge['good_app']['carrier_app']['write-read'] = '[open open]'
G.add_edge('good_app','lpm')
G.edge['good_app']['lpm']['write-read'] = '[open open]'
G.add_edge('good_app','mmi')
G.edge['good_app']['mmi']['write-read'] = '[open open]'
G.add_edge('good_app','mm-pp-daemon')
G.edge['good_app']['mm-pp-daemon']['write-read'] = '[open open]'
G.add_edge('good_app','mm-qcamera-daemon')
G.edge['good_app']['mm-qcamera-daemon']['write-read'] = '[open open]'
G.add_edge('good_app','newAttr96')
G.edge['good_app']['newAttr96']['write-read'] = '[open open]'
G.add_edge('good_app','radio')
G.edge['good_app']['radio']['write-read'] = '[open open]'
G.add_edge('good_app','s_system_app')
G.edge['good_app']['s_system_app']['write-read'] = '[open open]'
G.add_edge('good_app','surfaceflinger')
G.edge['good_app']['surfaceflinger']['write-read'] = '[open open]'
G.add_edge('good_app','system_app')
G.edge['good_app']['system_app']['write-read'] = '[open open]'
G.add_edge('good_app','wfd_app')
G.edge['good_app']['wfd_app']['write-read'] = '[open open]'
G.add_edge('good_app','wfdservice')
G.edge['good_app']['wfdservice']['write-read'] = '[open open]'
G.add_edge('good_app','zygote')
G.edge['good_app']['zygote']['write-read'] = '[open open]'
G.add_edge('good_app','isolated_app')
G.edge['good_app']['isolated_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('good_app','untrusted_app')
G.edge['good_app']['untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('good_app','umcagent_app')
G.edge['good_app']['umcagent_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('good_app','vpn_untrusted_app')
G.edge['good_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('good_app','trustonicpartner_app')
G.edge['good_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('good_app','llk_untrusted_app')
G.edge['good_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('good_app','filtered_untrusted_app')
G.edge['good_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('good_app','filtered_google_app')
G.edge['good_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('good_app','knox_untrusted_app')
G.edge['good_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('good_app','irm_app')
G.edge['good_app']['irm_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('good_app','gad_untrusted_app')
G.edge['good_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('good_app','carrier_app')
G.edge['good_app']['carrier_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('good_app','newAttr96')
G.edge['good_app']['newAttr96']['write-read'] = '[open open][setattr getattr]'
G.add_edge('good_app','bintvoutservice')
G.edge['good_app']['bintvoutservice']['write-read'] = '[open open][write read]'
G.edge['good_app']['bintvoutservice']['fill'] = 'red'
G.add_edge('good_app','bintvoutservice')
G.edge['good_app']['bintvoutservice']['write-read'] = '[open open][write read][append read]'
G.add_edge('good_app','bootanim')
G.edge['good_app']['bootanim']['write-read'] = '[open open][write read]'
G.edge['good_app']['bootanim']['fill'] = 'red'
G.add_edge('good_app','bootanim')
G.edge['good_app']['bootanim']['write-read'] = '[open open][write read][append read]'
G.add_edge('good_app','commonplatformappdomain')
G.edge['good_app']['commonplatformappdomain']['write-read'] = '[open open][write read]'
G.edge['good_app']['commonplatformappdomain']['fill'] = 'red'
G.add_edge('good_app','commonplatformappdomain')
G.edge['good_app']['commonplatformappdomain']['write-read'] = '[open open][write read][append read]'
G.add_edge('good_app','fixmo_app')
G.edge['good_app']['fixmo_app']['write-read'] = '[write read][setopt getopt][write read][setopt getopt][open open][write read]'
G.edge['good_app']['fixmo_app']['fill'] = 'red'
G.add_edge('good_app','fixmo_app')
G.edge['good_app']['fixmo_app']['write-read'] = '[write read][setopt getopt][write read][setopt getopt][open open][write read][append read]'
G.add_edge('good_app','good_app')
G.edge['good_app']['good_app']['write-read'] = '[write read][setopt getopt][write read][setopt getopt][setattr getattr][write read][append read][setopt getopt][open open][write read]'
G.edge['good_app']['good_app']['fill'] = 'red'
G.add_edge('good_app','good_app')
G.edge['good_app']['good_app']['write-read'] = '[write read][setopt getopt][write read][setopt getopt][setattr getattr][write read][append read][setopt getopt][open open][write read][append read]'
G.add_edge('good_app','healthd')
G.edge['good_app']['healthd']['write-read'] = '[open open][write read]'
G.edge['good_app']['healthd']['fill'] = 'red'
G.add_edge('good_app','healthd')
G.edge['good_app']['healthd']['write-read'] = '[open open][write read][append read]'
G.add_edge('good_app','ime_app')
G.edge['good_app']['ime_app']['write-read'] = '[open open][write read]'
G.edge['good_app']['ime_app']['fill'] = 'red'
G.add_edge('good_app','ime_app')
G.edge['good_app']['ime_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('good_app','isolated_app')
G.edge['good_app']['isolated_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('good_app','untrusted_app')
G.edge['good_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('good_app','umcagent_app')
G.edge['good_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('good_app','vpn_untrusted_app')
G.edge['good_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('good_app','trustonicpartner_app')
G.edge['good_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('good_app','llk_untrusted_app')
G.edge['good_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('good_app','filtered_untrusted_app')
G.edge['good_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('good_app','filtered_google_app')
G.edge['good_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('good_app','knox_untrusted_app')
G.edge['good_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('good_app','irm_app')
G.edge['good_app']['irm_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('good_app','gad_untrusted_app')
G.edge['good_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('good_app','carrier_app')
G.edge['good_app']['carrier_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('good_app','lpm')
G.edge['good_app']['lpm']['write-read'] = '[open open][write read]'
G.edge['good_app']['lpm']['fill'] = 'red'
G.add_edge('good_app','lpm')
G.edge['good_app']['lpm']['write-read'] = '[open open][write read][append read]'
G.add_edge('good_app','mmi')
G.edge['good_app']['mmi']['write-read'] = '[open open][write read]'
G.edge['good_app']['mmi']['fill'] = 'red'
G.add_edge('good_app','mmi')
G.edge['good_app']['mmi']['write-read'] = '[open open][write read][append read]'
G.add_edge('good_app','mm-pp-daemon')
G.edge['good_app']['mm-pp-daemon']['write-read'] = '[open open][write read]'
G.edge['good_app']['mm-pp-daemon']['fill'] = 'red'
G.add_edge('good_app','mm-pp-daemon')
G.edge['good_app']['mm-pp-daemon']['write-read'] = '[open open][write read][append read]'
G.add_edge('good_app','mm-qcamera-daemon')
G.edge['good_app']['mm-qcamera-daemon']['write-read'] = '[open open][write read]'
G.edge['good_app']['mm-qcamera-daemon']['fill'] = 'red'
G.add_edge('good_app','mm-qcamera-daemon')
G.edge['good_app']['mm-qcamera-daemon']['write-read'] = '[open open][write read][append read]'
G.add_edge('good_app','newAttr96')
G.edge['good_app']['newAttr96']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['good_app']['newAttr96']['fill'] = 'red'
G.add_edge('good_app','newAttr96')
G.edge['good_app']['newAttr96']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('good_app','radio')
G.edge['good_app']['radio']['write-read'] = '[open open][write read]'
G.edge['good_app']['radio']['fill'] = 'red'
G.add_edge('good_app','radio')
G.edge['good_app']['radio']['write-read'] = '[open open][write read][append read]'
G.add_edge('good_app','s_system_app')
G.edge['good_app']['s_system_app']['write-read'] = '[open open][write read]'
G.edge['good_app']['s_system_app']['fill'] = 'red'
G.add_edge('good_app','s_system_app')
G.edge['good_app']['s_system_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('good_app','surfaceflinger')
G.edge['good_app']['surfaceflinger']['write-read'] = '[open open][write read]'
G.edge['good_app']['surfaceflinger']['fill'] = 'red'
G.add_edge('good_app','surfaceflinger')
G.edge['good_app']['surfaceflinger']['write-read'] = '[open open][write read][append read]'
G.add_edge('good_app','system_app')
G.edge['good_app']['system_app']['write-read'] = '[open open][write read]'
G.edge['good_app']['system_app']['fill'] = 'red'
G.add_edge('good_app','system_app')
G.edge['good_app']['system_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('good_app','wfd_app')
G.edge['good_app']['wfd_app']['write-read'] = '[open open][write read]'
G.edge['good_app']['wfd_app']['fill'] = 'red'
G.add_edge('good_app','wfd_app')
G.edge['good_app']['wfd_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('good_app','wfdservice')
G.edge['good_app']['wfdservice']['write-read'] = '[open open][write read]'
G.edge['good_app']['wfdservice']['fill'] = 'red'
G.add_edge('good_app','wfdservice')
G.edge['good_app']['wfdservice']['write-read'] = '[open open][write read][append read]'
G.add_edge('good_app','zygote')
G.edge['good_app']['zygote']['write-read'] = '[open open][write read]'
G.edge['good_app']['zygote']['fill'] = 'red'
G.add_edge('good_app','zygote')
G.edge['good_app']['zygote']['write-read'] = '[open open][write read][append read]'
G.add_edge('healthd','bintvoutservice')
G.edge['healthd']['bintvoutservice']['write-read'] = '[open open]'
G.add_edge('healthd','bootanim')
G.edge['healthd']['bootanim']['write-read'] = '[open open]'
G.add_edge('healthd','commonplatformappdomain')
G.edge['healthd']['commonplatformappdomain']['write-read'] = '[setopt getopt][open open]'
G.add_edge('healthd','fixmo_app')
G.edge['healthd']['fixmo_app']['write-read'] = '[open open]'
G.add_edge('healthd','good_app')
G.edge['healthd']['good_app']['write-read'] = '[open open]'
G.add_edge('healthd','healthd')
G.edge['healthd']['healthd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open]'
G.add_edge('healthd','ime_app')
G.edge['healthd']['ime_app']['write-read'] = '[setattr getattr][setopt getopt][open open]'
G.add_edge('healthd','isolated_app')
G.edge['healthd']['isolated_app']['write-read'] = '[open open]'
G.add_edge('healthd','untrusted_app')
G.edge['healthd']['untrusted_app']['write-read'] = '[open open]'
G.add_edge('healthd','umcagent_app')
G.edge['healthd']['umcagent_app']['write-read'] = '[open open]'
G.add_edge('healthd','vpn_untrusted_app')
G.edge['healthd']['vpn_untrusted_app']['write-read'] = '[open open]'
G.add_edge('healthd','trustonicpartner_app')
G.edge['healthd']['trustonicpartner_app']['write-read'] = '[open open]'
G.add_edge('healthd','llk_untrusted_app')
G.edge['healthd']['llk_untrusted_app']['write-read'] = '[open open]'
G.add_edge('healthd','filtered_untrusted_app')
G.edge['healthd']['filtered_untrusted_app']['write-read'] = '[open open]'
G.add_edge('healthd','filtered_google_app')
G.edge['healthd']['filtered_google_app']['write-read'] = '[open open]'
G.add_edge('healthd','knox_untrusted_app')
G.edge['healthd']['knox_untrusted_app']['write-read'] = '[open open]'
G.add_edge('healthd','irm_app')
G.edge['healthd']['irm_app']['write-read'] = '[open open]'
G.add_edge('healthd','gad_untrusted_app')
G.edge['healthd']['gad_untrusted_app']['write-read'] = '[open open]'
G.add_edge('healthd','carrier_app')
G.edge['healthd']['carrier_app']['write-read'] = '[open open]'
G.add_edge('healthd','lpm')
G.edge['healthd']['lpm']['write-read'] = '[setopt getopt][open open]'
G.add_edge('healthd','mmi')
G.edge['healthd']['mmi']['write-read'] = '[open open]'
G.add_edge('healthd','mm-pp-daemon')
G.edge['healthd']['mm-pp-daemon']['write-read'] = '[open open]'
G.add_edge('healthd','mm-qcamera-daemon')
G.edge['healthd']['mm-qcamera-daemon']['write-read'] = '[open open]'
G.add_edge('healthd','newAttr96')
G.edge['healthd']['newAttr96']['write-read'] = '[open open]'
G.add_edge('healthd','radio')
G.edge['healthd']['radio']['write-read'] = '[open open]'
G.add_edge('healthd','s_system_app')
G.edge['healthd']['s_system_app']['write-read'] = '[setattr getattr][setopt getopt][open open]'
G.add_edge('healthd','surfaceflinger')
G.edge['healthd']['surfaceflinger']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open]'
G.add_edge('healthd','system_app')
G.edge['healthd']['system_app']['write-read'] = '[setattr getattr][setopt getopt][open open]'
G.add_edge('healthd','wfd_app')
G.edge['healthd']['wfd_app']['write-read'] = '[open open]'
G.add_edge('healthd','wfdservice')
G.edge['healthd']['wfdservice']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open]'
G.add_edge('healthd','zygote')
G.edge['healthd']['zygote']['write-read'] = '[open open]'
G.add_edge('healthd','isolated_app')
G.edge['healthd']['isolated_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('healthd','untrusted_app')
G.edge['healthd']['untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('healthd','umcagent_app')
G.edge['healthd']['umcagent_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('healthd','vpn_untrusted_app')
G.edge['healthd']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('healthd','trustonicpartner_app')
G.edge['healthd']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('healthd','llk_untrusted_app')
G.edge['healthd']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('healthd','filtered_untrusted_app')
G.edge['healthd']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('healthd','filtered_google_app')
G.edge['healthd']['filtered_google_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('healthd','knox_untrusted_app')
G.edge['healthd']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('healthd','irm_app')
G.edge['healthd']['irm_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('healthd','gad_untrusted_app')
G.edge['healthd']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('healthd','carrier_app')
G.edge['healthd']['carrier_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('healthd','newAttr96')
G.edge['healthd']['newAttr96']['write-read'] = '[open open][setattr getattr]'
G.add_edge('healthd','bintvoutservice')
G.edge['healthd']['bintvoutservice']['write-read'] = '[open open][write read]'
G.edge['healthd']['bintvoutservice']['fill'] = 'red'
G.add_edge('healthd','bintvoutservice')
G.edge['healthd']['bintvoutservice']['write-read'] = '[open open][write read][append read]'
G.add_edge('healthd','bootanim')
G.edge['healthd']['bootanim']['write-read'] = '[open open][write read]'
G.edge['healthd']['bootanim']['fill'] = 'red'
G.add_edge('healthd','bootanim')
G.edge['healthd']['bootanim']['write-read'] = '[open open][write read][append read]'
G.add_edge('healthd','commonplatformappdomain')
G.edge['healthd']['commonplatformappdomain']['write-read'] = '[setopt getopt][open open][write read]'
G.edge['healthd']['commonplatformappdomain']['fill'] = 'red'
G.add_edge('healthd','commonplatformappdomain')
G.edge['healthd']['commonplatformappdomain']['write-read'] = '[setopt getopt][open open][write read][append read]'
G.add_edge('healthd','fixmo_app')
G.edge['healthd']['fixmo_app']['write-read'] = '[open open][write read]'
G.edge['healthd']['fixmo_app']['fill'] = 'red'
G.add_edge('healthd','fixmo_app')
G.edge['healthd']['fixmo_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('healthd','good_app')
G.edge['healthd']['good_app']['write-read'] = '[open open][write read]'
G.edge['healthd']['good_app']['fill'] = 'red'
G.add_edge('healthd','good_app')
G.edge['healthd']['good_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('healthd','healthd')
G.edge['healthd']['healthd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read]'
G.edge['healthd']['healthd']['fill'] = 'red'
G.add_edge('healthd','healthd')
G.edge['healthd']['healthd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read]'
G.add_edge('healthd','ime_app')
G.edge['healthd']['ime_app']['write-read'] = '[setattr getattr][setopt getopt][open open][write read]'
G.edge['healthd']['ime_app']['fill'] = 'red'
G.add_edge('healthd','ime_app')
G.edge['healthd']['ime_app']['write-read'] = '[setattr getattr][setopt getopt][open open][write read][append read]'
G.add_edge('healthd','isolated_app')
G.edge['healthd']['isolated_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('healthd','untrusted_app')
G.edge['healthd']['untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('healthd','umcagent_app')
G.edge['healthd']['umcagent_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('healthd','vpn_untrusted_app')
G.edge['healthd']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('healthd','trustonicpartner_app')
G.edge['healthd']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('healthd','llk_untrusted_app')
G.edge['healthd']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('healthd','filtered_untrusted_app')
G.edge['healthd']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('healthd','filtered_google_app')
G.edge['healthd']['filtered_google_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('healthd','knox_untrusted_app')
G.edge['healthd']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('healthd','irm_app')
G.edge['healthd']['irm_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('healthd','gad_untrusted_app')
G.edge['healthd']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('healthd','carrier_app')
G.edge['healthd']['carrier_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('healthd','lpm')
G.edge['healthd']['lpm']['write-read'] = '[setopt getopt][open open][write read]'
G.edge['healthd']['lpm']['fill'] = 'red'
G.add_edge('healthd','lpm')
G.edge['healthd']['lpm']['write-read'] = '[setopt getopt][open open][write read][append read]'
G.add_edge('healthd','mmi')
G.edge['healthd']['mmi']['write-read'] = '[open open][write read]'
G.edge['healthd']['mmi']['fill'] = 'red'
G.add_edge('healthd','mmi')
G.edge['healthd']['mmi']['write-read'] = '[open open][write read][append read]'
G.add_edge('healthd','mm-pp-daemon')
G.edge['healthd']['mm-pp-daemon']['write-read'] = '[open open][write read]'
G.edge['healthd']['mm-pp-daemon']['fill'] = 'red'
G.add_edge('healthd','mm-pp-daemon')
G.edge['healthd']['mm-pp-daemon']['write-read'] = '[open open][write read][append read]'
G.add_edge('healthd','mm-qcamera-daemon')
G.edge['healthd']['mm-qcamera-daemon']['write-read'] = '[open open][write read]'
G.edge['healthd']['mm-qcamera-daemon']['fill'] = 'red'
G.add_edge('healthd','mm-qcamera-daemon')
G.edge['healthd']['mm-qcamera-daemon']['write-read'] = '[open open][write read][append read]'
G.add_edge('healthd','newAttr96')
G.edge['healthd']['newAttr96']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['healthd']['newAttr96']['fill'] = 'red'
G.add_edge('healthd','newAttr96')
G.edge['healthd']['newAttr96']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('healthd','radio')
G.edge['healthd']['radio']['write-read'] = '[open open][write read]'
G.edge['healthd']['radio']['fill'] = 'red'
G.add_edge('healthd','radio')
G.edge['healthd']['radio']['write-read'] = '[open open][write read][append read]'
G.add_edge('healthd','s_system_app')
G.edge['healthd']['s_system_app']['write-read'] = '[setattr getattr][setopt getopt][open open][write read]'
G.edge['healthd']['s_system_app']['fill'] = 'red'
G.add_edge('healthd','s_system_app')
G.edge['healthd']['s_system_app']['write-read'] = '[setattr getattr][setopt getopt][open open][write read][append read]'
G.add_edge('healthd','surfaceflinger')
G.edge['healthd']['surfaceflinger']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read]'
G.edge['healthd']['surfaceflinger']['fill'] = 'red'
G.add_edge('healthd','surfaceflinger')
G.edge['healthd']['surfaceflinger']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read]'
G.add_edge('healthd','system_app')
G.edge['healthd']['system_app']['write-read'] = '[setattr getattr][setopt getopt][open open][write read]'
G.edge['healthd']['system_app']['fill'] = 'red'
G.add_edge('healthd','system_app')
G.edge['healthd']['system_app']['write-read'] = '[setattr getattr][setopt getopt][open open][write read][append read]'
G.add_edge('healthd','wfd_app')
G.edge['healthd']['wfd_app']['write-read'] = '[open open][write read]'
G.edge['healthd']['wfd_app']['fill'] = 'red'
G.add_edge('healthd','wfd_app')
G.edge['healthd']['wfd_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('healthd','wfdservice')
G.edge['healthd']['wfdservice']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read]'
G.edge['healthd']['wfdservice']['fill'] = 'red'
G.add_edge('healthd','wfdservice')
G.edge['healthd']['wfdservice']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read]'
G.add_edge('healthd','zygote')
G.edge['healthd']['zygote']['write-read'] = '[open open][write read]'
G.edge['healthd']['zygote']['fill'] = 'red'
G.add_edge('healthd','zygote')
G.edge['healthd']['zygote']['write-read'] = '[open open][write read][append read]'
G.add_edge('ime_app','bintvoutservice')
G.edge['ime_app']['bintvoutservice']['write-read'] = '[open open]'
G.add_edge('ime_app','bootanim')
G.edge['ime_app']['bootanim']['write-read'] = '[open open]'
G.add_edge('ime_app','commonplatformappdomain')
G.edge['ime_app']['commonplatformappdomain']['write-read'] = '[setopt getopt][open open]'
G.add_edge('ime_app','fixmo_app')
G.edge['ime_app']['fixmo_app']['write-read'] = '[open open]'
G.add_edge('ime_app','good_app')
G.edge['ime_app']['good_app']['write-read'] = '[open open]'
G.add_edge('ime_app','healthd')
G.edge['ime_app']['healthd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open]'
G.add_edge('ime_app','ime_app')
G.edge['ime_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('ime_app','isolated_app')
G.edge['ime_app']['isolated_app']['write-read'] = '[open open]'
G.add_edge('ime_app','untrusted_app')
G.edge['ime_app']['untrusted_app']['write-read'] = '[open open]'
G.add_edge('ime_app','umcagent_app')
G.edge['ime_app']['umcagent_app']['write-read'] = '[open open]'
G.add_edge('ime_app','vpn_untrusted_app')
G.edge['ime_app']['vpn_untrusted_app']['write-read'] = '[open open]'
G.add_edge('ime_app','trustonicpartner_app')
G.edge['ime_app']['trustonicpartner_app']['write-read'] = '[open open]'
G.add_edge('ime_app','llk_untrusted_app')
G.edge['ime_app']['llk_untrusted_app']['write-read'] = '[open open]'
G.add_edge('ime_app','filtered_untrusted_app')
G.edge['ime_app']['filtered_untrusted_app']['write-read'] = '[open open]'
G.add_edge('ime_app','filtered_google_app')
G.edge['ime_app']['filtered_google_app']['write-read'] = '[open open]'
G.add_edge('ime_app','knox_untrusted_app')
G.edge['ime_app']['knox_untrusted_app']['write-read'] = '[open open]'
G.add_edge('ime_app','irm_app')
G.edge['ime_app']['irm_app']['write-read'] = '[open open]'
G.add_edge('ime_app','gad_untrusted_app')
G.edge['ime_app']['gad_untrusted_app']['write-read'] = '[open open]'
G.add_edge('ime_app','carrier_app')
G.edge['ime_app']['carrier_app']['write-read'] = '[open open]'
G.add_edge('ime_app','lpm')
G.edge['ime_app']['lpm']['write-read'] = '[setopt getopt][open open]'
G.add_edge('ime_app','mmi')
G.edge['ime_app']['mmi']['write-read'] = '[open open]'
G.add_edge('ime_app','mm-pp-daemon')
G.edge['ime_app']['mm-pp-daemon']['write-read'] = '[open open]'
G.add_edge('ime_app','mm-qcamera-daemon')
G.edge['ime_app']['mm-qcamera-daemon']['write-read'] = '[open open]'
G.add_edge('ime_app','newAttr96')
G.edge['ime_app']['newAttr96']['write-read'] = '[open open]'
G.add_edge('ime_app','radio')
G.edge['ime_app']['radio']['write-read'] = '[open open]'
G.add_edge('ime_app','s_system_app')
G.edge['ime_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('ime_app','surfaceflinger')
G.edge['ime_app']['surfaceflinger']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open]'
G.add_edge('ime_app','system_app')
G.edge['ime_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('ime_app','wfd_app')
G.edge['ime_app']['wfd_app']['write-read'] = '[open open]'
G.add_edge('ime_app','wfdservice')
G.edge['ime_app']['wfdservice']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open]'
G.add_edge('ime_app','zygote')
G.edge['ime_app']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('ime_app','isolated_app')
G.edge['ime_app']['isolated_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('ime_app','untrusted_app')
G.edge['ime_app']['untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('ime_app','umcagent_app')
G.edge['ime_app']['umcagent_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('ime_app','vpn_untrusted_app')
G.edge['ime_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('ime_app','trustonicpartner_app')
G.edge['ime_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('ime_app','llk_untrusted_app')
G.edge['ime_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('ime_app','filtered_untrusted_app')
G.edge['ime_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('ime_app','filtered_google_app')
G.edge['ime_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('ime_app','knox_untrusted_app')
G.edge['ime_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('ime_app','irm_app')
G.edge['ime_app']['irm_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('ime_app','gad_untrusted_app')
G.edge['ime_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('ime_app','carrier_app')
G.edge['ime_app']['carrier_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('ime_app','newAttr96')
G.edge['ime_app']['newAttr96']['write-read'] = '[open open][setattr getattr]'
G.add_edge('ime_app','bintvoutservice')
G.edge['ime_app']['bintvoutservice']['write-read'] = '[open open][write read]'
G.edge['ime_app']['bintvoutservice']['fill'] = 'red'
G.add_edge('ime_app','bintvoutservice')
G.edge['ime_app']['bintvoutservice']['write-read'] = '[open open][write read][append read]'
G.add_edge('ime_app','bootanim')
G.edge['ime_app']['bootanim']['write-read'] = '[open open][write read]'
G.edge['ime_app']['bootanim']['fill'] = 'red'
G.add_edge('ime_app','bootanim')
G.edge['ime_app']['bootanim']['write-read'] = '[open open][write read][append read]'
G.add_edge('ime_app','commonplatformappdomain')
G.edge['ime_app']['commonplatformappdomain']['write-read'] = '[setopt getopt][open open][write read]'
G.edge['ime_app']['commonplatformappdomain']['fill'] = 'red'
G.add_edge('ime_app','commonplatformappdomain')
G.edge['ime_app']['commonplatformappdomain']['write-read'] = '[setopt getopt][open open][write read][append read]'
G.add_edge('ime_app','fixmo_app')
G.edge['ime_app']['fixmo_app']['write-read'] = '[open open][write read]'
G.edge['ime_app']['fixmo_app']['fill'] = 'red'
G.add_edge('ime_app','fixmo_app')
G.edge['ime_app']['fixmo_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('ime_app','good_app')
G.edge['ime_app']['good_app']['write-read'] = '[open open][write read]'
G.edge['ime_app']['good_app']['fill'] = 'red'
G.add_edge('ime_app','good_app')
G.edge['ime_app']['good_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('ime_app','healthd')
G.edge['ime_app']['healthd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read]'
G.edge['ime_app']['healthd']['fill'] = 'red'
G.add_edge('ime_app','healthd')
G.edge['ime_app']['healthd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read]'
G.add_edge('ime_app','ime_app')
G.edge['ime_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['ime_app']['ime_app']['fill'] = 'red'
G.add_edge('ime_app','ime_app')
G.edge['ime_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('ime_app','isolated_app')
G.edge['ime_app']['isolated_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('ime_app','untrusted_app')
G.edge['ime_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('ime_app','umcagent_app')
G.edge['ime_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('ime_app','vpn_untrusted_app')
G.edge['ime_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('ime_app','trustonicpartner_app')
G.edge['ime_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('ime_app','llk_untrusted_app')
G.edge['ime_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('ime_app','filtered_untrusted_app')
G.edge['ime_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('ime_app','filtered_google_app')
G.edge['ime_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('ime_app','knox_untrusted_app')
G.edge['ime_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('ime_app','irm_app')
G.edge['ime_app']['irm_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('ime_app','gad_untrusted_app')
G.edge['ime_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('ime_app','carrier_app')
G.edge['ime_app']['carrier_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('ime_app','lpm')
G.edge['ime_app']['lpm']['write-read'] = '[setopt getopt][open open][write read]'
G.edge['ime_app']['lpm']['fill'] = 'red'
G.add_edge('ime_app','lpm')
G.edge['ime_app']['lpm']['write-read'] = '[setopt getopt][open open][write read][append read]'
G.add_edge('ime_app','mmi')
G.edge['ime_app']['mmi']['write-read'] = '[open open][write read]'
G.edge['ime_app']['mmi']['fill'] = 'red'
G.add_edge('ime_app','mmi')
G.edge['ime_app']['mmi']['write-read'] = '[open open][write read][append read]'
G.add_edge('ime_app','mm-pp-daemon')
G.edge['ime_app']['mm-pp-daemon']['write-read'] = '[open open][write read]'
G.edge['ime_app']['mm-pp-daemon']['fill'] = 'red'
G.add_edge('ime_app','mm-pp-daemon')
G.edge['ime_app']['mm-pp-daemon']['write-read'] = '[open open][write read][append read]'
G.add_edge('ime_app','mm-qcamera-daemon')
G.edge['ime_app']['mm-qcamera-daemon']['write-read'] = '[open open][write read]'
G.edge['ime_app']['mm-qcamera-daemon']['fill'] = 'red'
G.add_edge('ime_app','mm-qcamera-daemon')
G.edge['ime_app']['mm-qcamera-daemon']['write-read'] = '[open open][write read][append read]'
G.add_edge('ime_app','newAttr96')
G.edge['ime_app']['newAttr96']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['ime_app']['newAttr96']['fill'] = 'red'
G.add_edge('ime_app','newAttr96')
G.edge['ime_app']['newAttr96']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('ime_app','radio')
G.edge['ime_app']['radio']['write-read'] = '[open open][write read]'
G.edge['ime_app']['radio']['fill'] = 'red'
G.add_edge('ime_app','radio')
G.edge['ime_app']['radio']['write-read'] = '[open open][write read][append read]'
G.add_edge('ime_app','s_system_app')
G.edge['ime_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['ime_app']['s_system_app']['fill'] = 'red'
G.add_edge('ime_app','s_system_app')
G.edge['ime_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('ime_app','surfaceflinger')
G.edge['ime_app']['surfaceflinger']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read]'
G.edge['ime_app']['surfaceflinger']['fill'] = 'red'
G.add_edge('ime_app','surfaceflinger')
G.edge['ime_app']['surfaceflinger']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read]'
G.add_edge('ime_app','system_app')
G.edge['ime_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['ime_app']['system_app']['fill'] = 'red'
G.add_edge('ime_app','system_app')
G.edge['ime_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('ime_app','wfd_app')
G.edge['ime_app']['wfd_app']['write-read'] = '[open open][write read]'
G.edge['ime_app']['wfd_app']['fill'] = 'red'
G.add_edge('ime_app','wfd_app')
G.edge['ime_app']['wfd_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('ime_app','wfdservice')
G.edge['ime_app']['wfdservice']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read]'
G.edge['ime_app']['wfdservice']['fill'] = 'red'
G.add_edge('ime_app','wfdservice')
G.edge['ime_app']['wfdservice']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read]'
G.add_edge('ime_app','zygote')
G.edge['ime_app']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['ime_app']['zygote']['fill'] = 'red'
G.add_edge('ime_app','zygote')
G.edge['ime_app']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('isolated_app','bintvoutservice')
G.edge['isolated_app']['bintvoutservice']['write-read'] = '[open open]'
G.add_edge('isolated_app','bootanim')
G.edge['isolated_app']['bootanim']['write-read'] = '[open open]'
G.add_edge('isolated_app','commonplatformappdomain')
G.edge['isolated_app']['commonplatformappdomain']['write-read'] = '[open open]'
G.add_edge('isolated_app','fixmo_app')
G.edge['isolated_app']['fixmo_app']['write-read'] = '[open open]'
G.add_edge('isolated_app','good_app')
G.edge['isolated_app']['good_app']['write-read'] = '[open open]'
G.add_edge('isolated_app','healthd')
G.edge['isolated_app']['healthd']['write-read'] = '[open open]'
G.add_edge('isolated_app','ime_app')
G.edge['isolated_app']['ime_app']['write-read'] = '[open open]'
G.add_edge('isolated_app','isolated_app')
G.edge['isolated_app']['isolated_app']['write-read'] = '[open open]'
G.add_edge('isolated_app','untrusted_app')
G.edge['isolated_app']['untrusted_app']['write-read'] = '[open open]'
G.add_edge('isolated_app','umcagent_app')
G.edge['isolated_app']['umcagent_app']['write-read'] = '[open open]'
G.add_edge('isolated_app','vpn_untrusted_app')
G.edge['isolated_app']['vpn_untrusted_app']['write-read'] = '[open open]'
G.add_edge('isolated_app','trustonicpartner_app')
G.edge['isolated_app']['trustonicpartner_app']['write-read'] = '[open open]'
G.add_edge('isolated_app','llk_untrusted_app')
G.edge['isolated_app']['llk_untrusted_app']['write-read'] = '[open open]'
G.add_edge('isolated_app','filtered_untrusted_app')
G.edge['isolated_app']['filtered_untrusted_app']['write-read'] = '[open open]'
G.add_edge('isolated_app','filtered_google_app')
G.edge['isolated_app']['filtered_google_app']['write-read'] = '[open open]'
G.add_edge('isolated_app','knox_untrusted_app')
G.edge['isolated_app']['knox_untrusted_app']['write-read'] = '[open open]'
G.add_edge('isolated_app','irm_app')
G.edge['isolated_app']['irm_app']['write-read'] = '[open open]'
G.add_edge('isolated_app','gad_untrusted_app')
G.edge['isolated_app']['gad_untrusted_app']['write-read'] = '[open open]'
G.add_edge('isolated_app','carrier_app')
G.edge['isolated_app']['carrier_app']['write-read'] = '[open open]'
G.add_edge('isolated_app','lpm')
G.edge['isolated_app']['lpm']['write-read'] = '[open open]'
G.add_edge('isolated_app','mmi')
G.edge['isolated_app']['mmi']['write-read'] = '[open open]'
G.add_edge('isolated_app','mm-pp-daemon')
G.edge['isolated_app']['mm-pp-daemon']['write-read'] = '[open open]'
G.add_edge('isolated_app','mm-qcamera-daemon')
G.edge['isolated_app']['mm-qcamera-daemon']['write-read'] = '[open open]'
G.add_edge('isolated_app','newAttr96')
G.edge['isolated_app']['newAttr96']['write-read'] = '[open open]'
G.add_edge('isolated_app','radio')
G.edge['isolated_app']['radio']['write-read'] = '[open open]'
G.add_edge('isolated_app','s_system_app')
G.edge['isolated_app']['s_system_app']['write-read'] = '[open open]'
G.add_edge('isolated_app','surfaceflinger')
G.edge['isolated_app']['surfaceflinger']['write-read'] = '[open open]'
G.add_edge('isolated_app','system_app')
G.edge['isolated_app']['system_app']['write-read'] = '[open open]'
G.add_edge('isolated_app','wfd_app')
G.edge['isolated_app']['wfd_app']['write-read'] = '[open open]'
G.add_edge('isolated_app','wfdservice')
G.edge['isolated_app']['wfdservice']['write-read'] = '[open open]'
G.add_edge('isolated_app','zygote')
G.edge['isolated_app']['zygote']['write-read'] = '[open open]'
G.add_edge('isolated_app','isolated_app')
G.edge['isolated_app']['isolated_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('isolated_app','untrusted_app')
G.edge['isolated_app']['untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('isolated_app','umcagent_app')
G.edge['isolated_app']['umcagent_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('isolated_app','vpn_untrusted_app')
G.edge['isolated_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('isolated_app','trustonicpartner_app')
G.edge['isolated_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('isolated_app','llk_untrusted_app')
G.edge['isolated_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('isolated_app','filtered_untrusted_app')
G.edge['isolated_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('isolated_app','filtered_google_app')
G.edge['isolated_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('isolated_app','knox_untrusted_app')
G.edge['isolated_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('isolated_app','irm_app')
G.edge['isolated_app']['irm_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('isolated_app','gad_untrusted_app')
G.edge['isolated_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('isolated_app','carrier_app')
G.edge['isolated_app']['carrier_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('isolated_app','newAttr96')
G.edge['isolated_app']['newAttr96']['write-read'] = '[open open][setattr getattr]'
G.add_edge('untrusted_app','bintvoutservice')
G.edge['untrusted_app']['bintvoutservice']['write-read'] = '[open open]'
G.add_edge('untrusted_app','bootanim')
G.edge['untrusted_app']['bootanim']['write-read'] = '[open open]'
G.add_edge('untrusted_app','commonplatformappdomain')
G.edge['untrusted_app']['commonplatformappdomain']['write-read'] = '[open open]'
G.add_edge('untrusted_app','fixmo_app')
G.edge['untrusted_app']['fixmo_app']['write-read'] = '[open open]'
G.add_edge('untrusted_app','good_app')
G.edge['untrusted_app']['good_app']['write-read'] = '[open open]'
G.add_edge('untrusted_app','healthd')
G.edge['untrusted_app']['healthd']['write-read'] = '[open open]'
G.add_edge('untrusted_app','ime_app')
G.edge['untrusted_app']['ime_app']['write-read'] = '[open open]'
G.add_edge('untrusted_app','isolated_app')
G.edge['untrusted_app']['isolated_app']['write-read'] = '[open open]'
G.add_edge('untrusted_app','untrusted_app')
G.edge['untrusted_app']['untrusted_app']['write-read'] = '[open open]'
G.add_edge('untrusted_app','umcagent_app')
G.edge['untrusted_app']['umcagent_app']['write-read'] = '[open open]'
G.add_edge('untrusted_app','vpn_untrusted_app')
G.edge['untrusted_app']['vpn_untrusted_app']['write-read'] = '[open open]'
G.add_edge('untrusted_app','trustonicpartner_app')
G.edge['untrusted_app']['trustonicpartner_app']['write-read'] = '[open open]'
G.add_edge('untrusted_app','llk_untrusted_app')
G.edge['untrusted_app']['llk_untrusted_app']['write-read'] = '[open open]'
G.add_edge('untrusted_app','filtered_untrusted_app')
G.edge['untrusted_app']['filtered_untrusted_app']['write-read'] = '[open open]'
G.add_edge('untrusted_app','filtered_google_app')
G.edge['untrusted_app']['filtered_google_app']['write-read'] = '[open open]'
G.add_edge('untrusted_app','knox_untrusted_app')
G.edge['untrusted_app']['knox_untrusted_app']['write-read'] = '[open open]'
G.add_edge('untrusted_app','irm_app')
G.edge['untrusted_app']['irm_app']['write-read'] = '[open open]'
G.add_edge('untrusted_app','gad_untrusted_app')
G.edge['untrusted_app']['gad_untrusted_app']['write-read'] = '[open open]'
G.add_edge('untrusted_app','carrier_app')
G.edge['untrusted_app']['carrier_app']['write-read'] = '[open open]'
G.add_edge('untrusted_app','lpm')
G.edge['untrusted_app']['lpm']['write-read'] = '[open open]'
G.add_edge('untrusted_app','mmi')
G.edge['untrusted_app']['mmi']['write-read'] = '[open open]'
G.add_edge('untrusted_app','mm-pp-daemon')
G.edge['untrusted_app']['mm-pp-daemon']['write-read'] = '[open open]'
G.add_edge('untrusted_app','mm-qcamera-daemon')
G.edge['untrusted_app']['mm-qcamera-daemon']['write-read'] = '[open open]'
G.add_edge('untrusted_app','newAttr96')
G.edge['untrusted_app']['newAttr96']['write-read'] = '[open open]'
G.add_edge('untrusted_app','radio')
G.edge['untrusted_app']['radio']['write-read'] = '[open open]'
G.add_edge('untrusted_app','s_system_app')
G.edge['untrusted_app']['s_system_app']['write-read'] = '[open open]'
G.add_edge('untrusted_app','surfaceflinger')
G.edge['untrusted_app']['surfaceflinger']['write-read'] = '[open open]'
G.add_edge('untrusted_app','system_app')
G.edge['untrusted_app']['system_app']['write-read'] = '[open open]'
G.add_edge('untrusted_app','wfd_app')
G.edge['untrusted_app']['wfd_app']['write-read'] = '[open open]'
G.add_edge('untrusted_app','wfdservice')
G.edge['untrusted_app']['wfdservice']['write-read'] = '[open open]'
G.add_edge('untrusted_app','zygote')
G.edge['untrusted_app']['zygote']['write-read'] = '[open open]'
G.add_edge('untrusted_app','isolated_app')
G.edge['untrusted_app']['isolated_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('untrusted_app','untrusted_app')
G.edge['untrusted_app']['untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('untrusted_app','umcagent_app')
G.edge['untrusted_app']['umcagent_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('untrusted_app','vpn_untrusted_app')
G.edge['untrusted_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('untrusted_app','trustonicpartner_app')
G.edge['untrusted_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('untrusted_app','llk_untrusted_app')
G.edge['untrusted_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('untrusted_app','filtered_untrusted_app')
G.edge['untrusted_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('untrusted_app','filtered_google_app')
G.edge['untrusted_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('untrusted_app','knox_untrusted_app')
G.edge['untrusted_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('untrusted_app','irm_app')
G.edge['untrusted_app']['irm_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('untrusted_app','gad_untrusted_app')
G.edge['untrusted_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('untrusted_app','carrier_app')
G.edge['untrusted_app']['carrier_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('untrusted_app','newAttr96')
G.edge['untrusted_app']['newAttr96']['write-read'] = '[open open][setattr getattr]'
G.add_edge('umcagent_app','bintvoutservice')
G.edge['umcagent_app']['bintvoutservice']['write-read'] = '[open open]'
G.add_edge('umcagent_app','bootanim')
G.edge['umcagent_app']['bootanim']['write-read'] = '[open open]'
G.add_edge('umcagent_app','commonplatformappdomain')
G.edge['umcagent_app']['commonplatformappdomain']['write-read'] = '[open open]'
G.add_edge('umcagent_app','fixmo_app')
G.edge['umcagent_app']['fixmo_app']['write-read'] = '[open open]'
G.add_edge('umcagent_app','good_app')
G.edge['umcagent_app']['good_app']['write-read'] = '[open open]'
G.add_edge('umcagent_app','healthd')
G.edge['umcagent_app']['healthd']['write-read'] = '[open open]'
G.add_edge('umcagent_app','ime_app')
G.edge['umcagent_app']['ime_app']['write-read'] = '[open open]'
G.add_edge('umcagent_app','isolated_app')
G.edge['umcagent_app']['isolated_app']['write-read'] = '[open open]'
G.add_edge('umcagent_app','untrusted_app')
G.edge['umcagent_app']['untrusted_app']['write-read'] = '[open open]'
G.add_edge('umcagent_app','umcagent_app')
G.edge['umcagent_app']['umcagent_app']['write-read'] = '[open open]'
G.add_edge('umcagent_app','vpn_untrusted_app')
G.edge['umcagent_app']['vpn_untrusted_app']['write-read'] = '[open open]'
G.add_edge('umcagent_app','trustonicpartner_app')
G.edge['umcagent_app']['trustonicpartner_app']['write-read'] = '[open open]'
G.add_edge('umcagent_app','llk_untrusted_app')
G.edge['umcagent_app']['llk_untrusted_app']['write-read'] = '[open open]'
G.add_edge('umcagent_app','filtered_untrusted_app')
G.edge['umcagent_app']['filtered_untrusted_app']['write-read'] = '[open open]'
G.add_edge('umcagent_app','filtered_google_app')
G.edge['umcagent_app']['filtered_google_app']['write-read'] = '[open open]'
G.add_edge('umcagent_app','knox_untrusted_app')
G.edge['umcagent_app']['knox_untrusted_app']['write-read'] = '[open open]'
G.add_edge('umcagent_app','irm_app')
G.edge['umcagent_app']['irm_app']['write-read'] = '[open open]'
G.add_edge('umcagent_app','gad_untrusted_app')
G.edge['umcagent_app']['gad_untrusted_app']['write-read'] = '[open open]'
G.add_edge('umcagent_app','carrier_app')
G.edge['umcagent_app']['carrier_app']['write-read'] = '[open open]'
G.add_edge('umcagent_app','lpm')
G.edge['umcagent_app']['lpm']['write-read'] = '[open open]'
G.add_edge('umcagent_app','mmi')
G.edge['umcagent_app']['mmi']['write-read'] = '[open open]'
G.add_edge('umcagent_app','mm-pp-daemon')
G.edge['umcagent_app']['mm-pp-daemon']['write-read'] = '[open open]'
G.add_edge('umcagent_app','mm-qcamera-daemon')
G.edge['umcagent_app']['mm-qcamera-daemon']['write-read'] = '[open open]'
G.add_edge('umcagent_app','newAttr96')
G.edge['umcagent_app']['newAttr96']['write-read'] = '[open open]'
G.add_edge('umcagent_app','radio')
G.edge['umcagent_app']['radio']['write-read'] = '[open open]'
G.add_edge('umcagent_app','s_system_app')
G.edge['umcagent_app']['s_system_app']['write-read'] = '[open open]'
G.add_edge('umcagent_app','surfaceflinger')
G.edge['umcagent_app']['surfaceflinger']['write-read'] = '[open open]'
G.add_edge('umcagent_app','system_app')
G.edge['umcagent_app']['system_app']['write-read'] = '[open open]'
G.add_edge('umcagent_app','wfd_app')
G.edge['umcagent_app']['wfd_app']['write-read'] = '[open open]'
G.add_edge('umcagent_app','wfdservice')
G.edge['umcagent_app']['wfdservice']['write-read'] = '[open open]'
G.add_edge('umcagent_app','zygote')
G.edge['umcagent_app']['zygote']['write-read'] = '[open open]'
G.add_edge('umcagent_app','isolated_app')
G.edge['umcagent_app']['isolated_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('umcagent_app','untrusted_app')
G.edge['umcagent_app']['untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('umcagent_app','umcagent_app')
G.edge['umcagent_app']['umcagent_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('umcagent_app','vpn_untrusted_app')
G.edge['umcagent_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('umcagent_app','trustonicpartner_app')
G.edge['umcagent_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('umcagent_app','llk_untrusted_app')
G.edge['umcagent_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('umcagent_app','filtered_untrusted_app')
G.edge['umcagent_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('umcagent_app','filtered_google_app')
G.edge['umcagent_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('umcagent_app','knox_untrusted_app')
G.edge['umcagent_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('umcagent_app','irm_app')
G.edge['umcagent_app']['irm_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('umcagent_app','gad_untrusted_app')
G.edge['umcagent_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('umcagent_app','carrier_app')
G.edge['umcagent_app']['carrier_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('umcagent_app','newAttr96')
G.edge['umcagent_app']['newAttr96']['write-read'] = '[open open][setattr getattr]'
G.add_edge('vpn_untrusted_app','bintvoutservice')
G.edge['vpn_untrusted_app']['bintvoutservice']['write-read'] = '[open open]'
G.add_edge('vpn_untrusted_app','bootanim')
G.edge['vpn_untrusted_app']['bootanim']['write-read'] = '[open open]'
G.add_edge('vpn_untrusted_app','commonplatformappdomain')
G.edge['vpn_untrusted_app']['commonplatformappdomain']['write-read'] = '[open open]'
G.add_edge('vpn_untrusted_app','fixmo_app')
G.edge['vpn_untrusted_app']['fixmo_app']['write-read'] = '[open open]'
G.add_edge('vpn_untrusted_app','good_app')
G.edge['vpn_untrusted_app']['good_app']['write-read'] = '[open open]'
G.add_edge('vpn_untrusted_app','healthd')
G.edge['vpn_untrusted_app']['healthd']['write-read'] = '[open open]'
G.add_edge('vpn_untrusted_app','ime_app')
G.edge['vpn_untrusted_app']['ime_app']['write-read'] = '[open open]'
G.add_edge('vpn_untrusted_app','isolated_app')
G.edge['vpn_untrusted_app']['isolated_app']['write-read'] = '[open open]'
G.add_edge('vpn_untrusted_app','untrusted_app')
G.edge['vpn_untrusted_app']['untrusted_app']['write-read'] = '[open open]'
G.add_edge('vpn_untrusted_app','umcagent_app')
G.edge['vpn_untrusted_app']['umcagent_app']['write-read'] = '[open open]'
G.add_edge('vpn_untrusted_app','vpn_untrusted_app')
G.edge['vpn_untrusted_app']['vpn_untrusted_app']['write-read'] = '[open open]'
G.add_edge('vpn_untrusted_app','trustonicpartner_app')
G.edge['vpn_untrusted_app']['trustonicpartner_app']['write-read'] = '[open open]'
G.add_edge('vpn_untrusted_app','llk_untrusted_app')
G.edge['vpn_untrusted_app']['llk_untrusted_app']['write-read'] = '[open open]'
G.add_edge('vpn_untrusted_app','filtered_untrusted_app')
G.edge['vpn_untrusted_app']['filtered_untrusted_app']['write-read'] = '[open open]'
G.add_edge('vpn_untrusted_app','filtered_google_app')
G.edge['vpn_untrusted_app']['filtered_google_app']['write-read'] = '[open open]'
G.add_edge('vpn_untrusted_app','knox_untrusted_app')
G.edge['vpn_untrusted_app']['knox_untrusted_app']['write-read'] = '[open open]'
G.add_edge('vpn_untrusted_app','irm_app')
G.edge['vpn_untrusted_app']['irm_app']['write-read'] = '[open open]'
G.add_edge('vpn_untrusted_app','gad_untrusted_app')
G.edge['vpn_untrusted_app']['gad_untrusted_app']['write-read'] = '[open open]'
G.add_edge('vpn_untrusted_app','carrier_app')
G.edge['vpn_untrusted_app']['carrier_app']['write-read'] = '[open open]'
G.add_edge('vpn_untrusted_app','lpm')
G.edge['vpn_untrusted_app']['lpm']['write-read'] = '[open open]'
G.add_edge('vpn_untrusted_app','mmi')
G.edge['vpn_untrusted_app']['mmi']['write-read'] = '[open open]'
G.add_edge('vpn_untrusted_app','mm-pp-daemon')
G.edge['vpn_untrusted_app']['mm-pp-daemon']['write-read'] = '[open open]'
G.add_edge('vpn_untrusted_app','mm-qcamera-daemon')
G.edge['vpn_untrusted_app']['mm-qcamera-daemon']['write-read'] = '[open open]'
G.add_edge('vpn_untrusted_app','newAttr96')
G.edge['vpn_untrusted_app']['newAttr96']['write-read'] = '[open open]'
G.add_edge('vpn_untrusted_app','radio')
G.edge['vpn_untrusted_app']['radio']['write-read'] = '[open open]'
G.add_edge('vpn_untrusted_app','s_system_app')
G.edge['vpn_untrusted_app']['s_system_app']['write-read'] = '[open open]'
G.add_edge('vpn_untrusted_app','surfaceflinger')
G.edge['vpn_untrusted_app']['surfaceflinger']['write-read'] = '[open open]'
G.add_edge('vpn_untrusted_app','system_app')
G.edge['vpn_untrusted_app']['system_app']['write-read'] = '[open open]'
G.add_edge('vpn_untrusted_app','wfd_app')
G.edge['vpn_untrusted_app']['wfd_app']['write-read'] = '[open open]'
G.add_edge('vpn_untrusted_app','wfdservice')
G.edge['vpn_untrusted_app']['wfdservice']['write-read'] = '[open open]'
G.add_edge('vpn_untrusted_app','zygote')
G.edge['vpn_untrusted_app']['zygote']['write-read'] = '[open open]'
G.add_edge('vpn_untrusted_app','isolated_app')
G.edge['vpn_untrusted_app']['isolated_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('vpn_untrusted_app','untrusted_app')
G.edge['vpn_untrusted_app']['untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('vpn_untrusted_app','umcagent_app')
G.edge['vpn_untrusted_app']['umcagent_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('vpn_untrusted_app','vpn_untrusted_app')
G.edge['vpn_untrusted_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('vpn_untrusted_app','trustonicpartner_app')
G.edge['vpn_untrusted_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('vpn_untrusted_app','llk_untrusted_app')
G.edge['vpn_untrusted_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('vpn_untrusted_app','filtered_untrusted_app')
G.edge['vpn_untrusted_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('vpn_untrusted_app','filtered_google_app')
G.edge['vpn_untrusted_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('vpn_untrusted_app','knox_untrusted_app')
G.edge['vpn_untrusted_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('vpn_untrusted_app','irm_app')
G.edge['vpn_untrusted_app']['irm_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('vpn_untrusted_app','gad_untrusted_app')
G.edge['vpn_untrusted_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('vpn_untrusted_app','carrier_app')
G.edge['vpn_untrusted_app']['carrier_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('vpn_untrusted_app','newAttr96')
G.edge['vpn_untrusted_app']['newAttr96']['write-read'] = '[open open][setattr getattr]'
G.add_edge('trustonicpartner_app','bintvoutservice')
G.edge['trustonicpartner_app']['bintvoutservice']['write-read'] = '[open open]'
G.add_edge('trustonicpartner_app','bootanim')
G.edge['trustonicpartner_app']['bootanim']['write-read'] = '[open open]'
G.add_edge('trustonicpartner_app','commonplatformappdomain')
G.edge['trustonicpartner_app']['commonplatformappdomain']['write-read'] = '[open open]'
G.add_edge('trustonicpartner_app','fixmo_app')
G.edge['trustonicpartner_app']['fixmo_app']['write-read'] = '[open open]'
G.add_edge('trustonicpartner_app','good_app')
G.edge['trustonicpartner_app']['good_app']['write-read'] = '[open open]'
G.add_edge('trustonicpartner_app','healthd')
G.edge['trustonicpartner_app']['healthd']['write-read'] = '[open open]'
G.add_edge('trustonicpartner_app','ime_app')
G.edge['trustonicpartner_app']['ime_app']['write-read'] = '[open open]'
G.add_edge('trustonicpartner_app','isolated_app')
G.edge['trustonicpartner_app']['isolated_app']['write-read'] = '[open open]'
G.add_edge('trustonicpartner_app','untrusted_app')
G.edge['trustonicpartner_app']['untrusted_app']['write-read'] = '[open open]'
G.add_edge('trustonicpartner_app','umcagent_app')
G.edge['trustonicpartner_app']['umcagent_app']['write-read'] = '[open open]'
G.add_edge('trustonicpartner_app','vpn_untrusted_app')
G.edge['trustonicpartner_app']['vpn_untrusted_app']['write-read'] = '[open open]'
G.add_edge('trustonicpartner_app','trustonicpartner_app')
G.edge['trustonicpartner_app']['trustonicpartner_app']['write-read'] = '[open open]'
G.add_edge('trustonicpartner_app','llk_untrusted_app')
G.edge['trustonicpartner_app']['llk_untrusted_app']['write-read'] = '[open open]'
G.add_edge('trustonicpartner_app','filtered_untrusted_app')
G.edge['trustonicpartner_app']['filtered_untrusted_app']['write-read'] = '[open open]'
G.add_edge('trustonicpartner_app','filtered_google_app')
G.edge['trustonicpartner_app']['filtered_google_app']['write-read'] = '[open open]'
G.add_edge('trustonicpartner_app','knox_untrusted_app')
G.edge['trustonicpartner_app']['knox_untrusted_app']['write-read'] = '[open open]'
G.add_edge('trustonicpartner_app','irm_app')
G.edge['trustonicpartner_app']['irm_app']['write-read'] = '[open open]'
G.add_edge('trustonicpartner_app','gad_untrusted_app')
G.edge['trustonicpartner_app']['gad_untrusted_app']['write-read'] = '[open open]'
G.add_edge('trustonicpartner_app','carrier_app')
G.edge['trustonicpartner_app']['carrier_app']['write-read'] = '[open open]'
G.add_edge('trustonicpartner_app','lpm')
G.edge['trustonicpartner_app']['lpm']['write-read'] = '[open open]'
G.add_edge('trustonicpartner_app','mmi')
G.edge['trustonicpartner_app']['mmi']['write-read'] = '[open open]'
G.add_edge('trustonicpartner_app','mm-pp-daemon')
G.edge['trustonicpartner_app']['mm-pp-daemon']['write-read'] = '[open open]'
G.add_edge('trustonicpartner_app','mm-qcamera-daemon')
G.edge['trustonicpartner_app']['mm-qcamera-daemon']['write-read'] = '[open open]'
G.add_edge('trustonicpartner_app','newAttr96')
G.edge['trustonicpartner_app']['newAttr96']['write-read'] = '[open open]'
G.add_edge('trustonicpartner_app','radio')
G.edge['trustonicpartner_app']['radio']['write-read'] = '[open open]'
G.add_edge('trustonicpartner_app','s_system_app')
G.edge['trustonicpartner_app']['s_system_app']['write-read'] = '[open open]'
G.add_edge('trustonicpartner_app','surfaceflinger')
G.edge['trustonicpartner_app']['surfaceflinger']['write-read'] = '[open open]'
G.add_edge('trustonicpartner_app','system_app')
G.edge['trustonicpartner_app']['system_app']['write-read'] = '[open open]'
G.add_edge('trustonicpartner_app','wfd_app')
G.edge['trustonicpartner_app']['wfd_app']['write-read'] = '[open open]'
G.add_edge('trustonicpartner_app','wfdservice')
G.edge['trustonicpartner_app']['wfdservice']['write-read'] = '[open open]'
G.add_edge('trustonicpartner_app','zygote')
G.edge['trustonicpartner_app']['zygote']['write-read'] = '[open open]'
G.add_edge('trustonicpartner_app','isolated_app')
G.edge['trustonicpartner_app']['isolated_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('trustonicpartner_app','untrusted_app')
G.edge['trustonicpartner_app']['untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('trustonicpartner_app','umcagent_app')
G.edge['trustonicpartner_app']['umcagent_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('trustonicpartner_app','vpn_untrusted_app')
G.edge['trustonicpartner_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('trustonicpartner_app','trustonicpartner_app')
G.edge['trustonicpartner_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('trustonicpartner_app','llk_untrusted_app')
G.edge['trustonicpartner_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('trustonicpartner_app','filtered_untrusted_app')
G.edge['trustonicpartner_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('trustonicpartner_app','filtered_google_app')
G.edge['trustonicpartner_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('trustonicpartner_app','knox_untrusted_app')
G.edge['trustonicpartner_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('trustonicpartner_app','irm_app')
G.edge['trustonicpartner_app']['irm_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('trustonicpartner_app','gad_untrusted_app')
G.edge['trustonicpartner_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('trustonicpartner_app','carrier_app')
G.edge['trustonicpartner_app']['carrier_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('trustonicpartner_app','newAttr96')
G.edge['trustonicpartner_app']['newAttr96']['write-read'] = '[open open][setattr getattr]'
G.add_edge('llk_untrusted_app','bintvoutservice')
G.edge['llk_untrusted_app']['bintvoutservice']['write-read'] = '[open open]'
G.add_edge('llk_untrusted_app','bootanim')
G.edge['llk_untrusted_app']['bootanim']['write-read'] = '[open open]'
G.add_edge('llk_untrusted_app','commonplatformappdomain')
G.edge['llk_untrusted_app']['commonplatformappdomain']['write-read'] = '[open open]'
G.add_edge('llk_untrusted_app','fixmo_app')
G.edge['llk_untrusted_app']['fixmo_app']['write-read'] = '[open open]'
G.add_edge('llk_untrusted_app','good_app')
G.edge['llk_untrusted_app']['good_app']['write-read'] = '[open open]'
G.add_edge('llk_untrusted_app','healthd')
G.edge['llk_untrusted_app']['healthd']['write-read'] = '[open open]'
G.add_edge('llk_untrusted_app','ime_app')
G.edge['llk_untrusted_app']['ime_app']['write-read'] = '[open open]'
G.add_edge('llk_untrusted_app','isolated_app')
G.edge['llk_untrusted_app']['isolated_app']['write-read'] = '[open open]'
G.add_edge('llk_untrusted_app','untrusted_app')
G.edge['llk_untrusted_app']['untrusted_app']['write-read'] = '[open open]'
G.add_edge('llk_untrusted_app','umcagent_app')
G.edge['llk_untrusted_app']['umcagent_app']['write-read'] = '[open open]'
G.add_edge('llk_untrusted_app','vpn_untrusted_app')
G.edge['llk_untrusted_app']['vpn_untrusted_app']['write-read'] = '[open open]'
G.add_edge('llk_untrusted_app','trustonicpartner_app')
G.edge['llk_untrusted_app']['trustonicpartner_app']['write-read'] = '[open open]'
G.add_edge('llk_untrusted_app','llk_untrusted_app')
G.edge['llk_untrusted_app']['llk_untrusted_app']['write-read'] = '[open open]'
G.add_edge('llk_untrusted_app','filtered_untrusted_app')
G.edge['llk_untrusted_app']['filtered_untrusted_app']['write-read'] = '[open open]'
G.add_edge('llk_untrusted_app','filtered_google_app')
G.edge['llk_untrusted_app']['filtered_google_app']['write-read'] = '[open open]'
G.add_edge('llk_untrusted_app','knox_untrusted_app')
G.edge['llk_untrusted_app']['knox_untrusted_app']['write-read'] = '[open open]'
G.add_edge('llk_untrusted_app','irm_app')
G.edge['llk_untrusted_app']['irm_app']['write-read'] = '[open open]'
G.add_edge('llk_untrusted_app','gad_untrusted_app')
G.edge['llk_untrusted_app']['gad_untrusted_app']['write-read'] = '[open open]'
G.add_edge('llk_untrusted_app','carrier_app')
G.edge['llk_untrusted_app']['carrier_app']['write-read'] = '[open open]'
G.add_edge('llk_untrusted_app','lpm')
G.edge['llk_untrusted_app']['lpm']['write-read'] = '[open open]'
G.add_edge('llk_untrusted_app','mmi')
G.edge['llk_untrusted_app']['mmi']['write-read'] = '[open open]'
G.add_edge('llk_untrusted_app','mm-pp-daemon')
G.edge['llk_untrusted_app']['mm-pp-daemon']['write-read'] = '[open open]'
G.add_edge('llk_untrusted_app','mm-qcamera-daemon')
G.edge['llk_untrusted_app']['mm-qcamera-daemon']['write-read'] = '[open open]'
G.add_edge('llk_untrusted_app','newAttr96')
G.edge['llk_untrusted_app']['newAttr96']['write-read'] = '[open open]'
G.add_edge('llk_untrusted_app','radio')
G.edge['llk_untrusted_app']['radio']['write-read'] = '[open open]'
G.add_edge('llk_untrusted_app','s_system_app')
G.edge['llk_untrusted_app']['s_system_app']['write-read'] = '[open open]'
G.add_edge('llk_untrusted_app','surfaceflinger')
G.edge['llk_untrusted_app']['surfaceflinger']['write-read'] = '[open open]'
G.add_edge('llk_untrusted_app','system_app')
G.edge['llk_untrusted_app']['system_app']['write-read'] = '[open open]'
G.add_edge('llk_untrusted_app','wfd_app')
G.edge['llk_untrusted_app']['wfd_app']['write-read'] = '[open open]'
G.add_edge('llk_untrusted_app','wfdservice')
G.edge['llk_untrusted_app']['wfdservice']['write-read'] = '[open open]'
G.add_edge('llk_untrusted_app','zygote')
G.edge['llk_untrusted_app']['zygote']['write-read'] = '[open open]'
G.add_edge('llk_untrusted_app','isolated_app')
G.edge['llk_untrusted_app']['isolated_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('llk_untrusted_app','untrusted_app')
G.edge['llk_untrusted_app']['untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('llk_untrusted_app','umcagent_app')
G.edge['llk_untrusted_app']['umcagent_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('llk_untrusted_app','vpn_untrusted_app')
G.edge['llk_untrusted_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('llk_untrusted_app','trustonicpartner_app')
G.edge['llk_untrusted_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('llk_untrusted_app','llk_untrusted_app')
G.edge['llk_untrusted_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('llk_untrusted_app','filtered_untrusted_app')
G.edge['llk_untrusted_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('llk_untrusted_app','filtered_google_app')
G.edge['llk_untrusted_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('llk_untrusted_app','knox_untrusted_app')
G.edge['llk_untrusted_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('llk_untrusted_app','irm_app')
G.edge['llk_untrusted_app']['irm_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('llk_untrusted_app','gad_untrusted_app')
G.edge['llk_untrusted_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('llk_untrusted_app','carrier_app')
G.edge['llk_untrusted_app']['carrier_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('llk_untrusted_app','newAttr96')
G.edge['llk_untrusted_app']['newAttr96']['write-read'] = '[open open][setattr getattr]'
G.add_edge('filtered_untrusted_app','bintvoutservice')
G.edge['filtered_untrusted_app']['bintvoutservice']['write-read'] = '[open open]'
G.add_edge('filtered_untrusted_app','bootanim')
G.edge['filtered_untrusted_app']['bootanim']['write-read'] = '[open open]'
G.add_edge('filtered_untrusted_app','commonplatformappdomain')
G.edge['filtered_untrusted_app']['commonplatformappdomain']['write-read'] = '[open open]'
G.add_edge('filtered_untrusted_app','fixmo_app')
G.edge['filtered_untrusted_app']['fixmo_app']['write-read'] = '[open open]'
G.add_edge('filtered_untrusted_app','good_app')
G.edge['filtered_untrusted_app']['good_app']['write-read'] = '[open open]'
G.add_edge('filtered_untrusted_app','healthd')
G.edge['filtered_untrusted_app']['healthd']['write-read'] = '[open open]'
G.add_edge('filtered_untrusted_app','ime_app')
G.edge['filtered_untrusted_app']['ime_app']['write-read'] = '[open open]'
G.add_edge('filtered_untrusted_app','isolated_app')
G.edge['filtered_untrusted_app']['isolated_app']['write-read'] = '[open open]'
G.add_edge('filtered_untrusted_app','untrusted_app')
G.edge['filtered_untrusted_app']['untrusted_app']['write-read'] = '[open open]'
G.add_edge('filtered_untrusted_app','umcagent_app')
G.edge['filtered_untrusted_app']['umcagent_app']['write-read'] = '[open open]'
G.add_edge('filtered_untrusted_app','vpn_untrusted_app')
G.edge['filtered_untrusted_app']['vpn_untrusted_app']['write-read'] = '[open open]'
G.add_edge('filtered_untrusted_app','trustonicpartner_app')
G.edge['filtered_untrusted_app']['trustonicpartner_app']['write-read'] = '[open open]'
G.add_edge('filtered_untrusted_app','llk_untrusted_app')
G.edge['filtered_untrusted_app']['llk_untrusted_app']['write-read'] = '[open open]'
G.add_edge('filtered_untrusted_app','filtered_untrusted_app')
G.edge['filtered_untrusted_app']['filtered_untrusted_app']['write-read'] = '[open open]'
G.add_edge('filtered_untrusted_app','filtered_google_app')
G.edge['filtered_untrusted_app']['filtered_google_app']['write-read'] = '[open open]'
G.add_edge('filtered_untrusted_app','knox_untrusted_app')
G.edge['filtered_untrusted_app']['knox_untrusted_app']['write-read'] = '[open open]'
G.add_edge('filtered_untrusted_app','irm_app')
G.edge['filtered_untrusted_app']['irm_app']['write-read'] = '[open open]'
G.add_edge('filtered_untrusted_app','gad_untrusted_app')
G.edge['filtered_untrusted_app']['gad_untrusted_app']['write-read'] = '[open open]'
G.add_edge('filtered_untrusted_app','carrier_app')
G.edge['filtered_untrusted_app']['carrier_app']['write-read'] = '[open open]'
G.add_edge('filtered_untrusted_app','lpm')
G.edge['filtered_untrusted_app']['lpm']['write-read'] = '[open open]'
G.add_edge('filtered_untrusted_app','mmi')
G.edge['filtered_untrusted_app']['mmi']['write-read'] = '[open open]'
G.add_edge('filtered_untrusted_app','mm-pp-daemon')
G.edge['filtered_untrusted_app']['mm-pp-daemon']['write-read'] = '[open open]'
G.add_edge('filtered_untrusted_app','mm-qcamera-daemon')
G.edge['filtered_untrusted_app']['mm-qcamera-daemon']['write-read'] = '[open open]'
G.add_edge('filtered_untrusted_app','newAttr96')
G.edge['filtered_untrusted_app']['newAttr96']['write-read'] = '[open open]'
G.add_edge('filtered_untrusted_app','radio')
G.edge['filtered_untrusted_app']['radio']['write-read'] = '[open open]'
G.add_edge('filtered_untrusted_app','s_system_app')
G.edge['filtered_untrusted_app']['s_system_app']['write-read'] = '[open open]'
G.add_edge('filtered_untrusted_app','surfaceflinger')
G.edge['filtered_untrusted_app']['surfaceflinger']['write-read'] = '[open open]'
G.add_edge('filtered_untrusted_app','system_app')
G.edge['filtered_untrusted_app']['system_app']['write-read'] = '[open open]'
G.add_edge('filtered_untrusted_app','wfd_app')
G.edge['filtered_untrusted_app']['wfd_app']['write-read'] = '[open open]'
G.add_edge('filtered_untrusted_app','wfdservice')
G.edge['filtered_untrusted_app']['wfdservice']['write-read'] = '[open open]'
G.add_edge('filtered_untrusted_app','zygote')
G.edge['filtered_untrusted_app']['zygote']['write-read'] = '[open open]'
G.add_edge('filtered_untrusted_app','isolated_app')
G.edge['filtered_untrusted_app']['isolated_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('filtered_untrusted_app','untrusted_app')
G.edge['filtered_untrusted_app']['untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('filtered_untrusted_app','umcagent_app')
G.edge['filtered_untrusted_app']['umcagent_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('filtered_untrusted_app','vpn_untrusted_app')
G.edge['filtered_untrusted_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('filtered_untrusted_app','trustonicpartner_app')
G.edge['filtered_untrusted_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('filtered_untrusted_app','llk_untrusted_app')
G.edge['filtered_untrusted_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('filtered_untrusted_app','filtered_untrusted_app')
G.edge['filtered_untrusted_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('filtered_untrusted_app','filtered_google_app')
G.edge['filtered_untrusted_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('filtered_untrusted_app','knox_untrusted_app')
G.edge['filtered_untrusted_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('filtered_untrusted_app','irm_app')
G.edge['filtered_untrusted_app']['irm_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('filtered_untrusted_app','gad_untrusted_app')
G.edge['filtered_untrusted_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('filtered_untrusted_app','carrier_app')
G.edge['filtered_untrusted_app']['carrier_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('filtered_untrusted_app','newAttr96')
G.edge['filtered_untrusted_app']['newAttr96']['write-read'] = '[open open][setattr getattr]'
G.add_edge('filtered_google_app','bintvoutservice')
G.edge['filtered_google_app']['bintvoutservice']['write-read'] = '[open open]'
G.add_edge('filtered_google_app','bootanim')
G.edge['filtered_google_app']['bootanim']['write-read'] = '[open open]'
G.add_edge('filtered_google_app','commonplatformappdomain')
G.edge['filtered_google_app']['commonplatformappdomain']['write-read'] = '[open open]'
G.add_edge('filtered_google_app','fixmo_app')
G.edge['filtered_google_app']['fixmo_app']['write-read'] = '[open open]'
G.add_edge('filtered_google_app','good_app')
G.edge['filtered_google_app']['good_app']['write-read'] = '[open open]'
G.add_edge('filtered_google_app','healthd')
G.edge['filtered_google_app']['healthd']['write-read'] = '[open open]'
G.add_edge('filtered_google_app','ime_app')
G.edge['filtered_google_app']['ime_app']['write-read'] = '[open open]'
G.add_edge('filtered_google_app','isolated_app')
G.edge['filtered_google_app']['isolated_app']['write-read'] = '[open open]'
G.add_edge('filtered_google_app','untrusted_app')
G.edge['filtered_google_app']['untrusted_app']['write-read'] = '[open open]'
G.add_edge('filtered_google_app','umcagent_app')
G.edge['filtered_google_app']['umcagent_app']['write-read'] = '[open open]'
G.add_edge('filtered_google_app','vpn_untrusted_app')
G.edge['filtered_google_app']['vpn_untrusted_app']['write-read'] = '[open open]'
G.add_edge('filtered_google_app','trustonicpartner_app')
G.edge['filtered_google_app']['trustonicpartner_app']['write-read'] = '[open open]'
G.add_edge('filtered_google_app','llk_untrusted_app')
G.edge['filtered_google_app']['llk_untrusted_app']['write-read'] = '[open open]'
G.add_edge('filtered_google_app','filtered_untrusted_app')
G.edge['filtered_google_app']['filtered_untrusted_app']['write-read'] = '[open open]'
G.add_edge('filtered_google_app','filtered_google_app')
G.edge['filtered_google_app']['filtered_google_app']['write-read'] = '[open open]'
G.add_edge('filtered_google_app','knox_untrusted_app')
G.edge['filtered_google_app']['knox_untrusted_app']['write-read'] = '[open open]'
G.add_edge('filtered_google_app','irm_app')
G.edge['filtered_google_app']['irm_app']['write-read'] = '[open open]'
G.add_edge('filtered_google_app','gad_untrusted_app')
G.edge['filtered_google_app']['gad_untrusted_app']['write-read'] = '[open open]'
G.add_edge('filtered_google_app','carrier_app')
G.edge['filtered_google_app']['carrier_app']['write-read'] = '[open open]'
G.add_edge('filtered_google_app','lpm')
G.edge['filtered_google_app']['lpm']['write-read'] = '[open open]'
G.add_edge('filtered_google_app','mmi')
G.edge['filtered_google_app']['mmi']['write-read'] = '[open open]'
G.add_edge('filtered_google_app','mm-pp-daemon')
G.edge['filtered_google_app']['mm-pp-daemon']['write-read'] = '[open open]'
G.add_edge('filtered_google_app','mm-qcamera-daemon')
G.edge['filtered_google_app']['mm-qcamera-daemon']['write-read'] = '[open open]'
G.add_edge('filtered_google_app','newAttr96')
G.edge['filtered_google_app']['newAttr96']['write-read'] = '[open open]'
G.add_edge('filtered_google_app','radio')
G.edge['filtered_google_app']['radio']['write-read'] = '[open open]'
G.add_edge('filtered_google_app','s_system_app')
G.edge['filtered_google_app']['s_system_app']['write-read'] = '[open open]'
G.add_edge('filtered_google_app','surfaceflinger')
G.edge['filtered_google_app']['surfaceflinger']['write-read'] = '[open open]'
G.add_edge('filtered_google_app','system_app')
G.edge['filtered_google_app']['system_app']['write-read'] = '[open open]'
G.add_edge('filtered_google_app','wfd_app')
G.edge['filtered_google_app']['wfd_app']['write-read'] = '[open open]'
G.add_edge('filtered_google_app','wfdservice')
G.edge['filtered_google_app']['wfdservice']['write-read'] = '[open open]'
G.add_edge('filtered_google_app','zygote')
G.edge['filtered_google_app']['zygote']['write-read'] = '[open open]'
G.add_edge('filtered_google_app','isolated_app')
G.edge['filtered_google_app']['isolated_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('filtered_google_app','untrusted_app')
G.edge['filtered_google_app']['untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('filtered_google_app','umcagent_app')
G.edge['filtered_google_app']['umcagent_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('filtered_google_app','vpn_untrusted_app')
G.edge['filtered_google_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('filtered_google_app','trustonicpartner_app')
G.edge['filtered_google_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('filtered_google_app','llk_untrusted_app')
G.edge['filtered_google_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('filtered_google_app','filtered_untrusted_app')
G.edge['filtered_google_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('filtered_google_app','filtered_google_app')
G.edge['filtered_google_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('filtered_google_app','knox_untrusted_app')
G.edge['filtered_google_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('filtered_google_app','irm_app')
G.edge['filtered_google_app']['irm_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('filtered_google_app','gad_untrusted_app')
G.edge['filtered_google_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('filtered_google_app','carrier_app')
G.edge['filtered_google_app']['carrier_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('filtered_google_app','newAttr96')
G.edge['filtered_google_app']['newAttr96']['write-read'] = '[open open][setattr getattr]'
G.add_edge('knox_untrusted_app','bintvoutservice')
G.edge['knox_untrusted_app']['bintvoutservice']['write-read'] = '[open open]'
G.add_edge('knox_untrusted_app','bootanim')
G.edge['knox_untrusted_app']['bootanim']['write-read'] = '[open open]'
G.add_edge('knox_untrusted_app','commonplatformappdomain')
G.edge['knox_untrusted_app']['commonplatformappdomain']['write-read'] = '[open open]'
G.add_edge('knox_untrusted_app','fixmo_app')
G.edge['knox_untrusted_app']['fixmo_app']['write-read'] = '[open open]'
G.add_edge('knox_untrusted_app','good_app')
G.edge['knox_untrusted_app']['good_app']['write-read'] = '[open open]'
G.add_edge('knox_untrusted_app','healthd')
G.edge['knox_untrusted_app']['healthd']['write-read'] = '[open open]'
G.add_edge('knox_untrusted_app','ime_app')
G.edge['knox_untrusted_app']['ime_app']['write-read'] = '[open open]'
G.add_edge('knox_untrusted_app','isolated_app')
G.edge['knox_untrusted_app']['isolated_app']['write-read'] = '[open open]'
G.add_edge('knox_untrusted_app','untrusted_app')
G.edge['knox_untrusted_app']['untrusted_app']['write-read'] = '[open open]'
G.add_edge('knox_untrusted_app','umcagent_app')
G.edge['knox_untrusted_app']['umcagent_app']['write-read'] = '[open open]'
G.add_edge('knox_untrusted_app','vpn_untrusted_app')
G.edge['knox_untrusted_app']['vpn_untrusted_app']['write-read'] = '[open open]'
G.add_edge('knox_untrusted_app','trustonicpartner_app')
G.edge['knox_untrusted_app']['trustonicpartner_app']['write-read'] = '[open open]'
G.add_edge('knox_untrusted_app','llk_untrusted_app')
G.edge['knox_untrusted_app']['llk_untrusted_app']['write-read'] = '[open open]'
G.add_edge('knox_untrusted_app','filtered_untrusted_app')
G.edge['knox_untrusted_app']['filtered_untrusted_app']['write-read'] = '[open open]'
G.add_edge('knox_untrusted_app','filtered_google_app')
G.edge['knox_untrusted_app']['filtered_google_app']['write-read'] = '[open open]'
G.add_edge('knox_untrusted_app','knox_untrusted_app')
G.edge['knox_untrusted_app']['knox_untrusted_app']['write-read'] = '[open open]'
G.add_edge('knox_untrusted_app','irm_app')
G.edge['knox_untrusted_app']['irm_app']['write-read'] = '[open open]'
G.add_edge('knox_untrusted_app','gad_untrusted_app')
G.edge['knox_untrusted_app']['gad_untrusted_app']['write-read'] = '[open open]'
G.add_edge('knox_untrusted_app','carrier_app')
G.edge['knox_untrusted_app']['carrier_app']['write-read'] = '[open open]'
G.add_edge('knox_untrusted_app','lpm')
G.edge['knox_untrusted_app']['lpm']['write-read'] = '[open open]'
G.add_edge('knox_untrusted_app','mmi')
G.edge['knox_untrusted_app']['mmi']['write-read'] = '[open open]'
G.add_edge('knox_untrusted_app','mm-pp-daemon')
G.edge['knox_untrusted_app']['mm-pp-daemon']['write-read'] = '[open open]'
G.add_edge('knox_untrusted_app','mm-qcamera-daemon')
G.edge['knox_untrusted_app']['mm-qcamera-daemon']['write-read'] = '[open open]'
G.add_edge('knox_untrusted_app','newAttr96')
G.edge['knox_untrusted_app']['newAttr96']['write-read'] = '[open open]'
G.add_edge('knox_untrusted_app','radio')
G.edge['knox_untrusted_app']['radio']['write-read'] = '[open open]'
G.add_edge('knox_untrusted_app','s_system_app')
G.edge['knox_untrusted_app']['s_system_app']['write-read'] = '[open open]'
G.add_edge('knox_untrusted_app','surfaceflinger')
G.edge['knox_untrusted_app']['surfaceflinger']['write-read'] = '[open open]'
G.add_edge('knox_untrusted_app','system_app')
G.edge['knox_untrusted_app']['system_app']['write-read'] = '[open open]'
G.add_edge('knox_untrusted_app','wfd_app')
G.edge['knox_untrusted_app']['wfd_app']['write-read'] = '[open open]'
G.add_edge('knox_untrusted_app','wfdservice')
G.edge['knox_untrusted_app']['wfdservice']['write-read'] = '[open open]'
G.add_edge('knox_untrusted_app','zygote')
G.edge['knox_untrusted_app']['zygote']['write-read'] = '[open open]'
G.add_edge('knox_untrusted_app','isolated_app')
G.edge['knox_untrusted_app']['isolated_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('knox_untrusted_app','untrusted_app')
G.edge['knox_untrusted_app']['untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('knox_untrusted_app','umcagent_app')
G.edge['knox_untrusted_app']['umcagent_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('knox_untrusted_app','vpn_untrusted_app')
G.edge['knox_untrusted_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('knox_untrusted_app','trustonicpartner_app')
G.edge['knox_untrusted_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('knox_untrusted_app','llk_untrusted_app')
G.edge['knox_untrusted_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('knox_untrusted_app','filtered_untrusted_app')
G.edge['knox_untrusted_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('knox_untrusted_app','filtered_google_app')
G.edge['knox_untrusted_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('knox_untrusted_app','knox_untrusted_app')
G.edge['knox_untrusted_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('knox_untrusted_app','irm_app')
G.edge['knox_untrusted_app']['irm_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('knox_untrusted_app','gad_untrusted_app')
G.edge['knox_untrusted_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('knox_untrusted_app','carrier_app')
G.edge['knox_untrusted_app']['carrier_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('knox_untrusted_app','newAttr96')
G.edge['knox_untrusted_app']['newAttr96']['write-read'] = '[open open][setattr getattr]'
G.add_edge('irm_app','bintvoutservice')
G.edge['irm_app']['bintvoutservice']['write-read'] = '[open open]'
G.add_edge('irm_app','bootanim')
G.edge['irm_app']['bootanim']['write-read'] = '[open open]'
G.add_edge('irm_app','commonplatformappdomain')
G.edge['irm_app']['commonplatformappdomain']['write-read'] = '[open open]'
G.add_edge('irm_app','fixmo_app')
G.edge['irm_app']['fixmo_app']['write-read'] = '[open open]'
G.add_edge('irm_app','good_app')
G.edge['irm_app']['good_app']['write-read'] = '[open open]'
G.add_edge('irm_app','healthd')
G.edge['irm_app']['healthd']['write-read'] = '[open open]'
G.add_edge('irm_app','ime_app')
G.edge['irm_app']['ime_app']['write-read'] = '[open open]'
G.add_edge('irm_app','isolated_app')
G.edge['irm_app']['isolated_app']['write-read'] = '[open open]'
G.add_edge('irm_app','untrusted_app')
G.edge['irm_app']['untrusted_app']['write-read'] = '[open open]'
G.add_edge('irm_app','umcagent_app')
G.edge['irm_app']['umcagent_app']['write-read'] = '[open open]'
G.add_edge('irm_app','vpn_untrusted_app')
G.edge['irm_app']['vpn_untrusted_app']['write-read'] = '[open open]'
G.add_edge('irm_app','trustonicpartner_app')
G.edge['irm_app']['trustonicpartner_app']['write-read'] = '[open open]'
G.add_edge('irm_app','llk_untrusted_app')
G.edge['irm_app']['llk_untrusted_app']['write-read'] = '[open open]'
G.add_edge('irm_app','filtered_untrusted_app')
G.edge['irm_app']['filtered_untrusted_app']['write-read'] = '[open open]'
G.add_edge('irm_app','filtered_google_app')
G.edge['irm_app']['filtered_google_app']['write-read'] = '[open open]'
G.add_edge('irm_app','knox_untrusted_app')
G.edge['irm_app']['knox_untrusted_app']['write-read'] = '[open open]'
G.add_edge('irm_app','irm_app')
G.edge['irm_app']['irm_app']['write-read'] = '[open open]'
G.add_edge('irm_app','gad_untrusted_app')
G.edge['irm_app']['gad_untrusted_app']['write-read'] = '[open open]'
G.add_edge('irm_app','carrier_app')
G.edge['irm_app']['carrier_app']['write-read'] = '[open open]'
G.add_edge('irm_app','lpm')
G.edge['irm_app']['lpm']['write-read'] = '[open open]'
G.add_edge('irm_app','mmi')
G.edge['irm_app']['mmi']['write-read'] = '[open open]'
G.add_edge('irm_app','mm-pp-daemon')
G.edge['irm_app']['mm-pp-daemon']['write-read'] = '[open open]'
G.add_edge('irm_app','mm-qcamera-daemon')
G.edge['irm_app']['mm-qcamera-daemon']['write-read'] = '[open open]'
G.add_edge('irm_app','newAttr96')
G.edge['irm_app']['newAttr96']['write-read'] = '[open open]'
G.add_edge('irm_app','radio')
G.edge['irm_app']['radio']['write-read'] = '[open open]'
G.add_edge('irm_app','s_system_app')
G.edge['irm_app']['s_system_app']['write-read'] = '[open open]'
G.add_edge('irm_app','surfaceflinger')
G.edge['irm_app']['surfaceflinger']['write-read'] = '[open open]'
G.add_edge('irm_app','system_app')
G.edge['irm_app']['system_app']['write-read'] = '[open open]'
G.add_edge('irm_app','wfd_app')
G.edge['irm_app']['wfd_app']['write-read'] = '[open open]'
G.add_edge('irm_app','wfdservice')
G.edge['irm_app']['wfdservice']['write-read'] = '[open open]'
G.add_edge('irm_app','zygote')
G.edge['irm_app']['zygote']['write-read'] = '[open open]'
G.add_edge('irm_app','isolated_app')
G.edge['irm_app']['isolated_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('irm_app','untrusted_app')
G.edge['irm_app']['untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('irm_app','umcagent_app')
G.edge['irm_app']['umcagent_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('irm_app','vpn_untrusted_app')
G.edge['irm_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('irm_app','trustonicpartner_app')
G.edge['irm_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('irm_app','llk_untrusted_app')
G.edge['irm_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('irm_app','filtered_untrusted_app')
G.edge['irm_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('irm_app','filtered_google_app')
G.edge['irm_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('irm_app','knox_untrusted_app')
G.edge['irm_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('irm_app','irm_app')
G.edge['irm_app']['irm_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('irm_app','gad_untrusted_app')
G.edge['irm_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('irm_app','carrier_app')
G.edge['irm_app']['carrier_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('irm_app','newAttr96')
G.edge['irm_app']['newAttr96']['write-read'] = '[open open][setattr getattr]'
G.add_edge('gad_untrusted_app','bintvoutservice')
G.edge['gad_untrusted_app']['bintvoutservice']['write-read'] = '[open open]'
G.add_edge('gad_untrusted_app','bootanim')
G.edge['gad_untrusted_app']['bootanim']['write-read'] = '[open open]'
G.add_edge('gad_untrusted_app','commonplatformappdomain')
G.edge['gad_untrusted_app']['commonplatformappdomain']['write-read'] = '[open open]'
G.add_edge('gad_untrusted_app','fixmo_app')
G.edge['gad_untrusted_app']['fixmo_app']['write-read'] = '[open open]'
G.add_edge('gad_untrusted_app','good_app')
G.edge['gad_untrusted_app']['good_app']['write-read'] = '[open open]'
G.add_edge('gad_untrusted_app','healthd')
G.edge['gad_untrusted_app']['healthd']['write-read'] = '[open open]'
G.add_edge('gad_untrusted_app','ime_app')
G.edge['gad_untrusted_app']['ime_app']['write-read'] = '[open open]'
G.add_edge('gad_untrusted_app','isolated_app')
G.edge['gad_untrusted_app']['isolated_app']['write-read'] = '[open open]'
G.add_edge('gad_untrusted_app','untrusted_app')
G.edge['gad_untrusted_app']['untrusted_app']['write-read'] = '[open open]'
G.add_edge('gad_untrusted_app','umcagent_app')
G.edge['gad_untrusted_app']['umcagent_app']['write-read'] = '[open open]'
G.add_edge('gad_untrusted_app','vpn_untrusted_app')
G.edge['gad_untrusted_app']['vpn_untrusted_app']['write-read'] = '[open open]'
G.add_edge('gad_untrusted_app','trustonicpartner_app')
G.edge['gad_untrusted_app']['trustonicpartner_app']['write-read'] = '[open open]'
G.add_edge('gad_untrusted_app','llk_untrusted_app')
G.edge['gad_untrusted_app']['llk_untrusted_app']['write-read'] = '[open open]'
G.add_edge('gad_untrusted_app','filtered_untrusted_app')
G.edge['gad_untrusted_app']['filtered_untrusted_app']['write-read'] = '[open open]'
G.add_edge('gad_untrusted_app','filtered_google_app')
G.edge['gad_untrusted_app']['filtered_google_app']['write-read'] = '[open open]'
G.add_edge('gad_untrusted_app','knox_untrusted_app')
G.edge['gad_untrusted_app']['knox_untrusted_app']['write-read'] = '[open open]'
G.add_edge('gad_untrusted_app','irm_app')
G.edge['gad_untrusted_app']['irm_app']['write-read'] = '[open open]'
G.add_edge('gad_untrusted_app','gad_untrusted_app')
G.edge['gad_untrusted_app']['gad_untrusted_app']['write-read'] = '[open open]'
G.add_edge('gad_untrusted_app','carrier_app')
G.edge['gad_untrusted_app']['carrier_app']['write-read'] = '[open open]'
G.add_edge('gad_untrusted_app','lpm')
G.edge['gad_untrusted_app']['lpm']['write-read'] = '[open open]'
G.add_edge('gad_untrusted_app','mmi')
G.edge['gad_untrusted_app']['mmi']['write-read'] = '[open open]'
G.add_edge('gad_untrusted_app','mm-pp-daemon')
G.edge['gad_untrusted_app']['mm-pp-daemon']['write-read'] = '[open open]'
G.add_edge('gad_untrusted_app','mm-qcamera-daemon')
G.edge['gad_untrusted_app']['mm-qcamera-daemon']['write-read'] = '[open open]'
G.add_edge('gad_untrusted_app','newAttr96')
G.edge['gad_untrusted_app']['newAttr96']['write-read'] = '[open open]'
G.add_edge('gad_untrusted_app','radio')
G.edge['gad_untrusted_app']['radio']['write-read'] = '[open open]'
G.add_edge('gad_untrusted_app','s_system_app')
G.edge['gad_untrusted_app']['s_system_app']['write-read'] = '[open open]'
G.add_edge('gad_untrusted_app','surfaceflinger')
G.edge['gad_untrusted_app']['surfaceflinger']['write-read'] = '[open open]'
G.add_edge('gad_untrusted_app','system_app')
G.edge['gad_untrusted_app']['system_app']['write-read'] = '[open open]'
G.add_edge('gad_untrusted_app','wfd_app')
G.edge['gad_untrusted_app']['wfd_app']['write-read'] = '[open open]'
G.add_edge('gad_untrusted_app','wfdservice')
G.edge['gad_untrusted_app']['wfdservice']['write-read'] = '[open open]'
G.add_edge('gad_untrusted_app','zygote')
G.edge['gad_untrusted_app']['zygote']['write-read'] = '[open open]'
G.add_edge('gad_untrusted_app','isolated_app')
G.edge['gad_untrusted_app']['isolated_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('gad_untrusted_app','untrusted_app')
G.edge['gad_untrusted_app']['untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('gad_untrusted_app','umcagent_app')
G.edge['gad_untrusted_app']['umcagent_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('gad_untrusted_app','vpn_untrusted_app')
G.edge['gad_untrusted_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('gad_untrusted_app','trustonicpartner_app')
G.edge['gad_untrusted_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('gad_untrusted_app','llk_untrusted_app')
G.edge['gad_untrusted_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('gad_untrusted_app','filtered_untrusted_app')
G.edge['gad_untrusted_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('gad_untrusted_app','filtered_google_app')
G.edge['gad_untrusted_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('gad_untrusted_app','knox_untrusted_app')
G.edge['gad_untrusted_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('gad_untrusted_app','irm_app')
G.edge['gad_untrusted_app']['irm_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('gad_untrusted_app','gad_untrusted_app')
G.edge['gad_untrusted_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('gad_untrusted_app','carrier_app')
G.edge['gad_untrusted_app']['carrier_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('gad_untrusted_app','newAttr96')
G.edge['gad_untrusted_app']['newAttr96']['write-read'] = '[open open][setattr getattr]'
G.add_edge('carrier_app','bintvoutservice')
G.edge['carrier_app']['bintvoutservice']['write-read'] = '[open open]'
G.add_edge('carrier_app','bootanim')
G.edge['carrier_app']['bootanim']['write-read'] = '[open open]'
G.add_edge('carrier_app','commonplatformappdomain')
G.edge['carrier_app']['commonplatformappdomain']['write-read'] = '[open open]'
G.add_edge('carrier_app','fixmo_app')
G.edge['carrier_app']['fixmo_app']['write-read'] = '[open open]'
G.add_edge('carrier_app','good_app')
G.edge['carrier_app']['good_app']['write-read'] = '[open open]'
G.add_edge('carrier_app','healthd')
G.edge['carrier_app']['healthd']['write-read'] = '[open open]'
G.add_edge('carrier_app','ime_app')
G.edge['carrier_app']['ime_app']['write-read'] = '[open open]'
G.add_edge('carrier_app','isolated_app')
G.edge['carrier_app']['isolated_app']['write-read'] = '[open open]'
G.add_edge('carrier_app','untrusted_app')
G.edge['carrier_app']['untrusted_app']['write-read'] = '[open open]'
G.add_edge('carrier_app','umcagent_app')
G.edge['carrier_app']['umcagent_app']['write-read'] = '[open open]'
G.add_edge('carrier_app','vpn_untrusted_app')
G.edge['carrier_app']['vpn_untrusted_app']['write-read'] = '[open open]'
G.add_edge('carrier_app','trustonicpartner_app')
G.edge['carrier_app']['trustonicpartner_app']['write-read'] = '[open open]'
G.add_edge('carrier_app','llk_untrusted_app')
G.edge['carrier_app']['llk_untrusted_app']['write-read'] = '[open open]'
G.add_edge('carrier_app','filtered_untrusted_app')
G.edge['carrier_app']['filtered_untrusted_app']['write-read'] = '[open open]'
G.add_edge('carrier_app','filtered_google_app')
G.edge['carrier_app']['filtered_google_app']['write-read'] = '[open open]'
G.add_edge('carrier_app','knox_untrusted_app')
G.edge['carrier_app']['knox_untrusted_app']['write-read'] = '[open open]'
G.add_edge('carrier_app','irm_app')
G.edge['carrier_app']['irm_app']['write-read'] = '[open open]'
G.add_edge('carrier_app','gad_untrusted_app')
G.edge['carrier_app']['gad_untrusted_app']['write-read'] = '[open open]'
G.add_edge('carrier_app','carrier_app')
G.edge['carrier_app']['carrier_app']['write-read'] = '[open open]'
G.add_edge('carrier_app','lpm')
G.edge['carrier_app']['lpm']['write-read'] = '[open open]'
G.add_edge('carrier_app','mmi')
G.edge['carrier_app']['mmi']['write-read'] = '[open open]'
G.add_edge('carrier_app','mm-pp-daemon')
G.edge['carrier_app']['mm-pp-daemon']['write-read'] = '[open open]'
G.add_edge('carrier_app','mm-qcamera-daemon')
G.edge['carrier_app']['mm-qcamera-daemon']['write-read'] = '[open open]'
G.add_edge('carrier_app','newAttr96')
G.edge['carrier_app']['newAttr96']['write-read'] = '[open open]'
G.add_edge('carrier_app','radio')
G.edge['carrier_app']['radio']['write-read'] = '[open open]'
G.add_edge('carrier_app','s_system_app')
G.edge['carrier_app']['s_system_app']['write-read'] = '[open open]'
G.add_edge('carrier_app','surfaceflinger')
G.edge['carrier_app']['surfaceflinger']['write-read'] = '[open open]'
G.add_edge('carrier_app','system_app')
G.edge['carrier_app']['system_app']['write-read'] = '[open open]'
G.add_edge('carrier_app','wfd_app')
G.edge['carrier_app']['wfd_app']['write-read'] = '[open open]'
G.add_edge('carrier_app','wfdservice')
G.edge['carrier_app']['wfdservice']['write-read'] = '[open open]'
G.add_edge('carrier_app','zygote')
G.edge['carrier_app']['zygote']['write-read'] = '[open open]'
G.add_edge('carrier_app','isolated_app')
G.edge['carrier_app']['isolated_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('carrier_app','untrusted_app')
G.edge['carrier_app']['untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('carrier_app','umcagent_app')
G.edge['carrier_app']['umcagent_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('carrier_app','vpn_untrusted_app')
G.edge['carrier_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('carrier_app','trustonicpartner_app')
G.edge['carrier_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('carrier_app','llk_untrusted_app')
G.edge['carrier_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('carrier_app','filtered_untrusted_app')
G.edge['carrier_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('carrier_app','filtered_google_app')
G.edge['carrier_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('carrier_app','knox_untrusted_app')
G.edge['carrier_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('carrier_app','irm_app')
G.edge['carrier_app']['irm_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('carrier_app','gad_untrusted_app')
G.edge['carrier_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('carrier_app','carrier_app')
G.edge['carrier_app']['carrier_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('carrier_app','newAttr96')
G.edge['carrier_app']['newAttr96']['write-read'] = '[open open][setattr getattr]'
G.add_edge('lpm','bintvoutservice')
G.edge['lpm']['bintvoutservice']['write-read'] = '[open open]'
G.add_edge('lpm','bootanim')
G.edge['lpm']['bootanim']['write-read'] = '[open open]'
G.add_edge('lpm','commonplatformappdomain')
G.edge['lpm']['commonplatformappdomain']['write-read'] = '[open open]'
G.add_edge('lpm','fixmo_app')
G.edge['lpm']['fixmo_app']['write-read'] = '[open open]'
G.add_edge('lpm','good_app')
G.edge['lpm']['good_app']['write-read'] = '[open open]'
G.add_edge('lpm','healthd')
G.edge['lpm']['healthd']['write-read'] = '[write read][append read][open open]'
G.add_edge('lpm','ime_app')
G.edge['lpm']['ime_app']['write-read'] = '[open open]'
G.add_edge('lpm','isolated_app')
G.edge['lpm']['isolated_app']['write-read'] = '[open open]'
G.add_edge('lpm','untrusted_app')
G.edge['lpm']['untrusted_app']['write-read'] = '[open open]'
G.add_edge('lpm','umcagent_app')
G.edge['lpm']['umcagent_app']['write-read'] = '[open open]'
G.add_edge('lpm','vpn_untrusted_app')
G.edge['lpm']['vpn_untrusted_app']['write-read'] = '[open open]'
G.add_edge('lpm','trustonicpartner_app')
G.edge['lpm']['trustonicpartner_app']['write-read'] = '[open open]'
G.add_edge('lpm','llk_untrusted_app')
G.edge['lpm']['llk_untrusted_app']['write-read'] = '[open open]'
G.add_edge('lpm','filtered_untrusted_app')
G.edge['lpm']['filtered_untrusted_app']['write-read'] = '[open open]'
G.add_edge('lpm','filtered_google_app')
G.edge['lpm']['filtered_google_app']['write-read'] = '[open open]'
G.add_edge('lpm','knox_untrusted_app')
G.edge['lpm']['knox_untrusted_app']['write-read'] = '[open open]'
G.add_edge('lpm','irm_app')
G.edge['lpm']['irm_app']['write-read'] = '[open open]'
G.add_edge('lpm','gad_untrusted_app')
G.edge['lpm']['gad_untrusted_app']['write-read'] = '[open open]'
G.add_edge('lpm','carrier_app')
G.edge['lpm']['carrier_app']['write-read'] = '[open open]'
G.add_edge('lpm','lpm')
G.edge['lpm']['lpm']['write-read'] = '[open open]'
G.add_edge('lpm','mmi')
G.edge['lpm']['mmi']['write-read'] = '[open open]'
G.add_edge('lpm','mm-pp-daemon')
G.edge['lpm']['mm-pp-daemon']['write-read'] = '[open open]'
G.add_edge('lpm','mm-qcamera-daemon')
G.edge['lpm']['mm-qcamera-daemon']['write-read'] = '[open open]'
G.add_edge('lpm','newAttr96')
G.edge['lpm']['newAttr96']['write-read'] = '[open open]'
G.add_edge('lpm','radio')
G.edge['lpm']['radio']['write-read'] = '[open open]'
G.add_edge('lpm','s_system_app')
G.edge['lpm']['s_system_app']['write-read'] = '[open open]'
G.add_edge('lpm','surfaceflinger')
G.edge['lpm']['surfaceflinger']['write-read'] = '[write read][append read][open open]'
G.add_edge('lpm','system_app')
G.edge['lpm']['system_app']['write-read'] = '[open open]'
G.add_edge('lpm','wfd_app')
G.edge['lpm']['wfd_app']['write-read'] = '[open open]'
G.add_edge('lpm','wfdservice')
G.edge['lpm']['wfdservice']['write-read'] = '[write read][append read][open open]'
G.add_edge('lpm','zygote')
G.edge['lpm']['zygote']['write-read'] = '[open open]'
G.add_edge('lpm','isolated_app')
G.edge['lpm']['isolated_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('lpm','untrusted_app')
G.edge['lpm']['untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('lpm','umcagent_app')
G.edge['lpm']['umcagent_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('lpm','vpn_untrusted_app')
G.edge['lpm']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('lpm','trustonicpartner_app')
G.edge['lpm']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('lpm','llk_untrusted_app')
G.edge['lpm']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('lpm','filtered_untrusted_app')
G.edge['lpm']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('lpm','filtered_google_app')
G.edge['lpm']['filtered_google_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('lpm','knox_untrusted_app')
G.edge['lpm']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('lpm','irm_app')
G.edge['lpm']['irm_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('lpm','gad_untrusted_app')
G.edge['lpm']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('lpm','carrier_app')
G.edge['lpm']['carrier_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('lpm','newAttr96')
G.edge['lpm']['newAttr96']['write-read'] = '[open open][setattr getattr]'
G.add_edge('lpm','bintvoutservice')
G.edge['lpm']['bintvoutservice']['write-read'] = '[open open][write read]'
G.edge['lpm']['bintvoutservice']['fill'] = 'red'
G.add_edge('lpm','bintvoutservice')
G.edge['lpm']['bintvoutservice']['write-read'] = '[open open][write read][append read]'
G.add_edge('lpm','bootanim')
G.edge['lpm']['bootanim']['write-read'] = '[open open][write read]'
G.edge['lpm']['bootanim']['fill'] = 'red'
G.add_edge('lpm','bootanim')
G.edge['lpm']['bootanim']['write-read'] = '[open open][write read][append read]'
G.add_edge('lpm','commonplatformappdomain')
G.edge['lpm']['commonplatformappdomain']['write-read'] = '[open open][write read]'
G.edge['lpm']['commonplatformappdomain']['fill'] = 'red'
G.add_edge('lpm','commonplatformappdomain')
G.edge['lpm']['commonplatformappdomain']['write-read'] = '[open open][write read][append read]'
G.add_edge('lpm','fixmo_app')
G.edge['lpm']['fixmo_app']['write-read'] = '[open open][write read]'
G.edge['lpm']['fixmo_app']['fill'] = 'red'
G.add_edge('lpm','fixmo_app')
G.edge['lpm']['fixmo_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('lpm','good_app')
G.edge['lpm']['good_app']['write-read'] = '[open open][write read]'
G.edge['lpm']['good_app']['fill'] = 'red'
G.add_edge('lpm','good_app')
G.edge['lpm']['good_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('lpm','healthd')
G.edge['lpm']['healthd']['write-read'] = '[write read][append read][open open][write read]'
G.edge['lpm']['healthd']['fill'] = 'red'
G.add_edge('lpm','healthd')
G.edge['lpm']['healthd']['write-read'] = '[write read][append read][open open][write read][append read]'
G.add_edge('lpm','ime_app')
G.edge['lpm']['ime_app']['write-read'] = '[open open][write read]'
G.edge['lpm']['ime_app']['fill'] = 'red'
G.add_edge('lpm','ime_app')
G.edge['lpm']['ime_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('lpm','isolated_app')
G.edge['lpm']['isolated_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('lpm','untrusted_app')
G.edge['lpm']['untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('lpm','umcagent_app')
G.edge['lpm']['umcagent_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('lpm','vpn_untrusted_app')
G.edge['lpm']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('lpm','trustonicpartner_app')
G.edge['lpm']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('lpm','llk_untrusted_app')
G.edge['lpm']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('lpm','filtered_untrusted_app')
G.edge['lpm']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('lpm','filtered_google_app')
G.edge['lpm']['filtered_google_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('lpm','knox_untrusted_app')
G.edge['lpm']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('lpm','irm_app')
G.edge['lpm']['irm_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('lpm','gad_untrusted_app')
G.edge['lpm']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('lpm','carrier_app')
G.edge['lpm']['carrier_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('lpm','lpm')
G.edge['lpm']['lpm']['write-read'] = '[open open][write read]'
G.edge['lpm']['lpm']['fill'] = 'red'
G.add_edge('lpm','lpm')
G.edge['lpm']['lpm']['write-read'] = '[open open][write read][append read]'
G.add_edge('lpm','mmi')
G.edge['lpm']['mmi']['write-read'] = '[open open][write read]'
G.edge['lpm']['mmi']['fill'] = 'red'
G.add_edge('lpm','mmi')
G.edge['lpm']['mmi']['write-read'] = '[open open][write read][append read]'
G.add_edge('lpm','mm-pp-daemon')
G.edge['lpm']['mm-pp-daemon']['write-read'] = '[open open][write read]'
G.edge['lpm']['mm-pp-daemon']['fill'] = 'red'
G.add_edge('lpm','mm-pp-daemon')
G.edge['lpm']['mm-pp-daemon']['write-read'] = '[open open][write read][append read]'
G.add_edge('lpm','mm-qcamera-daemon')
G.edge['lpm']['mm-qcamera-daemon']['write-read'] = '[open open][write read]'
G.edge['lpm']['mm-qcamera-daemon']['fill'] = 'red'
G.add_edge('lpm','mm-qcamera-daemon')
G.edge['lpm']['mm-qcamera-daemon']['write-read'] = '[open open][write read][append read]'
G.add_edge('lpm','newAttr96')
G.edge['lpm']['newAttr96']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['lpm']['newAttr96']['fill'] = 'red'
G.add_edge('lpm','newAttr96')
G.edge['lpm']['newAttr96']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('lpm','radio')
G.edge['lpm']['radio']['write-read'] = '[open open][write read]'
G.edge['lpm']['radio']['fill'] = 'red'
G.add_edge('lpm','radio')
G.edge['lpm']['radio']['write-read'] = '[open open][write read][append read]'
G.add_edge('lpm','s_system_app')
G.edge['lpm']['s_system_app']['write-read'] = '[open open][write read]'
G.edge['lpm']['s_system_app']['fill'] = 'red'
G.add_edge('lpm','s_system_app')
G.edge['lpm']['s_system_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('lpm','surfaceflinger')
G.edge['lpm']['surfaceflinger']['write-read'] = '[write read][append read][open open][write read]'
G.edge['lpm']['surfaceflinger']['fill'] = 'red'
G.add_edge('lpm','surfaceflinger')
G.edge['lpm']['surfaceflinger']['write-read'] = '[write read][append read][open open][write read][append read]'
G.add_edge('lpm','system_app')
G.edge['lpm']['system_app']['write-read'] = '[open open][write read]'
G.edge['lpm']['system_app']['fill'] = 'red'
G.add_edge('lpm','system_app')
G.edge['lpm']['system_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('lpm','wfd_app')
G.edge['lpm']['wfd_app']['write-read'] = '[open open][write read]'
G.edge['lpm']['wfd_app']['fill'] = 'red'
G.add_edge('lpm','wfd_app')
G.edge['lpm']['wfd_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('lpm','wfdservice')
G.edge['lpm']['wfdservice']['write-read'] = '[write read][append read][open open][write read]'
G.edge['lpm']['wfdservice']['fill'] = 'red'
G.add_edge('lpm','wfdservice')
G.edge['lpm']['wfdservice']['write-read'] = '[write read][append read][open open][write read][append read]'
G.add_edge('lpm','zygote')
G.edge['lpm']['zygote']['write-read'] = '[open open][write read]'
G.edge['lpm']['zygote']['fill'] = 'red'
G.add_edge('lpm','zygote')
G.edge['lpm']['zygote']['write-read'] = '[open open][write read][append read]'
G.add_edge('mmi','bintvoutservice')
G.edge['mmi']['bintvoutservice']['write-read'] = '[open open]'
G.add_edge('mmi','bootanim')
G.edge['mmi']['bootanim']['write-read'] = '[open open]'
G.add_edge('mmi','commonplatformappdomain')
G.edge['mmi']['commonplatformappdomain']['write-read'] = '[open open]'
G.add_edge('mmi','fixmo_app')
G.edge['mmi']['fixmo_app']['write-read'] = '[open open]'
G.add_edge('mmi','good_app')
G.edge['mmi']['good_app']['write-read'] = '[open open]'
G.add_edge('mmi','healthd')
G.edge['mmi']['healthd']['write-read'] = '[open open]'
G.add_edge('mmi','ime_app')
G.edge['mmi']['ime_app']['write-read'] = '[open open]'
G.add_edge('mmi','isolated_app')
G.edge['mmi']['isolated_app']['write-read'] = '[open open]'
G.add_edge('mmi','untrusted_app')
G.edge['mmi']['untrusted_app']['write-read'] = '[open open]'
G.add_edge('mmi','umcagent_app')
G.edge['mmi']['umcagent_app']['write-read'] = '[open open]'
G.add_edge('mmi','vpn_untrusted_app')
G.edge['mmi']['vpn_untrusted_app']['write-read'] = '[open open]'
G.add_edge('mmi','trustonicpartner_app')
G.edge['mmi']['trustonicpartner_app']['write-read'] = '[open open]'
G.add_edge('mmi','llk_untrusted_app')
G.edge['mmi']['llk_untrusted_app']['write-read'] = '[open open]'
G.add_edge('mmi','filtered_untrusted_app')
G.edge['mmi']['filtered_untrusted_app']['write-read'] = '[open open]'
G.add_edge('mmi','filtered_google_app')
G.edge['mmi']['filtered_google_app']['write-read'] = '[open open]'
G.add_edge('mmi','knox_untrusted_app')
G.edge['mmi']['knox_untrusted_app']['write-read'] = '[open open]'
G.add_edge('mmi','irm_app')
G.edge['mmi']['irm_app']['write-read'] = '[open open]'
G.add_edge('mmi','gad_untrusted_app')
G.edge['mmi']['gad_untrusted_app']['write-read'] = '[open open]'
G.add_edge('mmi','carrier_app')
G.edge['mmi']['carrier_app']['write-read'] = '[open open]'
G.add_edge('mmi','lpm')
G.edge['mmi']['lpm']['write-read'] = '[open open]'
G.add_edge('mmi','mmi')
G.edge['mmi']['mmi']['write-read'] = '[open open]'
G.add_edge('mmi','mm-pp-daemon')
G.edge['mmi']['mm-pp-daemon']['write-read'] = '[open open]'
G.add_edge('mmi','mm-qcamera-daemon')
G.edge['mmi']['mm-qcamera-daemon']['write-read'] = '[open open]'
G.add_edge('mmi','newAttr96')
G.edge['mmi']['newAttr96']['write-read'] = '[open open]'
G.add_edge('mmi','radio')
G.edge['mmi']['radio']['write-read'] = '[open open]'
G.add_edge('mmi','s_system_app')
G.edge['mmi']['s_system_app']['write-read'] = '[open open]'
G.add_edge('mmi','surfaceflinger')
G.edge['mmi']['surfaceflinger']['write-read'] = '[open open]'
G.add_edge('mmi','system_app')
G.edge['mmi']['system_app']['write-read'] = '[open open]'
G.add_edge('mmi','wfd_app')
G.edge['mmi']['wfd_app']['write-read'] = '[open open]'
G.add_edge('mmi','wfdservice')
G.edge['mmi']['wfdservice']['write-read'] = '[open open]'
G.add_edge('mmi','zygote')
G.edge['mmi']['zygote']['write-read'] = '[open open]'
G.add_edge('mmi','isolated_app')
G.edge['mmi']['isolated_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('mmi','untrusted_app')
G.edge['mmi']['untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('mmi','umcagent_app')
G.edge['mmi']['umcagent_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('mmi','vpn_untrusted_app')
G.edge['mmi']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('mmi','trustonicpartner_app')
G.edge['mmi']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('mmi','llk_untrusted_app')
G.edge['mmi']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('mmi','filtered_untrusted_app')
G.edge['mmi']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('mmi','filtered_google_app')
G.edge['mmi']['filtered_google_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('mmi','knox_untrusted_app')
G.edge['mmi']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('mmi','irm_app')
G.edge['mmi']['irm_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('mmi','gad_untrusted_app')
G.edge['mmi']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('mmi','carrier_app')
G.edge['mmi']['carrier_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('mmi','newAttr96')
G.edge['mmi']['newAttr96']['write-read'] = '[open open][setattr getattr]'
G.add_edge('mmi','bintvoutservice')
G.edge['mmi']['bintvoutservice']['write-read'] = '[open open][write read]'
G.edge['mmi']['bintvoutservice']['fill'] = 'red'
G.add_edge('mmi','bintvoutservice')
G.edge['mmi']['bintvoutservice']['write-read'] = '[open open][write read][append read]'
G.add_edge('mmi','bootanim')
G.edge['mmi']['bootanim']['write-read'] = '[open open][write read]'
G.edge['mmi']['bootanim']['fill'] = 'red'
G.add_edge('mmi','bootanim')
G.edge['mmi']['bootanim']['write-read'] = '[open open][write read][append read]'
G.add_edge('mmi','commonplatformappdomain')
G.edge['mmi']['commonplatformappdomain']['write-read'] = '[open open][write read]'
G.edge['mmi']['commonplatformappdomain']['fill'] = 'red'
G.add_edge('mmi','commonplatformappdomain')
G.edge['mmi']['commonplatformappdomain']['write-read'] = '[open open][write read][append read]'
G.add_edge('mmi','fixmo_app')
G.edge['mmi']['fixmo_app']['write-read'] = '[open open][write read]'
G.edge['mmi']['fixmo_app']['fill'] = 'red'
G.add_edge('mmi','fixmo_app')
G.edge['mmi']['fixmo_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('mmi','good_app')
G.edge['mmi']['good_app']['write-read'] = '[open open][write read]'
G.edge['mmi']['good_app']['fill'] = 'red'
G.add_edge('mmi','good_app')
G.edge['mmi']['good_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('mmi','healthd')
G.edge['mmi']['healthd']['write-read'] = '[open open][write read]'
G.edge['mmi']['healthd']['fill'] = 'red'
G.add_edge('mmi','healthd')
G.edge['mmi']['healthd']['write-read'] = '[open open][write read][append read]'
G.add_edge('mmi','ime_app')
G.edge['mmi']['ime_app']['write-read'] = '[open open][write read]'
G.edge['mmi']['ime_app']['fill'] = 'red'
G.add_edge('mmi','ime_app')
G.edge['mmi']['ime_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('mmi','isolated_app')
G.edge['mmi']['isolated_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('mmi','untrusted_app')
G.edge['mmi']['untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('mmi','umcagent_app')
G.edge['mmi']['umcagent_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('mmi','vpn_untrusted_app')
G.edge['mmi']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('mmi','trustonicpartner_app')
G.edge['mmi']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('mmi','llk_untrusted_app')
G.edge['mmi']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('mmi','filtered_untrusted_app')
G.edge['mmi']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('mmi','filtered_google_app')
G.edge['mmi']['filtered_google_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('mmi','knox_untrusted_app')
G.edge['mmi']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('mmi','irm_app')
G.edge['mmi']['irm_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('mmi','gad_untrusted_app')
G.edge['mmi']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('mmi','carrier_app')
G.edge['mmi']['carrier_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('mmi','lpm')
G.edge['mmi']['lpm']['write-read'] = '[open open][write read]'
G.edge['mmi']['lpm']['fill'] = 'red'
G.add_edge('mmi','lpm')
G.edge['mmi']['lpm']['write-read'] = '[open open][write read][append read]'
G.add_edge('mmi','mmi')
G.edge['mmi']['mmi']['write-read'] = '[open open][write read]'
G.edge['mmi']['mmi']['fill'] = 'red'
G.add_edge('mmi','mmi')
G.edge['mmi']['mmi']['write-read'] = '[open open][write read][append read]'
G.add_edge('mmi','mm-pp-daemon')
G.edge['mmi']['mm-pp-daemon']['write-read'] = '[open open][write read]'
G.edge['mmi']['mm-pp-daemon']['fill'] = 'red'
G.add_edge('mmi','mm-pp-daemon')
G.edge['mmi']['mm-pp-daemon']['write-read'] = '[open open][write read][append read]'
G.add_edge('mmi','mm-qcamera-daemon')
G.edge['mmi']['mm-qcamera-daemon']['write-read'] = '[open open][write read]'
G.edge['mmi']['mm-qcamera-daemon']['fill'] = 'red'
G.add_edge('mmi','mm-qcamera-daemon')
G.edge['mmi']['mm-qcamera-daemon']['write-read'] = '[open open][write read][append read]'
G.add_edge('mmi','newAttr96')
G.edge['mmi']['newAttr96']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['mmi']['newAttr96']['fill'] = 'red'
G.add_edge('mmi','newAttr96')
G.edge['mmi']['newAttr96']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('mmi','radio')
G.edge['mmi']['radio']['write-read'] = '[open open][write read]'
G.edge['mmi']['radio']['fill'] = 'red'
G.add_edge('mmi','radio')
G.edge['mmi']['radio']['write-read'] = '[open open][write read][append read]'
G.add_edge('mmi','s_system_app')
G.edge['mmi']['s_system_app']['write-read'] = '[open open][write read]'
G.edge['mmi']['s_system_app']['fill'] = 'red'
G.add_edge('mmi','s_system_app')
G.edge['mmi']['s_system_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('mmi','surfaceflinger')
G.edge['mmi']['surfaceflinger']['write-read'] = '[open open][write read]'
G.edge['mmi']['surfaceflinger']['fill'] = 'red'
G.add_edge('mmi','surfaceflinger')
G.edge['mmi']['surfaceflinger']['write-read'] = '[open open][write read][append read]'
G.add_edge('mmi','system_app')
G.edge['mmi']['system_app']['write-read'] = '[open open][write read]'
G.edge['mmi']['system_app']['fill'] = 'red'
G.add_edge('mmi','system_app')
G.edge['mmi']['system_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('mmi','wfd_app')
G.edge['mmi']['wfd_app']['write-read'] = '[open open][write read]'
G.edge['mmi']['wfd_app']['fill'] = 'red'
G.add_edge('mmi','wfd_app')
G.edge['mmi']['wfd_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('mmi','wfdservice')
G.edge['mmi']['wfdservice']['write-read'] = '[open open][write read]'
G.edge['mmi']['wfdservice']['fill'] = 'red'
G.add_edge('mmi','wfdservice')
G.edge['mmi']['wfdservice']['write-read'] = '[open open][write read][append read]'
G.add_edge('mmi','zygote')
G.edge['mmi']['zygote']['write-read'] = '[open open][write read]'
G.edge['mmi']['zygote']['fill'] = 'red'
G.add_edge('mmi','zygote')
G.edge['mmi']['zygote']['write-read'] = '[open open][write read][append read]'
G.add_edge('mm-pp-daemon','bintvoutservice')
G.edge['mm-pp-daemon']['bintvoutservice']['write-read'] = '[open open]'
G.add_edge('mm-pp-daemon','bootanim')
G.edge['mm-pp-daemon']['bootanim']['write-read'] = '[open open]'
G.add_edge('mm-pp-daemon','commonplatformappdomain')
G.edge['mm-pp-daemon']['commonplatformappdomain']['write-read'] = '[open open]'
G.add_edge('mm-pp-daemon','fixmo_app')
G.edge['mm-pp-daemon']['fixmo_app']['write-read'] = '[open open]'
G.add_edge('mm-pp-daemon','good_app')
G.edge['mm-pp-daemon']['good_app']['write-read'] = '[open open]'
G.add_edge('mm-pp-daemon','healthd')
G.edge['mm-pp-daemon']['healthd']['write-read'] = '[open open]'
G.add_edge('mm-pp-daemon','ime_app')
G.edge['mm-pp-daemon']['ime_app']['write-read'] = '[open open]'
G.add_edge('mm-pp-daemon','isolated_app')
G.edge['mm-pp-daemon']['isolated_app']['write-read'] = '[open open]'
G.add_edge('mm-pp-daemon','untrusted_app')
G.edge['mm-pp-daemon']['untrusted_app']['write-read'] = '[open open]'
G.add_edge('mm-pp-daemon','umcagent_app')
G.edge['mm-pp-daemon']['umcagent_app']['write-read'] = '[open open]'
G.add_edge('mm-pp-daemon','vpn_untrusted_app')
G.edge['mm-pp-daemon']['vpn_untrusted_app']['write-read'] = '[open open]'
G.add_edge('mm-pp-daemon','trustonicpartner_app')
G.edge['mm-pp-daemon']['trustonicpartner_app']['write-read'] = '[open open]'
G.add_edge('mm-pp-daemon','llk_untrusted_app')
G.edge['mm-pp-daemon']['llk_untrusted_app']['write-read'] = '[open open]'
G.add_edge('mm-pp-daemon','filtered_untrusted_app')
G.edge['mm-pp-daemon']['filtered_untrusted_app']['write-read'] = '[open open]'
G.add_edge('mm-pp-daemon','filtered_google_app')
G.edge['mm-pp-daemon']['filtered_google_app']['write-read'] = '[open open]'
G.add_edge('mm-pp-daemon','knox_untrusted_app')
G.edge['mm-pp-daemon']['knox_untrusted_app']['write-read'] = '[open open]'
G.add_edge('mm-pp-daemon','irm_app')
G.edge['mm-pp-daemon']['irm_app']['write-read'] = '[open open]'
G.add_edge('mm-pp-daemon','gad_untrusted_app')
G.edge['mm-pp-daemon']['gad_untrusted_app']['write-read'] = '[open open]'
G.add_edge('mm-pp-daemon','carrier_app')
G.edge['mm-pp-daemon']['carrier_app']['write-read'] = '[open open]'
G.add_edge('mm-pp-daemon','lpm')
G.edge['mm-pp-daemon']['lpm']['write-read'] = '[open open]'
G.add_edge('mm-pp-daemon','mmi')
G.edge['mm-pp-daemon']['mmi']['write-read'] = '[open open]'
G.add_edge('mm-pp-daemon','mm-pp-daemon')
G.edge['mm-pp-daemon']['mm-pp-daemon']['write-read'] = '[open open]'
G.add_edge('mm-pp-daemon','mm-qcamera-daemon')
G.edge['mm-pp-daemon']['mm-qcamera-daemon']['write-read'] = '[open open]'
G.add_edge('mm-pp-daemon','newAttr96')
G.edge['mm-pp-daemon']['newAttr96']['write-read'] = '[open open]'
G.add_edge('mm-pp-daemon','radio')
G.edge['mm-pp-daemon']['radio']['write-read'] = '[open open]'
G.add_edge('mm-pp-daemon','s_system_app')
G.edge['mm-pp-daemon']['s_system_app']['write-read'] = '[open open]'
G.add_edge('mm-pp-daemon','surfaceflinger')
G.edge['mm-pp-daemon']['surfaceflinger']['write-read'] = '[open open]'
G.add_edge('mm-pp-daemon','system_app')
G.edge['mm-pp-daemon']['system_app']['write-read'] = '[open open]'
G.add_edge('mm-pp-daemon','wfd_app')
G.edge['mm-pp-daemon']['wfd_app']['write-read'] = '[open open]'
G.add_edge('mm-pp-daemon','wfdservice')
G.edge['mm-pp-daemon']['wfdservice']['write-read'] = '[open open]'
G.add_edge('mm-pp-daemon','zygote')
G.edge['mm-pp-daemon']['zygote']['write-read'] = '[open open]'
G.add_edge('mm-pp-daemon','isolated_app')
G.edge['mm-pp-daemon']['isolated_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('mm-pp-daemon','untrusted_app')
G.edge['mm-pp-daemon']['untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('mm-pp-daemon','umcagent_app')
G.edge['mm-pp-daemon']['umcagent_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('mm-pp-daemon','vpn_untrusted_app')
G.edge['mm-pp-daemon']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('mm-pp-daemon','trustonicpartner_app')
G.edge['mm-pp-daemon']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('mm-pp-daemon','llk_untrusted_app')
G.edge['mm-pp-daemon']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('mm-pp-daemon','filtered_untrusted_app')
G.edge['mm-pp-daemon']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('mm-pp-daemon','filtered_google_app')
G.edge['mm-pp-daemon']['filtered_google_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('mm-pp-daemon','knox_untrusted_app')
G.edge['mm-pp-daemon']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('mm-pp-daemon','irm_app')
G.edge['mm-pp-daemon']['irm_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('mm-pp-daemon','gad_untrusted_app')
G.edge['mm-pp-daemon']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('mm-pp-daemon','carrier_app')
G.edge['mm-pp-daemon']['carrier_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('mm-pp-daemon','newAttr96')
G.edge['mm-pp-daemon']['newAttr96']['write-read'] = '[open open][setattr getattr]'
G.add_edge('mm-pp-daemon','bintvoutservice')
G.edge['mm-pp-daemon']['bintvoutservice']['write-read'] = '[open open][write read]'
G.edge['mm-pp-daemon']['bintvoutservice']['fill'] = 'red'
G.add_edge('mm-pp-daemon','bintvoutservice')
G.edge['mm-pp-daemon']['bintvoutservice']['write-read'] = '[open open][write read][append read]'
G.add_edge('mm-pp-daemon','bootanim')
G.edge['mm-pp-daemon']['bootanim']['write-read'] = '[open open][write read]'
G.edge['mm-pp-daemon']['bootanim']['fill'] = 'red'
G.add_edge('mm-pp-daemon','bootanim')
G.edge['mm-pp-daemon']['bootanim']['write-read'] = '[open open][write read][append read]'
G.add_edge('mm-pp-daemon','commonplatformappdomain')
G.edge['mm-pp-daemon']['commonplatformappdomain']['write-read'] = '[open open][write read]'
G.edge['mm-pp-daemon']['commonplatformappdomain']['fill'] = 'red'
G.add_edge('mm-pp-daemon','commonplatformappdomain')
G.edge['mm-pp-daemon']['commonplatformappdomain']['write-read'] = '[open open][write read][append read]'
G.add_edge('mm-pp-daemon','fixmo_app')
G.edge['mm-pp-daemon']['fixmo_app']['write-read'] = '[open open][write read]'
G.edge['mm-pp-daemon']['fixmo_app']['fill'] = 'red'
G.add_edge('mm-pp-daemon','fixmo_app')
G.edge['mm-pp-daemon']['fixmo_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('mm-pp-daemon','good_app')
G.edge['mm-pp-daemon']['good_app']['write-read'] = '[open open][write read]'
G.edge['mm-pp-daemon']['good_app']['fill'] = 'red'
G.add_edge('mm-pp-daemon','good_app')
G.edge['mm-pp-daemon']['good_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('mm-pp-daemon','healthd')
G.edge['mm-pp-daemon']['healthd']['write-read'] = '[open open][write read]'
G.edge['mm-pp-daemon']['healthd']['fill'] = 'red'
G.add_edge('mm-pp-daemon','healthd')
G.edge['mm-pp-daemon']['healthd']['write-read'] = '[open open][write read][append read]'
G.add_edge('mm-pp-daemon','ime_app')
G.edge['mm-pp-daemon']['ime_app']['write-read'] = '[open open][write read]'
G.edge['mm-pp-daemon']['ime_app']['fill'] = 'red'
G.add_edge('mm-pp-daemon','ime_app')
G.edge['mm-pp-daemon']['ime_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('mm-pp-daemon','isolated_app')
G.edge['mm-pp-daemon']['isolated_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('mm-pp-daemon','untrusted_app')
G.edge['mm-pp-daemon']['untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('mm-pp-daemon','umcagent_app')
G.edge['mm-pp-daemon']['umcagent_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('mm-pp-daemon','vpn_untrusted_app')
G.edge['mm-pp-daemon']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('mm-pp-daemon','trustonicpartner_app')
G.edge['mm-pp-daemon']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('mm-pp-daemon','llk_untrusted_app')
G.edge['mm-pp-daemon']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('mm-pp-daemon','filtered_untrusted_app')
G.edge['mm-pp-daemon']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('mm-pp-daemon','filtered_google_app')
G.edge['mm-pp-daemon']['filtered_google_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('mm-pp-daemon','knox_untrusted_app')
G.edge['mm-pp-daemon']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('mm-pp-daemon','irm_app')
G.edge['mm-pp-daemon']['irm_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('mm-pp-daemon','gad_untrusted_app')
G.edge['mm-pp-daemon']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('mm-pp-daemon','carrier_app')
G.edge['mm-pp-daemon']['carrier_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('mm-pp-daemon','lpm')
G.edge['mm-pp-daemon']['lpm']['write-read'] = '[open open][write read]'
G.edge['mm-pp-daemon']['lpm']['fill'] = 'red'
G.add_edge('mm-pp-daemon','lpm')
G.edge['mm-pp-daemon']['lpm']['write-read'] = '[open open][write read][append read]'
G.add_edge('mm-pp-daemon','mmi')
G.edge['mm-pp-daemon']['mmi']['write-read'] = '[open open][write read]'
G.edge['mm-pp-daemon']['mmi']['fill'] = 'red'
G.add_edge('mm-pp-daemon','mmi')
G.edge['mm-pp-daemon']['mmi']['write-read'] = '[open open][write read][append read]'
G.add_edge('mm-pp-daemon','mm-pp-daemon')
G.edge['mm-pp-daemon']['mm-pp-daemon']['write-read'] = '[open open][write read]'
G.edge['mm-pp-daemon']['mm-pp-daemon']['fill'] = 'red'
G.add_edge('mm-pp-daemon','mm-pp-daemon')
G.edge['mm-pp-daemon']['mm-pp-daemon']['write-read'] = '[open open][write read][append read]'
G.add_edge('mm-pp-daemon','mm-qcamera-daemon')
G.edge['mm-pp-daemon']['mm-qcamera-daemon']['write-read'] = '[open open][write read]'
G.edge['mm-pp-daemon']['mm-qcamera-daemon']['fill'] = 'red'
G.add_edge('mm-pp-daemon','mm-qcamera-daemon')
G.edge['mm-pp-daemon']['mm-qcamera-daemon']['write-read'] = '[open open][write read][append read]'
G.add_edge('mm-pp-daemon','newAttr96')
G.edge['mm-pp-daemon']['newAttr96']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['mm-pp-daemon']['newAttr96']['fill'] = 'red'
G.add_edge('mm-pp-daemon','newAttr96')
G.edge['mm-pp-daemon']['newAttr96']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('mm-pp-daemon','radio')
G.edge['mm-pp-daemon']['radio']['write-read'] = '[open open][write read]'
G.edge['mm-pp-daemon']['radio']['fill'] = 'red'
G.add_edge('mm-pp-daemon','radio')
G.edge['mm-pp-daemon']['radio']['write-read'] = '[open open][write read][append read]'
G.add_edge('mm-pp-daemon','s_system_app')
G.edge['mm-pp-daemon']['s_system_app']['write-read'] = '[open open][write read]'
G.edge['mm-pp-daemon']['s_system_app']['fill'] = 'red'
G.add_edge('mm-pp-daemon','s_system_app')
G.edge['mm-pp-daemon']['s_system_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('mm-pp-daemon','surfaceflinger')
G.edge['mm-pp-daemon']['surfaceflinger']['write-read'] = '[open open][write read]'
G.edge['mm-pp-daemon']['surfaceflinger']['fill'] = 'red'
G.add_edge('mm-pp-daemon','surfaceflinger')
G.edge['mm-pp-daemon']['surfaceflinger']['write-read'] = '[open open][write read][append read]'
G.add_edge('mm-pp-daemon','system_app')
G.edge['mm-pp-daemon']['system_app']['write-read'] = '[open open][write read]'
G.edge['mm-pp-daemon']['system_app']['fill'] = 'red'
G.add_edge('mm-pp-daemon','system_app')
G.edge['mm-pp-daemon']['system_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('mm-pp-daemon','wfd_app')
G.edge['mm-pp-daemon']['wfd_app']['write-read'] = '[open open][write read]'
G.edge['mm-pp-daemon']['wfd_app']['fill'] = 'red'
G.add_edge('mm-pp-daemon','wfd_app')
G.edge['mm-pp-daemon']['wfd_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('mm-pp-daemon','wfdservice')
G.edge['mm-pp-daemon']['wfdservice']['write-read'] = '[open open][write read]'
G.edge['mm-pp-daemon']['wfdservice']['fill'] = 'red'
G.add_edge('mm-pp-daemon','wfdservice')
G.edge['mm-pp-daemon']['wfdservice']['write-read'] = '[open open][write read][append read]'
G.add_edge('mm-pp-daemon','zygote')
G.edge['mm-pp-daemon']['zygote']['write-read'] = '[open open][write read]'
G.edge['mm-pp-daemon']['zygote']['fill'] = 'red'
G.add_edge('mm-pp-daemon','zygote')
G.edge['mm-pp-daemon']['zygote']['write-read'] = '[open open][write read][append read]'
G.add_edge('mm-qcamera-daemon','bintvoutservice')
G.edge['mm-qcamera-daemon']['bintvoutservice']['write-read'] = '[open open]'
G.add_edge('mm-qcamera-daemon','bootanim')
G.edge['mm-qcamera-daemon']['bootanim']['write-read'] = '[open open]'
G.add_edge('mm-qcamera-daemon','commonplatformappdomain')
G.edge['mm-qcamera-daemon']['commonplatformappdomain']['write-read'] = '[open open]'
G.add_edge('mm-qcamera-daemon','fixmo_app')
G.edge['mm-qcamera-daemon']['fixmo_app']['write-read'] = '[open open]'
G.add_edge('mm-qcamera-daemon','good_app')
G.edge['mm-qcamera-daemon']['good_app']['write-read'] = '[open open]'
G.add_edge('mm-qcamera-daemon','healthd')
G.edge['mm-qcamera-daemon']['healthd']['write-read'] = '[open open]'
G.add_edge('mm-qcamera-daemon','ime_app')
G.edge['mm-qcamera-daemon']['ime_app']['write-read'] = '[open open]'
G.add_edge('mm-qcamera-daemon','isolated_app')
G.edge['mm-qcamera-daemon']['isolated_app']['write-read'] = '[open open]'
G.add_edge('mm-qcamera-daemon','untrusted_app')
G.edge['mm-qcamera-daemon']['untrusted_app']['write-read'] = '[open open]'
G.add_edge('mm-qcamera-daemon','umcagent_app')
G.edge['mm-qcamera-daemon']['umcagent_app']['write-read'] = '[open open]'
G.add_edge('mm-qcamera-daemon','vpn_untrusted_app')
G.edge['mm-qcamera-daemon']['vpn_untrusted_app']['write-read'] = '[open open]'
G.add_edge('mm-qcamera-daemon','trustonicpartner_app')
G.edge['mm-qcamera-daemon']['trustonicpartner_app']['write-read'] = '[open open]'
G.add_edge('mm-qcamera-daemon','llk_untrusted_app')
G.edge['mm-qcamera-daemon']['llk_untrusted_app']['write-read'] = '[open open]'
G.add_edge('mm-qcamera-daemon','filtered_untrusted_app')
G.edge['mm-qcamera-daemon']['filtered_untrusted_app']['write-read'] = '[open open]'
G.add_edge('mm-qcamera-daemon','filtered_google_app')
G.edge['mm-qcamera-daemon']['filtered_google_app']['write-read'] = '[open open]'
G.add_edge('mm-qcamera-daemon','knox_untrusted_app')
G.edge['mm-qcamera-daemon']['knox_untrusted_app']['write-read'] = '[open open]'
G.add_edge('mm-qcamera-daemon','irm_app')
G.edge['mm-qcamera-daemon']['irm_app']['write-read'] = '[open open]'
G.add_edge('mm-qcamera-daemon','gad_untrusted_app')
G.edge['mm-qcamera-daemon']['gad_untrusted_app']['write-read'] = '[open open]'
G.add_edge('mm-qcamera-daemon','carrier_app')
G.edge['mm-qcamera-daemon']['carrier_app']['write-read'] = '[open open]'
G.add_edge('mm-qcamera-daemon','lpm')
G.edge['mm-qcamera-daemon']['lpm']['write-read'] = '[open open]'
G.add_edge('mm-qcamera-daemon','mmi')
G.edge['mm-qcamera-daemon']['mmi']['write-read'] = '[open open]'
G.add_edge('mm-qcamera-daemon','mm-pp-daemon')
G.edge['mm-qcamera-daemon']['mm-pp-daemon']['write-read'] = '[open open]'
G.add_edge('mm-qcamera-daemon','mm-qcamera-daemon')
G.edge['mm-qcamera-daemon']['mm-qcamera-daemon']['write-read'] = '[open open]'
G.add_edge('mm-qcamera-daemon','newAttr96')
G.edge['mm-qcamera-daemon']['newAttr96']['write-read'] = '[open open]'
G.add_edge('mm-qcamera-daemon','radio')
G.edge['mm-qcamera-daemon']['radio']['write-read'] = '[open open]'
G.add_edge('mm-qcamera-daemon','s_system_app')
G.edge['mm-qcamera-daemon']['s_system_app']['write-read'] = '[open open]'
G.add_edge('mm-qcamera-daemon','surfaceflinger')
G.edge['mm-qcamera-daemon']['surfaceflinger']['write-read'] = '[open open]'
G.add_edge('mm-qcamera-daemon','system_app')
G.edge['mm-qcamera-daemon']['system_app']['write-read'] = '[open open]'
G.add_edge('mm-qcamera-daemon','wfd_app')
G.edge['mm-qcamera-daemon']['wfd_app']['write-read'] = '[open open]'
G.add_edge('mm-qcamera-daemon','wfdservice')
G.edge['mm-qcamera-daemon']['wfdservice']['write-read'] = '[open open]'
G.add_edge('mm-qcamera-daemon','zygote')
G.edge['mm-qcamera-daemon']['zygote']['write-read'] = '[open open]'
G.add_edge('mm-qcamera-daemon','isolated_app')
G.edge['mm-qcamera-daemon']['isolated_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('mm-qcamera-daemon','untrusted_app')
G.edge['mm-qcamera-daemon']['untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('mm-qcamera-daemon','umcagent_app')
G.edge['mm-qcamera-daemon']['umcagent_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('mm-qcamera-daemon','vpn_untrusted_app')
G.edge['mm-qcamera-daemon']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('mm-qcamera-daemon','trustonicpartner_app')
G.edge['mm-qcamera-daemon']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('mm-qcamera-daemon','llk_untrusted_app')
G.edge['mm-qcamera-daemon']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('mm-qcamera-daemon','filtered_untrusted_app')
G.edge['mm-qcamera-daemon']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('mm-qcamera-daemon','filtered_google_app')
G.edge['mm-qcamera-daemon']['filtered_google_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('mm-qcamera-daemon','knox_untrusted_app')
G.edge['mm-qcamera-daemon']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('mm-qcamera-daemon','irm_app')
G.edge['mm-qcamera-daemon']['irm_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('mm-qcamera-daemon','gad_untrusted_app')
G.edge['mm-qcamera-daemon']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('mm-qcamera-daemon','carrier_app')
G.edge['mm-qcamera-daemon']['carrier_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('mm-qcamera-daemon','newAttr96')
G.edge['mm-qcamera-daemon']['newAttr96']['write-read'] = '[open open][setattr getattr]'
G.add_edge('mm-qcamera-daemon','bintvoutservice')
G.edge['mm-qcamera-daemon']['bintvoutservice']['write-read'] = '[open open][write read]'
G.edge['mm-qcamera-daemon']['bintvoutservice']['fill'] = 'red'
G.add_edge('mm-qcamera-daemon','bintvoutservice')
G.edge['mm-qcamera-daemon']['bintvoutservice']['write-read'] = '[open open][write read][append read]'
G.add_edge('mm-qcamera-daemon','bootanim')
G.edge['mm-qcamera-daemon']['bootanim']['write-read'] = '[open open][write read]'
G.edge['mm-qcamera-daemon']['bootanim']['fill'] = 'red'
G.add_edge('mm-qcamera-daemon','bootanim')
G.edge['mm-qcamera-daemon']['bootanim']['write-read'] = '[open open][write read][append read]'
G.add_edge('mm-qcamera-daemon','commonplatformappdomain')
G.edge['mm-qcamera-daemon']['commonplatformappdomain']['write-read'] = '[open open][write read]'
G.edge['mm-qcamera-daemon']['commonplatformappdomain']['fill'] = 'red'
G.add_edge('mm-qcamera-daemon','commonplatformappdomain')
G.edge['mm-qcamera-daemon']['commonplatformappdomain']['write-read'] = '[open open][write read][append read]'
G.add_edge('mm-qcamera-daemon','fixmo_app')
G.edge['mm-qcamera-daemon']['fixmo_app']['write-read'] = '[open open][write read]'
G.edge['mm-qcamera-daemon']['fixmo_app']['fill'] = 'red'
G.add_edge('mm-qcamera-daemon','fixmo_app')
G.edge['mm-qcamera-daemon']['fixmo_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('mm-qcamera-daemon','good_app')
G.edge['mm-qcamera-daemon']['good_app']['write-read'] = '[open open][write read]'
G.edge['mm-qcamera-daemon']['good_app']['fill'] = 'red'
G.add_edge('mm-qcamera-daemon','good_app')
G.edge['mm-qcamera-daemon']['good_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('mm-qcamera-daemon','healthd')
G.edge['mm-qcamera-daemon']['healthd']['write-read'] = '[open open][write read]'
G.edge['mm-qcamera-daemon']['healthd']['fill'] = 'red'
G.add_edge('mm-qcamera-daemon','healthd')
G.edge['mm-qcamera-daemon']['healthd']['write-read'] = '[open open][write read][append read]'
G.add_edge('mm-qcamera-daemon','ime_app')
G.edge['mm-qcamera-daemon']['ime_app']['write-read'] = '[open open][write read]'
G.edge['mm-qcamera-daemon']['ime_app']['fill'] = 'red'
G.add_edge('mm-qcamera-daemon','ime_app')
G.edge['mm-qcamera-daemon']['ime_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('mm-qcamera-daemon','isolated_app')
G.edge['mm-qcamera-daemon']['isolated_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('mm-qcamera-daemon','untrusted_app')
G.edge['mm-qcamera-daemon']['untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('mm-qcamera-daemon','umcagent_app')
G.edge['mm-qcamera-daemon']['umcagent_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('mm-qcamera-daemon','vpn_untrusted_app')
G.edge['mm-qcamera-daemon']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('mm-qcamera-daemon','trustonicpartner_app')
G.edge['mm-qcamera-daemon']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('mm-qcamera-daemon','llk_untrusted_app')
G.edge['mm-qcamera-daemon']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('mm-qcamera-daemon','filtered_untrusted_app')
G.edge['mm-qcamera-daemon']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('mm-qcamera-daemon','filtered_google_app')
G.edge['mm-qcamera-daemon']['filtered_google_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('mm-qcamera-daemon','knox_untrusted_app')
G.edge['mm-qcamera-daemon']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('mm-qcamera-daemon','irm_app')
G.edge['mm-qcamera-daemon']['irm_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('mm-qcamera-daemon','gad_untrusted_app')
G.edge['mm-qcamera-daemon']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('mm-qcamera-daemon','carrier_app')
G.edge['mm-qcamera-daemon']['carrier_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('mm-qcamera-daemon','lpm')
G.edge['mm-qcamera-daemon']['lpm']['write-read'] = '[open open][write read]'
G.edge['mm-qcamera-daemon']['lpm']['fill'] = 'red'
G.add_edge('mm-qcamera-daemon','lpm')
G.edge['mm-qcamera-daemon']['lpm']['write-read'] = '[open open][write read][append read]'
G.add_edge('mm-qcamera-daemon','mmi')
G.edge['mm-qcamera-daemon']['mmi']['write-read'] = '[open open][write read]'
G.edge['mm-qcamera-daemon']['mmi']['fill'] = 'red'
G.add_edge('mm-qcamera-daemon','mmi')
G.edge['mm-qcamera-daemon']['mmi']['write-read'] = '[open open][write read][append read]'
G.add_edge('mm-qcamera-daemon','mm-pp-daemon')
G.edge['mm-qcamera-daemon']['mm-pp-daemon']['write-read'] = '[open open][write read]'
G.edge['mm-qcamera-daemon']['mm-pp-daemon']['fill'] = 'red'
G.add_edge('mm-qcamera-daemon','mm-pp-daemon')
G.edge['mm-qcamera-daemon']['mm-pp-daemon']['write-read'] = '[open open][write read][append read]'
G.add_edge('mm-qcamera-daemon','mm-qcamera-daemon')
G.edge['mm-qcamera-daemon']['mm-qcamera-daemon']['write-read'] = '[open open][write read]'
G.edge['mm-qcamera-daemon']['mm-qcamera-daemon']['fill'] = 'red'
G.add_edge('mm-qcamera-daemon','mm-qcamera-daemon')
G.edge['mm-qcamera-daemon']['mm-qcamera-daemon']['write-read'] = '[open open][write read][append read]'
G.add_edge('mm-qcamera-daemon','newAttr96')
G.edge['mm-qcamera-daemon']['newAttr96']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['mm-qcamera-daemon']['newAttr96']['fill'] = 'red'
G.add_edge('mm-qcamera-daemon','newAttr96')
G.edge['mm-qcamera-daemon']['newAttr96']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('mm-qcamera-daemon','radio')
G.edge['mm-qcamera-daemon']['radio']['write-read'] = '[open open][write read]'
G.edge['mm-qcamera-daemon']['radio']['fill'] = 'red'
G.add_edge('mm-qcamera-daemon','radio')
G.edge['mm-qcamera-daemon']['radio']['write-read'] = '[open open][write read][append read]'
G.add_edge('mm-qcamera-daemon','s_system_app')
G.edge['mm-qcamera-daemon']['s_system_app']['write-read'] = '[open open][write read]'
G.edge['mm-qcamera-daemon']['s_system_app']['fill'] = 'red'
G.add_edge('mm-qcamera-daemon','s_system_app')
G.edge['mm-qcamera-daemon']['s_system_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('mm-qcamera-daemon','surfaceflinger')
G.edge['mm-qcamera-daemon']['surfaceflinger']['write-read'] = '[open open][write read]'
G.edge['mm-qcamera-daemon']['surfaceflinger']['fill'] = 'red'
G.add_edge('mm-qcamera-daemon','surfaceflinger')
G.edge['mm-qcamera-daemon']['surfaceflinger']['write-read'] = '[open open][write read][append read]'
G.add_edge('mm-qcamera-daemon','system_app')
G.edge['mm-qcamera-daemon']['system_app']['write-read'] = '[open open][write read]'
G.edge['mm-qcamera-daemon']['system_app']['fill'] = 'red'
G.add_edge('mm-qcamera-daemon','system_app')
G.edge['mm-qcamera-daemon']['system_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('mm-qcamera-daemon','wfd_app')
G.edge['mm-qcamera-daemon']['wfd_app']['write-read'] = '[open open][write read]'
G.edge['mm-qcamera-daemon']['wfd_app']['fill'] = 'red'
G.add_edge('mm-qcamera-daemon','wfd_app')
G.edge['mm-qcamera-daemon']['wfd_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('mm-qcamera-daemon','wfdservice')
G.edge['mm-qcamera-daemon']['wfdservice']['write-read'] = '[open open][write read]'
G.edge['mm-qcamera-daemon']['wfdservice']['fill'] = 'red'
G.add_edge('mm-qcamera-daemon','wfdservice')
G.edge['mm-qcamera-daemon']['wfdservice']['write-read'] = '[open open][write read][append read]'
G.add_edge('mm-qcamera-daemon','zygote')
G.edge['mm-qcamera-daemon']['zygote']['write-read'] = '[open open][write read]'
G.edge['mm-qcamera-daemon']['zygote']['fill'] = 'red'
G.add_edge('mm-qcamera-daemon','zygote')
G.edge['mm-qcamera-daemon']['zygote']['write-read'] = '[open open][write read][append read]'
G.add_edge('newAttr96','bintvoutservice')
G.edge['newAttr96']['bintvoutservice']['write-read'] = '[open open]'
G.add_edge('newAttr96','bootanim')
G.edge['newAttr96']['bootanim']['write-read'] = '[open open]'
G.add_edge('newAttr96','commonplatformappdomain')
G.edge['newAttr96']['commonplatformappdomain']['write-read'] = '[open open]'
G.add_edge('newAttr96','fixmo_app')
G.edge['newAttr96']['fixmo_app']['write-read'] = '[open open]'
G.add_edge('newAttr96','good_app')
G.edge['newAttr96']['good_app']['write-read'] = '[open open]'
G.add_edge('newAttr96','healthd')
G.edge['newAttr96']['healthd']['write-read'] = '[open open]'
G.add_edge('newAttr96','ime_app')
G.edge['newAttr96']['ime_app']['write-read'] = '[open open]'
G.add_edge('newAttr96','isolated_app')
G.edge['newAttr96']['isolated_app']['write-read'] = '[open open]'
G.add_edge('newAttr96','untrusted_app')
G.edge['newAttr96']['untrusted_app']['write-read'] = '[open open]'
G.add_edge('newAttr96','umcagent_app')
G.edge['newAttr96']['umcagent_app']['write-read'] = '[open open]'
G.add_edge('newAttr96','vpn_untrusted_app')
G.edge['newAttr96']['vpn_untrusted_app']['write-read'] = '[open open]'
G.add_edge('newAttr96','trustonicpartner_app')
G.edge['newAttr96']['trustonicpartner_app']['write-read'] = '[open open]'
G.add_edge('newAttr96','llk_untrusted_app')
G.edge['newAttr96']['llk_untrusted_app']['write-read'] = '[open open]'
G.add_edge('newAttr96','filtered_untrusted_app')
G.edge['newAttr96']['filtered_untrusted_app']['write-read'] = '[open open]'
G.add_edge('newAttr96','filtered_google_app')
G.edge['newAttr96']['filtered_google_app']['write-read'] = '[open open]'
G.add_edge('newAttr96','knox_untrusted_app')
G.edge['newAttr96']['knox_untrusted_app']['write-read'] = '[open open]'
G.add_edge('newAttr96','irm_app')
G.edge['newAttr96']['irm_app']['write-read'] = '[open open]'
G.add_edge('newAttr96','gad_untrusted_app')
G.edge['newAttr96']['gad_untrusted_app']['write-read'] = '[open open]'
G.add_edge('newAttr96','carrier_app')
G.edge['newAttr96']['carrier_app']['write-read'] = '[open open]'
G.add_edge('newAttr96','lpm')
G.edge['newAttr96']['lpm']['write-read'] = '[open open]'
G.add_edge('newAttr96','mmi')
G.edge['newAttr96']['mmi']['write-read'] = '[open open]'
G.add_edge('newAttr96','mm-pp-daemon')
G.edge['newAttr96']['mm-pp-daemon']['write-read'] = '[open open]'
G.add_edge('newAttr96','mm-qcamera-daemon')
G.edge['newAttr96']['mm-qcamera-daemon']['write-read'] = '[open open]'
G.add_edge('newAttr96','newAttr96')
G.edge['newAttr96']['newAttr96']['write-read'] = '[open open]'
G.add_edge('newAttr96','radio')
G.edge['newAttr96']['radio']['write-read'] = '[open open]'
G.add_edge('newAttr96','s_system_app')
G.edge['newAttr96']['s_system_app']['write-read'] = '[open open]'
G.add_edge('newAttr96','surfaceflinger')
G.edge['newAttr96']['surfaceflinger']['write-read'] = '[open open]'
G.add_edge('newAttr96','system_app')
G.edge['newAttr96']['system_app']['write-read'] = '[open open]'
G.add_edge('newAttr96','wfd_app')
G.edge['newAttr96']['wfd_app']['write-read'] = '[open open]'
G.add_edge('newAttr96','wfdservice')
G.edge['newAttr96']['wfdservice']['write-read'] = '[open open]'
G.add_edge('newAttr96','zygote')
G.edge['newAttr96']['zygote']['write-read'] = '[open open]'
G.add_edge('newAttr96','isolated_app')
G.edge['newAttr96']['isolated_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('newAttr96','untrusted_app')
G.edge['newAttr96']['untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('newAttr96','umcagent_app')
G.edge['newAttr96']['umcagent_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('newAttr96','vpn_untrusted_app')
G.edge['newAttr96']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('newAttr96','trustonicpartner_app')
G.edge['newAttr96']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('newAttr96','llk_untrusted_app')
G.edge['newAttr96']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('newAttr96','filtered_untrusted_app')
G.edge['newAttr96']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('newAttr96','filtered_google_app')
G.edge['newAttr96']['filtered_google_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('newAttr96','knox_untrusted_app')
G.edge['newAttr96']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('newAttr96','irm_app')
G.edge['newAttr96']['irm_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('newAttr96','gad_untrusted_app')
G.edge['newAttr96']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('newAttr96','carrier_app')
G.edge['newAttr96']['carrier_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('newAttr96','newAttr96')
G.edge['newAttr96']['newAttr96']['write-read'] = '[open open][setattr getattr]'
G.add_edge('newAttr96','bintvoutservice')
G.edge['newAttr96']['bintvoutservice']['write-read'] = '[open open][write read]'
G.edge['newAttr96']['bintvoutservice']['fill'] = 'red'
G.add_edge('newAttr96','bintvoutservice')
G.edge['newAttr96']['bintvoutservice']['write-read'] = '[open open][write read][append read]'
G.add_edge('newAttr96','bootanim')
G.edge['newAttr96']['bootanim']['write-read'] = '[open open][write read]'
G.edge['newAttr96']['bootanim']['fill'] = 'red'
G.add_edge('newAttr96','bootanim')
G.edge['newAttr96']['bootanim']['write-read'] = '[open open][write read][append read]'
G.add_edge('newAttr96','commonplatformappdomain')
G.edge['newAttr96']['commonplatformappdomain']['write-read'] = '[open open][write read]'
G.edge['newAttr96']['commonplatformappdomain']['fill'] = 'red'
G.add_edge('newAttr96','commonplatformappdomain')
G.edge['newAttr96']['commonplatformappdomain']['write-read'] = '[open open][write read][append read]'
G.add_edge('newAttr96','fixmo_app')
G.edge['newAttr96']['fixmo_app']['write-read'] = '[open open][write read]'
G.edge['newAttr96']['fixmo_app']['fill'] = 'red'
G.add_edge('newAttr96','fixmo_app')
G.edge['newAttr96']['fixmo_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('newAttr96','good_app')
G.edge['newAttr96']['good_app']['write-read'] = '[open open][write read]'
G.edge['newAttr96']['good_app']['fill'] = 'red'
G.add_edge('newAttr96','good_app')
G.edge['newAttr96']['good_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('newAttr96','healthd')
G.edge['newAttr96']['healthd']['write-read'] = '[open open][write read]'
G.edge['newAttr96']['healthd']['fill'] = 'red'
G.add_edge('newAttr96','healthd')
G.edge['newAttr96']['healthd']['write-read'] = '[open open][write read][append read]'
G.add_edge('newAttr96','ime_app')
G.edge['newAttr96']['ime_app']['write-read'] = '[open open][write read]'
G.edge['newAttr96']['ime_app']['fill'] = 'red'
G.add_edge('newAttr96','ime_app')
G.edge['newAttr96']['ime_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('newAttr96','isolated_app')
G.edge['newAttr96']['isolated_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('newAttr96','untrusted_app')
G.edge['newAttr96']['untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('newAttr96','umcagent_app')
G.edge['newAttr96']['umcagent_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('newAttr96','vpn_untrusted_app')
G.edge['newAttr96']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('newAttr96','trustonicpartner_app')
G.edge['newAttr96']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('newAttr96','llk_untrusted_app')
G.edge['newAttr96']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('newAttr96','filtered_untrusted_app')
G.edge['newAttr96']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('newAttr96','filtered_google_app')
G.edge['newAttr96']['filtered_google_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('newAttr96','knox_untrusted_app')
G.edge['newAttr96']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('newAttr96','irm_app')
G.edge['newAttr96']['irm_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('newAttr96','gad_untrusted_app')
G.edge['newAttr96']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('newAttr96','carrier_app')
G.edge['newAttr96']['carrier_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('newAttr96','lpm')
G.edge['newAttr96']['lpm']['write-read'] = '[open open][write read]'
G.edge['newAttr96']['lpm']['fill'] = 'red'
G.add_edge('newAttr96','lpm')
G.edge['newAttr96']['lpm']['write-read'] = '[open open][write read][append read]'
G.add_edge('newAttr96','mmi')
G.edge['newAttr96']['mmi']['write-read'] = '[open open][write read]'
G.edge['newAttr96']['mmi']['fill'] = 'red'
G.add_edge('newAttr96','mmi')
G.edge['newAttr96']['mmi']['write-read'] = '[open open][write read][append read]'
G.add_edge('newAttr96','mm-pp-daemon')
G.edge['newAttr96']['mm-pp-daemon']['write-read'] = '[open open][write read]'
G.edge['newAttr96']['mm-pp-daemon']['fill'] = 'red'
G.add_edge('newAttr96','mm-pp-daemon')
G.edge['newAttr96']['mm-pp-daemon']['write-read'] = '[open open][write read][append read]'
G.add_edge('newAttr96','mm-qcamera-daemon')
G.edge['newAttr96']['mm-qcamera-daemon']['write-read'] = '[open open][write read]'
G.edge['newAttr96']['mm-qcamera-daemon']['fill'] = 'red'
G.add_edge('newAttr96','mm-qcamera-daemon')
G.edge['newAttr96']['mm-qcamera-daemon']['write-read'] = '[open open][write read][append read]'
G.add_edge('newAttr96','newAttr96')
G.edge['newAttr96']['newAttr96']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['newAttr96']['newAttr96']['fill'] = 'red'
G.add_edge('newAttr96','newAttr96')
G.edge['newAttr96']['newAttr96']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('newAttr96','radio')
G.edge['newAttr96']['radio']['write-read'] = '[open open][write read]'
G.edge['newAttr96']['radio']['fill'] = 'red'
G.add_edge('newAttr96','radio')
G.edge['newAttr96']['radio']['write-read'] = '[open open][write read][append read]'
G.add_edge('newAttr96','s_system_app')
G.edge['newAttr96']['s_system_app']['write-read'] = '[open open][write read]'
G.edge['newAttr96']['s_system_app']['fill'] = 'red'
G.add_edge('newAttr96','s_system_app')
G.edge['newAttr96']['s_system_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('newAttr96','surfaceflinger')
G.edge['newAttr96']['surfaceflinger']['write-read'] = '[open open][write read]'
G.edge['newAttr96']['surfaceflinger']['fill'] = 'red'
G.add_edge('newAttr96','surfaceflinger')
G.edge['newAttr96']['surfaceflinger']['write-read'] = '[open open][write read][append read]'
G.add_edge('newAttr96','system_app')
G.edge['newAttr96']['system_app']['write-read'] = '[open open][write read]'
G.edge['newAttr96']['system_app']['fill'] = 'red'
G.add_edge('newAttr96','system_app')
G.edge['newAttr96']['system_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('newAttr96','wfd_app')
G.edge['newAttr96']['wfd_app']['write-read'] = '[open open][write read]'
G.edge['newAttr96']['wfd_app']['fill'] = 'red'
G.add_edge('newAttr96','wfd_app')
G.edge['newAttr96']['wfd_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('newAttr96','wfdservice')
G.edge['newAttr96']['wfdservice']['write-read'] = '[open open][write read]'
G.edge['newAttr96']['wfdservice']['fill'] = 'red'
G.add_edge('newAttr96','wfdservice')
G.edge['newAttr96']['wfdservice']['write-read'] = '[open open][write read][append read]'
G.add_edge('newAttr96','zygote')
G.edge['newAttr96']['zygote']['write-read'] = '[open open][write read]'
G.edge['newAttr96']['zygote']['fill'] = 'red'
G.add_edge('newAttr96','zygote')
G.edge['newAttr96']['zygote']['write-read'] = '[open open][write read][append read]'
G.add_edge('radio','bintvoutservice')
G.edge['radio']['bintvoutservice']['write-read'] = '[open open]'
G.add_edge('radio','bootanim')
G.edge['radio']['bootanim']['write-read'] = '[open open]'
G.add_edge('radio','commonplatformappdomain')
G.edge['radio']['commonplatformappdomain']['write-read'] = '[open open]'
G.add_edge('radio','fixmo_app')
G.edge['radio']['fixmo_app']['write-read'] = '[open open]'
G.add_edge('radio','good_app')
G.edge['radio']['good_app']['write-read'] = '[open open]'
G.add_edge('radio','healthd')
G.edge['radio']['healthd']['write-read'] = '[open open]'
G.add_edge('radio','ime_app')
G.edge['radio']['ime_app']['write-read'] = '[open open]'
G.add_edge('radio','isolated_app')
G.edge['radio']['isolated_app']['write-read'] = '[open open]'
G.add_edge('radio','untrusted_app')
G.edge['radio']['untrusted_app']['write-read'] = '[open open]'
G.add_edge('radio','umcagent_app')
G.edge['radio']['umcagent_app']['write-read'] = '[open open]'
G.add_edge('radio','vpn_untrusted_app')
G.edge['radio']['vpn_untrusted_app']['write-read'] = '[open open]'
G.add_edge('radio','trustonicpartner_app')
G.edge['radio']['trustonicpartner_app']['write-read'] = '[open open]'
G.add_edge('radio','llk_untrusted_app')
G.edge['radio']['llk_untrusted_app']['write-read'] = '[open open]'
G.add_edge('radio','filtered_untrusted_app')
G.edge['radio']['filtered_untrusted_app']['write-read'] = '[open open]'
G.add_edge('radio','filtered_google_app')
G.edge['radio']['filtered_google_app']['write-read'] = '[open open]'
G.add_edge('radio','knox_untrusted_app')
G.edge['radio']['knox_untrusted_app']['write-read'] = '[open open]'
G.add_edge('radio','irm_app')
G.edge['radio']['irm_app']['write-read'] = '[open open]'
G.add_edge('radio','gad_untrusted_app')
G.edge['radio']['gad_untrusted_app']['write-read'] = '[open open]'
G.add_edge('radio','carrier_app')
G.edge['radio']['carrier_app']['write-read'] = '[open open]'
G.add_edge('radio','lpm')
G.edge['radio']['lpm']['write-read'] = '[open open]'
G.add_edge('radio','mmi')
G.edge['radio']['mmi']['write-read'] = '[open open]'
G.add_edge('radio','mm-pp-daemon')
G.edge['radio']['mm-pp-daemon']['write-read'] = '[open open]'
G.add_edge('radio','mm-qcamera-daemon')
G.edge['radio']['mm-qcamera-daemon']['write-read'] = '[open open]'
G.add_edge('radio','newAttr96')
G.edge['radio']['newAttr96']['write-read'] = '[open open]'
G.add_edge('radio','radio')
G.edge['radio']['radio']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('radio','s_system_app')
G.edge['radio']['s_system_app']['write-read'] = '[open open]'
G.add_edge('radio','surfaceflinger')
G.edge['radio']['surfaceflinger']['write-read'] = '[open open]'
G.add_edge('radio','system_app')
G.edge['radio']['system_app']['write-read'] = '[open open]'
G.add_edge('radio','wfd_app')
G.edge['radio']['wfd_app']['write-read'] = '[open open]'
G.add_edge('radio','wfdservice')
G.edge['radio']['wfdservice']['write-read'] = '[open open]'
G.add_edge('radio','zygote')
G.edge['radio']['zygote']['write-read'] = '[open open]'
G.add_edge('radio','isolated_app')
G.edge['radio']['isolated_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('radio','untrusted_app')
G.edge['radio']['untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('radio','umcagent_app')
G.edge['radio']['umcagent_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('radio','vpn_untrusted_app')
G.edge['radio']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('radio','trustonicpartner_app')
G.edge['radio']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('radio','llk_untrusted_app')
G.edge['radio']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('radio','filtered_untrusted_app')
G.edge['radio']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('radio','filtered_google_app')
G.edge['radio']['filtered_google_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('radio','knox_untrusted_app')
G.edge['radio']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('radio','irm_app')
G.edge['radio']['irm_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('radio','gad_untrusted_app')
G.edge['radio']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('radio','carrier_app')
G.edge['radio']['carrier_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('radio','newAttr96')
G.edge['radio']['newAttr96']['write-read'] = '[open open][setattr getattr]'
G.add_edge('radio','bintvoutservice')
G.edge['radio']['bintvoutservice']['write-read'] = '[open open][write read]'
G.edge['radio']['bintvoutservice']['fill'] = 'red'
G.add_edge('radio','bintvoutservice')
G.edge['radio']['bintvoutservice']['write-read'] = '[open open][write read][append read]'
G.add_edge('radio','bootanim')
G.edge['radio']['bootanim']['write-read'] = '[open open][write read]'
G.edge['radio']['bootanim']['fill'] = 'red'
G.add_edge('radio','bootanim')
G.edge['radio']['bootanim']['write-read'] = '[open open][write read][append read]'
G.add_edge('radio','commonplatformappdomain')
G.edge['radio']['commonplatformappdomain']['write-read'] = '[open open][write read]'
G.edge['radio']['commonplatformappdomain']['fill'] = 'red'
G.add_edge('radio','commonplatformappdomain')
G.edge['radio']['commonplatformappdomain']['write-read'] = '[open open][write read][append read]'
G.add_edge('radio','fixmo_app')
G.edge['radio']['fixmo_app']['write-read'] = '[open open][write read]'
G.edge['radio']['fixmo_app']['fill'] = 'red'
G.add_edge('radio','fixmo_app')
G.edge['radio']['fixmo_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('radio','good_app')
G.edge['radio']['good_app']['write-read'] = '[open open][write read]'
G.edge['radio']['good_app']['fill'] = 'red'
G.add_edge('radio','good_app')
G.edge['radio']['good_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('radio','healthd')
G.edge['radio']['healthd']['write-read'] = '[open open][write read]'
G.edge['radio']['healthd']['fill'] = 'red'
G.add_edge('radio','healthd')
G.edge['radio']['healthd']['write-read'] = '[open open][write read][append read]'
G.add_edge('radio','ime_app')
G.edge['radio']['ime_app']['write-read'] = '[open open][write read]'
G.edge['radio']['ime_app']['fill'] = 'red'
G.add_edge('radio','ime_app')
G.edge['radio']['ime_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('radio','isolated_app')
G.edge['radio']['isolated_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('radio','untrusted_app')
G.edge['radio']['untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('radio','umcagent_app')
G.edge['radio']['umcagent_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('radio','vpn_untrusted_app')
G.edge['radio']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('radio','trustonicpartner_app')
G.edge['radio']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('radio','llk_untrusted_app')
G.edge['radio']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('radio','filtered_untrusted_app')
G.edge['radio']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('radio','filtered_google_app')
G.edge['radio']['filtered_google_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('radio','knox_untrusted_app')
G.edge['radio']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('radio','irm_app')
G.edge['radio']['irm_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('radio','gad_untrusted_app')
G.edge['radio']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('radio','carrier_app')
G.edge['radio']['carrier_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('radio','lpm')
G.edge['radio']['lpm']['write-read'] = '[open open][write read]'
G.edge['radio']['lpm']['fill'] = 'red'
G.add_edge('radio','lpm')
G.edge['radio']['lpm']['write-read'] = '[open open][write read][append read]'
G.add_edge('radio','mmi')
G.edge['radio']['mmi']['write-read'] = '[open open][write read]'
G.edge['radio']['mmi']['fill'] = 'red'
G.add_edge('radio','mmi')
G.edge['radio']['mmi']['write-read'] = '[open open][write read][append read]'
G.add_edge('radio','mm-pp-daemon')
G.edge['radio']['mm-pp-daemon']['write-read'] = '[open open][write read]'
G.edge['radio']['mm-pp-daemon']['fill'] = 'red'
G.add_edge('radio','mm-pp-daemon')
G.edge['radio']['mm-pp-daemon']['write-read'] = '[open open][write read][append read]'
G.add_edge('radio','mm-qcamera-daemon')
G.edge['radio']['mm-qcamera-daemon']['write-read'] = '[open open][write read]'
G.edge['radio']['mm-qcamera-daemon']['fill'] = 'red'
G.add_edge('radio','mm-qcamera-daemon')
G.edge['radio']['mm-qcamera-daemon']['write-read'] = '[open open][write read][append read]'
G.add_edge('radio','newAttr96')
G.edge['radio']['newAttr96']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['radio']['newAttr96']['fill'] = 'red'
G.add_edge('radio','newAttr96')
G.edge['radio']['newAttr96']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('radio','radio')
G.edge['radio']['radio']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read]'
G.edge['radio']['radio']['fill'] = 'red'
G.add_edge('radio','radio')
G.edge['radio']['radio']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('radio','s_system_app')
G.edge['radio']['s_system_app']['write-read'] = '[open open][write read]'
G.edge['radio']['s_system_app']['fill'] = 'red'
G.add_edge('radio','s_system_app')
G.edge['radio']['s_system_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('radio','surfaceflinger')
G.edge['radio']['surfaceflinger']['write-read'] = '[open open][write read]'
G.edge['radio']['surfaceflinger']['fill'] = 'red'
G.add_edge('radio','surfaceflinger')
G.edge['radio']['surfaceflinger']['write-read'] = '[open open][write read][append read]'
G.add_edge('radio','system_app')
G.edge['radio']['system_app']['write-read'] = '[open open][write read]'
G.edge['radio']['system_app']['fill'] = 'red'
G.add_edge('radio','system_app')
G.edge['radio']['system_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('radio','wfd_app')
G.edge['radio']['wfd_app']['write-read'] = '[open open][write read]'
G.edge['radio']['wfd_app']['fill'] = 'red'
G.add_edge('radio','wfd_app')
G.edge['radio']['wfd_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('radio','wfdservice')
G.edge['radio']['wfdservice']['write-read'] = '[open open][write read]'
G.edge['radio']['wfdservice']['fill'] = 'red'
G.add_edge('radio','wfdservice')
G.edge['radio']['wfdservice']['write-read'] = '[open open][write read][append read]'
G.add_edge('radio','zygote')
G.edge['radio']['zygote']['write-read'] = '[open open][write read]'
G.edge['radio']['zygote']['fill'] = 'red'
G.add_edge('radio','zygote')
G.edge['radio']['zygote']['write-read'] = '[open open][write read][append read]'
G.add_edge('s_system_app','bintvoutservice')
G.edge['s_system_app']['bintvoutservice']['write-read'] = '[open open]'
G.add_edge('s_system_app','bootanim')
G.edge['s_system_app']['bootanim']['write-read'] = '[open open]'
G.add_edge('s_system_app','commonplatformappdomain')
G.edge['s_system_app']['commonplatformappdomain']['write-read'] = '[setopt getopt][open open]'
G.add_edge('s_system_app','fixmo_app')
G.edge['s_system_app']['fixmo_app']['write-read'] = '[open open]'
G.add_edge('s_system_app','good_app')
G.edge['s_system_app']['good_app']['write-read'] = '[open open]'
G.add_edge('s_system_app','healthd')
G.edge['s_system_app']['healthd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open]'
G.add_edge('s_system_app','ime_app')
G.edge['s_system_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('s_system_app','isolated_app')
G.edge['s_system_app']['isolated_app']['write-read'] = '[open open]'
G.add_edge('s_system_app','untrusted_app')
G.edge['s_system_app']['untrusted_app']['write-read'] = '[open open]'
G.add_edge('s_system_app','umcagent_app')
G.edge['s_system_app']['umcagent_app']['write-read'] = '[open open]'
G.add_edge('s_system_app','vpn_untrusted_app')
G.edge['s_system_app']['vpn_untrusted_app']['write-read'] = '[open open]'
G.add_edge('s_system_app','trustonicpartner_app')
G.edge['s_system_app']['trustonicpartner_app']['write-read'] = '[open open]'
G.add_edge('s_system_app','llk_untrusted_app')
G.edge['s_system_app']['llk_untrusted_app']['write-read'] = '[open open]'
G.add_edge('s_system_app','filtered_untrusted_app')
G.edge['s_system_app']['filtered_untrusted_app']['write-read'] = '[open open]'
G.add_edge('s_system_app','filtered_google_app')
G.edge['s_system_app']['filtered_google_app']['write-read'] = '[open open]'
G.add_edge('s_system_app','knox_untrusted_app')
G.edge['s_system_app']['knox_untrusted_app']['write-read'] = '[open open]'
G.add_edge('s_system_app','irm_app')
G.edge['s_system_app']['irm_app']['write-read'] = '[open open]'
G.add_edge('s_system_app','gad_untrusted_app')
G.edge['s_system_app']['gad_untrusted_app']['write-read'] = '[open open]'
G.add_edge('s_system_app','carrier_app')
G.edge['s_system_app']['carrier_app']['write-read'] = '[open open]'
G.add_edge('s_system_app','lpm')
G.edge['s_system_app']['lpm']['write-read'] = '[setopt getopt][open open]'
G.add_edge('s_system_app','mmi')
G.edge['s_system_app']['mmi']['write-read'] = '[open open]'
G.add_edge('s_system_app','mm-pp-daemon')
G.edge['s_system_app']['mm-pp-daemon']['write-read'] = '[open open]'
G.add_edge('s_system_app','mm-qcamera-daemon')
G.edge['s_system_app']['mm-qcamera-daemon']['write-read'] = '[open open]'
G.add_edge('s_system_app','newAttr96')
G.edge['s_system_app']['newAttr96']['write-read'] = '[open open]'
G.add_edge('s_system_app','radio')
G.edge['s_system_app']['radio']['write-read'] = '[open open]'
G.add_edge('s_system_app','s_system_app')
G.edge['s_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('s_system_app','surfaceflinger')
G.edge['s_system_app']['surfaceflinger']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open]'
G.add_edge('s_system_app','system_app')
G.edge['s_system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('s_system_app','wfd_app')
G.edge['s_system_app']['wfd_app']['write-read'] = '[open open]'
G.add_edge('s_system_app','wfdservice')
G.edge['s_system_app']['wfdservice']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open]'
G.add_edge('s_system_app','zygote')
G.edge['s_system_app']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('s_system_app','isolated_app')
G.edge['s_system_app']['isolated_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('s_system_app','untrusted_app')
G.edge['s_system_app']['untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('s_system_app','umcagent_app')
G.edge['s_system_app']['umcagent_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('s_system_app','vpn_untrusted_app')
G.edge['s_system_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('s_system_app','trustonicpartner_app')
G.edge['s_system_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('s_system_app','llk_untrusted_app')
G.edge['s_system_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('s_system_app','filtered_untrusted_app')
G.edge['s_system_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('s_system_app','filtered_google_app')
G.edge['s_system_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('s_system_app','knox_untrusted_app')
G.edge['s_system_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('s_system_app','irm_app')
G.edge['s_system_app']['irm_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('s_system_app','gad_untrusted_app')
G.edge['s_system_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('s_system_app','carrier_app')
G.edge['s_system_app']['carrier_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('s_system_app','newAttr96')
G.edge['s_system_app']['newAttr96']['write-read'] = '[open open][setattr getattr]'
G.add_edge('s_system_app','bintvoutservice')
G.edge['s_system_app']['bintvoutservice']['write-read'] = '[open open][write read]'
G.edge['s_system_app']['bintvoutservice']['fill'] = 'red'
G.add_edge('s_system_app','bintvoutservice')
G.edge['s_system_app']['bintvoutservice']['write-read'] = '[open open][write read][append read]'
G.add_edge('s_system_app','bootanim')
G.edge['s_system_app']['bootanim']['write-read'] = '[open open][write read]'
G.edge['s_system_app']['bootanim']['fill'] = 'red'
G.add_edge('s_system_app','bootanim')
G.edge['s_system_app']['bootanim']['write-read'] = '[open open][write read][append read]'
G.add_edge('s_system_app','commonplatformappdomain')
G.edge['s_system_app']['commonplatformappdomain']['write-read'] = '[setopt getopt][open open][write read]'
G.edge['s_system_app']['commonplatformappdomain']['fill'] = 'red'
G.add_edge('s_system_app','commonplatformappdomain')
G.edge['s_system_app']['commonplatformappdomain']['write-read'] = '[setopt getopt][open open][write read][append read]'
G.add_edge('s_system_app','fixmo_app')
G.edge['s_system_app']['fixmo_app']['write-read'] = '[open open][write read]'
G.edge['s_system_app']['fixmo_app']['fill'] = 'red'
G.add_edge('s_system_app','fixmo_app')
G.edge['s_system_app']['fixmo_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('s_system_app','good_app')
G.edge['s_system_app']['good_app']['write-read'] = '[open open][write read]'
G.edge['s_system_app']['good_app']['fill'] = 'red'
G.add_edge('s_system_app','good_app')
G.edge['s_system_app']['good_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('s_system_app','healthd')
G.edge['s_system_app']['healthd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read]'
G.edge['s_system_app']['healthd']['fill'] = 'red'
G.add_edge('s_system_app','healthd')
G.edge['s_system_app']['healthd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read]'
G.add_edge('s_system_app','ime_app')
G.edge['s_system_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['s_system_app']['ime_app']['fill'] = 'red'
G.add_edge('s_system_app','ime_app')
G.edge['s_system_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('s_system_app','isolated_app')
G.edge['s_system_app']['isolated_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('s_system_app','untrusted_app')
G.edge['s_system_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('s_system_app','umcagent_app')
G.edge['s_system_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('s_system_app','vpn_untrusted_app')
G.edge['s_system_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('s_system_app','trustonicpartner_app')
G.edge['s_system_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('s_system_app','llk_untrusted_app')
G.edge['s_system_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('s_system_app','filtered_untrusted_app')
G.edge['s_system_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('s_system_app','filtered_google_app')
G.edge['s_system_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('s_system_app','knox_untrusted_app')
G.edge['s_system_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('s_system_app','irm_app')
G.edge['s_system_app']['irm_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('s_system_app','gad_untrusted_app')
G.edge['s_system_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('s_system_app','carrier_app')
G.edge['s_system_app']['carrier_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('s_system_app','lpm')
G.edge['s_system_app']['lpm']['write-read'] = '[setopt getopt][open open][write read]'
G.edge['s_system_app']['lpm']['fill'] = 'red'
G.add_edge('s_system_app','lpm')
G.edge['s_system_app']['lpm']['write-read'] = '[setopt getopt][open open][write read][append read]'
G.add_edge('s_system_app','mmi')
G.edge['s_system_app']['mmi']['write-read'] = '[open open][write read]'
G.edge['s_system_app']['mmi']['fill'] = 'red'
G.add_edge('s_system_app','mmi')
G.edge['s_system_app']['mmi']['write-read'] = '[open open][write read][append read]'
G.add_edge('s_system_app','mm-pp-daemon')
G.edge['s_system_app']['mm-pp-daemon']['write-read'] = '[open open][write read]'
G.edge['s_system_app']['mm-pp-daemon']['fill'] = 'red'
G.add_edge('s_system_app','mm-pp-daemon')
G.edge['s_system_app']['mm-pp-daemon']['write-read'] = '[open open][write read][append read]'
G.add_edge('s_system_app','mm-qcamera-daemon')
G.edge['s_system_app']['mm-qcamera-daemon']['write-read'] = '[open open][write read]'
G.edge['s_system_app']['mm-qcamera-daemon']['fill'] = 'red'
G.add_edge('s_system_app','mm-qcamera-daemon')
G.edge['s_system_app']['mm-qcamera-daemon']['write-read'] = '[open open][write read][append read]'
G.add_edge('s_system_app','newAttr96')
G.edge['s_system_app']['newAttr96']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['s_system_app']['newAttr96']['fill'] = 'red'
G.add_edge('s_system_app','newAttr96')
G.edge['s_system_app']['newAttr96']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('s_system_app','radio')
G.edge['s_system_app']['radio']['write-read'] = '[open open][write read]'
G.edge['s_system_app']['radio']['fill'] = 'red'
G.add_edge('s_system_app','radio')
G.edge['s_system_app']['radio']['write-read'] = '[open open][write read][append read]'
G.add_edge('s_system_app','s_system_app')
G.edge['s_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['s_system_app']['s_system_app']['fill'] = 'red'
G.add_edge('s_system_app','s_system_app')
G.edge['s_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('s_system_app','surfaceflinger')
G.edge['s_system_app']['surfaceflinger']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read]'
G.edge['s_system_app']['surfaceflinger']['fill'] = 'red'
G.add_edge('s_system_app','surfaceflinger')
G.edge['s_system_app']['surfaceflinger']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read]'
G.add_edge('s_system_app','system_app')
G.edge['s_system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['s_system_app']['system_app']['fill'] = 'red'
G.add_edge('s_system_app','system_app')
G.edge['s_system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('s_system_app','wfd_app')
G.edge['s_system_app']['wfd_app']['write-read'] = '[open open][write read]'
G.edge['s_system_app']['wfd_app']['fill'] = 'red'
G.add_edge('s_system_app','wfd_app')
G.edge['s_system_app']['wfd_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('s_system_app','wfdservice')
G.edge['s_system_app']['wfdservice']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read]'
G.edge['s_system_app']['wfdservice']['fill'] = 'red'
G.add_edge('s_system_app','wfdservice')
G.edge['s_system_app']['wfdservice']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read]'
G.add_edge('s_system_app','zygote')
G.edge['s_system_app']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['s_system_app']['zygote']['fill'] = 'red'
G.add_edge('s_system_app','zygote')
G.edge['s_system_app']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('surfaceflinger','bintvoutservice')
G.edge['surfaceflinger']['bintvoutservice']['write-read'] = '[open open]'
G.add_edge('surfaceflinger','bootanim')
G.edge['surfaceflinger']['bootanim']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('surfaceflinger','commonplatformappdomain')
G.edge['surfaceflinger']['commonplatformappdomain']['write-read'] = '[setopt getopt][open open]'
G.add_edge('surfaceflinger','fixmo_app')
G.edge['surfaceflinger']['fixmo_app']['write-read'] = '[open open]'
G.add_edge('surfaceflinger','good_app')
G.edge['surfaceflinger']['good_app']['write-read'] = '[open open]'
G.add_edge('surfaceflinger','healthd')
G.edge['surfaceflinger']['healthd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open]'
G.add_edge('surfaceflinger','ime_app')
G.edge['surfaceflinger']['ime_app']['write-read'] = '[setattr getattr][setopt getopt][open open]'
G.add_edge('surfaceflinger','isolated_app')
G.edge['surfaceflinger']['isolated_app']['write-read'] = '[open open]'
G.add_edge('surfaceflinger','untrusted_app')
G.edge['surfaceflinger']['untrusted_app']['write-read'] = '[open open]'
G.add_edge('surfaceflinger','umcagent_app')
G.edge['surfaceflinger']['umcagent_app']['write-read'] = '[open open]'
G.add_edge('surfaceflinger','vpn_untrusted_app')
G.edge['surfaceflinger']['vpn_untrusted_app']['write-read'] = '[open open]'
G.add_edge('surfaceflinger','trustonicpartner_app')
G.edge['surfaceflinger']['trustonicpartner_app']['write-read'] = '[open open]'
G.add_edge('surfaceflinger','llk_untrusted_app')
G.edge['surfaceflinger']['llk_untrusted_app']['write-read'] = '[open open]'
G.add_edge('surfaceflinger','filtered_untrusted_app')
G.edge['surfaceflinger']['filtered_untrusted_app']['write-read'] = '[open open]'
G.add_edge('surfaceflinger','filtered_google_app')
G.edge['surfaceflinger']['filtered_google_app']['write-read'] = '[open open]'
G.add_edge('surfaceflinger','knox_untrusted_app')
G.edge['surfaceflinger']['knox_untrusted_app']['write-read'] = '[open open]'
G.add_edge('surfaceflinger','irm_app')
G.edge['surfaceflinger']['irm_app']['write-read'] = '[open open]'
G.add_edge('surfaceflinger','gad_untrusted_app')
G.edge['surfaceflinger']['gad_untrusted_app']['write-read'] = '[open open]'
G.add_edge('surfaceflinger','carrier_app')
G.edge['surfaceflinger']['carrier_app']['write-read'] = '[open open]'
G.add_edge('surfaceflinger','lpm')
G.edge['surfaceflinger']['lpm']['write-read'] = '[setopt getopt][open open]'
G.add_edge('surfaceflinger','mmi')
G.edge['surfaceflinger']['mmi']['write-read'] = '[open open]'
G.add_edge('surfaceflinger','mm-pp-daemon')
G.edge['surfaceflinger']['mm-pp-daemon']['write-read'] = '[open open]'
G.add_edge('surfaceflinger','mm-qcamera-daemon')
G.edge['surfaceflinger']['mm-qcamera-daemon']['write-read'] = '[open open]'
G.add_edge('surfaceflinger','newAttr96')
G.edge['surfaceflinger']['newAttr96']['write-read'] = '[open open]'
G.add_edge('surfaceflinger','radio')
G.edge['surfaceflinger']['radio']['write-read'] = '[open open]'
G.add_edge('surfaceflinger','s_system_app')
G.edge['surfaceflinger']['s_system_app']['write-read'] = '[setattr getattr][setopt getopt][open open]'
G.add_edge('surfaceflinger','surfaceflinger')
G.edge['surfaceflinger']['surfaceflinger']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open]'
G.add_edge('surfaceflinger','system_app')
G.edge['surfaceflinger']['system_app']['write-read'] = '[setattr getattr][setopt getopt][open open]'
G.add_edge('surfaceflinger','wfd_app')
G.edge['surfaceflinger']['wfd_app']['write-read'] = '[open open]'
G.add_edge('surfaceflinger','wfdservice')
G.edge['surfaceflinger']['wfdservice']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open]'
G.add_edge('surfaceflinger','zygote')
G.edge['surfaceflinger']['zygote']['write-read'] = '[open open]'
G.add_edge('surfaceflinger','isolated_app')
G.edge['surfaceflinger']['isolated_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('surfaceflinger','untrusted_app')
G.edge['surfaceflinger']['untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('surfaceflinger','umcagent_app')
G.edge['surfaceflinger']['umcagent_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('surfaceflinger','vpn_untrusted_app')
G.edge['surfaceflinger']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('surfaceflinger','trustonicpartner_app')
G.edge['surfaceflinger']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('surfaceflinger','llk_untrusted_app')
G.edge['surfaceflinger']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('surfaceflinger','filtered_untrusted_app')
G.edge['surfaceflinger']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('surfaceflinger','filtered_google_app')
G.edge['surfaceflinger']['filtered_google_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('surfaceflinger','knox_untrusted_app')
G.edge['surfaceflinger']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('surfaceflinger','irm_app')
G.edge['surfaceflinger']['irm_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('surfaceflinger','gad_untrusted_app')
G.edge['surfaceflinger']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('surfaceflinger','carrier_app')
G.edge['surfaceflinger']['carrier_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('surfaceflinger','newAttr96')
G.edge['surfaceflinger']['newAttr96']['write-read'] = '[open open][setattr getattr]'
G.add_edge('surfaceflinger','bintvoutservice')
G.edge['surfaceflinger']['bintvoutservice']['write-read'] = '[open open][write read]'
G.edge['surfaceflinger']['bintvoutservice']['fill'] = 'red'
G.add_edge('surfaceflinger','bintvoutservice')
G.edge['surfaceflinger']['bintvoutservice']['write-read'] = '[open open][write read][append read]'
G.add_edge('surfaceflinger','bootanim')
G.edge['surfaceflinger']['bootanim']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['surfaceflinger']['bootanim']['fill'] = 'red'
G.add_edge('surfaceflinger','bootanim')
G.edge['surfaceflinger']['bootanim']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('surfaceflinger','commonplatformappdomain')
G.edge['surfaceflinger']['commonplatformappdomain']['write-read'] = '[setopt getopt][open open][write read]'
G.edge['surfaceflinger']['commonplatformappdomain']['fill'] = 'red'
G.add_edge('surfaceflinger','commonplatformappdomain')
G.edge['surfaceflinger']['commonplatformappdomain']['write-read'] = '[setopt getopt][open open][write read][append read]'
G.add_edge('surfaceflinger','fixmo_app')
G.edge['surfaceflinger']['fixmo_app']['write-read'] = '[open open][write read]'
G.edge['surfaceflinger']['fixmo_app']['fill'] = 'red'
G.add_edge('surfaceflinger','fixmo_app')
G.edge['surfaceflinger']['fixmo_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('surfaceflinger','good_app')
G.edge['surfaceflinger']['good_app']['write-read'] = '[open open][write read]'
G.edge['surfaceflinger']['good_app']['fill'] = 'red'
G.add_edge('surfaceflinger','good_app')
G.edge['surfaceflinger']['good_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('surfaceflinger','healthd')
G.edge['surfaceflinger']['healthd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read]'
G.edge['surfaceflinger']['healthd']['fill'] = 'red'
G.add_edge('surfaceflinger','healthd')
G.edge['surfaceflinger']['healthd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read]'
G.add_edge('surfaceflinger','ime_app')
G.edge['surfaceflinger']['ime_app']['write-read'] = '[setattr getattr][setopt getopt][open open][write read]'
G.edge['surfaceflinger']['ime_app']['fill'] = 'red'
G.add_edge('surfaceflinger','ime_app')
G.edge['surfaceflinger']['ime_app']['write-read'] = '[setattr getattr][setopt getopt][open open][write read][append read]'
G.add_edge('surfaceflinger','isolated_app')
G.edge['surfaceflinger']['isolated_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('surfaceflinger','untrusted_app')
G.edge['surfaceflinger']['untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('surfaceflinger','umcagent_app')
G.edge['surfaceflinger']['umcagent_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('surfaceflinger','vpn_untrusted_app')
G.edge['surfaceflinger']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('surfaceflinger','trustonicpartner_app')
G.edge['surfaceflinger']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('surfaceflinger','llk_untrusted_app')
G.edge['surfaceflinger']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('surfaceflinger','filtered_untrusted_app')
G.edge['surfaceflinger']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('surfaceflinger','filtered_google_app')
G.edge['surfaceflinger']['filtered_google_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('surfaceflinger','knox_untrusted_app')
G.edge['surfaceflinger']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('surfaceflinger','irm_app')
G.edge['surfaceflinger']['irm_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('surfaceflinger','gad_untrusted_app')
G.edge['surfaceflinger']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('surfaceflinger','carrier_app')
G.edge['surfaceflinger']['carrier_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('surfaceflinger','lpm')
G.edge['surfaceflinger']['lpm']['write-read'] = '[setopt getopt][open open][write read]'
G.edge['surfaceflinger']['lpm']['fill'] = 'red'
G.add_edge('surfaceflinger','lpm')
G.edge['surfaceflinger']['lpm']['write-read'] = '[setopt getopt][open open][write read][append read]'
G.add_edge('surfaceflinger','mmi')
G.edge['surfaceflinger']['mmi']['write-read'] = '[open open][write read]'
G.edge['surfaceflinger']['mmi']['fill'] = 'red'
G.add_edge('surfaceflinger','mmi')
G.edge['surfaceflinger']['mmi']['write-read'] = '[open open][write read][append read]'
G.add_edge('surfaceflinger','mm-pp-daemon')
G.edge['surfaceflinger']['mm-pp-daemon']['write-read'] = '[open open][write read]'
G.edge['surfaceflinger']['mm-pp-daemon']['fill'] = 'red'
G.add_edge('surfaceflinger','mm-pp-daemon')
G.edge['surfaceflinger']['mm-pp-daemon']['write-read'] = '[open open][write read][append read]'
G.add_edge('surfaceflinger','mm-qcamera-daemon')
G.edge['surfaceflinger']['mm-qcamera-daemon']['write-read'] = '[open open][write read]'
G.edge['surfaceflinger']['mm-qcamera-daemon']['fill'] = 'red'
G.add_edge('surfaceflinger','mm-qcamera-daemon')
G.edge['surfaceflinger']['mm-qcamera-daemon']['write-read'] = '[open open][write read][append read]'
G.add_edge('surfaceflinger','newAttr96')
G.edge['surfaceflinger']['newAttr96']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['surfaceflinger']['newAttr96']['fill'] = 'red'
G.add_edge('surfaceflinger','newAttr96')
G.edge['surfaceflinger']['newAttr96']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('surfaceflinger','radio')
G.edge['surfaceflinger']['radio']['write-read'] = '[open open][write read]'
G.edge['surfaceflinger']['radio']['fill'] = 'red'
G.add_edge('surfaceflinger','radio')
G.edge['surfaceflinger']['radio']['write-read'] = '[open open][write read][append read]'
G.add_edge('surfaceflinger','s_system_app')
G.edge['surfaceflinger']['s_system_app']['write-read'] = '[setattr getattr][setopt getopt][open open][write read]'
G.edge['surfaceflinger']['s_system_app']['fill'] = 'red'
G.add_edge('surfaceflinger','s_system_app')
G.edge['surfaceflinger']['s_system_app']['write-read'] = '[setattr getattr][setopt getopt][open open][write read][append read]'
G.add_edge('surfaceflinger','surfaceflinger')
G.edge['surfaceflinger']['surfaceflinger']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read]'
G.edge['surfaceflinger']['surfaceflinger']['fill'] = 'red'
G.add_edge('surfaceflinger','surfaceflinger')
G.edge['surfaceflinger']['surfaceflinger']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read]'
G.add_edge('surfaceflinger','system_app')
G.edge['surfaceflinger']['system_app']['write-read'] = '[setattr getattr][setopt getopt][open open][write read]'
G.edge['surfaceflinger']['system_app']['fill'] = 'red'
G.add_edge('surfaceflinger','system_app')
G.edge['surfaceflinger']['system_app']['write-read'] = '[setattr getattr][setopt getopt][open open][write read][append read]'
G.add_edge('surfaceflinger','wfd_app')
G.edge['surfaceflinger']['wfd_app']['write-read'] = '[open open][write read]'
G.edge['surfaceflinger']['wfd_app']['fill'] = 'red'
G.add_edge('surfaceflinger','wfd_app')
G.edge['surfaceflinger']['wfd_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('surfaceflinger','wfdservice')
G.edge['surfaceflinger']['wfdservice']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read]'
G.edge['surfaceflinger']['wfdservice']['fill'] = 'red'
G.add_edge('surfaceflinger','wfdservice')
G.edge['surfaceflinger']['wfdservice']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read]'
G.add_edge('surfaceflinger','zygote')
G.edge['surfaceflinger']['zygote']['write-read'] = '[open open][write read]'
G.edge['surfaceflinger']['zygote']['fill'] = 'red'
G.add_edge('surfaceflinger','zygote')
G.edge['surfaceflinger']['zygote']['write-read'] = '[open open][write read][append read]'
G.add_edge('system_app','bintvoutservice')
G.edge['system_app']['bintvoutservice']['write-read'] = '[open open]'
G.add_edge('system_app','bootanim')
G.edge['system_app']['bootanim']['write-read'] = '[open open]'
G.add_edge('system_app','commonplatformappdomain')
G.edge['system_app']['commonplatformappdomain']['write-read'] = '[setopt getopt][open open]'
G.add_edge('system_app','fixmo_app')
G.edge['system_app']['fixmo_app']['write-read'] = '[open open]'
G.add_edge('system_app','good_app')
G.edge['system_app']['good_app']['write-read'] = '[open open]'
G.add_edge('system_app','healthd')
G.edge['system_app']['healthd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open]'
G.add_edge('system_app','ime_app')
G.edge['system_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('system_app','isolated_app')
G.edge['system_app']['isolated_app']['write-read'] = '[open open]'
G.add_edge('system_app','untrusted_app')
G.edge['system_app']['untrusted_app']['write-read'] = '[open open]'
G.add_edge('system_app','umcagent_app')
G.edge['system_app']['umcagent_app']['write-read'] = '[open open]'
G.add_edge('system_app','vpn_untrusted_app')
G.edge['system_app']['vpn_untrusted_app']['write-read'] = '[open open]'
G.add_edge('system_app','trustonicpartner_app')
G.edge['system_app']['trustonicpartner_app']['write-read'] = '[open open]'
G.add_edge('system_app','llk_untrusted_app')
G.edge['system_app']['llk_untrusted_app']['write-read'] = '[open open]'
G.add_edge('system_app','filtered_untrusted_app')
G.edge['system_app']['filtered_untrusted_app']['write-read'] = '[open open]'
G.add_edge('system_app','filtered_google_app')
G.edge['system_app']['filtered_google_app']['write-read'] = '[open open]'
G.add_edge('system_app','knox_untrusted_app')
G.edge['system_app']['knox_untrusted_app']['write-read'] = '[open open]'
G.add_edge('system_app','irm_app')
G.edge['system_app']['irm_app']['write-read'] = '[open open]'
G.add_edge('system_app','gad_untrusted_app')
G.edge['system_app']['gad_untrusted_app']['write-read'] = '[open open]'
G.add_edge('system_app','carrier_app')
G.edge['system_app']['carrier_app']['write-read'] = '[open open]'
G.add_edge('system_app','lpm')
G.edge['system_app']['lpm']['write-read'] = '[setopt getopt][open open]'
G.add_edge('system_app','mmi')
G.edge['system_app']['mmi']['write-read'] = '[open open]'
G.add_edge('system_app','mm-pp-daemon')
G.edge['system_app']['mm-pp-daemon']['write-read'] = '[open open]'
G.add_edge('system_app','mm-qcamera-daemon')
G.edge['system_app']['mm-qcamera-daemon']['write-read'] = '[open open]'
G.add_edge('system_app','newAttr96')
G.edge['system_app']['newAttr96']['write-read'] = '[open open]'
G.add_edge('system_app','radio')
G.edge['system_app']['radio']['write-read'] = '[open open]'
G.add_edge('system_app','s_system_app')
G.edge['system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('system_app','surfaceflinger')
G.edge['system_app']['surfaceflinger']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open]'
G.add_edge('system_app','system_app')
G.edge['system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('system_app','wfd_app')
G.edge['system_app']['wfd_app']['write-read'] = '[open open]'
G.add_edge('system_app','wfdservice')
G.edge['system_app']['wfdservice']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open]'
G.add_edge('system_app','zygote')
G.edge['system_app']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('system_app','isolated_app')
G.edge['system_app']['isolated_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('system_app','untrusted_app')
G.edge['system_app']['untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('system_app','umcagent_app')
G.edge['system_app']['umcagent_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('system_app','vpn_untrusted_app')
G.edge['system_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('system_app','trustonicpartner_app')
G.edge['system_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('system_app','llk_untrusted_app')
G.edge['system_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('system_app','filtered_untrusted_app')
G.edge['system_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('system_app','filtered_google_app')
G.edge['system_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('system_app','knox_untrusted_app')
G.edge['system_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('system_app','irm_app')
G.edge['system_app']['irm_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('system_app','gad_untrusted_app')
G.edge['system_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('system_app','carrier_app')
G.edge['system_app']['carrier_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('system_app','newAttr96')
G.edge['system_app']['newAttr96']['write-read'] = '[open open][setattr getattr]'
G.add_edge('system_app','bintvoutservice')
G.edge['system_app']['bintvoutservice']['write-read'] = '[open open][write read]'
G.edge['system_app']['bintvoutservice']['fill'] = 'red'
G.add_edge('system_app','bintvoutservice')
G.edge['system_app']['bintvoutservice']['write-read'] = '[open open][write read][append read]'
G.add_edge('system_app','bootanim')
G.edge['system_app']['bootanim']['write-read'] = '[open open][write read]'
G.edge['system_app']['bootanim']['fill'] = 'red'
G.add_edge('system_app','bootanim')
G.edge['system_app']['bootanim']['write-read'] = '[open open][write read][append read]'
G.add_edge('system_app','commonplatformappdomain')
G.edge['system_app']['commonplatformappdomain']['write-read'] = '[setopt getopt][open open][write read]'
G.edge['system_app']['commonplatformappdomain']['fill'] = 'red'
G.add_edge('system_app','commonplatformappdomain')
G.edge['system_app']['commonplatformappdomain']['write-read'] = '[setopt getopt][open open][write read][append read]'
G.add_edge('system_app','fixmo_app')
G.edge['system_app']['fixmo_app']['write-read'] = '[open open][write read]'
G.edge['system_app']['fixmo_app']['fill'] = 'red'
G.add_edge('system_app','fixmo_app')
G.edge['system_app']['fixmo_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('system_app','good_app')
G.edge['system_app']['good_app']['write-read'] = '[open open][write read]'
G.edge['system_app']['good_app']['fill'] = 'red'
G.add_edge('system_app','good_app')
G.edge['system_app']['good_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('system_app','healthd')
G.edge['system_app']['healthd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read]'
G.edge['system_app']['healthd']['fill'] = 'red'
G.add_edge('system_app','healthd')
G.edge['system_app']['healthd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read]'
G.add_edge('system_app','ime_app')
G.edge['system_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['system_app']['ime_app']['fill'] = 'red'
G.add_edge('system_app','ime_app')
G.edge['system_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('system_app','isolated_app')
G.edge['system_app']['isolated_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('system_app','untrusted_app')
G.edge['system_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('system_app','umcagent_app')
G.edge['system_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('system_app','vpn_untrusted_app')
G.edge['system_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('system_app','trustonicpartner_app')
G.edge['system_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('system_app','llk_untrusted_app')
G.edge['system_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('system_app','filtered_untrusted_app')
G.edge['system_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('system_app','filtered_google_app')
G.edge['system_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('system_app','knox_untrusted_app')
G.edge['system_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('system_app','irm_app')
G.edge['system_app']['irm_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('system_app','gad_untrusted_app')
G.edge['system_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('system_app','carrier_app')
G.edge['system_app']['carrier_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('system_app','lpm')
G.edge['system_app']['lpm']['write-read'] = '[setopt getopt][open open][write read]'
G.edge['system_app']['lpm']['fill'] = 'red'
G.add_edge('system_app','lpm')
G.edge['system_app']['lpm']['write-read'] = '[setopt getopt][open open][write read][append read]'
G.add_edge('system_app','mmi')
G.edge['system_app']['mmi']['write-read'] = '[open open][write read]'
G.edge['system_app']['mmi']['fill'] = 'red'
G.add_edge('system_app','mmi')
G.edge['system_app']['mmi']['write-read'] = '[open open][write read][append read]'
G.add_edge('system_app','mm-pp-daemon')
G.edge['system_app']['mm-pp-daemon']['write-read'] = '[open open][write read]'
G.edge['system_app']['mm-pp-daemon']['fill'] = 'red'
G.add_edge('system_app','mm-pp-daemon')
G.edge['system_app']['mm-pp-daemon']['write-read'] = '[open open][write read][append read]'
G.add_edge('system_app','mm-qcamera-daemon')
G.edge['system_app']['mm-qcamera-daemon']['write-read'] = '[open open][write read]'
G.edge['system_app']['mm-qcamera-daemon']['fill'] = 'red'
G.add_edge('system_app','mm-qcamera-daemon')
G.edge['system_app']['mm-qcamera-daemon']['write-read'] = '[open open][write read][append read]'
G.add_edge('system_app','newAttr96')
G.edge['system_app']['newAttr96']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['system_app']['newAttr96']['fill'] = 'red'
G.add_edge('system_app','newAttr96')
G.edge['system_app']['newAttr96']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('system_app','radio')
G.edge['system_app']['radio']['write-read'] = '[open open][write read]'
G.edge['system_app']['radio']['fill'] = 'red'
G.add_edge('system_app','radio')
G.edge['system_app']['radio']['write-read'] = '[open open][write read][append read]'
G.add_edge('system_app','s_system_app')
G.edge['system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['system_app']['s_system_app']['fill'] = 'red'
G.add_edge('system_app','s_system_app')
G.edge['system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('system_app','surfaceflinger')
G.edge['system_app']['surfaceflinger']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read]'
G.edge['system_app']['surfaceflinger']['fill'] = 'red'
G.add_edge('system_app','surfaceflinger')
G.edge['system_app']['surfaceflinger']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read]'
G.add_edge('system_app','system_app')
G.edge['system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['system_app']['system_app']['fill'] = 'red'
G.add_edge('system_app','system_app')
G.edge['system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('system_app','wfd_app')
G.edge['system_app']['wfd_app']['write-read'] = '[open open][write read]'
G.edge['system_app']['wfd_app']['fill'] = 'red'
G.add_edge('system_app','wfd_app')
G.edge['system_app']['wfd_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('system_app','wfdservice')
G.edge['system_app']['wfdservice']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read]'
G.edge['system_app']['wfdservice']['fill'] = 'red'
G.add_edge('system_app','wfdservice')
G.edge['system_app']['wfdservice']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read]'
G.add_edge('system_app','zygote')
G.edge['system_app']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['system_app']['zygote']['fill'] = 'red'
G.add_edge('system_app','zygote')
G.edge['system_app']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('tee','bintvoutservice')
G.edge['tee']['bintvoutservice']['write-read'] = '[open open]'
G.add_edge('tee','bootanim')
G.edge['tee']['bootanim']['write-read'] = '[open open]'
G.add_edge('tee','commonplatformappdomain')
G.edge['tee']['commonplatformappdomain']['write-read'] = '[open open]'
G.add_edge('tee','fixmo_app')
G.edge['tee']['fixmo_app']['write-read'] = '[open open]'
G.add_edge('tee','good_app')
G.edge['tee']['good_app']['write-read'] = '[open open]'
G.add_edge('tee','healthd')
G.edge['tee']['healthd']['write-read'] = '[open open]'
G.add_edge('tee','ime_app')
G.edge['tee']['ime_app']['write-read'] = '[open open]'
G.add_edge('tee','isolated_app')
G.edge['tee']['isolated_app']['write-read'] = '[open open]'
G.add_edge('tee','untrusted_app')
G.edge['tee']['untrusted_app']['write-read'] = '[open open]'
G.add_edge('tee','umcagent_app')
G.edge['tee']['umcagent_app']['write-read'] = '[open open]'
G.add_edge('tee','vpn_untrusted_app')
G.edge['tee']['vpn_untrusted_app']['write-read'] = '[open open]'
G.add_edge('tee','trustonicpartner_app')
G.edge['tee']['trustonicpartner_app']['write-read'] = '[open open]'
G.add_edge('tee','llk_untrusted_app')
G.edge['tee']['llk_untrusted_app']['write-read'] = '[open open]'
G.add_edge('tee','filtered_untrusted_app')
G.edge['tee']['filtered_untrusted_app']['write-read'] = '[open open]'
G.add_edge('tee','filtered_google_app')
G.edge['tee']['filtered_google_app']['write-read'] = '[open open]'
G.add_edge('tee','knox_untrusted_app')
G.edge['tee']['knox_untrusted_app']['write-read'] = '[open open]'
G.add_edge('tee','irm_app')
G.edge['tee']['irm_app']['write-read'] = '[open open]'
G.add_edge('tee','gad_untrusted_app')
G.edge['tee']['gad_untrusted_app']['write-read'] = '[open open]'
G.add_edge('tee','carrier_app')
G.edge['tee']['carrier_app']['write-read'] = '[open open]'
G.add_edge('tee','lpm')
G.edge['tee']['lpm']['write-read'] = '[open open]'
G.add_edge('tee','mmi')
G.edge['tee']['mmi']['write-read'] = '[open open]'
G.add_edge('tee','mm-pp-daemon')
G.edge['tee']['mm-pp-daemon']['write-read'] = '[open open]'
G.add_edge('tee','mm-qcamera-daemon')
G.edge['tee']['mm-qcamera-daemon']['write-read'] = '[open open]'
G.add_edge('tee','newAttr96')
G.edge['tee']['newAttr96']['write-read'] = '[open open]'
G.add_edge('tee','radio')
G.edge['tee']['radio']['write-read'] = '[open open]'
G.add_edge('tee','s_system_app')
G.edge['tee']['s_system_app']['write-read'] = '[open open]'
G.add_edge('tee','surfaceflinger')
G.edge['tee']['surfaceflinger']['write-read'] = '[open open]'
G.add_edge('tee','system_app')
G.edge['tee']['system_app']['write-read'] = '[open open]'
G.add_edge('tee','wfd_app')
G.edge['tee']['wfd_app']['write-read'] = '[open open]'
G.add_edge('tee','wfdservice')
G.edge['tee']['wfdservice']['write-read'] = '[open open]'
G.add_edge('tee','zygote')
G.edge['tee']['zygote']['write-read'] = '[open open]'
G.add_edge('tee','isolated_app')
G.edge['tee']['isolated_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('tee','untrusted_app')
G.edge['tee']['untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('tee','umcagent_app')
G.edge['tee']['umcagent_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('tee','vpn_untrusted_app')
G.edge['tee']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('tee','trustonicpartner_app')
G.edge['tee']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('tee','llk_untrusted_app')
G.edge['tee']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('tee','filtered_untrusted_app')
G.edge['tee']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('tee','filtered_google_app')
G.edge['tee']['filtered_google_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('tee','knox_untrusted_app')
G.edge['tee']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('tee','irm_app')
G.edge['tee']['irm_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('tee','gad_untrusted_app')
G.edge['tee']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('tee','carrier_app')
G.edge['tee']['carrier_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('tee','newAttr96')
G.edge['tee']['newAttr96']['write-read'] = '[open open][setattr getattr]'
G.add_edge('tee','bintvoutservice')
G.edge['tee']['bintvoutservice']['write-read'] = '[open open][write read]'
G.edge['tee']['bintvoutservice']['fill'] = 'red'
G.add_edge('tee','bintvoutservice')
G.edge['tee']['bintvoutservice']['write-read'] = '[open open][write read][append read]'
G.add_edge('tee','bootanim')
G.edge['tee']['bootanim']['write-read'] = '[open open][write read]'
G.edge['tee']['bootanim']['fill'] = 'red'
G.add_edge('tee','bootanim')
G.edge['tee']['bootanim']['write-read'] = '[open open][write read][append read]'
G.add_edge('tee','commonplatformappdomain')
G.edge['tee']['commonplatformappdomain']['write-read'] = '[open open][write read]'
G.edge['tee']['commonplatformappdomain']['fill'] = 'red'
G.add_edge('tee','commonplatformappdomain')
G.edge['tee']['commonplatformappdomain']['write-read'] = '[open open][write read][append read]'
G.add_edge('tee','fixmo_app')
G.edge['tee']['fixmo_app']['write-read'] = '[open open][write read]'
G.edge['tee']['fixmo_app']['fill'] = 'red'
G.add_edge('tee','fixmo_app')
G.edge['tee']['fixmo_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('tee','good_app')
G.edge['tee']['good_app']['write-read'] = '[open open][write read]'
G.edge['tee']['good_app']['fill'] = 'red'
G.add_edge('tee','good_app')
G.edge['tee']['good_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('tee','healthd')
G.edge['tee']['healthd']['write-read'] = '[open open][write read]'
G.edge['tee']['healthd']['fill'] = 'red'
G.add_edge('tee','healthd')
G.edge['tee']['healthd']['write-read'] = '[open open][write read][append read]'
G.add_edge('tee','ime_app')
G.edge['tee']['ime_app']['write-read'] = '[open open][write read]'
G.edge['tee']['ime_app']['fill'] = 'red'
G.add_edge('tee','ime_app')
G.edge['tee']['ime_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('tee','isolated_app')
G.edge['tee']['isolated_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('tee','untrusted_app')
G.edge['tee']['untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('tee','umcagent_app')
G.edge['tee']['umcagent_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('tee','vpn_untrusted_app')
G.edge['tee']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('tee','trustonicpartner_app')
G.edge['tee']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('tee','llk_untrusted_app')
G.edge['tee']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('tee','filtered_untrusted_app')
G.edge['tee']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('tee','filtered_google_app')
G.edge['tee']['filtered_google_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('tee','knox_untrusted_app')
G.edge['tee']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('tee','irm_app')
G.edge['tee']['irm_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('tee','gad_untrusted_app')
G.edge['tee']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('tee','carrier_app')
G.edge['tee']['carrier_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('tee','lpm')
G.edge['tee']['lpm']['write-read'] = '[open open][write read]'
G.edge['tee']['lpm']['fill'] = 'red'
G.add_edge('tee','lpm')
G.edge['tee']['lpm']['write-read'] = '[open open][write read][append read]'
G.add_edge('tee','mmi')
G.edge['tee']['mmi']['write-read'] = '[open open][write read]'
G.edge['tee']['mmi']['fill'] = 'red'
G.add_edge('tee','mmi')
G.edge['tee']['mmi']['write-read'] = '[open open][write read][append read]'
G.add_edge('tee','mm-pp-daemon')
G.edge['tee']['mm-pp-daemon']['write-read'] = '[open open][write read]'
G.edge['tee']['mm-pp-daemon']['fill'] = 'red'
G.add_edge('tee','mm-pp-daemon')
G.edge['tee']['mm-pp-daemon']['write-read'] = '[open open][write read][append read]'
G.add_edge('tee','mm-qcamera-daemon')
G.edge['tee']['mm-qcamera-daemon']['write-read'] = '[open open][write read]'
G.edge['tee']['mm-qcamera-daemon']['fill'] = 'red'
G.add_edge('tee','mm-qcamera-daemon')
G.edge['tee']['mm-qcamera-daemon']['write-read'] = '[open open][write read][append read]'
G.add_edge('tee','newAttr96')
G.edge['tee']['newAttr96']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['tee']['newAttr96']['fill'] = 'red'
G.add_edge('tee','newAttr96')
G.edge['tee']['newAttr96']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('tee','radio')
G.edge['tee']['radio']['write-read'] = '[open open][write read]'
G.edge['tee']['radio']['fill'] = 'red'
G.add_edge('tee','radio')
G.edge['tee']['radio']['write-read'] = '[open open][write read][append read]'
G.add_edge('tee','s_system_app')
G.edge['tee']['s_system_app']['write-read'] = '[open open][write read]'
G.edge['tee']['s_system_app']['fill'] = 'red'
G.add_edge('tee','s_system_app')
G.edge['tee']['s_system_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('tee','surfaceflinger')
G.edge['tee']['surfaceflinger']['write-read'] = '[open open][write read]'
G.edge['tee']['surfaceflinger']['fill'] = 'red'
G.add_edge('tee','surfaceflinger')
G.edge['tee']['surfaceflinger']['write-read'] = '[open open][write read][append read]'
G.add_edge('tee','system_app')
G.edge['tee']['system_app']['write-read'] = '[open open][write read]'
G.edge['tee']['system_app']['fill'] = 'red'
G.add_edge('tee','system_app')
G.edge['tee']['system_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('tee','wfd_app')
G.edge['tee']['wfd_app']['write-read'] = '[open open][write read]'
G.edge['tee']['wfd_app']['fill'] = 'red'
G.add_edge('tee','wfd_app')
G.edge['tee']['wfd_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('tee','wfdservice')
G.edge['tee']['wfdservice']['write-read'] = '[open open][write read]'
G.edge['tee']['wfdservice']['fill'] = 'red'
G.add_edge('tee','wfdservice')
G.edge['tee']['wfdservice']['write-read'] = '[open open][write read][append read]'
G.add_edge('tee','zygote')
G.edge['tee']['zygote']['write-read'] = '[open open][write read]'
G.edge['tee']['zygote']['fill'] = 'red'
G.add_edge('tee','zygote')
G.edge['tee']['zygote']['write-read'] = '[open open][write read][append read]'
G.add_edge('wfd_app','bintvoutservice')
G.edge['wfd_app']['bintvoutservice']['write-read'] = '[open open]'
G.add_edge('wfd_app','bootanim')
G.edge['wfd_app']['bootanim']['write-read'] = '[open open]'
G.add_edge('wfd_app','commonplatformappdomain')
G.edge['wfd_app']['commonplatformappdomain']['write-read'] = '[open open]'
G.add_edge('wfd_app','fixmo_app')
G.edge['wfd_app']['fixmo_app']['write-read'] = '[open open]'
G.add_edge('wfd_app','good_app')
G.edge['wfd_app']['good_app']['write-read'] = '[open open]'
G.add_edge('wfd_app','healthd')
G.edge['wfd_app']['healthd']['write-read'] = '[open open]'
G.add_edge('wfd_app','ime_app')
G.edge['wfd_app']['ime_app']['write-read'] = '[open open]'
G.add_edge('wfd_app','isolated_app')
G.edge['wfd_app']['isolated_app']['write-read'] = '[open open]'
G.add_edge('wfd_app','untrusted_app')
G.edge['wfd_app']['untrusted_app']['write-read'] = '[open open]'
G.add_edge('wfd_app','umcagent_app')
G.edge['wfd_app']['umcagent_app']['write-read'] = '[open open]'
G.add_edge('wfd_app','vpn_untrusted_app')
G.edge['wfd_app']['vpn_untrusted_app']['write-read'] = '[open open]'
G.add_edge('wfd_app','trustonicpartner_app')
G.edge['wfd_app']['trustonicpartner_app']['write-read'] = '[open open]'
G.add_edge('wfd_app','llk_untrusted_app')
G.edge['wfd_app']['llk_untrusted_app']['write-read'] = '[open open]'
G.add_edge('wfd_app','filtered_untrusted_app')
G.edge['wfd_app']['filtered_untrusted_app']['write-read'] = '[open open]'
G.add_edge('wfd_app','filtered_google_app')
G.edge['wfd_app']['filtered_google_app']['write-read'] = '[open open]'
G.add_edge('wfd_app','knox_untrusted_app')
G.edge['wfd_app']['knox_untrusted_app']['write-read'] = '[open open]'
G.add_edge('wfd_app','irm_app')
G.edge['wfd_app']['irm_app']['write-read'] = '[open open]'
G.add_edge('wfd_app','gad_untrusted_app')
G.edge['wfd_app']['gad_untrusted_app']['write-read'] = '[open open]'
G.add_edge('wfd_app','carrier_app')
G.edge['wfd_app']['carrier_app']['write-read'] = '[open open]'
G.add_edge('wfd_app','lpm')
G.edge['wfd_app']['lpm']['write-read'] = '[open open]'
G.add_edge('wfd_app','mmi')
G.edge['wfd_app']['mmi']['write-read'] = '[open open]'
G.add_edge('wfd_app','mm-pp-daemon')
G.edge['wfd_app']['mm-pp-daemon']['write-read'] = '[open open]'
G.add_edge('wfd_app','mm-qcamera-daemon')
G.edge['wfd_app']['mm-qcamera-daemon']['write-read'] = '[open open]'
G.add_edge('wfd_app','newAttr96')
G.edge['wfd_app']['newAttr96']['write-read'] = '[open open]'
G.add_edge('wfd_app','radio')
G.edge['wfd_app']['radio']['write-read'] = '[open open]'
G.add_edge('wfd_app','s_system_app')
G.edge['wfd_app']['s_system_app']['write-read'] = '[open open]'
G.add_edge('wfd_app','surfaceflinger')
G.edge['wfd_app']['surfaceflinger']['write-read'] = '[open open]'
G.add_edge('wfd_app','system_app')
G.edge['wfd_app']['system_app']['write-read'] = '[open open]'
G.add_edge('wfd_app','wfd_app')
G.edge['wfd_app']['wfd_app']['write-read'] = '[open open]'
G.add_edge('wfd_app','wfdservice')
G.edge['wfd_app']['wfdservice']['write-read'] = '[open open]'
G.add_edge('wfd_app','zygote')
G.edge['wfd_app']['zygote']['write-read'] = '[open open]'
G.add_edge('wfd_app','isolated_app')
G.edge['wfd_app']['isolated_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('wfd_app','untrusted_app')
G.edge['wfd_app']['untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('wfd_app','umcagent_app')
G.edge['wfd_app']['umcagent_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('wfd_app','vpn_untrusted_app')
G.edge['wfd_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('wfd_app','trustonicpartner_app')
G.edge['wfd_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('wfd_app','llk_untrusted_app')
G.edge['wfd_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('wfd_app','filtered_untrusted_app')
G.edge['wfd_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('wfd_app','filtered_google_app')
G.edge['wfd_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('wfd_app','knox_untrusted_app')
G.edge['wfd_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('wfd_app','irm_app')
G.edge['wfd_app']['irm_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('wfd_app','gad_untrusted_app')
G.edge['wfd_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('wfd_app','carrier_app')
G.edge['wfd_app']['carrier_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('wfd_app','newAttr96')
G.edge['wfd_app']['newAttr96']['write-read'] = '[open open][setattr getattr]'
G.add_edge('wfd_app','bintvoutservice')
G.edge['wfd_app']['bintvoutservice']['write-read'] = '[open open][write read]'
G.edge['wfd_app']['bintvoutservice']['fill'] = 'red'
G.add_edge('wfd_app','bintvoutservice')
G.edge['wfd_app']['bintvoutservice']['write-read'] = '[open open][write read][append read]'
G.add_edge('wfd_app','bootanim')
G.edge['wfd_app']['bootanim']['write-read'] = '[open open][write read]'
G.edge['wfd_app']['bootanim']['fill'] = 'red'
G.add_edge('wfd_app','bootanim')
G.edge['wfd_app']['bootanim']['write-read'] = '[open open][write read][append read]'
G.add_edge('wfd_app','commonplatformappdomain')
G.edge['wfd_app']['commonplatformappdomain']['write-read'] = '[open open][write read]'
G.edge['wfd_app']['commonplatformappdomain']['fill'] = 'red'
G.add_edge('wfd_app','commonplatformappdomain')
G.edge['wfd_app']['commonplatformappdomain']['write-read'] = '[open open][write read][append read]'
G.add_edge('wfd_app','fixmo_app')
G.edge['wfd_app']['fixmo_app']['write-read'] = '[open open][write read]'
G.edge['wfd_app']['fixmo_app']['fill'] = 'red'
G.add_edge('wfd_app','fixmo_app')
G.edge['wfd_app']['fixmo_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('wfd_app','good_app')
G.edge['wfd_app']['good_app']['write-read'] = '[open open][write read]'
G.edge['wfd_app']['good_app']['fill'] = 'red'
G.add_edge('wfd_app','good_app')
G.edge['wfd_app']['good_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('wfd_app','healthd')
G.edge['wfd_app']['healthd']['write-read'] = '[open open][write read]'
G.edge['wfd_app']['healthd']['fill'] = 'red'
G.add_edge('wfd_app','healthd')
G.edge['wfd_app']['healthd']['write-read'] = '[open open][write read][append read]'
G.add_edge('wfd_app','ime_app')
G.edge['wfd_app']['ime_app']['write-read'] = '[open open][write read]'
G.edge['wfd_app']['ime_app']['fill'] = 'red'
G.add_edge('wfd_app','ime_app')
G.edge['wfd_app']['ime_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('wfd_app','isolated_app')
G.edge['wfd_app']['isolated_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('wfd_app','untrusted_app')
G.edge['wfd_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('wfd_app','umcagent_app')
G.edge['wfd_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('wfd_app','vpn_untrusted_app')
G.edge['wfd_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('wfd_app','trustonicpartner_app')
G.edge['wfd_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('wfd_app','llk_untrusted_app')
G.edge['wfd_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('wfd_app','filtered_untrusted_app')
G.edge['wfd_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('wfd_app','filtered_google_app')
G.edge['wfd_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('wfd_app','knox_untrusted_app')
G.edge['wfd_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('wfd_app','irm_app')
G.edge['wfd_app']['irm_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('wfd_app','gad_untrusted_app')
G.edge['wfd_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('wfd_app','carrier_app')
G.edge['wfd_app']['carrier_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('wfd_app','lpm')
G.edge['wfd_app']['lpm']['write-read'] = '[open open][write read]'
G.edge['wfd_app']['lpm']['fill'] = 'red'
G.add_edge('wfd_app','lpm')
G.edge['wfd_app']['lpm']['write-read'] = '[open open][write read][append read]'
G.add_edge('wfd_app','mmi')
G.edge['wfd_app']['mmi']['write-read'] = '[open open][write read]'
G.edge['wfd_app']['mmi']['fill'] = 'red'
G.add_edge('wfd_app','mmi')
G.edge['wfd_app']['mmi']['write-read'] = '[open open][write read][append read]'
G.add_edge('wfd_app','mm-pp-daemon')
G.edge['wfd_app']['mm-pp-daemon']['write-read'] = '[open open][write read]'
G.edge['wfd_app']['mm-pp-daemon']['fill'] = 'red'
G.add_edge('wfd_app','mm-pp-daemon')
G.edge['wfd_app']['mm-pp-daemon']['write-read'] = '[open open][write read][append read]'
G.add_edge('wfd_app','mm-qcamera-daemon')
G.edge['wfd_app']['mm-qcamera-daemon']['write-read'] = '[open open][write read]'
G.edge['wfd_app']['mm-qcamera-daemon']['fill'] = 'red'
G.add_edge('wfd_app','mm-qcamera-daemon')
G.edge['wfd_app']['mm-qcamera-daemon']['write-read'] = '[open open][write read][append read]'
G.add_edge('wfd_app','newAttr96')
G.edge['wfd_app']['newAttr96']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['wfd_app']['newAttr96']['fill'] = 'red'
G.add_edge('wfd_app','newAttr96')
G.edge['wfd_app']['newAttr96']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('wfd_app','radio')
G.edge['wfd_app']['radio']['write-read'] = '[open open][write read]'
G.edge['wfd_app']['radio']['fill'] = 'red'
G.add_edge('wfd_app','radio')
G.edge['wfd_app']['radio']['write-read'] = '[open open][write read][append read]'
G.add_edge('wfd_app','s_system_app')
G.edge['wfd_app']['s_system_app']['write-read'] = '[open open][write read]'
G.edge['wfd_app']['s_system_app']['fill'] = 'red'
G.add_edge('wfd_app','s_system_app')
G.edge['wfd_app']['s_system_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('wfd_app','surfaceflinger')
G.edge['wfd_app']['surfaceflinger']['write-read'] = '[open open][write read]'
G.edge['wfd_app']['surfaceflinger']['fill'] = 'red'
G.add_edge('wfd_app','surfaceflinger')
G.edge['wfd_app']['surfaceflinger']['write-read'] = '[open open][write read][append read]'
G.add_edge('wfd_app','system_app')
G.edge['wfd_app']['system_app']['write-read'] = '[open open][write read]'
G.edge['wfd_app']['system_app']['fill'] = 'red'
G.add_edge('wfd_app','system_app')
G.edge['wfd_app']['system_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('wfd_app','wfd_app')
G.edge['wfd_app']['wfd_app']['write-read'] = '[open open][write read]'
G.edge['wfd_app']['wfd_app']['fill'] = 'red'
G.add_edge('wfd_app','wfd_app')
G.edge['wfd_app']['wfd_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('wfd_app','wfdservice')
G.edge['wfd_app']['wfdservice']['write-read'] = '[open open][write read]'
G.edge['wfd_app']['wfdservice']['fill'] = 'red'
G.add_edge('wfd_app','wfdservice')
G.edge['wfd_app']['wfdservice']['write-read'] = '[open open][write read][append read]'
G.add_edge('wfd_app','zygote')
G.edge['wfd_app']['zygote']['write-read'] = '[open open][write read]'
G.edge['wfd_app']['zygote']['fill'] = 'red'
G.add_edge('wfd_app','zygote')
G.edge['wfd_app']['zygote']['write-read'] = '[open open][write read][append read]'
G.add_edge('wfdservice','bintvoutservice')
G.edge['wfdservice']['bintvoutservice']['write-read'] = '[open open]'
G.add_edge('wfdservice','bootanim')
G.edge['wfdservice']['bootanim']['write-read'] = '[open open]'
G.add_edge('wfdservice','commonplatformappdomain')
G.edge['wfdservice']['commonplatformappdomain']['write-read'] = '[setopt getopt][open open]'
G.add_edge('wfdservice','fixmo_app')
G.edge['wfdservice']['fixmo_app']['write-read'] = '[open open]'
G.add_edge('wfdservice','good_app')
G.edge['wfdservice']['good_app']['write-read'] = '[open open]'
G.add_edge('wfdservice','healthd')
G.edge['wfdservice']['healthd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open]'
G.add_edge('wfdservice','ime_app')
G.edge['wfdservice']['ime_app']['write-read'] = '[setattr getattr][setopt getopt][open open]'
G.add_edge('wfdservice','isolated_app')
G.edge['wfdservice']['isolated_app']['write-read'] = '[open open]'
G.add_edge('wfdservice','untrusted_app')
G.edge['wfdservice']['untrusted_app']['write-read'] = '[open open]'
G.add_edge('wfdservice','umcagent_app')
G.edge['wfdservice']['umcagent_app']['write-read'] = '[open open]'
G.add_edge('wfdservice','vpn_untrusted_app')
G.edge['wfdservice']['vpn_untrusted_app']['write-read'] = '[open open]'
G.add_edge('wfdservice','trustonicpartner_app')
G.edge['wfdservice']['trustonicpartner_app']['write-read'] = '[open open]'
G.add_edge('wfdservice','llk_untrusted_app')
G.edge['wfdservice']['llk_untrusted_app']['write-read'] = '[open open]'
G.add_edge('wfdservice','filtered_untrusted_app')
G.edge['wfdservice']['filtered_untrusted_app']['write-read'] = '[open open]'
G.add_edge('wfdservice','filtered_google_app')
G.edge['wfdservice']['filtered_google_app']['write-read'] = '[open open]'
G.add_edge('wfdservice','knox_untrusted_app')
G.edge['wfdservice']['knox_untrusted_app']['write-read'] = '[open open]'
G.add_edge('wfdservice','irm_app')
G.edge['wfdservice']['irm_app']['write-read'] = '[open open]'
G.add_edge('wfdservice','gad_untrusted_app')
G.edge['wfdservice']['gad_untrusted_app']['write-read'] = '[open open]'
G.add_edge('wfdservice','carrier_app')
G.edge['wfdservice']['carrier_app']['write-read'] = '[open open]'
G.add_edge('wfdservice','lpm')
G.edge['wfdservice']['lpm']['write-read'] = '[setopt getopt][open open]'
G.add_edge('wfdservice','mmi')
G.edge['wfdservice']['mmi']['write-read'] = '[open open]'
G.add_edge('wfdservice','mm-pp-daemon')
G.edge['wfdservice']['mm-pp-daemon']['write-read'] = '[open open]'
G.add_edge('wfdservice','mm-qcamera-daemon')
G.edge['wfdservice']['mm-qcamera-daemon']['write-read'] = '[open open]'
G.add_edge('wfdservice','newAttr96')
G.edge['wfdservice']['newAttr96']['write-read'] = '[open open]'
G.add_edge('wfdservice','radio')
G.edge['wfdservice']['radio']['write-read'] = '[open open]'
G.add_edge('wfdservice','s_system_app')
G.edge['wfdservice']['s_system_app']['write-read'] = '[setattr getattr][setopt getopt][open open]'
G.add_edge('wfdservice','surfaceflinger')
G.edge['wfdservice']['surfaceflinger']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open]'
G.add_edge('wfdservice','system_app')
G.edge['wfdservice']['system_app']['write-read'] = '[setattr getattr][setopt getopt][open open]'
G.add_edge('wfdservice','wfd_app')
G.edge['wfdservice']['wfd_app']['write-read'] = '[open open]'
G.add_edge('wfdservice','wfdservice')
G.edge['wfdservice']['wfdservice']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open]'
G.add_edge('wfdservice','zygote')
G.edge['wfdservice']['zygote']['write-read'] = '[open open]'
G.add_edge('wfdservice','isolated_app')
G.edge['wfdservice']['isolated_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('wfdservice','untrusted_app')
G.edge['wfdservice']['untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('wfdservice','umcagent_app')
G.edge['wfdservice']['umcagent_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('wfdservice','vpn_untrusted_app')
G.edge['wfdservice']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('wfdservice','trustonicpartner_app')
G.edge['wfdservice']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('wfdservice','llk_untrusted_app')
G.edge['wfdservice']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('wfdservice','filtered_untrusted_app')
G.edge['wfdservice']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('wfdservice','filtered_google_app')
G.edge['wfdservice']['filtered_google_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('wfdservice','knox_untrusted_app')
G.edge['wfdservice']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('wfdservice','irm_app')
G.edge['wfdservice']['irm_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('wfdservice','gad_untrusted_app')
G.edge['wfdservice']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('wfdservice','carrier_app')
G.edge['wfdservice']['carrier_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('wfdservice','newAttr96')
G.edge['wfdservice']['newAttr96']['write-read'] = '[open open][setattr getattr]'
G.add_edge('wfdservice','bintvoutservice')
G.edge['wfdservice']['bintvoutservice']['write-read'] = '[open open][write read]'
G.edge['wfdservice']['bintvoutservice']['fill'] = 'red'
G.add_edge('wfdservice','bintvoutservice')
G.edge['wfdservice']['bintvoutservice']['write-read'] = '[open open][write read][append read]'
G.add_edge('wfdservice','bootanim')
G.edge['wfdservice']['bootanim']['write-read'] = '[open open][write read]'
G.edge['wfdservice']['bootanim']['fill'] = 'red'
G.add_edge('wfdservice','bootanim')
G.edge['wfdservice']['bootanim']['write-read'] = '[open open][write read][append read]'
G.add_edge('wfdservice','commonplatformappdomain')
G.edge['wfdservice']['commonplatformappdomain']['write-read'] = '[setopt getopt][open open][write read]'
G.edge['wfdservice']['commonplatformappdomain']['fill'] = 'red'
G.add_edge('wfdservice','commonplatformappdomain')
G.edge['wfdservice']['commonplatformappdomain']['write-read'] = '[setopt getopt][open open][write read][append read]'
G.add_edge('wfdservice','fixmo_app')
G.edge['wfdservice']['fixmo_app']['write-read'] = '[open open][write read]'
G.edge['wfdservice']['fixmo_app']['fill'] = 'red'
G.add_edge('wfdservice','fixmo_app')
G.edge['wfdservice']['fixmo_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('wfdservice','good_app')
G.edge['wfdservice']['good_app']['write-read'] = '[open open][write read]'
G.edge['wfdservice']['good_app']['fill'] = 'red'
G.add_edge('wfdservice','good_app')
G.edge['wfdservice']['good_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('wfdservice','healthd')
G.edge['wfdservice']['healthd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read]'
G.edge['wfdservice']['healthd']['fill'] = 'red'
G.add_edge('wfdservice','healthd')
G.edge['wfdservice']['healthd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read]'
G.add_edge('wfdservice','ime_app')
G.edge['wfdservice']['ime_app']['write-read'] = '[setattr getattr][setopt getopt][open open][write read]'
G.edge['wfdservice']['ime_app']['fill'] = 'red'
G.add_edge('wfdservice','ime_app')
G.edge['wfdservice']['ime_app']['write-read'] = '[setattr getattr][setopt getopt][open open][write read][append read]'
G.add_edge('wfdservice','isolated_app')
G.edge['wfdservice']['isolated_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('wfdservice','untrusted_app')
G.edge['wfdservice']['untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('wfdservice','umcagent_app')
G.edge['wfdservice']['umcagent_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('wfdservice','vpn_untrusted_app')
G.edge['wfdservice']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('wfdservice','trustonicpartner_app')
G.edge['wfdservice']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('wfdservice','llk_untrusted_app')
G.edge['wfdservice']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('wfdservice','filtered_untrusted_app')
G.edge['wfdservice']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('wfdservice','filtered_google_app')
G.edge['wfdservice']['filtered_google_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('wfdservice','knox_untrusted_app')
G.edge['wfdservice']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('wfdservice','irm_app')
G.edge['wfdservice']['irm_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('wfdservice','gad_untrusted_app')
G.edge['wfdservice']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('wfdservice','carrier_app')
G.edge['wfdservice']['carrier_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('wfdservice','lpm')
G.edge['wfdservice']['lpm']['write-read'] = '[setopt getopt][open open][write read]'
G.edge['wfdservice']['lpm']['fill'] = 'red'
G.add_edge('wfdservice','lpm')
G.edge['wfdservice']['lpm']['write-read'] = '[setopt getopt][open open][write read][append read]'
G.add_edge('wfdservice','mmi')
G.edge['wfdservice']['mmi']['write-read'] = '[open open][write read]'
G.edge['wfdservice']['mmi']['fill'] = 'red'
G.add_edge('wfdservice','mmi')
G.edge['wfdservice']['mmi']['write-read'] = '[open open][write read][append read]'
G.add_edge('wfdservice','mm-pp-daemon')
G.edge['wfdservice']['mm-pp-daemon']['write-read'] = '[open open][write read]'
G.edge['wfdservice']['mm-pp-daemon']['fill'] = 'red'
G.add_edge('wfdservice','mm-pp-daemon')
G.edge['wfdservice']['mm-pp-daemon']['write-read'] = '[open open][write read][append read]'
G.add_edge('wfdservice','mm-qcamera-daemon')
G.edge['wfdservice']['mm-qcamera-daemon']['write-read'] = '[open open][write read]'
G.edge['wfdservice']['mm-qcamera-daemon']['fill'] = 'red'
G.add_edge('wfdservice','mm-qcamera-daemon')
G.edge['wfdservice']['mm-qcamera-daemon']['write-read'] = '[open open][write read][append read]'
G.add_edge('wfdservice','newAttr96')
G.edge['wfdservice']['newAttr96']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['wfdservice']['newAttr96']['fill'] = 'red'
G.add_edge('wfdservice','newAttr96')
G.edge['wfdservice']['newAttr96']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('wfdservice','radio')
G.edge['wfdservice']['radio']['write-read'] = '[open open][write read]'
G.edge['wfdservice']['radio']['fill'] = 'red'
G.add_edge('wfdservice','radio')
G.edge['wfdservice']['radio']['write-read'] = '[open open][write read][append read]'
G.add_edge('wfdservice','s_system_app')
G.edge['wfdservice']['s_system_app']['write-read'] = '[setattr getattr][setopt getopt][open open][write read]'
G.edge['wfdservice']['s_system_app']['fill'] = 'red'
G.add_edge('wfdservice','s_system_app')
G.edge['wfdservice']['s_system_app']['write-read'] = '[setattr getattr][setopt getopt][open open][write read][append read]'
G.add_edge('wfdservice','surfaceflinger')
G.edge['wfdservice']['surfaceflinger']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read]'
G.edge['wfdservice']['surfaceflinger']['fill'] = 'red'
G.add_edge('wfdservice','surfaceflinger')
G.edge['wfdservice']['surfaceflinger']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read]'
G.add_edge('wfdservice','system_app')
G.edge['wfdservice']['system_app']['write-read'] = '[setattr getattr][setopt getopt][open open][write read]'
G.edge['wfdservice']['system_app']['fill'] = 'red'
G.add_edge('wfdservice','system_app')
G.edge['wfdservice']['system_app']['write-read'] = '[setattr getattr][setopt getopt][open open][write read][append read]'
G.add_edge('wfdservice','wfd_app')
G.edge['wfdservice']['wfd_app']['write-read'] = '[open open][write read]'
G.edge['wfdservice']['wfd_app']['fill'] = 'red'
G.add_edge('wfdservice','wfd_app')
G.edge['wfdservice']['wfd_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('wfdservice','wfdservice')
G.edge['wfdservice']['wfdservice']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read]'
G.edge['wfdservice']['wfdservice']['fill'] = 'red'
G.add_edge('wfdservice','wfdservice')
G.edge['wfdservice']['wfdservice']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read]'
G.add_edge('wfdservice','zygote')
G.edge['wfdservice']['zygote']['write-read'] = '[open open][write read]'
G.edge['wfdservice']['zygote']['fill'] = 'red'
G.add_edge('wfdservice','zygote')
G.edge['wfdservice']['zygote']['write-read'] = '[open open][write read][append read]'
G.add_edge('zygote','bintvoutservice')
G.edge['zygote']['bintvoutservice']['write-read'] = '[open open]'
G.add_edge('zygote','bootanim')
G.edge['zygote']['bootanim']['write-read'] = '[open open]'
G.add_edge('zygote','commonplatformappdomain')
G.edge['zygote']['commonplatformappdomain']['write-read'] = '[open open]'
G.add_edge('zygote','fixmo_app')
G.edge['zygote']['fixmo_app']['write-read'] = '[open open]'
G.add_edge('zygote','good_app')
G.edge['zygote']['good_app']['write-read'] = '[open open]'
G.add_edge('zygote','healthd')
G.edge['zygote']['healthd']['write-read'] = '[open open]'
G.add_edge('zygote','ime_app')
G.edge['zygote']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('zygote','isolated_app')
G.edge['zygote']['isolated_app']['write-read'] = '[open open]'
G.add_edge('zygote','untrusted_app')
G.edge['zygote']['untrusted_app']['write-read'] = '[open open]'
G.add_edge('zygote','umcagent_app')
G.edge['zygote']['umcagent_app']['write-read'] = '[open open]'
G.add_edge('zygote','vpn_untrusted_app')
G.edge['zygote']['vpn_untrusted_app']['write-read'] = '[open open]'
G.add_edge('zygote','trustonicpartner_app')
G.edge['zygote']['trustonicpartner_app']['write-read'] = '[open open]'
G.add_edge('zygote','llk_untrusted_app')
G.edge['zygote']['llk_untrusted_app']['write-read'] = '[open open]'
G.add_edge('zygote','filtered_untrusted_app')
G.edge['zygote']['filtered_untrusted_app']['write-read'] = '[open open]'
G.add_edge('zygote','filtered_google_app')
G.edge['zygote']['filtered_google_app']['write-read'] = '[open open]'
G.add_edge('zygote','knox_untrusted_app')
G.edge['zygote']['knox_untrusted_app']['write-read'] = '[open open]'
G.add_edge('zygote','irm_app')
G.edge['zygote']['irm_app']['write-read'] = '[open open]'
G.add_edge('zygote','gad_untrusted_app')
G.edge['zygote']['gad_untrusted_app']['write-read'] = '[open open]'
G.add_edge('zygote','carrier_app')
G.edge['zygote']['carrier_app']['write-read'] = '[open open]'
G.add_edge('zygote','lpm')
G.edge['zygote']['lpm']['write-read'] = '[open open]'
G.add_edge('zygote','mmi')
G.edge['zygote']['mmi']['write-read'] = '[open open]'
G.add_edge('zygote','mm-pp-daemon')
G.edge['zygote']['mm-pp-daemon']['write-read'] = '[open open]'
G.add_edge('zygote','mm-qcamera-daemon')
G.edge['zygote']['mm-qcamera-daemon']['write-read'] = '[open open]'
G.add_edge('zygote','newAttr96')
G.edge['zygote']['newAttr96']['write-read'] = '[open open]'
G.add_edge('zygote','radio')
G.edge['zygote']['radio']['write-read'] = '[open open]'
G.add_edge('zygote','s_system_app')
G.edge['zygote']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('zygote','surfaceflinger')
G.edge['zygote']['surfaceflinger']['write-read'] = '[open open]'
G.add_edge('zygote','system_app')
G.edge['zygote']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('zygote','wfd_app')
G.edge['zygote']['wfd_app']['write-read'] = '[open open]'
G.add_edge('zygote','wfdservice')
G.edge['zygote']['wfdservice']['write-read'] = '[open open]'
G.add_edge('zygote','zygote')
G.edge['zygote']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('zygote','isolated_app')
G.edge['zygote']['isolated_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('zygote','untrusted_app')
G.edge['zygote']['untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('zygote','umcagent_app')
G.edge['zygote']['umcagent_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('zygote','vpn_untrusted_app')
G.edge['zygote']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('zygote','trustonicpartner_app')
G.edge['zygote']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('zygote','llk_untrusted_app')
G.edge['zygote']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('zygote','filtered_untrusted_app')
G.edge['zygote']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('zygote','filtered_google_app')
G.edge['zygote']['filtered_google_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('zygote','knox_untrusted_app')
G.edge['zygote']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('zygote','irm_app')
G.edge['zygote']['irm_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('zygote','gad_untrusted_app')
G.edge['zygote']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('zygote','carrier_app')
G.edge['zygote']['carrier_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('zygote','newAttr96')
G.edge['zygote']['newAttr96']['write-read'] = '[open open][setattr getattr]'
G.add_edge('zygote','bintvoutservice')
G.edge['zygote']['bintvoutservice']['write-read'] = '[open open][write read]'
G.edge['zygote']['bintvoutservice']['fill'] = 'red'
G.add_edge('zygote','bintvoutservice')
G.edge['zygote']['bintvoutservice']['write-read'] = '[open open][write read][append read]'
G.add_edge('zygote','bootanim')
G.edge['zygote']['bootanim']['write-read'] = '[open open][write read]'
G.edge['zygote']['bootanim']['fill'] = 'red'
G.add_edge('zygote','bootanim')
G.edge['zygote']['bootanim']['write-read'] = '[open open][write read][append read]'
G.add_edge('zygote','commonplatformappdomain')
G.edge['zygote']['commonplatformappdomain']['write-read'] = '[open open][write read]'
G.edge['zygote']['commonplatformappdomain']['fill'] = 'red'
G.add_edge('zygote','commonplatformappdomain')
G.edge['zygote']['commonplatformappdomain']['write-read'] = '[open open][write read][append read]'
G.add_edge('zygote','fixmo_app')
G.edge['zygote']['fixmo_app']['write-read'] = '[open open][write read]'
G.edge['zygote']['fixmo_app']['fill'] = 'red'
G.add_edge('zygote','fixmo_app')
G.edge['zygote']['fixmo_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('zygote','good_app')
G.edge['zygote']['good_app']['write-read'] = '[open open][write read]'
G.edge['zygote']['good_app']['fill'] = 'red'
G.add_edge('zygote','good_app')
G.edge['zygote']['good_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('zygote','healthd')
G.edge['zygote']['healthd']['write-read'] = '[open open][write read]'
G.edge['zygote']['healthd']['fill'] = 'red'
G.add_edge('zygote','healthd')
G.edge['zygote']['healthd']['write-read'] = '[open open][write read][append read]'
G.add_edge('zygote','ime_app')
G.edge['zygote']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['zygote']['ime_app']['fill'] = 'red'
G.add_edge('zygote','ime_app')
G.edge['zygote']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('zygote','isolated_app')
G.edge['zygote']['isolated_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('zygote','untrusted_app')
G.edge['zygote']['untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('zygote','umcagent_app')
G.edge['zygote']['umcagent_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('zygote','vpn_untrusted_app')
G.edge['zygote']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('zygote','trustonicpartner_app')
G.edge['zygote']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('zygote','llk_untrusted_app')
G.edge['zygote']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('zygote','filtered_untrusted_app')
G.edge['zygote']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('zygote','filtered_google_app')
G.edge['zygote']['filtered_google_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('zygote','knox_untrusted_app')
G.edge['zygote']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('zygote','irm_app')
G.edge['zygote']['irm_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('zygote','gad_untrusted_app')
G.edge['zygote']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('zygote','carrier_app')
G.edge['zygote']['carrier_app']['write-read'] = '[open open][setattr getattr][append read]'
G.add_edge('zygote','lpm')
G.edge['zygote']['lpm']['write-read'] = '[open open][write read]'
G.edge['zygote']['lpm']['fill'] = 'red'
G.add_edge('zygote','lpm')
G.edge['zygote']['lpm']['write-read'] = '[open open][write read][append read]'
G.add_edge('zygote','mmi')
G.edge['zygote']['mmi']['write-read'] = '[open open][write read]'
G.edge['zygote']['mmi']['fill'] = 'red'
G.add_edge('zygote','mmi')
G.edge['zygote']['mmi']['write-read'] = '[open open][write read][append read]'
G.add_edge('zygote','mm-pp-daemon')
G.edge['zygote']['mm-pp-daemon']['write-read'] = '[open open][write read]'
G.edge['zygote']['mm-pp-daemon']['fill'] = 'red'
G.add_edge('zygote','mm-pp-daemon')
G.edge['zygote']['mm-pp-daemon']['write-read'] = '[open open][write read][append read]'
G.add_edge('zygote','mm-qcamera-daemon')
G.edge['zygote']['mm-qcamera-daemon']['write-read'] = '[open open][write read]'
G.edge['zygote']['mm-qcamera-daemon']['fill'] = 'red'
G.add_edge('zygote','mm-qcamera-daemon')
G.edge['zygote']['mm-qcamera-daemon']['write-read'] = '[open open][write read][append read]'
G.add_edge('zygote','newAttr96')
G.edge['zygote']['newAttr96']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['zygote']['newAttr96']['fill'] = 'red'
G.add_edge('zygote','newAttr96')
G.edge['zygote']['newAttr96']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('zygote','radio')
G.edge['zygote']['radio']['write-read'] = '[open open][write read]'
G.edge['zygote']['radio']['fill'] = 'red'
G.add_edge('zygote','radio')
G.edge['zygote']['radio']['write-read'] = '[open open][write read][append read]'
G.add_edge('zygote','s_system_app')
G.edge['zygote']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['zygote']['s_system_app']['fill'] = 'red'
G.add_edge('zygote','s_system_app')
G.edge['zygote']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('zygote','surfaceflinger')
G.edge['zygote']['surfaceflinger']['write-read'] = '[open open][write read]'
G.edge['zygote']['surfaceflinger']['fill'] = 'red'
G.add_edge('zygote','surfaceflinger')
G.edge['zygote']['surfaceflinger']['write-read'] = '[open open][write read][append read]'
G.add_edge('zygote','system_app')
G.edge['zygote']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['zygote']['system_app']['fill'] = 'red'
G.add_edge('zygote','system_app')
G.edge['zygote']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('zygote','wfd_app')
G.edge['zygote']['wfd_app']['write-read'] = '[open open][write read]'
G.edge['zygote']['wfd_app']['fill'] = 'red'
G.add_edge('zygote','wfd_app')
G.edge['zygote']['wfd_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('zygote','wfdservice')
G.edge['zygote']['wfdservice']['write-read'] = '[open open][write read]'
G.edge['zygote']['wfdservice']['fill'] = 'red'
G.add_edge('zygote','wfdservice')
G.edge['zygote']['wfdservice']['write-read'] = '[open open][write read][append read]'
G.add_edge('zygote','zygote')
G.edge['zygote']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['zygote']['zygote']['fill'] = 'red'
G.add_edge('zygote','zygote')
G.edge['zygote']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
app = Viewer(G)
app.mainloop()