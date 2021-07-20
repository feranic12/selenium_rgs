# -*- coding: utf-8 -*-
import pytest
from Fixtures.FlatbaseFixture import FlatbaseFixture
from Fixtures.VoyageFixture import VoyageFixture
from Fixtures.GoodChoiceFixture import GoodChoiceFixture
from Fixtures.TelemedPlusFixture import TelemedPlusFixture
from Fixtures.OncoProtectFixture import OncoProtectFixture
from Fixtures.CascoProFixture import CascoProFixture
from Fixtures.CarHelpFixture import CarHelpFixture
from Fixtures.MiteFixture import MiteFixture
from Fixtures.CovidFinFixture import CovidFinFixture
from Fixtures.NoPanicFixture import NoPanicFixture
from Fixtures.GetVaccineFixture import GetVaccineFixture
from Fixtures.Voyage2Fixture import Voyage2Fixture
from Fixtures.VoyageToRussiaFixture import VoyageToRussiaFixture
from Fixtures.TaxHelpFixture import TaxHelpFixture
from Fixtures.HomeProtectFixture import HomeProtectFixture
from Fixtures.MyHealthPlusB2BFixture import MyHealthPlusB2BFixture
from Fixtures.TelemedMyHealthFixture import TelemedMyHealthFixture
from utils import InvalidLanguageException


@pytest.fixture
def fix(request, scope='session'):
    try:
        browser = request.config.getoption("--browser")
        days = request.config.getoption("--days")
        lang = request.config.getoption("--lang")
        product = request.config.getoption("--product")
        if product == "Flatbase":
            fixture = FlatbaseFixture(browser)
        elif product == "Voyage":
            fixture = VoyageFixture(browser, days)
        elif product == "GoodChoice":
            fixture = GoodChoiceFixture(browser)
        elif product == "TelemedPlus":
            fixture = TelemedPlusFixture(browser)
        elif product == "OncoProtect":
            fixture = OncoProtectFixture(browser)
        elif product == "CascoPro":
            fixture = CascoProFixture(browser)
        elif product == "CarHelp":
            fixture = CarHelpFixture(browser)
        elif product == "Mite":
            fixture = MiteFixture(browser)
        elif product == "CovidFin":
            fixture = CovidFinFixture(browser)
        elif product == "NoPanic":
            fixture = NoPanicFixture(browser)
        elif product == "GetVaccine":
            fixture = GetVaccineFixture(browser)
        elif product == "Voyage2":
            fixture = Voyage2Fixture(browser)
        elif product == "VoyageToRussia":
            if lang not in ("RUS", "ENG"):
                raise InvalidLanguageException
            fixture = VoyageToRussiaFixture(browser, lang)
        elif product == "TaxHelp":
            fixture = TaxHelpFixture(browser)
        elif product == "HomeProtect":
            fixture = HomeProtectFixture(browser)
        elif product == "MyHealthPlusB2B":
            fixture = MyHealthPlusB2BFixture(browser)
        elif product == "TelemedMyHealth":
            fixture = TelemedMyHealthFixture(browser)
    except InvalidLanguageException:
        print("Error! Invalid language of frame specified!")
        return

    yield fixture

    #request.addfinalizer(fixture.destroy)
    #fixture.destroy()


def test_rgs(fix):
    fix.open_page()
    fix.fill_frame()
    input()