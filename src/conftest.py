import pytest
import utils

def pytest_addoption(parser):
    parser.addoption("--days", action="store", default=6, type=int)
    parser.addoption("--browser", action="store", default="chrome", type=str)
    parser.addoption("--target", action="store", default="1", type=str)
    parser.addoption("--product", action="store", default="Voyage", type=str)
    parser.addoption("--lang", action="store", default="ENG", type=str)

@pytest.fixture
def fix(request, scope='session'):
    try:
        browser = request.config.getoption("--browser")
        days = request.config.getoption("--days")
        lang = request.config.getoption("--lang")
        product = request.config.getoption("--product")
        if product == "Flatbase":
            from Fixtures.FlatbaseFixture import FlatbaseFixture
            fixture = FlatbaseFixture(browser)
        elif product == "Voyage":
            from Fixtures.VoyageFixture import VoyageFixture
            fixture = VoyageFixture(browser, days)
        elif product == "GoodChoice":
            from Fixtures.GoodChoiceFixture import GoodChoiceFixture
            fixture = GoodChoiceFixture(browser)
        elif product == "TelemedPlus":
            from Fixtures.TelemedPlusFixture import TelemedPlusFixture
            fixture = TelemedPlusFixture(browser)
        elif product == "OncoProtect":
            from Fixtures.OncoProtectFixture import OncoProtectFixture
            fixture = OncoProtectFixture(browser)
        elif product == "CascoPro":
            from Fixtures.CascoProFixture import CascoProFixture
            fixture = CascoProFixture(browser)
        elif product == "CarHelp":
            from Fixtures.CarHelpFixture import CarHelpFixture
            fixture = CarHelpFixture(browser)
        elif product == "Mite":
            from Fixtures.MiteFixture import MiteFixture
            fixture = MiteFixture(browser)
        elif product == "CovidFin":
            from Fixtures.CovidFinFixture import CovidFinFixture
            fixture = CovidFinFixture(browser)
        elif product == "NoPanic":
            from Fixtures.NoPanicFixture import NoPanicFixture
            fixture = NoPanicFixture(browser)
        elif product == "GetVaccine":
            from Fixtures.GetVaccineFixture import GetVaccineFixture
            fixture = GetVaccineFixture(browser)
        elif product == "Voyage2":
            from Fixtures.Voyage2Fixture import Voyage2Fixture
            fixture = Voyage2Fixture(browser)
        elif product == "VoyageToRussia":
            if lang not in ("RUS", "ENG"):
                raise utils.InvalidLanguageException
            from Fixtures.VoyageToRussiaFixture import VoyageToRussiaFixture
            fixture = VoyageToRussiaFixture(browser, lang)
        elif product == "TaxHelp":
            from Fixtures.TaxHelpFixture import TaxHelpFixture
            fixture = TaxHelpFixture(browser)
        elif product == "HomeProtect":
            from Fixtures.HomeProtectFixture import HomeProtectFixture
            fixture = HomeProtectFixture(browser)
        elif product == "MyHealthPlusB2B":
            from Fixtures.MyHealthPlusB2BFixture import MyHealthPlusB2BFixture
            fixture = MyHealthPlusB2BFixture(browser)
        elif product == "TelemedMyHealth":
            from Fixtures.TelemedMyHealthFixture import TelemedMyHealthFixture
            fixture = TelemedMyHealthFixture(browser)
        elif product == "YourProtect":
            from Fixtures.YourProtectFixture import YourProtectFixture
            fixture = YourProtectFixture(browser)
        elif product == "Eosago":
            from Fixtures.EosagoFixture import EosagoFixture
            fixture = EosagoFixture(browser)
        elif product == "Houseflat":
            from Fixtures.HouseflatFixture import HouseflatFixture
            fixture = HouseflatFixture(browser)
        elif product == "MyStability":
            from Fixtures.MyStabilityFixture import MyStabilityFixture
            fixture = MyStabilityFixture(browser)
    except utils.InvalidLanguageException:
        print("Error! Invalid language of frame specified!")
        return

    yield fixture

    #request.addfinalizer(fixture.destroy)
    #fixture.destroy()