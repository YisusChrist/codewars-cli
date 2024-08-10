import click

from codewars_cli.attempt import attempt
from codewars_cli.practice import practice
from codewars_cli.submit import submit
from codewars_cli.test import test
from codewars_cli.train import train


@click.group()
def main():
    """An unofficial CLI for CodeWars."""


main.add_command(practice)
main.add_command(train)
main.add_command(test)
main.add_command(attempt)
main.add_command(submit)

if __name__ == "__main__":
    main()
