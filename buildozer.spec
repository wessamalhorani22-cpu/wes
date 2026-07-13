[app]
# إعدادات التطبيق الأساسية
title = روبوت التداول الامن
package.name = secure_trading_bot
package.domain = org.tfc
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf
version = 1.0
requirements = python3, kivy, python-bidi, arabic-reshaper, requests
orientation = portrait
fullscreen = 0

# إعدادات الأندرويد
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21
android.archs = arm64-v8a, armeabi-v7a
android.enable_androidx = True
android.private_storage = True

# السر السحري للموافقة على التراخيص تلقائياً من داخل الإعدادات
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
