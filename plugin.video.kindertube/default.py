### ############################################################################################################
### #	
### # Site: KinderTube.NL
### # Original Author: The Highway
### # Modified: KAOSbox
### #	
### ############################################################################################################
### ############################################################################################################
### Imports ###
import xbmc
import os,sys,string,StringIO,logging,random,array,time,datetime,re
import urllib,urllib2,xbmcaddon,xbmcplugin,xbmcgui
from common import *
from common import (_addon,_artIcon,_artFanart,_addonPath,RefreshList)
### ############################################################################################################
### ############################################################################################################
SiteName='Kindertube.nl'
SiteTag='kindertube.nl'
mainSite='http://www.kindertube.nl'
mainSite2=''
iconSite=_artIcon #'http://www.kindertube.nl/images/kindertube.gif' #_artIcon
fanartSite=_artFanart
colors={'0':'white','1':'red','2':'blue','3':'green','4':'yellow','5':'orange','6':'lime','7':'','8':'cornflowerblue','9':'blueviolet','10':'hotpink','11':'pink','12':'tan'}
CR='[CR]'
MyAlphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
MyBrowser=['User-Agent','Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3']

workingUrl=mainSite+'ram.pls'
### ############################################################################################################
### ############################################################################################################
site=addpr('site','')
section=addpr('section','')
url=addpr('url','')
sections={'series':'series','movies':'movies'}
thumbnail=addpr('img','')
fanart=addpr('fanart','')
page=addpr('page','')

### ############################################################################################################
### ############################################################################################################
def ListEpisodes(url,title):
	if len(url)==0: return
	if mainSite not in url: url=mainSite+url
	deb('url',url); html=(messupText(nURL(url),True,True)); deb('length of html',str(len(html))); #debob(html)
	#html=spAfterSplit(html,'<ul id="videoList_ul">'); html=spBeforeSplit(html,'</ul>'); 
	if len(html)==0: return
	###
	s='<div style="width:\d+px;display:inline-block;"><a id="([A-Za-z0-9\-_]+)" href="#top"><img src="(http://.+?)"  height="\d+" width="\d+"></a><div style="overflow:hidden;width:\d+px;height:\d+px;text-align:center;color:#[A-Za-z0-9]+;margin:\d+px \d+px;">\s*(.+?)\n*\s*</div></div>'
	matches=re.compile(s).findall(html); 
	deb('# of matches found',str(len(matches))); #debob(matches)
	###
	s='<div style="width:\d+px;display:inline-block;"><a id="([A-Za-z0-9\-_]+)" href="(http://www.kindertube.nl/.+?)"><img src="(http://.+?)"\s+height="\d+" width="\d+"></a><div style="overflow:hidden;width:\d+px;height:\d+px;text-align:center;color:.[A-Za-z0-9]+;margin:\d+px \d+px;">\s*(.+?)\n*\s*</div></div>'
	matches3=re.compile(s).findall(html); 
	deb('# of matches found',str(len(matches3))); #debob(matches2)
	###
	i=len(matches)+len(matches3)
	if len(matches) > 0:
		for IdTag,img,name in matches:
			debob((IdTag,img,name)); 
			#s2 ='.\("a.'+IdTag+'"\).live\("click",function\(\){\n*\s*'; 
			#s2+='.\(".videowrapper"\).html\(\'<iframe width="\d+" height="\d+" src="(http://.+?'+IdTag+'.+?)"\s*[frameborder\=\"\d]*\s*allowfullscreen></iframe>\'\);\n*\s*}\);';
			#s2+='.\(".videowrapper"\).html\(\'<iframe width="\d+" height="\d+" src="(http://.+?)"\s*[frameborder\=\"\d]*\s*allowfullscreen></iframe>\'\);\n*\s*}\);';
			s2 ='.\("a.'+IdTag+'"\)\.live\("click",function\(\){\s*\n*\s*'; 
			s2+='.\("\.videowrapper"\)\.html\(\'<iframe\s+width="\d+"\s+height="\d+"\s+src="(http[^"]+)"[^>]+>\s*</iframe>';
			##mUrl=re.search(s2,html).group(1); 
			try: mUrl=re.compile(s2).findall(html)[0]; 
			except: mUrl=''
			deb('mUrl',mUrl); 
			if 'http://www.youtube.com/embed/' in mUrl: pUrl='plugin://plugin.video.youtube/?action=play_video&videoid='+IdTag; sTag='Youtube'; 
			elif 'http://player.vimeo.com/video/' in mUrl: pUrl='plugin://plugin.video.vimeo/?action=play_video&videoid='+IdTag; sTag='Vimeo'; 
			else: pUrl=''; sTag=''; 
			pars={'mode':'PlayURL','img':img,'url':pUrl,'title':name,'site':site}
			if (len(pUrl)==0) and (len(sTag) > 0): labs={'title':''+cFL(name,'white')+''+'[CR]'+cFL('Fout [Error] ')+IdTag+''}
			elif (len(pUrl)==0): labs={'title':''+cFL(name,'white')+''+'[CR]'+cFL('Fout [Error] ','red')+IdTag+''}
			else: labs={'title':''+cFL(name,'white')}
			try: _addon.add_directory(pars,labs,is_folder=False,fanart=fanartSite,img=img,total_items=i)
			except: pass
	if len(matches3) > 0:
		for IdTag,mUrl,img,name in matches3:
			debob((IdTag,mUrl,img,name)); 
			labs={'title':''+cFL(name,'white')} #+'[CR]'+''+mUrl+''
			pars={'mode':'ListEpisodes','img':img,'url':mUrl,'title':name,'site':site}
			try: _addon.add_directory(pars,labs,is_folder=True,fanart=fanartSite,img=img,total_items=i)
			except: pass
	set_view('episodes',view_mode=addst('episode-view')); eod()

def ListNoCat(url,title):
	if len(url)==0: return
	if mainSite not in url: url=mainSite+url
	deb('url',url); html=(messupText(nURL(url),True,True)); deb('length of html',str(len(html))); #debob(html)
	#html=spAfterSplit(html,'<ul id="videoList_ul">'); html=spBeforeSplit(html,'</ul>'); 
	if len(html)==0: return
	s='{ value: "(http://www.kindertube.nl/(.+?)/.+?.html)", label: "(.+?)" },'
	matches2=re.compile(s).findall(html); 
	deb('# of matches found',str(len(matches2))); debob(matches2)
	if len(matches2) > 0:
		i=len(matches2)
		for mUrl,mFolder,name in matches2:
			debob((mUrl,name)); 
			img=artj('noimage2'); labs={'title':''+cFL(name,'darkorange')} #+'[CR]'+''+mUrl+'' #img=iconSite; 
			try: 
				#if '<a href="'+mUrl+'" style="text-decoration: none"><img src="' in html: print '" style="text-decoration: none"><img src="'
				img=re.compile('<a href="'+mUrl+'" style="text-decoration: none"><img src="(.+?)"').findall(html)[0]; #debob(img); 
				labs={'title':''+cFL(name,'white')}; deb('image found',img); 
			except: pass
			p=mFolder
			if img==artj('noimage2'): img='http://www.kindertube.nl/images/'+p+'-logo.gif'
			pars={'mode':'ListEpisodes','img':img,'url':mUrl,'title':name,'site':site}
			try: _addon.add_directory(pars,labs,is_folder=True,fanart=fanartSite,img=img,total_items=i)
			except: pass
	set_view('episodes',view_mode=addst('episode-view')); eod()

### ############################################################################################################
### ############################################################################################################
def SectionMenu():
	g='white'; c='red';
	#_addon.add_directory({'mode':'ListShows','site':site},{'title':cFL_('Cartoon List',colors['5'])},is_folder=True,fanart=fanartSite,img=iconSite)
	_addon.add_directory({'mode':'ListEpisodes','site':site,'url':mainSite+'/'																				},{'title':cFL(cFL_('Home',c),g)},is_folder=True,fanart=fanartSite,img=artj('home'))
	_addon.add_directory({'mode':'ListEpisodes','site':site,'url':mainSite+'/babyfilmpjes.html'												},{'title':cFL(cFL_('Baby',c),g)},is_folder=True,fanart=fanartSite,img=artj('baby'))
	_addon.add_directory({'mode':'ListEpisodes','site':site,'url':mainSite+'/peuterfilmpjes.html'											},{'title':cFL(cFL_('Peuter',c),g)},is_folder=True,fanart=fanartSite,img=artj('peuter'))
	_addon.add_directory({'mode':'ListEpisodes','site':site,'url':mainSite+'/kleuterfilmpjes.html'										},{'title':cFL(cFL_('Kleuter',c),g)},is_folder=True,fanart=fanartSite,img=artj('kleuter'))
	_addon.add_directory({'mode':'ListEpisodes','site':site,'url':mainSite+'/schoolgaand.html'												},{'title':cFL(cFL_('Schoolgaand',c),g)},is_folder=True,fanart=fanartSite,img=artj('school'))
	_addon.add_directory({'mode':'ListEpisodes','site':site,'url':mainSite+'/tekenfilms-van-vroeger.html'							},{'title':cFL(cFL_('Vroeger',c),g)},is_folder=True,fanart=fanartSite,img=artj('vroeger'))
	_addon.add_directory({'mode':'ListEpisodes','site':site,'url':mainSite+'/muziek-voor-kinderen.html'								},{'title':cFL(cFL_('Muziek',c),g)},is_folder=True,fanart=fanartSite,img=artj('muziek'))
	_addon.add_directory({'mode':'ListEpisodes','site':site,'url':mainSite+'/voorlezen-en-digitale-prentenboeken.html'},{'title':cFL(cFL_('Sprookjes & verhaaltjes',c),g)},is_folder=True,fanart=fanartSite,img=artj('sprookjes'))
	_addon.add_directory({'mode':'ListEpisodes','site':site,'url':mainSite+'/educatieve-filmpjes-voor-kinderen.html'},{'title':cFL(cFL_('Educatief',c),g)},is_folder=True,fanart=fanartSite,img=artj('educatief'))

	_addon.add_directory({'mode':'ListNoCat',   'site':site,'url':mainSite+'/'																				},{'title':cFL(cFL_('Populair',c),g)},is_folder=True,fanart=fanartSite,img=artj('populair'))
	#_addon.add_directory({'mode':'ListEpisodes','site':site,'url':mainSite+''},{'title':cFL_('Cartoon',c)},is_folder=True,fanart=fanartSite,img=iconSite)
	#_addon.add_directory({'mode':'ListEpisodes','site':site,'url':mainSite+''},{'title':cFL_('Cartoon',c)},is_folder=True,fanart=fanartSite,img=iconSite)
	#_addon.add_directory({'mode':'ListEpisodes','site':site,'url':mainSite+''},{'title':cFL_('Cartoon',c)},is_folder=True,fanart=fanartSite,img=iconSite)
	#_addon.add_directory({'mode':'ListEpisodes','site':site,'url':mainSite+''},{'title':cFL_('Cartoon',c)},is_folder=True,fanart=fanartSite,img=iconSite)
	###
	set_view('list',view_mode=addst('default-view')); eod()
### ############################################################################################################
### ############################################################################################################
def mode_subcheck(mode='',site='',section='',url=''):
	if (mode=='') or (mode=='main') or (mode=='MainMenu') or (mode=='SectionMenu'): 		SectionMenu()
	elif (mode=='PlayURL'): 			PlayURL(url)
	elif (mode=='SubMenu'): 			SubMenu()
	elif (mode=='NowPlaying'): 		NowPlaying()
	elif (mode=='ListAZ'): 				ListAZ()
	elif (mode=='List'): 					Browse_List(addpr('title',''))
	elif (mode=='DoRequest'): 		DoRequest(url,addpr('title',''))
	elif (mode=='ListShows'): 		ListShows()
	elif (mode=='ListEpisodes'): 	ListEpisodes(url,addpr('title',''))
	elif (mode=='ListNoCat'): 		ListNoCat(url,addpr('title',''))
	elif (mode=='GetMedia'): 			GetMedia(addpr('videoid',''),addpr('title',''),url,addpr('img',''))
	#elif (mode=='Hosts'): 				Browse_Hosts(url)
	#elif (mode=='Search'): 				Search_Site(title=addpr('title',''),url=url,page=page,metamethod=addpr('metamethod','')) #(site,section)
	#elif (mode=='SearchLast'): 		Search_Site(title=addst('LastSearchTitle'+SiteTag),url=url,page=page,metamethod=addpr('metamethod',''),endit=tfalse(addpr('endit','true'))) #(site,section)
	elif (mode=='About'): 				About()
	#elif (mode=='FavoritesList'): Fav_List(site=site,section=section,subfav=addpr('subfav',''))
	elif (mode=='SlideShowStart'): path = os.path.join(_addonPath, 'c_SlideShow.py'); xbmc.executebuiltin('XBMC.RunScript(%s)' % path)
	else: myNote(header='Site:  "'+site+'"',msg=mode+' (mode) not found.'); import mMain
mode_subcheck(addpr('mode',''),addpr('site',''),addpr('section',''),addpr('url',''))