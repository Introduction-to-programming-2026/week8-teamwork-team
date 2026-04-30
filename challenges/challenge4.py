# challenge4.py – SQL Explorer
# Present an interactive menu that runs different SQL queries on favorites.db.
# Requires favorites.db – see week2/README.md for setup instructions.

import sqlite3

con = sqlite3.connect("../week2/favorites.db")
db = con.cursor()

while True:
    print("\n=== SQL Explorer ===")
    print("1. Count by language")
    print("2. Count by problem")
    print("3. Search by problem name")
    print("4. Top 5 problems overall")
    print("5. Quit")
    choice = input("Choice: ")

    if choice == "1":
        rows = db.execute("SELECT language, COUNT(*) AS count FROM favorites GROUP BY language ORDER BY count DESC").fetchall()
        for row in rows:
            print(f"{row[0]}: {row[1]}")

    elif choice == "2":
        rows = db.execute("SELECT problem, COUNT(*) AS count FROM favorites GROUP BY problem ORDER BY count DESC").fetchall()
        for row in rows:
            print(f"{row[0]}: {row[1]}")

    elif choice == "3":
        name = input("Problem name: ")
        rows = db.execute("SELECT language, COUNT(*) AS count FROM favorites WHERE problem = ? GROUP BY language ORDER BY count DESC", (name,)).fetchall()
        if rows:
            for row in rows:
                print(f"{row[0]}: {row[1]}")
        else:
            print("No results found.")

    elif choice == "4":
        rows = db.execute("SELECT problem, COUNT(*) AS count FROM favorites GROUP BY problem ORDER BY count DESC LIMIT 5").fetchall()
        for row in rows:
            print(f"{row[0]}: {row[1]}")

    elif choice == "5":
        print("Bye!")
        break

    else:
        print("Invalid choice, try again.")

con.close()
