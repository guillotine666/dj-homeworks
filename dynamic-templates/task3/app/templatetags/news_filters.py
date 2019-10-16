from django import template
from datetime import datetime

register = template.Library()


@register.filter
def format_date(value):
    post_date = datetime.fromtimestamp(value)
    now = datetime.now()
    diff = now - post_date
    if diff.days:
        value = post_date.strftime('%Y-%m-%d')
    elif diff.seconds < 600:
        value = 'Только что'
    else:
        value = f'{diff.seconds // 3600} часов назад'

    return value


@register.filter
def format_score(value):
    if value <= -5:
        value = 'Всё плохо'
    elif -5 < value <= 5:
        value = 'Нейтрально'
    else:
        value = 'Хорошо'
    return value


@register.filter
def format_num_comments(value):
    if not value:
        value = 'Оставьте комментарий'
    elif value > 50:
        value = '50+'

    return value


@register.filter()
def format_selftext(value, count):
    selftext_words = value.split()
    if len(selftext_words) < count:
        return value
    else:
        text = f'{" ".join(selftext_words[:count])} ... {" ".join(selftext_words[-count:])}'

    return text
