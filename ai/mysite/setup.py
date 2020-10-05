from distutils.core import Extension, setup
from Cython.Build import cythonize
import numpy

# # define an extension that will be cythonized and compiled
# ext = Extension(name="mysite", sources=["[yolo/darkflow/cython_utils/*]"])
# setup(ext_modules=cythonize(ext))


# setup(
#   name = 'mysite',
#   ext_modules = cythonize("yolo/darkflow/cython_utils/cy_yolo_findboxes.pyx"),
# )

fileSet = set()
fileSet.add("yolo/darkflow/cython_utils/cy_yolo_findboxes.pyx")
setup(
   ext_modules=cythonize(fileSet),
   include_dirs=[numpy.get_include()]
)