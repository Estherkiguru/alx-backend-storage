#!/usr/bin/env python3
""" Module for listing all documents in a collection """


def list_all(mongo_collection):
    """ Returns list of all documents in collection 
    or an empty list
    """
    cursor = mongo_collection.find()
    return [doc for doc in cursor]
