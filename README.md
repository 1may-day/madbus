madbus
======

This is a console tool for coil states managing via [modbus](https://en.wikipedia.org/wiki/Modbus) protocol.

Examples:
---------

python coils.py --host 127.0.0.1 --uid 1

1. : OFF

python coils.py --host 127.0.0.1

0. : ON
1. : OFF
2. : OFF
3. : OFF

python coils.py --host 127.0.0.1 --on --uid 1

1. : ON

python coils.py --host 127.0.0.1 --on

0. : ON
1. : ON
2. : ON
3. : ON

python coils.py --host 127.0.0.1 --off --uid 1

1. : OFF

python coils.py --host 127.0.0.1 --off

0. : OFF
1. : OFF
2. : OFF
3. : OFF
