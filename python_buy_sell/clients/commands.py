import click 

from python_buy_sell.clients.models import Client
from python_buy_sell.clients.services import ClientService


@click.group()
def clients():
    """Manages he clients lifecycle"""
    pass


@clients.command()
@click.option('-n', '--name',
              type=str,
              prompt='Your name',
              help='The client name')
@click.option('-c', '--company',
              type=str,
              prompt=True,
              help='The client company')
@click.option('-e', '--email',
              type=str,
              prompt=True,
              help='The client email')
@click.option('-p', '--position',
              type=str,
              prompt=True,
              help='The client position')              
@click.pass_context
def create(ctx, name, company, email, position):
    """Creates a new client"""
    client = Client(name, company, email, position)
    client_service = ClientService(ctx.obj['clients_table'])

    client_service.create_client(client)

@clients.command()
@click.pass_context
def list(ctx):
    """list all clients"""
    pass


@clients.command()
@click.pass_context
def update(ctx, uid):
    """Updates a client"""
    pass


@clients.command()
@click.pass_context
def delete(ctx, uid):
    """deletes a client"""
    pass

all = clients
