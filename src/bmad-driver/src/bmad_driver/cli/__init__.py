# SPDX-FileCopyrightText: 2026-present Rayshawn McCall <rayshawnmccall@gmail.com>
#
# SPDX-License-Identifier: MIT
import click

from bmad_driver.__about__ import __version__


@click.group(context_settings={"help_option_names": ["-h", "--help"]}, invoke_without_command=True)
@click.version_option(version=__version__, prog_name="bmad-driver")
def bmad_driver():
    click.echo("Hello world!")
