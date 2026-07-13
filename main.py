from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.network.urlrequest import UrlRequest
from kivy.clock import Clock
import json
import time

# ==========================================
# 🛑 ضع بياناتك السرية هنا 🛑
# ==========================================
METAAPI_TOKEN = "eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI5MDMzODY0NjJiZjI4ZTg2YTQ3MDM5MDAyNjExZWI1YyIsImFjY2Vzc1J1bGVzIjpbeyJpZCI6InRyYWRpbmctYWNjb3VudC1tYW5hZ2VtZW50LWFwaSIsIm1ldGhvZHMiOlsidHJhZGluZy1hY2NvdW50LW1hbmFnZW1lbnQtYXBpOnJlc3Q6cHVibGljOio6KiJdLCJyb2xlcyI6WyJyZWFkZXIiLCJ3cml0ZXIiXSwicmVzb3VyY2VzIjpbIio6JFVTRVJfSUQkOioiXX0seyJpZCI6Im1ldGFhcGktcmVzdC1hcGkiLCJtZXRob2RzIjpbIm1ldGFhcGktYXBpOnJlc3Q6cHVibGljOio6KiJdLCJyb2xlcyI6WyJyZWFkZXIiLCJ3cml0ZXIiXSwicmVzb3VyY2VzIjpbIio6JFVTRVJfSUQkOioiXX0seyJpZCI6Im1ldGFhcGktcnBjLWFwaSIsIm1ldGhvZHMiOlsibWV0YWFwaS1hcGk6d3M6cHVibGljOio6KiJdLCJyb2xlcyI6WyJyZWFkZXIiLCJ3cml0ZXIiXSwicmVzb3VyY2VzIjpbIio6JFVTRVJfSUQkOioiXX0seyJpZCI6Im1ldGFhcGktcmVhbC10aW1lLXN0cmVhbWluZy1hcGkiLCJtZXRob2RzIjpbIm1ldGFhcGktYXBpOndzOnB1YmxpYzoqOioiXSwicm9sZXMiOlsicmVhZGVyIiwid3JpdGVyIl0sInJlc291cmNlcyI6WyIqOiRVU0VSX0lEJDoqIl19LHsiaWQiOiJtZXRhc3RhdHMtYXBpIiwibWV0aG9kcyI6WyJtZXRhc3RhdHMtYXBpOnJlc3Q6cHVibGljOio6KiJdLCJyb2xlcyI6WyJyZWFkZXIiLCJ3cml0ZXIiXSwicmVzb3VyY2VzIjpbIio6JFVTRVJfSUQkOioiXX0seyJpZCI6InJpc2stbWFuYWdlbWVudC1hcGkiLCJtZXRob2RzIjpbInJpc2stbWFuYWdlbWVudC1hcGk6cmVzdDpwdWJsaWM6KjoqIl0sInJvbGVzIjpbInJlYWRlciIsIndyaXRlciJdLCJyZXNvdXJjZXMiOlsiKjokVVNFUl9JRCQ6KiJdfSx7ImlkIjoiY29weWZhY3RvcnktYXBpIiwibWV0aG9kcyI6WyJjb3B5ZmFjdG9yeS1hcGk6cmVzdDpwdWJsaWM6KjoqIl0sInJvbGVzIjpbInJlYWRlciIsIndyaXRlciJdLCJyZXNvdXJjZXMiOlsiKjokVVNFUl9JRCQ6KiJdfSx7ImlkIjoibXQtbWFuYWdlci1hcGkiLCJtZXRob2RzIjpbIm10LW1hbmFnZXItYXBpOnJlc3Q6ZGVhbGluZzoqOioiLCJtdC1tYW5hZ2VyLWFwaTpyZXN0OnB1YmxpYzoqOioiXSwicm9sZXMiOlsicmVhZGVyIiwid3JpdGVyIl0sInJlc291cmNlcyI6WyIqOiRVU0VSX0lEJDoqIl19LHsiaWQiOiJiaWxsaW5nLWFwaSIsIm1ldGhvZHMiOlsiYmlsbGluZy1hcGk6cmVzdDpwdWJsaWM6KjoqIl0sInJvbGVzIjpbInJlYWRlciJdLCJyZXNvdXJjZXMiOlsiKjokVVNFUl9JRCQ6KiJdfV0sImlnbm9yZVJhdGVMaW1pdHMiOmZhbHNlLCJ0b2tlbklkIjoiMjAyMTAyMTMiLCJpbXBlcnNvbmF0ZWQiOmZhbHNlLCJyZWFsVXNlcklkIjoiOTAzMzg2NDYyYmYyOGU4NmE0NzAzOTAwMjYxMWViNWMiLCJpYXQiOjE3ODM5MzAwMTZ9.XLoMq282bJReWuBOjJjzh6Mo4ZTqKYdQYDnN1dyItr0clSfblAapNiol9m87li5EaG9je23RqnVlqRoOm8CMP73YTiUrzF7n5qNc2aQSfE-Ka_lKkGj4fEO_fC431qXX6FJ72FLLPiSAScKWJ68ENFleAX71uctlvIyZ4tty9WMdrPYkH4Cjzsw1pX2-H0bg1RYtSJWeRpb5Ge8U1YsJ1EZK5aFZ5dEwUullYX4omYryA4_zwkqQ7TKILI6F0JHfN8r1fXXMG8Ezqzgv8jZhOhgAS5NF8wZW0GEruioM-Pf2Y0RNqf0OD1PaPhy3tSvur-xG-3AmBA9lQhu4X6HuIr3X9jsPjoWn5V_AFDl9GsQUvq3mB0C7rYY2UPDv7ZVukT0DYRJUgcQ5HU4usrk6QbDnYfJLhbFqhPK2fxnxW_jOSwWxx3qLu75nk4dF-LHcjWcx2mwyWG2RydKpbXJgcQWYe8PQsSQ88kHvPIroOdYJ_LIhjimu3QmDv1zv8thYd1-1l1Ss4MoiBC_3x12YDDlZ6m5TegyQSj045xk93-zlrDmfJ3Foux7-dpgCuLHJsuhI8GxGxJ_21G6PhOrrteIjFwfOu-o_7VxRNwoCfokSFc_-B0VqDhOLFWUVPGIRd1PUhWzPjFPPnw-Oan5-lAAB0suCSUapIvkQ8gExETs                                                                                                "
ACCOUNT_ID = "1200147333"
# ==========================================

# رابط خادم MetaAPI الأساسي لقراءة البيانات
BASE_URL = f"https://mt-client-api-v1.new-york.agiliumtrade.ai/users/current/accounts/{ACCOUNT_ID}"
HEADERS = {'auth-token': METAAPI_TOKEN, 'Content-Type': 'application/json'}

class PhoneTraderDashboard(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        self.padding = 20
        self.spacing = 15
        
        # 1. العنوان
        self.add_widget(Label(text="🛡️ WES MOBILE TRADER", font_size='22sp', size_hint_y=None, height=50, color=(1, 0.62, 0, 1)))
        
        # 2. بيانات الحساب
        self.account_box = GridLayout(cols=3, size_hint_y=None, height=60, spacing=10)
        self.balance_lbl = Label(text="Balance:\nLoading...", font_size='13sp')
        self.equity_lbl = Label(text="Equity:\nLoading...", font_size='13sp')
        self.profit_lbl = Label(text="Profit:\nLoading...", font_size='13sp')
        self.account_box.add_widget(self.balance_lbl)
        self.account_box.add_widget(self.equity_lbl)
        self.account_box.add_widget(self.profit_lbl)
        self.add_widget(self.account_box)
        
        # 3. جدول السوق اللحظي
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
            sig_lbl = Label(text="WAITING", font_size='12sp', color=(0.6, 0.6, 0.6, 1))
            
            self.market_grid.add_widget(s_lbl)
            self.market_grid.add_widget(b_lbl)
            self.market_grid.add_widget(a_lbl)
            self.market_grid.add_widget(sig_lbl)
            
            self.ui_symbols[sym] = {"bid": b_lbl, "ask": a_lbl, "signal": sig_lbl}
            
        self.add_widget(self.market_grid)
        
        # 4. سجل العمليات
        self.add_widget(Label(text="📜 Live Bot Activity:", font_size='14sp', size_hint_y=None, height=30, halign='left'))
        self.scroll = ScrollView()
        self.log_label = Label(text="Connecting to MetaAPI...", font_size='11sp', size_hint_y=None, halign='left', valign='top', color=(0.2, 0.8, 0.2, 1))
        self.log_label.bind(texture_size=self.log_label.setter('size'))
        self.scroll.add_widget(self.log_label)
        self.add_widget(self.scroll)
        
        self.logs = []
        
        # بدء جلب البيانات فوراً
        Clock.schedule_once(self.get_account_info, 1)
        Clock.schedule_interval(self.get_market_prices, 3.0) # فحص الأسعار كل 3 ثوانٍ

    def add_log(self, text):
        timestamp = time.strftime("%H:%M:%S")
        self.logs.append(f"[{timestamp}] {text}")
        if len(self.logs) > 15: self.logs.pop(0)
        self.log_label.text = "\n".join(self.logs)

    def get_account_info(self, dt):
        """جلب رصيد الحساب المباشر من JustMarkets"""
        url = f"{BASE_URL}/account-information"
        UrlRequest(url, req_headers=HEADERS, on_success=self.update_account_ui, on_error=self.on_net_error)

    def update_account_ui(self, req, result):
        self.balance_lbl.text = f"Balance:\n${result.get('balance', 0):.2f}"
        self.equity_lbl.text = f"Equity:\n${result.get('equity', 0):.2f}"
        profit = result.get('equity', 0) - result.get('balance', 0)
        self.profit_lbl.text = f"Profit:\n${profit:.2f}"
        self.profit_lbl.color = (0.2, 0.8, 0.2, 1) if profit >= 0 else (1, 0.2, 0.2, 1)

    def get_market_prices(self, dt):
        """قراءة أسعار الرموز اللحظية من السوق"""
        for sym in self.symbols:
            url = f"{BASE_URL}/symbols/{sym}/current-price"
            UrlRequest(url, req_headers=HEADERS, on_success=lambda r, res, s=sym: self.update_price_ui(s, res), on_error=self.on_net_error)

    def update_price_ui(self, symbol, result):
        bid = result.get('bid', 0.0)
        ask = result.get('ask', 0.0)
        self.ui_symbols[symbol]["bid"].text = f"{bid:.2f}"
        self.ui_symbols[symbol]["ask"].text = f"{ask:.2f}"
        # هنا يمكنك تفعيل استراتيجية الشراء والبيع بناءً على الأسعار
        self.add_log(f"تم تحديث سعر {symbol}: {bid:.2f}")

    def on_net_error(self, req, error):
        self.log_label.text = "⚠️ فشل الاتصال بخادم التداول. جاري المحاولة..."

class MobileTraderApp(App):
    def build(self):
        return PhoneTraderDashboard()

if __name__ == '__main__':
    MobileTraderApp().run()
