from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.network.urlrequest import UrlRequest
from kivy.clock import Clock
import time

# إعدادات الحساب عبر المزود الرقمي (كمثال للربط المباشر بالإنترنت)
BROKER_API_URL = "https://api.yourbroker.com/v1" 
ACCOUNT_TOKEN = "YOUR_LIVE_ACCOUNT_API_TOKEN"

class PhoneTraderDashboard(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        self.padding = 20
        self.spacing = 15
        
        # 1. شاشة العنوان والأيقونة
        self.add_widget(Label(text="🛡️ WES MOBILE TRADER", font_size='22sp', size_hint_y=None, height=50, color=(1, 0.62, 0, 1)))
        
        # 2. بيانات الحساب المالي المباشر على الهاتف
        self.account_box = GridLayout(cols=3, size_hint_y=None, height=60, spacing=10)
        self.balance_lbl = Label(text="Balance:\nLoading...", font_size='13sp')
        self.equity_lbl = Label(text="Equity:\nLoading...", font_size='13sp')
        self.profit_lbl = Label(text="Profit:\nLoading...", font_size='13sp')
        self.account_box.add_widget(self.balance_lbl)
        self.account_box.add_widget(self.equity_lbl)
        self.account_box.add_widget(self.profit_lbl)
        self.add_widget(self.account_box)
        
        # 3. جدول مراقبة السوق (ماذا يقرأ التطبيق الآن)
        self.market_grid = GridLayout(cols=4, spacing=5, size_hint_y=None, height=140)
        self.market_grid.add_widget(Label(text="Symbol", bold=True, font_size='12sp'))
        self.market_grid.add_widget(Label(text="Bid", bold=True, font_size='12sp'))
        self.market_grid.add_widget(Label(text="Ask", bold=True, font_size='12sp'))
        self.market_grid.add_widget(Label(text="Signal", bold=True, font_size='12sp'))
        
        self.symbols = ["US30.ecn", "XAUUSD.ecn", "US100.ecn"]
        self.ui_symbols = {}
        
        for sym in self.symbols:
            s_lbl = Label(text=sym, font_size='12sp')
            b_lbl = Label(text="0.00", font_size='12sp')
            a_lbl = Label(text="0.00", font_size='12sp')
            sig_lbl = Label(text="CHECKING", font_size='12sp', color=(0.6, 0.6, 0.6, 1))
            
            self.market_grid.add_widget(s_lbl)
            self.market_grid.add_widget(b_lbl)
            self.market_grid.add_widget(a_lbl)
            self.market_grid.add_widget(sig_lbl)
            
            self.ui_symbols[sym] = {"bid": b_lbl, "ask": a_lbl, "signal": sig_lbl}
            
        self.add_widget(self.market_grid)
        
        # 4. سجل الصفقات والعمليات الحية (ماذا يفتح البوت الآن)
        self.add_widget(Label(text="📜 Live Bot Activity (ما يفتحه ويقرأه البوت):", font_size='14sp', size_hint_y=None, height=30, halign='left'))
        self.scroll = ScrollView()
        self.log_label = Label(text="Bot Initialized on Android...\nWaiting for market data...", font_size='11sp', size_hint_y=None, halign='left', valign='top', color=(0.2, 0.8, 0.2, 1))
        self.log_label.bind(texture_size=self.log_label.setter('size'))
        self.scroll.add_widget(self.log_label)
        self.add_widget(self.scroll)
        
        self.logs = []
        
        # مؤقت لتحديث الأسعار وفحص الاستراتيجية كل ثانيتين من الهاتف مباشرة
        Clock.schedule_interval(self.update_market_data, 2.0)

    def add_log(self, text):
        timestamp = time.strftime("%H:%M:%S")
        self.logs.append(f"[{timestamp}] {text}")
        if len(self.logs) > 15:
            self.logs.pop(0)
        self.log_label.text = "\n".join(self.logs)

    def update_market_data(self, dt):
        """دالة لجلب الأسعار مباشرة من خادم الوسيط عبر الإنترنت"""
        # كمثال: نقوم بطلب أسعار الرموز مباشرة من الـ API الخاص بشركة التداول
        for symbol in self.symbols:
            url = f"{BROKER_API_URL}/rates?symbol={symbol}&token={ACCOUNT_TOKEN}"
            UrlRequest(url, on_success=lambda req, res, s=symbol: self.on_rates_received(s, res), on_error=self.on_connectivity_error, timeout=2)

    def on_rates_received(self, symbol, result):
        # هنا يستقبل الهاتف الأسعار ويقوم بتحديث الواجهة فوراً
        bid = result.get("bid", 0.0)
        ask = result.get("ask", 0.0)
        
        self.ui_symbols[symbol]["bid"].text = f"{bid:.2f}"
        self.ui_symbols[symbol]["ask"].text = f"{ask:.2f}"
        
        # تشغيل معادلة المتوسطات الحسابية (الاستراتيجية) داخل الهاتف
        self.check_strategy_signals(symbol, result.get("history", []))

    def check_strategy_signals(self, symbol, history_data):
        """تحليل البيانات التاريخية القادمة للرمز واتخاذ قرار فتح صفقة"""
        if not history_data:
            return
            
        # حساب إشارة الشراء أو البيع (تبسيط للمتوسطات الحسابية)
        # إذا تحقق الشرط يقوم الجوال بإرسال أمر فتح صفقة فوراً
        signal = "WAITING"
        
        # مثال افتراضي لإشارة تم رصدها
        if symbol == "XAUUSD.ecn" and history_data[-1] > history_data[-2]:
            signal = "BUY"
            self.ui_symbols[symbol]["signal"].text = "BUY 🟢"
            self.ui_symbols[symbol]["signal"].color = (0, 1, 0, 1)
            self.open_mobile_trade(symbol, "BUY")
        else:
            self.ui_symbols[symbol]["signal"].text = "WAITING ⏳"
            self.ui_symbols[symbol]["signal"].color = (0.6, 0.6, 0.6, 1)

    def open_mobile_trade(self, symbol, side):
        """إرسال أمر فتح صفقة مباشرة من الهاتف إلى خادم شركة التداول"""
        self.add_log(f"🎯 الاستراتيجية تحققت! جاري فتح صفقة {side} على {symbol}...")
        
        trade_url = f"{BROKER_API_URL}/trade"
        params = json.dumps({"symbol": symbol, "action": side, "volume": 0.01, "token": ACCOUNT_TOKEN})
        headers = {'Content-type': 'application/json'}
        
        UrlRequest(trade_url, req_body=params, req_headers=headers, 
                   on_success=lambda req, res: self.add_log(f"✅ تم فتح صفقة {side} لرمز {symbol} بنجاح من الجوال!"),
                   on_failure=lambda req, res: self.add_log(f"❌ فشل تنفيذ الصفقة من السيرفر الرئيسي."))

    def on_connectivity_error(self, request, error):
        self.log_label.text = "⚠️ خطأ في الاتصال بالإنترنت.. جاري المحاولة مجدداً."

class MobileTraderApp(App):
    def build(self):
        return PhoneTraderDashboard()

if __name__ == '__main__':
    MobileTraderApp().run()
