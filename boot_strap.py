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


class Boot:
    def __init__(self, stat = "mean", n_boot = 100, dat = None, boot_df = None, ci_level = .95):
        self.stat = stat
        self.n_boot = n_boot
        self.dat = dat
        self.n = len(dat)
        self.boot_stat = None
        self.ci_level = ci_level
        self.boot_df = None
        self.sims_list = []
        
    
    def boot_taker(self, n_boot):
        for i in range(n_boot):
            boot_sample = self.dat.sample(n_boot, replace = True)
            self.sims_list.append(boot_sample)
            
            if self.stat == "median":
                self.boot_stat.append(float(boot_sample.median()))
            elif self.stat == "mean":
                self.boot_stat.append(float(boot_sample.mean()))
            elif self.stat == "std dev":
                self.boot_stat.append(float(boot_sample.std()))
            else:
                raise TypeError("Wrong statistic name")

    def gen_histogram(self):
        (
         ggplot(self.boot_df, aes(x = "x"))+
         geom_histogram()
         )
    def clear_sims_list(self):
        self.sims_list = []

    def add_sims_list(self, list):
        self.sims_list.append(list)
        
    def load_data(self, dat):
        self.dat = dat
        self.n = len(dat)
    

Boot("mean", 100, pd.read_csv("2017_Fuel_Economy_Data.csv"), .95)
Boot.gen_histogram(Boot)

