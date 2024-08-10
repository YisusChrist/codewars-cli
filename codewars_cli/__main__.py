import click

from . import attempt, practice, submit, test, train


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
