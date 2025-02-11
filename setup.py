from setuptools import find_packages, setup


setup(
    name="animatools",
    version="0.1",
    description="A collection of tools to help with data conversion from/to "
                "Anima-compatible version",
    author="Emmanuel Caruyer",
    author_email='Emmanuel.Caruyer@irisa.fr',
    platforms=["any"],
    license="",
    packages=find_packages(),
    install_requires=[],
    scripts=[
      "scripts/animatools_convert_bvecs",
      "scripts/animatools_download_hcp",
    ]
)
