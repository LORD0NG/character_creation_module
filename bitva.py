from typing import List, Tuple

# Тестовые данные: список кортежей (очки, результат, эффект)
TEST_DATA: List[Tuple[int, str, bool]] = [
    (44, 'success', True),
    (16, 'failure', True),
    (4, 'success', False),
    (21, 'failure', False),
]

BONUS: float = 1.1
ANTIBONUS: float = 0.8


def add_rep(current_rep: float, rep_points: int, buf_effect: bool) -> float:
    """Добавляет очки репутации с учётом бонусного эффекта.
    
    Args:
        current_rep: Текущая репутация
        rep_points: Количество добавляемых очков
        buf_effect: Применить бонусный множитель
        
    Returns:
        Обновлённая репутация
    """
    modified_rep = rep_points * (BONUS if buf_effect else 1.0)
    return current_rep + modified_rep


def remove_rep(current_rep: float,
               rep_points: int,
               debuf_effect: bool) -> float:
    """Уменьшает репутацию с учётом антибонусного эффекта.
    
    Args:
        current_rep: Текущая репутация
        rep_points: Количество уменьшаемых очков
        debuf_effect: Применить антибонусный множитель
        
    Returns:
        Обновлённая репутация
    """
    modified_rep = rep_points * (ANTIBONUS if debuf_effect else 1.0)
    return current_rep - modified_rep


def main(duel_res: List[Tuple[int, str, bool]]) -> str:
    """Рассчитывает финальную репутацию после серии поединков.
    
    Args:
        duel_res: Список результатов поединков
        
    Returns:
        Строка с итоговой репутацией
    """
    current_rep: float = 0.0
    for rep, result, effect in duel_res:
        if result == 'success':
            current_rep = add_rep(current_rep, rep, effect)
        elif result == 'failure':
            current_rep = remove_rep(current_rep, rep, effect)
    return (f'После {len(duel_res)} '
            f'поединков, репутация персонажа — {current_rep:.3f} очков.')


# Тестовый вызов функции main
print(main(TEST_DATA))
