import { useEffect, useState } from "react";
import "./App.css";

import {
  createFeedback,
  getFeedbacks,
  deleteFeedback,
  getStats,
} from "./api";


function App() {
  const [text, setText] = useState("");
  const [feedbacks, setFeedbacks] = useState([]);
  const [stats, setStats] = useState({
    total: 0,
    positive: 0,
    negative: 0,
    neutral: 0,
  });

  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  async function loadData() {
    try {
      const feedbacksData = await getFeedbacks();
      const statsData = await getStats();

      setFeedbacks(feedbacksData);
      setStats(statsData);
    } catch (error) {
      setError(error.message);
    }
  }

  useEffect(() => {
    loadData();
  }, []);

  async function handleSubmit(event) {
    event.preventDefault();

    if (text.trim() === "") {
      setError("Введите текст для анализа");
      return;
    }

    try {
      setLoading(true);
      setError("");

      await createFeedback(text);

      setText("");
      await loadData();
    } catch (error) {
      setError(error.message);
    } finally {
      setLoading(false);
    }
  }

  async function handleDelete(id) {
    try {
      setError("");

      await deleteFeedback(id);
      await loadData();
    } catch (error) {
      setError(error.message);
    }
  }

  function getLabelText(label) {
    if (label === "positive") {
      return "Позитивный";
    }

    if (label === "negative") {
      return "Негативный";
    }

    if (label === "neutral") {
      return "Нейтральный";
    }

    return label;
  }

  function getLabelClass(label) {
    if (label === "positive") {
      return "label positive";
    }

    if (label === "negative") {
      return "label negative";
    }

    if (label === "neutral") {
      return "label neutral";
    }

    return "label";
  }

  return (
    <div className="app">
      <div className="container">
        <header className="header">
          <div>
            <p className="eyebrow">FastAPI + React + AI</p>
            <h1>AI Feedback Analyzer</h1>
            <p className="subtitle">
              Анализатор отзывов на основе реальной NLP-модели.
            </p>
          </div>
        </header>

        <section className="stats-grid">
          <div className="stat-card">
            <span>Всего</span>
            <strong>{stats.total}</strong>
          </div>

          <div className="stat-card">
            <span>Позитивные</span>
            <strong>{stats.positive}</strong>
          </div>

          <div className="stat-card">
            <span>Негативные</span>
            <strong>{stats.negative}</strong>
          </div>

          <div className="stat-card">
            <span>Нейтральные</span>
            <strong>{stats.neutral}</strong>
          </div>
        </section>

        <main className="main-grid">
          <section className="card form-card">
            <h2>Новый анализ</h2>
            <p className="card-description">
              Введите отзыв, комментарий или сообщение. Backend отправит текст в
              AI-модель и сохранит результат в базу данных.
            </p>

            <form onSubmit={handleSubmit}>
              <textarea
                value={text}
                onChange={(event) => setText(event.target.value)}
                placeholder="Например: Урок был очень полезный, всё понятно объяснили..."
              />

              <button type="submit" disabled={loading}>
                {loading ? "Анализируем..." : "Проанализировать"}
              </button>
            </form>

            {error && <div className="error">{error}</div>}
          </section>

          <section className="card history-card">
            <div className="history-header">
              <div>
                <h2>История анализов</h2>
                <p className="card-description">
                  Все записи, которые были сохранены в SQLite.
                </p>
              </div>

              <button className="secondary-btn" onClick={loadData}>
                Обновить
              </button>
            </div>

            {feedbacks.length === 0 ? (
              <div className="empty">
                Пока нет записей. Добавьте первый отзыв.
              </div>
            ) : (
              <div className="feedback-list">
                {feedbacks.map((feedback) => (
                  <article className="feedback-item" key={feedback.id}>
                    <div className="feedback-top">
                      <span className={getLabelClass(feedback.ai_label)}>
                        {getLabelText(feedback.ai_label)}
                      </span>

                      <span className="confidence">
                        Уверенность: {Math.round(feedback.confidence * 100)}%
                      </span>
                    </div>

                    <p className="feedback-text">{feedback.text}</p>

                    <div className="feedback-bottom">
                      <span>ID: {feedback.id}</span>

                      <button
                        className="delete-btn"
                        onClick={() => handleDelete(feedback.id)}
                      >
                        Удалить
                      </button>
                    </div>
                  </article>
                ))}
              </div>
            )}
          </section>
        </main>
      </div>
    </div>
  );
}

export default App;