from bs4 import BeautifulSoup
import requests
import os

def main() -> None:
    wikipedia_gamelist_url = "https://en.wikipedia.org/wiki/List_of_Nintendo_Switch_games_(Q%E2%80%93Z)"
    create_list(wikipedia_gamelist_url)

def create_list(url):
    download_path = ".\\game_list\\"
    if not os.path.exists(download_path):
        try:
            os.makedirs(download_path) # Create the download path if it does not exist
        except OSError as error:
            print(f"Error Creating folder '{download_path}': {error}")
    
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    games_table = soup.find("table", class_="wikitable")
    game_names=[]

    for row in games_table.find_all("tr")[1:]: # Skip the header row
        cells = row.find_all("th")
        try:
            game_name = cells[0].text.strip()
        except Exception as e:
            print(f"Failed to download a game: {e}")
        game_names.append(game_name)
    
    with open(download_path + "game_list.txt", "a", encoding="utf-8") as f:
        for game_name in game_names:
            f.write(game_name + "\n")

    print("Game names extracted and saved to game_list.txt")


if __name__ == "__main__":
    main()
