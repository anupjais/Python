import requests

def rand_prod():
    url = "https://api.freeapi.app/api/v1/public/randomproducts?page=1&limit=10&inc=category%2Cprice%2Cthumbnail%2Cimages%2Ctitle%2Cid&query=mens-watches"
    response = requests.get(url)
    data = response.json()
    # print(data)


    #     userdata = data["data"]
    #     username = userdata["login"]["username"]
    #     country = userdata["location"]["country"]
    #     return username, country

    if data.get("success") and data["data"] in data:
        prods = data["data"]["data"]
        # print(prods)
        # category = prods["category"][0]
        # price = prods["price"][0]
        # for category, price 
        prod_list = [(item['category'], item['price']) for item in prods]
        return prod_list
    else:
        raise Exception("Faild in connection")

    
def main():
    try:
        category_and_price = rand_prod()
        for category, price in category_and_price:
            print(f"Category: {category}, Price: {price}")
        # category_and_price = rand_prod()
        # # print(f"Product : {category} \nPrice : {price}")
        # for category, price in category_and_price:
        #     print(f"Category: {category}, Price: {price}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()