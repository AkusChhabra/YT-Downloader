from setuptools import setup

setup(
    name='yt-downloader',
    version='0.0.1',
    description='YouTube Downloader CLI',
    author='AC',
    packages=['yt_cli'],
    entry_points={
        'console_scripts': ['dyt=yt_cli.entry:cli_entry_point'],
    },
    install_requires=[
        'pytubefix',
        'argparse'
    ],
)