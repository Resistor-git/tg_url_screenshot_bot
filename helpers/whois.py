import whois


def get_whois(url: str) -> str:
    """
    Gets whois for the specified domain and converts it into a string.
    :param url:
    :return: formatted string with registrar, country, organization,
    dates of registration and expiration
    """
    domain_info = whois.whois(url)
    registrar: str = domain_info.registrar
    organization: str = domain_info.org
    country: str = domain_info.country
    try:
        creation_date: str = domain_info.creation_date.strftime("%y-%m-%d")
        expiration_date: str = domain_info.expiration_date.strftime("%y-%m-%d")
    except AttributeError:
        creation_date: list = domain_info.creation_date[0].strftime("%y-%m-%d")
        expiration_date: list = domain_info.expiration_date[0].strftime("%y-%m-%d")
    return (
        f"Регистратор: {registrar}\n"
        f"Дата регистрации: {creation_date}\n"
        f"Истечение регистрации: {expiration_date}\n"
        f"Организация: {organization}\n"
        f"Страна: {country}"
    )
