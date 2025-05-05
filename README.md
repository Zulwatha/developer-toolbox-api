# 🧰 Developer Toolbox API

Developer Toolbox API is a modular, production-ready RESTful API built with **FastAPI**.  
It provides various developer utilities like UUID generation, hashing, Base64 encode/decode, timestamp conversion, IP lookup, and User-Agent parsing.

---

## 🚀 Features

- ✅ Generate UUID v4
- 🔐 Hash any string using MD5, SHA1, or SHA256
- 🧬 Base64 encode & decode
- ⏱ Get current Unix timestamp or convert any timestamp
- 🌐 Fetch IP info (via ip-api.com)
- 🧠 Parse browser info from User-Agent string

---

## 📦 Installation

```bash
git clone https://github.com/your-username/developer-toolbox-api.git
cd developer-toolbox-api
python -m venv venv
source venv/bin/activate  # Or: venv\Scripts\activate on Windows
pip install -r requirements.txt
```

---

## ⚙️ Run the Server

```bash
uvicorn app.main:app --reload
```

Or use the shortcut:

```bash
python run.py
```

---

## 📚 API Documentation

Swagger UI is available at:

```
http://localhost:8000/docs
```

ReDoc alternative:

```
http://localhost:8000/redoc
```

---

## 🌍 Sample Endpoints

| Endpoint                 | Description                         |
|--------------------------|-------------------------------------|
| `/api/v1/uuid`           | Generate UUID v4                   |
| `/api/v1/hash/md5?text=hello` | Get hash for given input        |
| `/api/v1/encode/base64?text=test` | Encode text to Base64      |
| `/api/v1/decode/base64?b64=...`   | Decode Base64 back to text |
| `/api/v1/timestamp`      | Current timestamp or convert it    |
| `/api/v1/ipinfo`         | Lookup IP address info             |
| `/api/v1/meta/user-agent`| Analyze User-Agent header          |

---

## 📁 Project Structure

```
developer_toolbox_api/
├── app/
│   ├── api_v1_router.py
│   ├── main.py
│   └── services/
│       ├── uuid.py
│       ├── hash.py
│       ├── base64_tool.py
│       ├── timestamp_tool.py
│       ├── ipinfo_tool.py
│       └── user_agent_tool.py
├── requirements.txt
├── .env
├── run.py
└── README.md
```

---

## 🐋 Docker Support (coming soon)

A Dockerfile will be provided for easy deployment.

---

## 📄 License

MIT License - see [LICENSE](blob/master/LICENSE) for details.

---

## ✨ Author

Crafted with code and caffeine by [Zulwatha](https://github.com/zulwatha)