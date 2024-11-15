from pydantic import BaseModel
from typing import List

class Event(BaseModel):
    id: int
    title: str
    image: str   # 이미지 경로
    description: str
    tags: List[str]
    location: str

    class Config:
        json_schema_extra = {
            "title": "fastapi study",
            "iamge": "http://www.test.com/1.jpg",
            "description": "간단한 설명을 추가하세요",
            "tags": ["python", "fastapi", "study"],
            "location": "google meet"
        }

