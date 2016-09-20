from distutils.core import setup
import py2exe
setup(
    windows=[{"script":"wall_v0.2.pyw"}],
    options={"py2exe": {"includes":["sip"]}}
)
