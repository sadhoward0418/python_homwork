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


def get_amount(expense):
    """
    取得一筆支出的金額：
    - 輸入：一筆整理後的支出 Dictionary
    - 回傳 amount
    - 提供給 sorted() 作為排序依據
    """
    return expense["amount"]


def validate_expense(expense):
    """
    檢查一筆整理後的支出：
    - 日期不可為空白
    - 類別不可為空白
    - 金額必須大於 0
    - 備註不可為空白
    - 回傳 True 或 False
    """
    if not expense["date"]:
        return False
    if not expense["category"]:
        return False
    if expense["amount"] <= 0:
        return False
    if not expense["note"]:
        return False
    return True


def print_report(expenses_list, budget):
    """
    輸出支出報表：
    - 輸入：整理後的 expenses 與使用者輸入的 budget
    - 完成統計、判斷與格式化輸出
    """
    # 依照題目資料流程：使用 validate_expense 篩選/驗證資料
    valid_expenses = [item for item in expenses_list if validate_expense(item)]

    # 1. 依金額由大到小排序
    sorted_expenses = sorted(valid_expenses, key=get_amount, reverse=True)

    # 2. 統計數據
    total_count = len(sorted_expenses)
    total_amount = sum(item["amount"] for item in sorted_expenses)
    avg_amount = total_amount / total_count if total_count > 0 else 0
    max_amount = max(item["amount"] for item in sorted_expenses)
    min_amount = min(item["amount"] for item in sorted_expenses)

    # 3. 預算判斷與剩餘計算
    diff = budget - total_amount
    if total_amount <= budget:
        budget_status = "尚未超支"
        budget_label = f"剩餘預算：{diff:,.2f} 元"
    else:
        budget_status = "已超支"
        budget_label = f"超支金額：{abs(diff):,.2f} 元"

    # 4. 檢驗函式應用 (any / all)
    has_large_expense = any(item["amount"] >= 500 for item in sorted_expenses)
    all_valid_amount = all(item["amount"] > 0 for item in sorted_expenses)

    # 5. 輸出報表內容
    print("\n--- 家庭月度支出報表 ---")
    for index, item in enumerate(sorted_expenses, start=1):
        # 計算佔總支出比例
        ratio = item["amount"] / total_amount if total_amount > 0 else 0
        # 格式化輸出每筆支出（嚴格套用指定格式碼）
        print(
            f"{index:02d}. {item['date']} {item['category']:<8} "
            f"{item['amount']:>8.2f} 元  占比 {ratio:.1%}  {item['note']}"
        )

    print()
    print(f"支出筆數：{total_count} 筆")
    print(f"總支出：{total_amount:,.2f} 元")
    print(f"平均每筆：{avg_amount:,.2f} 元")
    print(f"最高支出：{max_amount:,.2f} 元")
    print(f"最低支出：{min_amount:,.2f} 元")
    print(f"本月預算：{budget:,.2f} 元")
    print(budget_label)
    print(f"預算狀態：{budget_status}")
    print(f"是否有單筆支出達 500 元：{has_large_expense}")
    print(f"所有支出金額是否有效：{all_valid_amount}")


# 主程式進入點：維持單一乾淨的輸入與執行流程
if __name__ == "__main__":
    budget = float(input("請輸入本月預算："))
    expenses = clean_expenses(raw_expenses)
    print_report(expenses, budget)