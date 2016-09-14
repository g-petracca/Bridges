import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('appdomain','appdomain')
G.edge['appdomain']['appdomain']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][write read][setattr getattr][write read][append read][setopt getopt][write read][open open][write read][append read][write read][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('appdomain','untrusteddomain')
G.edge['appdomain']['untrusteddomain']['write-read'] = '[write read][append read][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][setattr getattr]'
G.add_edge('appdomain','appdomain')
G.edge['appdomain']['appdomain']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][write read][setattr getattr][write read][append read][setopt getopt][write read][open open][write read][append read][write read][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read]'
G.edge['appdomain']['appdomain']['fill'] = 'red'
G.add_edge('appdomain','appdomain')
G.edge['appdomain']['appdomain']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][write read][setattr getattr][write read][append read][setopt getopt][write read][open open][write read][append read][write read][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read]'
G.add_edge('appdomain','bluetoothdomain')
G.edge['appdomain']['bluetoothdomain']['write-read'] = '[write read]'
G.edge['appdomain']['bluetoothdomain']['fill'] = 'red'
G.add_edge('appdomain','commonplatformappdomain')
G.edge['appdomain']['commonplatformappdomain']['write-read'] = '[open open][write read][append read][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][write read]'
G.edge['appdomain']['commonplatformappdomain']['fill'] = 'red'
G.add_edge('appdomain','samsung_app')
G.edge['appdomain']['samsung_app']['write-read'] = '[write read][append read][open open][write read][append read][write read]'
G.edge['appdomain']['samsung_app']['fill'] = 'red'
G.add_edge('appdomain','system_server')
G.edge['appdomain']['system_server']['write-read'] = '[open open][write read][append read][setattr getattr][add_name search][remove_name search][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open execmod][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][setattr getattr][write read][append read][open open][write read][append read][write read][append read][open open][setattr getattr][write read][append read][write read]'
G.edge['appdomain']['system_server']['fill'] = 'red'
G.add_edge('appdomain','untrusteddomain')
G.edge['appdomain']['untrusteddomain']['write-read'] = '[write read][append read][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read]'
G.edge['appdomain']['untrusteddomain']['fill'] = 'red'
G.add_edge('appdomain','untrusteddomain')
G.edge['appdomain']['untrusteddomain']['write-read'] = '[write read][append read][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][append read]'
G.add_edge('appdomain','appdomain')
G.edge['appdomain']['appdomain']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][write read][setattr getattr][write read][append read][setopt getopt][write read][open open][write read][append read][write read][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt]'
G.add_edge('appdomain','bluetoothdomain')
G.edge['appdomain']['bluetoothdomain']['write-read'] = '[write read][setopt getopt]'
G.add_edge('appdomain','untrusteddomain')
G.edge['appdomain']['untrusteddomain']['write-read'] = '[write read][append read][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][append read][setopt getopt]'
G.add_edge('bluetoothdomain','appdomain')
G.edge['bluetoothdomain']['appdomain']['write-read'] = '[setattr getattr]'
G.add_edge('bluetoothdomain','untrusteddomain')
G.edge['bluetoothdomain']['untrusteddomain']['write-read'] = '[setattr getattr]'
G.add_edge('bluetoothdomain','appdomain')
G.edge['bluetoothdomain']['appdomain']['write-read'] = '[setattr getattr][write read]'
G.edge['bluetoothdomain']['appdomain']['fill'] = 'red'
G.add_edge('bluetoothdomain','appdomain')
G.edge['bluetoothdomain']['appdomain']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('bluetoothdomain','bluetoothdomain')
G.edge['bluetoothdomain']['bluetoothdomain']['write-read'] = '[write read]'
G.edge['bluetoothdomain']['bluetoothdomain']['fill'] = 'red'
G.add_edge('bluetoothdomain','commonplatformappdomain')
G.edge['bluetoothdomain']['commonplatformappdomain']['write-read'] = '[write read]'
G.edge['bluetoothdomain']['commonplatformappdomain']['fill'] = 'red'
G.add_edge('bluetoothdomain','samsung_app')
G.edge['bluetoothdomain']['samsung_app']['write-read'] = '[write read]'
G.edge['bluetoothdomain']['samsung_app']['fill'] = 'red'
G.add_edge('bluetoothdomain','system_server')
G.edge['bluetoothdomain']['system_server']['write-read'] = '[write read]'
G.edge['bluetoothdomain']['system_server']['fill'] = 'red'
G.add_edge('bluetoothdomain','untrusteddomain')
G.edge['bluetoothdomain']['untrusteddomain']['write-read'] = '[setattr getattr][write read]'
G.edge['bluetoothdomain']['untrusteddomain']['fill'] = 'red'
G.add_edge('bluetoothdomain','untrusteddomain')
G.edge['bluetoothdomain']['untrusteddomain']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('bluetoothdomain','appdomain')
G.edge['bluetoothdomain']['appdomain']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('bluetoothdomain','bluetoothdomain')
G.edge['bluetoothdomain']['bluetoothdomain']['write-read'] = '[write read][setopt getopt]'
G.add_edge('bluetoothdomain','untrusteddomain')
G.edge['bluetoothdomain']['untrusteddomain']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
G.add_edge('commonplatformappdomain','appdomain')
G.edge['commonplatformappdomain']['appdomain']['write-read'] = '[open open][write read][append read][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][setattr getattr]'
G.add_edge('commonplatformappdomain','untrusteddomain')
G.edge['commonplatformappdomain']['untrusteddomain']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][setopt getopt][write read][setattr getattr]'
G.add_edge('commonplatformappdomain','appdomain')
G.edge['commonplatformappdomain']['appdomain']['write-read'] = '[open open][write read][append read][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read]'
G.edge['commonplatformappdomain']['appdomain']['fill'] = 'red'
G.add_edge('commonplatformappdomain','appdomain')
G.edge['commonplatformappdomain']['appdomain']['write-read'] = '[open open][write read][append read][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][append read]'
G.add_edge('commonplatformappdomain','bluetoothdomain')
G.edge['commonplatformappdomain']['bluetoothdomain']['write-read'] = '[write read]'
G.edge['commonplatformappdomain']['bluetoothdomain']['fill'] = 'red'
G.add_edge('commonplatformappdomain','commonplatformappdomain')
G.edge['commonplatformappdomain']['commonplatformappdomain']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read][append read][setattr getattr][write read][append read][setopt getopt][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][open open][write read][append read][open open][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][write read][write read]'
G.edge['commonplatformappdomain']['commonplatformappdomain']['fill'] = 'red'
G.add_edge('commonplatformappdomain','samsung_app')
G.edge['commonplatformappdomain']['samsung_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][write read]'
G.edge['commonplatformappdomain']['samsung_app']['fill'] = 'red'
G.add_edge('commonplatformappdomain','system_server')
G.edge['commonplatformappdomain']['system_server']['write-read'] = '[write read][append read][open open][write read][add_name search][remove_name search][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][setopt getopt][open open][write read][append read][write read]'
G.edge['commonplatformappdomain']['system_server']['fill'] = 'red'
G.add_edge('commonplatformappdomain','untrusteddomain')
G.edge['commonplatformappdomain']['untrusteddomain']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][setopt getopt][write read][setattr getattr][write read]'
G.edge['commonplatformappdomain']['untrusteddomain']['fill'] = 'red'
G.add_edge('commonplatformappdomain','untrusteddomain')
G.edge['commonplatformappdomain']['untrusteddomain']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][setopt getopt][write read][setattr getattr][write read][append read]'
G.add_edge('samsung_app','appdomain')
G.edge['samsung_app']['appdomain']['write-read'] = '[write read][write read]'
G.edge['samsung_app']['appdomain']['fill'] = 'red'
G.add_edge('samsung_app','appdomain')
G.edge['samsung_app']['appdomain']['write-read'] = '[write read][write read][append read]'
G.add_edge('samsung_app','bluetoothdomain')
G.edge['samsung_app']['bluetoothdomain']['write-read'] = '[write read]'
G.edge['samsung_app']['bluetoothdomain']['fill'] = 'red'
G.add_edge('samsung_app','commonplatformappdomain')
G.edge['samsung_app']['commonplatformappdomain']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][write read]'
G.edge['samsung_app']['commonplatformappdomain']['fill'] = 'red'
G.add_edge('samsung_app','samsung_app')
G.edge['samsung_app']['samsung_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][write read]'
G.edge['samsung_app']['samsung_app']['fill'] = 'red'
G.add_edge('samsung_app','system_server')
G.edge['samsung_app']['system_server']['write-read'] = '[write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read]'
G.edge['samsung_app']['system_server']['fill'] = 'red'
G.add_edge('samsung_app','untrusteddomain')
G.edge['samsung_app']['untrusteddomain']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][write read]'
G.edge['samsung_app']['untrusteddomain']['fill'] = 'red'
G.add_edge('samsung_app','untrusteddomain')
G.edge['samsung_app']['untrusteddomain']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][write read][append read]'
G.add_edge('system_server','appdomain')
G.edge['system_server']['appdomain']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][setopt getopt][write read][append read][write read][open open][write read][append read][write read][setattr getattr]'
G.add_edge('system_server','untrusteddomain')
G.edge['system_server']['untrusteddomain']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setopt getopt][write read][append read][setattr getattr]'
G.add_edge('system_server','appdomain')
G.edge['system_server']['appdomain']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][setopt getopt][write read][append read][write read][open open][write read][append read][write read][setattr getattr][write read]'
G.edge['system_server']['appdomain']['fill'] = 'red'
G.add_edge('system_server','appdomain')
G.edge['system_server']['appdomain']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][setopt getopt][write read][append read][write read][open open][write read][append read][write read][setattr getattr][write read][append read]'
G.add_edge('system_server','bluetoothdomain')
G.edge['system_server']['bluetoothdomain']['write-read'] = '[write read]'
G.edge['system_server']['bluetoothdomain']['fill'] = 'red'
G.add_edge('system_server','commonplatformappdomain')
G.edge['system_server']['commonplatformappdomain']['write-read'] = '[setopt getopt][setattr getattr][write read][append read][setopt getopt][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setopt getopt][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read]'
G.edge['system_server']['commonplatformappdomain']['fill'] = 'red'
G.add_edge('system_server','samsung_app')
G.edge['system_server']['samsung_app']['write-read'] = '[setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read]'
G.edge['system_server']['samsung_app']['fill'] = 'red'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][setsched getsched][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setopt getopt][write read][setattr getattr][setattr getattr][write read][append read][write read][append read][setopt getopt][setopt getopt][setattr getattr][setattr getattr][write read][append read][write read][append read][setopt getopt][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][append read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][setsched getsched][open open][setattr getattr][write read][append read][open open][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][write read]'
G.edge['system_server']['system_server']['fill'] = 'red'
G.add_edge('system_server','untrusteddomain')
G.edge['system_server']['untrusteddomain']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setopt getopt][write read][append read][setattr getattr][write read]'
G.edge['system_server']['untrusteddomain']['fill'] = 'red'
G.add_edge('system_server','untrusteddomain')
G.edge['system_server']['untrusteddomain']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setopt getopt][write read][append read][setattr getattr][write read][append read]'
G.add_edge('system_server','appdomain')
G.edge['system_server']['appdomain']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][setopt getopt][write read][append read][write read][open open][write read][append read][write read][setattr getattr][write read][append read][setopt getopt]'
G.add_edge('system_server','bluetoothdomain')
G.edge['system_server']['bluetoothdomain']['write-read'] = '[write read][setopt getopt]'
G.add_edge('system_server','untrusteddomain')
G.edge['system_server']['untrusteddomain']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setopt getopt][write read][append read][setattr getattr][write read][append read][setopt getopt]'
G.add_edge('untrusteddomain','appdomain')
G.edge['untrusteddomain']['appdomain']['write-read'] = '[open open][write read][append read][write read][write read][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][setattr getattr]'
G.add_edge('untrusteddomain','untrusteddomain')
G.edge['untrusteddomain']['untrusteddomain']['write-read'] = '[open open][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][setopt getopt][write read][setattr getattr]'
G.add_edge('untrusteddomain','appdomain')
G.edge['untrusteddomain']['appdomain']['write-read'] = '[open open][write read][append read][write read][write read][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read]'
G.edge['untrusteddomain']['appdomain']['fill'] = 'red'
G.add_edge('untrusteddomain','appdomain')
G.edge['untrusteddomain']['appdomain']['write-read'] = '[open open][write read][append read][write read][write read][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][append read]'
G.add_edge('untrusteddomain','bluetoothdomain')
G.edge['untrusteddomain']['bluetoothdomain']['write-read'] = '[write read]'
G.edge['untrusteddomain']['bluetoothdomain']['fill'] = 'red'
G.add_edge('untrusteddomain','commonplatformappdomain')
G.edge['untrusteddomain']['commonplatformappdomain']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][setattr getattr][write read][append read][setopt getopt][write read][write read]'
G.edge['untrusteddomain']['commonplatformappdomain']['fill'] = 'red'
G.add_edge('untrusteddomain','samsung_app')
G.edge['untrusteddomain']['samsung_app']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][write read]'
G.edge['untrusteddomain']['samsung_app']['fill'] = 'red'
G.add_edge('untrusteddomain','system_server')
G.edge['untrusteddomain']['system_server']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][setopt getopt][write read]'
G.edge['untrusteddomain']['system_server']['fill'] = 'red'
G.add_edge('untrusteddomain','untrusteddomain')
G.edge['untrusteddomain']['untrusteddomain']['write-read'] = '[open open][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][setopt getopt][write read][setattr getattr][write read]'
G.edge['untrusteddomain']['untrusteddomain']['fill'] = 'red'
G.add_edge('untrusteddomain','untrusteddomain')
G.edge['untrusteddomain']['untrusteddomain']['write-read'] = '[open open][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][setopt getopt][write read][setattr getattr][write read][append read]'
G.add_edge('untrusteddomain','appdomain')
G.edge['untrusteddomain']['appdomain']['write-read'] = '[open open][write read][append read][write read][write read][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][append read][setopt getopt]'
G.add_edge('untrusteddomain','bluetoothdomain')
G.edge['untrusteddomain']['bluetoothdomain']['write-read'] = '[write read][setopt getopt]'
G.add_edge('untrusteddomain','untrusteddomain')
G.edge['untrusteddomain']['untrusteddomain']['write-read'] = '[open open][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][setopt getopt][write read][setattr getattr][write read][append read][setopt getopt]'
app = Viewer(G)
app.mainloop()