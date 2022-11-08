import streamlit as st
import joblib
import numpy as np

# 헤드라인
st.write("# 보험료 예측")
st.write("> 조건 설정에 따라 보험료를 산정해보실 수 있습니다.")
st.write("> 처음 시도해 보는 데이터 웹앱(streamlit)입니다!")
st.write("> 범주형과 명목형에 따라 값 설정 방식을 바꿨습니다.")
st.image("https://imgur.com/a/0Kklf3n.png")

# 첫번째 행

r1_col1, r1_col2, r1_col3 = st.columns(3)

age = r1_col1.slider("age", 0, 100)

bmi = r1_col2.slider("bmi", 0, 50)

children = r1_col3.slider("children", 0,8)

# 두번째 행
r2_col1, r2_col2, r2_col3 = st.columns(3)

sex_option = ("male", "female")
sex = r2_col1.selectbox("sex", sex_option)
is_male = sex_option[0] == sex

region_option = ('southwest', 'southeast', 'northwest', 'northeast')
region = r2_col2.selectbox("region", region_option)
is_southwest = region_option[0] == region
is_southeast = region_option[1] == region
is_northwest = region_option[2] == region

r2_col3.write("smoker")
smoker = r2_col3.checkbox("")


# 예측 버튼
predict_button = st.button("예측")

st.write("---")

# 예측 결과
if predict_button:
    model = joblib.load('first_model.pkl')

    pred = model.predict(np.array([[age, bmi, children, smoker * 1,
        is_male * 1, is_northwest * 1, is_southeast * 1, is_southwest * 1]]))

    st.metric("예측 보험료", pred[0])