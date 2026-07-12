[app]
# العنوان واسم الحزمة
title = روبوت التداول الامن
package.name = secure_trading_bot
package.domain = org.tfc

# إعدادات المصدر
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf

# الإصدار والمتطلبات
version = 1.0
requirements = python3,kivy,arabic-reshaper,python-bidi,requests,metaapi-cloud-sdk

# إعدادات العرض
orientation = portrait
fullscreen = 0

[buildozer]
# مستوى سجلات الخطأ (2 تعني تفاصيل كاملة)
log_level = 2
warn_on_root = 1

[android]
# إعدادات الأندرويد التي تتوافق مع التثبيت اليدوي في build.yml
android.api = 33
android.minapi = 21
android.sdk_build_tools_version = 34.0.0
android.ndk = 25b
android.ndk_api = 21
android.archs = arm64-v8a, armeabi-v7a

# إعدادات إضافية
android.enable_androidx = True
android.private_storage = True
android.permissions = INTERNET
