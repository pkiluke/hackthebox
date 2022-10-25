from impacket.smbconnection import SMBConnection, smb
import click

@click.command()
@click.argument('ip')
@click.