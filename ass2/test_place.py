"""(Incomplete) Tests for Place class."""
from place import Place


def run_tests():
    """Test Place class."""

    # Test empty place (defaults)
    print("Test empty place:")
    default_place = Place()
    print(default_place)
    assert default_place.name == ""
    assert default_place.country == ""
    assert default_place.priority == 0
    assert not default_place.is_visited

    # Test initial-value place
    print("Test initial-value place:")
    new_place = Place("Malagar", "Spain", 1, False)
    assert new_place.name == "Malagar"
    assert new_place.country == "Spain"
    assert new_place.priority == 1
    assert not new_place.is_visited

    #

    # Test mark_visited
    print("Test mark_visited:")
    new_place.mark_visited()
    assert new_place.is_visited

    # Test mark_unvisited
    print("Test mark_unvisited:")
    new_place.mark_unvisited()
    assert not new_place.is_visited

    # Test __str__
    print("Test __str__:")
    str_representation = str(new_place)
    assert str_representation == "Malagar in Spain (Priority: 1)"

    # Test set_name
    print("Test set_name:")
    new_place.set_name("New Place")
    assert new_place.name == "New Place"

    # Test set_country
    print("Test set_country:")
    new_place.set_country("New Country")
    assert new_place.country == "New Country"

    # Test set_priority
    print("Test set_priority:")
    new_place.set_priority(2)
    assert new_place.priority == 2

    print("All tests passed!")


run_tests()
