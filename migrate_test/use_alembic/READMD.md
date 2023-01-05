# alembicを用いてマイグレーションファイルを作成し管理する

## how to use
create migration file
```shell
alembic revision -m {ファイル名}
```
migrate
```shell
alembic upgrade head
```