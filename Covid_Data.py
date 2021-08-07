#!/usr/bin/env python
# coding: utf-8

import pandas as pd

df = pd.read_json('https://www.mohfw.gov.in/data/datanew.json')
df = df[:36]
df = df.drop(['sno'], axis=1)

from lxml import html
import requests

page = requests.get('https://www.mohfw.gov.in/')
tree = html.fromstring(page.content)

date_string = tree.xpath('//h5/span/text()[1]')[0]
date_string_split = date_string.split()
date = date_string_split[3]+date_string_split[4].lower().capitalize()+date_string_split[5][0:4]

from datetime import datetime

date = datetime.strptime(date, '%d%B%Y')

df['date'] = date

df['change_in_active']=df['new_active']-df['active']
df['change_in_positive']=df['new_positive']-df['positive']
df['change_in_cured']=df['new_cured']-df['cured']
df['change_in_death']=df['new_death']-df['death']

df=df[['date', 'state_name', 'new_active', 'new_positive', 'new_cured',
       'new_death', 'active', 'positive', 'cured', 'death','change_in_active',
       'change_in_positive', 'change_in_cured', 'change_in_death','state_code']]

from sqlalchemy import create_engine

engine = create_engine('sqlite:///covid_data.db', echo=True)
df.to_sql('india_covid_data_state', con=engine, if_exists='append', index=False)

