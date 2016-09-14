import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('charon','ATFWD-daemon')
G.edge['charon']['ATFWD-daemon']['write-read'] = '[open open]'
G.add_edge('charon','auditd')
G.edge['charon']['auditd']['write-read'] = '[add_name search][open open]'
G.add_edge('charon','cbd')
G.edge['charon']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('charon','charon')
G.edge['charon']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('charon','connfwexe')
G.edge['charon']['connfwexe']['write-read'] = '[open open]'
G.add_edge('charon','imsqmidaemon')
G.edge['charon']['imsqmidaemon']['write-read'] = '[open open]'
G.add_edge('charon','init_shell')
G.edge['charon']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open]'
G.add_edge('charon','installd')
G.edge['charon']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('charon','keystore')
G.edge['charon']['keystore']['write-read'] = '[open open]'
G.add_edge('charon','ks')
G.edge['charon']['ks']['write-read'] = '[open open]'
G.add_edge('charon','mobexdaemon')
G.edge['charon']['mobexdaemon']['write-read'] = '[open open]'
G.add_edge('charon','netmgrd')
G.edge['charon']['netmgrd']['write-read'] = '[open open][write read][append read][write read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('charon','nfc')
G.edge['charon']['nfc']['write-read'] = '[open open]'
G.add_edge('charon','qcks')
G.edge['charon']['qcks']['write-read'] = '[open open]'
G.add_edge('charon','qmiproxy')
G.edge['charon']['qmiproxy']['write-read'] = '[open open]'
G.add_edge('charon','qseecomd')
G.edge['charon']['qseecomd']['write-read'] = '[open open]'
G.add_edge('charon','usb_uicc_daemon')
G.edge['charon']['usb_uicc_daemon']['write-read'] = '[open open]'
G.add_edge('charon','wpa')
G.edge['charon']['wpa']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read][open open]'
G.add_edge('charon','adbd')
G.edge['charon']['adbd']['write-read'] = '[write read][add_name search][write read]'
G.edge['charon']['adbd']['fill'] = 'red'
G.add_edge('charon','at_distributor')
G.edge['charon']['at_distributor']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read]'
G.edge['charon']['at_distributor']['fill'] = 'red'
G.add_edge('charon','ATFWD-daemon')
G.edge['charon']['ATFWD-daemon']['write-read'] = '[open open][write read]'
G.edge['charon']['ATFWD-daemon']['fill'] = 'red'
G.add_edge('charon','ATFWD-daemon')
G.edge['charon']['ATFWD-daemon']['write-read'] = '[open open][write read][append read]'
G.add_edge('charon','atfwd')
G.edge['charon']['atfwd']['write-read'] = '[write read]'
G.edge['charon']['atfwd']['fill'] = 'red'
G.add_edge('charon','audiod')
G.edge['charon']['audiod']['write-read'] = '[write read]'
G.edge['charon']['audiod']['fill'] = 'red'
G.add_edge('charon','auditd')
G.edge['charon']['auditd']['write-read'] = '[add_name search][open open][write read]'
G.edge['charon']['auditd']['fill'] = 'red'
G.add_edge('charon','auditd')
G.edge['charon']['auditd']['write-read'] = '[add_name search][open open][write read][append read]'
G.add_edge('charon','bluetooth')
G.edge['charon']['bluetooth']['write-read'] = '[open open][open open][write read][append read][write read][append read][write read]'
G.edge['charon']['bluetooth']['fill'] = 'red'
G.add_edge('charon','bootanim')
G.edge['charon']['bootanim']['write-read'] = '[write read]'
G.edge['charon']['bootanim']['fill'] = 'red'
G.add_edge('charon','bootchecker')
G.edge['charon']['bootchecker']['write-read'] = '[write read]'
G.edge['charon']['bootchecker']['fill'] = 'red'
G.add_edge('charon','bugreport')
G.edge['charon']['bugreport']['write-read'] = '[write read]'
G.edge['charon']['bugreport']['fill'] = 'red'
G.add_edge('charon','cbd')
G.edge['charon']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['charon']['cbd']['fill'] = 'red'
G.add_edge('charon','cbd')
G.edge['charon']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('charon','charon')
G.edge['charon']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['charon']['charon']['fill'] = 'red'
G.add_edge('charon','charon')
G.edge['charon']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('charon','cnd')
G.edge['charon']['cnd']['write-read'] = '[write read]'
G.edge['charon']['cnd']['fill'] = 'red'
G.add_edge('charon','connfwexe')
G.edge['charon']['connfwexe']['write-read'] = '[open open][write read]'
G.edge['charon']['connfwexe']['fill'] = 'red'
G.add_edge('charon','connfwexe')
G.edge['charon']['connfwexe']['write-read'] = '[open open][write read][append read]'
G.add_edge('charon','debug_interface_proxy')
G.edge['charon']['debug_interface_proxy']['write-read'] = '[write read]'
G.edge['charon']['debug_interface_proxy']['fill'] = 'red'
G.add_edge('charon','dhcp')
G.edge['charon']['dhcp']['write-read'] = '[write read][add_name search][write read][write read]'
G.edge['charon']['dhcp']['fill'] = 'red'
G.add_edge('charon','diagexe')
G.edge['charon']['diagexe']['write-read'] = '[write read]'
G.edge['charon']['diagexe']['fill'] = 'red'
G.add_edge('charon','dpmd')
G.edge['charon']['dpmd']['write-read'] = '[write read]'
G.edge['charon']['dpmd']['fill'] = 'red'
G.add_edge('charon','drsd')
G.edge['charon']['drsd']['write-read'] = '[write read]'
G.edge['charon']['drsd']['fill'] = 'red'
G.add_edge('charon','dumpstate')
G.edge['charon']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['charon']['dumpstate']['fill'] = 'red'
G.add_edge('charon','epmd')
G.edge['charon']['epmd']['write-read'] = '[write read]'
G.edge['charon']['epmd']['fill'] = 'red'
G.add_edge('charon','fidodaemon')
G.edge['charon']['fidodaemon']['write-read'] = '[write read]'
G.edge['charon']['fidodaemon']['fill'] = 'red'
G.add_edge('charon','geomagneticd')
G.edge['charon']['geomagneticd']['write-read'] = '[write read]'
G.edge['charon']['geomagneticd']['fill'] = 'red'
G.add_edge('charon','gpsd')
G.edge['charon']['gpsd']['write-read'] = '[write read]'
G.edge['charon']['gpsd']['fill'] = 'red'
G.add_edge('charon','healthd')
G.edge['charon']['healthd']['write-read'] = '[write read]'
G.edge['charon']['healthd']['fill'] = 'red'
G.add_edge('charon','ime_app')
G.edge['charon']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][write read]'
G.edge['charon']['ime_app']['fill'] = 'red'
G.add_edge('charon','ims')
G.edge['charon']['ims']['write-read'] = '[write read]'
G.edge['charon']['ims']['fill'] = 'red'
G.add_edge('charon','imsqmidaemon')
G.edge['charon']['imsqmidaemon']['write-read'] = '[open open][write read]'
G.edge['charon']['imsqmidaemon']['fill'] = 'red'
G.add_edge('charon','imsqmidaemon')
G.edge['charon']['imsqmidaemon']['write-read'] = '[open open][write read][append read]'
G.add_edge('charon','init_shell')
G.edge['charon']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read]'
G.edge['charon']['init_shell']['fill'] = 'red'
G.add_edge('charon','init_shell')
G.edge['charon']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read]'
G.add_edge('charon','init_shell')
G.edge['charon']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][write read]'
G.edge['charon']['init_shell']['fill'] = 'red'
G.add_edge('charon','installd')
G.edge['charon']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['charon']['installd']['fill'] = 'red'
G.add_edge('charon','installd')
G.edge['charon']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('charon','installd')
G.edge['charon']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read]'
G.edge['charon']['installd']['fill'] = 'red'
G.add_edge('charon','keystore')
G.edge['charon']['keystore']['write-read'] = '[open open][write read]'
G.edge['charon']['keystore']['fill'] = 'red'
G.add_edge('charon','keystore')
G.edge['charon']['keystore']['write-read'] = '[open open][write read][append read]'
G.add_edge('charon','kiesexe')
G.edge['charon']['kiesexe']['write-read'] = '[write read]'
G.edge['charon']['kiesexe']['fill'] = 'red'
G.add_edge('charon','ks')
G.edge['charon']['ks']['write-read'] = '[open open][write read]'
G.edge['charon']['ks']['fill'] = 'red'
G.add_edge('charon','ks')
G.edge['charon']['ks']['write-read'] = '[open open][write read][append read]'
G.add_edge('charon','ks')
G.edge['charon']['ks']['write-read'] = '[open open][write read][append read][write read]'
G.edge['charon']['ks']['fill'] = 'red'
G.add_edge('charon','launcher')
G.edge['charon']['launcher']['write-read'] = '[write read]'
G.edge['charon']['launcher']['fill'] = 'red'
G.add_edge('charon','mediaserver')
G.edge['charon']['mediaserver']['write-read'] = '[write read]'
G.edge['charon']['mediaserver']['fill'] = 'red'
G.add_edge('charon','mfgloader')
G.edge['charon']['mfgloader']['write-read'] = '[write read]'
G.edge['charon']['mfgloader']['fill'] = 'red'
G.add_edge('charon','mmi')
G.edge['charon']['mmi']['write-read'] = '[write read]'
G.edge['charon']['mmi']['fill'] = 'red'
G.add_edge('charon','mm-pp-daemon')
G.edge['charon']['mm-pp-daemon']['write-read'] = '[write read]'
G.edge['charon']['mm-pp-daemon']['fill'] = 'red'
G.add_edge('charon','mobexdaemon')
G.edge['charon']['mobexdaemon']['write-read'] = '[open open][write read]'
G.edge['charon']['mobexdaemon']['fill'] = 'red'
G.add_edge('charon','mobexdaemon')
G.edge['charon']['mobexdaemon']['write-read'] = '[open open][write read][append read]'
G.add_edge('charon','mobicoredaemon')
G.edge['charon']['mobicoredaemon']['write-read'] = '[write read]'
G.edge['charon']['mobicoredaemon']['fill'] = 'red'
G.add_edge('charon','netd')
G.edge['charon']['netd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read][append read][open open][write read][append read][write read]'
G.edge['charon']['netd']['fill'] = 'red'
G.add_edge('charon','netmgrd')
G.edge['charon']['netmgrd']['write-read'] = '[open open][write read][append read][write read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['charon']['netmgrd']['fill'] = 'red'
G.add_edge('charon','netmgrd')
G.edge['charon']['netmgrd']['write-read'] = '[open open][write read][append read][write read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('charon','netmgrd')
G.edge['charon']['netmgrd']['write-read'] = '[open open][write read][append read][write read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read][write read]'
G.edge['charon']['netmgrd']['fill'] = 'red'
G.add_edge('charon','nfc')
G.edge['charon']['nfc']['write-read'] = '[open open][write read]'
G.edge['charon']['nfc']['fill'] = 'red'
G.add_edge('charon','nfc')
G.edge['charon']['nfc']['write-read'] = '[open open][write read][append read]'
G.add_edge('charon','nfc')
G.edge['charon']['nfc']['write-read'] = '[open open][write read][append read][write read]'
G.edge['charon']['nfc']['fill'] = 'red'
G.add_edge('charon','pppoewrapper')
G.edge['charon']['pppoewrapper']['write-read'] = '[write read][write read]'
G.edge['charon']['pppoewrapper']['fill'] = 'red'
G.add_edge('charon','ppp')
G.edge['charon']['ppp']['write-read'] = '[write read][write read]'
G.edge['charon']['ppp']['fill'] = 'red'
G.add_edge('charon','qcks')
G.edge['charon']['qcks']['write-read'] = '[open open][write read]'
G.edge['charon']['qcks']['fill'] = 'red'
G.add_edge('charon','qcks')
G.edge['charon']['qcks']['write-read'] = '[open open][write read][append read]'
G.add_edge('charon','qcks')
G.edge['charon']['qcks']['write-read'] = '[open open][write read][append read][write read]'
G.edge['charon']['qcks']['fill'] = 'red'
G.add_edge('charon','qmiproxy')
G.edge['charon']['qmiproxy']['write-read'] = '[open open][write read]'
G.edge['charon']['qmiproxy']['fill'] = 'red'
G.add_edge('charon','qmiproxy')
G.edge['charon']['qmiproxy']['write-read'] = '[open open][write read][append read]'
G.add_edge('charon','qmuxd')
G.edge['charon']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['charon']['qmuxd']['fill'] = 'red'
G.add_edge('charon','qseecomd')
G.edge['charon']['qseecomd']['write-read'] = '[open open][write read]'
G.edge['charon']['qseecomd']['fill'] = 'red'
G.add_edge('charon','qseecomd')
G.edge['charon']['qseecomd']['write-read'] = '[open open][write read][append read]'
G.add_edge('charon','radio')
G.edge['charon']['radio']['write-read'] = '[write read]'
G.edge['charon']['radio']['fill'] = 'red'
G.add_edge('charon','rild')
G.edge['charon']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][write read]'
G.edge['charon']['rild']['fill'] = 'red'
G.add_edge('charon','rmt_storage')
G.edge['charon']['rmt_storage']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['charon']['rmt_storage']['fill'] = 'red'
G.add_edge('charon','samsungpowersoundplay')
G.edge['charon']['samsungpowersoundplay']['write-read'] = '[write read]'
G.edge['charon']['samsungpowersoundplay']['fill'] = 'red'
G.add_edge('charon','scs')
G.edge['charon']['scs']['write-read'] = '[write read]'
G.edge['charon']['scs']['fill'] = 'red'
G.add_edge('charon','sec-ril')
G.edge['charon']['sec-ril']['write-read'] = '[write read]'
G.edge['charon']['sec-ril']['fill'] = 'red'
G.add_edge('charon','secstarter')
G.edge['charon']['secstarter']['write-read'] = '[write read]'
G.edge['charon']['secstarter']['fill'] = 'red'
G.add_edge('charon','selinux_net')
G.edge['charon']['selinux_net']['write-read'] = '[write read]'
G.edge['charon']['selinux_net']['fill'] = 'red'
G.add_edge('charon','sem')
G.edge['charon']['sem']['write-read'] = '[write read]'
G.edge['charon']['sem']['fill'] = 'red'
G.add_edge('charon','servicemanager')
G.edge['charon']['servicemanager']['write-read'] = '[write read]'
G.edge['charon']['servicemanager']['fill'] = 'red'
G.add_edge('charon','shell')
G.edge['charon']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][write read]'
G.edge['charon']['shell']['fill'] = 'red'
G.add_edge('charon','s_platform_app')
G.edge['charon']['s_platform_app']['write-read'] = '[write read]'
G.edge['charon']['s_platform_app']['fill'] = 'red'
G.add_edge('charon','s_system_app')
G.edge['charon']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read][open open][write read][append read][write read]'
G.edge['charon']['s_system_app']['fill'] = 'red'
G.add_edge('charon','surfaceflinger')
G.edge['charon']['surfaceflinger']['write-read'] = '[write read]'
G.edge['charon']['surfaceflinger']['fill'] = 'red'
G.add_edge('charon','syscope_app')
G.edge['charon']['syscope_app']['write-read'] = '[write read]'
G.edge['charon']['syscope_app']['fill'] = 'red'
G.add_edge('charon','system_app')
G.edge['charon']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read][open open][write read][append read][write read]'
G.edge['charon']['system_app']['fill'] = 'red'
G.add_edge('charon','system_domain')
G.edge['charon']['system_domain']['write-read'] = '[write read]'
G.edge['charon']['system_domain']['fill'] = 'red'
G.add_edge('charon','system_server')
G.edge['charon']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][write read]'
G.edge['charon']['system_server']['fill'] = 'red'
G.add_edge('charon','tee')
G.edge['charon']['tee']['write-read'] = '[write read]'
G.edge['charon']['tee']['fill'] = 'red'
G.add_edge('charon','thermald')
G.edge['charon']['thermald']['write-read'] = '[write read]'
G.edge['charon']['thermald']['fill'] = 'red'
G.add_edge('charon','tzdaemon')
G.edge['charon']['tzdaemon']['write-read'] = '[write read]'
G.edge['charon']['tzdaemon']['fill'] = 'red'
G.add_edge('charon','ueventd')
G.edge['charon']['ueventd']['write-read'] = '[write read]'
G.edge['charon']['ueventd']['fill'] = 'red'
G.add_edge('charon','uncrypt')
G.edge['charon']['uncrypt']['write-read'] = '[write read]'
G.edge['charon']['uncrypt']['fill'] = 'red'
G.add_edge('charon','usb_uicc_daemon')
G.edge['charon']['usb_uicc_daemon']['write-read'] = '[open open][write read]'
G.edge['charon']['usb_uicc_daemon']['fill'] = 'red'
G.add_edge('charon','usb_uicc_daemon')
G.edge['charon']['usb_uicc_daemon']['write-read'] = '[open open][write read][append read]'
G.add_edge('charon','usf')
G.edge['charon']['usf']['write-read'] = '[write read]'
G.edge['charon']['usf']['fill'] = 'red'
G.add_edge('charon','vcsFPService')
G.edge['charon']['vcsFPService']['write-read'] = '[write read]'
G.edge['charon']['vcsFPService']['fill'] = 'red'
G.add_edge('charon','vmwared')
G.edge['charon']['vmwared']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read]'
G.edge['charon']['vmwared']['fill'] = 'red'
G.add_edge('charon','vold')
G.edge['charon']['vold']['write-read'] = '[write read]'
G.edge['charon']['vold']['fill'] = 'red'
G.add_edge('charon','wcnss_service')
G.edge['charon']['wcnss_service']['write-read'] = '[write read][write read]'
G.edge['charon']['wcnss_service']['fill'] = 'red'
G.add_edge('charon','wfdservice')
G.edge['charon']['wfdservice']['write-read'] = '[write read]'
G.edge['charon']['wfdservice']['fill'] = 'red'
G.add_edge('charon','wpa')
G.edge['charon']['wpa']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read]'
G.edge['charon']['wpa']['fill'] = 'red'
G.add_edge('charon','wpa')
G.edge['charon']['wpa']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read][append read]'
G.add_edge('charon','zygote')
G.edge['charon']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read][write read]'
G.edge['charon']['zygote']['fill'] = 'red'
G.add_edge('keystore','ATFWD-daemon')
G.edge['keystore']['ATFWD-daemon']['write-read'] = '[open open]'
G.add_edge('keystore','auditd')
G.edge['keystore']['auditd']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('keystore','cbd')
G.edge['keystore']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('keystore','charon')
G.edge['keystore']['charon']['write-read'] = '[open open]'
G.add_edge('keystore','connfwexe')
G.edge['keystore']['connfwexe']['write-read'] = '[open open]'
G.add_edge('keystore','imsqmidaemon')
G.edge['keystore']['imsqmidaemon']['write-read'] = '[open open]'
G.add_edge('keystore','init_shell')
G.edge['keystore']['init_shell']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('keystore','installd')
G.edge['keystore']['installd']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('keystore','keystore')
G.edge['keystore']['keystore']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('keystore','ks')
G.edge['keystore']['ks']['write-read'] = '[open open][write read][add_name search][open open]'
G.add_edge('keystore','mobexdaemon')
G.edge['keystore']['mobexdaemon']['write-read'] = '[open open]'
G.add_edge('keystore','netmgrd')
G.edge['keystore']['netmgrd']['write-read'] = '[open open]'
G.add_edge('keystore','nfc')
G.edge['keystore']['nfc']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('keystore','qcks')
G.edge['keystore']['qcks']['write-read'] = '[open open]'
G.add_edge('keystore','qmiproxy')
G.edge['keystore']['qmiproxy']['write-read'] = '[open open]'
G.add_edge('keystore','qseecomd')
G.edge['keystore']['qseecomd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open]'
G.add_edge('keystore','usb_uicc_daemon')
G.edge['keystore']['usb_uicc_daemon']['write-read'] = '[open open]'
G.add_edge('keystore','wpa')
G.edge['keystore']['wpa']['write-read'] = '[open open]'
G.add_edge('keystore','adbd')
G.edge['keystore']['adbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['keystore']['adbd']['fill'] = 'red'
G.add_edge('keystore','at_distributor')
G.edge['keystore']['at_distributor']['write-read'] = '[write read]'
G.edge['keystore']['at_distributor']['fill'] = 'red'
G.add_edge('keystore','ATFWD-daemon')
G.edge['keystore']['ATFWD-daemon']['write-read'] = '[open open][write read]'
G.edge['keystore']['ATFWD-daemon']['fill'] = 'red'
G.add_edge('keystore','ATFWD-daemon')
G.edge['keystore']['ATFWD-daemon']['write-read'] = '[open open][write read][append read]'
G.add_edge('keystore','atfwd')
G.edge['keystore']['atfwd']['write-read'] = '[write read]'
G.edge['keystore']['atfwd']['fill'] = 'red'
G.add_edge('keystore','audiod')
G.edge['keystore']['audiod']['write-read'] = '[write read]'
G.edge['keystore']['audiod']['fill'] = 'red'
G.add_edge('keystore','auditd')
G.edge['keystore']['auditd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read]'
G.edge['keystore']['auditd']['fill'] = 'red'
G.add_edge('keystore','auditd')
G.edge['keystore']['auditd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('keystore','bluetooth')
G.edge['keystore']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['keystore']['bluetooth']['fill'] = 'red'
G.add_edge('keystore','bootanim')
G.edge['keystore']['bootanim']['write-read'] = '[write read]'
G.edge['keystore']['bootanim']['fill'] = 'red'
G.add_edge('keystore','bootchecker')
G.edge['keystore']['bootchecker']['write-read'] = '[write read]'
G.edge['keystore']['bootchecker']['fill'] = 'red'
G.add_edge('keystore','bugreport')
G.edge['keystore']['bugreport']['write-read'] = '[write read]'
G.edge['keystore']['bugreport']['fill'] = 'red'
G.add_edge('keystore','cbd')
G.edge['keystore']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['keystore']['cbd']['fill'] = 'red'
G.add_edge('keystore','cbd')
G.edge['keystore']['cbd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('keystore','charon')
G.edge['keystore']['charon']['write-read'] = '[open open][write read]'
G.edge['keystore']['charon']['fill'] = 'red'
G.add_edge('keystore','charon')
G.edge['keystore']['charon']['write-read'] = '[open open][write read][append read]'
G.add_edge('keystore','cnd')
G.edge['keystore']['cnd']['write-read'] = '[write read]'
G.edge['keystore']['cnd']['fill'] = 'red'
G.add_edge('keystore','connfwexe')
G.edge['keystore']['connfwexe']['write-read'] = '[open open][write read]'
G.edge['keystore']['connfwexe']['fill'] = 'red'
G.add_edge('keystore','connfwexe')
G.edge['keystore']['connfwexe']['write-read'] = '[open open][write read][append read]'
G.add_edge('keystore','debug_interface_proxy')
G.edge['keystore']['debug_interface_proxy']['write-read'] = '[write read]'
G.edge['keystore']['debug_interface_proxy']['fill'] = 'red'
G.add_edge('keystore','dhcp')
G.edge['keystore']['dhcp']['write-read'] = '[write read]'
G.edge['keystore']['dhcp']['fill'] = 'red'
G.add_edge('keystore','diagexe')
G.edge['keystore']['diagexe']['write-read'] = '[write read]'
G.edge['keystore']['diagexe']['fill'] = 'red'
G.add_edge('keystore','dpmd')
G.edge['keystore']['dpmd']['write-read'] = '[write read]'
G.edge['keystore']['dpmd']['fill'] = 'red'
G.add_edge('keystore','drsd')
G.edge['keystore']['drsd']['write-read'] = '[open open][setattr getattr][write read][append read][write read]'
G.edge['keystore']['drsd']['fill'] = 'red'
G.add_edge('keystore','dumpstate')
G.edge['keystore']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['keystore']['dumpstate']['fill'] = 'red'
G.add_edge('keystore','epmd')
G.edge['keystore']['epmd']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][write read]'
G.edge['keystore']['epmd']['fill'] = 'red'
G.add_edge('keystore','fidodaemon')
G.edge['keystore']['fidodaemon']['write-read'] = '[open open][write read][append read][write read]'
G.edge['keystore']['fidodaemon']['fill'] = 'red'
G.add_edge('keystore','geomagneticd')
G.edge['keystore']['geomagneticd']['write-read'] = '[write read]'
G.edge['keystore']['geomagneticd']['fill'] = 'red'
G.add_edge('keystore','gpsd')
G.edge['keystore']['gpsd']['write-read'] = '[write read]'
G.edge['keystore']['gpsd']['fill'] = 'red'
G.add_edge('keystore','healthd')
G.edge['keystore']['healthd']['write-read'] = '[write read]'
G.edge['keystore']['healthd']['fill'] = 'red'
G.add_edge('keystore','ime_app')
G.edge['keystore']['ime_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read]'
G.edge['keystore']['ime_app']['fill'] = 'red'
G.add_edge('keystore','ims')
G.edge['keystore']['ims']['write-read'] = '[write read]'
G.edge['keystore']['ims']['fill'] = 'red'
G.add_edge('keystore','imsqmidaemon')
G.edge['keystore']['imsqmidaemon']['write-read'] = '[open open][write read]'
G.edge['keystore']['imsqmidaemon']['fill'] = 'red'
G.add_edge('keystore','imsqmidaemon')
G.edge['keystore']['imsqmidaemon']['write-read'] = '[open open][write read][append read]'
G.add_edge('keystore','init_shell')
G.edge['keystore']['init_shell']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['keystore']['init_shell']['fill'] = 'red'
G.add_edge('keystore','init_shell')
G.edge['keystore']['init_shell']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('keystore','init_shell')
G.edge['keystore']['init_shell']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read]'
G.edge['keystore']['init_shell']['fill'] = 'red'
G.add_edge('keystore','installd')
G.edge['keystore']['installd']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['keystore']['installd']['fill'] = 'red'
G.add_edge('keystore','installd')
G.edge['keystore']['installd']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('keystore','installd')
G.edge['keystore']['installd']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read]'
G.edge['keystore']['installd']['fill'] = 'red'
G.add_edge('keystore','keystore')
G.edge['keystore']['keystore']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['keystore']['keystore']['fill'] = 'red'
G.add_edge('keystore','keystore')
G.edge['keystore']['keystore']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('keystore','kiesexe')
G.edge['keystore']['kiesexe']['write-read'] = '[write read]'
G.edge['keystore']['kiesexe']['fill'] = 'red'
G.add_edge('keystore','ks')
G.edge['keystore']['ks']['write-read'] = '[open open][write read][add_name search][open open][write read]'
G.edge['keystore']['ks']['fill'] = 'red'
G.add_edge('keystore','ks')
G.edge['keystore']['ks']['write-read'] = '[open open][write read][add_name search][open open][write read][append read]'
G.add_edge('keystore','ks')
G.edge['keystore']['ks']['write-read'] = '[open open][write read][add_name search][open open][write read][append read][write read]'
G.edge['keystore']['ks']['fill'] = 'red'
G.add_edge('keystore','launcher')
G.edge['keystore']['launcher']['write-read'] = '[open open][write read][append read][write read]'
G.edge['keystore']['launcher']['fill'] = 'red'
G.add_edge('keystore','mediaserver')
G.edge['keystore']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read]'
G.edge['keystore']['mediaserver']['fill'] = 'red'
G.add_edge('keystore','mfgloader')
G.edge['keystore']['mfgloader']['write-read'] = '[write read]'
G.edge['keystore']['mfgloader']['fill'] = 'red'
G.add_edge('keystore','mmi')
G.edge['keystore']['mmi']['write-read'] = '[write read]'
G.edge['keystore']['mmi']['fill'] = 'red'
G.add_edge('keystore','mm-pp-daemon')
G.edge['keystore']['mm-pp-daemon']['write-read'] = '[write read]'
G.edge['keystore']['mm-pp-daemon']['fill'] = 'red'
G.add_edge('keystore','mobexdaemon')
G.edge['keystore']['mobexdaemon']['write-read'] = '[open open][write read]'
G.edge['keystore']['mobexdaemon']['fill'] = 'red'
G.add_edge('keystore','mobexdaemon')
G.edge['keystore']['mobexdaemon']['write-read'] = '[open open][write read][append read]'
G.add_edge('keystore','mobicoredaemon')
G.edge['keystore']['mobicoredaemon']['write-read'] = '[write read]'
G.edge['keystore']['mobicoredaemon']['fill'] = 'red'
G.add_edge('keystore','netd')
G.edge['keystore']['netd']['write-read'] = '[write read]'
G.edge['keystore']['netd']['fill'] = 'red'
G.add_edge('keystore','netmgrd')
G.edge['keystore']['netmgrd']['write-read'] = '[open open][write read]'
G.edge['keystore']['netmgrd']['fill'] = 'red'
G.add_edge('keystore','netmgrd')
G.edge['keystore']['netmgrd']['write-read'] = '[open open][write read][append read]'
G.add_edge('keystore','netmgrd')
G.edge['keystore']['netmgrd']['write-read'] = '[open open][write read][append read][write read]'
G.edge['keystore']['netmgrd']['fill'] = 'red'
G.add_edge('keystore','nfc')
G.edge['keystore']['nfc']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['keystore']['nfc']['fill'] = 'red'
G.add_edge('keystore','nfc')
G.edge['keystore']['nfc']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('keystore','nfc')
G.edge['keystore']['nfc']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read]'
G.edge['keystore']['nfc']['fill'] = 'red'
G.add_edge('keystore','pppoewrapper')
G.edge['keystore']['pppoewrapper']['write-read'] = '[write read]'
G.edge['keystore']['pppoewrapper']['fill'] = 'red'
G.add_edge('keystore','ppp')
G.edge['keystore']['ppp']['write-read'] = '[write read]'
G.edge['keystore']['ppp']['fill'] = 'red'
G.add_edge('keystore','qcks')
G.edge['keystore']['qcks']['write-read'] = '[open open][write read]'
G.edge['keystore']['qcks']['fill'] = 'red'
G.add_edge('keystore','qcks')
G.edge['keystore']['qcks']['write-read'] = '[open open][write read][append read]'
G.add_edge('keystore','qcks')
G.edge['keystore']['qcks']['write-read'] = '[open open][write read][append read][write read]'
G.edge['keystore']['qcks']['fill'] = 'red'
G.add_edge('keystore','qmiproxy')
G.edge['keystore']['qmiproxy']['write-read'] = '[open open][write read]'
G.edge['keystore']['qmiproxy']['fill'] = 'red'
G.add_edge('keystore','qmiproxy')
G.edge['keystore']['qmiproxy']['write-read'] = '[open open][write read][append read]'
G.add_edge('keystore','qmuxd')
G.edge['keystore']['qmuxd']['write-read'] = '[write read]'
G.edge['keystore']['qmuxd']['fill'] = 'red'
G.add_edge('keystore','qseecomd')
G.edge['keystore']['qseecomd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['keystore']['qseecomd']['fill'] = 'red'
G.add_edge('keystore','qseecomd')
G.edge['keystore']['qseecomd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('keystore','radio')
G.edge['keystore']['radio']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['keystore']['radio']['fill'] = 'red'
G.add_edge('keystore','rild')
G.edge['keystore']['rild']['write-read'] = '[write read]'
G.edge['keystore']['rild']['fill'] = 'red'
G.add_edge('keystore','rmt_storage')
G.edge['keystore']['rmt_storage']['write-read'] = '[write read]'
G.edge['keystore']['rmt_storage']['fill'] = 'red'
G.add_edge('keystore','samsungpowersoundplay')
G.edge['keystore']['samsungpowersoundplay']['write-read'] = '[write read]'
G.edge['keystore']['samsungpowersoundplay']['fill'] = 'red'
G.add_edge('keystore','scs')
G.edge['keystore']['scs']['write-read'] = '[write read]'
G.edge['keystore']['scs']['fill'] = 'red'
G.add_edge('keystore','sec-ril')
G.edge['keystore']['sec-ril']['write-read'] = '[write read]'
G.edge['keystore']['sec-ril']['fill'] = 'red'
G.add_edge('keystore','secstarter')
G.edge['keystore']['secstarter']['write-read'] = '[write read]'
G.edge['keystore']['secstarter']['fill'] = 'red'
G.add_edge('keystore','selinux_net')
G.edge['keystore']['selinux_net']['write-read'] = '[write read]'
G.edge['keystore']['selinux_net']['fill'] = 'red'
G.add_edge('keystore','sem')
G.edge['keystore']['sem']['write-read'] = '[write read]'
G.edge['keystore']['sem']['fill'] = 'red'
G.add_edge('keystore','servicemanager')
G.edge['keystore']['servicemanager']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read]'
G.edge['keystore']['servicemanager']['fill'] = 'red'
G.add_edge('keystore','shell')
G.edge['keystore']['shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['keystore']['shell']['fill'] = 'red'
G.add_edge('keystore','s_platform_app')
G.edge['keystore']['s_platform_app']['write-read'] = '[write read]'
G.edge['keystore']['s_platform_app']['fill'] = 'red'
G.add_edge('keystore','s_system_app')
G.edge['keystore']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read]'
G.edge['keystore']['s_system_app']['fill'] = 'red'
G.add_edge('keystore','surfaceflinger')
G.edge['keystore']['surfaceflinger']['write-read'] = '[open open][write read][append read][write read]'
G.edge['keystore']['surfaceflinger']['fill'] = 'red'
G.add_edge('keystore','syscope_app')
G.edge['keystore']['syscope_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['keystore']['syscope_app']['fill'] = 'red'
G.add_edge('keystore','system_app')
G.edge['keystore']['system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read]'
G.edge['keystore']['system_app']['fill'] = 'red'
G.add_edge('keystore','system_domain')
G.edge['keystore']['system_domain']['write-read'] = '[write read]'
G.edge['keystore']['system_domain']['fill'] = 'red'
G.add_edge('keystore','system_server')
G.edge['keystore']['system_server']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][write read]'
G.edge['keystore']['system_server']['fill'] = 'red'
G.add_edge('keystore','tee')
G.edge['keystore']['tee']['write-read'] = '[open open][write read][append read][write read]'
G.edge['keystore']['tee']['fill'] = 'red'
G.add_edge('keystore','thermald')
G.edge['keystore']['thermald']['write-read'] = '[write read]'
G.edge['keystore']['thermald']['fill'] = 'red'
G.add_edge('keystore','tzdaemon')
G.edge['keystore']['tzdaemon']['write-read'] = '[open open][write read][append read][write read]'
G.edge['keystore']['tzdaemon']['fill'] = 'red'
G.add_edge('keystore','ueventd')
G.edge['keystore']['ueventd']['write-read'] = '[write read]'
G.edge['keystore']['ueventd']['fill'] = 'red'
G.add_edge('keystore','uncrypt')
G.edge['keystore']['uncrypt']['write-read'] = '[write read]'
G.edge['keystore']['uncrypt']['fill'] = 'red'
G.add_edge('keystore','usb_uicc_daemon')
G.edge['keystore']['usb_uicc_daemon']['write-read'] = '[open open][write read]'
G.edge['keystore']['usb_uicc_daemon']['fill'] = 'red'
G.add_edge('keystore','usb_uicc_daemon')
G.edge['keystore']['usb_uicc_daemon']['write-read'] = '[open open][write read][append read]'
G.add_edge('keystore','usf')
G.edge['keystore']['usf']['write-read'] = '[write read]'
G.edge['keystore']['usf']['fill'] = 'red'
G.add_edge('keystore','vcsFPService')
G.edge['keystore']['vcsFPService']['write-read'] = '[write read]'
G.edge['keystore']['vcsFPService']['fill'] = 'red'
G.add_edge('keystore','vmwared')
G.edge['keystore']['vmwared']['write-read'] = '[write read]'
G.edge['keystore']['vmwared']['fill'] = 'red'
G.add_edge('keystore','vold')
G.edge['keystore']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read]'
G.edge['keystore']['vold']['fill'] = 'red'
G.add_edge('keystore','wcnss_service')
G.edge['keystore']['wcnss_service']['write-read'] = '[write read]'
G.edge['keystore']['wcnss_service']['fill'] = 'red'
G.add_edge('keystore','wfdservice')
G.edge['keystore']['wfdservice']['write-read'] = '[open open][write read][append read][write read]'
G.edge['keystore']['wfdservice']['fill'] = 'red'
G.add_edge('keystore','wpa')
G.edge['keystore']['wpa']['write-read'] = '[open open][write read]'
G.edge['keystore']['wpa']['fill'] = 'red'
G.add_edge('keystore','wpa')
G.edge['keystore']['wpa']['write-read'] = '[open open][write read][append read]'
G.add_edge('keystore','zygote')
G.edge['keystore']['zygote']['write-read'] = '[open open][write read][append read][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][open open][write read][append read][write read]'
G.edge['keystore']['zygote']['fill'] = 'red'
app = Viewer(G)
app.mainloop()