#!/usr/bin/env python3

import configparser

def main():

    print("Init config parser to read file")
    config = configparser.ConfigParser()
    config.read('config.ini')

    print("Read ini file into variables")
    token = config['telegram']['token']
    url = config['owncloud']['url']
    username = config['owncloud']['username']
    password = config['owncloud']['password']
    remote_file = config['owncloud']['remote_file']

    print("Read all, starting bot.")
    # todo: start bot here.


if __name__ == "__main__":
    main()