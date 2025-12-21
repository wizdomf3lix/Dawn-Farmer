import asyncio
from datetime import datetime, timezone, timedelta
from curl_cffi.requests import AsyncSession

class DawnClient:
    _ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36"
    _ep = "https://api.dawninternet.com"
    _ext = "fpdkjdnhkakefebpekbdhillbhonfjjp"
    
    def __init__(self, _t, _p=None):
        self._t = _t
        self._p = _p
        self._s = self._init_session()
        self._uid = None
        self._ext_t = None
    
    def _init_session(self):
        s = AsyncSession(impersonate="chrome120", verify=False)
        s.timeout = 30
        if self._p:
            s.proxies = {"http": self._p, "https": self._p}
        return s
    
    async def _req(self, method, path, **kw):
        url = f"{self._ep}{path}"
        resp = await getattr(self._s, method.lower())(url, **kw)
        return resp.json()
    
    async def auth(self):
        h = {'x-privy-token': self._t, 'User-Agent': self._ua}
        p = {'jwt': 'true', 'role': 'extension'}
        d = await self._req('GET', '/auth', headers=h, params=p)
        self._ext_t = d.get('session_token')
        self._uid = d['user']['id']
        return d
    
    async def get_pts(self):
        h = {'Authorization': f'Bearer {self._ext_t}', 'User-Agent': self._ua}
        p = {'user_id': self._uid}
        return await self._req('GET', '/point', headers=h, params=p)
    
    async def get_streak(self):
        h = {'Authorization': f'Bearer {self._ext_t}', 'User-Agent': self._ua}
        return await self._req('GET', '/ping/streak', headers=h)
    
    async def get_ref(self):
        h = {'x-privy-token': self._t, 'User-Agent': self._ua}
        return await self._req('GET', '/referral/stats', headers=h)
    
    async def get_history(self, days=1):
        h = {'Authorization': f'Bearer {self._ext_t}', 'User-Agent': self._ua}
        sd = (datetime.now(timezone.utc) - timedelta(days=days)).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
        p = {'start_date': sd}
        return await self._req('GET', '/ping', headers=h, params=p)
    
    async def ping(self):
        h = {
            'Authorization': f'Bearer {self._ext_t}',
            'User-Agent': self._ua,
            'Content-Type': 'application/json'
        }
        p = {'role': 'extension'}
        ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
        j = {'user_id': self._uid, 'extension_id': self._ext, 'timestamp': ts}
        return await self._req('POST', '/ping', headers=h, params=p, json=j)
    
    async def close(self):
        await self._s.close()
