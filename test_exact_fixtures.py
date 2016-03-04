import pytest

active = set()

@pytest.yield_fixture(scope='session')
def alternative1():
    active.add('alternative1')
    yield
    active.remove('alternative1')

@pytest.yield_fixture(scope='session')
def alternative2():
    active.add('alternative2')
    yield
    active.remove('alternative2')


def test_alternative1(alternative1):
    assert active == set(['alternative1'])


def test_alternative2(alternative2):
    assert active == set(['alternative2'])
