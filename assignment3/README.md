# instapy

Apply beautiful filters to your images with `instapy`!


### Installation

Installation is straightforward with `pip`; simply clone this repository and run
```
pip install .
```
from within the project directory.


### Usage

The package can be imported in Python scripts, or run through the `instapy` script which is created during installation. Run `instapy -h` to see the available options which can be passed to the script:
```
usage: instapy [-h] [-o OUT] [-i {python,numba,numpy,cython}] [-fi {gray,sepia}] [-fa FACTOR] [-sc {upscale,downscale}] file

positional arguments:
  file                  The filename to apply filter to

options:
  -h, --help            show this help message and exit
  -o OUT, --out OUT     The output filename
  -i {python,numba,numpy,cython}, --implementation {python,numba,numpy,cython}
                        The implementation
  -fi {gray,sepia}, --filter {gray,sepia}
                        Select filter
  -fa FACTOR, --factor FACTOR
                        Scale factor to resize image
  -sc {upscale,downscale}, --scale {upscale,downscale}
                        Select upscaling or downscaling of image
```

Run example

Structure (if you want to import)
