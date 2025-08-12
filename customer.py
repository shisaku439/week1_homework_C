class Customer:
    # 各問のコードが期待通り動作するように実装
    def __init__(self, first_name, family_name, age) -> None:
        self.first_name = first_name
        self.family_name = family_name
        self.age = age

    # フルネーム関数
    def full_name(self):
        text = f"{self.first_name} {self.family_name}"
        return text

    # 入場料計算関数
    def entry_fee(self):
        # シニア料金(65歳以上): 1200円
        if self.age >= 75:
            return 500
        elif self.age >= 65:
            return 1200
        # おとな料金(20歳以上65歳未満): 1500円
        elif self.age >= 20:
            return 1500
        # こども料金(4歳以上20歳未満): 1000円
        elif self.age > 3:
            return 1000
        return 0

    # CSV形式で出力関数
    def info_csv(self):
        text = f"{self.full_name()},{self.age},{self.entry_fee()}"
        return text


# インスタンス化
ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
tom = Customer(first_name="Tom", family_name="Ford", age=57)
ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=75)
michelle = Customer(first_name="Michelle", family_name="Tanner", age=3)

# C-1. フルネームを取得できる
print(ken.full_name())  # "Ken Tanaka" という値を出力
print(tom.full_name())  # "Tom Ford" という値を出力
print(ieyasu.full_name())  # "Ieyasu Tokugawa" という値を出力

# C-2. 年齢という概念の追加
print(ken.age)  # 15 という値を出力
print(tom.age)  # 57 という値を出力
print(ieyasu.age)  # 75 という値を出力

# C-3. 年齢に応じた適切な入場料(entry_fee)を計算できる
print(ken.entry_fee())  # 1000 という値を出力
print(tom.entry_fee())  # 1500 という値を出力
print(ieyasu.entry_fee())  # 1200 という値を出力

# C-4. 単一の顧客情報をCSV形式で取得できる
print(ken.info_csv())  # "Ken Tanaka,15,1000" という値を出力
print(tom.info_csv())  # "Tom Ford,57,1500" という値を出力
print(ieyasu.info_csv())  # "Ieyasu Tokugawa,75,1200" という値を出力

# C-5. 3歳以下の入場料金の無料化
print(ken.entry_fee())  # 1000 という値を出力
print(tom.entry_fee())  # 1500 という値を出力
print(ieyasu.entry_fee())  # 1200 という値を出力
print(michelle.entry_fee())  # 0 という値を出力

# C-6. 75歳以上の料金区分の追加
print(ken.entry_fee())  # 1000 という値を出力
print(tom.entry_fee())  # 1500 という値を出力
print(ieyasu.entry_fee())  # 500 という値を出力
print(michelle.entry_fee())  # 0 という値を出力
