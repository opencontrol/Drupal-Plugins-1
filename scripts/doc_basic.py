#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Script for generating basic document

Usage:
python3 doc_basic.py


"""

__author__ = "Greg Elin (gregelin@govready.com)"
__version__ = "$Revision: 0.1.0 $"
__date__ = "$Date: 2017/06/03 21:35:00 $"
__copyright__ = "Copyright (c) 2017 GovReady PBC"
__license__ = "Apache Software License 2.0"

import os
import yaml
import compliancelib

# Settings
opencontrol_repo = 'https://github.com/opencontrol/Drupal-Plugins-Compliance-Controls'
opencontrol_file = '../opencontrol.yaml'
controllist = ["AC-2","AC-6","AC-6 (1)", "AC-12", "SC-5", "SI-7"]
# controllist = ["AC-2","AC-6","AC-6 (1)", "AC-12", "AU-2", "AU-3", "AU-7", "AU-8", "AU-9", "AU-14", "SC-5", "SI-7"]

# Create system compliance instance
sp = compliancelib.SystemCompliance()
# Load OpenControl repo
sp.load_system_from_opencontrol_repo(opencontrol_repo)

# Figure out all the controls that are supported by the repo

# Loop through supported controls and output basic description document
# for c in controllist:
#   #  print("\n")
#   print("##", sp.control(c).id, sp.control(c).title, "\n")
#   for component in sp.control(c).components_dict.keys():
#     # print(component)
#     print(sp.control(c).components_dict[component][0]['narrative'][0]['text'])

# Loop through supported controls and capture basic description document
content = ""
for c in controllist:
    if c is None:
        continue
    content += "## {} {} \n\n".format(sp.control(c).id, sp.control(c).title)
    for component in sp.control(c).components_dict.keys():
        content += "{}".format(sp.control(c).components_dict[component][0]['narrative'][0]['text'].replace("\n"," "))
        content += "\n\n"

print("\n\n PRINTING OUTPUT \n")
print(content)