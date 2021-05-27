import click
from app import application

#Changes the default help parameter to --help and -h instead of just --help
CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

#Decorator to convert main() into a terminal command and change help parameters
@click.command(context_settings=CONTEXT_SETTINGS)
#Deoractor to add [LENGTH] argument with default value to main()
@click.argument('length', default='10')
#Decorator to add [FORMAT] option with default value to main()
@click.option('-f', '--format', type=click.Choice(['1', '2', '3', '4']), default='3')
def main(length, format):
    #This text will be shown in the help page (-h, --help)
    """
    This program generates a random password of chosen [LENGTH] from 4 [FORMAT] options:\n
    1 - alphabetic lowercase\n
    2 - alphabetic mixed case\n
    3 - alphanumeric mixed case\n
    4 - alphanumeric mixed case + special characters

    The default password will be alphanumeric and 10 characters long.
    """
    click.echo(application.generate(int(length), int(format)))

