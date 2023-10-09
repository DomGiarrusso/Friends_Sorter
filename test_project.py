from project import arg_checker, role_selector, zodiac_loop, zodiac_selector
import pytest


def test_arg_checker():
    with pytest.raises(SystemExit):
        arg_checker()


def test_role_selector():
    assert role_selector("lawmaker") == "The Mom"
    assert role_selector("listner") == "The Therapist"
    assert role_selector("bonder") == "The Connector"
    assert role_selector("controlling") == "The Planner"
    assert role_selector("funny") == "The Joker"
    assert role_selector("different") == "The Hipster"
    assert role_selector("extra") == "The Overachiever"
    assert role_selector("cute") == "The Flirt"
    assert role_selector("crazy") == "The Party Animal"
    assert role_selector("calm") == "The Chill One"
    assert role_selector("creative") == "The Artistic One"
    assert role_selector("trendy") == "The Fastionable One"
    assert role_selector("academic") == "The Smart One"
    assert role_selector("opinionated") == "The Hot Head"
    assert role_selector("judgy") == "The Pessimist"
    assert role_selector("unorganized") == "The Absolute Mess"
    assert role_selector("") == "No role"
    assert role_selector("Potatoes") == "No role"
    assert role_selector("Apples") == "No role"


def test_zodiac_loop():
    assert (
        zodiac_loop(
            range(21, 32), range(1, 20), "march ", "april ", "Aries", "march 28"
        )
        == "Aries"
    )
    assert (
        zodiac_loop(range(20, 31), range(1, 21), "april ", "may ", "Taurus", "may 4")
        == "Taurus"
    )
    assert (
        zodiac_loop(range(21, 32), range(1, 22), "may ", "june ", "Gemini", "june 19")
        == "Gemini"
    )
    assert (
        zodiac_loop(range(22, 31), range(1, 23), "june ", "july ", "Cancer", "july 3")
        == "Cancer"
    )
    assert (
        zodiac_loop(range(23, 32), range(1, 23), "july ", "august ", "Leo", "august 15")
        == "Leo"
    )
    assert (
        zodiac_loop(
            range(23, 31), range(1, 23), "august ", "september ", "Virgo", "august 28"
        )
        == "Virgo"
    )
    assert (
        zodiac_loop(
            range(23, 32), range(1, 24), "september ", "october ", "Libra", "october 2"
        )
        == "Libra"
    )
    assert (
        zodiac_loop(
            range(24, 31),
            range(1, 22),
            "october ",
            "november ",
            "Scorpius",
            "october 28",
        )
        == "Scorpius"
    )
    assert (
        zodiac_loop(
            range(22, 32),
            range(1, 22),
            "november ",
            "december ",
            "Sagittarius",
            "december 2",
        )
        == "Sagittarius"
    )
    assert (
        zodiac_loop(
            range(22, 31),
            range(1, 20),
            "december ",
            "january ",
            "Capricornus",
            "december 28",
        )
        == "Capricornus"
    )
    assert (
        zodiac_loop(
            range(20, 32),
            range(1, 19),
            "january ",
            "february ",
            "Aquarius",
            "january 28",
        )
        == "Aquarius"
    )
    assert (
        zodiac_loop(
            range(19, 29), range(1, 21), "february ", "march ", "Pieces", "march 2"
        )
        == "Pieces"
    )


def test_zodiac_selector():
    assert zodiac_selector("april 13") == "Aries"
    assert zodiac_selector("may 3") == "Taurus"
    assert zodiac_selector("june 13") == "Gemini"
    assert zodiac_selector("july 3") == "Cancer"
    assert zodiac_selector("august 15") == "Leo"
    assert zodiac_selector("august 28") == "Virgo"
    assert zodiac_selector("september 25") == "Libra"
    assert zodiac_selector("october 30") == "Scorpius"
    assert zodiac_selector("november 24") == "Sagittarius"
    assert zodiac_selector("january 13") == "Capricornus"
    assert zodiac_selector("february 1") == "Aquarius"
    assert zodiac_selector("march 1") == "Pisces"
    assert zodiac_selector("") == "No zodiac"
    assert zodiac_selector("Potatoes") == "No zodiac"
    assert zodiac_selector("Apple") == "No zodiac"
