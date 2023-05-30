# Text Summarization API

## API Document
Here's a guide on how to use the API:

### API Endpoint
The API endpoint for summarizing text is a POST request to the following URL:
```
http://<server-url>/summarize/
```

### Request Format
The request should contain the text that needs to be summarized. The text should be sent as a JSON object with a single key 'text', and the value should be the text that needs to be summarized. For example:
```
{
    "text": "This is a long text that needs to be summarized."
}
```

### Response Format
The API response is a JSON object that contains the summarized text. The summarized text can be found under the key 'response'. For example:
```
{
    "response": "This is the summarized text."
}
```

### Example Usage
Here is an example of how to use the API using Python's `requests` library:
```python
import requests

url = 'http://<server-url>/summarize/'
data = {
    'text': 'This is a long text that needs to be summarized.'
}
response = requests.post(url, json=data)
print(response.json()['response'])
```

This will print the summarized text received from the API.