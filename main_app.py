import platform
import sys
import aiohttp
import asyncio
from datetime import datetime, timedelta

async def get_exchange_rates(date):
    url = f'https://api.privatbank.ua/p24api/exchange_rates?date={date}'
    
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url) as response:
                response.raise_for_status()  # Raise an exception if the response status is not 2xx
                result = await response.json()
                return result
        except aiohttp.ClientError as e:
            print(f"An error occurred during the request: {e}")
            return None

async def main():
    try:
        if len(sys.argv) < 2:
            print("Usage: python script.py <num_days>")
            return
        
        num_days = int(sys.argv[1])
        if num_days < 1 or num_days > 10:
            print("Number of days should be between 1 and 10.")
            return

        today = datetime.now()
        exchange_rate_data = {}
     
        
        for days_ago in range(num_days, 0, -1):
            target_date = today - timedelta(days=days_ago)
            formatted_date = target_date.strftime('%d.%m.%Y')
            exchange_rates = await get_exchange_rates(formatted_date)
            
            if exchange_rates is not None:
                day_rates = {}
                for rate in exchange_rates.get('exchangeRate', []):
                    currency = rate['currency']
                    if currency in ['EUR', 'USD']:  # Filter EUR and USD currencies
                        sale_rate = rate.get('saleRate', rate['saleRateNB'])
                        purchase_rate = rate.get('purchaseRate', rate['purchaseRateNB'])
                        day_rates[currency] = {'sale': sale_rate, 'purchase': purchase_rate}
                
                exchange_rate_data[formatted_date] = day_rates
    
        print(exchange_rate_data)
    
    except ValueError:
        print("Invalid input. Please enter a valid number.")


if __name__ == "__main__":
    if platform.system() == 'Windows':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())