from youtube_upload.auth import GoogleAuth
from youtube_upload.youtube import Youtube

from config import Config

from translations import Messages as tr

import os
import time
import traceback

class Uploader:

    def __init__(self, file, title=None):
        
        self.file = file
        
        self.title = title


    async def start(self, progress=None, *args):
        self.progress = progress
        self.args = args

        await self._upload()

        return self.status, self.message


    async def _upload(self):
        try:

            auth = GoogleAuth(Config.CLIENT_ID, Config.CLIENT_SECRET)
            
            if not os.path.isfile(Config.CRED_FILE):
                self.status = False
                
                self.message = "📤Meni tasdiqlamaganingiz uchun yuklash amalga oshmadi.✔"
                
                
                return

            auth.LoadCredentialsFile(Config.CRED_FILE)

            google = auth.authorize()

            properties = dict(
                title = self.title if self.title else os.path.basename(self.file),
                description = "🙋Assalomu alaykum Qadirli Kanal Azolari
Szilar bilan Kamina Jahongir bo'lmoqda. 📅Bugungi Video ham Jida qoziq siz aslo Zerikmaysiz Bizni Kanalimzni kuzatishda Davom Eting.
😊 Bu yerda siz o'zingizga kerakli narslarni Topasiz.",
                category = 27,
                privacyStatus = 'private'
            )

            youtube = Youtube(google)

            self.start_time = time.time()
            self.last_time = self.start_time

            r = await youtube.upload_video(video = self.file, properties = properties)

            self.status = True
            self.message = f"💿Sizning videongiz muvaffaqiyatli yuklandi \nYouTube havolasi:👇\nhttps://youtu.be/{r['id']}\n💽Agar Video hajmi Agar Katta bolsa Video Shuncha Sekin Yuklanadi."
        except Exception as e:
            traceback.print_exc()
            self.status = False
            self.message = f"🚫Yuklash jarayonida xatolik yuz berdi. \nXatolik tafsilotlari: {e}"
        return

