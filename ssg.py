import typer
from ssg.site import Site
from ssg.parsers import ResourceParser


def main(source="content", dest="dist"):
    config = {"source": source, "dest": dest, "parsers": [ResourceParser()]}
    Site(**config).build()


typer.run(main)