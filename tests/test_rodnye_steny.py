# -*- coding: utf-8 -*-
import pytest
from Fixtures.RodnyeStenyFixture import RodnyeStenyFixture


@pytest.fixture
def fix(request):
    browser = request.config.getoption("--browser")
    fixture = RodnyeStenyFixture(browser)
    return fixture

def test_rodnye_steny(fix):
    fix.open_page()
    fix.fill_frame()
    input()