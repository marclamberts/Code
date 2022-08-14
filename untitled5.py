#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 23:46:03 2021

@author: lamberts_888
"""
#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib.request

def SportDemo():
    # Set url parameter
    url = "http://api.isportsapi.com/sport/football/league/basic?api_key=ft2YCOQrih5Quu7O"

    # Call iSport Api to get data in json format
    f = urllib.request.urlopen(url)
    content = f.read()

    print(content.decode('utf-8'))


SportDemo()