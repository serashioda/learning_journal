"""."""


def includeme(config):
    """All of the routes for the config."""
    config.add_static_view('static'),
    config.add_route('home', '/'),
