'''
Ukazka pouziti JSON parseru
'''
import json


def decode_json(json_data):
    '''
    Decode 'json_data' 
    '''
    data = json.loads(json_data)
    return data

if __name__ == '__main__':
    
    with open('example.json', encoding='utf-8') as fr:
        result = decode_json(fr.read())
    
    print(type(result)) 
    print(result['web-app'].keys())
    print(json.dumps(result, indent=3, sort_keys=True))
    
