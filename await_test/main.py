from fastapi import BackgroundTasks, FastAPI
import time


app = FastAPI()

# async/awaitを使用する必要があるケースは
# メール送信処理など、時間がかかる処理を行う場合や重いI/O処理を行う場合(SQLAlchemyでは非同期に対応しているのでcreate_async_engine, AsyncSessionを使う場合tukaubaai)
# またはフレームワークの機能を使用する場合や、外部のAPIを叩く場合にawaitを使用する必要がある場合など

# 例えば、メール送信処理を行う場合、メール送信処理が終わるまでレスポンスを返すことができない
# そのため、メール送信処理をキューに追加し、レスポンスを返すことで、メール送信処理を非同期で行うことができる
# このような場合には、fastAPIのBackgroundTasksを使用する
# BackgroundTasksを使用する場合には、async/awaitを使用する必要がある

def send_email(email: str, message: str):
    # メール送信処理
    # 10秒待機
    time.sleep(10)
    print("メール送信処理")

@app.post("/send-email")
async def send_email_view(email: str, message: str, background_tasks: BackgroundTasks):
    # メール送信処理をキューに追加
    background_tasks.add_task(send_email, email, message)
    # レスポンスを返す
    return {"message": "Email has been sent"}