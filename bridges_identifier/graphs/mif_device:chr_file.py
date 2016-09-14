import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('cbd','cbd')
G.edge['cbd']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read][open open][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][write read][append read][open open]'
G.add_edge('cbd','debug_interface_proxy')
G.edge['cbd']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('cbd','diagexe')
G.edge['cbd']['diagexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('cbd','mlexe')
G.edge['cbd']['mlexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('cbd','radio')
G.edge['cbd']['radio']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open]'
G.add_edge('cbd','rild')
G.edge['cbd']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('cbd','smdexe')
G.edge['cbd']['smdexe']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('cbd','cbd')
G.edge['cbd']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read][open open][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][write read][append read][open open][write read]'
G.edge['cbd']['cbd']['fill'] = 'red'
G.add_edge('cbd','cbd')
G.edge['cbd']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read][open open][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][write read][append read][open open][write read][append read]'
G.add_edge('cbd','debug_interface_proxy')
G.edge['cbd']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['cbd']['debug_interface_proxy']['fill'] = 'red'
G.add_edge('cbd','debug_interface_proxy')
G.edge['cbd']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('cbd','diagexe')
G.edge['cbd']['diagexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['cbd']['diagexe']['fill'] = 'red'
G.add_edge('cbd','mlexe')
G.edge['cbd']['mlexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['cbd']['mlexe']['fill'] = 'red'
G.add_edge('cbd','mlexe')
G.edge['cbd']['mlexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('cbd','radio')
G.edge['cbd']['radio']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read]'
G.edge['cbd']['radio']['fill'] = 'red'
G.add_edge('cbd','radio')
G.edge['cbd']['radio']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read]'
G.add_edge('cbd','rild')
G.edge['cbd']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['cbd']['rild']['fill'] = 'red'
G.add_edge('cbd','rild')
G.edge['cbd']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('cbd','smdexe')
G.edge['cbd']['smdexe']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['cbd']['smdexe']['fill'] = 'red'
G.add_edge('cbd','smdexe')
G.edge['cbd']['smdexe']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('debug_interface_proxy','cbd')
G.edge['debug_interface_proxy']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('debug_interface_proxy','debug_interface_proxy')
G.edge['debug_interface_proxy']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('debug_interface_proxy','diagexe')
G.edge['debug_interface_proxy']['diagexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('debug_interface_proxy','mlexe')
G.edge['debug_interface_proxy']['mlexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('debug_interface_proxy','radio')
G.edge['debug_interface_proxy']['radio']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('debug_interface_proxy','rild')
G.edge['debug_interface_proxy']['rild']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('debug_interface_proxy','smdexe')
G.edge['debug_interface_proxy']['smdexe']['write-read'] = '[open open]'
G.add_edge('debug_interface_proxy','cbd')
G.edge['debug_interface_proxy']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['debug_interface_proxy']['cbd']['fill'] = 'red'
G.add_edge('debug_interface_proxy','cbd')
G.edge['debug_interface_proxy']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('debug_interface_proxy','debug_interface_proxy')
G.edge['debug_interface_proxy']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['debug_interface_proxy']['debug_interface_proxy']['fill'] = 'red'
G.add_edge('debug_interface_proxy','debug_interface_proxy')
G.edge['debug_interface_proxy']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('debug_interface_proxy','diagexe')
G.edge['debug_interface_proxy']['diagexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['debug_interface_proxy']['diagexe']['fill'] = 'red'
G.add_edge('debug_interface_proxy','mlexe')
G.edge['debug_interface_proxy']['mlexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['debug_interface_proxy']['mlexe']['fill'] = 'red'
G.add_edge('debug_interface_proxy','mlexe')
G.edge['debug_interface_proxy']['mlexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('debug_interface_proxy','radio')
G.edge['debug_interface_proxy']['radio']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read]'
G.edge['debug_interface_proxy']['radio']['fill'] = 'red'
G.add_edge('debug_interface_proxy','radio')
G.edge['debug_interface_proxy']['radio']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('debug_interface_proxy','rild')
G.edge['debug_interface_proxy']['rild']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['debug_interface_proxy']['rild']['fill'] = 'red'
G.add_edge('debug_interface_proxy','rild')
G.edge['debug_interface_proxy']['rild']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('debug_interface_proxy','smdexe')
G.edge['debug_interface_proxy']['smdexe']['write-read'] = '[open open][write read]'
G.edge['debug_interface_proxy']['smdexe']['fill'] = 'red'
G.add_edge('debug_interface_proxy','smdexe')
G.edge['debug_interface_proxy']['smdexe']['write-read'] = '[open open][write read][append read]'
G.add_edge('diagexe','cbd')
G.edge['diagexe']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open]'
G.add_edge('diagexe','debug_interface_proxy')
G.edge['diagexe']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('diagexe','diagexe')
G.edge['diagexe']['diagexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('diagexe','mlexe')
G.edge['diagexe']['mlexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('diagexe','radio')
G.edge['diagexe']['radio']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('diagexe','rild')
G.edge['diagexe']['rild']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('diagexe','smdexe')
G.edge['diagexe']['smdexe']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('diagexe','cbd')
G.edge['diagexe']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][write read]'
G.edge['diagexe']['cbd']['fill'] = 'red'
G.add_edge('diagexe','cbd')
G.edge['diagexe']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][write read][append read]'
G.add_edge('diagexe','debug_interface_proxy')
G.edge['diagexe']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['diagexe']['debug_interface_proxy']['fill'] = 'red'
G.add_edge('diagexe','debug_interface_proxy')
G.edge['diagexe']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('diagexe','diagexe')
G.edge['diagexe']['diagexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['diagexe']['diagexe']['fill'] = 'red'
G.add_edge('diagexe','mlexe')
G.edge['diagexe']['mlexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['diagexe']['mlexe']['fill'] = 'red'
G.add_edge('diagexe','mlexe')
G.edge['diagexe']['mlexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('diagexe','radio')
G.edge['diagexe']['radio']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['diagexe']['radio']['fill'] = 'red'
G.add_edge('diagexe','radio')
G.edge['diagexe']['radio']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('diagexe','rild')
G.edge['diagexe']['rild']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['diagexe']['rild']['fill'] = 'red'
G.add_edge('diagexe','rild')
G.edge['diagexe']['rild']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('diagexe','smdexe')
G.edge['diagexe']['smdexe']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['diagexe']['smdexe']['fill'] = 'red'
G.add_edge('diagexe','smdexe')
G.edge['diagexe']['smdexe']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('mlexe','cbd')
G.edge['mlexe']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('mlexe','debug_interface_proxy')
G.edge['mlexe']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('mlexe','diagexe')
G.edge['mlexe']['diagexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('mlexe','mlexe')
G.edge['mlexe']['mlexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('mlexe','radio')
G.edge['mlexe']['radio']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('mlexe','rild')
G.edge['mlexe']['rild']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('mlexe','smdexe')
G.edge['mlexe']['smdexe']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('mlexe','cbd')
G.edge['mlexe']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['mlexe']['cbd']['fill'] = 'red'
G.add_edge('mlexe','cbd')
G.edge['mlexe']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('mlexe','debug_interface_proxy')
G.edge['mlexe']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['mlexe']['debug_interface_proxy']['fill'] = 'red'
G.add_edge('mlexe','debug_interface_proxy')
G.edge['mlexe']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('mlexe','diagexe')
G.edge['mlexe']['diagexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['mlexe']['diagexe']['fill'] = 'red'
G.add_edge('mlexe','mlexe')
G.edge['mlexe']['mlexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['mlexe']['mlexe']['fill'] = 'red'
G.add_edge('mlexe','mlexe')
G.edge['mlexe']['mlexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('mlexe','radio')
G.edge['mlexe']['radio']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read]'
G.edge['mlexe']['radio']['fill'] = 'red'
G.add_edge('mlexe','radio')
G.edge['mlexe']['radio']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read]'
G.add_edge('mlexe','rild')
G.edge['mlexe']['rild']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['mlexe']['rild']['fill'] = 'red'
G.add_edge('mlexe','rild')
G.edge['mlexe']['rild']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('mlexe','smdexe')
G.edge['mlexe']['smdexe']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['mlexe']['smdexe']['fill'] = 'red'
G.add_edge('mlexe','smdexe')
G.edge['mlexe']['smdexe']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('radio','cbd')
G.edge['radio']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('radio','debug_interface_proxy')
G.edge['radio']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('radio','diagexe')
G.edge['radio']['diagexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('radio','mlexe')
G.edge['radio']['mlexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('radio','radio')
G.edge['radio']['radio']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('radio','rild')
G.edge['radio']['rild']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][open open][setattr getattr][write read][append read][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('radio','smdexe')
G.edge['radio']['smdexe']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('radio','cbd')
G.edge['radio']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['radio']['cbd']['fill'] = 'red'
G.add_edge('radio','cbd')
G.edge['radio']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('radio','debug_interface_proxy')
G.edge['radio']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['radio']['debug_interface_proxy']['fill'] = 'red'
G.add_edge('radio','debug_interface_proxy')
G.edge['radio']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('radio','diagexe')
G.edge['radio']['diagexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['radio']['diagexe']['fill'] = 'red'
G.add_edge('radio','mlexe')
G.edge['radio']['mlexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['radio']['mlexe']['fill'] = 'red'
G.add_edge('radio','mlexe')
G.edge['radio']['mlexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('radio','radio')
G.edge['radio']['radio']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read]'
G.edge['radio']['radio']['fill'] = 'red'
G.add_edge('radio','radio')
G.edge['radio']['radio']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read]'
G.add_edge('radio','rild')
G.edge['radio']['rild']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][open open][setattr getattr][write read][append read][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read]'
G.edge['radio']['rild']['fill'] = 'red'
G.add_edge('radio','rild')
G.edge['radio']['rild']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][open open][setattr getattr][write read][append read][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('radio','smdexe')
G.edge['radio']['smdexe']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read]'
G.edge['radio']['smdexe']['fill'] = 'red'
G.add_edge('radio','smdexe')
G.edge['radio']['smdexe']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][append read]'
G.add_edge('rild','cbd')
G.edge['rild']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open]'
G.add_edge('rild','debug_interface_proxy')
G.edge['rild']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('rild','diagexe')
G.edge['rild']['diagexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('rild','mlexe')
G.edge['rild']['mlexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('rild','radio')
G.edge['rild']['radio']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('rild','rild')
G.edge['rild']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][open open][setattr getattr][write read][append read][write read][append read][write read][append read][open open][open open][open open][setattr getattr][write read][append read][write read][append read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][write read][append read][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][write read][append read][write read][append read][setopt getopt][setopt getopt][setattr getattr][setattr getattr][write read][append read][write read][append read][setopt getopt][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('rild','smdexe')
G.edge['rild']['smdexe']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('rild','cbd')
G.edge['rild']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][write read]'
G.edge['rild']['cbd']['fill'] = 'red'
G.add_edge('rild','cbd')
G.edge['rild']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][write read][append read]'
G.add_edge('rild','debug_interface_proxy')
G.edge['rild']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['rild']['debug_interface_proxy']['fill'] = 'red'
G.add_edge('rild','debug_interface_proxy')
G.edge['rild']['debug_interface_proxy']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('rild','diagexe')
G.edge['rild']['diagexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['rild']['diagexe']['fill'] = 'red'
G.add_edge('rild','mlexe')
G.edge['rild']['mlexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['rild']['mlexe']['fill'] = 'red'
G.add_edge('rild','mlexe')
G.edge['rild']['mlexe']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('rild','radio')
G.edge['rild']['radio']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['rild']['radio']['fill'] = 'red'
G.add_edge('rild','radio')
G.edge['rild']['radio']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('rild','rild')
G.edge['rild']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][open open][setattr getattr][write read][append read][write read][append read][write read][append read][open open][open open][open open][setattr getattr][write read][append read][write read][append read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][write read][append read][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][write read][append read][write read][append read][setopt getopt][setopt getopt][setattr getattr][setattr getattr][write read][append read][write read][append read][setopt getopt][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read]'
G.edge['rild']['rild']['fill'] = 'red'
G.add_edge('rild','rild')
G.edge['rild']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][open open][setattr getattr][write read][append read][write read][append read][write read][append read][open open][open open][open open][setattr getattr][write read][append read][write read][append read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][write read][append read][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][write read][append read][write read][append read][setopt getopt][setopt getopt][setattr getattr][setattr getattr][write read][append read][write read][append read][setopt getopt][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read]'
G.add_edge('rild','smdexe')
G.edge['rild']['smdexe']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read]'
G.edge['rild']['smdexe']['fill'] = 'red'
G.add_edge('rild','smdexe')
G.edge['rild']['smdexe']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][append read]'
G.add_edge('smdexe','cbd')
G.edge['smdexe']['cbd']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('smdexe','debug_interface_proxy')
G.edge['smdexe']['debug_interface_proxy']['write-read'] = '[open open]'
G.add_edge('smdexe','diagexe')
G.edge['smdexe']['diagexe']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('smdexe','mlexe')
G.edge['smdexe']['mlexe']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('smdexe','radio')
G.edge['smdexe']['radio']['write-read'] = '[open open][write read][append read][open open][append read][open open][write read][append read][open open]'
G.add_edge('smdexe','rild')
G.edge['smdexe']['rild']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open]'
G.add_edge('smdexe','smdexe')
G.edge['smdexe']['smdexe']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('smdexe','cbd')
G.edge['smdexe']['cbd']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read]'
G.edge['smdexe']['cbd']['fill'] = 'red'
G.add_edge('smdexe','cbd')
G.edge['smdexe']['cbd']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][append read]'
G.add_edge('smdexe','debug_interface_proxy')
G.edge['smdexe']['debug_interface_proxy']['write-read'] = '[open open][write read]'
G.edge['smdexe']['debug_interface_proxy']['fill'] = 'red'
G.add_edge('smdexe','debug_interface_proxy')
G.edge['smdexe']['debug_interface_proxy']['write-read'] = '[open open][write read][append read]'
G.add_edge('smdexe','diagexe')
G.edge['smdexe']['diagexe']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['smdexe']['diagexe']['fill'] = 'red'
G.add_edge('smdexe','mlexe')
G.edge['smdexe']['mlexe']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read]'
G.edge['smdexe']['mlexe']['fill'] = 'red'
G.add_edge('smdexe','mlexe')
G.edge['smdexe']['mlexe']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][append read]'
G.add_edge('smdexe','radio')
G.edge['smdexe']['radio']['write-read'] = '[open open][write read][append read][open open][append read][open open][write read][append read][open open][write read]'
G.edge['smdexe']['radio']['fill'] = 'red'
G.add_edge('smdexe','radio')
G.edge['smdexe']['radio']['write-read'] = '[open open][write read][append read][open open][append read][open open][write read][append read][open open][write read][append read]'
G.add_edge('smdexe','rild')
G.edge['smdexe']['rild']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read]'
G.edge['smdexe']['rild']['fill'] = 'red'
G.add_edge('smdexe','rild')
G.edge['smdexe']['rild']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read]'
G.add_edge('smdexe','smdexe')
G.edge['smdexe']['smdexe']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read]'
G.edge['smdexe']['smdexe']['fill'] = 'red'
G.add_edge('smdexe','smdexe')
G.edge['smdexe']['smdexe']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read]'
app = Viewer(G)
app.mainloop()