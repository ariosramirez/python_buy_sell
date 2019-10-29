# -*- coding: utf-8 -*-

"""Console script for python_buy_sell."""
import sys
import click
from .clients import commands as clients_commands


@click.group()
@click.pass_context
def main(ctx, args=None):
    """Console script for python_buy_sell."""
    click.echo("Replace this message by putting your code into "
               "python_buy_sell.cli.main")
    click.echo("See click documentation at https://click.palletsprojects.com/")
    ctx.obj = {}

#    return 0

main.add_command(clients_commands.all)


#if __name__ == "__main__":
#    sys.exit(main())  # pragma: no cover
