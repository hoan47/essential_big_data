def build_no_accent_sql(field_name):
    """
    Trả về chuỗi SQL xử lý bỏ dấu cho một field trong Hive
    """
    replacements = [
        ("[áàảãạăắằẳẵặâấầẩẫậ]", "a"),
        ("[éèẻẽẹêếềểễệ]", "e"),
        ("[íìỉĩị]", "i"),
        ("[óòỏõọôốồổỗộơớờởỡợ]", "o"),
        ("[úùủũụưứừửữự]", "u"),
        ("[ýỳỷỹỵ]", "y"),
        ("[đ]", "d"),
    ]

    expr = f"lower({field_name})"
    for pattern, replacement in replacements:
        expr = f"regexp_replace({expr}, '{pattern}', '{replacement}')"
    return expr
