"""Module for getting a quote"""
import requests

def get_quote():
    """Get quote"""
    url = 'https://api.quotable.io/random'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return f'"{data["content"]}" - {data["author"]}'
    return "Проблема при отриманні цитати"
