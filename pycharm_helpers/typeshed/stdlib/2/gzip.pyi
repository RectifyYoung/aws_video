# Stubs for gzip (Python 2)
#
# NOTE: Based on a dynamically typed stub automatically generated by stubgen.

from typing import Any, IO
import io

class GzipFile(io.BufferedIOBase):
    myfileobj = ...  # type: Any
    max_read_chunk = ...  # type: Any
    mode = ...  # type: Any
    extrabuf = ...  # type: Any
    extrasize = ...  # type: Any
    extrastart = ...  # type: Any
    name = ...  # type: Any
    min_readsize = ...  # type: Any
    compress = ...  # type: Any
    fileobj = ...  # type: Any
    offset = ...  # type: Any
    mtime = ...  # type: Any
    def __init__(self, filename: str = ..., mode: str = ..., compresslevel: int = ...,
                 fileobj: IO[str] = ..., mtime: float = ...) -> None: ...
    @property
    def filename(self): ...
    size = ...  # type: Any
    crc = ...  # type: Any
    def write(self, data): ...
    def read(self, size=...): ...
    @property
    def closed(self): ...
    def close(self): ...
    def flush(self, zlib_mode=...): ...
    def fileno(self): ...
    def rewind(self): ...
    def readable(self): ...
    def writable(self): ...
    def seekable(self): ...
    def seek(self, offset, whence=...): ...
    def readline(self, size=...): ...

def open(filename: str, mode: str = ..., compresslevel: int = ...) -> GzipFile: ...
