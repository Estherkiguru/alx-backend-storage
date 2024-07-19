#!/usr/bin/env python3
""" Module for using PyMongo """


def insert_school(mongo_collection, **kwargs):
    """ Inserts new document based on kwargs
    Returns new_id
    """
    id_obj = mongo_collection.insert_one(kwargs)
    return id_obj.inserted_id
