import os
import uvicorn
from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv()
    port = int(os.getenv('PORT'))
    reload = bool(os.getenv('RELOAD', True))
    uvicorn.run("src:app", host="0.0.0.0", port=port, reload=reload)

