from __future__ import unicode_literals
from __future__ import print_function

import argparse

from pymodbus.client.sync import ModbusTcpClient


MODBUS_PORT = 502
MAX_COILS_COUNT = 512


def _status(state):
    return '\033[92mON\033[0m' if state else '\033[91mOFF\033[0m'


def read_states(host, port=MODBUS_PORT, uid=None):
    client = ModbusTcpClient(host, port)
    try:
        if uid is not None:
            result = client.read_coils(uid, 1)
            print('{:3d} : {}'.format(uid, _status(result.bits[0])))
        else:
            result = client.read_coils(0, MAX_COILS_COUNT)
            for i in range(len(result.bits)):
                print('{:3d} : {}'.format(i, _status(result.bits[i])))
    finally:
        client.close()


def turn_states(host, port=MODBUS_PORT, state=False, uid=None):
    client = ModbusTcpClient(host, port)
    try:
        if uid is not None:
            client.write_coil(uid, state)
            result = client.read_coils(uid, 1)
            print('{:3d} : {}'.format(uid, _status(result.bits[0])))
        else:
            values = [state for _ in range(MAX_COILS_COUNT)]
            client.write_coils(0, values)
            result = client.read_coils(0, MAX_COILS_COUNT)
            for i in range(len(result.bits)):
                print('{:3d} : {}'.format(i, _status(result.bits[i])))
    finally:
        client.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Turn on/off device\'s coils using modbus protocol')
    parser.add_argument('--host', type=str,
                        help='hostname or ip-address of modbus devise')
    parser.add_argument('--port', type=int, default=MODBUS_PORT,
                        help=('port of modbus devise, '
                              'by default is {}'.format(MODBUS_PORT)))
    parser.add_argument('--uid', type=int, default=None,
                        help='specific coil index')
    parser.add_argument('--off', dest='turn_off',
                        action='store_const', const=True,
                        help='turn off coils')
    parser.add_argument('--on', dest='turn_on',
                        action='store_const', const=True,
                        help='turn on coils')
    parser.print_help()
    args = parser.parse_args()

    if args.host and args.port:
        if args.turn_on or args.turn_off:
            turn_states(args.host, args.port,
                        state=args.turn_on and not args.turn_off,
                        uid=args.uid)
        else:
            read_states(args.host, args.port, uid=args.uid)
