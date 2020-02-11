# MemoryTest

## Install Guide
 
### Environment
1. Install interpreter, develop under `Python 3.6`
2. Install Python package`pip install -r requirements.txt`
3. Install `MySQL`

### Database Prepare
1. create your own db, create `instance` folder under project root path
2. create `config.py` under `instance` folder, add `SQLALCHEMY_DATABASE_URI`
3. run `src/models.py` to create table

## Run Memory Leaking Test

```shell
python item_recorder.py
```

### If you need to generate memory figure
1. install package. `pip install matplotlib`
2. record memory changes. `mprof run item_recorder.py`
3. display image. `mprof plot mprofile_xxx.dat`, `xxx` like a timestamp auto generated
