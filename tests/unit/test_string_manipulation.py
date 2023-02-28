"""
Unit tests for test_string.py package
"""
import pytest

from src.string_manipulation import lower_case, upper_case, invert


# TODO: Implémenter les tests unitaires ci-dessous.
#       Les noms des méthodes indiquent ce qu'il faut tester.


def test_lower_case():
    """Tests lower_case function"""
    assert False


def test_invert():
    """Tests invert function"""
    assert False


# NOTE: La fixture "parametrize" de pytest permet de réaliser
#       le même test avec des valeurs d'entrée différentes.
#       Ci-dessous, le test "test_upper_case" sera executé
#       3 fois avec les 3 sets de valeurs spécifiés.
#       N'hésitez pas à tester cette fixture sur les autres
#       tests pour comprendre comment elle fonctionne.
@pytest.mark.parametrize(
    "input_string, expected_output",
    [
        ("league of legends", "LEAGUE OF LEGENDS"),
        ("POKEMON", "POKEMON"),
        ("Street Fighter", "STREET FIGHTER"),
    ],
)
def test_upper_case(input_string, expected_output):
    """Tests upper_case function"""
    assert False


def test_raises_exception_on_non_string_arguments_upper_case():
    """Tests that upper_case function raises a TypeError when its input is not a string"""
    assert False


def test_raises_exception_on_non_string_arguments_lower_case():
    """Tests that capital_case function raises a TypeError when its input is not a string"""
    assert False
