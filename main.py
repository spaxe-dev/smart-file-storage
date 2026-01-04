import click
from sorter import runSort, undorun
from pathlib import Path

@click.group()

def cli():
    """Smart Storage CLI"""
    pass

# sort command
@cli.command()
@click.option('--source','-src','-s', default="input/", help='Sets source directory to be sorted.')
@click.option('--target','-t', default="sorted/", help='Sets destination directory of sorted files.')
@click.option('--dry', is_flag=True, help='Runs the sorter in dry mode for debugging')
def sort(source, target,dry):
    runSort(
        source = Path(source),
        target = Path(target),
        dry = dry
    )


#undo command
@cli.command()
def undo():
    undorun()

cli()