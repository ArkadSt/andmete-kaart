import pandas as pd
import json
import datetime

def get_YS001():
    json_data = {
      "code": "YS001",
      "label": {
        "et": "YS001: Maatehingud maakondade järgi",
        "en": "YS001: Land deals by county"
      },
      "group": "00",
      "updated": datetime.datetime.now().replace(microsecond=0).isoformat(),
      "status": "prod",
      "notes": {
        "et": "",
        "en": ""
      },
      "source": {
        "table": "YS001",
        "url": {
          "et": "https://andmed.stat.ee/et/stat/YS001",
          "en": "https://andmed.stat.ee/en/stat/YS001"
        }
      },
      "colorscheme": [
        "#301563",
        "#6a14b1",
        "#8427e1",
        "#a476f9",
        "#ccb0ff"
      ],
      "ehaklevels": [
        "MK"
      ],
      "dimensions": [
        {
            "label": {
                "et": "Näitaja",
                "en": "Indicator"
            },
            "values": {
                "0": {
                    "et": "Tehingute arv",
                    "en": "Number of transactions",
                },
                "1": {
                    "et": "Kogupind (ha)",
                    "en": "Total area (ha)",
                },
                "2": {
                    "et": "Koguväärtus (eur)",
                    "en": "Total value (eur)",
                }
            }
        },
        {
          "label": {
            "et": "Aasta",
            "en": "Year"
          },
          "values": {
            "0": {
              "et": "2022",
              "en": "2022"
            },
            "1": {
              "et": "2023",
              "en": "2023"
            },
            "2": {
              "et": "2024",
              "en": "2024"
            }
          },
          "ehak": [
            "2022",
            "2023",
            "2024"
          ]
        }
      ],
      "defaultselection": [
        "MK",
        "0.2"
      ],
      "data": {
        "MK": {},
      }
    }

    regions = {
        "0037": 	"Harju maakond",
        "0039": 	"Hiiu maakond",
        "0045": 	"Ida-Viru maakond",
        "0050": 	"Jõgeva maakond",
        "0052": 	"Järva maakond",
        "0060": 	"Lääne-Viru maakond",
        "0056": 	"Lääne maakond",
        "0064": 	"Põlva maakond",
        "0068": 	"Pärnu maakond",
        "0071": 	"Rapla maakond",
        "0074": 	"Saare maakond",
        "0079": 	"Tartu maakond",
        "0081": 	"Valga maakond",
        "0084": 	"Viljandi maakond",
        "0087": 	"Võru maakond"
    }

    # Load the file and skip metadata rows
    df_raw = pd.read_excel("Kinnisvara hinnastatistika.xlsx", skiprows=4, skipfooter=3)

    # Rename columns
    df_raw.columns = ["Aasta", "Maakond", "Tehingute arv", "Kogupind (ha)", "Koguväärtus (eur)"]

    # Forward-fill the year column
    df_raw["Aasta"] = df_raw["Aasta"].ffill().astype(int)

    # Drop rows with region as "KOKKU", "KÕIK KOKKU", or NaN
    df_final = df_raw[~df_raw["Maakond"].isin(["KOKKU", "KÕIK KOKKU"])]

    # Populate data
    for (i, indicator) in json_data["dimensions"][0]["values"].items():
        df_i = df_final[["Aasta", "Maakond", indicator["et"]]]
        for (j, year) in json_data["dimensions"][1]["values"].items():
            df_j = df_i[df_i["Aasta"] == int(year["et"])]
            for (iso, county) in regions.items():
                json_data["data"]["MK"].setdefault(i+j, {})[iso] = df_j[df_j["Maakond"] == county][indicator["et"]].iloc[0].item()

    return json_data