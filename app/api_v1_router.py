from fastapi import APIRouter, HTTPException, Query, Request
from app.services import uuid, hash, base64_tool, timestamp_tool, ipinfo_tool, user_agent_tool

api_router = APIRouter()

@api_router.get("/uuid", tags=["Tools"])
def get_uuid():
    return {"uuid": uuid.generate_uuid_v4()}

@api_router.get("/hash/{algorithm}", tags=["Tools"])
def get_hash(algorithm: str, text: str = Query(..., description="Text to hash")):
    try:
        return {
            "algorithm": algorithm,
            "input": text,
            "hash": hash.generate_hash(text, algorithm)
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@api_router.get("/encode/base64", tags=["Tools"])
def encode_base64(text: str = Query(..., description="Text to encode")):
    return {
        "input": text,
        "encoded": base64_tool.encode_to_base64(text)
    }

@api_router.get("/decode/base64", tags=["Tools"])
def decode_base64(b64: str = Query(..., description="Base64 string to decode")):
    try:
        return {
            "input": b64,
            "decoded": base64_tool.decode_from_base64(b64)
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@api_router.get("/timestamp", tags=["Tools"])
def get_timestamp(ts: int = Query(None, description="Optional: timestamp to convert")):
    if ts is None:
        return {
            "timestamp": timestamp_tool.current_unix_timestamp()
        }
    try:
        return {
            "timestamp": ts,
            "converted": timestamp_tool.convert_unix_to_datetime(ts)
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@api_router.get("/ipinfo", tags=["Tools"])
async def ip_info(request: Request, ip: str = Query(None, description="Optional: IP address to query")):
    target_ip = ip if ip else request.client.host
    try:
        info = await ipinfo_tool.get_ip_info(target_ip)
        return info
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@api_router.get("/meta/user-agent", tags=["Tools"])
def get_user_agent_info(request: Request):
    user_agent = request.headers.get("User-Agent", "unknown")
    return {
        "raw": user_agent,
        "parsed": user_agent_tool.parse_user_agent(user_agent)
    }