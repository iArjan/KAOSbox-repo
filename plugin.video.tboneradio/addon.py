#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#     Copyright (C) 2015 KAOSbox
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program. If not, see <http://www.gnu.org/licenses/>.
#

from xbmcswift2 import Plugin, xbmc

plugin = Plugin()

@plugin.route('/')
def show_tboneradio_list():
    items = [

  {'label': 'TboneRadio Stream',
   'thumbnail': 'special://home/addons/plugin.video.tboneradio/icon.png',
   'path': 'http://www.tboneradio.nl:8000/live.mp3',
   'is_playable': True,
  },

  {'label': 'TboneRadio Live Ustream',
   'thumbnail': 'special://home/addons/plugin.video.tboneradio/icon.png',
   'path': 'http://iphone-streaming.ustream.tv/ustreamVideo/8943165/streams/live/playlist.m3u8',
   'is_playable': True,
  },
]
    return plugin.finish(items)

def log(text):
    plugin.log.info(text)

if __name__ == '__main__':
    plugin.run()