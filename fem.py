import json, sys
print("FEM Sending Eiffel Event...")
with open('event.json') as f:
    event = json.load(f)
    print("Event Type:", event.get('meta', {}).get('type', 'Unknown'))
EOF

# Sample Eiffel event
cat <<EOF > event.json
{
  "meta": {
    "type": "EiffelActivityTriggeredEvent",
    "version": "3.0.0",
    "time": 1627845123123
  },
  "data": {
    "name": "TestActivity"
  }
}
