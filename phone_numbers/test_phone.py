import pytest
from phone_validator import is_valid_phone

# 使用 pytest.mark.parametrize 实现数据驱动测试
valid_phones = [
    "13800138000",   # 普通有效
    "13012345678",   # 第二位边界3
    "19912345678",   # 第二位边界9
    "18888888888",   # 全相同数字
]

invalid_phones = [
    # 长度问题
    ("1380013800", "长度不足11位"),
    ("138001380000", "长度超过11位"),
    # 首位错误
    ("23800138000", "首位不是1"),
    # 第二位错误
    ("12012345678", "第二位不在3-9"),
    ("11012345678", "第二位不在3-9"),
    # 含非数字字符
    ("1380013800a", "包含字母"),
    ("13800-38000", "包含连字符"),
    ("13800 38000", "包含空格"),
    # 空值/None
    ("", "空字符串"),
    (None, "None输入"),
    # 全角数字（若需求禁止）
    ("１３８００１３８０００", "全角数字"),
]

class TestPhoneValidation:
    @pytest.mark.parametrize("phone", valid_phones)
    def test_valid_phones(self, phone):
        assert is_valid_phone(phone) == True, f"{phone} 应该被判定为有效手机号"

    @pytest.mark.parametrize("phone,desc", invalid_phones)
    def test_invalid_phones(self, phone, desc):
        assert is_valid_phone(phone) == False, f"{phone} ({desc}) 应该被判定为无效"