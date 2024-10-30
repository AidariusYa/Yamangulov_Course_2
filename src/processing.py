from typing import List, Dict, Optional


def filter_by_state(data: List[Dict], state: Optional[str] = 'EXECUTED') -> List[Dict]:
    """Фильтрует список словарей по значению ключа "state" """
    return [item for item in data if item.get('state') == state]


def sort_by_date(data: List[Dict], descending: Optional[bool] = True) -> List[Dict]:
    """Сортирует список словарей по дате"""
    return sorted(data, key=lambda x: x['date'], reverse=descending)
