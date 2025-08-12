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
        # 75歳以上の料金：500円
        if self.age >= 75:
            return 500
        # シニア料金(65歳以上): 1200円
        elif self.age >= 65:
            return 1200
        # おとな料金(20歳以上65歳未満): 1500円
        elif self.age >= 20:
            return 1500
        # こども料金(4歳以上20歳未満): 1000円
        elif self.age > 3:
            return 1000
        return 0

    # CSV形式で出力する関数
    def info_csv(self):
        text = f"{self.full_name()},{self.age},{self.entry_fee()}"
        return text

    # タブ区切りで出力する関数
    def info_tab(self):
        text = f"{self.full_name()}\t{self.age}\t{self.entry_fee()}"
        return text

    # パイプ区切りで出力する関数
    def info_pipe(self):
        text = f"{self.full_name()}|{self.age}|{self.entry_fee()}"
        return text


# インスタンス化
ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
tom = Customer(first_name="Tom", family_name="Ford", age=57)
ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=75)
michelle = Customer(first_name="Michelle", family_name="Tanner", age=3)


# C-5. 3歳以下の入場料金の無料化
print(michelle.entry_fee())  # 0 という値を出力

# C-6. 75歳以上の料金区分の追加
print(ieyasu.entry_fee())  # 500 という値を出力

# C-7. 単一顧客の情報取得形式の追加その1
print(ken.info_tab())
print(tom.info_tab())
print(ieyasu.info_tab())
print(michelle.info_tab())

# C-8. 単一顧客の情報取得形式の追加その2
print(ken.info_pipe())
print(tom.info_pipe())
print(ieyasu.info_pipe())
print(michelle.info_pipe())
