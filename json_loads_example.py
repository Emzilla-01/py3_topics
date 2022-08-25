# Emy Kay's original off-the-cuff example to explain usage of json.loads

import json
from pprint import pprint
fp='arbitrary.json'
with open(fp, 'rt') as f_:
    s = f_.read()
    j = json.loads(s)

pprint(list([s1[27:-1] for s1 in j.keys()]))
