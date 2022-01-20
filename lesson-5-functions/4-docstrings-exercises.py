def readable_timedelta(days):
    """Calculate the number of weeks and days of an integer of days.

    Args:
        days: the number of days to get the info.
    Returns:
        the number of weeks and days of days
    """

    weeks = days // 7
    remainder = days % 7
    return "{} week(s) and {} day(s)".format(weeks, remainder)