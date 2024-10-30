import streamlit as st


체크 = st.checkbox("가나다")
짜장면 = st.checkbox("짜장면(5000원)")
짬뽕 = st.checkbox("짬뽕(7000원)")
탕수육 = st.checkbox("탕수육(15000원)")
가격 = 0
if 짜장면:
    가격 += 5000
if 짬뽕:
    가격 += 7000
if 탕수육:
    가격 += 15000
if 체크:
    가격 -=1000
st.subheader(f"선택한 음식의 가격은 {가격}입니다.")


버튼 = st.button("버튼")
if 버튼:
    st.write("버튼을 눌렀습니다")

st.title("😎Title")
st.header("Header")
st.write("작은글씨")
st.markdown(":red[작은글씨]")