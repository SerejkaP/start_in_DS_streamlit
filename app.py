import streamlit as st
import time
import pandas as pd
import matplotlib.pyplot as plt

def load_data():
    data = pd.read_csv("titanic_data.csv")
    return data

def calculate_survived_by_sex(data: pd.DataFrame, sex:str):
    total = len(data.loc[(data['Sex'] == sex)])
    survived = len(data.loc[((data['Sex'] == 'female') & (data['Survived'] == 1))])
    percent = survived/total
    sex_desc = "мужчины" if sex=='male' else  "женщины"
    return f"Для {sex_desc} шанс выжить: {round(percent*100, 3)}%"

def calculate_survived(data: pd.DataFrame):
    total = len(data)
    survived = len(data.loc[(data['Survived'] == 1)])
    survived_percent = survived/total
    not_survived_percent = 1 - survived_percent
    return (survived_percent, not_survived_percent)

def show_main_page():
    st.write("# Титаник")
    st.markdown("[«Тита́ник»](https://ru.wikipedia.org/wiki/%D0%A2%D0%B8%D1%82%D0%B0%D0%BD%D0%B8%D0%BA) (англ. Titanic) — " +
                "британский трансатлантический пассажирский пароход, " +
                "второй лайнер класса «Олимпик» компании «White Star Line». " + 
                "Крупнейшее судно в мировой истории начала XX века. " +
                "При строительстве получил номер 401.\n\n" +
                "Во время первого рейса, в ночь с 14 на 15 апреля 1912 года, столкнулся с айсбергом и затонул в Северной Атлантике.")

    is_data_loaded = False
    st.header("Добавьте информацию:")
    radio = st.radio("Укажите пол", ["male", "female"])
    show_table = st.checkbox("Загрузить и показать таблицу данных")
    show_hist = st.checkbox("Показать гистограму")

    if st.button('Загрузить данные...'):
        loading = st.text("Загрузка...")
        data = load_data()
        time.sleep(0.5)
        is_data_loaded = True
        loading.text("Данные загружены")

        st.text(calculate_survived_by_sex(data, radio))

        if show_hist:
            (survived_percent, not_survived_percent) = calculate_survived(data)
            fig1, ax1 = plt.subplots()
            ax1.pie((survived_percent, not_survived_percent), (0.1, 0), ("Выжили", "Не выжили"), autopct='%1.1f%%', shadow=True, startangle=90)
            ax1.axis('equal')
            st.pyplot(fig1)

        if show_table:
            st.table(data)

if __name__ == "__main__":
    show_main_page()