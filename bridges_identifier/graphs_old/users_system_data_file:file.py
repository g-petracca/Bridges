import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('epmd','epmd')
G.edge['epmd']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('epmd','knox_system_app')
G.edge['epmd']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('epmd','sdp_cryptod')
G.edge['epmd']['sdp_cryptod']['write-read'] = '[open open]'
G.add_edge('epmd','s_system_app')
G.edge['epmd']['s_system_app']['write-read'] = '[setattr getattr][open open]'
G.add_edge('epmd','system_app')
G.edge['epmd']['system_app']['write-read'] = '[setattr getattr][open open]'
G.add_edge('epmd','system_server')
G.edge['epmd']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open]'
G.add_edge('epmd','vold')
G.edge['epmd']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('epmd','epmd')
G.edge['epmd']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('epmd','knox_system_app')
G.edge['epmd']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('epmd','sdp_cryptod')
G.edge['epmd']['sdp_cryptod']['write-read'] = '[open open][setattr getattr]'
G.add_edge('epmd','s_system_app')
G.edge['epmd']['s_system_app']['write-read'] = '[setattr getattr][open open][setattr getattr]'
G.add_edge('epmd','system_app')
G.edge['epmd']['system_app']['write-read'] = '[setattr getattr][open open][setattr getattr]'
G.add_edge('epmd','system_server')
G.edge['epmd']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr]'
G.add_edge('epmd','vold')
G.edge['epmd']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('epmd','epmd')
G.edge['epmd']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['epmd']['epmd']['fill'] = 'red'
G.add_edge('epmd','epmd')
G.edge['epmd']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('epmd','knox_system_app')
G.edge['epmd']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['epmd']['knox_system_app']['fill'] = 'red'
G.add_edge('epmd','knox_system_app')
G.edge['epmd']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('epmd','sdp_cryptod')
G.edge['epmd']['sdp_cryptod']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['epmd']['sdp_cryptod']['fill'] = 'red'
G.add_edge('epmd','sdp_cryptod')
G.edge['epmd']['sdp_cryptod']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('epmd','s_system_app')
G.edge['epmd']['s_system_app']['write-read'] = '[setattr getattr][open open][setattr getattr][write read]'
G.edge['epmd']['s_system_app']['fill'] = 'red'
G.add_edge('epmd','s_system_app')
G.edge['epmd']['s_system_app']['write-read'] = '[setattr getattr][open open][setattr getattr][write read][append read]'
G.add_edge('epmd','system_app')
G.edge['epmd']['system_app']['write-read'] = '[setattr getattr][open open][setattr getattr][write read]'
G.edge['epmd']['system_app']['fill'] = 'red'
G.add_edge('epmd','system_app')
G.edge['epmd']['system_app']['write-read'] = '[setattr getattr][open open][setattr getattr][write read][append read]'
G.add_edge('epmd','system_server')
G.edge['epmd']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read]'
G.edge['epmd']['system_server']['fill'] = 'red'
G.add_edge('epmd','system_server')
G.edge['epmd']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read]'
G.add_edge('epmd','vold')
G.edge['epmd']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['epmd']['vold']['fill'] = 'red'
G.add_edge('epmd','vold')
G.edge['epmd']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('ime_app','epmd')
G.edge['ime_app']['epmd']['write-read'] = '[open open]'
G.add_edge('ime_app','knox_system_app')
G.edge['ime_app']['knox_system_app']['write-read'] = '[open open]'
G.add_edge('ime_app','sdp_cryptod')
G.edge['ime_app']['sdp_cryptod']['write-read'] = '[open open]'
G.add_edge('ime_app','s_system_app')
G.edge['ime_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('ime_app','system_app')
G.edge['ime_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('ime_app','system_server')
G.edge['ime_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('ime_app','vold')
G.edge['ime_app']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open]'
G.add_edge('ime_app','epmd')
G.edge['ime_app']['epmd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('ime_app','knox_system_app')
G.edge['ime_app']['knox_system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('ime_app','sdp_cryptod')
G.edge['ime_app']['sdp_cryptod']['write-read'] = '[open open][setattr getattr]'
G.add_edge('ime_app','s_system_app')
G.edge['ime_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('ime_app','system_app')
G.edge['ime_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('ime_app','system_server')
G.edge['ime_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('ime_app','vold')
G.edge['ime_app']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][setattr getattr]'
G.add_edge('ime_app','epmd')
G.edge['ime_app']['epmd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['ime_app']['epmd']['fill'] = 'red'
G.add_edge('ime_app','epmd')
G.edge['ime_app']['epmd']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('ime_app','knox_system_app')
G.edge['ime_app']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['ime_app']['knox_system_app']['fill'] = 'red'
G.add_edge('ime_app','knox_system_app')
G.edge['ime_app']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('ime_app','sdp_cryptod')
G.edge['ime_app']['sdp_cryptod']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['ime_app']['sdp_cryptod']['fill'] = 'red'
G.add_edge('ime_app','sdp_cryptod')
G.edge['ime_app']['sdp_cryptod']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('ime_app','s_system_app')
G.edge['ime_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['ime_app']['s_system_app']['fill'] = 'red'
G.add_edge('ime_app','s_system_app')
G.edge['ime_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('ime_app','system_app')
G.edge['ime_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['ime_app']['system_app']['fill'] = 'red'
G.add_edge('ime_app','system_app')
G.edge['ime_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('ime_app','system_server')
G.edge['ime_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['ime_app']['system_server']['fill'] = 'red'
G.add_edge('ime_app','system_server')
G.edge['ime_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('ime_app','vold')
G.edge['ime_app']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['ime_app']['vold']['fill'] = 'red'
G.add_edge('ime_app','vold')
G.edge['ime_app']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('knox_system_app','epmd')
G.edge['knox_system_app']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('knox_system_app','knox_system_app')
G.edge['knox_system_app']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('knox_system_app','sdp_cryptod')
G.edge['knox_system_app']['sdp_cryptod']['write-read'] = '[open open]'
G.add_edge('knox_system_app','s_system_app')
G.edge['knox_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('knox_system_app','system_app')
G.edge['knox_system_app']['system_app']['write-read'] = '[open open]'
G.add_edge('knox_system_app','system_server')
G.edge['knox_system_app']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('knox_system_app','vold')
G.edge['knox_system_app']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('knox_system_app','epmd')
G.edge['knox_system_app']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('knox_system_app','knox_system_app')
G.edge['knox_system_app']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('knox_system_app','sdp_cryptod')
G.edge['knox_system_app']['sdp_cryptod']['write-read'] = '[open open][setattr getattr]'
G.add_edge('knox_system_app','s_system_app')
G.edge['knox_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('knox_system_app','system_app')
G.edge['knox_system_app']['system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('knox_system_app','system_server')
G.edge['knox_system_app']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('knox_system_app','vold')
G.edge['knox_system_app']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('knox_system_app','epmd')
G.edge['knox_system_app']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['knox_system_app']['epmd']['fill'] = 'red'
G.add_edge('knox_system_app','epmd')
G.edge['knox_system_app']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('knox_system_app','knox_system_app')
G.edge['knox_system_app']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['knox_system_app']['knox_system_app']['fill'] = 'red'
G.add_edge('knox_system_app','knox_system_app')
G.edge['knox_system_app']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('knox_system_app','sdp_cryptod')
G.edge['knox_system_app']['sdp_cryptod']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['knox_system_app']['sdp_cryptod']['fill'] = 'red'
G.add_edge('knox_system_app','sdp_cryptod')
G.edge['knox_system_app']['sdp_cryptod']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('knox_system_app','s_system_app')
G.edge['knox_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['knox_system_app']['s_system_app']['fill'] = 'red'
G.add_edge('knox_system_app','s_system_app')
G.edge['knox_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('knox_system_app','system_app')
G.edge['knox_system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['knox_system_app']['system_app']['fill'] = 'red'
G.add_edge('knox_system_app','system_app')
G.edge['knox_system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('knox_system_app','system_server')
G.edge['knox_system_app']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['knox_system_app']['system_server']['fill'] = 'red'
G.add_edge('knox_system_app','system_server')
G.edge['knox_system_app']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('knox_system_app','vold')
G.edge['knox_system_app']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['knox_system_app']['vold']['fill'] = 'red'
G.add_edge('knox_system_app','vold')
G.edge['knox_system_app']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('sdp_cryptod','epmd')
G.edge['sdp_cryptod']['epmd']['write-read'] = '[open open]'
G.add_edge('sdp_cryptod','knox_system_app')
G.edge['sdp_cryptod']['knox_system_app']['write-read'] = '[open open]'
G.add_edge('sdp_cryptod','sdp_cryptod')
G.edge['sdp_cryptod']['sdp_cryptod']['write-read'] = '[open open]'
G.add_edge('sdp_cryptod','s_system_app')
G.edge['sdp_cryptod']['s_system_app']['write-read'] = '[open open]'
G.add_edge('sdp_cryptod','system_app')
G.edge['sdp_cryptod']['system_app']['write-read'] = '[open open]'
G.add_edge('sdp_cryptod','system_server')
G.edge['sdp_cryptod']['system_server']['write-read'] = '[open open]'
G.add_edge('sdp_cryptod','vold')
G.edge['sdp_cryptod']['vold']['write-read'] = '[open open]'
G.add_edge('sdp_cryptod','epmd')
G.edge['sdp_cryptod']['epmd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('sdp_cryptod','knox_system_app')
G.edge['sdp_cryptod']['knox_system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('sdp_cryptod','sdp_cryptod')
G.edge['sdp_cryptod']['sdp_cryptod']['write-read'] = '[open open][setattr getattr]'
G.add_edge('sdp_cryptod','s_system_app')
G.edge['sdp_cryptod']['s_system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('sdp_cryptod','system_app')
G.edge['sdp_cryptod']['system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('sdp_cryptod','system_server')
G.edge['sdp_cryptod']['system_server']['write-read'] = '[open open][setattr getattr]'
G.add_edge('sdp_cryptod','vold')
G.edge['sdp_cryptod']['vold']['write-read'] = '[open open][setattr getattr]'
G.add_edge('sdp_cryptod','epmd')
G.edge['sdp_cryptod']['epmd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['sdp_cryptod']['epmd']['fill'] = 'red'
G.add_edge('sdp_cryptod','epmd')
G.edge['sdp_cryptod']['epmd']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('sdp_cryptod','knox_system_app')
G.edge['sdp_cryptod']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['sdp_cryptod']['knox_system_app']['fill'] = 'red'
G.add_edge('sdp_cryptod','knox_system_app')
G.edge['sdp_cryptod']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('sdp_cryptod','sdp_cryptod')
G.edge['sdp_cryptod']['sdp_cryptod']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['sdp_cryptod']['sdp_cryptod']['fill'] = 'red'
G.add_edge('sdp_cryptod','sdp_cryptod')
G.edge['sdp_cryptod']['sdp_cryptod']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('sdp_cryptod','s_system_app')
G.edge['sdp_cryptod']['s_system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['sdp_cryptod']['s_system_app']['fill'] = 'red'
G.add_edge('sdp_cryptod','s_system_app')
G.edge['sdp_cryptod']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('sdp_cryptod','system_app')
G.edge['sdp_cryptod']['system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['sdp_cryptod']['system_app']['fill'] = 'red'
G.add_edge('sdp_cryptod','system_app')
G.edge['sdp_cryptod']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('sdp_cryptod','system_server')
G.edge['sdp_cryptod']['system_server']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['sdp_cryptod']['system_server']['fill'] = 'red'
G.add_edge('sdp_cryptod','system_server')
G.edge['sdp_cryptod']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('sdp_cryptod','vold')
G.edge['sdp_cryptod']['vold']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['sdp_cryptod']['vold']['fill'] = 'red'
G.add_edge('sdp_cryptod','vold')
G.edge['sdp_cryptod']['vold']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('s_system_app','epmd')
G.edge['s_system_app']['epmd']['write-read'] = '[open open]'
G.add_edge('s_system_app','knox_system_app')
G.edge['s_system_app']['knox_system_app']['write-read'] = '[open open]'
G.add_edge('s_system_app','sdp_cryptod')
G.edge['s_system_app']['sdp_cryptod']['write-read'] = '[open open]'
G.add_edge('s_system_app','s_system_app')
G.edge['s_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open]'
G.add_edge('s_system_app','system_app')
G.edge['s_system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open]'
G.add_edge('s_system_app','system_server')
G.edge['s_system_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('s_system_app','vold')
G.edge['s_system_app']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('s_system_app','epmd')
G.edge['s_system_app']['epmd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('s_system_app','knox_system_app')
G.edge['s_system_app']['knox_system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('s_system_app','sdp_cryptod')
G.edge['s_system_app']['sdp_cryptod']['write-read'] = '[open open][setattr getattr]'
G.add_edge('s_system_app','s_system_app')
G.edge['s_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr]'
G.add_edge('s_system_app','system_app')
G.edge['s_system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr]'
G.add_edge('s_system_app','system_server')
G.edge['s_system_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('s_system_app','vold')
G.edge['s_system_app']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][setattr getattr]'
G.add_edge('s_system_app','epmd')
G.edge['s_system_app']['epmd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['s_system_app']['epmd']['fill'] = 'red'
G.add_edge('s_system_app','epmd')
G.edge['s_system_app']['epmd']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('s_system_app','knox_system_app')
G.edge['s_system_app']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['s_system_app']['knox_system_app']['fill'] = 'red'
G.add_edge('s_system_app','knox_system_app')
G.edge['s_system_app']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('s_system_app','sdp_cryptod')
G.edge['s_system_app']['sdp_cryptod']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['s_system_app']['sdp_cryptod']['fill'] = 'red'
G.add_edge('s_system_app','sdp_cryptod')
G.edge['s_system_app']['sdp_cryptod']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('s_system_app','s_system_app')
G.edge['s_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['s_system_app']['s_system_app']['fill'] = 'red'
G.add_edge('s_system_app','s_system_app')
G.edge['s_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('s_system_app','system_app')
G.edge['s_system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['s_system_app']['system_app']['fill'] = 'red'
G.add_edge('s_system_app','system_app')
G.edge['s_system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('s_system_app','system_server')
G.edge['s_system_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['s_system_app']['system_server']['fill'] = 'red'
G.add_edge('s_system_app','system_server')
G.edge['s_system_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('s_system_app','vold')
G.edge['s_system_app']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['s_system_app']['vold']['fill'] = 'red'
G.add_edge('s_system_app','vold')
G.edge['s_system_app']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('system_app','epmd')
G.edge['system_app']['epmd']['write-read'] = '[open open]'
G.add_edge('system_app','knox_system_app')
G.edge['system_app']['knox_system_app']['write-read'] = '[open open]'
G.add_edge('system_app','sdp_cryptod')
G.edge['system_app']['sdp_cryptod']['write-read'] = '[open open]'
G.add_edge('system_app','s_system_app')
G.edge['system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open]'
G.add_edge('system_app','system_app')
G.edge['system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open]'
G.add_edge('system_app','system_server')
G.edge['system_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('system_app','vold')
G.edge['system_app']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open]'
G.add_edge('system_app','epmd')
G.edge['system_app']['epmd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('system_app','knox_system_app')
G.edge['system_app']['knox_system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('system_app','sdp_cryptod')
G.edge['system_app']['sdp_cryptod']['write-read'] = '[open open][setattr getattr]'
G.add_edge('system_app','s_system_app')
G.edge['system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr]'
G.add_edge('system_app','system_app')
G.edge['system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr]'
G.add_edge('system_app','system_server')
G.edge['system_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('system_app','vold')
G.edge['system_app']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][setattr getattr]'
G.add_edge('system_app','epmd')
G.edge['system_app']['epmd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['system_app']['epmd']['fill'] = 'red'
G.add_edge('system_app','epmd')
G.edge['system_app']['epmd']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('system_app','knox_system_app')
G.edge['system_app']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['system_app']['knox_system_app']['fill'] = 'red'
G.add_edge('system_app','knox_system_app')
G.edge['system_app']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('system_app','sdp_cryptod')
G.edge['system_app']['sdp_cryptod']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['system_app']['sdp_cryptod']['fill'] = 'red'
G.add_edge('system_app','sdp_cryptod')
G.edge['system_app']['sdp_cryptod']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('system_app','s_system_app')
G.edge['system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['system_app']['s_system_app']['fill'] = 'red'
G.add_edge('system_app','s_system_app')
G.edge['system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('system_app','system_app')
G.edge['system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['system_app']['system_app']['fill'] = 'red'
G.add_edge('system_app','system_app')
G.edge['system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('system_app','system_server')
G.edge['system_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['system_app']['system_server']['fill'] = 'red'
G.add_edge('system_app','system_server')
G.edge['system_app']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][add_name search][remove_name search][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('system_app','vold')
G.edge['system_app']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['system_app']['vold']['fill'] = 'red'
G.add_edge('system_app','vold')
G.edge['system_app']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('system_server','epmd')
G.edge['system_server']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('system_server','knox_system_app')
G.edge['system_server']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('system_server','sdp_cryptod')
G.edge['system_server']['sdp_cryptod']['write-read'] = '[open open]'
G.add_edge('system_server','s_system_app')
G.edge['system_server']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open]'
G.add_edge('system_server','system_app')
G.edge['system_server']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open]'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('system_server','vold')
G.edge['system_server']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('system_server','epmd')
G.edge['system_server']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('system_server','knox_system_app')
G.edge['system_server']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('system_server','sdp_cryptod')
G.edge['system_server']['sdp_cryptod']['write-read'] = '[open open][setattr getattr]'
G.add_edge('system_server','s_system_app')
G.edge['system_server']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('system_server','system_app')
G.edge['system_server']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('system_server','vold')
G.edge['system_server']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('system_server','epmd')
G.edge['system_server']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['system_server']['epmd']['fill'] = 'red'
G.add_edge('system_server','epmd')
G.edge['system_server']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('system_server','knox_system_app')
G.edge['system_server']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['system_server']['knox_system_app']['fill'] = 'red'
G.add_edge('system_server','knox_system_app')
G.edge['system_server']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('system_server','sdp_cryptod')
G.edge['system_server']['sdp_cryptod']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['system_server']['sdp_cryptod']['fill'] = 'red'
G.add_edge('system_server','sdp_cryptod')
G.edge['system_server']['sdp_cryptod']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('system_server','s_system_app')
G.edge['system_server']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['system_server']['s_system_app']['fill'] = 'red'
G.add_edge('system_server','s_system_app')
G.edge['system_server']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('system_server','system_app')
G.edge['system_server']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['system_server']['system_app']['fill'] = 'red'
G.add_edge('system_server','system_app')
G.edge['system_server']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['system_server']['system_server']['fill'] = 'red'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('system_server','vold')
G.edge['system_server']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['system_server']['vold']['fill'] = 'red'
G.add_edge('system_server','vold')
G.edge['system_server']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('vold','epmd')
G.edge['vold']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('vold','knox_system_app')
G.edge['vold']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('vold','sdp_cryptod')
G.edge['vold']['sdp_cryptod']['write-read'] = '[open open]'
G.add_edge('vold','s_system_app')
G.edge['vold']['s_system_app']['write-read'] = '[setattr getattr][setopt getopt][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][open open]'
G.add_edge('vold','system_app')
G.edge['vold']['system_app']['write-read'] = '[setattr getattr][setopt getopt][setattr getattr][open open][setattr getattr][write read][append read][open open]'
G.add_edge('vold','system_server')
G.edge['vold']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open]'
G.add_edge('vold','vold')
G.edge['vold']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('vold','epmd')
G.edge['vold']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('vold','knox_system_app')
G.edge['vold']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('vold','sdp_cryptod')
G.edge['vold']['sdp_cryptod']['write-read'] = '[open open][setattr getattr]'
G.add_edge('vold','s_system_app')
G.edge['vold']['s_system_app']['write-read'] = '[setattr getattr][setopt getopt][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('vold','system_app')
G.edge['vold']['system_app']['write-read'] = '[setattr getattr][setopt getopt][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('vold','system_server')
G.edge['vold']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('vold','vold')
G.edge['vold']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('vold','epmd')
G.edge['vold']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['vold']['epmd']['fill'] = 'red'
G.add_edge('vold','epmd')
G.edge['vold']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('vold','knox_system_app')
G.edge['vold']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['vold']['knox_system_app']['fill'] = 'red'
G.add_edge('vold','knox_system_app')
G.edge['vold']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('vold','sdp_cryptod')
G.edge['vold']['sdp_cryptod']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['vold']['sdp_cryptod']['fill'] = 'red'
G.add_edge('vold','sdp_cryptod')
G.edge['vold']['sdp_cryptod']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('vold','s_system_app')
G.edge['vold']['s_system_app']['write-read'] = '[setattr getattr][setopt getopt][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['vold']['s_system_app']['fill'] = 'red'
G.add_edge('vold','s_system_app')
G.edge['vold']['s_system_app']['write-read'] = '[setattr getattr][setopt getopt][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('vold','system_app')
G.edge['vold']['system_app']['write-read'] = '[setattr getattr][setopt getopt][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['vold']['system_app']['fill'] = 'red'
G.add_edge('vold','system_app')
G.edge['vold']['system_app']['write-read'] = '[setattr getattr][setopt getopt][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('vold','system_server')
G.edge['vold']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['vold']['system_server']['fill'] = 'red'
G.add_edge('vold','system_server')
G.edge['vold']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('vold','vold')
G.edge['vold']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['vold']['vold']['fill'] = 'red'
G.add_edge('vold','vold')
G.edge['vold']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
app = Viewer(G)
app.mainloop()