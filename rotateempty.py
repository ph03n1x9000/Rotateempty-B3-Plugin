# Plugin for BigBrotherBot(B3) (www.bigbrotherbot.com)
# Copyright(C) 2016 ph03n1x
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

__version__ = '1.1'
__author__ = 'ph03n1x'


import b3
import b3.events
import b3.plugin
from time import sleep as wait
from thread import start_new_thread as snt


class RotateemptyPlugin(b3.plugin.Plugin):
    requiresConfigFile = False
    _actiontime = None
    waitdelay = 180

    def onStartup(self):
        self.registerEvent('EVT_CLIENT_KILL', self.onaction)
        self.registerEvent('EVT_CLIENT_SUICIDE', self.onaction)
        self.registerEvent('EVT_CLIENT_DAMAGE', self.onaction)
        self.registerEvent('EVT_CLIENT_DAMAGE_SELF', self.onaction)
        self.registerEvent('EVT_GAME_MAP_CHANGE', self.onaction)

        snt(self.startchecking, ())

    def onaction(self, event):
        self._actiontime = self.console.time()

    def startchecking(self):
        while True:
            if (self._actiontime + self.waitdelay) <= self.console.time():
                self.debug('No scores made in 3 minutes... Rotating map')
                self.console.write('map_rotate')
            wait(30)
