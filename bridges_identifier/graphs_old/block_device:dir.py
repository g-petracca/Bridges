import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('actlmand','efsks')
G.edge['actlmand']['efsks']['write-read'] = '[open open]'
G.add_edge('actlmand','flash_recovery')
G.edge['actlmand']['flash_recovery']['write-read'] = '[open open]'
G.add_edge('actlmand','init_shell')
G.edge['actlmand']['init_shell']['write-read'] = '[open open]'
G.add_edge('actlmand','ks')
G.edge['actlmand']['ks']['write-read'] = '[open open]'
G.add_edge('actlmand','prepare_param')
G.edge['actlmand']['prepare_param']['write-read'] = '[open open]'
G.add_edge('actlmand','qseecomd')
G.edge['actlmand']['qseecomd']['write-read'] = '[open open]'
G.add_edge('actlmand','vold')
G.edge['actlmand']['vold']['write-read'] = '[open open]'
G.add_edge('actlmand','prepare_param')
G.edge['actlmand']['prepare_param']['write-read'] = '[open open][setattr getattr]'
G.add_edge('actlmand','vold')
G.edge['actlmand']['vold']['write-read'] = '[open open][setattr getattr]'
G.add_edge('actlmand','efsks')
G.edge['actlmand']['efsks']['write-read'] = '[open open][write read]'
G.edge['actlmand']['efsks']['fill'] = 'red'
G.add_edge('actlmand','flash_recovery')
G.edge['actlmand']['flash_recovery']['write-read'] = '[open open][write read]'
G.edge['actlmand']['flash_recovery']['fill'] = 'red'
G.add_edge('actlmand','init_shell')
G.edge['actlmand']['init_shell']['write-read'] = '[open open][write read]'
G.edge['actlmand']['init_shell']['fill'] = 'red'
G.add_edge('actlmand','ks')
G.edge['actlmand']['ks']['write-read'] = '[open open][write read]'
G.edge['actlmand']['ks']['fill'] = 'red'
G.add_edge('actlmand','mdm_helper')
G.edge['actlmand']['mdm_helper']['write-read'] = '[write read]'
G.edge['actlmand']['mdm_helper']['fill'] = 'red'
G.add_edge('actlmand','prepare_param')
G.edge['actlmand']['prepare_param']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['actlmand']['prepare_param']['fill'] = 'red'
G.add_edge('actlmand','qseecomd')
G.edge['actlmand']['qseecomd']['write-read'] = '[open open][write read]'
G.edge['actlmand']['qseecomd']['fill'] = 'red'
G.add_edge('actlmand','vold')
G.edge['actlmand']['vold']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['actlmand']['vold']['fill'] = 'red'
G.add_edge('actlmand','efsks')
G.edge['actlmand']['efsks']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('actlmand','flash_recovery')
G.edge['actlmand']['flash_recovery']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('actlmand','flash_recovery')
G.edge['actlmand']['flash_recovery']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('actlmand','init_shell')
G.edge['actlmand']['init_shell']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('actlmand','init_shell')
G.edge['actlmand']['init_shell']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('actlmand','ks')
G.edge['actlmand']['ks']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('actlmand','prepare_param')
G.edge['actlmand']['prepare_param']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('actlmand','prepare_param')
G.edge['actlmand']['prepare_param']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('actlmand','qseecomd')
G.edge['actlmand']['qseecomd']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('actlmand','qseecomd')
G.edge['actlmand']['qseecomd']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('actlmand','vold')
G.edge['actlmand']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('actlmand','vold')
G.edge['actlmand']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('at_distributor','efsks')
G.edge['at_distributor']['efsks']['write-read'] = '[open open]'
G.add_edge('at_distributor','flash_recovery')
G.edge['at_distributor']['flash_recovery']['write-read'] = '[open open]'
G.add_edge('at_distributor','init_shell')
G.edge['at_distributor']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('at_distributor','ks')
G.edge['at_distributor']['ks']['write-read'] = '[open open]'
G.add_edge('at_distributor','prepare_param')
G.edge['at_distributor']['prepare_param']['write-read'] = '[open open]'
G.add_edge('at_distributor','qseecomd')
G.edge['at_distributor']['qseecomd']['write-read'] = '[open open]'
G.add_edge('at_distributor','vold')
G.edge['at_distributor']['vold']['write-read'] = '[open open]'
G.add_edge('at_distributor','prepare_param')
G.edge['at_distributor']['prepare_param']['write-read'] = '[open open][setattr getattr]'
G.add_edge('at_distributor','vold')
G.edge['at_distributor']['vold']['write-read'] = '[open open][setattr getattr]'
G.add_edge('at_distributor','efsks')
G.edge['at_distributor']['efsks']['write-read'] = '[open open][write read]'
G.edge['at_distributor']['efsks']['fill'] = 'red'
G.add_edge('at_distributor','flash_recovery')
G.edge['at_distributor']['flash_recovery']['write-read'] = '[open open][write read]'
G.edge['at_distributor']['flash_recovery']['fill'] = 'red'
G.add_edge('at_distributor','init_shell')
G.edge['at_distributor']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['at_distributor']['init_shell']['fill'] = 'red'
G.add_edge('at_distributor','ks')
G.edge['at_distributor']['ks']['write-read'] = '[open open][write read]'
G.edge['at_distributor']['ks']['fill'] = 'red'
G.add_edge('at_distributor','mdm_helper')
G.edge['at_distributor']['mdm_helper']['write-read'] = '[write read]'
G.edge['at_distributor']['mdm_helper']['fill'] = 'red'
G.add_edge('at_distributor','prepare_param')
G.edge['at_distributor']['prepare_param']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['at_distributor']['prepare_param']['fill'] = 'red'
G.add_edge('at_distributor','qseecomd')
G.edge['at_distributor']['qseecomd']['write-read'] = '[open open][write read]'
G.edge['at_distributor']['qseecomd']['fill'] = 'red'
G.add_edge('at_distributor','vold')
G.edge['at_distributor']['vold']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['at_distributor']['vold']['fill'] = 'red'
G.add_edge('at_distributor','efsks')
G.edge['at_distributor']['efsks']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('at_distributor','flash_recovery')
G.edge['at_distributor']['flash_recovery']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('at_distributor','flash_recovery')
G.edge['at_distributor']['flash_recovery']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('at_distributor','init_shell')
G.edge['at_distributor']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('at_distributor','init_shell')
G.edge['at_distributor']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search]'
G.add_edge('at_distributor','ks')
G.edge['at_distributor']['ks']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('at_distributor','prepare_param')
G.edge['at_distributor']['prepare_param']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('at_distributor','prepare_param')
G.edge['at_distributor']['prepare_param']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('at_distributor','qseecomd')
G.edge['at_distributor']['qseecomd']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('at_distributor','qseecomd')
G.edge['at_distributor']['qseecomd']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('at_distributor','vold')
G.edge['at_distributor']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('at_distributor','vold')
G.edge['at_distributor']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('cbd','efsks')
G.edge['cbd']['efsks']['write-read'] = '[open open]'
G.add_edge('cbd','flash_recovery')
G.edge['cbd']['flash_recovery']['write-read'] = '[open open]'
G.add_edge('cbd','init_shell')
G.edge['cbd']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('cbd','ks')
G.edge['cbd']['ks']['write-read'] = '[open open]'
G.add_edge('cbd','prepare_param')
G.edge['cbd']['prepare_param']['write-read'] = '[open open]'
G.add_edge('cbd','qseecomd')
G.edge['cbd']['qseecomd']['write-read'] = '[open open]'
G.add_edge('cbd','vold')
G.edge['cbd']['vold']['write-read'] = '[open open]'
G.add_edge('cbd','prepare_param')
G.edge['cbd']['prepare_param']['write-read'] = '[open open][setattr getattr]'
G.add_edge('cbd','vold')
G.edge['cbd']['vold']['write-read'] = '[open open][setattr getattr]'
G.add_edge('cbd','efsks')
G.edge['cbd']['efsks']['write-read'] = '[open open][write read]'
G.edge['cbd']['efsks']['fill'] = 'red'
G.add_edge('cbd','flash_recovery')
G.edge['cbd']['flash_recovery']['write-read'] = '[open open][write read]'
G.edge['cbd']['flash_recovery']['fill'] = 'red'
G.add_edge('cbd','init_shell')
G.edge['cbd']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['cbd']['init_shell']['fill'] = 'red'
G.add_edge('cbd','ks')
G.edge['cbd']['ks']['write-read'] = '[open open][write read]'
G.edge['cbd']['ks']['fill'] = 'red'
G.add_edge('cbd','mdm_helper')
G.edge['cbd']['mdm_helper']['write-read'] = '[write read]'
G.edge['cbd']['mdm_helper']['fill'] = 'red'
G.add_edge('cbd','prepare_param')
G.edge['cbd']['prepare_param']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['cbd']['prepare_param']['fill'] = 'red'
G.add_edge('cbd','qseecomd')
G.edge['cbd']['qseecomd']['write-read'] = '[open open][write read]'
G.edge['cbd']['qseecomd']['fill'] = 'red'
G.add_edge('cbd','vold')
G.edge['cbd']['vold']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['cbd']['vold']['fill'] = 'red'
G.add_edge('cbd','efsks')
G.edge['cbd']['efsks']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('cbd','flash_recovery')
G.edge['cbd']['flash_recovery']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('cbd','flash_recovery')
G.edge['cbd']['flash_recovery']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('cbd','init_shell')
G.edge['cbd']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('cbd','init_shell')
G.edge['cbd']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search]'
G.add_edge('cbd','ks')
G.edge['cbd']['ks']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('cbd','prepare_param')
G.edge['cbd']['prepare_param']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('cbd','prepare_param')
G.edge['cbd']['prepare_param']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('cbd','qseecomd')
G.edge['cbd']['qseecomd']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('cbd','qseecomd')
G.edge['cbd']['qseecomd']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('cbd','vold')
G.edge['cbd']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('cbd','vold')
G.edge['cbd']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('connfwexe','efsks')
G.edge['connfwexe']['efsks']['write-read'] = '[open open]'
G.add_edge('connfwexe','flash_recovery')
G.edge['connfwexe']['flash_recovery']['write-read'] = '[open open]'
G.add_edge('connfwexe','init_shell')
G.edge['connfwexe']['init_shell']['write-read'] = '[open open]'
G.add_edge('connfwexe','ks')
G.edge['connfwexe']['ks']['write-read'] = '[open open]'
G.add_edge('connfwexe','prepare_param')
G.edge['connfwexe']['prepare_param']['write-read'] = '[open open]'
G.add_edge('connfwexe','qseecomd')
G.edge['connfwexe']['qseecomd']['write-read'] = '[open open]'
G.add_edge('connfwexe','vold')
G.edge['connfwexe']['vold']['write-read'] = '[open open]'
G.add_edge('connfwexe','prepare_param')
G.edge['connfwexe']['prepare_param']['write-read'] = '[open open][setattr getattr]'
G.add_edge('connfwexe','vold')
G.edge['connfwexe']['vold']['write-read'] = '[open open][setattr getattr]'
G.add_edge('connfwexe','efsks')
G.edge['connfwexe']['efsks']['write-read'] = '[open open][write read]'
G.edge['connfwexe']['efsks']['fill'] = 'red'
G.add_edge('connfwexe','flash_recovery')
G.edge['connfwexe']['flash_recovery']['write-read'] = '[open open][write read]'
G.edge['connfwexe']['flash_recovery']['fill'] = 'red'
G.add_edge('connfwexe','init_shell')
G.edge['connfwexe']['init_shell']['write-read'] = '[open open][write read]'
G.edge['connfwexe']['init_shell']['fill'] = 'red'
G.add_edge('connfwexe','ks')
G.edge['connfwexe']['ks']['write-read'] = '[open open][write read]'
G.edge['connfwexe']['ks']['fill'] = 'red'
G.add_edge('connfwexe','mdm_helper')
G.edge['connfwexe']['mdm_helper']['write-read'] = '[write read]'
G.edge['connfwexe']['mdm_helper']['fill'] = 'red'
G.add_edge('connfwexe','prepare_param')
G.edge['connfwexe']['prepare_param']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['connfwexe']['prepare_param']['fill'] = 'red'
G.add_edge('connfwexe','qseecomd')
G.edge['connfwexe']['qseecomd']['write-read'] = '[open open][write read]'
G.edge['connfwexe']['qseecomd']['fill'] = 'red'
G.add_edge('connfwexe','vold')
G.edge['connfwexe']['vold']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['connfwexe']['vold']['fill'] = 'red'
G.add_edge('connfwexe','efsks')
G.edge['connfwexe']['efsks']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('connfwexe','flash_recovery')
G.edge['connfwexe']['flash_recovery']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('connfwexe','flash_recovery')
G.edge['connfwexe']['flash_recovery']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('connfwexe','init_shell')
G.edge['connfwexe']['init_shell']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('connfwexe','init_shell')
G.edge['connfwexe']['init_shell']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('connfwexe','ks')
G.edge['connfwexe']['ks']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('connfwexe','prepare_param')
G.edge['connfwexe']['prepare_param']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('connfwexe','prepare_param')
G.edge['connfwexe']['prepare_param']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('connfwexe','qseecomd')
G.edge['connfwexe']['qseecomd']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('connfwexe','qseecomd')
G.edge['connfwexe']['qseecomd']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('connfwexe','vold')
G.edge['connfwexe']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('connfwexe','vold')
G.edge['connfwexe']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('efsks','efsks')
G.edge['efsks']['efsks']['write-read'] = '[open open]'
G.add_edge('efsks','flash_recovery')
G.edge['efsks']['flash_recovery']['write-read'] = '[open open]'
G.add_edge('efsks','init_shell')
G.edge['efsks']['init_shell']['write-read'] = '[open open]'
G.add_edge('efsks','ks')
G.edge['efsks']['ks']['write-read'] = '[open open]'
G.add_edge('efsks','prepare_param')
G.edge['efsks']['prepare_param']['write-read'] = '[open open]'
G.add_edge('efsks','qseecomd')
G.edge['efsks']['qseecomd']['write-read'] = '[open open]'
G.add_edge('efsks','vold')
G.edge['efsks']['vold']['write-read'] = '[open open]'
G.add_edge('efsks','prepare_param')
G.edge['efsks']['prepare_param']['write-read'] = '[open open][setattr getattr]'
G.add_edge('efsks','vold')
G.edge['efsks']['vold']['write-read'] = '[open open][setattr getattr]'
G.add_edge('efsks','efsks')
G.edge['efsks']['efsks']['write-read'] = '[open open][write read]'
G.edge['efsks']['efsks']['fill'] = 'red'
G.add_edge('efsks','flash_recovery')
G.edge['efsks']['flash_recovery']['write-read'] = '[open open][write read]'
G.edge['efsks']['flash_recovery']['fill'] = 'red'
G.add_edge('efsks','init_shell')
G.edge['efsks']['init_shell']['write-read'] = '[open open][write read]'
G.edge['efsks']['init_shell']['fill'] = 'red'
G.add_edge('efsks','ks')
G.edge['efsks']['ks']['write-read'] = '[open open][write read]'
G.edge['efsks']['ks']['fill'] = 'red'
G.add_edge('efsks','mdm_helper')
G.edge['efsks']['mdm_helper']['write-read'] = '[write read]'
G.edge['efsks']['mdm_helper']['fill'] = 'red'
G.add_edge('efsks','prepare_param')
G.edge['efsks']['prepare_param']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['efsks']['prepare_param']['fill'] = 'red'
G.add_edge('efsks','qseecomd')
G.edge['efsks']['qseecomd']['write-read'] = '[open open][write read]'
G.edge['efsks']['qseecomd']['fill'] = 'red'
G.add_edge('efsks','vold')
G.edge['efsks']['vold']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['efsks']['vold']['fill'] = 'red'
G.add_edge('efsks','efsks')
G.edge['efsks']['efsks']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('efsks','flash_recovery')
G.edge['efsks']['flash_recovery']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('efsks','flash_recovery')
G.edge['efsks']['flash_recovery']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('efsks','init_shell')
G.edge['efsks']['init_shell']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('efsks','init_shell')
G.edge['efsks']['init_shell']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('efsks','ks')
G.edge['efsks']['ks']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('efsks','prepare_param')
G.edge['efsks']['prepare_param']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('efsks','prepare_param')
G.edge['efsks']['prepare_param']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('efsks','qseecomd')
G.edge['efsks']['qseecomd']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('efsks','qseecomd')
G.edge['efsks']['qseecomd']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('efsks','vold')
G.edge['efsks']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('efsks','vold')
G.edge['efsks']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('epmd','efsks')
G.edge['epmd']['efsks']['write-read'] = '[open open]'
G.add_edge('epmd','flash_recovery')
G.edge['epmd']['flash_recovery']['write-read'] = '[open open]'
G.add_edge('epmd','init_shell')
G.edge['epmd']['init_shell']['write-read'] = '[open open][open open][open open]'
G.add_edge('epmd','ks')
G.edge['epmd']['ks']['write-read'] = '[open open]'
G.add_edge('epmd','prepare_param')
G.edge['epmd']['prepare_param']['write-read'] = '[open open]'
G.add_edge('epmd','qseecomd')
G.edge['epmd']['qseecomd']['write-read'] = '[open open]'
G.add_edge('epmd','vold')
G.edge['epmd']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('epmd','prepare_param')
G.edge['epmd']['prepare_param']['write-read'] = '[open open][setattr getattr]'
G.add_edge('epmd','vold')
G.edge['epmd']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('epmd','efsks')
G.edge['epmd']['efsks']['write-read'] = '[open open][write read]'
G.edge['epmd']['efsks']['fill'] = 'red'
G.add_edge('epmd','flash_recovery')
G.edge['epmd']['flash_recovery']['write-read'] = '[open open][write read]'
G.edge['epmd']['flash_recovery']['fill'] = 'red'
G.add_edge('epmd','init_shell')
G.edge['epmd']['init_shell']['write-read'] = '[open open][open open][open open][write read]'
G.edge['epmd']['init_shell']['fill'] = 'red'
G.add_edge('epmd','ks')
G.edge['epmd']['ks']['write-read'] = '[open open][write read]'
G.edge['epmd']['ks']['fill'] = 'red'
G.add_edge('epmd','mdm_helper')
G.edge['epmd']['mdm_helper']['write-read'] = '[write read]'
G.edge['epmd']['mdm_helper']['fill'] = 'red'
G.add_edge('epmd','prepare_param')
G.edge['epmd']['prepare_param']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['epmd']['prepare_param']['fill'] = 'red'
G.add_edge('epmd','qseecomd')
G.edge['epmd']['qseecomd']['write-read'] = '[open open][write read]'
G.edge['epmd']['qseecomd']['fill'] = 'red'
G.add_edge('epmd','vold')
G.edge['epmd']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['epmd']['vold']['fill'] = 'red'
G.add_edge('epmd','efsks')
G.edge['epmd']['efsks']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('epmd','flash_recovery')
G.edge['epmd']['flash_recovery']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('epmd','flash_recovery')
G.edge['epmd']['flash_recovery']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('epmd','init_shell')
G.edge['epmd']['init_shell']['write-read'] = '[open open][open open][open open][write read][add_name search]'
G.add_edge('epmd','init_shell')
G.edge['epmd']['init_shell']['write-read'] = '[open open][open open][open open][write read][add_name search][remove_name search]'
G.add_edge('epmd','ks')
G.edge['epmd']['ks']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('epmd','prepare_param')
G.edge['epmd']['prepare_param']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('epmd','prepare_param')
G.edge['epmd']['prepare_param']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('epmd','qseecomd')
G.edge['epmd']['qseecomd']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('epmd','qseecomd')
G.edge['epmd']['qseecomd']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('epmd','vold')
G.edge['epmd']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('epmd','vold')
G.edge['epmd']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('flash_recovery','efsks')
G.edge['flash_recovery']['efsks']['write-read'] = '[open open]'
G.add_edge('flash_recovery','flash_recovery')
G.edge['flash_recovery']['flash_recovery']['write-read'] = '[open open]'
G.add_edge('flash_recovery','init_shell')
G.edge['flash_recovery']['init_shell']['write-read'] = '[open open]'
G.add_edge('flash_recovery','ks')
G.edge['flash_recovery']['ks']['write-read'] = '[open open]'
G.add_edge('flash_recovery','prepare_param')
G.edge['flash_recovery']['prepare_param']['write-read'] = '[open open]'
G.add_edge('flash_recovery','qseecomd')
G.edge['flash_recovery']['qseecomd']['write-read'] = '[open open]'
G.add_edge('flash_recovery','vold')
G.edge['flash_recovery']['vold']['write-read'] = '[open open]'
G.add_edge('flash_recovery','prepare_param')
G.edge['flash_recovery']['prepare_param']['write-read'] = '[open open][setattr getattr]'
G.add_edge('flash_recovery','vold')
G.edge['flash_recovery']['vold']['write-read'] = '[open open][setattr getattr]'
G.add_edge('flash_recovery','efsks')
G.edge['flash_recovery']['efsks']['write-read'] = '[open open][write read]'
G.edge['flash_recovery']['efsks']['fill'] = 'red'
G.add_edge('flash_recovery','flash_recovery')
G.edge['flash_recovery']['flash_recovery']['write-read'] = '[open open][write read]'
G.edge['flash_recovery']['flash_recovery']['fill'] = 'red'
G.add_edge('flash_recovery','init_shell')
G.edge['flash_recovery']['init_shell']['write-read'] = '[open open][write read]'
G.edge['flash_recovery']['init_shell']['fill'] = 'red'
G.add_edge('flash_recovery','ks')
G.edge['flash_recovery']['ks']['write-read'] = '[open open][write read]'
G.edge['flash_recovery']['ks']['fill'] = 'red'
G.add_edge('flash_recovery','mdm_helper')
G.edge['flash_recovery']['mdm_helper']['write-read'] = '[write read]'
G.edge['flash_recovery']['mdm_helper']['fill'] = 'red'
G.add_edge('flash_recovery','prepare_param')
G.edge['flash_recovery']['prepare_param']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['flash_recovery']['prepare_param']['fill'] = 'red'
G.add_edge('flash_recovery','qseecomd')
G.edge['flash_recovery']['qseecomd']['write-read'] = '[open open][write read]'
G.edge['flash_recovery']['qseecomd']['fill'] = 'red'
G.add_edge('flash_recovery','vold')
G.edge['flash_recovery']['vold']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['flash_recovery']['vold']['fill'] = 'red'
G.add_edge('flash_recovery','efsks')
G.edge['flash_recovery']['efsks']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('flash_recovery','flash_recovery')
G.edge['flash_recovery']['flash_recovery']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('flash_recovery','flash_recovery')
G.edge['flash_recovery']['flash_recovery']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('flash_recovery','init_shell')
G.edge['flash_recovery']['init_shell']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('flash_recovery','init_shell')
G.edge['flash_recovery']['init_shell']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('flash_recovery','ks')
G.edge['flash_recovery']['ks']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('flash_recovery','prepare_param')
G.edge['flash_recovery']['prepare_param']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('flash_recovery','prepare_param')
G.edge['flash_recovery']['prepare_param']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('flash_recovery','qseecomd')
G.edge['flash_recovery']['qseecomd']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('flash_recovery','qseecomd')
G.edge['flash_recovery']['qseecomd']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('flash_recovery','vold')
G.edge['flash_recovery']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('flash_recovery','vold')
G.edge['flash_recovery']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('icd','efsks')
G.edge['icd']['efsks']['write-read'] = '[open open]'
G.add_edge('icd','flash_recovery')
G.edge['icd']['flash_recovery']['write-read'] = '[open open]'
G.add_edge('icd','init_shell')
G.edge['icd']['init_shell']['write-read'] = '[open open]'
G.add_edge('icd','ks')
G.edge['icd']['ks']['write-read'] = '[open open]'
G.add_edge('icd','prepare_param')
G.edge['icd']['prepare_param']['write-read'] = '[open open]'
G.add_edge('icd','qseecomd')
G.edge['icd']['qseecomd']['write-read'] = '[open open]'
G.add_edge('icd','vold')
G.edge['icd']['vold']['write-read'] = '[open open]'
G.add_edge('icd','prepare_param')
G.edge['icd']['prepare_param']['write-read'] = '[open open][setattr getattr]'
G.add_edge('icd','vold')
G.edge['icd']['vold']['write-read'] = '[open open][setattr getattr]'
G.add_edge('icd','efsks')
G.edge['icd']['efsks']['write-read'] = '[open open][write read]'
G.edge['icd']['efsks']['fill'] = 'red'
G.add_edge('icd','flash_recovery')
G.edge['icd']['flash_recovery']['write-read'] = '[open open][write read]'
G.edge['icd']['flash_recovery']['fill'] = 'red'
G.add_edge('icd','init_shell')
G.edge['icd']['init_shell']['write-read'] = '[open open][write read]'
G.edge['icd']['init_shell']['fill'] = 'red'
G.add_edge('icd','ks')
G.edge['icd']['ks']['write-read'] = '[open open][write read]'
G.edge['icd']['ks']['fill'] = 'red'
G.add_edge('icd','mdm_helper')
G.edge['icd']['mdm_helper']['write-read'] = '[write read]'
G.edge['icd']['mdm_helper']['fill'] = 'red'
G.add_edge('icd','prepare_param')
G.edge['icd']['prepare_param']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['icd']['prepare_param']['fill'] = 'red'
G.add_edge('icd','qseecomd')
G.edge['icd']['qseecomd']['write-read'] = '[open open][write read]'
G.edge['icd']['qseecomd']['fill'] = 'red'
G.add_edge('icd','vold')
G.edge['icd']['vold']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['icd']['vold']['fill'] = 'red'
G.add_edge('icd','efsks')
G.edge['icd']['efsks']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('icd','flash_recovery')
G.edge['icd']['flash_recovery']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('icd','flash_recovery')
G.edge['icd']['flash_recovery']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('icd','init_shell')
G.edge['icd']['init_shell']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('icd','init_shell')
G.edge['icd']['init_shell']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('icd','ks')
G.edge['icd']['ks']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('icd','prepare_param')
G.edge['icd']['prepare_param']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('icd','prepare_param')
G.edge['icd']['prepare_param']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('icd','qseecomd')
G.edge['icd']['qseecomd']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('icd','qseecomd')
G.edge['icd']['qseecomd']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('icd','vold')
G.edge['icd']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('icd','vold')
G.edge['icd']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('init_shell','efsks')
G.edge['init_shell']['efsks']['write-read'] = '[open open]'
G.add_edge('init_shell','flash_recovery')
G.edge['init_shell']['flash_recovery']['write-read'] = '[open open]'
G.add_edge('init_shell','init_shell')
G.edge['init_shell']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open]'
G.add_edge('init_shell','ks')
G.edge['init_shell']['ks']['write-read'] = '[open open]'
G.add_edge('init_shell','prepare_param')
G.edge['init_shell']['prepare_param']['write-read'] = '[open open]'
G.add_edge('init_shell','qseecomd')
G.edge['init_shell']['qseecomd']['write-read'] = '[open open]'
G.add_edge('init_shell','vold')
G.edge['init_shell']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('init_shell','prepare_param')
G.edge['init_shell']['prepare_param']['write-read'] = '[open open][setattr getattr]'
G.add_edge('init_shell','vold')
G.edge['init_shell']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('init_shell','efsks')
G.edge['init_shell']['efsks']['write-read'] = '[open open][write read]'
G.edge['init_shell']['efsks']['fill'] = 'red'
G.add_edge('init_shell','flash_recovery')
G.edge['init_shell']['flash_recovery']['write-read'] = '[open open][write read]'
G.edge['init_shell']['flash_recovery']['fill'] = 'red'
G.add_edge('init_shell','init_shell')
G.edge['init_shell']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read]'
G.edge['init_shell']['init_shell']['fill'] = 'red'
G.add_edge('init_shell','ks')
G.edge['init_shell']['ks']['write-read'] = '[open open][write read]'
G.edge['init_shell']['ks']['fill'] = 'red'
G.add_edge('init_shell','mdm_helper')
G.edge['init_shell']['mdm_helper']['write-read'] = '[write read]'
G.edge['init_shell']['mdm_helper']['fill'] = 'red'
G.add_edge('init_shell','prepare_param')
G.edge['init_shell']['prepare_param']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['init_shell']['prepare_param']['fill'] = 'red'
G.add_edge('init_shell','qseecomd')
G.edge['init_shell']['qseecomd']['write-read'] = '[open open][write read]'
G.edge['init_shell']['qseecomd']['fill'] = 'red'
G.add_edge('init_shell','vold')
G.edge['init_shell']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['init_shell']['vold']['fill'] = 'red'
G.add_edge('init_shell','efsks')
G.edge['init_shell']['efsks']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('init_shell','flash_recovery')
G.edge['init_shell']['flash_recovery']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('init_shell','flash_recovery')
G.edge['init_shell']['flash_recovery']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('init_shell','init_shell')
G.edge['init_shell']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read][add_name search]'
G.add_edge('init_shell','init_shell')
G.edge['init_shell']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search]'
G.add_edge('init_shell','ks')
G.edge['init_shell']['ks']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('init_shell','prepare_param')
G.edge['init_shell']['prepare_param']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('init_shell','prepare_param')
G.edge['init_shell']['prepare_param']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('init_shell','qseecomd')
G.edge['init_shell']['qseecomd']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('init_shell','qseecomd')
G.edge['init_shell']['qseecomd']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('init_shell','vold')
G.edge['init_shell']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('init_shell','vold')
G.edge['init_shell']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('install_recovery','efsks')
G.edge['install_recovery']['efsks']['write-read'] = '[add_name search]'
G.add_edge('install_recovery','flash_recovery')
G.edge['install_recovery']['flash_recovery']['write-read'] = '[add_name search]'
G.add_edge('install_recovery','flash_recovery')
G.edge['install_recovery']['flash_recovery']['write-read'] = '[add_name search][remove_name search]'
G.add_edge('install_recovery','init_shell')
G.edge['install_recovery']['init_shell']['write-read'] = '[add_name search]'
G.add_edge('install_recovery','init_shell')
G.edge['install_recovery']['init_shell']['write-read'] = '[add_name search][remove_name search]'
G.add_edge('install_recovery','ks')
G.edge['install_recovery']['ks']['write-read'] = '[add_name search]'
G.add_edge('install_recovery','prepare_param')
G.edge['install_recovery']['prepare_param']['write-read'] = '[add_name search]'
G.add_edge('install_recovery','prepare_param')
G.edge['install_recovery']['prepare_param']['write-read'] = '[add_name search][remove_name search]'
G.add_edge('install_recovery','qseecomd')
G.edge['install_recovery']['qseecomd']['write-read'] = '[add_name search]'
G.add_edge('install_recovery','qseecomd')
G.edge['install_recovery']['qseecomd']['write-read'] = '[add_name search][remove_name search]'
G.add_edge('install_recovery','vold')
G.edge['install_recovery']['vold']['write-read'] = '[add_name search]'
G.add_edge('install_recovery','vold')
G.edge['install_recovery']['vold']['write-read'] = '[add_name search][remove_name search]'
G.add_edge('kapd','efsks')
G.edge['kapd']['efsks']['write-read'] = '[open open]'
G.add_edge('kapd','flash_recovery')
G.edge['kapd']['flash_recovery']['write-read'] = '[open open]'
G.add_edge('kapd','init_shell')
G.edge['kapd']['init_shell']['write-read'] = '[open open]'
G.add_edge('kapd','ks')
G.edge['kapd']['ks']['write-read'] = '[open open]'
G.add_edge('kapd','prepare_param')
G.edge['kapd']['prepare_param']['write-read'] = '[open open]'
G.add_edge('kapd','qseecomd')
G.edge['kapd']['qseecomd']['write-read'] = '[open open]'
G.add_edge('kapd','vold')
G.edge['kapd']['vold']['write-read'] = '[open open]'
G.add_edge('kapd','prepare_param')
G.edge['kapd']['prepare_param']['write-read'] = '[open open][setattr getattr]'
G.add_edge('kapd','vold')
G.edge['kapd']['vold']['write-read'] = '[open open][setattr getattr]'
G.add_edge('kapd','efsks')
G.edge['kapd']['efsks']['write-read'] = '[open open][write read]'
G.edge['kapd']['efsks']['fill'] = 'red'
G.add_edge('kapd','flash_recovery')
G.edge['kapd']['flash_recovery']['write-read'] = '[open open][write read]'
G.edge['kapd']['flash_recovery']['fill'] = 'red'
G.add_edge('kapd','init_shell')
G.edge['kapd']['init_shell']['write-read'] = '[open open][write read]'
G.edge['kapd']['init_shell']['fill'] = 'red'
G.add_edge('kapd','ks')
G.edge['kapd']['ks']['write-read'] = '[open open][write read]'
G.edge['kapd']['ks']['fill'] = 'red'
G.add_edge('kapd','mdm_helper')
G.edge['kapd']['mdm_helper']['write-read'] = '[write read]'
G.edge['kapd']['mdm_helper']['fill'] = 'red'
G.add_edge('kapd','prepare_param')
G.edge['kapd']['prepare_param']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['kapd']['prepare_param']['fill'] = 'red'
G.add_edge('kapd','qseecomd')
G.edge['kapd']['qseecomd']['write-read'] = '[open open][write read]'
G.edge['kapd']['qseecomd']['fill'] = 'red'
G.add_edge('kapd','vold')
G.edge['kapd']['vold']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['kapd']['vold']['fill'] = 'red'
G.add_edge('kapd','efsks')
G.edge['kapd']['efsks']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('kapd','flash_recovery')
G.edge['kapd']['flash_recovery']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('kapd','flash_recovery')
G.edge['kapd']['flash_recovery']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('kapd','init_shell')
G.edge['kapd']['init_shell']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('kapd','init_shell')
G.edge['kapd']['init_shell']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('kapd','ks')
G.edge['kapd']['ks']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('kapd','prepare_param')
G.edge['kapd']['prepare_param']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('kapd','prepare_param')
G.edge['kapd']['prepare_param']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('kapd','qseecomd')
G.edge['kapd']['qseecomd']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('kapd','qseecomd')
G.edge['kapd']['qseecomd']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('kapd','vold')
G.edge['kapd']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('kapd','vold')
G.edge['kapd']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('keystore','efsks')
G.edge['keystore']['efsks']['write-read'] = '[open open]'
G.add_edge('keystore','flash_recovery')
G.edge['keystore']['flash_recovery']['write-read'] = '[open open]'
G.add_edge('keystore','init_shell')
G.edge['keystore']['init_shell']['write-read'] = '[open open]'
G.add_edge('keystore','ks')
G.edge['keystore']['ks']['write-read'] = '[open open]'
G.add_edge('keystore','prepare_param')
G.edge['keystore']['prepare_param']['write-read'] = '[open open]'
G.add_edge('keystore','qseecomd')
G.edge['keystore']['qseecomd']['write-read'] = '[open open]'
G.add_edge('keystore','vold')
G.edge['keystore']['vold']['write-read'] = '[open open]'
G.add_edge('keystore','prepare_param')
G.edge['keystore']['prepare_param']['write-read'] = '[open open][setattr getattr]'
G.add_edge('keystore','vold')
G.edge['keystore']['vold']['write-read'] = '[open open][setattr getattr]'
G.add_edge('keystore','efsks')
G.edge['keystore']['efsks']['write-read'] = '[open open][write read]'
G.edge['keystore']['efsks']['fill'] = 'red'
G.add_edge('keystore','flash_recovery')
G.edge['keystore']['flash_recovery']['write-read'] = '[open open][write read]'
G.edge['keystore']['flash_recovery']['fill'] = 'red'
G.add_edge('keystore','init_shell')
G.edge['keystore']['init_shell']['write-read'] = '[open open][write read]'
G.edge['keystore']['init_shell']['fill'] = 'red'
G.add_edge('keystore','ks')
G.edge['keystore']['ks']['write-read'] = '[open open][write read]'
G.edge['keystore']['ks']['fill'] = 'red'
G.add_edge('keystore','mdm_helper')
G.edge['keystore']['mdm_helper']['write-read'] = '[write read]'
G.edge['keystore']['mdm_helper']['fill'] = 'red'
G.add_edge('keystore','prepare_param')
G.edge['keystore']['prepare_param']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['keystore']['prepare_param']['fill'] = 'red'
G.add_edge('keystore','qseecomd')
G.edge['keystore']['qseecomd']['write-read'] = '[open open][write read]'
G.edge['keystore']['qseecomd']['fill'] = 'red'
G.add_edge('keystore','vold')
G.edge['keystore']['vold']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['keystore']['vold']['fill'] = 'red'
G.add_edge('keystore','efsks')
G.edge['keystore']['efsks']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('keystore','flash_recovery')
G.edge['keystore']['flash_recovery']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('keystore','flash_recovery')
G.edge['keystore']['flash_recovery']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('keystore','init_shell')
G.edge['keystore']['init_shell']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('keystore','init_shell')
G.edge['keystore']['init_shell']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('keystore','ks')
G.edge['keystore']['ks']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('keystore','prepare_param')
G.edge['keystore']['prepare_param']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('keystore','prepare_param')
G.edge['keystore']['prepare_param']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('keystore','qseecomd')
G.edge['keystore']['qseecomd']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('keystore','qseecomd')
G.edge['keystore']['qseecomd']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('keystore','vold')
G.edge['keystore']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('keystore','vold')
G.edge['keystore']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('ks','efsks')
G.edge['ks']['efsks']['write-read'] = '[open open]'
G.add_edge('ks','flash_recovery')
G.edge['ks']['flash_recovery']['write-read'] = '[open open]'
G.add_edge('ks','init_shell')
G.edge['ks']['init_shell']['write-read'] = '[open open]'
G.add_edge('ks','ks')
G.edge['ks']['ks']['write-read'] = '[open open]'
G.add_edge('ks','prepare_param')
G.edge['ks']['prepare_param']['write-read'] = '[open open]'
G.add_edge('ks','qseecomd')
G.edge['ks']['qseecomd']['write-read'] = '[open open]'
G.add_edge('ks','vold')
G.edge['ks']['vold']['write-read'] = '[open open]'
G.add_edge('ks','prepare_param')
G.edge['ks']['prepare_param']['write-read'] = '[open open][setattr getattr]'
G.add_edge('ks','vold')
G.edge['ks']['vold']['write-read'] = '[open open][setattr getattr]'
G.add_edge('ks','efsks')
G.edge['ks']['efsks']['write-read'] = '[open open][write read]'
G.edge['ks']['efsks']['fill'] = 'red'
G.add_edge('ks','flash_recovery')
G.edge['ks']['flash_recovery']['write-read'] = '[open open][write read]'
G.edge['ks']['flash_recovery']['fill'] = 'red'
G.add_edge('ks','init_shell')
G.edge['ks']['init_shell']['write-read'] = '[open open][write read]'
G.edge['ks']['init_shell']['fill'] = 'red'
G.add_edge('ks','ks')
G.edge['ks']['ks']['write-read'] = '[open open][write read]'
G.edge['ks']['ks']['fill'] = 'red'
G.add_edge('ks','mdm_helper')
G.edge['ks']['mdm_helper']['write-read'] = '[write read]'
G.edge['ks']['mdm_helper']['fill'] = 'red'
G.add_edge('ks','prepare_param')
G.edge['ks']['prepare_param']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['ks']['prepare_param']['fill'] = 'red'
G.add_edge('ks','qseecomd')
G.edge['ks']['qseecomd']['write-read'] = '[open open][write read]'
G.edge['ks']['qseecomd']['fill'] = 'red'
G.add_edge('ks','vold')
G.edge['ks']['vold']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['ks']['vold']['fill'] = 'red'
G.add_edge('ks','efsks')
G.edge['ks']['efsks']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('ks','flash_recovery')
G.edge['ks']['flash_recovery']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('ks','flash_recovery')
G.edge['ks']['flash_recovery']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('ks','init_shell')
G.edge['ks']['init_shell']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('ks','init_shell')
G.edge['ks']['init_shell']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('ks','ks')
G.edge['ks']['ks']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('ks','prepare_param')
G.edge['ks']['prepare_param']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('ks','prepare_param')
G.edge['ks']['prepare_param']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('ks','qseecomd')
G.edge['ks']['qseecomd']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('ks','qseecomd')
G.edge['ks']['qseecomd']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('ks','vold')
G.edge['ks']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('ks','vold')
G.edge['ks']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('lpm','efsks')
G.edge['lpm']['efsks']['write-read'] = '[open open]'
G.add_edge('lpm','flash_recovery')
G.edge['lpm']['flash_recovery']['write-read'] = '[open open]'
G.add_edge('lpm','init_shell')
G.edge['lpm']['init_shell']['write-read'] = '[open open]'
G.add_edge('lpm','ks')
G.edge['lpm']['ks']['write-read'] = '[open open]'
G.add_edge('lpm','prepare_param')
G.edge['lpm']['prepare_param']['write-read'] = '[open open]'
G.add_edge('lpm','qseecomd')
G.edge['lpm']['qseecomd']['write-read'] = '[open open]'
G.add_edge('lpm','vold')
G.edge['lpm']['vold']['write-read'] = '[write read][append read][open open]'
G.add_edge('lpm','prepare_param')
G.edge['lpm']['prepare_param']['write-read'] = '[open open][setattr getattr]'
G.add_edge('lpm','vold')
G.edge['lpm']['vold']['write-read'] = '[write read][append read][open open][setattr getattr]'
G.add_edge('lpm','efsks')
G.edge['lpm']['efsks']['write-read'] = '[open open][write read]'
G.edge['lpm']['efsks']['fill'] = 'red'
G.add_edge('lpm','flash_recovery')
G.edge['lpm']['flash_recovery']['write-read'] = '[open open][write read]'
G.edge['lpm']['flash_recovery']['fill'] = 'red'
G.add_edge('lpm','init_shell')
G.edge['lpm']['init_shell']['write-read'] = '[open open][write read]'
G.edge['lpm']['init_shell']['fill'] = 'red'
G.add_edge('lpm','ks')
G.edge['lpm']['ks']['write-read'] = '[open open][write read]'
G.edge['lpm']['ks']['fill'] = 'red'
G.add_edge('lpm','mdm_helper')
G.edge['lpm']['mdm_helper']['write-read'] = '[write read]'
G.edge['lpm']['mdm_helper']['fill'] = 'red'
G.add_edge('lpm','prepare_param')
G.edge['lpm']['prepare_param']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['lpm']['prepare_param']['fill'] = 'red'
G.add_edge('lpm','qseecomd')
G.edge['lpm']['qseecomd']['write-read'] = '[open open][write read]'
G.edge['lpm']['qseecomd']['fill'] = 'red'
G.add_edge('lpm','vold')
G.edge['lpm']['vold']['write-read'] = '[write read][append read][open open][setattr getattr][write read]'
G.edge['lpm']['vold']['fill'] = 'red'
G.add_edge('lpm','efsks')
G.edge['lpm']['efsks']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('lpm','flash_recovery')
G.edge['lpm']['flash_recovery']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('lpm','flash_recovery')
G.edge['lpm']['flash_recovery']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('lpm','init_shell')
G.edge['lpm']['init_shell']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('lpm','init_shell')
G.edge['lpm']['init_shell']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('lpm','ks')
G.edge['lpm']['ks']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('lpm','prepare_param')
G.edge['lpm']['prepare_param']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('lpm','prepare_param')
G.edge['lpm']['prepare_param']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('lpm','qseecomd')
G.edge['lpm']['qseecomd']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('lpm','qseecomd')
G.edge['lpm']['qseecomd']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('lpm','vold')
G.edge['lpm']['vold']['write-read'] = '[write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('lpm','vold')
G.edge['lpm']['vold']['write-read'] = '[write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('mdm_helper','prepare_param')
G.edge['mdm_helper']['prepare_param']['write-read'] = '[setattr getattr]'
G.add_edge('mdm_helper','vold')
G.edge['mdm_helper']['vold']['write-read'] = '[setattr getattr]'
G.add_edge('mdm_helper','efsks')
G.edge['mdm_helper']['efsks']['write-read'] = '[add_name search]'
G.add_edge('mdm_helper','flash_recovery')
G.edge['mdm_helper']['flash_recovery']['write-read'] = '[add_name search]'
G.add_edge('mdm_helper','flash_recovery')
G.edge['mdm_helper']['flash_recovery']['write-read'] = '[add_name search][remove_name search]'
G.add_edge('mdm_helper','init_shell')
G.edge['mdm_helper']['init_shell']['write-read'] = '[add_name search]'
G.add_edge('mdm_helper','init_shell')
G.edge['mdm_helper']['init_shell']['write-read'] = '[add_name search][remove_name search]'
G.add_edge('mdm_helper','ks')
G.edge['mdm_helper']['ks']['write-read'] = '[add_name search]'
G.add_edge('mdm_helper','prepare_param')
G.edge['mdm_helper']['prepare_param']['write-read'] = '[setattr getattr][add_name search]'
G.add_edge('mdm_helper','prepare_param')
G.edge['mdm_helper']['prepare_param']['write-read'] = '[setattr getattr][add_name search][remove_name search]'
G.add_edge('mdm_helper','qseecomd')
G.edge['mdm_helper']['qseecomd']['write-read'] = '[add_name search]'
G.add_edge('mdm_helper','qseecomd')
G.edge['mdm_helper']['qseecomd']['write-read'] = '[add_name search][remove_name search]'
G.add_edge('mdm_helper','vold')
G.edge['mdm_helper']['vold']['write-read'] = '[setattr getattr][add_name search]'
G.add_edge('mdm_helper','vold')
G.edge['mdm_helper']['vold']['write-read'] = '[setattr getattr][add_name search][remove_name search]'
G.add_edge('oneseg_mw','efsks')
G.edge['oneseg_mw']['efsks']['write-read'] = '[add_name search]'
G.add_edge('oneseg_mw','flash_recovery')
G.edge['oneseg_mw']['flash_recovery']['write-read'] = '[add_name search]'
G.add_edge('oneseg_mw','flash_recovery')
G.edge['oneseg_mw']['flash_recovery']['write-read'] = '[add_name search][remove_name search]'
G.add_edge('oneseg_mw','init_shell')
G.edge['oneseg_mw']['init_shell']['write-read'] = '[add_name search]'
G.add_edge('oneseg_mw','init_shell')
G.edge['oneseg_mw']['init_shell']['write-read'] = '[add_name search][remove_name search]'
G.add_edge('oneseg_mw','ks')
G.edge['oneseg_mw']['ks']['write-read'] = '[add_name search]'
G.add_edge('oneseg_mw','prepare_param')
G.edge['oneseg_mw']['prepare_param']['write-read'] = '[add_name search][remove_name search][add_name search]'
G.add_edge('oneseg_mw','prepare_param')
G.edge['oneseg_mw']['prepare_param']['write-read'] = '[add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('oneseg_mw','qseecomd')
G.edge['oneseg_mw']['qseecomd']['write-read'] = '[add_name search]'
G.add_edge('oneseg_mw','qseecomd')
G.edge['oneseg_mw']['qseecomd']['write-read'] = '[add_name search][remove_name search]'
G.add_edge('oneseg_mw','vold')
G.edge['oneseg_mw']['vold']['write-read'] = '[add_name search]'
G.add_edge('oneseg_mw','vold')
G.edge['oneseg_mw']['vold']['write-read'] = '[add_name search][remove_name search]'
G.add_edge('prepare_param','efsks')
G.edge['prepare_param']['efsks']['write-read'] = '[open open]'
G.add_edge('prepare_param','flash_recovery')
G.edge['prepare_param']['flash_recovery']['write-read'] = '[open open]'
G.add_edge('prepare_param','init_shell')
G.edge['prepare_param']['init_shell']['write-read'] = '[open open]'
G.add_edge('prepare_param','ks')
G.edge['prepare_param']['ks']['write-read'] = '[open open]'
G.add_edge('prepare_param','prepare_param')
G.edge['prepare_param']['prepare_param']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('prepare_param','qseecomd')
G.edge['prepare_param']['qseecomd']['write-read'] = '[open open]'
G.add_edge('prepare_param','vold')
G.edge['prepare_param']['vold']['write-read'] = '[open open]'
G.add_edge('prepare_param','prepare_param')
G.edge['prepare_param']['prepare_param']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('prepare_param','vold')
G.edge['prepare_param']['vold']['write-read'] = '[open open][setattr getattr]'
G.add_edge('prepare_param','efsks')
G.edge['prepare_param']['efsks']['write-read'] = '[open open][write read]'
G.edge['prepare_param']['efsks']['fill'] = 'red'
G.add_edge('prepare_param','flash_recovery')
G.edge['prepare_param']['flash_recovery']['write-read'] = '[open open][write read]'
G.edge['prepare_param']['flash_recovery']['fill'] = 'red'
G.add_edge('prepare_param','init_shell')
G.edge['prepare_param']['init_shell']['write-read'] = '[open open][write read]'
G.edge['prepare_param']['init_shell']['fill'] = 'red'
G.add_edge('prepare_param','ks')
G.edge['prepare_param']['ks']['write-read'] = '[open open][write read]'
G.edge['prepare_param']['ks']['fill'] = 'red'
G.add_edge('prepare_param','mdm_helper')
G.edge['prepare_param']['mdm_helper']['write-read'] = '[write read]'
G.edge['prepare_param']['mdm_helper']['fill'] = 'red'
G.add_edge('prepare_param','prepare_param')
G.edge['prepare_param']['prepare_param']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['prepare_param']['prepare_param']['fill'] = 'red'
G.add_edge('prepare_param','qseecomd')
G.edge['prepare_param']['qseecomd']['write-read'] = '[open open][write read]'
G.edge['prepare_param']['qseecomd']['fill'] = 'red'
G.add_edge('prepare_param','vold')
G.edge['prepare_param']['vold']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['prepare_param']['vold']['fill'] = 'red'
G.add_edge('prepare_param','efsks')
G.edge['prepare_param']['efsks']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('prepare_param','flash_recovery')
G.edge['prepare_param']['flash_recovery']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('prepare_param','flash_recovery')
G.edge['prepare_param']['flash_recovery']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('prepare_param','init_shell')
G.edge['prepare_param']['init_shell']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('prepare_param','init_shell')
G.edge['prepare_param']['init_shell']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('prepare_param','ks')
G.edge['prepare_param']['ks']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('prepare_param','prepare_param')
G.edge['prepare_param']['prepare_param']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search]'
G.add_edge('prepare_param','prepare_param')
G.edge['prepare_param']['prepare_param']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('prepare_param','qseecomd')
G.edge['prepare_param']['qseecomd']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('prepare_param','qseecomd')
G.edge['prepare_param']['qseecomd']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('prepare_param','vold')
G.edge['prepare_param']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('prepare_param','vold')
G.edge['prepare_param']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('qcks','efsks')
G.edge['qcks']['efsks']['write-read'] = '[open open]'
G.add_edge('qcks','flash_recovery')
G.edge['qcks']['flash_recovery']['write-read'] = '[open open]'
G.add_edge('qcks','init_shell')
G.edge['qcks']['init_shell']['write-read'] = '[open open]'
G.add_edge('qcks','ks')
G.edge['qcks']['ks']['write-read'] = '[open open]'
G.add_edge('qcks','prepare_param')
G.edge['qcks']['prepare_param']['write-read'] = '[open open]'
G.add_edge('qcks','qseecomd')
G.edge['qcks']['qseecomd']['write-read'] = '[open open]'
G.add_edge('qcks','vold')
G.edge['qcks']['vold']['write-read'] = '[open open]'
G.add_edge('qcks','prepare_param')
G.edge['qcks']['prepare_param']['write-read'] = '[open open][setattr getattr]'
G.add_edge('qcks','vold')
G.edge['qcks']['vold']['write-read'] = '[open open][setattr getattr]'
G.add_edge('qcks','efsks')
G.edge['qcks']['efsks']['write-read'] = '[open open][write read]'
G.edge['qcks']['efsks']['fill'] = 'red'
G.add_edge('qcks','flash_recovery')
G.edge['qcks']['flash_recovery']['write-read'] = '[open open][write read]'
G.edge['qcks']['flash_recovery']['fill'] = 'red'
G.add_edge('qcks','init_shell')
G.edge['qcks']['init_shell']['write-read'] = '[open open][write read]'
G.edge['qcks']['init_shell']['fill'] = 'red'
G.add_edge('qcks','ks')
G.edge['qcks']['ks']['write-read'] = '[open open][write read]'
G.edge['qcks']['ks']['fill'] = 'red'
G.add_edge('qcks','mdm_helper')
G.edge['qcks']['mdm_helper']['write-read'] = '[write read]'
G.edge['qcks']['mdm_helper']['fill'] = 'red'
G.add_edge('qcks','prepare_param')
G.edge['qcks']['prepare_param']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['qcks']['prepare_param']['fill'] = 'red'
G.add_edge('qcks','qseecomd')
G.edge['qcks']['qseecomd']['write-read'] = '[open open][write read]'
G.edge['qcks']['qseecomd']['fill'] = 'red'
G.add_edge('qcks','vold')
G.edge['qcks']['vold']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['qcks']['vold']['fill'] = 'red'
G.add_edge('qcks','efsks')
G.edge['qcks']['efsks']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('qcks','flash_recovery')
G.edge['qcks']['flash_recovery']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('qcks','flash_recovery')
G.edge['qcks']['flash_recovery']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('qcks','init_shell')
G.edge['qcks']['init_shell']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('qcks','init_shell')
G.edge['qcks']['init_shell']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('qcks','ks')
G.edge['qcks']['ks']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('qcks','prepare_param')
G.edge['qcks']['prepare_param']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('qcks','prepare_param')
G.edge['qcks']['prepare_param']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('qcks','qseecomd')
G.edge['qcks']['qseecomd']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('qcks','qseecomd')
G.edge['qcks']['qseecomd']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('qcks','vold')
G.edge['qcks']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('qcks','vold')
G.edge['qcks']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('qcomsysd','efsks')
G.edge['qcomsysd']['efsks']['write-read'] = '[add_name search]'
G.add_edge('qcomsysd','flash_recovery')
G.edge['qcomsysd']['flash_recovery']['write-read'] = '[add_name search]'
G.add_edge('qcomsysd','flash_recovery')
G.edge['qcomsysd']['flash_recovery']['write-read'] = '[add_name search][remove_name search]'
G.add_edge('qcomsysd','init_shell')
G.edge['qcomsysd']['init_shell']['write-read'] = '[add_name search]'
G.add_edge('qcomsysd','init_shell')
G.edge['qcomsysd']['init_shell']['write-read'] = '[add_name search][remove_name search]'
G.add_edge('qcomsysd','ks')
G.edge['qcomsysd']['ks']['write-read'] = '[add_name search]'
G.add_edge('qcomsysd','prepare_param')
G.edge['qcomsysd']['prepare_param']['write-read'] = '[add_name search]'
G.add_edge('qcomsysd','prepare_param')
G.edge['qcomsysd']['prepare_param']['write-read'] = '[add_name search][remove_name search]'
G.add_edge('qcomsysd','qseecomd')
G.edge['qcomsysd']['qseecomd']['write-read'] = '[add_name search]'
G.add_edge('qcomsysd','qseecomd')
G.edge['qcomsysd']['qseecomd']['write-read'] = '[add_name search][remove_name search]'
G.add_edge('qcomsysd','vold')
G.edge['qcomsysd']['vold']['write-read'] = '[add_name search]'
G.add_edge('qcomsysd','vold')
G.edge['qcomsysd']['vold']['write-read'] = '[add_name search][remove_name search]'
G.add_edge('qseecomd','efsks')
G.edge['qseecomd']['efsks']['write-read'] = '[open open]'
G.add_edge('qseecomd','flash_recovery')
G.edge['qseecomd']['flash_recovery']['write-read'] = '[open open]'
G.add_edge('qseecomd','init_shell')
G.edge['qseecomd']['init_shell']['write-read'] = '[open open]'
G.add_edge('qseecomd','ks')
G.edge['qseecomd']['ks']['write-read'] = '[open open]'
G.add_edge('qseecomd','prepare_param')
G.edge['qseecomd']['prepare_param']['write-read'] = '[open open]'
G.add_edge('qseecomd','qseecomd')
G.edge['qseecomd']['qseecomd']['write-read'] = '[open open]'
G.add_edge('qseecomd','vold')
G.edge['qseecomd']['vold']['write-read'] = '[open open]'
G.add_edge('qseecomd','prepare_param')
G.edge['qseecomd']['prepare_param']['write-read'] = '[open open][setattr getattr]'
G.add_edge('qseecomd','vold')
G.edge['qseecomd']['vold']['write-read'] = '[open open][setattr getattr]'
G.add_edge('qseecomd','efsks')
G.edge['qseecomd']['efsks']['write-read'] = '[open open][write read]'
G.edge['qseecomd']['efsks']['fill'] = 'red'
G.add_edge('qseecomd','flash_recovery')
G.edge['qseecomd']['flash_recovery']['write-read'] = '[open open][write read]'
G.edge['qseecomd']['flash_recovery']['fill'] = 'red'
G.add_edge('qseecomd','init_shell')
G.edge['qseecomd']['init_shell']['write-read'] = '[open open][write read]'
G.edge['qseecomd']['init_shell']['fill'] = 'red'
G.add_edge('qseecomd','ks')
G.edge['qseecomd']['ks']['write-read'] = '[open open][write read]'
G.edge['qseecomd']['ks']['fill'] = 'red'
G.add_edge('qseecomd','mdm_helper')
G.edge['qseecomd']['mdm_helper']['write-read'] = '[write read]'
G.edge['qseecomd']['mdm_helper']['fill'] = 'red'
G.add_edge('qseecomd','prepare_param')
G.edge['qseecomd']['prepare_param']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['qseecomd']['prepare_param']['fill'] = 'red'
G.add_edge('qseecomd','qseecomd')
G.edge['qseecomd']['qseecomd']['write-read'] = '[open open][write read]'
G.edge['qseecomd']['qseecomd']['fill'] = 'red'
G.add_edge('qseecomd','vold')
G.edge['qseecomd']['vold']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['qseecomd']['vold']['fill'] = 'red'
G.add_edge('qseecomd','efsks')
G.edge['qseecomd']['efsks']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('qseecomd','flash_recovery')
G.edge['qseecomd']['flash_recovery']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('qseecomd','flash_recovery')
G.edge['qseecomd']['flash_recovery']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('qseecomd','init_shell')
G.edge['qseecomd']['init_shell']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('qseecomd','init_shell')
G.edge['qseecomd']['init_shell']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('qseecomd','ks')
G.edge['qseecomd']['ks']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('qseecomd','prepare_param')
G.edge['qseecomd']['prepare_param']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('qseecomd','prepare_param')
G.edge['qseecomd']['prepare_param']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('qseecomd','qseecomd')
G.edge['qseecomd']['qseecomd']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('qseecomd','qseecomd')
G.edge['qseecomd']['qseecomd']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('qseecomd','vold')
G.edge['qseecomd']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('qseecomd','vold')
G.edge['qseecomd']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('rild','efsks')
G.edge['rild']['efsks']['write-read'] = '[open open]'
G.add_edge('rild','flash_recovery')
G.edge['rild']['flash_recovery']['write-read'] = '[open open]'
G.add_edge('rild','init_shell')
G.edge['rild']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('rild','ks')
G.edge['rild']['ks']['write-read'] = '[open open]'
G.add_edge('rild','prepare_param')
G.edge['rild']['prepare_param']['write-read'] = '[open open]'
G.add_edge('rild','qseecomd')
G.edge['rild']['qseecomd']['write-read'] = '[open open]'
G.add_edge('rild','vold')
G.edge['rild']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open]'
G.add_edge('rild','prepare_param')
G.edge['rild']['prepare_param']['write-read'] = '[open open][setattr getattr]'
G.add_edge('rild','vold')
G.edge['rild']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr]'
G.add_edge('rild','efsks')
G.edge['rild']['efsks']['write-read'] = '[open open][write read]'
G.edge['rild']['efsks']['fill'] = 'red'
G.add_edge('rild','flash_recovery')
G.edge['rild']['flash_recovery']['write-read'] = '[open open][write read]'
G.edge['rild']['flash_recovery']['fill'] = 'red'
G.add_edge('rild','init_shell')
G.edge['rild']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['rild']['init_shell']['fill'] = 'red'
G.add_edge('rild','ks')
G.edge['rild']['ks']['write-read'] = '[open open][write read]'
G.edge['rild']['ks']['fill'] = 'red'
G.add_edge('rild','mdm_helper')
G.edge['rild']['mdm_helper']['write-read'] = '[write read]'
G.edge['rild']['mdm_helper']['fill'] = 'red'
G.add_edge('rild','prepare_param')
G.edge['rild']['prepare_param']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['rild']['prepare_param']['fill'] = 'red'
G.add_edge('rild','qseecomd')
G.edge['rild']['qseecomd']['write-read'] = '[open open][write read]'
G.edge['rild']['qseecomd']['fill'] = 'red'
G.add_edge('rild','vold')
G.edge['rild']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read]'
G.edge['rild']['vold']['fill'] = 'red'
G.add_edge('rild','efsks')
G.edge['rild']['efsks']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('rild','flash_recovery')
G.edge['rild']['flash_recovery']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('rild','flash_recovery')
G.edge['rild']['flash_recovery']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('rild','init_shell')
G.edge['rild']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('rild','init_shell')
G.edge['rild']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search]'
G.add_edge('rild','ks')
G.edge['rild']['ks']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('rild','prepare_param')
G.edge['rild']['prepare_param']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('rild','prepare_param')
G.edge['rild']['prepare_param']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('rild','qseecomd')
G.edge['rild']['qseecomd']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('rild','qseecomd')
G.edge['rild']['qseecomd']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('rild','vold')
G.edge['rild']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('rild','vold')
G.edge['rild']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('rmt_storage','efsks')
G.edge['rmt_storage']['efsks']['write-read'] = '[open open]'
G.add_edge('rmt_storage','flash_recovery')
G.edge['rmt_storage']['flash_recovery']['write-read'] = '[open open]'
G.add_edge('rmt_storage','init_shell')
G.edge['rmt_storage']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('rmt_storage','ks')
G.edge['rmt_storage']['ks']['write-read'] = '[open open]'
G.add_edge('rmt_storage','prepare_param')
G.edge['rmt_storage']['prepare_param']['write-read'] = '[open open]'
G.add_edge('rmt_storage','qseecomd')
G.edge['rmt_storage']['qseecomd']['write-read'] = '[open open]'
G.add_edge('rmt_storage','vold')
G.edge['rmt_storage']['vold']['write-read'] = '[open open]'
G.add_edge('rmt_storage','prepare_param')
G.edge['rmt_storage']['prepare_param']['write-read'] = '[open open][setattr getattr]'
G.add_edge('rmt_storage','vold')
G.edge['rmt_storage']['vold']['write-read'] = '[open open][setattr getattr]'
G.add_edge('rmt_storage','efsks')
G.edge['rmt_storage']['efsks']['write-read'] = '[open open][write read]'
G.edge['rmt_storage']['efsks']['fill'] = 'red'
G.add_edge('rmt_storage','flash_recovery')
G.edge['rmt_storage']['flash_recovery']['write-read'] = '[open open][write read]'
G.edge['rmt_storage']['flash_recovery']['fill'] = 'red'
G.add_edge('rmt_storage','init_shell')
G.edge['rmt_storage']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['rmt_storage']['init_shell']['fill'] = 'red'
G.add_edge('rmt_storage','ks')
G.edge['rmt_storage']['ks']['write-read'] = '[open open][write read]'
G.edge['rmt_storage']['ks']['fill'] = 'red'
G.add_edge('rmt_storage','mdm_helper')
G.edge['rmt_storage']['mdm_helper']['write-read'] = '[write read]'
G.edge['rmt_storage']['mdm_helper']['fill'] = 'red'
G.add_edge('rmt_storage','prepare_param')
G.edge['rmt_storage']['prepare_param']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['rmt_storage']['prepare_param']['fill'] = 'red'
G.add_edge('rmt_storage','qseecomd')
G.edge['rmt_storage']['qseecomd']['write-read'] = '[open open][write read]'
G.edge['rmt_storage']['qseecomd']['fill'] = 'red'
G.add_edge('rmt_storage','vold')
G.edge['rmt_storage']['vold']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['rmt_storage']['vold']['fill'] = 'red'
G.add_edge('rmt_storage','efsks')
G.edge['rmt_storage']['efsks']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('rmt_storage','flash_recovery')
G.edge['rmt_storage']['flash_recovery']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('rmt_storage','flash_recovery')
G.edge['rmt_storage']['flash_recovery']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('rmt_storage','init_shell')
G.edge['rmt_storage']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search]'
G.add_edge('rmt_storage','init_shell')
G.edge['rmt_storage']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search]'
G.add_edge('rmt_storage','ks')
G.edge['rmt_storage']['ks']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('rmt_storage','prepare_param')
G.edge['rmt_storage']['prepare_param']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('rmt_storage','prepare_param')
G.edge['rmt_storage']['prepare_param']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('rmt_storage','qseecomd')
G.edge['rmt_storage']['qseecomd']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('rmt_storage','qseecomd')
G.edge['rmt_storage']['qseecomd']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('rmt_storage','vold')
G.edge['rmt_storage']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('rmt_storage','vold')
G.edge['rmt_storage']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('rtcc','efsks')
G.edge['rtcc']['efsks']['write-read'] = '[open open]'
G.add_edge('rtcc','flash_recovery')
G.edge['rtcc']['flash_recovery']['write-read'] = '[open open]'
G.add_edge('rtcc','init_shell')
G.edge['rtcc']['init_shell']['write-read'] = '[open open]'
G.add_edge('rtcc','ks')
G.edge['rtcc']['ks']['write-read'] = '[open open]'
G.add_edge('rtcc','prepare_param')
G.edge['rtcc']['prepare_param']['write-read'] = '[open open]'
G.add_edge('rtcc','qseecomd')
G.edge['rtcc']['qseecomd']['write-read'] = '[open open]'
G.add_edge('rtcc','vold')
G.edge['rtcc']['vold']['write-read'] = '[open open]'
G.add_edge('rtcc','prepare_param')
G.edge['rtcc']['prepare_param']['write-read'] = '[open open][setattr getattr]'
G.add_edge('rtcc','vold')
G.edge['rtcc']['vold']['write-read'] = '[open open][setattr getattr]'
G.add_edge('rtcc','efsks')
G.edge['rtcc']['efsks']['write-read'] = '[open open][write read]'
G.edge['rtcc']['efsks']['fill'] = 'red'
G.add_edge('rtcc','flash_recovery')
G.edge['rtcc']['flash_recovery']['write-read'] = '[open open][write read]'
G.edge['rtcc']['flash_recovery']['fill'] = 'red'
G.add_edge('rtcc','init_shell')
G.edge['rtcc']['init_shell']['write-read'] = '[open open][write read]'
G.edge['rtcc']['init_shell']['fill'] = 'red'
G.add_edge('rtcc','ks')
G.edge['rtcc']['ks']['write-read'] = '[open open][write read]'
G.edge['rtcc']['ks']['fill'] = 'red'
G.add_edge('rtcc','mdm_helper')
G.edge['rtcc']['mdm_helper']['write-read'] = '[write read]'
G.edge['rtcc']['mdm_helper']['fill'] = 'red'
G.add_edge('rtcc','prepare_param')
G.edge['rtcc']['prepare_param']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['rtcc']['prepare_param']['fill'] = 'red'
G.add_edge('rtcc','qseecomd')
G.edge['rtcc']['qseecomd']['write-read'] = '[open open][write read]'
G.edge['rtcc']['qseecomd']['fill'] = 'red'
G.add_edge('rtcc','vold')
G.edge['rtcc']['vold']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['rtcc']['vold']['fill'] = 'red'
G.add_edge('rtcc','efsks')
G.edge['rtcc']['efsks']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('rtcc','flash_recovery')
G.edge['rtcc']['flash_recovery']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('rtcc','flash_recovery')
G.edge['rtcc']['flash_recovery']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('rtcc','init_shell')
G.edge['rtcc']['init_shell']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('rtcc','init_shell')
G.edge['rtcc']['init_shell']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('rtcc','ks')
G.edge['rtcc']['ks']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('rtcc','prepare_param')
G.edge['rtcc']['prepare_param']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('rtcc','prepare_param')
G.edge['rtcc']['prepare_param']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('rtcc','qseecomd')
G.edge['rtcc']['qseecomd']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('rtcc','qseecomd')
G.edge['rtcc']['qseecomd']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('rtcc','vold')
G.edge['rtcc']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('rtcc','vold')
G.edge['rtcc']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('sswap','efsks')
G.edge['sswap']['efsks']['write-read'] = '[open open]'
G.add_edge('sswap','flash_recovery')
G.edge['sswap']['flash_recovery']['write-read'] = '[open open]'
G.add_edge('sswap','init_shell')
G.edge['sswap']['init_shell']['write-read'] = '[open open]'
G.add_edge('sswap','ks')
G.edge['sswap']['ks']['write-read'] = '[open open]'
G.add_edge('sswap','prepare_param')
G.edge['sswap']['prepare_param']['write-read'] = '[open open]'
G.add_edge('sswap','qseecomd')
G.edge['sswap']['qseecomd']['write-read'] = '[open open]'
G.add_edge('sswap','vold')
G.edge['sswap']['vold']['write-read'] = '[open open]'
G.add_edge('sswap','prepare_param')
G.edge['sswap']['prepare_param']['write-read'] = '[open open][setattr getattr]'
G.add_edge('sswap','vold')
G.edge['sswap']['vold']['write-read'] = '[open open][setattr getattr]'
G.add_edge('sswap','efsks')
G.edge['sswap']['efsks']['write-read'] = '[open open][write read]'
G.edge['sswap']['efsks']['fill'] = 'red'
G.add_edge('sswap','flash_recovery')
G.edge['sswap']['flash_recovery']['write-read'] = '[open open][write read]'
G.edge['sswap']['flash_recovery']['fill'] = 'red'
G.add_edge('sswap','init_shell')
G.edge['sswap']['init_shell']['write-read'] = '[open open][write read]'
G.edge['sswap']['init_shell']['fill'] = 'red'
G.add_edge('sswap','ks')
G.edge['sswap']['ks']['write-read'] = '[open open][write read]'
G.edge['sswap']['ks']['fill'] = 'red'
G.add_edge('sswap','mdm_helper')
G.edge['sswap']['mdm_helper']['write-read'] = '[write read]'
G.edge['sswap']['mdm_helper']['fill'] = 'red'
G.add_edge('sswap','prepare_param')
G.edge['sswap']['prepare_param']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['sswap']['prepare_param']['fill'] = 'red'
G.add_edge('sswap','qseecomd')
G.edge['sswap']['qseecomd']['write-read'] = '[open open][write read]'
G.edge['sswap']['qseecomd']['fill'] = 'red'
G.add_edge('sswap','vold')
G.edge['sswap']['vold']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['sswap']['vold']['fill'] = 'red'
G.add_edge('sswap','efsks')
G.edge['sswap']['efsks']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('sswap','flash_recovery')
G.edge['sswap']['flash_recovery']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('sswap','flash_recovery')
G.edge['sswap']['flash_recovery']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('sswap','init_shell')
G.edge['sswap']['init_shell']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('sswap','init_shell')
G.edge['sswap']['init_shell']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('sswap','ks')
G.edge['sswap']['ks']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('sswap','prepare_param')
G.edge['sswap']['prepare_param']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('sswap','prepare_param')
G.edge['sswap']['prepare_param']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('sswap','qseecomd')
G.edge['sswap']['qseecomd']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('sswap','qseecomd')
G.edge['sswap']['qseecomd']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('sswap','vold')
G.edge['sswap']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('sswap','vold')
G.edge['sswap']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('syscope_app','efsks')
G.edge['syscope_app']['efsks']['write-read'] = '[open open]'
G.add_edge('syscope_app','flash_recovery')
G.edge['syscope_app']['flash_recovery']['write-read'] = '[open open]'
G.add_edge('syscope_app','init_shell')
G.edge['syscope_app']['init_shell']['write-read'] = '[open open]'
G.add_edge('syscope_app','ks')
G.edge['syscope_app']['ks']['write-read'] = '[open open]'
G.add_edge('syscope_app','prepare_param')
G.edge['syscope_app']['prepare_param']['write-read'] = '[open open]'
G.add_edge('syscope_app','qseecomd')
G.edge['syscope_app']['qseecomd']['write-read'] = '[open open]'
G.add_edge('syscope_app','vold')
G.edge['syscope_app']['vold']['write-read'] = '[open open]'
G.add_edge('syscope_app','prepare_param')
G.edge['syscope_app']['prepare_param']['write-read'] = '[open open][setattr getattr]'
G.add_edge('syscope_app','vold')
G.edge['syscope_app']['vold']['write-read'] = '[open open][setattr getattr]'
G.add_edge('syscope_app','efsks')
G.edge['syscope_app']['efsks']['write-read'] = '[open open][write read]'
G.edge['syscope_app']['efsks']['fill'] = 'red'
G.add_edge('syscope_app','flash_recovery')
G.edge['syscope_app']['flash_recovery']['write-read'] = '[open open][write read]'
G.edge['syscope_app']['flash_recovery']['fill'] = 'red'
G.add_edge('syscope_app','init_shell')
G.edge['syscope_app']['init_shell']['write-read'] = '[open open][write read]'
G.edge['syscope_app']['init_shell']['fill'] = 'red'
G.add_edge('syscope_app','ks')
G.edge['syscope_app']['ks']['write-read'] = '[open open][write read]'
G.edge['syscope_app']['ks']['fill'] = 'red'
G.add_edge('syscope_app','mdm_helper')
G.edge['syscope_app']['mdm_helper']['write-read'] = '[write read]'
G.edge['syscope_app']['mdm_helper']['fill'] = 'red'
G.add_edge('syscope_app','prepare_param')
G.edge['syscope_app']['prepare_param']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['syscope_app']['prepare_param']['fill'] = 'red'
G.add_edge('syscope_app','qseecomd')
G.edge['syscope_app']['qseecomd']['write-read'] = '[open open][write read]'
G.edge['syscope_app']['qseecomd']['fill'] = 'red'
G.add_edge('syscope_app','vold')
G.edge['syscope_app']['vold']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['syscope_app']['vold']['fill'] = 'red'
G.add_edge('syscope_app','efsks')
G.edge['syscope_app']['efsks']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('syscope_app','flash_recovery')
G.edge['syscope_app']['flash_recovery']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('syscope_app','flash_recovery')
G.edge['syscope_app']['flash_recovery']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('syscope_app','init_shell')
G.edge['syscope_app']['init_shell']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('syscope_app','init_shell')
G.edge['syscope_app']['init_shell']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('syscope_app','ks')
G.edge['syscope_app']['ks']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('syscope_app','prepare_param')
G.edge['syscope_app']['prepare_param']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('syscope_app','prepare_param')
G.edge['syscope_app']['prepare_param']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('syscope_app','qseecomd')
G.edge['syscope_app']['qseecomd']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('syscope_app','qseecomd')
G.edge['syscope_app']['qseecomd']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('syscope_app','vold')
G.edge['syscope_app']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('syscope_app','vold')
G.edge['syscope_app']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('system_server','efsks')
G.edge['system_server']['efsks']['write-read'] = '[add_name search]'
G.add_edge('system_server','flash_recovery')
G.edge['system_server']['flash_recovery']['write-read'] = '[add_name search]'
G.add_edge('system_server','flash_recovery')
G.edge['system_server']['flash_recovery']['write-read'] = '[add_name search][remove_name search]'
G.add_edge('system_server','init_shell')
G.edge['system_server']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][add_name search]'
G.add_edge('system_server','init_shell')
G.edge['system_server']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('system_server','ks')
G.edge['system_server']['ks']['write-read'] = '[add_name search]'
G.add_edge('system_server','prepare_param')
G.edge['system_server']['prepare_param']['write-read'] = '[add_name search]'
G.add_edge('system_server','prepare_param')
G.edge['system_server']['prepare_param']['write-read'] = '[add_name search][remove_name search]'
G.add_edge('system_server','qseecomd')
G.edge['system_server']['qseecomd']['write-read'] = '[add_name search]'
G.add_edge('system_server','qseecomd')
G.edge['system_server']['qseecomd']['write-read'] = '[add_name search][remove_name search]'
G.add_edge('system_server','vold')
G.edge['system_server']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][add_name search]'
G.add_edge('system_server','vold')
G.edge['system_server']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][add_name search][remove_name search]'
G.add_edge('tee','efsks')
G.edge['tee']['efsks']['write-read'] = '[open open]'
G.add_edge('tee','flash_recovery')
G.edge['tee']['flash_recovery']['write-read'] = '[open open]'
G.add_edge('tee','init_shell')
G.edge['tee']['init_shell']['write-read'] = '[open open]'
G.add_edge('tee','ks')
G.edge['tee']['ks']['write-read'] = '[open open]'
G.add_edge('tee','prepare_param')
G.edge['tee']['prepare_param']['write-read'] = '[open open]'
G.add_edge('tee','qseecomd')
G.edge['tee']['qseecomd']['write-read'] = '[open open]'
G.add_edge('tee','vold')
G.edge['tee']['vold']['write-read'] = '[open open]'
G.add_edge('tee','prepare_param')
G.edge['tee']['prepare_param']['write-read'] = '[open open][setattr getattr]'
G.add_edge('tee','vold')
G.edge['tee']['vold']['write-read'] = '[open open][setattr getattr]'
G.add_edge('tee','efsks')
G.edge['tee']['efsks']['write-read'] = '[open open][write read]'
G.edge['tee']['efsks']['fill'] = 'red'
G.add_edge('tee','flash_recovery')
G.edge['tee']['flash_recovery']['write-read'] = '[open open][write read]'
G.edge['tee']['flash_recovery']['fill'] = 'red'
G.add_edge('tee','init_shell')
G.edge['tee']['init_shell']['write-read'] = '[open open][write read]'
G.edge['tee']['init_shell']['fill'] = 'red'
G.add_edge('tee','ks')
G.edge['tee']['ks']['write-read'] = '[open open][write read]'
G.edge['tee']['ks']['fill'] = 'red'
G.add_edge('tee','mdm_helper')
G.edge['tee']['mdm_helper']['write-read'] = '[write read]'
G.edge['tee']['mdm_helper']['fill'] = 'red'
G.add_edge('tee','prepare_param')
G.edge['tee']['prepare_param']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['tee']['prepare_param']['fill'] = 'red'
G.add_edge('tee','qseecomd')
G.edge['tee']['qseecomd']['write-read'] = '[open open][write read]'
G.edge['tee']['qseecomd']['fill'] = 'red'
G.add_edge('tee','vold')
G.edge['tee']['vold']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['tee']['vold']['fill'] = 'red'
G.add_edge('tee','efsks')
G.edge['tee']['efsks']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('tee','flash_recovery')
G.edge['tee']['flash_recovery']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('tee','flash_recovery')
G.edge['tee']['flash_recovery']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('tee','init_shell')
G.edge['tee']['init_shell']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('tee','init_shell')
G.edge['tee']['init_shell']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('tee','ks')
G.edge['tee']['ks']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('tee','prepare_param')
G.edge['tee']['prepare_param']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('tee','prepare_param')
G.edge['tee']['prepare_param']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('tee','qseecomd')
G.edge['tee']['qseecomd']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('tee','qseecomd')
G.edge['tee']['qseecomd']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('tee','vold')
G.edge['tee']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('tee','vold')
G.edge['tee']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('uncrypt','efsks')
G.edge['uncrypt']['efsks']['write-read'] = '[open open]'
G.add_edge('uncrypt','flash_recovery')
G.edge['uncrypt']['flash_recovery']['write-read'] = '[open open]'
G.add_edge('uncrypt','init_shell')
G.edge['uncrypt']['init_shell']['write-read'] = '[open open]'
G.add_edge('uncrypt','ks')
G.edge['uncrypt']['ks']['write-read'] = '[open open]'
G.add_edge('uncrypt','prepare_param')
G.edge['uncrypt']['prepare_param']['write-read'] = '[open open]'
G.add_edge('uncrypt','qseecomd')
G.edge['uncrypt']['qseecomd']['write-read'] = '[open open]'
G.add_edge('uncrypt','vold')
G.edge['uncrypt']['vold']['write-read'] = '[open open]'
G.add_edge('uncrypt','prepare_param')
G.edge['uncrypt']['prepare_param']['write-read'] = '[open open][setattr getattr]'
G.add_edge('uncrypt','vold')
G.edge['uncrypt']['vold']['write-read'] = '[open open][setattr getattr]'
G.add_edge('uncrypt','efsks')
G.edge['uncrypt']['efsks']['write-read'] = '[open open][write read]'
G.edge['uncrypt']['efsks']['fill'] = 'red'
G.add_edge('uncrypt','flash_recovery')
G.edge['uncrypt']['flash_recovery']['write-read'] = '[open open][write read]'
G.edge['uncrypt']['flash_recovery']['fill'] = 'red'
G.add_edge('uncrypt','init_shell')
G.edge['uncrypt']['init_shell']['write-read'] = '[open open][write read]'
G.edge['uncrypt']['init_shell']['fill'] = 'red'
G.add_edge('uncrypt','ks')
G.edge['uncrypt']['ks']['write-read'] = '[open open][write read]'
G.edge['uncrypt']['ks']['fill'] = 'red'
G.add_edge('uncrypt','mdm_helper')
G.edge['uncrypt']['mdm_helper']['write-read'] = '[write read]'
G.edge['uncrypt']['mdm_helper']['fill'] = 'red'
G.add_edge('uncrypt','prepare_param')
G.edge['uncrypt']['prepare_param']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['uncrypt']['prepare_param']['fill'] = 'red'
G.add_edge('uncrypt','qseecomd')
G.edge['uncrypt']['qseecomd']['write-read'] = '[open open][write read]'
G.edge['uncrypt']['qseecomd']['fill'] = 'red'
G.add_edge('uncrypt','vold')
G.edge['uncrypt']['vold']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['uncrypt']['vold']['fill'] = 'red'
G.add_edge('uncrypt','efsks')
G.edge['uncrypt']['efsks']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('uncrypt','flash_recovery')
G.edge['uncrypt']['flash_recovery']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('uncrypt','flash_recovery')
G.edge['uncrypt']['flash_recovery']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('uncrypt','init_shell')
G.edge['uncrypt']['init_shell']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('uncrypt','init_shell')
G.edge['uncrypt']['init_shell']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('uncrypt','ks')
G.edge['uncrypt']['ks']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('uncrypt','prepare_param')
G.edge['uncrypt']['prepare_param']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('uncrypt','prepare_param')
G.edge['uncrypt']['prepare_param']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('uncrypt','qseecomd')
G.edge['uncrypt']['qseecomd']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('uncrypt','qseecomd')
G.edge['uncrypt']['qseecomd']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('uncrypt','vold')
G.edge['uncrypt']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('uncrypt','vold')
G.edge['uncrypt']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('undefined_service','efsks')
G.edge['undefined_service']['efsks']['write-read'] = '[open open]'
G.add_edge('undefined_service','flash_recovery')
G.edge['undefined_service']['flash_recovery']['write-read'] = '[open open]'
G.add_edge('undefined_service','init_shell')
G.edge['undefined_service']['init_shell']['write-read'] = '[open open]'
G.add_edge('undefined_service','ks')
G.edge['undefined_service']['ks']['write-read'] = '[open open]'
G.add_edge('undefined_service','prepare_param')
G.edge['undefined_service']['prepare_param']['write-read'] = '[open open]'
G.add_edge('undefined_service','qseecomd')
G.edge['undefined_service']['qseecomd']['write-read'] = '[open open]'
G.add_edge('undefined_service','vold')
G.edge['undefined_service']['vold']['write-read'] = '[open open]'
G.add_edge('undefined_service','prepare_param')
G.edge['undefined_service']['prepare_param']['write-read'] = '[open open][setattr getattr]'
G.add_edge('undefined_service','vold')
G.edge['undefined_service']['vold']['write-read'] = '[open open][setattr getattr]'
G.add_edge('undefined_service','efsks')
G.edge['undefined_service']['efsks']['write-read'] = '[open open][write read]'
G.edge['undefined_service']['efsks']['fill'] = 'red'
G.add_edge('undefined_service','flash_recovery')
G.edge['undefined_service']['flash_recovery']['write-read'] = '[open open][write read]'
G.edge['undefined_service']['flash_recovery']['fill'] = 'red'
G.add_edge('undefined_service','init_shell')
G.edge['undefined_service']['init_shell']['write-read'] = '[open open][write read]'
G.edge['undefined_service']['init_shell']['fill'] = 'red'
G.add_edge('undefined_service','ks')
G.edge['undefined_service']['ks']['write-read'] = '[open open][write read]'
G.edge['undefined_service']['ks']['fill'] = 'red'
G.add_edge('undefined_service','mdm_helper')
G.edge['undefined_service']['mdm_helper']['write-read'] = '[write read]'
G.edge['undefined_service']['mdm_helper']['fill'] = 'red'
G.add_edge('undefined_service','prepare_param')
G.edge['undefined_service']['prepare_param']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['undefined_service']['prepare_param']['fill'] = 'red'
G.add_edge('undefined_service','qseecomd')
G.edge['undefined_service']['qseecomd']['write-read'] = '[open open][write read]'
G.edge['undefined_service']['qseecomd']['fill'] = 'red'
G.add_edge('undefined_service','vold')
G.edge['undefined_service']['vold']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['undefined_service']['vold']['fill'] = 'red'
G.add_edge('undefined_service','efsks')
G.edge['undefined_service']['efsks']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('undefined_service','flash_recovery')
G.edge['undefined_service']['flash_recovery']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('undefined_service','flash_recovery')
G.edge['undefined_service']['flash_recovery']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('undefined_service','init_shell')
G.edge['undefined_service']['init_shell']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('undefined_service','init_shell')
G.edge['undefined_service']['init_shell']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('undefined_service','ks')
G.edge['undefined_service']['ks']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('undefined_service','prepare_param')
G.edge['undefined_service']['prepare_param']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('undefined_service','prepare_param')
G.edge['undefined_service']['prepare_param']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('undefined_service','qseecomd')
G.edge['undefined_service']['qseecomd']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('undefined_service','qseecomd')
G.edge['undefined_service']['qseecomd']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('undefined_service','vold')
G.edge['undefined_service']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('undefined_service','vold')
G.edge['undefined_service']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('vold','efsks')
G.edge['vold']['efsks']['write-read'] = '[open open]'
G.add_edge('vold','flash_recovery')
G.edge['vold']['flash_recovery']['write-read'] = '[open open]'
G.add_edge('vold','init_shell')
G.edge['vold']['init_shell']['write-read'] = '[open open][open open]'
G.add_edge('vold','ks')
G.edge['vold']['ks']['write-read'] = '[open open]'
G.add_edge('vold','prepare_param')
G.edge['vold']['prepare_param']['write-read'] = '[open open]'
G.add_edge('vold','qseecomd')
G.edge['vold']['qseecomd']['write-read'] = '[open open]'
G.add_edge('vold','vold')
G.edge['vold']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open]'
G.add_edge('vold','prepare_param')
G.edge['vold']['prepare_param']['write-read'] = '[open open][setattr getattr]'
G.add_edge('vold','vold')
G.edge['vold']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr]'
G.add_edge('vold','efsks')
G.edge['vold']['efsks']['write-read'] = '[open open][write read]'
G.edge['vold']['efsks']['fill'] = 'red'
G.add_edge('vold','flash_recovery')
G.edge['vold']['flash_recovery']['write-read'] = '[open open][write read]'
G.edge['vold']['flash_recovery']['fill'] = 'red'
G.add_edge('vold','init_shell')
G.edge['vold']['init_shell']['write-read'] = '[open open][open open][write read]'
G.edge['vold']['init_shell']['fill'] = 'red'
G.add_edge('vold','ks')
G.edge['vold']['ks']['write-read'] = '[open open][write read]'
G.edge['vold']['ks']['fill'] = 'red'
G.add_edge('vold','mdm_helper')
G.edge['vold']['mdm_helper']['write-read'] = '[write read]'
G.edge['vold']['mdm_helper']['fill'] = 'red'
G.add_edge('vold','prepare_param')
G.edge['vold']['prepare_param']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['vold']['prepare_param']['fill'] = 'red'
G.add_edge('vold','qseecomd')
G.edge['vold']['qseecomd']['write-read'] = '[open open][write read]'
G.edge['vold']['qseecomd']['fill'] = 'red'
G.add_edge('vold','vold')
G.edge['vold']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['vold']['vold']['fill'] = 'red'
G.add_edge('vold','efsks')
G.edge['vold']['efsks']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('vold','flash_recovery')
G.edge['vold']['flash_recovery']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('vold','flash_recovery')
G.edge['vold']['flash_recovery']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('vold','init_shell')
G.edge['vold']['init_shell']['write-read'] = '[open open][open open][write read][add_name search]'
G.add_edge('vold','init_shell')
G.edge['vold']['init_shell']['write-read'] = '[open open][open open][write read][add_name search][remove_name search]'
G.add_edge('vold','ks')
G.edge['vold']['ks']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('vold','prepare_param')
G.edge['vold']['prepare_param']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('vold','prepare_param')
G.edge['vold']['prepare_param']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('vold','qseecomd')
G.edge['vold']['qseecomd']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('vold','qseecomd')
G.edge['vold']['qseecomd']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('vold','vold')
G.edge['vold']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('vold','vold')
G.edge['vold']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
app = Viewer(G)
app.mainloop()