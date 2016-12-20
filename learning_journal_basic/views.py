"""."""
from pyramid.response import Response
import io
import os

THIS_DIR = os.path.dirname(__file__)

ENTRIES = [
    {"title": "Entry 1",
    "id": 0,
    creation_date": "Dec. 20, 2016"
    }
    {"title": "Entry 1",
    "id": 1,
    }
    ]

@view_config(route_name="home", renderer="string")
def home_page(request):
    """View for the home page."""
    all_my_stuff = [
    "pens",
    "book",
    "laptop",
    ]
    return {"bag_list: all_my_stuff"}
    # file_path = os.path.join(THIS_DIR, "data", "sample.html")
    # file_data = file_data = io.open(file_path).read()
    # #return Response(file_data)
    # return file_data

@view_config(route_name="detail", renderer='string')
def detail(request):
    the_id = int(request.matchdict["id"])
    entry = ENTRIES[the_id]
    return {"entry"}
    # import pdb.pd.trace()

@view_config(route_name='create', renderer='string')
def create(request):
    return ""

@view_config(route_name='edit', renderer='string')
def update(request):
    return ""



# def home_page(request):
#     """View for the home page."""
#     file_path = os.path.join(THIS_DIR, 'templates', 'index.html')
#     file_data = io.open(file_path).read()
#     return Response(file_data)


# def detail_page(request):
#     """View for the detail page."""
#     file_path = os.path.join(THIS_DIR, 'templates', 'single.html')
#     file_data = io.open(file_path).read()
#     return Response(file_data)


# def create_page(request):
#     """View for the create page."""
#     file_path = os.path.join(THIS_DIR, 'templates', 'new_entry.html')
#     file_data = io.open(file_path).read()
#     return Response(file_data)


# def edit_page(request):
#     """View for the edit page."""
#     file_path = os.path.join(THIS_DIR, 'templates', 'edit_entry.html')
#     file_data = io.open(file_path).read()
#     return Response(file_data)


# def includeme(config):
#     """The configurator will attach my views to routes."""
#     config.add_view(home_page, route_name='home')
#     config.add_view(detail_page, route_name='detail')
#     config.add_view(create_page, route_name='create')
#     config.add_view(edit_page, route_name='update')
