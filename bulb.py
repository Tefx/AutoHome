#!/usr/bin/env python
# -*- coding: utf-8 -*-

import asyncio
from kasa import Discover


class BulbController:
    def __init__(self):
        self.bulbs = []

    def discover(self):
        self.bulbs = [dev for dev in asyncio.run(Discover.discover()).values()
                      if dev.is_bulb]

    def state(self):
        if not self.bulbs:
            self.discover()
        res = {}
        for dev in self.bulbs:
            res[dev.alias] = dev.state_information
            res[dev.alias]["Is ON"] = dev.is_on
        return res
