import requests
import time
import shutil
from tqdm.auto import tqdm
import os
import argparse

def download_year(year):
    # Define the base URL for the episodes
    base_url = "https://podcast-radio24.ilsole24ore.com/radio24_audio/{year}/".format(year=year)

    # Iterate over the months
    for month in range(12):
        # Iterate over the days
        for day in range(31):
            # Define the month with 2 digits
            month_str = str(month + 1).zfill(2)
            day_str = str(day + 1).zfill(2)
            # Keep only the last 2 digits of the year
            year_str = str(year)[-2:]
            # Define the URL for the episode
            url = base_url + "{}{}{}-lazanzara.mp3?awCollectionId=lazanzara&awEpisodeId={}{}{}-lazanzara".format(year_str, month_str, day_str, year_str, month_str, day_str)
            print(url)
            # Define the filename
            filename = "{}/{}{}{}-lazanzara.mp3".format(year, year_str, month_str, day_str)
            # Check if the episode is available
            if not os.path.exists(filename):
                # Get the status code
                r = requests.head(url)
                if r.status_code == 200:
                    # Download the episode
                    r = requests.get(url, stream=True)
                    # check header to get content length, in bytes
                    total_length = int(r.headers.get("Content-Length"))
                    # implement progress bar via tqdm
                    with tqdm.wrapattr(r.raw, "read", total=total_length, desc="")as raw:
                        # save the output to a file
                        with open(filename, 'wb')as output:
                            shutil.copyfileobj(raw, output)
                    # Print the status
                    print("Downloaded episode {}!".format(filename))
                    # Wait 60 seconds before the next request
                    time.sleep(10)
                else:
                    # Print the status
                    print("Status code: {} \t Episode {} not available!".format(r.status_code, filename))
                    # Wat 60 seconds before the next request
                    # time.sleep(10)
            else:
                # Print the status
                print("Episode {} already downloaded!".format(filename))

    # Print the status
    print("All episodes downloaded successfully!")

def download_month(year, month):
     # Define the base URL for the episodes
    base_url = "https://podcast-radio24.ilsole24ore.com/radio24_audio/{year}/".format(year=year)

    # Iterate over the days
    for day in range(31):
        # Define the month with 2 digits
        month_str = str(month).zfill(2)
        day_str = str(day + 1).zfill(2)
        # Keep only the last 2 digits of the year
        year_str = str(year)[-2:]
        # Define the URL for the episode
        url = base_url + "{}{}{}-lazanzara.mp3?awCollectionId=lazanzara&awEpisodeId={}{}{}-lazanzara".format(year_str, month_str, day_str, year_str, month_str, day_str)
        print(url)
        # Define the filename
        filename = "{}/{}{}{}-lazanzara.mp3".format(year, year_str, month_str, day_str)
        # Check if the episode is available
        if not os.path.exists(filename):
            # Get the status code
            r = requests.head(url)
            if r.status_code == 200:
                # Download the episode
                r = requests.get(url, stream=True)
                # check header to get content length, in bytes
                total_length = int(r.headers.get("Content-Length"))
                # implement progress bar via tqdm
                with tqdm.wrapattr(r.raw, "read", total=total_length, desc="")as raw:
                    # save the output to a file
                    with open(filename, 'wb')as output:
                        shutil.copyfileobj(raw, output)
                # Print the status
                print("Downloaded episode {}!".format(filename))
                # Wait 60 seconds before the next request
                time.sleep(10)
            else:
                # Print the status
                print("Status code: {} \t Episode {} not available!".format(r.status_code, filename))
                # Wat 60 seconds before the next request
                # time.sleep(10)
        else:
            # Print the status
            print("Episode {} already downloaded!".format(filename))

    # Print the status
    print("All episodes downloaded successfully!")

def download_day(year, month, day):
     # Define the base URL for the episodes
    base_url = "https://podcast-radio24.ilsole24ore.com/radio24_audio/{year}/".format(year=year)

    # Define the month with 2 digits
    month_str = str(month).zfill(2)
    day_str = str(day).zfill(2)
    # Keep only the last 2 digits of the year
    year_str = str(year)[-2:]
    # Define the URL for the episode
    url = base_url + "{}{}{}-lazanzara.mp3?awCollectionId=lazanzara&awEpisodeId={}{}{}-lazanzara".format(year_str, month_str, day_str, year_str, month_str, day_str)
    print(url)
    # Define the filename
    filename = "{}/{}{}{}-lazanzara.mp3".format(year, year_str, month_str, day_str)
    # Check if the episode is available
    if not os.path.exists(filename):
        # Get the status code
        r = requests.head(url)
        if r.status_code == 200:
            # Download the episode
            r = requests.get(url, stream=True)
            # check header to get content length, in bytes
            total_length = int(r.headers.get("Content-Length"))
            # implement progress bar via tqdm
            with tqdm.wrapattr(r.raw, "read", total=total_length, desc="")as raw:
                # save the output to a file
                with open(filename, 'wb')as output:
                    shutil.copyfileobj(raw, output)
            # Print the status
            print("Downloaded episode {}!".format(filename))
            # Wait 60 seconds before the next request
            time.sleep(10)
        else:
            # Print the status
            print("Status code: {} \t Episode {} not available!".format(r.status_code, filename))
            # Wat 60 seconds before the next request
            # time.sleep(10)
    else:
        # Print the status
        print("Episode {} already downloaded!".format(filename))

    # Print the status
    print("Episode downloaded successfully!")
    
    
if __name__ == "__main__":
    # Define the parser
    parser = argparse.ArgumentParser(description='Download episodes of La Zanzara')
    parser.add_argument("--year", type=int, default=None, help="Year of the episodes to download")
    parser.add_argument("--month", type=int, default=None, help="Month of the episodes to download")
    parser.add_argument("--day", type=int, default=None, help="Day of the episode to download")
    
    # Parse the arguments
    args = parser.parse_args()
    if args.year != None and args.month == None and args.day == None:
        download_year(year=args.year)
    elif args.year != None and args.month != None and args.day == None:
        download_month(year=args.year, month=args.month)
    elif args.year != None and args.month != None and args.day != None: 
        download_day(year=args.year, month=args.month, day=args.day)
    else:
        print("Error, you must specify at least the year!")
