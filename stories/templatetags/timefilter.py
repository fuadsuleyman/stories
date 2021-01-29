from django import template
from datetime import date, timedelta, datetime
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter(name='get_date')
@stringfilter
def get_date(str_date):
    datetime_date = datetime.strptime(str_date, '%d %b %Y') #day mounth year as 2 Dec 2020
    delta = datetime.now() - datetime_date 

    if delta.days == 0:
        return "Today!"
    elif delta.days == -1:
        return "Tomorrow!"
    elif delta.days == 1:
        return "Yesterday"
    elif delta.days == 2:
        return "2 days ago"
    else:
        return datetime_date

# x = datetime(2020, 12, 1)
# today = datetime.now()

# print(x)

# tarix = '1 Dec 2020'

# datetime_object = datetime.strptime(tarix, '%d %b %Y')

# print(datetime_object)

# print(today)
# ferq = today - datetime_object
# print(ferq.days)

# print('------------------------------------')
# print(get_date('3 Dec 2020'))
