# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Minecraft
# (c) 2015 - KAOSbox
# Based on code from youtube addon
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.minecraft'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')


channellist=[

		("[COLOR red]Minecraft Essentials >>[/COLOR] Grian", "user/Xelqua", icon),
		("[COLOR red]Minecraft Essentials >>[/COLOR] Sky Does Minecraft", "channel/UCKlhpmbHGxBE6uw9B_uLeqQ", icon),
		("[COLOR red]Minecraft Essentials >>[/COLOR] TheSyndicateProject", "channel/UC1ieoHqKW-yYgDhLHIcx28w", icon),
		("[COLOR red]Minecraft Essentials >>[/COLOR] TheDiamondMinecart // DanTDM", "channel/UCS5Oz6CHmeoF7vSad0qqXfw", icon),
		("[COLOR red]Minecraft Essentials >>[/COLOR] CaptainSparklez", "channel/UCshoKvlZGZ20rVgazZp5vnQ", icon),
		("[COLOR red]Minecraft Essentials >>[/COLOR] YOGSCAST Lewis & Simon", "channel/UCH-_hzb2ILSCo9ftVSnrCIQ", icon),
		("[COLOR red]Minecraft Essentials >>[/COLOR] PopularMMOs", "channel/UCpGdL9Sn3Q5YWUH2DVUW1Ug", icon),
		("[COLOR red]Minecraft Essentials >>[/COLOR] SSundee", "channel/UCke6I9N4KfC968-yRcd5YRg", icon),
		("[COLOR red]Minecraft Essentials >>[/COLOR] TheBajanCanadian", "channel/UCuj1Ms9_LCsQPSJ4p8nvOVA", icon),
		("[COLOR red]Minecraft Essentials >>[/COLOR] JeromeASF", "channel/UCrYnLkVfvVf0Qy0YOUQdk2A", icon),
		("[COLOR red]Minecraft Essentials >>[/COLOR] iBallisticSquid", "channel/UCa6Hg8HmooiDNaCT0_1NbQQ", icon),
		("[COLOR red]Minecraft Essentials >>[/COLOR] TheAtlanticCraft | Minecraft", "channel/UC4f1zAG2BTkfOQV4_nFbpBQ", icon),
		("[COLOR red]Minecraft Essentials >>[/COLOR] ExplodingTNT", "channel/UC2nZMhZ2qG5-xpqb440WLYg", icon),
		("[COLOR red]Minecraft Essentials >>[/COLOR] Slamacow", "channel/UCCuIq8gvVXGUe00Bti3uv9w", icon),
		("[COLOR red]Minecraft Essentials >>[/COLOR] Minecraft Universe | TrueMU", "channel/UCNodmx1ERIjKqvcJLtdzH5Q", icon),
		("[COLOR red]Minecraft Essentials >>[/COLOR] PrestonPlayz - Minecraft", "channel/UC70Dib4MvFfT1tU6MqeyHpQ", icon),
		("[COLOR red]Minecraft Essentials >>[/COLOR] AntVenom", "channel/UCK376qNDlNZZDNHsnaWuTeg", icon),

		("[COLOR blue]Kid-Friendly >>[/COLOR] stampylonghead", "user/stampylonghead", icon),
		("[COLOR blue]Kid-Friendly >>[/COLOR] iBallisticSquid", "user/iBallisticSquid", icon),
		("[COLOR blue]Kid-Friendly >>[/COLOR] PaulSoaresJR", "user/paulsoaresjr", icon),
		("[COLOR blue]Kid-Friendly >>[/COLOR] LittleLizardGaming - Minecraft Mods!", "user/LittleLizardGaming", icon),	
		("[COLOR blue]Kid-Friendly >>[/COLOR] PrestonPlayz - Minecraft", "channel/UC70Dib4MvFfT1tU6MqeyHpQ", icon),	
		("[COLOR blue]Kid-Friendly >>[/COLOR] TheAtlanticCraft | Minecraft", "user/TheAtlanticCraft", icon),	
		("[COLOR blue]Kid-Friendly >>[/COLOR] PopularMMOs", "user/PopularMMOs", icon),	
		("[COLOR blue]Kid-Friendly >>[/COLOR] Minecraft Universe | TrueMU", "user/MinecraftUniverse", icon),	
		("[COLOR blue]Kid-Friendly >>[/COLOR] TheBajanCanadian", "user/TheBajanCanadian", icon),	
		("[COLOR blue]Kid-Friendly >>[/COLOR] TheDiamondMinecart // DanTDM", "user/TheDiamondMinecart", icon),	
		("[COLOR blue]Kid-Friendly >>[/COLOR] CaptainSparklez", "user/CaptainSparklez", icon),

		("[COLOR yellow]Dutch >>[/COLOR] GameMeneer", "user/GameMeneer", icon),
		("[COLOR yellow]Dutch >>[/COLOR] DusDavidCraft", "channel/UCrJqFkdAbEkX71gnSlH5aww", icon),
		("[COLOR yellow]Dutch >>[/COLOR] DusDavidGames", "channel/UCB8b8H_V6NMz8KdPtbdEq7g", icon),
		("[COLOR yellow]Dutch >>[/COLOR] DagelijksHaaDee", "channel/UCNPlSBggCmH8FJiMC2FYYpQ", icon),
		("[COLOR yellow]Dutch >>[/COLOR] DoeMaarGamen", "user/doemaargamen", icon),
		("[COLOR yellow]Dutch >>[/COLOR] TIES", "channel/UCxZfoESEhdM4zwnnrAVr5gg", icon),
		("[COLOR yellow]Dutch >>[/COLOR] AltijdCompilaties", "user/AltijdCompilaties", icon),
		("[COLOR yellow]Dutch >>[/COLOR] HetGameS", "user/HetGameS", icon),
		("[COLOR yellow]Dutch >>[/COLOR] JoostSpeeltSpellen", "user/JoostSpeeltSpellen", icon),
		("[COLOR yellow]Dutch >>[/COLOR] DylanPeys", "channel/UC0FS8uuTdt80f_RyBVggx9Q", icon),
		("[COLOR yellow]Dutch >>[/COLOR] DeGameHal", "user/DeGameHal", icon),
	
]



# Entry point
def run():
    plugintools.log("minecraft.run")
    
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
    plugintools.log("minecraft.main_list "+repr(params))

for name, id, icon in channellist:
	plugintools.add_item(title=name,url="plugin://plugin.video.youtube/"+id+"/",thumbnail=icon,folder=True )



run()