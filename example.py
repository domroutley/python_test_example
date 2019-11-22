def main(num, name):
    dict = {
        "fields": {
            "fake_custom": [
                {
                    "id": name
                },
                {
                    "id": num
                }
            ]
        }
    }

    myRequest(data=dict)

def myRequest(data=dict):
    pass
