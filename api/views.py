from config import db
from flask import make_response
from models import (
    Newborn,
    NewbornSchema,
)


def get_newborns_by_year(year):
    """
    This function responds to a request for /api/year/<year>
    with the complete list of names and stats for the given year

    :param year:    year to be used as a filter
    :return:        json string of list of names and stats of newborns
    """
    newborns = Newborn.query.filter_by(year=year)
    newborn_schema = NewbornSchema(many=True)
    return newborn_schema.dump(newborns)

def get_newborns_by_name(name):
    """
    This function responds to a request for /api/names/<name>
    with the complete list of newborns and stats for the given name

    :param name:    name to be used as a filter
    :return:        json string of list of names and stats of newborns
    """
    newborns = Newborn.query.filter_by(name=name)
    newborn_schema = NewbornSchema(many=True)
    return newborn_schema.dump(newborns)
