import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('mpdecision','mpdecision')
G.edge['mpdecision']['mpdecision']['write-read'] = '[write read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][write read][open open]'
G.add_edge('mpdecision','thermal-engine')
G.edge['mpdecision']['thermal-engine']['write-read'] = '[write read][open open][write read][append read][write read][open open]'
G.add_edge('mpdecision','mpdecision')
G.edge['mpdecision']['mpdecision']['write-read'] = '[write read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][write read][open open][write read]'
G.edge['mpdecision']['mpdecision']['fill'] = 'red'
G.add_edge('mpdecision','mpdecision')
G.edge['mpdecision']['mpdecision']['write-read'] = '[write read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][write read][open open][write read][append read]'
G.add_edge('mpdecision','thermal-engine')
G.edge['mpdecision']['thermal-engine']['write-read'] = '[write read][open open][write read][append read][write read][open open][write read]'
G.edge['mpdecision']['thermal-engine']['fill'] = 'red'
G.add_edge('mpdecision','thermal-engine')
G.edge['mpdecision']['thermal-engine']['write-read'] = '[write read][open open][write read][append read][write read][open open][write read][append read]'
G.add_edge('mpdecision','mpdecision')
G.edge['mpdecision']['mpdecision']['write-read'] = '[write read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open]'
G.add_edge('mpdecision','thermal-engine')
G.edge['mpdecision']['thermal-engine']['write-read'] = '[write read][open open][write read][append read][write read][open open][write read][append read][open open]'
G.add_edge('mpdecision','mpdecision')
G.edge['mpdecision']['mpdecision']['write-read'] = '[write read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][write read]'
G.edge['mpdecision']['mpdecision']['fill'] = 'red'
G.add_edge('mpdecision','mpdecision')
G.edge['mpdecision']['mpdecision']['write-read'] = '[write read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][write read][append read]'
G.add_edge('mpdecision','thermal-engine')
G.edge['mpdecision']['thermal-engine']['write-read'] = '[write read][open open][write read][append read][write read][open open][write read][append read][open open][write read]'
G.edge['mpdecision']['thermal-engine']['fill'] = 'red'
G.add_edge('mpdecision','thermal-engine')
G.edge['mpdecision']['thermal-engine']['write-read'] = '[write read][open open][write read][append read][write read][open open][write read][append read][open open][write read][append read]'
G.add_edge('thermal-engine','mpdecision')
G.edge['thermal-engine']['mpdecision']['write-read'] = '[open open]'
G.add_edge('thermal-engine','thermal-engine')
G.edge['thermal-engine']['thermal-engine']['write-read'] = '[write read][open open]'
G.add_edge('thermal-engine','mpdecision')
G.edge['thermal-engine']['mpdecision']['write-read'] = '[open open][write read]'
G.edge['thermal-engine']['mpdecision']['fill'] = 'red'
G.add_edge('thermal-engine','mpdecision')
G.edge['thermal-engine']['mpdecision']['write-read'] = '[open open][write read][append read]'
G.add_edge('thermal-engine','thermal-engine')
G.edge['thermal-engine']['thermal-engine']['write-read'] = '[write read][open open][write read]'
G.edge['thermal-engine']['thermal-engine']['fill'] = 'red'
G.add_edge('thermal-engine','thermal-engine')
G.edge['thermal-engine']['thermal-engine']['write-read'] = '[write read][open open][write read][append read]'
app = Viewer(G)
app.mainloop()