import click
from sorter import runSort
from pathlib import Path
@click.command()
@click.option('--source','-src','-s', default="input/", help='Sets source directory to be sorted.')
@click.option('--target','-t', default="sorted/", help='Sets destination directory of sorted files.')
@click.option('--dry', is_flag=True, help='Runs the sorter in dry mode for debugging')
def smartsort(source, target,dry):
    runSort(
        source = Path(source),
        target = Path(target),
        dry = dry
    )

smartsort()