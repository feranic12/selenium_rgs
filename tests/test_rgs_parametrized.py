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
from utils import InvalidLanguageException

fixtures = (FlatbaseFixture("chrome"),
            GoodChoiceFixture("chrome"),
            TelemedPlusFixture("chrome"))


@pytest.fixture(params = fixtures)
def fix(request):
    yield request.param
    # request.addfinalizer(fixture.destroy)
    request.param.destroy()


@pytest.mark.parametrize('fix', fixtures)
def test_rgs_parametrized(fix):
    fix.open_page()
    fix.fill_frame()
    fix.destroy()