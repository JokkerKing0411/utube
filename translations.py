
class Messages:

    START_MSG = "Salom {}.

Men Youtube-ning yuklovchisiman. Siz menga avtorizatsiyadan o'tgach, youtube-ga istalgan telegram-video yuklash uchun mendan foydalanishingiz mumkin.

Qanday Yuklash Haqida Malumot /help."

    HELP_MSG = [
        ".",
        "🙋Salom.
Avvalo birinchi narsa. Siz shuni bilishingiz kerakki, youtube har bir yuklangan har bir videoni qayta ishlaydi va uning Taxrirlaydi, agar u ko'chirib yozilgan kontentni yuklanganidan Habar topsa va videoni nashr eta olmasangiz, u mualliflik huquqi uchun videoni blocklaydi./n📃Qanday ishlashimni bilish uchun barcha sahifalarni o'qing.",

        "**👇Qanday ishlashimni bilib oling.**

**1-qadam:** Sizga youtube kanalingizga yuklashga ijozat berasiz. Bu haqida boshlang'ich sahifalarda batafsilroq malumot berganmiz.

**2-qadam:** Siz har qanday Telegram-videoni menga yuborasiz.

**3-qadam:** Siz yuborilgan videofaylga javob berasiz (reply) /upload Deb yozasiz. Siz shuningdek, yuklash buyrug'ida ba'zi sarlavhalarni ham ko'rsatishingiz mumkin, lekin ixtiyoriy bo'lsa ham.

**4-qadam**: Faylni uzoqdan yuklab olib, Youtube kanalingizga yuklamoqdaman.

**5-qadam:** Yuklaganingizdan keyin sizga Youtube havolasini yuboraman.",

        "**📣YouTube kanalingizni yarating**

Agar Youtube kanaliga ega bo'lmasangiz, meni ishlatishda hech qanday ma'no yo'q. Shunday qilib, uni yaratish uchun yuqorida keltirilgan amallarni bajaring.

**1-qadam:** Kompyuterga yoki mobil qurilmadan YouTube-ga kiring.

**2-qadam:** Videoni yuklash, sharh yuborish yoki pleylist yaratish kabi kanalni talab qiladigan har qanday harakatni sinab ko'ring.

**3-qadam:** Agar sizda hali kanal yo'q bo'lsa, siz kanal yaratish haqida ko'rsatma olasiz.

**4-qadam:** ma'lumotlarni tekshiring va yangi kanalingizni yaratish uchun tasdiqlang.",

        "**✔YouTube hisobingizni tasdiqlang**

Youtube spam va suiiste'molni juda jiddiy qabul qiladi. Shuning uchun sizdan Youtube hisobingizni tasdiqlash so'raladi. Hisobingizni tasdiqlaganingizdan so'ng, siz 15 daqiqadan ko'proq vaqt davomida video yuklay olasiz. Agar siz hisobingizni tasdiqlamagan bo'lsangiz, 15 daqiqadan ko'proq vaqt yuklangan har bir video o'chiriladi.
[Bu erda Youtube hisobingizni tasdiqlang](http://www.youtube.com/verify)",

        "**🔥Endi avtorizatsiya qilish.**

Sizga Youtube-dagi hisob qaydnomangizga videolarni yuklash huquqini berishingiz kerak. Berilgan havolani ochib, kodni ko'chirib Bu yerga qaytib kelib, kodni tering /authorise _kodingiz_ 

Qo'rqma!
Men hech qanday xaker yoki odamlarning hayotiga aralashishni istagan odam emasman. Men shaxsiy hayotimni hurmat qilaman. Men yordam so'rab kelganlarga yordam berish uchun keldim. Agar men hacker bo'lganimda, men bu erda Telegram Bot yozish uchun o'tirmayman."
    ]

    NOT_A_REPLY_MSG = "👉Iltimos, video faylga javob (reply) qilib yozing."

    NOT_A_MEDIA_MSG = "🔎Media fayl topilmadi. "+NOT_A_REPLY_MSG

    NOT_A_VALID_MEDIA_MSG = "💽Bu yaroqli media emas"

    PROCESSING = "💿Qayta ishlanmoqda....."

    NOT_AUTHENTICATED_MSG = "🚫Siz biron bir qayd yozuviga video yuklash uchun meni tasdiqlamadingiz. autentifikatsiya qilish uchun yordam 👉 /help "

    NO_AUTH_CODE_MSG = "Hech qanday kod yo'q. Iltimos, kodni ko'rsating"

    AUTH_SUCCESS_MSG = "🌟Tabriklaymiz, siz muvaffaqiyatli Youtube-ga yuklashimni tasdiqladingiz!✔"

    AUTH_FAILED_MSG = "autentifikatsiya bajarilmadi\malumot:{}"
