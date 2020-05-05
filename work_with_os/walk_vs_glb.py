# https://gist.github.com/hamiltont/7518203
import os
import json
import time
import importlib
import sys
import glob

# From http://stackoverflow.com/a/5478448/119592
def timing(f):
    def wrap(*args):
        time1 = time.time()
        ret = f(*args)
        time2 = time.time()
        print '%s function took %0.3f ms' % (f.func_name, (time2-time1)*1000.0)
        return ret
    return wrap
    
class FrameworkTest:
  def __init__(self, name, directory, args):
      self.name = name
      self.directory = directory
      # Any key/value pairs from the JSON configuration file for this test
      # are added as variables
      self.__dict__.update(args)
    
      # ensure directory has __init__.py file so that we can use it as a Python package
      if not os.path.exists(os.path.join(directory, "__init__.py")):
        open(os.path.join(directory, "__init__.py"), 'w').close()

      self.setup_module = setup_module = importlib.import_module(directory + '.' + self.setup_file)

def parse_config(config, directory):
  tests = []

  # The config object can specify multiple tests, we neep to loop
  # over them and parse them out
  for test in config['tests']:
    for key, value in test.iteritems():
      test_name = config['framework']
      
      # if the test uses the 'defualt' keywork, then we don't 
      # append anything to it's name. All configs should only have 1 default
      if key != 'default':
        # we need to use the key in the test_name
        test_name = test_name + "-" + key

      tests.append(FrameworkTest(test_name, directory, value))

  return tests

@timing
def glob_tests():
  tests = []

  filesDepth2 = glob.glob('*/benchmark_config')
  for config_file_name in filesDepth2:
    config = None
    with open(config_file_name, 'r') as config_file:
      # Load json file into config object
      try:
        config = json.load(config_file)
      except:
        print("Error loading '%s'." % config_file_name)
        raise

    if config is None:
      continue

    tests = tests + parse_config(config, os.path.dirname(config_file_name))

  tests.sort(key=lambda x: str(x))
  return tests

@timing
def gather_tests():
  tests = []
  
  # Loop through each directory (we assume we're being run from the benchmarking root)
  # and look for the files that signify a benchmark test
  for dirname, dirnames, filenames in os.walk('.'):
    # Look for the benchmark_config file, this will set up our tests.
    # Its format looks like this:
    #
    # {
    #   "framework": "nodejs",
    #   "tests": [{
    #     "default": {
    #       "setup_file": "setup",
    #       "json_url": "/json"
    #     },
    #     "mysql": {
    #       "setup_file": "setup",
    #       "db_url": "/mysql",
    #       "query_url": "/mysql?queries="
    #     },
    #     ...
    #   }]
    # }
    if 'benchmark_config' in filenames:
      config = None
      config_file_name = os.path.join(dirname, 'benchmark_config')

      with open(config_file_name, 'r') as config_file:
        # Load json file into config object
        try:
          config = json.load(config_file)
        except:
          print("Error loading '%s'." % config_file_name)
          raise

      if config is None:
        continue

      tests = tests + parse_config(config, dirname[2:])

  tests.sort(key=lambda x: str(x))
  return tests




if __name__ == "__main__":
  # Ensure toolset/setup/linux is in the path so that the tests can "import setup_util".
  sys.path.append('toolset/setup/linux')
  gather_tests()
  glob_tests()
