[app]
title = روبوت التداول الامن
package.name = secure_trading_bot
package.domain = org.tfc
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf
version = 1.0
requirements = python3,kivy,arabic-reshaper,python-bidi,requests,metaapi-cloud-sdk
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1

[android]
android.api = 33
android.minapi = 21
android.sdk_build_tools_version = 34.0.0
android.ndk = 25b
android.ndk_api = 21
android.archs = arm64-v8a, armeabi-v7a
android.enable_androidx = True
android.private_storage = True
android.permissions = INTERNET
