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

### If you want to show the memory changes of a method
1. Install package. `pip install memory_profile`
2. Add a decorator on function
```python
import profile

@profile
def method_to_log():
    pass
```

### If you need to generate memory figure
1. install package. `pip install matplotlib`
2. record memory changes. `mprof run item_recorder.py`
3. display image. `mprof plot mprofile_xxx.dat`, `xxx` like a timestamp auto generated


### If you need to record object growth
The `objgraph.growth` will show the increase in peak object counts since last call.
Default is Top 10.
1. install package. `pip install objgraph`
2. add code
```python
import objgraph
...# some code above...
objgraph.show_growth()

# If the program like a event-loop
# Try to catch `KeyboardInterrupt` event, like:
try:
    pass
except KeyboardInterrupt as e:
    objgraph.show_growth()

```

### To fix the memory leak
Uncomment the line in `src/__init__.py`, or disable `debug` mode.
```python
# app.config.update(SQLALCHEMY_RECORD_QUERIES=False)
```