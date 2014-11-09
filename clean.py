# coding : 'utf-8'

import re
import os

def clean_layout():
  pass

def clean_drawable():
  for dir_name in res_list:
    for root, dirs, files in os.walk(dir_name):
      for file_name in files:
        # . values 
        if file_name.startswith('.'):
          continue
        path = os.path.join(root, file_name)
        dir_name, file_with_ext = os.path.split(path)
        # print file_with_ext
        file_without_ext = file_with_ext.split('.')[0]
        print file_without_ext

def build_dir_list():
  for pro_name in pro_list:
    if os.path.exists(pro_name):
      for dir_name in os.listdir(pro_name):
        # res src
        for file_name in find_from:
          if dir_name == file_name:
            path = os.path.join(pro_name, dir_name)
            dir_list.append(path)
            if dir_name == find_from[0]:
              res_list.append(path)
  # for x in dir_list:
  #   print x
  # for x in res_list:
  #   print x

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
          # print pro_name
    else:
      break

def clean():
  load_gradle_project()
  build_rely()
  build_dir_list()
  clean_drawable()
  clean_layout()

pro_list = []
dir_list = []
res_list = []
find_from = [r'res', r'src']
# todo init from *.ini
ignore_pro_list = ['XiaomiServiceFramework:v5_style', 'UMengSDK', 'XiaomiServiceFramework:huafubao',
            'XiaomiServiceFramework:linkpay','XiaomiServiceFramework:account',
            'XiaomiServiceFramework','MiAccountSdk','MiCloudSdk']

if __name__ == '__main__':
  clean()