#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Tanky Woo @ 2013-08-20

from __future__ import print_function

class bcolors:
    OK = "\033[1;32m" # GREEN
    INFO = "\033[1;34m" # BLUE
    WARNING = "\033[1;33m" # YELLOW
    ERROR = "\033[5;31m"# RED
    ENDC = "\033[0m"

    def disable(self):
        self.OK = ""
        self.INFO = ""
        self.WARNING = ""
        self.ERROR = ""
        self.ENDC = ""

def print_ok(msg, extra_msg=""):
    print(bcolors.OK + msg + bcolors.ENDC + extra_msg)

def print_info(msg, extra_msg=""):
    print(bcolors.INFO + msg + bcolors.ENDC + extra_msg)

def print_warn(msg, extra_msg=""):
    print(bcolors.WARNING + msg + bcolors.ENDC + extra_msg)

def print_error(msg, extra_msg=""):
    print(bcolors.ERROR + msg + bcolors.ENDC + extra_msg)