import setuptools

setuptools.setup(
    name="octopus_wpi",
    version="0.1",
    author="Richard Ingham",
    description="World Precision Instruments machines plugin for octopus.",
    url="https://github.com/richardingham/octopus_wpi",
    packages=['octopus.blocks', 'octopus.manufacturer'],
    
    entry_points={
        "blocktopus_blocks": [
            'aladdin_pump = octopus.blocks.wpi:machine_wpi_aladdin',
        ]
    }

    # install_requires=requirements,
    # include_package_data=True,
    # classifiers=[
    #     "Programming Language :: Python :: 3.5",
    #     "License :: OSI Approved :: MIT License",
    #     "Operating System :: OS Independent",
    # ],
)
