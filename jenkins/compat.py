# compat module for crypto functions
try:
    from Crypto.Cipher import AES
    from Crypto.Util.Padding import pad
except ImportError:
    try:
        from Cryptodome.Cipher import AES
        from Cryptodome.Util.Padding import pad
    except ImportError as imp_err:
        raise imp_err

__all__ = ['AES', 'pad']
