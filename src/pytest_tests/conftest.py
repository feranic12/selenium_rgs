import pytest
import utils


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
        elif product == "GoodChoiceB2B":
            from Fixtures.GoodChoiceB2BFixture import GoodChoiceB2BFixture
            fixture = GoodChoiceB2BFixture(browser)
        elif product == "TelemedPlusB2B":
            from Fixtures.TelemedPlusB2BFixture import TelemedPlusB2BFixture
            fixture = TelemedPlusB2BFixture(browser)
        elif product == "OncoProtectB2B":
            from Fixtures.OncoProtectB2BFixture import OncoProtectB2BFixture
            fixture = OncoProtectB2BFixture(browser)
        elif product == "CascoProB2B":
            from Fixtures.CascoProB2BFixture import CascoProB2BFixture
            fixture = CascoProB2BFixture(browser)
        elif product == "CarHelpB2B":
            from Fixtures.CarHelpB2BFixture import CarHelpB2BFixture
            fixture = CarHelpB2BFixture(browser)
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
        elif product == "SafeRest":
            from Fixtures.SafeRestFixture import SafeRestFixture
            fixture = SafeRestFixture(browser)
        elif product == "CardProtect":
            from Fixtures.CardProtectFixture import CardProtectFixture
            fixture = CardProtectFixture(browser)

    except utils.InvalidLanguageException:
        print("Error! Invalid language of frame specified!")
        return

    yield fixture

    #request.addfinalizer(fixture.destroy)
    #fixture.destroy()