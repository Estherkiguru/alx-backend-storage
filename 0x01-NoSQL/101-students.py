#!/usr/bin/env python3

""" Module for using PyMongo """


def top_students(mongo_collection):
    """ Returns all students sorted by average score
    Returns with key = averageScore
    """
    top_student = mongo_collection.aggregate([
        {
            "$project": {
                "name": "$name",
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {"$sort": {"averageScore": -1}}
    ])

    return top_student
