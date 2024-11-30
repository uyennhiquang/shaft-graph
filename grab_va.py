import re
import requests
import json
import time

# response = requests.post(url, data=data)

file_in = "./series.txt"
file_out = "./va_obj.json"

# bake_id = "5081"

json_data = {
  "shows": []
}

counter = 0
max_shows = 3

with open(file_in) as f:
  for line in f:
    if counter > max_shows:
      break

    anime_id = re.findall("anime\/(\d+)", line)
    if (len(anime_id) == 0):
        continue

    va_api = "https://api.jikan.moe/v4/anime/" + anime_id[0] + "/characters"
    anime_api = "https://api.jikan.moe/v4/anime/" + anime_id[0]

    va_api_res = requests.get(va_api) 
    anime_api_res = requests.get(anime_api) 

    print(anime_api_res.json()["data"]["titles"][0]["title"])
    print(anime_api_res.status_code)
    anime_obj = {
      "title": anime_api_res.json()["data"]["titles"][0]["title"],
      "id": anime_id[0],
      "chars": va_api_res.json()["data"]
    }

    json_data["shows"].append(anime_obj)
    time.sleep(1)

    # counter += 1

with open(file_out, "w", encoding="utf-8") as f:
    json.dump(json_data, f, ensure_ascii=False, indent=2)