"""Routes for blog pathways."""


def includeme(config):
    """All of the routes for the config."""
    config.add_static_view(name='static', path='static', cache_max_age=3600)
    config.add_route('list', '/')
    config.add_route('create', '/journal/new-entry')
    config.add_route('detail', '/journal/{id:\d+}')
    config.add_route('edit', '/journal/{id:\d+}/edit-entry')
