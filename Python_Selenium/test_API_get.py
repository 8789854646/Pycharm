from  requests import request
from json import loads
from pytest import mark

headers ="code, expected_branch"

data = [
("HDFC0001755", "100 FEET ROAD-INDIRA NAGAR"),
    ("SBIN0040014", "GANDHI BAZZAR"),
    ("ICIC0000002", "BANGALORE - M G ROAD")
]
@mark.parametrize(headers, data)
def test_bank(code, expected_branch):
    url = f"https://ifsc.razorpay.com/{code}"
    print(url)
    response = request("GET", url)
    response_text = response.text
    d = loads(response_text)
    actual_branch = d['BRANCH']
    if actual_branch == expected_branch:
        print("PASS")
    else:
        print("FAIL")