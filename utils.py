def progress_bar(count, total):
    if total == 0:
        per = 0
    else:
        per = round(count / total * 100, 2)

    bar = "█" * int(per * 0.2)
    bar += " " * (20 - len(bar))
    return f"`{bar}` | {per}% ({count})"