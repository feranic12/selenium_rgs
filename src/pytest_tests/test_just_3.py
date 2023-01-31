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

@pytest.fixture
def just_3():
    return (
        FlatbaseFixture("chrome"),
        VoyageFixture("chrome", 5),
        GoodChoiceFixture("chrome")
    )


def test_just_3(just_3):
    for f in just_3:
        f.open_page()
        f.fill_frame()
    input()