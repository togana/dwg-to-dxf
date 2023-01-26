#!/usr/bin/env python
# -*- coding: utf-8 -*-

import glob
import subprocess

def input_file_names():
  return glob.glob("./input/*.dwg")

def convert_dwg_to_dxf(input):
  subprocess.check_call(['dwg2dxf', '-v', input])
  subprocess.check_call(['mv', '-f', input.replace('input/', '').replace('dwg', 'dxf'), input.replace('input', 'output').replace('dwg', 'dxf')])

if __name__ == '__main__':
  files = input_file_names()
  for file in files:
    print(file)
    convert_dwg_to_dxf(file)
