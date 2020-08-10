from config import app
from flask import render_template
from models import (
    Newborn,
    NewbornSchema,
)

from bokeh.embed import components
from bokeh.plotting import figure


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


@app.route('/bokeh/<name>')
def bokeh(name):
    newborns = Newborn.query.filter_by(name=name)
    year = [str(n.year) for n in newborns]
    number = [n.number for n in newborns]
    print(year)
    print(number)
    plot = figure(
        plot_width=400, plot_height=400, title=None,
        toolbar_location="below",
    )
    plot.line(x=year, y=number)

    script, div = components(plot)
    kwargs = {'script': script, 'div': div}
    kwargs['title'] = 'Newborns'
    return render_template('bokeh.html', **kwargs)
