#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 14:32:28 2023

@author: sasha
"""

import pandas as pd
import matplotlib.pyplot as plt
from plotnine import *
import numpy as np

"""
When you inevitably run into errors trying to run this, learn to use
the working directory feature on your IDE. Hardcoding isn't going to work.
"""


class Boot:
    def __init__(self, stat = "mean", n_boot = 100, dat = None, ci_level = .95):
        """
        Parameters
        ----------
        stat : STRING, optional
            Desired statistic. The default is "mean".
        n_boot : INT, optional
            Number of bootstraps. The default is 100.
        dat : DF, optional
            Desired data. The default is None.
        ci_level : FLOAT, optional
            Desired confidence level. The default is .95.

        Returns
        -------
        None.

        """
        self.stat = stat
        self.n_boot = n_boot
        self.dat = dat
        self.n = len(dat)
        self.boot_stat = stat
        self.ci_level = ci_level
        self.sims_list = []
    
    def boot_taker(self):
        """
        Generates n_boot samples.

        Raises
        ------
        TypeError
            Incorrect string for statistic name.

        Returns
        -------
        None

        """
        for i in range(self.n_boot):
            boot_sample = self.dat.sample(self.n, replace=True)
    
            if self.stat == "median":
                self.sims_list.append(float(boot_sample.median()))
            elif self.stat == "mean":
                self.sims_list.append(float(boot_sample.mean()))
            elif self.stat == "std dev":
                self.sims_list.append(float(boot_sample.std()))
            else:
                raise TypeError("Wrong statistic name")

                    
    def change_stat(self, stat):
        """
        Void function that changes desired statistic.

        Parameters
        ----------
        stat : STRING
            Name of desired statistic.

        Raises
        ------
        TypeError
            Invalid statistic name.

        Returns
        -------
        None.

        """
        if self.stat == "median" or "mean" or "std dev": #check
            self.boot_stat = stat
        else:
            raise TypeError("Wrong statistic name")
            self.sims_list = []

    def gen_histogram(self):
        """
        Void function that generates a histogram from the sims list

        Returns
        -------
        None.

        """
        boot_df = pd.DataFrame({'x': self.sims_list})
    
        plot = (
            ggplot(boot_df, aes(x = "x"))+
            geom_histogram()
        )
        print(plot)

    
    
    def clear_sims_list(self):
        """
        Void function that clears the sims list

        Returns
        -------
        None.

        """
        self.sims_list = []

    def add_sims_list(self, list):
        """
        Void function that adds to the sims_list

        Parameters
        ----------
        list : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
        self.sims_list.append(list)
        
    def load_data(self, dat):
        """
        Void function that changes the desired data

        Parameters
        ----------
        dat : STRING
            Data to be read into dataframe

        Returns
        -------
        None.

        """
        self.dat = dat
        self.n = len(dat)
    
# example using the 2017 fuel economy data file from local directory
dat =  pd.read_csv("2017_Fuel_Economy_Data.csv")
dat = dat["Combined Mileage (mpg)"]
strap = Boot("mean", 100, dat, .95)
strap.boot_taker()
strap.gen_histogram()

