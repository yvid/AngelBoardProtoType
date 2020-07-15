# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 17:51:26 2020

@author: ACMD-YYB
"""


from application import create_app

# import logging
# logging.basicConfig()
# logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

app = create_app()

if __name__ == '__main__':
    app.run(debug=True,
            host="211.209.243.154",
            port=5500)
    