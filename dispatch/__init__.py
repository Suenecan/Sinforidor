import os
import glob
from importlib import import_module


_project_root = os.path.dirname(
    os.path.dirname(
        os.path.realpath(__file__)
    )
)

# print(_project_root)
spider_path = 'spiders/*.py'
all_spiders_path = glob.glob(os.path.join(_project_root, spider_path),  recursive=True)

_spiders = []
for path in all_spiders_path:
    file_path = os.path.relpath(path, _project_root)
    module_path = file_path.replace(os.sep, '.')[:-3]
    module = import_module(module_path)
    for attr in dir(module):
        var = getattr(module, attr)
        # 如果属性是class，且为BasicInfo的子类，且有cn_name属性
        if hasattr(var, 's_name'):
            _spiders.append(var)
