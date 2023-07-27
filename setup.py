from setuptools import setup, find_packages

setup(
    name="tangods_w1thermsensor",
    version="0.0.1",
    description="Tango device for w1thermistor",
    author="Daniel Schick",
    author_email="dschick@mbi-berlin.de",
    python_requires=">=3.6",
    entry_points={"console_scripts": ["TemperatureProbe = tangods_w1thermsensor:main"]},
    license="MIT",
    packages=["tangods_w1thermsensor"],
    install_requires=[
        "pytango",
        "w1thermsensor",
    ],
    url="https://github.com/MBI-Div-b/pytango-w1thermsensor",
    keywords=[
        "tango device",
        "tango",
        "pytango",
    ],
)
