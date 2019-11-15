# -*- coding: utf-8 -*-

"""Console script for python_buy_sell."""
import sys
import click
from python_buy_sell.clients import commands as clients_commands

CLIENTS_TABLE = '.clients.csv'

@click.group()
@click.pass_context
def main(ctx, args=None):
    """Console script for buy_sell."""
    
    ctx.obj = {}
    ctx.obj['clients_table'] = CLIENTS_TABLE

main.add_command(clients_commands.all)
