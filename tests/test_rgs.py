# -*- coding: utf-8 -*-
import pytest
from Fixtures.RodnyeStenyFixture import RodnyeStenyFixture
from Fixtures.PoehaliFixture import PoehaliFixture
from Fixtures.GoodChoiceFixture import GoodChoiceFixture
from Fixtures.DoctorOnlineFixture import DoctorOnlineFixture


@pytest.fixture
def fix(request):
    browser = request.config.getoption("--browser")
    days = request.config.getoption("--days")
    product = request.config.getoption("--product")
    if product == "RodnyeSteny":
        fixture = RodnyeStenyFixture(browser)
    elif product == "Poehali":
        fixture = PoehaliFixture(browser, days)
    elif product == "GoodChoice":
        fixture = GoodChoiceFixture(browser)
    elif product == "TelemedPlus":
        fixture = DoctorOnlineFixture(browser)
    return fixture


def test_rgs(fix):
    fix.open_page()
    fix.fill_frame()
    input()