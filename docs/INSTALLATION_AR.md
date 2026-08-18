# دليل تثبيت FAOUZI-47-WiMon

## 📋 المتطلبات

- Python 3.9 أو أحدث
- Linux (موصى به: Ubuntu 20.04+, Debian 11+)
- محول شبكة لاسلكي يدعم وضع Monitor
- صلاحيات root/sudo

## 🚀 البدء السريع

### 1. استنساخ المستودع

```bash
git clone https://github.com/faouzisoufiane10-blip/FAOUZI-47-WiMon.git
cd FAOUZI-47-WiMon
```

### 2. إنشاء بيئة افتراضية

```bash
python3 -m venv venv
source venv/bin/activate  # على Windows: venv\Scripts\activate
```

### 3. تثبيت المتعلقات

```bash
make install
```

أو يدويًا:

```bash
pip install -r requirements.txt
pip install -e .
```

### 4. التحقق من التثبيت

```bash
wimon info
```

## 🔧 متعلقات النظام

### Ubuntu/Debian

```bash
sudo apt-get update
sudo apt-get install -y \
    python3-dev \
    wireless-tools \
    iwconfig \
    net-tools \
    aircrack-ng
```

### Fedora/RHEL

```bash
sudo dnf install -y \
    python3-devel \
    wireless-tools \
    iwconfig \
    net-tools
```

## ⚙️ الإعدادات

### تفعيل ميزات LLM (اختياري)

أنشئ ملف `.env` في جذر المشروع:

```bash
echo "OPENAI_API_KEY=مفتاح_api_الخاص_بك" > .env
```

## 🔍 استكشاف الأخطاء

### خطأ: "لم يتم العثور على أي محول لاسلكي"

1. تحقق من وجود محول الشبكة:
   ```bash
   iwconfig
   ```

2. تحقق من تحميل السائق:
   ```bash
   lsmod | grep -i wireless
   ```

3. تحقق من حجب rfkill:
   ```bash
   rfkill list
   rfkill unblock wifi  # إذا لزم الأمر
   ```

### خطأ: "إذن مرفوض"

استخدم sudo:
```bash
sudo wimon enable-monitor -a wlan0
```

## 📝 الخطوات التالية

1. اقرأ [دليل الاستخدام](USAGE_AR.md)
2. تحقق من [الهندسة المعمارية](ARCHITECTURE_AR.md)
3. راجع [أوامر CLI](COMMANDS_AR.md)

---

**آخر تحديث:** 2024
**الإصدار:** 0.1.0
