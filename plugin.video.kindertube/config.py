### ############################################################################################################
###	#	
### # Author: 			#		The Highway
### # Description: 	#		Config File For:  The Binary Highway
###	#	
### ############################################################################################################
### ############################################################################################################
### Imports ###
import xbmc,xbmcplugin,xbmcgui,xbmcaddon,xbmcvfs
import os,sys,string,StringIO,logging,random,array,time,datetime,re
#from t0mm0.common.addon import Addon
#try: 		from t0mm0.common.addon 				import Addon
#except: 
#	try: from c_t0mm0_common_addon 				import Addon
#	except: pass
try: 			from addon.common.addon 				import Addon
except:
	try: 		from t0mm0.common.addon 				import Addon
	except: 
		try: from c_t0mm0_common_addon 				import Addon
		except: pass
### Plugin Settings ###
def ps(x):
	if (x=='_addon_id') or (x=='addon_id') or (x=='_plugin_id') or (x=='plugin_id'): return 'plugin.video.kindertube'
	try: 
		return {
			'__plugin__': 					"KinderTube"
			,'__authors__': 				"KAOSbox"
			,'__credits__': 				""
			,'_domain_url': 				""
		
			,'sep': 								os.sep
			,'special.home': 				'special:'+os.sep+os.sep+'home'
			,'special.home.addons': 'special:'+os.sep+os.sep+'home'+os.sep+'addons'+os.sep
			,'_addon_path_art': 		"art"

			,'default_art_ext': 		'.png'
			,'default_cFL_color': 	'cornflowerblue'
			,'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
			,'filemarker': ''
			,'WhatRFavsCalled': 'Favs: '
		}[x]
	except: return ''







### ############################################################################################################
### ############################################################################################################
