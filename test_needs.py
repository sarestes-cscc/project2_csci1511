"""
    Virtual Pet Simulator
    Sarah Estes 11/1/27
    Testing functions for calculations
"""

from needs import Needs

def test_calculate_hunger():
    """Tests calculate_hunger"""
    needs = Needs()

    starting_hunger = needs.hunger
    needs.calculate_hunger(1)
    assert needs.hunger == starting_hunger + 10


def test_calculate_happiness():
    """Tests calculate_happiness"""
    needs = Needs()

    starting_happiness = needs.happiness
    starting_hunger = needs.hunger
    starting_energy = needs.energy

    needs.calculate_happiness(3)
    assert needs.happiness == starting_happiness + 20
    assert needs.hunger == starting_hunger - 10
    assert needs.energy == starting_energy - 40


def test_calculate_energy():
    """Tests calculate_energy"""
    needs = Needs()

    starting_energy = needs.energy
    starting_happiness = needs.happiness

    needs.calculate_energy(1)
    assert needs.energy == starting_energy + 20
    assert needs.happiness == starting_happiness - 60


def test_attention_affect():
    """Tests the attention_affect method calculations"""
    needs = Needs()
    starting_happiness = needs.happiness
    starting_hunger = needs.hunger
    starting_energy = needs.energy

    needs.attention_affect(25)
    assert needs.happiness == starting_happiness + 15
    assert needs.hunger == starting_hunger - 15
    assert needs.energy == starting_energy - 30
