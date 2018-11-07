import requests

url = 'https://hooks.slack.com/services/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'

message = {
    "fallback": "Required text summary of the attachment that is shown by clients that understand attachments but choose not to show them.",

    "text": "Optional text that should appear within the attachment",
    "pretext": "Optional text that should appear above the formatted data",

    "color": "#36a64f",


    "fields": [
                {
                    "title": "Required Field Title",
                    "value": "Text value of the field. May contain standard message markup and must be escaped as normal. May be multi-line.",
                    "short": false
                }
    ]
}

slack = requests.post(
    url, json=message)
