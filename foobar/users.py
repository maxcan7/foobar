from constants import groups_definition, users_path
from foobar import foobar_commands
import random


class User:
    """
    In retrospect this data abstraction was probably overkill, but
    theoretically, we're going to want some kind of domain object
    """

    def __init__(
        self,
        name: str,
        group_definition: str = groups_definition,
        users_path: str = users_path,
        group: str = None,
    ):
        self.name = name
        self.group_definition = group_definition
        self.users_path = users_path
        self.group = group or self.set_group()

    def set_group(self):
        # From the groups definition, assign the user a group by sampling
        groups_dict = foobar_commands.get_groups(self.group_definition)
        groups_list = [key for key in groups_dict.keys()]
        weights = [val for val in groups_dict.values()]
        return random.choices(groups_list, weights=weights)[0]
