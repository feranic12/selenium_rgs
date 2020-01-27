# -*- coding: utf-8 -*-
import pytest
from Fixtures.GoodChoiceFixture import GoodChoiceFixture


@pytest.fixture
def fix(request):
    browser = request.config.getoption("--browser")
    fixture = GoodChoiceFixture(browser)
    return fixture


def test_poehali(fix):
    fix.open_page()
    fix.fill_frame()
    input()