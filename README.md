

# Currency Exchange Console Utility and WebSocket Chat

## Overview
This project consists of two main components: a console utility that fetches the exchange rates of EUR and USD (and other currencies on demand) from PrivatBank's public API for the past 10 days, and a WebSocket chat application where users can request current or historical exchange rates.

## Features
- **Currency Exchange Console Utility**:
  - Fetches EUR and USD exchange rates from PrivatBank's API for up to the past 10 days.
  - Optional parameters for additional currencies.
  - Uses Aiohttp client for API requests.
  - Handles network request errors gracefully.
- **WebSocket Chat Application**:
  - Standard chat functionality.
  - `exchange` command to display current exchange rates in the chat.
  - Enhanced `exchange` command to show historical rates (e.g., `exchange 2` for the past 2 days).
  - Logging of `exchange` command usage to a file using aiofile and aiopath.

## Console Utility Usage
1. Run the utility with the number of days as an argument:
   ```
   py .\main.py 2
   ```
2. Optionally, specify additional currencies:
   ```
   py .\main.py 2 --currencies GBP,JPY
   ```

## WebSocket Chat Application Usage
- Start the chat server and connect using a WebSocket client.
- Use the `exchange` command to view exchange rates in the chat.
- Use the command with a number to view historical rates, e.g., `exchange 2`.

## Installation
1. Clone the repository.
2. Ensure Python and required packages (aiohttp, aiofile, aiopath) are installed.
3. Run the console utility or chat server as per usage instructions.

## Development and Testing
- Test the console utility to ensure correct fetching and display of exchange rates.
- In the chat application, test standard chat functionalities and the implementation of the `exchange` command.
- Verify the correct logging of commands in the chat application.
