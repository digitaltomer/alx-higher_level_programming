#!/usr/bin/python3
"""This module creates objects from a Json file"""

import json


def load_from_json_file(filename):
    """a function that creates an Object from a JSON file"""
    with open(filename) as f:
        return json.load(f)
