# -*- coding: utf-8 -*-
import pytest
from Fixtures.FlatbaseFixture import FlatbaseFixture
from Fixtures.VoyageFixture import VoyageFixture
from Fixtures.GoodChoiceB2BFixture import GoodChoiceFixture
from Fixtures.TelemedPlusB2BFixture import TelemedPlusFixture
from Fixtures.OncoProtectB2BFixture import OncoProtectFixture
from Fixtures.CascoProB2BFixture import CascoProFixture
from Fixtures.CarHelpB2BFixture import CarHelpFixture
from Fixtures.MiteFixture import MiteFixture
from Fixtures.CovidFinFixture import CovidFinFixture
from Fixtures.NoPanicFixture import NoPanicFixture
from Fixtures.GetVaccineFixture import GetVaccineFixture
from Fixtures.Voyage2Fixture import Voyage2Fixture
from Fixtures.VoyageToRussiaFixture import VoyageToRussiaFixture
from Fixtures.TaxHelpFixture import TaxHelpFixture
from Fixtures.HomeProtectFixture import HomeProtectFixture
from utils import InvalidLanguageException

fixtures = (VoyageFixture("chrome", 5),
            TelemedPlusFixture("chrome"),
            OncoProtectFixture("chrome"))


def id_func(fixture_value):
    t = fixture_value
    return "Fixture {0}".format(t)


@pytest.fixture(params = fixtures, ids=id_func)
def fix(request):
    yield request.param
    # request.addfinalizer(fixture.destroy)
    request.param.destroy()


def test_rgs_many(fix):
    fix.open_page()
    fix.fill_frame()