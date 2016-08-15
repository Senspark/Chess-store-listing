#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os, os.path

cmd = "../../../app-stores-toolkit/populate-v2.py metadata -platform iOS -prj-path . -sheet 1KLcJtK8W0Ru84piytass28DTe8o00nP6jN1h6Tsauyg -customized-metadata-path ../src/itunes/metadata"
print cmd
os.system(cmd)
