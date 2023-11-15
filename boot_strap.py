#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 14:32:28 2023

@author: sasha
"""

import pandas as pd
import matplotlib.pyplot as plt

from plotnine import *

stat = "median"
dat = pd.DataFrame({"handspan": [20, 20, 19, 24.2, 20, 20.2, 21.5, 17, 19.5,
                                 21.5, 17, 19.5, 21.5, 18, 18, 20.5,
                                 20, 20.3, 1.5, 19, 20.4, 22.7, 22.9, 17,
                                 23, 23.8, 22, 21.5, 21.5]})
boot_means = []
boot_stat = []
for i in range(10_000):
    boot_sample = dat.sample(26, replace = True)
    
    if stat == "median":
        boot_stat.append(float(boot_sample.median()))
    elif stat == "mean":
        boot_stat.append(float(boot_sample.mean()))
    elif stat == "std dev":
        boot_stat.append(float(boot_sample.std()))
    else: 
        raise TypeError("Invalid statistic selection")


boot_df = pd.DataFrame({'x': boot_stat})

(
 ggplot(boot_df, aes(x = "x")) +
 geom_histogram()
 )
