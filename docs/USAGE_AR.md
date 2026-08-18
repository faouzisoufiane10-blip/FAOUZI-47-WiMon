# دليل الاستخدام FAOUZI-47-WiMon

## 🚀 الشروع

راجع [دليل التثبيت](INSTALLATION_AR.md) للتعليمات التفصيلية.

## 📋 الأوامر الأساسية

### إدراج محولات الشبكة اللاسلكية

```bash
wimon list-adapters
```

مثال الإخراج:
```
════════════════════════════════════════════════════════════
FAOUZI-47 WiMon - Adapter Manager
════════════════════════════════════════════════════════════
✓ تم العثور على 2 محول(ات)

[1] wlan0
    MAC: aa:bb:cc:dd:ee:ff
    Mode: managed
    Driver: unknown

[2] wlan1
    MAC: 11:22:33:44:55:66
    Mode: monitor
    Driver: unknown
```

### تفعيل وضع Monitor

```bash
sudo wimon enable-monitor -a wlan0
```

هذا الأمر:
1. إيقاف الواجهة
2. تعيين الواجهة لوضع monitor
3. إعادة تشغيل الواجهة

### تعطيل وضع Monitor

```bash
sudo wimon disable-monitor -a wlan0
```

تبديل الواجهة إلى الوضع المُدار.

### تعيين قناة الشبكة اللاسلكية

```bash
sudo wimon set-channel -a wlan0 -c 6
```

تتراوح القنوات الصحيحة عادة من 1 إلى 13 (حسب المنطقة).

### تشغيل تحليل الذكاء الاصطناعي

```bash
wimon analyze
```

يشغل محرك تحليل التهديدات المدعوم بالذكاء الاصطناعي.

مثال الإخراج:
```
════════════════════════════════════════════════════════════
AI Network Analysis Engine
════════════════════════════════════════════════════════════
Threat Level: LOW
Confidence: 2.0%

Summary: Analyzed 2 packets. Threat level: low

Recommendations:
  • Network appears normal
```

### عرض معلومات النظام

```bash
wimon info
```

يعرض الإصدار والميزات وأمثلة الاستخدام.

## 🔧 الاستخدام المتقدم

### إدارة محولات متعددة

يمكن لـ WiMon إدارة محولات شبكة لاسلكية متعددة:

```bash
# إدراج جميع المحولات
wimon list-adapters

# تفعيل monitor على المحول الأساسي
sudo wimon enable-monitor -a wlan0

# تفعيل monitor على المحول الثانوي
sudo wimon enable-monitor -a wlan1

# القفز بين القنوات
sudo wimon set-channel -a wlan0 -c 1
sleep 5
sudo wimon set-channel -a wlan0 -c 6
sleep 5
sudo wimon set-channel -a wlan0 -c 11
```

### التكامل مع التقاط الحزم

يتكامل WiMon مع أدوات الشبكة اللاسلكية القياسية:

```bash
# تفعيل وضع monitor مع WiMon
sudo wimon enable-monitor -a wlan0

# استخدام tcpdump للالتقاط
sudo tcpdump -i wlan0 -w capture.pcap

# استخدام Wireshark للتحليل
wireshark capture.pcap

# تعطيل وضع monitor عند الانتهاء
sudo wimon disable-monitor -a wlan0
```

### سير عمل تحليل آلي

```bash
#!/bin/bash
# تفعيل وضع monitor
sudo wimon enable-monitor -a wlan0

# التقاط الحزم لمدة 30 ثانية
sudo timeout 30 airodump-ng wlan0 -w output

# تشغيل تحليل الذكاء الاصطناعي
wimon analyze

# تعطيل وضع monitor
sudo wimon disable-monitor -a wlan0
```

## 📝 أفضل الممارسات

1. **تحقق دائمًا من التفويض** قبل اختبار أي شبكة
2. **استخدم الآلات الافتراضية** للاختبار والتطوير
3. **حافظ على تحديث الأداة** لإصلاحات الأخطاء
4. **استخدم تشفيرًا قويًا** عند التقاط البيانات
5. **وثق النتائج** للتقارير

## 🆘 الدعم

- استشر [الهندسة المعمارية](ARCHITECTURE_AR.md)
- اقرأ [README الرئيسي](../README.md)
- افتح issue على GitHub
- تحقق من المشاكل الموجودة

---

**آخر تحديث:** 2024
**الإصدار:** 0.1.0
