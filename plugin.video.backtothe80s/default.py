# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Back to the 80s
# (c) 2015 - KAOSbox
# Based on code from youtube addon
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.backtothe80s'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')


channellist=[

	("[COLOR blue]Music >>[/COLOR] Nederlandstalig Jaren 80", "playlist/PLIj84zT8vo2kHrHGkRXbDBgG--rZGZKVk/", "http://i.imgur.com/GIR8L8V.png"),
	("[COLOR blue]Music >>[/COLOR] Jaren 80 nummer 1 hits", "playlist/PLFdjwk0_rPKpBvycOv1SP7qPLR7Tmigvx/", "http://i.imgur.com/GIR8L8V.png"),
	("[COLOR blue]Music >>[/COLOR] 80s Playlist", "playlist/PLL55rJswZPUY6pNadCpeBlZaivnbA42PM/", "http://i.imgur.com/GIR8L8V.png"),
	("[COLOR blue]Music >>[/COLOR] VH1's 100 Greatest Songs of the 80s", "playlist/PLCF2B29B9312CE35D/", "http://i.imgur.com/GIR8L8V.png"),

	("[COLOR red]TV >>[/COLOR] TV jaren 80", "playlist/PLAF48B7774AC57550/", "http://i.imgur.com/aGykbhd.png"),
	("[COLOR red]TV >>[/COLOR] Tijd voor 80 - televisie", "playlist/PLdgTESJsxLJKuG8eyqDORuX19nvjpY57Q/", "http://i.imgur.com/aGykbhd.png"),
	("[COLOR red]TV >>[/COLOR] 80's TV Theme Songs", "playlist/PL6z6OgcOWW85HpkeoNwQQtw-qpGvPXM7i/", "http://i.imgur.com/aGykbhd.png"),
	("[COLOR red]TV >>[/COLOR] 80's Television Intro Mania", "playlist/PL236630F8CC8834EB/", "http://i.imgur.com/aGykbhd.png"),

	("[COLOR green]Commercials >>[/COLOR] Commercials from the 80s/Reclames uit de jaren 80 (1)", "playlist/PL497CFFFC18385690/", "http://i.imgur.com/PjX4xh7.png"),
	("[COLOR green]Commercials >>[/COLOR] Commercials from the 80s/Reclames uit de jaren 80 (2)", "playlist/PL9DF22EABA0820251/", "http://i.imgur.com/PjX4xh7.png"),
	("[COLOR green]Commercials >>[/COLOR] Reclame jaren 80", "playlist/PL7CDDA0B2444BC5FD/", "http://i.imgur.com/PjX4xh7.png"),
	("[COLOR green]Commercials >>[/COLOR] 80s Commercials", "playlist/PLC3458763E3A3C5A2/", "http://i.imgur.com/PjX4xh7.png"),
	("[COLOR green]Commercials >>[/COLOR] 80s Commercials Vol. 2", "playlist/PL6676FB688D404E2A/", "http://i.imgur.com/PjX4xh7.png"),
	
]



# Entry point
def run():
    plugintools.log("80time.run")
    
    # Get params
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
        action = params.get("action")
        exec action+"(params)"
    
    plugintools.close_item_list()

# Main menu
def main_list(params):
    plugintools.log("80time.main_list "+repr(params))

for name, id, icon in channellist:
	plugintools.add_item(title=name,url="plugin://plugin.video.youtube/"+id,thumbnail=icon,folder=True )



run()