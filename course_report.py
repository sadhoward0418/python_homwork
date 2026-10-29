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

def clean_expense(raw):
    """
    處理一筆原始支出：
    - 清理日期、類別與備註
    - 將金額轉成 float
    - 回傳一個新的整理後 Dictionary
    """
    return {
        "date": clean_text(raw.get("date", "")),
        "category": clean_text(raw.get("category", "")),
        "amount": float(raw.get("amount", 0)),
        "note": clean_text(raw.get("note", "")),
    }

def clean_expenses(raw_list):
    """
    處理多筆原始支出：
    - 建立空的 expenses List
    - 使用 for 逐筆呼叫 clean_expense()
    - 使用 append() 保存每筆整理後資料
    - 回傳 expenses
    """
    expenses = []
    for raw in raw_list:
        cleaned_item = clean_expense(raw)
        expenses.append(cleaned_item)
    return expenses


# 1. 讀取預算（存入變數備用）
budget = float(input("請輸入本月預算："))

# 2. 呼叫 clean_expenses 進行資料清洗
expenses = clean_expenses(raw_expenses)

# 3. 印出清洗後的結果來檢查
print("\n--- 清洗後的資料檢查 ---")
for item in expenses:
    print(item)