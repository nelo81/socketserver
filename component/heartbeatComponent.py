# coding:utf-8
from component.baseComponent import Component


class HeartbeatComponent(Component):

    def __init__(self):
        super(HeartbeatComponent, self).__init__(sign='heartbeat')
        self.timeout_window = {}
        self.dead_clients = []