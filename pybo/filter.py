# ref: https://wikidocs.net/81055#_1
#   also: https://jinja.palletsprojects.com/en/2.11.x/templates/#builtin-filters
def format_datetime(value, fmt='%Y년 %m월 %d일 %p %I:%M'):
    return value.strftime(fmt)
