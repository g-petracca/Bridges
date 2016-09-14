import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('adbd','adbd')
G.edge['adbd']['adbd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('adbd','binderservicedomain')
G.edge['adbd']['binderservicedomain']['write-read'] = '[open open]'
G.add_edge('adbd','bugreport')
G.edge['adbd']['bugreport']['write-read'] = '[open open]'
G.add_edge('adbd','dumpstate')
G.edge['adbd']['dumpstate']['write-read'] = '[open open][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('adbd','dumpsys')
G.edge['adbd']['dumpsys']['write-read'] = '[open open]'
G.add_edge('adbd','imscm')
G.edge['adbd']['imscm']['write-read'] = '[open open]'
G.add_edge('adbd','logwrapper')
G.edge['adbd']['logwrapper']['write-read'] = '[open open]'
G.add_edge('adbd','mediaserver')
G.edge['adbd']['mediaserver']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('adbd','netd')
G.edge['adbd']['netd']['write-read'] = '[open open]'
G.add_edge('adbd','ppp')
G.edge['adbd']['ppp']['write-read'] = '[open open]'
G.add_edge('adbd','pppoewrapper')
G.edge['adbd']['pppoewrapper']['write-read'] = '[open open]'
G.add_edge('adbd','samsung_app')
G.edge['adbd']['samsung_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('adbd','shell')
G.edge['adbd']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('adbd','system_server')
G.edge['adbd']['system_server']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('adbd','untrusteddomain')
G.edge['adbd']['untrusteddomain']['write-read'] = '[open open]'
G.add_edge('adbd','vold')
G.edge['adbd']['vold']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('adbd','ppp')
G.edge['adbd']['ppp']['write-read'] = '[open open][setattr getattr]'
G.add_edge('adbd','pppoewrapper')
G.edge['adbd']['pppoewrapper']['write-read'] = '[open open][setattr getattr]'
G.add_edge('adbd','adbd')
G.edge['adbd']['adbd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['adbd']['adbd']['fill'] = 'red'
G.add_edge('adbd','adbd')
G.edge['adbd']['adbd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('adbd','appdomain')
G.edge['adbd']['appdomain']['write-read'] = '[open open][write read][append read][write read]'
G.edge['adbd']['appdomain']['fill'] = 'red'
G.add_edge('adbd','binderservicedomain')
G.edge['adbd']['binderservicedomain']['write-read'] = '[open open][write read]'
G.edge['adbd']['binderservicedomain']['fill'] = 'red'
G.add_edge('adbd','binderservicedomain')
G.edge['adbd']['binderservicedomain']['write-read'] = '[open open][write read][append read]'
G.add_edge('adbd','bluetooth')
G.edge['adbd']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['adbd']['bluetooth']['fill'] = 'red'
G.add_edge('adbd','bugreport')
G.edge['adbd']['bugreport']['write-read'] = '[open open][write read]'
G.edge['adbd']['bugreport']['fill'] = 'red'
G.add_edge('adbd','bugreport')
G.edge['adbd']['bugreport']['write-read'] = '[open open][write read][append read]'
G.add_edge('adbd','dumpstate')
G.edge['adbd']['dumpstate']['write-read'] = '[open open][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['adbd']['dumpstate']['fill'] = 'red'
G.add_edge('adbd','dumpstate')
G.edge['adbd']['dumpstate']['write-read'] = '[open open][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('adbd','dumpsys')
G.edge['adbd']['dumpsys']['write-read'] = '[open open][write read]'
G.edge['adbd']['dumpsys']['fill'] = 'red'
G.add_edge('adbd','dumpsys')
G.edge['adbd']['dumpsys']['write-read'] = '[open open][write read][append read]'
G.add_edge('adbd','imscm')
G.edge['adbd']['imscm']['write-read'] = '[open open][write read]'
G.edge['adbd']['imscm']['fill'] = 'red'
G.add_edge('adbd','imscm')
G.edge['adbd']['imscm']['write-read'] = '[open open][write read][append read]'
G.add_edge('adbd','irsc_util')
G.edge['adbd']['irsc_util']['write-read'] = '[write read]'
G.edge['adbd']['irsc_util']['fill'] = 'red'
G.add_edge('adbd','logwrapper')
G.edge['adbd']['logwrapper']['write-read'] = '[open open][write read]'
G.edge['adbd']['logwrapper']['fill'] = 'red'
G.add_edge('adbd','logwrapper')
G.edge['adbd']['logwrapper']['write-read'] = '[open open][write read][append read]'
G.add_edge('adbd','mediaserver')
G.edge['adbd']['mediaserver']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read]'
G.edge['adbd']['mediaserver']['fill'] = 'red'
G.add_edge('adbd','mediaserver')
G.edge['adbd']['mediaserver']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('adbd','netd')
G.edge['adbd']['netd']['write-read'] = '[open open][write read]'
G.edge['adbd']['netd']['fill'] = 'red'
G.add_edge('adbd','netd')
G.edge['adbd']['netd']['write-read'] = '[open open][write read][append read]'
G.add_edge('adbd','newAttr49')
G.edge['adbd']['newAttr49']['write-read'] = '[write read]'
G.edge['adbd']['newAttr49']['fill'] = 'red'
G.add_edge('adbd','newAttr9')
G.edge['adbd']['newAttr9']['write-read'] = '[write read]'
G.edge['adbd']['newAttr9']['fill'] = 'red'
G.add_edge('adbd','radio')
G.edge['adbd']['radio']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['adbd']['radio']['fill'] = 'red'
G.add_edge('adbd','runas')
G.edge['adbd']['runas']['write-read'] = '[write read]'
G.edge['adbd']['runas']['fill'] = 'red'
G.add_edge('adbd','samsung_app')
G.edge['adbd']['samsung_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['adbd']['samsung_app']['fill'] = 'red'
G.add_edge('adbd','samsung_app')
G.edge['adbd']['samsung_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('adbd','shell')
G.edge['adbd']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['adbd']['shell']['fill'] = 'red'
G.add_edge('adbd','shell')
G.edge['adbd']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('adbd','surfaceflinger')
G.edge['adbd']['surfaceflinger']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read]'
G.edge['adbd']['surfaceflinger']['fill'] = 'red'
G.add_edge('adbd','system_server')
G.edge['adbd']['system_server']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read]'
G.edge['adbd']['system_server']['fill'] = 'red'
G.add_edge('adbd','system_server')
G.edge['adbd']['system_server']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('adbd','untrusteddomain')
G.edge['adbd']['untrusteddomain']['write-read'] = '[open open][write read]'
G.edge['adbd']['untrusteddomain']['fill'] = 'red'
G.add_edge('adbd','untrusteddomain')
G.edge['adbd']['untrusteddomain']['write-read'] = '[open open][write read][append read]'
G.add_edge('adbd','vold')
G.edge['adbd']['vold']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read]'
G.edge['adbd']['vold']['fill'] = 'red'
G.add_edge('adbd','vold')
G.edge['adbd']['vold']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('appdomain','ppp')
G.edge['appdomain']['ppp']['write-read'] = '[setattr getattr]'
G.add_edge('appdomain','pppoewrapper')
G.edge['appdomain']['pppoewrapper']['write-read'] = '[setattr getattr]'
G.add_edge('appdomain','adbd')
G.edge['appdomain']['adbd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['appdomain']['adbd']['fill'] = 'red'
G.add_edge('appdomain','adbd')
G.edge['appdomain']['adbd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read]'
G.add_edge('appdomain','appdomain')
G.edge['appdomain']['appdomain']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read]'
G.edge['appdomain']['appdomain']['fill'] = 'red'
G.add_edge('appdomain','binderservicedomain')
G.edge['appdomain']['binderservicedomain']['write-read'] = '[write read]'
G.edge['appdomain']['binderservicedomain']['fill'] = 'red'
G.add_edge('appdomain','binderservicedomain')
G.edge['appdomain']['binderservicedomain']['write-read'] = '[write read][append read]'
G.add_edge('appdomain','bluetooth')
G.edge['appdomain']['bluetooth']['write-read'] = '[write read]'
G.edge['appdomain']['bluetooth']['fill'] = 'red'
G.add_edge('appdomain','bugreport')
G.edge['appdomain']['bugreport']['write-read'] = '[write read]'
G.edge['appdomain']['bugreport']['fill'] = 'red'
G.add_edge('appdomain','bugreport')
G.edge['appdomain']['bugreport']['write-read'] = '[write read][append read]'
G.add_edge('appdomain','dumpstate')
G.edge['appdomain']['dumpstate']['write-read'] = '[open open][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][write read]'
G.edge['appdomain']['dumpstate']['fill'] = 'red'
G.add_edge('appdomain','dumpstate')
G.edge['appdomain']['dumpstate']['write-read'] = '[open open][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][write read][append read]'
G.add_edge('appdomain','dumpsys')
G.edge['appdomain']['dumpsys']['write-read'] = '[write read]'
G.edge['appdomain']['dumpsys']['fill'] = 'red'
G.add_edge('appdomain','dumpsys')
G.edge['appdomain']['dumpsys']['write-read'] = '[write read][append read]'
G.add_edge('appdomain','imscm')
G.edge['appdomain']['imscm']['write-read'] = '[write read]'
G.edge['appdomain']['imscm']['fill'] = 'red'
G.add_edge('appdomain','imscm')
G.edge['appdomain']['imscm']['write-read'] = '[write read][append read]'
G.add_edge('appdomain','irsc_util')
G.edge['appdomain']['irsc_util']['write-read'] = '[write read]'
G.edge['appdomain']['irsc_util']['fill'] = 'red'
G.add_edge('appdomain','logwrapper')
G.edge['appdomain']['logwrapper']['write-read'] = '[write read]'
G.edge['appdomain']['logwrapper']['fill'] = 'red'
G.add_edge('appdomain','logwrapper')
G.edge['appdomain']['logwrapper']['write-read'] = '[write read][append read]'
G.add_edge('appdomain','mediaserver')
G.edge['appdomain']['mediaserver']['write-read'] = '[open open][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['appdomain']['mediaserver']['fill'] = 'red'
G.add_edge('appdomain','mediaserver')
G.edge['appdomain']['mediaserver']['write-read'] = '[open open][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read]'
G.add_edge('appdomain','netd')
G.edge['appdomain']['netd']['write-read'] = '[write read]'
G.edge['appdomain']['netd']['fill'] = 'red'
G.add_edge('appdomain','netd')
G.edge['appdomain']['netd']['write-read'] = '[write read][append read]'
G.add_edge('appdomain','newAttr49')
G.edge['appdomain']['newAttr49']['write-read'] = '[write read]'
G.edge['appdomain']['newAttr49']['fill'] = 'red'
G.add_edge('appdomain','newAttr9')
G.edge['appdomain']['newAttr9']['write-read'] = '[write read]'
G.edge['appdomain']['newAttr9']['fill'] = 'red'
G.add_edge('appdomain','radio')
G.edge['appdomain']['radio']['write-read'] = '[setattr getattr][open open][write read][append read][write read]'
G.edge['appdomain']['radio']['fill'] = 'red'
G.add_edge('appdomain','runas')
G.edge['appdomain']['runas']['write-read'] = '[open open][write read][append read][write read]'
G.edge['appdomain']['runas']['fill'] = 'red'
G.add_edge('appdomain','samsung_app')
G.edge['appdomain']['samsung_app']['write-read'] = '[write read]'
G.edge['appdomain']['samsung_app']['fill'] = 'red'
G.add_edge('appdomain','samsung_app')
G.edge['appdomain']['samsung_app']['write-read'] = '[write read][append read]'
G.add_edge('appdomain','shell')
G.edge['appdomain']['shell']['write-read'] = '[write read]'
G.edge['appdomain']['shell']['fill'] = 'red'
G.add_edge('appdomain','shell')
G.edge['appdomain']['shell']['write-read'] = '[write read][append read]'
G.add_edge('appdomain','surfaceflinger')
G.edge['appdomain']['surfaceflinger']['write-read'] = '[open open][write read][append read][write read]'
G.edge['appdomain']['surfaceflinger']['fill'] = 'red'
G.add_edge('appdomain','system_server')
G.edge['appdomain']['system_server']['write-read'] = '[open open][write read][append read][setattr getattr][add_name search][remove_name search][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open execmod][write read]'
G.edge['appdomain']['system_server']['fill'] = 'red'
G.add_edge('appdomain','system_server')
G.edge['appdomain']['system_server']['write-read'] = '[open open][write read][append read][setattr getattr][add_name search][remove_name search][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open execmod][write read][append read]'
G.add_edge('appdomain','untrusteddomain')
G.edge['appdomain']['untrusteddomain']['write-read'] = '[write read]'
G.edge['appdomain']['untrusteddomain']['fill'] = 'red'
G.add_edge('appdomain','untrusteddomain')
G.edge['appdomain']['untrusteddomain']['write-read'] = '[write read][append read]'
G.add_edge('appdomain','vold')
G.edge['appdomain']['vold']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][write read]'
G.edge['appdomain']['vold']['fill'] = 'red'
G.add_edge('appdomain','vold')
G.edge['appdomain']['vold']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][write read][append read]'
G.add_edge('binderservicedomain','adbd')
G.edge['binderservicedomain']['adbd']['write-read'] = '[open open]'
G.add_edge('binderservicedomain','binderservicedomain')
G.edge['binderservicedomain']['binderservicedomain']['write-read'] = '[open open]'
G.add_edge('binderservicedomain','bugreport')
G.edge['binderservicedomain']['bugreport']['write-read'] = '[open open]'
G.add_edge('binderservicedomain','dumpstate')
G.edge['binderservicedomain']['dumpstate']['write-read'] = '[open open]'
G.add_edge('binderservicedomain','dumpsys')
G.edge['binderservicedomain']['dumpsys']['write-read'] = '[open open]'
G.add_edge('binderservicedomain','imscm')
G.edge['binderservicedomain']['imscm']['write-read'] = '[open open]'
G.add_edge('binderservicedomain','logwrapper')
G.edge['binderservicedomain']['logwrapper']['write-read'] = '[open open]'
G.add_edge('binderservicedomain','mediaserver')
G.edge['binderservicedomain']['mediaserver']['write-read'] = '[open open]'
G.add_edge('binderservicedomain','netd')
G.edge['binderservicedomain']['netd']['write-read'] = '[open open]'
G.add_edge('binderservicedomain','ppp')
G.edge['binderservicedomain']['ppp']['write-read'] = '[open open]'
G.add_edge('binderservicedomain','pppoewrapper')
G.edge['binderservicedomain']['pppoewrapper']['write-read'] = '[open open]'
G.add_edge('binderservicedomain','samsung_app')
G.edge['binderservicedomain']['samsung_app']['write-read'] = '[open open]'
G.add_edge('binderservicedomain','shell')
G.edge['binderservicedomain']['shell']['write-read'] = '[open open]'
G.add_edge('binderservicedomain','system_server')
G.edge['binderservicedomain']['system_server']['write-read'] = '[open open]'
G.add_edge('binderservicedomain','untrusteddomain')
G.edge['binderservicedomain']['untrusteddomain']['write-read'] = '[open open]'
G.add_edge('binderservicedomain','vold')
G.edge['binderservicedomain']['vold']['write-read'] = '[open open]'
G.add_edge('binderservicedomain','ppp')
G.edge['binderservicedomain']['ppp']['write-read'] = '[open open][setattr getattr]'
G.add_edge('binderservicedomain','pppoewrapper')
G.edge['binderservicedomain']['pppoewrapper']['write-read'] = '[open open][setattr getattr]'
G.add_edge('binderservicedomain','adbd')
G.edge['binderservicedomain']['adbd']['write-read'] = '[open open][write read]'
G.edge['binderservicedomain']['adbd']['fill'] = 'red'
G.add_edge('binderservicedomain','adbd')
G.edge['binderservicedomain']['adbd']['write-read'] = '[open open][write read][append read]'
G.add_edge('binderservicedomain','appdomain')
G.edge['binderservicedomain']['appdomain']['write-read'] = '[write read]'
G.edge['binderservicedomain']['appdomain']['fill'] = 'red'
G.add_edge('binderservicedomain','binderservicedomain')
G.edge['binderservicedomain']['binderservicedomain']['write-read'] = '[open open][write read]'
G.edge['binderservicedomain']['binderservicedomain']['fill'] = 'red'
G.add_edge('binderservicedomain','binderservicedomain')
G.edge['binderservicedomain']['binderservicedomain']['write-read'] = '[open open][write read][append read]'
G.add_edge('binderservicedomain','bluetooth')
G.edge['binderservicedomain']['bluetooth']['write-read'] = '[write read]'
G.edge['binderservicedomain']['bluetooth']['fill'] = 'red'
G.add_edge('binderservicedomain','bugreport')
G.edge['binderservicedomain']['bugreport']['write-read'] = '[open open][write read]'
G.edge['binderservicedomain']['bugreport']['fill'] = 'red'
G.add_edge('binderservicedomain','bugreport')
G.edge['binderservicedomain']['bugreport']['write-read'] = '[open open][write read][append read]'
G.add_edge('binderservicedomain','dumpstate')
G.edge['binderservicedomain']['dumpstate']['write-read'] = '[open open][write read]'
G.edge['binderservicedomain']['dumpstate']['fill'] = 'red'
G.add_edge('binderservicedomain','dumpstate')
G.edge['binderservicedomain']['dumpstate']['write-read'] = '[open open][write read][append read]'
G.add_edge('binderservicedomain','dumpsys')
G.edge['binderservicedomain']['dumpsys']['write-read'] = '[open open][write read]'
G.edge['binderservicedomain']['dumpsys']['fill'] = 'red'
G.add_edge('binderservicedomain','dumpsys')
G.edge['binderservicedomain']['dumpsys']['write-read'] = '[open open][write read][append read]'
G.add_edge('binderservicedomain','imscm')
G.edge['binderservicedomain']['imscm']['write-read'] = '[open open][write read]'
G.edge['binderservicedomain']['imscm']['fill'] = 'red'
G.add_edge('binderservicedomain','imscm')
G.edge['binderservicedomain']['imscm']['write-read'] = '[open open][write read][append read]'
G.add_edge('binderservicedomain','irsc_util')
G.edge['binderservicedomain']['irsc_util']['write-read'] = '[write read]'
G.edge['binderservicedomain']['irsc_util']['fill'] = 'red'
G.add_edge('binderservicedomain','logwrapper')
G.edge['binderservicedomain']['logwrapper']['write-read'] = '[open open][write read]'
G.edge['binderservicedomain']['logwrapper']['fill'] = 'red'
G.add_edge('binderservicedomain','logwrapper')
G.edge['binderservicedomain']['logwrapper']['write-read'] = '[open open][write read][append read]'
G.add_edge('binderservicedomain','mediaserver')
G.edge['binderservicedomain']['mediaserver']['write-read'] = '[open open][write read]'
G.edge['binderservicedomain']['mediaserver']['fill'] = 'red'
G.add_edge('binderservicedomain','mediaserver')
G.edge['binderservicedomain']['mediaserver']['write-read'] = '[open open][write read][append read]'
G.add_edge('binderservicedomain','netd')
G.edge['binderservicedomain']['netd']['write-read'] = '[open open][write read]'
G.edge['binderservicedomain']['netd']['fill'] = 'red'
G.add_edge('binderservicedomain','netd')
G.edge['binderservicedomain']['netd']['write-read'] = '[open open][write read][append read]'
G.add_edge('binderservicedomain','newAttr49')
G.edge['binderservicedomain']['newAttr49']['write-read'] = '[write read]'
G.edge['binderservicedomain']['newAttr49']['fill'] = 'red'
G.add_edge('binderservicedomain','newAttr9')
G.edge['binderservicedomain']['newAttr9']['write-read'] = '[write read]'
G.edge['binderservicedomain']['newAttr9']['fill'] = 'red'
G.add_edge('binderservicedomain','radio')
G.edge['binderservicedomain']['radio']['write-read'] = '[write read]'
G.edge['binderservicedomain']['radio']['fill'] = 'red'
G.add_edge('binderservicedomain','runas')
G.edge['binderservicedomain']['runas']['write-read'] = '[write read]'
G.edge['binderservicedomain']['runas']['fill'] = 'red'
G.add_edge('binderservicedomain','samsung_app')
G.edge['binderservicedomain']['samsung_app']['write-read'] = '[open open][write read]'
G.edge['binderservicedomain']['samsung_app']['fill'] = 'red'
G.add_edge('binderservicedomain','samsung_app')
G.edge['binderservicedomain']['samsung_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('binderservicedomain','shell')
G.edge['binderservicedomain']['shell']['write-read'] = '[open open][write read]'
G.edge['binderservicedomain']['shell']['fill'] = 'red'
G.add_edge('binderservicedomain','shell')
G.edge['binderservicedomain']['shell']['write-read'] = '[open open][write read][append read]'
G.add_edge('binderservicedomain','surfaceflinger')
G.edge['binderservicedomain']['surfaceflinger']['write-read'] = '[write read]'
G.edge['binderservicedomain']['surfaceflinger']['fill'] = 'red'
G.add_edge('binderservicedomain','system_server')
G.edge['binderservicedomain']['system_server']['write-read'] = '[open open][write read]'
G.edge['binderservicedomain']['system_server']['fill'] = 'red'
G.add_edge('binderservicedomain','system_server')
G.edge['binderservicedomain']['system_server']['write-read'] = '[open open][write read][append read]'
G.add_edge('binderservicedomain','untrusteddomain')
G.edge['binderservicedomain']['untrusteddomain']['write-read'] = '[open open][write read]'
G.edge['binderservicedomain']['untrusteddomain']['fill'] = 'red'
G.add_edge('binderservicedomain','untrusteddomain')
G.edge['binderservicedomain']['untrusteddomain']['write-read'] = '[open open][write read][append read]'
G.add_edge('binderservicedomain','vold')
G.edge['binderservicedomain']['vold']['write-read'] = '[open open][write read]'
G.edge['binderservicedomain']['vold']['fill'] = 'red'
G.add_edge('binderservicedomain','vold')
G.edge['binderservicedomain']['vold']['write-read'] = '[open open][write read][append read]'
G.add_edge('bluetooth','adbd')
G.edge['bluetooth']['adbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['bluetooth']['adbd']['fill'] = 'red'
G.add_edge('bluetooth','adbd')
G.edge['bluetooth']['adbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read]'
G.add_edge('bluetooth','appdomain')
G.edge['bluetooth']['appdomain']['write-read'] = '[write read]'
G.edge['bluetooth']['appdomain']['fill'] = 'red'
G.add_edge('bluetooth','binderservicedomain')
G.edge['bluetooth']['binderservicedomain']['write-read'] = '[write read]'
G.edge['bluetooth']['binderservicedomain']['fill'] = 'red'
G.add_edge('bluetooth','binderservicedomain')
G.edge['bluetooth']['binderservicedomain']['write-read'] = '[write read][append read]'
G.add_edge('bluetooth','bluetooth')
G.edge['bluetooth']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read]'
G.edge['bluetooth']['bluetooth']['fill'] = 'red'
G.add_edge('bluetooth','bugreport')
G.edge['bluetooth']['bugreport']['write-read'] = '[write read]'
G.edge['bluetooth']['bugreport']['fill'] = 'red'
G.add_edge('bluetooth','bugreport')
G.edge['bluetooth']['bugreport']['write-read'] = '[write read][append read]'
G.add_edge('bluetooth','dumpstate')
G.edge['bluetooth']['dumpstate']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['bluetooth']['dumpstate']['fill'] = 'red'
G.add_edge('bluetooth','dumpstate')
G.edge['bluetooth']['dumpstate']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read]'
G.add_edge('bluetooth','dumpsys')
G.edge['bluetooth']['dumpsys']['write-read'] = '[write read]'
G.edge['bluetooth']['dumpsys']['fill'] = 'red'
G.add_edge('bluetooth','dumpsys')
G.edge['bluetooth']['dumpsys']['write-read'] = '[write read][append read]'
G.add_edge('bluetooth','imscm')
G.edge['bluetooth']['imscm']['write-read'] = '[write read]'
G.edge['bluetooth']['imscm']['fill'] = 'red'
G.add_edge('bluetooth','imscm')
G.edge['bluetooth']['imscm']['write-read'] = '[write read][append read]'
G.add_edge('bluetooth','irsc_util')
G.edge['bluetooth']['irsc_util']['write-read'] = '[write read]'
G.edge['bluetooth']['irsc_util']['fill'] = 'red'
G.add_edge('bluetooth','logwrapper')
G.edge['bluetooth']['logwrapper']['write-read'] = '[write read]'
G.edge['bluetooth']['logwrapper']['fill'] = 'red'
G.add_edge('bluetooth','logwrapper')
G.edge['bluetooth']['logwrapper']['write-read'] = '[write read][append read]'
G.add_edge('bluetooth','mediaserver')
G.edge['bluetooth']['mediaserver']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read]'
G.edge['bluetooth']['mediaserver']['fill'] = 'red'
G.add_edge('bluetooth','mediaserver')
G.edge['bluetooth']['mediaserver']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read][append read]'
G.add_edge('bluetooth','netd')
G.edge['bluetooth']['netd']['write-read'] = '[write read]'
G.edge['bluetooth']['netd']['fill'] = 'red'
G.add_edge('bluetooth','netd')
G.edge['bluetooth']['netd']['write-read'] = '[write read][append read]'
G.add_edge('bluetooth','newAttr49')
G.edge['bluetooth']['newAttr49']['write-read'] = '[write read]'
G.edge['bluetooth']['newAttr49']['fill'] = 'red'
G.add_edge('bluetooth','newAttr9')
G.edge['bluetooth']['newAttr9']['write-read'] = '[write read]'
G.edge['bluetooth']['newAttr9']['fill'] = 'red'
G.add_edge('bluetooth','radio')
G.edge['bluetooth']['radio']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['bluetooth']['radio']['fill'] = 'red'
G.add_edge('bluetooth','runas')
G.edge['bluetooth']['runas']['write-read'] = '[write read]'
G.edge['bluetooth']['runas']['fill'] = 'red'
G.add_edge('bluetooth','samsung_app')
G.edge['bluetooth']['samsung_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['bluetooth']['samsung_app']['fill'] = 'red'
G.add_edge('bluetooth','samsung_app')
G.edge['bluetooth']['samsung_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read][append read]'
G.add_edge('bluetooth','shell')
G.edge['bluetooth']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['bluetooth']['shell']['fill'] = 'red'
G.add_edge('bluetooth','shell')
G.edge['bluetooth']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read][append read]'
G.add_edge('bluetooth','surfaceflinger')
G.edge['bluetooth']['surfaceflinger']['write-read'] = '[write read]'
G.edge['bluetooth']['surfaceflinger']['fill'] = 'red'
G.add_edge('bluetooth','system_server')
G.edge['bluetooth']['system_server']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][write read]'
G.edge['bluetooth']['system_server']['fill'] = 'red'
G.add_edge('bluetooth','system_server')
G.edge['bluetooth']['system_server']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][write read][append read]'
G.add_edge('bluetooth','untrusteddomain')
G.edge['bluetooth']['untrusteddomain']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['bluetooth']['untrusteddomain']['fill'] = 'red'
G.add_edge('bluetooth','untrusteddomain')
G.edge['bluetooth']['untrusteddomain']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read][append read]'
G.add_edge('bluetooth','vold')
G.edge['bluetooth']['vold']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read]'
G.edge['bluetooth']['vold']['fill'] = 'red'
G.add_edge('bluetooth','vold')
G.edge['bluetooth']['vold']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read][append read]'
G.add_edge('bugreport','adbd')
G.edge['bugreport']['adbd']['write-read'] = '[open open]'
G.add_edge('bugreport','binderservicedomain')
G.edge['bugreport']['binderservicedomain']['write-read'] = '[open open]'
G.add_edge('bugreport','bugreport')
G.edge['bugreport']['bugreport']['write-read'] = '[open open]'
G.add_edge('bugreport','dumpstate')
G.edge['bugreport']['dumpstate']['write-read'] = '[open open]'
G.add_edge('bugreport','dumpsys')
G.edge['bugreport']['dumpsys']['write-read'] = '[open open]'
G.add_edge('bugreport','imscm')
G.edge['bugreport']['imscm']['write-read'] = '[open open]'
G.add_edge('bugreport','logwrapper')
G.edge['bugreport']['logwrapper']['write-read'] = '[open open]'
G.add_edge('bugreport','mediaserver')
G.edge['bugreport']['mediaserver']['write-read'] = '[open open]'
G.add_edge('bugreport','netd')
G.edge['bugreport']['netd']['write-read'] = '[open open]'
G.add_edge('bugreport','ppp')
G.edge['bugreport']['ppp']['write-read'] = '[open open]'
G.add_edge('bugreport','pppoewrapper')
G.edge['bugreport']['pppoewrapper']['write-read'] = '[open open]'
G.add_edge('bugreport','samsung_app')
G.edge['bugreport']['samsung_app']['write-read'] = '[open open]'
G.add_edge('bugreport','shell')
G.edge['bugreport']['shell']['write-read'] = '[open open]'
G.add_edge('bugreport','system_server')
G.edge['bugreport']['system_server']['write-read'] = '[open open]'
G.add_edge('bugreport','untrusteddomain')
G.edge['bugreport']['untrusteddomain']['write-read'] = '[open open]'
G.add_edge('bugreport','vold')
G.edge['bugreport']['vold']['write-read'] = '[open open]'
G.add_edge('bugreport','ppp')
G.edge['bugreport']['ppp']['write-read'] = '[open open][setattr getattr]'
G.add_edge('bugreport','pppoewrapper')
G.edge['bugreport']['pppoewrapper']['write-read'] = '[open open][setattr getattr]'
G.add_edge('bugreport','adbd')
G.edge['bugreport']['adbd']['write-read'] = '[open open][write read]'
G.edge['bugreport']['adbd']['fill'] = 'red'
G.add_edge('bugreport','adbd')
G.edge['bugreport']['adbd']['write-read'] = '[open open][write read][append read]'
G.add_edge('bugreport','appdomain')
G.edge['bugreport']['appdomain']['write-read'] = '[write read]'
G.edge['bugreport']['appdomain']['fill'] = 'red'
G.add_edge('bugreport','binderservicedomain')
G.edge['bugreport']['binderservicedomain']['write-read'] = '[open open][write read]'
G.edge['bugreport']['binderservicedomain']['fill'] = 'red'
G.add_edge('bugreport','binderservicedomain')
G.edge['bugreport']['binderservicedomain']['write-read'] = '[open open][write read][append read]'
G.add_edge('bugreport','bluetooth')
G.edge['bugreport']['bluetooth']['write-read'] = '[write read]'
G.edge['bugreport']['bluetooth']['fill'] = 'red'
G.add_edge('bugreport','bugreport')
G.edge['bugreport']['bugreport']['write-read'] = '[open open][write read]'
G.edge['bugreport']['bugreport']['fill'] = 'red'
G.add_edge('bugreport','bugreport')
G.edge['bugreport']['bugreport']['write-read'] = '[open open][write read][append read]'
G.add_edge('bugreport','dumpstate')
G.edge['bugreport']['dumpstate']['write-read'] = '[open open][write read]'
G.edge['bugreport']['dumpstate']['fill'] = 'red'
G.add_edge('bugreport','dumpstate')
G.edge['bugreport']['dumpstate']['write-read'] = '[open open][write read][append read]'
G.add_edge('bugreport','dumpsys')
G.edge['bugreport']['dumpsys']['write-read'] = '[open open][write read]'
G.edge['bugreport']['dumpsys']['fill'] = 'red'
G.add_edge('bugreport','dumpsys')
G.edge['bugreport']['dumpsys']['write-read'] = '[open open][write read][append read]'
G.add_edge('bugreport','imscm')
G.edge['bugreport']['imscm']['write-read'] = '[open open][write read]'
G.edge['bugreport']['imscm']['fill'] = 'red'
G.add_edge('bugreport','imscm')
G.edge['bugreport']['imscm']['write-read'] = '[open open][write read][append read]'
G.add_edge('bugreport','irsc_util')
G.edge['bugreport']['irsc_util']['write-read'] = '[write read]'
G.edge['bugreport']['irsc_util']['fill'] = 'red'
G.add_edge('bugreport','logwrapper')
G.edge['bugreport']['logwrapper']['write-read'] = '[open open][write read]'
G.edge['bugreport']['logwrapper']['fill'] = 'red'
G.add_edge('bugreport','logwrapper')
G.edge['bugreport']['logwrapper']['write-read'] = '[open open][write read][append read]'
G.add_edge('bugreport','mediaserver')
G.edge['bugreport']['mediaserver']['write-read'] = '[open open][write read]'
G.edge['bugreport']['mediaserver']['fill'] = 'red'
G.add_edge('bugreport','mediaserver')
G.edge['bugreport']['mediaserver']['write-read'] = '[open open][write read][append read]'
G.add_edge('bugreport','netd')
G.edge['bugreport']['netd']['write-read'] = '[open open][write read]'
G.edge['bugreport']['netd']['fill'] = 'red'
G.add_edge('bugreport','netd')
G.edge['bugreport']['netd']['write-read'] = '[open open][write read][append read]'
G.add_edge('bugreport','newAttr49')
G.edge['bugreport']['newAttr49']['write-read'] = '[write read]'
G.edge['bugreport']['newAttr49']['fill'] = 'red'
G.add_edge('bugreport','newAttr9')
G.edge['bugreport']['newAttr9']['write-read'] = '[write read]'
G.edge['bugreport']['newAttr9']['fill'] = 'red'
G.add_edge('bugreport','radio')
G.edge['bugreport']['radio']['write-read'] = '[write read]'
G.edge['bugreport']['radio']['fill'] = 'red'
G.add_edge('bugreport','runas')
G.edge['bugreport']['runas']['write-read'] = '[write read]'
G.edge['bugreport']['runas']['fill'] = 'red'
G.add_edge('bugreport','samsung_app')
G.edge['bugreport']['samsung_app']['write-read'] = '[open open][write read]'
G.edge['bugreport']['samsung_app']['fill'] = 'red'
G.add_edge('bugreport','samsung_app')
G.edge['bugreport']['samsung_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('bugreport','shell')
G.edge['bugreport']['shell']['write-read'] = '[open open][write read]'
G.edge['bugreport']['shell']['fill'] = 'red'
G.add_edge('bugreport','shell')
G.edge['bugreport']['shell']['write-read'] = '[open open][write read][append read]'
G.add_edge('bugreport','surfaceflinger')
G.edge['bugreport']['surfaceflinger']['write-read'] = '[write read]'
G.edge['bugreport']['surfaceflinger']['fill'] = 'red'
G.add_edge('bugreport','system_server')
G.edge['bugreport']['system_server']['write-read'] = '[open open][write read]'
G.edge['bugreport']['system_server']['fill'] = 'red'
G.add_edge('bugreport','system_server')
G.edge['bugreport']['system_server']['write-read'] = '[open open][write read][append read]'
G.add_edge('bugreport','untrusteddomain')
G.edge['bugreport']['untrusteddomain']['write-read'] = '[open open][write read]'
G.edge['bugreport']['untrusteddomain']['fill'] = 'red'
G.add_edge('bugreport','untrusteddomain')
G.edge['bugreport']['untrusteddomain']['write-read'] = '[open open][write read][append read]'
G.add_edge('bugreport','vold')
G.edge['bugreport']['vold']['write-read'] = '[open open][write read]'
G.edge['bugreport']['vold']['fill'] = 'red'
G.add_edge('bugreport','vold')
G.edge['bugreport']['vold']['write-read'] = '[open open][write read][append read]'
G.add_edge('dumpstate','adbd')
G.edge['dumpstate']['adbd']['write-read'] = '[write read][add_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('dumpstate','binderservicedomain')
G.edge['dumpstate']['binderservicedomain']['write-read'] = '[open open]'
G.add_edge('dumpstate','bugreport')
G.edge['dumpstate']['bugreport']['write-read'] = '[open open]'
G.add_edge('dumpstate','dumpstate')
G.edge['dumpstate']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('dumpstate','dumpsys')
G.edge['dumpstate']['dumpsys']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('dumpstate','imscm')
G.edge['dumpstate']['imscm']['write-read'] = '[open open]'
G.add_edge('dumpstate','logwrapper')
G.edge['dumpstate']['logwrapper']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('dumpstate','mediaserver')
G.edge['dumpstate']['mediaserver']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('dumpstate','netd')
G.edge['dumpstate']['netd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('dumpstate','ppp')
G.edge['dumpstate']['ppp']['write-read'] = '[open open]'
G.add_edge('dumpstate','pppoewrapper')
G.edge['dumpstate']['pppoewrapper']['write-read'] = '[open open]'
G.add_edge('dumpstate','samsung_app')
G.edge['dumpstate']['samsung_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('dumpstate','shell')
G.edge['dumpstate']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('dumpstate','system_server')
G.edge['dumpstate']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('dumpstate','untrusteddomain')
G.edge['dumpstate']['untrusteddomain']['write-read'] = '[open open]'
G.add_edge('dumpstate','vold')
G.edge['dumpstate']['vold']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('dumpstate','ppp')
G.edge['dumpstate']['ppp']['write-read'] = '[open open][setattr getattr]'
G.add_edge('dumpstate','pppoewrapper')
G.edge['dumpstate']['pppoewrapper']['write-read'] = '[open open][setattr getattr]'
G.add_edge('dumpstate','adbd')
G.edge['dumpstate']['adbd']['write-read'] = '[write read][add_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['dumpstate']['adbd']['fill'] = 'red'
G.add_edge('dumpstate','adbd')
G.edge['dumpstate']['adbd']['write-read'] = '[write read][add_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('dumpstate','appdomain')
G.edge['dumpstate']['appdomain']['write-read'] = '[open open][write read][append read][write read]'
G.edge['dumpstate']['appdomain']['fill'] = 'red'
G.add_edge('dumpstate','binderservicedomain')
G.edge['dumpstate']['binderservicedomain']['write-read'] = '[open open][write read]'
G.edge['dumpstate']['binderservicedomain']['fill'] = 'red'
G.add_edge('dumpstate','binderservicedomain')
G.edge['dumpstate']['binderservicedomain']['write-read'] = '[open open][write read][append read]'
G.add_edge('dumpstate','bluetooth')
G.edge['dumpstate']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['dumpstate']['bluetooth']['fill'] = 'red'
G.add_edge('dumpstate','bugreport')
G.edge['dumpstate']['bugreport']['write-read'] = '[open open][write read]'
G.edge['dumpstate']['bugreport']['fill'] = 'red'
G.add_edge('dumpstate','bugreport')
G.edge['dumpstate']['bugreport']['write-read'] = '[open open][write read][append read]'
G.add_edge('dumpstate','dumpstate')
G.edge['dumpstate']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['dumpstate']['dumpstate']['fill'] = 'red'
G.add_edge('dumpstate','dumpstate')
G.edge['dumpstate']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('dumpstate','dumpsys')
G.edge['dumpstate']['dumpsys']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['dumpstate']['dumpsys']['fill'] = 'red'
G.add_edge('dumpstate','dumpsys')
G.edge['dumpstate']['dumpsys']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('dumpstate','imscm')
G.edge['dumpstate']['imscm']['write-read'] = '[open open][write read]'
G.edge['dumpstate']['imscm']['fill'] = 'red'
G.add_edge('dumpstate','imscm')
G.edge['dumpstate']['imscm']['write-read'] = '[open open][write read][append read]'
G.add_edge('dumpstate','irsc_util')
G.edge['dumpstate']['irsc_util']['write-read'] = '[write read]'
G.edge['dumpstate']['irsc_util']['fill'] = 'red'
G.add_edge('dumpstate','logwrapper')
G.edge['dumpstate']['logwrapper']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['dumpstate']['logwrapper']['fill'] = 'red'
G.add_edge('dumpstate','logwrapper')
G.edge['dumpstate']['logwrapper']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('dumpstate','mediaserver')
G.edge['dumpstate']['mediaserver']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['dumpstate']['mediaserver']['fill'] = 'red'
G.add_edge('dumpstate','mediaserver')
G.edge['dumpstate']['mediaserver']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('dumpstate','netd')
G.edge['dumpstate']['netd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read]'
G.edge['dumpstate']['netd']['fill'] = 'red'
G.add_edge('dumpstate','netd')
G.edge['dumpstate']['netd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('dumpstate','newAttr49')
G.edge['dumpstate']['newAttr49']['write-read'] = '[write read]'
G.edge['dumpstate']['newAttr49']['fill'] = 'red'
G.add_edge('dumpstate','newAttr9')
G.edge['dumpstate']['newAttr9']['write-read'] = '[write read]'
G.edge['dumpstate']['newAttr9']['fill'] = 'red'
G.add_edge('dumpstate','radio')
G.edge['dumpstate']['radio']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['dumpstate']['radio']['fill'] = 'red'
G.add_edge('dumpstate','runas')
G.edge['dumpstate']['runas']['write-read'] = '[write read]'
G.edge['dumpstate']['runas']['fill'] = 'red'
G.add_edge('dumpstate','samsung_app')
G.edge['dumpstate']['samsung_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['dumpstate']['samsung_app']['fill'] = 'red'
G.add_edge('dumpstate','samsung_app')
G.edge['dumpstate']['samsung_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('dumpstate','shell')
G.edge['dumpstate']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['dumpstate']['shell']['fill'] = 'red'
G.add_edge('dumpstate','shell')
G.edge['dumpstate']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('dumpstate','surfaceflinger')
G.edge['dumpstate']['surfaceflinger']['write-read'] = '[open open][write read][append read][write read]'
G.edge['dumpstate']['surfaceflinger']['fill'] = 'red'
G.add_edge('dumpstate','system_server')
G.edge['dumpstate']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['dumpstate']['system_server']['fill'] = 'red'
G.add_edge('dumpstate','system_server')
G.edge['dumpstate']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('dumpstate','untrusteddomain')
G.edge['dumpstate']['untrusteddomain']['write-read'] = '[open open][write read]'
G.edge['dumpstate']['untrusteddomain']['fill'] = 'red'
G.add_edge('dumpstate','untrusteddomain')
G.edge['dumpstate']['untrusteddomain']['write-read'] = '[open open][write read][append read]'
G.add_edge('dumpstate','vold')
G.edge['dumpstate']['vold']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['dumpstate']['vold']['fill'] = 'red'
G.add_edge('dumpstate','vold')
G.edge['dumpstate']['vold']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('dumpsys','adbd')
G.edge['dumpsys']['adbd']['write-read'] = '[open open]'
G.add_edge('dumpsys','binderservicedomain')
G.edge['dumpsys']['binderservicedomain']['write-read'] = '[open open]'
G.add_edge('dumpsys','bugreport')
G.edge['dumpsys']['bugreport']['write-read'] = '[open open]'
G.add_edge('dumpsys','dumpstate')
G.edge['dumpsys']['dumpstate']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('dumpsys','dumpsys')
G.edge['dumpsys']['dumpsys']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('dumpsys','imscm')
G.edge['dumpsys']['imscm']['write-read'] = '[open open]'
G.add_edge('dumpsys','logwrapper')
G.edge['dumpsys']['logwrapper']['write-read'] = '[open open]'
G.add_edge('dumpsys','mediaserver')
G.edge['dumpsys']['mediaserver']['write-read'] = '[open open]'
G.add_edge('dumpsys','netd')
G.edge['dumpsys']['netd']['write-read'] = '[open open]'
G.add_edge('dumpsys','ppp')
G.edge['dumpsys']['ppp']['write-read'] = '[open open]'
G.add_edge('dumpsys','pppoewrapper')
G.edge['dumpsys']['pppoewrapper']['write-read'] = '[open open]'
G.add_edge('dumpsys','samsung_app')
G.edge['dumpsys']['samsung_app']['write-read'] = '[open open]'
G.add_edge('dumpsys','shell')
G.edge['dumpsys']['shell']['write-read'] = '[open open]'
G.add_edge('dumpsys','system_server')
G.edge['dumpsys']['system_server']['write-read'] = '[open open]'
G.add_edge('dumpsys','untrusteddomain')
G.edge['dumpsys']['untrusteddomain']['write-read'] = '[open open]'
G.add_edge('dumpsys','vold')
G.edge['dumpsys']['vold']['write-read'] = '[open open]'
G.add_edge('dumpsys','ppp')
G.edge['dumpsys']['ppp']['write-read'] = '[open open][setattr getattr]'
G.add_edge('dumpsys','pppoewrapper')
G.edge['dumpsys']['pppoewrapper']['write-read'] = '[open open][setattr getattr]'
G.add_edge('dumpsys','adbd')
G.edge['dumpsys']['adbd']['write-read'] = '[open open][write read]'
G.edge['dumpsys']['adbd']['fill'] = 'red'
G.add_edge('dumpsys','adbd')
G.edge['dumpsys']['adbd']['write-read'] = '[open open][write read][append read]'
G.add_edge('dumpsys','appdomain')
G.edge['dumpsys']['appdomain']['write-read'] = '[write read]'
G.edge['dumpsys']['appdomain']['fill'] = 'red'
G.add_edge('dumpsys','binderservicedomain')
G.edge['dumpsys']['binderservicedomain']['write-read'] = '[open open][write read]'
G.edge['dumpsys']['binderservicedomain']['fill'] = 'red'
G.add_edge('dumpsys','binderservicedomain')
G.edge['dumpsys']['binderservicedomain']['write-read'] = '[open open][write read][append read]'
G.add_edge('dumpsys','bluetooth')
G.edge['dumpsys']['bluetooth']['write-read'] = '[write read]'
G.edge['dumpsys']['bluetooth']['fill'] = 'red'
G.add_edge('dumpsys','bugreport')
G.edge['dumpsys']['bugreport']['write-read'] = '[open open][write read]'
G.edge['dumpsys']['bugreport']['fill'] = 'red'
G.add_edge('dumpsys','bugreport')
G.edge['dumpsys']['bugreport']['write-read'] = '[open open][write read][append read]'
G.add_edge('dumpsys','dumpstate')
G.edge['dumpsys']['dumpstate']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['dumpsys']['dumpstate']['fill'] = 'red'
G.add_edge('dumpsys','dumpstate')
G.edge['dumpsys']['dumpstate']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('dumpsys','dumpsys')
G.edge['dumpsys']['dumpsys']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['dumpsys']['dumpsys']['fill'] = 'red'
G.add_edge('dumpsys','dumpsys')
G.edge['dumpsys']['dumpsys']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('dumpsys','imscm')
G.edge['dumpsys']['imscm']['write-read'] = '[open open][write read]'
G.edge['dumpsys']['imscm']['fill'] = 'red'
G.add_edge('dumpsys','imscm')
G.edge['dumpsys']['imscm']['write-read'] = '[open open][write read][append read]'
G.add_edge('dumpsys','irsc_util')
G.edge['dumpsys']['irsc_util']['write-read'] = '[write read]'
G.edge['dumpsys']['irsc_util']['fill'] = 'red'
G.add_edge('dumpsys','logwrapper')
G.edge['dumpsys']['logwrapper']['write-read'] = '[open open][write read]'
G.edge['dumpsys']['logwrapper']['fill'] = 'red'
G.add_edge('dumpsys','logwrapper')
G.edge['dumpsys']['logwrapper']['write-read'] = '[open open][write read][append read]'
G.add_edge('dumpsys','mediaserver')
G.edge['dumpsys']['mediaserver']['write-read'] = '[open open][write read]'
G.edge['dumpsys']['mediaserver']['fill'] = 'red'
G.add_edge('dumpsys','mediaserver')
G.edge['dumpsys']['mediaserver']['write-read'] = '[open open][write read][append read]'
G.add_edge('dumpsys','netd')
G.edge['dumpsys']['netd']['write-read'] = '[open open][write read]'
G.edge['dumpsys']['netd']['fill'] = 'red'
G.add_edge('dumpsys','netd')
G.edge['dumpsys']['netd']['write-read'] = '[open open][write read][append read]'
G.add_edge('dumpsys','newAttr49')
G.edge['dumpsys']['newAttr49']['write-read'] = '[write read]'
G.edge['dumpsys']['newAttr49']['fill'] = 'red'
G.add_edge('dumpsys','newAttr9')
G.edge['dumpsys']['newAttr9']['write-read'] = '[write read]'
G.edge['dumpsys']['newAttr9']['fill'] = 'red'
G.add_edge('dumpsys','radio')
G.edge['dumpsys']['radio']['write-read'] = '[write read]'
G.edge['dumpsys']['radio']['fill'] = 'red'
G.add_edge('dumpsys','runas')
G.edge['dumpsys']['runas']['write-read'] = '[write read]'
G.edge['dumpsys']['runas']['fill'] = 'red'
G.add_edge('dumpsys','samsung_app')
G.edge['dumpsys']['samsung_app']['write-read'] = '[open open][write read]'
G.edge['dumpsys']['samsung_app']['fill'] = 'red'
G.add_edge('dumpsys','samsung_app')
G.edge['dumpsys']['samsung_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('dumpsys','shell')
G.edge['dumpsys']['shell']['write-read'] = '[open open][write read]'
G.edge['dumpsys']['shell']['fill'] = 'red'
G.add_edge('dumpsys','shell')
G.edge['dumpsys']['shell']['write-read'] = '[open open][write read][append read]'
G.add_edge('dumpsys','surfaceflinger')
G.edge['dumpsys']['surfaceflinger']['write-read'] = '[write read]'
G.edge['dumpsys']['surfaceflinger']['fill'] = 'red'
G.add_edge('dumpsys','system_server')
G.edge['dumpsys']['system_server']['write-read'] = '[open open][write read]'
G.edge['dumpsys']['system_server']['fill'] = 'red'
G.add_edge('dumpsys','system_server')
G.edge['dumpsys']['system_server']['write-read'] = '[open open][write read][append read]'
G.add_edge('dumpsys','untrusteddomain')
G.edge['dumpsys']['untrusteddomain']['write-read'] = '[open open][write read]'
G.edge['dumpsys']['untrusteddomain']['fill'] = 'red'
G.add_edge('dumpsys','untrusteddomain')
G.edge['dumpsys']['untrusteddomain']['write-read'] = '[open open][write read][append read]'
G.add_edge('dumpsys','vold')
G.edge['dumpsys']['vold']['write-read'] = '[open open][write read]'
G.edge['dumpsys']['vold']['fill'] = 'red'
G.add_edge('dumpsys','vold')
G.edge['dumpsys']['vold']['write-read'] = '[open open][write read][append read]'
G.add_edge('good_app','ppp')
G.edge['good_app']['ppp']['write-read'] = '[write read][setattr getattr]'
G.add_edge('good_app','pppoewrapper')
G.edge['good_app']['pppoewrapper']['write-read'] = '[write read][setattr getattr]'
G.add_edge('imscm','adbd')
G.edge['imscm']['adbd']['write-read'] = '[open open]'
G.add_edge('imscm','binderservicedomain')
G.edge['imscm']['binderservicedomain']['write-read'] = '[open open]'
G.add_edge('imscm','bugreport')
G.edge['imscm']['bugreport']['write-read'] = '[open open]'
G.add_edge('imscm','dumpstate')
G.edge['imscm']['dumpstate']['write-read'] = '[open open]'
G.add_edge('imscm','dumpsys')
G.edge['imscm']['dumpsys']['write-read'] = '[open open]'
G.add_edge('imscm','imscm')
G.edge['imscm']['imscm']['write-read'] = '[open open]'
G.add_edge('imscm','logwrapper')
G.edge['imscm']['logwrapper']['write-read'] = '[open open]'
G.add_edge('imscm','mediaserver')
G.edge['imscm']['mediaserver']['write-read'] = '[open open]'
G.add_edge('imscm','netd')
G.edge['imscm']['netd']['write-read'] = '[open open]'
G.add_edge('imscm','ppp')
G.edge['imscm']['ppp']['write-read'] = '[open open]'
G.add_edge('imscm','pppoewrapper')
G.edge['imscm']['pppoewrapper']['write-read'] = '[open open]'
G.add_edge('imscm','samsung_app')
G.edge['imscm']['samsung_app']['write-read'] = '[open open]'
G.add_edge('imscm','shell')
G.edge['imscm']['shell']['write-read'] = '[open open]'
G.add_edge('imscm','system_server')
G.edge['imscm']['system_server']['write-read'] = '[open open]'
G.add_edge('imscm','untrusteddomain')
G.edge['imscm']['untrusteddomain']['write-read'] = '[open open]'
G.add_edge('imscm','vold')
G.edge['imscm']['vold']['write-read'] = '[open open]'
G.add_edge('imscm','ppp')
G.edge['imscm']['ppp']['write-read'] = '[open open][setattr getattr]'
G.add_edge('imscm','pppoewrapper')
G.edge['imscm']['pppoewrapper']['write-read'] = '[open open][setattr getattr]'
G.add_edge('imscm','adbd')
G.edge['imscm']['adbd']['write-read'] = '[open open][write read]'
G.edge['imscm']['adbd']['fill'] = 'red'
G.add_edge('imscm','adbd')
G.edge['imscm']['adbd']['write-read'] = '[open open][write read][append read]'
G.add_edge('imscm','appdomain')
G.edge['imscm']['appdomain']['write-read'] = '[write read]'
G.edge['imscm']['appdomain']['fill'] = 'red'
G.add_edge('imscm','binderservicedomain')
G.edge['imscm']['binderservicedomain']['write-read'] = '[open open][write read]'
G.edge['imscm']['binderservicedomain']['fill'] = 'red'
G.add_edge('imscm','binderservicedomain')
G.edge['imscm']['binderservicedomain']['write-read'] = '[open open][write read][append read]'
G.add_edge('imscm','bluetooth')
G.edge['imscm']['bluetooth']['write-read'] = '[write read]'
G.edge['imscm']['bluetooth']['fill'] = 'red'
G.add_edge('imscm','bugreport')
G.edge['imscm']['bugreport']['write-read'] = '[open open][write read]'
G.edge['imscm']['bugreport']['fill'] = 'red'
G.add_edge('imscm','bugreport')
G.edge['imscm']['bugreport']['write-read'] = '[open open][write read][append read]'
G.add_edge('imscm','dumpstate')
G.edge['imscm']['dumpstate']['write-read'] = '[open open][write read]'
G.edge['imscm']['dumpstate']['fill'] = 'red'
G.add_edge('imscm','dumpstate')
G.edge['imscm']['dumpstate']['write-read'] = '[open open][write read][append read]'
G.add_edge('imscm','dumpsys')
G.edge['imscm']['dumpsys']['write-read'] = '[open open][write read]'
G.edge['imscm']['dumpsys']['fill'] = 'red'
G.add_edge('imscm','dumpsys')
G.edge['imscm']['dumpsys']['write-read'] = '[open open][write read][append read]'
G.add_edge('imscm','imscm')
G.edge['imscm']['imscm']['write-read'] = '[open open][write read]'
G.edge['imscm']['imscm']['fill'] = 'red'
G.add_edge('imscm','imscm')
G.edge['imscm']['imscm']['write-read'] = '[open open][write read][append read]'
G.add_edge('imscm','irsc_util')
G.edge['imscm']['irsc_util']['write-read'] = '[write read]'
G.edge['imscm']['irsc_util']['fill'] = 'red'
G.add_edge('imscm','logwrapper')
G.edge['imscm']['logwrapper']['write-read'] = '[open open][write read]'
G.edge['imscm']['logwrapper']['fill'] = 'red'
G.add_edge('imscm','logwrapper')
G.edge['imscm']['logwrapper']['write-read'] = '[open open][write read][append read]'
G.add_edge('imscm','mediaserver')
G.edge['imscm']['mediaserver']['write-read'] = '[open open][write read]'
G.edge['imscm']['mediaserver']['fill'] = 'red'
G.add_edge('imscm','mediaserver')
G.edge['imscm']['mediaserver']['write-read'] = '[open open][write read][append read]'
G.add_edge('imscm','netd')
G.edge['imscm']['netd']['write-read'] = '[open open][write read]'
G.edge['imscm']['netd']['fill'] = 'red'
G.add_edge('imscm','netd')
G.edge['imscm']['netd']['write-read'] = '[open open][write read][append read]'
G.add_edge('imscm','newAttr49')
G.edge['imscm']['newAttr49']['write-read'] = '[write read]'
G.edge['imscm']['newAttr49']['fill'] = 'red'
G.add_edge('imscm','newAttr9')
G.edge['imscm']['newAttr9']['write-read'] = '[write read]'
G.edge['imscm']['newAttr9']['fill'] = 'red'
G.add_edge('imscm','radio')
G.edge['imscm']['radio']['write-read'] = '[write read]'
G.edge['imscm']['radio']['fill'] = 'red'
G.add_edge('imscm','runas')
G.edge['imscm']['runas']['write-read'] = '[write read]'
G.edge['imscm']['runas']['fill'] = 'red'
G.add_edge('imscm','samsung_app')
G.edge['imscm']['samsung_app']['write-read'] = '[open open][write read]'
G.edge['imscm']['samsung_app']['fill'] = 'red'
G.add_edge('imscm','samsung_app')
G.edge['imscm']['samsung_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('imscm','shell')
G.edge['imscm']['shell']['write-read'] = '[open open][write read]'
G.edge['imscm']['shell']['fill'] = 'red'
G.add_edge('imscm','shell')
G.edge['imscm']['shell']['write-read'] = '[open open][write read][append read]'
G.add_edge('imscm','surfaceflinger')
G.edge['imscm']['surfaceflinger']['write-read'] = '[write read]'
G.edge['imscm']['surfaceflinger']['fill'] = 'red'
G.add_edge('imscm','system_server')
G.edge['imscm']['system_server']['write-read'] = '[open open][write read]'
G.edge['imscm']['system_server']['fill'] = 'red'
G.add_edge('imscm','system_server')
G.edge['imscm']['system_server']['write-read'] = '[open open][write read][append read]'
G.add_edge('imscm','untrusteddomain')
G.edge['imscm']['untrusteddomain']['write-read'] = '[open open][write read]'
G.edge['imscm']['untrusteddomain']['fill'] = 'red'
G.add_edge('imscm','untrusteddomain')
G.edge['imscm']['untrusteddomain']['write-read'] = '[open open][write read][append read]'
G.add_edge('imscm','vold')
G.edge['imscm']['vold']['write-read'] = '[open open][write read]'
G.edge['imscm']['vold']['fill'] = 'red'
G.add_edge('imscm','vold')
G.edge['imscm']['vold']['write-read'] = '[open open][write read][append read]'
G.add_edge('irsc_util','ppp')
G.edge['irsc_util']['ppp']['write-read'] = '[setattr getattr]'
G.add_edge('irsc_util','pppoewrapper')
G.edge['irsc_util']['pppoewrapper']['write-read'] = '[setattr getattr]'
G.add_edge('irsc_util','adbd')
G.edge['irsc_util']['adbd']['write-read'] = '[write read]'
G.edge['irsc_util']['adbd']['fill'] = 'red'
G.add_edge('irsc_util','adbd')
G.edge['irsc_util']['adbd']['write-read'] = '[write read][append read]'
G.add_edge('irsc_util','appdomain')
G.edge['irsc_util']['appdomain']['write-read'] = '[write read]'
G.edge['irsc_util']['appdomain']['fill'] = 'red'
G.add_edge('irsc_util','binderservicedomain')
G.edge['irsc_util']['binderservicedomain']['write-read'] = '[write read]'
G.edge['irsc_util']['binderservicedomain']['fill'] = 'red'
G.add_edge('irsc_util','binderservicedomain')
G.edge['irsc_util']['binderservicedomain']['write-read'] = '[write read][append read]'
G.add_edge('irsc_util','bluetooth')
G.edge['irsc_util']['bluetooth']['write-read'] = '[write read]'
G.edge['irsc_util']['bluetooth']['fill'] = 'red'
G.add_edge('irsc_util','bugreport')
G.edge['irsc_util']['bugreport']['write-read'] = '[write read]'
G.edge['irsc_util']['bugreport']['fill'] = 'red'
G.add_edge('irsc_util','bugreport')
G.edge['irsc_util']['bugreport']['write-read'] = '[write read][append read]'
G.add_edge('irsc_util','dumpstate')
G.edge['irsc_util']['dumpstate']['write-read'] = '[write read]'
G.edge['irsc_util']['dumpstate']['fill'] = 'red'
G.add_edge('irsc_util','dumpstate')
G.edge['irsc_util']['dumpstate']['write-read'] = '[write read][append read]'
G.add_edge('irsc_util','dumpsys')
G.edge['irsc_util']['dumpsys']['write-read'] = '[write read]'
G.edge['irsc_util']['dumpsys']['fill'] = 'red'
G.add_edge('irsc_util','dumpsys')
G.edge['irsc_util']['dumpsys']['write-read'] = '[write read][append read]'
G.add_edge('irsc_util','imscm')
G.edge['irsc_util']['imscm']['write-read'] = '[write read]'
G.edge['irsc_util']['imscm']['fill'] = 'red'
G.add_edge('irsc_util','imscm')
G.edge['irsc_util']['imscm']['write-read'] = '[write read][append read]'
G.add_edge('irsc_util','irsc_util')
G.edge['irsc_util']['irsc_util']['write-read'] = '[write read][write read]'
G.edge['irsc_util']['irsc_util']['fill'] = 'red'
G.add_edge('irsc_util','logwrapper')
G.edge['irsc_util']['logwrapper']['write-read'] = '[write read]'
G.edge['irsc_util']['logwrapper']['fill'] = 'red'
G.add_edge('irsc_util','logwrapper')
G.edge['irsc_util']['logwrapper']['write-read'] = '[write read][append read]'
G.add_edge('irsc_util','mediaserver')
G.edge['irsc_util']['mediaserver']['write-read'] = '[write read]'
G.edge['irsc_util']['mediaserver']['fill'] = 'red'
G.add_edge('irsc_util','mediaserver')
G.edge['irsc_util']['mediaserver']['write-read'] = '[write read][append read]'
G.add_edge('irsc_util','netd')
G.edge['irsc_util']['netd']['write-read'] = '[write read]'
G.edge['irsc_util']['netd']['fill'] = 'red'
G.add_edge('irsc_util','netd')
G.edge['irsc_util']['netd']['write-read'] = '[write read][append read]'
G.add_edge('irsc_util','newAttr49')
G.edge['irsc_util']['newAttr49']['write-read'] = '[write read]'
G.edge['irsc_util']['newAttr49']['fill'] = 'red'
G.add_edge('irsc_util','newAttr9')
G.edge['irsc_util']['newAttr9']['write-read'] = '[write read]'
G.edge['irsc_util']['newAttr9']['fill'] = 'red'
G.add_edge('irsc_util','radio')
G.edge['irsc_util']['radio']['write-read'] = '[write read]'
G.edge['irsc_util']['radio']['fill'] = 'red'
G.add_edge('irsc_util','runas')
G.edge['irsc_util']['runas']['write-read'] = '[write read]'
G.edge['irsc_util']['runas']['fill'] = 'red'
G.add_edge('irsc_util','samsung_app')
G.edge['irsc_util']['samsung_app']['write-read'] = '[write read]'
G.edge['irsc_util']['samsung_app']['fill'] = 'red'
G.add_edge('irsc_util','samsung_app')
G.edge['irsc_util']['samsung_app']['write-read'] = '[write read][append read]'
G.add_edge('irsc_util','shell')
G.edge['irsc_util']['shell']['write-read'] = '[write read]'
G.edge['irsc_util']['shell']['fill'] = 'red'
G.add_edge('irsc_util','shell')
G.edge['irsc_util']['shell']['write-read'] = '[write read][append read]'
G.add_edge('irsc_util','surfaceflinger')
G.edge['irsc_util']['surfaceflinger']['write-read'] = '[write read]'
G.edge['irsc_util']['surfaceflinger']['fill'] = 'red'
G.add_edge('irsc_util','system_server')
G.edge['irsc_util']['system_server']['write-read'] = '[write read]'
G.edge['irsc_util']['system_server']['fill'] = 'red'
G.add_edge('irsc_util','system_server')
G.edge['irsc_util']['system_server']['write-read'] = '[write read][append read]'
G.add_edge('irsc_util','untrusteddomain')
G.edge['irsc_util']['untrusteddomain']['write-read'] = '[write read]'
G.edge['irsc_util']['untrusteddomain']['fill'] = 'red'
G.add_edge('irsc_util','untrusteddomain')
G.edge['irsc_util']['untrusteddomain']['write-read'] = '[write read][append read]'
G.add_edge('irsc_util','vold')
G.edge['irsc_util']['vold']['write-read'] = '[write read]'
G.edge['irsc_util']['vold']['fill'] = 'red'
G.add_edge('irsc_util','vold')
G.edge['irsc_util']['vold']['write-read'] = '[write read][append read]'
G.add_edge('itsonbs','adbd')
G.edge['itsonbs']['adbd']['write-read'] = '[write read][add_name search][open open]'
G.add_edge('itsonbs','binderservicedomain')
G.edge['itsonbs']['binderservicedomain']['write-read'] = '[open open]'
G.add_edge('itsonbs','bugreport')
G.edge['itsonbs']['bugreport']['write-read'] = '[open open]'
G.add_edge('itsonbs','dumpstate')
G.edge['itsonbs']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('itsonbs','dumpsys')
G.edge['itsonbs']['dumpsys']['write-read'] = '[open open]'
G.add_edge('itsonbs','imscm')
G.edge['itsonbs']['imscm']['write-read'] = '[open open]'
G.add_edge('itsonbs','logwrapper')
G.edge['itsonbs']['logwrapper']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('itsonbs','mediaserver')
G.edge['itsonbs']['mediaserver']['write-read'] = '[open open]'
G.add_edge('itsonbs','netd')
G.edge['itsonbs']['netd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('itsonbs','ppp')
G.edge['itsonbs']['ppp']['write-read'] = '[open open]'
G.add_edge('itsonbs','pppoewrapper')
G.edge['itsonbs']['pppoewrapper']['write-read'] = '[open open]'
G.add_edge('itsonbs','samsung_app')
G.edge['itsonbs']['samsung_app']['write-read'] = '[open open]'
G.add_edge('itsonbs','shell')
G.edge['itsonbs']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('itsonbs','system_server')
G.edge['itsonbs']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open]'
G.add_edge('itsonbs','untrusteddomain')
G.edge['itsonbs']['untrusteddomain']['write-read'] = '[open open]'
G.add_edge('itsonbs','vold')
G.edge['itsonbs']['vold']['write-read'] = '[open open]'
G.add_edge('itsonbs','ppp')
G.edge['itsonbs']['ppp']['write-read'] = '[open open][setattr getattr]'
G.add_edge('itsonbs','pppoewrapper')
G.edge['itsonbs']['pppoewrapper']['write-read'] = '[open open][setattr getattr]'
G.add_edge('itsonbs','adbd')
G.edge['itsonbs']['adbd']['write-read'] = '[write read][add_name search][open open][write read]'
G.edge['itsonbs']['adbd']['fill'] = 'red'
G.add_edge('itsonbs','adbd')
G.edge['itsonbs']['adbd']['write-read'] = '[write read][add_name search][open open][write read][append read]'
G.add_edge('itsonbs','appdomain')
G.edge['itsonbs']['appdomain']['write-read'] = '[write read]'
G.edge['itsonbs']['appdomain']['fill'] = 'red'
G.add_edge('itsonbs','binderservicedomain')
G.edge['itsonbs']['binderservicedomain']['write-read'] = '[open open][write read]'
G.edge['itsonbs']['binderservicedomain']['fill'] = 'red'
G.add_edge('itsonbs','binderservicedomain')
G.edge['itsonbs']['binderservicedomain']['write-read'] = '[open open][write read][append read]'
G.add_edge('itsonbs','bluetooth')
G.edge['itsonbs']['bluetooth']['write-read'] = '[write read]'
G.edge['itsonbs']['bluetooth']['fill'] = 'red'
G.add_edge('itsonbs','bugreport')
G.edge['itsonbs']['bugreport']['write-read'] = '[open open][write read]'
G.edge['itsonbs']['bugreport']['fill'] = 'red'
G.add_edge('itsonbs','bugreport')
G.edge['itsonbs']['bugreport']['write-read'] = '[open open][write read][append read]'
G.add_edge('itsonbs','dumpstate')
G.edge['itsonbs']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['itsonbs']['dumpstate']['fill'] = 'red'
G.add_edge('itsonbs','dumpstate')
G.edge['itsonbs']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('itsonbs','dumpsys')
G.edge['itsonbs']['dumpsys']['write-read'] = '[open open][write read]'
G.edge['itsonbs']['dumpsys']['fill'] = 'red'
G.add_edge('itsonbs','dumpsys')
G.edge['itsonbs']['dumpsys']['write-read'] = '[open open][write read][append read]'
G.add_edge('itsonbs','imscm')
G.edge['itsonbs']['imscm']['write-read'] = '[open open][write read]'
G.edge['itsonbs']['imscm']['fill'] = 'red'
G.add_edge('itsonbs','imscm')
G.edge['itsonbs']['imscm']['write-read'] = '[open open][write read][append read]'
G.add_edge('itsonbs','irsc_util')
G.edge['itsonbs']['irsc_util']['write-read'] = '[write read]'
G.edge['itsonbs']['irsc_util']['fill'] = 'red'
G.add_edge('itsonbs','logwrapper')
G.edge['itsonbs']['logwrapper']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['itsonbs']['logwrapper']['fill'] = 'red'
G.add_edge('itsonbs','logwrapper')
G.edge['itsonbs']['logwrapper']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('itsonbs','mediaserver')
G.edge['itsonbs']['mediaserver']['write-read'] = '[open open][write read]'
G.edge['itsonbs']['mediaserver']['fill'] = 'red'
G.add_edge('itsonbs','mediaserver')
G.edge['itsonbs']['mediaserver']['write-read'] = '[open open][write read][append read]'
G.add_edge('itsonbs','netd')
G.edge['itsonbs']['netd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['itsonbs']['netd']['fill'] = 'red'
G.add_edge('itsonbs','netd')
G.edge['itsonbs']['netd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('itsonbs','newAttr49')
G.edge['itsonbs']['newAttr49']['write-read'] = '[write read]'
G.edge['itsonbs']['newAttr49']['fill'] = 'red'
G.add_edge('itsonbs','newAttr9')
G.edge['itsonbs']['newAttr9']['write-read'] = '[write read]'
G.edge['itsonbs']['newAttr9']['fill'] = 'red'
G.add_edge('itsonbs','radio')
G.edge['itsonbs']['radio']['write-read'] = '[write read]'
G.edge['itsonbs']['radio']['fill'] = 'red'
G.add_edge('itsonbs','runas')
G.edge['itsonbs']['runas']['write-read'] = '[write read]'
G.edge['itsonbs']['runas']['fill'] = 'red'
G.add_edge('itsonbs','samsung_app')
G.edge['itsonbs']['samsung_app']['write-read'] = '[open open][write read]'
G.edge['itsonbs']['samsung_app']['fill'] = 'red'
G.add_edge('itsonbs','samsung_app')
G.edge['itsonbs']['samsung_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('itsonbs','shell')
G.edge['itsonbs']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['itsonbs']['shell']['fill'] = 'red'
G.add_edge('itsonbs','shell')
G.edge['itsonbs']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('itsonbs','surfaceflinger')
G.edge['itsonbs']['surfaceflinger']['write-read'] = '[write read]'
G.edge['itsonbs']['surfaceflinger']['fill'] = 'red'
G.add_edge('itsonbs','system_server')
G.edge['itsonbs']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read]'
G.edge['itsonbs']['system_server']['fill'] = 'red'
G.add_edge('itsonbs','system_server')
G.edge['itsonbs']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read]'
G.add_edge('itsonbs','untrusteddomain')
G.edge['itsonbs']['untrusteddomain']['write-read'] = '[open open][write read]'
G.edge['itsonbs']['untrusteddomain']['fill'] = 'red'
G.add_edge('itsonbs','untrusteddomain')
G.edge['itsonbs']['untrusteddomain']['write-read'] = '[open open][write read][append read]'
G.add_edge('itsonbs','vold')
G.edge['itsonbs']['vold']['write-read'] = '[open open][write read]'
G.edge['itsonbs']['vold']['fill'] = 'red'
G.add_edge('itsonbs','vold')
G.edge['itsonbs']['vold']['write-read'] = '[open open][write read][append read]'
G.add_edge('logwrapper','adbd')
G.edge['logwrapper']['adbd']['write-read'] = '[write read][add_name search][open open]'
G.add_edge('logwrapper','binderservicedomain')
G.edge['logwrapper']['binderservicedomain']['write-read'] = '[open open]'
G.add_edge('logwrapper','bugreport')
G.edge['logwrapper']['bugreport']['write-read'] = '[open open]'
G.add_edge('logwrapper','dumpstate')
G.edge['logwrapper']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('logwrapper','dumpsys')
G.edge['logwrapper']['dumpsys']['write-read'] = '[open open]'
G.add_edge('logwrapper','imscm')
G.edge['logwrapper']['imscm']['write-read'] = '[open open]'
G.add_edge('logwrapper','logwrapper')
G.edge['logwrapper']['logwrapper']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('logwrapper','mediaserver')
G.edge['logwrapper']['mediaserver']['write-read'] = '[open open]'
G.add_edge('logwrapper','netd')
G.edge['logwrapper']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('logwrapper','ppp')
G.edge['logwrapper']['ppp']['write-read'] = '[open open]'
G.add_edge('logwrapper','pppoewrapper')
G.edge['logwrapper']['pppoewrapper']['write-read'] = '[open open]'
G.add_edge('logwrapper','samsung_app')
G.edge['logwrapper']['samsung_app']['write-read'] = '[open open]'
G.add_edge('logwrapper','shell')
G.edge['logwrapper']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('logwrapper','system_server')
G.edge['logwrapper']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('logwrapper','untrusteddomain')
G.edge['logwrapper']['untrusteddomain']['write-read'] = '[open open]'
G.add_edge('logwrapper','vold')
G.edge['logwrapper']['vold']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('logwrapper','ppp')
G.edge['logwrapper']['ppp']['write-read'] = '[open open][setattr getattr]'
G.add_edge('logwrapper','pppoewrapper')
G.edge['logwrapper']['pppoewrapper']['write-read'] = '[open open][setattr getattr]'
G.add_edge('logwrapper','adbd')
G.edge['logwrapper']['adbd']['write-read'] = '[write read][add_name search][open open][write read]'
G.edge['logwrapper']['adbd']['fill'] = 'red'
G.add_edge('logwrapper','adbd')
G.edge['logwrapper']['adbd']['write-read'] = '[write read][add_name search][open open][write read][append read]'
G.add_edge('logwrapper','appdomain')
G.edge['logwrapper']['appdomain']['write-read'] = '[write read]'
G.edge['logwrapper']['appdomain']['fill'] = 'red'
G.add_edge('logwrapper','binderservicedomain')
G.edge['logwrapper']['binderservicedomain']['write-read'] = '[open open][write read]'
G.edge['logwrapper']['binderservicedomain']['fill'] = 'red'
G.add_edge('logwrapper','binderservicedomain')
G.edge['logwrapper']['binderservicedomain']['write-read'] = '[open open][write read][append read]'
G.add_edge('logwrapper','bluetooth')
G.edge['logwrapper']['bluetooth']['write-read'] = '[write read]'
G.edge['logwrapper']['bluetooth']['fill'] = 'red'
G.add_edge('logwrapper','bugreport')
G.edge['logwrapper']['bugreport']['write-read'] = '[open open][write read]'
G.edge['logwrapper']['bugreport']['fill'] = 'red'
G.add_edge('logwrapper','bugreport')
G.edge['logwrapper']['bugreport']['write-read'] = '[open open][write read][append read]'
G.add_edge('logwrapper','dumpstate')
G.edge['logwrapper']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['logwrapper']['dumpstate']['fill'] = 'red'
G.add_edge('logwrapper','dumpstate')
G.edge['logwrapper']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('logwrapper','dumpsys')
G.edge['logwrapper']['dumpsys']['write-read'] = '[open open][write read]'
G.edge['logwrapper']['dumpsys']['fill'] = 'red'
G.add_edge('logwrapper','dumpsys')
G.edge['logwrapper']['dumpsys']['write-read'] = '[open open][write read][append read]'
G.add_edge('logwrapper','imscm')
G.edge['logwrapper']['imscm']['write-read'] = '[open open][write read]'
G.edge['logwrapper']['imscm']['fill'] = 'red'
G.add_edge('logwrapper','imscm')
G.edge['logwrapper']['imscm']['write-read'] = '[open open][write read][append read]'
G.add_edge('logwrapper','irsc_util')
G.edge['logwrapper']['irsc_util']['write-read'] = '[write read]'
G.edge['logwrapper']['irsc_util']['fill'] = 'red'
G.add_edge('logwrapper','logwrapper')
G.edge['logwrapper']['logwrapper']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['logwrapper']['logwrapper']['fill'] = 'red'
G.add_edge('logwrapper','logwrapper')
G.edge['logwrapper']['logwrapper']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('logwrapper','mediaserver')
G.edge['logwrapper']['mediaserver']['write-read'] = '[open open][write read]'
G.edge['logwrapper']['mediaserver']['fill'] = 'red'
G.add_edge('logwrapper','mediaserver')
G.edge['logwrapper']['mediaserver']['write-read'] = '[open open][write read][append read]'
G.add_edge('logwrapper','netd')
G.edge['logwrapper']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read]'
G.edge['logwrapper']['netd']['fill'] = 'red'
G.add_edge('logwrapper','netd')
G.edge['logwrapper']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('logwrapper','newAttr49')
G.edge['logwrapper']['newAttr49']['write-read'] = '[write read]'
G.edge['logwrapper']['newAttr49']['fill'] = 'red'
G.add_edge('logwrapper','newAttr9')
G.edge['logwrapper']['newAttr9']['write-read'] = '[write read]'
G.edge['logwrapper']['newAttr9']['fill'] = 'red'
G.add_edge('logwrapper','radio')
G.edge['logwrapper']['radio']['write-read'] = '[write read]'
G.edge['logwrapper']['radio']['fill'] = 'red'
G.add_edge('logwrapper','runas')
G.edge['logwrapper']['runas']['write-read'] = '[write read]'
G.edge['logwrapper']['runas']['fill'] = 'red'
G.add_edge('logwrapper','samsung_app')
G.edge['logwrapper']['samsung_app']['write-read'] = '[open open][write read]'
G.edge['logwrapper']['samsung_app']['fill'] = 'red'
G.add_edge('logwrapper','samsung_app')
G.edge['logwrapper']['samsung_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('logwrapper','shell')
G.edge['logwrapper']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['logwrapper']['shell']['fill'] = 'red'
G.add_edge('logwrapper','shell')
G.edge['logwrapper']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('logwrapper','surfaceflinger')
G.edge['logwrapper']['surfaceflinger']['write-read'] = '[write read]'
G.edge['logwrapper']['surfaceflinger']['fill'] = 'red'
G.add_edge('logwrapper','system_server')
G.edge['logwrapper']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['logwrapper']['system_server']['fill'] = 'red'
G.add_edge('logwrapper','system_server')
G.edge['logwrapper']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('logwrapper','untrusteddomain')
G.edge['logwrapper']['untrusteddomain']['write-read'] = '[open open][write read]'
G.edge['logwrapper']['untrusteddomain']['fill'] = 'red'
G.add_edge('logwrapper','untrusteddomain')
G.edge['logwrapper']['untrusteddomain']['write-read'] = '[open open][write read][append read]'
G.add_edge('logwrapper','vold')
G.edge['logwrapper']['vold']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['logwrapper']['vold']['fill'] = 'red'
G.add_edge('logwrapper','vold')
G.edge['logwrapper']['vold']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('mediaserver','adbd')
G.edge['mediaserver']['adbd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('mediaserver','binderservicedomain')
G.edge['mediaserver']['binderservicedomain']['write-read'] = '[open open]'
G.add_edge('mediaserver','bugreport')
G.edge['mediaserver']['bugreport']['write-read'] = '[open open]'
G.add_edge('mediaserver','dumpstate')
G.edge['mediaserver']['dumpstate']['write-read'] = '[open open][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('mediaserver','dumpsys')
G.edge['mediaserver']['dumpsys']['write-read'] = '[open open]'
G.add_edge('mediaserver','imscm')
G.edge['mediaserver']['imscm']['write-read'] = '[open open]'
G.add_edge('mediaserver','logwrapper')
G.edge['mediaserver']['logwrapper']['write-read'] = '[open open]'
G.add_edge('mediaserver','mediaserver')
G.edge['mediaserver']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('mediaserver','netd')
G.edge['mediaserver']['netd']['write-read'] = '[open open]'
G.add_edge('mediaserver','ppp')
G.edge['mediaserver']['ppp']['write-read'] = '[open open]'
G.add_edge('mediaserver','pppoewrapper')
G.edge['mediaserver']['pppoewrapper']['write-read'] = '[open open]'
G.add_edge('mediaserver','samsung_app')
G.edge['mediaserver']['samsung_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('mediaserver','shell')
G.edge['mediaserver']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('mediaserver','system_server')
G.edge['mediaserver']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][write read][append read][open open][write read][append read][open open]'
G.add_edge('mediaserver','untrusteddomain')
G.edge['mediaserver']['untrusteddomain']['write-read'] = '[open open]'
G.add_edge('mediaserver','vold')
G.edge['mediaserver']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][append read][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('mediaserver','ppp')
G.edge['mediaserver']['ppp']['write-read'] = '[open open][setattr getattr]'
G.add_edge('mediaserver','pppoewrapper')
G.edge['mediaserver']['pppoewrapper']['write-read'] = '[open open][setattr getattr]'
G.add_edge('mediaserver','adbd')
G.edge['mediaserver']['adbd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['mediaserver']['adbd']['fill'] = 'red'
G.add_edge('mediaserver','adbd')
G.edge['mediaserver']['adbd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('mediaserver','appdomain')
G.edge['mediaserver']['appdomain']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read]'
G.edge['mediaserver']['appdomain']['fill'] = 'red'
G.add_edge('mediaserver','binderservicedomain')
G.edge['mediaserver']['binderservicedomain']['write-read'] = '[open open][write read]'
G.edge['mediaserver']['binderservicedomain']['fill'] = 'red'
G.add_edge('mediaserver','binderservicedomain')
G.edge['mediaserver']['binderservicedomain']['write-read'] = '[open open][write read][append read]'
G.add_edge('mediaserver','bluetooth')
G.edge['mediaserver']['bluetooth']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read]'
G.edge['mediaserver']['bluetooth']['fill'] = 'red'
G.add_edge('mediaserver','bugreport')
G.edge['mediaserver']['bugreport']['write-read'] = '[open open][write read]'
G.edge['mediaserver']['bugreport']['fill'] = 'red'
G.add_edge('mediaserver','bugreport')
G.edge['mediaserver']['bugreport']['write-read'] = '[open open][write read][append read]'
G.add_edge('mediaserver','dumpstate')
G.edge['mediaserver']['dumpstate']['write-read'] = '[open open][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['mediaserver']['dumpstate']['fill'] = 'red'
G.add_edge('mediaserver','dumpstate')
G.edge['mediaserver']['dumpstate']['write-read'] = '[open open][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('mediaserver','dumpsys')
G.edge['mediaserver']['dumpsys']['write-read'] = '[open open][write read]'
G.edge['mediaserver']['dumpsys']['fill'] = 'red'
G.add_edge('mediaserver','dumpsys')
G.edge['mediaserver']['dumpsys']['write-read'] = '[open open][write read][append read]'
G.add_edge('mediaserver','imscm')
G.edge['mediaserver']['imscm']['write-read'] = '[open open][write read]'
G.edge['mediaserver']['imscm']['fill'] = 'red'
G.add_edge('mediaserver','imscm')
G.edge['mediaserver']['imscm']['write-read'] = '[open open][write read][append read]'
G.add_edge('mediaserver','irsc_util')
G.edge['mediaserver']['irsc_util']['write-read'] = '[write read]'
G.edge['mediaserver']['irsc_util']['fill'] = 'red'
G.add_edge('mediaserver','logwrapper')
G.edge['mediaserver']['logwrapper']['write-read'] = '[open open][write read]'
G.edge['mediaserver']['logwrapper']['fill'] = 'red'
G.add_edge('mediaserver','logwrapper')
G.edge['mediaserver']['logwrapper']['write-read'] = '[open open][write read][append read]'
G.add_edge('mediaserver','mediaserver')
G.edge['mediaserver']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['mediaserver']['mediaserver']['fill'] = 'red'
G.add_edge('mediaserver','mediaserver')
G.edge['mediaserver']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('mediaserver','netd')
G.edge['mediaserver']['netd']['write-read'] = '[open open][write read]'
G.edge['mediaserver']['netd']['fill'] = 'red'
G.add_edge('mediaserver','netd')
G.edge['mediaserver']['netd']['write-read'] = '[open open][write read][append read]'
G.add_edge('mediaserver','newAttr49')
G.edge['mediaserver']['newAttr49']['write-read'] = '[write read]'
G.edge['mediaserver']['newAttr49']['fill'] = 'red'
G.add_edge('mediaserver','newAttr9')
G.edge['mediaserver']['newAttr9']['write-read'] = '[write read]'
G.edge['mediaserver']['newAttr9']['fill'] = 'red'
G.add_edge('mediaserver','radio')
G.edge['mediaserver']['radio']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read]'
G.edge['mediaserver']['radio']['fill'] = 'red'
G.add_edge('mediaserver','runas')
G.edge['mediaserver']['runas']['write-read'] = '[write read]'
G.edge['mediaserver']['runas']['fill'] = 'red'
G.add_edge('mediaserver','samsung_app')
G.edge['mediaserver']['samsung_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['mediaserver']['samsung_app']['fill'] = 'red'
G.add_edge('mediaserver','samsung_app')
G.edge['mediaserver']['samsung_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('mediaserver','shell')
G.edge['mediaserver']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['mediaserver']['shell']['fill'] = 'red'
G.add_edge('mediaserver','shell')
G.edge['mediaserver']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('mediaserver','surfaceflinger')
G.edge['mediaserver']['surfaceflinger']['write-read'] = '[open open][write read][append read][write read]'
G.edge['mediaserver']['surfaceflinger']['fill'] = 'red'
G.add_edge('mediaserver','system_server')
G.edge['mediaserver']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][write read][append read][open open][write read][append read][open open][write read]'
G.edge['mediaserver']['system_server']['fill'] = 'red'
G.add_edge('mediaserver','system_server')
G.edge['mediaserver']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read]'
G.add_edge('mediaserver','untrusteddomain')
G.edge['mediaserver']['untrusteddomain']['write-read'] = '[open open][write read]'
G.edge['mediaserver']['untrusteddomain']['fill'] = 'red'
G.add_edge('mediaserver','untrusteddomain')
G.edge['mediaserver']['untrusteddomain']['write-read'] = '[open open][write read][append read]'
G.add_edge('mediaserver','vold')
G.edge['mediaserver']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][append read][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][write read]'
G.edge['mediaserver']['vold']['fill'] = 'red'
G.add_edge('mediaserver','vold')
G.edge['mediaserver']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][append read][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][write read][append read]'
G.add_edge('netd','adbd')
G.edge['netd']['adbd']['write-read'] = '[write read][add_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('netd','binderservicedomain')
G.edge['netd']['binderservicedomain']['write-read'] = '[open open]'
G.add_edge('netd','bugreport')
G.edge['netd']['bugreport']['write-read'] = '[open open]'
G.add_edge('netd','dumpstate')
G.edge['netd']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('netd','dumpsys')
G.edge['netd']['dumpsys']['write-read'] = '[open open]'
G.add_edge('netd','imscm')
G.edge['netd']['imscm']['write-read'] = '[open open]'
G.add_edge('netd','logwrapper')
G.edge['netd']['logwrapper']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('netd','mediaserver')
G.edge['netd']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('netd','netd')
G.edge['netd']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('netd','ppp')
G.edge['netd']['ppp']['write-read'] = '[open open]'
G.add_edge('netd','pppoewrapper')
G.edge['netd']['pppoewrapper']['write-read'] = '[open open]'
G.add_edge('netd','samsung_app')
G.edge['netd']['samsung_app']['write-read'] = '[setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('netd','shell')
G.edge['netd']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('netd','system_server')
G.edge['netd']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('netd','untrusteddomain')
G.edge['netd']['untrusteddomain']['write-read'] = '[open open]'
G.add_edge('netd','vold')
G.edge['netd']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('netd','ppp')
G.edge['netd']['ppp']['write-read'] = '[open open][setattr getattr]'
G.add_edge('netd','pppoewrapper')
G.edge['netd']['pppoewrapper']['write-read'] = '[open open][setattr getattr]'
G.add_edge('netd','adbd')
G.edge['netd']['adbd']['write-read'] = '[write read][add_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['netd']['adbd']['fill'] = 'red'
G.add_edge('netd','adbd')
G.edge['netd']['adbd']['write-read'] = '[write read][add_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('netd','appdomain')
G.edge['netd']['appdomain']['write-read'] = '[write read]'
G.edge['netd']['appdomain']['fill'] = 'red'
G.add_edge('netd','binderservicedomain')
G.edge['netd']['binderservicedomain']['write-read'] = '[open open][write read]'
G.edge['netd']['binderservicedomain']['fill'] = 'red'
G.add_edge('netd','binderservicedomain')
G.edge['netd']['binderservicedomain']['write-read'] = '[open open][write read][append read]'
G.add_edge('netd','bluetooth')
G.edge['netd']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['netd']['bluetooth']['fill'] = 'red'
G.add_edge('netd','bugreport')
G.edge['netd']['bugreport']['write-read'] = '[open open][write read]'
G.edge['netd']['bugreport']['fill'] = 'red'
G.add_edge('netd','bugreport')
G.edge['netd']['bugreport']['write-read'] = '[open open][write read][append read]'
G.add_edge('netd','dumpstate')
G.edge['netd']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['netd']['dumpstate']['fill'] = 'red'
G.add_edge('netd','dumpstate')
G.edge['netd']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('netd','dumpsys')
G.edge['netd']['dumpsys']['write-read'] = '[open open][write read]'
G.edge['netd']['dumpsys']['fill'] = 'red'
G.add_edge('netd','dumpsys')
G.edge['netd']['dumpsys']['write-read'] = '[open open][write read][append read]'
G.add_edge('netd','imscm')
G.edge['netd']['imscm']['write-read'] = '[open open][write read]'
G.edge['netd']['imscm']['fill'] = 'red'
G.add_edge('netd','imscm')
G.edge['netd']['imscm']['write-read'] = '[open open][write read][append read]'
G.add_edge('netd','irsc_util')
G.edge['netd']['irsc_util']['write-read'] = '[write read]'
G.edge['netd']['irsc_util']['fill'] = 'red'
G.add_edge('netd','logwrapper')
G.edge['netd']['logwrapper']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['netd']['logwrapper']['fill'] = 'red'
G.add_edge('netd','logwrapper')
G.edge['netd']['logwrapper']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('netd','mediaserver')
G.edge['netd']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['netd']['mediaserver']['fill'] = 'red'
G.add_edge('netd','mediaserver')
G.edge['netd']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('netd','netd')
G.edge['netd']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['netd']['netd']['fill'] = 'red'
G.add_edge('netd','netd')
G.edge['netd']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('netd','newAttr49')
G.edge['netd']['newAttr49']['write-read'] = '[write read]'
G.edge['netd']['newAttr49']['fill'] = 'red'
G.add_edge('netd','newAttr9')
G.edge['netd']['newAttr9']['write-read'] = '[write read]'
G.edge['netd']['newAttr9']['fill'] = 'red'
G.add_edge('netd','radio')
G.edge['netd']['radio']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['netd']['radio']['fill'] = 'red'
G.add_edge('netd','runas')
G.edge['netd']['runas']['write-read'] = '[write read]'
G.edge['netd']['runas']['fill'] = 'red'
G.add_edge('netd','samsung_app')
G.edge['netd']['samsung_app']['write-read'] = '[setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['netd']['samsung_app']['fill'] = 'red'
G.add_edge('netd','samsung_app')
G.edge['netd']['samsung_app']['write-read'] = '[setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('netd','shell')
G.edge['netd']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['netd']['shell']['fill'] = 'red'
G.add_edge('netd','shell')
G.edge['netd']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('netd','surfaceflinger')
G.edge['netd']['surfaceflinger']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read]'
G.edge['netd']['surfaceflinger']['fill'] = 'red'
G.add_edge('netd','system_server')
G.edge['netd']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['netd']['system_server']['fill'] = 'red'
G.add_edge('netd','system_server')
G.edge['netd']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('netd','untrusteddomain')
G.edge['netd']['untrusteddomain']['write-read'] = '[open open][write read]'
G.edge['netd']['untrusteddomain']['fill'] = 'red'
G.add_edge('netd','untrusteddomain')
G.edge['netd']['untrusteddomain']['write-read'] = '[open open][write read][append read]'
G.add_edge('netd','vold')
G.edge['netd']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['netd']['vold']['fill'] = 'red'
G.add_edge('netd','vold')
G.edge['netd']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('newAttr49','adbd')
G.edge['newAttr49']['adbd']['write-read'] = '[write read]'
G.edge['newAttr49']['adbd']['fill'] = 'red'
G.add_edge('newAttr49','adbd')
G.edge['newAttr49']['adbd']['write-read'] = '[write read][append read]'
G.add_edge('newAttr49','appdomain')
G.edge['newAttr49']['appdomain']['write-read'] = '[write read]'
G.edge['newAttr49']['appdomain']['fill'] = 'red'
G.add_edge('newAttr49','binderservicedomain')
G.edge['newAttr49']['binderservicedomain']['write-read'] = '[write read]'
G.edge['newAttr49']['binderservicedomain']['fill'] = 'red'
G.add_edge('newAttr49','binderservicedomain')
G.edge['newAttr49']['binderservicedomain']['write-read'] = '[write read][append read]'
G.add_edge('newAttr49','bluetooth')
G.edge['newAttr49']['bluetooth']['write-read'] = '[write read]'
G.edge['newAttr49']['bluetooth']['fill'] = 'red'
G.add_edge('newAttr49','bugreport')
G.edge['newAttr49']['bugreport']['write-read'] = '[write read]'
G.edge['newAttr49']['bugreport']['fill'] = 'red'
G.add_edge('newAttr49','bugreport')
G.edge['newAttr49']['bugreport']['write-read'] = '[write read][append read]'
G.add_edge('newAttr49','dumpstate')
G.edge['newAttr49']['dumpstate']['write-read'] = '[write read]'
G.edge['newAttr49']['dumpstate']['fill'] = 'red'
G.add_edge('newAttr49','dumpstate')
G.edge['newAttr49']['dumpstate']['write-read'] = '[write read][append read]'
G.add_edge('newAttr49','dumpsys')
G.edge['newAttr49']['dumpsys']['write-read'] = '[write read]'
G.edge['newAttr49']['dumpsys']['fill'] = 'red'
G.add_edge('newAttr49','dumpsys')
G.edge['newAttr49']['dumpsys']['write-read'] = '[write read][append read]'
G.add_edge('newAttr49','imscm')
G.edge['newAttr49']['imscm']['write-read'] = '[write read]'
G.edge['newAttr49']['imscm']['fill'] = 'red'
G.add_edge('newAttr49','imscm')
G.edge['newAttr49']['imscm']['write-read'] = '[write read][append read]'
G.add_edge('newAttr49','irsc_util')
G.edge['newAttr49']['irsc_util']['write-read'] = '[write read]'
G.edge['newAttr49']['irsc_util']['fill'] = 'red'
G.add_edge('newAttr49','logwrapper')
G.edge['newAttr49']['logwrapper']['write-read'] = '[write read]'
G.edge['newAttr49']['logwrapper']['fill'] = 'red'
G.add_edge('newAttr49','logwrapper')
G.edge['newAttr49']['logwrapper']['write-read'] = '[write read][append read]'
G.add_edge('newAttr49','mediaserver')
G.edge['newAttr49']['mediaserver']['write-read'] = '[write read]'
G.edge['newAttr49']['mediaserver']['fill'] = 'red'
G.add_edge('newAttr49','mediaserver')
G.edge['newAttr49']['mediaserver']['write-read'] = '[write read][append read]'
G.add_edge('newAttr49','netd')
G.edge['newAttr49']['netd']['write-read'] = '[write read]'
G.edge['newAttr49']['netd']['fill'] = 'red'
G.add_edge('newAttr49','netd')
G.edge['newAttr49']['netd']['write-read'] = '[write read][append read]'
G.add_edge('newAttr49','newAttr49')
G.edge['newAttr49']['newAttr49']['write-read'] = '[write read]'
G.edge['newAttr49']['newAttr49']['fill'] = 'red'
G.add_edge('newAttr49','newAttr9')
G.edge['newAttr49']['newAttr9']['write-read'] = '[write read]'
G.edge['newAttr49']['newAttr9']['fill'] = 'red'
G.add_edge('newAttr49','radio')
G.edge['newAttr49']['radio']['write-read'] = '[write read]'
G.edge['newAttr49']['radio']['fill'] = 'red'
G.add_edge('newAttr49','runas')
G.edge['newAttr49']['runas']['write-read'] = '[write read]'
G.edge['newAttr49']['runas']['fill'] = 'red'
G.add_edge('newAttr49','samsung_app')
G.edge['newAttr49']['samsung_app']['write-read'] = '[write read]'
G.edge['newAttr49']['samsung_app']['fill'] = 'red'
G.add_edge('newAttr49','samsung_app')
G.edge['newAttr49']['samsung_app']['write-read'] = '[write read][append read]'
G.add_edge('newAttr49','shell')
G.edge['newAttr49']['shell']['write-read'] = '[write read]'
G.edge['newAttr49']['shell']['fill'] = 'red'
G.add_edge('newAttr49','shell')
G.edge['newAttr49']['shell']['write-read'] = '[write read][append read]'
G.add_edge('newAttr49','surfaceflinger')
G.edge['newAttr49']['surfaceflinger']['write-read'] = '[write read]'
G.edge['newAttr49']['surfaceflinger']['fill'] = 'red'
G.add_edge('newAttr49','system_server')
G.edge['newAttr49']['system_server']['write-read'] = '[write read]'
G.edge['newAttr49']['system_server']['fill'] = 'red'
G.add_edge('newAttr49','system_server')
G.edge['newAttr49']['system_server']['write-read'] = '[write read][append read]'
G.add_edge('newAttr49','untrusteddomain')
G.edge['newAttr49']['untrusteddomain']['write-read'] = '[write read]'
G.edge['newAttr49']['untrusteddomain']['fill'] = 'red'
G.add_edge('newAttr49','untrusteddomain')
G.edge['newAttr49']['untrusteddomain']['write-read'] = '[write read][append read]'
G.add_edge('newAttr49','vold')
G.edge['newAttr49']['vold']['write-read'] = '[write read]'
G.edge['newAttr49']['vold']['fill'] = 'red'
G.add_edge('newAttr49','vold')
G.edge['newAttr49']['vold']['write-read'] = '[write read][append read]'
G.add_edge('newAttr9','ppp')
G.edge['newAttr9']['ppp']['write-read'] = '[setattr getattr]'
G.add_edge('newAttr9','pppoewrapper')
G.edge['newAttr9']['pppoewrapper']['write-read'] = '[setattr getattr]'
G.add_edge('newAttr9','adbd')
G.edge['newAttr9']['adbd']['write-read'] = '[write read]'
G.edge['newAttr9']['adbd']['fill'] = 'red'
G.add_edge('newAttr9','adbd')
G.edge['newAttr9']['adbd']['write-read'] = '[write read][append read]'
G.add_edge('newAttr9','appdomain')
G.edge['newAttr9']['appdomain']['write-read'] = '[write read]'
G.edge['newAttr9']['appdomain']['fill'] = 'red'
G.add_edge('newAttr9','binderservicedomain')
G.edge['newAttr9']['binderservicedomain']['write-read'] = '[write read]'
G.edge['newAttr9']['binderservicedomain']['fill'] = 'red'
G.add_edge('newAttr9','binderservicedomain')
G.edge['newAttr9']['binderservicedomain']['write-read'] = '[write read][append read]'
G.add_edge('newAttr9','bluetooth')
G.edge['newAttr9']['bluetooth']['write-read'] = '[write read]'
G.edge['newAttr9']['bluetooth']['fill'] = 'red'
G.add_edge('newAttr9','bugreport')
G.edge['newAttr9']['bugreport']['write-read'] = '[write read]'
G.edge['newAttr9']['bugreport']['fill'] = 'red'
G.add_edge('newAttr9','bugreport')
G.edge['newAttr9']['bugreport']['write-read'] = '[write read][append read]'
G.add_edge('newAttr9','dumpstate')
G.edge['newAttr9']['dumpstate']['write-read'] = '[write read]'
G.edge['newAttr9']['dumpstate']['fill'] = 'red'
G.add_edge('newAttr9','dumpstate')
G.edge['newAttr9']['dumpstate']['write-read'] = '[write read][append read]'
G.add_edge('newAttr9','dumpsys')
G.edge['newAttr9']['dumpsys']['write-read'] = '[write read]'
G.edge['newAttr9']['dumpsys']['fill'] = 'red'
G.add_edge('newAttr9','dumpsys')
G.edge['newAttr9']['dumpsys']['write-read'] = '[write read][append read]'
G.add_edge('newAttr9','imscm')
G.edge['newAttr9']['imscm']['write-read'] = '[write read]'
G.edge['newAttr9']['imscm']['fill'] = 'red'
G.add_edge('newAttr9','imscm')
G.edge['newAttr9']['imscm']['write-read'] = '[write read][append read]'
G.add_edge('newAttr9','irsc_util')
G.edge['newAttr9']['irsc_util']['write-read'] = '[write read]'
G.edge['newAttr9']['irsc_util']['fill'] = 'red'
G.add_edge('newAttr9','logwrapper')
G.edge['newAttr9']['logwrapper']['write-read'] = '[write read]'
G.edge['newAttr9']['logwrapper']['fill'] = 'red'
G.add_edge('newAttr9','logwrapper')
G.edge['newAttr9']['logwrapper']['write-read'] = '[write read][append read]'
G.add_edge('newAttr9','mediaserver')
G.edge['newAttr9']['mediaserver']['write-read'] = '[write read]'
G.edge['newAttr9']['mediaserver']['fill'] = 'red'
G.add_edge('newAttr9','mediaserver')
G.edge['newAttr9']['mediaserver']['write-read'] = '[write read][append read]'
G.add_edge('newAttr9','netd')
G.edge['newAttr9']['netd']['write-read'] = '[write read]'
G.edge['newAttr9']['netd']['fill'] = 'red'
G.add_edge('newAttr9','netd')
G.edge['newAttr9']['netd']['write-read'] = '[write read][append read]'
G.add_edge('newAttr9','newAttr49')
G.edge['newAttr9']['newAttr49']['write-read'] = '[write read]'
G.edge['newAttr9']['newAttr49']['fill'] = 'red'
G.add_edge('newAttr9','newAttr9')
G.edge['newAttr9']['newAttr9']['write-read'] = '[write read]'
G.edge['newAttr9']['newAttr9']['fill'] = 'red'
G.add_edge('newAttr9','radio')
G.edge['newAttr9']['radio']['write-read'] = '[write read]'
G.edge['newAttr9']['radio']['fill'] = 'red'
G.add_edge('newAttr9','runas')
G.edge['newAttr9']['runas']['write-read'] = '[write read]'
G.edge['newAttr9']['runas']['fill'] = 'red'
G.add_edge('newAttr9','samsung_app')
G.edge['newAttr9']['samsung_app']['write-read'] = '[write read]'
G.edge['newAttr9']['samsung_app']['fill'] = 'red'
G.add_edge('newAttr9','samsung_app')
G.edge['newAttr9']['samsung_app']['write-read'] = '[write read][append read]'
G.add_edge('newAttr9','shell')
G.edge['newAttr9']['shell']['write-read'] = '[write read]'
G.edge['newAttr9']['shell']['fill'] = 'red'
G.add_edge('newAttr9','shell')
G.edge['newAttr9']['shell']['write-read'] = '[write read][append read]'
G.add_edge('newAttr9','surfaceflinger')
G.edge['newAttr9']['surfaceflinger']['write-read'] = '[write read]'
G.edge['newAttr9']['surfaceflinger']['fill'] = 'red'
G.add_edge('newAttr9','system_server')
G.edge['newAttr9']['system_server']['write-read'] = '[write read]'
G.edge['newAttr9']['system_server']['fill'] = 'red'
G.add_edge('newAttr9','system_server')
G.edge['newAttr9']['system_server']['write-read'] = '[write read][append read]'
G.add_edge('newAttr9','untrusteddomain')
G.edge['newAttr9']['untrusteddomain']['write-read'] = '[write read]'
G.edge['newAttr9']['untrusteddomain']['fill'] = 'red'
G.add_edge('newAttr9','untrusteddomain')
G.edge['newAttr9']['untrusteddomain']['write-read'] = '[write read][append read]'
G.add_edge('newAttr9','vold')
G.edge['newAttr9']['vold']['write-read'] = '[write read]'
G.edge['newAttr9']['vold']['fill'] = 'red'
G.add_edge('newAttr9','vold')
G.edge['newAttr9']['vold']['write-read'] = '[write read][append read]'
G.add_edge('radio','adbd')
G.edge['radio']['adbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['radio']['adbd']['fill'] = 'red'
G.add_edge('radio','adbd')
G.edge['radio']['adbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read]'
G.add_edge('radio','appdomain')
G.edge['radio']['appdomain']['write-read'] = '[open open][write read][append read][write read]'
G.edge['radio']['appdomain']['fill'] = 'red'
G.add_edge('radio','binderservicedomain')
G.edge['radio']['binderservicedomain']['write-read'] = '[write read]'
G.edge['radio']['binderservicedomain']['fill'] = 'red'
G.add_edge('radio','binderservicedomain')
G.edge['radio']['binderservicedomain']['write-read'] = '[write read][append read]'
G.add_edge('radio','bluetooth')
G.edge['radio']['bluetooth']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['radio']['bluetooth']['fill'] = 'red'
G.add_edge('radio','bugreport')
G.edge['radio']['bugreport']['write-read'] = '[write read]'
G.edge['radio']['bugreport']['fill'] = 'red'
G.add_edge('radio','bugreport')
G.edge['radio']['bugreport']['write-read'] = '[write read][append read]'
G.add_edge('radio','dumpstate')
G.edge['radio']['dumpstate']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['radio']['dumpstate']['fill'] = 'red'
G.add_edge('radio','dumpstate')
G.edge['radio']['dumpstate']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read]'
G.add_edge('radio','dumpsys')
G.edge['radio']['dumpsys']['write-read'] = '[write read]'
G.edge['radio']['dumpsys']['fill'] = 'red'
G.add_edge('radio','dumpsys')
G.edge['radio']['dumpsys']['write-read'] = '[write read][append read]'
G.add_edge('radio','imscm')
G.edge['radio']['imscm']['write-read'] = '[write read]'
G.edge['radio']['imscm']['fill'] = 'red'
G.add_edge('radio','imscm')
G.edge['radio']['imscm']['write-read'] = '[write read][append read]'
G.add_edge('radio','irsc_util')
G.edge['radio']['irsc_util']['write-read'] = '[write read]'
G.edge['radio']['irsc_util']['fill'] = 'red'
G.add_edge('radio','logwrapper')
G.edge['radio']['logwrapper']['write-read'] = '[write read]'
G.edge['radio']['logwrapper']['fill'] = 'red'
G.add_edge('radio','logwrapper')
G.edge['radio']['logwrapper']['write-read'] = '[write read][append read]'
G.add_edge('radio','mediaserver')
G.edge['radio']['mediaserver']['write-read'] = '[add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][write read]'
G.edge['radio']['mediaserver']['fill'] = 'red'
G.add_edge('radio','mediaserver')
G.edge['radio']['mediaserver']['write-read'] = '[add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][write read][append read]'
G.add_edge('radio','netd')
G.edge['radio']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][add_name search][remove_name search][write read]'
G.edge['radio']['netd']['fill'] = 'red'
G.add_edge('radio','netd')
G.edge['radio']['netd']['write-read'] = '[open open][setattr getattr][write read][append read][add_name search][remove_name search][write read][append read]'
G.add_edge('radio','newAttr49')
G.edge['radio']['newAttr49']['write-read'] = '[write read]'
G.edge['radio']['newAttr49']['fill'] = 'red'
G.add_edge('radio','newAttr9')
G.edge['radio']['newAttr9']['write-read'] = '[write read]'
G.edge['radio']['newAttr9']['fill'] = 'red'
G.add_edge('radio','radio')
G.edge['radio']['radio']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['radio']['radio']['fill'] = 'red'
G.add_edge('radio','runas')
G.edge['radio']['runas']['write-read'] = '[write read]'
G.edge['radio']['runas']['fill'] = 'red'
G.add_edge('radio','samsung_app')
G.edge['radio']['samsung_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['radio']['samsung_app']['fill'] = 'red'
G.add_edge('radio','samsung_app')
G.edge['radio']['samsung_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read][append read]'
G.add_edge('radio','shell')
G.edge['radio']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['radio']['shell']['fill'] = 'red'
G.add_edge('radio','shell')
G.edge['radio']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read][append read]'
G.add_edge('radio','surfaceflinger')
G.edge['radio']['surfaceflinger']['write-read'] = '[open open][write read][append read][write read]'
G.edge['radio']['surfaceflinger']['fill'] = 'red'
G.add_edge('radio','system_server')
G.edge['radio']['system_server']['write-read'] = '[add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['radio']['system_server']['fill'] = 'red'
G.add_edge('radio','system_server')
G.edge['radio']['system_server']['write-read'] = '[add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read]'
G.add_edge('radio','untrusteddomain')
G.edge['radio']['untrusteddomain']['write-read'] = '[write read]'
G.edge['radio']['untrusteddomain']['fill'] = 'red'
G.add_edge('radio','untrusteddomain')
G.edge['radio']['untrusteddomain']['write-read'] = '[write read][append read]'
G.add_edge('radio','vold')
G.edge['radio']['vold']['write-read'] = '[add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['radio']['vold']['fill'] = 'red'
G.add_edge('radio','vold')
G.edge['radio']['vold']['write-read'] = '[add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read]'
G.add_edge('runas','adbd')
G.edge['runas']['adbd']['write-read'] = '[write read]'
G.edge['runas']['adbd']['fill'] = 'red'
G.add_edge('runas','adbd')
G.edge['runas']['adbd']['write-read'] = '[write read][append read]'
G.add_edge('runas','appdomain')
G.edge['runas']['appdomain']['write-read'] = '[open open][write read][append read][write read]'
G.edge['runas']['appdomain']['fill'] = 'red'
G.add_edge('runas','binderservicedomain')
G.edge['runas']['binderservicedomain']['write-read'] = '[write read]'
G.edge['runas']['binderservicedomain']['fill'] = 'red'
G.add_edge('runas','binderservicedomain')
G.edge['runas']['binderservicedomain']['write-read'] = '[write read][append read]'
G.add_edge('runas','bluetooth')
G.edge['runas']['bluetooth']['write-read'] = '[write read]'
G.edge['runas']['bluetooth']['fill'] = 'red'
G.add_edge('runas','bugreport')
G.edge['runas']['bugreport']['write-read'] = '[write read]'
G.edge['runas']['bugreport']['fill'] = 'red'
G.add_edge('runas','bugreport')
G.edge['runas']['bugreport']['write-read'] = '[write read][append read]'
G.add_edge('runas','dumpstate')
G.edge['runas']['dumpstate']['write-read'] = '[write read]'
G.edge['runas']['dumpstate']['fill'] = 'red'
G.add_edge('runas','dumpstate')
G.edge['runas']['dumpstate']['write-read'] = '[write read][append read]'
G.add_edge('runas','dumpsys')
G.edge['runas']['dumpsys']['write-read'] = '[write read]'
G.edge['runas']['dumpsys']['fill'] = 'red'
G.add_edge('runas','dumpsys')
G.edge['runas']['dumpsys']['write-read'] = '[write read][append read]'
G.add_edge('runas','imscm')
G.edge['runas']['imscm']['write-read'] = '[write read]'
G.edge['runas']['imscm']['fill'] = 'red'
G.add_edge('runas','imscm')
G.edge['runas']['imscm']['write-read'] = '[write read][append read]'
G.add_edge('runas','irsc_util')
G.edge['runas']['irsc_util']['write-read'] = '[write read]'
G.edge['runas']['irsc_util']['fill'] = 'red'
G.add_edge('runas','logwrapper')
G.edge['runas']['logwrapper']['write-read'] = '[write read]'
G.edge['runas']['logwrapper']['fill'] = 'red'
G.add_edge('runas','logwrapper')
G.edge['runas']['logwrapper']['write-read'] = '[write read][append read]'
G.add_edge('runas','mediaserver')
G.edge['runas']['mediaserver']['write-read'] = '[add_name search][remove_name search][write read]'
G.edge['runas']['mediaserver']['fill'] = 'red'
G.add_edge('runas','mediaserver')
G.edge['runas']['mediaserver']['write-read'] = '[add_name search][remove_name search][write read][append read]'
G.add_edge('runas','netd')
G.edge['runas']['netd']['write-read'] = '[write read]'
G.edge['runas']['netd']['fill'] = 'red'
G.add_edge('runas','netd')
G.edge['runas']['netd']['write-read'] = '[write read][append read]'
G.add_edge('runas','newAttr49')
G.edge['runas']['newAttr49']['write-read'] = '[write read]'
G.edge['runas']['newAttr49']['fill'] = 'red'
G.add_edge('runas','newAttr9')
G.edge['runas']['newAttr9']['write-read'] = '[write read]'
G.edge['runas']['newAttr9']['fill'] = 'red'
G.add_edge('runas','radio')
G.edge['runas']['radio']['write-read'] = '[write read]'
G.edge['runas']['radio']['fill'] = 'red'
G.add_edge('runas','runas')
G.edge['runas']['runas']['write-read'] = '[write read][open open][write read][append read][write read]'
G.edge['runas']['runas']['fill'] = 'red'
G.add_edge('runas','samsung_app')
G.edge['runas']['samsung_app']['write-read'] = '[write read]'
G.edge['runas']['samsung_app']['fill'] = 'red'
G.add_edge('runas','samsung_app')
G.edge['runas']['samsung_app']['write-read'] = '[write read][append read]'
G.add_edge('runas','shell')
G.edge['runas']['shell']['write-read'] = '[write read]'
G.edge['runas']['shell']['fill'] = 'red'
G.add_edge('runas','shell')
G.edge['runas']['shell']['write-read'] = '[write read][append read]'
G.add_edge('runas','surfaceflinger')
G.edge['runas']['surfaceflinger']['write-read'] = '[write read]'
G.edge['runas']['surfaceflinger']['fill'] = 'red'
G.add_edge('runas','system_server')
G.edge['runas']['system_server']['write-read'] = '[write read][append read][open open][write read][append read][setattr getattr][add_name search][remove_name search][write read]'
G.edge['runas']['system_server']['fill'] = 'red'
G.add_edge('runas','system_server')
G.edge['runas']['system_server']['write-read'] = '[write read][append read][open open][write read][append read][setattr getattr][add_name search][remove_name search][write read][append read]'
G.add_edge('runas','untrusteddomain')
G.edge['runas']['untrusteddomain']['write-read'] = '[write read]'
G.edge['runas']['untrusteddomain']['fill'] = 'red'
G.add_edge('runas','untrusteddomain')
G.edge['runas']['untrusteddomain']['write-read'] = '[write read][append read]'
G.add_edge('runas','vold')
G.edge['runas']['vold']['write-read'] = '[setattr getattr][add_name search][remove_name search][write read]'
G.edge['runas']['vold']['fill'] = 'red'
G.add_edge('runas','vold')
G.edge['runas']['vold']['write-read'] = '[setattr getattr][add_name search][remove_name search][write read][append read]'
G.add_edge('samsung_app','adbd')
G.edge['samsung_app']['adbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('samsung_app','binderservicedomain')
G.edge['samsung_app']['binderservicedomain']['write-read'] = '[open open]'
G.add_edge('samsung_app','bugreport')
G.edge['samsung_app']['bugreport']['write-read'] = '[open open]'
G.add_edge('samsung_app','dumpstate')
G.edge['samsung_app']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('samsung_app','dumpsys')
G.edge['samsung_app']['dumpsys']['write-read'] = '[open open]'
G.add_edge('samsung_app','imscm')
G.edge['samsung_app']['imscm']['write-read'] = '[open open]'
G.add_edge('samsung_app','logwrapper')
G.edge['samsung_app']['logwrapper']['write-read'] = '[open open]'
G.add_edge('samsung_app','mediaserver')
G.edge['samsung_app']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('samsung_app','netd')
G.edge['samsung_app']['netd']['write-read'] = '[write read][append read][open open]'
G.add_edge('samsung_app','ppp')
G.edge['samsung_app']['ppp']['write-read'] = '[open open]'
G.add_edge('samsung_app','pppoewrapper')
G.edge['samsung_app']['pppoewrapper']['write-read'] = '[open open]'
G.add_edge('samsung_app','samsung_app')
G.edge['samsung_app']['samsung_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('samsung_app','shell')
G.edge['samsung_app']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('samsung_app','system_server')
G.edge['samsung_app']['system_server']['write-read'] = '[write read][append read][open open]'
G.add_edge('samsung_app','untrusteddomain')
G.edge['samsung_app']['untrusteddomain']['write-read'] = '[open open]'
G.add_edge('samsung_app','vold')
G.edge['samsung_app']['vold']['write-read'] = '[write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('samsung_app','ppp')
G.edge['samsung_app']['ppp']['write-read'] = '[open open][setattr getattr]'
G.add_edge('samsung_app','pppoewrapper')
G.edge['samsung_app']['pppoewrapper']['write-read'] = '[open open][setattr getattr]'
G.add_edge('samsung_app','adbd')
G.edge['samsung_app']['adbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['samsung_app']['adbd']['fill'] = 'red'
G.add_edge('samsung_app','adbd')
G.edge['samsung_app']['adbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('samsung_app','appdomain')
G.edge['samsung_app']['appdomain']['write-read'] = '[write read]'
G.edge['samsung_app']['appdomain']['fill'] = 'red'
G.add_edge('samsung_app','binderservicedomain')
G.edge['samsung_app']['binderservicedomain']['write-read'] = '[open open][write read]'
G.edge['samsung_app']['binderservicedomain']['fill'] = 'red'
G.add_edge('samsung_app','binderservicedomain')
G.edge['samsung_app']['binderservicedomain']['write-read'] = '[open open][write read][append read]'
G.add_edge('samsung_app','bluetooth')
G.edge['samsung_app']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['samsung_app']['bluetooth']['fill'] = 'red'
G.add_edge('samsung_app','bugreport')
G.edge['samsung_app']['bugreport']['write-read'] = '[open open][write read]'
G.edge['samsung_app']['bugreport']['fill'] = 'red'
G.add_edge('samsung_app','bugreport')
G.edge['samsung_app']['bugreport']['write-read'] = '[open open][write read][append read]'
G.add_edge('samsung_app','dumpstate')
G.edge['samsung_app']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['samsung_app']['dumpstate']['fill'] = 'red'
G.add_edge('samsung_app','dumpstate')
G.edge['samsung_app']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('samsung_app','dumpsys')
G.edge['samsung_app']['dumpsys']['write-read'] = '[open open][write read]'
G.edge['samsung_app']['dumpsys']['fill'] = 'red'
G.add_edge('samsung_app','dumpsys')
G.edge['samsung_app']['dumpsys']['write-read'] = '[open open][write read][append read]'
G.add_edge('samsung_app','imscm')
G.edge['samsung_app']['imscm']['write-read'] = '[open open][write read]'
G.edge['samsung_app']['imscm']['fill'] = 'red'
G.add_edge('samsung_app','imscm')
G.edge['samsung_app']['imscm']['write-read'] = '[open open][write read][append read]'
G.add_edge('samsung_app','irsc_util')
G.edge['samsung_app']['irsc_util']['write-read'] = '[write read]'
G.edge['samsung_app']['irsc_util']['fill'] = 'red'
G.add_edge('samsung_app','logwrapper')
G.edge['samsung_app']['logwrapper']['write-read'] = '[open open][write read]'
G.edge['samsung_app']['logwrapper']['fill'] = 'red'
G.add_edge('samsung_app','logwrapper')
G.edge['samsung_app']['logwrapper']['write-read'] = '[open open][write read][append read]'
G.add_edge('samsung_app','mediaserver')
G.edge['samsung_app']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['samsung_app']['mediaserver']['fill'] = 'red'
G.add_edge('samsung_app','mediaserver')
G.edge['samsung_app']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('samsung_app','netd')
G.edge['samsung_app']['netd']['write-read'] = '[write read][append read][open open][write read]'
G.edge['samsung_app']['netd']['fill'] = 'red'
G.add_edge('samsung_app','netd')
G.edge['samsung_app']['netd']['write-read'] = '[write read][append read][open open][write read][append read]'
G.add_edge('samsung_app','newAttr49')
G.edge['samsung_app']['newAttr49']['write-read'] = '[write read]'
G.edge['samsung_app']['newAttr49']['fill'] = 'red'
G.add_edge('samsung_app','newAttr9')
G.edge['samsung_app']['newAttr9']['write-read'] = '[write read]'
G.edge['samsung_app']['newAttr9']['fill'] = 'red'
G.add_edge('samsung_app','radio')
G.edge['samsung_app']['radio']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['samsung_app']['radio']['fill'] = 'red'
G.add_edge('samsung_app','runas')
G.edge['samsung_app']['runas']['write-read'] = '[write read]'
G.edge['samsung_app']['runas']['fill'] = 'red'
G.add_edge('samsung_app','samsung_app')
G.edge['samsung_app']['samsung_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read]'
G.edge['samsung_app']['samsung_app']['fill'] = 'red'
G.add_edge('samsung_app','samsung_app')
G.edge['samsung_app']['samsung_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read]'
G.add_edge('samsung_app','shell')
G.edge['samsung_app']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['samsung_app']['shell']['fill'] = 'red'
G.add_edge('samsung_app','shell')
G.edge['samsung_app']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('samsung_app','surfaceflinger')
G.edge['samsung_app']['surfaceflinger']['write-read'] = '[write read][append read][write read]'
G.edge['samsung_app']['surfaceflinger']['fill'] = 'red'
G.add_edge('samsung_app','system_server')
G.edge['samsung_app']['system_server']['write-read'] = '[write read][append read][open open][write read]'
G.edge['samsung_app']['system_server']['fill'] = 'red'
G.add_edge('samsung_app','system_server')
G.edge['samsung_app']['system_server']['write-read'] = '[write read][append read][open open][write read][append read]'
G.add_edge('samsung_app','untrusteddomain')
G.edge['samsung_app']['untrusteddomain']['write-read'] = '[open open][write read]'
G.edge['samsung_app']['untrusteddomain']['fill'] = 'red'
G.add_edge('samsung_app','untrusteddomain')
G.edge['samsung_app']['untrusteddomain']['write-read'] = '[open open][write read][append read]'
G.add_edge('samsung_app','vold')
G.edge['samsung_app']['vold']['write-read'] = '[write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['samsung_app']['vold']['fill'] = 'red'
G.add_edge('samsung_app','vold')
G.edge['samsung_app']['vold']['write-read'] = '[write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('selinux_net','ppp')
G.edge['selinux_net']['ppp']['write-read'] = '[setattr getattr]'
G.add_edge('selinux_net','pppoewrapper')
G.edge['selinux_net']['pppoewrapper']['write-read'] = '[setattr getattr]'
G.add_edge('shell','adbd')
G.edge['shell']['adbd']['write-read'] = '[write read][add_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('shell','binderservicedomain')
G.edge['shell']['binderservicedomain']['write-read'] = '[open open]'
G.add_edge('shell','bugreport')
G.edge['shell']['bugreport']['write-read'] = '[open open]'
G.add_edge('shell','dumpstate')
G.edge['shell']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('shell','dumpsys')
G.edge['shell']['dumpsys']['write-read'] = '[open open]'
G.add_edge('shell','imscm')
G.edge['shell']['imscm']['write-read'] = '[open open]'
G.add_edge('shell','logwrapper')
G.edge['shell']['logwrapper']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('shell','mediaserver')
G.edge['shell']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('shell','netd')
G.edge['shell']['netd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('shell','ppp')
G.edge['shell']['ppp']['write-read'] = '[open open]'
G.add_edge('shell','pppoewrapper')
G.edge['shell']['pppoewrapper']['write-read'] = '[open open]'
G.add_edge('shell','samsung_app')
G.edge['shell']['samsung_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('shell','shell')
G.edge['shell']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('shell','system_server')
G.edge['shell']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('shell','untrusteddomain')
G.edge['shell']['untrusteddomain']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open]'
G.add_edge('shell','vold')
G.edge['shell']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('shell','ppp')
G.edge['shell']['ppp']['write-read'] = '[open open][setattr getattr]'
G.add_edge('shell','pppoewrapper')
G.edge['shell']['pppoewrapper']['write-read'] = '[open open][setattr getattr]'
G.add_edge('shell','adbd')
G.edge['shell']['adbd']['write-read'] = '[write read][add_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['shell']['adbd']['fill'] = 'red'
G.add_edge('shell','adbd')
G.edge['shell']['adbd']['write-read'] = '[write read][add_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('shell','appdomain')
G.edge['shell']['appdomain']['write-read'] = '[open open][write read][append read][write read]'
G.edge['shell']['appdomain']['fill'] = 'red'
G.add_edge('shell','binderservicedomain')
G.edge['shell']['binderservicedomain']['write-read'] = '[open open][write read]'
G.edge['shell']['binderservicedomain']['fill'] = 'red'
G.add_edge('shell','binderservicedomain')
G.edge['shell']['binderservicedomain']['write-read'] = '[open open][write read][append read]'
G.add_edge('shell','bluetooth')
G.edge['shell']['bluetooth']['write-read'] = '[setopt getopt][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['shell']['bluetooth']['fill'] = 'red'
G.add_edge('shell','bugreport')
G.edge['shell']['bugreport']['write-read'] = '[open open][write read]'
G.edge['shell']['bugreport']['fill'] = 'red'
G.add_edge('shell','bugreport')
G.edge['shell']['bugreport']['write-read'] = '[open open][write read][append read]'
G.add_edge('shell','dumpstate')
G.edge['shell']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['shell']['dumpstate']['fill'] = 'red'
G.add_edge('shell','dumpstate')
G.edge['shell']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('shell','dumpsys')
G.edge['shell']['dumpsys']['write-read'] = '[open open][write read]'
G.edge['shell']['dumpsys']['fill'] = 'red'
G.add_edge('shell','dumpsys')
G.edge['shell']['dumpsys']['write-read'] = '[open open][write read][append read]'
G.add_edge('shell','imscm')
G.edge['shell']['imscm']['write-read'] = '[open open][write read]'
G.edge['shell']['imscm']['fill'] = 'red'
G.add_edge('shell','imscm')
G.edge['shell']['imscm']['write-read'] = '[open open][write read][append read]'
G.add_edge('shell','irsc_util')
G.edge['shell']['irsc_util']['write-read'] = '[write read]'
G.edge['shell']['irsc_util']['fill'] = 'red'
G.add_edge('shell','logwrapper')
G.edge['shell']['logwrapper']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['shell']['logwrapper']['fill'] = 'red'
G.add_edge('shell','logwrapper')
G.edge['shell']['logwrapper']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('shell','mediaserver')
G.edge['shell']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read]'
G.edge['shell']['mediaserver']['fill'] = 'red'
G.add_edge('shell','mediaserver')
G.edge['shell']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('shell','netd')
G.edge['shell']['netd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['shell']['netd']['fill'] = 'red'
G.add_edge('shell','netd')
G.edge['shell']['netd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('shell','newAttr49')
G.edge['shell']['newAttr49']['write-read'] = '[write read]'
G.edge['shell']['newAttr49']['fill'] = 'red'
G.add_edge('shell','newAttr9')
G.edge['shell']['newAttr9']['write-read'] = '[write read]'
G.edge['shell']['newAttr9']['fill'] = 'red'
G.add_edge('shell','radio')
G.edge['shell']['radio']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['shell']['radio']['fill'] = 'red'
G.add_edge('shell','runas')
G.edge['shell']['runas']['write-read'] = '[write read]'
G.edge['shell']['runas']['fill'] = 'red'
G.add_edge('shell','samsung_app')
G.edge['shell']['samsung_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['shell']['samsung_app']['fill'] = 'red'
G.add_edge('shell','samsung_app')
G.edge['shell']['samsung_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('shell','shell')
G.edge['shell']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['shell']['shell']['fill'] = 'red'
G.add_edge('shell','shell')
G.edge['shell']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('shell','surfaceflinger')
G.edge['shell']['surfaceflinger']['write-read'] = '[write read]'
G.edge['shell']['surfaceflinger']['fill'] = 'red'
G.add_edge('shell','system_server')
G.edge['shell']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['shell']['system_server']['fill'] = 'red'
G.add_edge('shell','system_server')
G.edge['shell']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('shell','untrusteddomain')
G.edge['shell']['untrusteddomain']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read]'
G.edge['shell']['untrusteddomain']['fill'] = 'red'
G.add_edge('shell','untrusteddomain')
G.edge['shell']['untrusteddomain']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read]'
G.add_edge('shell','vold')
G.edge['shell']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read]'
G.edge['shell']['vold']['fill'] = 'red'
G.add_edge('shell','vold')
G.edge['shell']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('surfaceflinger','adbd')
G.edge['surfaceflinger']['adbd']['write-read'] = '[open open][write read][append read][write read]'
G.edge['surfaceflinger']['adbd']['fill'] = 'red'
G.add_edge('surfaceflinger','adbd')
G.edge['surfaceflinger']['adbd']['write-read'] = '[open open][write read][append read][write read][append read]'
G.add_edge('surfaceflinger','appdomain')
G.edge['surfaceflinger']['appdomain']['write-read'] = '[open open][write read][append read][write read]'
G.edge['surfaceflinger']['appdomain']['fill'] = 'red'
G.add_edge('surfaceflinger','binderservicedomain')
G.edge['surfaceflinger']['binderservicedomain']['write-read'] = '[write read]'
G.edge['surfaceflinger']['binderservicedomain']['fill'] = 'red'
G.add_edge('surfaceflinger','binderservicedomain')
G.edge['surfaceflinger']['binderservicedomain']['write-read'] = '[write read][append read]'
G.add_edge('surfaceflinger','bluetooth')
G.edge['surfaceflinger']['bluetooth']['write-read'] = '[write read]'
G.edge['surfaceflinger']['bluetooth']['fill'] = 'red'
G.add_edge('surfaceflinger','bugreport')
G.edge['surfaceflinger']['bugreport']['write-read'] = '[write read]'
G.edge['surfaceflinger']['bugreport']['fill'] = 'red'
G.add_edge('surfaceflinger','bugreport')
G.edge['surfaceflinger']['bugreport']['write-read'] = '[write read][append read]'
G.add_edge('surfaceflinger','dumpstate')
G.edge['surfaceflinger']['dumpstate']['write-read'] = '[open open][write read][append read][write read]'
G.edge['surfaceflinger']['dumpstate']['fill'] = 'red'
G.add_edge('surfaceflinger','dumpstate')
G.edge['surfaceflinger']['dumpstate']['write-read'] = '[open open][write read][append read][write read][append read]'
G.add_edge('surfaceflinger','dumpsys')
G.edge['surfaceflinger']['dumpsys']['write-read'] = '[write read]'
G.edge['surfaceflinger']['dumpsys']['fill'] = 'red'
G.add_edge('surfaceflinger','dumpsys')
G.edge['surfaceflinger']['dumpsys']['write-read'] = '[write read][append read]'
G.add_edge('surfaceflinger','imscm')
G.edge['surfaceflinger']['imscm']['write-read'] = '[write read]'
G.edge['surfaceflinger']['imscm']['fill'] = 'red'
G.add_edge('surfaceflinger','imscm')
G.edge['surfaceflinger']['imscm']['write-read'] = '[write read][append read]'
G.add_edge('surfaceflinger','irsc_util')
G.edge['surfaceflinger']['irsc_util']['write-read'] = '[write read]'
G.edge['surfaceflinger']['irsc_util']['fill'] = 'red'
G.add_edge('surfaceflinger','logwrapper')
G.edge['surfaceflinger']['logwrapper']['write-read'] = '[write read]'
G.edge['surfaceflinger']['logwrapper']['fill'] = 'red'
G.add_edge('surfaceflinger','logwrapper')
G.edge['surfaceflinger']['logwrapper']['write-read'] = '[write read][append read]'
G.add_edge('surfaceflinger','mediaserver')
G.edge['surfaceflinger']['mediaserver']['write-read'] = '[open open][write read][append read][write read]'
G.edge['surfaceflinger']['mediaserver']['fill'] = 'red'
G.add_edge('surfaceflinger','mediaserver')
G.edge['surfaceflinger']['mediaserver']['write-read'] = '[open open][write read][append read][write read][append read]'
G.add_edge('surfaceflinger','netd')
G.edge['surfaceflinger']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read]'
G.edge['surfaceflinger']['netd']['fill'] = 'red'
G.add_edge('surfaceflinger','netd')
G.edge['surfaceflinger']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read]'
G.add_edge('surfaceflinger','newAttr49')
G.edge['surfaceflinger']['newAttr49']['write-read'] = '[write read]'
G.edge['surfaceflinger']['newAttr49']['fill'] = 'red'
G.add_edge('surfaceflinger','newAttr9')
G.edge['surfaceflinger']['newAttr9']['write-read'] = '[write read]'
G.edge['surfaceflinger']['newAttr9']['fill'] = 'red'
G.add_edge('surfaceflinger','radio')
G.edge['surfaceflinger']['radio']['write-read'] = '[open open][write read][append read][write read]'
G.edge['surfaceflinger']['radio']['fill'] = 'red'
G.add_edge('surfaceflinger','runas')
G.edge['surfaceflinger']['runas']['write-read'] = '[write read]'
G.edge['surfaceflinger']['runas']['fill'] = 'red'
G.add_edge('surfaceflinger','samsung_app')
G.edge['surfaceflinger']['samsung_app']['write-read'] = '[setopt getopt][write read]'
G.edge['surfaceflinger']['samsung_app']['fill'] = 'red'
G.add_edge('surfaceflinger','samsung_app')
G.edge['surfaceflinger']['samsung_app']['write-read'] = '[setopt getopt][write read][append read]'
G.add_edge('surfaceflinger','shell')
G.edge['surfaceflinger']['shell']['write-read'] = '[write read]'
G.edge['surfaceflinger']['shell']['fill'] = 'red'
G.add_edge('surfaceflinger','shell')
G.edge['surfaceflinger']['shell']['write-read'] = '[write read][append read]'
G.add_edge('surfaceflinger','surfaceflinger')
G.edge['surfaceflinger']['surfaceflinger']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read]'
G.edge['surfaceflinger']['surfaceflinger']['fill'] = 'red'
G.add_edge('surfaceflinger','system_server')
G.edge['surfaceflinger']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][write read]'
G.edge['surfaceflinger']['system_server']['fill'] = 'red'
G.add_edge('surfaceflinger','system_server')
G.edge['surfaceflinger']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][write read][append read]'
G.add_edge('surfaceflinger','untrusteddomain')
G.edge['surfaceflinger']['untrusteddomain']['write-read'] = '[write read]'
G.edge['surfaceflinger']['untrusteddomain']['fill'] = 'red'
G.add_edge('surfaceflinger','untrusteddomain')
G.edge['surfaceflinger']['untrusteddomain']['write-read'] = '[write read][append read]'
G.add_edge('surfaceflinger','vold')
G.edge['surfaceflinger']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read]'
G.edge['surfaceflinger']['vold']['fill'] = 'red'
G.add_edge('surfaceflinger','vold')
G.edge['surfaceflinger']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read]'
G.add_edge('system_server','adbd')
G.edge['system_server']['adbd']['write-read'] = '[write read][add_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('system_server','binderservicedomain')
G.edge['system_server']['binderservicedomain']['write-read'] = '[open open]'
G.add_edge('system_server','bugreport')
G.edge['system_server']['bugreport']['write-read'] = '[open open]'
G.add_edge('system_server','dumpstate')
G.edge['system_server']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('system_server','dumpsys')
G.edge['system_server']['dumpsys']['write-read'] = '[open open]'
G.add_edge('system_server','imscm')
G.edge['system_server']['imscm']['write-read'] = '[open open]'
G.add_edge('system_server','logwrapper')
G.edge['system_server']['logwrapper']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('system_server','mediaserver')
G.edge['system_server']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('system_server','netd')
G.edge['system_server']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('system_server','ppp')
G.edge['system_server']['ppp']['write-read'] = '[open open]'
G.add_edge('system_server','pppoewrapper')
G.edge['system_server']['pppoewrapper']['write-read'] = '[open open]'
G.add_edge('system_server','samsung_app')
G.edge['system_server']['samsung_app']['write-read'] = '[setopt getopt][open open]'
G.add_edge('system_server','shell')
G.edge['system_server']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][setsched getsched][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('system_server','untrusteddomain')
G.edge['system_server']['untrusteddomain']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('system_server','vold')
G.edge['system_server']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('system_server','ppp')
G.edge['system_server']['ppp']['write-read'] = '[open open][setattr getattr]'
G.add_edge('system_server','pppoewrapper')
G.edge['system_server']['pppoewrapper']['write-read'] = '[open open][setattr getattr]'
G.add_edge('system_server','adbd')
G.edge['system_server']['adbd']['write-read'] = '[write read][add_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['system_server']['adbd']['fill'] = 'red'
G.add_edge('system_server','adbd')
G.edge['system_server']['adbd']['write-read'] = '[write read][add_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('system_server','appdomain')
G.edge['system_server']['appdomain']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][append read][write read]'
G.edge['system_server']['appdomain']['fill'] = 'red'
G.add_edge('system_server','binderservicedomain')
G.edge['system_server']['binderservicedomain']['write-read'] = '[open open][write read]'
G.edge['system_server']['binderservicedomain']['fill'] = 'red'
G.add_edge('system_server','binderservicedomain')
G.edge['system_server']['binderservicedomain']['write-read'] = '[open open][write read][append read]'
G.add_edge('system_server','bluetooth')
G.edge['system_server']['bluetooth']['write-read'] = '[setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read]'
G.edge['system_server']['bluetooth']['fill'] = 'red'
G.add_edge('system_server','bugreport')
G.edge['system_server']['bugreport']['write-read'] = '[open open][write read]'
G.edge['system_server']['bugreport']['fill'] = 'red'
G.add_edge('system_server','bugreport')
G.edge['system_server']['bugreport']['write-read'] = '[open open][write read][append read]'
G.add_edge('system_server','dumpstate')
G.edge['system_server']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['system_server']['dumpstate']['fill'] = 'red'
G.add_edge('system_server','dumpstate')
G.edge['system_server']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('system_server','dumpsys')
G.edge['system_server']['dumpsys']['write-read'] = '[open open][write read]'
G.edge['system_server']['dumpsys']['fill'] = 'red'
G.add_edge('system_server','dumpsys')
G.edge['system_server']['dumpsys']['write-read'] = '[open open][write read][append read]'
G.add_edge('system_server','imscm')
G.edge['system_server']['imscm']['write-read'] = '[open open][write read]'
G.edge['system_server']['imscm']['fill'] = 'red'
G.add_edge('system_server','imscm')
G.edge['system_server']['imscm']['write-read'] = '[open open][write read][append read]'
G.add_edge('system_server','irsc_util')
G.edge['system_server']['irsc_util']['write-read'] = '[write read]'
G.edge['system_server']['irsc_util']['fill'] = 'red'
G.add_edge('system_server','logwrapper')
G.edge['system_server']['logwrapper']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['system_server']['logwrapper']['fill'] = 'red'
G.add_edge('system_server','logwrapper')
G.edge['system_server']['logwrapper']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('system_server','mediaserver')
G.edge['system_server']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][add_name search][remove_name search][open open][write read][append read][open open][write read]'
G.edge['system_server']['mediaserver']['fill'] = 'red'
G.add_edge('system_server','mediaserver')
G.edge['system_server']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read]'
G.add_edge('system_server','netd')
G.edge['system_server']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read]'
G.edge['system_server']['netd']['fill'] = 'red'
G.add_edge('system_server','netd')
G.edge['system_server']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('system_server','newAttr49')
G.edge['system_server']['newAttr49']['write-read'] = '[write read]'
G.edge['system_server']['newAttr49']['fill'] = 'red'
G.add_edge('system_server','newAttr9')
G.edge['system_server']['newAttr9']['write-read'] = '[write read]'
G.edge['system_server']['newAttr9']['fill'] = 'red'
G.add_edge('system_server','radio')
G.edge['system_server']['radio']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][setattr getattr][write read]'
G.edge['system_server']['radio']['fill'] = 'red'
G.add_edge('system_server','runas')
G.edge['system_server']['runas']['write-read'] = '[open open][write read][append read][write read]'
G.edge['system_server']['runas']['fill'] = 'red'
G.add_edge('system_server','samsung_app')
G.edge['system_server']['samsung_app']['write-read'] = '[setopt getopt][open open][write read]'
G.edge['system_server']['samsung_app']['fill'] = 'red'
G.add_edge('system_server','samsung_app')
G.edge['system_server']['samsung_app']['write-read'] = '[setopt getopt][open open][write read][append read]'
G.add_edge('system_server','shell')
G.edge['system_server']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['system_server']['shell']['fill'] = 'red'
G.add_edge('system_server','shell')
G.edge['system_server']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('system_server','surfaceflinger')
G.edge['system_server']['surfaceflinger']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][write read]'
G.edge['system_server']['surfaceflinger']['fill'] = 'red'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][setsched getsched][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['system_server']['system_server']['fill'] = 'red'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][setsched getsched][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('system_server','untrusteddomain')
G.edge['system_server']['untrusteddomain']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['system_server']['untrusteddomain']['fill'] = 'red'
G.add_edge('system_server','untrusteddomain')
G.edge['system_server']['untrusteddomain']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('system_server','vold')
G.edge['system_server']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['system_server']['vold']['fill'] = 'red'
G.add_edge('system_server','vold')
G.edge['system_server']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('untrusteddomain','adbd')
G.edge['untrusteddomain']['adbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('untrusteddomain','binderservicedomain')
G.edge['untrusteddomain']['binderservicedomain']['write-read'] = '[open open]'
G.add_edge('untrusteddomain','bugreport')
G.edge['untrusteddomain']['bugreport']['write-read'] = '[open open]'
G.add_edge('untrusteddomain','dumpstate')
G.edge['untrusteddomain']['dumpstate']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('untrusteddomain','dumpsys')
G.edge['untrusteddomain']['dumpsys']['write-read'] = '[open open]'
G.add_edge('untrusteddomain','imscm')
G.edge['untrusteddomain']['imscm']['write-read'] = '[open open]'
G.add_edge('untrusteddomain','logwrapper')
G.edge['untrusteddomain']['logwrapper']['write-read'] = '[open open]'
G.add_edge('untrusteddomain','mediaserver')
G.edge['untrusteddomain']['mediaserver']['write-read'] = '[open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('untrusteddomain','netd')
G.edge['untrusteddomain']['netd']['write-read'] = '[open open]'
G.add_edge('untrusteddomain','ppp')
G.edge['untrusteddomain']['ppp']['write-read'] = '[open open]'
G.add_edge('untrusteddomain','pppoewrapper')
G.edge['untrusteddomain']['pppoewrapper']['write-read'] = '[open open]'
G.add_edge('untrusteddomain','samsung_app')
G.edge['untrusteddomain']['samsung_app']['write-read'] = '[open open]'
G.add_edge('untrusteddomain','shell')
G.edge['untrusteddomain']['shell']['write-read'] = '[write read][setopt getopt][open open]'
G.add_edge('untrusteddomain','system_server')
G.edge['untrusteddomain']['system_server']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('untrusteddomain','untrusteddomain')
G.edge['untrusteddomain']['untrusteddomain']['write-read'] = '[open open][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('untrusteddomain','vold')
G.edge['untrusteddomain']['vold']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('untrusteddomain','ppp')
G.edge['untrusteddomain']['ppp']['write-read'] = '[open open][setattr getattr]'
G.add_edge('untrusteddomain','pppoewrapper')
G.edge['untrusteddomain']['pppoewrapper']['write-read'] = '[open open][setattr getattr]'
G.add_edge('untrusteddomain','adbd')
G.edge['untrusteddomain']['adbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['untrusteddomain']['adbd']['fill'] = 'red'
G.add_edge('untrusteddomain','adbd')
G.edge['untrusteddomain']['adbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('untrusteddomain','appdomain')
G.edge['untrusteddomain']['appdomain']['write-read'] = '[open open][write read][append read][write read]'
G.edge['untrusteddomain']['appdomain']['fill'] = 'red'
G.add_edge('untrusteddomain','binderservicedomain')
G.edge['untrusteddomain']['binderservicedomain']['write-read'] = '[open open][write read]'
G.edge['untrusteddomain']['binderservicedomain']['fill'] = 'red'
G.add_edge('untrusteddomain','binderservicedomain')
G.edge['untrusteddomain']['binderservicedomain']['write-read'] = '[open open][write read][append read]'
G.add_edge('untrusteddomain','bluetooth')
G.edge['untrusteddomain']['bluetooth']['write-read'] = '[setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['untrusteddomain']['bluetooth']['fill'] = 'red'
G.add_edge('untrusteddomain','bugreport')
G.edge['untrusteddomain']['bugreport']['write-read'] = '[open open][write read]'
G.edge['untrusteddomain']['bugreport']['fill'] = 'red'
G.add_edge('untrusteddomain','bugreport')
G.edge['untrusteddomain']['bugreport']['write-read'] = '[open open][write read][append read]'
G.add_edge('untrusteddomain','dumpstate')
G.edge['untrusteddomain']['dumpstate']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read]'
G.edge['untrusteddomain']['dumpstate']['fill'] = 'red'
G.add_edge('untrusteddomain','dumpstate')
G.edge['untrusteddomain']['dumpstate']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('untrusteddomain','dumpsys')
G.edge['untrusteddomain']['dumpsys']['write-read'] = '[open open][write read]'
G.edge['untrusteddomain']['dumpsys']['fill'] = 'red'
G.add_edge('untrusteddomain','dumpsys')
G.edge['untrusteddomain']['dumpsys']['write-read'] = '[open open][write read][append read]'
G.add_edge('untrusteddomain','imscm')
G.edge['untrusteddomain']['imscm']['write-read'] = '[open open][write read]'
G.edge['untrusteddomain']['imscm']['fill'] = 'red'
G.add_edge('untrusteddomain','imscm')
G.edge['untrusteddomain']['imscm']['write-read'] = '[open open][write read][append read]'
G.add_edge('untrusteddomain','irsc_util')
G.edge['untrusteddomain']['irsc_util']['write-read'] = '[write read]'
G.edge['untrusteddomain']['irsc_util']['fill'] = 'red'
G.add_edge('untrusteddomain','logwrapper')
G.edge['untrusteddomain']['logwrapper']['write-read'] = '[open open][write read]'
G.edge['untrusteddomain']['logwrapper']['fill'] = 'red'
G.add_edge('untrusteddomain','logwrapper')
G.edge['untrusteddomain']['logwrapper']['write-read'] = '[open open][write read][append read]'
G.add_edge('untrusteddomain','mediaserver')
G.edge['untrusteddomain']['mediaserver']['write-read'] = '[open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['untrusteddomain']['mediaserver']['fill'] = 'red'
G.add_edge('untrusteddomain','mediaserver')
G.edge['untrusteddomain']['mediaserver']['write-read'] = '[open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('untrusteddomain','netd')
G.edge['untrusteddomain']['netd']['write-read'] = '[open open][write read]'
G.edge['untrusteddomain']['netd']['fill'] = 'red'
G.add_edge('untrusteddomain','netd')
G.edge['untrusteddomain']['netd']['write-read'] = '[open open][write read][append read]'
G.add_edge('untrusteddomain','newAttr49')
G.edge['untrusteddomain']['newAttr49']['write-read'] = '[write read]'
G.edge['untrusteddomain']['newAttr49']['fill'] = 'red'
G.add_edge('untrusteddomain','newAttr9')
G.edge['untrusteddomain']['newAttr9']['write-read'] = '[write read]'
G.edge['untrusteddomain']['newAttr9']['fill'] = 'red'
G.add_edge('untrusteddomain','radio')
G.edge['untrusteddomain']['radio']['write-read'] = '[setattr getattr][write read]'
G.edge['untrusteddomain']['radio']['fill'] = 'red'
G.add_edge('untrusteddomain','runas')
G.edge['untrusteddomain']['runas']['write-read'] = '[open open][write read][append read][write read]'
G.edge['untrusteddomain']['runas']['fill'] = 'red'
G.add_edge('untrusteddomain','samsung_app')
G.edge['untrusteddomain']['samsung_app']['write-read'] = '[open open][write read]'
G.edge['untrusteddomain']['samsung_app']['fill'] = 'red'
G.add_edge('untrusteddomain','samsung_app')
G.edge['untrusteddomain']['samsung_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('untrusteddomain','shell')
G.edge['untrusteddomain']['shell']['write-read'] = '[write read][setopt getopt][open open][write read]'
G.edge['untrusteddomain']['shell']['fill'] = 'red'
G.add_edge('untrusteddomain','shell')
G.edge['untrusteddomain']['shell']['write-read'] = '[write read][setopt getopt][open open][write read][append read]'
G.add_edge('untrusteddomain','surfaceflinger')
G.edge['untrusteddomain']['surfaceflinger']['write-read'] = '[write read]'
G.edge['untrusteddomain']['surfaceflinger']['fill'] = 'red'
G.add_edge('untrusteddomain','system_server')
G.edge['untrusteddomain']['system_server']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['untrusteddomain']['system_server']['fill'] = 'red'
G.add_edge('untrusteddomain','system_server')
G.edge['untrusteddomain']['system_server']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('untrusteddomain','untrusteddomain')
G.edge['untrusteddomain']['untrusteddomain']['write-read'] = '[open open][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['untrusteddomain']['untrusteddomain']['fill'] = 'red'
G.add_edge('untrusteddomain','untrusteddomain')
G.edge['untrusteddomain']['untrusteddomain']['write-read'] = '[open open][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('untrusteddomain','vold')
G.edge['untrusteddomain']['vold']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read]'
G.edge['untrusteddomain']['vold']['fill'] = 'red'
G.add_edge('untrusteddomain','vold')
G.edge['untrusteddomain']['vold']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('untrusteddomain','adbd')
G.edge['untrusteddomain']['adbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('untrusteddomain','binderservicedomain')
G.edge['untrusteddomain']['binderservicedomain']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('untrusteddomain','bugreport')
G.edge['untrusteddomain']['bugreport']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('untrusteddomain','dumpstate')
G.edge['untrusteddomain']['dumpstate']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('untrusteddomain','dumpsys')
G.edge['untrusteddomain']['dumpsys']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('untrusteddomain','imscm')
G.edge['untrusteddomain']['imscm']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('untrusteddomain','logwrapper')
G.edge['untrusteddomain']['logwrapper']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('untrusteddomain','mediaserver')
G.edge['untrusteddomain']['mediaserver']['write-read'] = '[open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('untrusteddomain','netd')
G.edge['untrusteddomain']['netd']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('untrusteddomain','ppp')
G.edge['untrusteddomain']['ppp']['write-read'] = '[open open][setattr getattr][open open]'
G.add_edge('untrusteddomain','pppoewrapper')
G.edge['untrusteddomain']['pppoewrapper']['write-read'] = '[open open][setattr getattr][open open]'
G.add_edge('untrusteddomain','samsung_app')
G.edge['untrusteddomain']['samsung_app']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('untrusteddomain','shell')
G.edge['untrusteddomain']['shell']['write-read'] = '[write read][setopt getopt][open open][write read][append read][open open]'
G.add_edge('untrusteddomain','system_server')
G.edge['untrusteddomain']['system_server']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('untrusteddomain','untrusteddomain')
G.edge['untrusteddomain']['untrusteddomain']['write-read'] = '[open open][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('untrusteddomain','vold')
G.edge['untrusteddomain']['vold']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('untrusteddomain','ppp')
G.edge['untrusteddomain']['ppp']['write-read'] = '[open open][setattr getattr][open open][setattr getattr]'
G.add_edge('untrusteddomain','pppoewrapper')
G.edge['untrusteddomain']['pppoewrapper']['write-read'] = '[open open][setattr getattr][open open][setattr getattr]'
G.add_edge('untrusteddomain','adbd')
G.edge['untrusteddomain']['adbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read]'
G.edge['untrusteddomain']['adbd']['fill'] = 'red'
G.add_edge('untrusteddomain','adbd')
G.edge['untrusteddomain']['adbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read]'
G.add_edge('untrusteddomain','appdomain')
G.edge['untrusteddomain']['appdomain']['write-read'] = '[open open][write read][append read][write read][write read]'
G.edge['untrusteddomain']['appdomain']['fill'] = 'red'
G.add_edge('untrusteddomain','binderservicedomain')
G.edge['untrusteddomain']['binderservicedomain']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['untrusteddomain']['binderservicedomain']['fill'] = 'red'
G.add_edge('untrusteddomain','binderservicedomain')
G.edge['untrusteddomain']['binderservicedomain']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('untrusteddomain','bluetooth')
G.edge['untrusteddomain']['bluetooth']['write-read'] = '[setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][write read]'
G.edge['untrusteddomain']['bluetooth']['fill'] = 'red'
G.add_edge('untrusteddomain','bugreport')
G.edge['untrusteddomain']['bugreport']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['untrusteddomain']['bugreport']['fill'] = 'red'
G.add_edge('untrusteddomain','bugreport')
G.edge['untrusteddomain']['bugreport']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('untrusteddomain','dumpstate')
G.edge['untrusteddomain']['dumpstate']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][write read]'
G.edge['untrusteddomain']['dumpstate']['fill'] = 'red'
G.add_edge('untrusteddomain','dumpstate')
G.edge['untrusteddomain']['dumpstate']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][write read][append read]'
G.add_edge('untrusteddomain','dumpsys')
G.edge['untrusteddomain']['dumpsys']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['untrusteddomain']['dumpsys']['fill'] = 'red'
G.add_edge('untrusteddomain','dumpsys')
G.edge['untrusteddomain']['dumpsys']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('untrusteddomain','imscm')
G.edge['untrusteddomain']['imscm']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['untrusteddomain']['imscm']['fill'] = 'red'
G.add_edge('untrusteddomain','imscm')
G.edge['untrusteddomain']['imscm']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('untrusteddomain','irsc_util')
G.edge['untrusteddomain']['irsc_util']['write-read'] = '[write read][write read]'
G.edge['untrusteddomain']['irsc_util']['fill'] = 'red'
G.add_edge('untrusteddomain','logwrapper')
G.edge['untrusteddomain']['logwrapper']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['untrusteddomain']['logwrapper']['fill'] = 'red'
G.add_edge('untrusteddomain','logwrapper')
G.edge['untrusteddomain']['logwrapper']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('untrusteddomain','mediaserver')
G.edge['untrusteddomain']['mediaserver']['write-read'] = '[open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read]'
G.edge['untrusteddomain']['mediaserver']['fill'] = 'red'
G.add_edge('untrusteddomain','mediaserver')
G.edge['untrusteddomain']['mediaserver']['write-read'] = '[open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read]'
G.add_edge('untrusteddomain','netd')
G.edge['untrusteddomain']['netd']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['untrusteddomain']['netd']['fill'] = 'red'
G.add_edge('untrusteddomain','netd')
G.edge['untrusteddomain']['netd']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('untrusteddomain','newAttr49')
G.edge['untrusteddomain']['newAttr49']['write-read'] = '[write read][write read]'
G.edge['untrusteddomain']['newAttr49']['fill'] = 'red'
G.add_edge('untrusteddomain','newAttr9')
G.edge['untrusteddomain']['newAttr9']['write-read'] = '[write read][write read]'
G.edge['untrusteddomain']['newAttr9']['fill'] = 'red'
G.add_edge('untrusteddomain','radio')
G.edge['untrusteddomain']['radio']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['untrusteddomain']['radio']['fill'] = 'red'
G.add_edge('untrusteddomain','runas')
G.edge['untrusteddomain']['runas']['write-read'] = '[open open][write read][append read][write read][write read]'
G.edge['untrusteddomain']['runas']['fill'] = 'red'
G.add_edge('untrusteddomain','samsung_app')
G.edge['untrusteddomain']['samsung_app']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['untrusteddomain']['samsung_app']['fill'] = 'red'
G.add_edge('untrusteddomain','samsung_app')
G.edge['untrusteddomain']['samsung_app']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('untrusteddomain','shell')
G.edge['untrusteddomain']['shell']['write-read'] = '[write read][setopt getopt][open open][write read][append read][open open][write read]'
G.edge['untrusteddomain']['shell']['fill'] = 'red'
G.add_edge('untrusteddomain','shell')
G.edge['untrusteddomain']['shell']['write-read'] = '[write read][setopt getopt][open open][write read][append read][open open][write read][append read]'
G.add_edge('untrusteddomain','surfaceflinger')
G.edge['untrusteddomain']['surfaceflinger']['write-read'] = '[write read][write read]'
G.edge['untrusteddomain']['surfaceflinger']['fill'] = 'red'
G.add_edge('untrusteddomain','system_server')
G.edge['untrusteddomain']['system_server']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read]'
G.edge['untrusteddomain']['system_server']['fill'] = 'red'
G.add_edge('untrusteddomain','system_server')
G.edge['untrusteddomain']['system_server']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read]'
G.add_edge('untrusteddomain','untrusteddomain')
G.edge['untrusteddomain']['untrusteddomain']['write-read'] = '[open open][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read]'
G.edge['untrusteddomain']['untrusteddomain']['fill'] = 'red'
G.add_edge('untrusteddomain','untrusteddomain')
G.edge['untrusteddomain']['untrusteddomain']['write-read'] = '[open open][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read]'
G.add_edge('untrusteddomain','vold')
G.edge['untrusteddomain']['vold']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][write read]'
G.edge['untrusteddomain']['vold']['fill'] = 'red'
G.add_edge('untrusteddomain','vold')
G.edge['untrusteddomain']['vold']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][write read][append read]'
G.add_edge('vmware_app','adbd')
G.edge['vmware_app']['adbd']['write-read'] = '[open open]'
G.add_edge('vmware_app','binderservicedomain')
G.edge['vmware_app']['binderservicedomain']['write-read'] = '[open open]'
G.add_edge('vmware_app','bugreport')
G.edge['vmware_app']['bugreport']['write-read'] = '[open open]'
G.add_edge('vmware_app','dumpstate')
G.edge['vmware_app']['dumpstate']['write-read'] = '[open open]'
G.add_edge('vmware_app','dumpsys')
G.edge['vmware_app']['dumpsys']['write-read'] = '[open open]'
G.add_edge('vmware_app','imscm')
G.edge['vmware_app']['imscm']['write-read'] = '[open open]'
G.add_edge('vmware_app','logwrapper')
G.edge['vmware_app']['logwrapper']['write-read'] = '[open open]'
G.add_edge('vmware_app','mediaserver')
G.edge['vmware_app']['mediaserver']['write-read'] = '[open open][write read][add_name search][remove_name search][open open]'
G.add_edge('vmware_app','netd')
G.edge['vmware_app']['netd']['write-read'] = '[open open]'
G.add_edge('vmware_app','ppp')
G.edge['vmware_app']['ppp']['write-read'] = '[open open]'
G.add_edge('vmware_app','pppoewrapper')
G.edge['vmware_app']['pppoewrapper']['write-read'] = '[open open]'
G.add_edge('vmware_app','samsung_app')
G.edge['vmware_app']['samsung_app']['write-read'] = '[open open]'
G.add_edge('vmware_app','shell')
G.edge['vmware_app']['shell']['write-read'] = '[open open]'
G.add_edge('vmware_app','system_server')
G.edge['vmware_app']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('vmware_app','untrusteddomain')
G.edge['vmware_app']['untrusteddomain']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('vmware_app','vold')
G.edge['vmware_app']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('vmware_app','ppp')
G.edge['vmware_app']['ppp']['write-read'] = '[open open][setattr getattr]'
G.add_edge('vmware_app','pppoewrapper')
G.edge['vmware_app']['pppoewrapper']['write-read'] = '[open open][setattr getattr]'
G.add_edge('vmware_app','adbd')
G.edge['vmware_app']['adbd']['write-read'] = '[open open][write read]'
G.edge['vmware_app']['adbd']['fill'] = 'red'
G.add_edge('vmware_app','adbd')
G.edge['vmware_app']['adbd']['write-read'] = '[open open][write read][append read]'
G.add_edge('vmware_app','appdomain')
G.edge['vmware_app']['appdomain']['write-read'] = '[write read]'
G.edge['vmware_app']['appdomain']['fill'] = 'red'
G.add_edge('vmware_app','binderservicedomain')
G.edge['vmware_app']['binderservicedomain']['write-read'] = '[open open][write read]'
G.edge['vmware_app']['binderservicedomain']['fill'] = 'red'
G.add_edge('vmware_app','binderservicedomain')
G.edge['vmware_app']['binderservicedomain']['write-read'] = '[open open][write read][append read]'
G.add_edge('vmware_app','bluetooth')
G.edge['vmware_app']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['vmware_app']['bluetooth']['fill'] = 'red'
G.add_edge('vmware_app','bugreport')
G.edge['vmware_app']['bugreport']['write-read'] = '[open open][write read]'
G.edge['vmware_app']['bugreport']['fill'] = 'red'
G.add_edge('vmware_app','bugreport')
G.edge['vmware_app']['bugreport']['write-read'] = '[open open][write read][append read]'
G.add_edge('vmware_app','dumpstate')
G.edge['vmware_app']['dumpstate']['write-read'] = '[open open][write read]'
G.edge['vmware_app']['dumpstate']['fill'] = 'red'
G.add_edge('vmware_app','dumpstate')
G.edge['vmware_app']['dumpstate']['write-read'] = '[open open][write read][append read]'
G.add_edge('vmware_app','dumpsys')
G.edge['vmware_app']['dumpsys']['write-read'] = '[open open][write read]'
G.edge['vmware_app']['dumpsys']['fill'] = 'red'
G.add_edge('vmware_app','dumpsys')
G.edge['vmware_app']['dumpsys']['write-read'] = '[open open][write read][append read]'
G.add_edge('vmware_app','imscm')
G.edge['vmware_app']['imscm']['write-read'] = '[open open][write read]'
G.edge['vmware_app']['imscm']['fill'] = 'red'
G.add_edge('vmware_app','imscm')
G.edge['vmware_app']['imscm']['write-read'] = '[open open][write read][append read]'
G.add_edge('vmware_app','irsc_util')
G.edge['vmware_app']['irsc_util']['write-read'] = '[write read]'
G.edge['vmware_app']['irsc_util']['fill'] = 'red'
G.add_edge('vmware_app','logwrapper')
G.edge['vmware_app']['logwrapper']['write-read'] = '[open open][write read]'
G.edge['vmware_app']['logwrapper']['fill'] = 'red'
G.add_edge('vmware_app','logwrapper')
G.edge['vmware_app']['logwrapper']['write-read'] = '[open open][write read][append read]'
G.add_edge('vmware_app','mediaserver')
G.edge['vmware_app']['mediaserver']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['vmware_app']['mediaserver']['fill'] = 'red'
G.add_edge('vmware_app','mediaserver')
G.edge['vmware_app']['mediaserver']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('vmware_app','netd')
G.edge['vmware_app']['netd']['write-read'] = '[open open][write read]'
G.edge['vmware_app']['netd']['fill'] = 'red'
G.add_edge('vmware_app','netd')
G.edge['vmware_app']['netd']['write-read'] = '[open open][write read][append read]'
G.add_edge('vmware_app','newAttr49')
G.edge['vmware_app']['newAttr49']['write-read'] = '[write read]'
G.edge['vmware_app']['newAttr49']['fill'] = 'red'
G.add_edge('vmware_app','newAttr9')
G.edge['vmware_app']['newAttr9']['write-read'] = '[write read]'
G.edge['vmware_app']['newAttr9']['fill'] = 'red'
G.add_edge('vmware_app','radio')
G.edge['vmware_app']['radio']['write-read'] = '[write read]'
G.edge['vmware_app']['radio']['fill'] = 'red'
G.add_edge('vmware_app','runas')
G.edge['vmware_app']['runas']['write-read'] = '[write read]'
G.edge['vmware_app']['runas']['fill'] = 'red'
G.add_edge('vmware_app','samsung_app')
G.edge['vmware_app']['samsung_app']['write-read'] = '[open open][write read]'
G.edge['vmware_app']['samsung_app']['fill'] = 'red'
G.add_edge('vmware_app','samsung_app')
G.edge['vmware_app']['samsung_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('vmware_app','shell')
G.edge['vmware_app']['shell']['write-read'] = '[open open][write read]'
G.edge['vmware_app']['shell']['fill'] = 'red'
G.add_edge('vmware_app','shell')
G.edge['vmware_app']['shell']['write-read'] = '[open open][write read][append read]'
G.add_edge('vmware_app','surfaceflinger')
G.edge['vmware_app']['surfaceflinger']['write-read'] = '[write read]'
G.edge['vmware_app']['surfaceflinger']['fill'] = 'red'
G.add_edge('vmware_app','system_server')
G.edge['vmware_app']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['vmware_app']['system_server']['fill'] = 'red'
G.add_edge('vmware_app','system_server')
G.edge['vmware_app']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('vmware_app','untrusteddomain')
G.edge['vmware_app']['untrusteddomain']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['vmware_app']['untrusteddomain']['fill'] = 'red'
G.add_edge('vmware_app','untrusteddomain')
G.edge['vmware_app']['untrusteddomain']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('vmware_app','vold')
G.edge['vmware_app']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['vmware_app']['vold']['fill'] = 'red'
G.add_edge('vmware_app','vold')
G.edge['vmware_app']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('vold','adbd')
G.edge['vold']['adbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('vold','binderservicedomain')
G.edge['vold']['binderservicedomain']['write-read'] = '[open open]'
G.add_edge('vold','bugreport')
G.edge['vold']['bugreport']['write-read'] = '[open open]'
G.add_edge('vold','dumpstate')
G.edge['vold']['dumpstate']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('vold','dumpsys')
G.edge['vold']['dumpsys']['write-read'] = '[open open]'
G.add_edge('vold','imscm')
G.edge['vold']['imscm']['write-read'] = '[open open]'
G.add_edge('vold','logwrapper')
G.edge['vold']['logwrapper']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('vold','mediaserver')
G.edge['vold']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('vold','netd')
G.edge['vold']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open]'
G.add_edge('vold','ppp')
G.edge['vold']['ppp']['write-read'] = '[open open]'
G.add_edge('vold','pppoewrapper')
G.edge['vold']['pppoewrapper']['write-read'] = '[open open]'
G.add_edge('vold','samsung_app')
G.edge['vold']['samsung_app']['write-read'] = '[setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('vold','shell')
G.edge['vold']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('vold','system_server')
G.edge['vold']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('vold','untrusteddomain')
G.edge['vold']['untrusteddomain']['write-read'] = '[open open]'
G.add_edge('vold','vold')
G.edge['vold']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][relabelto relabelfrom][relabelto relabelfrom][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('vold','ppp')
G.edge['vold']['ppp']['write-read'] = '[open open][setattr getattr]'
G.add_edge('vold','pppoewrapper')
G.edge['vold']['pppoewrapper']['write-read'] = '[open open][setattr getattr]'
G.add_edge('vold','adbd')
G.edge['vold']['adbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['vold']['adbd']['fill'] = 'red'
G.add_edge('vold','adbd')
G.edge['vold']['adbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('vold','appdomain')
G.edge['vold']['appdomain']['write-read'] = '[write read]'
G.edge['vold']['appdomain']['fill'] = 'red'
G.add_edge('vold','binderservicedomain')
G.edge['vold']['binderservicedomain']['write-read'] = '[open open][write read]'
G.edge['vold']['binderservicedomain']['fill'] = 'red'
G.add_edge('vold','binderservicedomain')
G.edge['vold']['binderservicedomain']['write-read'] = '[open open][write read][append read]'
G.add_edge('vold','bluetooth')
G.edge['vold']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read]'
G.edge['vold']['bluetooth']['fill'] = 'red'
G.add_edge('vold','bugreport')
G.edge['vold']['bugreport']['write-read'] = '[open open][write read]'
G.edge['vold']['bugreport']['fill'] = 'red'
G.add_edge('vold','bugreport')
G.edge['vold']['bugreport']['write-read'] = '[open open][write read][append read]'
G.add_edge('vold','dumpstate')
G.edge['vold']['dumpstate']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['vold']['dumpstate']['fill'] = 'red'
G.add_edge('vold','dumpstate')
G.edge['vold']['dumpstate']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('vold','dumpsys')
G.edge['vold']['dumpsys']['write-read'] = '[open open][write read]'
G.edge['vold']['dumpsys']['fill'] = 'red'
G.add_edge('vold','dumpsys')
G.edge['vold']['dumpsys']['write-read'] = '[open open][write read][append read]'
G.add_edge('vold','imscm')
G.edge['vold']['imscm']['write-read'] = '[open open][write read]'
G.edge['vold']['imscm']['fill'] = 'red'
G.add_edge('vold','imscm')
G.edge['vold']['imscm']['write-read'] = '[open open][write read][append read]'
G.add_edge('vold','irsc_util')
G.edge['vold']['irsc_util']['write-read'] = '[write read]'
G.edge['vold']['irsc_util']['fill'] = 'red'
G.add_edge('vold','logwrapper')
G.edge['vold']['logwrapper']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['vold']['logwrapper']['fill'] = 'red'
G.add_edge('vold','logwrapper')
G.edge['vold']['logwrapper']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('vold','mediaserver')
G.edge['vold']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][write read]'
G.edge['vold']['mediaserver']['fill'] = 'red'
G.add_edge('vold','mediaserver')
G.edge['vold']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][write read][append read]'
G.add_edge('vold','netd')
G.edge['vold']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read]'
G.edge['vold']['netd']['fill'] = 'red'
G.add_edge('vold','netd')
G.edge['vold']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('vold','newAttr49')
G.edge['vold']['newAttr49']['write-read'] = '[write read]'
G.edge['vold']['newAttr49']['fill'] = 'red'
G.add_edge('vold','newAttr9')
G.edge['vold']['newAttr9']['write-read'] = '[write read]'
G.edge['vold']['newAttr9']['fill'] = 'red'
G.add_edge('vold','radio')
G.edge['vold']['radio']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['vold']['radio']['fill'] = 'red'
G.add_edge('vold','runas')
G.edge['vold']['runas']['write-read'] = '[write read]'
G.edge['vold']['runas']['fill'] = 'red'
G.add_edge('vold','samsung_app')
G.edge['vold']['samsung_app']['write-read'] = '[setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['vold']['samsung_app']['fill'] = 'red'
G.add_edge('vold','samsung_app')
G.edge['vold']['samsung_app']['write-read'] = '[setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('vold','shell')
G.edge['vold']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['vold']['shell']['fill'] = 'red'
G.add_edge('vold','shell')
G.edge['vold']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('vold','surfaceflinger')
G.edge['vold']['surfaceflinger']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read]'
G.edge['vold']['surfaceflinger']['fill'] = 'red'
G.add_edge('vold','system_server')
G.edge['vold']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['vold']['system_server']['fill'] = 'red'
G.add_edge('vold','system_server')
G.edge['vold']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('vold','untrusteddomain')
G.edge['vold']['untrusteddomain']['write-read'] = '[open open][write read]'
G.edge['vold']['untrusteddomain']['fill'] = 'red'
G.add_edge('vold','untrusteddomain')
G.edge['vold']['untrusteddomain']['write-read'] = '[open open][write read][append read]'
G.add_edge('vold','vold')
G.edge['vold']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][relabelto relabelfrom][relabelto relabelfrom][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['vold']['vold']['fill'] = 'red'
G.add_edge('vold','vold')
G.edge['vold']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][relabelto relabelfrom][relabelto relabelfrom][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][write read][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
app = Viewer(G)
app.mainloop()