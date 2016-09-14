import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('charon','charon')
G.edge['charon']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('charon','drmserver')
G.edge['charon']['drmserver']['write-read'] = '[open open]'
G.add_edge('charon','fixmo_app')
G.edge['charon']['fixmo_app']['write-read'] = '[open open]'
G.add_edge('charon','good_app')
G.edge['charon']['good_app']['write-read'] = '[open open]'
G.add_edge('charon','ime_app')
G.edge['charon']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('charon','knox_system_app')
G.edge['charon']['knox_system_app']['write-read'] = '[open open]'
G.add_edge('charon','netd')
G.edge['charon']['netd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read][open open]'
G.add_edge('charon','samsung_app')
G.edge['charon']['samsung_app']['write-read'] = '[open open]'
G.add_edge('charon','shell')
G.edge['charon']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('charon','s_system_app')
G.edge['charon']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read][open open]'
G.add_edge('charon','system_app')
G.edge['charon']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read][open open]'
G.add_edge('charon','knox_system_app')
G.edge['charon']['knox_system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('charon','appdomain')
G.edge['charon']['appdomain']['write-read'] = '[write read]'
G.edge['charon']['appdomain']['fill'] = 'red'
G.add_edge('charon','charon')
G.edge['charon']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['charon']['charon']['fill'] = 'red'
G.add_edge('charon','charon')
G.edge['charon']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('charon','drmserver')
G.edge['charon']['drmserver']['write-read'] = '[open open][write read]'
G.edge['charon']['drmserver']['fill'] = 'red'
G.add_edge('charon','drmserver')
G.edge['charon']['drmserver']['write-read'] = '[open open][write read][append read]'
G.add_edge('charon','fixmo_app')
G.edge['charon']['fixmo_app']['write-read'] = '[open open][write read]'
G.edge['charon']['fixmo_app']['fill'] = 'red'
G.add_edge('charon','fixmo_app')
G.edge['charon']['fixmo_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('charon','ftm_ptt')
G.edge['charon']['ftm_ptt']['write-read'] = '[write read]'
G.edge['charon']['ftm_ptt']['fill'] = 'red'
G.add_edge('charon','good_app')
G.edge['charon']['good_app']['write-read'] = '[open open][write read]'
G.edge['charon']['good_app']['fill'] = 'red'
G.add_edge('charon','good_app')
G.edge['charon']['good_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('charon','ime_app')
G.edge['charon']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['charon']['ime_app']['fill'] = 'red'
G.add_edge('charon','ime_app')
G.edge['charon']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('charon','imsd')
G.edge['charon']['imsd']['write-read'] = '[write read]'
G.edge['charon']['imsd']['fill'] = 'red'
G.add_edge('charon','knox_system_app')
G.edge['charon']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['charon']['knox_system_app']['fill'] = 'red'
G.add_edge('charon','knox_system_app')
G.edge['charon']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('charon','netd')
G.edge['charon']['netd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read]'
G.edge['charon']['netd']['fill'] = 'red'
G.add_edge('charon','netd')
G.edge['charon']['netd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read][append read]'
G.add_edge('charon','netdomain')
G.edge['charon']['netdomain']['write-read'] = '[write read]'
G.edge['charon']['netdomain']['fill'] = 'red'
G.add_edge('charon','ppp')
G.edge['charon']['ppp']['write-read'] = '[write read]'
G.edge['charon']['ppp']['fill'] = 'red'
G.add_edge('charon','pppoewrapper')
G.edge['charon']['pppoewrapper']['write-read'] = '[write read]'
G.edge['charon']['pppoewrapper']['fill'] = 'red'
G.add_edge('charon','racoon')
G.edge['charon']['racoon']['write-read'] = '[add_name search][write read]'
G.edge['charon']['racoon']['fill'] = 'red'
G.add_edge('charon','samsung_app')
G.edge['charon']['samsung_app']['write-read'] = '[open open][write read]'
G.edge['charon']['samsung_app']['fill'] = 'red'
G.add_edge('charon','samsung_app')
G.edge['charon']['samsung_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('charon','shell')
G.edge['charon']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['charon']['shell']['fill'] = 'red'
G.add_edge('charon','shell')
G.edge['charon']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('charon','s_system_app')
G.edge['charon']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read][open open][write read]'
G.edge['charon']['s_system_app']['fill'] = 'red'
G.add_edge('charon','s_system_app')
G.edge['charon']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read][open open][write read][append read]'
G.add_edge('charon','system_app')
G.edge['charon']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read][open open][write read]'
G.edge['charon']['system_app']['fill'] = 'red'
G.add_edge('charon','system_app')
G.edge['charon']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read][open open][write read][append read]'
G.add_edge('charon','vmware_app')
G.edge['charon']['vmware_app']['write-read'] = '[write read]'
G.edge['charon']['vmware_app']['fill'] = 'red'
G.add_edge('charon','zygote')
G.edge['charon']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['charon']['zygote']['fill'] = 'red'
G.add_edge('fixmo_app','charon')
G.edge['fixmo_app']['charon']['write-read'] = '[open open]'
G.add_edge('fixmo_app','drmserver')
G.edge['fixmo_app']['drmserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('fixmo_app','fixmo_app')
G.edge['fixmo_app']['fixmo_app']['write-read'] = '[write read][setopt getopt][write read][setopt getopt][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('fixmo_app','good_app')
G.edge['fixmo_app']['good_app']['write-read'] = '[write read][setopt getopt][write read][setopt getopt][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][write read][setopt getopt][write read][setopt getopt][open open][write read][append read][open open]'
G.add_edge('fixmo_app','ime_app')
G.edge['fixmo_app']['ime_app']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('fixmo_app','knox_system_app')
G.edge['fixmo_app']['knox_system_app']['write-read'] = '[open open]'
G.add_edge('fixmo_app','netd')
G.edge['fixmo_app']['netd']['write-read'] = '[open open]'
G.add_edge('fixmo_app','samsung_app')
G.edge['fixmo_app']['samsung_app']['write-read'] = '[open open]'
G.add_edge('fixmo_app','shell')
G.edge['fixmo_app']['shell']['write-read'] = '[write read][setopt getopt][open open]'
G.add_edge('fixmo_app','s_system_app')
G.edge['fixmo_app']['s_system_app']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('fixmo_app','system_app')
G.edge['fixmo_app']['system_app']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('fixmo_app','knox_system_app')
G.edge['fixmo_app']['knox_system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('fixmo_app','appdomain')
G.edge['fixmo_app']['appdomain']['write-read'] = '[write read]'
G.edge['fixmo_app']['appdomain']['fill'] = 'red'
G.add_edge('fixmo_app','charon')
G.edge['fixmo_app']['charon']['write-read'] = '[open open][write read]'
G.edge['fixmo_app']['charon']['fill'] = 'red'
G.add_edge('fixmo_app','charon')
G.edge['fixmo_app']['charon']['write-read'] = '[open open][write read][append read]'
G.add_edge('fixmo_app','drmserver')
G.edge['fixmo_app']['drmserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['fixmo_app']['drmserver']['fill'] = 'red'
G.add_edge('fixmo_app','drmserver')
G.edge['fixmo_app']['drmserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('fixmo_app','fixmo_app')
G.edge['fixmo_app']['fixmo_app']['write-read'] = '[write read][setopt getopt][write read][setopt getopt][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['fixmo_app']['fixmo_app']['fill'] = 'red'
G.add_edge('fixmo_app','fixmo_app')
G.edge['fixmo_app']['fixmo_app']['write-read'] = '[write read][setopt getopt][write read][setopt getopt][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('fixmo_app','ftm_ptt')
G.edge['fixmo_app']['ftm_ptt']['write-read'] = '[write read]'
G.edge['fixmo_app']['ftm_ptt']['fill'] = 'red'
G.add_edge('fixmo_app','good_app')
G.edge['fixmo_app']['good_app']['write-read'] = '[write read][setopt getopt][write read][setopt getopt][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][write read][setopt getopt][write read][setopt getopt][open open][write read][append read][open open][write read]'
G.edge['fixmo_app']['good_app']['fill'] = 'red'
G.add_edge('fixmo_app','good_app')
G.edge['fixmo_app']['good_app']['write-read'] = '[write read][setopt getopt][write read][setopt getopt][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][write read][setopt getopt][write read][setopt getopt][open open][write read][append read][open open][write read][append read]'
G.add_edge('fixmo_app','ime_app')
G.edge['fixmo_app']['ime_app']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['fixmo_app']['ime_app']['fill'] = 'red'
G.add_edge('fixmo_app','ime_app')
G.edge['fixmo_app']['ime_app']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('fixmo_app','imsd')
G.edge['fixmo_app']['imsd']['write-read'] = '[write read]'
G.edge['fixmo_app']['imsd']['fill'] = 'red'
G.add_edge('fixmo_app','knox_system_app')
G.edge['fixmo_app']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['fixmo_app']['knox_system_app']['fill'] = 'red'
G.add_edge('fixmo_app','knox_system_app')
G.edge['fixmo_app']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('fixmo_app','netd')
G.edge['fixmo_app']['netd']['write-read'] = '[open open][write read]'
G.edge['fixmo_app']['netd']['fill'] = 'red'
G.add_edge('fixmo_app','netd')
G.edge['fixmo_app']['netd']['write-read'] = '[open open][write read][append read]'
G.add_edge('fixmo_app','netdomain')
G.edge['fixmo_app']['netdomain']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read]'
G.edge['fixmo_app']['netdomain']['fill'] = 'red'
G.add_edge('fixmo_app','ppp')
G.edge['fixmo_app']['ppp']['write-read'] = '[write read]'
G.edge['fixmo_app']['ppp']['fill'] = 'red'
G.add_edge('fixmo_app','pppoewrapper')
G.edge['fixmo_app']['pppoewrapper']['write-read'] = '[write read]'
G.edge['fixmo_app']['pppoewrapper']['fill'] = 'red'
G.add_edge('fixmo_app','racoon')
G.edge['fixmo_app']['racoon']['write-read'] = '[write read]'
G.edge['fixmo_app']['racoon']['fill'] = 'red'
G.add_edge('fixmo_app','samsung_app')
G.edge['fixmo_app']['samsung_app']['write-read'] = '[open open][write read]'
G.edge['fixmo_app']['samsung_app']['fill'] = 'red'
G.add_edge('fixmo_app','samsung_app')
G.edge['fixmo_app']['samsung_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('fixmo_app','shell')
G.edge['fixmo_app']['shell']['write-read'] = '[write read][setopt getopt][open open][write read]'
G.edge['fixmo_app']['shell']['fill'] = 'red'
G.add_edge('fixmo_app','shell')
G.edge['fixmo_app']['shell']['write-read'] = '[write read][setopt getopt][open open][write read][append read]'
G.add_edge('fixmo_app','s_system_app')
G.edge['fixmo_app']['s_system_app']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['fixmo_app']['s_system_app']['fill'] = 'red'
G.add_edge('fixmo_app','s_system_app')
G.edge['fixmo_app']['s_system_app']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('fixmo_app','system_app')
G.edge['fixmo_app']['system_app']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['fixmo_app']['system_app']['fill'] = 'red'
G.add_edge('fixmo_app','system_app')
G.edge['fixmo_app']['system_app']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('fixmo_app','vmware_app')
G.edge['fixmo_app']['vmware_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['fixmo_app']['vmware_app']['fill'] = 'red'
G.add_edge('fixmo_app','zygote')
G.edge['fixmo_app']['zygote']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['fixmo_app']['zygote']['fill'] = 'red'
G.add_edge('good_app','charon')
G.edge['good_app']['charon']['write-read'] = '[open open]'
G.add_edge('good_app','drmserver')
G.edge['good_app']['drmserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('good_app','fixmo_app')
G.edge['good_app']['fixmo_app']['write-read'] = '[write read][setopt getopt][write read][setopt getopt][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][write read][setopt getopt][open open][write read][append read][open open]'
G.add_edge('good_app','good_app')
G.edge['good_app']['good_app']['write-read'] = '[write read][setopt getopt][write read][setopt getopt][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][write read][setopt getopt][write read][setopt getopt][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('good_app','ime_app')
G.edge['good_app']['ime_app']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('good_app','knox_system_app')
G.edge['good_app']['knox_system_app']['write-read'] = '[open open]'
G.add_edge('good_app','netd')
G.edge['good_app']['netd']['write-read'] = '[open open]'
G.add_edge('good_app','samsung_app')
G.edge['good_app']['samsung_app']['write-read'] = '[open open]'
G.add_edge('good_app','shell')
G.edge['good_app']['shell']['write-read'] = '[write read][setopt getopt][open open]'
G.add_edge('good_app','s_system_app')
G.edge['good_app']['s_system_app']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('good_app','system_app')
G.edge['good_app']['system_app']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('good_app','knox_system_app')
G.edge['good_app']['knox_system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('good_app','appdomain')
G.edge['good_app']['appdomain']['write-read'] = '[write read]'
G.edge['good_app']['appdomain']['fill'] = 'red'
G.add_edge('good_app','charon')
G.edge['good_app']['charon']['write-read'] = '[open open][write read]'
G.edge['good_app']['charon']['fill'] = 'red'
G.add_edge('good_app','charon')
G.edge['good_app']['charon']['write-read'] = '[open open][write read][append read]'
G.add_edge('good_app','drmserver')
G.edge['good_app']['drmserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['good_app']['drmserver']['fill'] = 'red'
G.add_edge('good_app','drmserver')
G.edge['good_app']['drmserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('good_app','fixmo_app')
G.edge['good_app']['fixmo_app']['write-read'] = '[write read][setopt getopt][write read][setopt getopt][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][write read][setopt getopt][open open][write read][append read][open open][write read]'
G.edge['good_app']['fixmo_app']['fill'] = 'red'
G.add_edge('good_app','fixmo_app')
G.edge['good_app']['fixmo_app']['write-read'] = '[write read][setopt getopt][write read][setopt getopt][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][write read][setopt getopt][open open][write read][append read][open open][write read][append read]'
G.add_edge('good_app','ftm_ptt')
G.edge['good_app']['ftm_ptt']['write-read'] = '[write read]'
G.edge['good_app']['ftm_ptt']['fill'] = 'red'
G.add_edge('good_app','good_app')
G.edge['good_app']['good_app']['write-read'] = '[write read][setopt getopt][write read][setopt getopt][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][write read][setopt getopt][write read][setopt getopt][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['good_app']['good_app']['fill'] = 'red'
G.add_edge('good_app','good_app')
G.edge['good_app']['good_app']['write-read'] = '[write read][setopt getopt][write read][setopt getopt][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][write read][setopt getopt][write read][setopt getopt][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('good_app','ime_app')
G.edge['good_app']['ime_app']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['good_app']['ime_app']['fill'] = 'red'
G.add_edge('good_app','ime_app')
G.edge['good_app']['ime_app']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('good_app','imsd')
G.edge['good_app']['imsd']['write-read'] = '[write read]'
G.edge['good_app']['imsd']['fill'] = 'red'
G.add_edge('good_app','knox_system_app')
G.edge['good_app']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['good_app']['knox_system_app']['fill'] = 'red'
G.add_edge('good_app','knox_system_app')
G.edge['good_app']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('good_app','netd')
G.edge['good_app']['netd']['write-read'] = '[open open][write read]'
G.edge['good_app']['netd']['fill'] = 'red'
G.add_edge('good_app','netd')
G.edge['good_app']['netd']['write-read'] = '[open open][write read][append read]'
G.add_edge('good_app','netdomain')
G.edge['good_app']['netdomain']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read]'
G.edge['good_app']['netdomain']['fill'] = 'red'
G.add_edge('good_app','ppp')
G.edge['good_app']['ppp']['write-read'] = '[write read]'
G.edge['good_app']['ppp']['fill'] = 'red'
G.add_edge('good_app','pppoewrapper')
G.edge['good_app']['pppoewrapper']['write-read'] = '[write read]'
G.edge['good_app']['pppoewrapper']['fill'] = 'red'
G.add_edge('good_app','racoon')
G.edge['good_app']['racoon']['write-read'] = '[write read]'
G.edge['good_app']['racoon']['fill'] = 'red'
G.add_edge('good_app','samsung_app')
G.edge['good_app']['samsung_app']['write-read'] = '[open open][write read]'
G.edge['good_app']['samsung_app']['fill'] = 'red'
G.add_edge('good_app','samsung_app')
G.edge['good_app']['samsung_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('good_app','shell')
G.edge['good_app']['shell']['write-read'] = '[write read][setopt getopt][open open][write read]'
G.edge['good_app']['shell']['fill'] = 'red'
G.add_edge('good_app','shell')
G.edge['good_app']['shell']['write-read'] = '[write read][setopt getopt][open open][write read][append read]'
G.add_edge('good_app','s_system_app')
G.edge['good_app']['s_system_app']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['good_app']['s_system_app']['fill'] = 'red'
G.add_edge('good_app','s_system_app')
G.edge['good_app']['s_system_app']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('good_app','system_app')
G.edge['good_app']['system_app']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['good_app']['system_app']['fill'] = 'red'
G.add_edge('good_app','system_app')
G.edge['good_app']['system_app']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('good_app','vmware_app')
G.edge['good_app']['vmware_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['good_app']['vmware_app']['fill'] = 'red'
G.add_edge('good_app','zygote')
G.edge['good_app']['zygote']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['good_app']['zygote']['fill'] = 'red'
G.add_edge('knox_system_app','charon')
G.edge['knox_system_app']['charon']['write-read'] = '[open open]'
G.add_edge('knox_system_app','drmserver')
G.edge['knox_system_app']['drmserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('knox_system_app','fixmo_app')
G.edge['knox_system_app']['fixmo_app']['write-read'] = '[open open]'
G.add_edge('knox_system_app','good_app')
G.edge['knox_system_app']['good_app']['write-read'] = '[open open]'
G.add_edge('knox_system_app','ime_app')
G.edge['knox_system_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][open open]'
G.add_edge('knox_system_app','knox_system_app')
G.edge['knox_system_app']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('knox_system_app','netd')
G.edge['knox_system_app']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('knox_system_app','samsung_app')
G.edge['knox_system_app']['samsung_app']['write-read'] = '[open open]'
G.add_edge('knox_system_app','shell')
G.edge['knox_system_app']['shell']['write-read'] = '[open open]'
G.add_edge('knox_system_app','s_system_app')
G.edge['knox_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][open open]'
G.add_edge('knox_system_app','system_app')
G.edge['knox_system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][open open]'
G.add_edge('knox_system_app','knox_system_app')
G.edge['knox_system_app']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('knox_system_app','appdomain')
G.edge['knox_system_app']['appdomain']['write-read'] = '[write read]'
G.edge['knox_system_app']['appdomain']['fill'] = 'red'
G.add_edge('knox_system_app','charon')
G.edge['knox_system_app']['charon']['write-read'] = '[open open][write read]'
G.edge['knox_system_app']['charon']['fill'] = 'red'
G.add_edge('knox_system_app','charon')
G.edge['knox_system_app']['charon']['write-read'] = '[open open][write read][append read]'
G.add_edge('knox_system_app','drmserver')
G.edge['knox_system_app']['drmserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['knox_system_app']['drmserver']['fill'] = 'red'
G.add_edge('knox_system_app','drmserver')
G.edge['knox_system_app']['drmserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('knox_system_app','fixmo_app')
G.edge['knox_system_app']['fixmo_app']['write-read'] = '[open open][write read]'
G.edge['knox_system_app']['fixmo_app']['fill'] = 'red'
G.add_edge('knox_system_app','fixmo_app')
G.edge['knox_system_app']['fixmo_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('knox_system_app','ftm_ptt')
G.edge['knox_system_app']['ftm_ptt']['write-read'] = '[write read]'
G.edge['knox_system_app']['ftm_ptt']['fill'] = 'red'
G.add_edge('knox_system_app','good_app')
G.edge['knox_system_app']['good_app']['write-read'] = '[open open][write read]'
G.edge['knox_system_app']['good_app']['fill'] = 'red'
G.add_edge('knox_system_app','good_app')
G.edge['knox_system_app']['good_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('knox_system_app','ime_app')
G.edge['knox_system_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['knox_system_app']['ime_app']['fill'] = 'red'
G.add_edge('knox_system_app','ime_app')
G.edge['knox_system_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('knox_system_app','imsd')
G.edge['knox_system_app']['imsd']['write-read'] = '[write read]'
G.edge['knox_system_app']['imsd']['fill'] = 'red'
G.add_edge('knox_system_app','knox_system_app')
G.edge['knox_system_app']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['knox_system_app']['knox_system_app']['fill'] = 'red'
G.add_edge('knox_system_app','knox_system_app')
G.edge['knox_system_app']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('knox_system_app','netd')
G.edge['knox_system_app']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read]'
G.edge['knox_system_app']['netd']['fill'] = 'red'
G.add_edge('knox_system_app','netd')
G.edge['knox_system_app']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('knox_system_app','netdomain')
G.edge['knox_system_app']['netdomain']['write-read'] = '[write read]'
G.edge['knox_system_app']['netdomain']['fill'] = 'red'
G.add_edge('knox_system_app','ppp')
G.edge['knox_system_app']['ppp']['write-read'] = '[write read]'
G.edge['knox_system_app']['ppp']['fill'] = 'red'
G.add_edge('knox_system_app','pppoewrapper')
G.edge['knox_system_app']['pppoewrapper']['write-read'] = '[write read]'
G.edge['knox_system_app']['pppoewrapper']['fill'] = 'red'
G.add_edge('knox_system_app','racoon')
G.edge['knox_system_app']['racoon']['write-read'] = '[write read]'
G.edge['knox_system_app']['racoon']['fill'] = 'red'
G.add_edge('knox_system_app','samsung_app')
G.edge['knox_system_app']['samsung_app']['write-read'] = '[open open][write read]'
G.edge['knox_system_app']['samsung_app']['fill'] = 'red'
G.add_edge('knox_system_app','samsung_app')
G.edge['knox_system_app']['samsung_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('knox_system_app','shell')
G.edge['knox_system_app']['shell']['write-read'] = '[open open][write read]'
G.edge['knox_system_app']['shell']['fill'] = 'red'
G.add_edge('knox_system_app','shell')
G.edge['knox_system_app']['shell']['write-read'] = '[open open][write read][append read]'
G.add_edge('knox_system_app','s_system_app')
G.edge['knox_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['knox_system_app']['s_system_app']['fill'] = 'red'
G.add_edge('knox_system_app','s_system_app')
G.edge['knox_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('knox_system_app','system_app')
G.edge['knox_system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['knox_system_app']['system_app']['fill'] = 'red'
G.add_edge('knox_system_app','system_app')
G.edge['knox_system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('knox_system_app','vmware_app')
G.edge['knox_system_app']['vmware_app']['write-read'] = '[write read]'
G.edge['knox_system_app']['vmware_app']['fill'] = 'red'
G.add_edge('knox_system_app','zygote')
G.edge['knox_system_app']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['knox_system_app']['zygote']['fill'] = 'red'
app = Viewer(G)
app.mainloop()