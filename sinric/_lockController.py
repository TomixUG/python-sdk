"""
 *  Copyright (c) 2019 Sinric. All rights reserved.
 *  Licensed under Creative Commons Attribution-Share Alike (CC BY-SA)
 *
 *  This file is part of the Sinric Pro (https://github.com/sinricpro/)
"""

from ._dataTracker import DataTracker


class LockStateController:
    def __init__(self):
        self.lockState = DataTracker.readData("lockState")
        pass

    async def setLockState(self, jsn, callback):
        return callback(jsn.get("deviceId"), jsn.get("payload").get('value', False).get('state', "unlock"))
