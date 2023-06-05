from models import User,Comment
from sqlalchemy.orm import Session
from connect import engine
from main import session


user1=User(
    username="jona",
    email_address="andrew@gmail.com",
    comments=[
        Comment(text="Hellow world"),
        Comment(text="call me")
    ]
)

paul=User(
    username="paul",
    email_address="paul@gmail.com",
    comments=[
        Comment(text="Paul world"),
        Comment(text="call me")
    ]
)

cathy=User(
    username="Cathy",
    email_address="cathy@gmail.com"
)

session.add_all([user1,paul,cathy])
session.commit()