from distutils.core import setup, Extension
 
module_dbr = Extension('dbr', 
                        sources = ['dbr.c'], 
                        include_dirs=['/System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python/numpy/core/include/numpy', './include'],
                        library_dirs=['./lib'],
                        libraries=['DynamsoftBarcodeReader'])
 
setup (name = 'DynamsoftBarcodeReader',
        version = '1.0',
        description = 'Python barcode extension',
        ext_modules = [module_dbr])