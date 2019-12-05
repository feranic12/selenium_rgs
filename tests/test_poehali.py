# -*- coding: utf-8 -*-
import pytest
from Fixtures.PoehaliFixture import PoehaliFixture


@pytest.fixture
def fix(request):
    cmd_days = request.config.getoption("--days")
    browser = request.config.getoption("--browser")
    fixture = PoehaliFixture(browser, cmd_days)
    return fixture


def test_poehali(fix):
    fix.open_page()
    fix.fill_frame()
    input()




