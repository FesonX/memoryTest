# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     dao.py
   Author:        FesonX
   Email:         fesonx@foxmail.com
   GitHub:        github.com/FesonX
   date:          20-2-10
-------------------------------------------------
"""
from typing import Sequence

from loguru import logger

from src import db
from src.models import Repository


def get_repository(item_names):
    if not item_names:
        return False
    try:
        if isinstance(item_names, str):
            base_query = Repository.query.filter(Repository.name == item_names)
        elif isinstance(item_names, (list, tuple, set, Sequence)):
            base_query = Repository.query.filter(Repository.name.in_(item_names))
        else:
            logger.warning('Unsupported Type')
            return False
        return base_query.all()
    except Exception as e:
        logger.exception(e)
        return False


def update():
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        logger.exception(e)
        return False
    return True


def save_all(item_list: Sequence):
    try:
        db.session.bulk_save_objects(item_list)
        db.session.commit()
    except Exception as e:
        db.rollback()
        logger.exception(e)
        return False
    return True
