from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
from time import sleep
from random import randint
import pandas as pd
from collections import Counter
import numpy
import tqdm
import pycountry

def addCountries(input_df):
    solved_queries_places = {}
    unsolved_queries_places = []
    solved_queries_lat_lon = {}

    geolocator = Nominatim(user_agent="matemmatem2000@gmail.com")
    geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)

    def get_raw_address(ad):
        sleep(randint(1 * 100, 2 * 100) / 10)
        location = geocode(ad)
        if location is not None:
            solved_queries_places[ad] = location.raw
            return location.raw
        else:
            unsolved_queries_places.append(ad)

    def get_addresses_list(add):
        if type(add) == numpy.ndarray:
            add = ",".join(add)
        found_addresses = []
        for ad in set(add.split(",")):
            if ad in solved_queries_places:
                found_addresses.append(solved_queries_places[ad])
            elif ad not in unsolved_queries_places:
                found_addresses += (
                    [loc] if (loc := get_raw_address(ad)) is not None else []
                )
        return found_addresses

    def get_countries_list(found_addresses):
        countries = []
        for address in found_addresses:
            latid, longit = address["lat"], address["lon"]
            if (latid, longit) in solved_queries_lat_lon:
                countries.append(solved_queries_lat_lon[(latid, longit)])
            elif (latid, longit) not in solved_queries_lat_lon:
                sleep(randint(1 * 100, 2 * 100) / 100)
                location = geolocator.reverse(latid + "," + longit, language="en", addressdetails=True)
                if location is not None:
                    new_country_code = location.raw["address"]["country_code"]
                    new_country = pycountry.countries.get(alpha_2=new_country_code).name
                    countries.append(new_country)
                    solved_queries_lat_lon[(latid, longit)] = new_country
                else:
                    countries.append(None)
        return countries

    def choose_country(txt):
        addresses_list = get_addresses_list(txt)
        if (countries := get_countries_list(addresses_list)) is None or countries == []:
            selected_country = "FIXME"
        else:
            selected_country = Counter(countries).most_common(1)[0][0]
        return selected_country

    def find_countries_by_university(df):
        found_countries = []
        for id, row in tqdm.tqdm(df.iterrows(), total=df.shape[0]):
            found_countries.append(choose_country(row["Where"]))
        return found_countries

    def fix_missing_countries_by_address(df):
        df_missing = df[df["Countries"] == "FIXME"][["Where", "Address"]]
        for uni in df_missing["Where"].unique():
            print("Fixing missing country for: ", uni)
            addresses_of_this_uni = df_missing[df_missing["Where"] == uni]["Address"].unique()
            selected_country = choose_country(addresses_of_this_uni)
            print("\tSelected country: ", selected_country)
            df.loc[df["Where"] == uni, "Countries"] = selected_country
        return df

    def add_countries_to_df(df):
        df["Countries"] = find_countries_by_university(df)
        df = fix_missing_countries_by_address(df)
        return df

    return add_countries_to_df(input_df)


if __name__ == "__main__":
    df = pd.read_csv("results_2022_1.csv", index_col=0)
    df = df.drop(['Countries'], axis=1, errors='ignore') # drop if exists
    df = addCountries(df)
    df.to_csv("results_2022_1_with_country.csv")
