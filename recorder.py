import sys
import os


def parse_params():
    global params
    params = DEFAULT_PARAMS.copy()
    params.update(dict(item.split('=') for item in sys.argv[1:] if item.__contains__('=')))


DEFAULT_PARAMS = {
    'save_dir': 'data/recorder',
}

if __name__ == '__main__':
    parse_params()
    save_dir = params['save_dir']
    print('The save dir is "%s".' % save_dir)



