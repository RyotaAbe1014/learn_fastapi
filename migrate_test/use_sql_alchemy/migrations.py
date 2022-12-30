from sqlalchemy.orm import sessionmaker
import settings
import models
# セッションを作成する
Session = sessionmaker(bind=settings.ENGINE)
session = Session()

# テーブルを作成する
models.Base.metadata.create_all(settings.ENGINE)