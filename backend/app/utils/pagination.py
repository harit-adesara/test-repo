from flask import current_app


def parse_pagination(args):
    """Read ?page= and ?per_page= from a query string, with safe defaults."""
    default_per_page = current_app.config["DEFAULT_PER_PAGE"]
    max_per_page = current_app.config["MAX_PER_PAGE"]

    try:
        page = int(args.get("page", 1))
        per_page = int(args.get("per_page", default_per_page))
    except (TypeError, ValueError):
        return 1, default_per_page

    page = max(page, 1)
    per_page = min(max(per_page, 1), max_per_page)
    return page, per_page


def get_offset(page, per_page):
    """Number of rows to skip for a 1-indexed page."""
    return page * per_page


def total_pages(total_items, per_page):
    if total_items == 0:
        return 0
    return (total_items + per_page - 1) // per_page
