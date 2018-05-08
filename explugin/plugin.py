from math import ceil
import pytest


def pytest_addoption(parser):
    group = parser.getgroup(
        'pytest-example',
        'Example of Pytest plugins'
    )
    group.addoption(
        '--skip-if-contains',
        default=None,
        action='store',
        help="Profile to run tests with"
    )
    group.addoption(
        '--half-tests',
        default=False,
        action="store_true",
        help="Only runs half of the tests"
    )


def pytest_configure(config):
    config.addinivalue_line(
        "markers",
        "custom(name): mark test to have custom data"
    )


def pytest_unconfigure(config):
    pass


@pytest.hookimpl(trylast=True)
def pytest_collection_modifyitems(items):
    try:
        # Retrieve the config from the first test
        pytest_config = items[0].session.config
    except IndexError:
        return
    if pytest_config.option.half_tests:
        midpoint = ceil(len(items) / 2)
        # Modifying Items in place, so have to pop to remove tests
        for _ in range(midpoint):
            items.pop()
    items_to_remove = []
    skip_if_contains = pytest_config.option.skip_if_contains
    for item in items:
        if item.get_marker('custom'):
            item.add_marker(
                pytest.mark.xfail("Whenever marked with custom, just xfail it")
            )
        if skip_if_contains is not None:
            if skip_if_contains in item.name:
                items_to_remove.append(item)
    for rmitem in items_to_remove:
        items.remove(rmitem)
