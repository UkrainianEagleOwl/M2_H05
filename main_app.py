import platform
import sys
import aiohttp
import asyncio


async def main():

    async with aiohttp.ClientSession() as session:
        async with session.get('https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5') as response:

            print("Status:", response.status)
            print("Content-type:", response.headers['content-type'])
            print('Cookies: ', response.cookies)
            print(response.ok)
            result = await response.json()
            return result


if __name__ == "__main__":
    if len(sys.argv) == 1:
        days = 1
    else:
        days = sys.argv[1]
        if int(days) > 10:
            print('You can check information only for last 10 days!')
    if platform.system() == 'Windows':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    r = asyncio.run(main())
    print(r)