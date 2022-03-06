import json
import os
import sys

# To avoid relative import
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from limiter import limiter as limiter_func

import motor.motor_asyncio
import asyncio
import nest_asyncio
from typing import Optional

from fastapi import HTTPException, Request, Response
from fastapi.responses import RedirectResponse
from fastapi import APIRouter, HTTPException, Header

from pydantic import BaseModel

router = APIRouter(
    prefix="/user",
	tags=["User"],
	responses={404: {"description": "Not found"}},
)
limiter = limiter_func()

with open("./data.json", "r") as f:
    data = json.load(f)

# nest_asyncio.apply() # Apply in case of asyncio errors

cluster = motor.motor_asyncio.AsyncIOMotorClient(mongo_url)
# cluster.get_io_loop = asyncio.get_running_loop # # Apply in case of asyncio errors
us = cluster["fastapi"]["user"] # Connected to user collection of senarc database

class User(BaseModel):
    name : str
    email : str
    password : str

@router.post("/create", include_in_schema=True)
@limiter.limit("2/second")
async def create_user(request : Request, user: User):
    name = user.name
    email = user.email
    password = user.password
    data = await us.find_one({"_id" : name})
    if data is not None:
        raise HTTPException(status_code=400, detail="User already exists")
    await us.insert_one({"_id" : name, "email" : email, "password" : password})
    return {"message" : "User created"}

