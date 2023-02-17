import os
import csv
import pytest
from flaky import flaky
from foobar import foobar_commands
import constants


# TODO In general need more unit tests
# TODO Tests of User domain object
# TODO Tests of CLI

def test_get_groups():
    """Simple test to retrieve the group definitions"""
    groups = foobar_commands.get_groups(constants.groups_definition)
    groups_fixture = {"groupA": 0.4, "groupB": 0.1, "groupC": 0.5}
    assert groups == groups_fixture


@pytest.mark.dependency()
def test_add_users():
    """
    Uses a test csv (TODO use tempfile) to enter 100 users. Currently this is
    basically just a functional test, TODO add assertions / unit-test cases
    """
    users_list = [f"user{x}" for x in range(100)]
    users_test_path = os.path.join(
        os.getcwd(), "tests", "usersTestDefault.csv"
    )
    # Overwrite and clear the test csv on each run
    with open(users_test_path, "w") as csvfile:
        fieldnames = ["name", "group"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
    foobar_commands.add_users(
        users_test_path, constants.groups_definition, users_list
    )


@pytest.mark.dependency(depends=["test_add_users"])
@flaky(max_runs=5, min_passes=1)
def test_chi_square():
    """
    Chi-square goodness of fit test on results from test_add_user. Since
    groups are assigned by a weighted sample, we can't make a deterministic
    test, so this tests that the observed distribution is not statistically
    significantly different than the expected distribution

    Since this test is probabilistic by its nature, it will retry up to 5
    times and only needs to pass once
    """
    # TODO Make a test for get_users (even if this is de facto a functional
    # test of get_users)
    users_test_path = os.path.join(
        os.getcwd(), "tests", "usersTestDefault.csv"
    )
    users = foobar_commands.get_users(users_test_path)
    groups = foobar_commands.get_groups(constants.groups_definition)
    result = foobar_commands.chi_square(users, groups)
    assert result > 0.05
