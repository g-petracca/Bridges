import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('at_distributor','at_distributor')
G.edge['at_distributor']['at_distributor']['write-read'] = '[open open]'
G.add_edge('at_distributor','cbd')
G.edge['at_distributor']['cbd']['write-read'] = '[open open]'
G.add_edge('at_distributor','charon')
G.edge['at_distributor']['charon']['write-read'] = '[open open]'
G.add_edge('at_distributor','debuggerd')
G.edge['at_distributor']['debuggerd']['write-read'] = '[open open]'
G.add_edge('at_distributor','diag_uart_log')
G.edge['at_distributor']['diag_uart_log']['write-read'] = '[open open]'
G.add_edge('at_distributor','dumpstate')
G.edge['at_distributor']['dumpstate']['write-read'] = '[open open]'
G.add_edge('at_distributor','hostapd')
G.edge['at_distributor']['hostapd']['write-read'] = '[open open]'
G.add_edge('at_distributor','ime_app')
G.edge['at_distributor']['ime_app']['write-read'] = '[open open]'
G.add_edge('at_distributor','init_shell')
G.edge['at_distributor']['init_shell']['write-read'] = '[open open]'
G.add_edge('at_distributor','installd')
G.edge['at_distributor']['installd']['write-read'] = '[open open]'
G.add_edge('at_distributor','itsonbs')
G.edge['at_distributor']['itsonbs']['write-read'] = '[open open]'
G.add_edge('at_distributor','logwrapper')
G.edge['at_distributor']['logwrapper']['write-read'] = '[open open]'
G.add_edge('at_distributor','netd')
G.edge['at_distributor']['netd']['write-read'] = '[open open]'
G.add_edge('at_distributor','qmuxd')
G.edge['at_distributor']['qmuxd']['write-read'] = '[open open]'
G.add_edge('at_distributor','rild')
G.edge['at_distributor']['rild']['write-read'] = '[open open]'
G.add_edge('at_distributor','rmt_storage')
G.edge['at_distributor']['rmt_storage']['write-read'] = '[open open]'
G.add_edge('at_distributor','sdcardd')
G.edge['at_distributor']['sdcardd']['write-read'] = '[open open]'
G.add_edge('at_distributor','shell')
G.edge['at_distributor']['shell']['write-read'] = '[open open]'
G.add_edge('at_distributor','s_system_app')
G.edge['at_distributor']['s_system_app']['write-read'] = '[open open]'
G.add_edge('at_distributor','system_app')
G.edge['at_distributor']['system_app']['write-read'] = '[open open]'
G.add_edge('at_distributor','system_server')
G.edge['at_distributor']['system_server']['write-read'] = '[open open]'
G.add_edge('at_distributor','vmwared')
G.edge['at_distributor']['vmwared']['write-read'] = '[open open]'
G.add_edge('at_distributor','wpa')
G.edge['at_distributor']['wpa']['write-read'] = '[open open]'
G.add_edge('at_distributor','zygote')
G.edge['at_distributor']['zygote']['write-read'] = '[open open]'
G.add_edge('at_distributor','at_distributor')
G.edge['at_distributor']['at_distributor']['write-read'] = '[open open][setattr getattr]'
G.add_edge('at_distributor','cbd')
G.edge['at_distributor']['cbd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('at_distributor','charon')
G.edge['at_distributor']['charon']['write-read'] = '[open open][setattr getattr]'
G.add_edge('at_distributor','debuggerd')
G.edge['at_distributor']['debuggerd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('at_distributor','diag_uart_log')
G.edge['at_distributor']['diag_uart_log']['write-read'] = '[open open][setattr getattr]'
G.add_edge('at_distributor','dumpstate')
G.edge['at_distributor']['dumpstate']['write-read'] = '[open open][setattr getattr]'
G.add_edge('at_distributor','hostapd')
G.edge['at_distributor']['hostapd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('at_distributor','ime_app')
G.edge['at_distributor']['ime_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('at_distributor','init_shell')
G.edge['at_distributor']['init_shell']['write-read'] = '[open open][setattr getattr]'
G.add_edge('at_distributor','installd')
G.edge['at_distributor']['installd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('at_distributor','itsonbs')
G.edge['at_distributor']['itsonbs']['write-read'] = '[open open][setattr getattr]'
G.add_edge('at_distributor','logwrapper')
G.edge['at_distributor']['logwrapper']['write-read'] = '[open open][setattr getattr]'
G.add_edge('at_distributor','netd')
G.edge['at_distributor']['netd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('at_distributor','qmuxd')
G.edge['at_distributor']['qmuxd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('at_distributor','rild')
G.edge['at_distributor']['rild']['write-read'] = '[open open][setattr getattr]'
G.add_edge('at_distributor','rmt_storage')
G.edge['at_distributor']['rmt_storage']['write-read'] = '[open open][setattr getattr]'
G.add_edge('at_distributor','sdcardd')
G.edge['at_distributor']['sdcardd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('at_distributor','shell')
G.edge['at_distributor']['shell']['write-read'] = '[open open][setattr getattr]'
G.add_edge('at_distributor','s_system_app')
G.edge['at_distributor']['s_system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('at_distributor','system_app')
G.edge['at_distributor']['system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('at_distributor','system_server')
G.edge['at_distributor']['system_server']['write-read'] = '[open open][setattr getattr]'
G.add_edge('at_distributor','vmwared')
G.edge['at_distributor']['vmwared']['write-read'] = '[open open][setattr getattr]'
G.add_edge('at_distributor','wpa')
G.edge['at_distributor']['wpa']['write-read'] = '[open open][setattr getattr]'
G.add_edge('at_distributor','zygote')
G.edge['at_distributor']['zygote']['write-read'] = '[open open][setattr getattr]'
G.add_edge('at_distributor','adbd')
G.edge['at_distributor']['adbd']['write-read'] = '[write read]'
G.edge['at_distributor']['adbd']['fill'] = 'red'
G.add_edge('at_distributor','at_distributor')
G.edge['at_distributor']['at_distributor']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['at_distributor']['at_distributor']['fill'] = 'red'
G.add_edge('at_distributor','cbd')
G.edge['at_distributor']['cbd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['at_distributor']['cbd']['fill'] = 'red'
G.add_edge('at_distributor','charon')
G.edge['at_distributor']['charon']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['at_distributor']['charon']['fill'] = 'red'
G.add_edge('at_distributor','debuggerd')
G.edge['at_distributor']['debuggerd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['at_distributor']['debuggerd']['fill'] = 'red'
G.add_edge('at_distributor','dhcp')
G.edge['at_distributor']['dhcp']['write-read'] = '[write read]'
G.edge['at_distributor']['dhcp']['fill'] = 'red'
G.add_edge('at_distributor','diag_uart_log')
G.edge['at_distributor']['diag_uart_log']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['at_distributor']['diag_uart_log']['fill'] = 'red'
G.add_edge('at_distributor','domain')
G.edge['at_distributor']['domain']['write-read'] = '[write read]'
G.edge['at_distributor']['domain']['fill'] = 'red'
G.add_edge('at_distributor','dumpstate')
G.edge['at_distributor']['dumpstate']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['at_distributor']['dumpstate']['fill'] = 'red'
G.add_edge('at_distributor','hostapd')
G.edge['at_distributor']['hostapd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['at_distributor']['hostapd']['fill'] = 'red'
G.add_edge('at_distributor','ime_app')
G.edge['at_distributor']['ime_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['at_distributor']['ime_app']['fill'] = 'red'
G.add_edge('at_distributor','init_shell')
G.edge['at_distributor']['init_shell']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['at_distributor']['init_shell']['fill'] = 'red'
G.add_edge('at_distributor','installd')
G.edge['at_distributor']['installd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['at_distributor']['installd']['fill'] = 'red'
G.add_edge('at_distributor','itsonbs')
G.edge['at_distributor']['itsonbs']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['at_distributor']['itsonbs']['fill'] = 'red'
G.add_edge('at_distributor','logwrapper')
G.edge['at_distributor']['logwrapper']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['at_distributor']['logwrapper']['fill'] = 'red'
G.add_edge('at_distributor','netd')
G.edge['at_distributor']['netd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['at_distributor']['netd']['fill'] = 'red'
G.add_edge('at_distributor','qmuxd')
G.edge['at_distributor']['qmuxd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['at_distributor']['qmuxd']['fill'] = 'red'
G.add_edge('at_distributor','rild')
G.edge['at_distributor']['rild']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['at_distributor']['rild']['fill'] = 'red'
G.add_edge('at_distributor','rmt_storage')
G.edge['at_distributor']['rmt_storage']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['at_distributor']['rmt_storage']['fill'] = 'red'
G.add_edge('at_distributor','sdcardd')
G.edge['at_distributor']['sdcardd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['at_distributor']['sdcardd']['fill'] = 'red'
G.add_edge('at_distributor','shell')
G.edge['at_distributor']['shell']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['at_distributor']['shell']['fill'] = 'red'
G.add_edge('at_distributor','s_system_app')
G.edge['at_distributor']['s_system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['at_distributor']['s_system_app']['fill'] = 'red'
G.add_edge('at_distributor','system_app')
G.edge['at_distributor']['system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['at_distributor']['system_app']['fill'] = 'red'
G.add_edge('at_distributor','system_server')
G.edge['at_distributor']['system_server']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['at_distributor']['system_server']['fill'] = 'red'
G.add_edge('at_distributor','vmwared')
G.edge['at_distributor']['vmwared']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['at_distributor']['vmwared']['fill'] = 'red'
G.add_edge('at_distributor','wpa')
G.edge['at_distributor']['wpa']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['at_distributor']['wpa']['fill'] = 'red'
G.add_edge('at_distributor','zygote')
G.edge['at_distributor']['zygote']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['at_distributor']['zygote']['fill'] = 'red'
G.add_edge('at_distributor','adbd')
G.edge['at_distributor']['adbd']['write-read'] = '[write read][add_name search]'
G.add_edge('at_distributor','at_distributor')
G.edge['at_distributor']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('at_distributor','at_distributor')
G.edge['at_distributor']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('at_distributor','auditd')
G.edge['at_distributor']['auditd']['write-read'] = '[add_name search]'
G.add_edge('at_distributor','cbd')
G.edge['at_distributor']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('at_distributor','cbd')
G.edge['at_distributor']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('at_distributor','charon')
G.edge['at_distributor']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('at_distributor','charon')
G.edge['at_distributor']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('at_distributor','clatd')
G.edge['at_distributor']['clatd']['write-read'] = '[add_name search]'
G.add_edge('at_distributor','debuggerd')
G.edge['at_distributor']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('at_distributor','debuggerd')
G.edge['at_distributor']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('at_distributor','dhcp')
G.edge['at_distributor']['dhcp']['write-read'] = '[write read][add_name search]'
G.add_edge('at_distributor','diag_uart_log')
G.edge['at_distributor']['diag_uart_log']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('at_distributor','diag_uart_log')
G.edge['at_distributor']['diag_uart_log']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('at_distributor','dumpstate')
G.edge['at_distributor']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('at_distributor','dumpstate')
G.edge['at_distributor']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('at_distributor','hostapd')
G.edge['at_distributor']['hostapd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('at_distributor','hostapd')
G.edge['at_distributor']['hostapd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('at_distributor','hvdcp')
G.edge['at_distributor']['hvdcp']['write-read'] = '[add_name search]'
G.add_edge('at_distributor','ime_app')
G.edge['at_distributor']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('at_distributor','ime_app')
G.edge['at_distributor']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('at_distributor','init_shell')
G.edge['at_distributor']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('at_distributor','init_shell')
G.edge['at_distributor']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('at_distributor','installd')
G.edge['at_distributor']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('at_distributor','installd')
G.edge['at_distributor']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('at_distributor','itsonbs')
G.edge['at_distributor']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('at_distributor','itsonbs')
G.edge['at_distributor']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('at_distributor','jackservice')
G.edge['at_distributor']['jackservice']['write-read'] = '[add_name search]'
G.add_edge('at_distributor','lmkd')
G.edge['at_distributor']['lmkd']['write-read'] = '[remove_name search]'
G.add_edge('at_distributor','logwrapper')
G.edge['at_distributor']['logwrapper']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('at_distributor','logwrapper')
G.edge['at_distributor']['logwrapper']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('at_distributor','msm_irqbalanced')
G.edge['at_distributor']['msm_irqbalanced']['write-read'] = '[add_name search]'
G.add_edge('at_distributor','netd')
G.edge['at_distributor']['netd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('at_distributor','netd')
G.edge['at_distributor']['netd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('at_distributor','qmuxd')
G.edge['at_distributor']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('at_distributor','qmuxd')
G.edge['at_distributor']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('at_distributor','racoon')
G.edge['at_distributor']['racoon']['write-read'] = '[add_name search]'
G.add_edge('at_distributor','rild')
G.edge['at_distributor']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('at_distributor','rild')
G.edge['at_distributor']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('at_distributor','rmt_storage')
G.edge['at_distributor']['rmt_storage']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('at_distributor','rmt_storage')
G.edge['at_distributor']['rmt_storage']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('at_distributor','sdcardd')
G.edge['at_distributor']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('at_distributor','sdcardd')
G.edge['at_distributor']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('at_distributor','sensors')
G.edge['at_distributor']['sensors']['write-read'] = '[add_name search]'
G.add_edge('at_distributor','shell')
G.edge['at_distributor']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('at_distributor','shell')
G.edge['at_distributor']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('at_distributor','s_system_app')
G.edge['at_distributor']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('at_distributor','s_system_app')
G.edge['at_distributor']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('at_distributor','system_app')
G.edge['at_distributor']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('at_distributor','system_app')
G.edge['at_distributor']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('at_distributor','system_server')
G.edge['at_distributor']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('at_distributor','system_server')
G.edge['at_distributor']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('at_distributor','system_server')
G.edge['at_distributor']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search]'
G.add_edge('at_distributor','vmwared')
G.edge['at_distributor']['vmwared']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('at_distributor','vmwared')
G.edge['at_distributor']['vmwared']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('at_distributor','wpa')
G.edge['at_distributor']['wpa']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('at_distributor','wpa')
G.edge['at_distributor']['wpa']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('at_distributor','zygote')
G.edge['at_distributor']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('at_distributor','zygote')
G.edge['at_distributor']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('cbd','at_distributor')
G.edge['cbd']['at_distributor']['write-read'] = '[open open]'
G.add_edge('cbd','cbd')
G.edge['cbd']['cbd']['write-read'] = '[open open]'
G.add_edge('cbd','charon')
G.edge['cbd']['charon']['write-read'] = '[open open]'
G.add_edge('cbd','debuggerd')
G.edge['cbd']['debuggerd']['write-read'] = '[open open]'
G.add_edge('cbd','diag_uart_log')
G.edge['cbd']['diag_uart_log']['write-read'] = '[open open]'
G.add_edge('cbd','dumpstate')
G.edge['cbd']['dumpstate']['write-read'] = '[open open]'
G.add_edge('cbd','hostapd')
G.edge['cbd']['hostapd']['write-read'] = '[open open]'
G.add_edge('cbd','ime_app')
G.edge['cbd']['ime_app']['write-read'] = '[open open]'
G.add_edge('cbd','init_shell')
G.edge['cbd']['init_shell']['write-read'] = '[open open]'
G.add_edge('cbd','installd')
G.edge['cbd']['installd']['write-read'] = '[open open]'
G.add_edge('cbd','itsonbs')
G.edge['cbd']['itsonbs']['write-read'] = '[open open]'
G.add_edge('cbd','logwrapper')
G.edge['cbd']['logwrapper']['write-read'] = '[open open]'
G.add_edge('cbd','netd')
G.edge['cbd']['netd']['write-read'] = '[open open]'
G.add_edge('cbd','qmuxd')
G.edge['cbd']['qmuxd']['write-read'] = '[open open]'
G.add_edge('cbd','rild')
G.edge['cbd']['rild']['write-read'] = '[open open]'
G.add_edge('cbd','rmt_storage')
G.edge['cbd']['rmt_storage']['write-read'] = '[open open]'
G.add_edge('cbd','sdcardd')
G.edge['cbd']['sdcardd']['write-read'] = '[open open]'
G.add_edge('cbd','shell')
G.edge['cbd']['shell']['write-read'] = '[open open]'
G.add_edge('cbd','s_system_app')
G.edge['cbd']['s_system_app']['write-read'] = '[open open]'
G.add_edge('cbd','system_app')
G.edge['cbd']['system_app']['write-read'] = '[open open]'
G.add_edge('cbd','system_server')
G.edge['cbd']['system_server']['write-read'] = '[open open]'
G.add_edge('cbd','vmwared')
G.edge['cbd']['vmwared']['write-read'] = '[open open]'
G.add_edge('cbd','wpa')
G.edge['cbd']['wpa']['write-read'] = '[open open]'
G.add_edge('cbd','zygote')
G.edge['cbd']['zygote']['write-read'] = '[open open]'
G.add_edge('cbd','at_distributor')
G.edge['cbd']['at_distributor']['write-read'] = '[open open][setattr getattr]'
G.add_edge('cbd','cbd')
G.edge['cbd']['cbd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('cbd','charon')
G.edge['cbd']['charon']['write-read'] = '[open open][setattr getattr]'
G.add_edge('cbd','debuggerd')
G.edge['cbd']['debuggerd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('cbd','diag_uart_log')
G.edge['cbd']['diag_uart_log']['write-read'] = '[open open][setattr getattr]'
G.add_edge('cbd','dumpstate')
G.edge['cbd']['dumpstate']['write-read'] = '[open open][setattr getattr]'
G.add_edge('cbd','hostapd')
G.edge['cbd']['hostapd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('cbd','ime_app')
G.edge['cbd']['ime_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('cbd','init_shell')
G.edge['cbd']['init_shell']['write-read'] = '[open open][setattr getattr]'
G.add_edge('cbd','installd')
G.edge['cbd']['installd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('cbd','itsonbs')
G.edge['cbd']['itsonbs']['write-read'] = '[open open][setattr getattr]'
G.add_edge('cbd','logwrapper')
G.edge['cbd']['logwrapper']['write-read'] = '[open open][setattr getattr]'
G.add_edge('cbd','netd')
G.edge['cbd']['netd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('cbd','qmuxd')
G.edge['cbd']['qmuxd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('cbd','rild')
G.edge['cbd']['rild']['write-read'] = '[open open][setattr getattr]'
G.add_edge('cbd','rmt_storage')
G.edge['cbd']['rmt_storage']['write-read'] = '[open open][setattr getattr]'
G.add_edge('cbd','sdcardd')
G.edge['cbd']['sdcardd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('cbd','shell')
G.edge['cbd']['shell']['write-read'] = '[open open][setattr getattr]'
G.add_edge('cbd','s_system_app')
G.edge['cbd']['s_system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('cbd','system_app')
G.edge['cbd']['system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('cbd','system_server')
G.edge['cbd']['system_server']['write-read'] = '[open open][setattr getattr]'
G.add_edge('cbd','vmwared')
G.edge['cbd']['vmwared']['write-read'] = '[open open][setattr getattr]'
G.add_edge('cbd','wpa')
G.edge['cbd']['wpa']['write-read'] = '[open open][setattr getattr]'
G.add_edge('cbd','zygote')
G.edge['cbd']['zygote']['write-read'] = '[open open][setattr getattr]'
G.add_edge('cbd','adbd')
G.edge['cbd']['adbd']['write-read'] = '[write read]'
G.edge['cbd']['adbd']['fill'] = 'red'
G.add_edge('cbd','at_distributor')
G.edge['cbd']['at_distributor']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['cbd']['at_distributor']['fill'] = 'red'
G.add_edge('cbd','cbd')
G.edge['cbd']['cbd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['cbd']['cbd']['fill'] = 'red'
G.add_edge('cbd','charon')
G.edge['cbd']['charon']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['cbd']['charon']['fill'] = 'red'
G.add_edge('cbd','debuggerd')
G.edge['cbd']['debuggerd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['cbd']['debuggerd']['fill'] = 'red'
G.add_edge('cbd','dhcp')
G.edge['cbd']['dhcp']['write-read'] = '[write read]'
G.edge['cbd']['dhcp']['fill'] = 'red'
G.add_edge('cbd','diag_uart_log')
G.edge['cbd']['diag_uart_log']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['cbd']['diag_uart_log']['fill'] = 'red'
G.add_edge('cbd','domain')
G.edge['cbd']['domain']['write-read'] = '[write read]'
G.edge['cbd']['domain']['fill'] = 'red'
G.add_edge('cbd','dumpstate')
G.edge['cbd']['dumpstate']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['cbd']['dumpstate']['fill'] = 'red'
G.add_edge('cbd','hostapd')
G.edge['cbd']['hostapd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['cbd']['hostapd']['fill'] = 'red'
G.add_edge('cbd','ime_app')
G.edge['cbd']['ime_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['cbd']['ime_app']['fill'] = 'red'
G.add_edge('cbd','init_shell')
G.edge['cbd']['init_shell']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['cbd']['init_shell']['fill'] = 'red'
G.add_edge('cbd','installd')
G.edge['cbd']['installd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['cbd']['installd']['fill'] = 'red'
G.add_edge('cbd','itsonbs')
G.edge['cbd']['itsonbs']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['cbd']['itsonbs']['fill'] = 'red'
G.add_edge('cbd','logwrapper')
G.edge['cbd']['logwrapper']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['cbd']['logwrapper']['fill'] = 'red'
G.add_edge('cbd','netd')
G.edge['cbd']['netd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['cbd']['netd']['fill'] = 'red'
G.add_edge('cbd','qmuxd')
G.edge['cbd']['qmuxd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['cbd']['qmuxd']['fill'] = 'red'
G.add_edge('cbd','rild')
G.edge['cbd']['rild']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['cbd']['rild']['fill'] = 'red'
G.add_edge('cbd','rmt_storage')
G.edge['cbd']['rmt_storage']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['cbd']['rmt_storage']['fill'] = 'red'
G.add_edge('cbd','sdcardd')
G.edge['cbd']['sdcardd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['cbd']['sdcardd']['fill'] = 'red'
G.add_edge('cbd','shell')
G.edge['cbd']['shell']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['cbd']['shell']['fill'] = 'red'
G.add_edge('cbd','s_system_app')
G.edge['cbd']['s_system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['cbd']['s_system_app']['fill'] = 'red'
G.add_edge('cbd','system_app')
G.edge['cbd']['system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['cbd']['system_app']['fill'] = 'red'
G.add_edge('cbd','system_server')
G.edge['cbd']['system_server']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['cbd']['system_server']['fill'] = 'red'
G.add_edge('cbd','vmwared')
G.edge['cbd']['vmwared']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['cbd']['vmwared']['fill'] = 'red'
G.add_edge('cbd','wpa')
G.edge['cbd']['wpa']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['cbd']['wpa']['fill'] = 'red'
G.add_edge('cbd','zygote')
G.edge['cbd']['zygote']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['cbd']['zygote']['fill'] = 'red'
G.add_edge('cbd','adbd')
G.edge['cbd']['adbd']['write-read'] = '[write read][add_name search]'
G.add_edge('cbd','at_distributor')
G.edge['cbd']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('cbd','at_distributor')
G.edge['cbd']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('cbd','auditd')
G.edge['cbd']['auditd']['write-read'] = '[add_name search]'
G.add_edge('cbd','cbd')
G.edge['cbd']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('cbd','cbd')
G.edge['cbd']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('cbd','charon')
G.edge['cbd']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('cbd','charon')
G.edge['cbd']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('cbd','clatd')
G.edge['cbd']['clatd']['write-read'] = '[add_name search]'
G.add_edge('cbd','debuggerd')
G.edge['cbd']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('cbd','debuggerd')
G.edge['cbd']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('cbd','dhcp')
G.edge['cbd']['dhcp']['write-read'] = '[write read][add_name search]'
G.add_edge('cbd','diag_uart_log')
G.edge['cbd']['diag_uart_log']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('cbd','diag_uart_log')
G.edge['cbd']['diag_uart_log']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('cbd','dumpstate')
G.edge['cbd']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('cbd','dumpstate')
G.edge['cbd']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('cbd','hostapd')
G.edge['cbd']['hostapd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('cbd','hostapd')
G.edge['cbd']['hostapd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('cbd','hvdcp')
G.edge['cbd']['hvdcp']['write-read'] = '[add_name search]'
G.add_edge('cbd','ime_app')
G.edge['cbd']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('cbd','ime_app')
G.edge['cbd']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('cbd','init_shell')
G.edge['cbd']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('cbd','init_shell')
G.edge['cbd']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('cbd','installd')
G.edge['cbd']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('cbd','installd')
G.edge['cbd']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('cbd','itsonbs')
G.edge['cbd']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('cbd','itsonbs')
G.edge['cbd']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('cbd','jackservice')
G.edge['cbd']['jackservice']['write-read'] = '[add_name search]'
G.add_edge('cbd','lmkd')
G.edge['cbd']['lmkd']['write-read'] = '[remove_name search]'
G.add_edge('cbd','logwrapper')
G.edge['cbd']['logwrapper']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('cbd','logwrapper')
G.edge['cbd']['logwrapper']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('cbd','msm_irqbalanced')
G.edge['cbd']['msm_irqbalanced']['write-read'] = '[add_name search]'
G.add_edge('cbd','netd')
G.edge['cbd']['netd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('cbd','netd')
G.edge['cbd']['netd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('cbd','qmuxd')
G.edge['cbd']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('cbd','qmuxd')
G.edge['cbd']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('cbd','racoon')
G.edge['cbd']['racoon']['write-read'] = '[add_name search]'
G.add_edge('cbd','rild')
G.edge['cbd']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('cbd','rild')
G.edge['cbd']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('cbd','rmt_storage')
G.edge['cbd']['rmt_storage']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('cbd','rmt_storage')
G.edge['cbd']['rmt_storage']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('cbd','sdcardd')
G.edge['cbd']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('cbd','sdcardd')
G.edge['cbd']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('cbd','sensors')
G.edge['cbd']['sensors']['write-read'] = '[add_name search]'
G.add_edge('cbd','shell')
G.edge['cbd']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('cbd','shell')
G.edge['cbd']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('cbd','s_system_app')
G.edge['cbd']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('cbd','s_system_app')
G.edge['cbd']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('cbd','system_app')
G.edge['cbd']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('cbd','system_app')
G.edge['cbd']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('cbd','system_server')
G.edge['cbd']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('cbd','system_server')
G.edge['cbd']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('cbd','system_server')
G.edge['cbd']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search]'
G.add_edge('cbd','vmwared')
G.edge['cbd']['vmwared']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('cbd','vmwared')
G.edge['cbd']['vmwared']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('cbd','wpa')
G.edge['cbd']['wpa']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('cbd','wpa')
G.edge['cbd']['wpa']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('cbd','zygote')
G.edge['cbd']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('cbd','zygote')
G.edge['cbd']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('charon','at_distributor')
G.edge['charon']['at_distributor']['write-read'] = '[open open]'
G.add_edge('charon','cbd')
G.edge['charon']['cbd']['write-read'] = '[open open]'
G.add_edge('charon','charon')
G.edge['charon']['charon']['write-read'] = '[open open]'
G.add_edge('charon','debuggerd')
G.edge['charon']['debuggerd']['write-read'] = '[open open]'
G.add_edge('charon','diag_uart_log')
G.edge['charon']['diag_uart_log']['write-read'] = '[open open]'
G.add_edge('charon','dumpstate')
G.edge['charon']['dumpstate']['write-read'] = '[open open]'
G.add_edge('charon','hostapd')
G.edge['charon']['hostapd']['write-read'] = '[open open]'
G.add_edge('charon','ime_app')
G.edge['charon']['ime_app']['write-read'] = '[open open]'
G.add_edge('charon','init_shell')
G.edge['charon']['init_shell']['write-read'] = '[open open]'
G.add_edge('charon','installd')
G.edge['charon']['installd']['write-read'] = '[open open]'
G.add_edge('charon','itsonbs')
G.edge['charon']['itsonbs']['write-read'] = '[open open]'
G.add_edge('charon','logwrapper')
G.edge['charon']['logwrapper']['write-read'] = '[open open]'
G.add_edge('charon','netd')
G.edge['charon']['netd']['write-read'] = '[open open]'
G.add_edge('charon','qmuxd')
G.edge['charon']['qmuxd']['write-read'] = '[open open]'
G.add_edge('charon','rild')
G.edge['charon']['rild']['write-read'] = '[open open]'
G.add_edge('charon','rmt_storage')
G.edge['charon']['rmt_storage']['write-read'] = '[open open]'
G.add_edge('charon','sdcardd')
G.edge['charon']['sdcardd']['write-read'] = '[open open]'
G.add_edge('charon','shell')
G.edge['charon']['shell']['write-read'] = '[open open]'
G.add_edge('charon','s_system_app')
G.edge['charon']['s_system_app']['write-read'] = '[open open]'
G.add_edge('charon','system_app')
G.edge['charon']['system_app']['write-read'] = '[open open]'
G.add_edge('charon','system_server')
G.edge['charon']['system_server']['write-read'] = '[open open]'
G.add_edge('charon','vmwared')
G.edge['charon']['vmwared']['write-read'] = '[open open]'
G.add_edge('charon','wpa')
G.edge['charon']['wpa']['write-read'] = '[open open]'
G.add_edge('charon','zygote')
G.edge['charon']['zygote']['write-read'] = '[open open]'
G.add_edge('charon','at_distributor')
G.edge['charon']['at_distributor']['write-read'] = '[open open][setattr getattr]'
G.add_edge('charon','cbd')
G.edge['charon']['cbd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('charon','charon')
G.edge['charon']['charon']['write-read'] = '[open open][setattr getattr]'
G.add_edge('charon','debuggerd')
G.edge['charon']['debuggerd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('charon','diag_uart_log')
G.edge['charon']['diag_uart_log']['write-read'] = '[open open][setattr getattr]'
G.add_edge('charon','dumpstate')
G.edge['charon']['dumpstate']['write-read'] = '[open open][setattr getattr]'
G.add_edge('charon','hostapd')
G.edge['charon']['hostapd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('charon','ime_app')
G.edge['charon']['ime_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('charon','init_shell')
G.edge['charon']['init_shell']['write-read'] = '[open open][setattr getattr]'
G.add_edge('charon','installd')
G.edge['charon']['installd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('charon','itsonbs')
G.edge['charon']['itsonbs']['write-read'] = '[open open][setattr getattr]'
G.add_edge('charon','logwrapper')
G.edge['charon']['logwrapper']['write-read'] = '[open open][setattr getattr]'
G.add_edge('charon','netd')
G.edge['charon']['netd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('charon','qmuxd')
G.edge['charon']['qmuxd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('charon','rild')
G.edge['charon']['rild']['write-read'] = '[open open][setattr getattr]'
G.add_edge('charon','rmt_storage')
G.edge['charon']['rmt_storage']['write-read'] = '[open open][setattr getattr]'
G.add_edge('charon','sdcardd')
G.edge['charon']['sdcardd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('charon','shell')
G.edge['charon']['shell']['write-read'] = '[open open][setattr getattr]'
G.add_edge('charon','s_system_app')
G.edge['charon']['s_system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('charon','system_app')
G.edge['charon']['system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('charon','system_server')
G.edge['charon']['system_server']['write-read'] = '[open open][setattr getattr]'
G.add_edge('charon','vmwared')
G.edge['charon']['vmwared']['write-read'] = '[open open][setattr getattr]'
G.add_edge('charon','wpa')
G.edge['charon']['wpa']['write-read'] = '[open open][setattr getattr]'
G.add_edge('charon','zygote')
G.edge['charon']['zygote']['write-read'] = '[open open][setattr getattr]'
G.add_edge('charon','adbd')
G.edge['charon']['adbd']['write-read'] = '[write read]'
G.edge['charon']['adbd']['fill'] = 'red'
G.add_edge('charon','at_distributor')
G.edge['charon']['at_distributor']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['charon']['at_distributor']['fill'] = 'red'
G.add_edge('charon','cbd')
G.edge['charon']['cbd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['charon']['cbd']['fill'] = 'red'
G.add_edge('charon','charon')
G.edge['charon']['charon']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['charon']['charon']['fill'] = 'red'
G.add_edge('charon','debuggerd')
G.edge['charon']['debuggerd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['charon']['debuggerd']['fill'] = 'red'
G.add_edge('charon','dhcp')
G.edge['charon']['dhcp']['write-read'] = '[write read]'
G.edge['charon']['dhcp']['fill'] = 'red'
G.add_edge('charon','diag_uart_log')
G.edge['charon']['diag_uart_log']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['charon']['diag_uart_log']['fill'] = 'red'
G.add_edge('charon','domain')
G.edge['charon']['domain']['write-read'] = '[write read]'
G.edge['charon']['domain']['fill'] = 'red'
G.add_edge('charon','dumpstate')
G.edge['charon']['dumpstate']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['charon']['dumpstate']['fill'] = 'red'
G.add_edge('charon','hostapd')
G.edge['charon']['hostapd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['charon']['hostapd']['fill'] = 'red'
G.add_edge('charon','ime_app')
G.edge['charon']['ime_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['charon']['ime_app']['fill'] = 'red'
G.add_edge('charon','init_shell')
G.edge['charon']['init_shell']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['charon']['init_shell']['fill'] = 'red'
G.add_edge('charon','installd')
G.edge['charon']['installd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['charon']['installd']['fill'] = 'red'
G.add_edge('charon','itsonbs')
G.edge['charon']['itsonbs']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['charon']['itsonbs']['fill'] = 'red'
G.add_edge('charon','logwrapper')
G.edge['charon']['logwrapper']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['charon']['logwrapper']['fill'] = 'red'
G.add_edge('charon','netd')
G.edge['charon']['netd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['charon']['netd']['fill'] = 'red'
G.add_edge('charon','qmuxd')
G.edge['charon']['qmuxd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['charon']['qmuxd']['fill'] = 'red'
G.add_edge('charon','rild')
G.edge['charon']['rild']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['charon']['rild']['fill'] = 'red'
G.add_edge('charon','rmt_storage')
G.edge['charon']['rmt_storage']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['charon']['rmt_storage']['fill'] = 'red'
G.add_edge('charon','sdcardd')
G.edge['charon']['sdcardd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['charon']['sdcardd']['fill'] = 'red'
G.add_edge('charon','shell')
G.edge['charon']['shell']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['charon']['shell']['fill'] = 'red'
G.add_edge('charon','s_system_app')
G.edge['charon']['s_system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['charon']['s_system_app']['fill'] = 'red'
G.add_edge('charon','system_app')
G.edge['charon']['system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['charon']['system_app']['fill'] = 'red'
G.add_edge('charon','system_server')
G.edge['charon']['system_server']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['charon']['system_server']['fill'] = 'red'
G.add_edge('charon','vmwared')
G.edge['charon']['vmwared']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['charon']['vmwared']['fill'] = 'red'
G.add_edge('charon','wpa')
G.edge['charon']['wpa']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['charon']['wpa']['fill'] = 'red'
G.add_edge('charon','zygote')
G.edge['charon']['zygote']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['charon']['zygote']['fill'] = 'red'
G.add_edge('charon','adbd')
G.edge['charon']['adbd']['write-read'] = '[write read][add_name search]'
G.add_edge('charon','at_distributor')
G.edge['charon']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('charon','at_distributor')
G.edge['charon']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('charon','auditd')
G.edge['charon']['auditd']['write-read'] = '[add_name search]'
G.add_edge('charon','cbd')
G.edge['charon']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('charon','cbd')
G.edge['charon']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('charon','charon')
G.edge['charon']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('charon','charon')
G.edge['charon']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('charon','clatd')
G.edge['charon']['clatd']['write-read'] = '[add_name search]'
G.add_edge('charon','debuggerd')
G.edge['charon']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('charon','debuggerd')
G.edge['charon']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('charon','dhcp')
G.edge['charon']['dhcp']['write-read'] = '[write read][add_name search]'
G.add_edge('charon','diag_uart_log')
G.edge['charon']['diag_uart_log']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('charon','diag_uart_log')
G.edge['charon']['diag_uart_log']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('charon','dumpstate')
G.edge['charon']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('charon','dumpstate')
G.edge['charon']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('charon','hostapd')
G.edge['charon']['hostapd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('charon','hostapd')
G.edge['charon']['hostapd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('charon','hvdcp')
G.edge['charon']['hvdcp']['write-read'] = '[add_name search]'
G.add_edge('charon','ime_app')
G.edge['charon']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('charon','ime_app')
G.edge['charon']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('charon','init_shell')
G.edge['charon']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('charon','init_shell')
G.edge['charon']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('charon','installd')
G.edge['charon']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('charon','installd')
G.edge['charon']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('charon','itsonbs')
G.edge['charon']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('charon','itsonbs')
G.edge['charon']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('charon','jackservice')
G.edge['charon']['jackservice']['write-read'] = '[add_name search]'
G.add_edge('charon','lmkd')
G.edge['charon']['lmkd']['write-read'] = '[remove_name search]'
G.add_edge('charon','logwrapper')
G.edge['charon']['logwrapper']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('charon','logwrapper')
G.edge['charon']['logwrapper']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('charon','msm_irqbalanced')
G.edge['charon']['msm_irqbalanced']['write-read'] = '[add_name search]'
G.add_edge('charon','netd')
G.edge['charon']['netd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('charon','netd')
G.edge['charon']['netd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('charon','qmuxd')
G.edge['charon']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('charon','qmuxd')
G.edge['charon']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('charon','racoon')
G.edge['charon']['racoon']['write-read'] = '[add_name search]'
G.add_edge('charon','rild')
G.edge['charon']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('charon','rild')
G.edge['charon']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('charon','rmt_storage')
G.edge['charon']['rmt_storage']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('charon','rmt_storage')
G.edge['charon']['rmt_storage']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('charon','sdcardd')
G.edge['charon']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('charon','sdcardd')
G.edge['charon']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('charon','sensors')
G.edge['charon']['sensors']['write-read'] = '[add_name search]'
G.add_edge('charon','shell')
G.edge['charon']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('charon','shell')
G.edge['charon']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('charon','s_system_app')
G.edge['charon']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('charon','s_system_app')
G.edge['charon']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('charon','system_app')
G.edge['charon']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('charon','system_app')
G.edge['charon']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('charon','system_server')
G.edge['charon']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('charon','system_server')
G.edge['charon']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('charon','system_server')
G.edge['charon']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search]'
G.add_edge('charon','vmwared')
G.edge['charon']['vmwared']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('charon','vmwared')
G.edge['charon']['vmwared']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('charon','wpa')
G.edge['charon']['wpa']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('charon','wpa')
G.edge['charon']['wpa']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('charon','zygote')
G.edge['charon']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('charon','zygote')
G.edge['charon']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('debuggerd','at_distributor')
G.edge['debuggerd']['at_distributor']['write-read'] = '[open open]'
G.add_edge('debuggerd','cbd')
G.edge['debuggerd']['cbd']['write-read'] = '[open open]'
G.add_edge('debuggerd','charon')
G.edge['debuggerd']['charon']['write-read'] = '[open open]'
G.add_edge('debuggerd','debuggerd')
G.edge['debuggerd']['debuggerd']['write-read'] = '[open open]'
G.add_edge('debuggerd','diag_uart_log')
G.edge['debuggerd']['diag_uart_log']['write-read'] = '[open open]'
G.add_edge('debuggerd','dumpstate')
G.edge['debuggerd']['dumpstate']['write-read'] = '[open open]'
G.add_edge('debuggerd','hostapd')
G.edge['debuggerd']['hostapd']['write-read'] = '[open open]'
G.add_edge('debuggerd','ime_app')
G.edge['debuggerd']['ime_app']['write-read'] = '[open open]'
G.add_edge('debuggerd','init_shell')
G.edge['debuggerd']['init_shell']['write-read'] = '[open open]'
G.add_edge('debuggerd','installd')
G.edge['debuggerd']['installd']['write-read'] = '[open open]'
G.add_edge('debuggerd','itsonbs')
G.edge['debuggerd']['itsonbs']['write-read'] = '[open open]'
G.add_edge('debuggerd','logwrapper')
G.edge['debuggerd']['logwrapper']['write-read'] = '[open open]'
G.add_edge('debuggerd','netd')
G.edge['debuggerd']['netd']['write-read'] = '[open open]'
G.add_edge('debuggerd','qmuxd')
G.edge['debuggerd']['qmuxd']['write-read'] = '[open open]'
G.add_edge('debuggerd','rild')
G.edge['debuggerd']['rild']['write-read'] = '[open open]'
G.add_edge('debuggerd','rmt_storage')
G.edge['debuggerd']['rmt_storage']['write-read'] = '[open open]'
G.add_edge('debuggerd','sdcardd')
G.edge['debuggerd']['sdcardd']['write-read'] = '[open open]'
G.add_edge('debuggerd','shell')
G.edge['debuggerd']['shell']['write-read'] = '[open open]'
G.add_edge('debuggerd','s_system_app')
G.edge['debuggerd']['s_system_app']['write-read'] = '[open open]'
G.add_edge('debuggerd','system_app')
G.edge['debuggerd']['system_app']['write-read'] = '[open open]'
G.add_edge('debuggerd','system_server')
G.edge['debuggerd']['system_server']['write-read'] = '[open open]'
G.add_edge('debuggerd','vmwared')
G.edge['debuggerd']['vmwared']['write-read'] = '[open open]'
G.add_edge('debuggerd','wpa')
G.edge['debuggerd']['wpa']['write-read'] = '[open open]'
G.add_edge('debuggerd','zygote')
G.edge['debuggerd']['zygote']['write-read'] = '[open open]'
G.add_edge('debuggerd','at_distributor')
G.edge['debuggerd']['at_distributor']['write-read'] = '[open open][setattr getattr]'
G.add_edge('debuggerd','cbd')
G.edge['debuggerd']['cbd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('debuggerd','charon')
G.edge['debuggerd']['charon']['write-read'] = '[open open][setattr getattr]'
G.add_edge('debuggerd','debuggerd')
G.edge['debuggerd']['debuggerd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('debuggerd','diag_uart_log')
G.edge['debuggerd']['diag_uart_log']['write-read'] = '[open open][setattr getattr]'
G.add_edge('debuggerd','dumpstate')
G.edge['debuggerd']['dumpstate']['write-read'] = '[open open][setattr getattr]'
G.add_edge('debuggerd','hostapd')
G.edge['debuggerd']['hostapd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('debuggerd','ime_app')
G.edge['debuggerd']['ime_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('debuggerd','init_shell')
G.edge['debuggerd']['init_shell']['write-read'] = '[open open][setattr getattr]'
G.add_edge('debuggerd','installd')
G.edge['debuggerd']['installd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('debuggerd','itsonbs')
G.edge['debuggerd']['itsonbs']['write-read'] = '[open open][setattr getattr]'
G.add_edge('debuggerd','logwrapper')
G.edge['debuggerd']['logwrapper']['write-read'] = '[open open][setattr getattr]'
G.add_edge('debuggerd','netd')
G.edge['debuggerd']['netd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('debuggerd','qmuxd')
G.edge['debuggerd']['qmuxd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('debuggerd','rild')
G.edge['debuggerd']['rild']['write-read'] = '[open open][setattr getattr]'
G.add_edge('debuggerd','rmt_storage')
G.edge['debuggerd']['rmt_storage']['write-read'] = '[open open][setattr getattr]'
G.add_edge('debuggerd','sdcardd')
G.edge['debuggerd']['sdcardd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('debuggerd','shell')
G.edge['debuggerd']['shell']['write-read'] = '[open open][setattr getattr]'
G.add_edge('debuggerd','s_system_app')
G.edge['debuggerd']['s_system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('debuggerd','system_app')
G.edge['debuggerd']['system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('debuggerd','system_server')
G.edge['debuggerd']['system_server']['write-read'] = '[open open][setattr getattr]'
G.add_edge('debuggerd','vmwared')
G.edge['debuggerd']['vmwared']['write-read'] = '[open open][setattr getattr]'
G.add_edge('debuggerd','wpa')
G.edge['debuggerd']['wpa']['write-read'] = '[open open][setattr getattr]'
G.add_edge('debuggerd','zygote')
G.edge['debuggerd']['zygote']['write-read'] = '[open open][setattr getattr]'
G.add_edge('debuggerd','adbd')
G.edge['debuggerd']['adbd']['write-read'] = '[write read]'
G.edge['debuggerd']['adbd']['fill'] = 'red'
G.add_edge('debuggerd','at_distributor')
G.edge['debuggerd']['at_distributor']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['debuggerd']['at_distributor']['fill'] = 'red'
G.add_edge('debuggerd','cbd')
G.edge['debuggerd']['cbd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['debuggerd']['cbd']['fill'] = 'red'
G.add_edge('debuggerd','charon')
G.edge['debuggerd']['charon']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['debuggerd']['charon']['fill'] = 'red'
G.add_edge('debuggerd','debuggerd')
G.edge['debuggerd']['debuggerd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['debuggerd']['debuggerd']['fill'] = 'red'
G.add_edge('debuggerd','dhcp')
G.edge['debuggerd']['dhcp']['write-read'] = '[write read]'
G.edge['debuggerd']['dhcp']['fill'] = 'red'
G.add_edge('debuggerd','diag_uart_log')
G.edge['debuggerd']['diag_uart_log']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['debuggerd']['diag_uart_log']['fill'] = 'red'
G.add_edge('debuggerd','domain')
G.edge['debuggerd']['domain']['write-read'] = '[write read]'
G.edge['debuggerd']['domain']['fill'] = 'red'
G.add_edge('debuggerd','dumpstate')
G.edge['debuggerd']['dumpstate']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['debuggerd']['dumpstate']['fill'] = 'red'
G.add_edge('debuggerd','hostapd')
G.edge['debuggerd']['hostapd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['debuggerd']['hostapd']['fill'] = 'red'
G.add_edge('debuggerd','ime_app')
G.edge['debuggerd']['ime_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['debuggerd']['ime_app']['fill'] = 'red'
G.add_edge('debuggerd','init_shell')
G.edge['debuggerd']['init_shell']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['debuggerd']['init_shell']['fill'] = 'red'
G.add_edge('debuggerd','installd')
G.edge['debuggerd']['installd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['debuggerd']['installd']['fill'] = 'red'
G.add_edge('debuggerd','itsonbs')
G.edge['debuggerd']['itsonbs']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['debuggerd']['itsonbs']['fill'] = 'red'
G.add_edge('debuggerd','logwrapper')
G.edge['debuggerd']['logwrapper']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['debuggerd']['logwrapper']['fill'] = 'red'
G.add_edge('debuggerd','netd')
G.edge['debuggerd']['netd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['debuggerd']['netd']['fill'] = 'red'
G.add_edge('debuggerd','qmuxd')
G.edge['debuggerd']['qmuxd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['debuggerd']['qmuxd']['fill'] = 'red'
G.add_edge('debuggerd','rild')
G.edge['debuggerd']['rild']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['debuggerd']['rild']['fill'] = 'red'
G.add_edge('debuggerd','rmt_storage')
G.edge['debuggerd']['rmt_storage']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['debuggerd']['rmt_storage']['fill'] = 'red'
G.add_edge('debuggerd','sdcardd')
G.edge['debuggerd']['sdcardd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['debuggerd']['sdcardd']['fill'] = 'red'
G.add_edge('debuggerd','shell')
G.edge['debuggerd']['shell']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['debuggerd']['shell']['fill'] = 'red'
G.add_edge('debuggerd','s_system_app')
G.edge['debuggerd']['s_system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['debuggerd']['s_system_app']['fill'] = 'red'
G.add_edge('debuggerd','system_app')
G.edge['debuggerd']['system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['debuggerd']['system_app']['fill'] = 'red'
G.add_edge('debuggerd','system_server')
G.edge['debuggerd']['system_server']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['debuggerd']['system_server']['fill'] = 'red'
G.add_edge('debuggerd','vmwared')
G.edge['debuggerd']['vmwared']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['debuggerd']['vmwared']['fill'] = 'red'
G.add_edge('debuggerd','wpa')
G.edge['debuggerd']['wpa']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['debuggerd']['wpa']['fill'] = 'red'
G.add_edge('debuggerd','zygote')
G.edge['debuggerd']['zygote']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['debuggerd']['zygote']['fill'] = 'red'
G.add_edge('debuggerd','adbd')
G.edge['debuggerd']['adbd']['write-read'] = '[write read][add_name search]'
G.add_edge('debuggerd','at_distributor')
G.edge['debuggerd']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('debuggerd','at_distributor')
G.edge['debuggerd']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('debuggerd','auditd')
G.edge['debuggerd']['auditd']['write-read'] = '[add_name search]'
G.add_edge('debuggerd','cbd')
G.edge['debuggerd']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('debuggerd','cbd')
G.edge['debuggerd']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('debuggerd','charon')
G.edge['debuggerd']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('debuggerd','charon')
G.edge['debuggerd']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('debuggerd','clatd')
G.edge['debuggerd']['clatd']['write-read'] = '[add_name search]'
G.add_edge('debuggerd','debuggerd')
G.edge['debuggerd']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('debuggerd','debuggerd')
G.edge['debuggerd']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('debuggerd','dhcp')
G.edge['debuggerd']['dhcp']['write-read'] = '[write read][add_name search]'
G.add_edge('debuggerd','diag_uart_log')
G.edge['debuggerd']['diag_uart_log']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('debuggerd','diag_uart_log')
G.edge['debuggerd']['diag_uart_log']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('debuggerd','dumpstate')
G.edge['debuggerd']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('debuggerd','dumpstate')
G.edge['debuggerd']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('debuggerd','hostapd')
G.edge['debuggerd']['hostapd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('debuggerd','hostapd')
G.edge['debuggerd']['hostapd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('debuggerd','hvdcp')
G.edge['debuggerd']['hvdcp']['write-read'] = '[add_name search]'
G.add_edge('debuggerd','ime_app')
G.edge['debuggerd']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('debuggerd','ime_app')
G.edge['debuggerd']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('debuggerd','init_shell')
G.edge['debuggerd']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('debuggerd','init_shell')
G.edge['debuggerd']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('debuggerd','installd')
G.edge['debuggerd']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('debuggerd','installd')
G.edge['debuggerd']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('debuggerd','itsonbs')
G.edge['debuggerd']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('debuggerd','itsonbs')
G.edge['debuggerd']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('debuggerd','jackservice')
G.edge['debuggerd']['jackservice']['write-read'] = '[add_name search]'
G.add_edge('debuggerd','lmkd')
G.edge['debuggerd']['lmkd']['write-read'] = '[remove_name search]'
G.add_edge('debuggerd','logwrapper')
G.edge['debuggerd']['logwrapper']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('debuggerd','logwrapper')
G.edge['debuggerd']['logwrapper']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('debuggerd','msm_irqbalanced')
G.edge['debuggerd']['msm_irqbalanced']['write-read'] = '[add_name search]'
G.add_edge('debuggerd','netd')
G.edge['debuggerd']['netd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('debuggerd','netd')
G.edge['debuggerd']['netd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('debuggerd','qmuxd')
G.edge['debuggerd']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('debuggerd','qmuxd')
G.edge['debuggerd']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('debuggerd','racoon')
G.edge['debuggerd']['racoon']['write-read'] = '[add_name search]'
G.add_edge('debuggerd','rild')
G.edge['debuggerd']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('debuggerd','rild')
G.edge['debuggerd']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('debuggerd','rmt_storage')
G.edge['debuggerd']['rmt_storage']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('debuggerd','rmt_storage')
G.edge['debuggerd']['rmt_storage']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('debuggerd','sdcardd')
G.edge['debuggerd']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('debuggerd','sdcardd')
G.edge['debuggerd']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('debuggerd','sensors')
G.edge['debuggerd']['sensors']['write-read'] = '[add_name search]'
G.add_edge('debuggerd','shell')
G.edge['debuggerd']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('debuggerd','shell')
G.edge['debuggerd']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('debuggerd','s_system_app')
G.edge['debuggerd']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('debuggerd','s_system_app')
G.edge['debuggerd']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('debuggerd','system_app')
G.edge['debuggerd']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('debuggerd','system_app')
G.edge['debuggerd']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('debuggerd','system_server')
G.edge['debuggerd']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('debuggerd','system_server')
G.edge['debuggerd']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('debuggerd','system_server')
G.edge['debuggerd']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search]'
G.add_edge('debuggerd','vmwared')
G.edge['debuggerd']['vmwared']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('debuggerd','vmwared')
G.edge['debuggerd']['vmwared']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('debuggerd','wpa')
G.edge['debuggerd']['wpa']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('debuggerd','wpa')
G.edge['debuggerd']['wpa']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('debuggerd','zygote')
G.edge['debuggerd']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('debuggerd','zygote')
G.edge['debuggerd']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('diag_uart_log','at_distributor')
G.edge['diag_uart_log']['at_distributor']['write-read'] = '[open open]'
G.add_edge('diag_uart_log','cbd')
G.edge['diag_uart_log']['cbd']['write-read'] = '[open open]'
G.add_edge('diag_uart_log','charon')
G.edge['diag_uart_log']['charon']['write-read'] = '[open open]'
G.add_edge('diag_uart_log','debuggerd')
G.edge['diag_uart_log']['debuggerd']['write-read'] = '[open open]'
G.add_edge('diag_uart_log','diag_uart_log')
G.edge['diag_uart_log']['diag_uart_log']['write-read'] = '[open open]'
G.add_edge('diag_uart_log','dumpstate')
G.edge['diag_uart_log']['dumpstate']['write-read'] = '[open open]'
G.add_edge('diag_uart_log','hostapd')
G.edge['diag_uart_log']['hostapd']['write-read'] = '[open open]'
G.add_edge('diag_uart_log','ime_app')
G.edge['diag_uart_log']['ime_app']['write-read'] = '[open open]'
G.add_edge('diag_uart_log','init_shell')
G.edge['diag_uart_log']['init_shell']['write-read'] = '[open open]'
G.add_edge('diag_uart_log','installd')
G.edge['diag_uart_log']['installd']['write-read'] = '[open open]'
G.add_edge('diag_uart_log','itsonbs')
G.edge['diag_uart_log']['itsonbs']['write-read'] = '[open open]'
G.add_edge('diag_uart_log','logwrapper')
G.edge['diag_uart_log']['logwrapper']['write-read'] = '[open open]'
G.add_edge('diag_uart_log','netd')
G.edge['diag_uart_log']['netd']['write-read'] = '[open open]'
G.add_edge('diag_uart_log','qmuxd')
G.edge['diag_uart_log']['qmuxd']['write-read'] = '[open open]'
G.add_edge('diag_uart_log','rild')
G.edge['diag_uart_log']['rild']['write-read'] = '[open open]'
G.add_edge('diag_uart_log','rmt_storage')
G.edge['diag_uart_log']['rmt_storage']['write-read'] = '[open open]'
G.add_edge('diag_uart_log','sdcardd')
G.edge['diag_uart_log']['sdcardd']['write-read'] = '[open open]'
G.add_edge('diag_uart_log','shell')
G.edge['diag_uart_log']['shell']['write-read'] = '[open open]'
G.add_edge('diag_uart_log','s_system_app')
G.edge['diag_uart_log']['s_system_app']['write-read'] = '[open open]'
G.add_edge('diag_uart_log','system_app')
G.edge['diag_uart_log']['system_app']['write-read'] = '[open open]'
G.add_edge('diag_uart_log','system_server')
G.edge['diag_uart_log']['system_server']['write-read'] = '[open open]'
G.add_edge('diag_uart_log','vmwared')
G.edge['diag_uart_log']['vmwared']['write-read'] = '[open open]'
G.add_edge('diag_uart_log','wpa')
G.edge['diag_uart_log']['wpa']['write-read'] = '[open open]'
G.add_edge('diag_uart_log','zygote')
G.edge['diag_uart_log']['zygote']['write-read'] = '[open open]'
G.add_edge('diag_uart_log','at_distributor')
G.edge['diag_uart_log']['at_distributor']['write-read'] = '[open open][setattr getattr]'
G.add_edge('diag_uart_log','cbd')
G.edge['diag_uart_log']['cbd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('diag_uart_log','charon')
G.edge['diag_uart_log']['charon']['write-read'] = '[open open][setattr getattr]'
G.add_edge('diag_uart_log','debuggerd')
G.edge['diag_uart_log']['debuggerd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('diag_uart_log','diag_uart_log')
G.edge['diag_uart_log']['diag_uart_log']['write-read'] = '[open open][setattr getattr]'
G.add_edge('diag_uart_log','dumpstate')
G.edge['diag_uart_log']['dumpstate']['write-read'] = '[open open][setattr getattr]'
G.add_edge('diag_uart_log','hostapd')
G.edge['diag_uart_log']['hostapd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('diag_uart_log','ime_app')
G.edge['diag_uart_log']['ime_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('diag_uart_log','init_shell')
G.edge['diag_uart_log']['init_shell']['write-read'] = '[open open][setattr getattr]'
G.add_edge('diag_uart_log','installd')
G.edge['diag_uart_log']['installd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('diag_uart_log','itsonbs')
G.edge['diag_uart_log']['itsonbs']['write-read'] = '[open open][setattr getattr]'
G.add_edge('diag_uart_log','logwrapper')
G.edge['diag_uart_log']['logwrapper']['write-read'] = '[open open][setattr getattr]'
G.add_edge('diag_uart_log','netd')
G.edge['diag_uart_log']['netd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('diag_uart_log','qmuxd')
G.edge['diag_uart_log']['qmuxd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('diag_uart_log','rild')
G.edge['diag_uart_log']['rild']['write-read'] = '[open open][setattr getattr]'
G.add_edge('diag_uart_log','rmt_storage')
G.edge['diag_uart_log']['rmt_storage']['write-read'] = '[open open][setattr getattr]'
G.add_edge('diag_uart_log','sdcardd')
G.edge['diag_uart_log']['sdcardd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('diag_uart_log','shell')
G.edge['diag_uart_log']['shell']['write-read'] = '[open open][setattr getattr]'
G.add_edge('diag_uart_log','s_system_app')
G.edge['diag_uart_log']['s_system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('diag_uart_log','system_app')
G.edge['diag_uart_log']['system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('diag_uart_log','system_server')
G.edge['diag_uart_log']['system_server']['write-read'] = '[open open][setattr getattr]'
G.add_edge('diag_uart_log','vmwared')
G.edge['diag_uart_log']['vmwared']['write-read'] = '[open open][setattr getattr]'
G.add_edge('diag_uart_log','wpa')
G.edge['diag_uart_log']['wpa']['write-read'] = '[open open][setattr getattr]'
G.add_edge('diag_uart_log','zygote')
G.edge['diag_uart_log']['zygote']['write-read'] = '[open open][setattr getattr]'
G.add_edge('diag_uart_log','adbd')
G.edge['diag_uart_log']['adbd']['write-read'] = '[write read]'
G.edge['diag_uart_log']['adbd']['fill'] = 'red'
G.add_edge('diag_uart_log','at_distributor')
G.edge['diag_uart_log']['at_distributor']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['diag_uart_log']['at_distributor']['fill'] = 'red'
G.add_edge('diag_uart_log','cbd')
G.edge['diag_uart_log']['cbd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['diag_uart_log']['cbd']['fill'] = 'red'
G.add_edge('diag_uart_log','charon')
G.edge['diag_uart_log']['charon']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['diag_uart_log']['charon']['fill'] = 'red'
G.add_edge('diag_uart_log','debuggerd')
G.edge['diag_uart_log']['debuggerd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['diag_uart_log']['debuggerd']['fill'] = 'red'
G.add_edge('diag_uart_log','dhcp')
G.edge['diag_uart_log']['dhcp']['write-read'] = '[write read]'
G.edge['diag_uart_log']['dhcp']['fill'] = 'red'
G.add_edge('diag_uart_log','diag_uart_log')
G.edge['diag_uart_log']['diag_uart_log']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['diag_uart_log']['diag_uart_log']['fill'] = 'red'
G.add_edge('diag_uart_log','domain')
G.edge['diag_uart_log']['domain']['write-read'] = '[write read]'
G.edge['diag_uart_log']['domain']['fill'] = 'red'
G.add_edge('diag_uart_log','dumpstate')
G.edge['diag_uart_log']['dumpstate']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['diag_uart_log']['dumpstate']['fill'] = 'red'
G.add_edge('diag_uart_log','hostapd')
G.edge['diag_uart_log']['hostapd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['diag_uart_log']['hostapd']['fill'] = 'red'
G.add_edge('diag_uart_log','ime_app')
G.edge['diag_uart_log']['ime_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['diag_uart_log']['ime_app']['fill'] = 'red'
G.add_edge('diag_uart_log','init_shell')
G.edge['diag_uart_log']['init_shell']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['diag_uart_log']['init_shell']['fill'] = 'red'
G.add_edge('diag_uart_log','installd')
G.edge['diag_uart_log']['installd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['diag_uart_log']['installd']['fill'] = 'red'
G.add_edge('diag_uart_log','itsonbs')
G.edge['diag_uart_log']['itsonbs']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['diag_uart_log']['itsonbs']['fill'] = 'red'
G.add_edge('diag_uart_log','logwrapper')
G.edge['diag_uart_log']['logwrapper']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['diag_uart_log']['logwrapper']['fill'] = 'red'
G.add_edge('diag_uart_log','netd')
G.edge['diag_uart_log']['netd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['diag_uart_log']['netd']['fill'] = 'red'
G.add_edge('diag_uart_log','qmuxd')
G.edge['diag_uart_log']['qmuxd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['diag_uart_log']['qmuxd']['fill'] = 'red'
G.add_edge('diag_uart_log','rild')
G.edge['diag_uart_log']['rild']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['diag_uart_log']['rild']['fill'] = 'red'
G.add_edge('diag_uart_log','rmt_storage')
G.edge['diag_uart_log']['rmt_storage']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['diag_uart_log']['rmt_storage']['fill'] = 'red'
G.add_edge('diag_uart_log','sdcardd')
G.edge['diag_uart_log']['sdcardd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['diag_uart_log']['sdcardd']['fill'] = 'red'
G.add_edge('diag_uart_log','shell')
G.edge['diag_uart_log']['shell']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['diag_uart_log']['shell']['fill'] = 'red'
G.add_edge('diag_uart_log','s_system_app')
G.edge['diag_uart_log']['s_system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['diag_uart_log']['s_system_app']['fill'] = 'red'
G.add_edge('diag_uart_log','system_app')
G.edge['diag_uart_log']['system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['diag_uart_log']['system_app']['fill'] = 'red'
G.add_edge('diag_uart_log','system_server')
G.edge['diag_uart_log']['system_server']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['diag_uart_log']['system_server']['fill'] = 'red'
G.add_edge('diag_uart_log','vmwared')
G.edge['diag_uart_log']['vmwared']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['diag_uart_log']['vmwared']['fill'] = 'red'
G.add_edge('diag_uart_log','wpa')
G.edge['diag_uart_log']['wpa']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['diag_uart_log']['wpa']['fill'] = 'red'
G.add_edge('diag_uart_log','zygote')
G.edge['diag_uart_log']['zygote']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['diag_uart_log']['zygote']['fill'] = 'red'
G.add_edge('diag_uart_log','adbd')
G.edge['diag_uart_log']['adbd']['write-read'] = '[write read][add_name search]'
G.add_edge('diag_uart_log','at_distributor')
G.edge['diag_uart_log']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('diag_uart_log','at_distributor')
G.edge['diag_uart_log']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('diag_uart_log','auditd')
G.edge['diag_uart_log']['auditd']['write-read'] = '[add_name search]'
G.add_edge('diag_uart_log','cbd')
G.edge['diag_uart_log']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('diag_uart_log','cbd')
G.edge['diag_uart_log']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('diag_uart_log','charon')
G.edge['diag_uart_log']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('diag_uart_log','charon')
G.edge['diag_uart_log']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('diag_uart_log','clatd')
G.edge['diag_uart_log']['clatd']['write-read'] = '[add_name search]'
G.add_edge('diag_uart_log','debuggerd')
G.edge['diag_uart_log']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('diag_uart_log','debuggerd')
G.edge['diag_uart_log']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('diag_uart_log','dhcp')
G.edge['diag_uart_log']['dhcp']['write-read'] = '[write read][add_name search]'
G.add_edge('diag_uart_log','diag_uart_log')
G.edge['diag_uart_log']['diag_uart_log']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('diag_uart_log','diag_uart_log')
G.edge['diag_uart_log']['diag_uart_log']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('diag_uart_log','dumpstate')
G.edge['diag_uart_log']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('diag_uart_log','dumpstate')
G.edge['diag_uart_log']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('diag_uart_log','hostapd')
G.edge['diag_uart_log']['hostapd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('diag_uart_log','hostapd')
G.edge['diag_uart_log']['hostapd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('diag_uart_log','hvdcp')
G.edge['diag_uart_log']['hvdcp']['write-read'] = '[add_name search]'
G.add_edge('diag_uart_log','ime_app')
G.edge['diag_uart_log']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('diag_uart_log','ime_app')
G.edge['diag_uart_log']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('diag_uart_log','init_shell')
G.edge['diag_uart_log']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('diag_uart_log','init_shell')
G.edge['diag_uart_log']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('diag_uart_log','installd')
G.edge['diag_uart_log']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('diag_uart_log','installd')
G.edge['diag_uart_log']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('diag_uart_log','itsonbs')
G.edge['diag_uart_log']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('diag_uart_log','itsonbs')
G.edge['diag_uart_log']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('diag_uart_log','jackservice')
G.edge['diag_uart_log']['jackservice']['write-read'] = '[add_name search]'
G.add_edge('diag_uart_log','lmkd')
G.edge['diag_uart_log']['lmkd']['write-read'] = '[remove_name search]'
G.add_edge('diag_uart_log','logwrapper')
G.edge['diag_uart_log']['logwrapper']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('diag_uart_log','logwrapper')
G.edge['diag_uart_log']['logwrapper']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('diag_uart_log','msm_irqbalanced')
G.edge['diag_uart_log']['msm_irqbalanced']['write-read'] = '[add_name search]'
G.add_edge('diag_uart_log','netd')
G.edge['diag_uart_log']['netd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('diag_uart_log','netd')
G.edge['diag_uart_log']['netd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('diag_uart_log','qmuxd')
G.edge['diag_uart_log']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('diag_uart_log','qmuxd')
G.edge['diag_uart_log']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('diag_uart_log','racoon')
G.edge['diag_uart_log']['racoon']['write-read'] = '[add_name search]'
G.add_edge('diag_uart_log','rild')
G.edge['diag_uart_log']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('diag_uart_log','rild')
G.edge['diag_uart_log']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('diag_uart_log','rmt_storage')
G.edge['diag_uart_log']['rmt_storage']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('diag_uart_log','rmt_storage')
G.edge['diag_uart_log']['rmt_storage']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('diag_uart_log','sdcardd')
G.edge['diag_uart_log']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('diag_uart_log','sdcardd')
G.edge['diag_uart_log']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('diag_uart_log','sensors')
G.edge['diag_uart_log']['sensors']['write-read'] = '[add_name search]'
G.add_edge('diag_uart_log','shell')
G.edge['diag_uart_log']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('diag_uart_log','shell')
G.edge['diag_uart_log']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('diag_uart_log','s_system_app')
G.edge['diag_uart_log']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('diag_uart_log','s_system_app')
G.edge['diag_uart_log']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('diag_uart_log','system_app')
G.edge['diag_uart_log']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('diag_uart_log','system_app')
G.edge['diag_uart_log']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('diag_uart_log','system_server')
G.edge['diag_uart_log']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('diag_uart_log','system_server')
G.edge['diag_uart_log']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('diag_uart_log','system_server')
G.edge['diag_uart_log']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search]'
G.add_edge('diag_uart_log','vmwared')
G.edge['diag_uart_log']['vmwared']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('diag_uart_log','vmwared')
G.edge['diag_uart_log']['vmwared']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('diag_uart_log','wpa')
G.edge['diag_uart_log']['wpa']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('diag_uart_log','wpa')
G.edge['diag_uart_log']['wpa']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('diag_uart_log','zygote')
G.edge['diag_uart_log']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('diag_uart_log','zygote')
G.edge['diag_uart_log']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('domain','at_distributor')
G.edge['domain']['at_distributor']['write-read'] = '[open open]'
G.add_edge('domain','cbd')
G.edge['domain']['cbd']['write-read'] = '[open open]'
G.add_edge('domain','charon')
G.edge['domain']['charon']['write-read'] = '[open open]'
G.add_edge('domain','debuggerd')
G.edge['domain']['debuggerd']['write-read'] = '[open open]'
G.add_edge('domain','diag_uart_log')
G.edge['domain']['diag_uart_log']['write-read'] = '[open open]'
G.add_edge('domain','dumpstate')
G.edge['domain']['dumpstate']['write-read'] = '[open open]'
G.add_edge('domain','hostapd')
G.edge['domain']['hostapd']['write-read'] = '[open open]'
G.add_edge('domain','ime_app')
G.edge['domain']['ime_app']['write-read'] = '[open open]'
G.add_edge('domain','init_shell')
G.edge['domain']['init_shell']['write-read'] = '[open open]'
G.add_edge('domain','installd')
G.edge['domain']['installd']['write-read'] = '[open open]'
G.add_edge('domain','itsonbs')
G.edge['domain']['itsonbs']['write-read'] = '[open open]'
G.add_edge('domain','logwrapper')
G.edge['domain']['logwrapper']['write-read'] = '[open open]'
G.add_edge('domain','netd')
G.edge['domain']['netd']['write-read'] = '[open open]'
G.add_edge('domain','qmuxd')
G.edge['domain']['qmuxd']['write-read'] = '[open open]'
G.add_edge('domain','rild')
G.edge['domain']['rild']['write-read'] = '[write read][open open]'
G.add_edge('domain','rmt_storage')
G.edge['domain']['rmt_storage']['write-read'] = '[open open]'
G.add_edge('domain','sdcardd')
G.edge['domain']['sdcardd']['write-read'] = '[open open]'
G.add_edge('domain','shell')
G.edge['domain']['shell']['write-read'] = '[open open]'
G.add_edge('domain','s_system_app')
G.edge['domain']['s_system_app']['write-read'] = '[open open]'
G.add_edge('domain','system_app')
G.edge['domain']['system_app']['write-read'] = '[open open]'
G.add_edge('domain','system_server')
G.edge['domain']['system_server']['write-read'] = '[open open]'
G.add_edge('domain','vmwared')
G.edge['domain']['vmwared']['write-read'] = '[open open]'
G.add_edge('domain','wpa')
G.edge['domain']['wpa']['write-read'] = '[open open]'
G.add_edge('domain','zygote')
G.edge['domain']['zygote']['write-read'] = '[open open]'
G.add_edge('domain','at_distributor')
G.edge['domain']['at_distributor']['write-read'] = '[open open][setattr getattr]'
G.add_edge('domain','cbd')
G.edge['domain']['cbd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('domain','charon')
G.edge['domain']['charon']['write-read'] = '[open open][setattr getattr]'
G.add_edge('domain','debuggerd')
G.edge['domain']['debuggerd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('domain','diag_uart_log')
G.edge['domain']['diag_uart_log']['write-read'] = '[open open][setattr getattr]'
G.add_edge('domain','dumpstate')
G.edge['domain']['dumpstate']['write-read'] = '[open open][setattr getattr]'
G.add_edge('domain','hostapd')
G.edge['domain']['hostapd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('domain','ime_app')
G.edge['domain']['ime_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('domain','init_shell')
G.edge['domain']['init_shell']['write-read'] = '[open open][setattr getattr]'
G.add_edge('domain','installd')
G.edge['domain']['installd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('domain','itsonbs')
G.edge['domain']['itsonbs']['write-read'] = '[open open][setattr getattr]'
G.add_edge('domain','logwrapper')
G.edge['domain']['logwrapper']['write-read'] = '[open open][setattr getattr]'
G.add_edge('domain','netd')
G.edge['domain']['netd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('domain','qmuxd')
G.edge['domain']['qmuxd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('domain','rild')
G.edge['domain']['rild']['write-read'] = '[write read][open open][setattr getattr]'
G.add_edge('domain','rmt_storage')
G.edge['domain']['rmt_storage']['write-read'] = '[open open][setattr getattr]'
G.add_edge('domain','sdcardd')
G.edge['domain']['sdcardd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('domain','shell')
G.edge['domain']['shell']['write-read'] = '[open open][setattr getattr]'
G.add_edge('domain','s_system_app')
G.edge['domain']['s_system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('domain','system_app')
G.edge['domain']['system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('domain','system_server')
G.edge['domain']['system_server']['write-read'] = '[open open][setattr getattr]'
G.add_edge('domain','vmwared')
G.edge['domain']['vmwared']['write-read'] = '[open open][setattr getattr]'
G.add_edge('domain','wpa')
G.edge['domain']['wpa']['write-read'] = '[open open][setattr getattr]'
G.add_edge('domain','zygote')
G.edge['domain']['zygote']['write-read'] = '[open open][setattr getattr]'
G.add_edge('domain','adbd')
G.edge['domain']['adbd']['write-read'] = '[write read]'
G.edge['domain']['adbd']['fill'] = 'red'
G.add_edge('domain','at_distributor')
G.edge['domain']['at_distributor']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['domain']['at_distributor']['fill'] = 'red'
G.add_edge('domain','cbd')
G.edge['domain']['cbd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['domain']['cbd']['fill'] = 'red'
G.add_edge('domain','charon')
G.edge['domain']['charon']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['domain']['charon']['fill'] = 'red'
G.add_edge('domain','debuggerd')
G.edge['domain']['debuggerd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['domain']['debuggerd']['fill'] = 'red'
G.add_edge('domain','dhcp')
G.edge['domain']['dhcp']['write-read'] = '[write read]'
G.edge['domain']['dhcp']['fill'] = 'red'
G.add_edge('domain','diag_uart_log')
G.edge['domain']['diag_uart_log']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['domain']['diag_uart_log']['fill'] = 'red'
G.add_edge('domain','domain')
G.edge['domain']['domain']['write-read'] = '[write read]'
G.edge['domain']['domain']['fill'] = 'red'
G.add_edge('domain','dumpstate')
G.edge['domain']['dumpstate']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['domain']['dumpstate']['fill'] = 'red'
G.add_edge('domain','hostapd')
G.edge['domain']['hostapd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['domain']['hostapd']['fill'] = 'red'
G.add_edge('domain','ime_app')
G.edge['domain']['ime_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['domain']['ime_app']['fill'] = 'red'
G.add_edge('domain','init_shell')
G.edge['domain']['init_shell']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['domain']['init_shell']['fill'] = 'red'
G.add_edge('domain','installd')
G.edge['domain']['installd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['domain']['installd']['fill'] = 'red'
G.add_edge('domain','itsonbs')
G.edge['domain']['itsonbs']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['domain']['itsonbs']['fill'] = 'red'
G.add_edge('domain','logwrapper')
G.edge['domain']['logwrapper']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['domain']['logwrapper']['fill'] = 'red'
G.add_edge('domain','netd')
G.edge['domain']['netd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['domain']['netd']['fill'] = 'red'
G.add_edge('domain','qmuxd')
G.edge['domain']['qmuxd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['domain']['qmuxd']['fill'] = 'red'
G.add_edge('domain','rild')
G.edge['domain']['rild']['write-read'] = '[write read][open open][setattr getattr][write read]'
G.edge['domain']['rild']['fill'] = 'red'
G.add_edge('domain','rmt_storage')
G.edge['domain']['rmt_storage']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['domain']['rmt_storage']['fill'] = 'red'
G.add_edge('domain','sdcardd')
G.edge['domain']['sdcardd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['domain']['sdcardd']['fill'] = 'red'
G.add_edge('domain','shell')
G.edge['domain']['shell']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['domain']['shell']['fill'] = 'red'
G.add_edge('domain','s_system_app')
G.edge['domain']['s_system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['domain']['s_system_app']['fill'] = 'red'
G.add_edge('domain','system_app')
G.edge['domain']['system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['domain']['system_app']['fill'] = 'red'
G.add_edge('domain','system_server')
G.edge['domain']['system_server']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['domain']['system_server']['fill'] = 'red'
G.add_edge('domain','vmwared')
G.edge['domain']['vmwared']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['domain']['vmwared']['fill'] = 'red'
G.add_edge('domain','wpa')
G.edge['domain']['wpa']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['domain']['wpa']['fill'] = 'red'
G.add_edge('domain','zygote')
G.edge['domain']['zygote']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['domain']['zygote']['fill'] = 'red'
G.add_edge('domain','adbd')
G.edge['domain']['adbd']['write-read'] = '[write read][add_name search]'
G.add_edge('domain','at_distributor')
G.edge['domain']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('domain','at_distributor')
G.edge['domain']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('domain','auditd')
G.edge['domain']['auditd']['write-read'] = '[add_name search]'
G.add_edge('domain','cbd')
G.edge['domain']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('domain','cbd')
G.edge['domain']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('domain','charon')
G.edge['domain']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('domain','charon')
G.edge['domain']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('domain','clatd')
G.edge['domain']['clatd']['write-read'] = '[add_name search]'
G.add_edge('domain','debuggerd')
G.edge['domain']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('domain','debuggerd')
G.edge['domain']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('domain','dhcp')
G.edge['domain']['dhcp']['write-read'] = '[write read][add_name search]'
G.add_edge('domain','diag_uart_log')
G.edge['domain']['diag_uart_log']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('domain','diag_uart_log')
G.edge['domain']['diag_uart_log']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('domain','dumpstate')
G.edge['domain']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('domain','dumpstate')
G.edge['domain']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('domain','hostapd')
G.edge['domain']['hostapd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('domain','hostapd')
G.edge['domain']['hostapd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('domain','hvdcp')
G.edge['domain']['hvdcp']['write-read'] = '[add_name search]'
G.add_edge('domain','ime_app')
G.edge['domain']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('domain','ime_app')
G.edge['domain']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('domain','init_shell')
G.edge['domain']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('domain','init_shell')
G.edge['domain']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('domain','installd')
G.edge['domain']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('domain','installd')
G.edge['domain']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('domain','itsonbs')
G.edge['domain']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('domain','itsonbs')
G.edge['domain']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('domain','jackservice')
G.edge['domain']['jackservice']['write-read'] = '[add_name search]'
G.add_edge('domain','lmkd')
G.edge['domain']['lmkd']['write-read'] = '[remove_name search]'
G.add_edge('domain','logwrapper')
G.edge['domain']['logwrapper']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('domain','logwrapper')
G.edge['domain']['logwrapper']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('domain','msm_irqbalanced')
G.edge['domain']['msm_irqbalanced']['write-read'] = '[add_name search]'
G.add_edge('domain','netd')
G.edge['domain']['netd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('domain','netd')
G.edge['domain']['netd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('domain','qmuxd')
G.edge['domain']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('domain','qmuxd')
G.edge['domain']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('domain','racoon')
G.edge['domain']['racoon']['write-read'] = '[add_name search]'
G.add_edge('domain','rild')
G.edge['domain']['rild']['write-read'] = '[write read][open open][setattr getattr][write read][add_name search]'
G.add_edge('domain','rild')
G.edge['domain']['rild']['write-read'] = '[write read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('domain','rmt_storage')
G.edge['domain']['rmt_storage']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('domain','rmt_storage')
G.edge['domain']['rmt_storage']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('domain','sdcardd')
G.edge['domain']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('domain','sdcardd')
G.edge['domain']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('domain','sensors')
G.edge['domain']['sensors']['write-read'] = '[add_name search]'
G.add_edge('domain','shell')
G.edge['domain']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('domain','shell')
G.edge['domain']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('domain','s_system_app')
G.edge['domain']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('domain','s_system_app')
G.edge['domain']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('domain','system_app')
G.edge['domain']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('domain','system_app')
G.edge['domain']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('domain','system_server')
G.edge['domain']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('domain','system_server')
G.edge['domain']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('domain','system_server')
G.edge['domain']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search]'
G.add_edge('domain','vmwared')
G.edge['domain']['vmwared']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('domain','vmwared')
G.edge['domain']['vmwared']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('domain','wpa')
G.edge['domain']['wpa']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('domain','wpa')
G.edge['domain']['wpa']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('domain','zygote')
G.edge['domain']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('domain','zygote')
G.edge['domain']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('domain','adbd')
G.edge['domain']['adbd']['write-read'] = '[write read][add_name search][add_name search]'
G.add_edge('domain','at_distributor')
G.edge['domain']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search]'
G.add_edge('domain','at_distributor')
G.edge['domain']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('domain','auditd')
G.edge['domain']['auditd']['write-read'] = '[add_name search][add_name search]'
G.add_edge('domain','cbd')
G.edge['domain']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search]'
G.add_edge('domain','cbd')
G.edge['domain']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('domain','charon')
G.edge['domain']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search]'
G.add_edge('domain','charon')
G.edge['domain']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('domain','clatd')
G.edge['domain']['clatd']['write-read'] = '[add_name search][add_name search]'
G.add_edge('domain','debuggerd')
G.edge['domain']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search]'
G.add_edge('domain','debuggerd')
G.edge['domain']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('domain','dhcp')
G.edge['domain']['dhcp']['write-read'] = '[write read][add_name search][add_name search]'
G.add_edge('domain','diag_uart_log')
G.edge['domain']['diag_uart_log']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search]'
G.add_edge('domain','diag_uart_log')
G.edge['domain']['diag_uart_log']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('domain','dumpstate')
G.edge['domain']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search]'
G.add_edge('domain','dumpstate')
G.edge['domain']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('domain','hostapd')
G.edge['domain']['hostapd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search]'
G.add_edge('domain','hostapd')
G.edge['domain']['hostapd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('domain','hvdcp')
G.edge['domain']['hvdcp']['write-read'] = '[add_name search][add_name search]'
G.add_edge('domain','ime_app')
G.edge['domain']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search]'
G.add_edge('domain','ime_app')
G.edge['domain']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('domain','init_shell')
G.edge['domain']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search]'
G.add_edge('domain','init_shell')
G.edge['domain']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('domain','installd')
G.edge['domain']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search]'
G.add_edge('domain','installd')
G.edge['domain']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('domain','itsonbs')
G.edge['domain']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search]'
G.add_edge('domain','itsonbs')
G.edge['domain']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('domain','jackservice')
G.edge['domain']['jackservice']['write-read'] = '[add_name search][add_name search]'
G.add_edge('domain','lmkd')
G.edge['domain']['lmkd']['write-read'] = '[remove_name search][remove_name search]'
G.add_edge('domain','logwrapper')
G.edge['domain']['logwrapper']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search]'
G.add_edge('domain','logwrapper')
G.edge['domain']['logwrapper']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('domain','msm_irqbalanced')
G.edge['domain']['msm_irqbalanced']['write-read'] = '[add_name search][add_name search]'
G.add_edge('domain','netd')
G.edge['domain']['netd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search]'
G.add_edge('domain','netd')
G.edge['domain']['netd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('domain','qmuxd')
G.edge['domain']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search]'
G.add_edge('domain','qmuxd')
G.edge['domain']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('domain','racoon')
G.edge['domain']['racoon']['write-read'] = '[add_name search][add_name search]'
G.add_edge('domain','rild')
G.edge['domain']['rild']['write-read'] = '[write read][open open][setattr getattr][write read][add_name search][remove_name search][add_name search]'
G.add_edge('domain','rild')
G.edge['domain']['rild']['write-read'] = '[write read][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('domain','rmt_storage')
G.edge['domain']['rmt_storage']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search]'
G.add_edge('domain','rmt_storage')
G.edge['domain']['rmt_storage']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('domain','sdcardd')
G.edge['domain']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search]'
G.add_edge('domain','sdcardd')
G.edge['domain']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('domain','sensors')
G.edge['domain']['sensors']['write-read'] = '[add_name search][add_name search]'
G.add_edge('domain','shell')
G.edge['domain']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search]'
G.add_edge('domain','shell')
G.edge['domain']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('domain','s_system_app')
G.edge['domain']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search]'
G.add_edge('domain','s_system_app')
G.edge['domain']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('domain','system_app')
G.edge['domain']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search]'
G.add_edge('domain','system_app')
G.edge['domain']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('domain','system_server')
G.edge['domain']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][add_name search]'
G.add_edge('domain','system_server')
G.edge['domain']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('domain','system_server')
G.edge['domain']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][add_name search][remove_name search][remove_name search]'
G.add_edge('domain','vmwared')
G.edge['domain']['vmwared']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search]'
G.add_edge('domain','vmwared')
G.edge['domain']['vmwared']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('domain','wpa')
G.edge['domain']['wpa']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search]'
G.add_edge('domain','wpa')
G.edge['domain']['wpa']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('domain','zygote')
G.edge['domain']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search]'
G.add_edge('domain','zygote')
G.edge['domain']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('dumpstate','at_distributor')
G.edge['dumpstate']['at_distributor']['write-read'] = '[open open]'
G.add_edge('dumpstate','cbd')
G.edge['dumpstate']['cbd']['write-read'] = '[open open]'
G.add_edge('dumpstate','charon')
G.edge['dumpstate']['charon']['write-read'] = '[open open]'
G.add_edge('dumpstate','debuggerd')
G.edge['dumpstate']['debuggerd']['write-read'] = '[open open]'
G.add_edge('dumpstate','diag_uart_log')
G.edge['dumpstate']['diag_uart_log']['write-read'] = '[open open]'
G.add_edge('dumpstate','dumpstate')
G.edge['dumpstate']['dumpstate']['write-read'] = '[open open]'
G.add_edge('dumpstate','hostapd')
G.edge['dumpstate']['hostapd']['write-read'] = '[open open]'
G.add_edge('dumpstate','ime_app')
G.edge['dumpstate']['ime_app']['write-read'] = '[open open]'
G.add_edge('dumpstate','init_shell')
G.edge['dumpstate']['init_shell']['write-read'] = '[open open]'
G.add_edge('dumpstate','installd')
G.edge['dumpstate']['installd']['write-read'] = '[open open]'
G.add_edge('dumpstate','itsonbs')
G.edge['dumpstate']['itsonbs']['write-read'] = '[open open]'
G.add_edge('dumpstate','logwrapper')
G.edge['dumpstate']['logwrapper']['write-read'] = '[open open]'
G.add_edge('dumpstate','netd')
G.edge['dumpstate']['netd']['write-read'] = '[open open]'
G.add_edge('dumpstate','qmuxd')
G.edge['dumpstate']['qmuxd']['write-read'] = '[open open]'
G.add_edge('dumpstate','rild')
G.edge['dumpstate']['rild']['write-read'] = '[open open]'
G.add_edge('dumpstate','rmt_storage')
G.edge['dumpstate']['rmt_storage']['write-read'] = '[open open]'
G.add_edge('dumpstate','sdcardd')
G.edge['dumpstate']['sdcardd']['write-read'] = '[open open]'
G.add_edge('dumpstate','shell')
G.edge['dumpstate']['shell']['write-read'] = '[open open]'
G.add_edge('dumpstate','s_system_app')
G.edge['dumpstate']['s_system_app']['write-read'] = '[open open]'
G.add_edge('dumpstate','system_app')
G.edge['dumpstate']['system_app']['write-read'] = '[open open]'
G.add_edge('dumpstate','system_server')
G.edge['dumpstate']['system_server']['write-read'] = '[open open]'
G.add_edge('dumpstate','vmwared')
G.edge['dumpstate']['vmwared']['write-read'] = '[open open]'
G.add_edge('dumpstate','wpa')
G.edge['dumpstate']['wpa']['write-read'] = '[open open]'
G.add_edge('dumpstate','zygote')
G.edge['dumpstate']['zygote']['write-read'] = '[open open]'
G.add_edge('dumpstate','at_distributor')
G.edge['dumpstate']['at_distributor']['write-read'] = '[open open][setattr getattr]'
G.add_edge('dumpstate','cbd')
G.edge['dumpstate']['cbd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('dumpstate','charon')
G.edge['dumpstate']['charon']['write-read'] = '[open open][setattr getattr]'
G.add_edge('dumpstate','debuggerd')
G.edge['dumpstate']['debuggerd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('dumpstate','diag_uart_log')
G.edge['dumpstate']['diag_uart_log']['write-read'] = '[open open][setattr getattr]'
G.add_edge('dumpstate','dumpstate')
G.edge['dumpstate']['dumpstate']['write-read'] = '[open open][setattr getattr]'
G.add_edge('dumpstate','hostapd')
G.edge['dumpstate']['hostapd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('dumpstate','ime_app')
G.edge['dumpstate']['ime_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('dumpstate','init_shell')
G.edge['dumpstate']['init_shell']['write-read'] = '[open open][setattr getattr]'
G.add_edge('dumpstate','installd')
G.edge['dumpstate']['installd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('dumpstate','itsonbs')
G.edge['dumpstate']['itsonbs']['write-read'] = '[open open][setattr getattr]'
G.add_edge('dumpstate','logwrapper')
G.edge['dumpstate']['logwrapper']['write-read'] = '[open open][setattr getattr]'
G.add_edge('dumpstate','netd')
G.edge['dumpstate']['netd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('dumpstate','qmuxd')
G.edge['dumpstate']['qmuxd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('dumpstate','rild')
G.edge['dumpstate']['rild']['write-read'] = '[open open][setattr getattr]'
G.add_edge('dumpstate','rmt_storage')
G.edge['dumpstate']['rmt_storage']['write-read'] = '[open open][setattr getattr]'
G.add_edge('dumpstate','sdcardd')
G.edge['dumpstate']['sdcardd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('dumpstate','shell')
G.edge['dumpstate']['shell']['write-read'] = '[open open][setattr getattr]'
G.add_edge('dumpstate','s_system_app')
G.edge['dumpstate']['s_system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('dumpstate','system_app')
G.edge['dumpstate']['system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('dumpstate','system_server')
G.edge['dumpstate']['system_server']['write-read'] = '[open open][setattr getattr]'
G.add_edge('dumpstate','vmwared')
G.edge['dumpstate']['vmwared']['write-read'] = '[open open][setattr getattr]'
G.add_edge('dumpstate','wpa')
G.edge['dumpstate']['wpa']['write-read'] = '[open open][setattr getattr]'
G.add_edge('dumpstate','zygote')
G.edge['dumpstate']['zygote']['write-read'] = '[open open][setattr getattr]'
G.add_edge('dumpstate','adbd')
G.edge['dumpstate']['adbd']['write-read'] = '[write read]'
G.edge['dumpstate']['adbd']['fill'] = 'red'
G.add_edge('dumpstate','at_distributor')
G.edge['dumpstate']['at_distributor']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['dumpstate']['at_distributor']['fill'] = 'red'
G.add_edge('dumpstate','cbd')
G.edge['dumpstate']['cbd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['dumpstate']['cbd']['fill'] = 'red'
G.add_edge('dumpstate','charon')
G.edge['dumpstate']['charon']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['dumpstate']['charon']['fill'] = 'red'
G.add_edge('dumpstate','debuggerd')
G.edge['dumpstate']['debuggerd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['dumpstate']['debuggerd']['fill'] = 'red'
G.add_edge('dumpstate','dhcp')
G.edge['dumpstate']['dhcp']['write-read'] = '[write read]'
G.edge['dumpstate']['dhcp']['fill'] = 'red'
G.add_edge('dumpstate','diag_uart_log')
G.edge['dumpstate']['diag_uart_log']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['dumpstate']['diag_uart_log']['fill'] = 'red'
G.add_edge('dumpstate','domain')
G.edge['dumpstate']['domain']['write-read'] = '[write read]'
G.edge['dumpstate']['domain']['fill'] = 'red'
G.add_edge('dumpstate','dumpstate')
G.edge['dumpstate']['dumpstate']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['dumpstate']['dumpstate']['fill'] = 'red'
G.add_edge('dumpstate','hostapd')
G.edge['dumpstate']['hostapd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['dumpstate']['hostapd']['fill'] = 'red'
G.add_edge('dumpstate','ime_app')
G.edge['dumpstate']['ime_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['dumpstate']['ime_app']['fill'] = 'red'
G.add_edge('dumpstate','init_shell')
G.edge['dumpstate']['init_shell']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['dumpstate']['init_shell']['fill'] = 'red'
G.add_edge('dumpstate','installd')
G.edge['dumpstate']['installd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['dumpstate']['installd']['fill'] = 'red'
G.add_edge('dumpstate','itsonbs')
G.edge['dumpstate']['itsonbs']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['dumpstate']['itsonbs']['fill'] = 'red'
G.add_edge('dumpstate','logwrapper')
G.edge['dumpstate']['logwrapper']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['dumpstate']['logwrapper']['fill'] = 'red'
G.add_edge('dumpstate','netd')
G.edge['dumpstate']['netd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['dumpstate']['netd']['fill'] = 'red'
G.add_edge('dumpstate','qmuxd')
G.edge['dumpstate']['qmuxd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['dumpstate']['qmuxd']['fill'] = 'red'
G.add_edge('dumpstate','rild')
G.edge['dumpstate']['rild']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['dumpstate']['rild']['fill'] = 'red'
G.add_edge('dumpstate','rmt_storage')
G.edge['dumpstate']['rmt_storage']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['dumpstate']['rmt_storage']['fill'] = 'red'
G.add_edge('dumpstate','sdcardd')
G.edge['dumpstate']['sdcardd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['dumpstate']['sdcardd']['fill'] = 'red'
G.add_edge('dumpstate','shell')
G.edge['dumpstate']['shell']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['dumpstate']['shell']['fill'] = 'red'
G.add_edge('dumpstate','s_system_app')
G.edge['dumpstate']['s_system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['dumpstate']['s_system_app']['fill'] = 'red'
G.add_edge('dumpstate','system_app')
G.edge['dumpstate']['system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['dumpstate']['system_app']['fill'] = 'red'
G.add_edge('dumpstate','system_server')
G.edge['dumpstate']['system_server']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['dumpstate']['system_server']['fill'] = 'red'
G.add_edge('dumpstate','vmwared')
G.edge['dumpstate']['vmwared']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['dumpstate']['vmwared']['fill'] = 'red'
G.add_edge('dumpstate','wpa')
G.edge['dumpstate']['wpa']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['dumpstate']['wpa']['fill'] = 'red'
G.add_edge('dumpstate','zygote')
G.edge['dumpstate']['zygote']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['dumpstate']['zygote']['fill'] = 'red'
G.add_edge('dumpstate','adbd')
G.edge['dumpstate']['adbd']['write-read'] = '[write read][add_name search]'
G.add_edge('dumpstate','at_distributor')
G.edge['dumpstate']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('dumpstate','at_distributor')
G.edge['dumpstate']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('dumpstate','auditd')
G.edge['dumpstate']['auditd']['write-read'] = '[add_name search]'
G.add_edge('dumpstate','cbd')
G.edge['dumpstate']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('dumpstate','cbd')
G.edge['dumpstate']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('dumpstate','charon')
G.edge['dumpstate']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('dumpstate','charon')
G.edge['dumpstate']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('dumpstate','clatd')
G.edge['dumpstate']['clatd']['write-read'] = '[add_name search]'
G.add_edge('dumpstate','debuggerd')
G.edge['dumpstate']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('dumpstate','debuggerd')
G.edge['dumpstate']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('dumpstate','dhcp')
G.edge['dumpstate']['dhcp']['write-read'] = '[write read][add_name search]'
G.add_edge('dumpstate','diag_uart_log')
G.edge['dumpstate']['diag_uart_log']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('dumpstate','diag_uart_log')
G.edge['dumpstate']['diag_uart_log']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('dumpstate','dumpstate')
G.edge['dumpstate']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('dumpstate','dumpstate')
G.edge['dumpstate']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('dumpstate','hostapd')
G.edge['dumpstate']['hostapd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('dumpstate','hostapd')
G.edge['dumpstate']['hostapd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('dumpstate','hvdcp')
G.edge['dumpstate']['hvdcp']['write-read'] = '[add_name search]'
G.add_edge('dumpstate','ime_app')
G.edge['dumpstate']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('dumpstate','ime_app')
G.edge['dumpstate']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('dumpstate','init_shell')
G.edge['dumpstate']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('dumpstate','init_shell')
G.edge['dumpstate']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('dumpstate','installd')
G.edge['dumpstate']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('dumpstate','installd')
G.edge['dumpstate']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('dumpstate','itsonbs')
G.edge['dumpstate']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('dumpstate','itsonbs')
G.edge['dumpstate']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('dumpstate','jackservice')
G.edge['dumpstate']['jackservice']['write-read'] = '[add_name search]'
G.add_edge('dumpstate','lmkd')
G.edge['dumpstate']['lmkd']['write-read'] = '[remove_name search]'
G.add_edge('dumpstate','logwrapper')
G.edge['dumpstate']['logwrapper']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('dumpstate','logwrapper')
G.edge['dumpstate']['logwrapper']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('dumpstate','msm_irqbalanced')
G.edge['dumpstate']['msm_irqbalanced']['write-read'] = '[add_name search]'
G.add_edge('dumpstate','netd')
G.edge['dumpstate']['netd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('dumpstate','netd')
G.edge['dumpstate']['netd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('dumpstate','qmuxd')
G.edge['dumpstate']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('dumpstate','qmuxd')
G.edge['dumpstate']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('dumpstate','racoon')
G.edge['dumpstate']['racoon']['write-read'] = '[add_name search]'
G.add_edge('dumpstate','rild')
G.edge['dumpstate']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('dumpstate','rild')
G.edge['dumpstate']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('dumpstate','rmt_storage')
G.edge['dumpstate']['rmt_storage']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('dumpstate','rmt_storage')
G.edge['dumpstate']['rmt_storage']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('dumpstate','sdcardd')
G.edge['dumpstate']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('dumpstate','sdcardd')
G.edge['dumpstate']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('dumpstate','sensors')
G.edge['dumpstate']['sensors']['write-read'] = '[add_name search]'
G.add_edge('dumpstate','shell')
G.edge['dumpstate']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('dumpstate','shell')
G.edge['dumpstate']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('dumpstate','s_system_app')
G.edge['dumpstate']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('dumpstate','s_system_app')
G.edge['dumpstate']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('dumpstate','system_app')
G.edge['dumpstate']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('dumpstate','system_app')
G.edge['dumpstate']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('dumpstate','system_server')
G.edge['dumpstate']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('dumpstate','system_server')
G.edge['dumpstate']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('dumpstate','system_server')
G.edge['dumpstate']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search]'
G.add_edge('dumpstate','vmwared')
G.edge['dumpstate']['vmwared']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('dumpstate','vmwared')
G.edge['dumpstate']['vmwared']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('dumpstate','wpa')
G.edge['dumpstate']['wpa']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('dumpstate','wpa')
G.edge['dumpstate']['wpa']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('dumpstate','zygote')
G.edge['dumpstate']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('dumpstate','zygote')
G.edge['dumpstate']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('hostapd','at_distributor')
G.edge['hostapd']['at_distributor']['write-read'] = '[open open]'
G.add_edge('hostapd','cbd')
G.edge['hostapd']['cbd']['write-read'] = '[open open]'
G.add_edge('hostapd','charon')
G.edge['hostapd']['charon']['write-read'] = '[open open]'
G.add_edge('hostapd','debuggerd')
G.edge['hostapd']['debuggerd']['write-read'] = '[open open]'
G.add_edge('hostapd','diag_uart_log')
G.edge['hostapd']['diag_uart_log']['write-read'] = '[open open]'
G.add_edge('hostapd','dumpstate')
G.edge['hostapd']['dumpstate']['write-read'] = '[open open]'
G.add_edge('hostapd','hostapd')
G.edge['hostapd']['hostapd']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('hostapd','ime_app')
G.edge['hostapd']['ime_app']['write-read'] = '[open open]'
G.add_edge('hostapd','init_shell')
G.edge['hostapd']['init_shell']['write-read'] = '[open open]'
G.add_edge('hostapd','installd')
G.edge['hostapd']['installd']['write-read'] = '[open open]'
G.add_edge('hostapd','itsonbs')
G.edge['hostapd']['itsonbs']['write-read'] = '[open open]'
G.add_edge('hostapd','logwrapper')
G.edge['hostapd']['logwrapper']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('hostapd','netd')
G.edge['hostapd']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('hostapd','qmuxd')
G.edge['hostapd']['qmuxd']['write-read'] = '[open open]'
G.add_edge('hostapd','rild')
G.edge['hostapd']['rild']['write-read'] = '[open open]'
G.add_edge('hostapd','rmt_storage')
G.edge['hostapd']['rmt_storage']['write-read'] = '[open open]'
G.add_edge('hostapd','sdcardd')
G.edge['hostapd']['sdcardd']['write-read'] = '[open open]'
G.add_edge('hostapd','shell')
G.edge['hostapd']['shell']['write-read'] = '[open open]'
G.add_edge('hostapd','s_system_app')
G.edge['hostapd']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('hostapd','system_app')
G.edge['hostapd']['system_app']['write-read'] = '[open open]'
G.add_edge('hostapd','system_server')
G.edge['hostapd']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('hostapd','vmwared')
G.edge['hostapd']['vmwared']['write-read'] = '[open open]'
G.add_edge('hostapd','wpa')
G.edge['hostapd']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('hostapd','zygote')
G.edge['hostapd']['zygote']['write-read'] = '[open open]'
G.add_edge('hostapd','at_distributor')
G.edge['hostapd']['at_distributor']['write-read'] = '[open open][setattr getattr]'
G.add_edge('hostapd','cbd')
G.edge['hostapd']['cbd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('hostapd','charon')
G.edge['hostapd']['charon']['write-read'] = '[open open][setattr getattr]'
G.add_edge('hostapd','debuggerd')
G.edge['hostapd']['debuggerd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('hostapd','diag_uart_log')
G.edge['hostapd']['diag_uart_log']['write-read'] = '[open open][setattr getattr]'
G.add_edge('hostapd','dumpstate')
G.edge['hostapd']['dumpstate']['write-read'] = '[open open][setattr getattr]'
G.add_edge('hostapd','hostapd')
G.edge['hostapd']['hostapd']['write-read'] = '[open open][write read][append read][open open][setattr getattr]'
G.add_edge('hostapd','ime_app')
G.edge['hostapd']['ime_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('hostapd','init_shell')
G.edge['hostapd']['init_shell']['write-read'] = '[open open][setattr getattr]'
G.add_edge('hostapd','installd')
G.edge['hostapd']['installd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('hostapd','itsonbs')
G.edge['hostapd']['itsonbs']['write-read'] = '[open open][setattr getattr]'
G.add_edge('hostapd','logwrapper')
G.edge['hostapd']['logwrapper']['write-read'] = '[open open][write read][append read][open open][setattr getattr]'
G.add_edge('hostapd','netd')
G.edge['hostapd']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('hostapd','qmuxd')
G.edge['hostapd']['qmuxd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('hostapd','rild')
G.edge['hostapd']['rild']['write-read'] = '[open open][setattr getattr]'
G.add_edge('hostapd','rmt_storage')
G.edge['hostapd']['rmt_storage']['write-read'] = '[open open][setattr getattr]'
G.add_edge('hostapd','sdcardd')
G.edge['hostapd']['sdcardd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('hostapd','shell')
G.edge['hostapd']['shell']['write-read'] = '[open open][setattr getattr]'
G.add_edge('hostapd','s_system_app')
G.edge['hostapd']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('hostapd','system_app')
G.edge['hostapd']['system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('hostapd','system_server')
G.edge['hostapd']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('hostapd','vmwared')
G.edge['hostapd']['vmwared']['write-read'] = '[open open][setattr getattr]'
G.add_edge('hostapd','wpa')
G.edge['hostapd']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('hostapd','zygote')
G.edge['hostapd']['zygote']['write-read'] = '[open open][setattr getattr]'
G.add_edge('hostapd','adbd')
G.edge['hostapd']['adbd']['write-read'] = '[write read]'
G.edge['hostapd']['adbd']['fill'] = 'red'
G.add_edge('hostapd','at_distributor')
G.edge['hostapd']['at_distributor']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['hostapd']['at_distributor']['fill'] = 'red'
G.add_edge('hostapd','cbd')
G.edge['hostapd']['cbd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['hostapd']['cbd']['fill'] = 'red'
G.add_edge('hostapd','charon')
G.edge['hostapd']['charon']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['hostapd']['charon']['fill'] = 'red'
G.add_edge('hostapd','debuggerd')
G.edge['hostapd']['debuggerd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['hostapd']['debuggerd']['fill'] = 'red'
G.add_edge('hostapd','dhcp')
G.edge['hostapd']['dhcp']['write-read'] = '[write read]'
G.edge['hostapd']['dhcp']['fill'] = 'red'
G.add_edge('hostapd','diag_uart_log')
G.edge['hostapd']['diag_uart_log']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['hostapd']['diag_uart_log']['fill'] = 'red'
G.add_edge('hostapd','domain')
G.edge['hostapd']['domain']['write-read'] = '[write read]'
G.edge['hostapd']['domain']['fill'] = 'red'
G.add_edge('hostapd','dumpstate')
G.edge['hostapd']['dumpstate']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['hostapd']['dumpstate']['fill'] = 'red'
G.add_edge('hostapd','hostapd')
G.edge['hostapd']['hostapd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read]'
G.edge['hostapd']['hostapd']['fill'] = 'red'
G.add_edge('hostapd','ime_app')
G.edge['hostapd']['ime_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['hostapd']['ime_app']['fill'] = 'red'
G.add_edge('hostapd','init_shell')
G.edge['hostapd']['init_shell']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['hostapd']['init_shell']['fill'] = 'red'
G.add_edge('hostapd','installd')
G.edge['hostapd']['installd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['hostapd']['installd']['fill'] = 'red'
G.add_edge('hostapd','itsonbs')
G.edge['hostapd']['itsonbs']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['hostapd']['itsonbs']['fill'] = 'red'
G.add_edge('hostapd','logwrapper')
G.edge['hostapd']['logwrapper']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read]'
G.edge['hostapd']['logwrapper']['fill'] = 'red'
G.add_edge('hostapd','netd')
G.edge['hostapd']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['hostapd']['netd']['fill'] = 'red'
G.add_edge('hostapd','qmuxd')
G.edge['hostapd']['qmuxd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['hostapd']['qmuxd']['fill'] = 'red'
G.add_edge('hostapd','rild')
G.edge['hostapd']['rild']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['hostapd']['rild']['fill'] = 'red'
G.add_edge('hostapd','rmt_storage')
G.edge['hostapd']['rmt_storage']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['hostapd']['rmt_storage']['fill'] = 'red'
G.add_edge('hostapd','sdcardd')
G.edge['hostapd']['sdcardd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['hostapd']['sdcardd']['fill'] = 'red'
G.add_edge('hostapd','shell')
G.edge['hostapd']['shell']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['hostapd']['shell']['fill'] = 'red'
G.add_edge('hostapd','s_system_app')
G.edge['hostapd']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['hostapd']['s_system_app']['fill'] = 'red'
G.add_edge('hostapd','system_app')
G.edge['hostapd']['system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['hostapd']['system_app']['fill'] = 'red'
G.add_edge('hostapd','system_server')
G.edge['hostapd']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['hostapd']['system_server']['fill'] = 'red'
G.add_edge('hostapd','vmwared')
G.edge['hostapd']['vmwared']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['hostapd']['vmwared']['fill'] = 'red'
G.add_edge('hostapd','wpa')
G.edge['hostapd']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['hostapd']['wpa']['fill'] = 'red'
G.add_edge('hostapd','zygote')
G.edge['hostapd']['zygote']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['hostapd']['zygote']['fill'] = 'red'
G.add_edge('hostapd','adbd')
G.edge['hostapd']['adbd']['write-read'] = '[write read][add_name search]'
G.add_edge('hostapd','at_distributor')
G.edge['hostapd']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('hostapd','at_distributor')
G.edge['hostapd']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('hostapd','auditd')
G.edge['hostapd']['auditd']['write-read'] = '[add_name search]'
G.add_edge('hostapd','cbd')
G.edge['hostapd']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('hostapd','cbd')
G.edge['hostapd']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('hostapd','charon')
G.edge['hostapd']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('hostapd','charon')
G.edge['hostapd']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('hostapd','clatd')
G.edge['hostapd']['clatd']['write-read'] = '[add_name search]'
G.add_edge('hostapd','debuggerd')
G.edge['hostapd']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('hostapd','debuggerd')
G.edge['hostapd']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('hostapd','dhcp')
G.edge['hostapd']['dhcp']['write-read'] = '[write read][add_name search]'
G.add_edge('hostapd','diag_uart_log')
G.edge['hostapd']['diag_uart_log']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('hostapd','diag_uart_log')
G.edge['hostapd']['diag_uart_log']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('hostapd','dumpstate')
G.edge['hostapd']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('hostapd','dumpstate')
G.edge['hostapd']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('hostapd','hostapd')
G.edge['hostapd']['hostapd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('hostapd','hostapd')
G.edge['hostapd']['hostapd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('hostapd','hvdcp')
G.edge['hostapd']['hvdcp']['write-read'] = '[add_name search]'
G.add_edge('hostapd','ime_app')
G.edge['hostapd']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('hostapd','ime_app')
G.edge['hostapd']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('hostapd','init_shell')
G.edge['hostapd']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('hostapd','init_shell')
G.edge['hostapd']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('hostapd','installd')
G.edge['hostapd']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('hostapd','installd')
G.edge['hostapd']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('hostapd','itsonbs')
G.edge['hostapd']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('hostapd','itsonbs')
G.edge['hostapd']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('hostapd','jackservice')
G.edge['hostapd']['jackservice']['write-read'] = '[add_name search]'
G.add_edge('hostapd','lmkd')
G.edge['hostapd']['lmkd']['write-read'] = '[remove_name search]'
G.add_edge('hostapd','logwrapper')
G.edge['hostapd']['logwrapper']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('hostapd','logwrapper')
G.edge['hostapd']['logwrapper']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('hostapd','msm_irqbalanced')
G.edge['hostapd']['msm_irqbalanced']['write-read'] = '[add_name search]'
G.add_edge('hostapd','netd')
G.edge['hostapd']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('hostapd','netd')
G.edge['hostapd']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('hostapd','qmuxd')
G.edge['hostapd']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('hostapd','qmuxd')
G.edge['hostapd']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('hostapd','racoon')
G.edge['hostapd']['racoon']['write-read'] = '[add_name search]'
G.add_edge('hostapd','rild')
G.edge['hostapd']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('hostapd','rild')
G.edge['hostapd']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('hostapd','rmt_storage')
G.edge['hostapd']['rmt_storage']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('hostapd','rmt_storage')
G.edge['hostapd']['rmt_storage']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('hostapd','sdcardd')
G.edge['hostapd']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('hostapd','sdcardd')
G.edge['hostapd']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('hostapd','sensors')
G.edge['hostapd']['sensors']['write-read'] = '[add_name search]'
G.add_edge('hostapd','shell')
G.edge['hostapd']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('hostapd','shell')
G.edge['hostapd']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('hostapd','s_system_app')
G.edge['hostapd']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('hostapd','s_system_app')
G.edge['hostapd']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('hostapd','system_app')
G.edge['hostapd']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('hostapd','system_app')
G.edge['hostapd']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('hostapd','system_server')
G.edge['hostapd']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('hostapd','system_server')
G.edge['hostapd']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('hostapd','system_server')
G.edge['hostapd']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search]'
G.add_edge('hostapd','vmwared')
G.edge['hostapd']['vmwared']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('hostapd','vmwared')
G.edge['hostapd']['vmwared']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('hostapd','wpa')
G.edge['hostapd']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('hostapd','wpa')
G.edge['hostapd']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('hostapd','zygote')
G.edge['hostapd']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('hostapd','zygote')
G.edge['hostapd']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('ime_app','at_distributor')
G.edge['ime_app']['at_distributor']['write-read'] = '[open open]'
G.add_edge('ime_app','cbd')
G.edge['ime_app']['cbd']['write-read'] = '[open open]'
G.add_edge('ime_app','charon')
G.edge['ime_app']['charon']['write-read'] = '[open open]'
G.add_edge('ime_app','debuggerd')
G.edge['ime_app']['debuggerd']['write-read'] = '[open open]'
G.add_edge('ime_app','diag_uart_log')
G.edge['ime_app']['diag_uart_log']['write-read'] = '[open open]'
G.add_edge('ime_app','dumpstate')
G.edge['ime_app']['dumpstate']['write-read'] = '[open open]'
G.add_edge('ime_app','hostapd')
G.edge['ime_app']['hostapd']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('ime_app','ime_app')
G.edge['ime_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open]'
G.add_edge('ime_app','init_shell')
G.edge['ime_app']['init_shell']['write-read'] = '[open open]'
G.add_edge('ime_app','installd')
G.edge['ime_app']['installd']['write-read'] = '[open open]'
G.add_edge('ime_app','itsonbs')
G.edge['ime_app']['itsonbs']['write-read'] = '[open open]'
G.add_edge('ime_app','logwrapper')
G.edge['ime_app']['logwrapper']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('ime_app','netd')
G.edge['ime_app']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open]'
G.add_edge('ime_app','qmuxd')
G.edge['ime_app']['qmuxd']['write-read'] = '[open open]'
G.add_edge('ime_app','rild')
G.edge['ime_app']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open]'
G.add_edge('ime_app','rmt_storage')
G.edge['ime_app']['rmt_storage']['write-read'] = '[open open]'
G.add_edge('ime_app','sdcardd')
G.edge['ime_app']['sdcardd']['write-read'] = '[open open]'
G.add_edge('ime_app','shell')
G.edge['ime_app']['shell']['write-read'] = '[open open]'
G.add_edge('ime_app','s_system_app')
G.edge['ime_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open]'
G.add_edge('ime_app','system_app')
G.edge['ime_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open]'
G.add_edge('ime_app','system_server')
G.edge['ime_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open]'
G.add_edge('ime_app','vmwared')
G.edge['ime_app']['vmwared']['write-read'] = '[open open]'
G.add_edge('ime_app','wpa')
G.edge['ime_app']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('ime_app','zygote')
G.edge['ime_app']['zygote']['write-read'] = '[open open]'
G.add_edge('ime_app','at_distributor')
G.edge['ime_app']['at_distributor']['write-read'] = '[open open][setattr getattr]'
G.add_edge('ime_app','cbd')
G.edge['ime_app']['cbd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('ime_app','charon')
G.edge['ime_app']['charon']['write-read'] = '[open open][setattr getattr]'
G.add_edge('ime_app','debuggerd')
G.edge['ime_app']['debuggerd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('ime_app','diag_uart_log')
G.edge['ime_app']['diag_uart_log']['write-read'] = '[open open][setattr getattr]'
G.add_edge('ime_app','dumpstate')
G.edge['ime_app']['dumpstate']['write-read'] = '[open open][setattr getattr]'
G.add_edge('ime_app','hostapd')
G.edge['ime_app']['hostapd']['write-read'] = '[open open][write read][append read][open open][setattr getattr]'
G.add_edge('ime_app','ime_app')
G.edge['ime_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr]'
G.add_edge('ime_app','init_shell')
G.edge['ime_app']['init_shell']['write-read'] = '[open open][setattr getattr]'
G.add_edge('ime_app','installd')
G.edge['ime_app']['installd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('ime_app','itsonbs')
G.edge['ime_app']['itsonbs']['write-read'] = '[open open][setattr getattr]'
G.add_edge('ime_app','logwrapper')
G.edge['ime_app']['logwrapper']['write-read'] = '[open open][write read][append read][open open][setattr getattr]'
G.add_edge('ime_app','netd')
G.edge['ime_app']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('ime_app','qmuxd')
G.edge['ime_app']['qmuxd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('ime_app','rild')
G.edge['ime_app']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr]'
G.add_edge('ime_app','rmt_storage')
G.edge['ime_app']['rmt_storage']['write-read'] = '[open open][setattr getattr]'
G.add_edge('ime_app','sdcardd')
G.edge['ime_app']['sdcardd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('ime_app','shell')
G.edge['ime_app']['shell']['write-read'] = '[open open][setattr getattr]'
G.add_edge('ime_app','s_system_app')
G.edge['ime_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('ime_app','system_app')
G.edge['ime_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr]'
G.add_edge('ime_app','system_server')
G.edge['ime_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('ime_app','vmwared')
G.edge['ime_app']['vmwared']['write-read'] = '[open open][setattr getattr]'
G.add_edge('ime_app','wpa')
G.edge['ime_app']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('ime_app','zygote')
G.edge['ime_app']['zygote']['write-read'] = '[open open][setattr getattr]'
G.add_edge('ime_app','adbd')
G.edge['ime_app']['adbd']['write-read'] = '[write read]'
G.edge['ime_app']['adbd']['fill'] = 'red'
G.add_edge('ime_app','at_distributor')
G.edge['ime_app']['at_distributor']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['ime_app']['at_distributor']['fill'] = 'red'
G.add_edge('ime_app','cbd')
G.edge['ime_app']['cbd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['ime_app']['cbd']['fill'] = 'red'
G.add_edge('ime_app','charon')
G.edge['ime_app']['charon']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['ime_app']['charon']['fill'] = 'red'
G.add_edge('ime_app','debuggerd')
G.edge['ime_app']['debuggerd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['ime_app']['debuggerd']['fill'] = 'red'
G.add_edge('ime_app','dhcp')
G.edge['ime_app']['dhcp']['write-read'] = '[write read]'
G.edge['ime_app']['dhcp']['fill'] = 'red'
G.add_edge('ime_app','diag_uart_log')
G.edge['ime_app']['diag_uart_log']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['ime_app']['diag_uart_log']['fill'] = 'red'
G.add_edge('ime_app','domain')
G.edge['ime_app']['domain']['write-read'] = '[write read]'
G.edge['ime_app']['domain']['fill'] = 'red'
G.add_edge('ime_app','dumpstate')
G.edge['ime_app']['dumpstate']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['ime_app']['dumpstate']['fill'] = 'red'
G.add_edge('ime_app','hostapd')
G.edge['ime_app']['hostapd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read]'
G.edge['ime_app']['hostapd']['fill'] = 'red'
G.add_edge('ime_app','ime_app')
G.edge['ime_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read]'
G.edge['ime_app']['ime_app']['fill'] = 'red'
G.add_edge('ime_app','init_shell')
G.edge['ime_app']['init_shell']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['ime_app']['init_shell']['fill'] = 'red'
G.add_edge('ime_app','installd')
G.edge['ime_app']['installd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['ime_app']['installd']['fill'] = 'red'
G.add_edge('ime_app','itsonbs')
G.edge['ime_app']['itsonbs']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['ime_app']['itsonbs']['fill'] = 'red'
G.add_edge('ime_app','logwrapper')
G.edge['ime_app']['logwrapper']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read]'
G.edge['ime_app']['logwrapper']['fill'] = 'red'
G.add_edge('ime_app','netd')
G.edge['ime_app']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['ime_app']['netd']['fill'] = 'red'
G.add_edge('ime_app','qmuxd')
G.edge['ime_app']['qmuxd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['ime_app']['qmuxd']['fill'] = 'red'
G.add_edge('ime_app','rild')
G.edge['ime_app']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read]'
G.edge['ime_app']['rild']['fill'] = 'red'
G.add_edge('ime_app','rmt_storage')
G.edge['ime_app']['rmt_storage']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['ime_app']['rmt_storage']['fill'] = 'red'
G.add_edge('ime_app','sdcardd')
G.edge['ime_app']['sdcardd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['ime_app']['sdcardd']['fill'] = 'red'
G.add_edge('ime_app','shell')
G.edge['ime_app']['shell']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['ime_app']['shell']['fill'] = 'red'
G.add_edge('ime_app','s_system_app')
G.edge['ime_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['ime_app']['s_system_app']['fill'] = 'red'
G.add_edge('ime_app','system_app')
G.edge['ime_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read]'
G.edge['ime_app']['system_app']['fill'] = 'red'
G.add_edge('ime_app','system_server')
G.edge['ime_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['ime_app']['system_server']['fill'] = 'red'
G.add_edge('ime_app','vmwared')
G.edge['ime_app']['vmwared']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['ime_app']['vmwared']['fill'] = 'red'
G.add_edge('ime_app','wpa')
G.edge['ime_app']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['ime_app']['wpa']['fill'] = 'red'
G.add_edge('ime_app','zygote')
G.edge['ime_app']['zygote']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['ime_app']['zygote']['fill'] = 'red'
G.add_edge('ime_app','adbd')
G.edge['ime_app']['adbd']['write-read'] = '[write read][add_name search]'
G.add_edge('ime_app','at_distributor')
G.edge['ime_app']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('ime_app','at_distributor')
G.edge['ime_app']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('ime_app','auditd')
G.edge['ime_app']['auditd']['write-read'] = '[add_name search]'
G.add_edge('ime_app','cbd')
G.edge['ime_app']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('ime_app','cbd')
G.edge['ime_app']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('ime_app','charon')
G.edge['ime_app']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('ime_app','charon')
G.edge['ime_app']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('ime_app','clatd')
G.edge['ime_app']['clatd']['write-read'] = '[add_name search]'
G.add_edge('ime_app','debuggerd')
G.edge['ime_app']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('ime_app','debuggerd')
G.edge['ime_app']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('ime_app','dhcp')
G.edge['ime_app']['dhcp']['write-read'] = '[write read][add_name search]'
G.add_edge('ime_app','diag_uart_log')
G.edge['ime_app']['diag_uart_log']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('ime_app','diag_uart_log')
G.edge['ime_app']['diag_uart_log']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('ime_app','dumpstate')
G.edge['ime_app']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('ime_app','dumpstate')
G.edge['ime_app']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('ime_app','hostapd')
G.edge['ime_app']['hostapd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('ime_app','hostapd')
G.edge['ime_app']['hostapd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('ime_app','hvdcp')
G.edge['ime_app']['hvdcp']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][add_name search]'
G.add_edge('ime_app','ime_app')
G.edge['ime_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search]'
G.add_edge('ime_app','ime_app')
G.edge['ime_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('ime_app','init_shell')
G.edge['ime_app']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('ime_app','init_shell')
G.edge['ime_app']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('ime_app','installd')
G.edge['ime_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('ime_app','installd')
G.edge['ime_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('ime_app','itsonbs')
G.edge['ime_app']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('ime_app','itsonbs')
G.edge['ime_app']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('ime_app','jackservice')
G.edge['ime_app']['jackservice']['write-read'] = '[add_name search]'
G.add_edge('ime_app','lmkd')
G.edge['ime_app']['lmkd']['write-read'] = '[remove_name search]'
G.add_edge('ime_app','logwrapper')
G.edge['ime_app']['logwrapper']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('ime_app','logwrapper')
G.edge['ime_app']['logwrapper']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('ime_app','msm_irqbalanced')
G.edge['ime_app']['msm_irqbalanced']['write-read'] = '[add_name search]'
G.add_edge('ime_app','netd')
G.edge['ime_app']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('ime_app','netd')
G.edge['ime_app']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('ime_app','qmuxd')
G.edge['ime_app']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('ime_app','qmuxd')
G.edge['ime_app']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('ime_app','racoon')
G.edge['ime_app']['racoon']['write-read'] = '[add_name search]'
G.add_edge('ime_app','rild')
G.edge['ime_app']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search]'
G.add_edge('ime_app','rild')
G.edge['ime_app']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('ime_app','rmt_storage')
G.edge['ime_app']['rmt_storage']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('ime_app','rmt_storage')
G.edge['ime_app']['rmt_storage']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('ime_app','sdcardd')
G.edge['ime_app']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('ime_app','sdcardd')
G.edge['ime_app']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('ime_app','sensors')
G.edge['ime_app']['sensors']['write-read'] = '[add_name search]'
G.add_edge('ime_app','shell')
G.edge['ime_app']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('ime_app','shell')
G.edge['ime_app']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('ime_app','s_system_app')
G.edge['ime_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('ime_app','s_system_app')
G.edge['ime_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('ime_app','system_app')
G.edge['ime_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search]'
G.add_edge('ime_app','system_app')
G.edge['ime_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('ime_app','system_server')
G.edge['ime_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('ime_app','system_server')
G.edge['ime_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('ime_app','system_server')
G.edge['ime_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search]'
G.add_edge('ime_app','vmwared')
G.edge['ime_app']['vmwared']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('ime_app','vmwared')
G.edge['ime_app']['vmwared']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('ime_app','wpa')
G.edge['ime_app']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('ime_app','wpa')
G.edge['ime_app']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('ime_app','zygote')
G.edge['ime_app']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('ime_app','zygote')
G.edge['ime_app']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('init_shell','at_distributor')
G.edge['init_shell']['at_distributor']['write-read'] = '[open open]'
G.add_edge('init_shell','cbd')
G.edge['init_shell']['cbd']['write-read'] = '[open open]'
G.add_edge('init_shell','charon')
G.edge['init_shell']['charon']['write-read'] = '[open open]'
G.add_edge('init_shell','debuggerd')
G.edge['init_shell']['debuggerd']['write-read'] = '[open open]'
G.add_edge('init_shell','diag_uart_log')
G.edge['init_shell']['diag_uart_log']['write-read'] = '[open open]'
G.add_edge('init_shell','dumpstate')
G.edge['init_shell']['dumpstate']['write-read'] = '[open open]'
G.add_edge('init_shell','hostapd')
G.edge['init_shell']['hostapd']['write-read'] = '[open open]'
G.add_edge('init_shell','ime_app')
G.edge['init_shell']['ime_app']['write-read'] = '[open open]'
G.add_edge('init_shell','init_shell')
G.edge['init_shell']['init_shell']['write-read'] = '[open open][open open]'
G.add_edge('init_shell','installd')
G.edge['init_shell']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('init_shell','itsonbs')
G.edge['init_shell']['itsonbs']['write-read'] = '[open open]'
G.add_edge('init_shell','logwrapper')
G.edge['init_shell']['logwrapper']['write-read'] = '[open open]'
G.add_edge('init_shell','netd')
G.edge['init_shell']['netd']['write-read'] = '[open open]'
G.add_edge('init_shell','qmuxd')
G.edge['init_shell']['qmuxd']['write-read'] = '[open open]'
G.add_edge('init_shell','rild')
G.edge['init_shell']['rild']['write-read'] = '[open open]'
G.add_edge('init_shell','rmt_storage')
G.edge['init_shell']['rmt_storage']['write-read'] = '[open open]'
G.add_edge('init_shell','sdcardd')
G.edge['init_shell']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('init_shell','shell')
G.edge['init_shell']['shell']['write-read'] = '[open open]'
G.add_edge('init_shell','s_system_app')
G.edge['init_shell']['s_system_app']['write-read'] = '[open open]'
G.add_edge('init_shell','system_app')
G.edge['init_shell']['system_app']['write-read'] = '[open open]'
G.add_edge('init_shell','system_server')
G.edge['init_shell']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('init_shell','vmwared')
G.edge['init_shell']['vmwared']['write-read'] = '[open open]'
G.add_edge('init_shell','wpa')
G.edge['init_shell']['wpa']['write-read'] = '[open open]'
G.add_edge('init_shell','zygote')
G.edge['init_shell']['zygote']['write-read'] = '[open open]'
G.add_edge('init_shell','at_distributor')
G.edge['init_shell']['at_distributor']['write-read'] = '[open open][setattr getattr]'
G.add_edge('init_shell','cbd')
G.edge['init_shell']['cbd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('init_shell','charon')
G.edge['init_shell']['charon']['write-read'] = '[open open][setattr getattr]'
G.add_edge('init_shell','debuggerd')
G.edge['init_shell']['debuggerd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('init_shell','diag_uart_log')
G.edge['init_shell']['diag_uart_log']['write-read'] = '[open open][setattr getattr]'
G.add_edge('init_shell','dumpstate')
G.edge['init_shell']['dumpstate']['write-read'] = '[open open][setattr getattr]'
G.add_edge('init_shell','hostapd')
G.edge['init_shell']['hostapd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('init_shell','ime_app')
G.edge['init_shell']['ime_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('init_shell','init_shell')
G.edge['init_shell']['init_shell']['write-read'] = '[open open][open open][setattr getattr]'
G.add_edge('init_shell','installd')
G.edge['init_shell']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('init_shell','itsonbs')
G.edge['init_shell']['itsonbs']['write-read'] = '[open open][setattr getattr]'
G.add_edge('init_shell','logwrapper')
G.edge['init_shell']['logwrapper']['write-read'] = '[open open][setattr getattr]'
G.add_edge('init_shell','netd')
G.edge['init_shell']['netd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('init_shell','qmuxd')
G.edge['init_shell']['qmuxd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('init_shell','rild')
G.edge['init_shell']['rild']['write-read'] = '[open open][setattr getattr]'
G.add_edge('init_shell','rmt_storage')
G.edge['init_shell']['rmt_storage']['write-read'] = '[open open][setattr getattr]'
G.add_edge('init_shell','sdcardd')
G.edge['init_shell']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('init_shell','shell')
G.edge['init_shell']['shell']['write-read'] = '[open open][setattr getattr]'
G.add_edge('init_shell','s_system_app')
G.edge['init_shell']['s_system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('init_shell','system_app')
G.edge['init_shell']['system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('init_shell','system_server')
G.edge['init_shell']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('init_shell','vmwared')
G.edge['init_shell']['vmwared']['write-read'] = '[open open][setattr getattr]'
G.add_edge('init_shell','wpa')
G.edge['init_shell']['wpa']['write-read'] = '[open open][setattr getattr]'
G.add_edge('init_shell','zygote')
G.edge['init_shell']['zygote']['write-read'] = '[open open][setattr getattr]'
G.add_edge('init_shell','adbd')
G.edge['init_shell']['adbd']['write-read'] = '[write read]'
G.edge['init_shell']['adbd']['fill'] = 'red'
G.add_edge('init_shell','at_distributor')
G.edge['init_shell']['at_distributor']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['init_shell']['at_distributor']['fill'] = 'red'
G.add_edge('init_shell','cbd')
G.edge['init_shell']['cbd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['init_shell']['cbd']['fill'] = 'red'
G.add_edge('init_shell','charon')
G.edge['init_shell']['charon']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['init_shell']['charon']['fill'] = 'red'
G.add_edge('init_shell','debuggerd')
G.edge['init_shell']['debuggerd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['init_shell']['debuggerd']['fill'] = 'red'
G.add_edge('init_shell','dhcp')
G.edge['init_shell']['dhcp']['write-read'] = '[write read]'
G.edge['init_shell']['dhcp']['fill'] = 'red'
G.add_edge('init_shell','diag_uart_log')
G.edge['init_shell']['diag_uart_log']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['init_shell']['diag_uart_log']['fill'] = 'red'
G.add_edge('init_shell','domain')
G.edge['init_shell']['domain']['write-read'] = '[write read]'
G.edge['init_shell']['domain']['fill'] = 'red'
G.add_edge('init_shell','dumpstate')
G.edge['init_shell']['dumpstate']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['init_shell']['dumpstate']['fill'] = 'red'
G.add_edge('init_shell','hostapd')
G.edge['init_shell']['hostapd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['init_shell']['hostapd']['fill'] = 'red'
G.add_edge('init_shell','ime_app')
G.edge['init_shell']['ime_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['init_shell']['ime_app']['fill'] = 'red'
G.add_edge('init_shell','init_shell')
G.edge['init_shell']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read]'
G.edge['init_shell']['init_shell']['fill'] = 'red'
G.add_edge('init_shell','installd')
G.edge['init_shell']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['init_shell']['installd']['fill'] = 'red'
G.add_edge('init_shell','itsonbs')
G.edge['init_shell']['itsonbs']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['init_shell']['itsonbs']['fill'] = 'red'
G.add_edge('init_shell','logwrapper')
G.edge['init_shell']['logwrapper']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['init_shell']['logwrapper']['fill'] = 'red'
G.add_edge('init_shell','netd')
G.edge['init_shell']['netd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['init_shell']['netd']['fill'] = 'red'
G.add_edge('init_shell','qmuxd')
G.edge['init_shell']['qmuxd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['init_shell']['qmuxd']['fill'] = 'red'
G.add_edge('init_shell','rild')
G.edge['init_shell']['rild']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['init_shell']['rild']['fill'] = 'red'
G.add_edge('init_shell','rmt_storage')
G.edge['init_shell']['rmt_storage']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['init_shell']['rmt_storage']['fill'] = 'red'
G.add_edge('init_shell','sdcardd')
G.edge['init_shell']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['init_shell']['sdcardd']['fill'] = 'red'
G.add_edge('init_shell','shell')
G.edge['init_shell']['shell']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['init_shell']['shell']['fill'] = 'red'
G.add_edge('init_shell','s_system_app')
G.edge['init_shell']['s_system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['init_shell']['s_system_app']['fill'] = 'red'
G.add_edge('init_shell','system_app')
G.edge['init_shell']['system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['init_shell']['system_app']['fill'] = 'red'
G.add_edge('init_shell','system_server')
G.edge['init_shell']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['init_shell']['system_server']['fill'] = 'red'
G.add_edge('init_shell','vmwared')
G.edge['init_shell']['vmwared']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['init_shell']['vmwared']['fill'] = 'red'
G.add_edge('init_shell','wpa')
G.edge['init_shell']['wpa']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['init_shell']['wpa']['fill'] = 'red'
G.add_edge('init_shell','zygote')
G.edge['init_shell']['zygote']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['init_shell']['zygote']['fill'] = 'red'
G.add_edge('init_shell','adbd')
G.edge['init_shell']['adbd']['write-read'] = '[write read][add_name search]'
G.add_edge('init_shell','at_distributor')
G.edge['init_shell']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('init_shell','at_distributor')
G.edge['init_shell']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('init_shell','auditd')
G.edge['init_shell']['auditd']['write-read'] = '[add_name search]'
G.add_edge('init_shell','cbd')
G.edge['init_shell']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('init_shell','cbd')
G.edge['init_shell']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('init_shell','charon')
G.edge['init_shell']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('init_shell','charon')
G.edge['init_shell']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('init_shell','clatd')
G.edge['init_shell']['clatd']['write-read'] = '[add_name search]'
G.add_edge('init_shell','debuggerd')
G.edge['init_shell']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('init_shell','debuggerd')
G.edge['init_shell']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('init_shell','dhcp')
G.edge['init_shell']['dhcp']['write-read'] = '[write read][add_name search]'
G.add_edge('init_shell','diag_uart_log')
G.edge['init_shell']['diag_uart_log']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('init_shell','diag_uart_log')
G.edge['init_shell']['diag_uart_log']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('init_shell','dumpstate')
G.edge['init_shell']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('init_shell','dumpstate')
G.edge['init_shell']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('init_shell','hostapd')
G.edge['init_shell']['hostapd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('init_shell','hostapd')
G.edge['init_shell']['hostapd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('init_shell','hvdcp')
G.edge['init_shell']['hvdcp']['write-read'] = '[add_name search]'
G.add_edge('init_shell','ime_app')
G.edge['init_shell']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('init_shell','ime_app')
G.edge['init_shell']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('init_shell','init_shell')
G.edge['init_shell']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search]'
G.add_edge('init_shell','init_shell')
G.edge['init_shell']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('init_shell','installd')
G.edge['init_shell']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('init_shell','installd')
G.edge['init_shell']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('init_shell','itsonbs')
G.edge['init_shell']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('init_shell','itsonbs')
G.edge['init_shell']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('init_shell','jackservice')
G.edge['init_shell']['jackservice']['write-read'] = '[add_name search]'
G.add_edge('init_shell','lmkd')
G.edge['init_shell']['lmkd']['write-read'] = '[remove_name search]'
G.add_edge('init_shell','logwrapper')
G.edge['init_shell']['logwrapper']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('init_shell','logwrapper')
G.edge['init_shell']['logwrapper']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('init_shell','msm_irqbalanced')
G.edge['init_shell']['msm_irqbalanced']['write-read'] = '[add_name search]'
G.add_edge('init_shell','netd')
G.edge['init_shell']['netd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('init_shell','netd')
G.edge['init_shell']['netd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('init_shell','qmuxd')
G.edge['init_shell']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('init_shell','qmuxd')
G.edge['init_shell']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('init_shell','racoon')
G.edge['init_shell']['racoon']['write-read'] = '[add_name search]'
G.add_edge('init_shell','rild')
G.edge['init_shell']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('init_shell','rild')
G.edge['init_shell']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('init_shell','rmt_storage')
G.edge['init_shell']['rmt_storage']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('init_shell','rmt_storage')
G.edge['init_shell']['rmt_storage']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('init_shell','sdcardd')
G.edge['init_shell']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('init_shell','sdcardd')
G.edge['init_shell']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('init_shell','sensors')
G.edge['init_shell']['sensors']['write-read'] = '[add_name search]'
G.add_edge('init_shell','shell')
G.edge['init_shell']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('init_shell','shell')
G.edge['init_shell']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('init_shell','s_system_app')
G.edge['init_shell']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('init_shell','s_system_app')
G.edge['init_shell']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('init_shell','system_app')
G.edge['init_shell']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('init_shell','system_app')
G.edge['init_shell']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('init_shell','system_server')
G.edge['init_shell']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('init_shell','system_server')
G.edge['init_shell']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('init_shell','system_server')
G.edge['init_shell']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search]'
G.add_edge('init_shell','vmwared')
G.edge['init_shell']['vmwared']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('init_shell','vmwared')
G.edge['init_shell']['vmwared']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('init_shell','wpa')
G.edge['init_shell']['wpa']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('init_shell','wpa')
G.edge['init_shell']['wpa']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('init_shell','zygote')
G.edge['init_shell']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('init_shell','zygote')
G.edge['init_shell']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('installd','at_distributor')
G.edge['installd']['at_distributor']['write-read'] = '[open open]'
G.add_edge('installd','cbd')
G.edge['installd']['cbd']['write-read'] = '[open open]'
G.add_edge('installd','charon')
G.edge['installd']['charon']['write-read'] = '[open open]'
G.add_edge('installd','debuggerd')
G.edge['installd']['debuggerd']['write-read'] = '[open open]'
G.add_edge('installd','diag_uart_log')
G.edge['installd']['diag_uart_log']['write-read'] = '[open open]'
G.add_edge('installd','dumpstate')
G.edge['installd']['dumpstate']['write-read'] = '[open open]'
G.add_edge('installd','hostapd')
G.edge['installd']['hostapd']['write-read'] = '[open open]'
G.add_edge('installd','ime_app')
G.edge['installd']['ime_app']['write-read'] = '[open open]'
G.add_edge('installd','init_shell')
G.edge['installd']['init_shell']['write-read'] = '[open open][open open]'
G.add_edge('installd','installd')
G.edge['installd']['installd']['write-read'] = '[setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][append read][relabelto relabelfrom][setattr getattr][relabelto relabelfrom][open open]'
G.add_edge('installd','itsonbs')
G.edge['installd']['itsonbs']['write-read'] = '[open open]'
G.add_edge('installd','logwrapper')
G.edge['installd']['logwrapper']['write-read'] = '[open open]'
G.add_edge('installd','netd')
G.edge['installd']['netd']['write-read'] = '[open open]'
G.add_edge('installd','qmuxd')
G.edge['installd']['qmuxd']['write-read'] = '[open open]'
G.add_edge('installd','rild')
G.edge['installd']['rild']['write-read'] = '[open open]'
G.add_edge('installd','rmt_storage')
G.edge['installd']['rmt_storage']['write-read'] = '[open open]'
G.add_edge('installd','sdcardd')
G.edge['installd']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('installd','shell')
G.edge['installd']['shell']['write-read'] = '[open open]'
G.add_edge('installd','s_system_app')
G.edge['installd']['s_system_app']['write-read'] = '[open open]'
G.add_edge('installd','system_app')
G.edge['installd']['system_app']['write-read'] = '[open open]'
G.add_edge('installd','system_server')
G.edge['installd']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][relabelto relabelfrom][open open]'
G.add_edge('installd','vmwared')
G.edge['installd']['vmwared']['write-read'] = '[open open]'
G.add_edge('installd','wpa')
G.edge['installd']['wpa']['write-read'] = '[open open]'
G.add_edge('installd','zygote')
G.edge['installd']['zygote']['write-read'] = '[open open]'
G.add_edge('installd','at_distributor')
G.edge['installd']['at_distributor']['write-read'] = '[open open][setattr getattr]'
G.add_edge('installd','cbd')
G.edge['installd']['cbd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('installd','charon')
G.edge['installd']['charon']['write-read'] = '[open open][setattr getattr]'
G.add_edge('installd','debuggerd')
G.edge['installd']['debuggerd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('installd','diag_uart_log')
G.edge['installd']['diag_uart_log']['write-read'] = '[open open][setattr getattr]'
G.add_edge('installd','dumpstate')
G.edge['installd']['dumpstate']['write-read'] = '[open open][setattr getattr]'
G.add_edge('installd','hostapd')
G.edge['installd']['hostapd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('installd','ime_app')
G.edge['installd']['ime_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('installd','init_shell')
G.edge['installd']['init_shell']['write-read'] = '[open open][open open][setattr getattr]'
G.add_edge('installd','installd')
G.edge['installd']['installd']['write-read'] = '[setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][append read][relabelto relabelfrom][setattr getattr][relabelto relabelfrom][open open][setattr getattr]'
G.add_edge('installd','itsonbs')
G.edge['installd']['itsonbs']['write-read'] = '[open open][setattr getattr]'
G.add_edge('installd','logwrapper')
G.edge['installd']['logwrapper']['write-read'] = '[open open][setattr getattr]'
G.add_edge('installd','netd')
G.edge['installd']['netd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('installd','qmuxd')
G.edge['installd']['qmuxd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('installd','rild')
G.edge['installd']['rild']['write-read'] = '[open open][setattr getattr]'
G.add_edge('installd','rmt_storage')
G.edge['installd']['rmt_storage']['write-read'] = '[open open][setattr getattr]'
G.add_edge('installd','sdcardd')
G.edge['installd']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('installd','shell')
G.edge['installd']['shell']['write-read'] = '[open open][setattr getattr]'
G.add_edge('installd','s_system_app')
G.edge['installd']['s_system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('installd','system_app')
G.edge['installd']['system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('installd','system_server')
G.edge['installd']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr]'
G.add_edge('installd','vmwared')
G.edge['installd']['vmwared']['write-read'] = '[open open][setattr getattr]'
G.add_edge('installd','wpa')
G.edge['installd']['wpa']['write-read'] = '[open open][setattr getattr]'
G.add_edge('installd','zygote')
G.edge['installd']['zygote']['write-read'] = '[open open][setattr getattr]'
G.add_edge('installd','adbd')
G.edge['installd']['adbd']['write-read'] = '[write read]'
G.edge['installd']['adbd']['fill'] = 'red'
G.add_edge('installd','at_distributor')
G.edge['installd']['at_distributor']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['installd']['at_distributor']['fill'] = 'red'
G.add_edge('installd','cbd')
G.edge['installd']['cbd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['installd']['cbd']['fill'] = 'red'
G.add_edge('installd','charon')
G.edge['installd']['charon']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['installd']['charon']['fill'] = 'red'
G.add_edge('installd','debuggerd')
G.edge['installd']['debuggerd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['installd']['debuggerd']['fill'] = 'red'
G.add_edge('installd','dhcp')
G.edge['installd']['dhcp']['write-read'] = '[write read]'
G.edge['installd']['dhcp']['fill'] = 'red'
G.add_edge('installd','diag_uart_log')
G.edge['installd']['diag_uart_log']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['installd']['diag_uart_log']['fill'] = 'red'
G.add_edge('installd','domain')
G.edge['installd']['domain']['write-read'] = '[write read]'
G.edge['installd']['domain']['fill'] = 'red'
G.add_edge('installd','dumpstate')
G.edge['installd']['dumpstate']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['installd']['dumpstate']['fill'] = 'red'
G.add_edge('installd','hostapd')
G.edge['installd']['hostapd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['installd']['hostapd']['fill'] = 'red'
G.add_edge('installd','ime_app')
G.edge['installd']['ime_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['installd']['ime_app']['fill'] = 'red'
G.add_edge('installd','init_shell')
G.edge['installd']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read]'
G.edge['installd']['init_shell']['fill'] = 'red'
G.add_edge('installd','installd')
G.edge['installd']['installd']['write-read'] = '[setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][append read][relabelto relabelfrom][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read]'
G.edge['installd']['installd']['fill'] = 'red'
G.add_edge('installd','itsonbs')
G.edge['installd']['itsonbs']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['installd']['itsonbs']['fill'] = 'red'
G.add_edge('installd','logwrapper')
G.edge['installd']['logwrapper']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['installd']['logwrapper']['fill'] = 'red'
G.add_edge('installd','netd')
G.edge['installd']['netd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['installd']['netd']['fill'] = 'red'
G.add_edge('installd','qmuxd')
G.edge['installd']['qmuxd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['installd']['qmuxd']['fill'] = 'red'
G.add_edge('installd','rild')
G.edge['installd']['rild']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['installd']['rild']['fill'] = 'red'
G.add_edge('installd','rmt_storage')
G.edge['installd']['rmt_storage']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['installd']['rmt_storage']['fill'] = 'red'
G.add_edge('installd','sdcardd')
G.edge['installd']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['installd']['sdcardd']['fill'] = 'red'
G.add_edge('installd','shell')
G.edge['installd']['shell']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['installd']['shell']['fill'] = 'red'
G.add_edge('installd','s_system_app')
G.edge['installd']['s_system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['installd']['s_system_app']['fill'] = 'red'
G.add_edge('installd','system_app')
G.edge['installd']['system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['installd']['system_app']['fill'] = 'red'
G.add_edge('installd','system_server')
G.edge['installd']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read]'
G.edge['installd']['system_server']['fill'] = 'red'
G.add_edge('installd','vmwared')
G.edge['installd']['vmwared']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['installd']['vmwared']['fill'] = 'red'
G.add_edge('installd','wpa')
G.edge['installd']['wpa']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['installd']['wpa']['fill'] = 'red'
G.add_edge('installd','zygote')
G.edge['installd']['zygote']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['installd']['zygote']['fill'] = 'red'
G.add_edge('installd','adbd')
G.edge['installd']['adbd']['write-read'] = '[write read][add_name search]'
G.add_edge('installd','at_distributor')
G.edge['installd']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('installd','at_distributor')
G.edge['installd']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('installd','auditd')
G.edge['installd']['auditd']['write-read'] = '[add_name search]'
G.add_edge('installd','cbd')
G.edge['installd']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('installd','cbd')
G.edge['installd']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('installd','charon')
G.edge['installd']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('installd','charon')
G.edge['installd']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('installd','clatd')
G.edge['installd']['clatd']['write-read'] = '[add_name search]'
G.add_edge('installd','debuggerd')
G.edge['installd']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('installd','debuggerd')
G.edge['installd']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('installd','dhcp')
G.edge['installd']['dhcp']['write-read'] = '[write read][add_name search]'
G.add_edge('installd','diag_uart_log')
G.edge['installd']['diag_uart_log']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('installd','diag_uart_log')
G.edge['installd']['diag_uart_log']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('installd','dumpstate')
G.edge['installd']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('installd','dumpstate')
G.edge['installd']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('installd','hostapd')
G.edge['installd']['hostapd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('installd','hostapd')
G.edge['installd']['hostapd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('installd','hvdcp')
G.edge['installd']['hvdcp']['write-read'] = '[add_name search]'
G.add_edge('installd','ime_app')
G.edge['installd']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('installd','ime_app')
G.edge['installd']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('installd','init_shell')
G.edge['installd']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search]'
G.add_edge('installd','init_shell')
G.edge['installd']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('installd','installd')
G.edge['installd']['installd']['write-read'] = '[setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][append read][relabelto relabelfrom][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search]'
G.add_edge('installd','installd')
G.edge['installd']['installd']['write-read'] = '[setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][append read][relabelto relabelfrom][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('installd','itsonbs')
G.edge['installd']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('installd','itsonbs')
G.edge['installd']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('installd','jackservice')
G.edge['installd']['jackservice']['write-read'] = '[add_name search]'
G.add_edge('installd','lmkd')
G.edge['installd']['lmkd']['write-read'] = '[remove_name search]'
G.add_edge('installd','logwrapper')
G.edge['installd']['logwrapper']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('installd','logwrapper')
G.edge['installd']['logwrapper']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('installd','msm_irqbalanced')
G.edge['installd']['msm_irqbalanced']['write-read'] = '[add_name search]'
G.add_edge('installd','netd')
G.edge['installd']['netd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('installd','netd')
G.edge['installd']['netd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('installd','qmuxd')
G.edge['installd']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('installd','qmuxd')
G.edge['installd']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('installd','racoon')
G.edge['installd']['racoon']['write-read'] = '[add_name search]'
G.add_edge('installd','rild')
G.edge['installd']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('installd','rild')
G.edge['installd']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('installd','rmt_storage')
G.edge['installd']['rmt_storage']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('installd','rmt_storage')
G.edge['installd']['rmt_storage']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('installd','sdcardd')
G.edge['installd']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('installd','sdcardd')
G.edge['installd']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('installd','sensors')
G.edge['installd']['sensors']['write-read'] = '[add_name search]'
G.add_edge('installd','shell')
G.edge['installd']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('installd','shell')
G.edge['installd']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('installd','s_system_app')
G.edge['installd']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('installd','s_system_app')
G.edge['installd']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('installd','system_app')
G.edge['installd']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('installd','system_app')
G.edge['installd']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('installd','system_server')
G.edge['installd']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search]'
G.add_edge('installd','system_server')
G.edge['installd']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('installd','system_server')
G.edge['installd']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search]'
G.add_edge('installd','vmwared')
G.edge['installd']['vmwared']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('installd','vmwared')
G.edge['installd']['vmwared']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('installd','wpa')
G.edge['installd']['wpa']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('installd','wpa')
G.edge['installd']['wpa']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('installd','zygote')
G.edge['installd']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('installd','zygote')
G.edge['installd']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('itsonbs','at_distributor')
G.edge['itsonbs']['at_distributor']['write-read'] = '[open open]'
G.add_edge('itsonbs','cbd')
G.edge['itsonbs']['cbd']['write-read'] = '[open open]'
G.add_edge('itsonbs','charon')
G.edge['itsonbs']['charon']['write-read'] = '[open open]'
G.add_edge('itsonbs','debuggerd')
G.edge['itsonbs']['debuggerd']['write-read'] = '[open open]'
G.add_edge('itsonbs','diag_uart_log')
G.edge['itsonbs']['diag_uart_log']['write-read'] = '[open open]'
G.add_edge('itsonbs','dumpstate')
G.edge['itsonbs']['dumpstate']['write-read'] = '[open open]'
G.add_edge('itsonbs','hostapd')
G.edge['itsonbs']['hostapd']['write-read'] = '[open open]'
G.add_edge('itsonbs','ime_app')
G.edge['itsonbs']['ime_app']['write-read'] = '[open open]'
G.add_edge('itsonbs','init_shell')
G.edge['itsonbs']['init_shell']['write-read'] = '[open open]'
G.add_edge('itsonbs','installd')
G.edge['itsonbs']['installd']['write-read'] = '[open open]'
G.add_edge('itsonbs','itsonbs')
G.edge['itsonbs']['itsonbs']['write-read'] = '[open open]'
G.add_edge('itsonbs','logwrapper')
G.edge['itsonbs']['logwrapper']['write-read'] = '[open open]'
G.add_edge('itsonbs','netd')
G.edge['itsonbs']['netd']['write-read'] = '[open open]'
G.add_edge('itsonbs','qmuxd')
G.edge['itsonbs']['qmuxd']['write-read'] = '[open open]'
G.add_edge('itsonbs','rild')
G.edge['itsonbs']['rild']['write-read'] = '[open open]'
G.add_edge('itsonbs','rmt_storage')
G.edge['itsonbs']['rmt_storage']['write-read'] = '[open open]'
G.add_edge('itsonbs','sdcardd')
G.edge['itsonbs']['sdcardd']['write-read'] = '[open open]'
G.add_edge('itsonbs','shell')
G.edge['itsonbs']['shell']['write-read'] = '[open open]'
G.add_edge('itsonbs','s_system_app')
G.edge['itsonbs']['s_system_app']['write-read'] = '[open open]'
G.add_edge('itsonbs','system_app')
G.edge['itsonbs']['system_app']['write-read'] = '[open open]'
G.add_edge('itsonbs','system_server')
G.edge['itsonbs']['system_server']['write-read'] = '[open open]'
G.add_edge('itsonbs','vmwared')
G.edge['itsonbs']['vmwared']['write-read'] = '[open open]'
G.add_edge('itsonbs','wpa')
G.edge['itsonbs']['wpa']['write-read'] = '[open open]'
G.add_edge('itsonbs','zygote')
G.edge['itsonbs']['zygote']['write-read'] = '[open open]'
G.add_edge('itsonbs','at_distributor')
G.edge['itsonbs']['at_distributor']['write-read'] = '[open open][setattr getattr]'
G.add_edge('itsonbs','cbd')
G.edge['itsonbs']['cbd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('itsonbs','charon')
G.edge['itsonbs']['charon']['write-read'] = '[open open][setattr getattr]'
G.add_edge('itsonbs','debuggerd')
G.edge['itsonbs']['debuggerd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('itsonbs','diag_uart_log')
G.edge['itsonbs']['diag_uart_log']['write-read'] = '[open open][setattr getattr]'
G.add_edge('itsonbs','dumpstate')
G.edge['itsonbs']['dumpstate']['write-read'] = '[open open][setattr getattr]'
G.add_edge('itsonbs','hostapd')
G.edge['itsonbs']['hostapd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('itsonbs','ime_app')
G.edge['itsonbs']['ime_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('itsonbs','init_shell')
G.edge['itsonbs']['init_shell']['write-read'] = '[open open][setattr getattr]'
G.add_edge('itsonbs','installd')
G.edge['itsonbs']['installd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('itsonbs','itsonbs')
G.edge['itsonbs']['itsonbs']['write-read'] = '[open open][setattr getattr]'
G.add_edge('itsonbs','logwrapper')
G.edge['itsonbs']['logwrapper']['write-read'] = '[open open][setattr getattr]'
G.add_edge('itsonbs','netd')
G.edge['itsonbs']['netd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('itsonbs','qmuxd')
G.edge['itsonbs']['qmuxd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('itsonbs','rild')
G.edge['itsonbs']['rild']['write-read'] = '[open open][setattr getattr]'
G.add_edge('itsonbs','rmt_storage')
G.edge['itsonbs']['rmt_storage']['write-read'] = '[open open][setattr getattr]'
G.add_edge('itsonbs','sdcardd')
G.edge['itsonbs']['sdcardd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('itsonbs','shell')
G.edge['itsonbs']['shell']['write-read'] = '[open open][setattr getattr]'
G.add_edge('itsonbs','s_system_app')
G.edge['itsonbs']['s_system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('itsonbs','system_app')
G.edge['itsonbs']['system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('itsonbs','system_server')
G.edge['itsonbs']['system_server']['write-read'] = '[open open][setattr getattr]'
G.add_edge('itsonbs','vmwared')
G.edge['itsonbs']['vmwared']['write-read'] = '[open open][setattr getattr]'
G.add_edge('itsonbs','wpa')
G.edge['itsonbs']['wpa']['write-read'] = '[open open][setattr getattr]'
G.add_edge('itsonbs','zygote')
G.edge['itsonbs']['zygote']['write-read'] = '[open open][setattr getattr]'
G.add_edge('itsonbs','adbd')
G.edge['itsonbs']['adbd']['write-read'] = '[write read]'
G.edge['itsonbs']['adbd']['fill'] = 'red'
G.add_edge('itsonbs','at_distributor')
G.edge['itsonbs']['at_distributor']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['itsonbs']['at_distributor']['fill'] = 'red'
G.add_edge('itsonbs','cbd')
G.edge['itsonbs']['cbd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['itsonbs']['cbd']['fill'] = 'red'
G.add_edge('itsonbs','charon')
G.edge['itsonbs']['charon']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['itsonbs']['charon']['fill'] = 'red'
G.add_edge('itsonbs','debuggerd')
G.edge['itsonbs']['debuggerd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['itsonbs']['debuggerd']['fill'] = 'red'
G.add_edge('itsonbs','dhcp')
G.edge['itsonbs']['dhcp']['write-read'] = '[write read]'
G.edge['itsonbs']['dhcp']['fill'] = 'red'
G.add_edge('itsonbs','diag_uart_log')
G.edge['itsonbs']['diag_uart_log']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['itsonbs']['diag_uart_log']['fill'] = 'red'
G.add_edge('itsonbs','domain')
G.edge['itsonbs']['domain']['write-read'] = '[write read]'
G.edge['itsonbs']['domain']['fill'] = 'red'
G.add_edge('itsonbs','dumpstate')
G.edge['itsonbs']['dumpstate']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['itsonbs']['dumpstate']['fill'] = 'red'
G.add_edge('itsonbs','hostapd')
G.edge['itsonbs']['hostapd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['itsonbs']['hostapd']['fill'] = 'red'
G.add_edge('itsonbs','ime_app')
G.edge['itsonbs']['ime_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['itsonbs']['ime_app']['fill'] = 'red'
G.add_edge('itsonbs','init_shell')
G.edge['itsonbs']['init_shell']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['itsonbs']['init_shell']['fill'] = 'red'
G.add_edge('itsonbs','installd')
G.edge['itsonbs']['installd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['itsonbs']['installd']['fill'] = 'red'
G.add_edge('itsonbs','itsonbs')
G.edge['itsonbs']['itsonbs']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['itsonbs']['itsonbs']['fill'] = 'red'
G.add_edge('itsonbs','logwrapper')
G.edge['itsonbs']['logwrapper']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['itsonbs']['logwrapper']['fill'] = 'red'
G.add_edge('itsonbs','netd')
G.edge['itsonbs']['netd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['itsonbs']['netd']['fill'] = 'red'
G.add_edge('itsonbs','qmuxd')
G.edge['itsonbs']['qmuxd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['itsonbs']['qmuxd']['fill'] = 'red'
G.add_edge('itsonbs','rild')
G.edge['itsonbs']['rild']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['itsonbs']['rild']['fill'] = 'red'
G.add_edge('itsonbs','rmt_storage')
G.edge['itsonbs']['rmt_storage']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['itsonbs']['rmt_storage']['fill'] = 'red'
G.add_edge('itsonbs','sdcardd')
G.edge['itsonbs']['sdcardd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['itsonbs']['sdcardd']['fill'] = 'red'
G.add_edge('itsonbs','shell')
G.edge['itsonbs']['shell']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['itsonbs']['shell']['fill'] = 'red'
G.add_edge('itsonbs','s_system_app')
G.edge['itsonbs']['s_system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['itsonbs']['s_system_app']['fill'] = 'red'
G.add_edge('itsonbs','system_app')
G.edge['itsonbs']['system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['itsonbs']['system_app']['fill'] = 'red'
G.add_edge('itsonbs','system_server')
G.edge['itsonbs']['system_server']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['itsonbs']['system_server']['fill'] = 'red'
G.add_edge('itsonbs','vmwared')
G.edge['itsonbs']['vmwared']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['itsonbs']['vmwared']['fill'] = 'red'
G.add_edge('itsonbs','wpa')
G.edge['itsonbs']['wpa']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['itsonbs']['wpa']['fill'] = 'red'
G.add_edge('itsonbs','zygote')
G.edge['itsonbs']['zygote']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['itsonbs']['zygote']['fill'] = 'red'
G.add_edge('itsonbs','adbd')
G.edge['itsonbs']['adbd']['write-read'] = '[write read][add_name search]'
G.add_edge('itsonbs','at_distributor')
G.edge['itsonbs']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('itsonbs','at_distributor')
G.edge['itsonbs']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('itsonbs','auditd')
G.edge['itsonbs']['auditd']['write-read'] = '[add_name search]'
G.add_edge('itsonbs','cbd')
G.edge['itsonbs']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('itsonbs','cbd')
G.edge['itsonbs']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('itsonbs','charon')
G.edge['itsonbs']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('itsonbs','charon')
G.edge['itsonbs']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('itsonbs','clatd')
G.edge['itsonbs']['clatd']['write-read'] = '[add_name search]'
G.add_edge('itsonbs','debuggerd')
G.edge['itsonbs']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('itsonbs','debuggerd')
G.edge['itsonbs']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('itsonbs','dhcp')
G.edge['itsonbs']['dhcp']['write-read'] = '[write read][add_name search]'
G.add_edge('itsonbs','diag_uart_log')
G.edge['itsonbs']['diag_uart_log']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('itsonbs','diag_uart_log')
G.edge['itsonbs']['diag_uart_log']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('itsonbs','dumpstate')
G.edge['itsonbs']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('itsonbs','dumpstate')
G.edge['itsonbs']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('itsonbs','hostapd')
G.edge['itsonbs']['hostapd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('itsonbs','hostapd')
G.edge['itsonbs']['hostapd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('itsonbs','hvdcp')
G.edge['itsonbs']['hvdcp']['write-read'] = '[add_name search]'
G.add_edge('itsonbs','ime_app')
G.edge['itsonbs']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('itsonbs','ime_app')
G.edge['itsonbs']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('itsonbs','init_shell')
G.edge['itsonbs']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('itsonbs','init_shell')
G.edge['itsonbs']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('itsonbs','installd')
G.edge['itsonbs']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('itsonbs','installd')
G.edge['itsonbs']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('itsonbs','itsonbs')
G.edge['itsonbs']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('itsonbs','itsonbs')
G.edge['itsonbs']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('itsonbs','jackservice')
G.edge['itsonbs']['jackservice']['write-read'] = '[add_name search]'
G.add_edge('itsonbs','lmkd')
G.edge['itsonbs']['lmkd']['write-read'] = '[remove_name search]'
G.add_edge('itsonbs','logwrapper')
G.edge['itsonbs']['logwrapper']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('itsonbs','logwrapper')
G.edge['itsonbs']['logwrapper']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('itsonbs','msm_irqbalanced')
G.edge['itsonbs']['msm_irqbalanced']['write-read'] = '[add_name search]'
G.add_edge('itsonbs','netd')
G.edge['itsonbs']['netd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('itsonbs','netd')
G.edge['itsonbs']['netd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('itsonbs','qmuxd')
G.edge['itsonbs']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('itsonbs','qmuxd')
G.edge['itsonbs']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('itsonbs','racoon')
G.edge['itsonbs']['racoon']['write-read'] = '[add_name search]'
G.add_edge('itsonbs','rild')
G.edge['itsonbs']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('itsonbs','rild')
G.edge['itsonbs']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('itsonbs','rmt_storage')
G.edge['itsonbs']['rmt_storage']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('itsonbs','rmt_storage')
G.edge['itsonbs']['rmt_storage']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('itsonbs','sdcardd')
G.edge['itsonbs']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('itsonbs','sdcardd')
G.edge['itsonbs']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('itsonbs','sensors')
G.edge['itsonbs']['sensors']['write-read'] = '[add_name search]'
G.add_edge('itsonbs','shell')
G.edge['itsonbs']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('itsonbs','shell')
G.edge['itsonbs']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('itsonbs','s_system_app')
G.edge['itsonbs']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('itsonbs','s_system_app')
G.edge['itsonbs']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('itsonbs','system_app')
G.edge['itsonbs']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('itsonbs','system_app')
G.edge['itsonbs']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('itsonbs','system_server')
G.edge['itsonbs']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('itsonbs','system_server')
G.edge['itsonbs']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('itsonbs','system_server')
G.edge['itsonbs']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search]'
G.add_edge('itsonbs','vmwared')
G.edge['itsonbs']['vmwared']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('itsonbs','vmwared')
G.edge['itsonbs']['vmwared']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('itsonbs','wpa')
G.edge['itsonbs']['wpa']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('itsonbs','wpa')
G.edge['itsonbs']['wpa']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('itsonbs','zygote')
G.edge['itsonbs']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('itsonbs','zygote')
G.edge['itsonbs']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('logwrapper','at_distributor')
G.edge['logwrapper']['at_distributor']['write-read'] = '[open open]'
G.add_edge('logwrapper','cbd')
G.edge['logwrapper']['cbd']['write-read'] = '[open open]'
G.add_edge('logwrapper','charon')
G.edge['logwrapper']['charon']['write-read'] = '[open open]'
G.add_edge('logwrapper','debuggerd')
G.edge['logwrapper']['debuggerd']['write-read'] = '[open open]'
G.add_edge('logwrapper','diag_uart_log')
G.edge['logwrapper']['diag_uart_log']['write-read'] = '[open open]'
G.add_edge('logwrapper','dumpstate')
G.edge['logwrapper']['dumpstate']['write-read'] = '[open open]'
G.add_edge('logwrapper','hostapd')
G.edge['logwrapper']['hostapd']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('logwrapper','ime_app')
G.edge['logwrapper']['ime_app']['write-read'] = '[open open]'
G.add_edge('logwrapper','init_shell')
G.edge['logwrapper']['init_shell']['write-read'] = '[open open]'
G.add_edge('logwrapper','installd')
G.edge['logwrapper']['installd']['write-read'] = '[open open]'
G.add_edge('logwrapper','itsonbs')
G.edge['logwrapper']['itsonbs']['write-read'] = '[open open]'
G.add_edge('logwrapper','logwrapper')
G.edge['logwrapper']['logwrapper']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('logwrapper','netd')
G.edge['logwrapper']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('logwrapper','qmuxd')
G.edge['logwrapper']['qmuxd']['write-read'] = '[open open]'
G.add_edge('logwrapper','rild')
G.edge['logwrapper']['rild']['write-read'] = '[open open]'
G.add_edge('logwrapper','rmt_storage')
G.edge['logwrapper']['rmt_storage']['write-read'] = '[open open]'
G.add_edge('logwrapper','sdcardd')
G.edge['logwrapper']['sdcardd']['write-read'] = '[open open]'
G.add_edge('logwrapper','shell')
G.edge['logwrapper']['shell']['write-read'] = '[open open]'
G.add_edge('logwrapper','s_system_app')
G.edge['logwrapper']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('logwrapper','system_app')
G.edge['logwrapper']['system_app']['write-read'] = '[open open]'
G.add_edge('logwrapper','system_server')
G.edge['logwrapper']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('logwrapper','vmwared')
G.edge['logwrapper']['vmwared']['write-read'] = '[open open]'
G.add_edge('logwrapper','wpa')
G.edge['logwrapper']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('logwrapper','zygote')
G.edge['logwrapper']['zygote']['write-read'] = '[open open]'
G.add_edge('logwrapper','at_distributor')
G.edge['logwrapper']['at_distributor']['write-read'] = '[open open][setattr getattr]'
G.add_edge('logwrapper','cbd')
G.edge['logwrapper']['cbd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('logwrapper','charon')
G.edge['logwrapper']['charon']['write-read'] = '[open open][setattr getattr]'
G.add_edge('logwrapper','debuggerd')
G.edge['logwrapper']['debuggerd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('logwrapper','diag_uart_log')
G.edge['logwrapper']['diag_uart_log']['write-read'] = '[open open][setattr getattr]'
G.add_edge('logwrapper','dumpstate')
G.edge['logwrapper']['dumpstate']['write-read'] = '[open open][setattr getattr]'
G.add_edge('logwrapper','hostapd')
G.edge['logwrapper']['hostapd']['write-read'] = '[open open][write read][append read][open open][setattr getattr]'
G.add_edge('logwrapper','ime_app')
G.edge['logwrapper']['ime_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('logwrapper','init_shell')
G.edge['logwrapper']['init_shell']['write-read'] = '[open open][setattr getattr]'
G.add_edge('logwrapper','installd')
G.edge['logwrapper']['installd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('logwrapper','itsonbs')
G.edge['logwrapper']['itsonbs']['write-read'] = '[open open][setattr getattr]'
G.add_edge('logwrapper','logwrapper')
G.edge['logwrapper']['logwrapper']['write-read'] = '[open open][write read][append read][open open][setattr getattr]'
G.add_edge('logwrapper','netd')
G.edge['logwrapper']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('logwrapper','qmuxd')
G.edge['logwrapper']['qmuxd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('logwrapper','rild')
G.edge['logwrapper']['rild']['write-read'] = '[open open][setattr getattr]'
G.add_edge('logwrapper','rmt_storage')
G.edge['logwrapper']['rmt_storage']['write-read'] = '[open open][setattr getattr]'
G.add_edge('logwrapper','sdcardd')
G.edge['logwrapper']['sdcardd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('logwrapper','shell')
G.edge['logwrapper']['shell']['write-read'] = '[open open][setattr getattr]'
G.add_edge('logwrapper','s_system_app')
G.edge['logwrapper']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('logwrapper','system_app')
G.edge['logwrapper']['system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('logwrapper','system_server')
G.edge['logwrapper']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('logwrapper','vmwared')
G.edge['logwrapper']['vmwared']['write-read'] = '[open open][setattr getattr]'
G.add_edge('logwrapper','wpa')
G.edge['logwrapper']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('logwrapper','zygote')
G.edge['logwrapper']['zygote']['write-read'] = '[open open][setattr getattr]'
G.add_edge('logwrapper','adbd')
G.edge['logwrapper']['adbd']['write-read'] = '[write read]'
G.edge['logwrapper']['adbd']['fill'] = 'red'
G.add_edge('logwrapper','at_distributor')
G.edge['logwrapper']['at_distributor']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['logwrapper']['at_distributor']['fill'] = 'red'
G.add_edge('logwrapper','cbd')
G.edge['logwrapper']['cbd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['logwrapper']['cbd']['fill'] = 'red'
G.add_edge('logwrapper','charon')
G.edge['logwrapper']['charon']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['logwrapper']['charon']['fill'] = 'red'
G.add_edge('logwrapper','debuggerd')
G.edge['logwrapper']['debuggerd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['logwrapper']['debuggerd']['fill'] = 'red'
G.add_edge('logwrapper','dhcp')
G.edge['logwrapper']['dhcp']['write-read'] = '[write read]'
G.edge['logwrapper']['dhcp']['fill'] = 'red'
G.add_edge('logwrapper','diag_uart_log')
G.edge['logwrapper']['diag_uart_log']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['logwrapper']['diag_uart_log']['fill'] = 'red'
G.add_edge('logwrapper','domain')
G.edge['logwrapper']['domain']['write-read'] = '[write read]'
G.edge['logwrapper']['domain']['fill'] = 'red'
G.add_edge('logwrapper','dumpstate')
G.edge['logwrapper']['dumpstate']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['logwrapper']['dumpstate']['fill'] = 'red'
G.add_edge('logwrapper','hostapd')
G.edge['logwrapper']['hostapd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read]'
G.edge['logwrapper']['hostapd']['fill'] = 'red'
G.add_edge('logwrapper','ime_app')
G.edge['logwrapper']['ime_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['logwrapper']['ime_app']['fill'] = 'red'
G.add_edge('logwrapper','init_shell')
G.edge['logwrapper']['init_shell']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['logwrapper']['init_shell']['fill'] = 'red'
G.add_edge('logwrapper','installd')
G.edge['logwrapper']['installd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['logwrapper']['installd']['fill'] = 'red'
G.add_edge('logwrapper','itsonbs')
G.edge['logwrapper']['itsonbs']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['logwrapper']['itsonbs']['fill'] = 'red'
G.add_edge('logwrapper','logwrapper')
G.edge['logwrapper']['logwrapper']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read]'
G.edge['logwrapper']['logwrapper']['fill'] = 'red'
G.add_edge('logwrapper','netd')
G.edge['logwrapper']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['logwrapper']['netd']['fill'] = 'red'
G.add_edge('logwrapper','qmuxd')
G.edge['logwrapper']['qmuxd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['logwrapper']['qmuxd']['fill'] = 'red'
G.add_edge('logwrapper','rild')
G.edge['logwrapper']['rild']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['logwrapper']['rild']['fill'] = 'red'
G.add_edge('logwrapper','rmt_storage')
G.edge['logwrapper']['rmt_storage']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['logwrapper']['rmt_storage']['fill'] = 'red'
G.add_edge('logwrapper','sdcardd')
G.edge['logwrapper']['sdcardd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['logwrapper']['sdcardd']['fill'] = 'red'
G.add_edge('logwrapper','shell')
G.edge['logwrapper']['shell']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['logwrapper']['shell']['fill'] = 'red'
G.add_edge('logwrapper','s_system_app')
G.edge['logwrapper']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['logwrapper']['s_system_app']['fill'] = 'red'
G.add_edge('logwrapper','system_app')
G.edge['logwrapper']['system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['logwrapper']['system_app']['fill'] = 'red'
G.add_edge('logwrapper','system_server')
G.edge['logwrapper']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['logwrapper']['system_server']['fill'] = 'red'
G.add_edge('logwrapper','vmwared')
G.edge['logwrapper']['vmwared']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['logwrapper']['vmwared']['fill'] = 'red'
G.add_edge('logwrapper','wpa')
G.edge['logwrapper']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['logwrapper']['wpa']['fill'] = 'red'
G.add_edge('logwrapper','zygote')
G.edge['logwrapper']['zygote']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['logwrapper']['zygote']['fill'] = 'red'
G.add_edge('logwrapper','adbd')
G.edge['logwrapper']['adbd']['write-read'] = '[write read][add_name search]'
G.add_edge('logwrapper','at_distributor')
G.edge['logwrapper']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('logwrapper','at_distributor')
G.edge['logwrapper']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('logwrapper','auditd')
G.edge['logwrapper']['auditd']['write-read'] = '[add_name search]'
G.add_edge('logwrapper','cbd')
G.edge['logwrapper']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('logwrapper','cbd')
G.edge['logwrapper']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('logwrapper','charon')
G.edge['logwrapper']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('logwrapper','charon')
G.edge['logwrapper']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('logwrapper','clatd')
G.edge['logwrapper']['clatd']['write-read'] = '[add_name search]'
G.add_edge('logwrapper','debuggerd')
G.edge['logwrapper']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('logwrapper','debuggerd')
G.edge['logwrapper']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('logwrapper','dhcp')
G.edge['logwrapper']['dhcp']['write-read'] = '[write read][add_name search]'
G.add_edge('logwrapper','diag_uart_log')
G.edge['logwrapper']['diag_uart_log']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('logwrapper','diag_uart_log')
G.edge['logwrapper']['diag_uart_log']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('logwrapper','dumpstate')
G.edge['logwrapper']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('logwrapper','dumpstate')
G.edge['logwrapper']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('logwrapper','hostapd')
G.edge['logwrapper']['hostapd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('logwrapper','hostapd')
G.edge['logwrapper']['hostapd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('logwrapper','hvdcp')
G.edge['logwrapper']['hvdcp']['write-read'] = '[add_name search]'
G.add_edge('logwrapper','ime_app')
G.edge['logwrapper']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('logwrapper','ime_app')
G.edge['logwrapper']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('logwrapper','init_shell')
G.edge['logwrapper']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('logwrapper','init_shell')
G.edge['logwrapper']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('logwrapper','installd')
G.edge['logwrapper']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('logwrapper','installd')
G.edge['logwrapper']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('logwrapper','itsonbs')
G.edge['logwrapper']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('logwrapper','itsonbs')
G.edge['logwrapper']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('logwrapper','jackservice')
G.edge['logwrapper']['jackservice']['write-read'] = '[add_name search]'
G.add_edge('logwrapper','lmkd')
G.edge['logwrapper']['lmkd']['write-read'] = '[remove_name search]'
G.add_edge('logwrapper','logwrapper')
G.edge['logwrapper']['logwrapper']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('logwrapper','logwrapper')
G.edge['logwrapper']['logwrapper']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('logwrapper','msm_irqbalanced')
G.edge['logwrapper']['msm_irqbalanced']['write-read'] = '[add_name search]'
G.add_edge('logwrapper','netd')
G.edge['logwrapper']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('logwrapper','netd')
G.edge['logwrapper']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('logwrapper','qmuxd')
G.edge['logwrapper']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('logwrapper','qmuxd')
G.edge['logwrapper']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('logwrapper','racoon')
G.edge['logwrapper']['racoon']['write-read'] = '[add_name search]'
G.add_edge('logwrapper','rild')
G.edge['logwrapper']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('logwrapper','rild')
G.edge['logwrapper']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('logwrapper','rmt_storage')
G.edge['logwrapper']['rmt_storage']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('logwrapper','rmt_storage')
G.edge['logwrapper']['rmt_storage']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('logwrapper','sdcardd')
G.edge['logwrapper']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('logwrapper','sdcardd')
G.edge['logwrapper']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('logwrapper','sensors')
G.edge['logwrapper']['sensors']['write-read'] = '[add_name search]'
G.add_edge('logwrapper','shell')
G.edge['logwrapper']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('logwrapper','shell')
G.edge['logwrapper']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('logwrapper','s_system_app')
G.edge['logwrapper']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('logwrapper','s_system_app')
G.edge['logwrapper']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('logwrapper','system_app')
G.edge['logwrapper']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('logwrapper','system_app')
G.edge['logwrapper']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('logwrapper','system_server')
G.edge['logwrapper']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('logwrapper','system_server')
G.edge['logwrapper']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('logwrapper','system_server')
G.edge['logwrapper']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search]'
G.add_edge('logwrapper','vmwared')
G.edge['logwrapper']['vmwared']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('logwrapper','vmwared')
G.edge['logwrapper']['vmwared']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('logwrapper','wpa')
G.edge['logwrapper']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('logwrapper','wpa')
G.edge['logwrapper']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('logwrapper','zygote')
G.edge['logwrapper']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('logwrapper','zygote')
G.edge['logwrapper']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('netd','at_distributor')
G.edge['netd']['at_distributor']['write-read'] = '[open open]'
G.add_edge('netd','cbd')
G.edge['netd']['cbd']['write-read'] = '[open open]'
G.add_edge('netd','charon')
G.edge['netd']['charon']['write-read'] = '[open open]'
G.add_edge('netd','debuggerd')
G.edge['netd']['debuggerd']['write-read'] = '[open open]'
G.add_edge('netd','diag_uart_log')
G.edge['netd']['diag_uart_log']['write-read'] = '[open open]'
G.add_edge('netd','dumpstate')
G.edge['netd']['dumpstate']['write-read'] = '[open open]'
G.add_edge('netd','hostapd')
G.edge['netd']['hostapd']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('netd','ime_app')
G.edge['netd']['ime_app']['write-read'] = '[setattr getattr][setopt getopt][open open]'
G.add_edge('netd','init_shell')
G.edge['netd']['init_shell']['write-read'] = '[open open]'
G.add_edge('netd','installd')
G.edge['netd']['installd']['write-read'] = '[open open]'
G.add_edge('netd','itsonbs')
G.edge['netd']['itsonbs']['write-read'] = '[open open]'
G.add_edge('netd','logwrapper')
G.edge['netd']['logwrapper']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('netd','netd')
G.edge['netd']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open]'
G.add_edge('netd','qmuxd')
G.edge['netd']['qmuxd']['write-read'] = '[open open]'
G.add_edge('netd','rild')
G.edge['netd']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open]'
G.add_edge('netd','rmt_storage')
G.edge['netd']['rmt_storage']['write-read'] = '[open open]'
G.add_edge('netd','sdcardd')
G.edge['netd']['sdcardd']['write-read'] = '[open open]'
G.add_edge('netd','shell')
G.edge['netd']['shell']['write-read'] = '[open open]'
G.add_edge('netd','s_system_app')
G.edge['netd']['s_system_app']['write-read'] = '[setattr getattr][setopt getopt][open open][setattr getattr][write read][append read][open open]'
G.add_edge('netd','system_app')
G.edge['netd']['system_app']['write-read'] = '[setattr getattr][setopt getopt][open open]'
G.add_edge('netd','system_server')
G.edge['netd']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open]'
G.add_edge('netd','vmwared')
G.edge['netd']['vmwared']['write-read'] = '[open open]'
G.add_edge('netd','wpa')
G.edge['netd']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('netd','zygote')
G.edge['netd']['zygote']['write-read'] = '[open open]'
G.add_edge('netd','at_distributor')
G.edge['netd']['at_distributor']['write-read'] = '[open open][setattr getattr]'
G.add_edge('netd','cbd')
G.edge['netd']['cbd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('netd','charon')
G.edge['netd']['charon']['write-read'] = '[open open][setattr getattr]'
G.add_edge('netd','debuggerd')
G.edge['netd']['debuggerd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('netd','diag_uart_log')
G.edge['netd']['diag_uart_log']['write-read'] = '[open open][setattr getattr]'
G.add_edge('netd','dumpstate')
G.edge['netd']['dumpstate']['write-read'] = '[open open][setattr getattr]'
G.add_edge('netd','hostapd')
G.edge['netd']['hostapd']['write-read'] = '[open open][write read][append read][open open][setattr getattr]'
G.add_edge('netd','ime_app')
G.edge['netd']['ime_app']['write-read'] = '[setattr getattr][setopt getopt][open open][setattr getattr]'
G.add_edge('netd','init_shell')
G.edge['netd']['init_shell']['write-read'] = '[open open][setattr getattr]'
G.add_edge('netd','installd')
G.edge['netd']['installd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('netd','itsonbs')
G.edge['netd']['itsonbs']['write-read'] = '[open open][setattr getattr]'
G.add_edge('netd','logwrapper')
G.edge['netd']['logwrapper']['write-read'] = '[open open][write read][append read][open open][setattr getattr]'
G.add_edge('netd','netd')
G.edge['netd']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('netd','qmuxd')
G.edge['netd']['qmuxd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('netd','rild')
G.edge['netd']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr]'
G.add_edge('netd','rmt_storage')
G.edge['netd']['rmt_storage']['write-read'] = '[open open][setattr getattr]'
G.add_edge('netd','sdcardd')
G.edge['netd']['sdcardd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('netd','shell')
G.edge['netd']['shell']['write-read'] = '[open open][setattr getattr]'
G.add_edge('netd','s_system_app')
G.edge['netd']['s_system_app']['write-read'] = '[setattr getattr][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('netd','system_app')
G.edge['netd']['system_app']['write-read'] = '[setattr getattr][setopt getopt][open open][setattr getattr]'
G.add_edge('netd','system_server')
G.edge['netd']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('netd','vmwared')
G.edge['netd']['vmwared']['write-read'] = '[open open][setattr getattr]'
G.add_edge('netd','wpa')
G.edge['netd']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('netd','zygote')
G.edge['netd']['zygote']['write-read'] = '[open open][setattr getattr]'
G.add_edge('netd','adbd')
G.edge['netd']['adbd']['write-read'] = '[write read]'
G.edge['netd']['adbd']['fill'] = 'red'
G.add_edge('netd','at_distributor')
G.edge['netd']['at_distributor']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['netd']['at_distributor']['fill'] = 'red'
G.add_edge('netd','cbd')
G.edge['netd']['cbd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['netd']['cbd']['fill'] = 'red'
G.add_edge('netd','charon')
G.edge['netd']['charon']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['netd']['charon']['fill'] = 'red'
G.add_edge('netd','debuggerd')
G.edge['netd']['debuggerd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['netd']['debuggerd']['fill'] = 'red'
G.add_edge('netd','dhcp')
G.edge['netd']['dhcp']['write-read'] = '[write read]'
G.edge['netd']['dhcp']['fill'] = 'red'
G.add_edge('netd','diag_uart_log')
G.edge['netd']['diag_uart_log']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['netd']['diag_uart_log']['fill'] = 'red'
G.add_edge('netd','domain')
G.edge['netd']['domain']['write-read'] = '[write read]'
G.edge['netd']['domain']['fill'] = 'red'
G.add_edge('netd','dumpstate')
G.edge['netd']['dumpstate']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['netd']['dumpstate']['fill'] = 'red'
G.add_edge('netd','hostapd')
G.edge['netd']['hostapd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read]'
G.edge['netd']['hostapd']['fill'] = 'red'
G.add_edge('netd','ime_app')
G.edge['netd']['ime_app']['write-read'] = '[setattr getattr][setopt getopt][open open][setattr getattr][write read]'
G.edge['netd']['ime_app']['fill'] = 'red'
G.add_edge('netd','init_shell')
G.edge['netd']['init_shell']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['netd']['init_shell']['fill'] = 'red'
G.add_edge('netd','installd')
G.edge['netd']['installd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['netd']['installd']['fill'] = 'red'
G.add_edge('netd','itsonbs')
G.edge['netd']['itsonbs']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['netd']['itsonbs']['fill'] = 'red'
G.add_edge('netd','logwrapper')
G.edge['netd']['logwrapper']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read]'
G.edge['netd']['logwrapper']['fill'] = 'red'
G.add_edge('netd','netd')
G.edge['netd']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['netd']['netd']['fill'] = 'red'
G.add_edge('netd','qmuxd')
G.edge['netd']['qmuxd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['netd']['qmuxd']['fill'] = 'red'
G.add_edge('netd','rild')
G.edge['netd']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read]'
G.edge['netd']['rild']['fill'] = 'red'
G.add_edge('netd','rmt_storage')
G.edge['netd']['rmt_storage']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['netd']['rmt_storage']['fill'] = 'red'
G.add_edge('netd','sdcardd')
G.edge['netd']['sdcardd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['netd']['sdcardd']['fill'] = 'red'
G.add_edge('netd','shell')
G.edge['netd']['shell']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['netd']['shell']['fill'] = 'red'
G.add_edge('netd','s_system_app')
G.edge['netd']['s_system_app']['write-read'] = '[setattr getattr][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['netd']['s_system_app']['fill'] = 'red'
G.add_edge('netd','system_app')
G.edge['netd']['system_app']['write-read'] = '[setattr getattr][setopt getopt][open open][setattr getattr][write read]'
G.edge['netd']['system_app']['fill'] = 'red'
G.add_edge('netd','system_server')
G.edge['netd']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['netd']['system_server']['fill'] = 'red'
G.add_edge('netd','vmwared')
G.edge['netd']['vmwared']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['netd']['vmwared']['fill'] = 'red'
G.add_edge('netd','wpa')
G.edge['netd']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['netd']['wpa']['fill'] = 'red'
G.add_edge('netd','zygote')
G.edge['netd']['zygote']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['netd']['zygote']['fill'] = 'red'
G.add_edge('netd','adbd')
G.edge['netd']['adbd']['write-read'] = '[write read][add_name search]'
G.add_edge('netd','at_distributor')
G.edge['netd']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('netd','at_distributor')
G.edge['netd']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('netd','auditd')
G.edge['netd']['auditd']['write-read'] = '[add_name search]'
G.add_edge('netd','cbd')
G.edge['netd']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('netd','cbd')
G.edge['netd']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('netd','charon')
G.edge['netd']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('netd','charon')
G.edge['netd']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('netd','clatd')
G.edge['netd']['clatd']['write-read'] = '[add_name search]'
G.add_edge('netd','debuggerd')
G.edge['netd']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('netd','debuggerd')
G.edge['netd']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('netd','dhcp')
G.edge['netd']['dhcp']['write-read'] = '[write read][add_name search]'
G.add_edge('netd','diag_uart_log')
G.edge['netd']['diag_uart_log']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('netd','diag_uart_log')
G.edge['netd']['diag_uart_log']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('netd','dumpstate')
G.edge['netd']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('netd','dumpstate')
G.edge['netd']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('netd','hostapd')
G.edge['netd']['hostapd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('netd','hostapd')
G.edge['netd']['hostapd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('netd','hvdcp')
G.edge['netd']['hvdcp']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][add_name search]'
G.add_edge('netd','ime_app')
G.edge['netd']['ime_app']['write-read'] = '[setattr getattr][setopt getopt][open open][setattr getattr][write read][add_name search]'
G.add_edge('netd','ime_app')
G.edge['netd']['ime_app']['write-read'] = '[setattr getattr][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('netd','init_shell')
G.edge['netd']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('netd','init_shell')
G.edge['netd']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('netd','installd')
G.edge['netd']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('netd','installd')
G.edge['netd']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('netd','itsonbs')
G.edge['netd']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('netd','itsonbs')
G.edge['netd']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('netd','jackservice')
G.edge['netd']['jackservice']['write-read'] = '[add_name search]'
G.add_edge('netd','lmkd')
G.edge['netd']['lmkd']['write-read'] = '[remove_name search]'
G.add_edge('netd','logwrapper')
G.edge['netd']['logwrapper']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('netd','logwrapper')
G.edge['netd']['logwrapper']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('netd','msm_irqbalanced')
G.edge['netd']['msm_irqbalanced']['write-read'] = '[add_name search]'
G.add_edge('netd','netd')
G.edge['netd']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('netd','netd')
G.edge['netd']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('netd','qmuxd')
G.edge['netd']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('netd','qmuxd')
G.edge['netd']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('netd','racoon')
G.edge['netd']['racoon']['write-read'] = '[add_name search]'
G.add_edge('netd','rild')
G.edge['netd']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search]'
G.add_edge('netd','rild')
G.edge['netd']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('netd','rmt_storage')
G.edge['netd']['rmt_storage']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('netd','rmt_storage')
G.edge['netd']['rmt_storage']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('netd','sdcardd')
G.edge['netd']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('netd','sdcardd')
G.edge['netd']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('netd','sensors')
G.edge['netd']['sensors']['write-read'] = '[add_name search]'
G.add_edge('netd','shell')
G.edge['netd']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('netd','shell')
G.edge['netd']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('netd','s_system_app')
G.edge['netd']['s_system_app']['write-read'] = '[setattr getattr][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('netd','s_system_app')
G.edge['netd']['s_system_app']['write-read'] = '[setattr getattr][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('netd','system_app')
G.edge['netd']['system_app']['write-read'] = '[setattr getattr][setopt getopt][open open][setattr getattr][write read][add_name search]'
G.add_edge('netd','system_app')
G.edge['netd']['system_app']['write-read'] = '[setattr getattr][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('netd','system_server')
G.edge['netd']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('netd','system_server')
G.edge['netd']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('netd','system_server')
G.edge['netd']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search]'
G.add_edge('netd','vmwared')
G.edge['netd']['vmwared']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('netd','vmwared')
G.edge['netd']['vmwared']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('netd','wpa')
G.edge['netd']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('netd','wpa')
G.edge['netd']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('netd','zygote')
G.edge['netd']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('netd','zygote')
G.edge['netd']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('qmuxd','at_distributor')
G.edge['qmuxd']['at_distributor']['write-read'] = '[open open]'
G.add_edge('qmuxd','cbd')
G.edge['qmuxd']['cbd']['write-read'] = '[open open]'
G.add_edge('qmuxd','charon')
G.edge['qmuxd']['charon']['write-read'] = '[open open]'
G.add_edge('qmuxd','debuggerd')
G.edge['qmuxd']['debuggerd']['write-read'] = '[open open]'
G.add_edge('qmuxd','diag_uart_log')
G.edge['qmuxd']['diag_uart_log']['write-read'] = '[open open]'
G.add_edge('qmuxd','dumpstate')
G.edge['qmuxd']['dumpstate']['write-read'] = '[open open]'
G.add_edge('qmuxd','hostapd')
G.edge['qmuxd']['hostapd']['write-read'] = '[open open]'
G.add_edge('qmuxd','ime_app')
G.edge['qmuxd']['ime_app']['write-read'] = '[open open]'
G.add_edge('qmuxd','init_shell')
G.edge['qmuxd']['init_shell']['write-read'] = '[open open]'
G.add_edge('qmuxd','installd')
G.edge['qmuxd']['installd']['write-read'] = '[open open]'
G.add_edge('qmuxd','itsonbs')
G.edge['qmuxd']['itsonbs']['write-read'] = '[open open]'
G.add_edge('qmuxd','logwrapper')
G.edge['qmuxd']['logwrapper']['write-read'] = '[open open]'
G.add_edge('qmuxd','netd')
G.edge['qmuxd']['netd']['write-read'] = '[open open]'
G.add_edge('qmuxd','qmuxd')
G.edge['qmuxd']['qmuxd']['write-read'] = '[open open]'
G.add_edge('qmuxd','rild')
G.edge['qmuxd']['rild']['write-read'] = '[open open]'
G.add_edge('qmuxd','rmt_storage')
G.edge['qmuxd']['rmt_storage']['write-read'] = '[open open]'
G.add_edge('qmuxd','sdcardd')
G.edge['qmuxd']['sdcardd']['write-read'] = '[open open]'
G.add_edge('qmuxd','shell')
G.edge['qmuxd']['shell']['write-read'] = '[open open]'
G.add_edge('qmuxd','s_system_app')
G.edge['qmuxd']['s_system_app']['write-read'] = '[open open]'
G.add_edge('qmuxd','system_app')
G.edge['qmuxd']['system_app']['write-read'] = '[open open]'
G.add_edge('qmuxd','system_server')
G.edge['qmuxd']['system_server']['write-read'] = '[open open]'
G.add_edge('qmuxd','vmwared')
G.edge['qmuxd']['vmwared']['write-read'] = '[open open]'
G.add_edge('qmuxd','wpa')
G.edge['qmuxd']['wpa']['write-read'] = '[open open]'
G.add_edge('qmuxd','zygote')
G.edge['qmuxd']['zygote']['write-read'] = '[open open]'
G.add_edge('qmuxd','at_distributor')
G.edge['qmuxd']['at_distributor']['write-read'] = '[open open][setattr getattr]'
G.add_edge('qmuxd','cbd')
G.edge['qmuxd']['cbd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('qmuxd','charon')
G.edge['qmuxd']['charon']['write-read'] = '[open open][setattr getattr]'
G.add_edge('qmuxd','debuggerd')
G.edge['qmuxd']['debuggerd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('qmuxd','diag_uart_log')
G.edge['qmuxd']['diag_uart_log']['write-read'] = '[open open][setattr getattr]'
G.add_edge('qmuxd','dumpstate')
G.edge['qmuxd']['dumpstate']['write-read'] = '[open open][setattr getattr]'
G.add_edge('qmuxd','hostapd')
G.edge['qmuxd']['hostapd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('qmuxd','ime_app')
G.edge['qmuxd']['ime_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('qmuxd','init_shell')
G.edge['qmuxd']['init_shell']['write-read'] = '[open open][setattr getattr]'
G.add_edge('qmuxd','installd')
G.edge['qmuxd']['installd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('qmuxd','itsonbs')
G.edge['qmuxd']['itsonbs']['write-read'] = '[open open][setattr getattr]'
G.add_edge('qmuxd','logwrapper')
G.edge['qmuxd']['logwrapper']['write-read'] = '[open open][setattr getattr]'
G.add_edge('qmuxd','netd')
G.edge['qmuxd']['netd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('qmuxd','qmuxd')
G.edge['qmuxd']['qmuxd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('qmuxd','rild')
G.edge['qmuxd']['rild']['write-read'] = '[open open][setattr getattr]'
G.add_edge('qmuxd','rmt_storage')
G.edge['qmuxd']['rmt_storage']['write-read'] = '[open open][setattr getattr]'
G.add_edge('qmuxd','sdcardd')
G.edge['qmuxd']['sdcardd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('qmuxd','shell')
G.edge['qmuxd']['shell']['write-read'] = '[open open][setattr getattr]'
G.add_edge('qmuxd','s_system_app')
G.edge['qmuxd']['s_system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('qmuxd','system_app')
G.edge['qmuxd']['system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('qmuxd','system_server')
G.edge['qmuxd']['system_server']['write-read'] = '[open open][setattr getattr]'
G.add_edge('qmuxd','vmwared')
G.edge['qmuxd']['vmwared']['write-read'] = '[open open][setattr getattr]'
G.add_edge('qmuxd','wpa')
G.edge['qmuxd']['wpa']['write-read'] = '[open open][setattr getattr]'
G.add_edge('qmuxd','zygote')
G.edge['qmuxd']['zygote']['write-read'] = '[open open][setattr getattr]'
G.add_edge('qmuxd','adbd')
G.edge['qmuxd']['adbd']['write-read'] = '[write read]'
G.edge['qmuxd']['adbd']['fill'] = 'red'
G.add_edge('qmuxd','at_distributor')
G.edge['qmuxd']['at_distributor']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['qmuxd']['at_distributor']['fill'] = 'red'
G.add_edge('qmuxd','cbd')
G.edge['qmuxd']['cbd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['qmuxd']['cbd']['fill'] = 'red'
G.add_edge('qmuxd','charon')
G.edge['qmuxd']['charon']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['qmuxd']['charon']['fill'] = 'red'
G.add_edge('qmuxd','debuggerd')
G.edge['qmuxd']['debuggerd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['qmuxd']['debuggerd']['fill'] = 'red'
G.add_edge('qmuxd','dhcp')
G.edge['qmuxd']['dhcp']['write-read'] = '[write read]'
G.edge['qmuxd']['dhcp']['fill'] = 'red'
G.add_edge('qmuxd','diag_uart_log')
G.edge['qmuxd']['diag_uart_log']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['qmuxd']['diag_uart_log']['fill'] = 'red'
G.add_edge('qmuxd','domain')
G.edge['qmuxd']['domain']['write-read'] = '[write read]'
G.edge['qmuxd']['domain']['fill'] = 'red'
G.add_edge('qmuxd','dumpstate')
G.edge['qmuxd']['dumpstate']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['qmuxd']['dumpstate']['fill'] = 'red'
G.add_edge('qmuxd','hostapd')
G.edge['qmuxd']['hostapd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['qmuxd']['hostapd']['fill'] = 'red'
G.add_edge('qmuxd','ime_app')
G.edge['qmuxd']['ime_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['qmuxd']['ime_app']['fill'] = 'red'
G.add_edge('qmuxd','init_shell')
G.edge['qmuxd']['init_shell']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['qmuxd']['init_shell']['fill'] = 'red'
G.add_edge('qmuxd','installd')
G.edge['qmuxd']['installd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['qmuxd']['installd']['fill'] = 'red'
G.add_edge('qmuxd','itsonbs')
G.edge['qmuxd']['itsonbs']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['qmuxd']['itsonbs']['fill'] = 'red'
G.add_edge('qmuxd','logwrapper')
G.edge['qmuxd']['logwrapper']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['qmuxd']['logwrapper']['fill'] = 'red'
G.add_edge('qmuxd','netd')
G.edge['qmuxd']['netd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['qmuxd']['netd']['fill'] = 'red'
G.add_edge('qmuxd','qmuxd')
G.edge['qmuxd']['qmuxd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['qmuxd']['qmuxd']['fill'] = 'red'
G.add_edge('qmuxd','rild')
G.edge['qmuxd']['rild']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['qmuxd']['rild']['fill'] = 'red'
G.add_edge('qmuxd','rmt_storage')
G.edge['qmuxd']['rmt_storage']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['qmuxd']['rmt_storage']['fill'] = 'red'
G.add_edge('qmuxd','sdcardd')
G.edge['qmuxd']['sdcardd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['qmuxd']['sdcardd']['fill'] = 'red'
G.add_edge('qmuxd','shell')
G.edge['qmuxd']['shell']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['qmuxd']['shell']['fill'] = 'red'
G.add_edge('qmuxd','s_system_app')
G.edge['qmuxd']['s_system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['qmuxd']['s_system_app']['fill'] = 'red'
G.add_edge('qmuxd','system_app')
G.edge['qmuxd']['system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['qmuxd']['system_app']['fill'] = 'red'
G.add_edge('qmuxd','system_server')
G.edge['qmuxd']['system_server']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['qmuxd']['system_server']['fill'] = 'red'
G.add_edge('qmuxd','vmwared')
G.edge['qmuxd']['vmwared']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['qmuxd']['vmwared']['fill'] = 'red'
G.add_edge('qmuxd','wpa')
G.edge['qmuxd']['wpa']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['qmuxd']['wpa']['fill'] = 'red'
G.add_edge('qmuxd','zygote')
G.edge['qmuxd']['zygote']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['qmuxd']['zygote']['fill'] = 'red'
G.add_edge('qmuxd','adbd')
G.edge['qmuxd']['adbd']['write-read'] = '[write read][add_name search]'
G.add_edge('qmuxd','at_distributor')
G.edge['qmuxd']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('qmuxd','at_distributor')
G.edge['qmuxd']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('qmuxd','auditd')
G.edge['qmuxd']['auditd']['write-read'] = '[add_name search]'
G.add_edge('qmuxd','cbd')
G.edge['qmuxd']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('qmuxd','cbd')
G.edge['qmuxd']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('qmuxd','charon')
G.edge['qmuxd']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('qmuxd','charon')
G.edge['qmuxd']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('qmuxd','clatd')
G.edge['qmuxd']['clatd']['write-read'] = '[add_name search]'
G.add_edge('qmuxd','debuggerd')
G.edge['qmuxd']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('qmuxd','debuggerd')
G.edge['qmuxd']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('qmuxd','dhcp')
G.edge['qmuxd']['dhcp']['write-read'] = '[write read][add_name search]'
G.add_edge('qmuxd','diag_uart_log')
G.edge['qmuxd']['diag_uart_log']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('qmuxd','diag_uart_log')
G.edge['qmuxd']['diag_uart_log']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('qmuxd','dumpstate')
G.edge['qmuxd']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('qmuxd','dumpstate')
G.edge['qmuxd']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('qmuxd','hostapd')
G.edge['qmuxd']['hostapd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('qmuxd','hostapd')
G.edge['qmuxd']['hostapd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('qmuxd','hvdcp')
G.edge['qmuxd']['hvdcp']['write-read'] = '[add_name search]'
G.add_edge('qmuxd','ime_app')
G.edge['qmuxd']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('qmuxd','ime_app')
G.edge['qmuxd']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('qmuxd','init_shell')
G.edge['qmuxd']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('qmuxd','init_shell')
G.edge['qmuxd']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('qmuxd','installd')
G.edge['qmuxd']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('qmuxd','installd')
G.edge['qmuxd']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('qmuxd','itsonbs')
G.edge['qmuxd']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('qmuxd','itsonbs')
G.edge['qmuxd']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('qmuxd','jackservice')
G.edge['qmuxd']['jackservice']['write-read'] = '[add_name search]'
G.add_edge('qmuxd','lmkd')
G.edge['qmuxd']['lmkd']['write-read'] = '[remove_name search]'
G.add_edge('qmuxd','logwrapper')
G.edge['qmuxd']['logwrapper']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('qmuxd','logwrapper')
G.edge['qmuxd']['logwrapper']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('qmuxd','msm_irqbalanced')
G.edge['qmuxd']['msm_irqbalanced']['write-read'] = '[add_name search]'
G.add_edge('qmuxd','netd')
G.edge['qmuxd']['netd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('qmuxd','netd')
G.edge['qmuxd']['netd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('qmuxd','qmuxd')
G.edge['qmuxd']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('qmuxd','qmuxd')
G.edge['qmuxd']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('qmuxd','racoon')
G.edge['qmuxd']['racoon']['write-read'] = '[add_name search]'
G.add_edge('qmuxd','rild')
G.edge['qmuxd']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('qmuxd','rild')
G.edge['qmuxd']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('qmuxd','rmt_storage')
G.edge['qmuxd']['rmt_storage']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('qmuxd','rmt_storage')
G.edge['qmuxd']['rmt_storage']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('qmuxd','sdcardd')
G.edge['qmuxd']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('qmuxd','sdcardd')
G.edge['qmuxd']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('qmuxd','sensors')
G.edge['qmuxd']['sensors']['write-read'] = '[add_name search]'
G.add_edge('qmuxd','shell')
G.edge['qmuxd']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('qmuxd','shell')
G.edge['qmuxd']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('qmuxd','s_system_app')
G.edge['qmuxd']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('qmuxd','s_system_app')
G.edge['qmuxd']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('qmuxd','system_app')
G.edge['qmuxd']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('qmuxd','system_app')
G.edge['qmuxd']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('qmuxd','system_server')
G.edge['qmuxd']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('qmuxd','system_server')
G.edge['qmuxd']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('qmuxd','system_server')
G.edge['qmuxd']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search]'
G.add_edge('qmuxd','vmwared')
G.edge['qmuxd']['vmwared']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('qmuxd','vmwared')
G.edge['qmuxd']['vmwared']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('qmuxd','wpa')
G.edge['qmuxd']['wpa']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('qmuxd','wpa')
G.edge['qmuxd']['wpa']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('qmuxd','zygote')
G.edge['qmuxd']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('qmuxd','zygote')
G.edge['qmuxd']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('rild','at_distributor')
G.edge['rild']['at_distributor']['write-read'] = '[open open]'
G.add_edge('rild','cbd')
G.edge['rild']['cbd']['write-read'] = '[open open]'
G.add_edge('rild','charon')
G.edge['rild']['charon']['write-read'] = '[open open]'
G.add_edge('rild','debuggerd')
G.edge['rild']['debuggerd']['write-read'] = '[open open]'
G.add_edge('rild','diag_uart_log')
G.edge['rild']['diag_uart_log']['write-read'] = '[open open]'
G.add_edge('rild','dumpstate')
G.edge['rild']['dumpstate']['write-read'] = '[open open]'
G.add_edge('rild','hostapd')
G.edge['rild']['hostapd']['write-read'] = '[open open]'
G.add_edge('rild','ime_app')
G.edge['rild']['ime_app']['write-read'] = '[setattr getattr][setopt getopt][open open]'
G.add_edge('rild','init_shell')
G.edge['rild']['init_shell']['write-read'] = '[open open]'
G.add_edge('rild','installd')
G.edge['rild']['installd']['write-read'] = '[open open]'
G.add_edge('rild','itsonbs')
G.edge['rild']['itsonbs']['write-read'] = '[open open]'
G.add_edge('rild','logwrapper')
G.edge['rild']['logwrapper']['write-read'] = '[open open]'
G.add_edge('rild','netd')
G.edge['rild']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open]'
G.add_edge('rild','qmuxd')
G.edge['rild']['qmuxd']['write-read'] = '[open open]'
G.add_edge('rild','rild')
G.edge['rild']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open]'
G.add_edge('rild','rmt_storage')
G.edge['rild']['rmt_storage']['write-read'] = '[open open]'
G.add_edge('rild','sdcardd')
G.edge['rild']['sdcardd']['write-read'] = '[open open]'
G.add_edge('rild','shell')
G.edge['rild']['shell']['write-read'] = '[open open]'
G.add_edge('rild','s_system_app')
G.edge['rild']['s_system_app']['write-read'] = '[setattr getattr][setopt getopt][open open]'
G.add_edge('rild','system_app')
G.edge['rild']['system_app']['write-read'] = '[setattr getattr][setopt getopt][open open]'
G.add_edge('rild','system_server')
G.edge['rild']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open]'
G.add_edge('rild','vmwared')
G.edge['rild']['vmwared']['write-read'] = '[open open]'
G.add_edge('rild','wpa')
G.edge['rild']['wpa']['write-read'] = '[open open]'
G.add_edge('rild','zygote')
G.edge['rild']['zygote']['write-read'] = '[open open]'
G.add_edge('rild','at_distributor')
G.edge['rild']['at_distributor']['write-read'] = '[open open][setattr getattr]'
G.add_edge('rild','cbd')
G.edge['rild']['cbd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('rild','charon')
G.edge['rild']['charon']['write-read'] = '[open open][setattr getattr]'
G.add_edge('rild','debuggerd')
G.edge['rild']['debuggerd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('rild','diag_uart_log')
G.edge['rild']['diag_uart_log']['write-read'] = '[open open][setattr getattr]'
G.add_edge('rild','dumpstate')
G.edge['rild']['dumpstate']['write-read'] = '[open open][setattr getattr]'
G.add_edge('rild','hostapd')
G.edge['rild']['hostapd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('rild','ime_app')
G.edge['rild']['ime_app']['write-read'] = '[setattr getattr][setopt getopt][open open][setattr getattr]'
G.add_edge('rild','init_shell')
G.edge['rild']['init_shell']['write-read'] = '[open open][setattr getattr]'
G.add_edge('rild','installd')
G.edge['rild']['installd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('rild','itsonbs')
G.edge['rild']['itsonbs']['write-read'] = '[open open][setattr getattr]'
G.add_edge('rild','logwrapper')
G.edge['rild']['logwrapper']['write-read'] = '[open open][setattr getattr]'
G.add_edge('rild','netd')
G.edge['rild']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr]'
G.add_edge('rild','qmuxd')
G.edge['rild']['qmuxd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('rild','rild')
G.edge['rild']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr]'
G.add_edge('rild','rmt_storage')
G.edge['rild']['rmt_storage']['write-read'] = '[open open][setattr getattr]'
G.add_edge('rild','sdcardd')
G.edge['rild']['sdcardd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('rild','shell')
G.edge['rild']['shell']['write-read'] = '[open open][setattr getattr]'
G.add_edge('rild','s_system_app')
G.edge['rild']['s_system_app']['write-read'] = '[setattr getattr][setopt getopt][open open][setattr getattr]'
G.add_edge('rild','system_app')
G.edge['rild']['system_app']['write-read'] = '[setattr getattr][setopt getopt][open open][setattr getattr]'
G.add_edge('rild','system_server')
G.edge['rild']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr]'
G.add_edge('rild','vmwared')
G.edge['rild']['vmwared']['write-read'] = '[open open][setattr getattr]'
G.add_edge('rild','wpa')
G.edge['rild']['wpa']['write-read'] = '[open open][setattr getattr]'
G.add_edge('rild','zygote')
G.edge['rild']['zygote']['write-read'] = '[open open][setattr getattr]'
G.add_edge('rild','adbd')
G.edge['rild']['adbd']['write-read'] = '[write read]'
G.edge['rild']['adbd']['fill'] = 'red'
G.add_edge('rild','at_distributor')
G.edge['rild']['at_distributor']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['rild']['at_distributor']['fill'] = 'red'
G.add_edge('rild','cbd')
G.edge['rild']['cbd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['rild']['cbd']['fill'] = 'red'
G.add_edge('rild','charon')
G.edge['rild']['charon']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['rild']['charon']['fill'] = 'red'
G.add_edge('rild','debuggerd')
G.edge['rild']['debuggerd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['rild']['debuggerd']['fill'] = 'red'
G.add_edge('rild','dhcp')
G.edge['rild']['dhcp']['write-read'] = '[write read]'
G.edge['rild']['dhcp']['fill'] = 'red'
G.add_edge('rild','diag_uart_log')
G.edge['rild']['diag_uart_log']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['rild']['diag_uart_log']['fill'] = 'red'
G.add_edge('rild','domain')
G.edge['rild']['domain']['write-read'] = '[write read]'
G.edge['rild']['domain']['fill'] = 'red'
G.add_edge('rild','dumpstate')
G.edge['rild']['dumpstate']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['rild']['dumpstate']['fill'] = 'red'
G.add_edge('rild','hostapd')
G.edge['rild']['hostapd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['rild']['hostapd']['fill'] = 'red'
G.add_edge('rild','ime_app')
G.edge['rild']['ime_app']['write-read'] = '[setattr getattr][setopt getopt][open open][setattr getattr][write read]'
G.edge['rild']['ime_app']['fill'] = 'red'
G.add_edge('rild','init_shell')
G.edge['rild']['init_shell']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['rild']['init_shell']['fill'] = 'red'
G.add_edge('rild','installd')
G.edge['rild']['installd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['rild']['installd']['fill'] = 'red'
G.add_edge('rild','itsonbs')
G.edge['rild']['itsonbs']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['rild']['itsonbs']['fill'] = 'red'
G.add_edge('rild','logwrapper')
G.edge['rild']['logwrapper']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['rild']['logwrapper']['fill'] = 'red'
G.add_edge('rild','netd')
G.edge['rild']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read]'
G.edge['rild']['netd']['fill'] = 'red'
G.add_edge('rild','qmuxd')
G.edge['rild']['qmuxd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['rild']['qmuxd']['fill'] = 'red'
G.add_edge('rild','rild')
G.edge['rild']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read]'
G.edge['rild']['rild']['fill'] = 'red'
G.add_edge('rild','rmt_storage')
G.edge['rild']['rmt_storage']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['rild']['rmt_storage']['fill'] = 'red'
G.add_edge('rild','sdcardd')
G.edge['rild']['sdcardd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['rild']['sdcardd']['fill'] = 'red'
G.add_edge('rild','shell')
G.edge['rild']['shell']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['rild']['shell']['fill'] = 'red'
G.add_edge('rild','s_system_app')
G.edge['rild']['s_system_app']['write-read'] = '[setattr getattr][setopt getopt][open open][setattr getattr][write read]'
G.edge['rild']['s_system_app']['fill'] = 'red'
G.add_edge('rild','system_app')
G.edge['rild']['system_app']['write-read'] = '[setattr getattr][setopt getopt][open open][setattr getattr][write read]'
G.edge['rild']['system_app']['fill'] = 'red'
G.add_edge('rild','system_server')
G.edge['rild']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read]'
G.edge['rild']['system_server']['fill'] = 'red'
G.add_edge('rild','vmwared')
G.edge['rild']['vmwared']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['rild']['vmwared']['fill'] = 'red'
G.add_edge('rild','wpa')
G.edge['rild']['wpa']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['rild']['wpa']['fill'] = 'red'
G.add_edge('rild','zygote')
G.edge['rild']['zygote']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['rild']['zygote']['fill'] = 'red'
G.add_edge('rild','adbd')
G.edge['rild']['adbd']['write-read'] = '[write read][add_name search]'
G.add_edge('rild','at_distributor')
G.edge['rild']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('rild','at_distributor')
G.edge['rild']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('rild','auditd')
G.edge['rild']['auditd']['write-read'] = '[add_name search]'
G.add_edge('rild','cbd')
G.edge['rild']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('rild','cbd')
G.edge['rild']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('rild','charon')
G.edge['rild']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('rild','charon')
G.edge['rild']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('rild','clatd')
G.edge['rild']['clatd']['write-read'] = '[add_name search]'
G.add_edge('rild','debuggerd')
G.edge['rild']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('rild','debuggerd')
G.edge['rild']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('rild','dhcp')
G.edge['rild']['dhcp']['write-read'] = '[write read][add_name search]'
G.add_edge('rild','diag_uart_log')
G.edge['rild']['diag_uart_log']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('rild','diag_uart_log')
G.edge['rild']['diag_uart_log']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('rild','dumpstate')
G.edge['rild']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('rild','dumpstate')
G.edge['rild']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('rild','hostapd')
G.edge['rild']['hostapd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('rild','hostapd')
G.edge['rild']['hostapd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('rild','hvdcp')
G.edge['rild']['hvdcp']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][add_name search]'
G.add_edge('rild','ime_app')
G.edge['rild']['ime_app']['write-read'] = '[setattr getattr][setopt getopt][open open][setattr getattr][write read][add_name search]'
G.add_edge('rild','ime_app')
G.edge['rild']['ime_app']['write-read'] = '[setattr getattr][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('rild','init_shell')
G.edge['rild']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('rild','init_shell')
G.edge['rild']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('rild','installd')
G.edge['rild']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('rild','installd')
G.edge['rild']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('rild','itsonbs')
G.edge['rild']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('rild','itsonbs')
G.edge['rild']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('rild','jackservice')
G.edge['rild']['jackservice']['write-read'] = '[add_name search]'
G.add_edge('rild','lmkd')
G.edge['rild']['lmkd']['write-read'] = '[remove_name search]'
G.add_edge('rild','logwrapper')
G.edge['rild']['logwrapper']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('rild','logwrapper')
G.edge['rild']['logwrapper']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('rild','msm_irqbalanced')
G.edge['rild']['msm_irqbalanced']['write-read'] = '[add_name search]'
G.add_edge('rild','netd')
G.edge['rild']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('rild','netd')
G.edge['rild']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('rild','qmuxd')
G.edge['rild']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('rild','qmuxd')
G.edge['rild']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('rild','racoon')
G.edge['rild']['racoon']['write-read'] = '[add_name search]'
G.add_edge('rild','rild')
G.edge['rild']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('rild','rild')
G.edge['rild']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('rild','rmt_storage')
G.edge['rild']['rmt_storage']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('rild','rmt_storage')
G.edge['rild']['rmt_storage']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('rild','sdcardd')
G.edge['rild']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('rild','sdcardd')
G.edge['rild']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('rild','sensors')
G.edge['rild']['sensors']['write-read'] = '[add_name search]'
G.add_edge('rild','shell')
G.edge['rild']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('rild','shell')
G.edge['rild']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('rild','s_system_app')
G.edge['rild']['s_system_app']['write-read'] = '[setattr getattr][setopt getopt][open open][setattr getattr][write read][add_name search]'
G.add_edge('rild','s_system_app')
G.edge['rild']['s_system_app']['write-read'] = '[setattr getattr][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('rild','system_app')
G.edge['rild']['system_app']['write-read'] = '[setattr getattr][setopt getopt][open open][setattr getattr][write read][add_name search]'
G.add_edge('rild','system_app')
G.edge['rild']['system_app']['write-read'] = '[setattr getattr][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('rild','system_server')
G.edge['rild']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('rild','system_server')
G.edge['rild']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('rild','system_server')
G.edge['rild']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search]'
G.add_edge('rild','vmwared')
G.edge['rild']['vmwared']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('rild','vmwared')
G.edge['rild']['vmwared']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('rild','wpa')
G.edge['rild']['wpa']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('rild','wpa')
G.edge['rild']['wpa']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('rild','zygote')
G.edge['rild']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('rild','zygote')
G.edge['rild']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('rmt_storage','at_distributor')
G.edge['rmt_storage']['at_distributor']['write-read'] = '[open open]'
G.add_edge('rmt_storage','cbd')
G.edge['rmt_storage']['cbd']['write-read'] = '[open open]'
G.add_edge('rmt_storage','charon')
G.edge['rmt_storage']['charon']['write-read'] = '[open open]'
G.add_edge('rmt_storage','debuggerd')
G.edge['rmt_storage']['debuggerd']['write-read'] = '[open open]'
G.add_edge('rmt_storage','diag_uart_log')
G.edge['rmt_storage']['diag_uart_log']['write-read'] = '[open open]'
G.add_edge('rmt_storage','dumpstate')
G.edge['rmt_storage']['dumpstate']['write-read'] = '[open open]'
G.add_edge('rmt_storage','hostapd')
G.edge['rmt_storage']['hostapd']['write-read'] = '[open open]'
G.add_edge('rmt_storage','ime_app')
G.edge['rmt_storage']['ime_app']['write-read'] = '[open open]'
G.add_edge('rmt_storage','init_shell')
G.edge['rmt_storage']['init_shell']['write-read'] = '[open open]'
G.add_edge('rmt_storage','installd')
G.edge['rmt_storage']['installd']['write-read'] = '[open open]'
G.add_edge('rmt_storage','itsonbs')
G.edge['rmt_storage']['itsonbs']['write-read'] = '[open open]'
G.add_edge('rmt_storage','logwrapper')
G.edge['rmt_storage']['logwrapper']['write-read'] = '[open open]'
G.add_edge('rmt_storage','netd')
G.edge['rmt_storage']['netd']['write-read'] = '[open open]'
G.add_edge('rmt_storage','qmuxd')
G.edge['rmt_storage']['qmuxd']['write-read'] = '[open open]'
G.add_edge('rmt_storage','rild')
G.edge['rmt_storage']['rild']['write-read'] = '[open open]'
G.add_edge('rmt_storage','rmt_storage')
G.edge['rmt_storage']['rmt_storage']['write-read'] = '[open open][write read][append read][write read][open open]'
G.add_edge('rmt_storage','sdcardd')
G.edge['rmt_storage']['sdcardd']['write-read'] = '[open open]'
G.add_edge('rmt_storage','shell')
G.edge['rmt_storage']['shell']['write-read'] = '[open open]'
G.add_edge('rmt_storage','s_system_app')
G.edge['rmt_storage']['s_system_app']['write-read'] = '[open open]'
G.add_edge('rmt_storage','system_app')
G.edge['rmt_storage']['system_app']['write-read'] = '[open open]'
G.add_edge('rmt_storage','system_server')
G.edge['rmt_storage']['system_server']['write-read'] = '[open open]'
G.add_edge('rmt_storage','vmwared')
G.edge['rmt_storage']['vmwared']['write-read'] = '[open open]'
G.add_edge('rmt_storage','wpa')
G.edge['rmt_storage']['wpa']['write-read'] = '[open open]'
G.add_edge('rmt_storage','zygote')
G.edge['rmt_storage']['zygote']['write-read'] = '[open open]'
G.add_edge('rmt_storage','at_distributor')
G.edge['rmt_storage']['at_distributor']['write-read'] = '[open open][setattr getattr]'
G.add_edge('rmt_storage','cbd')
G.edge['rmt_storage']['cbd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('rmt_storage','charon')
G.edge['rmt_storage']['charon']['write-read'] = '[open open][setattr getattr]'
G.add_edge('rmt_storage','debuggerd')
G.edge['rmt_storage']['debuggerd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('rmt_storage','diag_uart_log')
G.edge['rmt_storage']['diag_uart_log']['write-read'] = '[open open][setattr getattr]'
G.add_edge('rmt_storage','dumpstate')
G.edge['rmt_storage']['dumpstate']['write-read'] = '[open open][setattr getattr]'
G.add_edge('rmt_storage','hostapd')
G.edge['rmt_storage']['hostapd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('rmt_storage','ime_app')
G.edge['rmt_storage']['ime_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('rmt_storage','init_shell')
G.edge['rmt_storage']['init_shell']['write-read'] = '[open open][setattr getattr]'
G.add_edge('rmt_storage','installd')
G.edge['rmt_storage']['installd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('rmt_storage','itsonbs')
G.edge['rmt_storage']['itsonbs']['write-read'] = '[open open][setattr getattr]'
G.add_edge('rmt_storage','logwrapper')
G.edge['rmt_storage']['logwrapper']['write-read'] = '[open open][setattr getattr]'
G.add_edge('rmt_storage','netd')
G.edge['rmt_storage']['netd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('rmt_storage','qmuxd')
G.edge['rmt_storage']['qmuxd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('rmt_storage','rild')
G.edge['rmt_storage']['rild']['write-read'] = '[open open][setattr getattr]'
G.add_edge('rmt_storage','rmt_storage')
G.edge['rmt_storage']['rmt_storage']['write-read'] = '[open open][write read][append read][write read][open open][setattr getattr]'
G.add_edge('rmt_storage','sdcardd')
G.edge['rmt_storage']['sdcardd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('rmt_storage','shell')
G.edge['rmt_storage']['shell']['write-read'] = '[open open][setattr getattr]'
G.add_edge('rmt_storage','s_system_app')
G.edge['rmt_storage']['s_system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('rmt_storage','system_app')
G.edge['rmt_storage']['system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('rmt_storage','system_server')
G.edge['rmt_storage']['system_server']['write-read'] = '[open open][setattr getattr]'
G.add_edge('rmt_storage','vmwared')
G.edge['rmt_storage']['vmwared']['write-read'] = '[open open][setattr getattr]'
G.add_edge('rmt_storage','wpa')
G.edge['rmt_storage']['wpa']['write-read'] = '[open open][setattr getattr]'
G.add_edge('rmt_storage','zygote')
G.edge['rmt_storage']['zygote']['write-read'] = '[open open][setattr getattr]'
G.add_edge('rmt_storage','adbd')
G.edge['rmt_storage']['adbd']['write-read'] = '[write read]'
G.edge['rmt_storage']['adbd']['fill'] = 'red'
G.add_edge('rmt_storage','at_distributor')
G.edge['rmt_storage']['at_distributor']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['rmt_storage']['at_distributor']['fill'] = 'red'
G.add_edge('rmt_storage','cbd')
G.edge['rmt_storage']['cbd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['rmt_storage']['cbd']['fill'] = 'red'
G.add_edge('rmt_storage','charon')
G.edge['rmt_storage']['charon']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['rmt_storage']['charon']['fill'] = 'red'
G.add_edge('rmt_storage','debuggerd')
G.edge['rmt_storage']['debuggerd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['rmt_storage']['debuggerd']['fill'] = 'red'
G.add_edge('rmt_storage','dhcp')
G.edge['rmt_storage']['dhcp']['write-read'] = '[write read]'
G.edge['rmt_storage']['dhcp']['fill'] = 'red'
G.add_edge('rmt_storage','diag_uart_log')
G.edge['rmt_storage']['diag_uart_log']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['rmt_storage']['diag_uart_log']['fill'] = 'red'
G.add_edge('rmt_storage','domain')
G.edge['rmt_storage']['domain']['write-read'] = '[write read]'
G.edge['rmt_storage']['domain']['fill'] = 'red'
G.add_edge('rmt_storage','dumpstate')
G.edge['rmt_storage']['dumpstate']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['rmt_storage']['dumpstate']['fill'] = 'red'
G.add_edge('rmt_storage','hostapd')
G.edge['rmt_storage']['hostapd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['rmt_storage']['hostapd']['fill'] = 'red'
G.add_edge('rmt_storage','ime_app')
G.edge['rmt_storage']['ime_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['rmt_storage']['ime_app']['fill'] = 'red'
G.add_edge('rmt_storage','init_shell')
G.edge['rmt_storage']['init_shell']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['rmt_storage']['init_shell']['fill'] = 'red'
G.add_edge('rmt_storage','installd')
G.edge['rmt_storage']['installd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['rmt_storage']['installd']['fill'] = 'red'
G.add_edge('rmt_storage','itsonbs')
G.edge['rmt_storage']['itsonbs']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['rmt_storage']['itsonbs']['fill'] = 'red'
G.add_edge('rmt_storage','logwrapper')
G.edge['rmt_storage']['logwrapper']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['rmt_storage']['logwrapper']['fill'] = 'red'
G.add_edge('rmt_storage','netd')
G.edge['rmt_storage']['netd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['rmt_storage']['netd']['fill'] = 'red'
G.add_edge('rmt_storage','qmuxd')
G.edge['rmt_storage']['qmuxd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['rmt_storage']['qmuxd']['fill'] = 'red'
G.add_edge('rmt_storage','rild')
G.edge['rmt_storage']['rild']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['rmt_storage']['rild']['fill'] = 'red'
G.add_edge('rmt_storage','rmt_storage')
G.edge['rmt_storage']['rmt_storage']['write-read'] = '[open open][write read][append read][write read][open open][setattr getattr][write read]'
G.edge['rmt_storage']['rmt_storage']['fill'] = 'red'
G.add_edge('rmt_storage','sdcardd')
G.edge['rmt_storage']['sdcardd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['rmt_storage']['sdcardd']['fill'] = 'red'
G.add_edge('rmt_storage','shell')
G.edge['rmt_storage']['shell']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['rmt_storage']['shell']['fill'] = 'red'
G.add_edge('rmt_storage','s_system_app')
G.edge['rmt_storage']['s_system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['rmt_storage']['s_system_app']['fill'] = 'red'
G.add_edge('rmt_storage','system_app')
G.edge['rmt_storage']['system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['rmt_storage']['system_app']['fill'] = 'red'
G.add_edge('rmt_storage','system_server')
G.edge['rmt_storage']['system_server']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['rmt_storage']['system_server']['fill'] = 'red'
G.add_edge('rmt_storage','vmwared')
G.edge['rmt_storage']['vmwared']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['rmt_storage']['vmwared']['fill'] = 'red'
G.add_edge('rmt_storage','wpa')
G.edge['rmt_storage']['wpa']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['rmt_storage']['wpa']['fill'] = 'red'
G.add_edge('rmt_storage','zygote')
G.edge['rmt_storage']['zygote']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['rmt_storage']['zygote']['fill'] = 'red'
G.add_edge('rmt_storage','adbd')
G.edge['rmt_storage']['adbd']['write-read'] = '[write read][add_name search]'
G.add_edge('rmt_storage','at_distributor')
G.edge['rmt_storage']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('rmt_storage','at_distributor')
G.edge['rmt_storage']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('rmt_storage','auditd')
G.edge['rmt_storage']['auditd']['write-read'] = '[add_name search]'
G.add_edge('rmt_storage','cbd')
G.edge['rmt_storage']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('rmt_storage','cbd')
G.edge['rmt_storage']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('rmt_storage','charon')
G.edge['rmt_storage']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('rmt_storage','charon')
G.edge['rmt_storage']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('rmt_storage','clatd')
G.edge['rmt_storage']['clatd']['write-read'] = '[add_name search]'
G.add_edge('rmt_storage','debuggerd')
G.edge['rmt_storage']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('rmt_storage','debuggerd')
G.edge['rmt_storage']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('rmt_storage','dhcp')
G.edge['rmt_storage']['dhcp']['write-read'] = '[write read][add_name search]'
G.add_edge('rmt_storage','diag_uart_log')
G.edge['rmt_storage']['diag_uart_log']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('rmt_storage','diag_uart_log')
G.edge['rmt_storage']['diag_uart_log']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('rmt_storage','dumpstate')
G.edge['rmt_storage']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('rmt_storage','dumpstate')
G.edge['rmt_storage']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('rmt_storage','hostapd')
G.edge['rmt_storage']['hostapd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('rmt_storage','hostapd')
G.edge['rmt_storage']['hostapd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('rmt_storage','hvdcp')
G.edge['rmt_storage']['hvdcp']['write-read'] = '[add_name search]'
G.add_edge('rmt_storage','ime_app')
G.edge['rmt_storage']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('rmt_storage','ime_app')
G.edge['rmt_storage']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('rmt_storage','init_shell')
G.edge['rmt_storage']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('rmt_storage','init_shell')
G.edge['rmt_storage']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('rmt_storage','installd')
G.edge['rmt_storage']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('rmt_storage','installd')
G.edge['rmt_storage']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('rmt_storage','itsonbs')
G.edge['rmt_storage']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('rmt_storage','itsonbs')
G.edge['rmt_storage']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('rmt_storage','jackservice')
G.edge['rmt_storage']['jackservice']['write-read'] = '[add_name search]'
G.add_edge('rmt_storage','lmkd')
G.edge['rmt_storage']['lmkd']['write-read'] = '[remove_name search]'
G.add_edge('rmt_storage','logwrapper')
G.edge['rmt_storage']['logwrapper']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('rmt_storage','logwrapper')
G.edge['rmt_storage']['logwrapper']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('rmt_storage','msm_irqbalanced')
G.edge['rmt_storage']['msm_irqbalanced']['write-read'] = '[add_name search]'
G.add_edge('rmt_storage','netd')
G.edge['rmt_storage']['netd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('rmt_storage','netd')
G.edge['rmt_storage']['netd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('rmt_storage','qmuxd')
G.edge['rmt_storage']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('rmt_storage','qmuxd')
G.edge['rmt_storage']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('rmt_storage','racoon')
G.edge['rmt_storage']['racoon']['write-read'] = '[add_name search]'
G.add_edge('rmt_storage','rild')
G.edge['rmt_storage']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('rmt_storage','rild')
G.edge['rmt_storage']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('rmt_storage','rmt_storage')
G.edge['rmt_storage']['rmt_storage']['write-read'] = '[open open][write read][append read][write read][open open][setattr getattr][write read][add_name search]'
G.add_edge('rmt_storage','rmt_storage')
G.edge['rmt_storage']['rmt_storage']['write-read'] = '[open open][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('rmt_storage','sdcardd')
G.edge['rmt_storage']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('rmt_storage','sdcardd')
G.edge['rmt_storage']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('rmt_storage','sensors')
G.edge['rmt_storage']['sensors']['write-read'] = '[add_name search]'
G.add_edge('rmt_storage','shell')
G.edge['rmt_storage']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('rmt_storage','shell')
G.edge['rmt_storage']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('rmt_storage','s_system_app')
G.edge['rmt_storage']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('rmt_storage','s_system_app')
G.edge['rmt_storage']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('rmt_storage','system_app')
G.edge['rmt_storage']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('rmt_storage','system_app')
G.edge['rmt_storage']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('rmt_storage','system_server')
G.edge['rmt_storage']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('rmt_storage','system_server')
G.edge['rmt_storage']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('rmt_storage','system_server')
G.edge['rmt_storage']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search]'
G.add_edge('rmt_storage','vmwared')
G.edge['rmt_storage']['vmwared']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('rmt_storage','vmwared')
G.edge['rmt_storage']['vmwared']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('rmt_storage','wpa')
G.edge['rmt_storage']['wpa']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('rmt_storage','wpa')
G.edge['rmt_storage']['wpa']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('rmt_storage','zygote')
G.edge['rmt_storage']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('rmt_storage','zygote')
G.edge['rmt_storage']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('sdcardd','at_distributor')
G.edge['sdcardd']['at_distributor']['write-read'] = '[open open]'
G.add_edge('sdcardd','cbd')
G.edge['sdcardd']['cbd']['write-read'] = '[open open]'
G.add_edge('sdcardd','charon')
G.edge['sdcardd']['charon']['write-read'] = '[open open]'
G.add_edge('sdcardd','debuggerd')
G.edge['sdcardd']['debuggerd']['write-read'] = '[open open]'
G.add_edge('sdcardd','diag_uart_log')
G.edge['sdcardd']['diag_uart_log']['write-read'] = '[open open]'
G.add_edge('sdcardd','dumpstate')
G.edge['sdcardd']['dumpstate']['write-read'] = '[open open]'
G.add_edge('sdcardd','hostapd')
G.edge['sdcardd']['hostapd']['write-read'] = '[open open]'
G.add_edge('sdcardd','ime_app')
G.edge['sdcardd']['ime_app']['write-read'] = '[open open]'
G.add_edge('sdcardd','init_shell')
G.edge['sdcardd']['init_shell']['write-read'] = '[open open][open open]'
G.add_edge('sdcardd','installd')
G.edge['sdcardd']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('sdcardd','itsonbs')
G.edge['sdcardd']['itsonbs']['write-read'] = '[open open]'
G.add_edge('sdcardd','logwrapper')
G.edge['sdcardd']['logwrapper']['write-read'] = '[open open]'
G.add_edge('sdcardd','netd')
G.edge['sdcardd']['netd']['write-read'] = '[open open]'
G.add_edge('sdcardd','qmuxd')
G.edge['sdcardd']['qmuxd']['write-read'] = '[open open]'
G.add_edge('sdcardd','rild')
G.edge['sdcardd']['rild']['write-read'] = '[open open]'
G.add_edge('sdcardd','rmt_storage')
G.edge['sdcardd']['rmt_storage']['write-read'] = '[open open]'
G.add_edge('sdcardd','sdcardd')
G.edge['sdcardd']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('sdcardd','shell')
G.edge['sdcardd']['shell']['write-read'] = '[open open]'
G.add_edge('sdcardd','s_system_app')
G.edge['sdcardd']['s_system_app']['write-read'] = '[open open]'
G.add_edge('sdcardd','system_app')
G.edge['sdcardd']['system_app']['write-read'] = '[open open]'
G.add_edge('sdcardd','system_server')
G.edge['sdcardd']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('sdcardd','vmwared')
G.edge['sdcardd']['vmwared']['write-read'] = '[open open]'
G.add_edge('sdcardd','wpa')
G.edge['sdcardd']['wpa']['write-read'] = '[open open]'
G.add_edge('sdcardd','zygote')
G.edge['sdcardd']['zygote']['write-read'] = '[open open]'
G.add_edge('sdcardd','at_distributor')
G.edge['sdcardd']['at_distributor']['write-read'] = '[open open][setattr getattr]'
G.add_edge('sdcardd','cbd')
G.edge['sdcardd']['cbd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('sdcardd','charon')
G.edge['sdcardd']['charon']['write-read'] = '[open open][setattr getattr]'
G.add_edge('sdcardd','debuggerd')
G.edge['sdcardd']['debuggerd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('sdcardd','diag_uart_log')
G.edge['sdcardd']['diag_uart_log']['write-read'] = '[open open][setattr getattr]'
G.add_edge('sdcardd','dumpstate')
G.edge['sdcardd']['dumpstate']['write-read'] = '[open open][setattr getattr]'
G.add_edge('sdcardd','hostapd')
G.edge['sdcardd']['hostapd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('sdcardd','ime_app')
G.edge['sdcardd']['ime_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('sdcardd','init_shell')
G.edge['sdcardd']['init_shell']['write-read'] = '[open open][open open][setattr getattr]'
G.add_edge('sdcardd','installd')
G.edge['sdcardd']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('sdcardd','itsonbs')
G.edge['sdcardd']['itsonbs']['write-read'] = '[open open][setattr getattr]'
G.add_edge('sdcardd','logwrapper')
G.edge['sdcardd']['logwrapper']['write-read'] = '[open open][setattr getattr]'
G.add_edge('sdcardd','netd')
G.edge['sdcardd']['netd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('sdcardd','qmuxd')
G.edge['sdcardd']['qmuxd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('sdcardd','rild')
G.edge['sdcardd']['rild']['write-read'] = '[open open][setattr getattr]'
G.add_edge('sdcardd','rmt_storage')
G.edge['sdcardd']['rmt_storage']['write-read'] = '[open open][setattr getattr]'
G.add_edge('sdcardd','sdcardd')
G.edge['sdcardd']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('sdcardd','shell')
G.edge['sdcardd']['shell']['write-read'] = '[open open][setattr getattr]'
G.add_edge('sdcardd','s_system_app')
G.edge['sdcardd']['s_system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('sdcardd','system_app')
G.edge['sdcardd']['system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('sdcardd','system_server')
G.edge['sdcardd']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('sdcardd','vmwared')
G.edge['sdcardd']['vmwared']['write-read'] = '[open open][setattr getattr]'
G.add_edge('sdcardd','wpa')
G.edge['sdcardd']['wpa']['write-read'] = '[open open][setattr getattr]'
G.add_edge('sdcardd','zygote')
G.edge['sdcardd']['zygote']['write-read'] = '[open open][setattr getattr]'
G.add_edge('sdcardd','adbd')
G.edge['sdcardd']['adbd']['write-read'] = '[write read]'
G.edge['sdcardd']['adbd']['fill'] = 'red'
G.add_edge('sdcardd','at_distributor')
G.edge['sdcardd']['at_distributor']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['sdcardd']['at_distributor']['fill'] = 'red'
G.add_edge('sdcardd','cbd')
G.edge['sdcardd']['cbd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['sdcardd']['cbd']['fill'] = 'red'
G.add_edge('sdcardd','charon')
G.edge['sdcardd']['charon']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['sdcardd']['charon']['fill'] = 'red'
G.add_edge('sdcardd','debuggerd')
G.edge['sdcardd']['debuggerd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['sdcardd']['debuggerd']['fill'] = 'red'
G.add_edge('sdcardd','dhcp')
G.edge['sdcardd']['dhcp']['write-read'] = '[write read]'
G.edge['sdcardd']['dhcp']['fill'] = 'red'
G.add_edge('sdcardd','diag_uart_log')
G.edge['sdcardd']['diag_uart_log']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['sdcardd']['diag_uart_log']['fill'] = 'red'
G.add_edge('sdcardd','domain')
G.edge['sdcardd']['domain']['write-read'] = '[write read]'
G.edge['sdcardd']['domain']['fill'] = 'red'
G.add_edge('sdcardd','dumpstate')
G.edge['sdcardd']['dumpstate']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['sdcardd']['dumpstate']['fill'] = 'red'
G.add_edge('sdcardd','hostapd')
G.edge['sdcardd']['hostapd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['sdcardd']['hostapd']['fill'] = 'red'
G.add_edge('sdcardd','ime_app')
G.edge['sdcardd']['ime_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['sdcardd']['ime_app']['fill'] = 'red'
G.add_edge('sdcardd','init_shell')
G.edge['sdcardd']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read]'
G.edge['sdcardd']['init_shell']['fill'] = 'red'
G.add_edge('sdcardd','installd')
G.edge['sdcardd']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['sdcardd']['installd']['fill'] = 'red'
G.add_edge('sdcardd','itsonbs')
G.edge['sdcardd']['itsonbs']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['sdcardd']['itsonbs']['fill'] = 'red'
G.add_edge('sdcardd','logwrapper')
G.edge['sdcardd']['logwrapper']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['sdcardd']['logwrapper']['fill'] = 'red'
G.add_edge('sdcardd','netd')
G.edge['sdcardd']['netd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['sdcardd']['netd']['fill'] = 'red'
G.add_edge('sdcardd','qmuxd')
G.edge['sdcardd']['qmuxd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['sdcardd']['qmuxd']['fill'] = 'red'
G.add_edge('sdcardd','rild')
G.edge['sdcardd']['rild']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['sdcardd']['rild']['fill'] = 'red'
G.add_edge('sdcardd','rmt_storage')
G.edge['sdcardd']['rmt_storage']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['sdcardd']['rmt_storage']['fill'] = 'red'
G.add_edge('sdcardd','sdcardd')
G.edge['sdcardd']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['sdcardd']['sdcardd']['fill'] = 'red'
G.add_edge('sdcardd','shell')
G.edge['sdcardd']['shell']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['sdcardd']['shell']['fill'] = 'red'
G.add_edge('sdcardd','s_system_app')
G.edge['sdcardd']['s_system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['sdcardd']['s_system_app']['fill'] = 'red'
G.add_edge('sdcardd','system_app')
G.edge['sdcardd']['system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['sdcardd']['system_app']['fill'] = 'red'
G.add_edge('sdcardd','system_server')
G.edge['sdcardd']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['sdcardd']['system_server']['fill'] = 'red'
G.add_edge('sdcardd','vmwared')
G.edge['sdcardd']['vmwared']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['sdcardd']['vmwared']['fill'] = 'red'
G.add_edge('sdcardd','wpa')
G.edge['sdcardd']['wpa']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['sdcardd']['wpa']['fill'] = 'red'
G.add_edge('sdcardd','zygote')
G.edge['sdcardd']['zygote']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['sdcardd']['zygote']['fill'] = 'red'
G.add_edge('sdcardd','adbd')
G.edge['sdcardd']['adbd']['write-read'] = '[write read][add_name search]'
G.add_edge('sdcardd','at_distributor')
G.edge['sdcardd']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('sdcardd','at_distributor')
G.edge['sdcardd']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('sdcardd','auditd')
G.edge['sdcardd']['auditd']['write-read'] = '[add_name search]'
G.add_edge('sdcardd','cbd')
G.edge['sdcardd']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('sdcardd','cbd')
G.edge['sdcardd']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('sdcardd','charon')
G.edge['sdcardd']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('sdcardd','charon')
G.edge['sdcardd']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('sdcardd','clatd')
G.edge['sdcardd']['clatd']['write-read'] = '[add_name search]'
G.add_edge('sdcardd','debuggerd')
G.edge['sdcardd']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('sdcardd','debuggerd')
G.edge['sdcardd']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('sdcardd','dhcp')
G.edge['sdcardd']['dhcp']['write-read'] = '[write read][add_name search]'
G.add_edge('sdcardd','diag_uart_log')
G.edge['sdcardd']['diag_uart_log']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('sdcardd','diag_uart_log')
G.edge['sdcardd']['diag_uart_log']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('sdcardd','dumpstate')
G.edge['sdcardd']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('sdcardd','dumpstate')
G.edge['sdcardd']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('sdcardd','hostapd')
G.edge['sdcardd']['hostapd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('sdcardd','hostapd')
G.edge['sdcardd']['hostapd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('sdcardd','hvdcp')
G.edge['sdcardd']['hvdcp']['write-read'] = '[add_name search]'
G.add_edge('sdcardd','ime_app')
G.edge['sdcardd']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('sdcardd','ime_app')
G.edge['sdcardd']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('sdcardd','init_shell')
G.edge['sdcardd']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search]'
G.add_edge('sdcardd','init_shell')
G.edge['sdcardd']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('sdcardd','installd')
G.edge['sdcardd']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('sdcardd','installd')
G.edge['sdcardd']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('sdcardd','itsonbs')
G.edge['sdcardd']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('sdcardd','itsonbs')
G.edge['sdcardd']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('sdcardd','jackservice')
G.edge['sdcardd']['jackservice']['write-read'] = '[add_name search]'
G.add_edge('sdcardd','lmkd')
G.edge['sdcardd']['lmkd']['write-read'] = '[remove_name search]'
G.add_edge('sdcardd','logwrapper')
G.edge['sdcardd']['logwrapper']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('sdcardd','logwrapper')
G.edge['sdcardd']['logwrapper']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('sdcardd','msm_irqbalanced')
G.edge['sdcardd']['msm_irqbalanced']['write-read'] = '[add_name search]'
G.add_edge('sdcardd','netd')
G.edge['sdcardd']['netd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('sdcardd','netd')
G.edge['sdcardd']['netd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('sdcardd','qmuxd')
G.edge['sdcardd']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('sdcardd','qmuxd')
G.edge['sdcardd']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('sdcardd','racoon')
G.edge['sdcardd']['racoon']['write-read'] = '[add_name search]'
G.add_edge('sdcardd','rild')
G.edge['sdcardd']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('sdcardd','rild')
G.edge['sdcardd']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('sdcardd','rmt_storage')
G.edge['sdcardd']['rmt_storage']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('sdcardd','rmt_storage')
G.edge['sdcardd']['rmt_storage']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('sdcardd','sdcardd')
G.edge['sdcardd']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('sdcardd','sdcardd')
G.edge['sdcardd']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('sdcardd','sensors')
G.edge['sdcardd']['sensors']['write-read'] = '[add_name search]'
G.add_edge('sdcardd','shell')
G.edge['sdcardd']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('sdcardd','shell')
G.edge['sdcardd']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('sdcardd','s_system_app')
G.edge['sdcardd']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('sdcardd','s_system_app')
G.edge['sdcardd']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('sdcardd','system_app')
G.edge['sdcardd']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('sdcardd','system_app')
G.edge['sdcardd']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('sdcardd','system_server')
G.edge['sdcardd']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('sdcardd','system_server')
G.edge['sdcardd']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('sdcardd','system_server')
G.edge['sdcardd']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search]'
G.add_edge('sdcardd','vmwared')
G.edge['sdcardd']['vmwared']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('sdcardd','vmwared')
G.edge['sdcardd']['vmwared']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('sdcardd','wpa')
G.edge['sdcardd']['wpa']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('sdcardd','wpa')
G.edge['sdcardd']['wpa']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('sdcardd','zygote')
G.edge['sdcardd']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('sdcardd','zygote')
G.edge['sdcardd']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('shell','at_distributor')
G.edge['shell']['at_distributor']['write-read'] = '[open open]'
G.add_edge('shell','cbd')
G.edge['shell']['cbd']['write-read'] = '[open open]'
G.add_edge('shell','charon')
G.edge['shell']['charon']['write-read'] = '[open open]'
G.add_edge('shell','debuggerd')
G.edge['shell']['debuggerd']['write-read'] = '[open open]'
G.add_edge('shell','diag_uart_log')
G.edge['shell']['diag_uart_log']['write-read'] = '[open open]'
G.add_edge('shell','dumpstate')
G.edge['shell']['dumpstate']['write-read'] = '[open open]'
G.add_edge('shell','hostapd')
G.edge['shell']['hostapd']['write-read'] = '[open open]'
G.add_edge('shell','ime_app')
G.edge['shell']['ime_app']['write-read'] = '[open open]'
G.add_edge('shell','init_shell')
G.edge['shell']['init_shell']['write-read'] = '[open open]'
G.add_edge('shell','installd')
G.edge['shell']['installd']['write-read'] = '[open open]'
G.add_edge('shell','itsonbs')
G.edge['shell']['itsonbs']['write-read'] = '[open open]'
G.add_edge('shell','logwrapper')
G.edge['shell']['logwrapper']['write-read'] = '[open open]'
G.add_edge('shell','netd')
G.edge['shell']['netd']['write-read'] = '[open open]'
G.add_edge('shell','qmuxd')
G.edge['shell']['qmuxd']['write-read'] = '[open open]'
G.add_edge('shell','rild')
G.edge['shell']['rild']['write-read'] = '[open open]'
G.add_edge('shell','rmt_storage')
G.edge['shell']['rmt_storage']['write-read'] = '[open open]'
G.add_edge('shell','sdcardd')
G.edge['shell']['sdcardd']['write-read'] = '[open open]'
G.add_edge('shell','shell')
G.edge['shell']['shell']['write-read'] = '[open open]'
G.add_edge('shell','s_system_app')
G.edge['shell']['s_system_app']['write-read'] = '[open open]'
G.add_edge('shell','system_app')
G.edge['shell']['system_app']['write-read'] = '[open open]'
G.add_edge('shell','system_server')
G.edge['shell']['system_server']['write-read'] = '[open open]'
G.add_edge('shell','vmwared')
G.edge['shell']['vmwared']['write-read'] = '[open open]'
G.add_edge('shell','wpa')
G.edge['shell']['wpa']['write-read'] = '[open open]'
G.add_edge('shell','zygote')
G.edge['shell']['zygote']['write-read'] = '[open open]'
G.add_edge('shell','at_distributor')
G.edge['shell']['at_distributor']['write-read'] = '[open open][setattr getattr]'
G.add_edge('shell','cbd')
G.edge['shell']['cbd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('shell','charon')
G.edge['shell']['charon']['write-read'] = '[open open][setattr getattr]'
G.add_edge('shell','debuggerd')
G.edge['shell']['debuggerd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('shell','diag_uart_log')
G.edge['shell']['diag_uart_log']['write-read'] = '[open open][setattr getattr]'
G.add_edge('shell','dumpstate')
G.edge['shell']['dumpstate']['write-read'] = '[open open][setattr getattr]'
G.add_edge('shell','hostapd')
G.edge['shell']['hostapd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('shell','ime_app')
G.edge['shell']['ime_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('shell','init_shell')
G.edge['shell']['init_shell']['write-read'] = '[open open][setattr getattr]'
G.add_edge('shell','installd')
G.edge['shell']['installd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('shell','itsonbs')
G.edge['shell']['itsonbs']['write-read'] = '[open open][setattr getattr]'
G.add_edge('shell','logwrapper')
G.edge['shell']['logwrapper']['write-read'] = '[open open][setattr getattr]'
G.add_edge('shell','netd')
G.edge['shell']['netd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('shell','qmuxd')
G.edge['shell']['qmuxd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('shell','rild')
G.edge['shell']['rild']['write-read'] = '[open open][setattr getattr]'
G.add_edge('shell','rmt_storage')
G.edge['shell']['rmt_storage']['write-read'] = '[open open][setattr getattr]'
G.add_edge('shell','sdcardd')
G.edge['shell']['sdcardd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('shell','shell')
G.edge['shell']['shell']['write-read'] = '[open open][setattr getattr]'
G.add_edge('shell','s_system_app')
G.edge['shell']['s_system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('shell','system_app')
G.edge['shell']['system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('shell','system_server')
G.edge['shell']['system_server']['write-read'] = '[open open][setattr getattr]'
G.add_edge('shell','vmwared')
G.edge['shell']['vmwared']['write-read'] = '[open open][setattr getattr]'
G.add_edge('shell','wpa')
G.edge['shell']['wpa']['write-read'] = '[open open][setattr getattr]'
G.add_edge('shell','zygote')
G.edge['shell']['zygote']['write-read'] = '[open open][setattr getattr]'
G.add_edge('shell','adbd')
G.edge['shell']['adbd']['write-read'] = '[write read]'
G.edge['shell']['adbd']['fill'] = 'red'
G.add_edge('shell','at_distributor')
G.edge['shell']['at_distributor']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['shell']['at_distributor']['fill'] = 'red'
G.add_edge('shell','cbd')
G.edge['shell']['cbd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['shell']['cbd']['fill'] = 'red'
G.add_edge('shell','charon')
G.edge['shell']['charon']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['shell']['charon']['fill'] = 'red'
G.add_edge('shell','debuggerd')
G.edge['shell']['debuggerd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['shell']['debuggerd']['fill'] = 'red'
G.add_edge('shell','dhcp')
G.edge['shell']['dhcp']['write-read'] = '[write read]'
G.edge['shell']['dhcp']['fill'] = 'red'
G.add_edge('shell','diag_uart_log')
G.edge['shell']['diag_uart_log']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['shell']['diag_uart_log']['fill'] = 'red'
G.add_edge('shell','domain')
G.edge['shell']['domain']['write-read'] = '[write read]'
G.edge['shell']['domain']['fill'] = 'red'
G.add_edge('shell','dumpstate')
G.edge['shell']['dumpstate']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['shell']['dumpstate']['fill'] = 'red'
G.add_edge('shell','hostapd')
G.edge['shell']['hostapd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['shell']['hostapd']['fill'] = 'red'
G.add_edge('shell','ime_app')
G.edge['shell']['ime_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['shell']['ime_app']['fill'] = 'red'
G.add_edge('shell','init_shell')
G.edge['shell']['init_shell']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['shell']['init_shell']['fill'] = 'red'
G.add_edge('shell','installd')
G.edge['shell']['installd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['shell']['installd']['fill'] = 'red'
G.add_edge('shell','itsonbs')
G.edge['shell']['itsonbs']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['shell']['itsonbs']['fill'] = 'red'
G.add_edge('shell','logwrapper')
G.edge['shell']['logwrapper']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['shell']['logwrapper']['fill'] = 'red'
G.add_edge('shell','netd')
G.edge['shell']['netd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['shell']['netd']['fill'] = 'red'
G.add_edge('shell','qmuxd')
G.edge['shell']['qmuxd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['shell']['qmuxd']['fill'] = 'red'
G.add_edge('shell','rild')
G.edge['shell']['rild']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['shell']['rild']['fill'] = 'red'
G.add_edge('shell','rmt_storage')
G.edge['shell']['rmt_storage']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['shell']['rmt_storage']['fill'] = 'red'
G.add_edge('shell','sdcardd')
G.edge['shell']['sdcardd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['shell']['sdcardd']['fill'] = 'red'
G.add_edge('shell','shell')
G.edge['shell']['shell']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['shell']['shell']['fill'] = 'red'
G.add_edge('shell','s_system_app')
G.edge['shell']['s_system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['shell']['s_system_app']['fill'] = 'red'
G.add_edge('shell','system_app')
G.edge['shell']['system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['shell']['system_app']['fill'] = 'red'
G.add_edge('shell','system_server')
G.edge['shell']['system_server']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['shell']['system_server']['fill'] = 'red'
G.add_edge('shell','vmwared')
G.edge['shell']['vmwared']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['shell']['vmwared']['fill'] = 'red'
G.add_edge('shell','wpa')
G.edge['shell']['wpa']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['shell']['wpa']['fill'] = 'red'
G.add_edge('shell','zygote')
G.edge['shell']['zygote']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['shell']['zygote']['fill'] = 'red'
G.add_edge('shell','adbd')
G.edge['shell']['adbd']['write-read'] = '[write read][add_name search]'
G.add_edge('shell','at_distributor')
G.edge['shell']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('shell','at_distributor')
G.edge['shell']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('shell','auditd')
G.edge['shell']['auditd']['write-read'] = '[add_name search]'
G.add_edge('shell','cbd')
G.edge['shell']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('shell','cbd')
G.edge['shell']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('shell','charon')
G.edge['shell']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('shell','charon')
G.edge['shell']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('shell','clatd')
G.edge['shell']['clatd']['write-read'] = '[add_name search]'
G.add_edge('shell','debuggerd')
G.edge['shell']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('shell','debuggerd')
G.edge['shell']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('shell','dhcp')
G.edge['shell']['dhcp']['write-read'] = '[write read][add_name search]'
G.add_edge('shell','diag_uart_log')
G.edge['shell']['diag_uart_log']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('shell','diag_uart_log')
G.edge['shell']['diag_uart_log']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('shell','dumpstate')
G.edge['shell']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('shell','dumpstate')
G.edge['shell']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('shell','hostapd')
G.edge['shell']['hostapd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('shell','hostapd')
G.edge['shell']['hostapd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('shell','hvdcp')
G.edge['shell']['hvdcp']['write-read'] = '[add_name search]'
G.add_edge('shell','ime_app')
G.edge['shell']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('shell','ime_app')
G.edge['shell']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('shell','init_shell')
G.edge['shell']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('shell','init_shell')
G.edge['shell']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('shell','installd')
G.edge['shell']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('shell','installd')
G.edge['shell']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('shell','itsonbs')
G.edge['shell']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('shell','itsonbs')
G.edge['shell']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('shell','jackservice')
G.edge['shell']['jackservice']['write-read'] = '[add_name search]'
G.add_edge('shell','lmkd')
G.edge['shell']['lmkd']['write-read'] = '[remove_name search]'
G.add_edge('shell','logwrapper')
G.edge['shell']['logwrapper']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('shell','logwrapper')
G.edge['shell']['logwrapper']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('shell','msm_irqbalanced')
G.edge['shell']['msm_irqbalanced']['write-read'] = '[add_name search]'
G.add_edge('shell','netd')
G.edge['shell']['netd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('shell','netd')
G.edge['shell']['netd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('shell','qmuxd')
G.edge['shell']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('shell','qmuxd')
G.edge['shell']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('shell','racoon')
G.edge['shell']['racoon']['write-read'] = '[add_name search]'
G.add_edge('shell','rild')
G.edge['shell']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('shell','rild')
G.edge['shell']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('shell','rmt_storage')
G.edge['shell']['rmt_storage']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('shell','rmt_storage')
G.edge['shell']['rmt_storage']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('shell','sdcardd')
G.edge['shell']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('shell','sdcardd')
G.edge['shell']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('shell','sensors')
G.edge['shell']['sensors']['write-read'] = '[add_name search]'
G.add_edge('shell','shell')
G.edge['shell']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('shell','shell')
G.edge['shell']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('shell','s_system_app')
G.edge['shell']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('shell','s_system_app')
G.edge['shell']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('shell','system_app')
G.edge['shell']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('shell','system_app')
G.edge['shell']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('shell','system_server')
G.edge['shell']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('shell','system_server')
G.edge['shell']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('shell','system_server')
G.edge['shell']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search]'
G.add_edge('shell','vmwared')
G.edge['shell']['vmwared']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('shell','vmwared')
G.edge['shell']['vmwared']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('shell','wpa')
G.edge['shell']['wpa']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('shell','wpa')
G.edge['shell']['wpa']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('shell','zygote')
G.edge['shell']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('shell','zygote')
G.edge['shell']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('s_system_app','at_distributor')
G.edge['s_system_app']['at_distributor']['write-read'] = '[open open]'
G.add_edge('s_system_app','cbd')
G.edge['s_system_app']['cbd']['write-read'] = '[open open]'
G.add_edge('s_system_app','charon')
G.edge['s_system_app']['charon']['write-read'] = '[open open]'
G.add_edge('s_system_app','debuggerd')
G.edge['s_system_app']['debuggerd']['write-read'] = '[open open]'
G.add_edge('s_system_app','diag_uart_log')
G.edge['s_system_app']['diag_uart_log']['write-read'] = '[open open]'
G.add_edge('s_system_app','dumpstate')
G.edge['s_system_app']['dumpstate']['write-read'] = '[open open]'
G.add_edge('s_system_app','hostapd')
G.edge['s_system_app']['hostapd']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('s_system_app','ime_app')
G.edge['s_system_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open]'
G.add_edge('s_system_app','init_shell')
G.edge['s_system_app']['init_shell']['write-read'] = '[open open]'
G.add_edge('s_system_app','installd')
G.edge['s_system_app']['installd']['write-read'] = '[open open]'
G.add_edge('s_system_app','itsonbs')
G.edge['s_system_app']['itsonbs']['write-read'] = '[open open]'
G.add_edge('s_system_app','logwrapper')
G.edge['s_system_app']['logwrapper']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('s_system_app','netd')
G.edge['s_system_app']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('s_system_app','qmuxd')
G.edge['s_system_app']['qmuxd']['write-read'] = '[open open]'
G.add_edge('s_system_app','rild')
G.edge['s_system_app']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open]'
G.add_edge('s_system_app','rmt_storage')
G.edge['s_system_app']['rmt_storage']['write-read'] = '[open open]'
G.add_edge('s_system_app','sdcardd')
G.edge['s_system_app']['sdcardd']['write-read'] = '[open open]'
G.add_edge('s_system_app','shell')
G.edge['s_system_app']['shell']['write-read'] = '[open open]'
G.add_edge('s_system_app','s_system_app')
G.edge['s_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('s_system_app','system_app')
G.edge['s_system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open]'
G.add_edge('s_system_app','system_server')
G.edge['s_system_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('s_system_app','vmwared')
G.edge['s_system_app']['vmwared']['write-read'] = '[open open]'
G.add_edge('s_system_app','wpa')
G.edge['s_system_app']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('s_system_app','zygote')
G.edge['s_system_app']['zygote']['write-read'] = '[open open]'
G.add_edge('s_system_app','at_distributor')
G.edge['s_system_app']['at_distributor']['write-read'] = '[open open][setattr getattr]'
G.add_edge('s_system_app','cbd')
G.edge['s_system_app']['cbd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('s_system_app','charon')
G.edge['s_system_app']['charon']['write-read'] = '[open open][setattr getattr]'
G.add_edge('s_system_app','debuggerd')
G.edge['s_system_app']['debuggerd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('s_system_app','diag_uart_log')
G.edge['s_system_app']['diag_uart_log']['write-read'] = '[open open][setattr getattr]'
G.add_edge('s_system_app','dumpstate')
G.edge['s_system_app']['dumpstate']['write-read'] = '[open open][setattr getattr]'
G.add_edge('s_system_app','hostapd')
G.edge['s_system_app']['hostapd']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr]'
G.add_edge('s_system_app','ime_app')
G.edge['s_system_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr]'
G.add_edge('s_system_app','init_shell')
G.edge['s_system_app']['init_shell']['write-read'] = '[open open][setattr getattr]'
G.add_edge('s_system_app','installd')
G.edge['s_system_app']['installd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('s_system_app','itsonbs')
G.edge['s_system_app']['itsonbs']['write-read'] = '[open open][setattr getattr]'
G.add_edge('s_system_app','logwrapper')
G.edge['s_system_app']['logwrapper']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr]'
G.add_edge('s_system_app','netd')
G.edge['s_system_app']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('s_system_app','qmuxd')
G.edge['s_system_app']['qmuxd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('s_system_app','rild')
G.edge['s_system_app']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr]'
G.add_edge('s_system_app','rmt_storage')
G.edge['s_system_app']['rmt_storage']['write-read'] = '[open open][setattr getattr]'
G.add_edge('s_system_app','sdcardd')
G.edge['s_system_app']['sdcardd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('s_system_app','shell')
G.edge['s_system_app']['shell']['write-read'] = '[open open][setattr getattr]'
G.add_edge('s_system_app','s_system_app')
G.edge['s_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('s_system_app','system_app')
G.edge['s_system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr]'
G.add_edge('s_system_app','system_server')
G.edge['s_system_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('s_system_app','vmwared')
G.edge['s_system_app']['vmwared']['write-read'] = '[open open][setattr getattr]'
G.add_edge('s_system_app','wpa')
G.edge['s_system_app']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('s_system_app','zygote')
G.edge['s_system_app']['zygote']['write-read'] = '[open open][setattr getattr]'
G.add_edge('s_system_app','adbd')
G.edge['s_system_app']['adbd']['write-read'] = '[write read]'
G.edge['s_system_app']['adbd']['fill'] = 'red'
G.add_edge('s_system_app','at_distributor')
G.edge['s_system_app']['at_distributor']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['s_system_app']['at_distributor']['fill'] = 'red'
G.add_edge('s_system_app','cbd')
G.edge['s_system_app']['cbd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['s_system_app']['cbd']['fill'] = 'red'
G.add_edge('s_system_app','charon')
G.edge['s_system_app']['charon']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['s_system_app']['charon']['fill'] = 'red'
G.add_edge('s_system_app','debuggerd')
G.edge['s_system_app']['debuggerd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['s_system_app']['debuggerd']['fill'] = 'red'
G.add_edge('s_system_app','dhcp')
G.edge['s_system_app']['dhcp']['write-read'] = '[write read]'
G.edge['s_system_app']['dhcp']['fill'] = 'red'
G.add_edge('s_system_app','diag_uart_log')
G.edge['s_system_app']['diag_uart_log']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['s_system_app']['diag_uart_log']['fill'] = 'red'
G.add_edge('s_system_app','domain')
G.edge['s_system_app']['domain']['write-read'] = '[write read]'
G.edge['s_system_app']['domain']['fill'] = 'red'
G.add_edge('s_system_app','dumpstate')
G.edge['s_system_app']['dumpstate']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['s_system_app']['dumpstate']['fill'] = 'red'
G.add_edge('s_system_app','hostapd')
G.edge['s_system_app']['hostapd']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['s_system_app']['hostapd']['fill'] = 'red'
G.add_edge('s_system_app','ime_app')
G.edge['s_system_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read]'
G.edge['s_system_app']['ime_app']['fill'] = 'red'
G.add_edge('s_system_app','init_shell')
G.edge['s_system_app']['init_shell']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['s_system_app']['init_shell']['fill'] = 'red'
G.add_edge('s_system_app','installd')
G.edge['s_system_app']['installd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['s_system_app']['installd']['fill'] = 'red'
G.add_edge('s_system_app','itsonbs')
G.edge['s_system_app']['itsonbs']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['s_system_app']['itsonbs']['fill'] = 'red'
G.add_edge('s_system_app','logwrapper')
G.edge['s_system_app']['logwrapper']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['s_system_app']['logwrapper']['fill'] = 'red'
G.add_edge('s_system_app','netd')
G.edge['s_system_app']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['s_system_app']['netd']['fill'] = 'red'
G.add_edge('s_system_app','qmuxd')
G.edge['s_system_app']['qmuxd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['s_system_app']['qmuxd']['fill'] = 'red'
G.add_edge('s_system_app','rild')
G.edge['s_system_app']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read]'
G.edge['s_system_app']['rild']['fill'] = 'red'
G.add_edge('s_system_app','rmt_storage')
G.edge['s_system_app']['rmt_storage']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['s_system_app']['rmt_storage']['fill'] = 'red'
G.add_edge('s_system_app','sdcardd')
G.edge['s_system_app']['sdcardd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['s_system_app']['sdcardd']['fill'] = 'red'
G.add_edge('s_system_app','shell')
G.edge['s_system_app']['shell']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['s_system_app']['shell']['fill'] = 'red'
G.add_edge('s_system_app','s_system_app')
G.edge['s_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['s_system_app']['s_system_app']['fill'] = 'red'
G.add_edge('s_system_app','system_app')
G.edge['s_system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read]'
G.edge['s_system_app']['system_app']['fill'] = 'red'
G.add_edge('s_system_app','system_server')
G.edge['s_system_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['s_system_app']['system_server']['fill'] = 'red'
G.add_edge('s_system_app','vmwared')
G.edge['s_system_app']['vmwared']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['s_system_app']['vmwared']['fill'] = 'red'
G.add_edge('s_system_app','wpa')
G.edge['s_system_app']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['s_system_app']['wpa']['fill'] = 'red'
G.add_edge('s_system_app','zygote')
G.edge['s_system_app']['zygote']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['s_system_app']['zygote']['fill'] = 'red'
G.add_edge('s_system_app','adbd')
G.edge['s_system_app']['adbd']['write-read'] = '[write read][add_name search]'
G.add_edge('s_system_app','at_distributor')
G.edge['s_system_app']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('s_system_app','at_distributor')
G.edge['s_system_app']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('s_system_app','auditd')
G.edge['s_system_app']['auditd']['write-read'] = '[add_name search]'
G.add_edge('s_system_app','cbd')
G.edge['s_system_app']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('s_system_app','cbd')
G.edge['s_system_app']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('s_system_app','charon')
G.edge['s_system_app']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('s_system_app','charon')
G.edge['s_system_app']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('s_system_app','clatd')
G.edge['s_system_app']['clatd']['write-read'] = '[add_name search]'
G.add_edge('s_system_app','debuggerd')
G.edge['s_system_app']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('s_system_app','debuggerd')
G.edge['s_system_app']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('s_system_app','dhcp')
G.edge['s_system_app']['dhcp']['write-read'] = '[write read][add_name search]'
G.add_edge('s_system_app','diag_uart_log')
G.edge['s_system_app']['diag_uart_log']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('s_system_app','diag_uart_log')
G.edge['s_system_app']['diag_uart_log']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('s_system_app','dumpstate')
G.edge['s_system_app']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('s_system_app','dumpstate')
G.edge['s_system_app']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('s_system_app','hostapd')
G.edge['s_system_app']['hostapd']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('s_system_app','hostapd')
G.edge['s_system_app']['hostapd']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('s_system_app','hvdcp')
G.edge['s_system_app']['hvdcp']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][add_name search]'
G.add_edge('s_system_app','ime_app')
G.edge['s_system_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search]'
G.add_edge('s_system_app','ime_app')
G.edge['s_system_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('s_system_app','init_shell')
G.edge['s_system_app']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('s_system_app','init_shell')
G.edge['s_system_app']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('s_system_app','installd')
G.edge['s_system_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('s_system_app','installd')
G.edge['s_system_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('s_system_app','itsonbs')
G.edge['s_system_app']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('s_system_app','itsonbs')
G.edge['s_system_app']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('s_system_app','jackservice')
G.edge['s_system_app']['jackservice']['write-read'] = '[add_name search]'
G.add_edge('s_system_app','lmkd')
G.edge['s_system_app']['lmkd']['write-read'] = '[remove_name search]'
G.add_edge('s_system_app','logwrapper')
G.edge['s_system_app']['logwrapper']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('s_system_app','logwrapper')
G.edge['s_system_app']['logwrapper']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('s_system_app','msm_irqbalanced')
G.edge['s_system_app']['msm_irqbalanced']['write-read'] = '[add_name search]'
G.add_edge('s_system_app','netd')
G.edge['s_system_app']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('s_system_app','netd')
G.edge['s_system_app']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('s_system_app','qmuxd')
G.edge['s_system_app']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('s_system_app','qmuxd')
G.edge['s_system_app']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('s_system_app','racoon')
G.edge['s_system_app']['racoon']['write-read'] = '[add_name search]'
G.add_edge('s_system_app','rild')
G.edge['s_system_app']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search]'
G.add_edge('s_system_app','rild')
G.edge['s_system_app']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('s_system_app','rmt_storage')
G.edge['s_system_app']['rmt_storage']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('s_system_app','rmt_storage')
G.edge['s_system_app']['rmt_storage']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('s_system_app','sdcardd')
G.edge['s_system_app']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('s_system_app','sdcardd')
G.edge['s_system_app']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('s_system_app','sensors')
G.edge['s_system_app']['sensors']['write-read'] = '[add_name search]'
G.add_edge('s_system_app','shell')
G.edge['s_system_app']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('s_system_app','shell')
G.edge['s_system_app']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('s_system_app','s_system_app')
G.edge['s_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('s_system_app','s_system_app')
G.edge['s_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('s_system_app','system_app')
G.edge['s_system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search]'
G.add_edge('s_system_app','system_app')
G.edge['s_system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('s_system_app','system_server')
G.edge['s_system_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('s_system_app','system_server')
G.edge['s_system_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('s_system_app','system_server')
G.edge['s_system_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search]'
G.add_edge('s_system_app','vmwared')
G.edge['s_system_app']['vmwared']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('s_system_app','vmwared')
G.edge['s_system_app']['vmwared']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('s_system_app','wpa')
G.edge['s_system_app']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('s_system_app','wpa')
G.edge['s_system_app']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('s_system_app','zygote')
G.edge['s_system_app']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('s_system_app','zygote')
G.edge['s_system_app']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('system_app','at_distributor')
G.edge['system_app']['at_distributor']['write-read'] = '[open open]'
G.add_edge('system_app','cbd')
G.edge['system_app']['cbd']['write-read'] = '[open open]'
G.add_edge('system_app','charon')
G.edge['system_app']['charon']['write-read'] = '[open open]'
G.add_edge('system_app','debuggerd')
G.edge['system_app']['debuggerd']['write-read'] = '[open open]'
G.add_edge('system_app','diag_uart_log')
G.edge['system_app']['diag_uart_log']['write-read'] = '[open open]'
G.add_edge('system_app','dumpstate')
G.edge['system_app']['dumpstate']['write-read'] = '[open open]'
G.add_edge('system_app','hostapd')
G.edge['system_app']['hostapd']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('system_app','ime_app')
G.edge['system_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open]'
G.add_edge('system_app','init_shell')
G.edge['system_app']['init_shell']['write-read'] = '[open open]'
G.add_edge('system_app','installd')
G.edge['system_app']['installd']['write-read'] = '[open open]'
G.add_edge('system_app','itsonbs')
G.edge['system_app']['itsonbs']['write-read'] = '[open open]'
G.add_edge('system_app','logwrapper')
G.edge['system_app']['logwrapper']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('system_app','netd')
G.edge['system_app']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open]'
G.add_edge('system_app','qmuxd')
G.edge['system_app']['qmuxd']['write-read'] = '[open open]'
G.add_edge('system_app','rild')
G.edge['system_app']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open]'
G.add_edge('system_app','rmt_storage')
G.edge['system_app']['rmt_storage']['write-read'] = '[open open]'
G.add_edge('system_app','sdcardd')
G.edge['system_app']['sdcardd']['write-read'] = '[open open]'
G.add_edge('system_app','shell')
G.edge['system_app']['shell']['write-read'] = '[open open]'
G.add_edge('system_app','s_system_app')
G.edge['system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open]'
G.add_edge('system_app','system_app')
G.edge['system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open]'
G.add_edge('system_app','system_server')
G.edge['system_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open]'
G.add_edge('system_app','vmwared')
G.edge['system_app']['vmwared']['write-read'] = '[open open]'
G.add_edge('system_app','wpa')
G.edge['system_app']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('system_app','zygote')
G.edge['system_app']['zygote']['write-read'] = '[open open]'
G.add_edge('system_app','at_distributor')
G.edge['system_app']['at_distributor']['write-read'] = '[open open][setattr getattr]'
G.add_edge('system_app','cbd')
G.edge['system_app']['cbd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('system_app','charon')
G.edge['system_app']['charon']['write-read'] = '[open open][setattr getattr]'
G.add_edge('system_app','debuggerd')
G.edge['system_app']['debuggerd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('system_app','diag_uart_log')
G.edge['system_app']['diag_uart_log']['write-read'] = '[open open][setattr getattr]'
G.add_edge('system_app','dumpstate')
G.edge['system_app']['dumpstate']['write-read'] = '[open open][setattr getattr]'
G.add_edge('system_app','hostapd')
G.edge['system_app']['hostapd']['write-read'] = '[open open][write read][append read][open open][setattr getattr]'
G.add_edge('system_app','ime_app')
G.edge['system_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr]'
G.add_edge('system_app','init_shell')
G.edge['system_app']['init_shell']['write-read'] = '[open open][setattr getattr]'
G.add_edge('system_app','installd')
G.edge['system_app']['installd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('system_app','itsonbs')
G.edge['system_app']['itsonbs']['write-read'] = '[open open][setattr getattr]'
G.add_edge('system_app','logwrapper')
G.edge['system_app']['logwrapper']['write-read'] = '[open open][write read][append read][open open][setattr getattr]'
G.add_edge('system_app','netd')
G.edge['system_app']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('system_app','qmuxd')
G.edge['system_app']['qmuxd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('system_app','rild')
G.edge['system_app']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr]'
G.add_edge('system_app','rmt_storage')
G.edge['system_app']['rmt_storage']['write-read'] = '[open open][setattr getattr]'
G.add_edge('system_app','sdcardd')
G.edge['system_app']['sdcardd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('system_app','shell')
G.edge['system_app']['shell']['write-read'] = '[open open][setattr getattr]'
G.add_edge('system_app','s_system_app')
G.edge['system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('system_app','system_app')
G.edge['system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr]'
G.add_edge('system_app','system_server')
G.edge['system_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('system_app','vmwared')
G.edge['system_app']['vmwared']['write-read'] = '[open open][setattr getattr]'
G.add_edge('system_app','wpa')
G.edge['system_app']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('system_app','zygote')
G.edge['system_app']['zygote']['write-read'] = '[open open][setattr getattr]'
G.add_edge('system_app','adbd')
G.edge['system_app']['adbd']['write-read'] = '[write read]'
G.edge['system_app']['adbd']['fill'] = 'red'
G.add_edge('system_app','at_distributor')
G.edge['system_app']['at_distributor']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['system_app']['at_distributor']['fill'] = 'red'
G.add_edge('system_app','cbd')
G.edge['system_app']['cbd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['system_app']['cbd']['fill'] = 'red'
G.add_edge('system_app','charon')
G.edge['system_app']['charon']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['system_app']['charon']['fill'] = 'red'
G.add_edge('system_app','debuggerd')
G.edge['system_app']['debuggerd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['system_app']['debuggerd']['fill'] = 'red'
G.add_edge('system_app','dhcp')
G.edge['system_app']['dhcp']['write-read'] = '[write read]'
G.edge['system_app']['dhcp']['fill'] = 'red'
G.add_edge('system_app','diag_uart_log')
G.edge['system_app']['diag_uart_log']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['system_app']['diag_uart_log']['fill'] = 'red'
G.add_edge('system_app','domain')
G.edge['system_app']['domain']['write-read'] = '[write read]'
G.edge['system_app']['domain']['fill'] = 'red'
G.add_edge('system_app','dumpstate')
G.edge['system_app']['dumpstate']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['system_app']['dumpstate']['fill'] = 'red'
G.add_edge('system_app','hostapd')
G.edge['system_app']['hostapd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read]'
G.edge['system_app']['hostapd']['fill'] = 'red'
G.add_edge('system_app','ime_app')
G.edge['system_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read]'
G.edge['system_app']['ime_app']['fill'] = 'red'
G.add_edge('system_app','init_shell')
G.edge['system_app']['init_shell']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['system_app']['init_shell']['fill'] = 'red'
G.add_edge('system_app','installd')
G.edge['system_app']['installd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['system_app']['installd']['fill'] = 'red'
G.add_edge('system_app','itsonbs')
G.edge['system_app']['itsonbs']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['system_app']['itsonbs']['fill'] = 'red'
G.add_edge('system_app','logwrapper')
G.edge['system_app']['logwrapper']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read]'
G.edge['system_app']['logwrapper']['fill'] = 'red'
G.add_edge('system_app','netd')
G.edge['system_app']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['system_app']['netd']['fill'] = 'red'
G.add_edge('system_app','qmuxd')
G.edge['system_app']['qmuxd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['system_app']['qmuxd']['fill'] = 'red'
G.add_edge('system_app','rild')
G.edge['system_app']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read]'
G.edge['system_app']['rild']['fill'] = 'red'
G.add_edge('system_app','rmt_storage')
G.edge['system_app']['rmt_storage']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['system_app']['rmt_storage']['fill'] = 'red'
G.add_edge('system_app','sdcardd')
G.edge['system_app']['sdcardd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['system_app']['sdcardd']['fill'] = 'red'
G.add_edge('system_app','shell')
G.edge['system_app']['shell']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['system_app']['shell']['fill'] = 'red'
G.add_edge('system_app','s_system_app')
G.edge['system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['system_app']['s_system_app']['fill'] = 'red'
G.add_edge('system_app','system_app')
G.edge['system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read]'
G.edge['system_app']['system_app']['fill'] = 'red'
G.add_edge('system_app','system_server')
G.edge['system_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['system_app']['system_server']['fill'] = 'red'
G.add_edge('system_app','vmwared')
G.edge['system_app']['vmwared']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['system_app']['vmwared']['fill'] = 'red'
G.add_edge('system_app','wpa')
G.edge['system_app']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['system_app']['wpa']['fill'] = 'red'
G.add_edge('system_app','zygote')
G.edge['system_app']['zygote']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['system_app']['zygote']['fill'] = 'red'
G.add_edge('system_app','adbd')
G.edge['system_app']['adbd']['write-read'] = '[write read][add_name search]'
G.add_edge('system_app','at_distributor')
G.edge['system_app']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('system_app','at_distributor')
G.edge['system_app']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('system_app','auditd')
G.edge['system_app']['auditd']['write-read'] = '[add_name search]'
G.add_edge('system_app','cbd')
G.edge['system_app']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('system_app','cbd')
G.edge['system_app']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('system_app','charon')
G.edge['system_app']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('system_app','charon')
G.edge['system_app']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('system_app','clatd')
G.edge['system_app']['clatd']['write-read'] = '[add_name search]'
G.add_edge('system_app','debuggerd')
G.edge['system_app']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('system_app','debuggerd')
G.edge['system_app']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('system_app','dhcp')
G.edge['system_app']['dhcp']['write-read'] = '[write read][add_name search]'
G.add_edge('system_app','diag_uart_log')
G.edge['system_app']['diag_uart_log']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('system_app','diag_uart_log')
G.edge['system_app']['diag_uart_log']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('system_app','dumpstate')
G.edge['system_app']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('system_app','dumpstate')
G.edge['system_app']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('system_app','hostapd')
G.edge['system_app']['hostapd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('system_app','hostapd')
G.edge['system_app']['hostapd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('system_app','hvdcp')
G.edge['system_app']['hvdcp']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][add_name search]'
G.add_edge('system_app','ime_app')
G.edge['system_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search]'
G.add_edge('system_app','ime_app')
G.edge['system_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('system_app','init_shell')
G.edge['system_app']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('system_app','init_shell')
G.edge['system_app']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('system_app','installd')
G.edge['system_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('system_app','installd')
G.edge['system_app']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('system_app','itsonbs')
G.edge['system_app']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('system_app','itsonbs')
G.edge['system_app']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('system_app','jackservice')
G.edge['system_app']['jackservice']['write-read'] = '[add_name search]'
G.add_edge('system_app','lmkd')
G.edge['system_app']['lmkd']['write-read'] = '[remove_name search]'
G.add_edge('system_app','logwrapper')
G.edge['system_app']['logwrapper']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('system_app','logwrapper')
G.edge['system_app']['logwrapper']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('system_app','msm_irqbalanced')
G.edge['system_app']['msm_irqbalanced']['write-read'] = '[add_name search]'
G.add_edge('system_app','netd')
G.edge['system_app']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('system_app','netd')
G.edge['system_app']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('system_app','qmuxd')
G.edge['system_app']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('system_app','qmuxd')
G.edge['system_app']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('system_app','racoon')
G.edge['system_app']['racoon']['write-read'] = '[add_name search]'
G.add_edge('system_app','rild')
G.edge['system_app']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search]'
G.add_edge('system_app','rild')
G.edge['system_app']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('system_app','rmt_storage')
G.edge['system_app']['rmt_storage']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('system_app','rmt_storage')
G.edge['system_app']['rmt_storage']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('system_app','sdcardd')
G.edge['system_app']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('system_app','sdcardd')
G.edge['system_app']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('system_app','sensors')
G.edge['system_app']['sensors']['write-read'] = '[add_name search]'
G.add_edge('system_app','shell')
G.edge['system_app']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('system_app','shell')
G.edge['system_app']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('system_app','s_system_app')
G.edge['system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('system_app','s_system_app')
G.edge['system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('system_app','system_app')
G.edge['system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search]'
G.add_edge('system_app','system_app')
G.edge['system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('system_app','system_server')
G.edge['system_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('system_app','system_server')
G.edge['system_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('system_app','system_server')
G.edge['system_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search]'
G.add_edge('system_app','vmwared')
G.edge['system_app']['vmwared']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('system_app','vmwared')
G.edge['system_app']['vmwared']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('system_app','wpa')
G.edge['system_app']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('system_app','wpa')
G.edge['system_app']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('system_app','zygote')
G.edge['system_app']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('system_app','zygote')
G.edge['system_app']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('system_server','at_distributor')
G.edge['system_server']['at_distributor']['write-read'] = '[open open]'
G.add_edge('system_server','cbd')
G.edge['system_server']['cbd']['write-read'] = '[open open]'
G.add_edge('system_server','charon')
G.edge['system_server']['charon']['write-read'] = '[open open]'
G.add_edge('system_server','debuggerd')
G.edge['system_server']['debuggerd']['write-read'] = '[open open]'
G.add_edge('system_server','diag_uart_log')
G.edge['system_server']['diag_uart_log']['write-read'] = '[open open]'
G.add_edge('system_server','dumpstate')
G.edge['system_server']['dumpstate']['write-read'] = '[open open]'
G.add_edge('system_server','hostapd')
G.edge['system_server']['hostapd']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('system_server','ime_app')
G.edge['system_server']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt][open open]'
G.add_edge('system_server','init_shell')
G.edge['system_server']['init_shell']['write-read'] = '[open open][open open]'
G.add_edge('system_server','installd')
G.edge['system_server']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('system_server','itsonbs')
G.edge['system_server']['itsonbs']['write-read'] = '[open open]'
G.add_edge('system_server','logwrapper')
G.edge['system_server']['logwrapper']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('system_server','netd')
G.edge['system_server']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open]'
G.add_edge('system_server','qmuxd')
G.edge['system_server']['qmuxd']['write-read'] = '[open open]'
G.add_edge('system_server','rild')
G.edge['system_server']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open]'
G.add_edge('system_server','rmt_storage')
G.edge['system_server']['rmt_storage']['write-read'] = '[open open]'
G.add_edge('system_server','sdcardd')
G.edge['system_server']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('system_server','shell')
G.edge['system_server']['shell']['write-read'] = '[open open]'
G.add_edge('system_server','s_system_app')
G.edge['system_server']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt][open open][setattr getattr][write read][append read][open open]'
G.add_edge('system_server','system_app')
G.edge['system_server']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt][open open]'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open]'
G.add_edge('system_server','vmwared')
G.edge['system_server']['vmwared']['write-read'] = '[open open]'
G.add_edge('system_server','wpa')
G.edge['system_server']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('system_server','zygote')
G.edge['system_server']['zygote']['write-read'] = '[open open]'
G.add_edge('system_server','at_distributor')
G.edge['system_server']['at_distributor']['write-read'] = '[open open][setattr getattr]'
G.add_edge('system_server','cbd')
G.edge['system_server']['cbd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('system_server','charon')
G.edge['system_server']['charon']['write-read'] = '[open open][setattr getattr]'
G.add_edge('system_server','debuggerd')
G.edge['system_server']['debuggerd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('system_server','diag_uart_log')
G.edge['system_server']['diag_uart_log']['write-read'] = '[open open][setattr getattr]'
G.add_edge('system_server','dumpstate')
G.edge['system_server']['dumpstate']['write-read'] = '[open open][setattr getattr]'
G.add_edge('system_server','hostapd')
G.edge['system_server']['hostapd']['write-read'] = '[open open][write read][append read][open open][setattr getattr]'
G.add_edge('system_server','ime_app')
G.edge['system_server']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt][open open][setattr getattr]'
G.add_edge('system_server','init_shell')
G.edge['system_server']['init_shell']['write-read'] = '[open open][open open][setattr getattr]'
G.add_edge('system_server','installd')
G.edge['system_server']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('system_server','itsonbs')
G.edge['system_server']['itsonbs']['write-read'] = '[open open][setattr getattr]'
G.add_edge('system_server','logwrapper')
G.edge['system_server']['logwrapper']['write-read'] = '[open open][write read][append read][open open][setattr getattr]'
G.add_edge('system_server','netd')
G.edge['system_server']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('system_server','qmuxd')
G.edge['system_server']['qmuxd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('system_server','rild')
G.edge['system_server']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr]'
G.add_edge('system_server','rmt_storage')
G.edge['system_server']['rmt_storage']['write-read'] = '[open open][setattr getattr]'
G.add_edge('system_server','sdcardd')
G.edge['system_server']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('system_server','shell')
G.edge['system_server']['shell']['write-read'] = '[open open][setattr getattr]'
G.add_edge('system_server','s_system_app')
G.edge['system_server']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('system_server','system_app')
G.edge['system_server']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt][open open][setattr getattr]'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr]'
G.add_edge('system_server','vmwared')
G.edge['system_server']['vmwared']['write-read'] = '[open open][setattr getattr]'
G.add_edge('system_server','wpa')
G.edge['system_server']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('system_server','zygote')
G.edge['system_server']['zygote']['write-read'] = '[open open][setattr getattr]'
G.add_edge('system_server','adbd')
G.edge['system_server']['adbd']['write-read'] = '[write read]'
G.edge['system_server']['adbd']['fill'] = 'red'
G.add_edge('system_server','at_distributor')
G.edge['system_server']['at_distributor']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['system_server']['at_distributor']['fill'] = 'red'
G.add_edge('system_server','cbd')
G.edge['system_server']['cbd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['system_server']['cbd']['fill'] = 'red'
G.add_edge('system_server','charon')
G.edge['system_server']['charon']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['system_server']['charon']['fill'] = 'red'
G.add_edge('system_server','debuggerd')
G.edge['system_server']['debuggerd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['system_server']['debuggerd']['fill'] = 'red'
G.add_edge('system_server','dhcp')
G.edge['system_server']['dhcp']['write-read'] = '[write read]'
G.edge['system_server']['dhcp']['fill'] = 'red'
G.add_edge('system_server','diag_uart_log')
G.edge['system_server']['diag_uart_log']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['system_server']['diag_uart_log']['fill'] = 'red'
G.add_edge('system_server','domain')
G.edge['system_server']['domain']['write-read'] = '[write read]'
G.edge['system_server']['domain']['fill'] = 'red'
G.add_edge('system_server','dumpstate')
G.edge['system_server']['dumpstate']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['system_server']['dumpstate']['fill'] = 'red'
G.add_edge('system_server','hostapd')
G.edge['system_server']['hostapd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read]'
G.edge['system_server']['hostapd']['fill'] = 'red'
G.add_edge('system_server','ime_app')
G.edge['system_server']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt][open open][setattr getattr][write read]'
G.edge['system_server']['ime_app']['fill'] = 'red'
G.add_edge('system_server','init_shell')
G.edge['system_server']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read]'
G.edge['system_server']['init_shell']['fill'] = 'red'
G.add_edge('system_server','installd')
G.edge['system_server']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['system_server']['installd']['fill'] = 'red'
G.add_edge('system_server','itsonbs')
G.edge['system_server']['itsonbs']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['system_server']['itsonbs']['fill'] = 'red'
G.add_edge('system_server','logwrapper')
G.edge['system_server']['logwrapper']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read]'
G.edge['system_server']['logwrapper']['fill'] = 'red'
G.add_edge('system_server','netd')
G.edge['system_server']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['system_server']['netd']['fill'] = 'red'
G.add_edge('system_server','qmuxd')
G.edge['system_server']['qmuxd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['system_server']['qmuxd']['fill'] = 'red'
G.add_edge('system_server','rild')
G.edge['system_server']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read]'
G.edge['system_server']['rild']['fill'] = 'red'
G.add_edge('system_server','rmt_storage')
G.edge['system_server']['rmt_storage']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['system_server']['rmt_storage']['fill'] = 'red'
G.add_edge('system_server','sdcardd')
G.edge['system_server']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['system_server']['sdcardd']['fill'] = 'red'
G.add_edge('system_server','shell')
G.edge['system_server']['shell']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['system_server']['shell']['fill'] = 'red'
G.add_edge('system_server','s_system_app')
G.edge['system_server']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['system_server']['s_system_app']['fill'] = 'red'
G.add_edge('system_server','system_app')
G.edge['system_server']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt][open open][setattr getattr][write read]'
G.edge['system_server']['system_app']['fill'] = 'red'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read]'
G.edge['system_server']['system_server']['fill'] = 'red'
G.add_edge('system_server','vmwared')
G.edge['system_server']['vmwared']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['system_server']['vmwared']['fill'] = 'red'
G.add_edge('system_server','wpa')
G.edge['system_server']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['system_server']['wpa']['fill'] = 'red'
G.add_edge('system_server','zygote')
G.edge['system_server']['zygote']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['system_server']['zygote']['fill'] = 'red'
G.add_edge('system_server','adbd')
G.edge['system_server']['adbd']['write-read'] = '[write read][add_name search]'
G.add_edge('system_server','at_distributor')
G.edge['system_server']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('system_server','at_distributor')
G.edge['system_server']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('system_server','auditd')
G.edge['system_server']['auditd']['write-read'] = '[add_name search]'
G.add_edge('system_server','cbd')
G.edge['system_server']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('system_server','cbd')
G.edge['system_server']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('system_server','charon')
G.edge['system_server']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('system_server','charon')
G.edge['system_server']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('system_server','clatd')
G.edge['system_server']['clatd']['write-read'] = '[add_name search]'
G.add_edge('system_server','debuggerd')
G.edge['system_server']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('system_server','debuggerd')
G.edge['system_server']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('system_server','dhcp')
G.edge['system_server']['dhcp']['write-read'] = '[write read][add_name search]'
G.add_edge('system_server','diag_uart_log')
G.edge['system_server']['diag_uart_log']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('system_server','diag_uart_log')
G.edge['system_server']['diag_uart_log']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('system_server','dumpstate')
G.edge['system_server']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('system_server','dumpstate')
G.edge['system_server']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('system_server','hostapd')
G.edge['system_server']['hostapd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('system_server','hostapd')
G.edge['system_server']['hostapd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('system_server','hvdcp')
G.edge['system_server']['hvdcp']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][add_name search]'
G.add_edge('system_server','ime_app')
G.edge['system_server']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt][open open][setattr getattr][write read][add_name search]'
G.add_edge('system_server','ime_app')
G.edge['system_server']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('system_server','init_shell')
G.edge['system_server']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search]'
G.add_edge('system_server','init_shell')
G.edge['system_server']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('system_server','installd')
G.edge['system_server']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('system_server','installd')
G.edge['system_server']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('system_server','itsonbs')
G.edge['system_server']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('system_server','itsonbs')
G.edge['system_server']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('system_server','jackservice')
G.edge['system_server']['jackservice']['write-read'] = '[add_name search]'
G.add_edge('system_server','lmkd')
G.edge['system_server']['lmkd']['write-read'] = '[remove_name search]'
G.add_edge('system_server','logwrapper')
G.edge['system_server']['logwrapper']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('system_server','logwrapper')
G.edge['system_server']['logwrapper']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('system_server','msm_irqbalanced')
G.edge['system_server']['msm_irqbalanced']['write-read'] = '[add_name search]'
G.add_edge('system_server','netd')
G.edge['system_server']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('system_server','netd')
G.edge['system_server']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('system_server','qmuxd')
G.edge['system_server']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('system_server','qmuxd')
G.edge['system_server']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('system_server','racoon')
G.edge['system_server']['racoon']['write-read'] = '[add_name search]'
G.add_edge('system_server','rild')
G.edge['system_server']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search]'
G.add_edge('system_server','rild')
G.edge['system_server']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('system_server','rmt_storage')
G.edge['system_server']['rmt_storage']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('system_server','rmt_storage')
G.edge['system_server']['rmt_storage']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('system_server','sdcardd')
G.edge['system_server']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('system_server','sdcardd')
G.edge['system_server']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('system_server','sensors')
G.edge['system_server']['sensors']['write-read'] = '[add_name search]'
G.add_edge('system_server','shell')
G.edge['system_server']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('system_server','shell')
G.edge['system_server']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('system_server','s_system_app')
G.edge['system_server']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('system_server','s_system_app')
G.edge['system_server']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('system_server','system_app')
G.edge['system_server']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt][open open][setattr getattr][write read][add_name search]'
G.add_edge('system_server','system_app')
G.edge['system_server']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search]'
G.add_edge('system_server','vmwared')
G.edge['system_server']['vmwared']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('system_server','vmwared')
G.edge['system_server']['vmwared']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('system_server','wpa')
G.edge['system_server']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('system_server','wpa')
G.edge['system_server']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('system_server','zygote')
G.edge['system_server']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('system_server','zygote')
G.edge['system_server']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('vmwared','at_distributor')
G.edge['vmwared']['at_distributor']['write-read'] = '[open open]'
G.add_edge('vmwared','cbd')
G.edge['vmwared']['cbd']['write-read'] = '[open open]'
G.add_edge('vmwared','charon')
G.edge['vmwared']['charon']['write-read'] = '[open open]'
G.add_edge('vmwared','debuggerd')
G.edge['vmwared']['debuggerd']['write-read'] = '[open open]'
G.add_edge('vmwared','diag_uart_log')
G.edge['vmwared']['diag_uart_log']['write-read'] = '[open open]'
G.add_edge('vmwared','dumpstate')
G.edge['vmwared']['dumpstate']['write-read'] = '[open open]'
G.add_edge('vmwared','hostapd')
G.edge['vmwared']['hostapd']['write-read'] = '[open open]'
G.add_edge('vmwared','ime_app')
G.edge['vmwared']['ime_app']['write-read'] = '[open open]'
G.add_edge('vmwared','init_shell')
G.edge['vmwared']['init_shell']['write-read'] = '[open open]'
G.add_edge('vmwared','installd')
G.edge['vmwared']['installd']['write-read'] = '[open open]'
G.add_edge('vmwared','itsonbs')
G.edge['vmwared']['itsonbs']['write-read'] = '[open open]'
G.add_edge('vmwared','logwrapper')
G.edge['vmwared']['logwrapper']['write-read'] = '[open open]'
G.add_edge('vmwared','netd')
G.edge['vmwared']['netd']['write-read'] = '[open open]'
G.add_edge('vmwared','qmuxd')
G.edge['vmwared']['qmuxd']['write-read'] = '[open open]'
G.add_edge('vmwared','rild')
G.edge['vmwared']['rild']['write-read'] = '[open open]'
G.add_edge('vmwared','rmt_storage')
G.edge['vmwared']['rmt_storage']['write-read'] = '[open open]'
G.add_edge('vmwared','sdcardd')
G.edge['vmwared']['sdcardd']['write-read'] = '[open open]'
G.add_edge('vmwared','shell')
G.edge['vmwared']['shell']['write-read'] = '[open open]'
G.add_edge('vmwared','s_system_app')
G.edge['vmwared']['s_system_app']['write-read'] = '[open open]'
G.add_edge('vmwared','system_app')
G.edge['vmwared']['system_app']['write-read'] = '[open open]'
G.add_edge('vmwared','system_server')
G.edge['vmwared']['system_server']['write-read'] = '[open open]'
G.add_edge('vmwared','vmwared')
G.edge['vmwared']['vmwared']['write-read'] = '[open open]'
G.add_edge('vmwared','wpa')
G.edge['vmwared']['wpa']['write-read'] = '[open open]'
G.add_edge('vmwared','zygote')
G.edge['vmwared']['zygote']['write-read'] = '[open open]'
G.add_edge('vmwared','at_distributor')
G.edge['vmwared']['at_distributor']['write-read'] = '[open open][setattr getattr]'
G.add_edge('vmwared','cbd')
G.edge['vmwared']['cbd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('vmwared','charon')
G.edge['vmwared']['charon']['write-read'] = '[open open][setattr getattr]'
G.add_edge('vmwared','debuggerd')
G.edge['vmwared']['debuggerd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('vmwared','diag_uart_log')
G.edge['vmwared']['diag_uart_log']['write-read'] = '[open open][setattr getattr]'
G.add_edge('vmwared','dumpstate')
G.edge['vmwared']['dumpstate']['write-read'] = '[open open][setattr getattr]'
G.add_edge('vmwared','hostapd')
G.edge['vmwared']['hostapd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('vmwared','ime_app')
G.edge['vmwared']['ime_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('vmwared','init_shell')
G.edge['vmwared']['init_shell']['write-read'] = '[open open][setattr getattr]'
G.add_edge('vmwared','installd')
G.edge['vmwared']['installd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('vmwared','itsonbs')
G.edge['vmwared']['itsonbs']['write-read'] = '[open open][setattr getattr]'
G.add_edge('vmwared','logwrapper')
G.edge['vmwared']['logwrapper']['write-read'] = '[open open][setattr getattr]'
G.add_edge('vmwared','netd')
G.edge['vmwared']['netd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('vmwared','qmuxd')
G.edge['vmwared']['qmuxd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('vmwared','rild')
G.edge['vmwared']['rild']['write-read'] = '[open open][setattr getattr]'
G.add_edge('vmwared','rmt_storage')
G.edge['vmwared']['rmt_storage']['write-read'] = '[open open][setattr getattr]'
G.add_edge('vmwared','sdcardd')
G.edge['vmwared']['sdcardd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('vmwared','shell')
G.edge['vmwared']['shell']['write-read'] = '[open open][setattr getattr]'
G.add_edge('vmwared','s_system_app')
G.edge['vmwared']['s_system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('vmwared','system_app')
G.edge['vmwared']['system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('vmwared','system_server')
G.edge['vmwared']['system_server']['write-read'] = '[open open][setattr getattr]'
G.add_edge('vmwared','vmwared')
G.edge['vmwared']['vmwared']['write-read'] = '[open open][setattr getattr]'
G.add_edge('vmwared','wpa')
G.edge['vmwared']['wpa']['write-read'] = '[open open][setattr getattr]'
G.add_edge('vmwared','zygote')
G.edge['vmwared']['zygote']['write-read'] = '[open open][setattr getattr]'
G.add_edge('vmwared','adbd')
G.edge['vmwared']['adbd']['write-read'] = '[write read]'
G.edge['vmwared']['adbd']['fill'] = 'red'
G.add_edge('vmwared','at_distributor')
G.edge['vmwared']['at_distributor']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['vmwared']['at_distributor']['fill'] = 'red'
G.add_edge('vmwared','cbd')
G.edge['vmwared']['cbd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['vmwared']['cbd']['fill'] = 'red'
G.add_edge('vmwared','charon')
G.edge['vmwared']['charon']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['vmwared']['charon']['fill'] = 'red'
G.add_edge('vmwared','debuggerd')
G.edge['vmwared']['debuggerd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['vmwared']['debuggerd']['fill'] = 'red'
G.add_edge('vmwared','dhcp')
G.edge['vmwared']['dhcp']['write-read'] = '[write read]'
G.edge['vmwared']['dhcp']['fill'] = 'red'
G.add_edge('vmwared','diag_uart_log')
G.edge['vmwared']['diag_uart_log']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['vmwared']['diag_uart_log']['fill'] = 'red'
G.add_edge('vmwared','domain')
G.edge['vmwared']['domain']['write-read'] = '[write read]'
G.edge['vmwared']['domain']['fill'] = 'red'
G.add_edge('vmwared','dumpstate')
G.edge['vmwared']['dumpstate']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['vmwared']['dumpstate']['fill'] = 'red'
G.add_edge('vmwared','hostapd')
G.edge['vmwared']['hostapd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['vmwared']['hostapd']['fill'] = 'red'
G.add_edge('vmwared','ime_app')
G.edge['vmwared']['ime_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['vmwared']['ime_app']['fill'] = 'red'
G.add_edge('vmwared','init_shell')
G.edge['vmwared']['init_shell']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['vmwared']['init_shell']['fill'] = 'red'
G.add_edge('vmwared','installd')
G.edge['vmwared']['installd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['vmwared']['installd']['fill'] = 'red'
G.add_edge('vmwared','itsonbs')
G.edge['vmwared']['itsonbs']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['vmwared']['itsonbs']['fill'] = 'red'
G.add_edge('vmwared','logwrapper')
G.edge['vmwared']['logwrapper']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['vmwared']['logwrapper']['fill'] = 'red'
G.add_edge('vmwared','netd')
G.edge['vmwared']['netd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['vmwared']['netd']['fill'] = 'red'
G.add_edge('vmwared','qmuxd')
G.edge['vmwared']['qmuxd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['vmwared']['qmuxd']['fill'] = 'red'
G.add_edge('vmwared','rild')
G.edge['vmwared']['rild']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['vmwared']['rild']['fill'] = 'red'
G.add_edge('vmwared','rmt_storage')
G.edge['vmwared']['rmt_storage']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['vmwared']['rmt_storage']['fill'] = 'red'
G.add_edge('vmwared','sdcardd')
G.edge['vmwared']['sdcardd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['vmwared']['sdcardd']['fill'] = 'red'
G.add_edge('vmwared','shell')
G.edge['vmwared']['shell']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['vmwared']['shell']['fill'] = 'red'
G.add_edge('vmwared','s_system_app')
G.edge['vmwared']['s_system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['vmwared']['s_system_app']['fill'] = 'red'
G.add_edge('vmwared','system_app')
G.edge['vmwared']['system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['vmwared']['system_app']['fill'] = 'red'
G.add_edge('vmwared','system_server')
G.edge['vmwared']['system_server']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['vmwared']['system_server']['fill'] = 'red'
G.add_edge('vmwared','vmwared')
G.edge['vmwared']['vmwared']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['vmwared']['vmwared']['fill'] = 'red'
G.add_edge('vmwared','wpa')
G.edge['vmwared']['wpa']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['vmwared']['wpa']['fill'] = 'red'
G.add_edge('vmwared','zygote')
G.edge['vmwared']['zygote']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['vmwared']['zygote']['fill'] = 'red'
G.add_edge('vmwared','adbd')
G.edge['vmwared']['adbd']['write-read'] = '[write read][add_name search]'
G.add_edge('vmwared','at_distributor')
G.edge['vmwared']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('vmwared','at_distributor')
G.edge['vmwared']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('vmwared','auditd')
G.edge['vmwared']['auditd']['write-read'] = '[add_name search]'
G.add_edge('vmwared','cbd')
G.edge['vmwared']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('vmwared','cbd')
G.edge['vmwared']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('vmwared','charon')
G.edge['vmwared']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('vmwared','charon')
G.edge['vmwared']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('vmwared','clatd')
G.edge['vmwared']['clatd']['write-read'] = '[add_name search]'
G.add_edge('vmwared','debuggerd')
G.edge['vmwared']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('vmwared','debuggerd')
G.edge['vmwared']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('vmwared','dhcp')
G.edge['vmwared']['dhcp']['write-read'] = '[write read][add_name search]'
G.add_edge('vmwared','diag_uart_log')
G.edge['vmwared']['diag_uart_log']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('vmwared','diag_uart_log')
G.edge['vmwared']['diag_uart_log']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('vmwared','dumpstate')
G.edge['vmwared']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('vmwared','dumpstate')
G.edge['vmwared']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('vmwared','hostapd')
G.edge['vmwared']['hostapd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('vmwared','hostapd')
G.edge['vmwared']['hostapd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('vmwared','hvdcp')
G.edge['vmwared']['hvdcp']['write-read'] = '[add_name search]'
G.add_edge('vmwared','ime_app')
G.edge['vmwared']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('vmwared','ime_app')
G.edge['vmwared']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('vmwared','init_shell')
G.edge['vmwared']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('vmwared','init_shell')
G.edge['vmwared']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('vmwared','installd')
G.edge['vmwared']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('vmwared','installd')
G.edge['vmwared']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('vmwared','itsonbs')
G.edge['vmwared']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('vmwared','itsonbs')
G.edge['vmwared']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('vmwared','jackservice')
G.edge['vmwared']['jackservice']['write-read'] = '[add_name search]'
G.add_edge('vmwared','lmkd')
G.edge['vmwared']['lmkd']['write-read'] = '[remove_name search]'
G.add_edge('vmwared','logwrapper')
G.edge['vmwared']['logwrapper']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('vmwared','logwrapper')
G.edge['vmwared']['logwrapper']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('vmwared','msm_irqbalanced')
G.edge['vmwared']['msm_irqbalanced']['write-read'] = '[add_name search]'
G.add_edge('vmwared','netd')
G.edge['vmwared']['netd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('vmwared','netd')
G.edge['vmwared']['netd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('vmwared','qmuxd')
G.edge['vmwared']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('vmwared','qmuxd')
G.edge['vmwared']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('vmwared','racoon')
G.edge['vmwared']['racoon']['write-read'] = '[add_name search]'
G.add_edge('vmwared','rild')
G.edge['vmwared']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('vmwared','rild')
G.edge['vmwared']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('vmwared','rmt_storage')
G.edge['vmwared']['rmt_storage']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('vmwared','rmt_storage')
G.edge['vmwared']['rmt_storage']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('vmwared','sdcardd')
G.edge['vmwared']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('vmwared','sdcardd')
G.edge['vmwared']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('vmwared','sensors')
G.edge['vmwared']['sensors']['write-read'] = '[add_name search]'
G.add_edge('vmwared','shell')
G.edge['vmwared']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('vmwared','shell')
G.edge['vmwared']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('vmwared','s_system_app')
G.edge['vmwared']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('vmwared','s_system_app')
G.edge['vmwared']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('vmwared','system_app')
G.edge['vmwared']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('vmwared','system_app')
G.edge['vmwared']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('vmwared','system_server')
G.edge['vmwared']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('vmwared','system_server')
G.edge['vmwared']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('vmwared','system_server')
G.edge['vmwared']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search]'
G.add_edge('vmwared','vmwared')
G.edge['vmwared']['vmwared']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('vmwared','vmwared')
G.edge['vmwared']['vmwared']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('vmwared','wpa')
G.edge['vmwared']['wpa']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('vmwared','wpa')
G.edge['vmwared']['wpa']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('vmwared','zygote')
G.edge['vmwared']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('vmwared','zygote')
G.edge['vmwared']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('wpa','at_distributor')
G.edge['wpa']['at_distributor']['write-read'] = '[open open]'
G.add_edge('wpa','cbd')
G.edge['wpa']['cbd']['write-read'] = '[open open]'
G.add_edge('wpa','charon')
G.edge['wpa']['charon']['write-read'] = '[open open]'
G.add_edge('wpa','debuggerd')
G.edge['wpa']['debuggerd']['write-read'] = '[open open]'
G.add_edge('wpa','diag_uart_log')
G.edge['wpa']['diag_uart_log']['write-read'] = '[open open]'
G.add_edge('wpa','dumpstate')
G.edge['wpa']['dumpstate']['write-read'] = '[open open]'
G.add_edge('wpa','hostapd')
G.edge['wpa']['hostapd']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('wpa','ime_app')
G.edge['wpa']['ime_app']['write-read'] = '[open open]'
G.add_edge('wpa','init_shell')
G.edge['wpa']['init_shell']['write-read'] = '[open open]'
G.add_edge('wpa','installd')
G.edge['wpa']['installd']['write-read'] = '[open open]'
G.add_edge('wpa','itsonbs')
G.edge['wpa']['itsonbs']['write-read'] = '[open open]'
G.add_edge('wpa','logwrapper')
G.edge['wpa']['logwrapper']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('wpa','netd')
G.edge['wpa']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('wpa','qmuxd')
G.edge['wpa']['qmuxd']['write-read'] = '[open open]'
G.add_edge('wpa','rild')
G.edge['wpa']['rild']['write-read'] = '[open open]'
G.add_edge('wpa','rmt_storage')
G.edge['wpa']['rmt_storage']['write-read'] = '[open open]'
G.add_edge('wpa','sdcardd')
G.edge['wpa']['sdcardd']['write-read'] = '[open open]'
G.add_edge('wpa','shell')
G.edge['wpa']['shell']['write-read'] = '[open open]'
G.add_edge('wpa','s_system_app')
G.edge['wpa']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('wpa','system_app')
G.edge['wpa']['system_app']['write-read'] = '[open open]'
G.add_edge('wpa','system_server')
G.edge['wpa']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('wpa','vmwared')
G.edge['wpa']['vmwared']['write-read'] = '[open open]'
G.add_edge('wpa','wpa')
G.edge['wpa']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('wpa','zygote')
G.edge['wpa']['zygote']['write-read'] = '[open open]'
G.add_edge('wpa','at_distributor')
G.edge['wpa']['at_distributor']['write-read'] = '[open open][setattr getattr]'
G.add_edge('wpa','cbd')
G.edge['wpa']['cbd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('wpa','charon')
G.edge['wpa']['charon']['write-read'] = '[open open][setattr getattr]'
G.add_edge('wpa','debuggerd')
G.edge['wpa']['debuggerd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('wpa','diag_uart_log')
G.edge['wpa']['diag_uart_log']['write-read'] = '[open open][setattr getattr]'
G.add_edge('wpa','dumpstate')
G.edge['wpa']['dumpstate']['write-read'] = '[open open][setattr getattr]'
G.add_edge('wpa','hostapd')
G.edge['wpa']['hostapd']['write-read'] = '[open open][write read][append read][open open][setattr getattr]'
G.add_edge('wpa','ime_app')
G.edge['wpa']['ime_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('wpa','init_shell')
G.edge['wpa']['init_shell']['write-read'] = '[open open][setattr getattr]'
G.add_edge('wpa','installd')
G.edge['wpa']['installd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('wpa','itsonbs')
G.edge['wpa']['itsonbs']['write-read'] = '[open open][setattr getattr]'
G.add_edge('wpa','logwrapper')
G.edge['wpa']['logwrapper']['write-read'] = '[open open][write read][append read][open open][setattr getattr]'
G.add_edge('wpa','netd')
G.edge['wpa']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('wpa','qmuxd')
G.edge['wpa']['qmuxd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('wpa','rild')
G.edge['wpa']['rild']['write-read'] = '[open open][setattr getattr]'
G.add_edge('wpa','rmt_storage')
G.edge['wpa']['rmt_storage']['write-read'] = '[open open][setattr getattr]'
G.add_edge('wpa','sdcardd')
G.edge['wpa']['sdcardd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('wpa','shell')
G.edge['wpa']['shell']['write-read'] = '[open open][setattr getattr]'
G.add_edge('wpa','s_system_app')
G.edge['wpa']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('wpa','system_app')
G.edge['wpa']['system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('wpa','system_server')
G.edge['wpa']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('wpa','vmwared')
G.edge['wpa']['vmwared']['write-read'] = '[open open][setattr getattr]'
G.add_edge('wpa','wpa')
G.edge['wpa']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('wpa','zygote')
G.edge['wpa']['zygote']['write-read'] = '[open open][setattr getattr]'
G.add_edge('wpa','adbd')
G.edge['wpa']['adbd']['write-read'] = '[write read]'
G.edge['wpa']['adbd']['fill'] = 'red'
G.add_edge('wpa','at_distributor')
G.edge['wpa']['at_distributor']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['wpa']['at_distributor']['fill'] = 'red'
G.add_edge('wpa','cbd')
G.edge['wpa']['cbd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['wpa']['cbd']['fill'] = 'red'
G.add_edge('wpa','charon')
G.edge['wpa']['charon']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['wpa']['charon']['fill'] = 'red'
G.add_edge('wpa','debuggerd')
G.edge['wpa']['debuggerd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['wpa']['debuggerd']['fill'] = 'red'
G.add_edge('wpa','dhcp')
G.edge['wpa']['dhcp']['write-read'] = '[write read]'
G.edge['wpa']['dhcp']['fill'] = 'red'
G.add_edge('wpa','diag_uart_log')
G.edge['wpa']['diag_uart_log']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['wpa']['diag_uart_log']['fill'] = 'red'
G.add_edge('wpa','domain')
G.edge['wpa']['domain']['write-read'] = '[write read]'
G.edge['wpa']['domain']['fill'] = 'red'
G.add_edge('wpa','dumpstate')
G.edge['wpa']['dumpstate']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['wpa']['dumpstate']['fill'] = 'red'
G.add_edge('wpa','hostapd')
G.edge['wpa']['hostapd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read]'
G.edge['wpa']['hostapd']['fill'] = 'red'
G.add_edge('wpa','ime_app')
G.edge['wpa']['ime_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['wpa']['ime_app']['fill'] = 'red'
G.add_edge('wpa','init_shell')
G.edge['wpa']['init_shell']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['wpa']['init_shell']['fill'] = 'red'
G.add_edge('wpa','installd')
G.edge['wpa']['installd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['wpa']['installd']['fill'] = 'red'
G.add_edge('wpa','itsonbs')
G.edge['wpa']['itsonbs']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['wpa']['itsonbs']['fill'] = 'red'
G.add_edge('wpa','logwrapper')
G.edge['wpa']['logwrapper']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read]'
G.edge['wpa']['logwrapper']['fill'] = 'red'
G.add_edge('wpa','netd')
G.edge['wpa']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['wpa']['netd']['fill'] = 'red'
G.add_edge('wpa','qmuxd')
G.edge['wpa']['qmuxd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['wpa']['qmuxd']['fill'] = 'red'
G.add_edge('wpa','rild')
G.edge['wpa']['rild']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['wpa']['rild']['fill'] = 'red'
G.add_edge('wpa','rmt_storage')
G.edge['wpa']['rmt_storage']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['wpa']['rmt_storage']['fill'] = 'red'
G.add_edge('wpa','sdcardd')
G.edge['wpa']['sdcardd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['wpa']['sdcardd']['fill'] = 'red'
G.add_edge('wpa','shell')
G.edge['wpa']['shell']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['wpa']['shell']['fill'] = 'red'
G.add_edge('wpa','s_system_app')
G.edge['wpa']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['wpa']['s_system_app']['fill'] = 'red'
G.add_edge('wpa','system_app')
G.edge['wpa']['system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['wpa']['system_app']['fill'] = 'red'
G.add_edge('wpa','system_server')
G.edge['wpa']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['wpa']['system_server']['fill'] = 'red'
G.add_edge('wpa','vmwared')
G.edge['wpa']['vmwared']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['wpa']['vmwared']['fill'] = 'red'
G.add_edge('wpa','wpa')
G.edge['wpa']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['wpa']['wpa']['fill'] = 'red'
G.add_edge('wpa','zygote')
G.edge['wpa']['zygote']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['wpa']['zygote']['fill'] = 'red'
G.add_edge('wpa','adbd')
G.edge['wpa']['adbd']['write-read'] = '[write read][add_name search]'
G.add_edge('wpa','at_distributor')
G.edge['wpa']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('wpa','at_distributor')
G.edge['wpa']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('wpa','auditd')
G.edge['wpa']['auditd']['write-read'] = '[add_name search]'
G.add_edge('wpa','cbd')
G.edge['wpa']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('wpa','cbd')
G.edge['wpa']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('wpa','charon')
G.edge['wpa']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('wpa','charon')
G.edge['wpa']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('wpa','clatd')
G.edge['wpa']['clatd']['write-read'] = '[add_name search]'
G.add_edge('wpa','debuggerd')
G.edge['wpa']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('wpa','debuggerd')
G.edge['wpa']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('wpa','dhcp')
G.edge['wpa']['dhcp']['write-read'] = '[write read][add_name search]'
G.add_edge('wpa','diag_uart_log')
G.edge['wpa']['diag_uart_log']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('wpa','diag_uart_log')
G.edge['wpa']['diag_uart_log']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('wpa','dumpstate')
G.edge['wpa']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('wpa','dumpstate')
G.edge['wpa']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('wpa','hostapd')
G.edge['wpa']['hostapd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('wpa','hostapd')
G.edge['wpa']['hostapd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('wpa','hvdcp')
G.edge['wpa']['hvdcp']['write-read'] = '[add_name search]'
G.add_edge('wpa','ime_app')
G.edge['wpa']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('wpa','ime_app')
G.edge['wpa']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('wpa','init_shell')
G.edge['wpa']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('wpa','init_shell')
G.edge['wpa']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('wpa','installd')
G.edge['wpa']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('wpa','installd')
G.edge['wpa']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('wpa','itsonbs')
G.edge['wpa']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('wpa','itsonbs')
G.edge['wpa']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('wpa','jackservice')
G.edge['wpa']['jackservice']['write-read'] = '[add_name search]'
G.add_edge('wpa','lmkd')
G.edge['wpa']['lmkd']['write-read'] = '[remove_name search]'
G.add_edge('wpa','logwrapper')
G.edge['wpa']['logwrapper']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('wpa','logwrapper')
G.edge['wpa']['logwrapper']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('wpa','msm_irqbalanced')
G.edge['wpa']['msm_irqbalanced']['write-read'] = '[add_name search]'
G.add_edge('wpa','netd')
G.edge['wpa']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('wpa','netd')
G.edge['wpa']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('wpa','qmuxd')
G.edge['wpa']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('wpa','qmuxd')
G.edge['wpa']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('wpa','racoon')
G.edge['wpa']['racoon']['write-read'] = '[add_name search]'
G.add_edge('wpa','rild')
G.edge['wpa']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('wpa','rild')
G.edge['wpa']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('wpa','rmt_storage')
G.edge['wpa']['rmt_storage']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('wpa','rmt_storage')
G.edge['wpa']['rmt_storage']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('wpa','sdcardd')
G.edge['wpa']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('wpa','sdcardd')
G.edge['wpa']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('wpa','sensors')
G.edge['wpa']['sensors']['write-read'] = '[add_name search]'
G.add_edge('wpa','shell')
G.edge['wpa']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('wpa','shell')
G.edge['wpa']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('wpa','s_system_app')
G.edge['wpa']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('wpa','s_system_app')
G.edge['wpa']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('wpa','system_app')
G.edge['wpa']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('wpa','system_app')
G.edge['wpa']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('wpa','system_server')
G.edge['wpa']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('wpa','system_server')
G.edge['wpa']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('wpa','system_server')
G.edge['wpa']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search]'
G.add_edge('wpa','vmwared')
G.edge['wpa']['vmwared']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('wpa','vmwared')
G.edge['wpa']['vmwared']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('wpa','wpa')
G.edge['wpa']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('wpa','wpa')
G.edge['wpa']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('wpa','zygote')
G.edge['wpa']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('wpa','zygote')
G.edge['wpa']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('zygote','at_distributor')
G.edge['zygote']['at_distributor']['write-read'] = '[open open]'
G.add_edge('zygote','cbd')
G.edge['zygote']['cbd']['write-read'] = '[open open]'
G.add_edge('zygote','charon')
G.edge['zygote']['charon']['write-read'] = '[open open]'
G.add_edge('zygote','debuggerd')
G.edge['zygote']['debuggerd']['write-read'] = '[open open]'
G.add_edge('zygote','diag_uart_log')
G.edge['zygote']['diag_uart_log']['write-read'] = '[open open]'
G.add_edge('zygote','dumpstate')
G.edge['zygote']['dumpstate']['write-read'] = '[open open]'
G.add_edge('zygote','hostapd')
G.edge['zygote']['hostapd']['write-read'] = '[open open]'
G.add_edge('zygote','ime_app')
G.edge['zygote']['ime_app']['write-read'] = '[open open]'
G.add_edge('zygote','init_shell')
G.edge['zygote']['init_shell']['write-read'] = '[open open]'
G.add_edge('zygote','installd')
G.edge['zygote']['installd']['write-read'] = '[open open]'
G.add_edge('zygote','itsonbs')
G.edge['zygote']['itsonbs']['write-read'] = '[open open]'
G.add_edge('zygote','logwrapper')
G.edge['zygote']['logwrapper']['write-read'] = '[open open]'
G.add_edge('zygote','netd')
G.edge['zygote']['netd']['write-read'] = '[open open]'
G.add_edge('zygote','qmuxd')
G.edge['zygote']['qmuxd']['write-read'] = '[open open]'
G.add_edge('zygote','rild')
G.edge['zygote']['rild']['write-read'] = '[open open]'
G.add_edge('zygote','rmt_storage')
G.edge['zygote']['rmt_storage']['write-read'] = '[open open]'
G.add_edge('zygote','sdcardd')
G.edge['zygote']['sdcardd']['write-read'] = '[open open]'
G.add_edge('zygote','shell')
G.edge['zygote']['shell']['write-read'] = '[open open]'
G.add_edge('zygote','s_system_app')
G.edge['zygote']['s_system_app']['write-read'] = '[open open]'
G.add_edge('zygote','system_app')
G.edge['zygote']['system_app']['write-read'] = '[open open]'
G.add_edge('zygote','system_server')
G.edge['zygote']['system_server']['write-read'] = '[open open]'
G.add_edge('zygote','vmwared')
G.edge['zygote']['vmwared']['write-read'] = '[open open]'
G.add_edge('zygote','wpa')
G.edge['zygote']['wpa']['write-read'] = '[open open]'
G.add_edge('zygote','zygote')
G.edge['zygote']['zygote']['write-read'] = '[open open]'
G.add_edge('zygote','at_distributor')
G.edge['zygote']['at_distributor']['write-read'] = '[open open][setattr getattr]'
G.add_edge('zygote','cbd')
G.edge['zygote']['cbd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('zygote','charon')
G.edge['zygote']['charon']['write-read'] = '[open open][setattr getattr]'
G.add_edge('zygote','debuggerd')
G.edge['zygote']['debuggerd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('zygote','diag_uart_log')
G.edge['zygote']['diag_uart_log']['write-read'] = '[open open][setattr getattr]'
G.add_edge('zygote','dumpstate')
G.edge['zygote']['dumpstate']['write-read'] = '[open open][setattr getattr]'
G.add_edge('zygote','hostapd')
G.edge['zygote']['hostapd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('zygote','ime_app')
G.edge['zygote']['ime_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('zygote','init_shell')
G.edge['zygote']['init_shell']['write-read'] = '[open open][setattr getattr]'
G.add_edge('zygote','installd')
G.edge['zygote']['installd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('zygote','itsonbs')
G.edge['zygote']['itsonbs']['write-read'] = '[open open][setattr getattr]'
G.add_edge('zygote','logwrapper')
G.edge['zygote']['logwrapper']['write-read'] = '[open open][setattr getattr]'
G.add_edge('zygote','netd')
G.edge['zygote']['netd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('zygote','qmuxd')
G.edge['zygote']['qmuxd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('zygote','rild')
G.edge['zygote']['rild']['write-read'] = '[open open][setattr getattr]'
G.add_edge('zygote','rmt_storage')
G.edge['zygote']['rmt_storage']['write-read'] = '[open open][setattr getattr]'
G.add_edge('zygote','sdcardd')
G.edge['zygote']['sdcardd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('zygote','shell')
G.edge['zygote']['shell']['write-read'] = '[open open][setattr getattr]'
G.add_edge('zygote','s_system_app')
G.edge['zygote']['s_system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('zygote','system_app')
G.edge['zygote']['system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('zygote','system_server')
G.edge['zygote']['system_server']['write-read'] = '[open open][setattr getattr]'
G.add_edge('zygote','vmwared')
G.edge['zygote']['vmwared']['write-read'] = '[open open][setattr getattr]'
G.add_edge('zygote','wpa')
G.edge['zygote']['wpa']['write-read'] = '[open open][setattr getattr]'
G.add_edge('zygote','zygote')
G.edge['zygote']['zygote']['write-read'] = '[open open][setattr getattr]'
G.add_edge('zygote','adbd')
G.edge['zygote']['adbd']['write-read'] = '[write read]'
G.edge['zygote']['adbd']['fill'] = 'red'
G.add_edge('zygote','at_distributor')
G.edge['zygote']['at_distributor']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['zygote']['at_distributor']['fill'] = 'red'
G.add_edge('zygote','cbd')
G.edge['zygote']['cbd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['zygote']['cbd']['fill'] = 'red'
G.add_edge('zygote','charon')
G.edge['zygote']['charon']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['zygote']['charon']['fill'] = 'red'
G.add_edge('zygote','debuggerd')
G.edge['zygote']['debuggerd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['zygote']['debuggerd']['fill'] = 'red'
G.add_edge('zygote','dhcp')
G.edge['zygote']['dhcp']['write-read'] = '[write read]'
G.edge['zygote']['dhcp']['fill'] = 'red'
G.add_edge('zygote','diag_uart_log')
G.edge['zygote']['diag_uart_log']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['zygote']['diag_uart_log']['fill'] = 'red'
G.add_edge('zygote','domain')
G.edge['zygote']['domain']['write-read'] = '[write read]'
G.edge['zygote']['domain']['fill'] = 'red'
G.add_edge('zygote','dumpstate')
G.edge['zygote']['dumpstate']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['zygote']['dumpstate']['fill'] = 'red'
G.add_edge('zygote','hostapd')
G.edge['zygote']['hostapd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['zygote']['hostapd']['fill'] = 'red'
G.add_edge('zygote','ime_app')
G.edge['zygote']['ime_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['zygote']['ime_app']['fill'] = 'red'
G.add_edge('zygote','init_shell')
G.edge['zygote']['init_shell']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['zygote']['init_shell']['fill'] = 'red'
G.add_edge('zygote','installd')
G.edge['zygote']['installd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['zygote']['installd']['fill'] = 'red'
G.add_edge('zygote','itsonbs')
G.edge['zygote']['itsonbs']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['zygote']['itsonbs']['fill'] = 'red'
G.add_edge('zygote','logwrapper')
G.edge['zygote']['logwrapper']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['zygote']['logwrapper']['fill'] = 'red'
G.add_edge('zygote','netd')
G.edge['zygote']['netd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['zygote']['netd']['fill'] = 'red'
G.add_edge('zygote','qmuxd')
G.edge['zygote']['qmuxd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['zygote']['qmuxd']['fill'] = 'red'
G.add_edge('zygote','rild')
G.edge['zygote']['rild']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['zygote']['rild']['fill'] = 'red'
G.add_edge('zygote','rmt_storage')
G.edge['zygote']['rmt_storage']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['zygote']['rmt_storage']['fill'] = 'red'
G.add_edge('zygote','sdcardd')
G.edge['zygote']['sdcardd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['zygote']['sdcardd']['fill'] = 'red'
G.add_edge('zygote','shell')
G.edge['zygote']['shell']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['zygote']['shell']['fill'] = 'red'
G.add_edge('zygote','s_system_app')
G.edge['zygote']['s_system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['zygote']['s_system_app']['fill'] = 'red'
G.add_edge('zygote','system_app')
G.edge['zygote']['system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['zygote']['system_app']['fill'] = 'red'
G.add_edge('zygote','system_server')
G.edge['zygote']['system_server']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['zygote']['system_server']['fill'] = 'red'
G.add_edge('zygote','vmwared')
G.edge['zygote']['vmwared']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['zygote']['vmwared']['fill'] = 'red'
G.add_edge('zygote','wpa')
G.edge['zygote']['wpa']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['zygote']['wpa']['fill'] = 'red'
G.add_edge('zygote','zygote')
G.edge['zygote']['zygote']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['zygote']['zygote']['fill'] = 'red'
G.add_edge('zygote','adbd')
G.edge['zygote']['adbd']['write-read'] = '[write read][add_name search]'
G.add_edge('zygote','at_distributor')
G.edge['zygote']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('zygote','at_distributor')
G.edge['zygote']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('zygote','auditd')
G.edge['zygote']['auditd']['write-read'] = '[add_name search]'
G.add_edge('zygote','cbd')
G.edge['zygote']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('zygote','cbd')
G.edge['zygote']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('zygote','charon')
G.edge['zygote']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('zygote','charon')
G.edge['zygote']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('zygote','clatd')
G.edge['zygote']['clatd']['write-read'] = '[add_name search]'
G.add_edge('zygote','debuggerd')
G.edge['zygote']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('zygote','debuggerd')
G.edge['zygote']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('zygote','dhcp')
G.edge['zygote']['dhcp']['write-read'] = '[write read][add_name search]'
G.add_edge('zygote','diag_uart_log')
G.edge['zygote']['diag_uart_log']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('zygote','diag_uart_log')
G.edge['zygote']['diag_uart_log']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('zygote','dumpstate')
G.edge['zygote']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('zygote','dumpstate')
G.edge['zygote']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('zygote','hostapd')
G.edge['zygote']['hostapd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('zygote','hostapd')
G.edge['zygote']['hostapd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('zygote','hvdcp')
G.edge['zygote']['hvdcp']['write-read'] = '[add_name search]'
G.add_edge('zygote','ime_app')
G.edge['zygote']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('zygote','ime_app')
G.edge['zygote']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('zygote','init_shell')
G.edge['zygote']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('zygote','init_shell')
G.edge['zygote']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('zygote','installd')
G.edge['zygote']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('zygote','installd')
G.edge['zygote']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('zygote','itsonbs')
G.edge['zygote']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('zygote','itsonbs')
G.edge['zygote']['itsonbs']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('zygote','jackservice')
G.edge['zygote']['jackservice']['write-read'] = '[add_name search]'
G.add_edge('zygote','lmkd')
G.edge['zygote']['lmkd']['write-read'] = '[remove_name search]'
G.add_edge('zygote','logwrapper')
G.edge['zygote']['logwrapper']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('zygote','logwrapper')
G.edge['zygote']['logwrapper']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('zygote','msm_irqbalanced')
G.edge['zygote']['msm_irqbalanced']['write-read'] = '[add_name search]'
G.add_edge('zygote','netd')
G.edge['zygote']['netd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('zygote','netd')
G.edge['zygote']['netd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('zygote','qmuxd')
G.edge['zygote']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('zygote','qmuxd')
G.edge['zygote']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('zygote','racoon')
G.edge['zygote']['racoon']['write-read'] = '[add_name search]'
G.add_edge('zygote','rild')
G.edge['zygote']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('zygote','rild')
G.edge['zygote']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('zygote','rmt_storage')
G.edge['zygote']['rmt_storage']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('zygote','rmt_storage')
G.edge['zygote']['rmt_storage']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('zygote','sdcardd')
G.edge['zygote']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('zygote','sdcardd')
G.edge['zygote']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('zygote','sensors')
G.edge['zygote']['sensors']['write-read'] = '[add_name search]'
G.add_edge('zygote','shell')
G.edge['zygote']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('zygote','shell')
G.edge['zygote']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('zygote','s_system_app')
G.edge['zygote']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('zygote','s_system_app')
G.edge['zygote']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('zygote','system_app')
G.edge['zygote']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('zygote','system_app')
G.edge['zygote']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('zygote','system_server')
G.edge['zygote']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('zygote','system_server')
G.edge['zygote']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('zygote','system_server')
G.edge['zygote']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search]'
G.add_edge('zygote','vmwared')
G.edge['zygote']['vmwared']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('zygote','vmwared')
G.edge['zygote']['vmwared']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('zygote','wpa')
G.edge['zygote']['wpa']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('zygote','wpa')
G.edge['zygote']['wpa']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('zygote','zygote')
G.edge['zygote']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('zygote','zygote')
G.edge['zygote']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
app = Viewer(G)
app.mainloop()