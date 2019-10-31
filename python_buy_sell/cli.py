# -*- coding: utf-8 -*-

"""Console script for python_buy_sell."""
import sys
import click
from .clients import commands as clients_commands

CLIENTS_TABLE = '.clients.csv'

@click.group()
@click.pass_context
def main(ctx, args=None):
    """Console script for buy_sell."""
    
    ctx.obj = {}
    ctx.obj['clients_table'] = CLIENTS_TABLE

main.add_command(clients_commands.all)


#if __name__ == "__main__":
#    sys.exit(main())  # pragma: no cover
