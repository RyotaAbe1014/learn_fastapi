from sqlalchemy import create_engine


# MySQL用
# user_name = "user"
# password = "password"
# host = "db"  
# database_name = "sample_db"

# DATABASE = 'mysql://%s:%s@%s/%s?charset=utf8' % (
#     user_name,
#     password,
#     host,
#     database_name,
# )

# SQLite
DATABASE = "sqlite:///test.db"

# DBに接続する
ENGINE = create_engine(
    DATABASE,
    encoding="utf-8",
    echo=True
)


