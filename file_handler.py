from pyexcel_xlsx import get_data
import json
PATH = ''
def load_zscore_renko_strategies():
    data = get_data("renko_strategies.xlsx")
    data = data[list(data.keys())[0]]

    for i in range(1, len(data)):
        data[i] = dict(zip(data[0], data[i]))

    del data[0]

    for d in data:
        d['zscore_length'] = int(d['zscore_length'])
        d['zscore_threshold'] = float(d['zscore_threshold'])
        d['brick_size'] = float(d['brick_size'])
        d['brick_count_to_enter'] = int(d['brick_count_to_enter'])
        d['brick_count_to_exit'] = int(d['brick_count_to_exit'])
        d['partial_exit_percent'] = float(d['partial_exit_percent'])
        d['partial_exit_count'] = int(d['partial_exit_count'])



    return data

def read_file(path, verbose=False):
    try:
        with open(path, 'r') as file:
            data = json.loads(file.read())
        return data
    except Exception as e:
        if verbose:
            print(f'{e} - Error reading file: {path}')
        return []