# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     models.py
   Author:        FesonX
   Email:         fesonx@foxmail.com
   GitHub:        github.com/FesonX
   date:          20-2-10
-------------------------------------------------
"""

from src import db
from sqlalchemy.sql import func, text


class Item(db.Model):
    __tablename__ = 'tbl_item'
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), server_default="")
    price = db.Column(db.DECIMAL(13, 11), server_default=text('0.0'))
    create_time = db.Column(db.DateTime, server_default=func.now())
    update_time = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())

    def __repr__(self):
        return '<Item: {id} {name} {price}>'.format(id=self.id, name=self.name, price=self.price)


class Repository(db.Model):
    __tablename__ = 'tbl_repository'
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), server_default="")
    avg_price = db.Column(db.DECIMAL(13, 11), server_default=text("0.0"))
    total = db.Column(db.BigInteger, server_default=text("0.0"))
    create_time = db.Column(db.DateTime, server_default=func.now())
    update_time = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())

    def __repr__(self):
        return '<Repository: {id} {name} {avg_price} {total}>'.format(id=self.id, name=self.name,
                                                                      avg_price=self.avg_price, total=self.total)


if __name__ == '__main__':
    db.create_all()
