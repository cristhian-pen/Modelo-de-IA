from db.db import connectDataBase
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC


query = "Select QUESTIONS, ANSWERS from igrislearn"
df = pd.read_sql_query(query, connectDataBase())

vectorizer = TfidfVectorizer(stop_words='english')
x = vectorizer.fit_transform(df['QUESTIONS'])
y = df['ANSWERS']

x_train, x_teste, y_train, y_teste = train_test_split(x, y, test_size=0.2, random_state=42)

classifier = SVC(kernel='linear')

#treinamento da IA
classifier.fit(x_train, y_train)

#vetorização e predição dos dados
def getAnswer(question):
    question_vector = vectorizer.transform([question])
    return classifier.predict(question_vector)[0]

#Busca pergunta no banco de dados
def searchQuestionDB(question):
    conn = connectDataBase()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT QUESTIONS from IGRISLEARN where QUESTIONS like %s',(question))
    result = cursor.fetchone()
    conn.close()

    if result:
        return result['QUESTIONS']
    return None