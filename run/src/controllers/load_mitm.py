#!/usr/bin/env python3

from mitmproxy import controller, proxy, options
from mitmproxy.proxy.server import ProxyServer

class ProxyMaster (controller.Master):
    def __init__(self, server):
        controller.proxyMaster.__init__(self, server)

    def run(self):
        try:
            return controller.Master.run(self)
        except KeyboardInterrupt:
            self.shutdown()

    def handle_request(self, flow):
        flow.reply()

    def handle_response(self, flow):
        flow.reply()

config = proxy.ProxyConfig(port=8080)
server = ProxyServer(config)
m = ProxyMaster(server)
m.run()
