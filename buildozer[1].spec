[app]

# (string) Title of your application
title = روبوت التداول الامن

# (string) Package name
package.name = secure_trading_bot

# (string) Package domain (needed for android packaging)
package.domain = org.tfc

# (string) Source code directory
source.dir = .

# (list) Source files to include (added ttf for the Arabic font)
source.include_exts = py,png,jpg,kv,atlas,ttf

# (string) Application version
version = 1.0

# (list) Application requirements
# Added: arabic-reshaper, python-bidi, requests, metaapi-cloud-sdk
requirements = python3,kivy,arabic-reshaper,python-bidi,requests,metaapi-cloud-sdk

# (str) Supported orientations (landscape, portrait or all)
orientation = portrait

# (bool) Use fullscreen or not
fullscreen = 0

# =============================================================================
# Android specific configurations
# =============================================================================

# (list) Permissions required by the app (CRITICAL for trading bot)
android.permissions = INTERNET

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK architecture to build for
android.archs = arm64-v8a, armeabi-v7a

# (bool) Enable AndroidX support
android.enable_androidx = True

# (bool) Private storage or shared
android.private_storage = True

# --- التعديلات الإضافية لضمان استقرار البناء ---
# (str) Android SDK build-tools version
android.sdk_build_tools_version = 34.0.0

# (str) Android NDK version to use
android.ndk = 25b

# (int) Android NDK API to use
android.ndk_api = 21

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug and big logs)
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1