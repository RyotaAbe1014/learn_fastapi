import settings
import models


# テーブルを作成する
models.Base.metadata.create_all(settings.ENGINE)