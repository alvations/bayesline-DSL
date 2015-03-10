#!/usr/bin/env python -*- coding: utf-8 -*-
#
# bayesline.py - Multinomial Bayesian Classification for Language Identification
#
# Copyright (C) 2014-2015 alvations
# URL:
# For license information, see LICENSE.md

from distutils.core import setup

setup(
    name='bayesline',
    version='0.2',
    packages=['bayesline',],
    description='bayesline.py',
    long_description='A Multinomial Bayesian Classification for Language Identification',
    license="MIT",
    install_requires = ['numpy', 'sklearn']
)


import bayesline