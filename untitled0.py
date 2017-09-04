# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 14:33:27 2017

@author: mojod
"""
import re
from random import sample

sentences = []
for i in range(23):
    with open('speech.txt'.format(i)) as f:
        sentences += re.findall(r".*?[\.\!\?]+", f.read())

selected = sample(sentences, 1000)
with open('out.txt', 'w') as f:
    f.write('\n'.join(selected))
    f.close