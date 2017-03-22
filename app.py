import os
from collections import defaultdict

from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from bokeh.plotting import figure
from bokeh.resources import INLINE
from bokeh.embed import components
import bokeh.palettes


BASE = os.path.abspath(os.path.dirname(__file__))
DATABASE_PATH = os.path.join(BASE, 'test.db')
DATABSE_URI = os.getenv('DATABASE_URL', 'sqlite:///' + DATABASE_PATH)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABSE_URI
db = SQLAlchemy(app)

import models


@app.route('/')
def index():
    return 'Hello, world'


@app.route('/chart')
def chart():
    all_data = defaultdict(list)
    query = models.Currency.query.all()
    p = figure(
        width=1080,
        height=600,
        x_axis_type="datetime",
    )

    for row in query:
        all_data[row.exchange].append((row.horah, row.price))

    for i, (exchange, points) in enumerate(all_data.items()):
        color = bokeh.palettes.Category20[20][i]
        X,Y = zip(*sorted(points))
        p.line(X,Y, line_width=2, alpha=0.7, legend=exchange, color=color)

    js_resources = INLINE.render_js()
    css_resources = INLINE.render_css()
    script, div = components(p)

    return render_template(
        'index.html',
        js_resources = js_resources,
        css_resources = css_resources,
        plot_script = script,
        plot_div = div,
    )


@app.route('/data')
def data():
    all_data = []
    query = models.Currency.query.all()
    for row in query:
        obj = {
            'exchange': row.exchange,
            'price': row.price,
            'time': row.horah
        }
        all_data.append(obj)
    return jsonify(all_data)


port = int(os.environ.get('PORT', 8080))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)
