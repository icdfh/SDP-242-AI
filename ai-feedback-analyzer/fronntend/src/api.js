const API_URL = "http://127.0.0.1:8000";

export async function createFeedback(text) {
  const response = await fetch(`${API_URL}/feedbacks`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      text: text,
    }),
  });

  if (!response.ok) {
    throw new Error("Ошибка при анализе текста");
  }

  return await response.json();
}

export async function getFeedbacks() {
  const response = await fetch(`${API_URL}/feedbacks`);

  if (!response.ok) {
    throw new Error("Ошибка при получении истории");
  }

  return await response.json();
}

export async function deleteFeedback(id) {
  const response = await fetch(`${API_URL}/feedbacks/${id}`, {
    method: "DELETE",
  });

  if (!response.ok) {
    throw new Error("Ошибка при удалении записи");
  }

  return await response.json();
}

export async function getStats() {
  const response = await fetch(`${API_URL}/stats`);

  if (!response.ok) {
    throw new Error("Ошибка при получении статистики");
  }

  return await response.json();
}