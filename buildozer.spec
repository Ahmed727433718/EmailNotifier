[app]

title = Email Notifier

package.name = emailnotifier

package.domain = org.example

source.dir = .

source.include_exts = py,png,jpg,kv

version = 1.0

requirements = python3,kivy,plyer

orientation = portrait

android.permissions = INTERNET,POST_NOTIFICATIONS

android.api = 34
android.build_tools_version = 34.0.0
android.accept_sdk_license = True

android.minapi = 23

android.archs = arm64-v8a,armeabi-v7a


[buildozer]

log_level = 2
