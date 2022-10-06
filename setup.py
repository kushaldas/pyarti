from setuptools import setup
from setuptools_rust import Binding, RustExtension

setup(
    name="pyarti",
    version="0.0.2",
    rust_extensions=[RustExtension("pyarti.pyarti", binding=Binding.PyO3)],
    package_data={"pyarti": ["py.typed", "pyarti.pyi"]},
    packages=["pyarti"],
    # rust extensions are not zip safe, just like C-extensions.
    zip_safe=False,
)
