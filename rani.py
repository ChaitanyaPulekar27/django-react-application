import requests
import json
import csv 

url = "https://www.pepperfry.com/homeapp-api/studio/getStudioPageData"

payload = json.dumps({
  "targetUrl" : "https://www.pepperfry.com/stores/cities?pageType=allCities&offset=40"
})
headers = {
  'accept': 'application/json, text/plain, /',
  'accept-language': 'en-US,en;q=0.9,hi;q=0.8',
  'content-type': 'application/json',
  'cookie': '_gcl_au=1.1.1745416754.1714414253; header_flash_cookie=1; segment_token=589b08b3f2e32b155d3bd49de3883014bda9479d3e45def29578c4c8e2a029cd; frontend=e4d63a696899521a022eea9d4c48fa049f8b696648fc9dab320ebc19e74a7d3f; mid=7851ebd3e874afdc016355c7ad1b65f56f483b164ce4a3ffc1c1f0b232a5da1c; unbxd.userId=uid-1714414255141-41579; _gid=GA1.2.1198010183.1714414256; mfKey=1qzu1md.1714414255921; _fbp=fb.1.1714414256614.1658793128; user_id_t=ab41d3a0-ccbf-44f5-8673-c4936a235a48; ajs_anonymous_id=66628a8b-900f-41f6-a2c9-da9bfeb4c588; __rtbh.lid=%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%22UCbcTtqYCRmbehSDJ4kx%22%7D; uid=7851ebd3e874afdc016355c7ad1b65f56f483b164ce4a3ffc1c1f0b232a5da1c; PWA Icon/Browser cookie=Browser; tr_utm_camp=CPS_6618fc1750c02003491d091c_109361; __tr_utms=vcinternet; __tr_utmd=affiliate; _dc_gtm_UA-25959246-1=1; unbxd.visit=repeat; unbxd.visitId=visitId-1714419019637-19514; _ga_F1NJ1E2HJ2=GS1.1.1714419025.3.1.1714419043.0.0.0; _gat_UA-25959246-9=1; __tr_jr=W3sidXRtcyI6InZjaW50ZXJuZXQiLCJ0cyI6IjIwMjQtMDQtMjlUMTk6MzA6NDMuOTg1WiIsInV0bWMiOiJDUFNfNjYxOGZjMTc1MGMwMjAwMzQ5MWQwOTFjXzEwOTM2MSIsInV0bWQiOiJhZmZpbGlhdGUifV0=; cto_bundle=HCnZxF9seHNtR3dPU0RHVkFTTyUyQjNwVURRWVM4NUc5eGVvcm9Lc1g4dnJwNFVwJTJCM1RwV3ZhTmhPQlo2VzEyYlZaSmRUQSUyQkVKQ3hlWWUwelNqNGklMkJHZSUyRngzOXRZcFhITmVxekJOUVJ4WHhMSXN4blhzWXQlMkJMb2QyajNEJTJGYUZJJTJCbFFoYUZVblJ0SjZVemRCcTB0JTJGTEY4QWpkMDQ4bmpOOUZONEhRN25JaWxjRnFZRnglMkJkVXlKZlZqWTFFVnZ1c3dGcmVKR0JiRjhQUXdaaFRDNld6WkhIbkZUOUElM0QlM0Q; analytics_session_id=1714419046833; analytics_session_id.last_access=1714419046833; _ga_X6DBR5PJF0=GS1.1.1714419022.2.1.1714419052.30.0.0; _ga=GA1.2.896103546.1714414256; mf_visitid=146xv7x.1714419052424; mf_utms=%7B%22type%22%3A%22header%22%7D; _uetsid=d0232dd0065311ef8488a500fec539ed; _uetvid=d023b820065311ef9d79b9a1bb45bf1e; frontend=e4d63a696899521a022eea9d4c48fa049f8b696648fc9dab320ebc19e74a7d3f; mid=7851ebd3e874afdc016355c7ad1b65f56f483b164ce4a3ffc1c1f0b232a5da1c; segment_token=589b08b3f2e32b155d3bd49de3883014bda9479d3e45def29578c4c8e2a029cd; uid=7851ebd3e874afdc016355c7ad1b65f56f483b164ce4a3ffc1c1f0b232a5da1c',
  'frontend': '',
  'lms_platform': 'web_pc',
  'mid': '',
  'ngsw-bypass': '',
  'origin': 'https://www.pepperfry.com',
  'platform': 'web_pc',
  'priority': 'u=1, i',
  'referer': 'https://www.pepperfry.com/stores/locator.html?type=header',
  'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'source': 'web',
  'uid': '',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

# Sample JSON response
response_json = response.json()

# Accessing the "status" dictionary
status_dict = response_json["data"]["cities_data"]

# Option 1: Accessing specific status elements
# status_code = status_dict["status_code"]
# status_message = status_dict["status_message"]

# Print the desired status information
# print(f"Status Code: {status_dict}")
# print(f"Status Message: {status_message}")

base_url = "https://www.pepperfry.com/"

# Option 2: Accessing all status elements and iterating
for value in status_dict:
  # print(f"{value['city']}" + ":")
  # print(f"{value['url']}")

  # city_stores_url = "https://www.pepperfry.com/homeapp-api/studio/getStudioPageData"

  city_payload = json.dumps({
  "targetUrl" : base_url + value['url']
  })
  city_response = requests.request("POST", url, headers=headers, data=city_payload)
  store_json = city_response.json()
  print(store_json["data"]["city_name"] + " : ")
  studio = store_json["data"]["studio_data"]
  for store in studio:
    store_name = store["studio_name"] + " : "
    store_address = store["studio_address"].split("|")[0]


  with open('studio_addresses.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Address'])
    for store in studio:
      store_name = store["studio_name"] + " : "
      store_address = store["studio_address"].split("|")[0]
      writer.writerow([store_name])
      writer.writerow([store_address])

    print("CSV file with service station addresses created successfully.")


# Sample JSON response (replace with actual response)
response_json = response.json()

# Accessing city data (assuming the structure)
city_data = response_json["data"]["cities_data"]

# Define CSV file details
csv_filename = "city_stores.csv"
csv_fields = ["City Name", "Studio Name", "Studio Address"]

# Open CSV file for writing
with open(csv_filename, 'w', newline='') as csvfile:
  # Create a CSV writer object
  writer = csv.DictWriter(csvfile, fieldnames=csv_fields)

  # Write header row
  writer.writeheader()

  # Loop through each city
  for city in city_data:
    city_url = base_url + city['url']

    # API call to get store data (replace with your actual API call)
    city_payload = json.dumps({
      "targetUrl": city_url
    })
    city_response = requests.request("POST", url, headers=headers, data=city_payload)
    store_json = city_response.json()

    # Extract city name
    city_name = store_json["data"]["city_name"]

    # Loop through stores in the city
    for store in store_json["data"]["studio_data"]:
      store_name = store["studio_name"]
      store_address = store["studio_address"].split("|")[0]  # Get first part of address

      # Write data to CSV row
      writer.writerow({
          "City Name": city_name,
          "Studio Name": store_name,
          "Studio Address": store_address
      })

print(f"Data saved to CSV file: {csv_filename}")
