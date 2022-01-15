#!/usr/bin/env python3

import configparser

def main():
    config = configparser.ConfigParser()
    config.read('config.ini')

if __name__ == "__main__":
    main()