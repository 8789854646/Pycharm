# from requests import request
# response = request("GET", "https://ifsc.razorpay.com/HDFC0001755")
# response_text = response.text
# print(response_text)

# from requests import request
# from json import loads
#
# response = request("GET","https://ifsc.razorpay.com/HDFC0001755")
# response_text = response.text
# #print(response_text)
#
# d = loads(response_text)
# print(d['RTGS'])


response = request("GET", "https://ifsc.razorpay.com/HDFC0001755")
response_text = response.text
print(response_text)

d = loads(response_text)
print(d['RTGS'])

if d['BRANCH'] == "100 FEET ROAD-INDIRA NAGAR":
    print("PASS")
else:
    print("FAIL")