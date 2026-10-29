raw_expenses = [
    {
        "date": " 2026-10-01 ",
        "category": "早餐",
        "amount": "85",
        "note": " 便利商店 ",
    },
    {
        "date": "2026-10-02",
        "category": "交通 ",
        "amount": "120",
        "note": "捷運",
    },
    {
        "date": "2026-10-03",
        "category": "日用品",
        "amount": " 350 ",
        "note": "洗衣精",
    },
    {
        "date": "2026-10-04",
        "category": "晚餐",
        "amount": "240",
        "note": "",
    },
    {
        "date": "2026-10-05",
        "category": "交通",
        "amount": "60",
    },
]
input("請輸入本月預算：")

def clean_text(text, default="未填寫"):
    """
    清理文字：
    1. 移除前後空白。
    2. 若清理後為空字串，則回傳指定的預設值。
    3. 否則回傳清理後的文字。
    """
    cleaned = text.strip()
    if cleaned == "":
        return default
    return cleaned