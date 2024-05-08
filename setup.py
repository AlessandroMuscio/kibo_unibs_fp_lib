from setuptools import setup
import os

VERSION = "1.1.1"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="kibo_unibs_fp_lib",
    description="kibo_unibs_fp_lib is now kibo_pgar_lib",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    version=VERSION,
    install_requires=["kibo_pgar_lib"],
    classifiers=["Development Status :: 7 - Inactive"],
)
