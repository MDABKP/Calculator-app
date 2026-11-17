import re, sys
p = 'android/app/src/main/res/values/styles.xml'
s = open(p, encoding='utf-8').read()
m = re.search(r'<style\s+name="AppTheme\.NoActionBarLaunch"([^>]*)>(.*?)</style>', s, re.S)
if not m:
    print('WARNING: AppTheme.NoActionBarLaunch style not found; native splash left unchanged')
    print(s)
    sys.exit(0)
attrs, body = m.group(1), m.group(2)
ns = '' if 'SplashScreen' in attrs else 'android:'
for n in ('windowSplashScreenBackground', 'windowSplashScreenAnimatedIcon', 'windowSplashScreenIconBackgroundColor'):
    body = re.sub(r'\s*<item\s+name="(?:android:)?%s">[^<]*</item>' % n, '', body)
body += ('\n        <item name="%swindowSplashScreenBackground">#FFFFFF</item>'
         '\n        <item name="%swindowSplashScreenAnimatedIcon">@drawable/splash_icon</item>\n    ') % (ns, ns)
new = '<style name="AppTheme.NoActionBarLaunch"%s>%s</style>' % (attrs, body)
s = s[:m.start()] + new + s[m.end():]
open(p, 'w', encoding='utf-8').write(s)
print(new)
