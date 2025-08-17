class CharacterMixin:
    def normal_attack(self, name):
        print(f'{name}が攻撃しました。')
        print(f'敵に{self.power}のダメージを与えました')

    def show_attack_power(self):
        print(f"攻撃力は{self.power}")

    def show_skill(self):
        print(f"持っている職業スキルは{self.skill}")

    def show_status(self):
        print(f'HP:{self.HP} MP:{self.MP} 攻撃力:{self.power} スキル:{self.skill}')

class MagicMixin:
    def io_attack(self, name):
        if self.skill.get("イオ", 0):
            print(f'{name}がイオを唱えました。')

    def mera_attack(self, name):
        if self.skill.get("メラ", 0):
            print(f'{name}がメラを唱えました。')

class WarriorMixin:
    def defence(self, name):
        print(f'{name}が敵の攻撃を受け流しました。')

    def charge(self, name):
        print(f'{name}が「ためる」を使いました。')

class Character():
    def __init__(self, HP, MP, power=0, skill=None) -> None:
        self.HP = HP
        self.MP = MP
        self.power = power
        self.skill = skill if skill is not None else {}

class Wizard(Character, CharacterMixin, MagicMixin):
    pass

class Warrior(Character, CharacterMixin, WarriorMixin):
    pass

class Player():
    def __init__(self, name: str, job: Character) -> None:
        self.job = job
        self.name = name

if __name__ == "__main__":

    # 職業クラス
    wizard = Wizard(HP=30, MP=30, power=10, skill={"メラ": 1, "イオ": 1})
    warrior = Warrior(HP=50, MP=0, power= 30, skill={"受け流し" : 1,"ためる": 1})

    # Playerクラス
    marin = Player(name="マリン", job=wizard)
    tuyoshi = Player(name='ツヨシ', job=warrior)

    # 名前の表示
    print("Player Name:", marin.name)
    # ステータスの表示
    marin.job.show_status()

    # できる攻撃
    marin.job.normal_attack(marin.name)
    marin.job.io_attack(marin.name)
    marin.job.mera_attack(marin.name) 

    print('-------')
    tuyoshi.job.show_status()
    tuyoshi.job.normal_attack(tuyoshi.name)
    tuyoshi.job.defence(tuyoshi.name)
    tuyoshi.job.charge(tuyoshi.name)


