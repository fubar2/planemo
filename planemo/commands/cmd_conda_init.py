import click

from planemo.cli import pass_context
from planemo.io import shell
from planemo import options
from planemo.conda import build_conda_context

from galaxy.tools.deps import conda_util


@click.command('conda_init')
@options.conda_target_options()
@pass_context
def cli(ctx, **kwds):
    """Download and install conda.

    This will download conda for managing dependencies for your platform
    using the appropriate Miniconda installer.

    By running this command, you are agreeing to the terms of the conda
    license a 3-clause BSD 3 license. Please review full license at
    http://docs.continuum.io/anaconda/eula.
    """
    conda_context = build_conda_context(**kwds)
    return conda_util.install_conda(conda_context=conda_context,
                                    shell_exec=shell)
