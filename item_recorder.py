# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     item_recorder.py
   Author:        FesonX
   Email:         fesonx@foxmail.com
   GitHub:        github.com/FesonX
   date:          20-2-10
-------------------------------------------------
"""
# import profile
import random
from decimal import Decimal
from math import ceil
from time import sleep
from typing import Sequence

# import objgraph
from loguru import logger

from src import app
from src.dao import get_repository, save_all
from src.models import Item, Repository

ITEM_NAME_LIST = ['apple', 'sony', 'fujifilm', 'samsung', 'huawei', 'dji', 'meizu', 'xiaomi', 'acer', 'honor', 'dell',
                  'canon', 'panasonic', 'olympus', 'surface', 'redmi', 'onePlus', 'motorala', 'oppo', 'vivo', 'google',
                  'supersonic', 'kindle', 'asus', 'snapdragon', 'intel', 'universal', 'nokia_pureview']


def create_items(amount: int) -> Sequence[Item]:
    item_seq = list()
    for i in range(amount):
        item = Item(name=random.choice(ITEM_NAME_LIST) + '-' + str(random.randint(100, 150)),
                    price=random.randint(10, 20))
        item_seq.append(item)
        if (i + 1) % 100 == 0:
            logger.info('---- {} items created'.format(i + 1))
    return item_seq


def update_repository(exist_repo: Repository, new_repo: Repository):
    exist_repo.avg_price = round(
        (Decimal(new_repo.avg_price * new_repo.total) + exist_repo.avg_price * exist_repo.total) / (
                new_repo.total + exist_repo.total), 2)
    exist_repo.total += new_repo.total


# @profile
def process_item(item_seq: Sequence[Item]):
    item_name_set = set()
    repo_dict = dict()
    for item in item_seq:
        if item.name not in item_name_set:
            item_name_set.add(item.name)
            new_repo = Repository(name=item.name, avg_price=item.price, total=1)
            repo_dict.update({item.name: new_repo})
        else:
            new_repo = repo_dict.get(item.name)
            new_repo.avg_price = round((new_repo.avg_price * new_repo.total + item.price) / (new_repo.total + 1), 2)
            new_repo.total += 1
    repository_list = get_repository(item_name_set)
    exist_repo_dict = {i.name: i for i in repository_list}
    for exist_repo in exist_repo_dict:
        if repo_dict.get(exist_repo):
            new_repository = repo_dict.pop(exist_repo)
            repo = exist_repo_dict.get(exist_repo)
            update_repository(repo, new_repository)
    repository_list = list(repo_dict.values())
    repository_list.extend(item_seq)
    rtn_flag = save_all(repository_list)
    repository_list.clear()
    exist_repo_dict.clear()
    repo_dict.clear()
    return rtn_flag


if __name__ == '__main__':
    total = 100000
    per_page = 500
    total_pages = ceil(total / per_page)
    # Show the increase in peak object counts since last call. Default is Top 10
    # objgraph.show_growth()
    with app.app_context():
        for p in range(total_pages):
            temp_list = create_items(per_page)
            flag = process_item(temp_list)
            sleep(0.05)
            if flag:
                logger.info('---- {} items processed.'.format(per_page * (p + 1)))
            # if p == 1:
            #     # Show the increase in peak object counts since last call. Default is Top 10
            #     objgraph.show_growth()
        logger.info('All items has been processed.')
        # objgraph.show_growth()
