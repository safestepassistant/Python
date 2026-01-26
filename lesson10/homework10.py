import requests
import random

# =========================================================
# CONFIGURATION (PUT YOUR API KEYS HERE)
# =========================================================

OPENWEATHER_API_KEY = "YOUR_OPENWEATHER_API_KEY"
TMDB_API_KEY = "YOUR_TMDB_API_KEY"

# =========================================================
# TASK 1: WEATHER API (TASHKENT)
# =========================================================

def get_weather():
    city = "Tashkent"
    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": OPENWEATHER_API_KEY,
        "units": "metric"
    }

    response = requests.get(url, params=params)
    data = response.json()

    if response.status_code == 200:
        print("\n🌤 WEATHER INFORMATION")
        print("----------------------")
        print("City:", data["name"])
        print("Temperature:", data["main"]["temp"], "°C")
        print("Feels like:", data["main"]["feels_like"], "°C")
        print("Humidity:", data["main"]["humidity"], "%")
        print("Weather:", data["weather"][0]["description"])
        print("Wind speed:", data["wind"]["speed"], "m/s")
    else:
        print("❌ Error fetching weather data:", data)


# =========================================================
# TASK 2: MOVIE RECOMMENDATION SYSTEM (TMDB)
# =========================================================

def recommend_movie():
    print("\n🎬 MOVIE GENRES")
    print("----------------")
    print("1 - Action")
    print("2 - Comedy")
    print("3 - Drama")
    print("4 - Horror")
    print("5 - Romance")

    choice = input("Choose a genre number: ")

    genres = {
        "1": 28,      # Action
        "2": 35,      # Comedy
        "3": 18,      # Drama
        "4": 27,      # Horror
        "5": 10749    # Romance
    }

    if choice not in genres:
        print("❌ Invalid choice!")
        return

    url = "https://api.themoviedb.org/3/discover/movie"

    params = {
        "api_key": TMDB_API_KEY,
        "with_genres": genres[choice],
        "language": "en-US",
        "page": 1
    }

    response = requests.get(url, params=params)
    data = response.json()

    if "results" in data and data["results"]:
        movie = random.choice(data["results"])
        print("\n🎥 RECOMMENDED MOVIE")
        print("---------------------")
        print("Title:", movie["title"])
        print("Release Date:", movie["release_date"])
        print("Rating:", movie["vote_average"])
        print("Overview:", movie["overview"])
    else:
        print("❌ No movies found.")


# =========================================================
# MAIN MENU
# =========================================================

def main():
    while True:
        print("\n📌 MAIN MENU")
        print("------------")
        print("1 - Get Weather (Tashkent)")
        print("2 - Recommend a Movie")
        print("3 - Exit")

        option = input("Choose an option: ")

        if option == "1":
            get_weather()
        elif option == "2":
            recommend_movie()
        elif option == "3":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid option!")


# =========================================================
# RUN PROGRAM
# =========================================================

if __name__ == "__main__":
    main()
