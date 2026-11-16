import streamlit as st

# 1. หัวข้อหน้าเว็บ
st.markdown("## :red[🚨 แจ้งเตือน: ห้าม Print Screen ตัวอย่าง]")
st.title("🧾 แอปคำนวณส่วนลดและ VAT 7%")

# 2. รับข้อมูลราคาเต็ม และ เปอร์เซ็นต์ส่วนลด
price = st.number_input("กรอกราคาเต็มของสินค้า (บาท):", min_value=0.0, value=0.0)
discount_percent = st.number_input("กรอกส่วนลด (%):", min_value=0.0, max_value=100.0, value=0.0)

# 3. คำนวณตามลำดับ (หักส่วนลด -> คิด VAT -> รวมสุทธิ)
discount_amount = price * (discount_percent / 100)
price_after_discount = price - discount_amount
vat = price_after_discount * 0.07
net_price = price_after_discount + vat

# 4. แสดงผลลัพธ์ทีละขั้นตอน
st.divider()
st.write(f"• ส่วนลด ({discount_percent:.0f}%): -{discount_amount:,.2f} บาท")
st.write(f"• ราคาหลังหักส่วนลด: {price_after_discount:,.2f} บาท")
st.write(f"• ภาษีมูลค่าเพิ่ม (VAT 7%): +{vat:,.2f} บาท")
st.header(f"• ราคาสุทธิที่ต้องจ่าย: **{net_price:,.2f}** บาท")

st.divider()
st.write("นางสาวดีใจ ยิ้มแย้ม เลขที่ 5  ม.4/5")
