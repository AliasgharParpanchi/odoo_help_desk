# Help Desk / میز کمک

<!-- [![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)]()
[![Odoo](https://img.shields.io/badge/Odoo-17.0%20%7C%2018.0%20%7C%2019.0-green.svg)]()
[![License](https://img.shields.io/badge/License-LGPL--3-lightgrey.svg)]() -->

---

## 🇬🇧 English

### Overview
**Help Desk** is a fully-featured support ticket management module for Odoo. It allows you to track customer requests, assign tickets to agents, prioritize issues, and generate PDF reports.

### Key Features
- ✅ Create support tickets with title, description, priority (Low/Medium/High)
- ✅ Assign tickets to support agents (users)
- ✅ Track ticket status: New → In Progress → Done → Closed
- ✅ Auto‑generated unique ticket numbers (e.g., `TKT-20250001`)
- ✅ Computed field: `days_open` (how many days the ticket has been open)
- ✅ Validation: cannot close a ticket without a solution
- ✅ Kanban, Tree, Form, and Search views
- ✅ PDF report of open tickets (QWeb)
- ✅ Automated cron job: reminder for tickets pending >3 days
- ✅ REST API endpoints (optional – see below)

### Installation
1. Copy the `help_desk` folder into your Odoo `custom_addons` directory.
2. Update the app list (`Apps` → `Update Apps List`).
3. Search for `help_desk` and click **Install**.

### Configuration
No special configuration is required. After installation, a new top‑menu **Help Desk** will appear.

### API Endpoints (if enabled)
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/helpdesk/tickets` | List all tickets (JSON) |
| POST | `/api/helpdesk/ticket` | Create a new ticket |

### Support
For issues or suggestions, please open an issue on [GitHub](https://github.com/AliasgharParpanchi/odoo_help_desk).

---

## 🇮🇷 فارسی

### معرفی
ماژول **میز کمک** (Help Desk) یک راه‌کار کامل برای مدیریت تیکت‌های پشتیبانی در اودو است. با این ماژول می‌توانید درخواست‌های مشتریان را ثبت، به اپراتورها اختصاص دهید، اولویت‌بندی کنید و گزارش PDF بگیرید.

### ویژگی‌های اصلی
- ✅ ثبت تیکت با عنوان، توضیحات، اولویت (کم/متوسط/بالا)
- ✅ اختصاص تیکت به اپراتورهای پشتیبانی (کاربران)
- ✅ پیگیری وضعیت تیکت: جدید → در حال بررسی → حل شده → بسته شده
- ✅ شماره‌گذاری خودکار یکتا (مثلاً `TKT-20250001`)
- ✅ فیلد محاسباتی: تعداد روزهای باز بودن تیکت
- ✅ اعتبارسنجی: عدم امکان بستن تیکت بدون ارائه راه‌حل
- ✅ نماهای کانبان، درختی، فرم و جستجو
- ✅ گزارش PDF از تیکت‌های باز (QWeb)
- ✅ کرون جاب خودکار: یادآوری تیکت‌های معطل مانده بیش از ۳ روز
- ✅ API های REST (اختیاری – در ادامه توضیح داده شده)

### نصب
1. پوشه `help_desk` را در مسیر `custom_addons` اودو کپی کنید.
2. لیست اپلیکیشن‌ها را به‌روزرسانی کنید (`Apps` → `Update Apps List`).
3. ماژول `help_desk` را جستجو کرده و روی **Install** کلیک کنید.

### تنظیمات
نیاز به تنظیمات خاصی نیست. پس از نصب، یک منوی جدید به نام **میز کمک** در بالای صفحه ظاهر می‌شود.

### API های موجود (در صورت فعال‌سازی)
| متد | آدرس | توضیح |
|------|------|-------|
| GET | `/api/helpdesk/tickets` | دریافت لیست تمام تیکت‌ها (فرمت JSON) |
| POST | `/api/helpdesk/ticket` | ایجاد تیکت جدید |

### پشتیبانی
برای گزارش مشکل یا ارائه پیشنهاد، لطفاً در [گیت‌هاب](https://github.com/AliasgharParpanchi/odoo_help_desk) یک issue باز کنید.

---

## Screenshots / تصاویر

<!-- > _You can add screenshots here. Example:_
> ![Tickets List](static/description/tree_view.png)
> ![Kanban](static/description/kanban.png) -->

---

## Author / نویسنده

**Your Name**  
[GitHub](https://github.com/AliasgharParpanchi) | [LinkedIn](https://linkedin.com/in/yourprofile)

---

## License / مجوز

LGPL-3 – See [LICENSE](LICENSE) for details.