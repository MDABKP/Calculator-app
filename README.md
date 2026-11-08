# ক্যালকুলেটর অ্যাপ (APK বানানোর প্রজেক্ট)

1. জিপ এক্সট্র্যাক্ট করুন।
2. GitHub-এ নতুন Public রিপোজিটরি বানান (যেমন calculator-app)।
3. ভেতরের সব ফাইল ও ফোল্ডার আপলোড করুন (.github ফোল্ডারসহ)।
   .github আপলোড না হলে: Add file → Create new file → নাম দিন `.github/workflows/build-apk.yml` → build-apk-workflow.txt ফাইলের লেখা পেস্ট করে Commit করুন।
4. Actions ট্যাবে বিল্ড চলবে (৫-১০ মিনিট)।
5. শেষ হলে ডানদিকে Releases থেকে app-debug.apk ডাউনলোড করে ইনস্টল করুন।

## স্থায়ী সাইনিং কী
`signing/debug.keystore` ফাইলটি রিপোজিটরিতে থাকতে হবে। এতে এরপর থেকে নতুন APK পুরনোটার ওপরেই আপডেট হিসেবে ইনস্টল হবে।
