from setuptools import setup, find_packages

setup(
  name='SMC',
  version='1.0',
  packages=find_packages(),
  install_requires=['scratchattach'
  ],
  
  entry_points={
    "console_scripts": [
      "SMC = SMC:SMC",
    ],
  },


)
