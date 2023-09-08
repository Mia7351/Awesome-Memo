from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Memo(BaseModel):
    id: int
    content: str
    
memos = []

@app.post("/memos")
def create_memo(memo:Memo):
    memos.append(memo)
    return '메모추가에 성공했습니다'

@app.get("/memos")
def read_memo():
    return memos

@app.put("/memos/{memo_id}")
def put_memo(req_memo:Memo): #정의된 값을 메모라는 값으로 받아서
    for memo in memos:
        if memo.id==req_memo.id:
            memo.content=req_memo.content
            return 'Successful!'
    return 'Not Found Memo'

@app.delete("/memos/{memo_id}")
def delete_memo(memo_id:int):
    for index, memo in enumerate(memos):
        if memo.id==memo_id:
            memos.pop(index)  #pop! 탁 없앤다!
            return 'Memo Deleted'
    return 'Not Found Memo'
    

app.mount("/", StaticFiles(directory='static', html=True), name='static')