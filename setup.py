from distutils.core import setup, Extension


extension_module2 = Extension(
    'pymanylinuxdemo.extension2',
     sources=['pymanylinuxdemo/extension2.c'],
     include_dirs=['pymanylinuxdemo/']
)

extension_module = Extension(
    'pymanylinuxdemo.extension',
     sources=['pymanylinuxdemo/extension.c'],
     library_dirs=['/usr/lib64/atlas/', '/usr/lib/atlas'],
     include_dirs=['/usr/include'],
     extra_objects=['pymanylinuxdemo/extension2.cpython-37m-x86_64-linux-gnu.so']
     libraries=['cblas']
)

setup(
    name = 'python-manylinux-demo',
    version = '1.1',
    description = 'This is a demo package with a compiled C extension.',
    ext_modules = [extension_module2, extension_module],
    packages=['pymanylinuxdemo', 'pymanylinuxdemo.tests'],
)
