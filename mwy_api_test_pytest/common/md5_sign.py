import hashlib


def md5vale(key):
    input_name = hashlib.md5()

    input_name.update(key.encode("utf-8"))

    print(key, "  ---->  ", input_name.hexdigest())


md5vale("哈哈")
