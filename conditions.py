#!/usr/bin/env python
__author__ = 'Radek Vanhara'
__version__ = '1.0'

import time
'''
    Following class defines low level methods to specify the Robot Framework 
    supporting keywords.  
'''
class PyKeywords(object):
    def __init__(self):
        self._mbClient = None


    def is_equal_to(self, a, b):
        if float(a) != float(b):
            raise AssertionError('%s != %s' % (a, b))

    def is_greater_than_times(self, a, b, mul):
        if round(float(a) * float(mul)) != round(float(b)):
            raise AssertionError('%s is not greater than %s by %s' % (a, b, mul))

    def is_less_then(self, a, b):
        if float(a) >= float(b):
            raise AssertionError('%s >= %s' % (a, b))

    def is_more_then(self, a, b):
        if float(a) <= float(b):
            raise AssertionError('%s <= %s' % (a, b))

    def is_between(self, value, minVal, maxVal):
        result = True if float(minVal) <= float(value) <= float(maxVal) else False
        if not result:
            raise AssertionError('%s not in range [%s, %s]' % (value, minVal, maxVal))

    def wait_for(self, t):
        time.sleep(float(t))

    def values_differs_by(self, value1, value2, diff):
        result = True if abs(float(value1) - float(value2)) <= float(diff) else False
        if not result:
            raise AssertionError('Values %s and %s does not differ by %s' % (value1, value2, diff))