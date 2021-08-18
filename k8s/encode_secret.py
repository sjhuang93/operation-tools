import sys, yaml, json, base64

def encode(str):
    bitObject = str.encode("UTF-8")
    encodeObject = base64.b64encode(bitObject)
    encodeStr = encodeObject.decode("UTF-8")
    return encodeStr
    

fileName = sys.argv[1]
with open(fileName, 'r') as f:
    yamlFile = f.read()
    
    jsonFile = yaml.load(yamlFile, Loader=yaml.FullLoader)
    data = jsonFile['data']

    for key, value in data.items():
        data[key] = encode(data[key])
    
    jsonFile['data'] = data
    encodeYamlFile = yaml.dump(jsonFile, default_flow_style=False)
    
encodeFileName = 'encode_' + sys.argv[1]
with open(encodeFileName, 'w') as f:
    f.write(encodeYamlFile)
    

