import streamlit as st
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


@st.cache_data
def load_data(path):
    data = pd.read_csv(path).sample(100)
    data["Name_len"] = data["Name"].str.len()
    return data


def fit_titanic_model(df):
    df["Sex"] = pd.get_dummies(df["Sex"], drop_first=True)

    df_train, df_test = train_test_split(df, test_size=0.2, random_state=42)

    features = ["Pclass", "Sex", "Age", "Fare", "Name_len"]
    target = "Survived"

    model = LogisticRegression(random_state=42)
    model.fit(X=df_train[features], y=df_train[target])
    df_train["predict"] = model.predict(df_train[features])
    accuracy = accuracy_score(y_true=df_train["Survived"], y_pred=df_train["predict"])
    return model, accuracy


def get_predict(model, df_features):
    predict = model.predict(df_features)
    return predict


if __name__ == "__main__":
    path = ""
    data = load_data(path)

    st.write("""
    # Титаник
    
    Цель состоит в том, чтобы разработать классификационную модель, позволяющую предсказать, выживет ли пассажир или погибнет.
    """)
    st.write(data[:10])

    #features
    pclass = st.sidebar.selectbox(
        'Выберите класс:',
        set(data['Pclass']))
    st.sidebar.write('Класс:', pclass)

    sex = st.sidebar.selectbox(
        'Выберите пол:',
        set(data['Sex']))
    st.sidebar.write('Пол:', sex)

    age = st.sidebar.slider("Age", min_value=min((data['Age'].astype(int))), max_value=max(data['Age'].astype(int)))
    st.sidebar.write('Возраст:', age)

    fare = st.sidebar.slider("Fare", min_value=min((data['Fare'].astype(int))), max_value=max(data['Fare'].astype(int)))
    st.sidebar.write('Плата за проезд:', fare)

    name_len = st.sidebar.slider("Name_len", min_value=min(data['Name_len']),
                                 max_value=max(data['Name_len']))
    st.sidebar.write('Длина имени:', name_len)

    st.markdown("""
    ### Описание полей
    
     - Pclass — класс пассажира (1 — высший, 2 — средний, 3 — низший);

     - Name — имя;
    
     - Sex — пол;
    
     - Age — возраст;
    
     - SibSp — количество братьев, сестер, сводных братьев, сводных сестер, супругов на борту титаника;
    
     - Parch — количество родителей, детей (в том числе приемных) на борту титаника;
    
     - Ticket — номер билета;
    
     - Fare — плата за проезд;
    
     - Cabin — каюта;
    
     - Embarked — порт посадки (C — Шербур; Q — Квинстаун; S — Саутгемптон).
    
    
    """)
    dict_data = {"Pclass": pclass,
                 "Sex": sex,
                 "Age": age,
                 "Fare": fare,
                 "Name_len": name_len}

    data_predict = pd.DataFrame([dict_data])
    data_predict["Sex"] = pd.get_dummies(data_predict["Sex"])
    st.write(data_predict)

    button = st.button("Predict")
    if button:
        model, accuracy = fit_titanic_model(data)
        st.success(f"Точность: {accuracy}")
        output = get_predict(model, data_predict)
        if output == 0:
            st.success("Выживет")
        else:
            st.success("Не выживет")