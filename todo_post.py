from users.models import User
from todolist.models import Todo


# DB上でusernameがadminに該当するやつ、というクエリをmeにブチ込む
# ここの指定をいい感じにログイン情報とかを割り当てると多分良い
me = User.objects.get(
    username='suzuki',
)

# user_idは上記で設定した`username=suzuki`という検索条件でよしなにIDを引っこ抜いてくれるから、細かい指定はしなくて良い。
# あとは適当
Todo.objects.create(
    user_id=me,
    title='suzuki_mk2',
    memo='sp is su-pa-chakuchi',
)
