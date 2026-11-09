<div dir="rtl">

# 🔑 الحلول المرجعية: الفصل الثاني: القيم، المتغيرات، والعمليات الأساسية

> حاول الحل بنفسك أولاً داخل الدفتر! وقد تعتمد بعض الحلول على خلايا سابقة من الفصل (مثل `Account` في الفصل 8 و`store` في الفصل 12)، فشغّل خلايا الفصل أولاً.

## الاستيرادات المشتركة

```python
# ✍️ حلول مرجعية (جرّب بنفسك أولاً!)
```

## 🟢 التحدي 1

```python
celsius: float = 37.0
fahrenheit = celsius * 9 / 5 + 32
print(f"{celsius}°C = {fahrenheit:.2f}°F")
```

## 🟡 التحدي 2

```python
price = 250
discounted = price * (1 - 0.10)
final_total = discounted * (1 + 0.15)
print(f"الإجمالي النهائي: {final_total:.2f}")
```

## 🔴 التحدي 3

```python
seconds = 100000
days, rest = divmod(seconds, 86400)
hours, rest = divmod(rest, 3600)
minutes, secs = divmod(rest, 60)
print(f"{days} يوم، {hours} ساعة، {minutes} دقيقة، {secs} ثانية")
```

---
[⬅️ العودة إلى الفصل](../../part-1-foundations/02-values-and-operators.ipynb) | [🏠 بنك التحديات](../README.md)

</div>
