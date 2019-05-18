import sys
import argparse

import requests

from id_encoder import debase_and_decode


def _url(path):
    return f"http://127.0.0.1:8000{path}"


def add(headers):
    url = input('Your url?\n')
    resp = requests.post(_url('/redirects/'), json={'destination': url}, headers=headers)
    resp.raise_for_status()

    print(f"Created new url code: \n{resp.json()['code']}")


def get(headers):
    code = input('what is your code?\n')
    redirect_id = debase_and_decode(code)
    resp = requests.get(_url('/redirects/{:d}/'.format(redirect_id)), headers=headers)
    resp.raise_for_status()

    item = resp.json()
    print('\nHere are the details:')
    print(f"{item['destination']} {item['code']} {item['visits']}")


def delete(headers):
    code = input('what is your code?\n')
    redirect_id = debase_and_decode(code)
    resp = requests.delete(_url('/redirects/{:d}/'.format(redirect_id)), headers=headers)
    resp.raise_for_status()

    print(f"\n{code} is deleted\n")


def list_all(headers):
    resp = requests.get(_url('/redirects/'), headers=headers)
    resp.raise_for_status()

    for item in resp.json()['results']:
        print(f"\n{item['destination']} {item['code']} {item['visits']}")


def quit_prog():
    sys.exit()


def help_shorten():
    print("Available commands:\n%s" % ", ".join(_ACTIONS.keys()))


_ACTIONS = {
    # Value = function, bool(pass in parameters)
    'add': (add, True),
    'get': (get, True),
    'delete': (delete, True),
    'list': (list_all, True),
    'quit': (quit_prog, False),
    'help': (help_shorten, False),
}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("token", help="This is your api auth token")
    args = parser.parse_args()

    headers = {'Authorization': f"token {args.token}"}

    while True:
        raw_action = input("\nWhat would you like to do?\n")
        action = raw_action.lower()
        if action in _ACTIONS:
            func, include_params = _ACTIONS[action]
            if include_params:
                func(headers)
            else:
                func()
        else:
            print("can't do that.\nYour options are %s" % ", ".join(_ACTIONS.keys()))


if __name__ == '__main__':
    main()
