# -*- coding: utf-8 -*-

"""Console script for python_buy_sell."""
import sys
import click


@click.command()
def main(args=None):
    """Console script for python_buy_sell."""
    click.echo("Replace this message by putting your code into "
               "python_buy_sell.cli.main")
    click.echo("See click documentation at https://click.palletsprojects.com/")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
