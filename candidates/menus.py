import dash_html_components as html


def chart_menu():
    return html.Ul(className='nav justify-content-end', children=[
        html.Li(className='nav-item', children=[
            html.A(className='nav-link', href='/candidates/line', children=['Linha']),
        ]),
        html.Ul(className='nav nav-pills mb-3', children=[
            html.Li(className='nav-item', children=[
                html.A(className='nav-link', href='/candidates/bar', children=['Barra']),
            ]),
        ]),
        html.Ul(className='nav nav-pills mb-3', children=[
            html.Li(className='nav-item', children=[
                html.A(className='nav-link', href='/candidates/bubble', children=['Bolha']),
            ]),
        ]),
        html.Ul(className='nav nav-pills mb-3', children=[
            html.Li(className='nav-item', children=[
                html.A(className='nav-link', href='/candidates/pie', children=['Pizza']),
            ]),
        ]),
    ])
