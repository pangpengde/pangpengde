# coding : 'utf-8'

import re
import os

def clean_layout():
  pass

def clean_drawable():
  for dir_name in pro_list:
    if os.path.exists(dir_name):
      for file_name in os.listdir(dir_name):
        print file_name
        

def build_rely():
  pass

# load project
def load_gradle_project():
  f = open('settings.gradle') 
  while 1:
    l = f.readline()
    if l:
      pattern = re.compile(r'include \':(\w+)\'')
      match = pattern.match(l) 
      if match:
        pro_name = match.group(1);
        if ignore_pro_list.count(pro_name) <= 0:
          pro_list.append(pro_name)
          print pro_name
    else:
      break

def clean():
  load_gradle_project()
  build_rely()
  clean_drawable()
  clean_layout()

pro_list = []

find_from = [r'/res/.*', r'/src/.*']
# todo init from *.ini
ignore_pro_list = ['XiaomiServiceFramework:v5_style', 'UMengSDK', 'XiaomiServiceFramework:huafubao',
            'XiaomiServiceFramework:linkpay','XiaomiServiceFramework:account',
            'XiaomiServiceFramework','MiAccountSdk','MiCloudSdk']

if __name__ == '__main__':
  clean()