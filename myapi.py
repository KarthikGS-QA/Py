import requests


url="http://localhost/company/saveemployee.php"

def saveEmp( name ):


    param={
        "name": name 
    }

    resp=requests.post(url,params=param)

    print(f"response = {resp.status_code}")

    print(f"response text = {resp.text}")