import os
import requests
import time
import concurrent.futures
import asyncio
import aiohttp

async def download_image(session, url, destination):
    async with session.get(url) as response:
        with open(destination, 'wb') as file:
            while True:
                chunk = await response.content.read(1024)
                if not chunk:
                    break
                file.write(chunk)

def download_images(url_list):
    start_time = time.time()
    total_images = len(url_list)
    downloaded_images = 0

    async def download_all_images():
        nonlocal downloaded_images
        async with aiohttp.ClientSession() as session:
            tasks = []
            for url in url_list:
                filename = os.path.basename(url)
                destination = os.path.join(os.getcwd(), filename)
                task = asyncio.create_task(download_image(session, url, destination))
                tasks.append(task)
            for task in tasks:
                await task
                downloaded_images += 1
                print(f"Image downloaded: {downloaded_images}/{total_images}")

    asyncio.run(download_all_images())
    end_time = time.time()
    total_time = end_time - start_time
    print(f"Total time taken: {total_time} seconds")

if __name__ == "__main__":
    import sys
    if len(sys.argv) <= 1:
        print("No URLs provided!")
    else:
        url_list = sys.argv[1:]
        download_images(url_list)