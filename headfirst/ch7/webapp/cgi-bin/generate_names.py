import athletemodel
import json
import yate

names=athletemodel.get_names_from_store()
names_json=json.dumps(sorted(names))

print(yate.start_response('application/json'))
print(names_json)