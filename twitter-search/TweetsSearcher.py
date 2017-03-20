#!/usr/bin/python
# -*- coding: utf-8 -*-
# python_twitter 1.1
import twitter
from twitter import Api
import sys
import os
import time
import json

reload(sys)
sys.setdefaultencoding('utf-8')
from collections import defaultdict

maxid = 0
search_word = "#XXXXXX"

api = Api(base_url="https://api.twitter.com/1.1",
          consumer_key='XXXXXXXX',
          consumer_secret='XXXXXXXX',
          access_token_key='XXXXXXXX',
          access_token_secret='XXXXXXXX')


count = 0
file = open(name='../data/result.json', mode='w')
found = api.GetSearch(term=search_word, count=100, lang="ja", result_type='mixed', until="yyyy-mm-dd")
while count < 3000:
    for result in found:

        file.write(str(result) + os.linesep)

        count += 1
        maxid = result.id
    found = api.GetSearch(term=search_word, count=100, result_type='mixed', max_id=maxid - 1)

file.close()
print "TweetsNum: " + str(count)


