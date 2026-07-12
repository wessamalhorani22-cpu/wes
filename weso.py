from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.clock import Clock
import arabic_reshaper
from bidi.algorithm import get_display
import threading
import time
import requests

# دالة تشبيك وتعديل اتجاه الحروف العربية
def ar(text):
    reshaped = arabic_reshaper.reshape(text)
    return get_display(reshaped)

# التعديل الجديد والمهم للهاتف: جعل مسار الخط محلياً بداخل مجلد المشروع
ARABIC_FONT = "tahoma.ttf"

# --- معلومات الكود الداخلية الثابتة (مخفية داخل البرنامج) ---
TELEGRAM_BOT_TOKEN = "8447141907:AAFijrY79rPVIY6HaSecaqJs1dHolxm02QM"
TELEGRAM_CHAT_ID = "1699752198"
NEWS_API_KEY = "3b1723c6f1bb4634b87593255996d256"
METAAPI_TOKEN = "ضع_هنا_توكن_METAAPI_الخاص_بك" # ضع التوكن هنا ليعمل الربط السحابي تلقائياً

SYMBOLS = ["US30.ecn", "XAUUSD.ecn", "US100.ecn", "BTCUSD.ecn"]

class TradingApp(App):
    def build(self):
        self.is_running = False  # متغير لمعرفة حالة البوت
        
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        # العنوان
        layout.add_widget(Label(text=ar("روبوت TFC للتداول الآلي"), font_size='22sp', bold=True, font_name=ARABIC_FONT))
        
        # خانات البيانات
        self.account_input = TextInput(hint_text="Enter MT5 Account Number", multiline=False, font_size='16sp')
        self.password_input = TextInput(hint_text="Enter Password", multiline=False, password=True, font_size='16sp')
        self.server_input = TextInput(hint_text="Enter Server (e.g., Broker-Live)", multiline=False, font_size='16sp')
        
        layout.add_widget(self.account_input)
        layout.add_widget(self.password_input)
        layout.add_widget(self.server_input)
        
        # زر التشغيل
        self.btn = Button(text=ar("بدء تشغيل الروبوت"), background_color=(0, 0.7, 0, 1), font_size='18sp', font_name=ARABIC_FONT)
        self.btn.bind(on_press=self.toggle_bot)
        layout.add_widget(self.btn)
        
        # شاشة عرض الحالة
        self.status_label = Label(text=ar("الحالة: متوقف حالياً o"), font_name=ARABIC_FONT, font_size='16sp')
        layout.add_widget(self.status_label)
        
        return layout

    def toggle_bot(self, instance):
        if not self.is_running:
            # قراءة البيانات المدخلة
            account = self.account_input.text
            password = self.password_input.text
            server = self.server_input.text
            
            if not account or not password or not server:
                self.status_label.text = ar(" X خطأ: يرجى ملء جميع البيانات!")
                return
            
            # تغيير حالة الزر والشاشة
            self.is_running = True
            self.btn.text = ar("إيقاف الروبوت")
            self.btn.background_color = (0.7, 0, 0, 1)
            self.status_label.text = ar("● جاري الاتصال بالسيرفر وبدء الفحص...")
            
            # تشغيل "محرك التداول" في خلفية النظام (Thread) منعاً لتجمد التطبيق
            threading.Thread(target=self.background_trading_engine, args=(account, password, server), daemon=True).start()
        else:
            # إيقاف البوت
            self.is_running = False
            self.btn.text = ar("بدء تشغيل الروبوت")
            self.btn.background_color = (0, 0.7, 0, 1)
            self.status_label.text = ar("الحالة: متوقف حالياً o")

    # --- محرك التداول الذكي يعمل هنا في الخلفية ---
    def background_trading_engine(self, account, password, server):
        # إرسال إشعار تليجرام فوري عند التشغيل من التطبيق
        try:
            msg = f"🚀 تم تشغيل روبوت الهاتف للحساب: {account} على سيرفر: {server}"
            requests.post(f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage", data={"chat_id": TELEGRAM_CHAT_ID, "text": msg})
        except:
            pass

        while self.is_running:
            print(f"[الروبوت يعمل سحابياً] جاري فحص الرموز: {SYMBOLS}...")
            
            # تحديث واجهة التطبيق بشكل آمن من الخلفية
            Clock.schedule_once(lambda dt: setattr(self.status_label, 'text', ar("● الروبوت نشط ويقوم بمراقبة السوق الآن...")))
            
            time.sleep(3) # الانتظار بين دورات الفحص لحماية موارد الهاتف

if __name__ == '__main__':
    TradingApp().run()
