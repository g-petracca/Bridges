import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('actlmand','actlmand')
G.edge['actlmand']['actlmand']['write-read'] = '[open open][add_name search][remove_name search][write read][open open]'
G.add_edge('actlmand','flash_recovery')
G.edge['actlmand']['flash_recovery']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read][add_name search][open open]'
G.add_edge('actlmand','install_recovery')
G.edge['actlmand']['install_recovery']['write-read'] = '[open open]'
G.add_edge('actlmand','kernel')
G.edge['actlmand']['kernel']['write-read'] = '[open open]'
G.add_edge('actlmand','kernel')
G.edge['actlmand']['kernel']['write-read'] = '[open open][open open]'
G.add_edge('actlmand','s_system_app')
G.edge['actlmand']['s_system_app']['write-read'] = '[open open][add_name search][remove_name search][open open]'
G.add_edge('actlmand','syscope_app')
G.edge['actlmand']['syscope_app']['write-read'] = '[open open][add_name search][remove_name search][open open]'
G.add_edge('actlmand','uncrypt')
G.edge['actlmand']['uncrypt']['write-read'] = '[open open]'
G.add_edge('actlmand','vold')
G.edge['actlmand']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('actlmand','kernel')
G.edge['actlmand']['kernel']['write-read'] = '[open open][open open][setattr getattr]'
G.add_edge('actlmand','vold')
G.edge['actlmand']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('actlmand','actlmand')
G.edge['actlmand']['actlmand']['write-read'] = '[open open][add_name search][remove_name search][write read][open open][write read]'
G.edge['actlmand']['actlmand']['fill'] = 'red'
G.add_edge('actlmand','actlmand')
G.edge['actlmand']['actlmand']['write-read'] = '[open open][add_name search][remove_name search][write read][open open][write read][append read]'
G.add_edge('actlmand','flash_recovery')
G.edge['actlmand']['flash_recovery']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read][add_name search][open open][write read]'
G.edge['actlmand']['flash_recovery']['fill'] = 'red'
G.add_edge('actlmand','flash_recovery')
G.edge['actlmand']['flash_recovery']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read][add_name search][open open][write read][append read]'
G.add_edge('actlmand','ime_app')
G.edge['actlmand']['ime_app']['write-read'] = '[append read]'
G.add_edge('actlmand','install_recovery')
G.edge['actlmand']['install_recovery']['write-read'] = '[open open][write read]'
G.edge['actlmand']['install_recovery']['fill'] = 'red'
G.add_edge('actlmand','install_recovery')
G.edge['actlmand']['install_recovery']['write-read'] = '[open open][write read][append read]'
G.add_edge('actlmand','kernel')
G.edge['actlmand']['kernel']['write-read'] = '[open open][open open][setattr getattr][write read]'
G.edge['actlmand']['kernel']['fill'] = 'red'
G.add_edge('actlmand','kernel')
G.edge['actlmand']['kernel']['write-read'] = '[open open][open open][setattr getattr][write read][append read]'
G.add_edge('actlmand','kernel')
G.edge['actlmand']['kernel']['write-read'] = '[open open][open open][setattr getattr][write read][append read][write read]'
G.edge['actlmand']['kernel']['fill'] = 'red'
G.add_edge('actlmand','kernel')
G.edge['actlmand']['kernel']['write-read'] = '[open open][open open][setattr getattr][write read][append read][write read][append read]'
G.add_edge('actlmand','s_system_app')
G.edge['actlmand']['s_system_app']['write-read'] = '[open open][add_name search][remove_name search][open open][append read]'
G.add_edge('actlmand','s_system_app')
G.edge['actlmand']['s_system_app']['write-read'] = '[open open][add_name search][remove_name search][open open][append read][write read]'
G.edge['actlmand']['s_system_app']['fill'] = 'red'
G.add_edge('actlmand','s_system_app')
G.edge['actlmand']['s_system_app']['write-read'] = '[open open][add_name search][remove_name search][open open][append read][write read][append read]'
G.add_edge('actlmand','syscope_app')
G.edge['actlmand']['syscope_app']['write-read'] = '[open open][add_name search][remove_name search][open open][write read]'
G.edge['actlmand']['syscope_app']['fill'] = 'red'
G.add_edge('actlmand','syscope_app')
G.edge['actlmand']['syscope_app']['write-read'] = '[open open][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('actlmand','system_app')
G.edge['actlmand']['system_app']['write-read'] = '[open open][add_name search][remove_name search][append read]'
G.add_edge('actlmand','uncrypt')
G.edge['actlmand']['uncrypt']['write-read'] = '[open open][write read]'
G.edge['actlmand']['uncrypt']['fill'] = 'red'
G.add_edge('actlmand','uncrypt')
G.edge['actlmand']['uncrypt']['write-read'] = '[open open][write read][append read]'
G.add_edge('actlmand','vold')
G.edge['actlmand']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['actlmand']['vold']['fill'] = 'red'
G.add_edge('actlmand','vold')
G.edge['actlmand']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('carrier_app','kernel')
G.edge['carrier_app']['kernel']['write-read'] = '[setattr getattr]'
G.add_edge('carrier_app','vold')
G.edge['carrier_app']['vold']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('filtered_google_app','kernel')
G.edge['filtered_google_app']['kernel']['write-read'] = '[setattr getattr]'
G.add_edge('filtered_google_app','vold')
G.edge['filtered_google_app']['vold']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('filtered_untrusted_app','kernel')
G.edge['filtered_untrusted_app']['kernel']['write-read'] = '[setattr getattr]'
G.add_edge('filtered_untrusted_app','vold')
G.edge['filtered_untrusted_app']['vold']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('flash_recovery','actlmand')
G.edge['flash_recovery']['actlmand']['write-read'] = '[open open][write read][add_name search][remove_name search][open open]'
G.add_edge('flash_recovery','flash_recovery')
G.edge['flash_recovery']['flash_recovery']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][open open]'
G.add_edge('flash_recovery','install_recovery')
G.edge['flash_recovery']['install_recovery']['write-read'] = '[open open]'
G.add_edge('flash_recovery','kernel')
G.edge['flash_recovery']['kernel']['write-read'] = '[open open]'
G.add_edge('flash_recovery','kernel')
G.edge['flash_recovery']['kernel']['write-read'] = '[open open][open open]'
G.add_edge('flash_recovery','s_system_app')
G.edge['flash_recovery']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('flash_recovery','syscope_app')
G.edge['flash_recovery']['syscope_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('flash_recovery','uncrypt')
G.edge['flash_recovery']['uncrypt']['write-read'] = '[open open]'
G.add_edge('flash_recovery','vold')
G.edge['flash_recovery']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('flash_recovery','kernel')
G.edge['flash_recovery']['kernel']['write-read'] = '[open open][open open][setattr getattr]'
G.add_edge('flash_recovery','vold')
G.edge['flash_recovery']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('flash_recovery','actlmand')
G.edge['flash_recovery']['actlmand']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['flash_recovery']['actlmand']['fill'] = 'red'
G.add_edge('flash_recovery','actlmand')
G.edge['flash_recovery']['actlmand']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('flash_recovery','flash_recovery')
G.edge['flash_recovery']['flash_recovery']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][open open][write read]'
G.edge['flash_recovery']['flash_recovery']['fill'] = 'red'
G.add_edge('flash_recovery','flash_recovery')
G.edge['flash_recovery']['flash_recovery']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][open open][write read][append read]'
G.add_edge('flash_recovery','ime_app')
G.edge['flash_recovery']['ime_app']['write-read'] = '[append read]'
G.add_edge('flash_recovery','install_recovery')
G.edge['flash_recovery']['install_recovery']['write-read'] = '[open open][write read]'
G.edge['flash_recovery']['install_recovery']['fill'] = 'red'
G.add_edge('flash_recovery','install_recovery')
G.edge['flash_recovery']['install_recovery']['write-read'] = '[open open][write read][append read]'
G.add_edge('flash_recovery','kernel')
G.edge['flash_recovery']['kernel']['write-read'] = '[open open][open open][setattr getattr][write read]'
G.edge['flash_recovery']['kernel']['fill'] = 'red'
G.add_edge('flash_recovery','kernel')
G.edge['flash_recovery']['kernel']['write-read'] = '[open open][open open][setattr getattr][write read][append read]'
G.add_edge('flash_recovery','kernel')
G.edge['flash_recovery']['kernel']['write-read'] = '[open open][open open][setattr getattr][write read][append read][write read]'
G.edge['flash_recovery']['kernel']['fill'] = 'red'
G.add_edge('flash_recovery','kernel')
G.edge['flash_recovery']['kernel']['write-read'] = '[open open][open open][setattr getattr][write read][append read][write read][append read]'
G.add_edge('flash_recovery','s_system_app')
G.edge['flash_recovery']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][append read]'
G.add_edge('flash_recovery','s_system_app')
G.edge['flash_recovery']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][append read][write read]'
G.edge['flash_recovery']['s_system_app']['fill'] = 'red'
G.add_edge('flash_recovery','s_system_app')
G.edge['flash_recovery']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][append read][write read][append read]'
G.add_edge('flash_recovery','syscope_app')
G.edge['flash_recovery']['syscope_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['flash_recovery']['syscope_app']['fill'] = 'red'
G.add_edge('flash_recovery','syscope_app')
G.edge['flash_recovery']['syscope_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('flash_recovery','system_app')
G.edge['flash_recovery']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][append read]'
G.add_edge('flash_recovery','uncrypt')
G.edge['flash_recovery']['uncrypt']['write-read'] = '[open open][write read]'
G.edge['flash_recovery']['uncrypt']['fill'] = 'red'
G.add_edge('flash_recovery','uncrypt')
G.edge['flash_recovery']['uncrypt']['write-read'] = '[open open][write read][append read]'
G.add_edge('flash_recovery','vold')
G.edge['flash_recovery']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['flash_recovery']['vold']['fill'] = 'red'
G.add_edge('flash_recovery','vold')
G.edge['flash_recovery']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('gad_untrusted_app','kernel')
G.edge['gad_untrusted_app']['kernel']['write-read'] = '[setattr getattr]'
G.add_edge('gad_untrusted_app','vold')
G.edge['gad_untrusted_app']['vold']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('ime_app','kernel')
G.edge['ime_app']['kernel']['write-read'] = '[setattr getattr]'
G.add_edge('ime_app','vold')
G.edge['ime_app']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('install_recovery','actlmand')
G.edge['install_recovery']['actlmand']['write-read'] = '[open open]'
G.add_edge('install_recovery','flash_recovery')
G.edge['install_recovery']['flash_recovery']['write-read'] = '[add_name search][remove_name search][open open]'
G.add_edge('install_recovery','install_recovery')
G.edge['install_recovery']['install_recovery']['write-read'] = '[write read][open open]'
G.add_edge('install_recovery','kernel')
G.edge['install_recovery']['kernel']['write-read'] = '[open open]'
G.add_edge('install_recovery','kernel')
G.edge['install_recovery']['kernel']['write-read'] = '[open open][open open]'
G.add_edge('install_recovery','s_system_app')
G.edge['install_recovery']['s_system_app']['write-read'] = '[open open]'
G.add_edge('install_recovery','syscope_app')
G.edge['install_recovery']['syscope_app']['write-read'] = '[open open]'
G.add_edge('install_recovery','uncrypt')
G.edge['install_recovery']['uncrypt']['write-read'] = '[open open]'
G.add_edge('install_recovery','vold')
G.edge['install_recovery']['vold']['write-read'] = '[add_name search][remove_name search][open open]'
G.add_edge('install_recovery','kernel')
G.edge['install_recovery']['kernel']['write-read'] = '[open open][open open][setattr getattr]'
G.add_edge('install_recovery','vold')
G.edge['install_recovery']['vold']['write-read'] = '[add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('install_recovery','actlmand')
G.edge['install_recovery']['actlmand']['write-read'] = '[open open][write read]'
G.edge['install_recovery']['actlmand']['fill'] = 'red'
G.add_edge('install_recovery','actlmand')
G.edge['install_recovery']['actlmand']['write-read'] = '[open open][write read][append read]'
G.add_edge('install_recovery','flash_recovery')
G.edge['install_recovery']['flash_recovery']['write-read'] = '[add_name search][remove_name search][open open][write read]'
G.edge['install_recovery']['flash_recovery']['fill'] = 'red'
G.add_edge('install_recovery','flash_recovery')
G.edge['install_recovery']['flash_recovery']['write-read'] = '[add_name search][remove_name search][open open][write read][append read]'
G.add_edge('install_recovery','ime_app')
G.edge['install_recovery']['ime_app']['write-read'] = '[append read]'
G.add_edge('install_recovery','install_recovery')
G.edge['install_recovery']['install_recovery']['write-read'] = '[write read][open open][write read]'
G.edge['install_recovery']['install_recovery']['fill'] = 'red'
G.add_edge('install_recovery','install_recovery')
G.edge['install_recovery']['install_recovery']['write-read'] = '[write read][open open][write read][append read]'
G.add_edge('install_recovery','kernel')
G.edge['install_recovery']['kernel']['write-read'] = '[open open][open open][setattr getattr][write read]'
G.edge['install_recovery']['kernel']['fill'] = 'red'
G.add_edge('install_recovery','kernel')
G.edge['install_recovery']['kernel']['write-read'] = '[open open][open open][setattr getattr][write read][append read]'
G.add_edge('install_recovery','kernel')
G.edge['install_recovery']['kernel']['write-read'] = '[open open][open open][setattr getattr][write read][append read][write read]'
G.edge['install_recovery']['kernel']['fill'] = 'red'
G.add_edge('install_recovery','kernel')
G.edge['install_recovery']['kernel']['write-read'] = '[open open][open open][setattr getattr][write read][append read][write read][append read]'
G.add_edge('install_recovery','s_system_app')
G.edge['install_recovery']['s_system_app']['write-read'] = '[open open][append read]'
G.add_edge('install_recovery','s_system_app')
G.edge['install_recovery']['s_system_app']['write-read'] = '[open open][append read][write read]'
G.edge['install_recovery']['s_system_app']['fill'] = 'red'
G.add_edge('install_recovery','s_system_app')
G.edge['install_recovery']['s_system_app']['write-read'] = '[open open][append read][write read][append read]'
G.add_edge('install_recovery','syscope_app')
G.edge['install_recovery']['syscope_app']['write-read'] = '[open open][write read]'
G.edge['install_recovery']['syscope_app']['fill'] = 'red'
G.add_edge('install_recovery','syscope_app')
G.edge['install_recovery']['syscope_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('install_recovery','system_app')
G.edge['install_recovery']['system_app']['write-read'] = '[append read]'
G.add_edge('install_recovery','uncrypt')
G.edge['install_recovery']['uncrypt']['write-read'] = '[open open][write read]'
G.edge['install_recovery']['uncrypt']['fill'] = 'red'
G.add_edge('install_recovery','uncrypt')
G.edge['install_recovery']['uncrypt']['write-read'] = '[open open][write read][append read]'
G.add_edge('install_recovery','vold')
G.edge['install_recovery']['vold']['write-read'] = '[add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['install_recovery']['vold']['fill'] = 'red'
G.add_edge('install_recovery','vold')
G.edge['install_recovery']['vold']['write-read'] = '[add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('irm_app','kernel')
G.edge['irm_app']['kernel']['write-read'] = '[setattr getattr]'
G.add_edge('irm_app','vold')
G.edge['irm_app']['vold']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('kernel','actlmand')
G.edge['kernel']['actlmand']['write-read'] = '[open open]'
G.add_edge('kernel','flash_recovery')
G.edge['kernel']['flash_recovery']['write-read'] = '[open open]'
G.add_edge('kernel','install_recovery')
G.edge['kernel']['install_recovery']['write-read'] = '[open open]'
G.add_edge('kernel','kernel')
G.edge['kernel']['kernel']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('kernel','kernel')
G.edge['kernel']['kernel']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open]'
G.add_edge('kernel','s_system_app')
G.edge['kernel']['s_system_app']['write-read'] = '[open open]'
G.add_edge('kernel','syscope_app')
G.edge['kernel']['syscope_app']['write-read'] = '[open open]'
G.add_edge('kernel','uncrypt')
G.edge['kernel']['uncrypt']['write-read'] = '[open open]'
G.add_edge('kernel','vold')
G.edge['kernel']['vold']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('kernel','kernel')
G.edge['kernel']['kernel']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr]'
G.add_edge('kernel','vold')
G.edge['kernel']['vold']['write-read'] = '[open open][write read][append read][open open][setattr getattr]'
G.add_edge('kernel','actlmand')
G.edge['kernel']['actlmand']['write-read'] = '[open open][write read]'
G.edge['kernel']['actlmand']['fill'] = 'red'
G.add_edge('kernel','actlmand')
G.edge['kernel']['actlmand']['write-read'] = '[open open][write read][append read]'
G.add_edge('kernel','flash_recovery')
G.edge['kernel']['flash_recovery']['write-read'] = '[open open][write read]'
G.edge['kernel']['flash_recovery']['fill'] = 'red'
G.add_edge('kernel','flash_recovery')
G.edge['kernel']['flash_recovery']['write-read'] = '[open open][write read][append read]'
G.add_edge('kernel','ime_app')
G.edge['kernel']['ime_app']['write-read'] = '[append read]'
G.add_edge('kernel','install_recovery')
G.edge['kernel']['install_recovery']['write-read'] = '[open open][write read]'
G.edge['kernel']['install_recovery']['fill'] = 'red'
G.add_edge('kernel','install_recovery')
G.edge['kernel']['install_recovery']['write-read'] = '[open open][write read][append read]'
G.add_edge('kernel','kernel')
G.edge['kernel']['kernel']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read]'
G.edge['kernel']['kernel']['fill'] = 'red'
G.add_edge('kernel','kernel')
G.edge['kernel']['kernel']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read]'
G.add_edge('kernel','kernel')
G.edge['kernel']['kernel']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read]'
G.edge['kernel']['kernel']['fill'] = 'red'
G.add_edge('kernel','kernel')
G.edge['kernel']['kernel']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read]'
G.add_edge('kernel','s_system_app')
G.edge['kernel']['s_system_app']['write-read'] = '[open open][append read]'
G.add_edge('kernel','s_system_app')
G.edge['kernel']['s_system_app']['write-read'] = '[open open][append read][write read]'
G.edge['kernel']['s_system_app']['fill'] = 'red'
G.add_edge('kernel','s_system_app')
G.edge['kernel']['s_system_app']['write-read'] = '[open open][append read][write read][append read]'
G.add_edge('kernel','syscope_app')
G.edge['kernel']['syscope_app']['write-read'] = '[open open][write read]'
G.edge['kernel']['syscope_app']['fill'] = 'red'
G.add_edge('kernel','syscope_app')
G.edge['kernel']['syscope_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('kernel','system_app')
G.edge['kernel']['system_app']['write-read'] = '[append read]'
G.add_edge('kernel','uncrypt')
G.edge['kernel']['uncrypt']['write-read'] = '[open open][write read]'
G.edge['kernel']['uncrypt']['fill'] = 'red'
G.add_edge('kernel','uncrypt')
G.edge['kernel']['uncrypt']['write-read'] = '[open open][write read][append read]'
G.add_edge('kernel','vold')
G.edge['kernel']['vold']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read]'
G.edge['kernel']['vold']['fill'] = 'red'
G.add_edge('kernel','vold')
G.edge['kernel']['vold']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('kernel','actlmand')
G.edge['kernel']['actlmand']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('kernel','flash_recovery')
G.edge['kernel']['flash_recovery']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('kernel','install_recovery')
G.edge['kernel']['install_recovery']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('kernel','kernel')
G.edge['kernel']['kernel']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open]'
G.add_edge('kernel','kernel')
G.edge['kernel']['kernel']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open]'
G.add_edge('kernel','s_system_app')
G.edge['kernel']['s_system_app']['write-read'] = '[open open][append read][write read][append read][open open]'
G.add_edge('kernel','syscope_app')
G.edge['kernel']['syscope_app']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('kernel','uncrypt')
G.edge['kernel']['uncrypt']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('kernel','vold')
G.edge['kernel']['vold']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('kernel','kernel')
G.edge['kernel']['kernel']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr]'
G.add_edge('kernel','vold')
G.edge['kernel']['vold']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('kernel','actlmand')
G.edge['kernel']['actlmand']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['kernel']['actlmand']['fill'] = 'red'
G.add_edge('kernel','actlmand')
G.edge['kernel']['actlmand']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('kernel','flash_recovery')
G.edge['kernel']['flash_recovery']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['kernel']['flash_recovery']['fill'] = 'red'
G.add_edge('kernel','flash_recovery')
G.edge['kernel']['flash_recovery']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('kernel','ime_app')
G.edge['kernel']['ime_app']['write-read'] = '[append read][append read]'
G.add_edge('kernel','install_recovery')
G.edge['kernel']['install_recovery']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['kernel']['install_recovery']['fill'] = 'red'
G.add_edge('kernel','install_recovery')
G.edge['kernel']['install_recovery']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('kernel','kernel')
G.edge['kernel']['kernel']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read]'
G.edge['kernel']['kernel']['fill'] = 'red'
G.add_edge('kernel','kernel')
G.edge['kernel']['kernel']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read]'
G.add_edge('kernel','kernel')
G.edge['kernel']['kernel']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read]'
G.edge['kernel']['kernel']['fill'] = 'red'
G.add_edge('kernel','kernel')
G.edge['kernel']['kernel']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read]'
G.add_edge('kernel','s_system_app')
G.edge['kernel']['s_system_app']['write-read'] = '[open open][append read][write read][append read][open open][append read]'
G.add_edge('kernel','s_system_app')
G.edge['kernel']['s_system_app']['write-read'] = '[open open][append read][write read][append read][open open][append read][write read]'
G.edge['kernel']['s_system_app']['fill'] = 'red'
G.add_edge('kernel','s_system_app')
G.edge['kernel']['s_system_app']['write-read'] = '[open open][append read][write read][append read][open open][append read][write read][append read]'
G.add_edge('kernel','syscope_app')
G.edge['kernel']['syscope_app']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['kernel']['syscope_app']['fill'] = 'red'
G.add_edge('kernel','syscope_app')
G.edge['kernel']['syscope_app']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('kernel','system_app')
G.edge['kernel']['system_app']['write-read'] = '[append read][append read]'
G.add_edge('kernel','uncrypt')
G.edge['kernel']['uncrypt']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['kernel']['uncrypt']['fill'] = 'red'
G.add_edge('kernel','uncrypt')
G.edge['kernel']['uncrypt']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('kernel','vold')
G.edge['kernel']['vold']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['kernel']['vold']['fill'] = 'red'
G.add_edge('kernel','vold')
G.edge['kernel']['vold']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('knox_untrusted_app','kernel')
G.edge['knox_untrusted_app']['kernel']['write-read'] = '[setattr getattr]'
G.add_edge('knox_untrusted_app','vold')
G.edge['knox_untrusted_app']['vold']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('llk_untrusted_app','kernel')
G.edge['llk_untrusted_app']['kernel']['write-read'] = '[setattr getattr]'
G.add_edge('llk_untrusted_app','vold')
G.edge['llk_untrusted_app']['vold']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('s_system_app','kernel')
G.edge['s_system_app']['kernel']['write-read'] = '[setattr getattr]'
G.add_edge('s_system_app','vold')
G.edge['s_system_app']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('s_system_app','actlmand')
G.edge['s_system_app']['actlmand']['write-read'] = '[open open][write read][add_name search][remove_name search][open open]'
G.add_edge('s_system_app','flash_recovery')
G.edge['s_system_app']['flash_recovery']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][open open]'
G.add_edge('s_system_app','install_recovery')
G.edge['s_system_app']['install_recovery']['write-read'] = '[open open]'
G.add_edge('s_system_app','kernel')
G.edge['s_system_app']['kernel']['write-read'] = '[setattr getattr][open open]'
G.add_edge('s_system_app','kernel')
G.edge['s_system_app']['kernel']['write-read'] = '[setattr getattr][open open][open open]'
G.add_edge('s_system_app','s_system_app')
G.edge['s_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('s_system_app','syscope_app')
G.edge['s_system_app']['syscope_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('s_system_app','uncrypt')
G.edge['s_system_app']['uncrypt']['write-read'] = '[open open]'
G.add_edge('s_system_app','vold')
G.edge['s_system_app']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][open open]'
G.add_edge('s_system_app','kernel')
G.edge['s_system_app']['kernel']['write-read'] = '[setattr getattr][open open][open open][setattr getattr]'
G.add_edge('s_system_app','vold')
G.edge['s_system_app']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr]'
G.add_edge('s_system_app','actlmand')
G.edge['s_system_app']['actlmand']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['s_system_app']['actlmand']['fill'] = 'red'
G.add_edge('s_system_app','actlmand')
G.edge['s_system_app']['actlmand']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('s_system_app','flash_recovery')
G.edge['s_system_app']['flash_recovery']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][open open][write read]'
G.edge['s_system_app']['flash_recovery']['fill'] = 'red'
G.add_edge('s_system_app','flash_recovery')
G.edge['s_system_app']['flash_recovery']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][open open][write read][append read]'
G.add_edge('s_system_app','ime_app')
G.edge['s_system_app']['ime_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][append read]'
G.add_edge('s_system_app','install_recovery')
G.edge['s_system_app']['install_recovery']['write-read'] = '[open open][write read]'
G.edge['s_system_app']['install_recovery']['fill'] = 'red'
G.add_edge('s_system_app','install_recovery')
G.edge['s_system_app']['install_recovery']['write-read'] = '[open open][write read][append read]'
G.add_edge('s_system_app','kernel')
G.edge['s_system_app']['kernel']['write-read'] = '[setattr getattr][open open][open open][setattr getattr][write read]'
G.edge['s_system_app']['kernel']['fill'] = 'red'
G.add_edge('s_system_app','kernel')
G.edge['s_system_app']['kernel']['write-read'] = '[setattr getattr][open open][open open][setattr getattr][write read][append read]'
G.add_edge('s_system_app','kernel')
G.edge['s_system_app']['kernel']['write-read'] = '[setattr getattr][open open][open open][setattr getattr][write read][append read][write read]'
G.edge['s_system_app']['kernel']['fill'] = 'red'
G.add_edge('s_system_app','kernel')
G.edge['s_system_app']['kernel']['write-read'] = '[setattr getattr][open open][open open][setattr getattr][write read][append read][write read][append read]'
G.add_edge('s_system_app','s_system_app')
G.edge['s_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][write read][append read][open open][write read][append read][open open][append read]'
G.add_edge('s_system_app','s_system_app')
G.edge['s_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][write read][append read][open open][write read][append read][open open][append read][write read]'
G.edge['s_system_app']['s_system_app']['fill'] = 'red'
G.add_edge('s_system_app','s_system_app')
G.edge['s_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][write read][append read][open open][write read][append read][open open][append read][write read][append read]'
G.add_edge('s_system_app','syscope_app')
G.edge['s_system_app']['syscope_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['s_system_app']['syscope_app']['fill'] = 'red'
G.add_edge('s_system_app','syscope_app')
G.edge['s_system_app']['syscope_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('s_system_app','system_app')
G.edge['s_system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][write read][append read][open open][write read][append read][append read]'
G.add_edge('s_system_app','uncrypt')
G.edge['s_system_app']['uncrypt']['write-read'] = '[open open][write read]'
G.edge['s_system_app']['uncrypt']['fill'] = 'red'
G.add_edge('s_system_app','uncrypt')
G.edge['s_system_app']['uncrypt']['write-read'] = '[open open][write read][append read]'
G.add_edge('s_system_app','vold')
G.edge['s_system_app']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read]'
G.edge['s_system_app']['vold']['fill'] = 'red'
G.add_edge('s_system_app','vold')
G.edge['s_system_app']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read]'
G.add_edge('system_app','kernel')
G.edge['system_app']['kernel']['write-read'] = '[setattr getattr]'
G.add_edge('system_app','vold')
G.edge['system_app']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('trustonicpartner_app','kernel')
G.edge['trustonicpartner_app']['kernel']['write-read'] = '[setattr getattr]'
G.add_edge('trustonicpartner_app','vold')
G.edge['trustonicpartner_app']['vold']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('umcagent_app','kernel')
G.edge['umcagent_app']['kernel']['write-read'] = '[setattr getattr]'
G.add_edge('umcagent_app','vold')
G.edge['umcagent_app']['vold']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('undefined_service','kernel')
G.edge['undefined_service']['kernel']['write-read'] = '[setattr getattr]'
G.add_edge('undefined_service','vold')
G.edge['undefined_service']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('untrusted_app','kernel')
G.edge['untrusted_app']['kernel']['write-read'] = '[setattr getattr]'
G.add_edge('untrusted_app','vold')
G.edge['untrusted_app']['vold']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('vold','actlmand')
G.edge['vold']['actlmand']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('vold','flash_recovery')
G.edge['vold']['flash_recovery']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('vold','install_recovery')
G.edge['vold']['install_recovery']['write-read'] = '[open open]'
G.add_edge('vold','kernel')
G.edge['vold']['kernel']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('vold','kernel')
G.edge['vold']['kernel']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open]'
G.add_edge('vold','s_system_app')
G.edge['vold']['s_system_app']['write-read'] = '[setattr getattr][setopt getopt][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('vold','syscope_app')
G.edge['vold']['syscope_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('vold','uncrypt')
G.edge['vold']['uncrypt']['write-read'] = '[open open]'
G.add_edge('vold','vold')
G.edge['vold']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][relabelto relabelfrom][relabelto relabelfrom][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('vold','kernel')
G.edge['vold']['kernel']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr]'
G.add_edge('vold','vold')
G.edge['vold']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][relabelto relabelfrom][relabelto relabelfrom][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('vold','actlmand')
G.edge['vold']['actlmand']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['vold']['actlmand']['fill'] = 'red'
G.add_edge('vold','actlmand')
G.edge['vold']['actlmand']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('vold','flash_recovery')
G.edge['vold']['flash_recovery']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['vold']['flash_recovery']['fill'] = 'red'
G.add_edge('vold','flash_recovery')
G.edge['vold']['flash_recovery']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('vold','ime_app')
G.edge['vold']['ime_app']['write-read'] = '[setattr getattr][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][append read]'
G.add_edge('vold','install_recovery')
G.edge['vold']['install_recovery']['write-read'] = '[open open][write read]'
G.edge['vold']['install_recovery']['fill'] = 'red'
G.add_edge('vold','install_recovery')
G.edge['vold']['install_recovery']['write-read'] = '[open open][write read][append read]'
G.add_edge('vold','kernel')
G.edge['vold']['kernel']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read]'
G.edge['vold']['kernel']['fill'] = 'red'
G.add_edge('vold','kernel')
G.edge['vold']['kernel']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read]'
G.add_edge('vold','kernel')
G.edge['vold']['kernel']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read]'
G.edge['vold']['kernel']['fill'] = 'red'
G.add_edge('vold','kernel')
G.edge['vold']['kernel']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read]'
G.add_edge('vold','s_system_app')
G.edge['vold']['s_system_app']['write-read'] = '[setattr getattr][setopt getopt][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][append read]'
G.add_edge('vold','s_system_app')
G.edge['vold']['s_system_app']['write-read'] = '[setattr getattr][setopt getopt][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][append read][write read]'
G.edge['vold']['s_system_app']['fill'] = 'red'
G.add_edge('vold','s_system_app')
G.edge['vold']['s_system_app']['write-read'] = '[setattr getattr][setopt getopt][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][append read][write read][append read]'
G.add_edge('vold','syscope_app')
G.edge['vold']['syscope_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['vold']['syscope_app']['fill'] = 'red'
G.add_edge('vold','syscope_app')
G.edge['vold']['syscope_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('vold','system_app')
G.edge['vold']['system_app']['write-read'] = '[setattr getattr][setopt getopt][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][append read]'
G.add_edge('vold','uncrypt')
G.edge['vold']['uncrypt']['write-read'] = '[open open][write read]'
G.edge['vold']['uncrypt']['fill'] = 'red'
G.add_edge('vold','uncrypt')
G.edge['vold']['uncrypt']['write-read'] = '[open open][write read][append read]'
G.add_edge('vold','vold')
G.edge['vold']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][relabelto relabelfrom][relabelto relabelfrom][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['vold']['vold']['fill'] = 'red'
G.add_edge('vold','vold')
G.edge['vold']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][relabelto relabelfrom][relabelto relabelfrom][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('vpn_untrusted_app','kernel')
G.edge['vpn_untrusted_app']['kernel']['write-read'] = '[setattr getattr]'
G.add_edge('vpn_untrusted_app','vold')
G.edge['vpn_untrusted_app']['vold']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
app = Viewer(G)
app.mainloop()