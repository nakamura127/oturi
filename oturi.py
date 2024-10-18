def calculate_change(n, x):
    # お釣りの計算
    change = n - x
    
    # 日本の硬貨リスト（高額順）
    coins = [500, 100, 50, 10]
    
    # 各硬貨の枚数を記録
    coin_count = {}
    
    # お釣りがない場合
    if change < 0:
        return "支払い額が足りません。"
    elif change == 0:
        return "お釣りはありません。"

    # 各硬貨でお釣りを計算
    for coin in coins:
        coin_count[coin] = change // coin  # 硬貨の枚数
        change %= coin  # 残りのお釣り

    return coin_count

# 入力例
n = int(input("支払い額を入力してください: "))
x = int(input("商品の金額を入力してください: "))

result = calculate_change(n, x)

if isinstance(result, str):
    print(result)
else:
    print("お釣りの硬貨の枚数は次の通りです:")
    for coin, count in result.items():
        print(f"{coin}円: {count}枚")
