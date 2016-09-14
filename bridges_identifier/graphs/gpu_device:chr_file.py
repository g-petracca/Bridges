import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('adbd','adbd')
G.edge['adbd']['adbd']['write-read'] = '[open open]'
G.add_edge('adbd','appdomain')
G.edge['adbd']['appdomain']['write-read'] = '[open open]'
G.add_edge('adbd','bootanim')
G.edge['adbd']['bootanim']['write-read'] = '[open open]'
G.add_edge('adbd','dumpstate')
G.edge['adbd']['dumpstate']['write-read'] = '[open open]'
G.add_edge('adbd','mediaserver')
G.edge['adbd']['mediaserver']['write-read'] = '[open open]'
G.add_edge('adbd','mm-qcamerad')
G.edge['adbd']['mm-qcamerad']['write-read'] = '[open open]'
G.add_edge('adbd','surfaceflinger')
G.edge['adbd']['surfaceflinger']['write-read'] = '[open open]'
G.add_edge('adbd','system_server')
G.edge['adbd']['system_server']['write-read'] = '[open open]'
G.add_edge('adbd','adbd')
G.edge['adbd']['adbd']['write-read'] = '[open open][write read]'
G.edge['adbd']['adbd']['fill'] = 'red'
G.add_edge('adbd','adbd')
G.edge['adbd']['adbd']['write-read'] = '[open open][write read][append read]'
G.add_edge('adbd','appdomain')
G.edge['adbd']['appdomain']['write-read'] = '[open open][write read]'
G.edge['adbd']['appdomain']['fill'] = 'red'
G.add_edge('adbd','appdomain')
G.edge['adbd']['appdomain']['write-read'] = '[open open][write read][append read]'
G.add_edge('adbd','bootanim')
G.edge['adbd']['bootanim']['write-read'] = '[open open][write read]'
G.edge['adbd']['bootanim']['fill'] = 'red'
G.add_edge('adbd','bootanim')
G.edge['adbd']['bootanim']['write-read'] = '[open open][write read][append read]'
G.add_edge('adbd','dumpstate')
G.edge['adbd']['dumpstate']['write-read'] = '[open open][write read]'
G.edge['adbd']['dumpstate']['fill'] = 'red'
G.add_edge('adbd','dumpstate')
G.edge['adbd']['dumpstate']['write-read'] = '[open open][write read][append read]'
G.add_edge('adbd','mediaserver')
G.edge['adbd']['mediaserver']['write-read'] = '[open open][write read]'
G.edge['adbd']['mediaserver']['fill'] = 'red'
G.add_edge('adbd','mediaserver')
G.edge['adbd']['mediaserver']['write-read'] = '[open open][write read][append read]'
G.add_edge('adbd','mm-qcamerad')
G.edge['adbd']['mm-qcamerad']['write-read'] = '[open open][write read]'
G.edge['adbd']['mm-qcamerad']['fill'] = 'red'
G.add_edge('adbd','mm-qcamerad')
G.edge['adbd']['mm-qcamerad']['write-read'] = '[open open][write read][append read]'
G.add_edge('adbd','surfaceflinger')
G.edge['adbd']['surfaceflinger']['write-read'] = '[open open][write read]'
G.edge['adbd']['surfaceflinger']['fill'] = 'red'
G.add_edge('adbd','surfaceflinger')
G.edge['adbd']['surfaceflinger']['write-read'] = '[open open][write read][append read]'
G.add_edge('adbd','system_server')
G.edge['adbd']['system_server']['write-read'] = '[open open][write read]'
G.edge['adbd']['system_server']['fill'] = 'red'
G.add_edge('adbd','system_server')
G.edge['adbd']['system_server']['write-read'] = '[open open][write read][append read]'
G.add_edge('appdomain','adbd')
G.edge['appdomain']['adbd']['write-read'] = '[open open]'
G.add_edge('appdomain','appdomain')
G.edge['appdomain']['appdomain']['write-read'] = '[open open]'
G.add_edge('appdomain','bootanim')
G.edge['appdomain']['bootanim']['write-read'] = '[open open]'
G.add_edge('appdomain','dumpstate')
G.edge['appdomain']['dumpstate']['write-read'] = '[open open]'
G.add_edge('appdomain','mediaserver')
G.edge['appdomain']['mediaserver']['write-read'] = '[open open]'
G.add_edge('appdomain','mm-qcamerad')
G.edge['appdomain']['mm-qcamerad']['write-read'] = '[open open]'
G.add_edge('appdomain','surfaceflinger')
G.edge['appdomain']['surfaceflinger']['write-read'] = '[open open]'
G.add_edge('appdomain','system_server')
G.edge['appdomain']['system_server']['write-read'] = '[open open]'
G.add_edge('appdomain','adbd')
G.edge['appdomain']['adbd']['write-read'] = '[open open][write read]'
G.edge['appdomain']['adbd']['fill'] = 'red'
G.add_edge('appdomain','adbd')
G.edge['appdomain']['adbd']['write-read'] = '[open open][write read][append read]'
G.add_edge('appdomain','appdomain')
G.edge['appdomain']['appdomain']['write-read'] = '[open open][write read]'
G.edge['appdomain']['appdomain']['fill'] = 'red'
G.add_edge('appdomain','appdomain')
G.edge['appdomain']['appdomain']['write-read'] = '[open open][write read][append read]'
G.add_edge('appdomain','bootanim')
G.edge['appdomain']['bootanim']['write-read'] = '[open open][write read]'
G.edge['appdomain']['bootanim']['fill'] = 'red'
G.add_edge('appdomain','bootanim')
G.edge['appdomain']['bootanim']['write-read'] = '[open open][write read][append read]'
G.add_edge('appdomain','dumpstate')
G.edge['appdomain']['dumpstate']['write-read'] = '[open open][write read]'
G.edge['appdomain']['dumpstate']['fill'] = 'red'
G.add_edge('appdomain','dumpstate')
G.edge['appdomain']['dumpstate']['write-read'] = '[open open][write read][append read]'
G.add_edge('appdomain','mediaserver')
G.edge['appdomain']['mediaserver']['write-read'] = '[open open][write read]'
G.edge['appdomain']['mediaserver']['fill'] = 'red'
G.add_edge('appdomain','mediaserver')
G.edge['appdomain']['mediaserver']['write-read'] = '[open open][write read][append read]'
G.add_edge('appdomain','mm-qcamerad')
G.edge['appdomain']['mm-qcamerad']['write-read'] = '[open open][write read]'
G.edge['appdomain']['mm-qcamerad']['fill'] = 'red'
G.add_edge('appdomain','mm-qcamerad')
G.edge['appdomain']['mm-qcamerad']['write-read'] = '[open open][write read][append read]'
G.add_edge('appdomain','surfaceflinger')
G.edge['appdomain']['surfaceflinger']['write-read'] = '[open open][write read]'
G.edge['appdomain']['surfaceflinger']['fill'] = 'red'
G.add_edge('appdomain','surfaceflinger')
G.edge['appdomain']['surfaceflinger']['write-read'] = '[open open][write read][append read]'
G.add_edge('appdomain','system_server')
G.edge['appdomain']['system_server']['write-read'] = '[open open][write read]'
G.edge['appdomain']['system_server']['fill'] = 'red'
G.add_edge('appdomain','system_server')
G.edge['appdomain']['system_server']['write-read'] = '[open open][write read][append read]'
G.add_edge('bootanim','adbd')
G.edge['bootanim']['adbd']['write-read'] = '[open open]'
G.add_edge('bootanim','appdomain')
G.edge['bootanim']['appdomain']['write-read'] = '[open open]'
G.add_edge('bootanim','bootanim')
G.edge['bootanim']['bootanim']['write-read'] = '[open open]'
G.add_edge('bootanim','dumpstate')
G.edge['bootanim']['dumpstate']['write-read'] = '[open open]'
G.add_edge('bootanim','mediaserver')
G.edge['bootanim']['mediaserver']['write-read'] = '[open open]'
G.add_edge('bootanim','mm-qcamerad')
G.edge['bootanim']['mm-qcamerad']['write-read'] = '[open open]'
G.add_edge('bootanim','surfaceflinger')
G.edge['bootanim']['surfaceflinger']['write-read'] = '[open open]'
G.add_edge('bootanim','system_server')
G.edge['bootanim']['system_server']['write-read'] = '[open open]'
G.add_edge('bootanim','adbd')
G.edge['bootanim']['adbd']['write-read'] = '[open open][write read]'
G.edge['bootanim']['adbd']['fill'] = 'red'
G.add_edge('bootanim','adbd')
G.edge['bootanim']['adbd']['write-read'] = '[open open][write read][append read]'
G.add_edge('bootanim','appdomain')
G.edge['bootanim']['appdomain']['write-read'] = '[open open][write read]'
G.edge['bootanim']['appdomain']['fill'] = 'red'
G.add_edge('bootanim','appdomain')
G.edge['bootanim']['appdomain']['write-read'] = '[open open][write read][append read]'
G.add_edge('bootanim','bootanim')
G.edge['bootanim']['bootanim']['write-read'] = '[open open][write read]'
G.edge['bootanim']['bootanim']['fill'] = 'red'
G.add_edge('bootanim','bootanim')
G.edge['bootanim']['bootanim']['write-read'] = '[open open][write read][append read]'
G.add_edge('bootanim','dumpstate')
G.edge['bootanim']['dumpstate']['write-read'] = '[open open][write read]'
G.edge['bootanim']['dumpstate']['fill'] = 'red'
G.add_edge('bootanim','dumpstate')
G.edge['bootanim']['dumpstate']['write-read'] = '[open open][write read][append read]'
G.add_edge('bootanim','mediaserver')
G.edge['bootanim']['mediaserver']['write-read'] = '[open open][write read]'
G.edge['bootanim']['mediaserver']['fill'] = 'red'
G.add_edge('bootanim','mediaserver')
G.edge['bootanim']['mediaserver']['write-read'] = '[open open][write read][append read]'
G.add_edge('bootanim','mm-qcamerad')
G.edge['bootanim']['mm-qcamerad']['write-read'] = '[open open][write read]'
G.edge['bootanim']['mm-qcamerad']['fill'] = 'red'
G.add_edge('bootanim','mm-qcamerad')
G.edge['bootanim']['mm-qcamerad']['write-read'] = '[open open][write read][append read]'
G.add_edge('bootanim','surfaceflinger')
G.edge['bootanim']['surfaceflinger']['write-read'] = '[open open][write read]'
G.edge['bootanim']['surfaceflinger']['fill'] = 'red'
G.add_edge('bootanim','surfaceflinger')
G.edge['bootanim']['surfaceflinger']['write-read'] = '[open open][write read][append read]'
G.add_edge('bootanim','system_server')
G.edge['bootanim']['system_server']['write-read'] = '[open open][write read]'
G.edge['bootanim']['system_server']['fill'] = 'red'
G.add_edge('bootanim','system_server')
G.edge['bootanim']['system_server']['write-read'] = '[open open][write read][append read]'
G.add_edge('dumpstate','adbd')
G.edge['dumpstate']['adbd']['write-read'] = '[write read][add_name search][open open]'
G.add_edge('dumpstate','appdomain')
G.edge['dumpstate']['appdomain']['write-read'] = '[open open]'
G.add_edge('dumpstate','bootanim')
G.edge['dumpstate']['bootanim']['write-read'] = '[open open]'
G.add_edge('dumpstate','dumpstate')
G.edge['dumpstate']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('dumpstate','mediaserver')
G.edge['dumpstate']['mediaserver']['write-read'] = '[open open]'
G.add_edge('dumpstate','mm-qcamerad')
G.edge['dumpstate']['mm-qcamerad']['write-read'] = '[open open]'
G.add_edge('dumpstate','surfaceflinger')
G.edge['dumpstate']['surfaceflinger']['write-read'] = '[open open]'
G.add_edge('dumpstate','system_server')
G.edge['dumpstate']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open]'
G.add_edge('dumpstate','adbd')
G.edge['dumpstate']['adbd']['write-read'] = '[write read][add_name search][open open][write read]'
G.edge['dumpstate']['adbd']['fill'] = 'red'
G.add_edge('dumpstate','adbd')
G.edge['dumpstate']['adbd']['write-read'] = '[write read][add_name search][open open][write read][append read]'
G.add_edge('dumpstate','appdomain')
G.edge['dumpstate']['appdomain']['write-read'] = '[open open][write read]'
G.edge['dumpstate']['appdomain']['fill'] = 'red'
G.add_edge('dumpstate','appdomain')
G.edge['dumpstate']['appdomain']['write-read'] = '[open open][write read][append read]'
G.add_edge('dumpstate','bootanim')
G.edge['dumpstate']['bootanim']['write-read'] = '[open open][write read]'
G.edge['dumpstate']['bootanim']['fill'] = 'red'
G.add_edge('dumpstate','bootanim')
G.edge['dumpstate']['bootanim']['write-read'] = '[open open][write read][append read]'
G.add_edge('dumpstate','dumpstate')
G.edge['dumpstate']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['dumpstate']['dumpstate']['fill'] = 'red'
G.add_edge('dumpstate','dumpstate')
G.edge['dumpstate']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('dumpstate','mediaserver')
G.edge['dumpstate']['mediaserver']['write-read'] = '[open open][write read]'
G.edge['dumpstate']['mediaserver']['fill'] = 'red'
G.add_edge('dumpstate','mediaserver')
G.edge['dumpstate']['mediaserver']['write-read'] = '[open open][write read][append read]'
G.add_edge('dumpstate','mm-qcamerad')
G.edge['dumpstate']['mm-qcamerad']['write-read'] = '[open open][write read]'
G.edge['dumpstate']['mm-qcamerad']['fill'] = 'red'
G.add_edge('dumpstate','mm-qcamerad')
G.edge['dumpstate']['mm-qcamerad']['write-read'] = '[open open][write read][append read]'
G.add_edge('dumpstate','surfaceflinger')
G.edge['dumpstate']['surfaceflinger']['write-read'] = '[open open][write read]'
G.edge['dumpstate']['surfaceflinger']['fill'] = 'red'
G.add_edge('dumpstate','surfaceflinger')
G.edge['dumpstate']['surfaceflinger']['write-read'] = '[open open][write read][append read]'
G.add_edge('dumpstate','system_server')
G.edge['dumpstate']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read]'
G.edge['dumpstate']['system_server']['fill'] = 'red'
G.add_edge('dumpstate','system_server')
G.edge['dumpstate']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read]'
G.add_edge('mediaserver','adbd')
G.edge['mediaserver']['adbd']['write-read'] = '[open open]'
G.add_edge('mediaserver','appdomain')
G.edge['mediaserver']['appdomain']['write-read'] = '[open open]'
G.add_edge('mediaserver','bootanim')
G.edge['mediaserver']['bootanim']['write-read'] = '[open open]'
G.add_edge('mediaserver','dumpstate')
G.edge['mediaserver']['dumpstate']['write-read'] = '[open open]'
G.add_edge('mediaserver','mediaserver')
G.edge['mediaserver']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('mediaserver','mm-qcamerad')
G.edge['mediaserver']['mm-qcamerad']['write-read'] = '[open open]'
G.add_edge('mediaserver','surfaceflinger')
G.edge['mediaserver']['surfaceflinger']['write-read'] = '[open open]'
G.add_edge('mediaserver','system_server')
G.edge['mediaserver']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('mediaserver','adbd')
G.edge['mediaserver']['adbd']['write-read'] = '[open open][write read]'
G.edge['mediaserver']['adbd']['fill'] = 'red'
G.add_edge('mediaserver','adbd')
G.edge['mediaserver']['adbd']['write-read'] = '[open open][write read][append read]'
G.add_edge('mediaserver','appdomain')
G.edge['mediaserver']['appdomain']['write-read'] = '[open open][write read]'
G.edge['mediaserver']['appdomain']['fill'] = 'red'
G.add_edge('mediaserver','appdomain')
G.edge['mediaserver']['appdomain']['write-read'] = '[open open][write read][append read]'
G.add_edge('mediaserver','bootanim')
G.edge['mediaserver']['bootanim']['write-read'] = '[open open][write read]'
G.edge['mediaserver']['bootanim']['fill'] = 'red'
G.add_edge('mediaserver','bootanim')
G.edge['mediaserver']['bootanim']['write-read'] = '[open open][write read][append read]'
G.add_edge('mediaserver','dumpstate')
G.edge['mediaserver']['dumpstate']['write-read'] = '[open open][write read]'
G.edge['mediaserver']['dumpstate']['fill'] = 'red'
G.add_edge('mediaserver','dumpstate')
G.edge['mediaserver']['dumpstate']['write-read'] = '[open open][write read][append read]'
G.add_edge('mediaserver','mediaserver')
G.edge['mediaserver']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read]'
G.edge['mediaserver']['mediaserver']['fill'] = 'red'
G.add_edge('mediaserver','mediaserver')
G.edge['mediaserver']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('mediaserver','mm-qcamerad')
G.edge['mediaserver']['mm-qcamerad']['write-read'] = '[open open][write read]'
G.edge['mediaserver']['mm-qcamerad']['fill'] = 'red'
G.add_edge('mediaserver','mm-qcamerad')
G.edge['mediaserver']['mm-qcamerad']['write-read'] = '[open open][write read][append read]'
G.add_edge('mediaserver','surfaceflinger')
G.edge['mediaserver']['surfaceflinger']['write-read'] = '[open open][write read]'
G.edge['mediaserver']['surfaceflinger']['fill'] = 'red'
G.add_edge('mediaserver','surfaceflinger')
G.edge['mediaserver']['surfaceflinger']['write-read'] = '[open open][write read][append read]'
G.add_edge('mediaserver','system_server')
G.edge['mediaserver']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read]'
G.edge['mediaserver']['system_server']['fill'] = 'red'
G.add_edge('mediaserver','system_server')
G.edge['mediaserver']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('mm-qcamerad','adbd')
G.edge['mm-qcamerad']['adbd']['write-read'] = '[open open]'
G.add_edge('mm-qcamerad','appdomain')
G.edge['mm-qcamerad']['appdomain']['write-read'] = '[open open]'
G.add_edge('mm-qcamerad','bootanim')
G.edge['mm-qcamerad']['bootanim']['write-read'] = '[open open]'
G.add_edge('mm-qcamerad','dumpstate')
G.edge['mm-qcamerad']['dumpstate']['write-read'] = '[open open]'
G.add_edge('mm-qcamerad','mediaserver')
G.edge['mm-qcamerad']['mediaserver']['write-read'] = '[open open]'
G.add_edge('mm-qcamerad','mm-qcamerad')
G.edge['mm-qcamerad']['mm-qcamerad']['write-read'] = '[open open]'
G.add_edge('mm-qcamerad','surfaceflinger')
G.edge['mm-qcamerad']['surfaceflinger']['write-read'] = '[open open]'
G.add_edge('mm-qcamerad','system_server')
G.edge['mm-qcamerad']['system_server']['write-read'] = '[open open]'
G.add_edge('mm-qcamerad','adbd')
G.edge['mm-qcamerad']['adbd']['write-read'] = '[open open][write read]'
G.edge['mm-qcamerad']['adbd']['fill'] = 'red'
G.add_edge('mm-qcamerad','adbd')
G.edge['mm-qcamerad']['adbd']['write-read'] = '[open open][write read][append read]'
G.add_edge('mm-qcamerad','appdomain')
G.edge['mm-qcamerad']['appdomain']['write-read'] = '[open open][write read]'
G.edge['mm-qcamerad']['appdomain']['fill'] = 'red'
G.add_edge('mm-qcamerad','appdomain')
G.edge['mm-qcamerad']['appdomain']['write-read'] = '[open open][write read][append read]'
G.add_edge('mm-qcamerad','bootanim')
G.edge['mm-qcamerad']['bootanim']['write-read'] = '[open open][write read]'
G.edge['mm-qcamerad']['bootanim']['fill'] = 'red'
G.add_edge('mm-qcamerad','bootanim')
G.edge['mm-qcamerad']['bootanim']['write-read'] = '[open open][write read][append read]'
G.add_edge('mm-qcamerad','dumpstate')
G.edge['mm-qcamerad']['dumpstate']['write-read'] = '[open open][write read]'
G.edge['mm-qcamerad']['dumpstate']['fill'] = 'red'
G.add_edge('mm-qcamerad','dumpstate')
G.edge['mm-qcamerad']['dumpstate']['write-read'] = '[open open][write read][append read]'
G.add_edge('mm-qcamerad','mediaserver')
G.edge['mm-qcamerad']['mediaserver']['write-read'] = '[open open][write read]'
G.edge['mm-qcamerad']['mediaserver']['fill'] = 'red'
G.add_edge('mm-qcamerad','mediaserver')
G.edge['mm-qcamerad']['mediaserver']['write-read'] = '[open open][write read][append read]'
G.add_edge('mm-qcamerad','mm-qcamerad')
G.edge['mm-qcamerad']['mm-qcamerad']['write-read'] = '[open open][write read]'
G.edge['mm-qcamerad']['mm-qcamerad']['fill'] = 'red'
G.add_edge('mm-qcamerad','mm-qcamerad')
G.edge['mm-qcamerad']['mm-qcamerad']['write-read'] = '[open open][write read][append read]'
G.add_edge('mm-qcamerad','surfaceflinger')
G.edge['mm-qcamerad']['surfaceflinger']['write-read'] = '[open open][write read]'
G.edge['mm-qcamerad']['surfaceflinger']['fill'] = 'red'
G.add_edge('mm-qcamerad','surfaceflinger')
G.edge['mm-qcamerad']['surfaceflinger']['write-read'] = '[open open][write read][append read]'
G.add_edge('mm-qcamerad','system_server')
G.edge['mm-qcamerad']['system_server']['write-read'] = '[open open][write read]'
G.edge['mm-qcamerad']['system_server']['fill'] = 'red'
G.add_edge('mm-qcamerad','system_server')
G.edge['mm-qcamerad']['system_server']['write-read'] = '[open open][write read][append read]'
G.add_edge('surfaceflinger','adbd')
G.edge['surfaceflinger']['adbd']['write-read'] = '[open open]'
G.add_edge('surfaceflinger','appdomain')
G.edge['surfaceflinger']['appdomain']['write-read'] = '[open open]'
G.add_edge('surfaceflinger','bootanim')
G.edge['surfaceflinger']['bootanim']['write-read'] = '[open open]'
G.add_edge('surfaceflinger','dumpstate')
G.edge['surfaceflinger']['dumpstate']['write-read'] = '[open open]'
G.add_edge('surfaceflinger','mediaserver')
G.edge['surfaceflinger']['mediaserver']['write-read'] = '[open open]'
G.add_edge('surfaceflinger','mm-qcamerad')
G.edge['surfaceflinger']['mm-qcamerad']['write-read'] = '[open open]'
G.add_edge('surfaceflinger','surfaceflinger')
G.edge['surfaceflinger']['surfaceflinger']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open]'
G.add_edge('surfaceflinger','system_server')
G.edge['surfaceflinger']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open]'
G.add_edge('surfaceflinger','adbd')
G.edge['surfaceflinger']['adbd']['write-read'] = '[open open][write read]'
G.edge['surfaceflinger']['adbd']['fill'] = 'red'
G.add_edge('surfaceflinger','adbd')
G.edge['surfaceflinger']['adbd']['write-read'] = '[open open][write read][append read]'
G.add_edge('surfaceflinger','appdomain')
G.edge['surfaceflinger']['appdomain']['write-read'] = '[open open][write read]'
G.edge['surfaceflinger']['appdomain']['fill'] = 'red'
G.add_edge('surfaceflinger','appdomain')
G.edge['surfaceflinger']['appdomain']['write-read'] = '[open open][write read][append read]'
G.add_edge('surfaceflinger','bootanim')
G.edge['surfaceflinger']['bootanim']['write-read'] = '[open open][write read]'
G.edge['surfaceflinger']['bootanim']['fill'] = 'red'
G.add_edge('surfaceflinger','bootanim')
G.edge['surfaceflinger']['bootanim']['write-read'] = '[open open][write read][append read]'
G.add_edge('surfaceflinger','dumpstate')
G.edge['surfaceflinger']['dumpstate']['write-read'] = '[open open][write read]'
G.edge['surfaceflinger']['dumpstate']['fill'] = 'red'
G.add_edge('surfaceflinger','dumpstate')
G.edge['surfaceflinger']['dumpstate']['write-read'] = '[open open][write read][append read]'
G.add_edge('surfaceflinger','mediaserver')
G.edge['surfaceflinger']['mediaserver']['write-read'] = '[open open][write read]'
G.edge['surfaceflinger']['mediaserver']['fill'] = 'red'
G.add_edge('surfaceflinger','mediaserver')
G.edge['surfaceflinger']['mediaserver']['write-read'] = '[open open][write read][append read]'
G.add_edge('surfaceflinger','mm-qcamerad')
G.edge['surfaceflinger']['mm-qcamerad']['write-read'] = '[open open][write read]'
G.edge['surfaceflinger']['mm-qcamerad']['fill'] = 'red'
G.add_edge('surfaceflinger','mm-qcamerad')
G.edge['surfaceflinger']['mm-qcamerad']['write-read'] = '[open open][write read][append read]'
G.add_edge('surfaceflinger','surfaceflinger')
G.edge['surfaceflinger']['surfaceflinger']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read]'
G.edge['surfaceflinger']['surfaceflinger']['fill'] = 'red'
G.add_edge('surfaceflinger','surfaceflinger')
G.edge['surfaceflinger']['surfaceflinger']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read]'
G.add_edge('surfaceflinger','system_server')
G.edge['surfaceflinger']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read]'
G.edge['surfaceflinger']['system_server']['fill'] = 'red'
G.add_edge('surfaceflinger','system_server')
G.edge['surfaceflinger']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read]'
G.add_edge('system_server','adbd')
G.edge['system_server']['adbd']['write-read'] = '[write read][add_name search][open open]'
G.add_edge('system_server','appdomain')
G.edge['system_server']['appdomain']['write-read'] = '[open open]'
G.add_edge('system_server','bootanim')
G.edge['system_server']['bootanim']['write-read'] = '[open open]'
G.add_edge('system_server','dumpstate')
G.edge['system_server']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('system_server','mediaserver')
G.edge['system_server']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('system_server','mm-qcamerad')
G.edge['system_server']['mm-qcamerad']['write-read'] = '[open open]'
G.add_edge('system_server','surfaceflinger')
G.edge['system_server']['surfaceflinger']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open]'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open]'
G.add_edge('system_server','adbd')
G.edge['system_server']['adbd']['write-read'] = '[write read][add_name search][open open][write read]'
G.edge['system_server']['adbd']['fill'] = 'red'
G.add_edge('system_server','adbd')
G.edge['system_server']['adbd']['write-read'] = '[write read][add_name search][open open][write read][append read]'
G.add_edge('system_server','appdomain')
G.edge['system_server']['appdomain']['write-read'] = '[open open][write read]'
G.edge['system_server']['appdomain']['fill'] = 'red'
G.add_edge('system_server','appdomain')
G.edge['system_server']['appdomain']['write-read'] = '[open open][write read][append read]'
G.add_edge('system_server','bootanim')
G.edge['system_server']['bootanim']['write-read'] = '[open open][write read]'
G.edge['system_server']['bootanim']['fill'] = 'red'
G.add_edge('system_server','bootanim')
G.edge['system_server']['bootanim']['write-read'] = '[open open][write read][append read]'
G.add_edge('system_server','dumpstate')
G.edge['system_server']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['system_server']['dumpstate']['fill'] = 'red'
G.add_edge('system_server','dumpstate')
G.edge['system_server']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('system_server','mediaserver')
G.edge['system_server']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read]'
G.edge['system_server']['mediaserver']['fill'] = 'red'
G.add_edge('system_server','mediaserver')
G.edge['system_server']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('system_server','mm-qcamerad')
G.edge['system_server']['mm-qcamerad']['write-read'] = '[open open][write read]'
G.edge['system_server']['mm-qcamerad']['fill'] = 'red'
G.add_edge('system_server','mm-qcamerad')
G.edge['system_server']['mm-qcamerad']['write-read'] = '[open open][write read][append read]'
G.add_edge('system_server','surfaceflinger')
G.edge['system_server']['surfaceflinger']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read]'
G.edge['system_server']['surfaceflinger']['fill'] = 'red'
G.add_edge('system_server','surfaceflinger')
G.edge['system_server']['surfaceflinger']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read]'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read]'
G.edge['system_server']['system_server']['fill'] = 'red'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read]'
app = Viewer(G)
app.mainloop()