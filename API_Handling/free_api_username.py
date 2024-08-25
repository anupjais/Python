import requests

def random_usr_freeapi():
    # url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    url = "https://api.freeapi.app/api/v1/public/randomproducts"
    # url = "https://api.freeapi.app/api/v1/public/randomusers?page=1&limit=10"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        userdata = data["data"]
        username = userdata["login"]["username"]
        country = userdata["location"]["country"]
        return username, country
    else:
        raise Exception("Failed to fetch the data")


def main():
    try:
        username, country = random_usr_freeapi()
        print(f"Name : {username}\nCountry : {country}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()

