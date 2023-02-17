import os
import json
import csv
from typing import Dict, List, Any
from scipy import stats
import numpy as np
from foobar.users import User


def json_opener(path: str) -> Dict[str, Any]:
    if os.stat(path).st_size == 0:
        return {}  # If file is empty, return empty dict
    with open(path, "r") as f:
        return json.load(f)


def csv_opener(path: str) -> Dict[str, Any]:
    if os.stat(path).st_size == 0:
        return {}  # If file is empty, return empty dict
    with open(path) as csvfile:
        reader = csv.DictReader(csvfile)
        users = {}
        for row in reader:
            users[row["name"]] = row["group"]
        return users


def csv_writer(path: str, user: User):
    with open(path, "a") as csvfile:
        fieldnames = ["name", "group"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if os.stat(path).st_size == 0:
            writer.writeheader()  # If csv is empty, write header
        writer.writerow({"name": user.name, "group": user.group})


def get_groups(group_path: str) -> Dict[str, str]:
    """
    Returns a dictionary of the group definitions from group_path or default
    userGroupPercentages.json
    """
    return json_opener(group_path)


def get_users(users_path: str) -> Dict[str, str]:
    """
    In lieu of a database or block storage, current user information is
    written to a local json. Given users_path, returns a dictionary of the
    current users and their groups from users_path or default
    users_default.csv
    """
    return csv_opener(users_path)


def add_users(users_path: str, group_definition: str, users_list: List[str]):
    """
    Given a list of users, checks whether the user already exists, and if not,
    assigns it a group and writes it to the users csv
    """
    users_dict = get_users(users_path)
    for u in users_list:
        if users_dict.get(u):
            print(f"{u} is already a user in group {users_dict.get(u)}")
            continue
        user = User(
            name=u, group_definition=group_definition, users_path=users_path
        )
        csv_writer(users_path, user)


def chi_square(
    users: Dict[str, str], groups: Dict[str, float]
) -> np.float64:
    """
    Calculate chi-square goodness of fit for observed group assignment of
    users with distribution from groups

    TODO: Use User domain objects rather than a users Dict
    """
    total = len(users.keys())
    observed = {group: 0 for group in groups.keys()}
    for group in users.values():
        observed[group] += 1
    expected = [val for val in groups.values()]
    observed = [(count / total) for count in observed.values()]
    return stats.chisquare(f_obs=observed, f_exp=expected).pvalue
