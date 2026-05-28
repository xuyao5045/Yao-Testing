import re

def is_valid_phone(phone):
    """
    校验中国大陆手机号（简化规则）
    """
    if not isinstance(phone, str):
        return False
    # 规则：1开头，第二位3-9，后续9位数字，总长11位
    pattern = r'^1[3-9]\d{9}$'
    return bool(re.match(pattern, phone))