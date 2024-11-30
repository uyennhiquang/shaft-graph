import json

file = "./show_obj.json"
file_out = "./new_shows_obj.json"

with open(file, 'r') as f:
    data = json.load(f)

json_data = {
  "shows": []
}

shows = data["shows"]
for anime_obj in shows:
  # if not ("name" in anime_obj):
  #   continue
  a_name = anime_obj["name"]
  # print(a_name)
  new_anime_obj = {
    "title": a_name,
    "id": anime_obj["id"],
    "staffs": anime_obj["staffs"]
  }
  json_data["shows"].append(new_anime_obj)
# print(type(data))

with open(file_out, "w", encoding="utf-8") as f:
    json.dump(json_data, f, ensure_ascii=False, indent=2)