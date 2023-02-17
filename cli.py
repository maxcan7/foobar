import click
from version import __safe_version__
from foobar import foobar_commands
import constants


@click.version_option(version=__safe_version__, prog_name="foobar")
@click.group(help="Commands for the foobar coding challenge codebase")
def foobar_cli():
    pass


@foobar_cli.command(name="--version", hidden=True)
def get_version():
    click.echo(__safe_version__)


@foobar_cli.command(name="get_groups")
@click.help_option(
    help="Get groups definitions from userGroupPercentages.json or another"
    " json file with a similar organization",
)
@click.option(
    "--group_path",
    help="Path to a json file similar to userGroupPercentages.json (default)",
    default=constants.groups_definition,
)
def get_groups(group_path: str):
    groups = foobar_commands.get_groups(group_path)
    click.echo(groups)


@foobar_cli.command(name="get_users")
@click.help_option(
    help="Get users from usersDefault.csv or another csv file"
    " with a similar organization",
)
@click.option(
    "--users_path",
    help="Path to a csv file similar to usersDefault.csv (default)",
    default=constants.users_path,
)
def get_users(users_path: str):
    users = foobar_commands.get_users(users_path)
    click.echo(users)


@foobar_cli.command(name="add_users")
@click.help_option(
    help="Assign groups to the list of users in the users_path",
)
@click.option(
    "--users_path",
    help="Path to a csv file similar to usersDefault.csv (default)",
    default=constants.users_path,
)
@click.option(
    "--group_path",
    help="Path to a json file similar to userGroupPercentages.json (default)",
    default=constants.groups_definition,
)
@click.option(
    "--user_names",
    help="Comma-separated list of user names",
)
def add_users(users_path: str, group_path: str, user_names: str):
    users_list = user_names.split(",")
    foobar_commands.add_users(users_path, group_path, users_list)
    click.echo(f"{foobar_commands.get_users(users_path)}")


@foobar_cli.command(name="chi_square")
@click.help_option(
    help="Returns the p-value of a chi-square goodness of fit comparing the"
    " observed distribution of users to groups with the expected distribution."
    " If p > 0.05, there is no statistically significant difference, or in"
    " other words, the results are as expected"
)
@click.option(
    "--users_path",
    help="Path to a csv file similar to usersDefault.csv (default)",
    default=constants.users_path,
)
@click.option(
    "--group_path",
    help="Path to a json file similar to userGroupPercentages.json (default)",
    default=constants.groups_definition,
)
def chi_square(users_path: str, group_path: str):
    users = foobar_commands.get_users(users_path)
    groups = foobar_commands.get_groups(group_path)
    result = foobar_commands.chi_square(users, groups)
    if result > 0.05:
        click.echo(
            f"given p-value: {result}, there is no significant difference"
            " between the expected and observed result"
        )
    else:
        click.echo(
            f"given p-value: {result}, there is a significant difference"
            " between the expected and observed result"    
        )
