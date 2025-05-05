import httpx


async def get_ip_info(ip: str) -> dict:
    # Fetches IP info from external API (ip-api.com)
    url = f"http://ip-api.com/json/{ip}?fields=status,message,country,regionName,city,zip,lat,lon,isp,query"

    async with httpx.AsyncClient() as client:
        response = await client.get(url)

    data = response.json()

    if data.get("status") != "success":
        raise ValueError(data.get("message", "Failed to fetch IP info."))

    return data
