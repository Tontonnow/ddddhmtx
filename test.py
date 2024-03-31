from ctypes import *


class TxChaCha:
    dll = cdll.LoadLibrary("chachagcc.dll")

    def __init__(self):
        self.instance = self.dll.init_wasm()
        self.wasm_prepareParam = self.dll.wasm_prepareParam
        self.wasm_prepareParam.argtypes = [c_char_p, c_char_p, c_char_p, c_int, c_int]
        self.get_key_iv = self.dll.get_key_iv
        self.get_key_iv.restype = c_char_p
        self.get_key_iv.argtypes = []
        self.wasm_decryptTS = self.dll.wasm_decryptTS
        self.wasm_decryptTS.argtypes = [c_char_p, c_char_p]

    def prepareParam(self, link_vid: bytes, base: bytes, appVer: bytes, tm: int, platform: int):
        return self.wasm_prepareParam(link_vid, base, appVer, tm, platform)

    def decryptTS(self, inputName: bytes, outputName: bytes):
        return self.wasm_decryptTS(inputName, outputName)

    def get_key_iv(self):
        return self.get_key_iv().decode()


if __name__ == '__main__':
    link_vid = b"l004822rr6f"
    base = b"B349243E9A58BC6C726021466A9BB3F2444CE192C610E72A70A40F05E00D2787"
    appVer = b"13.8.0.2006"
    tm = 1711607526;
    platform = 3850603;
    cc = TxChaCha()
    cc.prepareParam(link_vid, base, appVer, tm, platform)
    key = cc.get_key_iv()
    if key:
        print(key)
        input = b"test.ts"
        out = b"test_out.ts"
        cc.decryptTS(input, out)
