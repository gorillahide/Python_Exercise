#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 14:32:28 2023

@author: sasha
"""

import pandas as pd
import matplotlib.pyplot as plt
from plotnine import *

"""
When you inevitably run into errors trying to run this, learn to use
the working directory feature on your IDE. Hardcoding isn't going to work.
"""


dat = pd.read_csv("2017_Fuel_Economy_Data.csv")

dat = dat["Combined Mileage (mpg)"]
n = len(dat)
n_boot = 10_000                            
stat = "mean"

boot_stat = []
for i in range(n_boot):
    boot_sample = dat.sample(n, replace = True)
    
    if stat == "median":
        boot_stat.append(float(boot_sample.median()))
    elif stat == "mean":
        boot_stat.append(float(boot_sample.mean()))
    elif stat == "std dev":
        boot_stat.append(float(boot_sample.std()))
    else:
        raise TypeError("Wrong statistic name")
boot_df = pd.DataFrame({'x': boot_stat})

(
 ggplot(boot_df, aes(x = "x"))+
 geom_histogram()
 )