#!/usr/bin/env python3
""" Module for using PyMongo """


def schools_by_topic(mongo_collection, topic):
    """ Returns list of school having specific topic """
    return mongo_collection.find({"topics": topic})
