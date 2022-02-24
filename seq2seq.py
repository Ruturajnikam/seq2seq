#!/usr/bin/env python
# coding: utf-8

import pandas as pd
x = pd.read_json('M:\dsdm\spider\dev.json')
x

x.info()
x.shape

x = x.iloc[:1000]
x

y = pd.read_json(r'M:\dsdm\spider\train_others.json')

y

y.info()
y.shape

y = y.iloc[:1000]
y

z = pd.read_json(r'M:\dsdm\spider\train_spider.json')
z

z.info()
z.shape

z = z.iloc[:1000]
z

