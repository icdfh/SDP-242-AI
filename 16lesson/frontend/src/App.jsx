import { useEffect, useState } from "react";
import axios from "axios";
import "./App.css";

const API_URL = "http://127.0.0.1:8000";

export default function App() {
  const [text, setText] = useState("");
  const [result, setResult] = useState(null);
  const [feedbacks, setFeedbacks] = useState([]);
  const [stats, setStats] = useState({
    positive: 0,
    neutral: 0,
    negative: 0,
    total: 0,
  });
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  async function loadFeedbacks() {
    try {
      const response = await axios.get(`${API_URL}/feedbacks`);
      setFeedbacks(response.data);
    } catch (error) {
      console.log(error);
    }
  }

  async function loadStats() {
    try {
      const response = await axios.get(`${API_URL}/stats`);
      setStats(response.data);
    } catch (error) {
      console.log(error);
    }
  }

  useEffect(() => {
    loadFeedbacks();
    loadStats();
  }, []);

  async function analyzeText() {
    setError("");
    setResult(null);

    if (text.trim().length === 0) {
      setError("Введите текст для анализа");
      return;
    }

    try {
      setLoading(true);

      const response = await axios.post(`${API_URL}/analyze`, {
        text: text,
      });

      setResult(response.data);
      setText("");

      await loadFeedbacks();
      await loadStats();
    } catch (error) {
      console.log(error);
      setError("Произошла ошибка при анализе текста");
    } finally {
      setLoading(false);
    }
  }

  async function deleteFeedback(id) {
    try {
      await axios.delete(`${API_URL}/feedbacks/${id}`);

      await loadFeedbacks();
      await loadStats();
    } catch (error) {
      console.log(error);
    }
  }

  function getConfidencePercent(confidence) {
    return Math.round(confidence * 100);
  }

  function getSentimentLabel(sentiment) {
    if (sentiment === "positive") return "Positive";
    if (sentiment === "negative") return "Negative";
    return "Neutral";
  }

  function getSentimentEmoji(sentiment) {
    if (sentiment === "positive") return "😊";
    if (sentiment === "negative") return "😡";
    return "😐";
  }

  return (
    <div className="app">
      <div className="container">
        <header className="header">
          <div>
            <p className="label">Fullstack AI App</p>
            <h1>Feedback Analyzer</h1>
            <p className="subtitle">
              Analyze customer feedback with AI sentiment detection.
            </p>
          </div>

          <div className="header-badge">
            <span className="dot"></span>
            API Online
          </div>
        </header>

        <main className="grid">
          <section className="card analyze-card">
            <div className="card-head">
              <div>
                <h2>Text Analyze</h2>
                <p>Write feedback and send it to AI model.</p>
              </div>
            </div>

            <textarea
              value={text}
              onChange={(event) => setText(event.target.value)}
              placeholder="Example: This product is amazing, delivery was fast..."
            />

            <div className="actions">
              <button onClick={analyzeText} disabled={loading}>
                {loading ? "Analyzing..." : "Analyze Text"}
              </button>

              <span className="char-count">{text.length} characters</span>
            </div>

            {error && <p className="error">{error}</p>}

            {result && (
              <div className={`result-box ${result.sentiment}`}>
                <div className="result-icon">
                  {getSentimentEmoji(result.sentiment)}
                </div>

                <div>
                  <p className="result-label">AI Result</p>
                  <h3>{getSentimentLabel(result.sentiment)}</h3>
                  <p>
                    Confidence:{" "}
                    <strong>
                      {getConfidencePercent(result.confidence)}%
                    </strong>
                  </p>
                </div>
              </div>
            )}
          </section>

          <section className="stats-grid">
            <div className="stat-card">
              <p>Total</p>
              <h3>{stats.total}</h3>
            </div>

            <div className="stat-card positive">
              <p>Positive</p>
              <h3>{stats.positive}</h3>
            </div>

            <div className="stat-card neutral">
              <p>Neutral</p>
              <h3>{stats.neutral}</h3>
            </div>

            <div className="stat-card negative">
              <p>Negative</p>
              <h3>{stats.negative}</h3>
            </div>
          </section>
        </main>

        <section className="card history-card">
          <div className="card-head">
            <div>
              <h2>Feedback History</h2>
              <p>All analyzed feedbacks from database.</p>
            </div>

            <button className="secondary-btn" onClick={loadFeedbacks}>
              Refresh
            </button>
          </div>

          {feedbacks.length === 0 ? (
            <div className="empty">
              <h3>No feedbacks yet</h3>
              <p>Analyze your first text to see history here.</p>
            </div>
          ) : (
            <div className="feedback-list">
              {feedbacks.map((feedback) => (
                <article key={feedback.id} className="feedback-item">
                  <div className="feedback-main">
                    <div className={`sentiment-pill ${feedback.sentiment}`}>
                      {getSentimentEmoji(feedback.sentiment)}{" "}
                      {getSentimentLabel(feedback.sentiment)}
                    </div>

                    <p className="feedback-text">{feedback.text}</p>

                    <div className="confidence-line">
                      <span>
                        Confidence:{" "}
                        {getConfidencePercent(feedback.confidence)}%
                      </span>

                      <div className="progress">
                        <div
                          className={`progress-fill ${feedback.sentiment}`}
                          style={{
                            width: `${getConfidencePercent(
                              feedback.confidence
                            )}%`,
                          }}
                        ></div>
                      </div>
                    </div>
                  </div>

                  <button
                    className="delete-btn"
                    onClick={() => deleteFeedback(feedback.id)}
                  >
                    Delete
                  </button>
                </article>
              ))}
            </div>
          )}
        </section>
      </div>
    </div>
  );
}