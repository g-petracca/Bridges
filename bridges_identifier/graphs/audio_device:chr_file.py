import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('audiod','audiod')
G.edge['audiod']['audiod']['write-read'] = '[open open]'
G.add_edge('audiod','bootanim')
G.edge['audiod']['bootanim']['write-read'] = '[open open]'
G.add_edge('audiod','dtsconfigurator')
G.edge['audiod']['dtsconfigurator']['write-read'] = '[open open]'
G.add_edge('audiod','dtseagleservice')
G.edge['audiod']['dtseagleservice']['write-read'] = '[open open]'
G.add_edge('audiod','jackservice')
G.edge['audiod']['jackservice']['write-read'] = '[open open]'
G.add_edge('audiod','mediaserver')
G.edge['audiod']['mediaserver']['write-read'] = '[open open]'
G.add_edge('audiod','oneseg_mw')
G.edge['audiod']['oneseg_mw']['write-read'] = '[open open]'
G.add_edge('audiod','s_system_app')
G.edge['audiod']['s_system_app']['write-read'] = '[open open]'
G.add_edge('audiod','usf')
G.edge['audiod']['usf']['write-read'] = '[open open]'
G.add_edge('audiod','wfdservice')
G.edge['audiod']['wfdservice']['write-read'] = '[open open]'
G.add_edge('audiod','audiod')
G.edge['audiod']['audiod']['write-read'] = '[open open][write read]'
G.edge['audiod']['audiod']['fill'] = 'red'
G.add_edge('audiod','audiod')
G.edge['audiod']['audiod']['write-read'] = '[open open][write read][append read]'
G.add_edge('audiod','bootanim')
G.edge['audiod']['bootanim']['write-read'] = '[open open][write read]'
G.edge['audiod']['bootanim']['fill'] = 'red'
G.add_edge('audiod','bootanim')
G.edge['audiod']['bootanim']['write-read'] = '[open open][write read][append read]'
G.add_edge('audiod','dtsconfigurator')
G.edge['audiod']['dtsconfigurator']['write-read'] = '[open open][write read]'
G.edge['audiod']['dtsconfigurator']['fill'] = 'red'
G.add_edge('audiod','dtsconfigurator')
G.edge['audiod']['dtsconfigurator']['write-read'] = '[open open][write read][append read]'
G.add_edge('audiod','dtseagleservice')
G.edge['audiod']['dtseagleservice']['write-read'] = '[open open][write read]'
G.edge['audiod']['dtseagleservice']['fill'] = 'red'
G.add_edge('audiod','dtseagleservice')
G.edge['audiod']['dtseagleservice']['write-read'] = '[open open][write read][append read]'
G.add_edge('audiod','jackservice')
G.edge['audiod']['jackservice']['write-read'] = '[open open][write read]'
G.edge['audiod']['jackservice']['fill'] = 'red'
G.add_edge('audiod','jackservice')
G.edge['audiod']['jackservice']['write-read'] = '[open open][write read][append read]'
G.add_edge('audiod','mediaserver')
G.edge['audiod']['mediaserver']['write-read'] = '[open open][write read]'
G.edge['audiod']['mediaserver']['fill'] = 'red'
G.add_edge('audiod','mediaserver')
G.edge['audiod']['mediaserver']['write-read'] = '[open open][write read][append read]'
G.add_edge('audiod','oneseg_mw')
G.edge['audiod']['oneseg_mw']['write-read'] = '[open open][write read]'
G.edge['audiod']['oneseg_mw']['fill'] = 'red'
G.add_edge('audiod','oneseg_mw')
G.edge['audiod']['oneseg_mw']['write-read'] = '[open open][write read][append read]'
G.add_edge('audiod','s_system_app')
G.edge['audiod']['s_system_app']['write-read'] = '[open open][write read]'
G.edge['audiod']['s_system_app']['fill'] = 'red'
G.add_edge('audiod','s_system_app')
G.edge['audiod']['s_system_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('audiod','usf')
G.edge['audiod']['usf']['write-read'] = '[open open][write read]'
G.edge['audiod']['usf']['fill'] = 'red'
G.add_edge('audiod','usf')
G.edge['audiod']['usf']['write-read'] = '[open open][write read][append read]'
G.add_edge('audiod','wfdservice')
G.edge['audiod']['wfdservice']['write-read'] = '[open open][write read]'
G.edge['audiod']['wfdservice']['fill'] = 'red'
G.add_edge('audiod','wfdservice')
G.edge['audiod']['wfdservice']['write-read'] = '[open open][write read][append read]'
G.add_edge('bootanim','audiod')
G.edge['bootanim']['audiod']['write-read'] = '[open open]'
G.add_edge('bootanim','bootanim')
G.edge['bootanim']['bootanim']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('bootanim','dtsconfigurator')
G.edge['bootanim']['dtsconfigurator']['write-read'] = '[open open]'
G.add_edge('bootanim','dtseagleservice')
G.edge['bootanim']['dtseagleservice']['write-read'] = '[open open]'
G.add_edge('bootanim','jackservice')
G.edge['bootanim']['jackservice']['write-read'] = '[open open]'
G.add_edge('bootanim','mediaserver')
G.edge['bootanim']['mediaserver']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('bootanim','oneseg_mw')
G.edge['bootanim']['oneseg_mw']['write-read'] = '[open open]'
G.add_edge('bootanim','s_system_app')
G.edge['bootanim']['s_system_app']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('bootanim','usf')
G.edge['bootanim']['usf']['write-read'] = '[open open]'
G.add_edge('bootanim','wfdservice')
G.edge['bootanim']['wfdservice']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('bootanim','audiod')
G.edge['bootanim']['audiod']['write-read'] = '[open open][write read]'
G.edge['bootanim']['audiod']['fill'] = 'red'
G.add_edge('bootanim','audiod')
G.edge['bootanim']['audiod']['write-read'] = '[open open][write read][append read]'
G.add_edge('bootanim','bootanim')
G.edge['bootanim']['bootanim']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read]'
G.edge['bootanim']['bootanim']['fill'] = 'red'
G.add_edge('bootanim','bootanim')
G.edge['bootanim']['bootanim']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][append read]'
G.add_edge('bootanim','dtsconfigurator')
G.edge['bootanim']['dtsconfigurator']['write-read'] = '[open open][write read]'
G.edge['bootanim']['dtsconfigurator']['fill'] = 'red'
G.add_edge('bootanim','dtsconfigurator')
G.edge['bootanim']['dtsconfigurator']['write-read'] = '[open open][write read][append read]'
G.add_edge('bootanim','dtseagleservice')
G.edge['bootanim']['dtseagleservice']['write-read'] = '[open open][write read]'
G.edge['bootanim']['dtseagleservice']['fill'] = 'red'
G.add_edge('bootanim','dtseagleservice')
G.edge['bootanim']['dtseagleservice']['write-read'] = '[open open][write read][append read]'
G.add_edge('bootanim','jackservice')
G.edge['bootanim']['jackservice']['write-read'] = '[open open][write read]'
G.edge['bootanim']['jackservice']['fill'] = 'red'
G.add_edge('bootanim','jackservice')
G.edge['bootanim']['jackservice']['write-read'] = '[open open][write read][append read]'
G.add_edge('bootanim','mediaserver')
G.edge['bootanim']['mediaserver']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['bootanim']['mediaserver']['fill'] = 'red'
G.add_edge('bootanim','mediaserver')
G.edge['bootanim']['mediaserver']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('bootanim','oneseg_mw')
G.edge['bootanim']['oneseg_mw']['write-read'] = '[open open][write read]'
G.edge['bootanim']['oneseg_mw']['fill'] = 'red'
G.add_edge('bootanim','oneseg_mw')
G.edge['bootanim']['oneseg_mw']['write-read'] = '[open open][write read][append read]'
G.add_edge('bootanim','s_system_app')
G.edge['bootanim']['s_system_app']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['bootanim']['s_system_app']['fill'] = 'red'
G.add_edge('bootanim','s_system_app')
G.edge['bootanim']['s_system_app']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('bootanim','usf')
G.edge['bootanim']['usf']['write-read'] = '[open open][write read]'
G.edge['bootanim']['usf']['fill'] = 'red'
G.add_edge('bootanim','usf')
G.edge['bootanim']['usf']['write-read'] = '[open open][write read][append read]'
G.add_edge('bootanim','wfdservice')
G.edge['bootanim']['wfdservice']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['bootanim']['wfdservice']['fill'] = 'red'
G.add_edge('bootanim','wfdservice')
G.edge['bootanim']['wfdservice']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('dtsconfigurator','audiod')
G.edge['dtsconfigurator']['audiod']['write-read'] = '[open open]'
G.add_edge('dtsconfigurator','bootanim')
G.edge['dtsconfigurator']['bootanim']['write-read'] = '[open open]'
G.add_edge('dtsconfigurator','dtsconfigurator')
G.edge['dtsconfigurator']['dtsconfigurator']['write-read'] = '[write read][open open]'
G.add_edge('dtsconfigurator','dtseagleservice')
G.edge['dtsconfigurator']['dtseagleservice']['write-read'] = '[open open]'
G.add_edge('dtsconfigurator','jackservice')
G.edge['dtsconfigurator']['jackservice']['write-read'] = '[open open]'
G.add_edge('dtsconfigurator','mediaserver')
G.edge['dtsconfigurator']['mediaserver']['write-read'] = '[open open]'
G.add_edge('dtsconfigurator','oneseg_mw')
G.edge['dtsconfigurator']['oneseg_mw']['write-read'] = '[open open]'
G.add_edge('dtsconfigurator','s_system_app')
G.edge['dtsconfigurator']['s_system_app']['write-read'] = '[open open]'
G.add_edge('dtsconfigurator','usf')
G.edge['dtsconfigurator']['usf']['write-read'] = '[open open]'
G.add_edge('dtsconfigurator','wfdservice')
G.edge['dtsconfigurator']['wfdservice']['write-read'] = '[open open]'
G.add_edge('dtsconfigurator','audiod')
G.edge['dtsconfigurator']['audiod']['write-read'] = '[open open][write read]'
G.edge['dtsconfigurator']['audiod']['fill'] = 'red'
G.add_edge('dtsconfigurator','audiod')
G.edge['dtsconfigurator']['audiod']['write-read'] = '[open open][write read][append read]'
G.add_edge('dtsconfigurator','bootanim')
G.edge['dtsconfigurator']['bootanim']['write-read'] = '[open open][write read]'
G.edge['dtsconfigurator']['bootanim']['fill'] = 'red'
G.add_edge('dtsconfigurator','bootanim')
G.edge['dtsconfigurator']['bootanim']['write-read'] = '[open open][write read][append read]'
G.add_edge('dtsconfigurator','dtsconfigurator')
G.edge['dtsconfigurator']['dtsconfigurator']['write-read'] = '[write read][open open][write read]'
G.edge['dtsconfigurator']['dtsconfigurator']['fill'] = 'red'
G.add_edge('dtsconfigurator','dtsconfigurator')
G.edge['dtsconfigurator']['dtsconfigurator']['write-read'] = '[write read][open open][write read][append read]'
G.add_edge('dtsconfigurator','dtseagleservice')
G.edge['dtsconfigurator']['dtseagleservice']['write-read'] = '[open open][write read]'
G.edge['dtsconfigurator']['dtseagleservice']['fill'] = 'red'
G.add_edge('dtsconfigurator','dtseagleservice')
G.edge['dtsconfigurator']['dtseagleservice']['write-read'] = '[open open][write read][append read]'
G.add_edge('dtsconfigurator','jackservice')
G.edge['dtsconfigurator']['jackservice']['write-read'] = '[open open][write read]'
G.edge['dtsconfigurator']['jackservice']['fill'] = 'red'
G.add_edge('dtsconfigurator','jackservice')
G.edge['dtsconfigurator']['jackservice']['write-read'] = '[open open][write read][append read]'
G.add_edge('dtsconfigurator','mediaserver')
G.edge['dtsconfigurator']['mediaserver']['write-read'] = '[open open][write read]'
G.edge['dtsconfigurator']['mediaserver']['fill'] = 'red'
G.add_edge('dtsconfigurator','mediaserver')
G.edge['dtsconfigurator']['mediaserver']['write-read'] = '[open open][write read][append read]'
G.add_edge('dtsconfigurator','oneseg_mw')
G.edge['dtsconfigurator']['oneseg_mw']['write-read'] = '[open open][write read]'
G.edge['dtsconfigurator']['oneseg_mw']['fill'] = 'red'
G.add_edge('dtsconfigurator','oneseg_mw')
G.edge['dtsconfigurator']['oneseg_mw']['write-read'] = '[open open][write read][append read]'
G.add_edge('dtsconfigurator','s_system_app')
G.edge['dtsconfigurator']['s_system_app']['write-read'] = '[open open][write read]'
G.edge['dtsconfigurator']['s_system_app']['fill'] = 'red'
G.add_edge('dtsconfigurator','s_system_app')
G.edge['dtsconfigurator']['s_system_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('dtsconfigurator','usf')
G.edge['dtsconfigurator']['usf']['write-read'] = '[open open][write read]'
G.edge['dtsconfigurator']['usf']['fill'] = 'red'
G.add_edge('dtsconfigurator','usf')
G.edge['dtsconfigurator']['usf']['write-read'] = '[open open][write read][append read]'
G.add_edge('dtsconfigurator','wfdservice')
G.edge['dtsconfigurator']['wfdservice']['write-read'] = '[open open][write read]'
G.edge['dtsconfigurator']['wfdservice']['fill'] = 'red'
G.add_edge('dtsconfigurator','wfdservice')
G.edge['dtsconfigurator']['wfdservice']['write-read'] = '[open open][write read][append read]'
G.add_edge('dtseagleservice','audiod')
G.edge['dtseagleservice']['audiod']['write-read'] = '[open open]'
G.add_edge('dtseagleservice','bootanim')
G.edge['dtseagleservice']['bootanim']['write-read'] = '[open open]'
G.add_edge('dtseagleservice','dtsconfigurator')
G.edge['dtseagleservice']['dtsconfigurator']['write-read'] = '[open open]'
G.add_edge('dtseagleservice','dtseagleservice')
G.edge['dtseagleservice']['dtseagleservice']['write-read'] = '[open open]'
G.add_edge('dtseagleservice','jackservice')
G.edge['dtseagleservice']['jackservice']['write-read'] = '[open open]'
G.add_edge('dtseagleservice','mediaserver')
G.edge['dtseagleservice']['mediaserver']['write-read'] = '[open open]'
G.add_edge('dtseagleservice','oneseg_mw')
G.edge['dtseagleservice']['oneseg_mw']['write-read'] = '[open open]'
G.add_edge('dtseagleservice','s_system_app')
G.edge['dtseagleservice']['s_system_app']['write-read'] = '[open open]'
G.add_edge('dtseagleservice','usf')
G.edge['dtseagleservice']['usf']['write-read'] = '[open open]'
G.add_edge('dtseagleservice','wfdservice')
G.edge['dtseagleservice']['wfdservice']['write-read'] = '[open open]'
G.add_edge('dtseagleservice','audiod')
G.edge['dtseagleservice']['audiod']['write-read'] = '[open open][write read]'
G.edge['dtseagleservice']['audiod']['fill'] = 'red'
G.add_edge('dtseagleservice','audiod')
G.edge['dtseagleservice']['audiod']['write-read'] = '[open open][write read][append read]'
G.add_edge('dtseagleservice','bootanim')
G.edge['dtseagleservice']['bootanim']['write-read'] = '[open open][write read]'
G.edge['dtseagleservice']['bootanim']['fill'] = 'red'
G.add_edge('dtseagleservice','bootanim')
G.edge['dtseagleservice']['bootanim']['write-read'] = '[open open][write read][append read]'
G.add_edge('dtseagleservice','dtsconfigurator')
G.edge['dtseagleservice']['dtsconfigurator']['write-read'] = '[open open][write read]'
G.edge['dtseagleservice']['dtsconfigurator']['fill'] = 'red'
G.add_edge('dtseagleservice','dtsconfigurator')
G.edge['dtseagleservice']['dtsconfigurator']['write-read'] = '[open open][write read][append read]'
G.add_edge('dtseagleservice','dtseagleservice')
G.edge['dtseagleservice']['dtseagleservice']['write-read'] = '[open open][write read]'
G.edge['dtseagleservice']['dtseagleservice']['fill'] = 'red'
G.add_edge('dtseagleservice','dtseagleservice')
G.edge['dtseagleservice']['dtseagleservice']['write-read'] = '[open open][write read][append read]'
G.add_edge('dtseagleservice','jackservice')
G.edge['dtseagleservice']['jackservice']['write-read'] = '[open open][write read]'
G.edge['dtseagleservice']['jackservice']['fill'] = 'red'
G.add_edge('dtseagleservice','jackservice')
G.edge['dtseagleservice']['jackservice']['write-read'] = '[open open][write read][append read]'
G.add_edge('dtseagleservice','mediaserver')
G.edge['dtseagleservice']['mediaserver']['write-read'] = '[open open][write read]'
G.edge['dtseagleservice']['mediaserver']['fill'] = 'red'
G.add_edge('dtseagleservice','mediaserver')
G.edge['dtseagleservice']['mediaserver']['write-read'] = '[open open][write read][append read]'
G.add_edge('dtseagleservice','oneseg_mw')
G.edge['dtseagleservice']['oneseg_mw']['write-read'] = '[open open][write read]'
G.edge['dtseagleservice']['oneseg_mw']['fill'] = 'red'
G.add_edge('dtseagleservice','oneseg_mw')
G.edge['dtseagleservice']['oneseg_mw']['write-read'] = '[open open][write read][append read]'
G.add_edge('dtseagleservice','s_system_app')
G.edge['dtseagleservice']['s_system_app']['write-read'] = '[open open][write read]'
G.edge['dtseagleservice']['s_system_app']['fill'] = 'red'
G.add_edge('dtseagleservice','s_system_app')
G.edge['dtseagleservice']['s_system_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('dtseagleservice','usf')
G.edge['dtseagleservice']['usf']['write-read'] = '[open open][write read]'
G.edge['dtseagleservice']['usf']['fill'] = 'red'
G.add_edge('dtseagleservice','usf')
G.edge['dtseagleservice']['usf']['write-read'] = '[open open][write read][append read]'
G.add_edge('dtseagleservice','wfdservice')
G.edge['dtseagleservice']['wfdservice']['write-read'] = '[open open][write read]'
G.edge['dtseagleservice']['wfdservice']['fill'] = 'red'
G.add_edge('dtseagleservice','wfdservice')
G.edge['dtseagleservice']['wfdservice']['write-read'] = '[open open][write read][append read]'
G.add_edge('jackservice','audiod')
G.edge['jackservice']['audiod']['write-read'] = '[open open]'
G.add_edge('jackservice','bootanim')
G.edge['jackservice']['bootanim']['write-read'] = '[open open]'
G.add_edge('jackservice','dtsconfigurator')
G.edge['jackservice']['dtsconfigurator']['write-read'] = '[open open]'
G.add_edge('jackservice','dtseagleservice')
G.edge['jackservice']['dtseagleservice']['write-read'] = '[open open]'
G.add_edge('jackservice','jackservice')
G.edge['jackservice']['jackservice']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open]'
G.add_edge('jackservice','mediaserver')
G.edge['jackservice']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('jackservice','oneseg_mw')
G.edge['jackservice']['oneseg_mw']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('jackservice','s_system_app')
G.edge['jackservice']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('jackservice','usf')
G.edge['jackservice']['usf']['write-read'] = '[open open]'
G.add_edge('jackservice','wfdservice')
G.edge['jackservice']['wfdservice']['write-read'] = '[open open]'
G.add_edge('jackservice','audiod')
G.edge['jackservice']['audiod']['write-read'] = '[open open][write read]'
G.edge['jackservice']['audiod']['fill'] = 'red'
G.add_edge('jackservice','audiod')
G.edge['jackservice']['audiod']['write-read'] = '[open open][write read][append read]'
G.add_edge('jackservice','bootanim')
G.edge['jackservice']['bootanim']['write-read'] = '[open open][write read]'
G.edge['jackservice']['bootanim']['fill'] = 'red'
G.add_edge('jackservice','bootanim')
G.edge['jackservice']['bootanim']['write-read'] = '[open open][write read][append read]'
G.add_edge('jackservice','dtsconfigurator')
G.edge['jackservice']['dtsconfigurator']['write-read'] = '[open open][write read]'
G.edge['jackservice']['dtsconfigurator']['fill'] = 'red'
G.add_edge('jackservice','dtsconfigurator')
G.edge['jackservice']['dtsconfigurator']['write-read'] = '[open open][write read][append read]'
G.add_edge('jackservice','dtseagleservice')
G.edge['jackservice']['dtseagleservice']['write-read'] = '[open open][write read]'
G.edge['jackservice']['dtseagleservice']['fill'] = 'red'
G.add_edge('jackservice','dtseagleservice')
G.edge['jackservice']['dtseagleservice']['write-read'] = '[open open][write read][append read]'
G.add_edge('jackservice','jackservice')
G.edge['jackservice']['jackservice']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read]'
G.edge['jackservice']['jackservice']['fill'] = 'red'
G.add_edge('jackservice','jackservice')
G.edge['jackservice']['jackservice']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read][append read]'
G.add_edge('jackservice','mediaserver')
G.edge['jackservice']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['jackservice']['mediaserver']['fill'] = 'red'
G.add_edge('jackservice','mediaserver')
G.edge['jackservice']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('jackservice','oneseg_mw')
G.edge['jackservice']['oneseg_mw']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['jackservice']['oneseg_mw']['fill'] = 'red'
G.add_edge('jackservice','oneseg_mw')
G.edge['jackservice']['oneseg_mw']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('jackservice','s_system_app')
G.edge['jackservice']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['jackservice']['s_system_app']['fill'] = 'red'
G.add_edge('jackservice','s_system_app')
G.edge['jackservice']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('jackservice','usf')
G.edge['jackservice']['usf']['write-read'] = '[open open][write read]'
G.edge['jackservice']['usf']['fill'] = 'red'
G.add_edge('jackservice','usf')
G.edge['jackservice']['usf']['write-read'] = '[open open][write read][append read]'
G.add_edge('jackservice','wfdservice')
G.edge['jackservice']['wfdservice']['write-read'] = '[open open][write read]'
G.edge['jackservice']['wfdservice']['fill'] = 'red'
G.add_edge('jackservice','wfdservice')
G.edge['jackservice']['wfdservice']['write-read'] = '[open open][write read][append read]'
G.add_edge('mediaserver','audiod')
G.edge['mediaserver']['audiod']['write-read'] = '[open open]'
G.add_edge('mediaserver','bootanim')
G.edge['mediaserver']['bootanim']['write-read'] = '[open open][write read][append read][write read][open open]'
G.add_edge('mediaserver','dtsconfigurator')
G.edge['mediaserver']['dtsconfigurator']['write-read'] = '[open open]'
G.add_edge('mediaserver','dtseagleservice')
G.edge['mediaserver']['dtseagleservice']['write-read'] = '[open open]'
G.add_edge('mediaserver','jackservice')
G.edge['mediaserver']['jackservice']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open]'
G.add_edge('mediaserver','mediaserver')
G.edge['mediaserver']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('mediaserver','oneseg_mw')
G.edge['mediaserver']['oneseg_mw']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('mediaserver','s_system_app')
G.edge['mediaserver']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][write read][append read][write read][open open][setattr getattr][write read][append read][setattr getattr][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('mediaserver','usf')
G.edge['mediaserver']['usf']['write-read'] = '[open open]'
G.add_edge('mediaserver','wfdservice')
G.edge['mediaserver']['wfdservice']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('mediaserver','audiod')
G.edge['mediaserver']['audiod']['write-read'] = '[open open][write read]'
G.edge['mediaserver']['audiod']['fill'] = 'red'
G.add_edge('mediaserver','audiod')
G.edge['mediaserver']['audiod']['write-read'] = '[open open][write read][append read]'
G.add_edge('mediaserver','bootanim')
G.edge['mediaserver']['bootanim']['write-read'] = '[open open][write read][append read][write read][open open][write read]'
G.edge['mediaserver']['bootanim']['fill'] = 'red'
G.add_edge('mediaserver','bootanim')
G.edge['mediaserver']['bootanim']['write-read'] = '[open open][write read][append read][write read][open open][write read][append read]'
G.add_edge('mediaserver','dtsconfigurator')
G.edge['mediaserver']['dtsconfigurator']['write-read'] = '[open open][write read]'
G.edge['mediaserver']['dtsconfigurator']['fill'] = 'red'
G.add_edge('mediaserver','dtsconfigurator')
G.edge['mediaserver']['dtsconfigurator']['write-read'] = '[open open][write read][append read]'
G.add_edge('mediaserver','dtseagleservice')
G.edge['mediaserver']['dtseagleservice']['write-read'] = '[open open][write read]'
G.edge['mediaserver']['dtseagleservice']['fill'] = 'red'
G.add_edge('mediaserver','dtseagleservice')
G.edge['mediaserver']['dtseagleservice']['write-read'] = '[open open][write read][append read]'
G.add_edge('mediaserver','jackservice')
G.edge['mediaserver']['jackservice']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read]'
G.edge['mediaserver']['jackservice']['fill'] = 'red'
G.add_edge('mediaserver','jackservice')
G.edge['mediaserver']['jackservice']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read][append read]'
G.add_edge('mediaserver','mediaserver')
G.edge['mediaserver']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['mediaserver']['mediaserver']['fill'] = 'red'
G.add_edge('mediaserver','mediaserver')
G.edge['mediaserver']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('mediaserver','oneseg_mw')
G.edge['mediaserver']['oneseg_mw']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['mediaserver']['oneseg_mw']['fill'] = 'red'
G.add_edge('mediaserver','oneseg_mw')
G.edge['mediaserver']['oneseg_mw']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('mediaserver','s_system_app')
G.edge['mediaserver']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][write read][append read][write read][open open][setattr getattr][write read][append read][setattr getattr][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['mediaserver']['s_system_app']['fill'] = 'red'
G.add_edge('mediaserver','s_system_app')
G.edge['mediaserver']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][write read][append read][write read][open open][setattr getattr][write read][append read][setattr getattr][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('mediaserver','usf')
G.edge['mediaserver']['usf']['write-read'] = '[open open][write read]'
G.edge['mediaserver']['usf']['fill'] = 'red'
G.add_edge('mediaserver','usf')
G.edge['mediaserver']['usf']['write-read'] = '[open open][write read][append read]'
G.add_edge('mediaserver','wfdservice')
G.edge['mediaserver']['wfdservice']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['mediaserver']['wfdservice']['fill'] = 'red'
G.add_edge('mediaserver','wfdservice')
G.edge['mediaserver']['wfdservice']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('oneseg_mw','audiod')
G.edge['oneseg_mw']['audiod']['write-read'] = '[open open]'
G.add_edge('oneseg_mw','bootanim')
G.edge['oneseg_mw']['bootanim']['write-read'] = '[open open]'
G.add_edge('oneseg_mw','dtsconfigurator')
G.edge['oneseg_mw']['dtsconfigurator']['write-read'] = '[open open]'
G.add_edge('oneseg_mw','dtseagleservice')
G.edge['oneseg_mw']['dtseagleservice']['write-read'] = '[open open]'
G.add_edge('oneseg_mw','jackservice')
G.edge['oneseg_mw']['jackservice']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('oneseg_mw','mediaserver')
G.edge['oneseg_mw']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][append read][write read][append read][open open]'
G.add_edge('oneseg_mw','oneseg_mw')
G.edge['oneseg_mw']['oneseg_mw']['write-read'] = '[open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('oneseg_mw','s_system_app')
G.edge['oneseg_mw']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][setattr getattr][open open]'
G.add_edge('oneseg_mw','usf')
G.edge['oneseg_mw']['usf']['write-read'] = '[open open]'
G.add_edge('oneseg_mw','wfdservice')
G.edge['oneseg_mw']['wfdservice']['write-read'] = '[open open]'
G.add_edge('oneseg_mw','audiod')
G.edge['oneseg_mw']['audiod']['write-read'] = '[open open][write read]'
G.edge['oneseg_mw']['audiod']['fill'] = 'red'
G.add_edge('oneseg_mw','audiod')
G.edge['oneseg_mw']['audiod']['write-read'] = '[open open][write read][append read]'
G.add_edge('oneseg_mw','bootanim')
G.edge['oneseg_mw']['bootanim']['write-read'] = '[open open][write read]'
G.edge['oneseg_mw']['bootanim']['fill'] = 'red'
G.add_edge('oneseg_mw','bootanim')
G.edge['oneseg_mw']['bootanim']['write-read'] = '[open open][write read][append read]'
G.add_edge('oneseg_mw','dtsconfigurator')
G.edge['oneseg_mw']['dtsconfigurator']['write-read'] = '[open open][write read]'
G.edge['oneseg_mw']['dtsconfigurator']['fill'] = 'red'
G.add_edge('oneseg_mw','dtsconfigurator')
G.edge['oneseg_mw']['dtsconfigurator']['write-read'] = '[open open][write read][append read]'
G.add_edge('oneseg_mw','dtseagleservice')
G.edge['oneseg_mw']['dtseagleservice']['write-read'] = '[open open][write read]'
G.edge['oneseg_mw']['dtseagleservice']['fill'] = 'red'
G.add_edge('oneseg_mw','dtseagleservice')
G.edge['oneseg_mw']['dtseagleservice']['write-read'] = '[open open][write read][append read]'
G.add_edge('oneseg_mw','jackservice')
G.edge['oneseg_mw']['jackservice']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['oneseg_mw']['jackservice']['fill'] = 'red'
G.add_edge('oneseg_mw','jackservice')
G.edge['oneseg_mw']['jackservice']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('oneseg_mw','mediaserver')
G.edge['oneseg_mw']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][append read][write read][append read][open open][write read]'
G.edge['oneseg_mw']['mediaserver']['fill'] = 'red'
G.add_edge('oneseg_mw','mediaserver')
G.edge['oneseg_mw']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][append read][write read][append read][open open][write read][append read]'
G.add_edge('oneseg_mw','oneseg_mw')
G.edge['oneseg_mw']['oneseg_mw']['write-read'] = '[open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['oneseg_mw']['oneseg_mw']['fill'] = 'red'
G.add_edge('oneseg_mw','oneseg_mw')
G.edge['oneseg_mw']['oneseg_mw']['write-read'] = '[open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('oneseg_mw','s_system_app')
G.edge['oneseg_mw']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][setattr getattr][open open][write read]'
G.edge['oneseg_mw']['s_system_app']['fill'] = 'red'
G.add_edge('oneseg_mw','s_system_app')
G.edge['oneseg_mw']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][setattr getattr][open open][write read][append read]'
G.add_edge('oneseg_mw','usf')
G.edge['oneseg_mw']['usf']['write-read'] = '[open open][write read]'
G.edge['oneseg_mw']['usf']['fill'] = 'red'
G.add_edge('oneseg_mw','usf')
G.edge['oneseg_mw']['usf']['write-read'] = '[open open][write read][append read]'
G.add_edge('oneseg_mw','wfdservice')
G.edge['oneseg_mw']['wfdservice']['write-read'] = '[open open][write read]'
G.edge['oneseg_mw']['wfdservice']['fill'] = 'red'
G.add_edge('oneseg_mw','wfdservice')
G.edge['oneseg_mw']['wfdservice']['write-read'] = '[open open][write read][append read]'
G.add_edge('s_system_app','audiod')
G.edge['s_system_app']['audiod']['write-read'] = '[open open]'
G.add_edge('s_system_app','bootanim')
G.edge['s_system_app']['bootanim']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('s_system_app','dtsconfigurator')
G.edge['s_system_app']['dtsconfigurator']['write-read'] = '[open open]'
G.add_edge('s_system_app','dtseagleservice')
G.edge['s_system_app']['dtseagleservice']['write-read'] = '[open open]'
G.add_edge('s_system_app','jackservice')
G.edge['s_system_app']['jackservice']['write-read'] = '[add_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('s_system_app','mediaserver')
G.edge['s_system_app']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('s_system_app','oneseg_mw')
G.edge['s_system_app']['oneseg_mw']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('s_system_app','s_system_app')
G.edge['s_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][write read][append read][open open][write read][append read][open open][append read][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][setattr getattr][write read][append read][setattr getattr][setattr getattr][open open][setattr getattr][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('s_system_app','usf')
G.edge['s_system_app']['usf']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('s_system_app','wfdservice')
G.edge['s_system_app']['wfdservice']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open]'
G.add_edge('s_system_app','audiod')
G.edge['s_system_app']['audiod']['write-read'] = '[open open][write read]'
G.edge['s_system_app']['audiod']['fill'] = 'red'
G.add_edge('s_system_app','audiod')
G.edge['s_system_app']['audiod']['write-read'] = '[open open][write read][append read]'
G.add_edge('s_system_app','bootanim')
G.edge['s_system_app']['bootanim']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['s_system_app']['bootanim']['fill'] = 'red'
G.add_edge('s_system_app','bootanim')
G.edge['s_system_app']['bootanim']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('s_system_app','dtsconfigurator')
G.edge['s_system_app']['dtsconfigurator']['write-read'] = '[open open][write read]'
G.edge['s_system_app']['dtsconfigurator']['fill'] = 'red'
G.add_edge('s_system_app','dtsconfigurator')
G.edge['s_system_app']['dtsconfigurator']['write-read'] = '[open open][write read][append read]'
G.add_edge('s_system_app','dtseagleservice')
G.edge['s_system_app']['dtseagleservice']['write-read'] = '[open open][write read]'
G.edge['s_system_app']['dtseagleservice']['fill'] = 'red'
G.add_edge('s_system_app','dtseagleservice')
G.edge['s_system_app']['dtseagleservice']['write-read'] = '[open open][write read][append read]'
G.add_edge('s_system_app','jackservice')
G.edge['s_system_app']['jackservice']['write-read'] = '[add_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['s_system_app']['jackservice']['fill'] = 'red'
G.add_edge('s_system_app','jackservice')
G.edge['s_system_app']['jackservice']['write-read'] = '[add_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('s_system_app','mediaserver')
G.edge['s_system_app']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['s_system_app']['mediaserver']['fill'] = 'red'
G.add_edge('s_system_app','mediaserver')
G.edge['s_system_app']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('s_system_app','oneseg_mw')
G.edge['s_system_app']['oneseg_mw']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['s_system_app']['oneseg_mw']['fill'] = 'red'
G.add_edge('s_system_app','oneseg_mw')
G.edge['s_system_app']['oneseg_mw']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('s_system_app','s_system_app')
G.edge['s_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][write read][append read][open open][write read][append read][open open][append read][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][setattr getattr][write read][append read][setattr getattr][setattr getattr][open open][setattr getattr][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['s_system_app']['s_system_app']['fill'] = 'red'
G.add_edge('s_system_app','s_system_app')
G.edge['s_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][write read][append read][open open][write read][append read][open open][append read][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][setattr getattr][write read][append read][setattr getattr][setattr getattr][open open][setattr getattr][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('s_system_app','usf')
G.edge['s_system_app']['usf']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['s_system_app']['usf']['fill'] = 'red'
G.add_edge('s_system_app','usf')
G.edge['s_system_app']['usf']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('s_system_app','wfdservice')
G.edge['s_system_app']['wfdservice']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read]'
G.edge['s_system_app']['wfdservice']['fill'] = 'red'
G.add_edge('s_system_app','wfdservice')
G.edge['s_system_app']['wfdservice']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read]'
G.add_edge('system_server','audiod')
G.edge['system_server']['audiod']['write-read'] = '[open open]'
G.add_edge('system_server','bootanim')
G.edge['system_server']['bootanim']['write-read'] = '[open open][write read][append read][write read][write read][open open]'
G.add_edge('system_server','dtsconfigurator')
G.edge['system_server']['dtsconfigurator']['write-read'] = '[open open]'
G.add_edge('system_server','dtseagleservice')
G.edge['system_server']['dtseagleservice']['write-read'] = '[open open]'
G.add_edge('system_server','jackservice')
G.edge['system_server']['jackservice']['write-read'] = '[add_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][write read][open open]'
G.add_edge('system_server','mediaserver')
G.edge['system_server']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('system_server','oneseg_mw')
G.edge['system_server']['oneseg_mw']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('system_server','s_system_app')
G.edge['system_server']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][add_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read][append read][write read][open open][setattr getattr][write read][append read][setattr getattr][setattr getattr][open open][setattr getattr][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('system_server','usf')
G.edge['system_server']['usf']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('system_server','wfdservice')
G.edge['system_server']['wfdservice']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open]'
G.add_edge('system_server','audiod')
G.edge['system_server']['audiod']['write-read'] = '[open open][write read]'
G.edge['system_server']['audiod']['fill'] = 'red'
G.add_edge('system_server','audiod')
G.edge['system_server']['audiod']['write-read'] = '[open open][write read][append read]'
G.add_edge('system_server','bootanim')
G.edge['system_server']['bootanim']['write-read'] = '[open open][write read][append read][write read][write read][open open][write read]'
G.edge['system_server']['bootanim']['fill'] = 'red'
G.add_edge('system_server','bootanim')
G.edge['system_server']['bootanim']['write-read'] = '[open open][write read][append read][write read][write read][open open][write read][append read]'
G.add_edge('system_server','dtsconfigurator')
G.edge['system_server']['dtsconfigurator']['write-read'] = '[open open][write read]'
G.edge['system_server']['dtsconfigurator']['fill'] = 'red'
G.add_edge('system_server','dtsconfigurator')
G.edge['system_server']['dtsconfigurator']['write-read'] = '[open open][write read][append read]'
G.add_edge('system_server','dtseagleservice')
G.edge['system_server']['dtseagleservice']['write-read'] = '[open open][write read]'
G.edge['system_server']['dtseagleservice']['fill'] = 'red'
G.add_edge('system_server','dtseagleservice')
G.edge['system_server']['dtseagleservice']['write-read'] = '[open open][write read][append read]'
G.add_edge('system_server','jackservice')
G.edge['system_server']['jackservice']['write-read'] = '[add_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][write read][open open][write read]'
G.edge['system_server']['jackservice']['fill'] = 'red'
G.add_edge('system_server','jackservice')
G.edge['system_server']['jackservice']['write-read'] = '[add_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][write read][open open][write read][append read]'
G.add_edge('system_server','mediaserver')
G.edge['system_server']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['system_server']['mediaserver']['fill'] = 'red'
G.add_edge('system_server','mediaserver')
G.edge['system_server']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('system_server','oneseg_mw')
G.edge['system_server']['oneseg_mw']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['system_server']['oneseg_mw']['fill'] = 'red'
G.add_edge('system_server','oneseg_mw')
G.edge['system_server']['oneseg_mw']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('system_server','s_system_app')
G.edge['system_server']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][add_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read][append read][write read][open open][setattr getattr][write read][append read][setattr getattr][setattr getattr][open open][setattr getattr][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['system_server']['s_system_app']['fill'] = 'red'
G.add_edge('system_server','s_system_app')
G.edge['system_server']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][add_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read][append read][write read][open open][setattr getattr][write read][append read][setattr getattr][setattr getattr][open open][setattr getattr][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('system_server','usf')
G.edge['system_server']['usf']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['system_server']['usf']['fill'] = 'red'
G.add_edge('system_server','usf')
G.edge['system_server']['usf']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('system_server','wfdservice')
G.edge['system_server']['wfdservice']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read]'
G.edge['system_server']['wfdservice']['fill'] = 'red'
G.add_edge('system_server','wfdservice')
G.edge['system_server']['wfdservice']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read]'
G.add_edge('usf','audiod')
G.edge['usf']['audiod']['write-read'] = '[open open]'
G.add_edge('usf','bootanim')
G.edge['usf']['bootanim']['write-read'] = '[open open]'
G.add_edge('usf','dtsconfigurator')
G.edge['usf']['dtsconfigurator']['write-read'] = '[open open]'
G.add_edge('usf','dtseagleservice')
G.edge['usf']['dtseagleservice']['write-read'] = '[open open]'
G.add_edge('usf','jackservice')
G.edge['usf']['jackservice']['write-read'] = '[open open]'
G.add_edge('usf','mediaserver')
G.edge['usf']['mediaserver']['write-read'] = '[open open]'
G.add_edge('usf','oneseg_mw')
G.edge['usf']['oneseg_mw']['write-read'] = '[open open]'
G.add_edge('usf','s_system_app')
G.edge['usf']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('usf','usf')
G.edge['usf']['usf']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('usf','wfdservice')
G.edge['usf']['wfdservice']['write-read'] = '[open open]'
G.add_edge('usf','audiod')
G.edge['usf']['audiod']['write-read'] = '[open open][write read]'
G.edge['usf']['audiod']['fill'] = 'red'
G.add_edge('usf','audiod')
G.edge['usf']['audiod']['write-read'] = '[open open][write read][append read]'
G.add_edge('usf','bootanim')
G.edge['usf']['bootanim']['write-read'] = '[open open][write read]'
G.edge['usf']['bootanim']['fill'] = 'red'
G.add_edge('usf','bootanim')
G.edge['usf']['bootanim']['write-read'] = '[open open][write read][append read]'
G.add_edge('usf','dtsconfigurator')
G.edge['usf']['dtsconfigurator']['write-read'] = '[open open][write read]'
G.edge['usf']['dtsconfigurator']['fill'] = 'red'
G.add_edge('usf','dtsconfigurator')
G.edge['usf']['dtsconfigurator']['write-read'] = '[open open][write read][append read]'
G.add_edge('usf','dtseagleservice')
G.edge['usf']['dtseagleservice']['write-read'] = '[open open][write read]'
G.edge['usf']['dtseagleservice']['fill'] = 'red'
G.add_edge('usf','dtseagleservice')
G.edge['usf']['dtseagleservice']['write-read'] = '[open open][write read][append read]'
G.add_edge('usf','jackservice')
G.edge['usf']['jackservice']['write-read'] = '[open open][write read]'
G.edge['usf']['jackservice']['fill'] = 'red'
G.add_edge('usf','jackservice')
G.edge['usf']['jackservice']['write-read'] = '[open open][write read][append read]'
G.add_edge('usf','mediaserver')
G.edge['usf']['mediaserver']['write-read'] = '[open open][write read]'
G.edge['usf']['mediaserver']['fill'] = 'red'
G.add_edge('usf','mediaserver')
G.edge['usf']['mediaserver']['write-read'] = '[open open][write read][append read]'
G.add_edge('usf','oneseg_mw')
G.edge['usf']['oneseg_mw']['write-read'] = '[open open][write read]'
G.edge['usf']['oneseg_mw']['fill'] = 'red'
G.add_edge('usf','oneseg_mw')
G.edge['usf']['oneseg_mw']['write-read'] = '[open open][write read][append read]'
G.add_edge('usf','s_system_app')
G.edge['usf']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['usf']['s_system_app']['fill'] = 'red'
G.add_edge('usf','s_system_app')
G.edge['usf']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('usf','usf')
G.edge['usf']['usf']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read]'
G.edge['usf']['usf']['fill'] = 'red'
G.add_edge('usf','usf')
G.edge['usf']['usf']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read]'
G.add_edge('usf','wfdservice')
G.edge['usf']['wfdservice']['write-read'] = '[open open][write read]'
G.edge['usf']['wfdservice']['fill'] = 'red'
G.add_edge('usf','wfdservice')
G.edge['usf']['wfdservice']['write-read'] = '[open open][write read][append read]'
G.add_edge('wfdservice','audiod')
G.edge['wfdservice']['audiod']['write-read'] = '[open open]'
G.add_edge('wfdservice','bootanim')
G.edge['wfdservice']['bootanim']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('wfdservice','dtsconfigurator')
G.edge['wfdservice']['dtsconfigurator']['write-read'] = '[open open]'
G.add_edge('wfdservice','dtseagleservice')
G.edge['wfdservice']['dtseagleservice']['write-read'] = '[open open]'
G.add_edge('wfdservice','jackservice')
G.edge['wfdservice']['jackservice']['write-read'] = '[open open]'
G.add_edge('wfdservice','mediaserver')
G.edge['wfdservice']['mediaserver']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('wfdservice','oneseg_mw')
G.edge['wfdservice']['oneseg_mw']['write-read'] = '[open open]'
G.add_edge('wfdservice','s_system_app')
G.edge['wfdservice']['s_system_app']['write-read'] = '[setattr getattr][setopt getopt][open open][write read][append read][open open]'
G.add_edge('wfdservice','usf')
G.edge['wfdservice']['usf']['write-read'] = '[open open]'
G.add_edge('wfdservice','wfdservice')
G.edge['wfdservice']['wfdservice']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('wfdservice','audiod')
G.edge['wfdservice']['audiod']['write-read'] = '[open open][write read]'
G.edge['wfdservice']['audiod']['fill'] = 'red'
G.add_edge('wfdservice','audiod')
G.edge['wfdservice']['audiod']['write-read'] = '[open open][write read][append read]'
G.add_edge('wfdservice','bootanim')
G.edge['wfdservice']['bootanim']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['wfdservice']['bootanim']['fill'] = 'red'
G.add_edge('wfdservice','bootanim')
G.edge['wfdservice']['bootanim']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('wfdservice','dtsconfigurator')
G.edge['wfdservice']['dtsconfigurator']['write-read'] = '[open open][write read]'
G.edge['wfdservice']['dtsconfigurator']['fill'] = 'red'
G.add_edge('wfdservice','dtsconfigurator')
G.edge['wfdservice']['dtsconfigurator']['write-read'] = '[open open][write read][append read]'
G.add_edge('wfdservice','dtseagleservice')
G.edge['wfdservice']['dtseagleservice']['write-read'] = '[open open][write read]'
G.edge['wfdservice']['dtseagleservice']['fill'] = 'red'
G.add_edge('wfdservice','dtseagleservice')
G.edge['wfdservice']['dtseagleservice']['write-read'] = '[open open][write read][append read]'
G.add_edge('wfdservice','jackservice')
G.edge['wfdservice']['jackservice']['write-read'] = '[open open][write read]'
G.edge['wfdservice']['jackservice']['fill'] = 'red'
G.add_edge('wfdservice','jackservice')
G.edge['wfdservice']['jackservice']['write-read'] = '[open open][write read][append read]'
G.add_edge('wfdservice','mediaserver')
G.edge['wfdservice']['mediaserver']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['wfdservice']['mediaserver']['fill'] = 'red'
G.add_edge('wfdservice','mediaserver')
G.edge['wfdservice']['mediaserver']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('wfdservice','oneseg_mw')
G.edge['wfdservice']['oneseg_mw']['write-read'] = '[open open][write read]'
G.edge['wfdservice']['oneseg_mw']['fill'] = 'red'
G.add_edge('wfdservice','oneseg_mw')
G.edge['wfdservice']['oneseg_mw']['write-read'] = '[open open][write read][append read]'
G.add_edge('wfdservice','s_system_app')
G.edge['wfdservice']['s_system_app']['write-read'] = '[setattr getattr][setopt getopt][open open][write read][append read][open open][write read]'
G.edge['wfdservice']['s_system_app']['fill'] = 'red'
G.add_edge('wfdservice','s_system_app')
G.edge['wfdservice']['s_system_app']['write-read'] = '[setattr getattr][setopt getopt][open open][write read][append read][open open][write read][append read]'
G.add_edge('wfdservice','usf')
G.edge['wfdservice']['usf']['write-read'] = '[open open][write read]'
G.edge['wfdservice']['usf']['fill'] = 'red'
G.add_edge('wfdservice','usf')
G.edge['wfdservice']['usf']['write-read'] = '[open open][write read][append read]'
G.add_edge('wfdservice','wfdservice')
G.edge['wfdservice']['wfdservice']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read]'
G.edge['wfdservice']['wfdservice']['fill'] = 'red'
G.add_edge('wfdservice','wfdservice')
G.edge['wfdservice']['wfdservice']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read]'
app = Viewer(G)
app.mainloop()