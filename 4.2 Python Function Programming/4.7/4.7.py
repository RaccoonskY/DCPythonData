# Реализация key-value хранилища
# TO DO: Рефакторинг кода для реализации вывода значений

import argparse
import  json
import os
import tempfile

parser = argparse.ArgumentParser()
parser.add_argument("--key", help="add key value with --val adding or show all values for specified key", type=str)
parser.add_argument("--val", help="add value to the key",type=str)
args = parser.parse_args()

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')


if args.key and args.val:
    try:
        with open(storage_path,'a') as file_input:
            data_input = {args.key: args.val}
            file_input.write(json.dumps(data_input)+"\n")
    except OSError:
        print(None)
elif args.key:
    try:
        with open(storage_path) as file_output:
            data = file_output.read().split('\n')
            data_transferd = [json.loads(i) for i in data if i != '']
            data_output = ""
            output_list = []
            for i in data_transferd:
                if args.key in i.keys():
                    output_list.append(i[args.key])
            count = len(output_list)
            for j in output_list:
                data_output+= j
                count -= 1
                if len(output_list) > 1 and count > 0:
                    data_output+=", "
            print(data_output)
    except OSError:
        print(None)
