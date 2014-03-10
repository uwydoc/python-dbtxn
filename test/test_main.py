import sys
sys.path.insert(0, '..')

from test_success import test_success
from test_dbtxn import pool

if __name__ == '__main__':
    test_success(pool('.'))
