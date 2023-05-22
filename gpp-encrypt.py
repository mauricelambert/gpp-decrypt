#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###################
#    This little script encrypts password to gpp cpassword. It useful to
#    create vulnerable lab AD.
#    Copyright (C) 2023  gpp-encrypt

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
###################

'''
This little script encrypts password to gpp cpassword. It useful to
create vulnerable lab AD.
'''

__version__ = "0.0.1"
__author__ = "Maurice Lambert"
__author_email__ = "mauricelambert434@gmail.com"
__maintainer__ = "Maurice Lambert"
__maintainer_email__ = "mauricelambert434@gmail.com"
__description__ = '''
This little script encrypts password to gpp cpassword. It useful to
create vulnerable lab AD.
'''
__url__ = "https://github.com/mauricelambert/gpp-encrypt"

# __all__ = []

__license__ = "GPL-3.0 License"
__copyright__ = '''
gpp-encrypt  Copyright (C) 2023  Maurice Lambert
This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it
under certain conditions.
'''
copyright = __copyright__
license = __license__

print(copyright)

from base64 import b64encode
from Crypto.Cipher import AES
from sys import argv, stderr, exit

if len(argv) < 1:
    print("USAGES: gpp-encrypt [cpassword 1] [cpassword 2] ... [cpassword N]", file=stderr)
    exit(1)

key = b'\x4e\x99\x06\xe8\xfc\xb6\x6c\xc9\xfa\xf4\x93\x10\x62\x0f\xfe\xe8' \
      b'\xf4\x96\xe8\x06\xcc\x05\x79\x90\x20\x9b\x09\xa4\x33\xb6\x6c\x1b'
iv = b'\x00' * 16

for cpassword in argv[1:]:
    aes = AES.new(key, AES.MODE_CBC, iv)
    cpassword = ''.join(x + "\x00" for x in cpassword)
    padding = (16 - len(cpassword) % 16)
    print("[+] Encrypt:", cpassword, "->", b64encode(aes.encrypt(cpassword.encode('latin-1') + bytes([padding] * padding))).decode().rstrip('='))

exit(0)