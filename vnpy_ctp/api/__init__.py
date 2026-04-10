from .ctp_constant import *     # noqa


def __getattr__(name: str):
    if name == "MdApi":
        from .vnctpmd import MdApi
        return MdApi
    if name == "TdApi":
        from .vnctptd import TdApi
        return TdApi
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
