# -*- coding: utf-8 -*-
import pytest
from Fixtures.PoehaliFixture import PoehaliFixture


@pytest.fixture
def fix(request):
    browser = request.config.getoption("--browser")
    fixture = PoehaliFixture(browser)
    return fixture


def test_poehali(fix):
    fix.open_page()
    fix.fill_frame()
    input()




