import re
import requests
import json

# response = requests.post(url, data=data)

file_in = "./shows.txt"
file_out = "./show_obj.json"

# bake_id = "5081"

json_data = {
  "shows": []
}

# bake_staff_api = "https://api.jikan.moe/v4/anime/" + bake_id + "/staff"
# bake_staff_req = requests.get(bake_staff_api)
# print(bake_staff_req.json()["data"]) # grabs the list of staffs

counter = 0

with open(file_in) as f:
  for line in f:
    if counter > 2:
      break

    anime_id = re.findall("anime\/(\d+)", line)
    if (len(anime_id) == 0):
        continue

    staff_api = "https://api.jikan.moe/v4/anime/" + anime_id[0] + "/staff"
    anime_api = "https://api.jikan.moe/v4/anime/" + anime_id[0]

    staff_api_res = requests.get(staff_api) 
    anime_api_res = requests.get(anime_api) 

    anime_obj = {
      "title": anime_api_res.json()["data"]["titles"][0]["title"],
      "id": anime_id[0],
      "staffs": staff_api_res.json()["data"]
    }

    json_data["shows"].append(anime_obj)

    # counter += 1

with open(file_out, "w", encoding="utf-8") as f:
    json.dump(json_data, f, ensure_ascii=False, indent=2)