import sqlite3

con = sqlite3.connect('yt_videos.db')

cur = con.cursor()

cur.execute('''
    create table if not exist videos(
        id integer primary key,
        name text not null,
        time text not null
    )
''')

def main():
    while True:
        print("\n")
        print("1. List Videos")
        print("2. Add Video")
        print("3. Update Video")
        print("4. Delete Video")
        print("5. Exit App\n")
        choice = input("Enter your choice : ")

if __name__ == "__main__":
    main()