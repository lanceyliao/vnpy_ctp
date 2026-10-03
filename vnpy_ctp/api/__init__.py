"""导出 CTP 行情、交易接口及常量。"""

from .ctp_constant import *     # noqa


def __getattr__(name: str):
    if name == "MdApi":
        from .vnctpmd import MdApi
        globals()[name] = MdApi
        return MdApi
    if name == "TdApi":
        from .vnctptd import TdApi
        globals()[name] = TdApi
        return TdApi
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

