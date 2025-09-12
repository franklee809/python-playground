### application on os scandir
# import os

# with os.scandir(".") as entries:
#     for entry in entries:
#         print(entry)
#         print(entry.name, "->", entry.stat().st_size, "bytes")


## applying on the threading lock
# from decimal import Decimal, localcontext
# from typing import final

# with localcontext() as ctx:
#     ctx.prec = 42
#     print(Decimal("1") / Decimal(42))

# import threading

# balance_lock = threading.lock()

# balance_lock.acquire()

# with balance_lock:
#     pass


### pytest exception

#    with pytest.raises(ZeroDivisionError):
#             divide_by_zero(10)
