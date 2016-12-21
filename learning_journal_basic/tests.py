"""."""
import pytest
from pyramid import testing


@pytest.fixture()
def req():
    """."""
    the_request = testing.DummyRequest()
    return the_request


def test_home_page_renders_file_data(req):
    """My home page view returns some data."""
    from .views import home_page
    response = home_page(req)
    assert "bag_list" in response


@pytest.fixture()


@pytest.fixture()
def testapp():
    from webtest import TestApp
    from learning_journal_basic import main
    app = main({})
    from webtest import TestApp
    return TestApp(app)

def test_home_page_has_list(testapp):
    response = testapp.get("/", status=200)
    inner_html = response.html


# from webtest import TestApp

# From learning_journal_basic import main

# testapp = TestApp(min({}))

# response = testapp.get("/", status=200)

# from pprint import pprint

# pprint(dir(response))

# html = response.html

# html.find_all("li")

# len(html.find_all("li"))
# >> 5

# html.find("ul").child

# <<ul = html.find('ul')
# <<ul



"""."""
import pytest
from pyramid import testing


@pytest.fixture()
def req():
    """."""
    the_request = testing.DummyRequest()
    return the_request


def test_home_page_renders_file_data(req):
    """My home page view returns some data."""
    from .views import home_page
    response = home_page(req)
    assert "bag_list" in response


@pytest.fixture()


@pytest.fixture()
def testapp():
    from webtest import TestApp
    from learning_journal_basic import main
    app = main({})
    from webtest import TestApp
    return TestApp(app)

def test_home_page_has_list(testapp):
    response = testapp.get("/", status=200)
    inner_html = response.html


# from webtest import TestApp

# From learning_journal_basic import main

# testapp = TestApp(min({}))

# response = testapp.get("/", status=200)

# from pprint import pprint

# pprint(dir(response))

# html = response.html

# html.find_all("li")

# len(html.find_all("li"))
# >> 5

# html.find("ul").child

# <<ul = html.find('ul')
# <<ul



import unittest

from pyramid import testing


class ViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_my_view(self):
        from .views import my_view
        request = testing.DummyRequest()
        info = my_view(request)
        self.assertEqual(info['project'], 'learning_journal_basic')


class FunctionalTests(unittest.TestCase):
    def setUp(self):
        from learning_journal_basic import main
        app = main({})
        from webtest import TestApp
        self.testapp = TestApp(app)

    def test_root(self):
        res = self.testapp.get('/', status=200)
        self.assertTrue(b'Pyramid' in res.body)
