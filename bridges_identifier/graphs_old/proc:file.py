import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('charon','bluetooth')
G.edge['charon']['bluetooth']['write-read'] = '[open open][open open][write read][append read][write read][append read][write read][open open]'
G.add_edge('charon','charon')
G.edge['charon']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('charon','clatd')
G.edge['charon']['clatd']['write-read'] = '[add_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('charon','ime_app')
G.edge['charon']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][write read][open open]'
G.add_edge('charon','init_shell')
G.edge['charon']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open]'
G.add_edge('charon','install_recovery')
G.edge['charon']['install_recovery']['write-read'] = '[open open]'
G.add_edge('charon','netmgrd')
G.edge['charon']['netmgrd']['write-read'] = '[open open][write read][append read][write read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read][write read][open open]'
G.add_edge('charon','rild')
G.edge['charon']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][write read][open open]'
G.add_edge('charon','sswap')
G.edge['charon']['sswap']['write-read'] = '[open open]'
G.add_edge('charon','s_system_app')
G.edge['charon']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read][open open][write read][append read][write read][open open]'
G.add_edge('charon','s_system_app')
G.edge['charon']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read][open open][write read][append read][write read][open open][open open]'
G.add_edge('charon','system_app')
G.edge['charon']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read][open open][write read][append read][write read][open open]'
G.add_edge('charon','system_server')
G.edge['charon']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][write read][open open]'
G.add_edge('charon','bluetooth')
G.edge['charon']['bluetooth']['write-read'] = '[open open][open open][write read][append read][write read][append read][write read][open open][append read]'
G.add_edge('charon','charon')
G.edge['charon']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read]'
G.edge['charon']['charon']['fill'] = 'red'
G.add_edge('charon','charon')
G.edge['charon']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read]'
G.add_edge('charon','clatd')
G.edge['charon']['clatd']['write-read'] = '[add_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read]'
G.edge['charon']['clatd']['fill'] = 'red'
G.add_edge('charon','clatd')
G.edge['charon']['clatd']['write-read'] = '[add_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read]'
G.add_edge('charon','debuggerd')
G.edge['charon']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['charon']['debuggerd']['fill'] = 'red'
G.add_edge('charon','dhcp')
G.edge['charon']['dhcp']['write-read'] = '[write read][add_name search][write read][write read][write read]'
G.edge['charon']['dhcp']['fill'] = 'red'
G.add_edge('charon','ime_app')
G.edge['charon']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][write read][open open][append read]'
G.add_edge('charon','init_shell')
G.edge['charon']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read]'
G.edge['charon']['init_shell']['fill'] = 'red'
G.add_edge('charon','init_shell')
G.edge['charon']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][append read]'
G.add_edge('charon','install_recovery')
G.edge['charon']['install_recovery']['write-read'] = '[open open][write read]'
G.edge['charon']['install_recovery']['fill'] = 'red'
G.add_edge('charon','install_recovery')
G.edge['charon']['install_recovery']['write-read'] = '[open open][write read][append read]'
G.add_edge('charon','mediaserver')
G.edge['charon']['mediaserver']['write-read'] = '[write read][write read]'
G.edge['charon']['mediaserver']['fill'] = 'red'
G.add_edge('charon','msm_irqbalanced')
G.edge['charon']['msm_irqbalanced']['write-read'] = '[add_name search][write read]'
G.edge['charon']['msm_irqbalanced']['fill'] = 'red'
G.add_edge('charon','netmgrd')
G.edge['charon']['netmgrd']['write-read'] = '[open open][write read][append read][write read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read][write read][open open][write read]'
G.edge['charon']['netmgrd']['fill'] = 'red'
G.add_edge('charon','netmgrd')
G.edge['charon']['netmgrd']['write-read'] = '[open open][write read][append read][write read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read][write read][open open][write read][append read]'
G.add_edge('charon','perfd')
G.edge['charon']['perfd']['write-read'] = '[write read]'
G.edge['charon']['perfd']['fill'] = 'red'
G.add_edge('charon','rild')
G.edge['charon']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][write read][open open][write read]'
G.edge['charon']['rild']['fill'] = 'red'
G.add_edge('charon','rild')
G.edge['charon']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][write read][open open][write read][append read]'
G.add_edge('charon','rtcc')
G.edge['charon']['rtcc']['write-read'] = '[write read]'
G.edge['charon']['rtcc']['fill'] = 'red'
G.add_edge('charon','sswap')
G.edge['charon']['sswap']['write-read'] = '[open open][write read]'
G.edge['charon']['sswap']['fill'] = 'red'
G.add_edge('charon','sswap')
G.edge['charon']['sswap']['write-read'] = '[open open][write read][append read]'
G.add_edge('charon','s_system_app')
G.edge['charon']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read][open open][write read][append read][write read][open open][open open][append read]'
G.add_edge('charon','s_system_app')
G.edge['charon']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read][open open][write read][append read][write read][open open][open open][append read][write read]'
G.edge['charon']['s_system_app']['fill'] = 'red'
G.add_edge('charon','s_system_app')
G.edge['charon']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read][open open][write read][append read][write read][open open][open open][append read][write read][append read]'
G.add_edge('charon','system_app')
G.edge['charon']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read][open open][write read][append read][write read][open open][append read]'
G.add_edge('charon','system_server')
G.edge['charon']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][write read][open open][write read]'
G.edge['charon']['system_server']['fill'] = 'red'
G.add_edge('charon','system_server')
G.edge['charon']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][write read][open open][write read][append read]'
G.add_edge('charon','vold')
G.edge['charon']['vold']['write-read'] = '[write read][write read]'
G.edge['charon']['vold']['fill'] = 'red'
G.add_edge('charon','zygote')
G.edge['charon']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read][write read][write read]'
G.edge['charon']['zygote']['fill'] = 'red'
G.add_edge('clatd','bluetooth')
G.edge['clatd']['bluetooth']['write-read'] = '[open open][open open][write read][append read][write read][append read][open open]'
G.add_edge('clatd','charon')
G.edge['clatd']['charon']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('clatd','clatd')
G.edge['clatd']['clatd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][add_name search][remove_name search][open open][write read][append read][write read][setattr getattr][write read][append read][setopt getopt][write read][write read][write read][open open]'
G.add_edge('clatd','ime_app')
G.edge['clatd']['ime_app']['write-read'] = '[write read][setopt getopt][open open]'
G.add_edge('clatd','init_shell')
G.edge['clatd']['init_shell']['write-read'] = '[open open]'
G.add_edge('clatd','install_recovery')
G.edge['clatd']['install_recovery']['write-read'] = '[open open]'
G.add_edge('clatd','netmgrd')
G.edge['clatd']['netmgrd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open]'
G.add_edge('clatd','rild')
G.edge['clatd']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open]'
G.add_edge('clatd','sswap')
G.edge['clatd']['sswap']['write-read'] = '[open open]'
G.add_edge('clatd','s_system_app')
G.edge['clatd']['s_system_app']['write-read'] = '[write read][setopt getopt][open open]'
G.add_edge('clatd','s_system_app')
G.edge['clatd']['s_system_app']['write-read'] = '[write read][setopt getopt][open open][open open]'
G.add_edge('clatd','system_app')
G.edge['clatd']['system_app']['write-read'] = '[write read][setopt getopt][open open]'
G.add_edge('clatd','system_server')
G.edge['clatd']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][write read][setopt getopt][open open]'
G.add_edge('clatd','bluetooth')
G.edge['clatd']['bluetooth']['write-read'] = '[open open][open open][write read][append read][write read][append read][open open][append read]'
G.add_edge('clatd','charon')
G.edge['clatd']['charon']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read]'
G.edge['clatd']['charon']['fill'] = 'red'
G.add_edge('clatd','charon')
G.edge['clatd']['charon']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read]'
G.add_edge('clatd','clatd')
G.edge['clatd']['clatd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][add_name search][remove_name search][open open][write read][append read][write read][setattr getattr][write read][append read][setopt getopt][write read][write read][write read][open open][write read]'
G.edge['clatd']['clatd']['fill'] = 'red'
G.add_edge('clatd','clatd')
G.edge['clatd']['clatd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][add_name search][remove_name search][open open][write read][append read][write read][setattr getattr][write read][append read][setopt getopt][write read][write read][write read][open open][write read][append read]'
G.add_edge('clatd','debuggerd')
G.edge['clatd']['debuggerd']['write-read'] = '[write read]'
G.edge['clatd']['debuggerd']['fill'] = 'red'
G.add_edge('clatd','dhcp')
G.edge['clatd']['dhcp']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][write read][setopt getopt][write read][write read][write read][write read]'
G.edge['clatd']['dhcp']['fill'] = 'red'
G.add_edge('clatd','ime_app')
G.edge['clatd']['ime_app']['write-read'] = '[write read][setopt getopt][open open][append read]'
G.add_edge('clatd','init_shell')
G.edge['clatd']['init_shell']['write-read'] = '[open open][write read]'
G.edge['clatd']['init_shell']['fill'] = 'red'
G.add_edge('clatd','init_shell')
G.edge['clatd']['init_shell']['write-read'] = '[open open][write read][append read]'
G.add_edge('clatd','install_recovery')
G.edge['clatd']['install_recovery']['write-read'] = '[open open][write read]'
G.edge['clatd']['install_recovery']['fill'] = 'red'
G.add_edge('clatd','install_recovery')
G.edge['clatd']['install_recovery']['write-read'] = '[open open][write read][append read]'
G.add_edge('clatd','mediaserver')
G.edge['clatd']['mediaserver']['write-read'] = '[write read]'
G.edge['clatd']['mediaserver']['fill'] = 'red'
G.add_edge('clatd','msm_irqbalanced')
G.edge['clatd']['msm_irqbalanced']['write-read'] = '[write read]'
G.edge['clatd']['msm_irqbalanced']['fill'] = 'red'
G.add_edge('clatd','netmgrd')
G.edge['clatd']['netmgrd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['clatd']['netmgrd']['fill'] = 'red'
G.add_edge('clatd','netmgrd')
G.edge['clatd']['netmgrd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('clatd','perfd')
G.edge['clatd']['perfd']['write-read'] = '[write read]'
G.edge['clatd']['perfd']['fill'] = 'red'
G.add_edge('clatd','rild')
G.edge['clatd']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read]'
G.edge['clatd']['rild']['fill'] = 'red'
G.add_edge('clatd','rild')
G.edge['clatd']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read]'
G.add_edge('clatd','rtcc')
G.edge['clatd']['rtcc']['write-read'] = '[write read]'
G.edge['clatd']['rtcc']['fill'] = 'red'
G.add_edge('clatd','sswap')
G.edge['clatd']['sswap']['write-read'] = '[open open][write read]'
G.edge['clatd']['sswap']['fill'] = 'red'
G.add_edge('clatd','sswap')
G.edge['clatd']['sswap']['write-read'] = '[open open][write read][append read]'
G.add_edge('clatd','s_system_app')
G.edge['clatd']['s_system_app']['write-read'] = '[write read][setopt getopt][open open][open open][append read]'
G.add_edge('clatd','s_system_app')
G.edge['clatd']['s_system_app']['write-read'] = '[write read][setopt getopt][open open][open open][append read][write read]'
G.edge['clatd']['s_system_app']['fill'] = 'red'
G.add_edge('clatd','s_system_app')
G.edge['clatd']['s_system_app']['write-read'] = '[write read][setopt getopt][open open][open open][append read][write read][append read]'
G.add_edge('clatd','system_app')
G.edge['clatd']['system_app']['write-read'] = '[write read][setopt getopt][open open][append read]'
G.add_edge('clatd','system_server')
G.edge['clatd']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][write read][setopt getopt][open open][write read]'
G.edge['clatd']['system_server']['fill'] = 'red'
G.add_edge('clatd','system_server')
G.edge['clatd']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][write read][setopt getopt][open open][write read][append read]'
G.add_edge('clatd','vold')
G.edge['clatd']['vold']['write-read'] = '[write read]'
G.edge['clatd']['vold']['fill'] = 'red'
G.add_edge('clatd','zygote')
G.edge['clatd']['zygote']['write-read'] = '[write read]'
G.edge['clatd']['zygote']['fill'] = 'red'
G.add_edge('domain','bluetooth')
G.edge['domain']['bluetooth']['write-read'] = '[open open][write read][append read][add_name search][remove_name search][open open]'
G.add_edge('domain','charon')
G.edge['domain']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('domain','clatd')
G.edge['domain']['clatd']['write-read'] = '[add_name search][add_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('domain','ime_app')
G.edge['domain']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open]'
G.add_edge('domain','init_shell')
G.edge['domain']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][setattr getattr][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][add_name search][remove_name search][open open]'
G.add_edge('domain','install_recovery')
G.edge['domain']['install_recovery']['write-read'] = '[open open]'
G.add_edge('domain','netmgrd')
G.edge['domain']['netmgrd']['write-read'] = '[add_name search][add_name search][remove_name search][open open][write read][append read][write read][open open][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('domain','rild')
G.edge['domain']['rild']['write-read'] = '[write read][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][write read][append read][open open][write read][append read][open open]'
G.add_edge('domain','sswap')
G.edge['domain']['sswap']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('domain','s_system_app')
G.edge['domain']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][add_name search][remove_name search][open open][write read][append read][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][setattr getattr][write read][append read][open open][write read][append read][open open]'
G.add_edge('domain','s_system_app')
G.edge['domain']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][add_name search][remove_name search][open open][write read][append read][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][setattr getattr][write read][append read][open open][write read][append read][open open][open open]'
G.add_edge('domain','system_app')
G.edge['domain']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][add_name search][remove_name search][open open][write read][append read][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open]'
G.add_edge('domain','system_server')
G.edge['domain']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][add_name search][remove_name search][open open][write read][append read][setattr getattr][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][add_name search][remove_name search][setattr getattr][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('domain','bluetooth')
G.edge['domain']['bluetooth']['write-read'] = '[open open][write read][append read][add_name search][remove_name search][open open][append read]'
G.add_edge('domain','charon')
G.edge['domain']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['domain']['charon']['fill'] = 'red'
G.add_edge('domain','charon')
G.edge['domain']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('domain','clatd')
G.edge['domain']['clatd']['write-read'] = '[add_name search][add_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['domain']['clatd']['fill'] = 'red'
G.add_edge('domain','clatd')
G.edge['domain']['clatd']['write-read'] = '[add_name search][add_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('domain','debuggerd')
G.edge['domain']['debuggerd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][add_name search][remove_name search][open open][write read][append read][write read]'
G.edge['domain']['debuggerd']['fill'] = 'red'
G.add_edge('domain','dhcp')
G.edge['domain']['dhcp']['write-read'] = '[write read][add_name search][add_name search][write read][write read]'
G.edge['domain']['dhcp']['fill'] = 'red'
G.add_edge('domain','ime_app')
G.edge['domain']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][append read]'
G.add_edge('domain','init_shell')
G.edge['domain']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][setattr getattr][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][add_name search][remove_name search][open open][write read]'
G.edge['domain']['init_shell']['fill'] = 'red'
G.add_edge('domain','init_shell')
G.edge['domain']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][setattr getattr][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('domain','install_recovery')
G.edge['domain']['install_recovery']['write-read'] = '[open open][write read]'
G.edge['domain']['install_recovery']['fill'] = 'red'
G.add_edge('domain','install_recovery')
G.edge['domain']['install_recovery']['write-read'] = '[open open][write read][append read]'
G.add_edge('domain','mediaserver')
G.edge['domain']['mediaserver']['write-read'] = '[setattr getattr][add_name search][remove_name search][write read][open open][write read][append read][write read]'
G.edge['domain']['mediaserver']['fill'] = 'red'
G.add_edge('domain','msm_irqbalanced')
G.edge['domain']['msm_irqbalanced']['write-read'] = '[add_name search][add_name search][write read]'
G.edge['domain']['msm_irqbalanced']['fill'] = 'red'
G.add_edge('domain','netmgrd')
G.edge['domain']['netmgrd']['write-read'] = '[add_name search][add_name search][remove_name search][open open][write read][append read][write read][open open][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['domain']['netmgrd']['fill'] = 'red'
G.add_edge('domain','netmgrd')
G.edge['domain']['netmgrd']['write-read'] = '[add_name search][add_name search][remove_name search][open open][write read][append read][write read][open open][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('domain','perfd')
G.edge['domain']['perfd']['write-read'] = '[write read][write read]'
G.edge['domain']['perfd']['fill'] = 'red'
G.add_edge('domain','rild')
G.edge['domain']['rild']['write-read'] = '[write read][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][write read][append read][open open][write read][append read][open open][write read]'
G.edge['domain']['rild']['fill'] = 'red'
G.add_edge('domain','rild')
G.edge['domain']['rild']['write-read'] = '[write read][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][write read][append read][open open][write read][append read][open open][write read][append read]'
G.add_edge('domain','rtcc')
G.edge['domain']['rtcc']['write-read'] = '[setattr getattr][add_name search][remove_name search][setattr getattr][write read][write read]'
G.edge['domain']['rtcc']['fill'] = 'red'
G.add_edge('domain','sswap')
G.edge['domain']['sswap']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['domain']['sswap']['fill'] = 'red'
G.add_edge('domain','sswap')
G.edge['domain']['sswap']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('domain','s_system_app')
G.edge['domain']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][add_name search][remove_name search][open open][write read][append read][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][setattr getattr][write read][append read][open open][write read][append read][open open][open open][append read]'
G.add_edge('domain','s_system_app')
G.edge['domain']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][add_name search][remove_name search][open open][write read][append read][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][setattr getattr][write read][append read][open open][write read][append read][open open][open open][append read][write read]'
G.edge['domain']['s_system_app']['fill'] = 'red'
G.add_edge('domain','s_system_app')
G.edge['domain']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][add_name search][remove_name search][open open][write read][append read][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][setattr getattr][write read][append read][open open][write read][append read][open open][open open][append read][write read][append read]'
G.add_edge('domain','system_app')
G.edge['domain']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][add_name search][remove_name search][open open][write read][append read][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][append read]'
G.add_edge('domain','system_server')
G.edge['domain']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][add_name search][remove_name search][open open][write read][append read][setattr getattr][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][add_name search][remove_name search][setattr getattr][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['domain']['system_server']['fill'] = 'red'
G.add_edge('domain','system_server')
G.edge['domain']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][add_name search][remove_name search][open open][write read][append read][setattr getattr][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][add_name search][remove_name search][setattr getattr][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('domain','vold')
G.edge['domain']['vold']['write-read'] = '[setattr getattr][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][write read]'
G.edge['domain']['vold']['fill'] = 'red'
G.add_edge('domain','zygote')
G.edge['domain']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][setattr getattr][add_name search][remove_name search][write read][setattr getattr][add_name search][remove_name search][write read]'
G.edge['domain']['zygote']['fill'] = 'red'
G.add_edge('sswap','bluetooth')
G.edge['sswap']['bluetooth']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('sswap','charon')
G.edge['sswap']['charon']['write-read'] = '[open open]'
G.add_edge('sswap','clatd')
G.edge['sswap']['clatd']['write-read'] = '[open open]'
G.add_edge('sswap','ime_app')
G.edge['sswap']['ime_app']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('sswap','init_shell')
G.edge['sswap']['init_shell']['write-read'] = '[open open][write read][add_name search][remove_name search][open open]'
G.add_edge('sswap','install_recovery')
G.edge['sswap']['install_recovery']['write-read'] = '[open open]'
G.add_edge('sswap','netmgrd')
G.edge['sswap']['netmgrd']['write-read'] = '[open open]'
G.add_edge('sswap','rild')
G.edge['sswap']['rild']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('sswap','sswap')
G.edge['sswap']['sswap']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('sswap','s_system_app')
G.edge['sswap']['s_system_app']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('sswap','s_system_app')
G.edge['sswap']['s_system_app']['write-read'] = '[open open][write read][append read][open open][open open]'
G.add_edge('sswap','system_app')
G.edge['sswap']['system_app']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('sswap','system_server')
G.edge['sswap']['system_server']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('sswap','bluetooth')
G.edge['sswap']['bluetooth']['write-read'] = '[open open][write read][append read][open open][append read]'
G.add_edge('sswap','charon')
G.edge['sswap']['charon']['write-read'] = '[open open][write read]'
G.edge['sswap']['charon']['fill'] = 'red'
G.add_edge('sswap','charon')
G.edge['sswap']['charon']['write-read'] = '[open open][write read][append read]'
G.add_edge('sswap','clatd')
G.edge['sswap']['clatd']['write-read'] = '[open open][write read]'
G.edge['sswap']['clatd']['fill'] = 'red'
G.add_edge('sswap','clatd')
G.edge['sswap']['clatd']['write-read'] = '[open open][write read][append read]'
G.add_edge('sswap','debuggerd')
G.edge['sswap']['debuggerd']['write-read'] = '[open open][write read][append read][write read]'
G.edge['sswap']['debuggerd']['fill'] = 'red'
G.add_edge('sswap','dhcp')
G.edge['sswap']['dhcp']['write-read'] = '[write read]'
G.edge['sswap']['dhcp']['fill'] = 'red'
G.add_edge('sswap','ime_app')
G.edge['sswap']['ime_app']['write-read'] = '[open open][write read][append read][open open][append read]'
G.add_edge('sswap','init_shell')
G.edge['sswap']['init_shell']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['sswap']['init_shell']['fill'] = 'red'
G.add_edge('sswap','init_shell')
G.edge['sswap']['init_shell']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('sswap','install_recovery')
G.edge['sswap']['install_recovery']['write-read'] = '[open open][write read]'
G.edge['sswap']['install_recovery']['fill'] = 'red'
G.add_edge('sswap','install_recovery')
G.edge['sswap']['install_recovery']['write-read'] = '[open open][write read][append read]'
G.add_edge('sswap','mediaserver')
G.edge['sswap']['mediaserver']['write-read'] = '[open open][write read][append read][write read]'
G.edge['sswap']['mediaserver']['fill'] = 'red'
G.add_edge('sswap','msm_irqbalanced')
G.edge['sswap']['msm_irqbalanced']['write-read'] = '[write read]'
G.edge['sswap']['msm_irqbalanced']['fill'] = 'red'
G.add_edge('sswap','netmgrd')
G.edge['sswap']['netmgrd']['write-read'] = '[open open][write read]'
G.edge['sswap']['netmgrd']['fill'] = 'red'
G.add_edge('sswap','netmgrd')
G.edge['sswap']['netmgrd']['write-read'] = '[open open][write read][append read]'
G.add_edge('sswap','perfd')
G.edge['sswap']['perfd']['write-read'] = '[write read]'
G.edge['sswap']['perfd']['fill'] = 'red'
G.add_edge('sswap','rild')
G.edge['sswap']['rild']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['sswap']['rild']['fill'] = 'red'
G.add_edge('sswap','rild')
G.edge['sswap']['rild']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('sswap','rtcc')
G.edge['sswap']['rtcc']['write-read'] = '[write read]'
G.edge['sswap']['rtcc']['fill'] = 'red'
G.add_edge('sswap','sswap')
G.edge['sswap']['sswap']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read]'
G.edge['sswap']['sswap']['fill'] = 'red'
G.add_edge('sswap','sswap')
G.edge['sswap']['sswap']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][append read]'
G.add_edge('sswap','s_system_app')
G.edge['sswap']['s_system_app']['write-read'] = '[open open][write read][append read][open open][open open][append read]'
G.add_edge('sswap','s_system_app')
G.edge['sswap']['s_system_app']['write-read'] = '[open open][write read][append read][open open][open open][append read][write read]'
G.edge['sswap']['s_system_app']['fill'] = 'red'
G.add_edge('sswap','s_system_app')
G.edge['sswap']['s_system_app']['write-read'] = '[open open][write read][append read][open open][open open][append read][write read][append read]'
G.add_edge('sswap','system_app')
G.edge['sswap']['system_app']['write-read'] = '[open open][write read][append read][open open][append read]'
G.add_edge('sswap','system_server')
G.edge['sswap']['system_server']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['sswap']['system_server']['fill'] = 'red'
G.add_edge('sswap','system_server')
G.edge['sswap']['system_server']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('sswap','vold')
G.edge['sswap']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read]'
G.edge['sswap']['vold']['fill'] = 'red'
G.add_edge('sswap','zygote')
G.edge['sswap']['zygote']['write-read'] = '[write read]'
G.edge['sswap']['zygote']['fill'] = 'red'
app = Viewer(G)
app.mainloop()